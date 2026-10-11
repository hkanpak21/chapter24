#!/usr/bin/env python3
"""Report the citation tier and age of every \\cite in a section.

Implements standing rules S1 and S2 from
notes/2026-08-22-note-corrections-from-halil.md, so that citation weight is
checked rather than remembered.

  tier 1  peer-reviewed, top venue for the field
  tier 2  peer-reviewed, other venue
  tier 3  preprint, or venue this corpus could not confirm from the PDF

Usage:  python3 tools/cite-weight.py sections/01-introduction.tex [...]
        python3 tools/cite-weight.py --all
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
BIB = os.path.join(ROOT, "paper", "refs.bib")
THIS_YEAR = 2026
STALE_AFTER = 2          # a verdict resting on something older than this is flagged

TIER1 = [
    r"CRYPTO", r"EUROCRYPT", r"ASIACRYPT", r"\bTCC\b", r"IEEE S&P",
    r"USENIX Security", r"ACM CCS", r"\bNDSS\b", r"\bSTOC\b", r"\bFOCS\b",
    r"\bSODA\b", r"\bCOLT\b", r"NeurIPS", r"\bICML\b", r"\bICLR\b",
    r"\bJACM\b", r"Journal of Cryptology", r"\bITCS\b", r"\bJMLR\b",
]


def parse_bib():
    entries = {}
    text = open(BIB, encoding="utf-8").read()
    for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", text, re.S):
        kind, key, body = m.group(1), m.group(2).strip(), m.group(3)
        def field(name):
            f = re.search(name + r"\s*=\s*\{(.*?)\},?\s*(?:\n|$)", body, re.S)
            return f.group(1).strip() if f else ""
        entries[key] = dict(
            kind=kind, year=field("year"), booktitle=field("booktitle"),
            journal=field("journal"), howpublished=field("howpublished"),
            annote=field("annote"), title=field("title"),
        )
    return entries


def tier(e):
    if "venue-unconfirmed" in e["annote"] or e["kind"] == "misc":
        return 3
    venue = (e["booktitle"] or e["journal"]).replace("\\", "")
    if not venue or re.search(r"unconfirmed", venue, re.I):
        return 3
    # A workshop at a top venue is not the top venue.
    if re.search(r"workshop", venue, re.I):
        return 2
    for pat in TIER1:
        if re.search(pat, venue, re.I):
            return 1
    return 2


def main():
    args = sys.argv[1:]
    if args == ["--all"]:
        args = sorted(
            os.path.join(ROOT, "paper", "sections", f)
            for f in os.listdir(os.path.join(ROOT, "paper", "sections")) if f.endswith(".tex"))
    bib = parse_bib()
    worst = 0
    for path in args:
        text = open(path, encoding="utf-8").read()
        keys = []
        for m in re.finditer(r"\\cite\{([^}]*)\}", text):
            for k in m.group(1).split(","):
                k = k.strip()
                if k and k not in keys:
                    keys.append(k)
        if not keys:
            continue
        print("\n%s  (%d distinct citations)" % (os.path.relpath(path, ROOT), len(keys)))
        rows = []
        for k in keys:
            e = bib.get(k)
            if not e:
                rows.append((9, k, "?", "NOT IN refs.bib", ""))
                continue
            t = tier(e)
            venue = e["booktitle"] or e["journal"] or e["howpublished"] or "-"
            age = ""
            try:
                if THIS_YEAR - int(e["year"]) > STALE_AFTER:
                    age = "  [%d yr]" % (THIS_YEAR - int(e["year"]))
            except ValueError:
                pass
            rows.append((t, k, e["year"], venue[:44], age))
        for t, k, y, v, age in sorted(rows):
            mark = {1: "  ", 2: "  ", 3: "->"}.get(t, "??")
            print("  %s tier %s  %-14s %s  %-44s%s" % (mark, t, k, y, v, age))
            worst = max(worst, t if t != 9 else 3)
        n3 = sum(1 for r in rows if r[0] == 3)
        if n3:
            print("  %d tier-3 citation(s). S1: none may carry an argument alone "
                  "where a higher tier says the same thing." % n3)
    return 0


if __name__ == "__main__":
    sys.exit(main())
