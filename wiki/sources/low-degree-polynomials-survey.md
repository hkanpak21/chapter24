---
title: "Computational Complexity of Statistics: New Insights from Low-Degree Polynomials"
type: source
date_ingested: 2026-04-12
authors: [Alexander S. Wein]
venue: "arXiv:2506.10748 (June 2025) — Survey"
year: 2025
tags: [statistical-computational-gaps, complexity-theory, low-degree-polynomials, statistical-query, hardness-reductions, planted-clique]
---

## Summary

A 50-page survey by Alexander Wein on the low-degree polynomial framework for understanding statistical-computational tradeoffs. The survey covers: (1) the low-degree conjecture and its evidence base; (2) applications to detection, recovery, and estimation problems; (3) formal connections to the SQ model and the SOS hierarchy; (4) known counterexamples and limitations; (5) open problems. As of June 2025 this is the authoritative survey of the low-degree framework.

The key thesis: low-degree polynomials predict computational thresholds for "structureless" planted problems, but fail for problems with algebraic structure (lattice methods, anti-concentration algorithms). The framework is best understood as evidence for hardness of a specific class of problems, not a universal theory of computational complexity.

## Key Contributions (of the framework, as surveyed)

- **Low-degree likelihood ratio (LDLR)**: For hypothesis testing H₀ vs H₁, the degree-D likelihood ratio L^{≤D} = E_{H₁}[f(x)] / E_{H₀}[f(x)] measures "low-degree distinguishability." The conjecture: if ‖L^{≤D}‖ = O(1) for D = Ω(log n), no poly-time algorithm solves the testing problem.
- **SQ ≈ Low-degree equivalence** (Brennan, Bresler, Hopkins, Li, Schramm, COLT 2021): Under mild conditions, the SQ complexity and low-degree complexity of hypothesis testing problems are essentially equivalent. This is a formal theorem (not just a conjecture).
- **Extension to estimation and recovery**: Low-degree lower bounds now exist for estimation (low-degree MMSE) and optimization, not just hypothesis testing.
- **Applications**: Community detection, sparse PCA, spiked tensor models, planted clique, random CSPs, robust sparse mean estimation — tight thresholds via low-degree framework.

## Known Counterexamples (crucial for our research)

1. **Zadik, Song, Wein, Bruna (COLT 2022)**: Lattice-based algorithms for clustering Gaussian mixtures with degenerate covariance succeed above the low-degree threshold. Low-degree polynomials fail to predict the correct computational threshold when algebraic structure (lattice rounding) is exploitable. *This is the most important known counterexample.*

2. **Robust subspace recovery (arXiv 2603.02594, 2026)**: Polynomial-time solvable but low-degree method fails even up to degree n^{Ω(1)}, because the algorithm exploits anti-concentration properties invisible to low-degree polynomials.

3. **Holmgren and Wein (ITCS 2021)**: Refuted the original formulation of the low-degree conjecture but noted a simple modification avoids their construction.

**Emerging consensus**: The low-degree framework accurately predicts hardness for problems without hidden algebraic or anti-concentration structure — "structureless" problems. It fails when efficient algorithms can exploit algebraic structure (lattices, finite fields, anti-concentration).

## Key Definitions / Theorems

**Low-degree conjecture (informal)**: For natural hypothesis testing problems, no polynomial-time algorithm distinguishes H₀ from H₁ below the threshold where degree-O(log n) polynomials can distinguish them.

**Low-degree complexity of a problem**: The minimum degree D such that ‖L^{≤D}‖² = ω(1), where L^{≤D} is the low-degree likelihood ratio.

**SQ-LD equivalence theorem** (Brennan et al. 2021): For hypothesis testing problems satisfying mild regularity conditions, the minimum SQ complexity m_SQ and the low-degree complexity D satisfy: D = Θ(log(m_SQ)).

**Low-degree MMSE** (Schramm and Wein, Ann. Statist. 2022): For estimation problems, the performance of the best degree-D polynomial estimator provides a lower bound on the performance of any polynomial-time estimator. Extends the framework from detection to recovery.

## Connections

- [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md) — low-degree framework is a primary tool for evidencing gaps
- [Statistical Query Model](../concepts/statistical-query-model.md) — formally equivalent to low-degree under mild conditions
- [Planted Clique](../concepts/planted-clique.md) — primary test case for the framework
- [Secret Leakage Planted Clique](../concepts/secret-leakage-planted-clique.md) — low-degree lower bounds for PC_ρ support the Brennan-Bresler conjecture
- [Average-Case Reductions](../concepts/average-case-reductions.md)
- [Alexander Wein](../entities/alexander-wein.md)

## Open Questions

- Precisely characterize the class of problems for which the low-degree conjecture holds — what structural property separates "structureless" from "algebraically structured"?
- Can the low-degree framework be extended to handle algebraic structure by enriching the polynomial class (e.g., polynomials over finite fields)?
- Does low-degree hardness imply actual computational hardness for any natural problem (would be a formal theorem, not just a conjecture)?
- Connection to circuit complexity: do low-degree lower bounds imply AC⁰ or TC⁰ lower bounds?
