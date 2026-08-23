#!/usr/bin/env python3
"""Collect cls_ keys written back into wiki front matter into one TSV.

The wiki pages are the source of truth: classifiers write there, and this script
reads back. Anything a classifier claimed but did not write is therefore absent
here, which is the point.
"""
import csv, glob, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
SRC = os.path.join(ROOT, "wiki", "sources")
OUT = os.path.join(ROOT, "exp", "survey", "notes", "classification.tsv")
FIELDS = ["target","family","phase","access","write","frame","party","unit",
          "tightness","baseline","second","assessed","prov"]
rows, legacy = [], {}
for r in csv.DictReader(open(os.path.join(ROOT,"exp","survey","notes","classification-batch1.tsv"),encoding="utf-8"),delimiter="\t"):
    legacy[r["slug"]] = r
for fn in sorted(glob.glob(os.path.join(SRC, "*.md"))):
    slug = os.path.basename(fn)[:-3]
    t = open(fn, encoding="utf-8").read()
    if not t.startswith("---"): continue
    fm = t[3:t.find("\n---", 3)]
    row = {"slug": slug}
    got = False
    for f in FIELDS:
        m = re.search(r"^cls_%s:\s*(.*)$" % f, fm, re.M)
        if m:
            row[f] = m.group(1).strip().strip('"'); got = True
        else:
            row[f] = ""
    if got:
        row["src"] = "agent"
    elif slug in legacy:
        for f in FIELDS: row[f] = legacy[slug].get(f, "")
        row["prov"] = row.get("prov") or "hand"
        row["src"] = "hand"
    else:
        continue
    rows.append(row)
with open(OUT,"w",newline="",encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=["slug"]+FIELDS+["src"], delimiter="\t")
    w.writeheader(); w.writerows(rows)
a = sum(1 for r in rows if r["src"]=="agent")
print("classified: %d  (%d by agents, %d by hand)  of 181" % (len(rows), a, len(rows)-a))
