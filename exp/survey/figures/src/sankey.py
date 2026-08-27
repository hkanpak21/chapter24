#!/usr/bin/env python3
"""The survey's Sankey figure, generated from the classification.

Three stages: what a work attacks, which party it bounds, and how tightly. Band
width is the number of works, so the figure says the same thing the tables say
and says it in one view. It deliberately shows less than the tables: the tables
are the full ontology, this is the part that carries the argument.

Regenerate after any change to the classification:
    python3 figures/src/sankey.py
"""
import collections
import csv
import os
import sys

sys.path.insert(0, "/Users/a90/.claude/skills/research/scripts")
import plotstyle as ps
import matplotlib.path as mpath
import matplotlib.patches as mpatches

HERE = os.path.dirname(os.path.abspath(__file__))
SUR = os.path.abspath(os.path.join(HERE, "..", ".."))
TSV = os.path.join(SUR, "notes", "classification.tsv")
OUT = os.path.join(SUR, "figures", "sankey-corpus.pdf")

# Stage 1: what the work attacks. The fourteen family values collapse to four,
# because a Sankey with fourteen sources is a hairball and the argument does not
# need them apart.
TARGET = {
    "membership": "Training data", "attribute": "Training data",
    "reconstruct": "Training data", "distribution": "Training data",
    "evade": "Model behaviour", "inject": "Model behaviour",
    "backdoor": "Model behaviour", "poison": "Model behaviour",
    "extract": "The model", "invert": "The model",
    "forge": "Record of training", "evade audit": "Record of training",
}
S1 = ["Training data", "Model behaviour", "The model", "Record of training",
      "No single attack"]
S2 = ["attacker", "learner", "auditor", "mechanism", "none"]
S2L = {"attacker": "Attacker", "learner": "Learner", "auditor": "Auditor",
       "mechanism": "Mechanism", "none": "No party bounded"}
TIGHT = {
    "exponent": "Relative to honest work",
    "class": "Algorithm class",
    "poly": "Polynomial time", "quasi-poly": "Polynomial time",
    "conditional": "Polynomial time",
    "budget": "Numeric budget",
    "measured": "Measured only", "unstated": "Unstated",
}
S3 = ["Relative to honest work", "Algorithm class", "Polynomial time",
      "Numeric budget", "Measured only", "Unstated"]

# One colour per stage-2 party, carried through both ribbon sets so the eye can
# follow a party across the whole figure. Colour means party and nothing else.
COL = {"attacker": ps.C[1], "learner": ps.C[0], "auditor": ps.C[2],
       "mechanism": ps.C[3], "none": "#9AA0A6"}


def load():
    rows = list(csv.DictReader(open(TSV, encoding="utf-8"), delimiter="\t"))
    out = []
    for r in rows:
        s1 = TARGET.get(r["family"], "No single attack")
        s2 = r["party"] if r["party"] in S2 else "none"
        s3 = TIGHT.get(r["tightness"], "Unstated")
        out.append((s1, s2, s3))
    return out


def stack(labels, counts, gap, total_h):
    """y positions for a column of labelled blocks, top down."""
    n = sum(1 for l in labels if counts.get(l))
    span = total_h - gap * max(n - 1, 0)
    pos, y = {}, 0.0
    for l in labels:
        c = counts.get(l, 0)
        if not c:
            continue
        h = span * c / sum(counts.values())
        pos[l] = (y, h)
        y += h + gap
    return pos


def ribbon(ax, x0, y0, x1, y1, h0, h1, color, alpha=0.55):
    P = mpath.Path
    dx = (x1 - x0) * 0.5
    verts = [(x0, y0), (x0 + dx, y0), (x1 - dx, y1), (x1, y1),
             (x1, y1 + h1), (x1 - dx, y1 + h1), (x0 + dx, y0 + h0), (x0, y0 + h0),
             (x0, y0)]
    codes = [P.MOVETO, P.CURVE4, P.CURVE4, P.CURVE4,
             P.LINETO, P.CURVE4, P.CURVE4, P.CURVE4, P.CLOSEPOLY]
    ax.add_patch(mpatches.PathPatch(P(verts, codes), facecolor=color,
                                    edgecolor="none", alpha=alpha, lw=0))


