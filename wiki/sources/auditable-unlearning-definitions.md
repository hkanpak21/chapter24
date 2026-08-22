---
title: On the Necessity of Auditable Algorithmic Definitions for Machine Unlearning
type: source
date_ingested: 2026-08-20
authors: [Anvith Thudi, Hengrui Jia, Ilia Shumailov, Nicolas Papernot]
venue: 31st USENIX Security Symposium (stated on page 1 of the PDF; ingested copy is arXiv:2110.11891v2, 19 Feb 2022)
year: 2022
tags: [adversarial-ml, reconstruction, hardness-reductions, verifiable-computation]
claim_quantifier: existential
antecedent: "Theorem 3 requires: (i) the update rule g is a mean-sampler (minibatch SGD and relatives); (ii) the adversary chooses its own minibatch size b and can sample from the data distribution D indefinitely; (iii) every point of D has probability 0 under D (continuous distribution); (iv) the verification tolerance ε is strictly positive, justified by floating-point precision. All four hold for standard deep-learning practice but none is vacuous."
---

## Summary

Two claims, at two different strengths, about what unlearning can mean.

The first is a definitional refutation. Approximate unlearning is defined in **parameter space**: a
model has unlearned when its weights are close to those of a model that never saw the point. The
paper observes that identical parameters are reachable from non-overlapping datasets, so proximity in
parameter space cannot certify what was trained on. The consequence is stated bluntly in the
abstract: "one could unlearn without modifying the model at all." If there is a forging map from `D`
to `D \ {x*}`, the owner satisfies the approximate-unlearning definition by doing nothing.

The second is the machinery. **Forgeability** is defined over proof-of-learning logs, not over
models. A valid `(g, d, ε)` log is a sequence `{(w_i, x_i)}` with `d(w_{i+1}, g(w_i, x_i)) ≤ ε`;
`H_D` is the set of such logs from a fixed `w_0` and dataset `D`; a **forging map**
`B : H_D^{g,d,0} → H_{D'}^{g,d,ε}` is the identity on parameters and replaces each `x_i ∈ D` by some
`x̃_i ∈ D'` keeping the log valid. When maps exist both ways, `D` and `D'` are *forgeable*. At `ε = 0`
forgeability is an equivalence relation, and Theorem 1 characterizes its classes: `D` and `D'` are
`ε = 0` forgeable **iff** `H_D(W) = H_{D'}(W)` — the datasets produce exactly the same parameter
sequences.

The existence result is Theorem 3, and its shape matters more than its statement. For a mean-sampler
update rule, with the adversary free to choose the minibatch size `b` and to keep drawing from `D`,
for **every** `ε > 0` and **almost every** dataset `D` there **exists** a superset `D̃ ⊃ D` that is
forged by a **disjoint** `D'`. Corollary 2 then concludes that unlearning on minibatch SGD "is not
well-defined over the logs (and thus the models) of finite datasets", with a proof that turns on
exhibiting one bad instance: "being not well-defined for one instance in the domain ... is
sufficient."

The conclusion the paper draws is scoped accordingly: unlearning cannot be defined at the model or
log level, so it must be defined at the level of the **algorithm**, with external audit. The authors
draw the analogy to Dwork et al. — one cannot reason about privacy at the level of the dataset, only
at the level of the algorithm that touches it.

## Claim Boundary

- **Quantified over:** logs and models, under mean-sampler update rules (minibatch SGD), with a fixed
  initial `w_0`, fixed hyperparameters, and a single `(g, d, ε)`. The forging framework does not
  cover logs from different initializations or different update rules — the paper says it restricts
  to matching `w_0, g, d, ε` "because that is sufficient to prove our results" and leaves the general
  case as future work. Theorem 3 is **existential** twice over: existence of `D̃`, and existence of
  the forging `D'`.
- **Antecedent:** Theorem 3 needs the adversary to control `b` and to sample from `D` indefinitely;
  Corollary 1 obtains forgeability with probability `→ 1` only in the limit `b → ∞`. It also needs
  `ε > 0`, which the paper justifies by floating-point precision, and a continuous `D` (every point
  has probability 0). The probability bound
  `((1 − σ²_max/(bε²))(1 − (σ²_max/(bε²))ⁿ))^{mα}` degrades with small `b`, small `ε`, long logs `m`,
  and many logs `α` — so the result is a large-batch, loose-tolerance phenomenon, not a
  small-batch one.
