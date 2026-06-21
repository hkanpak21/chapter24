---
title: "Adaptive Diffusion Denoised Smoothing (ADDS)"
type: source
date_ingested: 2026-04-23
authors: [Frederick Shpilevskiy, Saiyue Lyu, Krishnamurthy Dj Dvijotham, Mathias Lécuyer, Pierre-André Noël]
venue: "arXiv:2507.08163 (Jul 2025); ICML 2025 (Oral)"
year: 2025
tags: [certified-robustness, randomized-smoothing, diffusion-models, differential-privacy, gdp-composition]
---

## Summary

This paper (SLDLN25, **ADDS** = **A**daptive **D**iffusion **D**enoised **S**moothing) reinterprets each step of a guided denoising diffusion model as an **adaptive Gaussian Differentially Private (GDP) mechanism** and composes them through a GDP privacy filter, yielding end-to-end certified robustness through a multi-step diffusion purifier.

The key theoretical step: classical [randomized smoothing (CRK19)](certified-robustness-randomized-smoothing.md) is, mathematically, a GDP composition analysis applied to an image classifier. Diffusion models perform sequential denoising — each step is a Gaussian-noise-added transformation. ADDS observes that each diffusion step can be analyzed as a GDP mechanism, and sequential composition through GDP privacy filter yields a certified robustness radius for the end-to-end diffusion-purified-classifier pipeline.

This extends **Adaptive Randomized Smoothing (ARS)** analysis to a practical, variance-adaptive composition — an important theoretical step because the underlying GDP composition is the mathematical kernel of RS. Empirically, ADDS achieves state-of-the-art certified robustness on CIFAR-10 and ImageNet under ℓ₂ perturbations.

ICML 2025 Oral.

## Key Contributions

- **GDP reinterpretation of diffusion steps**: each guided denoising step = adaptive Gaussian DP mechanism.
- **GDP composition for multi-step diffusion**: end-to-end certified robustness via privacy filter composition.
- **Extension of Adaptive Randomized Smoothing (ARS)**: variance-adaptive multi-step composition.
- **State-of-the-art certified robustness**: CIFAR-10 and ImageNet ℓ₂ benchmarks.
- **Unification of diffusion purification and randomized smoothing**: both now fall under the GDP framework.

## Connections

- Source: [Certified Robustness via Randomized Smoothing (CRK19)](certified-robustness-randomized-smoothing.md) — foundational; ADDS extends via GDP composition.
- Source: [SmoothAdv (SYL+19)](provably-robust-smoothadv.md) — adversarial training + smoothing.
- Source: [PixelDP (LAGHJ19)](certified-robustness-differential-privacy.md) — DP-based certified robustness predecessor.
- Source: [Deep Learning with DP (ACG+16)](deep-learning-differential-privacy.md) — GDP / DP-SGD foundation.
- Source: [RS meets VLM (SWKBC25)](rs-meets-vlm.md) — RS for generative models; different extension direction.
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md).

## Quotes / Notable Passages

> "Reinterprets each step of a guided denoising diffusion model as an adaptive Gaussian Differentially Private (GDP) mechanism and composes them through a GDP privacy filter, yielding end-to-end certified robustness through a multi-step diffusion purifier."
