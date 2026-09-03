#!/usr/bin/env python3
"""Gate G4: no number in the paper is stale.

Recomputes every counted macro in results.tex from the classification, the wiki
front matter and the two hand tables, and compares. With --write it rewrites the
macro values in results.tex in place, keeping every comment. Any disagreement
without --write is a number the paper prints that the corpus no longer supports.
"""
import collections
import csv
import glob
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SUR = os.path.abspath(os.path.join(HERE, ".."))
ROOT = os.path.abspath(os.path.join(SUR, "..", ".."))
R = list(csv.DictReader(open(os.path.join(SUR, "notes", "classification.tsv"), encoding="utf-8"), delimiter="\t"))


def front(slug, key):
    s = open(os.path.join(ROOT, "wiki", "sources", slug + ".md"), encoding="utf-8").read()
    m = re.search(r"^%s:[ \t]*(.*)$" % key, s, re.M)
    return m.group(1).strip() if m else ""


ml = [r for r in R if r["family"] not in ("none", "")]
non = [r for r in R if r["family"] in ("none", "")]
att = lambda rs, **k: sum(1 for r in rs if all(r[a] == b for a, b in k.items()))
t = collections.Counter(r["tightness"] for r in ml)
DEF = {"budget", "class", "conditional", "exponent", "relative", "poly", "quasi-poly"}
near = [r for r in R
        if (r["tightness"] in DEF and r["assessed"] == "implicit")
        or (r["tightness"] == "measured" and r["assessed"] == "explicit")
        or (r["tightness"] == "unstated" and r["assessed"])]
x = collections.defaultdict(collections.Counter)
for r in R:
    x[r["tightness"]][r["assessed"] or "b"] += 1

# theorem-bearing subset, from the claim quantifier on the wiki page
Q = {r["slug"]: front(r["slug"], "claim_quantifier") for r in R}
ta = [r for r in ml if Q[r["slug"]] != "empirical"]
to = [r for r in non if Q[r["slug"]] != "empirical"]


def diff_ci(a, n, b, m):
    p1, p2 = a / n, b / m
    se = math.sqrt(p1 * (1 - p1) / n + p2 * (1 - p2) / m)
    d = p1 - p2
    return 100 * (d - 1.96 * se), 100 * (d + 1.96 * se), p1 / p2


def top5(pairs):
    c = collections.Counter(pairs)
    return round(100 * sum(v for _, v in c.most_common(5)) / sum(c.values()))


# hand tables: their slug sets must equal the computed sets
rel = {r["slug"] for r in R if r["tightness"] == "relative"}
relh = {h["slug"] for h in csv.DictReader(open(os.path.join(SUR, "notes", "relative-rows.tsv"), encoding="utf-8"), delimiter="\t")}
nh = list(csv.DictReader(open(os.path.join(SUR, "notes", "near-miss-rows.tsv"), encoding="utf-8"), delimiter="\t"))
nhs = {h["slug"] for h in nh}
kinds = collections.Counter(h["kind"] for h in nh)
ev = collections.Counter()
for r in R:
    e = front(r["slug"], "cls_evidence").strip('"')
    ev["hand" if r["prov"] == "hand" else "absent" if e.lower() == "absent" else "quote" if e else "blank"] += 1

au, tu = att(ml, party="none"), att(non, party="none")
tau, tou = att(ta, party="none"), att(to, party="none")
lo, hi, ratio = diff_ci(au, len(ml), tu, len(non))
tlo, thi, tratio = diff_ci(tau, len(ta), tou, len(to))
learner = [r for r in R if r["party"] == "learner"]

