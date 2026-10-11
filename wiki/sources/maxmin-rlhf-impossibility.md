---
title: MaxMin-RLHF — Alignment with Diverse Human Preferences (Impossibility of Single-Reward RLHF)
type: source
date_ingested: 2026-04-12
authors: [Souradip Chakraborty, Jiahao Qiu, Hui Yuan, Alec Koppel, Dinesh Manocha, Furong Huang, Amrit Singh Bedi, Mengdi Wang]
venue: "arXiv:2402.08925v2 (26 Dec 2024); Proceedings of the 41st International Conference on Machine Learning, PMLR 235, 2024 (stated in the PDF footer)"
year: 2024
tags: [rlhf, impossibility, alignment, formal-models, social-choice]
claim_quantifier: conditional
antecedent: "A Bradley-Terry preference model with linear rewards r_phi = <phi, psi(y,x)>; a bounded feature norm D; a positive minimum eigenvalue lambda_psi of the feature Gram matrix; a Lipschitz constant L_pi on log pi; and a strictly positive diversity gap epsilon. The bound is vacuous when epsilon = 0, that is when the subpopulations do not in fact disagree."
adversary_bound: "none — there is no adversary. The obstruction is heterogeneity in the human population, not an attacker. The constrained party is the aligner, and the constraint is representational (one scalar reward) rather than a bound on any resource."
date_verified: 2026-08-20
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: absent
cls_evidence_src: "no bound on any party in the impossibility theorem or its setup"
cls_reason: "No attack or adversary appears anywhere. The constraint is representational, a single scalar reward serving a heterogeneous population, not a bound on any party's resource, so every field is none/unstated by Rule 2."
cls_prov: F
cls_date: 2026-08-22
---

## Summary
This paper gives a formal impossibility result for RLHF when the human population is heterogeneous: a single scalar reward model cannot simultaneously align an LLM policy with all user subpopulations. The authors model the human population H as a union of |U| subgroups H_u with group-specific preference distributions p*_u drawn from a Bradley–Terry model with per-group reward parameters φ*_u, aggregated into an overall preference p* via a mixing distribution η(u).

They prove two quantitative bounds. **Lemma 1** lower-bounds the gap between the MLE reward parameter φ̂ (which converges to φ* — the single ground-truth reward) and the group-optimal φ*_u by ε(1−η(u))/(4D), where ε captures diversity (a gap between TV-distances of preference distributions) and D is a feature-norm bound. **Theorem 1** lifts this to an alignment gap on the *policy* under KL-regularized RL fine-tuning: Align-Gap(π_RLHF) ≥ λ_ψ ε(1−η(u)) / (64 β² L_π D²), where λ_ψ is the minimum eigenvalue of the feature Gram matrix, β the KL regularization strength, and L_π the Lipschitz constant of log π.

The result is motivated by the Egalitarian (Rawlsian) principle from social choice theory: they propose MaxMin-RLHF, which learns a mixture of reward functions via EM clustering and then optimizes the max-min social welfare objective π*_F = argmax_π min_u F_{r*_u}(π). Experiments on GPT-2 and Tulu2-7B validate both the impossibility (single reward RLHF fails minorities) and the MaxMin fix.

## Claim Boundary

- **Quantified over:** one designated subgroup u, the one furthest from the aggregate, in a population modelled as a finite union of |U| subgroups with per-group Bradley–Terry reward parameters φ*_u and a mixing distribution η. Both Lemma 1 and Theorem 1 are lower bounds on the gap for that group. Nothing is claimed uniformly over all groups, and nothing is claimed for populations outside the mixture-of-Bradley–Terry model.
- **Antecedent:** rewards are linear in features, r_φ = ⟨φ, ψ(y, x)⟩, with feature norm bounded by D; the Gram matrix of features has minimum eigenvalue λ_ψ > 0; log π is Lipschitz with constant L_π; the RLHF objective is KL-regularized with strength β; and the diversity gap ε, defined as a difference of total-variation distances between the most diverse pair and the runner-up, is strictly positive. The bound λ_ψ ε(1−η(u)) / (64 β² L_π D²) degenerates to zero as ε → 0 or η(u) → 1, so the impossibility says nothing when subpopulations agree or when the minority is negligible.
- **Which party is constrained:** the aligner, and the constraint is representational — a single scalar reward function must serve the whole population. No party is bounded in computation, samples, queries, or memory. There is no adversary anywhere in the paper.
- **Does not establish:** that RLHF fails against an attacker, that a single reward cannot be learned, or that MaxMin-RLHF closes the gap in general. The lower bound is on the alignment gap of the KL-regularized RLHF policy under the stated parametrization; a nonlinear reward head is outside it, as the page's Open Questions already notes. Nor does the paper establish that the subgroups can be identified from data; it estimates them by EM and gives no guarantee for that step.
- **Abstract vs theorem:** the word "impossibility" carries more than the theorem. What is proved is a quantitative lower bound on a gap that shrinks with the diversity parameter, not that alignment with all subpopulations is impossible. On the page's own framing, "a single scalar reward model cannot simultaneously align an LLM policy with all user subpopulations" holds only in the limit of a bound whose size is set by ε.

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
The first passage was checked against `raw/CQY+24_MaxMinRLHF.pdf` on 2026-08-20 and is verbatim.

> "The assumption of a single ground truth reward is restrictive and can potentially subdue the preferences or opinions of minority groups, leading to societal biases."

> _Not verbatim. Checked against `raw/CQY+24_MaxMinRLHF.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> True to our finding, our work is the first to report such a result in the RLHF literature.

The paper's sentence, verbatim. One word differs, and it is the word that matters — the authors hedge to their knowledge, not to their finding:

> "True to our knowledge, our work is the first to report such a result in the RLHF literature."
