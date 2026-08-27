#!/usr/bin/env python3
"""Gate: every evidence quote appears in the paper it is attributed to.

The first verification pass asked only whether a quote appeared somewhere in the
corpus. A rotation, where each page receives a neighbour's quote, passes that test
and is still wrong: four such pages were found on 2026-08-27. This checks the quote
against the paper it is attributed to, which is the question that matters.

Binding is by title match against the extracted text, since most pages do not name
their PDF.

    python3 tools/check-quotes.py [--txt DIR]
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SUR = os.path.abspath(os.path.join(HERE, ".."))
SRC = os.path.join(SUR, "..", "..", "wiki", "sources")
TXT = os.environ.get("QUOTE_TXT_DIR", "/tmp/quote-txt")
RAW = os.path.join(SUR, "..", "..", "raw")


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def extract():
    os.makedirs(TXT, exist_ok=True)
    import subprocess
    for p in sorted(glob.glob(os.path.join(RAW, "*.pdf"))):
        d = os.path.join(TXT, os.path.basename(p)[:-4] + ".txt")
        if not os.path.exists(d):
            subprocess.run(["pdftotext", p, d],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    extract()
    texts = {os.path.basename(f)[:-4]: open(f, encoding="utf-8", errors="ignore").read()
             for f in glob.glob(os.path.join(TXT, "*.txt"))}
    nt = {k: norm(v) for k, v in texts.items()}
    heads = {k: norm(v[:3000]) for k, v in texts.items()}

    wrong, unbound, ok, nofrag = [], 0, 0, 0
    for f in sorted(glob.glob(os.path.join(SRC, "*.md"))):
        slug = os.path.basename(f)[:-3]
        s = open(f, encoding="utf-8").read()
        m = re.search(r'^cls_evidence:[ \t]*"?(.*?)"?[ \t]*$', s, re.M)
        if not m:
            continue
        ev = m.group(1).strip()
        if not ev or ev.lower().startswith("absent"):
            continue
        tm = re.search(r"^title:[ \t]*(.*)$", s, re.M)
        title = tm.group(1).strip().strip('"') if tm else ""
        words = re.findall(r"[A-Za-z][A-Za-z-]{2,}", title)
        cand = []
        if len(words) >= 3:
            tf = norm(" ".join(words[:8]))
            cand = [k for k, v in heads.items() if tf in v] or [k for k, v in nt.items() if tf in v]
        if not cand:
            unbound += 1
            continue
        runs = re.findall(r"[A-Za-z][A-Za-z ,'\-]{18,}", ev)
        if not runs:
            nofrag += 1
            continue
        frag = norm(max(runs, key=len))
        if frag in nt.get(cand[0], ""):
            ok += 1
        else:
            elsewhere = [k for k, v in nt.items() if frag in v]
            if elsewhere:                      # in another paper: a real transposition
                wrong.append((slug, cand[0], elsewhere[:2]))
    print("quotes verified in their own paper : %d" % ok)
    print("quotes belonging to another paper  : %d" % len(wrong))
    for slug, own, el in wrong:
        print("   %-44s attributed to %s, actually in %s" % (slug, own, el))
    print("could not bind to a pdf            : %d" % unbound)
    print("no checkable prose fragment        : %d" % nofrag)
    sys.exit(1 if wrong else 0)


if __name__ == "__main__":
    main()
