#!/usr/bin/env python3
"""Generate refs.bib from the front matter of wiki/sources/*.md.

Citation keys follow the IACR style fixed in the research skill's conventions.md:
one author gives the first three letters of the surname plus the two-digit year,
two or more give the initial of each surname in author order plus the year.
Collisions take a lowercase suffix in slug order.

Every entry carries annote = {wiki: <slug>} so the Part V mapping tables can be
joined to the corpus mechanically rather than by hand.
"""
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "..", "wiki", "sources"))
OUT = os.path.abspath(os.path.join(HERE, "..", "refs.bib"))

PARTICLES = {"van", "von", "de", "der", "den", "di", "du", "la", "le", "del", "da", "dos"}


def front_matter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
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


def unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        s = s[1:-1]
    return s.replace('\\"', '"').strip()


def authors(raw):
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        raw = raw[1:-1]
    names = [unquote(a) for a in raw.split(",") if a.strip()]
    return [n for n in names if n]


def surname(name):
    parts = [p for p in name.replace(".", ". ").split() if p]
    if not parts:
        return ""
    # walk back over a trailing suffix such as Jr
    while len(parts) > 1 and parts[-1].rstrip(".").lower() in {"jr", "sr", "ii", "iii"}:
        parts.pop()
    last = parts[-1]
    if len(parts) >= 2 and parts[-2].lower() in PARTICLES:
        pass  # the capitalized element is already `last`
    return last.split("-")[0]


def citekey(names, year):
    yy = str(year)[-2:]
    if not names:
        return "Anon" + yy
    if len(names) == 1:
        s = surname(names[0])
        return (s[:3].capitalize() if s else "Anon") + yy
    return "".join(surname(n)[:1].upper() for n in names if surname(n)) + yy


# Tectonic runs XeTeX, where a raw non-ASCII byte reaches the font directly and
# the EC fonts have no slot for most of them. The bibliography therefore carries
# LaTeX escapes rather than UTF-8, which also keeps it engine-independent.
UNI = {
    "\u2014": "---", "\u2013": "--", "\u2018": "`", "\u2019": "'",
    "\u201c": "``", "\u201d": "''", "\u00b2": "$^2$",
    "\u00e0": "\\`a", "\u00e1": "\\'a", "\u00e8": "\\`e", "\u00e9": "\\'e",
    "\u00eb": '\\"e', "\u00ed": "\\'i", "\u00f1": "\\~n", "\u00f3": "\\'o",
    "\u00fc": '\\"u', "\u0105": "\\k{a}", "\u0107": "\\'c", "\u010d": "\\v{c}",
    "\u0142": "\\l{}", "\u015b": "\\'s", "\u017c": "\\.z", "\u0161": "\\v{s}",
    "\u011f": "\\u{g}", "\u015f": "\\c{s}", "\u0130": "\\.I", "\u0131": "\\i{}",
}


def latex_escape(s):
    for a, b in (("&", r"\&"), ("%", r"\%"), ("#", r"\#"), ("_", r"\_")):
        s = s.replace(a, b)
    out = []
    for ch in s:
        if ord(ch) < 128:
            out.append(ch)
        elif ch in UNI:
            out.append("{" + UNI[ch] + "}")
        else:
            out.append("?")
            sys.stderr.write("unmapped character U+%04X in: %s\n" % (ord(ch), s[:60]))
    return "".join(out)


def short_venue(v):
    """The advisor's checklist asks for the short form with no year, so "ACM CCS"
    rather than "In Proceedings of the 36th ACM Conference ... , 2021"."""
    v = unquote(v)
    v = re.split(r"\s*\(", v)[0]
    v = v.strip().rstrip(",;.")
    v = re.sub(r"^(in\s+)?proceedings of (the\s+)?(\d+(st|nd|rd|th)\s+)?", "", v, flags=re.I)
    v = re.sub(r"^the\s+", "", v, flags=re.I)
    v = re.sub(r"^\d+(st|nd|rd|th)\s+(annual\s+)?", "", v, flags=re.I)
    v = re.sub(r"[,\s]*\b(19|20)\d\d\b", "", v)          # drop any year
    v = re.sub(r"[,\s]*\b(vol\.?|volume|pp\.?|pages)\b.*$", "", v, flags=re.I)
    v = re.split(r"\s*,", v)[0]                              # drop trailing commentary
    v = v.strip().rstrip(",;.:")
    for long, short in ABBREV:
        if re.fullmatch(long, v, re.I):
            return short
    return v


