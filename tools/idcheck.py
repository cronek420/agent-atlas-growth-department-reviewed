#!/usr/bin/env python3
"""V-3 / V-4: cross-reference integrity + path existence.

Usage:  python idcheck.py <repo_root> <file> [<file> ...]

Exit 0 = all cited IDs resolve and all cited relative paths exist.
Exit 1 = at least one unresolved ID or missing path.

Deliberately reports BOTH directions so a green result is meaningful:
it prints the definition counts it found, so a run that silently found
zero definitions (a broken checker) is visible rather than passing.
"""
import os
import re
import sys

ID_PATTERNS = {
    "D": re.compile(r"\bD-\d{3}[a-z]?\b"),
    "Q": re.compile(r"\bQ-\d{3}\b"),
    "R": re.compile(r"\bR-\d{2}\b"),
    "NG": re.compile(r"\bNG-\d{3}\b"),
    "F": re.compile(r"\bF-\d{2}-\d{2}\b"),
}

# Where each ID family is DEFINED (a row in a register / a heading).
DEF_SOURCES = {
    "D": ("DECISIONS.md", re.compile(r"^\|\s*(D-\d{3}[a-z]?)\s*\|", re.M)),
    "Q": ("OPEN_QUESTIONS.md", re.compile(r"^###\s+(Q-\d{3})\b", re.M)),
    "R": ("RISK_REGISTER.md", re.compile(r"^\|\s*(R-\d{2})\s*\|", re.M)),
    "NG": ("NON_GOALS.md", re.compile(r"\b(NG-\d{3})\b")),
    "F": ("findings.md", re.compile(r"^###\s+(F-\d{2}-\d{2})\b", re.M)),
}

PATH_RE = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|json|py|txt|yml|yaml|zip|example|gitignore))`")

# Bare filenames and placeholders that are DELIBERATELY forward references.
# CLAUDE.md §8 lists files "named by phase prompts but not yet existing" on
# purpose; `phase-XX` / `phase-NN` are template placeholders. Flagging these
# would be a checker fault, not a document defect (findings.md F-01-04).
FUTURE_DELIVERABLES = {
    "SECURITY_POLICY.md", "APPROVAL_POLICY.md", "AUTONOMY_POLICY.md",
    "BUDGET_POLICY.md", "PUBLISHING_POLICY.md", "MESSAGING_POLICY.md",
    "DATA_RETENTION_POLICY.md", "AGENT_PERMISSION_MATRIX.md",
}
PLACEHOLDER_RE = re.compile(r"phase-(XX|NN)|/\*|<")


def load_planned(root):
    """Every artefact MASTER_PLAN.md schedules for a future phase.

    Naming a not-yet-built deliverable is what a plan IS. Treating those as
    missing-path defects produced 92 false positives on the first run of this
    checker. The allowlist is derived from the plan rather than hand-kept so it
    cannot drift out of date.
    """
    path = os.path.join(root, "MASTER_PLAN.md")
    if not os.path.exists(path):
        return set()
    return set(PATH_RE.findall(read(path)))


PLANNED = set()


def is_forward_reference(cited):
    """True if `cited` is a deliberate reference to something not yet created."""
    if cited in FUTURE_DELIVERABLES or cited in PLANNED:
        return True
    if PLACEHOLDER_RE.search(cited):
        return True
    # Per-phase artefacts referred to by bare nickname rather than by their
    # real path under agent_runs/phase-NN/.
    if cited in {"PHASE_GATE_REPORT.md", "REVIEW_REPORT.md", "HANDOFFS.md"}:
        return True
    return False


def resolves(root, cited):
    """Path exists as written, or — for a BARE filename — anywhere in the tree.

    Documents legitimately refer to `USER_INSTRUCTIONS.md` when the file lives
    at `user-guide/USER_INSTRUCTIONS.md`. Phase 01's checker treated that as a
    missing path and produced ~40 false positives (findings.md F-01-04).
    """
    if os.path.exists(os.path.join(root, cited)):
        return True
    if "/" in cited:
        return False
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules"}]
        if cited in filenames:
            return True
    return False


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def main():
    global PLANNED
    root = sys.argv[1]
    targets = sys.argv[2:]
    if not targets:
        print("no target files given")
        return 1

    PLANNED = load_planned(root)
    print(f"  planned future artefacts allowlisted from MASTER_PLAN.md: {len(PLANNED)}")

    defined = {}
    for fam, (src, pat) in DEF_SOURCES.items():
        path = os.path.join(root, src)
        if not os.path.exists(path):
            print(f"CHECKER FAULT: definition source missing: {src}")
            return 2
        defined[fam] = set(pat.findall(read(path)))
        print(f"  definitions found  {fam}: {len(defined[fam])}  (from {src})")
        if not defined[fam]:
            print(f"CHECKER FAULT: zero {fam}- definitions parsed from {src}")
            return 2

    bad_ids, bad_paths = [], []
    for t in targets:
        full = os.path.join(root, t)
        if not os.path.exists(full):
            print(f"MISSING TARGET: {t}")
            bad_paths.append((t, "<target file itself>"))
            continue
        text = read(full)
        for fam, pat in ID_PATTERNS.items():
            for cited in sorted(set(pat.findall(text))):
                if cited not in defined[fam]:
                    bad_ids.append((t, cited))
        for cited in sorted(set(PATH_RE.findall(text))):
            if is_forward_reference(cited):
                continue
            if not resolves(root, cited):
                bad_paths.append((t, cited))

    print()
    if bad_ids:
        print(f"UNRESOLVED IDS ({len(bad_ids)}):")
        for f, i in bad_ids:
            print(f"  {f}: {i}")
    if bad_paths:
        print(f"MISSING PATHS ({len(bad_paths)}):")
        for f, p in bad_paths:
            print(f"  {f}: {p}")
    if not bad_ids and not bad_paths:
        print("OK: every cited ID resolves and every cited path exists")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
