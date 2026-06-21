---
title: "Certified Robustness to Adversarial Examples with Differential Privacy (PixelDP)"
type: source
date_ingested: 2026-04-23
authors: [Mathias Lecuyer, Vaggelis Atlidakis, Roxana Geambasu, Daniel Hsu, Suman Jana]
venue: IEEE S&P 2019
year: 2019
tags: [adversarial-ml, certified-robustness, differential-privacy, randomized-smoothing, evasion-attacks]
---

## Summary

This paper (LAGHJ19) introduces **PixelDP**, the first certified adversarial defense that scales to ImageNet-size networks, via a novel connection between **differential privacy** (DP) and **adversarial robustness**. The key conceptual insight is that DP, though traditionally used to hide information about individual records in training data, can be equivalently applied at inference time *over input features* (e.g., pixels): if a classifier is (ε, δ)-DP with respect to a norm-bounded change in input pixels, then its expected scores are stable under such perturbations, yielding a certified robustness radius.

Concretely, PixelDP inserts a Gaussian or Laplace noise layer inside the classifier and leverages two properties of DP: (1) **post-processing** — any function of a DP output remains DP, so noise can be injected anywhere in the pipeline; (2) the newly-proved **expected-output-stability bound** — for a (ε, δ)-DP function with bounded output, |E[A(x)] − E[A(x + α)]| ≤ (e^ε − 1) · E[A(x+α)] + bδ for ∥α∥ ≤ 1. Combining with a standard most-likely-class decision rule yields a certified robustness condition: if the noisy scoring function's top class margin exceeds the DP-induced bound, the prediction is certifiably robust.

PixelDP is the foundational predecessor of [Cohen-Rosenfeld-Kolter 2019 (Randomized Smoothing)](certified-robustness-randomized-smoothing.md); Cohen et al. showed that Gaussian smoothing admits a *tighter* robustness radius via the Neyman-Pearson lemma directly, though both approaches have the same certified-defense structure.

## Key Contributions

- **DP-robustness connection**: First formal reduction linking DP at inference time (over input features) to certified adversarial robustness.
- **First certified ImageNet defense**: PixelDP on the Inception network for ImageNet — scalable in a way no prior certified defense was.
- **Architecture-agnostic**: unlike convex-polytope bounds (Wong-Kolter) which assume ReLU structure, PixelDP works for arbitrary architectures.
- **Expected Output Stability Bound (Lemma 1)**: a general property of DP mechanisms that the paper uses to derive robustness certificates; useful beyond adversarial robustness.
- **Experimental validation**: matches empirical best-effort defenses (Madry adversarial training) on MNIST/CIFAR-10/SVHN while providing formal guarantees.
- **Flexible ℓp support**: PixelDP certificates extend from standard ℓ₂ (Gaussian mechanism) to ℓ₁ (Laplace mechanism) and ℓ∞.

## Key Definitions / Theorems

- **(ε, δ)-PixelDP classifier**: scoring function A satisfies (ε, δ)-DP w.r.t. ℓp norm on input features — i.e., for any x, x' with ∥x − x'∥_p ≤ 1 and any output set S, Pr[A(x) ∈ S] ≤ e^ε Pr[A(x') ∈ S] + δ.
- **Lemma 1 (Expected Output Stability)**: For (ε, δ)-DP function A with bounded output [0, b], for any α ∈ B_p(1): E[A(x)] ≤ e^ε E[A(x+α)] + bδ.
- **Robustness certification condition**: A prediction f(x) = argmax_c y_c(x) is certifiably robust to L-norm-bounded perturbations if the top-class expected score exceeds the second-class expected score after applying the DP-induced scaling by e^{εL}.
- **DP noise layer**: insert Gaussian/Laplace noise at a chosen layer; sensitivity depends on the intermediate computation up to that layer.

## Connections

- Source: [Certified Robustness via Randomized Smoothing (Cohen-Rosenfeld-Kolter 2019)](certified-robustness-randomized-smoothing.md) — the tighter Neyman-Pearson-based version of this paper's idea; supersedes PixelDP's guarantees in the Gaussian-ℓ₂ case.
- Source: [Deep Learning with Differential Privacy (Abadi et al. 2016)](deep-learning-differential-privacy.md) — DP-SGD provides the privacy-at-training-time mechanism; PixelDP is privacy-at-inference-time.
- Source: [Provably Robust SmoothAdv (Salman et al. 2019)](provably-robust-smoothadv.md) — adversarial-training boost to randomized smoothing.
- Source: [Provable Defenses via Convex Polytope (Wong-Kolter 2018)](provable-defenses-convex-polytope.md) — alternative certified defense that does *not* scale to ImageNet.
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md) — the attack surface this paper defends against.
- Concept: [Differential Privacy](../concepts/) — the mechanism.
- Concept: [Certified Robustness](../concepts/) — the goal.

## Open Questions / Limitations

- **Looseness**: The PixelDP bound is loose by a factor determined by the DP composition analysis; Cohen et al. tightened this using Neyman-Pearson directly.
- **Monte Carlo sampling overhead**: certification requires many forward passes to estimate expected scores.
- **ℓ∞ certification is weaker** than ℓ₂ — the Laplace-noise pathway for ℓ∞ does not give as tight a bound as Gaussian-noise for ℓ₂.
- **Certification is for a specific network architecture with specific noise injection**; adapting to new architectures requires re-analysis of sensitivity.
- **Does not compose well** with other defense mechanisms (e.g., adversarial training at inference time).

## Quotes / Notable Passages

> "Our defense, called PixelDP, is based on a novel connection between robustness against adversarial examples and differential privacy, a cryptographically-inspired privacy formalism, that provides a rigorous, generic, and flexible foundation for defense."

> "DP on a small number of pixels in an image guarantees robustness of predictions against adversarial examples that can change up to that number of pixels."

> "Incorporating DP into the learning procedure to increase robustness to adversarial examples is completely different and orthogonal to using DP to preserve the privacy of the training set."
