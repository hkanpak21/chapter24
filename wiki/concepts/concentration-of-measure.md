---
title: Concentration of Measure
type: concept
tags: [concentration-of-measure, adversarial-ml, evasion-attacks, complexity-theory]
---

## Definition

For a metric probability space (X, d, μ), the concentration of measure phenomenon states: for any subset A ⊆ X with μ(A) ≥ c > 0, almost every point x sampled from μ has sub-linear distance from A. Formally, for the ε-neighborhood A_ε = {x : d(x,A) ≤ ε}, we have μ(A_ε) → 1 as the dimension grows, even for sub-linear ε.

Equivalently: for any 1-Lipschitz function f on X, f is highly concentrated around its median.

## Intuition

High-dimensional geometry is counterintuitive. A set that occupies a constant fraction of the measure is "close to everywhere" — most of the mass of the space is within small distance of it. This is the same phenomenon underlying the curse of dimensionality, but it has a specific implication for robustness: if a classifier's error region has nontrivial measure, then most correct-classified points are close to the error region.

## Properties / Theorems

**Adversarial robustness upper bound** [MDM19]: If the metric probability space (X, d, μ) satisfies a concentration inequality, and a classifier h has error rate α > 0 on μ, then for most instances x correctly classified by h, there exists a perturbation δ with d(x, x+δ) = o(dimension) such that h(x+δ) ≠ h(x).

**Consequence**: For any classifier with constant error rate on a concentrated space, there is an information-theoretic adversary with sub-linear perturbation budget who can flip almost any instance's classification. This is *independent of the classifier architecture*.

**Key examples of concentrated spaces**:
- Product distributions under Hamming distance (uniform hypercube)
- Gaussian distributions under Euclidean distance
- Product of unit spheres under Euclidean/geodesic distance
- All Lévy families

**Bound on hypercube** [DMM18]: For any classifier with error rate ≥ 0.01 on `{0,1}^n`, there is an adversary changing `O(√n)` bits who raises the error to almost 1.

## Where It Appears

- [A Complexity Theoretic Approach to Adversarial ML](../sources/complexity-theoretic-adversarial-ml.md) — central tool for evasion attack lower bounds
- [Curse of Concentration (MDM19)](../sources/curse-of-concentration.md) — general theorem: any concentrated space + Ω(1) error ⇒ adversary drives risk to ≈1
- [Adversarial Vulnerability for Any Classifier (FFF18)](../sources/adversarial-vulnerability-any-classifier.md) — Gaussian isoperimetry version under smooth generative models
- [Empirically Measuring Concentration (MZME19)](../sources/empirically-measuring-concentration.md) — empirical bounds on real data; finds gap between concentration upper bound and SOTA classifiers
- [Computational Concentration of Measure (EMM20)](../sources/computational-concentration-of-measure-etesami.md) — polynomial-time version matching IT bounds
- [Reducibility and Statistical-Computational Gaps](../sources/reducibility-statistical-computational-gaps.md) — statistical-computational gaps can be seen as a related phenomenon (statistical feasibility vs. computational hardness)

## Related Concepts

- [Computational Concentration of Measure](computational-concentration-of-measure.md) — polynomial-time version
- [Evasion Attacks](evasion-attacks.md) — concentration gives lower bounds on adversary power
- [Intrinsic Robustness](intrinsic-robustness.md) — concentration upper-bounds it
- [Isoperimetry and Robustness](isoperimetry-and-robustness.md) — sharper version using isoperimetric inequalities
- [Statistical-Computational Gaps](statistical-computational-gaps.md)

## Open Questions

- Does concentration of measure fully explain adversarial examples in practice? Empirical evidence [MZME19] suggests it does not — the gap between concentration-based upper bounds and observed robustness is sometimes larger than predicted.
- Is there a characterization of when computational hardness can help close the concentration-implied robustness gap?
