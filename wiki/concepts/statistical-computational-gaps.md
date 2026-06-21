---
title: Statistical-Computational Gaps
type: concept
tags: [statistical-computational-gaps, complexity-theory, learning-theory, hardness-reductions, average-case-reductions]
---

## Definition

A **statistical-computational gap** for an inference problem P is a situation where:
- **Statistically**: P is solvable with n = n_stat samples (the information-theoretic minimum)
- **Computationally**: Any polynomial-time algorithm requires n = n_comp >> n_stat samples

The gap is the ratio or difference between n_comp and n_stat. These gaps are typically conjectured (based on failure of restricted algorithm classes and average-case reductions) rather than proven from worst-case complexity assumptions.

## Intuition

In high-dimensional statistics, the amount of data needed to solve a problem *in principle* (information-theoretically) is often far less than the amount needed by any known efficient algorithm. The gap between these thresholds is the statistical-computational gap. Understanding when and why such gaps arise is a central challenge at the intersection of statistics, computer science, and statistical physics.

Two approaches to evidencing gaps:
1. **Failure of algorithm classes**: Show that SQ algorithms, SOS hierarchy, low-degree polynomials all fail below the conjectured computational threshold.
2. **Average-case reductions**: Show that if a polynomial-time algorithm existed for P, it could be used to solve a canonical hard problem (like planted clique).

## Properties / Theorems

**Canonical examples**:
- **Planted Clique**: Statistical threshold k = Ω(log n); conjectured computational threshold k = Θ(√n)
- **Sparse PCA**: Statistical threshold θ = Θ(√(k log d/n)); computational threshold θ = Θ(√(k²/n))
- **Robust Sparse Mean Estimation**: n_stat = Θ(k log d); n_comp = Θ̃(k² log d) (conjectured)
- **Stochastic Block Model**: Statistical threshold at Kesten-Stigum; computational threshold at Kesten-Stigum (no gap for detection, gap for recovery)
- **Tensor PCA**: Gaps at different tensor orders

**Reduction-based evidence** [Brennan & Bresler 2020]: The PC_ρ framework provides the first web of reductions connecting problems with very different structure, providing simultaneous evidence for statistical-computational gaps across: RSME, SBM, hidden partition models, sparse PCA variants, mixtures of linear regressions, tensor PCA, sparse mixtures.

**Low-degree polynomial lower bounds**: Conjectured threshold supported by showing low-degree polynomials fail to distinguish H₀ from H₁ below the computational threshold [BHK+16, Hop18].

**SQ lower bounds**: Statistical Query algorithms fail at the conjectured computational threshold for many problems.

## Where It Appears

- [Reducibility and Statistical-Computational Gaps](../sources/reducibility-statistical-computational-gaps.md) — central topic
- [A Complexity Theoretic Approach to Adversarial ML](../sources/complexity-theoretic-adversarial-ml.md) — sample complexity gap between standard and adversarially robust PAC learning [DMM19]

## Related Concepts

- [Planted Clique](planted-clique.md) — flagship example
- [Secret Leakage Planted Clique](secret-leakage-planted-clique.md)
- [Average-Case Reductions](average-case-reductions.md)
- [Statistical Query Model](statistical-query-model.md)

## Open Questions

- Can statistical-computational gaps be proven from worst-case complexity assumptions?
- Is the PC conjecture the right starting assumption, or should we use stronger/different assumptions?
- Do statistical-computational gaps arise in *all* high-dimensional structured problems, or are there natural exceptions?
- What is the relationship between statistical-computational gaps and the computational hardness assumptions used in cryptography?
