---
title: "Certified Adversarial Robustness via Randomized Smoothing"
type: source
date_ingested: 2026-04-23
authors: [Jeremy Cohen, Elan Rosenfeld, J. Zico Kolter]
venue: ICML 2019
year: 2019
tags: [adversarial-ml, certified-robustness, randomized-smoothing, differential-privacy, robustness]
---

## Summary

This paper (CRK19) establishes **randomized smoothing** as the first certified adversarial defense that scales to ImageNet. Given any base classifier f : ℝ^d → Y (including arbitrary deep networks), the smoothed classifier g(x) = argmax_c Pr_{δ∼N(0,σ²I)} [f(x+δ) = c] is provably robust to ℓ₂-bounded adversarial perturbations. The paper's main technical contribution is a **tight robustness radius**: if the top class has smoothed probability at least p_A and the runner-up has at most p_B, then g is provably constant on the ℓ₂ ball of radius R = (σ/2) · (Φ⁻¹(p_A) − Φ⁻¹(p_B)), via the **Neyman-Pearson lemma**. This tight bound improves on the looser randomized-smoothing bounds of Lecuyer et al. (PixelDP) and Li et al.

The certification procedure uses Monte Carlo sampling to estimate p_A, p_B with high-probability lower/upper confidence bounds, making g practically certifiable. On ImageNet, randomized smoothing achieves 49% certified top-1 accuracy under ℓ₂ perturbations of norm ≤ 0.5; no competing certified defense has demonstrated any non-trivial accuracy at ImageNet scale. On CIFAR-10 and smaller datasets where alternatives are viable, smoothing still wins on certified accuracy.

The paper also introduces adversarial-training-for-smoothed-classifiers as an empirical improvement and lays the foundation for the [Salman et al. SmoothAdv](provably-robust-smoothadv.md) follow-up which tightens this further via adapted attacks.

## Key Contributions

- **Tight robustness radius via Neyman-Pearson**: R = (σ/2)(Φ⁻¹(p_A) − Φ⁻¹(p_B)) for Gaussian smoothing; provably tight.
- **ImageNet-scale certified defense**: 49% certified top-1 at ε=0.5 (ℓ₂), first certified defense with non-trivial accuracy at ImageNet.
- **Architecture-agnostic**: works for any base classifier; no assumption on ReLU structure or other architectural properties.
- **Monte Carlo certification procedure**: high-probability (p_A, p_B) estimates via PREDICT and CERTIFY algorithms.
- **Robustness-accuracy tradeoff via σ**: noise level σ is the single hyperparameter trading off certified radius vs. standard accuracy.

## Key Definitions / Theorems

- **Smoothed classifier**: g(x) = argmax_c Pr[f(x + δ) = c], δ ~ N(0, σ²I).
- **Main theorem (robust radius)**: If Pr[f(x+δ) = c_A] ≥ p_A ≥ p_B ≥ Pr[f(x+δ) = c_B] for every other class, then g(x+δ') = c_A for all ∥δ'∥₂ ≤ (σ/2)(Φ⁻¹(p_A) − Φ⁻¹(p_B)), where Φ is the standard Gaussian CDF.
- **Tightness**: Without additional assumptions on f, the bound is tight — there exist f saturating it.
- **CERTIFY algorithm**: given x, use Monte Carlo samples to compute a high-probability lower bound on p_A, yielding a high-probability certified radius.
- **PREDICT algorithm**: return g's prediction with controlled abstention rate when confidence is insufficient.

## Connections

- Source: [Certified Robustness via Differential Privacy (PixelDP)](certified-robustness-differential-privacy.md) — Lecuyer et al. predecessor using DP framework; gives looser bounds that this paper tightens via Neyman-Pearson.
- Source: [Provably Robust SmoothAdv](provably-robust-smoothadv.md) — Salman et al. NeurIPS 2019 follow-up combining adversarial training with smoothing.
- Source: [Convex Outer Adversarial Polytope (Wong-Kolter 2018)](provable-defenses-convex-polytope.md) — an alternative certified defense using LP relaxations; scales less well but works on ℓ∞.
- Concept: [Certified Robustness](../concepts/) / [Evasion Attacks](../concepts/evasion-attacks.md).
- Concept: [Concentration of Measure](../concepts/concentration-of-measure.md) — Gaussian smoothing connects to Gaussian isoperimetry and hence to concentration bounds.
- Source: [Universal Law of Robustness](universal-law-of-robustness.md) — Bubeck-Sellke establish that overparameterization is necessary for Lipschitzness; smoothing is the other side of this coin (adding noise averages out overfit adversarial sensitivity).
- Author: J. Zico Kolter (CMU, co-author on [Wong-Kolter 2018](provable-defenses-convex-polytope.md)).

## Open Questions / Limitations

- **Gaussian smoothing gives ℓ₂ robustness but nothing for ℓ∞** (at ImageNet scale, ℓ∞ adversarial training beats smoothing empirically); other smoothing distributions for ℓ∞ or ℓ₁ are less tight.
- **Accuracy cost**: certified accuracy of 49% vs. standard >75% on ImageNet; the gap reflects the σ noise level necessary for meaningful radius.
- **Monte Carlo inefficiency**: certification requires ~100K forward passes per input to achieve tight confidence bounds.
- **Adaptive attacks against the smoothing procedure itself**: the SmoothAdv follow-up partially addresses this but adaptive analysis remains active.
- **Certification of the base classifier's input preprocessing pipeline** (normalization, augmentation) is not straightforward.

## Quotes / Notable Passages

> "We show how to turn any classifier that classifies well under Gaussian noise into a new classifier that is certifiably robust to adversarial perturbations under the ℓ₂ norm."

> "No certified defense has been shown feasible on ImageNet except for smoothing."

> "Smoothing delivers higher certified accuracies than competing approaches on smaller-scale datasets where alternatives are viable."