def main():
    ps.use(os.path.join(SUR, ".paper-meta.yml"))
    data = load()
    N = len(data)
    c1 = collections.Counter(d[0] for d in data)
    c2 = collections.Counter(d[1] for d in data)
    c3 = collections.Counter(d[2] for d in data)

    fig, ax = ps.figure(width="text", ratio=0.46)
    H, GAP, BW = 1.0, 0.022, 0.028
    X = [0.0, 0.46, 0.92]
    p1 = stack(S1, c1, GAP, H)
    p2 = stack(S2, c2, GAP, H)
    p3 = stack(S3, c3, GAP, H)

    for pos, labs, x, lab_of in ((p1, S1, X[0], lambda l: l),
                                 (p2, S2, X[1], lambda l: S2L[l]),
                                 (p3, S3, X[2], lambda l: l)):
        for l in labs:
            if l not in pos:
                continue
            y, h = pos[l]
            col = COL[l] if l in COL else "#5F6368"
            ax.add_patch(mpatches.Rectangle((x, y), BW, h, facecolor=col,
                                            edgecolor="none"))

    # stage 1 to stage 2, then stage 2 to stage 3
    off1 = {l: 0.0 for l in p1}
    off2i = {l: 0.0 for l in p2}
    for a in S1:
        if a not in p1:
            continue
        for b in S2:
            n = sum(1 for d in data if d[0] == a and d[1] == b)
            if not n:
                continue
            h = p1[a][1] * n / c1[a]
            h2 = p2[b][1] * n / c2[b]
            ribbon(ax, X[0] + BW, p1[a][0] + off1[a], X[1], p2[b][0] + off2i[b],
                   h, h2, COL[b])
            off1[a] += h
            off2i[b] += h2
    off2o = {l: 0.0 for l in p2}
    off3 = {l: 0.0 for l in p3}
    for b in S2:
        if b not in p2:
            continue
        for c in S3:
            n = sum(1 for d in data if d[1] == b and d[2] == c)
            if not n:
                continue
            h = p2[b][1] * n / c2[b]
            h3 = p3[c][1] * n / c3[c]
            ribbon(ax, X[1] + BW, p2[b][0] + off2o[b], X[2], p3[c][0] + off3[c],
                   h, h3, COL[b])
            off2o[b] += h
            off3[c] += h3

    for pos, labs, x, lab_of, ha in (
            (p1, S1, X[0], lambda l: l, "right"),
            (p2, S2, X[1] + BW / 2, lambda l: S2L[l], "center"),
            (p3, S3, X[2] + BW, lambda l: l, "left")):
        for l in labs:
            if l not in pos:
                continue
            y, h = pos[l]
            cnt = (c1 if pos is p1 else c2 if pos is p2 else c3)[l]
            txt = "%s (%d)" % (lab_of(l), cnt)
            if ha == "center":
                ax.text(x, y + h / 2, txt, ha="center", va="center",
                        fontsize=ps._META["caption_pt"], zorder=5,
                        bbox=dict(boxstyle="round,pad=0.18", facecolor="white",
                                  edgecolor="none", alpha=0.92))
            else:
                ax.text(x - 0.012 if ha == "right" else x + 0.012,
                        y + h / 2, txt, ha=ha, va="center",
                        fontsize=ps._META["caption_pt"])

    for x, t in ((X[0] + BW / 2, "What is attacked"),
                 (X[1] + BW / 2, "Which party is bounded"),
                 (X[2] + BW / 2, "How tightly")):
        ax.text(x, -0.045, t, ha="center", va="top",
                fontsize=ps._META["caption_pt"], style="italic")

    ax.set_xlim(-0.235, 1.235)
    ax.set_ylim(-0.09, 1.09)
    ax.invert_yaxis()
    ax.axis("off")
    ps.save(fig, OUT)
    sys.stderr.write("N = %d\n" % N)


if __name__ == "__main__":
    main()
