---
title: "Randomized Smoothing Meets Vision-Language Models (RS-VLM)"
type: source
date_ingested: 2026-04-23
authors: [Emmanouil Seferis, Changshun Wu, Stefanos Kollias, Saddek Bensalem, Chih-Hong Cheng]
venue: "arXiv:2509.16088v1 (19 Sep 2025). No venue is stated in the PDF."
year: 2025
tags: [certified-robustness, randomized-smoothing, vision-language-models, vla, generative-models]
claim_quantifier: conditional
antecedent: "Theorem 4.1 assumes only two answer types can be generated, that the oracle LLM's error rate is bounded by epsilon < 0.5, and that the oracle's only error is flipping between those two types. Theorem 5.3 additionally assumes the top-class probability is concentrated. The i.i.d. sampling that Clopper-Pearson needs is assumed throughout."
adversary_bound: "none — the adversary is bounded by an l2 radius on the image, which is a geometric constraint on the perturbation. Nothing bounds its compute, queries, or memory."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: white box
cls_write: none
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: n/a
cls_second_party: samples
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "gσ is robust around x, with a radius of at least: RpA = σΦ−1(pA)"
cls_evidence_src: "§3.1, Eq. 2 (background RS bound; Thm 4.1/4.2 extend it under an imperfect oracle)"
cls_reason: "The ℓ2 perturbation radius on the image is the bound Thm 4.1/4.2 certify against, capability-framed. access=white box because RS certification is a worst-case guarantee against any perturbation within the radius, independent of adversary information. Sample complexity ('tens to hundreds of thousands' of noisy samples per §1-2, cut 2-3 orders of magnitude) is the certifier's statistical cost, so it goes to second_party rather than the main row: neither the radius (capability) nor the sample count (statistical) is a frame=compute bound, so the attacker's bound decides per Rule 4's fallback. The oracle error rate ε<0.5 bounds a third party (the oracle), not a resource either the attacker or certifier spends, so it is not recorded as a unit."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (SWKBC25) extends [Cohen-Rosenfeld-Kolter 2019 randomized smoothing](certified-robustness-randomized-smoothing.md) to **generative Vision-Language Models (VLMs) and Vision-Language-Action (VLA) models** by connecting sequence outputs to an **oracle classification task** (harmful/harmless, discrete action, semantic-cluster vote) and bounding the oracle error rate. The phrase "the cleanest current theoretical extension of RS to the generative regime" stood here as an assessment; it is the wording of a secondary survey artifact, not of this paper or of any comparison made in the wiki, and it is withdrawn, corrected 2026-08-20.

The key insight: generative outputs (text, action sequences) don't have a natural "argmax class" to smooth, but many downstream uses can be cast as oracle classifications (e.g., "does this output contain harmful content?", "which action was taken?"). Smoothing the VLM outputs and then applying the classification oracle gives a certified radius for the classification decision — even though the underlying VLM output is generative.

Quantitatively, the paper derives improved scaling laws showing **2-3 orders of magnitude sample reduction under weaker assumptions** compared to naive per-output sampling. This makes certification practical for production-scale VLMs.

## Claim Boundary

- **Quantified over:** a single input pair (image x, text t), and perturbations e of the image with ‖e‖₂ within the certified radius. Theorem 4.1 is stated for a VLM whose answers fall into exactly two semantic classes. Theorems 5.3 and 5.5 concern the relation between sample count, certified radius, and certified accuracy, not the certificate itself.
- **Antecedent:** three assumptions carry Theorem 4.1, and the paper states each. Only two types of answer can be generated, so the setting is binary by fiat. The oracle LLM O has error rate ε < 0.5. The oracle's only possible error is flipping one of those two classes to the other, never producing a third. Under these, p̄_y = (q̄_y − ε)/(1 − 2ε), with q̄_y a Clopper-Pearson lower bound from n i.i.d. noise draws. Theorem 4.2 removes the need to know ε, but only when q̄_y > 0.5. Theorem 5.3 further assumes the top-class probability is concentrated.
- **Which party is constrained:** the adversary, by an ℓ₂ radius on the image. No party is bounded in compute, queries, or memory. The sample-count results price the *defender's* certification cost, which is the one place in this cluster where a computational quantity is measured at all, and it is the certifier's cost, not an attacker's.
- **Does not establish:** a certificate for the generative output. What is certified is the label an oracle assigns to the output, so the guarantee is only as good as the oracle and as the reduction of the task to two classes. Text-side perturbations are outside the guarantee entirely, since the noise is Gaussian on the image. The binary-answer assumption is severe for open-ended generation, and the paper does not extend the theorem past it.
- **Abstract vs theorem:** the abstract says RS "can still be enabled" for generative models "provided that the error rate for the oracle classifier comparison is bounded", which states the antecedent honestly. It does not mention the two-answer restriction or the directional-error assumption, both of which Theorem 4.1 needs.

## Key Contributions

- **RS for generative VLMs and VLAs**: extension from classifiers to generative sequence outputs via oracle classification.
- **Oracle classification framework**: the insight that downstream uses of generative outputs can often be cast as classifications.
- **Scaling laws**: 2-3 orders of magnitude sample reduction vs. naive approaches.
- The bullet that stood here called this the cleanest theoretical extension of CRK19 to the generative regime. That is the secondary survey artifact's wording and assessment, not the paper's and not a comparison the wiki has made. Withdrawn 2026-08-20.

## Connections

- Source: [Certified Robustness via Randomized Smoothing (CRK19)](certified-robustness-randomized-smoothing.md) — foundational; SWKBC25 extends to VLMs.
- Source: [SmoothAdv (SYL+19)](provably-robust-smoothadv.md) — adversarial-training boost; complementary.
- Source: [LeFCert (LXS+25)](lefcert-foundation-models.md) — RS for few-shot LEMs; SWKBC25 is for generative VLMs.
- Source: [NAAT (CYDS26)](naat-certified-semantic-smoothing.md) — RS for LLM jailbreaks via token ablation.
- Source: [RS-LLM-MAS (HDDH25)](rs-llm-multi-agent.md) — RS for multi-agent consensus.
- Source: [ADDS (SLDLN25)](adds-adaptive-diffusion-smoothing.md) — RS via diffusion purification.
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md).

## Quotes / Notable Passages

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> Extends Cohen-Rosenfeld-Kolter to generative VLMs and vision-language-action (VLA) models by connecting sequence outputs to an oracle classification task.

The abstract's own words on the same point, verbatim:

> "We resolve this by connecting generative outputs to an oracle classification task and showing that RS can still be enabled: the final response can be classified as a discrete action (e.g., service-robot commands in VLAs), as harmful vs. harmless (content moderation or toxicity detection in VLMs), or even applying oracles to cluster answers into semantically equivalent ones. Provided that the error rate for the oracle classifier comparison is bounded, we develop the theory that associates the number of samples with the corresponding robustness radius."

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> 2-3 orders of magnitude sample reduction under weaker assumptions — the cleanest current theoretical extension of RS to the generative regime.
