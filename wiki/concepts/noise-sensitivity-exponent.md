---
title: Noise Sensitivity Exponent
type: concept
tags: [statistical-computational-gaps, approximate-message-passing, single-index-model, multi-index-model, noise-sensitivity-exponent]
---

## Definition

Defilippis, Krzakala, Loureiro and Maillard define, for an activation `sigma : R -> R` of polynomial growth, [Definition 2.1](../sources/noise-sensitivity-exponent.md), verbatim:

> "The noise-sensitivity exponent is defined as"

followed by the display "β⋆ (σ) := min{β ∈ N : Ez∼N (0,1) σ β (z)(z 2 − 1) ̸= 0}".

## Intuition

`E[sigma^beta(z)(z^2 - 1)]` is the second-Hermite coefficient of the `beta`-th power of the activation. The NSE asks how many powers of the activation you must take before a second-Hermite signal appears. Since AMP's weak-recovery threshold in the proportional regime is `alpha^{Alg}_{WR} = (E_y[(E[z^2 - 1 | y])^2])^{-1}` and a large-noise expansion of that expression is driven by exactly these moments, `beta_*` reads off how fast the AMP threshold degrades as the signal-to-noise ratio falls.

## Properties / Theorems

- **Single-index, additive Gaussian noise, even `sigma`** ([Theorem 3.2](../sources/noise-sensitivity-exponent.md)): the optimal AMP algorithm achieves weak recovery exactly for `alpha > alpha^{Alg}_{WR}` with `alpha^{Alg}_{WR} = Theta(lambda^{-beta_*})` as `lambda -> 0`; while `alpha^{IT}_{WR} = Theta(lambda^{-1})` (Theorem 3.3). Hence a gap of size `Theta(lambda^{-beta_*})` when `beta_* > 1`.
- **Committee machines**: `alpha^{IT}_{spec} = Theta_p(p)`; `alpha^{Alg}_{spec} = Theta_p(p)` iff `beta_* = 1`; `= Theta_p(p^{beta_*})` for even activations. The general-activation case (Result 4.3) rests on statistical-physics arguments and a committee-symmetry ansatz and is "currently non-rigorous".
- **Hierarchical models** (Theorem 5.2): `alpha_k^{Alg} = Theta_k(k^{2 gamma beta_*})`. The information-theoretic counterpart `alpha_k^{IT} = Theta(k^{2 gamma})` is **Open Question 5.4**; only `>= C k^{2 gamma}` is rigorous, so the gap in this case is conjectural.
- **Classification**: `beta_* = 1` iff the information exponent is 2; `beta_* = 2` covers "the majority of functions with zero second Hermite coefficient", and all polynomials of degree `< 20`; `beta_* > 2` exists but is "usually fine-tuned"; `beta_* = infinity` iff the generative exponent exceeds 2.

## The composition warning

The NSE prices **AMP and first-order iterative methods in the proportional regime `n = alpha d`**. The [information exponent](information-exponent.md), [leap complexity](leap-complexity.md), [generative exponent](generative-exponent.md) and [generative leap exponent](generative-leap-exponent.md) all price a different algorithm class *and a different sample-complexity regime*: polynomial scalings `n ≍ d^{k}` with `k` fixed as `d -> infinity`, against online SGD, CSQ, SQ, or low-degree algorithms. `beta_*` appears as an exponent of `lambda`, `p`, or the feature index `k` — never of `d`. **The NSE therefore does not compose with the `d^k` exponents; do not chain a `beta_*` bound with a `d^{k*/2}` bound.**

## The brittleness argument

The paper's motivation is a sustained critique of the earlier units, and it is worth recording as an argument rather than a claim. Verbatim:

> "The information exponent, in particular, turns out to be too restrictive, as it can be easily bypassed by data reuse or by training with non-square losses"

> "with the notable exception of parity-like problems, functions in this class are typically fine-tuned and unstable: small perturbations of the target function often collapse them back into easier regimes ... As a result, these hardness classes appear brittle and arguably non-generic."

> "A more natural and robust classification instead emerges from the study of symmetries of the target function."

The evidential base for the brittleness half is largely by citation (Troiani et al., Cornacchia et al.), plus the independent corroboration inside the exponent literature itself: [DPLB24](../sources/generative-exponent-single-index.md) Example 2.7 (polynomial links have `k* <= 2`) and [DLB25](../sources/generative-leap-multi-index.md) Propositions 5 and 6 (piecewise-linear links and generic linear transformations give `k* <= 2`).

## Where It Appears

- [A Noise Sensitivity Exponent Controls Large Statistical-to-Computational Gaps in Single- and Multi-Index Models](../sources/noise-sensitivity-exponent.md) — origin.

## Related Concepts

- [Information Exponent](information-exponent.md), [Generative Exponent](generative-exponent.md), [Leap Complexity](leap-complexity.md), [Generative Leap Exponent](generative-leap-exponent.md)
- [Single-Index Model](single-index-model.md), [Multi-Index Model](multi-index-model.md), [Statistical-Computational Gaps](statistical-computational-gaps.md), [Statistical Query Model](statistical-query-model.md)

## Open Questions

- Open Question 5.4: the information-theoretic threshold for hierarchical models.
- Making Result 4.3 (general activations, committee machines) rigorous.
- Universality beyond Gaussian covariates.
- Whether the NSE has any counterpart pricing an *adversary* rather than a learner. None exists as of this ingest.
