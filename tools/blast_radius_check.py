#!/usr/bin/env python3
"""CSK-01 — blast-radius-check.

Enumerates files from PRIOR phases whose factual claims the CURRENT phase's work
may have made untrue, before the gate report is drafted. Full contract:
CUSTOM_SKILL_BACKLOG.md § "CSK-01 — blast-radius-check". Assigned to Phase 03 to
build (CURRENT_PHASE.md, real Phase 02 record); first needed at Phase 03,
the first phase after F-01-09 was written.

D-003 SPLIT: this script performs the DETERMINISTIC half only — enumeration of
candidate claims via pattern matching against changed_files. It does NOT judge
whether a candidate is actually false (that is LLM/phase-owner judgement) and it
NEVER sets verdict based on that judgement — verdict is a pure function of
(candidate count, unreadable count), per the contract's postcondition.
The phase owner records the disposition of every candidate, including rejections,
outside this script (in findings.md / the gate report).

Usage:
    python tools/blast_radius_check.py --phase-id 03 --baseline-ref <ref> [--changed-files f1 f2 ...] [--clock ISO8601]

If --changed-files is omitted, changed files are derived from
`git diff --name-only <baseline-ref>...HEAD` plus `git status --porcelain`
(uncommitted work), since this project's phases are frequently uncommitted
mid-run. Prints the JSON contract to stdout. Exit 0 always unless a hard-fail
precondition is violated (unresolvable ref, path escapes project root).
"""
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FIXED_INPUTS = [
    "RISK_REGISTER.md",
    "OPEN_QUESTIONS.md",
    "DECISIONS.md",
    "CURRENT_PHASE.md",
    "MASTER_PLAN.md",
    "README.md",
    "CLAUDE.md",
    "CAPABILITY_REGISTRY.md",
]

# Negation/staleness-shaped phrases: a line containing one of these, near a
# reference to something this phase changed, is a candidate for having gone stale.
NEGATION_PATTERNS = [
    r"does not exist", r"do not exist", r"never existed",
    r"not yet exist", r"not been created", r"not existing", r"still not",
    r"never (?:started|executed|run|happened|occurred)",
    r"not (?:yet )?started", r"NOT STARTED",
    r"has not been", r"have not been",
    r"no such", r"not present", r"not been performed",
    r"awaiting the owner", r"nothing has been built",
]
NEGATION_RE = re.compile("|".join(NEGATION_PATTERNS), re.IGNORECASE)

FORBIDDEN_PREFIX = "Rough-Draft-Builders-Club"


def resolve_safe(rel_path: str) -> Path:
    p = (ROOT / rel_path).resolve()
    try:
        p.relative_to(ROOT.resolve())
    except ValueError:
        raise SystemExit(f"HARD FAIL: path resolves outside project root: {rel_path}")
    if FORBIDDEN_PREFIX in str(p):
        raise SystemExit(f"HARD FAIL: path touches the protected RDBC boundary: {rel_path}")
    return p


def git(*args, check=True):
    proc = subprocess.run(["git", *args], cwd=str(ROOT), capture_output=True, text=True)
    if check and proc.returncode != 0:
        raise SystemExit(f"HARD FAIL: git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout


def derive_changed_files(baseline_ref: str):
    # Confirm the ref resolves before using it (contract: unresolvable ref -> hard fail, no verdict).
    proc = subprocess.run(["git", "rev-parse", "--verify", baseline_ref],
                           cwd=str(ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(f"HARD FAIL: unresolvable git ref '{baseline_ref}': {proc.stderr.strip()}")

    committed = git("diff", "--name-only", f"{baseline_ref}...HEAD", check=False).splitlines()
    status = git("status", "--porcelain", check=False).splitlines()
    uncommitted = [line[3:].strip() for line in status if line.strip()]
    changed = sorted(set(f for f in (committed + uncommitted) if f))
    return changed


def find_candidates(fixed_path_rel: str, text: str, changed_files: list):
    candidates = []
    lines = text.splitlines()
    changed_basenames = {Path(f).name: f for f in changed_files}
    for line_no, line in enumerate(lines, 1):
        if not NEGATION_RE.search(line):
            continue
        for basename, changed_path in changed_basenames.items():
            if basename == "":
                continue
            if basename in line:
                confidence = "HIGH"
                why = (f"Line matches a staleness-shaped phrase and names '{basename}', "
                       f"which this phase's own changed-files list ({changed_path}) touched. "
                       f"Confirm this claim about '{basename}' still holds after this phase's work.")
                candidates.append({
                    "file": fixed_path_rel,
                    "line": line_no,
                    "quoted_claim": line.strip()[:300],
                    "why_possibly_false": why,
                    "confidence": confidence,
                })
    return candidates


def run(phase_id: str, baseline_ref: str, changed_files, clock: str):
    checked = []
    unreadable = []
    all_candidates = []

    for rel in FIXED_INPUTS:
        path = resolve_safe(rel)
        if not path.exists() or not path.is_file():
            unreadable.append(rel)
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="strict")
        except Exception as e:
            unreadable.append(rel)
            continue
        checked.append(rel)
        all_candidates.extend(find_candidates(rel, text, changed_files))

    verdict = "CLEAN" if (len(all_candidates) == 0 and len(unreadable) == 0) else "REVIEW_REQUIRED"

    result = {
        "phase_id": phase_id,
        "baseline_ref": baseline_ref,
        "clock": clock,
        "changed_files": changed_files,
        "candidates": all_candidates,
        "checked": checked,
        "unreadable": unreadable,
        "verdict": verdict,
    }
    # Postcondition self-check (defensive — should be true by construction).
    assert set(checked) | set(unreadable) == set(FIXED_INPUTS), "every fixed input must appear in checked xor unreadable"
    if verdict == "CLEAN":
        assert not unreadable
    return result


def main():
    args = sys.argv[1:]

    def get_opt(name, default=None):
        if name in args:
            i = args.index(name)
            return args[i + 1]
        return default

    phase_id = get_opt("--phase-id", "03")
    baseline_ref = get_opt("--baseline-ref")
    if baseline_ref is None:
        print("HARD FAIL: --baseline-ref is required (e.g. the commit this phase's work branched from).")
        sys.exit(1)
    clock = get_opt("--clock", datetime.now(timezone.utc).isoformat())

    if "--changed-files" in args:
        i = args.index("--changed-files")
        changed_files = []
        j = i + 1
        while j < len(args) and not args[j].startswith("--"):
            changed_files.append(args[j])
            j += 1
    else:
        changed_files = derive_changed_files(baseline_ref)

    result = run(phase_id, baseline_ref, changed_files, clock)
    print(json.dumps(result, indent=2))
    # No file is modified; no exception means postconditions held.


if __name__ == "__main__":
    main()
