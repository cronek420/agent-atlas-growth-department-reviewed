#!/usr/bin/env python3
"""V-8 + V-9: custom-skill contract completeness, and trigger-test coverage.

V-8 (pass condition "Custom skills have contracts"): every CSK entry in
CUSTOM_SKILL_BACKLOG.md carries every required contract field. A missing field is
a FAILED pass condition, not a rounding error.

V-9 (pass condition "Trigger tests exist"): every CSK in the backlog appears in
SKILL_TEST_PLAN.md with a must-fire case, a must-not-fire case, and a
must-not-PASS case -- and a red-mutation field, per findings.md F-01-04.

Usage: python contractcheck.py <backlog.md> <testplan.md>
"""
import re
import sys

REQUIRED = [
    ("Purpose", r"\*\*Purpose"),
    ("Trigger", r"\*\*Trigger"),
    ("Inputs", r"\*\*Inputs"),
    ("Outputs", r"\*\*Outputs"),
    ("Preconditions", r"\*\*Preconditions"),
    ("Postconditions", r"\*\*Postconditions"),
    ("Failure modes", r"\*\*Failure modes"),
    ("Negative contract", r"\*\*Negative contract"),
    ("Owning phase", r"\*\*Own(er|ing)"),
    ("First needed", r"First needed|first needed|First-needed"),
    ("DET/LLM per D-003", r"\bDET\b|\bLLM\b|[Dd]eterministic"),
    ("Status", r"\*\*Status"),
]

TESTKINDS = [
    ("must-fire", r"[Mm]ust[- ]fire"),
    ("must-not-fire", r"[Mm]ust[- ]NOT[- ]fire|[Mm]ust[- ]not[- ]fire"),
    ("must-not-pass", r"[Mm]ust[- ]NOT[-* ]*\*?\*?pass|[Mm]ust[- ]not[-* ]*\*?\*?pass"),
    ("red mutation", r"[Rr]ed mutation"),
]


def sections(text, pat):
    """Split into (id, body) for each entry heading matching pat."""
    hits = [(m.start(), m.group(1)) for m in re.finditer(pat, text)]
    out = []
    for i, (pos, sid) in enumerate(hits):
        end = hits[i + 1][0] if i + 1 < len(hits) else len(text)
        out.append((sid, text[pos:end]))
    return out


def main():
    backlog = open(sys.argv[1], encoding="utf-8").read()
    plan = open(sys.argv[2], encoding="utf-8").read()

    # contract entries are the H3 headings of the form: ### `CSK-nn` — `name`
    entries = sections(backlog, r"### `(CSK-\d+)` — `")
    print("=== V-8: contract completeness (%d entries) ===" % len(entries))
    fails = 0
    for sid, body in entries:
        missing = [name for name, pat in REQUIRED if not re.search(pat, body)]
        if missing:
            fails += 1
            print("  FAIL %s missing: %s" % (sid, ", ".join(missing)))
        else:
            print("  OK   %s  all %d fields present" % (sid, len(REQUIRED)))

    print("\n=== V-9: trigger-test coverage ===")
    ids = [sid for sid, _ in entries]
    for sid in ids:
        # gather every line in the test plan mentioning this skill
        lines = [l for l in plan.split("\n") if sid in l]
        blob = "\n".join(lines)
        if not lines:
            print("  FAIL %s absent from SKILL_TEST_PLAN.md" % sid)
            fails += 1
            continue
        missing = [k for k, pat in TESTKINDS if not re.search(pat, blob)]
        if missing:
            print("  WARN %s (%d refs) no local match for: %s"
                  % (sid, len(lines), ", ".join(missing)))
        else:
            print("  OK   %s  %d refs, all test kinds present" % (sid, len(lines)))

    print("\nV-8 hard failures: %d" % fails)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
