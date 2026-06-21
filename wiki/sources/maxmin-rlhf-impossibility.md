---
title: MaxMin-RLHF — Alignment with Diverse Human Preferences (Impossibility of Single-Reward RLHF)
type: source
date_ingested: 2026-04-12
authors: [Souradip Chakraborty, Jiahao Qiu, Hui Yuan, Alec Koppel, Dinesh Manocha, Furong Huang, Amrit Singh Bedi, Mengdi Wang]
venue: ICML
year: 2024
tags: [rlhf, impossibility, alignment, formal-models, social-choice]
---

## Summary
This paper gives a formal impossibility result for RLHF when the human population is heterogeneous: a single scalar reward model cannot simultaneously align an LLM policy with all user subpopulations. The authors model the human population H as a union of |U| subgroups H_u with group-specific preference distributions p*_u drawn from a Bradley–Terry model with per-group reward parameters φ*_u, aggregated into an overall preference p* via a mixing distribution η(u).

They prove two quantitative bounds. **Lemma 1** lower-bounds the gap between the MLE reward parameter φ̂ (which converges to φ* — the single ground-truth reward) and the group-optimal φ*_u by ε(1−η(u))/(4D), where ε captures diversity (a gap between TV-distances of preference distributions) and D is a feature-norm bound. **Theorem 1** lifts this to an alignment gap on the *policy* under KL-regularized RL fine-tuning: Align-Gap(π_RLHF) ≥ λ_ψ ε(1−η(u)) / (64 β² L_π D²), where λ_ψ is the minimum eigenvalue of the feature Gram matrix, β the KL regularization strength, and L_π the Lipschitz constant of log π.

The result is motivated by the Egalitarian (Rawlsian) principle from social choice theory: they propose MaxMin-RLHF, which learns a mixture of reward functions via EM clustering and then optimizes the max-min social welfare objective π*_F = argmax_π min_u F_{r*_u}(π). Experiments on GPT-2 and Tulu2-7B validate both the impossibility (single reward RLHF fails minorities) and the MaxMin fix.

## Key Contributions
- First formal impossibility theorem for single-reward RLHF under preference diversity.
- Quantitative lower bound on alignment gap as a function of diversity ε and minority weight 1−η(u).
- MaxMin-RLHF algorithm (EM reward clustering + max-min PPO) grounded in Egalitarian social choice.
- Empirical validation showing single-reward RLHF converges to majority preferences and neglects minority subgroups.

## Key Definitions / Theorems
- **Definition 1 (Diversity)**: Diversity(i,j) := TV(p*_i, p*_j); ε := Diversity(i*,j*) − max_{k≠u} Diversity(k, j*), where (i*, j*) is the most diverse pair and u is the most-distant ("minority") group.
- **Lemma 1 (reward mismatch)**: ‖φ* − φ*_u‖ ≥ ε(1−η(u))/(4D).
- **Theorem 1 (alignment gap)**: Align-Gap(π_RLHF) ≥ λ_ψ · ε(1−η(u)) / (64 β² L_π D²).
- Proof chain: Bradley–Terry Lipschitzness (Lemma 2) → TV → policy gap via strong convexity of KL-regularized objective + DPO-style reward→policy mapping.
- **MaxMin objective**: π*_F = argmax_π min_{u ∈ U} E_{x,y}[r_{φ*_u}(y,x)] − β KL(π‖π_ref).

## Connections
- Links to [rlhf-formal-model](../concepts/rlhf-formal-model.md), [impossibility-frameworks](../concepts/impossibility-frameworks.md).
- Related crypto/AI security work: [extending-formalism-cryptography-ai](extending-formalism-cryptography-ai.md), [formalizing-llm-agent-security](formalizing-llm-agent-security.md).
- Contrasts with [immune-rlhf-jailbreak-defense](immune-rlhf-jailbreak-defense.md) (same lab, Chakraborty + Bedi; possibility result for a different RLHF gap).
- Authors: [Souradip Chakraborty](../entities/souradip-chakraborty.md), [Amrit Singh Bedi](../entities/amrit-singh-bedi.md), [Mengdi Wang](../entities/mengdi-wang.md), [Furong Huang](../entities/furong-huang.md).

## Open Questions / Limitations
- Bound depends on linear reward parametrization r_φ = ⟨φ, ψ(y,x)⟩; extension to nonlinear reward heads is open.
- Identification of minority subgroups in practice is an open estimation problem (the paper uses EM).
- Whether DPO-style methods evade the impossibility (they shouldn't — DPO is equivalent to single reward under BT) is noted but not exhaustively analyzed.
- No lower bound on the *statistical* sample complexity of learning the mixture.

## Quotes / Notable Passages
"The assumption of a single ground truth reward is restrictive and can potentially subdue the preferences or opinions of minority groups, leading to societal biases."

"True to our finding, our work is the first to report such a result in the RLHF literature."
