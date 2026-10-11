---
title: On the Impossibility of Retrain Equivalence in Machine Unlearning
type: source
date_ingested: 2026-08-20
authors: [Jiatong Yu, Yinghui He, Anirudh Goyal, Sanjeev Arora]
venue: "arXiv:2510.16629"
venue_evidence: "arXiv abstract page carries no Journal reference; OpenReview https://openreview.net/forum?id=r6Z3BXDrzO exists (submission under review) with no confirmed acceptance visible; dblp.org was unreachable this session (repeated ECONNRESET) — no refereed venue confirmed anywhere, kept as arXiv-only"
year: 2025
tags: [adversarial-ml, learning-theory, hardness-reductions]
claim_quantifier: conditional
antecedent: "The theorem holds only under: (i) overparameterized linear regression, two-stage proximal ridge training with the two stages in opposite orders; (ii) a *local* unlearning algorithm — updates use forget-set gradients only; (iii) the algorithm is *path-oblivious* — it does not know the learning history; (iv) gradient-ascent unlearning with step size η > 0; (v) forget matrix X_U of full row rank; (vi) a test set with m ≥ k i.i.d. rows from a continuous distribution; (vii) t ≥ max(t_0, 0). Staged training with distinct per-stage distributions is the empirical hypothesis, and it does hold of contemporary LLM pipelines."
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: mechanism
cls_unit: algo class
cls_tightness: class
cls_baseline: n/a
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: time
cls_assessed: implicit
cls_evidence: "An unlearning algorithm U(·, Df) is considered local if it only requires gradient information computed on the forget set Df."
cls_evidence_src: Def 2.2
cls_reason: "party=mechanism per Rule 3: the locality/path-oblivious bound binds the unlearning algorithm, not an attacker. No adversary is modeled (Claim Boundary point e), so target/family/phase/access/write are none/n/a. second_notion=time and assessed=implicit record 'unlearning algorithms should have runtime independent of the retain data size' (§1), a motivating side-condition never formalized as a theorem parameter. baseline=stated: Def 2.1 (RE) measures distance to the fully retrained model θ_r."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

Retrain Equivalence (RE) — the requirement that an unlearned model behave like one retrained from
scratch on the retained data — presupposes that model behaviour is a function of the *multiset* of
training data. Modern pipelines break that presupposition: pretraining, instruction tuning and
alignment are distinct stages with distinct distributions, and the *order* of stages leaves a trace
in the weights. The paper's thesis is that a local unlearning rule, which sees only forget-set
gradients and not the learning history, cannot compensate for a trace it cannot see.

The theory is a clean amplification argument in overparameterized linear regression. Two models
`θ_AB` and `θ_BA` are trained on the same two datasets in opposite orders by proximal ridge updates
regularized to the previous iterate. Both then undergo gradient-ascent unlearning on the same forget
set `S_U`. Lemma 3.2 gives the weight difference exactly: `Δθ_t = (I + M_U)^t Δθ_0` with
`M_U = (2η/k) X_U^T X_U`. Only the component of `Δθ_0` inside the forget span is amplified; the
orthogonal part is untouched. Theorem 3.1 lower-bounds the RE distance between the two unlearned
models by `(σ_U² ‖P_U Δθ_0‖²) / 4m · (1 + ρ*)^{2t}` — exponential in unlearning steps. Corollary 1
then converts this into the actual claim: for any RE tolerance `ε`, past a computable step count at
most one of the two models can be within `ε` of the single retrained target. **Not that neither can
be — that at most one can.**

The experiments carry the phenomenon to LLMs: Llama and Qwen bases (1B–14B) finetuned on four
identical datasets in four different orderings, then unlearned with gradient ascent, NPO and SimNPO.
Divergence appears within a few steps; GSM8K degradation after unlearning varies by over 20% across
paths. Two named phenomena fall out — a **recency effect** (unlearning is slowest when the forget set
was learned last) and **path-dependent superficial forgetting**, where whether probability mass moves
to paraphrases or to alternative concepts depends on the learning path.

