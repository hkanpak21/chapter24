#!/usr/bin/env python3
"""Build lib/literature/ontology/onto.tsv and views.md.

Usage: merge-onto.py [--write]

Inputs:
  lab/results/literature-ontology/coded-*.tsv   the agents' coded facts, no header
  lib/literature/ontology/hand.tsv              facts entered by hand, no header
  lib/literature/ontology/aliases.tsv           other ids for one work, mapped to one id
  lib/literature/ontology/papers.tsv            candidate works and the author's decisions
  lib/literature/ontology/schema.tsv            the vocabulary: every slug with its type

Outputs, with --write:
  onto.tsv               every fact, one per line, sorted by subject. Generated.
  views.md               counts and tables over onto.tsv. Generated.

Without --write it validates and prints the error count only.
"""
import collections
import csv
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ONTO = os.path.join(HERE, "..", "..", "lib", "literature", "ontology")
CODED = os.path.join(HERE, "..", "results", "literature-ontology")

# predicates from a work to a vocabulary slug, with the slug type they require
TYPED = {
    "relevance": "relevance", "treats-training-as": "training-model",
    "grants-access": "access-model", "quantifies-over": "adversary-class",
    "charges": "resource", "conditions-on": "utility-condition",
    "uses-notion": "security-notion", "defines": "security-notion",
    "assumes": "assumption", "concludes": "result-form", "addresses": "task",
    "reports-in": "phrasing", "author-decision": "author-decision", "in-group": "group",
}
# predicates between works, or between any two nodes, checked for known nodes only
FREE = {
    "extends", "converse-of", "converse", "refutes", "refutes-in-practice", "applies",
    "precursor-of", "systematizes", "competes-with", "cited-by", "related",
    "limit-of", "analogue-of", "equivalent-to", "modelled-on", "instance-of",
    "proves-impossible", "proves-equal", "separates", "strengthens", "queries",
    "bounds", "depends-on", "recovers-up-to", "answers", "uninstantiates",
    "shares-property",
}
CHECKED = {"wiki", "sweep", "pdf", "inferred", "heuristic", "hand", "to-verify"}


def read_rows(path):
    with open(path) as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if line.strip():
                yield f"{os.path.basename(path)}:{n}", line.split("\t")


