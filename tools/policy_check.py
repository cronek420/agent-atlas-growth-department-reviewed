#!/usr/bin/env python3
"""Deterministic Phase 03 policy checker.

Implements V-1 .. V-13 from task_plan.md. Run BEFORE independent review
(F-00-04: mechanical checks catch what adversarial review misses, and they are
cheaper to run first). This checker is itself unverified until it has been
shown to fail on cases it should fail on — see policy_check_selftest.py, which
is the actual evidence for this checker's correctness (F-01-04).

Usage:
    python tools/policy_check.py [--registry PATH]

Exit code 0 iff every check passes. Prints one PASS/FAIL line per check plus
detail on failure. Nothing here mutates any file.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REGISTRY = ROOT / "policy" / "action_registry.json"

REQUIRED_DELIVERABLES = [
    "SECURITY_POLICY.md",
    "APPROVAL_POLICY.md",
    "AUTONOMY_POLICY.md",
    "BUDGET_POLICY.md",
    "PUBLISHING_POLICY.md",
    "MESSAGING_POLICY.md",
    "DATA_RETENTION_POLICY.md",
    "AGENT_PERMISSION_MATRIX.md",
]

OUTCOME_ENUM = {"ALLOW", "ALLOW_LOGGED", "APPROVAL_REQUIRED", "OWNER_ONLY", "DENY", "BLOCKED"}

ID_PATTERN = re.compile(
    r"\b("
    r"D-\d{3}[a-z]?"      # D-016, D-016a
    r"|Q-\d{3}"           # Q-008
    r"|R-\d{2}"           # R-19
    r"|NG-\d{3}"          # NG-001
    r"|CNG-\d{3}"         # CNG-004
    r"|F-\d{2}-\d{2}"     # F-01-09
    r")\b"
)

SECRET_PATTERNS = [
    ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("generic private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}")),
    ("OpenAI-style key", re.compile(r"sk-[A-Za-z0-9]{20,}")),
    ("Slack token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("assigned high-entropy secret", re.compile(
        r"(?i)\b(api[_-]?key|secret|token|password|passwd)\b\s*[:=]\s*['\"][A-Za-z0-9/+_\-]{20,}['\"]"
    )),
]
# Deliberately-inert placeholder markers that must NOT trip the scanner:
SAFE_PLACEHOLDER_MARKERS = ("<obtain-from-owner-do-not-commit>", "REDACTED", "EXAMPLE_NOT_REAL")


class Result:
    def __init__(self, check_id, name, passed, detail=""):
        self.check_id = check_id
        self.name = name
        self.passed = passed
        self.detail = detail

    def line(self):
        status = "PASS" if self.passed else "FAIL"
        s = f"[{status}] {self.check_id} - {self.name}"
        if not self.passed and self.detail:
            s += f"\n         {self.detail}"
        return s


def load_registry(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# V-1  Every deliverable exists and is non-empty
# ---------------------------------------------------------------------------
def check_v1_deliverables(root: Path = ROOT):
    missing = []
    empty = []
    for name in REQUIRED_DELIVERABLES:
        p = root / name
        if not p.exists():
            missing.append(name)
        elif p.stat().st_size == 0:
            empty.append(name)
    passed = not missing and not empty
    detail = ""
    if missing:
        detail += f"Missing: {missing}. "
    if empty:
        detail += f"Empty: {empty}."
    return Result("V-1", "All 8 deliverables exist and are non-empty", passed, detail)


# ---------------------------------------------------------------------------
# V-2  action_registry.json parses
# ---------------------------------------------------------------------------
def check_v2_json_parses(registry_path: Path = DEFAULT_REGISTRY):
    try:
        load_registry(registry_path)
        return Result("V-2", "action_registry.json parses as JSON", True)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        return Result("V-2", "action_registry.json parses as JSON", False, str(e))


# ---------------------------------------------------------------------------
# V-3  Every outcome token is in the enum
# ---------------------------------------------------------------------------
def check_v3_outcome_tokens(reg: dict):
    bad = []
    for a in reg.get("actions", []):
        if a.get("outcome") not in OUTCOME_ENUM:
            bad.append((a.get("id", "?"), a.get("outcome")))
    passed = not bad
    return Result("V-3", "Every action outcome is a valid enum token", passed,
                  f"Unknown outcomes: {bad}" if bad else "")


# ---------------------------------------------------------------------------
# V-4  Fail-closed default
# ---------------------------------------------------------------------------
def evaluate_action(reg: dict, role: str, verb: str, resource: str):
    """Deterministic evaluator: returns the outcome for (role, verb, resource),
    or the registry's default_outcome if no row matches. This is the reference
    implementation the checker validates — the same logic any enforcement code
    should use."""
    matches = [
        a for a in reg.get("actions", [])
        if role in a.get("roles", []) and a.get("verb") == verb and a.get("resource") == resource
    ]
    if not matches:
        return reg.get("default_outcome", "DENY")
    order = reg.get("strictness_order", [])
    matches.sort(key=lambda a: order.index(a["outcome"]) if a["outcome"] in order else len(order))
    return matches[0]["outcome"]


def check_v4_fail_closed(reg: dict):
    # An action matching no row at all (nonsense verb/resource) must resolve to DENY.
    outcome = evaluate_action(reg, "RUNTIME_AGENT", "TIME_TRAVEL", "NONEXISTENT_RESOURCE")
    passed = outcome == "DENY"
    return Result("V-4", "Unmatched action resolves to fail-closed DENY", passed,
                  f"Got '{outcome}' instead of 'DENY'" if not passed else "")


# ---------------------------------------------------------------------------
# V-5  No contradictory rows
# ---------------------------------------------------------------------------
def check_v5_no_contradictions(reg: dict):
    seen = {}
    conflicts = []
    for a in reg.get("actions", []):
        for role in a.get("roles", []):
            key = (role, a.get("verb"), a.get("resource"), a.get("description"))
            prior = seen.get(key)
            if prior is not None and prior != a.get("outcome"):
                conflicts.append((key, prior, a.get("outcome"), a.get("id")))
            seen[key] = a.get("outcome")
    passed = not conflicts
    return Result("V-5", "No two rows assign different outcomes to the same statement",
                  passed, f"Conflicts: {conflicts}" if conflicts else "")


# ---------------------------------------------------------------------------
# V-6  All 9 gated categories covered
# ---------------------------------------------------------------------------
def check_v6_gated_coverage(reg: dict):
    strictness = reg.get("strictness_order", [])
    # "APPROVAL_REQUIRED or stricter" = index <= index(APPROVAL_REQUIRED)
    threshold = strictness.index("APPROVAL_REQUIRED") if "APPROVAL_REQUIRED" in strictness else 999
    covered = set()
    for a in reg.get("actions", []):
        outcome = a.get("outcome")
        if outcome in strictness and strictness.index(outcome) <= threshold:
            for gc in a.get("gated_categories", []):
                covered.add(gc)
    all_gc = {gc["id"] for gc in reg.get("gated_categories", [])}
    uncovered = all_gc - covered
    passed = not uncovered
    return Result("V-6", "All 9 gated categories referenced at APPROVAL_REQUIRED or stricter",
                  passed, f"Uncovered: {sorted(uncovered)}" if uncovered else "")


# ---------------------------------------------------------------------------
# V-7  Every basis ID resolves against the real registers
# ---------------------------------------------------------------------------
def load_real_ids(root: Path = ROOT):
    ids = {"D": set(), "Q": set(), "R": set(), "NG": set(), "CNG": set(), "F": set()}

    def scan(path: Path, target_set: set, pattern: re.Pattern):
        if not path.exists():
            return
        text = path.read_text(encoding="utf-8", errors="ignore")
        for m in pattern.finditer(text):
            target_set.add(m.group(0))

    scan(root / "DECISIONS.md", ids["D"], re.compile(r"\bD-\d{3}[a-z]?\b"))
    scan(root / "OPEN_QUESTIONS.md", ids["Q"], re.compile(r"\bQ-\d{3}\b"))
    scan(root / "RISK_REGISTER.md", ids["R"], re.compile(r"\bR-\d{2}\b"))
    scan(root / "NON_GOALS.md", ids["NG"], re.compile(r"\bNG-\d{3}\b"))
    scan(root / "NON_GOALS.md", ids["CNG"], re.compile(r"\bCNG-\d{3}\b"))
    scan(root / "findings.md", ids["F"], re.compile(r"\bF-\d{2}-\d{2}\b"))
    return ids


def extract_ids(text: str):
    return set(m.group(0) for m in ID_PATTERN.finditer(text))


def check_v7_basis_ids_resolve(root: Path = ROOT, registry_path: Path = DEFAULT_REGISTRY,
                                extra_files=None):
    real = load_real_ids(root)

    def resolves(identifier: str) -> bool:
        if identifier.startswith("CNG-"):
            return identifier in real["CNG"]
        if identifier.startswith("NG-"):
            return identifier in real["NG"]
        if identifier.startswith("D-"):
            return identifier in real["D"]
        if identifier.startswith("Q-"):
            return identifier in real["Q"]
        if identifier.startswith("R-"):
            return identifier in real["R"]
        if identifier.startswith("F-"):
            return identifier in real["F"]
        return False

    unresolved = {}

    # Scan the registry's own basis arrays.
    reg = load_registry(registry_path)
    cited = set()
    for a in reg.get("actions", []):
        cited.update(a.get("basis", []))
    for r in reg.get("roles", []):
        cited.update(r.get("basis", []))
    for gc in reg.get("gated_categories", []):
        cited.update(gc.get("basis", []))
    for cid in cited:
        m = ID_PATTERN.fullmatch(cid)
        if m and not resolves(cid):
            unresolved.setdefault("action_registry.json", []).append(cid)

    # Scan the policy markdown deliverables (and any extra files passed in, e.g. for fixtures).
    files = extra_files if extra_files is not None else [
        root / name for name in REQUIRED_DELIVERABLES if name != "AGENT_PERMISSION_MATRIX.md"
    ]
    for path in files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for identifier in extract_ids(text):
            if not resolves(identifier):
                unresolved.setdefault(path.name, []).append(identifier)

    passed = not unresolved
    return Result("V-7", "Every cited D-/Q-/R-/NG-/CNG-/F- identifier resolves against the real registers",
                  passed, f"Unresolved: {unresolved}" if unresolved else "")


# ---------------------------------------------------------------------------
# V-8  Every referenced policy file exists
# ---------------------------------------------------------------------------
def check_v8_policy_files_exist(reg: dict, root: Path = ROOT):
    dangling = set()
    for a in reg.get("actions", []):
        pf = a.get("policy")
        if pf and not (root / pf).exists():
            dangling.add((a.get("id"), pf))
    passed = not dangling
    return Result("V-8", "Every action's referenced policy file exists", passed,
                  f"Dangling: {sorted(dangling)}" if dangling else "")


# ---------------------------------------------------------------------------
# V-9  Approval state machine integrity
# ---------------------------------------------------------------------------
def check_v9_approval_machine(reg: dict):
    sm = reg["state_machines"]["approval"]
    states = set(sm["states"])
    terminal = set(sm["terminal"])
    transitions = sm["transitions"]
    problems = []

    # Reachability from initial state.
    graph = {}
    for t in transitions:
        graph.setdefault(t["from"], []).append(t["to"])
    seen = {sm["initial"]}
    stack = [sm["initial"]]
    while stack:
        cur = stack.pop()
        for nxt in graph.get(cur, []):
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    unreachable = states - seen
    if unreachable:
        problems.append(f"Unreachable states: {sorted(unreachable)}")

    # Terminal states have no outgoing transitions.
    for t in transitions:
        if t["from"] in terminal:
            problems.append(f"Terminal state '{t['from']}' has outgoing transition to '{t['to']}'")

    # Only PROJECT_OWNER may transition into APPROVED.
    for t in transitions:
        if t["to"] == "APPROVED" and t["actor"] != "PROJECT_OWNER":
            problems.append(f"Non-owner actor '{t['actor']}' can transition into APPROVED (from {t['from']})")

    # Exactly one edge type reaches APPROVED (the invariant "only PENDING_APPROVAL -> APPROVED").
    approved_sources = {t["from"] for t in transitions if t["to"] == "APPROVED"}
    if approved_sources != {"PENDING_APPROVAL"}:
        problems.append(f"APPROVED is reachable from unexpected states: {sorted(approved_sources)}")

    passed = not problems
    return Result("V-9", "Approval state machine integrity (reachability, terminal states, owner-only APPROVED)",
                  passed, "; ".join(problems) if problems else "")


# ---------------------------------------------------------------------------
# V-10  Ladder has no skip edges
# ---------------------------------------------------------------------------
def check_v10_no_skip_edges(reg: dict):
    ladder = reg["state_machines"]["autonomy_ladder"]
    states = ladder["states"]
    idx = {s: i for i, s in enumerate(states)}
    bad = []
    for t in ladder["transitions"]:
        if t["trigger"] == "promote":
            if idx.get(t["to"], -1) != idx.get(t["from"], -2) + 1:
                bad.append(t)
    passed = not bad
    return Result("V-10", "Every promotion edge advances exactly one ladder stage", passed,
                  f"Skip edges: {bad}" if bad else "")


# ---------------------------------------------------------------------------
# V-11  Emergency stop always one hop from every non-DISABLED state
# ---------------------------------------------------------------------------
def check_v11_estop_reachable(reg: dict):
    ladder = reg["state_machines"]["autonomy_ladder"]
    states = ladder["states"]
    has_estop = {t["from"] for t in ladder["transitions"] if t["to"] == "DISABLED"}
    missing = [s for s in states if s != "DISABLED" and s not in has_estop]
    passed = not missing
    return Result("V-11", "Every non-DISABLED autonomy stage has a one-hop edge to DISABLED", passed,
                  f"Missing e-stop edge from: {missing}" if missing else "")


# ---------------------------------------------------------------------------
# V-12  Generated matrix matches registry
# ---------------------------------------------------------------------------
def check_v12_matrix_matches_registry(root: Path = ROOT):
    script = root / "tools" / "render_permission_matrix.py"
    try:
        proc = subprocess.run(
            [sys.executable, str(script), "--check"],
            cwd=str(root), capture_output=True, text=True, timeout=30,
        )
        passed = proc.returncode == 0
        return Result("V-12", "AGENT_PERMISSION_MATRIX.md matches action_registry.json (no drift)",
                      passed, proc.stdout.strip() + proc.stderr.strip() if not passed else "")
    except Exception as e:
        return Result("V-12", "AGENT_PERMISSION_MATRIX.md matches action_registry.json (no drift)",
                      False, str(e))


# ---------------------------------------------------------------------------
# V-13  No secrets in any Phase 03 output
# ---------------------------------------------------------------------------
def check_v13_no_secrets(root: Path = ROOT, files=None):
    targets = files if files is not None else (
        [root / name for name in REQUIRED_DELIVERABLES] + [root / "policy" / "action_registry.json"]
    )
    hits = []
    for path in targets:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for line_no, line in enumerate(text.splitlines(), 1):
            if any(marker in line for marker in SAFE_PLACEHOLDER_MARKERS):
                continue
            for label, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    hits.append((path.name, line_no, label))
    passed = not hits
    return Result("V-13", "No secret-shaped strings in any Phase 03 deliverable", passed,
                  f"Hits: {hits}" if hits else "")


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------
def run_all(root: Path = ROOT, registry_path: Path = DEFAULT_REGISTRY):
    results = [check_v1_deliverables(root)]

    v2 = check_v2_json_parses(registry_path)
    results.append(v2)
    if not v2.passed:
        # Can't run registry-dependent checks against unparseable JSON.
        return results

    reg = load_registry(registry_path)
    results.append(check_v3_outcome_tokens(reg))
    results.append(check_v4_fail_closed(reg))
    results.append(check_v5_no_contradictions(reg))
    results.append(check_v6_gated_coverage(reg))
    results.append(check_v7_basis_ids_resolve(root, registry_path))
    results.append(check_v8_policy_files_exist(reg, root))
    results.append(check_v9_approval_machine(reg))
    results.append(check_v10_no_skip_edges(reg))
    results.append(check_v11_estop_reachable(reg))
    results.append(check_v12_matrix_matches_registry(root))
    results.append(check_v13_no_secrets(root))
    return results


def main():
    args = sys.argv[1:]
    registry_path = DEFAULT_REGISTRY
    if "--registry" in args:
        registry_path = Path(args[args.index("--registry") + 1])

    results = run_all(registry_path=registry_path)
    for r in results:
        print(r.line())
    n_pass = sum(1 for r in results if r.passed)
    print(f"\n{n_pass}/{len(results)} checks passed.")
    sys.exit(0 if n_pass == len(results) else 1)


if __name__ == "__main__":
    main()
