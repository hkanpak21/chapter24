---
title: Membership Inference Game
type: concept
tags: [adversarial-ml, computational-indistinguishability, differential-privacy, sample-complexity]
---

## Definition

A two-party security game. A challenger trains a model; the adversary, given a challenge point and some
access to the model, must decide whether that point was in the training set.

The reference form is Definition 1 of
[Carlini et al., MIA From First Principles](../sources/mia-from-first-principles.md), itself adapted
from Yeom et al. and Jayaraman et al.:

1. Challenger samples `D ← 𝔻` and trains `f_θ ← T(D)`.
2. Challenger flips a bit `b`. If `b = 0`, draws a fresh `(x,y) ← 𝔻` with `(x,y) ∉ D`; if `b = 1`, draws
   `(x,y) ←$ D`.
3. Challenger sends `(x,y)` to the adversary.
4. Adversary, with query access to `𝔻` and to `f_θ`, outputs `b̂`.
5. Output 1 iff `b̂ = b`.

Attacks output a real-valued score and threshold it: `A(x,y) = 1[A'(x,y) > τ]`.

**The two worlds.** Read as a hypothesis test, the game asks the adversary to distinguish two
distributions over models,

```
Q_in(x,y)  = { f ← T(D ∪ {(x,y)}) | D ← 𝔻 }
Q_out(x,y) = { f ← T(D \ {(x,y)}) | D ← 𝔻 }
```

By Neyman–Pearson the optimal test at fixed false positive rate thresholds the likelihood ratio
`p(f | Q_in) / p(f | Q_out)`. This is intractable over model parameters, so LiRA substitutes the ratio
over the scalar `ℓ(f(x),y)` under two fitted Gaussians.

## Intuition

The game is a distinguishing game, and everything interesting about it is in **what is randomized**.
Three quantities can each be fixed or drawn:

- the training set `D`,
- the challenge point `x`,
- the training randomness.

Choosing differently gives different security notions, and the literature has moved along this axis
without always saying so:

- **Both random** (the definition above) — an average-case notion. What is measured is a property of a
  data *population*.
- **Point fixed, dataset and training random** — the sample-level notion of
  [Aerni–Zhang–Tramèr](../sources/privacy-defense-evaluations-misleading.md), with a per-sample
  threshold `T_x`. Measures whether *this* individual is exposed.
- **Both adversarial** — differential privacy. DP bounds the TPR-to-FPR ratio of any MI attack
  distinguishing `D` from `D ∪ {x}`, with probability taken over the mechanism only, *for every* `D`
  and `x`.

Ye et al.'s **fixed-record versus fixed-model** distinction (reported in
[MSJ+25](../sources/sok-mia-llms-rushing-nowhere.md)) is the operational version of the same axis: in a
fixed-record game many models are trained with the target in or out; in a fixed-model game one model is
trained and targets are sampled IID. The first requires retraining; the second requires an IID
non-member set.

**Both requirements fail at foundation-model scale, and that failure generated an entire literature.**
Retraining is unaffordable, and an IID non-member set is unavailable when the training set is unknown.
The substitute — collecting likely members and likely non-members *post hoc*, from different time
windows or different sources — is not the game. It is a different distinguishing problem, and a
model-free classifier often solves it better (see [Blind Baseline](blind-baseline.md)).

## Properties / Theorems

- **Optimal test.** Neyman–Pearson gives the likelihood-ratio test as optimal at fixed FPR. Realizing it
  requires estimating `Q_in` and `Q_out`, i.e. training shadow models — the step that does not scale.
- **Dilution.** Under population-level evaluation the "name and shame" mechanism `NS_x̂`, which reveals
  membership of one fixed point and nothing else, satisfies `TPR ≤ FPR + 1/|D|`. So a population metric
  can be driven arbitrarily low by enlarging `D` while an individual stays fully exposed
  ([AZT24](../sources/privacy-defense-evaluations-misleading.md) §4.1).
- **The null must be samplable.** Bounding the false positive rate
  `Pr_{f ~ Train(D_0)}[T(f,x) ∈ S]` requires drawing models trained without `x`. Where the training set
  and procedure are unknown and retraining is unaffordable, this probability cannot be estimated at all
  — the argument of [ZDKT25](../sources/mia-cannot-prove-training.md). A **rank-based** variant escapes
  this: if `x` is drawn uniformly from a candidate set `X` independently of training, then rejecting
  when `rank(f, x, X) ≤ k` has `FPR ≤ k/|X|` with no retraining (Lemma 1).
- **The membership predicate may not be well defined.** With web-scale corpora, non-members share long
  n-grams with members at rates of 30–77%
  ([DSM+24](../sources/do-mias-work-on-llms.md)), and a one-token edit to a member is classified as a
  non-member with high confidence while carrying the same information. Exact-match membership is not
  the predicate a privacy auditor wants, and standard DP does not cover the near-member case.

## Where It Appears

- [MIA From First Principles (CCNSTT22)](../sources/mia-from-first-principles.md) — Definition 1, the
  two worlds, LiRA.
- [MIA Cannot Prove Training (ZDKT25)](../sources/mia-cannot-prove-training.md) — the two-worlds
  construction with an explicit coin flip by the developer; Lemma 1; the claim that the null is
  unsamplable for production models.
- [Privacy Defense Evaluations are Misleading (AZT24)](../sources/privacy-defense-evaluations-misleading.md)
  — population-level versus sample-level instantiation; the dilution bound.
- [SoK: MIAs on LLMs are Rushing Nowhere (MSJ+25)](../sources/sok-mia-llms-rushing-nowhere.md) —
  sequence-, document- and dataset-level variants; fixed-record versus fixed-model; post-hoc collection
  as a failed instantiation.
- [Do MIAs Work on LLMs? (DSM+24)](../sources/do-mias-work-on-llms.md) — the fuzzy-boundary attack on
  the membership predicate itself.
- [On the Difficulty of MIA (RL21)](../sources/difficulty-of-mia.md) — the base-rate problem: in
  deployment the non-member class dominates, and the true ratio is unestimable.
- [Sample Complexity of Membership Inference](../sources/haghifam-sample-complexity-mia.md) — how many
  samples the adversary in this game needs.

## Related Concepts

- [Low-FPR Evaluation Regime](low-fpr-evaluation-regime.md) — how success in this game should be scored.
- [Blind Baseline](blind-baseline.md) — the null the game's score must be read against.
- [Computational vs Statistical Memorization](computational-vs-statistical-memorization.md) — what a win
  in this game is evidence *of*.
- [Fiber of the Training Map](fiber-of-the-training-map.md) — the two worlds are two fibers; the game
  asks a bounded party which one `f` came from.
- [Computational Indistinguishability](computational-indistinguishability.md).

## Open Questions

- **Where on the randomization axis should the game sit?** AZT24 §6 poses this directly: the average-case
  extreme is diluted, the DP worst case is often called too pessimistic, and nothing in between has been
  argued for on principle. *"we thus need to clearly define the privacy semantics that the evaluation
  targets."*
- **What replaces exact membership?** DSM+24 proposes a semantic MI game with members defined by
  embedding proximity and does not build it. Nothing in this wiki formalizes approximate membership.
- **The bounded-verifier version.** ZDKT25 names retraining cost as an obstruction and does not
  quantify it. There is no notion here of a membership proof that is sound relative to a verifier with a
  stated compute budget, and no lower bound saying one is impossible.