The conclusion the authors state is a trilemma, not an impossibility: **path-independence,
retrain equivalence, locality — at most two of three**, when the model was trained in stages.

## Claim Boundary

- **Quantified over:** *path-oblivious, local* unlearning algorithms applied to models trained in
  multiple stages with distinct per-stage distributions. Locality is Definition 2.2: updates use only
  gradient information computed on the forget set. The theorem itself quantifies over a specific
  construction — a *pair* of overparameterized linear models trained by two-stage proximal ridge
  regression in opposite orders, unlearned by gradient ascent.
- **Antecedent:** staged training with order-varying histories. Under i.i.d. single-stage training —
  the setting RE was originally formulated for, as the abstract says — nothing here applies. The
  paper states its exclusions itself: "Our work does not discuss the hardness of retrain equivalence
  for unlearning schemes that (i) use retain-set information, (ii) modify the training process to
  enable future unlearning, or (iii) rely on certified procedures with stronger assumption of model
  or data access." Certified `(ε, δ)`-unlearning is explicitly placed outside scope.
- **Does not establish:** (a) that RE is unachievable — full retraining trivially satisfies it, as the
  paper notes in §1, and any non-local method that reads the retain set is out of scope; (b) that
  unlearning is impossible; (c) an impossibility for a *single* model — the theorem is about a pair
  with different histories and says at most one can meet the target; (d) anything for deep networks
  as a theorem — §4 opens by conceding "it is hard to perform an analogous theoretical analysis for
  LLMs powered by deep neural networks", and the LLM results are experimental; (e) any statement about
  adversaries or security — this is a specification defect, not an attack.
- **Abstract vs theorem:** the title says "Impossibility"; the theorem says exponential divergence
  between two histories. The abstract's own hedge is the accurate version — "making it impossible for
  path-oblivious algorithms to **universally** achieve Retrain Equivalence", and "so long as the
  target models are trained in stages". The unhedged reading — that retrain equivalence is impossible
  — is not what is proved and not what the paper claims. §5's trilemma is the honest summary and
  should be preferred over the title when citing.

## Key Contributions

- Definition 2.1 (Retrain Equivalence) and Definition 2.2 (Local Unlearning) written down explicitly.
- Theorem 3.1: exponential divergence of two order-swapped models under identical local unlearning.
- Corollary 1: an explicit step count past which RE is violated for at least one of the pair.
- LLM experiments across two model families and three unlearning algorithms confirming path
  dependence within few steps.
- Two empirical phenomena: the recency effect, and path-dependent superficial vs deep forgetting.
- The impossibility triangle: path-independence, retrain equivalence, locality — pick two.

## Key Definitions / Theorems

- **Definition 2.1 (Retrain Equivalence)**: with `Pred(θ, x) ∈ R^h`,
  `d(θ_u, θ_r) := (1/m) Σ_i ‖Pred(θ_u, x_i) − Pred(θ_r, x_i)‖²₂`; RE holds when `d(θ_u, θ_r) ≤ ε`.
- **Definition 2.2 (Local Unlearning)**: `U(·, D_f)` is local if it requires only gradient information
  computed on the forget set `D_f`. Examples given: gradient ascent, NPO, SimNPO.
- **Staged training**: `L(θ; X, y, θ_prev, µ) = ‖Xθ − y‖²₂ + µ‖θ − θ_prev‖²₂`, giving
  `θ_AB = (X_B^T X_B + µ_B I)^{-1}(X_B^T y_B + µ_B θ_A)` and symmetrically for `θ_BA`.
- **Lemma 3.2**: `Δθ_t = (I + M_U)^t Δθ_0`, `M_U = (2η/k) X_U^T X_U`.
- **Theorem 3.1**: with `P_U = X_U^T (X_U X_U^T)^{-1} X_U`,
  `ρ* = ⟨P_U Δθ_0, M_U P_U Δθ_0⟩ / ‖P_U Δθ_0‖²₂`, `σ_U = σ_min(X_test P_U)`, there is `t_0` such that
  for all `t ≥ max(t_0, 0)`,
  `d(θ_AB^{(t)}, θ_BA^{(t)}) ≥ (σ_U² ‖P_U Δθ_0‖²₂ / 4m) (1 + ρ*)^{2t}`.
