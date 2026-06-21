---
title: Stochastic Block Model (SBM)
type: concept
tags: [stochastic-block-model, community-detection, kesten-stigum, statistical-computational-gaps, graph-learning]
---

## Definition

The **Stochastic Block Model** is a canonical random graph model for community detection. The **symmetric k-SBM** SSBM(n, d/n, ε, k):
1. Assign each of n vertices a label uniformly at random from [k].
2. Place an edge between vertices with same label with probability (1 + (k-1)ε/k)(d/n); different labels with probability (1 - ε/k)(d/n).

Parameters: n = vertices, d = average degree, ε = bias, k = number of communities. When ε = 0, reduces to Erdős-Rényi G(n, d/n).

**Problems**: Given the graph, (a) **detection**: distinguish SBM from Erdős-Rényi; (b) **weak recovery**: output labels with constant correlation to truth; (c) **exact recovery** (dense regime); (d) **learning**: estimate parameters ε, d, k.

## Intuition

SBM is the canonical model for community structure in networks. The key phenomenon: sharp **Kesten-Stigum (KS) threshold** ε²d = k² separating computationally tractable from (conjecturally) hard regimes.

## Properties / Theorems

- **Kesten-Stigum threshold**: ε²d = k². Above this, poly-time algorithms achieve weak recovery [Massoulié 2014, Abbe-Sandon 2015]. Below, no poly-time algorithm is known.
- **Exponential-time algorithms** succeed above an information-theoretic threshold below KS (for k ≥ 5) [BMNN16] — the **conjectured statistical-computational gap**.
- **LD lower bounds** [Hop18, BBK+21a]: below KS, no low-degree polynomial achieves detection with probability 1 - o(1).
- **Weak recovery LD bounds** [Ding-Hua-Slot-Steurer 2025]: below KS, no LD algorithm achieves constant-probability weak recovery (assuming extended LD conjecture).
- **No reductions from PC to SBM with sharp thresholds** — reason: PC has no constant-sharp threshold while SBM does.

## Where It Appears

- [Ding Low-Degree Community Detection](../sources/ding-low-degree-community-detection.md)
- [Reducibility and Statistical-Computational Gaps](../sources/reducibility-statistical-computational-gaps.md) — PC_ρ reductions to SBM variants
- [Detection-Recovery-Refutation Gaps](../sources/detection-recovery-refutation-gaps.md)

## Related Concepts

- [Kesten-Stigum Threshold](kesten-stigum-threshold.md)
- [Planted Clique](planted-clique.md)
- [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md)
- [Statistical-Computational Gaps](statistical-computational-gaps.md)

## Open Questions

- Unconditional computational lower bounds below KS.
- Tight characterization of recovery vs. detection gaps for k ≥ 5.
- Extension to dense / non-symmetric / labeled SBMs.
