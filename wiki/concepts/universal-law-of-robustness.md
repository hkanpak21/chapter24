---
title: Universal Law of Robustness
type: concept
tags: [robustness, adversarial-ml, overparameterization, isoperimetry, concentration-of-measure, sample-complexity]
---

## Definition

The **Universal Law of Robustness** (Bubeck and Sellke, NeurIPS 2021): For any smoothly parameterized function class with polynomial-magnitude weights, and any covariate distribution satisfying an **isoperimetry condition** in R^d, smoothly interpolating n data points requires at least **p ≥ Ω(nd) parameters**.

Equivalently: a model with fewer than nd parameters cannot simultaneously (1) interpolate the training data and (2) be globally Lipschitz-smooth (and hence adversarially robust) on the data distribution.

## Intuition

Standard interpolation (e.g., nearest-neighbor, 1-NN) only requires n parameters. But smooth interpolation — where nearby inputs get similar outputs — is much harder in high dimensions. The law says you need d times more parameters. Since d is the ambient data dimension (e.g., d = 150K for ImageNet images), this is a massive requirement. Current large models are just approaching this threshold, explaining why scaling helps robustness empirically.

## Properties / Theorems

**Main theorem** (Bubeck-Sellke): For smoothly parametrized F_θ with θ ∈ R^p, polynomial weights, and isoperimetric distribution μ in R^d:
`if p < cnd then no θ achieves smooth interpolation of n i.i.d. points from μ`

**Isoperimetry**: A distribution μ satisfies isoperimetry if it concentrates well — for any set A with μ(A) ≥ 1/2, the ε-neighborhood A_ε has measure approaching 1. Gaussians, product distributions, and many natural distributions satisfy this.

**Smooth interpolation**: Function f is a smooth interpolator if f(xᵢ) = yᵢ for all training points and f has bounded Lipschitz constant (or bounded Jacobian spectral norm).

**ImageNet implication**: n ≈ 1.2M, d ≈ 150K → p ≥ ~10^{11} parameters required for robust smooth interpolation. Models with 10^{10} parameters (e.g., GPT-3) are still below this; models with 10^{12} parameters (frontier models) are approaching it.

**Architecture-agnostic**: The lower bound holds for MLPs, kernel machines, random features, and any other smoothly parameterized class.

**Relationship to concentration of measure**: Isoperimetry is the same condition that drives [concentration of measure](concentration-of-measure.md). Both phenomena are expressions of the same high-dimensional geometry. This connects the universal law to the Mahloujifar et al. adversarial robustness bounds.

## Where It Appears

- [Universal Law of Robustness](../sources/universal-law-of-robustness.md) — proved here
- Motivates the empirical connection between model size and robustness

## Related Concepts

- [Concentration of Measure](concentration-of-measure.md) — isoperimetry underlies both; the two laws are dual views of the same geometry
- [Evasion Attacks](evasion-attacks.md) — the law explains why insufficient parameterization leads to adversarial vulnerability
- [Computational Concentration of Measure](computational-concentration-of-measure.md)

## Open Questions

- Does the nd lower bound hold for non-smooth activations (ReLU networks)? "A Law of Robustness beyond Isoperimetry" (arXiv:2202.11592) extends to some non-isoperimetric distributions but not ReLU.
- Is the nd bound tight — are nd parameters sufficient for robust interpolation?
- Extensions to non-Euclidean data (text, graphs)?
- Can the law be made distribution-free (no isoperimetry assumption)?
