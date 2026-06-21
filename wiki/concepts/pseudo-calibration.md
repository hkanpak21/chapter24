---
title: Pseudo-Calibration
type: concept
tags: [sum-of-squares, lower-bounds, planted-clique, statistical-computational-gaps, bayesian]
---

## Definition

**Pseudo-calibration** [Barak-Hopkins-Kelner-Kothari-Moitra-Potechin 2016] is a framework for constructing sum-of-squares (SoS) pseudo-distributions for planted problems. Given a planted distribution (G, x) ~ G(n, 1/2, ω) and null distribution G ~ G(n, 1/2), the pseudo-calibration condition requires the pseudo-expectation Ẽ_G to satisfy:

E_{G ~ G(n,1/2)} [Ẽ_G f_G] = E_{(G,x) ~ G(n,1/2,ω)} [f(G, x)]

for every "simple" (low-degree in both G and x) function f. That is, the pseudo-expectation operator, viewed as a function of G, must match the true Bayesian conditional expectation on low-degree Fourier coefficients.

## Intuition

Pseudo-calibration takes a **computational Bayesian** perspective: a polynomially-bounded observer cannot compute the true Bayesian posterior E[f(G,x) | G], but can compute a low-degree approximation Ẽ[f]. Pseudo-calibration specifies that this approximation must be exactly right in expectation on all low-degree functions of G. This almost uniquely determines the pseudo-distribution.

The key insight: previous SoS lower bounds for PC required an "ansatz" or creative guess for the pseudo-distribution. Pseudo-calibration removes the guesswork by demanding consistency with the Bayesian prior at the level of low-degree moments — a principled, maximum-entropy-style choice.

## Properties / Theorems

- Pseudo-calibration implies satisfaction of **strong constraints** (e.g., Ẽ x_S = 0 for S not a clique) automatically.
- Pseudo-calibration implies satisfaction of **weak global constraints** (unlike FK03b pseudo-distribution).
- For planted clique, the pseudo-calibrated pseudo-distribution yields the near-tight SoS lower bound n^{1/2 - o(1)} at degree O(log n) [BHK+16].
- Proving positivity (Ẽ[p²] ≥ 0) of the pseudo-calibrated distribution is the main technical challenge; requires showing a large random moment matrix is PSD.
- Connects SoS to **low-degree polynomials**: the pseudo-calibrated distribution is essentially a low-degree polynomial in G.

## Where It Appears

- [Barak et al. SoS Lower Bound](../sources/barak-sos-lower-bound-planted-clique.md) — where pseudo-calibration was introduced
- [Low-Degree Polynomials Survey](../sources/low-degree-polynomials-survey.md) — discusses SoS ↔ LD via pseudo-calibration

## Related Concepts

- [Sum-of-Squares Hierarchy](sum-of-squares-hierarchy.md)
- [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md)
- [Planted Clique](planted-clique.md)

## Open Questions

- Extension of pseudo-calibration to other planted problems beyond PC (partially done for sparse PCA, SBM).
- Tight connection between pseudo-calibration and low-degree likelihood ratio: are they formally equivalent?
- Does pseudo-calibration yield *upper bounds* (algorithms) — can it suggest when SoS beats other methods?