ABBREV = [
    (r"IEEE European Symposium on Security and Privacy", "IEEE EuroS&P"),
    (r"IEEE Symposium on Security and Privacy", "IEEE S&P"),
    (r"IEEE Conference on Secure and Trustworthy Machine Learning", "IEEE SaTML"),
    (r"Advances in Neural Information Processing Systems", "NeurIPS"),
    (r"International Conference on Machine Learning", "ICML"),
    (r"International Conference on Learning Representations", "ICLR"),
    (r"ACM (SIGSAC )?Conference on Computer and Communications Security", "ACM CCS"),
    (r"USENIX Security Symposium", "USENIX Security"),
    (r"Conference on Learning Theory", "COLT"),
    (r"Network and Distributed System Security Symposium", "NDSS"),
    (r"ACM Symposium on Theory of Computing", "STOC"),
    (r"IEEE Symposium on Foundations of Computer Science", "FOCS"),
]


def arxiv_id(*fields):
    for f in fields:
        m = re.search(r"ar[Xx]iv(?:\s+(?:preprint|e-?print))?[:\s]\s*(\d{4}\.\d{4,5})", f or "")
        if m:
            return m.group(1)
    return None


def main():
    records = []
    for fn in sorted(os.listdir(SRC)):
        if not fn.endswith(".md"):
            continue
        slug = fn[:-3]
        text = open(os.path.join(SRC, fn), encoding="utf-8").read()
        fm = front_matter(text)
        if fm.get("type", "").strip() != "source":
            continue
        title = unquote(fm.get("title", slug))
        names = authors(fm.get("authors", "[]"))
        year = unquote(fm.get("year", "")) or "0000"
        venue_raw = unquote(fm.get("venue", ""))
        ingested = unquote(fm.get("date_ingested", ""))
        records.append(dict(slug=slug, title=title, names=names, year=year,
                            venue=venue_raw, ingested=ingested))

    # keys, with deterministic collision suffixes
    buckets = defaultdict(list)
    for r in records:
        buckets[citekey(r["names"], r["year"])].append(r)
    for base, group in buckets.items():
        group.sort(key=lambda r: r["slug"])
        for i, r in enumerate(group):
            r["key"] = base if len(group) == 1 else base + chr(ord("a") + i)

    records.sort(key=lambda r: r["key"])
    lines = [
        "% Generated by tools/gen-bib.py from the front matter of wiki/sources/*.md.",
        "% Do not edit by hand. Correct the wiki page and regenerate.",
        "% Entries whose venue could not be read off the primary PDF carry",
        "% venue-unconfirmed in the annote field and are still owed a check.",
        "",
    ]
    unconfirmed = 0
    for r in records:
        sv = short_venue(r["venue"])
        aid = arxiv_id(r["venue"])
        unconf = bool(re.search(r"unconfirmed", r["venue"], re.I))
        bare_arxiv = bool(re.match(r"^(arxiv|preprint|arxiv preprint)\b", sv, re.I)) or not sv
        if unconf:
            unconfirmed += 1
        note = "wiki: " + r["slug"]
        if unconf:
            note += "; venue-unconfirmed"
        auth = " and ".join(r["names"]) if r["names"] else "Anonymous"
        if aid and (bare_arxiv or unconf):
            lines.append("@misc{%s," % r["key"])
            lines.append("  author       = {%s}," % latex_escape(auth))
            lines.append("  title        = {%s}," % latex_escape(r["title"]))
            lines.append("  year         = {%s}," % r["year"])
            lines.append("  howpublished = {arXiv:%s}," % aid)
            if r["ingested"]:
                lines.append("  urldate      = {%s}," % r["ingested"])
        elif sv:
            lines.append("@inproceedings{%s," % r["key"])
            lines.append("  author       = {%s}," % latex_escape(auth))
            lines.append("  title        = {%s}," % latex_escape(r["title"]))
            lines.append("  booktitle    = {%s}," % latex_escape(sv))
            lines.append("  year         = {%s}," % r["year"])
        else:
            lines.append("@misc{%s," % r["key"])
            lines.append("  author       = {%s}," % latex_escape(auth))
            lines.append("  title        = {%s}," % latex_escape(r["title"]))
            lines.append("  year         = {%s}," % r["year"])
            if r["ingested"]:
                lines.append("  urldate      = {%s}," % r["ingested"])
        lines.append("  annote       = {%s}," % latex_escape(note))
        lines.append("}")
        lines.append("")

    open(OUT, "w", encoding="utf-8").write("\n".join(lines))
    sys.stderr.write("wrote %s: %d entries, %d with venue unconfirmed\n"
                     % (OUT, len(records), unconfirmed))


if __name__ == "__main__":
    main()
