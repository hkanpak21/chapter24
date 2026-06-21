---
title: Sum-of-Squares Hierarchy
type: concept
tags: [sum-of-squares, complexity-theory, semidefinite-programming, lower-bounds, statistical-computational-gaps]
---

## Definition

The **Sum-of-Squares (SoS) hierarchy** [Shor 1987, Parrilo 2000, Lasserre 2001] is a family of semidefinite programming (SDP) relaxations indexed by a degree parameter d. The degree-d SoS SDP can be solved in time n^{O(d)} and upper bounds the optimum of any polynomial optimization problem by optimizing over "degree-d pseudo-distributions": linear functionals Ẽ on polynomials of degree ≤ d satisfying linearity, normalization (Ẽ[1]=1), and positivity (Ẽ[p²] ≥ 0 for deg p ≤ d/2).

For **hypothesis testing / certification** problems (e.g., "does this random graph contain a k-clique?"), SoS lower bounds are typically proved by constructing a pseudo-distribution on the null instance that "looks like" a planted-case posterior up to degree d — certifying that SoS cannot distinguish the two.

## Intuition

SoS is among the most powerful known families of efficiently-solvable convex relaxations. It subsumes LP relaxations, Lovász-Schrijver, spectral methods, and many known ML algorithms. When SoS at moderate degree fails on a problem, it is strong evidence (though not unconditional) of polynomial-time hardness.

Degree corresponds roughly to runtime: degree d → n^{O(d)} time. Low degree (d = O(1)) captures spectral/basic SDP algorithms; degree O(log n) captures quasi-polynomial algorithms.

## Properties / Theorems

- **Planted Clique SoS lower bound** [Barak-Hopkins-Kelner-Kothari-Moitra-Potechin 2016]: degree-d SoS has integrality gap n^{1/2 - c(d/log n)^{1/2}} for any d = o(log n) — tightly matching the √n barrier.
- **Pseudo-calibration** framework [BHK+16]: constructs SoS pseudo-distributions by making them indistinguishable from the true posterior under low-degree tests.
- **SoS ↔ Low-Degree equivalence (heuristic)**: SoS at degree d and low-degree polynomials at degree d are believed to have essentially the same power; formalized in [HKP+17] for spectral algorithms.
- **Counterexamples to SoS / LD hardness**: [Zadik-Song-Wein-Bruna 2022] — LLL solves clustering / planted hypercube problems where SoS provably fails.
- **Applications**: SoS lower bounds established for planted clique, sparse PCA, tensor PCA, random CSPs, community detection.

## Where It Appears

- [Barak et al. SoS Lower Bound](../sources/barak-sos-lower-bound-planted-clique.md) — near-tight PC SoS lower bound
- [Lattice Methods Surpass SoS](../sources/zadik-lattice-surpass-sos.md) — SoS counterexample
- [Low-Degree Polynomials Survey](../sources/low-degree-polynomials-survey.md) — SoS / LD connection
- [Reducibility and Statistical-Computational Gaps](../sources/reducibility-statistical-computational-gaps.md)

## Related Concepts

- [Pseudo-Calibration](pseudo-calibration.md)
- [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md)
- [Statistical Query Model](statistical-query-model.md)
- [Planted Clique](planted-clique.md)
- [Statistical-Computational Gaps](statistical-computational-gaps.md)

## Open Questions

- Tight characterization of SoS ↔ LD relationship (beyond heuristic).
- Can SoS achieve non-trivial *upper bounds* (algorithms) beating spectral methods for natural problems?
- How to handle problems with algebraic structure that LLL solves but SoS does not?
