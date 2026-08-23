---
title: "Adaptive Diffusion Denoised Smoothing (ADDS)"
type: source
date_ingested: 2026-04-23
authors: [Frederick Shpilevskiy, Saiyue Lyu, Krishnamurthy Dj Dvijotham, Mathias Lécuyer, Pierre-André Noël]
venue: "arXiv:2507.08163v1 (10 Jul 2025). The PDF's running footer reads 'Submitted to 2nd Workshop on Test-Time Adaptation for ICML2025'. The string 'Oral' does not appear anywhere in the document, and no acceptance is stated. The earlier 'ICML 2025 (Oral)' attribution came from the ingest, not the PDF."
year: 2025
tags: [certified-robustness, randomized-smoothing, diffusion-models, differential-privacy, gdp-composition]
claim_quantifier: conditional
antecedent: "The guided DDPM denoising of Algorithm 2 runs with total randomized-smoothing variance sigma^2, and each pixel's mechanism is r_i/sigma-GDP as established in Proposition 3.2, which itself rests on the one-step budget of Proposition 3.1 and on concurrent composition of GDP mechanisms. The bounds p_+ and p_- on the top and runner-up class probabilities are estimated, not known."
adversary_bound: "none — the adversary is bounded by an l2 radius on the image, a geometric constraint on the perturbation. The differential privacy in this paper is a proof technique for composing the denoising steps, not a privacy guarantee and not a bound on anyone's resources."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: none
cls_write: none
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: "perturbed inputs x + e, with perturbation e ∈ Bp(r) in the Lp ball of radius r, that make a classifier g misclassify the input x"
cls_evidence_src: §2 Background
cls_reason: "Rule 5 (perturbation budget); no computational, query or memory bound on any party anywhere in the paper (grepped 'polynomial', 'computation', 'runtime' — only the defender's certification runtime in Fig. 4, a different party's cost, not the attacker's), so assessed is blank rather than implicit. access/write=none: the certificate is a worst-case guarantee over the whole ℓ2 ball, with no described query/interaction protocol."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (SLDLN25, **ADDS** = **A**daptive **D**iffusion **D**enoised **S**moothing) reinterprets each step of a guided denoising diffusion model as an **adaptive Gaussian Differentially Private (GDP) mechanism** and composes them through a GDP privacy filter, yielding end-to-end certified robustness through a multi-step diffusion purifier.

The key theoretical step: classical [randomized smoothing (CRK19)](certified-robustness-randomized-smoothing.md) is, mathematically, a GDP composition analysis applied to an image classifier. Diffusion models perform sequential denoising — each step is a Gaussian-noise-added transformation. ADDS observes that each diffusion step can be analyzed as a GDP mechanism, and sequential composition through GDP privacy filter yields a certified robustness radius for the end-to-end diffusion-purified-classifier pipeline.

This extends **Adaptive Randomized Smoothing (ARS)** analysis to a practical, variance-adaptive composition — an important theoretical step because the underlying GDP composition is the mathematical kernel of RS. Empirically, ADDS achieves state-of-the-art certified robustness on CIFAR-10 and ImageNet under ℓ₂ perturbations.

**Corrected 2026-08-20.** The line "ICML 2025 Oral" stood here. The PDF's own footer reads "Submitted to 2nd Workshop on Test-Time Adaptation for ICML2025", the word "Oral" occurs nowhere in it, and no acceptance is stated. Treat the venue as a workshop submission unless a published version is found.

## Claim Boundary

- **Quantified over:** a single input image x and adversarial changes e with ‖e‖₂ ≤ r_x. Theorem 3.3 certifies that the smoothed model's prediction is unchanged on the whole ℓ₂ ball of that radius, with r_x = (σ/2)(Φ⁻¹(p_+) − Φ⁻¹(p_−)). The certification is pointwise; certified accuracy over a test set is an aggregate of pointwise certificates. Experiments are on CIFAR-10 and ImageNet.
- **Antecedent:** the chain is Proposition 3.1, a one-step denoising budget; Proposition 3.2, which makes each pixel's mechanism r_i/σ-GDP end to end; then concurrent composition of the per-pixel GDP mechanisms, giving √(Σ r_i²)/σ = r_x/σ-GDP for Algorithm 2. Theorem 3.3 takes p_+ and p_− as given bounds on the top and runner-up class probabilities; in practice they are estimated by sampling, so the certificate carries that estimate's confidence. The guiding strategy is fixed, and the paper is explicit that the improvement holds "under a specific guiding strategy".
- **Which party is constrained:** the adversary, by an ℓ₂ radius on the image. Nothing bounds any party's compute, queries, or memory. **The differential privacy here is not a privacy guarantee.** GDP is used as the composition calculus that makes a many-step adaptive denoiser analyzable; no data subject is protected and no privacy budget is spent on anyone's behalf. Reading this page as evidence that a resource-bounded adversary appears in the certified-robustness literature would be a mistake.
- **Does not establish:** robustness beyond the certified radius, robustness to anything other than ℓ₂ perturbation, or that the diffusion purifier removes the attack. It certifies that the smoothed classifier's label is stable, not that the label is right. The paper also reports that additional unguided denoising increases variance and degrades clean accuracy, and that majority voting improves certified accuracy while reducing clean accuracy, so the reported gains are a trade rather than a free improvement.
- **Abstract vs theorem:** none found. The abstract claims the design "can improve both certified accuracy and standard accuracy on ImageNet for an ℓ₂ threat model" under a specific guiding strategy, which is what the experiments show, and it names the threat model.

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

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> Reinterprets each step of a guided denoising diffusion model as an adaptive Gaussian Differentially Private (GDP) mechanism and composes them through a GDP privacy filter, yielding end-to-end certified robustness through a multi-step diffusion purifier.

The abstract's own words on the same point, verbatim:

> "Our key insight is to reinterpret a guided denoising diffusion model as a long sequence of adaptive Gaussian Differentially Private (GDP) mechanisms refining a pure noise sample into an image. We show that these adaptive mechanisms can be composed through a GDP privacy filter to analyze the end-to-end robustness of the guided denoising process, yielding a provable certification that extends the adaptive randomized smoothing analysis."
