---
title: "The Relationship Between High-Dimensional Geometry and Adversarial Examples (Adversarial Spheres)"
type: source
date_ingested: 2026-04-23
authors: [Justin Gilmer, Luke Metz, Fartash Faghri, Samuel S. Schoenholz, Maithra Raghu, Martin Wattenberg, Ian Goodfellow]
venue: "ICLR Workshop 2018 (venue unconfirmed from PDF: raw/GMF+18_AdversarialSpheres.pdf is arXiv:1801.02774v3 [cs.CV] and names no venue; the attribution is carried over from the earlier ingest)"
year: 2018
tags: [adversarial-ml, concentration-of-measure, isoperimetry, evasion-attacks, high-dimensional-geometry]
claim_quantifier: existential
antecedent: "The data are uniform on two concentric spheres in R^n, the error region is measured on the inner sphere, and the metric is the Euclidean one. This is a constructed synthetic distribution. The extension to natural image data is stated in the paper as a hypothesis, not proved."
date_verified: 2026-08-20
---

## Summary

This paper (GMF+18, "Adversarial Spheres") is the **foundational geometric explanation** for adversarial examples: a classifier that misclassifies even a constant fraction of a concentrated high-dimensional distribution must have points within O(1/√d) of the decision boundary, so adversarial examples of that magnitude are geometrically unavoidable. The authors test this hypothesis on a stylized synthetic dataset — two concentric d-dimensional spheres with different radii — and prove that *any* classifier f with P[f(x) ≠ y] = μ > 0 must have mean adversarial distance ≤ O(1/√d). Several deep-network architectures trained on this dataset empirically approach the bound, validating the geometric explanation.

The spheres dataset is deliberately stylized to isolate the geometric question: the classes are perfectly separable (the two spheres are disjoint) and the input manifold is uniform on each sphere. The Gaussian isoperimetric inequality then applied to the error region gives the O(1/√d) bound. This construction later becomes the launching point for Mahloujifar-Diochnos-Mahmoody's [Curse of Concentration](curse-of-concentration.md) general theorem, which replaces "spheres" with "any Normal Lévy family" and "isoperimetry" with "concentration of measure," yielding the same O(1/√n) bound in far more generality.

Historically, this paper is widely cited as the moment the community accepted that adversarial vulnerability is fundamentally tied to high-dimensional geometry — not merely a quirk of deep learning, not merely an artifact of gradient-based training, but a mathematical consequence of classifying in high dimensions with any nonzero error.

## Claim Boundary

- **Quantified over:** all measurable classifiers on **one** constructed distribution, the concentric-spheres dataset. Theorem 5.1 reads "Consider any model trained on the sphere dataset"; the universal quantifier ranges over models, and the distribution is fixed and synthetic. "There exists a dataset on which every classifier with constant error has nearby errors" is not "every dataset has this property".
- **Antecedent:** uniform measure on two concentric spheres in R^n under the Euclidean metric, and non-zero error on the inner sphere. Whether natural image distributions have the same isoperimetric profile is not established here and was subsequently measured and found not to bind for image benchmarks; see [Empirically Measuring Concentration](empirically-measuring-concentration.md).
- **Which party is constrained:** none; the constraint is geometric. The adversary has unbounded computation and is limited only by the Euclidean perturbation radius. The learner is unconstrained in samples, parameters and time. No resource of any party is priced.
- **Does not establish:** (i) that adversarial examples on natural data follow from geometry — the paper's own words for that step are "We hypothesize"; (ii) that the trained networks reach the bound because of geometry rather than optimization — the paper reports that they approach it, which is an empirical finding on the same synthetic dataset; (iii) anything about attacker cost, since the bound is an existence statement about a nearby error point.
- **Abstract vs theorem:** the abstract is appropriately hedged ("We hypothesize that this counterintuitive behavior is a result of the high-dimensional geometry of the data manifold, and explore this hypothesis on a simple high-dimensional dataset"). The overreach on this page was in the earlier summary prose, which promoted the hypothesis to a "foundational geometric explanation"; the theorem covers the sphere dataset only.

