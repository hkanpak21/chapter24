---
title: "Robustness May Be at Odds with Accuracy"
type: source
date_ingested: 2026-04-23
authors: [Dimitris Tsipras, Shibani Santurkar, Logan Engstrom, Alexander Turner, Aleksander Mądry]
venue: ICLR 2019
year: 2019
tags: [adversarial-ml, robustness, accuracy-tradeoff, representation-learning, evasion-attacks]
---

## Summary

This paper (TSETM19) proves a **formal tradeoff between standard accuracy and adversarial robustness**: there exist natural data distributions on which the optimal standard classifier and the optimal robust classifier have fundamentally different feature representations, and neither can be optimal for both objectives simultaneously. The tradeoff is not a consequence of limited training data or insufficient computation — it **persists even in the infinite-data limit**.

The paper constructs a simple binary classification problem where features split into (i) one highly-correlated-with-label feature (small margin but large predictive value) and (ii) many weakly-correlated features (each with small individual signal). The optimal *standard* classifier leverages all features; the optimal *robust* classifier under a small ℓ_∞ adversary must rely only on the strong feature because the weak features are adversarially flippable. In this setting, robust accuracy upper-bounds standard accuracy by a dimension-dependent gap.

Beyond the formal tradeoff, the paper empirically demonstrates that adversarially trained models on MNIST/CIFAR/Restricted-ImageNet learn **qualitatively different representations**: their learned features are more "human-perceptible" — they align with salient object features, enable clean interpolation between classes (like GANs), and support smooth perceptual transitions. This "unexpected benefit" of robust training — better representation alignment with human perception — has become an influential observation shaping the broader theory of ML representation learning.

## Key Contributions

- **Provable accuracy-robustness tradeoff**: a formal binary classification problem where optimal standard accuracy and optimal robust accuracy cannot be simultaneously achieved even in the infinite-data limit.
- **Tradeoff not due to finite-sample effects**: robust training is not just more sample-hungry (as in Schmidt et al. 2018) — it requires fundamentally different features.
- **Qualitatively different feature representations**: empirical demonstration on MNIST, CIFAR-10, Restricted ImageNet that adversarial training learns features aligning with human perception.
- **Clean class interpolations**: adversarially trained models produce GAN-quality interpolations between classes via gradient ascent.
- **Robustness as regularization (small-data)**: at low training-data regimes, adversarial training improves *standard* accuracy (data augmentation effect) — but this reverses at large-data regimes.
- **Cost of robustness diagram**: standard accuracy vs. training data plot showing when robust training helps vs. hurts.

## Key Definitions / Theorems

- **Standard risk**: R_std(f) = E_{(x,y)~D}[L(x, y; θ)].
- **Adversarial risk**: R_adv(f) = E_{(x,y)~D}[max_{δ ∈ Δ} L(x + δ, y; θ)] where Δ = {δ : ∥δ∥_p ≤ ε} is the perturbation set.
- **Toy model (binary classification)**: y ∼ {±1} uniform; x₁ ∼ N(yμ, 1) with strong correlation; x₂, ..., x_{d+1} ∼ N(ηy, 1) with weak correlation η ≪ 1. The optimal standard classifier averages all features; the optimal ε-ℓ_∞-robust classifier under ε > 2η must discard all weak features.
- **Theorem (informal)**: In this toy model, for any ε > 2η, any classifier with robust accuracy ≥ 1 − p has standard accuracy ≤ 1 − (1−p) · (1 − Φ(η√d)), which is much less than the 1 − Φ(η√d) achievable without the robustness constraint.
- **Empirical representation finding**: gradient-of-loss with respect to input, on adversarially trained models, produces human-perceptible features; on standard-trained models, noise-like features.

## Connections

- Source: [Adversarially Robust Generalization Requires More Data (Schmidt et al. 2018)](../sources/) — complementary result: robust generalization requires more data than standard generalization. This paper shows the tradeoff persists even with infinite data.
- Source: [Universal Law of Robustness (Bubeck-Sellke 2021)](universal-law-of-robustness.md) — complementary: establishes that *overparameterization* is necessary for robustness; this paper argues *different features* are necessary.
- Source: [Empirically Measuring Concentration (MZME19)](empirically-measuring-concentration.md) — concentration bounds suggest there is room for better robust classifiers; this paper identifies a fundamental cost.
- Source: [Certified Robustness via Randomized Smoothing](certified-robustness-randomized-smoothing.md) — accuracy-robustness tradeoff manifests empirically in smoothing's σ parameter.
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md) — the adversary considered.
- Concept: [Robustness-Accuracy Tradeoff](../concepts/) (concept page potentially to create in follow-up lint).
- Concept: [Intrinsic Robustness](../concepts/intrinsic-robustness.md) — Tsipras et al.'s tradeoff is a form of distribution-level intrinsic-robustness ceiling that is not purely geometric (concentration-based).
- Authors: Aleksander Mądry (MIT).

## Open Questions / Limitations

- **Toy model is stylized**: the formal tradeoff is proved for a specific engineered distribution; whether natural distributions exhibit the same precisely is open.
- **Ignores computational aspects**: tradeoff is information-theoretic; no claim about computational robustness.
- **ℓ_∞-specific**: the toy-model construction relies on ℓ_∞ perturbations; ℓ₂ versions have been studied in follow-up work with different findings.
- **"Better representations"** claim is empirical and qualitative — formal characterization of "human-alignment" of features remains open.
- **Not all problems show this tradeoff**: low-signal-to-noise-ratio problems may exhibit it more than high-SNR problems.

## Quotes / Notable Passages

> "We show that there may exist an inherent tension between the goal of adversarial robustness and that of standard generalization. Specifically, training robust models may not only be more resource-consuming, but also lead to a reduction of standard accuracy."

> "At the root of this trade-off is the fact that features learned by the optimal standard and optimal robust classifiers can be fundamentally different and, interestingly, this phenomenon persists even in the limit of infinite data."

> "The representations learned by robust models tend to align better with salient data characteristics and human perception. For instance, the features learnt by robust models yield clean inter-class interpolations, similar to those found by generative adversarial networks."
