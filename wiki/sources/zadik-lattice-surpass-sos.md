---
title: Lattice-Based Methods Surpass Sum-of-Squares in Clustering
type: source
date_ingested: 2026-04-12
authors: [Ilias Zadik, Min Jae Song, Alexander S. Wein, Joan Bruna]
venue: COLT 2022
year: 2022
tags: [lattice-methods, LLL, sum-of-squares, low-degree-polynomials, clustering, counterexamples, statistical-computational-gaps]
---

## Summary

This paper shows that for certain noiseless/degenerate Gaussian clustering problems, LLL-based (Lenstra-Lenstra-Lovász) lattice reduction algorithms achieve the statistically optimal sample complexity (n = d+1 samples), provably surpassing both low-degree polynomial methods and the sum-of-squares hierarchy, which had been shown to fail up to n = Õ(d²). This is the first example where SoS and LD lower bounds are both active and both *broken* by a poly-time algorithm — a striking counterexample to the low-degree conjecture in structured settings.

The concrete problem is clustering Gaussian mixtures with degenerate covariance Σ = I - uu^T (equivalently: find a planted ±1 hypercube vector in a subspace, or noiseless non-Gaussian component analysis). The LLL-based algorithm recovers both the hidden direction u and the labels x_i from n = d+1 samples, which is information-theoretically optimal. Previous best poly-time bound was n ≫ d². Analogous successes apply to Planted Sparse Vector, hCLWE (noiseless Continuous LWE), and similar "noiseless" statistical problems.

The authors emphasize that LLL's success is brittle: adding inverse-polynomial noise breaks it (consistent with hCLWE being hard under lattice assumptions [Bruna-Regev-Song-Tang 2021]). This highlights noise as the crucial parameter separating LD/SoS-predicted hardness from actual hardness.

## Key Contributions

- LLL-based poly-time algorithm achieving optimal n = d+1 sample complexity for:
  - Planted Hypercube Vector in a Subspace
  - Gaussian Clustering (SNR = ∞)
  - Homogeneous Continuous LWE (hCLWE) with zero noise
- Refutes SoS/LD conjectured hardness (which predicted n = Ω̃(d²) for all three).
- Information-theoretic lower bound of n = d samples (matching up to +1) via separate analysis.
- Conceptual argument: "noiseless" inference problems may systematically escape SoS/LD lower bounds through algebraic lattice structure.

## Key Definitions / Theorems

- **Model (eq 1)**: z_i ~ N(x_i u, I - uu^T), x_i ~ Rademacher, i.i.d.
- **Theorem 1.1**: If n ≥ d+1, an LLL-based poly-time algorithm outputs exactly correct (x_i, u) w.p. 1 - exp(-Ω(d)).
- **Theorem 1.2**: No estimator can recover u from n ≤ d-1 samples (info-theoretic).
- **Theorem 1.3**: n = d+1 is optimal for label recovery up to 1+o(1).
- Brittleness: algorithm fails under inverse-poly noise perturbation (hCLWE hardness kicks in).

## Connections

- [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md) — counterexample
- [Sum-of-Squares Hierarchy](../concepts/sum-of-squares-hierarchy.md) — counterexample
- [LLL Algorithm](../concepts/lll-algorithm.md) — algorithmic tool
- [Continuous LWE](../concepts/continuous-lwe.md) — noisy version is hard
- [Bruna Continuous LWE](bruna-continuous-lwe.md) — hardness of noisy hCLWE
- [Alexander Wein](../entities/alexander-wein.md), [Ilias Zadik](../entities/ilias-zadik.md), [Joan Bruna](../entities/joan-bruna.md)

## Open Questions / Limitations

- LLL approach is brittle to noise: does not "close" statistical-computational gaps in noisy regimes.
- Does LLL break any other conjectured SoS-hard problem in the "noiseless" regime?
- How to formally define "noiseless" problems — the class where LLL might apply.
- Implications for planted clique: PC is not "noiseless" in the relevant sense, so PC hardness likely unaffected.

## Quotes / Notable Passages

> "Our result shows the success of an LLL-based method in a regime where low-degree and SoS lower bounds both suggest computational intractability."

> "All existing algorithms for statistical problems based on LLL suffer from the same lack of robustness. In this sense, there is a strong analogy between LLL and the other known successful polynomial-time method for noiseless inference, namely the Gaussian elimination approach to learning parity."
