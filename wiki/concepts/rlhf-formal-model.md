---
title: RLHF Formal Model
type: concept
tags: [rlhf, alignment, formal-models, bradley-terry, kl-regularization]
---

## Definition
The canonical formal model of Reinforcement Learning from Human Feedback consists of three stages applied to a base language policy π_θ:
1. **SFT**: supervised fine-tuning on a seed dataset to obtain π_ref.
2. **Reward modeling**: learn r_φ : X × Y → ℝ by MLE on a preference dataset D = {(x, y_1, y_2)} under the **Bradley–Terry** model p*(y_1 ≻ y_2 | x) = exp(r*(y_1,x)) / (exp(r*(y_1,x)) + exp(r*(y_2,x))). Loss: L_R(r_φ) = −E[log σ(r_φ(y_1,x) − r_φ(y_2,x))].
3. **KL-regularized RL fine-tuning**: π* = argmax_π E_{x,y∼π}[r_φ(y,x)] − β · KL(π(·|x) ‖ π_ref(·|x)).

Under the KL-regularized objective the optimal policy has the closed form π_r(y|x) = (1/Z(x)) π_ref(y|x) exp((1/β) r(y,x)) (Rafailov et al., DPO).

## Intuition
RLHF reduces preference alignment to learning a scalar latent reward and then softmaxing the base policy toward it. The KL term keeps the fine-tuned policy close to π_ref, providing stability and a handle for theoretical analysis.

## Properties / Theorems
- **Equivalence to DPO**: the KL-regularized optimum can be reparameterized so that r_φ itself is learned directly from preferences (DPO).
- **Strong concavity of −F_{r_φ}(π)** (w.r.t. π under KL regularization): enables reduction from policy gap to reward-parameter gap.
- **Lipschitzness of Bradley–Terry**: ‖p_φ − p_{φ'}‖ ≤ L_p ‖φ − φ'‖ with L_p = 4D where D bounds feature norms (Lemma 2, MaxMin-RLHF).
- **Impossibility under preference diversity**: single-reward RLHF cannot align diverse subpopulations; quantitative lower bound via feature-matrix minimum eigenvalue λ_ψ — see [impossibility-frameworks](impossibility-frameworks.md).
- **Inference-time complement**: controlled decoding against a safety reward yields a suboptimality upper bound tied to KL(p_0 ‖ p_adv) (Immune, Theorem 1).

## Where It Appears
- [maxmin-rlhf-impossibility](../sources/maxmin-rlhf-impossibility.md) — impossibility under diversity.
- [immune-rlhf-jailbreak-defense](../sources/immune-rlhf-jailbreak-defense.md) — inference-time safety alignment.

## Related Concepts
- [impossibility-frameworks](impossibility-frameworks.md).
- [attack-taxonomy-llms](attack-taxonomy-llms.md) — jailbreaks as adversarial inputs to RLHF-aligned policies.

## Open Questions
- Is the BT-model assumption necessary for the impossibility bound or can it be relaxed to general discrete-choice models?
- Sample complexity of learning reward mixtures (MaxMin-RLHF uses EM; no formal convergence rate).
- Formal connection between training-time alignment gap and inference-time attack success rate.
