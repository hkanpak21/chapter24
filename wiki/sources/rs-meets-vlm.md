---
title: "Randomized Smoothing Meets Vision-Language Models (RS-VLM)"
type: source
date_ingested: 2026-04-23
authors: [Emmanouil Seferis, Changshun Wu, Stefanos Kollias, Saddek Bensalem, Chih-Hong Cheng]
venue: "arXiv:2509.16088 (Sep 2025)"
year: 2025
tags: [certified-robustness, randomized-smoothing, vision-language-models, vla, generative-models]
---

## Summary

This paper (SWKBC25) extends [Cohen-Rosenfeld-Kolter 2019 randomized smoothing](certified-robustness-randomized-smoothing.md) to **generative Vision-Language Models (VLMs) and Vision-Language-Action (VLA) models** by connecting sequence outputs to an **oracle classification task** (harmful/harmless, discrete action, semantic-cluster vote) and bounding the oracle error rate. This is the **cleanest current theoretical extension of RS to the generative regime**.

The key insight: generative outputs (text, action sequences) don't have a natural "argmax class" to smooth, but many downstream uses can be cast as oracle classifications (e.g., "does this output contain harmful content?", "which action was taken?"). Smoothing the VLM outputs and then applying the classification oracle gives a certified radius for the classification decision — even though the underlying VLM output is generative.

Quantitatively, the paper derives improved scaling laws showing **2-3 orders of magnitude sample reduction under weaker assumptions** compared to naive per-output sampling. This makes certification practical for production-scale VLMs.

## Key Contributions

- **RS for generative VLMs and VLAs**: extension from classifiers to generative sequence outputs via oracle classification.
- **Oracle classification framework**: the insight that downstream uses of generative outputs can often be cast as classifications.
- **Scaling laws**: 2-3 orders of magnitude sample reduction vs. naive approaches.
- **Cleanest theoretical extension of CRK19 to generative regime**: foundation for further RS-for-generative research.

## Connections

- Source: [Certified Robustness via Randomized Smoothing (CRK19)](certified-robustness-randomized-smoothing.md) — foundational; SWKBC25 extends to VLMs.
- Source: [SmoothAdv (SYL+19)](provably-robust-smoothadv.md) — adversarial-training boost; complementary.
- Source: [LeFCert (LXS+25)](lefcert-foundation-models.md) — RS for few-shot LEMs; SWKBC25 is for generative VLMs.
- Source: [NAAT (CYDS26)](naat-certified-semantic-smoothing.md) — RS for LLM jailbreaks via token ablation.
- Source: [RS-LLM-MAS (HDDH25)](rs-llm-multi-agent.md) — RS for multi-agent consensus.
- Source: [ADDS (SLDLN25)](adds-adaptive-diffusion-smoothing.md) — RS via diffusion purification.
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md).

## Quotes / Notable Passages

> "Extends Cohen-Rosenfeld-Kolter to generative VLMs and vision-language-action (VLA) models by connecting sequence outputs to an oracle classification task."

> "2-3 orders of magnitude sample reduction under weaker assumptions — the cleanest current theoretical extension of RS to the generative regime."
