#!/usr/bin/env python3
"""Gate G4: no number in the paper is stale.

Recomputes every macro in results.tex from the classification and compares. Any
disagreement is a number the paper prints that the corpus no longer supports.
"""
import collections
import csv
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SUR = os.path.abspath(os.path.join(HERE, ".."))
R = list(csv.DictReader(open(os.path.join(SUR, "notes", "classification.tsv"),
                             encoding="utf-8"), delimiter="\t"))
ml = [r for r in R if r["family"] not in ("none", "")]
non = [r for r in R if r["family"] in ("none", "")]
t = collections.Counter(r["tightness"] for r in ml)
DEF = {"budget", "class", "conditional", "exponent", "relative", "poly", "quasi-poly"}
near = sum(1 for r in R
           if (r["tightness"] in DEF and r["assessed"] == "implicit")
           or (r["tightness"] == "measured" and r["assessed"] == "explicit")
           or (r["tightness"] == "unstated" and r["assessed"]))
x = collections.defaultdict(collections.Counter)
for r in R:
    x[r["tightness"]][r["assessed"] or "b"] += 1

want = {
    "NumSources": len(R),
    "NumPapers": len(glob.glob(os.path.join(SUR, "..", "..", "raw", "*.pdf"))),
    "NumUnstated": sum(1 for r in R if r["party"] == "none"),
    "NumPriced": sum(1 for r in R if r["party"] != "none"),
    "NumAttackWorks": len(ml), "NumTheoryWorks": len(non),
    "AttackUnbound": sum(1 for r in ml if r["party"] == "none"),
    "TheoryUnbound": sum(1 for r in non if r["party"] == "none"),
    "NumExponent": sum(1 for r in R if r["tightness"] == "exponent"),
    "NumRelative": sum(1 for r in R if r["tightness"] == "relative"),
    "NumRelativeAttack": sum(1 for r in ml if r["tightness"] == "relative"),
    "NumFlops": sum(1 for r in R if r["unit"] == "flops"),
    "AttackTimeAttacker": sum(1 for r in ml if r["unit"] == "time" and r["party"] == "attacker"),
    "NearMissA": sum(1 for r in R if r["tightness"] in DEF and r["assessed"] == "implicit"),
    "NearMissB": sum(1 for r in R if r["tightness"] == "measured" and r["assessed"] == "explicit"),
    "NearMissC": sum(1 for r in R if r["tightness"] == "unstated" and r["assessed"]),
    "AttackBudget": t["budget"], "AttackUnstated": t["unstated"],
    "AttackPoly": t["poly"], "AttackMeasured": t["measured"],
    "AttackClass": t["class"],
    "AttackPerturb": sum(1 for r in ml if r["unit"] == "perturbation"),
    "AttackCorrupt": sum(1 for r in ml if r["unit"] == "corruption"),
    "AttackAccessNamed": sum(1 for r in ml if r["access"] not in ("none", "")),
    "AttackPostHoc": sum(1 for r in ml if r["access"] not in ("none", "") and r["phase"] == "post hoc"),
    "AttackTestTime": sum(1 for r in ml if r["access"] not in ("none", "") and r["phase"] == "test time"),
    "AttackTrainTime": sum(1 for r in ml if r["access"] not in ("none", "") and r["phase"] == "train time"),
    "AttackQueriesAttacker": sum(1 for r in ml if r["unit"] == "queries" and r["party"] == "attacker"),
    "AttackSamplesAttacker": sum(1 for r in ml if r["unit"] == "samples" and r["party"] == "attacker"),
    "NumMIAfamily": sum(1 for r in R if r["family"] == "membership"),
    "NearMiss": near,
    "NumPhaseAccessCells": len(set((r["phase"], r["access"]) for r in R
                                   if r["phase"] and r["access"])),
    "NumPartyUnitCells": len(set((r["party"], r["unit"]) for r in R)),
    "AssessedPredictable": round(100 * sum(x[k].most_common(1)[0][1] for k in x) / len(R)),
}
src = open(os.path.join(SUR, "results.tex"), encoding="utf-8").read()
bad = []
for k, v in sorted(want.items()):
    m = re.search(r"\\newcommand\{\\%s\}\{([^}]*)\}" % k, src)
    if not m:
        bad.append((k, "absent", v))
    elif m.group(1).strip() != str(v):
        bad.append((k, m.group(1).strip(), v))
if bad:
    print("STALE NUMBERS: %d" % len(bad))
    for k, got, exp in bad:
        print("  %-22s paper=%-8s corpus=%s" % (k, got, exp))
    sys.exit(1)
print("all %d macros match the corpus" % len(want))
