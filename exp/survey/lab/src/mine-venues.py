#!/usr/bin/env python3
"""Recover unconfirmed venues by reading how other papers in the corpus cite them.

The arXiv copy of a paper usually states no venue, which is why 90 of the 181
wiki source pages carry venue-unconfirmed. But a paper's venue is written down
in the bibliography of every later paper that cites it, and this corpus holds
186 of those. This script mines them.

A venue is reported as agreed when two or more distinct citing papers name it.
Output is a markdown table for a human to accept or reject; nothing is written
back to the wiki automatically.
"""
import os
import re
import subprocess
import sys
import glob
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
SRC = os.path.join(ROOT, "wiki", "sources")
RAW = os.path.join(ROOT, "raw")
TXT = os.environ.get("VENUE_TXT_DIR", "/tmp/venue-txt")
OUT = os.path.join(ROOT, "exp", "survey", "lib", "reports", "archive", "2026-08-22-halil-note-venue-mining.md")

VENUES = [
    r"CRYPTO", r"EUROCRYPT", r"ASIACRYPT", r"\bTCC\b", r"\bPKC\b", r"\bCHES\b",
    r"IEEE S&P", r"S&P", r"Oakland", r"USENIX Security", r"\bCCS\b", r"\bNDSS\b",
    r"EuroS&P", r"\bSaTML\b", r"PoPETs", r"Privacy Enhancing Technologies",
    r"NeurIPS", r"Neural Information Processing Systems", r"\bICML\b", r"\bICLR\b",
    r"\bCOLT\b", r"\bAISTATS\b", r"\bUAI\b", r"\bAAAI\b", r"\bIJCAI\b", r"\bCVPR\b",
    r"\bICCV\b", r"\bECCV\b", r"\bACL\b", r"\bEMNLP\b", r"\bNAACL\b", r"\bCOLM\b",
    r"\bSTOC\b", r"\bFOCS\b", r"\bSODA\b", r"\bITCS\b", r"\bICALP\b", r"\bCCC\b",
    r"\bJACM\b", r"\bJMLR\b", r"\bSICOMP\b", r"Journal of Cryptology",
    r"\bALT\b", r"\bCSF\b", r"\bPODS\b", r"\bTIFS\b", r"\bTDSC\b",
    r"arXiv preprint",
]


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def front_matter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    block = text[3:end] if end != -1 else ""
    out = {}
    for line in block.splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"')
    return out


def extract_all():
    os.makedirs(TXT, exist_ok=True)
    pdfs = sorted(glob.glob(os.path.join(RAW, "*.pdf")))
    for p in pdfs:
        stem = os.path.basename(p)[:-4]
        dest = os.path.join(TXT, stem + ".txt")
        if not os.path.exists(dest):
            subprocess.run(["pdftotext", p, dest],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return sorted(glob.glob(os.path.join(TXT, "*.txt")))


def main():
    files = extract_all()
    corpus = {}
    for f in files:
        corpus[os.path.basename(f)[:-4]] = open(f, encoding="utf-8", errors="ignore").read()
    sys.stderr.write("corpus: %d extracted documents\n" % len(corpus))

    todo = []
    for fn in sorted(glob.glob(os.path.join(SRC, "*.md"))):
        text = open(fn, encoding="utf-8").read()
        fm = front_matter(text)
        if fm.get("type") != "source":
            continue
        if "unconfirmed" not in fm.get("venue", "").lower():
            continue
        title = fm.get("title", "").strip('"')
        if len(title) < 18:
            continue
        todo.append((os.path.basename(fn)[:-3], title, fm.get("year", "")))
    sys.stderr.write("unconfirmed venues to mine: %d\n" % len(todo))

    rows = []
    for i, (slug, title, year) in enumerate(todo):
        # a distinctive middle fragment of the title, to survive line breaks
        words = re.findall(r"[A-Za-z][A-Za-z-]{2,}", title)
        frag = " ".join(words[:7]) if len(words) >= 5 else title
        nf = norm(frag)
        votes = Counter()
        evidence = defaultdict(list)
        for name, txt in corpus.items():
            if nf not in norm(txt):
                continue
            for m in re.finditer(re.escape(words[0]), txt):
                seg = re.sub(r"\s+", " ", txt[m.start():m.start() + 340])
                if nf not in norm(seg):
                    continue
                tail = seg[len(frag):]
                for pat in VENUES:
                    if re.search(pat, tail, re.I):
                        v = re.sub(r"\\b|\\", "", pat)
                        votes[v] += 1
                        if len(evidence[v]) < 2:
                            evidence[v].append("[%s] %s" % (name, tail[:110].strip()))
                break
        agreed = [(v, n) for v, n in votes.most_common() if n >= 2]
        rows.append((slug, title, year, agreed, votes, evidence))
        sys.stderr.write("  %3d/%d %-46s %s\n" % (
            i + 1, len(todo), slug[:46],
            agreed[0][0] if agreed else ("weak: " + votes.most_common(1)[0][0] if votes else "-")))

    agreed_rows = [r for r in rows if r[3]]
    weak_rows = [r for r in rows if not r[3] and r[4]]
    none_rows = [r for r in rows if not r[4]]

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("# Venue mining, run 2026-08-22\n\n")
        fh.write("Recovers venues for the wiki pages marked `venue-unconfirmed`, by reading how the\n"
                 "other papers in this corpus cite them. No web access. Produced by\n"
                 "`tools/mine-venues.py`. **Nothing here is written back to the wiki automatically.**\n"
                 "Each row needs a human to accept it, and the evidence column is there to make that\n"
                 "a two-second decision.\n\n")
        fh.write("| | count |\n| --- | --- |\n")
        fh.write("| Unconfirmed venues mined | %d |\n" % len(rows))
        fh.write("| Two or more citers agree | %d |\n" % len(agreed_rows))
        fh.write("| One citer only | %d |\n" % len(weak_rows))
        fh.write("| No citer in the corpus | %d |\n\n" % len(none_rows))

        fh.write("## Agreed, two or more independent citing papers\n\n")
        fh.write("| Wiki page | Year | Venue | Votes | Evidence |\n| --- | --- | --- | --- | --- |\n")
        for slug, title, year, agreed, votes, ev in agreed_rows:
            v, n = agreed[0]
            e = ev[v][0].replace("|", "/")[:96] if ev[v] else ""
            fh.write("| `%s` | %s | **%s** | %d | %s |\n" % (slug, year, v, n, e))

        fh.write("\n## One citer only, treat as a lead\n\n")
        fh.write("| Wiki page | Year | Candidate | Evidence |\n| --- | --- | --- | --- |\n")
        for slug, title, year, _, votes, ev in weak_rows:
            v = votes.most_common(1)[0][0]
            e = ev[v][0].replace("|", "/")[:96] if ev[v] else ""
            fh.write("| `%s` | %s | %s | %s |\n" % (slug, year, v, e))

        fh.write("\n## No citing paper in this corpus\n\n")
        fh.write("These need an external lookup. %d pages.\n\n" % len(none_rows))
        for slug, title, year, _, _, _ in none_rows:
            fh.write("- `%s` (%s)\n" % (slug, year))

    sys.stderr.write("\nwrote %s\n" % OUT)
    sys.stderr.write("agreed %d, weak %d, none %d\n"
                     % (len(agreed_rows), len(weak_rows), len(none_rows)))


if __name__ == "__main__":
    main()
