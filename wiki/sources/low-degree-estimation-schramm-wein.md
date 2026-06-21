---
title: "Computational Barriers to Estimation from Low-Degree Polynomials"
type: source
date_ingested: 2026-04-23
authors: [Tselil Schramm, Alexander S. Wein]
venue: Annals of Statistics 2022 (arXiv:2008.02269)
year: 2022
tags: [low-degree-polynomials, statistical-computational-gaps, estimation, recovery, planted-problems]
---

## Summary

This paper (SW22) extends the **low-degree framework** from detection/hypothesis-testing to **estimation and recovery**, providing the first low-degree lower bounds on the best possible mean-squared error achievable by any degree-D polynomial estimator for a broad class of planted "signal-plus-noise" problems. Prior low-degree analysis (Hopkins 2018, BHK+19) focused on *detection* — can a polynomial distinguish planted from null? SW22 shows that *recovery* — can a polynomial estimate the planted signal? — can have its own computational threshold that may differ from the detection threshold, and provides a user-friendly tool for proving it.

The central technical contribution is the **low-degree MMSE lower bound**: for a signal x and observation Y = signal(x) + noise, the best MSE achievable by any degree-D polynomial estimator can be expressed in terms of a low-degree correlator between x and Y. This yields sharp lower bounds for:
- **Planted submatrix** (Gaussian / Wishart)
- **Planted dense subgraph** (detection-recovery gap)
- **Community detection** in stochastic block models

These are the *first* low-degree recovery lower bounds for problems where the associated detection problem is computationally easy — establishing that detection and recovery have genuinely different computational thresholds in some regimes, a phenomenon previously known but not formally justified at the low-degree level.

SW22 is now the standard reference for low-degree hardness of estimation problems and is foundational for subsequent developments (e.g., Ding-Hua-Slot-Steurer 2025 on SBM recovery below Kesten-Stigum).

## Key Contributions

- **Low-degree MMSE bound**: formal lower bound on the MSE of any degree-D polynomial estimator for a planted-signal recovery problem.
- **First low-degree recovery lower bounds** for detection-easy, recovery-hard regimes — formalizes that detection and recovery are genuinely different computational tasks.
- **Sharp applications**: planted submatrix, planted dense subgraph, community detection — gives tight computational thresholds for recovery matching conjectured poly-time algorithms.
- **User-friendly formulation**: reduces recovery lower bounds to computation of second moments of a low-degree correlator, making the framework easy to apply to new problems.
- **Framework extension**: low-degree method now applies to the full detection / recovery / refutation triad, not just detection.

## Key Definitions / Theorems

- **Signal-plus-noise model**: Y = F(x) + noise where x is the planted signal drawn from some prior and F encodes the observation process.
- **Low-degree MMSE**: LDMMSE(D) = inf over degree-D polynomial estimators f : Y ↦ x̂ of E[∥x − f(Y)∥²].
- **Theorem (informal)**: LDMMSE(D) ≥ ‖x‖² − ⟨x · F(x)^{≤D}, F(x)^{≤D}⟩_D / ⟨F(x)^{≤D}, F(x)^{≤D}⟩_D, where ⟨·⟩_D is the degree-D correlator inner product.
- **Planted submatrix recovery**: for k-submatrix in n × n Gaussian, low-degree recovery threshold matches the conjectured poly-time algorithm and is *higher* than the detection threshold.
- **Planted dense subgraph detection-recovery gap**: formalizes a gap where detection is poly-time but recovery provably requires super-polynomial time to any low-degree algorithm.

## Connections

- Source: [Low-Degree Polynomials Survey (Wein 2025)](low-degree-polynomials-survey.md) — the comprehensive synthesis; SW22 is the estimation-extension subsection.
- Source: [SQ Algorithms and Low-Degree Tests Are Almost Equivalent (Brennan et al. 2021)](brennan-sq-lowdegree-equivalence.md) — detection-side equivalence; SW22 extends the framework.
- Source: [Low-Degree Conjecture Implies Sharp SBM Thresholds (Ding et al. 2025)](ding-low-degree-community-detection.md) — applies SW22's machinery to community detection.
- Source: [Detection-Recovery and Detection-Refutation Gaps (Bresler-Jiang 2023)](detection-recovery-refutation-gaps.md) — different technique for the same phenomenon via average-case reductions.
- Source: [Counterexamples to the Low-Degree Conjecture (Holmgren-Wein 2021)](holmgren-counterexamples-low-degree.md) — counterexamples to the detection-side conjecture; SW22 extends to recovery which has different counterexample landscape.
- Concept: [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md).
- Concept: [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md).
- Concept: [Planted Clique](../concepts/planted-clique.md) — recovery version.
- Concept: [Stochastic Block Model](../concepts/stochastic-block-model.md).
- Authors: [Tselil Schramm](../entities/tselil-schramm.md), [Alexander Wein](../entities/alexander-wein.md).

## Open Questions / Limitations

- **Tightness vs. actual computational hardness**: low-degree recovery bounds match conjectured poly-time algorithms for several problems, but this is heuristic; no unconditional computational lower bound is proved.
- **Sensitive to "structureless" assumption**: like detection, recovery low-degree bounds fail for problems with algebraic structure (e.g., lattice-based recovery — see Zadik-Song-Wein-Bruna 2022).
- **Beyond polynomial estimators**: SW22 bounds degree-D polynomial estimators; whether the bounds transfer to arbitrary poly-time algorithms is the low-degree conjecture (heuristic).
- **Tensor PCA and sparse PCA**: recovery bounds proved; whether alternative algorithms can match them remains active.

## Quotes / Notable Passages

> "We give a user-friendly lower bound for the best possible mean squared error achievable by any degree-D polynomial for a large class of 'signal plus noise' problems."

> "These are the first results to establish low-degree hardness of recovery problems for which the associated detection problem is easy."
