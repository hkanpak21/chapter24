#!/usr/bin/env python3
"""Build the classification skeleton for the survey's two tables.

Fills only what can be read directly off wiki front matter, and leaves every other
cell blank for a human pass. It deliberately does NOT guess from tags: tags were
applied for retrieval, not classification, and a guessed cell presented as a
classification is the failure this survey exists to document.

Writes a TSV to notes/classification.tsv and prints a coverage report saying
exactly how many cells are filled, by what, and how many remain.
"""
import csv
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
SRC = os.path.join(ROOT, "wiki", "sources")
BIB = os.path.join(HERE, "..", "..", "paper", "refs.bib")
OUT = os.path.join(HERE, "..", "..", "lab", "results", "corpus-classification", "classification.tsv")

T1 = ["target", "family", "phase", "access", "write", "frame"]
T2 = ["party", "unit", "tightness", "baseline", "assessed", "quantifier", "antecedent"]
COLS = ["slug", "key", "year"] + T1 + T2 + ["prov"]


def front_matter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    block = text[3:end] if end != -1 else ""
    out, key, buf = {}, None, []
    for line in block.splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            if key:
                out[key] = " ".join(buf).strip()
            key, buf = m.group(1), [m.group(2)]
        elif key:
            buf.append(line.strip())
    if key:
        out[key] = " ".join(buf).strip()
    return out


def keys_by_slug():
    text = open(BIB, encoding="utf-8").read()
    out = {}
    for m in re.finditer(r"@\w+\{([^,]+),(.*?)\n\}", text, re.S):
        s = re.search(r"wiki: ([a-z0-9-]+)", m.group(2))
        if s:
            out[s.group(1)] = m.group(1).strip()
    return out


def main():
    kb = keys_by_slug()
    rows = []
    filled = {c: 0 for c in T1 + T2}
    for fn in sorted(glob.glob(os.path.join(SRC, "*.md"))):
        text = open(fn, encoding="utf-8").read()
        fm = front_matter(text)
        if fm.get("type", "").strip() != "source":
            continue
        slug = os.path.basename(fn)[:-3]
        row = {c: "" for c in COLS}
        row["slug"] = slug
        row["key"] = kb.get(slug, "?")
        row["year"] = fm.get("year", "").strip('"')

        # quantifier: present on all 181 pages, a controlled value already
        q = fm.get("claim_quantifier", "").strip('"').strip().lower()
        if q in ("universal", "existential", "conditional", "empirical"):
            row["quantifier"] = q
            filled["quantifier"] += 1

        # antecedent: the front matter distinguishes "none" from a stated hypothesis
        a = fm.get("antecedent", "").strip('"').strip()
        if a:
            row["antecedent"] = "none" if a.lower().rstrip(".") in ("none", "n/a") else "stated"
            filled["antecedent"] += 1

        row["prov"] = "F:quantifier,antecedent"
        rows.append(row)

    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    n = len(rows)
    total_cells = n * len(T1 + T2)
    done = sum(filled.values())
    print("rows: %d" % n)
    print("cells: %d total, %d filled from front matter, %d need a reading pass"
          % (total_cells, done, total_cells - done))
    print()
    for c in T1 + T2:
        bar = "filled from front matter" if filled[c] else "NEEDS READING"
        print("  %-11s %4d/%d  %s" % (c, filled[c], n, bar))
    print("\nwrote %s" % os.path.relpath(OUT, ROOT))


if __name__ == "__main__":
    main()