- **Does not establish:** (a) that unlearning is impossible — the paper's conclusion is that it is
  well-defined *at the algorithmic level*, and it proposes verifiable computation as the route; (b)
  that *certified* unlearning is refuted — §4.3 says certified approaches "have the advantage of
  providing rigorous guarantees at the model level" and need to be *combined with* algorithm-level
  verification that the certified algorithm was in fact the one run; (c) that forging is easy to
  find in practice — Theorem 3 is an existence proof; the practical instantiation is §6, and its own
  caveat is that a forging attack bypassing one PoL verification scheme "may not pass another"; (d)
  an attack on proof-of-learning as such — "we are not proposing an attack against PoL", whose
  original threat model is model stealing, not a dishonest owner.
- **Abstract vs theorem:** "one could unlearn without modifying the model at all" is exactly true
  *when a forging map exists*, and the abstract does not carry that conditional. Similarly "even for
  a given training trajectory one cannot formally prove the absence of certain data points used
  during training" reads as universal; Theorem 3 delivers it existentially, for almost every `D`, in
  a superset `D̃`, under the four antecedents above. The body is scrupulous — Corollary 2's proof
  states the one-instance sufficiency openly — but the abstract is the sweeping version.

## Key Contributions

- The refutation of parameter-space definitions of approximate unlearning.
- **Forgeability** as a formal relation between datasets, defined on PoL logs rather than models.
- Theorem 1: an exact characterization of the `ε = 0` forgeability classes as datasets with identical
  reachable parameter sequences.
- Theorem 3 / Corollary 2: existence of forging examples for minibatch SGD, hence no well-defined
  log-level or model-level notion of unlearning for it.
- The positive proposal: define unlearning **algorithmically** and make the algorithm auditable;
  verifiable computation named as the promising direction.
- An experimental instantiation of a forging attack on standard models and datasets.

## Key Definitions / Theorems

- **Valid `(g, d, ε)` log**: `{(w_i, x_i)}_{i∈J}` with `d(w_{i+1}, g(w_i, x_i)) ≤ ε` for all `i`.
- **`H_D^{g,d,ε}`**: all valid logs from `w_0` on dataset `D`.
- **Forging map**: `B : H_D^{g,d,0} → H_{D'}^{g,d,ε}`, identity on `{w_i}`, mapping `x_i ↦ x̃_i ∈ D'`
  with `d(w_{i+1}, g(w_i, x̃_i)) ≤ ε`. Then "`D'` forges `D` (with ε)". Maps both ways ⟹ `D` and `D'`
  are **forgeable**.
- **Lemma 1**: `ε = 0` forgeable ⟹ `H_D(w) = H_{D'}(w)`.
- **Lemma 2**: `ε = 0` forgeability is an equivalence relation.
- **Theorem 1**: `D` and `D'` are `ε = 0` forgeable **iff** `H_D(W) = H_{D'}(W)`.
- **Theorem 2 (Probabilistic Forging)**: for `D, D'` sampled i.i.d. from `D` with minibatches of size
  `b`, `g` a mean-sampler, `|D'| = n`, `|H_D^{g,d,0}| = α`, log length `≤ m`: `D'` forges `D` with
  `2ε` under `d = ℓ₂` with probability at least
  `((1 − σ²_max/(bε²))(1 − (σ²_max/(bε²))ⁿ))^{mα}`.
- **Corollary 1**: as `b → ∞`, forgeable for every `ε > 0` with probability `→ 1`.
- **Theorem 3 (Existence of Forging Adversary)**: if the adversary controls `b` and can sample from
  `D` indefinitely (every point of probability 0), then for every `ε > 0`, for almost every `D` there
  exists a finite `D̃ ⊃ D` forged by a disjoint finite `D'`.
- **Corollary 2**: unlearning on minibatch SGD is not well-defined over the logs — and hence the
  models — of finite datasets obtained from any `D`.