def main():
    write = "--write" in sys.argv
    slug_type = {}
    with open(os.path.join(ONTO, "schema.tsv")) as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["type"] != "type":
                slug_type[row["slug"]] = row["type"]
    alias = {}
    with open(os.path.join(ONTO, "aliases.tsv")) as f:
        for row in csv.DictReader(f, delimiter="\t"):
            alias[row["alias"]] = row["canonical"]
    sources = sorted(glob.glob(os.path.join(CODED, "coded-*.tsv"))) + [os.path.join(ONTO, "hand.tsv")]

    # a work coded under its own id wins over a duplicate coded under an alias
    direct = set()
    for path in sources:
        for _, parts in read_rows(path):
            if len(parts) == 5 and parts[1] == "relevance" and parts[0] not in alias:
                direct.add(parts[0])

    errors, proposed, facts = [], {}, []
    for path in sources:
        for where, parts in read_rows(path):
            if len(parts) != 5:
                errors.append(f"{where}: {len(parts)} columns")
                continue
            s, p, o, note, chk = parts
            if p == "is-a" and "proposed" in (chk, note):
                proposed[s] = (o, note if chk == "proposed" else "")
                continue
            if s in alias:
                if alias[s] in direct and path != os.path.join(ONTO, "hand.tsv"):
                    continue
                s = alias[s]
            o = alias.get(o, o)
            facts.append((s, p, o, note, chk, where))

    with open(os.path.join(ONTO, "papers.tsv")) as f:
        for n, row in enumerate(csv.DictReader(f, delimiter="\t"), 2):
            w = alias.get(row["key"], row["key"])
            facts.append((w, "author-decision", "decide-" + row["decision"], "", "hand", f"papers.tsv:{n}"))
            facts.append((w, "in-group", row["group"], "", "hand", f"papers.tsv:{n}"))

    known = dict(slug_type)
    for s, (ty, _) in proposed.items():
        known.setdefault(s, ty)
    works = {f[0] for f in facts if f[1] == "relevance"}
    nodes = set(known) | works | {f[0] for f in facts if f[4] == "hand"}
    for s, p, o, note, chk, where in facts:
        if chk not in CHECKED:
            errors.append(f"{where}: checked={chk!r}")
        if p in TYPED:
            if known.get(o) != TYPED[p]:
                errors.append(f"{where}: {p} {o} needs a {TYPED[p]}, found {known.get(o)}")
        elif p in FREE:
            for x in (s, o):
                if x not in nodes:
                    errors.append(f"{where}: unknown node {x}")
        else:
            errors.append(f"{where}: unknown predicate {p}")
    print(f"{len(facts)} facts, {len(works)} works, {len(proposed)} proposed slugs, {len(errors)} errors")
    for e in errors[:40]:
        print("  ERROR", e)
    if not write:
        return 1 if errors else 0

    facts.sort(key=lambda f: (f[0], f[1] != "relevance", f[1], f[2]))
    with open(os.path.join(ONTO, "onto.tsv"), "w") as f:
        f.write("subject\tpredicate\tobject\tnote\tchecked\n")
        for s, p, o, note, chk, _ in facts:
            f.write("\t".join((s, p, o, note, chk)) + "\n")
        for s, (ty, note) in sorted(proposed.items()):
            f.write("\t".join((s, "is-a", ty, note, "proposed")) + "\n")

    rel = {s: o for s, p, o, *_ in facts if p == "relevance"}
    keep = {w for w, r in rel.items() if r in ("core", "peripheral")}
    v = ["# Ontology views", "",
         "Generated by `lab/src/merge-onto.py` from `onto.tsv`. Do not edit.",
         "Counts are works, over those coded core or peripheral. The coding is the",
         "agents' reading of wiki pages and sweep sheets, so the counts describe the",
         "coding, not the papers.", "",
         "Relevance: " + ", ".join(f"{k} {n}" for k, n in collections.Counter(rel.values()).most_common()), ""]
    for pred in ["treats-training-as", "grants-access", "quantifies-over", "charges",
                 "conditions-on", "assumes", "concludes", "reports-in", "uses-notion", "defines"]:
        by = collections.defaultdict(set)
        for s, p, o, *_ in facts:
            if p == pred and s in keep:
                by[o].add(s)
        v += [f"## {pred}", "", "| value | works | examples |", "| --- | --- | --- |"]
        for o, ws in sorted(by.items(), key=lambda kv: -len(kv[1])):
            v.append(f"| {o} | {len(ws)} | {', '.join(sorted(ws)[:6])} |")
        v.append("")
    tm, ac = collections.defaultdict(set), collections.defaultdict(set)
    for s, p, o, *_ in facts:
        if s in keep and p == "treats-training-as":
            tm[s].add(o)
        if s in keep and p == "grants-access":
            ac[s].add(o)
    cross = collections.Counter()
    for s in keep:
        for a in tm.get(s, {"(none)"}):
            for b in ac.get(s, {"(none)"}):
                cross[(a, b)] += 1
    accs = sorted({b for _, b in cross})
    v += ["## treats-training-as against grants-access", "",
          "| training \\ access | " + " | ".join(accs) + " |", "|---" * (len(accs) + 1) + "|"]
    for a in sorted({a for a, _ in cross}):
        v.append(f"| {a} | " + " | ".join(str(cross.get((a, b), "")) for b in accs) + " |")
    v.append("")
    if proposed:
        v += ["## Slugs proposed by the coders, not yet in schema.tsv", ""]
        v += [f"- `{s}` ({ty}): {note}" for s, (ty, note) in sorted(proposed.items())]
    with open(os.path.join(ONTO, "views.md"), "w") as f:
        f.write("\n".join(v) + "\n")
    print("wrote lib/literature/ontology/onto.tsv and views.md")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
