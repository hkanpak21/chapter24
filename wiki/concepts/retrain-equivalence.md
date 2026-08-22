---
title: Retrain Equivalence
type: concept
tags: [adversarial-ml, learning-theory, verifiable-computation]
---

## Definition

**Retrain Equivalence (RE)** is the standard desideratum for
[machine unlearning](machine-unlearning.md): an unlearned model should behave indistinguishably from
one retrained from scratch on the retained data.

Made precise by [Yu, He, Goyal and Arora](../sources/impossibility-retrain-equivalence.md),
Definition 2.1: with `Pred(θ, x) ∈ R^h` on a test set `X_test = {x_i}_{i=1}^m`,

```
d(θ_u, θ_r) := (1/m) Σ_i ‖Pred(θ_u, x_i) − Pred(θ_r, x_i)‖²₂
```

and RE holds when `d(θ_u, θ_r) ≤ ε` for the unlearned `θ_u` and retrained `θ_r`.

The competing desideratum is efficiency: `T_unlearn = o(T_retrain)`. Full retraining satisfies RE
trivially and violates efficiency, which is why practice reaches for **local unlearning**
(Definition 2.2): an algorithm `U(·, D_f)` that uses only gradient information computed on the forget
set. Gradient ascent, NPO and SimNPO are local.

## The hidden assumption

RE presupposes that a model's behaviour is determined by the *multiset* of its training data.
Multi-stage pipelines — pretraining, instruction tuning, alignment — falsify that: the same stages in
a different order reach different internal states. A local rule cannot correct for a history it never
observes.

## Properties / Theorems

From [Yu et al.](../sources/impossibility-retrain-equivalence.md), in overparameterized linear
regression with two-stage proximal ridge training:

- **Lemma 3.2**: under gradient-ascent unlearning, `Δθ_t = (I + M_U)^t Δθ_0` with
  `M_U = (2η/k) X_U^T X_U`. Only the component of `Δθ_0` in the forget span is amplified.
- **Theorem 3.1**: for `t ≥ max(t_0, 0)`,
  `d(θ_AB^{(t)}, θ_BA^{(t)}) ≥ (σ_U² ‖P_U Δθ_0‖²₂ / 4m)(1 + ρ*)^{2t}`.
- **Corollary 1**: past an explicit step count, at least one of the two order-swapped models violates
  RE at tolerance `ε`. **At most one of a pair can be retrain-equivalent — not neither.**
- **The trilemma (§5)**: path-independence, retrain equivalence, locality — at most two of three,
  when the model was trained in stages.

**Scope, stated exactly.** This is *conditional*, and the antecedents are: staged training with
distinct per-stage distributions; a *local* and *path-oblivious* unlearning rule; gradient-ascent
unlearning with `η > 0`; forget matrix `X_U` of full row rank; test set with `m ≥ k` i.i.d. rows from
a continuous distribution. The authors exclude from scope any scheme that uses retain-set information,
modifies training to enable future unlearning, or is a certified procedure with stronger access
assumptions. Under single-stage i.i.d. training — the setting RE was formulated for — none of this
bites. The LLM results (Llama and Qwen, 1B–14B, gradient ascent / NPO / SimNPO, >20% spread in GSM8K
degradation across paths) are experimental confirmation, not theorem.

## A second, independent way RE fails

[Thudi et al.](../sources/auditable-unlearning-definitions.md) attack RE's *measurement* rather than
its reachability: if two disjoint datasets can produce the same parameter trajectory, then
`d(θ_u, θ_r) ≈ 0` is achievable without doing anything, and the predicate certifies nothing. The two
results are disjoint — one says the target is unreachable by a restricted algorithm class, the other
says the target is not a meaningful test — and neither implies the other.

## Where It Appears

- [On the Impossibility of Retrain Equivalence in Machine Unlearning](../sources/impossibility-retrain-equivalence.md)
- [On the Necessity of Auditable Algorithmic Definitions for Machine Unlearning](../sources/auditable-unlearning-definitions.md)
- [Verification of Machine Unlearning is Fragile](../sources/unlearning-verification-fragile.md)

## Related Concepts

- [Machine Unlearning](machine-unlearning.md)
- [Fiber of the Training Map](fiber-of-the-training-map.md) — path dependence says the fibre over a
  weight vector is not a complete description of what produced it.
- [Statistical Query Model](statistical-query-model.md),
  [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md) — the same
  restricted-algorithm-class move, with the *defender* restricted instead of the attacker.

## Open Questions

- Whether path-induced behaviour can be distinguished from algorithm-induced behaviour (the authors'
  own question).
- What replaces RE as a target once it is abandoned. The paper points at benchmarking beyond a single
  retrain baseline and stops there.
- The efficiency constraint `T_unlearn = o(T_retrain)` is the reason locality is imposed at all. It is
  a compute budget on the defender, stated asymptotically and never parameterized — the same omission
  as the extraction cost inequality in
  [Beyond Labeling Oracles](../sources/beyond-labeling-oracles.md) and Property 2 of
  [Proof-of-Learning](../sources/proof-of-learning.md).