- **Corollary 1**: for tolerance `ε` and `t* ≥ max( (log(16mε) − log(σ_U² ‖P_U Δθ_0‖²₂)) / (2 log(1+ρ*)), t_0 )`,
  at least one of `d(θ_AB^{(t*)}, θ_r) > ε` or `d(θ_BA^{(t*)}, θ_r) > ε` holds.
- **The trilemma (§5)**: of path-independence, retrain equivalence, and locality, at most two can hold
  simultaneously when the model was trained in stages.

## Connections

- **Complementary, not overlapping, with
  [Thudi et al.](auditable-unlearning-definitions.md).** Thudi et al. refute definitions written over
  *parameters and logs* for minibatch SGD, by exhibiting forgeability. Yu et al. leave the definition
  intact and show the *target* is unreachable by a restricted algorithm class under staged training.
  One is about what unlearning means; the other about what a path-oblivious local rule can hit. Both
  are narrow, and neither is a general impossibility.
- **The restriction is the interesting part.** "Local" and "path-oblivious" are restrictions on the
  *algorithm class*, and the negative result is relative to that class — the same shape as
  restricted-adversary-class results elsewhere in this wiki (SQ, low-degree). Here the restricted
  party is the defender, not the attacker. Compare
  [statistical-query-model](../concepts/statistical-query-model.md) and the
  [low-degree-polynomial-framework](../concepts/low-degree-polynomial-framework.md) for the same move
  in units the programme uses.
- **The cost axis is present but unpriced.** The reason locality is imposed at all is computational:
  "unlearning algorithms should have runtime independent of the retain data size", `T_unlearn =
  o(T_retrain)`. That is a compute-budget constraint on the defender, stated asymptotically and never
  parameterized — structurally the same omission as the cost inequality in
  [Beyond Labeling Oracles](beyond-labeling-oracles.md) and Property 2 of
  [Proof-of-Learning](proof-of-learning.md).
- Path dependence is a statement about the **trajectory**, not the endpoint, which is the same
  observation Thudi et al. make from the other side ("it is the trajectories taken by the optimization
  algorithm ... during training"). Both point at
  [fiber-of-the-training-map](../concepts/fiber-of-the-training-map.md): the fibre over a weight
  vector is not a complete description of what produced it.
- Concepts: [Retrain Equivalence](../concepts/retrain-equivalence.md),
  [Machine Unlearning](../concepts/machine-unlearning.md).

## Open Questions / Limitations

- The theorem lives in overparameterized linear regression; transfer to deep networks is argued by
  analogy (implicit bias, benign overfitting) and demonstrated only experimentally.
- No treatment of non-local methods, retain-set regularized methods, training-time-modified methods,
  or certified unlearning — all excluded by the authors.
- The authors' own open questions: whether path-induced behaviour can be distinguished from
  algorithm-induced behaviour, and what role the recency effect plays in RL post-training methods that
  also perform gradient ascent on undesired answers.
- The trilemma is asserted from the theorem plus the scaling argument against non-local methods; it is
  not itself proved as a three-way impossibility.

## Quotes / Notable Passages

> "The theory indicates that the outcome of local unlearning—methods that only use gradients computed
> on the forget set—is path-dependent."

> "making it impossible for path-oblivious algorithms to universally achieve Retrain Equivalence."

> "These results consistently show that Retrain Equivalence is an ill-posed target for local
> unlearning algorithms, so long as the target models are trained in stages."

> "Our work does not discuss the hardness of retrain equivalence for unlearning schemes that (i) use
> retain-set information, (ii) modify the training process to enable future unlearning, or (iii) rely
> on certified procedures with stronger assumption of model or data access."

> "Our findings surface an impossibility triangle that governs three desiderata for unlearning
> algorithms: (1) path-independence ... (2) retrain equivalence, and (3) locality ... at most two out
> of the three desiderata can be satisfied simultaneously."