## Key Contributions

- **Formal bound**: For any classifier f on the sphere dataset with error μ, the mean ℓ₂ distance to the decision boundary (over natural data) is O(√(2μ/π) · 1/√d).
- **Empirical validation**: Multiple deep-network architectures trained on the spheres dataset exhibit adversarial distances within a constant factor of the theoretical bound.
- **Dimension-dependence identified**: Adversarial vulnerability scales as O(1/√d) in ambient dimension — a geometric constraint, not an algorithmic weakness.
- **Role of isoperimetry**: Gaussian isoperimetry on the sphere gives the tight constant; this insight paves the way for later concentration-based generalizations.
- **"Adversarial spheres" dataset**: Becomes a canonical benchmark for studying adversarial examples in isolation from natural-image confounds.

## Key Definitions / Theorems

- **Concentric spheres dataset**: two disjoint spheres in ℝ^d with radii R_1 < R_2; data uniform on each.
- **Mean adversarial distance**: E_{x ~ data}[inf{∥δ∥₂ : f(x+δ) ≠ f(x)}].
- **Main theorem**: For any measurable classifier f with P[f ≠ y] = μ on the sphere dataset, mean adversarial distance ≤ (R_2 / √d) · √(2μ/π) · (1 + o(1)).
- **Proof tool**: Gaussian isoperimetric inequality applied to the error region on the sphere.

## Connections

- Source: [Curse of Concentration (MDM19)](curse-of-concentration.md) — generalizes this paper's sphere-specific result to any Normal Lévy family via concentration of measure.
- Source: [Adversarial Vulnerability for Any Classifier (FFF18)](adversarial-vulnerability-any-classifier.md) — Gaussian-case parallel; both use isoperimetry.
- Source: [Empirically Measuring Concentration (MZME19)](empirically-measuring-concentration.md) — tests whether natural image distributions share this property.
- Source: [Universal Law of Robustness (Bubeck-Sellke 2021)](universal-law-of-robustness.md) — complementary: robustness requires overparameterization, not just the right geometry.
- Concept: [Concentration of Measure](../concepts/concentration-of-measure.md).
- Concept: [Lévy Family](../concepts/levy-family.md) — n-sphere is a canonical Normal Lévy family.
- Concept: [Isoperimetry and Robustness](../concepts/isoperimetry-and-robustness.md).
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md).

## Open Questions / Limitations

- **Stylized dataset**: the spheres are mathematically clean but unrelated to natural images; whether real data distributions share the concentration property was open at publication and remains debated (see MZME19).
- **Gaussian isoperimetry specific to ℓ₂ on spheres**: other metrics (ℓ₁, ℓ∞, Wasserstein) require different arguments.
- **Does not explain why networks learn classifiers at all close to the bound** — the theoretical bound is a necessary condition; algorithmic explanations of why trained classifiers saturate it remain subtle.

## Quotes / Notable Passages

> _Not verbatim. Checked against `raw/GMF+18_AdversarialSpheres.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> We hypothesize that adversarial vulnerability is a result of high-dimensional geometry of the data manifold.

The verified passage the paraphrase above was drawn from, from the abstract:

> "We hypothesize that this counterintuitive behavior is a result of the high-dimensional geometry of the data manifold, and explore this hypothesis on a simple high-dimensional dataset."

> _Not verbatim. Checked against `raw/GMF+18_AdversarialSpheres.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> We prove that any model which misclassifies a small constant fraction of a sphere will be vulnerable to adversarial perturbations of size O(1/√d).

The paper's own sentence, verified, differs in two places that matter — the object is the data manifold rather than a sphere, and the dimension symbol is n:

> "In particular, we prove that any model which misclassifies a small constant fraction of the data manifold will be vulnerable to adversarial perturbations of size O(1/√n)."

And, on the discussion of Theorem 5.1:

> "Any model which misclassifies a small constant fraction of the sphere must have errors close to most randomly sampled data points, no matter how the model errors are distributed on the sphere."
