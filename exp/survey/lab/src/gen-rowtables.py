#!/usr/bin/env python3
"""Three tables for the body of the paper, generated from the classification.

  sections/05-relative-table.tex   the works whose bound relates two parties' work
  sections/05-nearmiss-table.tex   the works whose stated tightness and treatment disagree
  sections/05-party-unit.tex       party by unit, counts, attack works only

The relation and quantity columns are hand-written in notes/relative-rows.tsv and
notes/near-miss-rows.tsv. tools/check-numbers.py refuses to pass while either
file's slug set differs from the set the classification computes.
"""
import collections
import csv
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SUR = os.path.abspath(os.path.join(HERE, "..", ".."))
R = list(csv.DictReader(open(os.path.join(SUR, "lab", "results", "corpus-classification", "classification.tsv"), encoding="utf-8"), delimiter="\t"))
bib = open(os.path.join(SUR, "paper", "refs.bib"), encoding="utf-8").read()
KEY = {m.group(2).strip(): m.group(1) for m in re.finditer(r"@\w+\{(\w+),.*?annote\s*=\s*\{wiki: ([^;}]*)", bib, re.S)}
BY = {r["slug"]: r for r in R}
ATTACK = lambda r: r["family"] not in ("none", "")


def esc(s):
    return s.replace("&", "\\&").replace("%", "\\%")


def relative():
    rel = {r["slug"] for r in R if r["tightness"] == "relative"}
    hand = list(csv.DictReader(open(os.path.join(SUR, "lab", "results", "corpus-classification", "relative-rows.tsv"), encoding="utf-8"), delimiter="\t"))
    rows = sorted(hand, key=lambda h: (not ATTACK(BY[h["slug"]]), h["slug"]))
    n_att = sum(1 for h in rows if ATTACK(BY[h["slug"]]))
    out = ["\\begin{table*}[t]", "\\centering", "\\small",
           "\\caption{The \\NumRelative{} works that state a bound as a relation between two parties' "
           "work. The first \\NumRelativeAttack{} study an attack; the rest are cryptography with no "
           "machine learning content. Each relation is given in the source's own notation.}",
           "\\label{tab:relative}",
           "\\begin{tabular}{@{}lllp{2.2cm}p{7.4cm}@{}}", "\\toprule",
           "Work & Attack & Bounded party, unit & Second party's unit & Relation as stated \\\\", "\\midrule"]
    for i, h in enumerate(rows):
        r = BY[h["slug"]]
        if i == n_att:
            out.append("\\midrule")
        out.append("\\cite{%s} & %s & %s, %s & %s & %s \\\\" % (
            KEY[h["slug"]], esc(r["family"]) if ATTACK(r) else "none", r["party"], esc(r["unit"]),
            esc(r["second_party"]), h["relation"]))
    out += ["\\bottomrule", "\\end{tabular}", "\\end{table*}"]
    open(os.path.join(SUR, "paper", "tables", "05-relative-table.tex"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    return rel, {h["slug"] for h in hand}


DEF = {"budget", "class", "conditional", "exponent", "relative", "poly", "quasi-poly"}


def near_set():
    return {r["slug"] for r in R
            if (r["tightness"] in DEF and r["assessed"] == "implicit")
            or (r["tightness"] == "measured" and r["assessed"] == "explicit")
            or (r["tightness"] == "unstated" and r["assessed"])}


def nearmiss():
    hand = list(csv.DictReader(open(os.path.join(SUR, "lab", "results", "corpus-classification", "near-miss-rows.tsv"), encoding="utf-8"), delimiter="\t"))
    KIND = {"adversary": "adversary's cost", "training": "training cost", "capability": "capability or mechanism"}
    order = ["adversary", "training", "capability"]
    rows = sorted(hand, key=lambda h: (order.index(h["kind"]), h["slug"]))
    out = ["\\begin{table*}[t]", "\\centering", "\\small",
           "\\caption{The \\NearMiss{} works whose stated tightness and treatment of the bound disagree. "
           "Kind records what the quantity is: \\NearMissAdv{} hold an adversary's or auditor's cost, "
           "\\NearMissTrain{} a training cost, and \\NearMissCap{} a capability or a mechanism parameter.}",
           "\\label{tab:nearmiss}",
           "\\begin{tabular}{@{}lp{3.2cm}p{2.4cm}p{6.6cm}p{2.7cm}@{}}", "\\toprule",
           "Work & Kind & Tightness, treatment & Quantity held & Where \\\\", "\\midrule"]
    last = None
    for h in rows:
        r = BY[h["slug"]]
        if last and h["kind"] != last:
            out.append("\\midrule")
        last = h["kind"]
        out.append("\\cite{%s} & %s & %s, %s & %s & %s \\\\" % (
            KEY[h["slug"]], KIND[h["kind"]], r["tightness"], r["assessed"] or "none", h["quantity"], esc(h["where"])))
    out += ["\\bottomrule", "\\end{tabular}", "\\end{table*}"]
    open(os.path.join(SUR, "paper", "tables", "05-nearmiss-table.tex"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    return near_set(), {h["slug"] for h in hand}, collections.Counter(h["kind"] for h in hand)


def party_unit():
    ml = [r for r in R if ATTACK(r)]
    parties = ["attacker", "learner", "auditor", "mechanism", "none"]
    c = collections.Counter((r["unit"], r["party"]) for r in ml)
    units = [u for u, _ in collections.Counter(r["unit"] for r in ml).most_common()]
    out = ["\\begin{table}[t]", "\\centering", "\\small",
           "\\caption{The \\NumAttackWorks{} works that study an attack, by the party their main claim "
           "bounds and the unit of that bound. The largest cell is no party in no unit.}",
           "\\label{tab:attack-party-unit}",
           "\\begin{tabular}{@{}l" + "r" * len(parties) + "@{}}", "\\toprule",
           "Unit & " + " & ".join(p.capitalize() if p != "none" else "None" for p in parties) + " \\\\", "\\midrule"]
    for u in units:
        out.append(esc(u) + " & " + " & ".join(str(c[(u, p)]) if c[(u, p)] else "" for p in parties) + " \\\\")
    out += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    open(os.path.join(SUR, "paper", "tables", "05-party-unit.tex"), "w", encoding="utf-8").write("\n".join(out) + "\n")


if __name__ == "__main__":
    rel, relh = relative()
    ns, nh, kinds = nearmiss()
    party_unit()
    print("relative: computed %d, table %d, %s" % (len(rel), len(relh), "match" if rel == relh else "MISMATCH " + str(rel ^ relh)))
    print("near-miss: computed %d, table %d, %s; kinds %s" % (len(ns), len(nh), "match" if ns == nh else "MISMATCH " + str(ns ^ nh), dict(kinds)))