## Connections

- **The unlearning–forging–fibre triangle, and it is the same object.** A forging map is precisely a
  move within the [fiber of the training map](../concepts/fiber-of-the-training-map.md): two datasets
  that carry the same parameter trajectory are two points of the fibre over that trajectory. Theorem 1
  characterizes the `ε = 0` fibre exactly (`H_D(W) = H_{D'}(W)`); Theorem 3 asserts the fibre is
  *populated by a disjoint dataset*, which is fibre **size**. What it does not do is price the search
  — the forging map is asserted to exist, not constructed efficiently under constraints.
- **That missing half is [Suliman et al.](suliman-data-forging-attacks.md)**, which re-evaluates
  forging in practice and states the obstruction: the gradient-equivalent set is infinite, but the
  members satisfying **domain constraints** are what an attacker needs and no efficient technique is
  known for finding them. Thudi et al. supply the existence; Suliman et al. supply the conjecture that
  navigation is hard. Read as a pair, they are size-vs-navigability for the *training* map — the same
  split [Dinur–Nissim](dinur-nissim-revealing-information.md) made for reconstruction and
  [Kaplan et al.](kaplan-bayesian-memorization-reconstruction.md) restated as
  [computational vs statistical memorization](../concepts/computational-vs-statistical-memorization.md).
- **[Proof-of-Learning](proof-of-learning.md) is the substrate.** Feasibility here is *defined* by
  possession of a PoL log — "the log produced by proof-of-learning is a necessary and sufficient
  condition to define feasibility". The paper explicitly disclaims attacking PoL, whose threat model
  is a thief, not a dishonest owner.
- **[Verification of Machine Unlearning is Fragile](unlearning-verification-fragile.md)** builds
  directly on this and criticizes its forging map as unrealistic — because it holds parameters fixed,
  a verifier receiving repeated proofs would see identical weights each time.
- **[On the Impossibility of Retrain Equivalence](impossibility-retrain-equivalence.md)** attacks the
  *target* of unlearning from a different direction (path dependence under staged training), with a
  disjoint scope: this paper is about definitions over logs and parameters for minibatch SGD; that one
  is about local, path-oblivious algorithms.
- Concepts: [Machine Unlearning](../concepts/machine-unlearning.md),
  [Retrain Equivalence](../concepts/retrain-equivalence.md).

## Open Questions / Limitations

- Forging maps are proved to exist; the cost of finding one is not bounded in either direction. That
  is the whole open problem.
- Composition fails: `B` maps zero-error logs into `ε`-error logs, so forging maps do not compose
  unless `ε = 0`. The paper sketches a fix (`B_ε : H_D^{g,d,ε} → H_{D'}^{g,d,ε}`) and declines to use it.
- The framework fixes `w_0`, `g`, `d`, `ε` across both datasets; varying them is left open.
- Data ordering is unconstrained ("we do not assume any restrictions on data ordering which future
  work could add") — which is precisely the degree of freedom
  [Yu et al.](impossibility-retrain-equivalence.md) later exploits in the opposite direction.
- §7.3 floats `inf{ε : D, D' are ε forgeable}` as a candidate **metric on datasets** modulo the
  `ε = 0` equivalence class. Unpursued, and structurally interesting: it is a distance measured in
  reproduction error rather than in data space.

## Quotes / Notable Passages

> "Thus one could unlearn without modifying the model at all."

> "we show that one cannot prove unlearning simply by comparing points in the parameter space. This
> invalidates all existing approximate approaches to unlearning: they can only justify unlearning by
> the process they are enacting, and not the final outcome of their process"

> "Notably, this means one cannot verify unlearning (exact or approximate) at the model-level as
> there is no universally verifiable unlearning property of the weights."

> "This is the main conclusion of this paper: unlearning cannot be well-defined for minibatch SGD
> over the logs."

> "Note, we assume the verifier can not use ε = 0 simply because of floating point precision."

> "unlearning is only well-defined at the algorithmic level, where an entity's only possible auditable
> claim to unlearning is that they used a particular algorithm designed to allow for external scrutiny
> during an audit."
