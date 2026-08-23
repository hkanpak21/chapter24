---
title: Immune — Improving Safety Against Jailbreaks in Multi-modal LLMs via Inference-Time Alignment
type: source
date_ingested: 2026-04-12
authors: [Soumya Suvra Ghosal, Souradip Chakraborty, Vaibhav Singh, Tianrui Guan, Mengdi Wang, Alvaro Velasquez, Ahmad Beirami, Furong Huang, Dinesh Manocha, Amrit Singh Bedi]
venue: "arXiv:2411.18688v5 (14 Jun 2025). No venue is stated in the PDF; the earlier 'CVPR submission' attribution came from the ingest, not the document."
year: 2025
tags: [rlhf, jailbreak, llm-security, alignment, controlled-decoding, adversarial-ml]
claim_quantifier: conditional
antecedent: "A bounded safety reward R_safe(x,y) <= R_max; a given prompt distribution p_0 and an adversarial prompt distribution p_adv; and rho_safe, the trajectory distribution of an already safety-aligned model, taken as given. The bound is vacuous when the KL between p_0 and p_adv is large, and the paper does not bound it."
adversary_bound: "none — the adversary is an unrestricted optimizer over prompt distributions. It is constrained only by a KL regularizer to the natural prompt distribution, which prices similarity, not compute."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: white box
cls_write: read only
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: stated
cls_second: none
cls_assessed:
cls_evidence: "The adversarial prompt distribution in (2), padv, is defined as a solution to a KL-regularized optimization problem that minimizes expected reward Rsafe relative to p0, with regularization parameter β."
cls_evidence_src: Eq. 2 / Thm 1 discussion
cls_reason: "Classified on Theorem 1 (the suboptimality bound), not the empirical ASR reduction, per rule 1. frame/party/unit/tightness are none because neither party carries a compute bound: the adversary is an unrestricted argmin regularized only by a KL similarity term, and the defender's α is a decoding hyperparameter, not a resource bound, matching the wiki page's own Claim Boundary finding 'neither, in any resource'. baseline=stated from the paper's ASR-vs-base-model comparisons even though Theorem 1 itself carries no baseline framing."
cls_prov: P
cls_date: 2026-08-22
---

## Summary
Immune reframes defense against multi-modal LLM jailbreaks as an *inference-time alignment* problem rather than a training-time one. The authors argue (and demonstrate empirically) that RLHF-based training-time safety alignment is insufficient against image-based and text-based adversarial prompts, because adversaries can solve p_adv = argmin_p E_{q∼p, y∼π_safe}[R_safe(q,y)] + β · div(p(·|x_input), p_0(·|x_input)) to find adversarial prompt distributions that satisfy the input "cost metric" while driving the safe policy to unsafe outputs.

Rather than an *impossibility* theorem, the paper presents a *possibility* result: by moving the safeguard to decoding (using a safety reward model R_safe via KL-regularized controlled decoding), they obtain a bound on suboptimality. **Theorem 1** shows the sub-optimality gap of the defended policy decomposes as Δ₁ + Δ₂ where Δ₁ ≤ R_max √(½ KL(p_0‖p_adv)) and Δ₂ ≤ α KL(ρ*‖ρ_safe-dec). This characterizes when inference-time alignment succeeds (low KL between adversarial and natural prompt distributions, small α).

This paper is not an impossibility theorem about RLHF. It is a possibility result arguing RLHF training-time alignment has a fundamental *gap* (making the adversary's optimization problem tractable) and that inference-time decoding fills the gap. The formal contribution is an upper bound on suboptimality, not a lower bound on attack success.

## Claim Boundary

- **Quantified over:** Theorem 1 ranges over a single input x_input, bounding the suboptimality gap Δ_sub-gap(x_input) of the controlled-decoding policy relative to the optimal safe policy. It is pointwise, not uniform over inputs, and says nothing about attack success rates. The empirical claims range over LLaVA-1.6, MiniGPT-4, and Qwen-VL on MM-SafetyBench, FigStep, JailBreakV-28K, and visual adversarial attacks.
- **Antecedent:** the safety reward is bounded, R_safe(x, y) ≤ R_max. The prompt distributions p_0 and p_adv and the trajectory distributions ρ* and ρ_safe are given. The bound's leading term scales with the KL divergence between the natural and adversarial prompt distributions, so it is informative only when the adversary stays close to natural prompts, and the paper does not bound that divergence for any real attack.
- **Which party is constrained:** neither, in any resource. The adversary is defined as an unrestricted argmin over prompt distributions, p_adv = argmin_p E[R_safe] + β·div(p, p_0). The β·div term prices distance from the natural prompt distribution, which is a similarity constraint, not a compute, query, or memory bound. The defender is constrained only by the decoding temperature α.
- **Does not establish:** that inference-time alignment defeats jailbreaks, or that training-time alignment cannot. It is an upper bound on one policy's suboptimality, with no matching lower bound, so no claim that another defence could not do better follows from it. The abstract itself describes the analytic content as "a mathematical characterization of Immune, offering insights on why it improves safety", which is weaker than a guarantee. Adaptive and white-box attacks against Immune are not evaluated.
- **Abstract vs theorem:** none found. The abstract calls the analysis a characterization offering insights and does not claim a security guarantee. The overreach on this page came from the ingest, and the Summary already flags it.

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
Both passages below were checked against `raw/GCS+24_ImmuneRLHFJailbreak.pdf` on 2026-08-20 and are verbatim.

> "Current alignment achieved solely via safety training/fine-tuning with RLHF is insufficient to defend against jailbreak attacks."

> "We mathematically formalize this defense as an inference-time alignment problem within the KL-regularized reinforcement learning framework."
