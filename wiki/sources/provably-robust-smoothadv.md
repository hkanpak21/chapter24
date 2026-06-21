---
title: "Provably Robust Deep Learning via Adversarially Trained Smoothed Classifiers (SmoothAdv)"
type: source
date_ingested: 2026-04-23
authors: [Hadi Salman, Greg Yang, Jerry Li, Pengchuan Zhang, Huan Zhang, Ilya Razenshteyn, Sébastien Bubeck]
venue: NeurIPS 2019
year: 2019
tags: [adversarial-ml, certified-robustness, randomized-smoothing, adversarial-training, evasion-attacks]
---

## Summary

This paper (SYLZZ+19, "SmoothAdv") improves [Cohen-Rosenfeld-Kolter 2019](certified-robustness-randomized-smoothing.md)'s randomized smoothing via **adversarial training tailored to the smoothed classifier**. The key insight: when the base classifier f is adversarially trained not on f itself but on the smoothed soft-classifier G (computed over Gaussian noise), the resulting smoothed classifier g has substantially better certified robustness. At ImageNet ℓ₂ radius 0.5, SmoothAdv achieves 56% certified top-1 accuracy versus Cohen et al.'s 49%; on CIFAR-10 the gain is ~16% absolute across all radii, rising to ~22% when combined with pre-training and semi-supervised learning.

The core technical contribution is the **SmoothAdv attack objective** (S): maximize ℓ_CE(G(x'), y) over ∥x' − x∥₂ ≤ ε, where G is the smoothed soft-classifier. This differs from a naive "attack G via attacking f" because the argmax in G's definition is replaced by a soft version, making gradient-based optimization feasible. The paper provides several gradient estimators for (S) and shows that adversarial training with this objective improves the certified accuracy of the resulting smoothed classifier — not merely its empirical robustness.

Along the way, the paper also offers an alternative proof of Cohen et al.'s tight robustness guarantee via a nonlinear Lipschitz property of the smoothed classifier (Appendix A), providing a different (and more concise) perspective on why Gaussian smoothing gives ℓ₂ robustness.

## Key Contributions

- **SmoothAdv attack**: adversarial attack specifically designed for smoothed classifiers, via gradient optimization on the smoothed soft-classifier's cross-entropy loss.
- **State-of-the-art certified ℓ₂ robustness**: 56% certified top-1 on ImageNet at radius 0.5 (7% improvement over Cohen et al.); up to 22% improvement on CIFAR-10 when combined with pre-training.
- **Adversarial training boosts certified (not just empirical) robustness**: when base classifier f is adversarially trained against SmoothAdv, the certified radius of the resulting smoothed g increases.
- **Pre-training + semi-supervised learning compound the gains**: combined approach gives best-in-class results on CIFAR-10.
- **Alternative Neyman-Pearson proof** via Lipschitz property of the smoothed classifier — a cleaner derivation of the Cohen et al. tight bound.

## Key Definitions / Theorems

- **Smoothed soft classifier G(x) = E_{δ~N(0,σ²I)}[F(x+δ)]** where F: ℝ^d → P(Y) is a soft classifier.
- **SmoothAdv objective (S)**: x̂ = argmax_{∥x'−x∥₂ ≤ ε} −log E_δ [(F(x' + δ))_y] — attacks G's soft-classification probability of the true class y.
- **Distinction from naive objective (4)**: attack (4) = argmax E_δ[ℓ_CE(F(x'+δ), y)] finds adversarial examples of F *robust to Gaussian noise*, which is *not* the same as adversarial examples of G. The SmoothAdv objective (S) is the correct form.
- **Gradient estimators**: several Monte-Carlo gradient estimators for (S) under the non-convexity of the log-expectation; choice of estimator matters substantially.
- **Lipschitz proof of smoothed-classifier robustness (Appendix A)**: G has a specific nonlinear Lipschitz property that directly yields the Cohen et al. tight robustness radius.

## Connections

- Source: [Certified Robustness via Randomized Smoothing (Cohen-Rosenfeld-Kolter 2019)](certified-robustness-randomized-smoothing.md) — the baseline this paper improves.
- Source: [Certified Robustness via Differential Privacy (Lecuyer et al. 2019)](certified-robustness-differential-privacy.md) — earlier randomized-smoothing approach via DP.
- Source: [Universal Law of Robustness (Bubeck-Sellke 2021)](universal-law-of-robustness.md) — same Bubeck group; provides the overparameterization-necessary underpinning that smoothing partially sidesteps via noise-averaging.
- Source: [Provable Defenses via Convex Polytope (Wong-Kolter 2018)](provable-defenses-convex-polytope.md) — alternative certified defense for ℓ∞.
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md) — the attack surface defended against.
- Concept: [Certified Robustness](../concepts/) — the goal.
- Author: [Sébastien Bubeck](../entities/sebastien-bubeck.md), [Ilya Razenshteyn](../entities/ilya-razenshteyn.md), [Jerry Li](../entities/jerry-li.md).

## Open Questions / Limitations

- **Subtle non-convexity of the SmoothAdv objective**: different gradient estimators can lead to training instability; "best" estimator is empirically found, not formally derived.
- **ℓ∞ extension** via non-Gaussian noise distributions remains looser than Gaussian-ℓ₂.
- **Computational cost**: adversarial training for smoothed classifiers requires many Monte Carlo samples per step, multiplying training time by ~8-16×.
- **Does not provide new certification methodology** — uses Cohen et al.'s CERTIFY, so improvements come from better base classifiers not better bounds.
- **Pre-training + semi-supervised gains may not generalize to ImageNet** — the compounding is most pronounced on CIFAR-10.

## Quotes / Notable Passages

> "We demonstrate through extensive experimentation that our method consistently outperforms all existing provably ℓ₂-robust classifiers by a significant margin on ImageNet and CIFAR-10, establishing the state-of-the-art for provable ℓ₂-defenses."

> "Directly finding adversarial examples for the smoothed hard classifier g is a somewhat ill-behaved problem because of the argmax, so we instead propose to find adversarial examples for the smoothed soft classifier G."

> "Conceptually, solving (4) corresponds to finding an adversarial example of F that is robust to Gaussian noise. In contrast, (S) corresponds to finding an adversarial example of the smoothed classifier G itself."
