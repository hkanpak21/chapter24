---
title: Intrinsic Robustness
type: concept
tags: [adversarial-ml, concentration-of-measure, evasion-attacks, robustness, empirical]
---

## Definition

**Intrinsic robustness** of a distribution μ under perturbation budget b is the maximum achievable adversarial accuracy of any classifier on μ — i.e., 1 − inf_h Risk_b(h). It is a property of (X, d, μ) alone, independent of classifier choice.

For concentrated spaces, intrinsic robustness is upper-bounded by the concentration function: if α(b) is the concentration function, any classifier with error ≥ 1/2 has adversarial risk ≥ 1 − α(b), so intrinsic robustness ≤ α(b).

## Intuition

Adversarial vulnerability has two possible sources:
1. **Intrinsic** — the data distribution geometry forces vulnerability on any classifier (concentration argument).
2. **Classifier-induced** — the specific hypothesis / training procedure introduces vulnerability beyond what geometry demands.

Intrinsic robustness quantifies the first component: it is the "best any classifier could hope for" given only distributional geometry.

## Properties / Theorems

**Concentration upper bound** [MDM19, FFF18, Gilmer+18]: For concentrated metric probability spaces, intrinsic robustness under b-perturbation is at most α(b) ≤ exp(−Ω(b²/n)) for normal Lévy families.

**Empirical measurement** [MZME19]: Algorithmic estimators lower-bound the intrinsic robustness of MNIST / CIFAR-10 under standard ℓ_∞ / ℓ₂ budgets. The measured intrinsic robustness is *substantially higher* than SOTA classifier robustness, implying most observed adversarial vulnerability is classifier-induced, not intrinsic.

**Computational intrinsic robustness**: The poly-time analog — best adversarial accuracy of any efficient classifier — can be strictly lower than information-theoretic intrinsic robustness when crypto hardness is present ([BLPR19](../sources/adversarial-examples-computational-constraints.md), [GJMM20]).

## Where It Appears

- [Empirically Measuring Concentration](../sources/empirically-measuring-concentration.md) — empirical estimation + gap demonstration
- [Curse of Concentration](../sources/curse-of-concentration.md) — theoretical upper bounds
- [Adversarial Vulnerability for Any Classifier](../sources/adversarial-vulnerability-any-classifier.md) — classifier-agnostic bound under smooth generative models
- [Universal Law of Robustness](../sources/universal-law-of-robustness.md) — related overparameterization angle

## Related Concepts

- [Concentration of Measure](concentration-of-measure.md) — provides upper bounds on intrinsic robustness
- [Computational Concentration of Measure](computational-concentration-of-measure.md) — computational analog
- [Evasion Attacks](evasion-attacks.md)

## Open Questions

- Tight estimators for intrinsic robustness on high-dimensional natural distributions.
- If concentration does not bind, what is the binding constraint on intrinsic robustness? Candidates: local manifold curvature, ground-truth Lipschitz constant.
- Relationship between intrinsic robustness and sample complexity: does higher intrinsic robustness imply lower robust sample complexity?
