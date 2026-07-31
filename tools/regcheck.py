#!/usr/bin/env python3
"""V-6: registry vocabulary conformance, schema-aware.

Locates Ladder / Class / Relevance / Disposition by HEADER NAME, not by column
index, so it stays correct across tables with different schemas. An earlier
index-based version of this check reported ~80 false non-conformances that were
entirely the checker's fault (the findings.md F-01-04 pattern).

Usage: python regcheck.py <registry.md>
Exit 0 = every status cell holds one declared bare token.
"""
import collections
import re
import sys

VOCAB = {
    "Ladder": {"DISABLED", "SIMULATION", "DRAFT_ONLY", "APPROVAL_REQUIRED",
               "LIMITED_AUTONOMY", "ROUTINE_AUTONOMY", "NOT_PRODUCTION_FACING"},
    "Class": {"IMPLEMENTED", "SCAFFOLDED", "PROPOSED", "PRODUCTION_BLOCKED"},
    "Relevance": {"NEEDED", "POSSIBLE", "IRRELEVANT"},
    "Disposition": {"PERMITTED", "RESTRICTED", "PROHIBITED", "UNRESOLVED"},
}

ESC = "\x00ESCPIPE\x00"


def cells(line):
    """Split a Markdown table row, honouring escaped pipes inside cells."""
    protected = line.replace(chr(92) + "|", ESC)
    parts = protected.split("|")[1:-1]
    return [c.replace(ESC, chr(92) + "|").strip() for c in parts]


def main():
    lines = open(sys.argv[1], encoding="utf-8").read().split("\n")
    hdr = None
    bad = []
    tally = collections.defaultdict(collections.Counter)
    schemas = collections.Counter()
    rows = 0

    for n, line in enumerate(lines, 1):
        if not line.startswith("|"):
            continue
        c = cells(line)
        if not c:
            continue
        if c[0] == "ID":
            hdr = c
            schemas["|".join(c)] += 1
            continue
        if set(c[0]) <= set("-: "):
            continue
        if not re.match(r"^C-[0-9]+$", c[0]) or hdr is None:
            continue
        rows += 1
        if len(c) != len(hdr):
            bad.append((n, c[0], "row has %d cells, header has %d" % (len(c), len(hdr))))
            continue
        for col, vocab in VOCAB.items():
            if col in hdr:
                v = c[hdr.index(col)]
                tally[col][v] += 1
                if v not in vocab:
                    bad.append((n, c[0], "%s=[%s] not a declared bare token" % (col, v)))

    print("distinct table schemas: %d" % len(schemas))
    for s, k in schemas.items():
        print("  x%-2d %s" % (k, s))
    print("\ndata rows parsed: %d" % rows)
    for col in VOCAB:
        print("  %-12s %s" % (col, dict(tally[col])))
    print("\nNON-CONFORMING CELLS: %d" % len(bad))
    for n, i, m in bad:
        print("  line %d %s: %s" % (n, i, m))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
