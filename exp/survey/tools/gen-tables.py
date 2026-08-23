#!/usr/bin/env python3
"""Emit the survey's classification tables as LaTeX.

Two layers, both in the body for now so they can be inspected together.

  Layer 1, four cross-tabulations. Features on both axes, works in the cells, by
  citation number. This is the layer that makes absence visible: an empty cell is
  a combination nobody in the corpus has published.

  Layer 2, the two per-work tables. One row per work, the reference layer that
  makes every cross-tab cell traceable.

Regenerate after any change to the classification TSV. Nothing here is written by
hand.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SUR = os.path.abspath(os.path.join(HERE, ".."))
ROOT = os.path.abspath(os.path.join(SUR, "..", ".."))
SRC = os.path.join(ROOT, "wiki", "sources")
OUT = os.path.join(SUR, "sections", "03-tables.tex")

VALUES = {
    "party":     ["attacker", "learner", "auditor", "mechanism", "none"],
    "unit":      ["time", "circuit size", "queries", "samples", "memory",
                  "algo class", "parameters", "perturbation", "corruption",
                  "rounds", "privacy budget", "circuit depth",
                  "success prob", "none"],
    "phase":     ["train time", "test time", "post hoc", "n/a"],
    "access":    ["hard label", "scores", "black box", "white box", "weights",
                  "gradients", "channel", "none"],
    "tightness": ["unstated", "poly", "quasi-poly", "class", "budget",
                  "conditional", "exponent", "measured"],
    "frame":     ["compute", "statistical", "capability", "none"],
    "family":    ["membership", "attribute", "reconstruct", "distribution",
                  "extract", "invert", "forge", "evade", "evade audit",
                  "inject", "poison", "backdoor", "multiple", "none"],
}
NICE = {"party": "constrained party", "unit": "resource unit",
        "phase": "pipeline phase", "access": "access level",
        "tightness": "tightness of the bound", "family": "attack family"}

T1 = [("target", "Target"), ("family", "Family"), ("phase", "Phase"),
      ("access", "Access"), ("write", "Write"), ("frame", "Frame")]
T2 = [("party", "Party"), ("unit", "Unit"), ("tightness", "Tightness"),
      ("baseline", "Baseline"), ("second_party", "2nd party"),
      ("second_notion", "2nd notion"), ("assessed", "Assessed"),
      ("quantifier", "Quantifier"), ("antecedent", "Antecedent")]


def keys_by_slug():
    text = open(os.path.join(SUR, "refs.bib"), encoding="utf-8").read()
    out = {}
    for m in re.finditer(r"@\w+\{([^,]+),(.*?)\n\}", text, re.S):
        s = re.search(r"wiki: ([a-z0-9-]+)", m.group(2))
        if s:
            out[s.group(1)] = m.group(1).strip()
    return out


def front(slug):
    t = open(os.path.join(SRC, slug + ".md"), encoding="utf-8").read()
    fm = t[3:t.find("\n---", 3)]
    def g(k):
        m = re.search(r"^" + k + r":\s*(.*)$", fm, re.M)
        return m.group(1).strip().strip('"') if m else ""
    a = g("antecedent")
    return g("claim_quantifier").lower(), ("" if not a else
            ("none" if a.lower().rstrip(".") in ("none", "n/a") else "stated"))


def esc(s):
    return s.replace("&", r"\&").replace("_", r"\_") if s else "$\\cdot$"


def cite_group(keys):
    return "\\cite{%s}" % ",".join(keys) if keys else ""


def crosstab(rows, kb, a, b, label, mark_implicit=False):
    """Rows indexed by feature a, columns by feature b, cells carry citations."""
    # A classifier that leaves a field blank is asking for a second reader, which is
    # the behaviour the brief wants. Blanks therefore get their own row and column
    # rather than being dropped: a dropped row would silently falsify the totals.
    av, bv = list(VALUES[a]), list(VALUES[b])
    if any(not r.get(a, "") for r in rows): av.append("")
    if any(not r.get(b, "") for r in rows): bv.append("")
    grid = {(x, y): {"e": [], "i": []} for x in av for y in bv}
    off = 0
    for r in rows:
        x, y = r.get(a, ""), r.get(b, "")
        if (x, y) not in grid:
            off += 1
            continue
        k = kb.get(r["slug"])
        if not k:
            continue
        grid[(x, y)]["i" if (mark_implicit and r.get("assessed") == "implicit") else "e"].append(k)

    width = "%.2fcm" % min(3.1, max(1.7, 21.0 / (len(bv) + 1)))
    spec = "l" + ("p{%s}" % width) * len(bv) + "r"
    out = ["\\begin{landscape}", "\\begingroup\\scriptsize\\setlength{\\tabcolsep}{3pt}",
           "\\begin{longtable}{%s}" % spec]
    cap = ("The corpus by %s (rows) against %s (columns). Each cell lists every work "
           "with that combination, by citation number. An empty cell is a combination "
           "no work in the corpus occupies." % (NICE[a], NICE[b]))
    if mark_implicit:
        cap += (" A dagger marks works where the resource appears only as a side "
                "condition rather than as a parameter the work assesses on purpose.")
    out.append("\\caption{%s}\\label{%s}\\\\" % (cap, label))
    head = (" & ".join(["\\textbf{%s}" % esc(a)] + ["\\textbf{%s}" % ("\\emph{unassigned}" if y=="" else esc(y)) for y in bv]
                       + ["\\textbf{$\\Sigma$}"]) + " \\\\")
    out.append("\\toprule " + head + " \\midrule\\endfirsthead")
    out.append("\\multicolumn{%d}{l}{\\emph{Table \\ref{%s}, continued}}\\\\" % (len(bv) + 2, label))
    out.append("\\toprule " + head + " \\midrule\\endhead")
    out.append("\\bottomrule\\endfoot")
    for x in av:
        cells, tot = [], 0
        for y in bv:
            g = grid[(x, y)]
            tot += len(g["e"]) + len(g["i"])
            parts = []
            if g["e"]:
                parts.append(cite_group(sorted(g["e"])))
            if g["i"]:
                parts.append(cite_group(sorted(g["i"])) + "$^\\dagger$")
            cells.append(", ".join(parts) if parts else "")
        label = "\\emph{unassigned}" if x == "" else esc(x)
        out.append(label + " & " + " & ".join(cells) + " & %d \\\\" % tot)
    out.append("\\midrule")
    tots = []
    for y in bv:
        tots.append(str(sum(len(grid[(x, y)]["e"]) + len(grid[(x, y)]["i"]) for x in av)))
    out.append("$\\Sigma$ & " + " & ".join(tots) + " & %d \\\\" % (len(rows) - off))
    out += ["\\end{longtable}", "\\endgroup", "\\end{landscape}"]
    return "\n".join(out), off


def perwork(rows, cols, caption, label, kb):
    spec = "r" + "l" * len(cols)
    head = " & ".join(["\\#"] + ["\\textbf{%s}" % h for _, h in cols]) + " \\\\"
    out = ["\\begin{landscape}", "\\begingroup\\scriptsize\\setlength{\\tabcolsep}{4pt}",
           "\\begin{longtable}{%s}" % spec,
           "\\caption{%s}\\label{%s}\\\\" % (caption, label),
           "\\toprule " + head + " \\midrule\\endfirsthead",
           "\\multicolumn{%d}{l}{\\emph{Table \\ref{%s}, continued}}\\\\" % (len(cols) + 1, label),
           "\\toprule " + head + " \\midrule\\endhead", "\\bottomrule\\endfoot"]
    for r in rows:
        k = kb.get(r["slug"])
        out.append(("\\cite{%s}" % k if k else "--") + " & "
                   + " & ".join(esc(r.get(c, "")) for c, _ in cols) + " \\\\")
    out += ["\\end{longtable}", "\\endgroup", "\\end{landscape}"]
    return "\n".join(out)


def main():
    tsv = sys.argv[1] if len(sys.argv) > 1 else os.path.join(SUR, "notes", "classification-batch1.tsv")
    rows = list(csv.DictReader(open(tsv, encoding="utf-8"), delimiter="\t"))
    kb = keys_by_slug()
    for r in rows:
        r["quantifier"], r["antecedent"] = front(r["slug"])
    rows.sort(key=lambda r: (VALUES["family"].index(r["family"])
                             if r["family"] in VALUES["family"] else 99, r["slug"]))

    n = len(rows)
    n_out = sum(1 for r in rows if r.get("frame") == "out")
    n_none = sum(1 for r in rows if r.get("party") == "none")

    b = []
    b.append("\\section{Classifying the corpus}")
    b.append("\\label{sec:tables}")
    b.append("")
    b.append("This section reports the corpus in two layers. Tables~\\ref{tab:party-unit} "
             "to~\\ref{tab:family-party} cross-tabulate features against one another, with "
             "works in the cells by citation number. Tables~\\ref{tab:scenario} "
             "and~\\ref{tab:adversary} give one row per work, so that every cell above is "
             "traceable to the paper behind it. Every value comes from a fixed vocabulary "
             "settled before the pass began.")
    b.append("")
    b.append("The cross-tabulations are the layer that carries an argument, because in them "
             "an empty cell is a combination nobody has published. The value "
             "\\texttt{none} is an answer and not a missing entry, recording that a work "
             "constrains no party at all. Of the %d works classified so far, %d state no "
             "resource bound on any party, and %d fall outside the frame in the sense that "
             "deleting every resource restriction leaves the main claim unchanged."
             % (n, n_none, n_out))
    b.append("")
    b.append("\\emph{This is a partial pass. %d of the corpus's works are classified. The "
             "remainder are not yet placed.}" % n)
    b.append("")

    for a, bb, lab, mark in [("phase", "access", "tab:phase-access", False),
                             ("party", "unit", "tab:party-unit", True),
                             ("unit", "tightness", "tab:unit-tightness", False),
                             ("family", "party", "tab:family-party", False)]:
        tex, off = crosstab(rows, kb, a, bb, lab, mark)
        if off:
            sys.stderr.write("  warning: %d rows fell outside the %s x %s vocabulary\n" % (off, a, bb))
        b.append(tex)
        b.append("")

    b.append(perwork(rows, T1, "Per-work reference layer: attack scenario and threat model.",
                     "tab:scenario", kb))
    b.append("")
    b.append(perwork(rows, T2, "Per-work reference layer: adversary assumptions and claim "
                     "shape. Same rows and same order as Table~\\ref{tab:scenario}.",
                     "tab:adversary", kb))
    b.append("")
    open(OUT, "w", encoding="utf-8").write("\n".join(b) + "\n")
    sys.stderr.write("wrote %s: %d rows, 4 cross-tabs + 2 per-work tables\n"
                     % (os.path.relpath(OUT, ROOT), n))


if __name__ == "__main__":
    main()
