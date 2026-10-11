---
title: Correlational Statistical Query (CSQ) Model
type: concept
tags: [statistical-query, csq, learning-theory, lower-bounds, statistical-computational-gaps]
---

## Definition

A **correlational** statistical query is a query of the form `E[y phi(x)]` — the label enters only linearly, as a correlation. A general **statistical query** ([SQ](statistical-query-model.md)) is `E[phi(x, y)]` for a bounded test function `phi` of *both* arguments. Every CSQ is an SQ; the converse fails, and the failure is not a technicality.

The reason CSQ is the natural class for gradient methods on the square loss is a one-line computation, quoted verbatim from [DPLB24](../sources/generative-exponent-single-index.md):

> "L(θ) = E[(fθ (X) − Y )2 ] =⇒ ∇θ L(θ) = E[(fθ (X) − Y )∇θ fθ (X) ]"

with the bracket labelled "correlational query". Square-loss gradients only ever touch the data through correlational queries.

## Intuition

CSQ cannot pre-process the label. SQ can. That single difference is what separates the [information exponent](information-exponent.md) `l*` from the [generative exponent](generative-exponent.md) `k*`: `k* = inf_T l*((Id ⊗ T)_# P)` over label transformations `T`, so an SQ algorithm can apply `T` and then run a CSQ method, reaching `d^{k*/2}` where CSQ is stuck at `d^{l*/2}`.

[DTA+24](../sources/reusing-batches-breaks-exponents.md) makes the same point from the gradient-descent side, verbatim:

> "The presence of general transformations F in definition 3.1 allows our algorithm to bypass CSQ bounds, which are restricted to F = id. Such general transformations are however permitted under the framework of Statistical Query (SQ) algorithms (Kearns, 1998)."

## Properties / Theorems

- **A CSQ lower bound is not an SQ lower bound.** [ABM23](../sources/leap-complexity-sgd.md) Proposition 2 proves `c d^{Leap}` (Boolean) / `c d^{Leap/2}` (Gaussian) in CSQ. [DIKR25](../sources/robust-multi-index-sq-bounds.md) accordingly describes leap complexity as characterising "the Correlational SQ (CSQ) complexity of learning under certain assumptions". Treating it as SQ erases the entire `l*`-to-`k*` improvement.
- **CSQ bound for single-index models**: `n ≳ d^{max(1,l*/2)}` (Damian–Lee–Soltanolkotabi; also ABM23), which is achieved by loss smoothing (Damian–Nichani–Ge–Lee) and, in the agnostic setting, by [WZDD24](../sources/robust-single-index-efficient.md), whose algorithm "fits the CSQ framework".
- **ABM23's caveat on the CSQ correspondence** (Remark 2): it "may not hold beyond the finite P regime", with an explicit counterexample sketch where CSQ needs zero queries but SGD on a regular network may not succeed.
- SQ and low-degree tests are "almost equivalent" in a precise sense (Brennan–Bresler–Hopkins–Li–Schramm) — but that equivalence is for *SQ*, not CSQ. See [SQ and Low-Degree Almost Equivalent](../sources/brennan-sq-lowdegree-equivalence.md).
- Multi-index adds a further wrinkle: [DLB25](../sources/generative-leap-multi-index.md) notes SQ's "inherent inability to perform certain spectral tasks", so even LDP-to-SQ translation is not automatic there.

## Where It Appears

- [SGD Learning on Neural Networks: Leap Complexity](../sources/leap-complexity-sgd.md) — CSQ lower bounds matching the conjectured SGD scaling.
- [Computational-Statistical Gaps in Gaussian Single-Index Models](../sources/generative-exponent-single-index.md) — CSQ-to-SQ is the paper's central move.
- [Sample and Computationally Efficient Robust Learning of Gaussian Single-Index Models](../sources/robust-single-index-efficient.md) — an agnostic learner that stays inside CSQ.
- [The Benefits of Reusing Batches](../sources/reusing-batches-breaks-exponents.md) — multi-pass GD bypasses CSQ bounds by implicit label transformation.
- [The Merged-Staircase Property](../sources/merged-staircase-property.md) — the paper notes SQ-like arguments "are not expected to be tight" in its regime.
- [On the Hardness of Learning One Hidden Layer Neural Networks](../sources/hardness-one-hidden-layer.md) — motivates going beyond cSQ, which "is known in many settings to be underperforming compared to multiple other natural polynomial-time methods".

## Related Concepts

- [Statistical Query Model](statistical-query-model.md), [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md)
- [Information Exponent](information-exponent.md), [Generative Exponent](generative-exponent.md), [Leap Complexity](leap-complexity.md), [Generative Leap Exponent](generative-leap-exponent.md)
- [Statistical-Computational Gaps](statistical-computational-gaps.md)

## Open Questions

- Whether the SGD-to-CSQ correspondence survives beyond constant latent dimension.
- Whether multi-pass GD with batch reuse actually attains SQ-optimal complexity, as [DTA+24](../sources/reusing-batches-breaks-exponents.md) expects but does not prove.
