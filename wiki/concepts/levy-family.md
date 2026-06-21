---
title: Lévy Family (and Normal Lévy Family)
type: concept
tags: [concentration-of-measure, isoperimetry, probability-theory, adversarial-ml]
---

## Definition

A **Lévy family** [Lévy 1951, Amir-Milman 1985] is a sequence of metric probability spaces {(X_n, d_n, μ_n)}_{n∈ℕ} whose concentration functions α_n(b) = 1 − inf{μ_n(E_b) : μ_n(E) ≥ 1/2} converge to 0 as n → ∞, for every fixed b > 0.

A **Normal Lévy family** is the strong, quantitative version: a sequence where α_n(b) ≤ k₁ · exp(−k₂ · b²/n) for universal constants k₁, k₂ > 0. Equivalently, for any set S with μ_n(S) ≥ ε, at least 1 − δ fraction of points (under μ_n) are within Hamming/metric distance O(√(n · log(1/εδ))) of S.

## Intuition

Lévy families are the metric-probabilistic spaces where **concentration of measure is uniform across dimensions**. A set occupying a constant fraction of the space is "close to almost everywhere" with a sublinear distance that scales as O(√n) in the ambient dimension. This is the quantitative high-dimensional phenomenon that underlies concentration-based adversarial-robustness impossibility results.

## Properties / Theorems

**Canonical examples of Normal Lévy families**:
- **n-dimensional sphere** S^n under geodesic distance (Lévy 1951; the original).
- **Isotropic n-Gaussian** (ℝⁿ, ℓ₂, N(0, I_n)).
- **Boolean hypercube** {0,1}ⁿ under Hamming distance (proof via Harper 1964 / Talagrand 1995).
- **Product probability spaces** under Hamming distance (Amir-Milman 1980, McDiarmid 1989, Talagrand 1995). This includes any i.i.d. product space regardless of marginal distribution.
- **Unit cube** [0,1]ⁿ under Euclidean distance.
- **Special orthogonal group** SO(n) with Haar measure under Hilbert-Schmidt norm.
- **Symmetric group** S_n under the normalized Hamming (transposition) metric with uniform measure.

**Proof techniques** — concentration in Lévy families has been proved via:
- Classical isoperimetric inequalities (sphere, Gaussian).
- Talagrand's isoperimetric inequality for products.
- Martingale methods (Azuma-Hoeffding, McDiarmid).
- Differential geometry / Ricci curvature (sphere, manifolds).
- Eigenvalue bounds on the Laplacian.
- Blowing-up lemma of information theory [Ahlswede–Gács–Körner 1976, Marton 1986].

**Talagrand's product-space bound (Lemma 2.5 of [MDM19])**: For any product measure μ = μ₁ × ... × μ_n and any measurable S, μ(S_b) ≥ 1 − e^{−b²/n}/μ(S) where S_b is the Hamming b-expansion.

## Where It Appears

- [Curse of Concentration](../sources/curse-of-concentration.md) — main theorem applies to any Normal Lévy family, giving O(√n) adversarial-perturbation existence.
- [Computational Concentration of Measure](../sources/computational-concentration-of-measure-etesami.md) — MUCIO algorithm achieves Hamming O(√n) perturbation in poly-time for the Lévy-family product-Hamming case; reduction framework extends to Gaussian ℓ₁.
- [Adversarial Vulnerability for Any Classifier](../sources/adversarial-vulnerability-any-classifier.md) — Fawzi-Fawzi-Fawzi exploit the Gaussian-ℓ₂ Normal-Lévy structure.
- [Empirically Measuring Concentration](../sources/empirically-measuring-concentration.md) — asks whether natural image distributions enjoy Lévy-like concentration; finds the bound is not tight in practice.
- [Complexity-Theoretic Approach to Adversarial ML](../sources/complexity-theoretic-adversarial-ml.md) — umbrella synthesis.

## Related Concepts

- [Concentration of Measure](concentration-of-measure.md) — the general phenomenon; Lévy families are where it is quantitatively strong.
- [Isoperimetry and Robustness](isoperimetry-and-robustness.md) — isoperimetric inequalities give sharper constants than the general concentration argument.
- [Computational Concentration of Measure](computational-concentration-of-measure.md) — algorithmic analog.
- [Evasion Attacks](evasion-attacks.md) — the adversarial application.

## Open Questions

- Are natural image distributions, under perceptually meaningful metrics, (approximately) Lévy? Empirical evidence [MZME19] suggests not at the rate Normal Lévy families demand.
- For Lévy families that are not product-like, is computational concentration still achievable in poly-time? The EMM20 reduction framework answers yes for Gaussian ℓ₁; broader families are open.
- Does the manifold structure of real data violate Normal-Lévy concentration in a way that explains the empirical gap, or is the gap due to algorithmic shortcomings of current robust learners?