want = {
    "NumSources": len(R),
    "NumPapers": len(glob.glob(os.path.join(ROOT, "raw", "*.pdf"))),
    "NumUnstated": att(R, party="none"), "NumPriced": len(R) - att(R, party="none"),
    "NumAttackWorks": len(ml), "NumTheoryWorks": len(non),
    "AttackUnbound": au, "TheoryUnbound": tu,
    "RateAttack": round(100 * au / len(ml)), "RateOther": round(100 * tu / len(non)),
    "RatioUnbound": "%.1f" % ratio, "DiffLo": "%.1f" % lo, "DiffHi": "%.1f" % hi,
    "ThmAttack": len(ta), "ThmAttackUnbound": tau, "ThmOther": len(to), "ThmOtherUnbound": tou,
    "ThmRatio": "%.1f" % tratio, "ThmDiffLo": "$%.1f$" % tlo, "ThmDiffHi": "%.1f" % thi,
    "NumExponent": att(R, tightness="exponent"),
    "NumRelative": att(R, tightness="relative"), "NumRelativeAttack": att(ml, tightness="relative"),
    "NumFlops": att(R, unit="flops"),
    "NumScaling": sum(1 for r in R if re.search(r"scaling", front(r["slug"], "tags"))),
    "AttackTimeAttacker": att(ml, unit="time", party="attacker"),
    "AttackQueriesAttacker": att(ml, unit="queries", party="attacker"),
    "AttackSamplesAttacker": att(ml, unit="samples", party="attacker"),
    "AttackPerturb": att(ml, unit="perturbation"), "AttackCorrupt": att(ml, unit="corruption"),
    "AttackBudget": t["budget"], "AttackUnstated": t["unstated"], "AttackPoly": t["poly"],
    "AttackMeasured": t["measured"], "AttackClass": t["class"],
    "AttackAccessNamed": sum(1 for r in ml if r["access"] not in ("none", "")),
    "AttackPostHoc": sum(1 for r in ml if r["access"] not in ("none", "") and r["phase"] == "post hoc"),
    "AttackTestTime": sum(1 for r in ml if r["access"] not in ("none", "") and r["phase"] == "test time"),
    "AttackTrainTime": sum(1 for r in ml if r["access"] not in ("none", "") and r["phase"] == "train time"),
    "PhaseAccessTopFive": top5((r["phase"], r["access"]) for r in ml),
    "PartyUnitTopFive": top5((r["party"], r["unit"]) for r in ml),
    "NumMIAfamily": att(R, family="membership"),
    "NearMiss": len(near),
    "NearMissA": sum(1 for r in near if r["tightness"] in DEF),
    "NearMissB": sum(1 for r in near if r["tightness"] == "measured"),
    "NearMissC": sum(1 for r in near if r["tightness"] == "unstated"),
    "NearMissAdv": kinds["adversary"], "NearMissTrain": kinds["training"], "NearMissCap": kinds["capability"],
    "AssessedPredictable": round(100 * sum(x[k].most_common(1)[0][1] for k in x) / len(R)),
    "BaselineNA": att(R, baseline="n/a"),
    "BaselineCrit": sum(1 for r in ml if r["baseline"] != "n/a"),
    "BaselineStated": att(ml, baseline="stated"), "BaselineAbsent": att(ml, baseline="absent"),
    "AttackerTimeCirc": sum(1 for r in R if r["party"] == "attacker" and r["unit"] in ("time", "circuit size")),
    "AttackerCapability": sum(1 for r in R if r["party"] == "attacker" and r["unit"] in ("perturbation", "corruption")),
    "AttackerPerturbAll": att(R, party="attacker", unit="perturbation"),
    "AttackerCorruptAll": att(R, party="attacker", unit="corruption"),
    "AttackerMemory": att(R, party="attacker", unit="memory"),
    "LearnerBound": len(learner), "LearnerTime": att(learner, unit="time"),
    "LearnerSamples": att(learner, unit="samples"), "LearnerClass": att(learner, unit="algo class"),
    "LearnerFlops": att(learner, unit="flops"),
    "LearnerOther": len(learner) - att(learner, unit="time") - att(learner, unit="samples") - att(learner, unit="algo class") - att(learner, unit="flops"),
    "AuditorBound": att(R, party="auditor"), "MechanismBound": att(R, party="mechanism"),
    "QuoteOnFile": ev["quote"], "QuoteAbsent": ev["absent"], "QuoteHand": ev["hand"],
}
problems = []
if rel != relh:
    problems.append("relative-rows.tsv differs from the classification: %s" % sorted(rel ^ relh))
if {r["slug"] for r in near} != nhs:
    problems.append("near-miss-rows.tsv differs from the classification: %s" % sorted({r["slug"] for r in near} ^ nhs))
if ev["blank"]:
    problems.append("%d rows carry neither a quotation nor an evidenced absence" % ev["blank"])

path = os.path.join(SUR, "results.tex")
src = open(path, encoding="utf-8").read()
bad, absent = [], []
for k, v in want.items():
    m = re.search(r"(\\newcommand\{\\%s\}\{)([^}]*)(\})" % k, src)
    if not m:
        absent.append(k)
    elif m.group(2).strip() != str(v):
        bad.append((k, m.group(2).strip(), v))
if "--write" in sys.argv:
    for k, got, v in bad:
        src = re.sub(r"(\\newcommand\{\\%s\}\{)[^}]*(\})" % k, lambda m: m.group(1) + str(v) + m.group(2), src)
    if absent:
        src += "\n% --- Added by check-numbers.py --write; computed from the classification.\n"
        src += "".join("\\newcommand{\\%s}{%s}\n" % (k, want[k]) for k in absent)
    open(path, "w", encoding="utf-8").write(src)
    print("wrote %d changed and %d new macros" % (len(bad), len(absent)))
    bad, absent = [], []
for p in problems:
    print("PROBLEM:", p)
if bad or absent:
    print("STALE NUMBERS: %d, ABSENT: %d" % (len(bad), len(absent)))
    for k, got, exp in bad:
        print("  %-22s paper=%-8s corpus=%s" % (k, got, exp))
    for k in absent:
        print("  %-22s absent   corpus=%s" % (k, want[k]))
    sys.exit(1)
if problems:
    sys.exit(1)
print("all %d macros match the corpus" % len(want))
