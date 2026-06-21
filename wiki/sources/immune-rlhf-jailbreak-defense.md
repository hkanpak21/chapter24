---
title: Immune — Improving Safety Against Jailbreaks in Multi-modal LLMs via Inference-Time Alignment
type: source
date_ingested: 2026-04-12
authors: [Soumya Suvra Ghosal, Souradip Chakraborty, Vaibhav Singh, Tianrui Guan, Mengdi Wang, Alvaro Velasquez, Ahmad Beirami, Furong Huang, Dinesh Manocha, Amrit Singh Bedi]
venue: arXiv / CVPR submission
year: 2025
tags: [rlhf, jailbreak, llm-security, alignment, controlled-decoding, adversarial-ml]
---

## Summary
Immune reframes defense against multi-modal LLM jailbreaks as an *inference-time alignment* problem rather than a training-time one. The authors argue (and demonstrate empirically) that RLHF-based training-time safety alignment is insufficient against image-based and text-based adversarial prompts, because adversaries can solve p_adv = argmin_p E_{q∼p, y∼π_safe}[R_safe(q,y)] + β · div(p(·|x_input), p_0(·|x_input)) to find adversarial prompt distributions that satisfy the input "cost metric" while driving the safe policy to unsafe outputs.

Rather than an *impossibility* theorem, the paper presents a *possibility* result: by moving the safeguard to decoding (using a safety reward model R_safe via KL-regularized controlled decoding), they obtain a bound on suboptimality. **Theorem 1** shows the sub-optimality gap of the defended policy decomposes as Δ₁ + Δ₂ where Δ₁ ≤ R_max √(½ KL(p_0‖p_adv)) and Δ₂ ≤ α KL(ρ*‖ρ_safe-dec). This characterizes when inference-time alignment succeeds (low KL between adversarial and natural prompt distributions, small α).

**Important note for the wiki**: despite the user's framing, this paper is not an impossibility theorem about RLHF; it is a possibility result arguing RLHF training-time alignment has a fundamental *gap* (making the adversary's optimization problem tractable) and that inference-time decoding fills the gap. The formal contribution is an upper bound on suboptimality, not a lower bound on attack success.

## Key Contributions
- Formalizes jailbreak as a min-max adversarial alignment problem where the adversary controls the prompt distribution p_adv.
- Presents Immune: a controlled-decoding algorithm using a safety reward R_safe and KL regularization to the base safe policy.
- Theorem 1: upper bound on the sub-optimality gap Δ_sub-gap in terms of KL divergences.
- Empirical evaluation on LLaVA, MiniGPT-4, Qwen-VL across MM-SafetyBench, FigStep, JailBreakV-28K, visual adversarial attacks, showing large ASR reductions (e.g., 57.82% reduction on text-based attacks vs. base model).

## Key Definitions / Theorems
- **Adversarial prompt distribution (def)**: p_adv := argmin_p E[R_safe(x,y)] + β · div(p(·|x_input), p_0(·|x_input)).
- **Controlled decoding policy**: π*_safe-dec(z|s_t) = (1/Z) π_safe(z|s_t) exp(Q_safe(s_t,z)/α).
- **Theorem 1 (sub-optimality bound)**: Δ_sub-gap(x_input) ≤ R_max √(½ KL(p_0‖p_adv)) + α KL(ρ*‖ρ_safe-dec).
- Proof via decomposition Δ = Δ₁ + Δ₂, Pinsker's inequality for Δ₁, KL-regularized optimality of controlled decoding for Δ₂.

## Connections
- Companion theory-of-diversity paper: [maxmin-rlhf-impossibility](maxmin-rlhf-impossibility.md) (shared authors Chakraborty, Bedi, Wang, Huang, Manocha).
- Uses controlled decoding framework of Mroueh / Mudgal et al.
- Adversarial-ML connection: [evasion-attacks](../concepts/evasion-attacks.md) on LLMs.
- Authors: [Souradip Chakraborty](../entities/souradip-chakraborty.md), [Amrit Singh Bedi](../entities/amrit-singh-bedi.md), [Furong Huang](../entities/furong-huang.md), [Mengdi Wang](../entities/mengdi-wang.md), [Soumya Suvra Ghosal](../entities/soumya-suvra-ghosal.md).

## Open Questions / Limitations
- Evaluation is on static datasets; adaptive / whitebox attacks not evaluated.
- The bound requires a good safety reward R_safe; the paper uses off-the-shelf RewardBench-style models without lower-bounding reward quality.
- No matching lower bound (would require showing no inference-time defense can do better) — the claim is not an impossibility theorem.

## Quotes / Notable Passages
"Current alignment achieved solely via safety training/fine-tuning with RLHF is insufficient to defend against jailbreak attacks."

"We mathematically formalize this defense as an inference-time alignment problem within the KL-regularized reinforcement learning framework."
