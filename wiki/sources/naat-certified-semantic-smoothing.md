---
title: "Provable Defense Framework for LLM Jailbreaks via Noise-Augmented Alignment (NAAT + CSS)"
type: source
date_ingested: 2026-04-23
authors: [Zehua Cheng, Jianwei Yang, Wei Dai, Jiahao Sun]
venue: "arXiv:2602.01587 (Feb 2026)"
year: 2026
tags: [llm-security, certified-robustness, randomized-smoothing, jailbreak, hypergeometric, semantic-smoothing]
---

## Summary

This paper (CYDS26) presents **Certified Semantic Smoothing (CSS)** — the first end-to-end deterministic certification protocol for instruction-tuned LLMs against gradient-based jailbreaks such as GCG. Classical [randomized smoothing (Cohen-Rosenfeld-Kolter 2019)](certified-robustness-randomized-smoothing.md) applies Gaussian noise in continuous input space, which is **not well-defined** for the high-dimensional *discrete* token space of language models. CSS solves this by introducing **stratified randomized ablation**: the prompt is partitioned into immutable structural tokens (system-level instructions, tool invocations) and mutable payload tokens (user-provided content), and a subset of the payload is randomly ablated. The certified radius is derived from the **Hypergeometric distribution** (exact combinatorial analysis), yielding an **ℓ₀-norm** certified robustness radius.

The companion **Noise-Augmented Alignment Tuning (NAAT)** is a fine-tuning procedure that aligns the base LLM's representations with the smoothing distribution — effectively turning the LLM into a *semantic denoiser* so that utility does not collapse under sparse-ablated inputs. NAAT solves the "inverted scaling fallacy" that plagued character-level SmoothLLM (where smoothing reduced both attack success and benign utility proportionally).

Positioned as the first practical certified LLM jailbreak defense with (1) deterministic certification under the Hypergeometric distribution, (2) preserved utility via alignment-aware fine-tuning, and (3) direct applicability to production models.

## Key Contributions

- **Certified Semantic Smoothing (CSS)**: stratified randomized ablation defining an ℓ₀-norm certified radius via Hypergeometric tail bounds.
- **Stratified token partition**: immutable structural tokens vs. mutable payload tokens — semantically-aware smoothing.
- **Hypergeometric distribution for certification**: replaces CRK19's Gaussian analysis; exact combinatorial tail bound.
- **Noise-Augmented Alignment Tuning (NAAT)**: fine-tuning procedure that makes the LLM a semantic denoiser under sparse inputs.
- **Solves inverted-scaling fallacy**: previous character-level SmoothLLM saw utility collapse; NAAT preserves utility while maintaining certified robustness.
- **First end-to-end deterministic certification for LLM jailbreaks**: GCG and gradient-based attacks are formally ruled out up to the certified ℓ₀ radius.

## Key Definitions / Theorems

- **Stratified smoothing**: input x = (x_struct, x_payload); smoothing samples subsets of x_payload while keeping x_struct fixed.
- **CSS certificate**: if the smoothed classifier's top-class margin exceeds a Hypergeometric-derived threshold, the prediction is certifiably robust to ℓ₀-bounded attacks on the payload.
- **NAAT objective**: fine-tune the LLM to minimize KL divergence between outputs on ablated and non-ablated prompts, for benign training examples.
- **Neyman-Pearson-style tight bound**: the Hypergeometric analysis is tight for the ablation mechanism.

## Connections

- Source: [Certified Robustness via Randomized Smoothing (CRK19)](certified-robustness-randomized-smoothing.md) — foundational smoothing paper; CSS is the LLM/discrete-space extension.
- Source: [SmoothAdv (SYL+19)](provably-robust-smoothadv.md) — adversarial training boost to smoothing; NAAT is the LLM analogue.
- Source: [Filter Impossibility (BGGKRR25)](filter-impossibility-ai-alignment.md) — shows black-box filters fail; CSS is a model-intervention (not black-box filter) consistent with BGGKRR's framework.
- Source: [Universal Jailbreak Backdoors from Poisoned RLHF (RT23)](universal-jailbreak-rlhf-backdoors.md) — practical jailbreak attack; CSS is the corresponding provable defense.
- Source: [Immune: RLHF Jailbreak Defense](immune-rlhf-jailbreak-defense.md) — inference-time defense; CSS is complementary with provable guarantees.
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md) — jailbreaks as evasion in LLM context.

## Open Questions / Limitations

- **ℓ₀ radius is small**: certified robustness applies to ablation of a few tokens; jailbreaks using many-token manipulations may still succeed.
- **Structural-payload partition requires care**: if attacker can influence the "structural" tokens, the certification doesn't apply.
- **Fine-tuning cost**: NAAT requires substantial compute; scaling to frontier models is an open engineering challenge.
- **Hypergeometric radius**: specific to fixed-budget ablation; other discrete-smoothing distributions may give tighter bounds in specific regimes.

## Quotes / Notable Passages

> "The first end-to-end deterministic certification protocol for instruction-tuned LLMs against gradient-based jailbreaks."

> "Certified Semantic Smoothing via stratified randomized ablation — partitioning the prompt into immutable structural tokens and mutable payloads — derives an ℓ₀-norm certified radius from the Hypergeometric distribution."
