---
title: Information Exponent
type: concept
tags: [learning-theory, sample-complexity, single-index-model, statistical-computational-gaps, information-exponent]
---

## Definition

For a population loss of the form `Phi_N(x) = phi(m_N(x))` with `m_N(x) = x · theta_N` the correlation with the planted direction, Ben Arous, Gheissari and Jagannath define the information exponent `k` as the order of the first non-vanishing derivative of `phi` at `m = 0`. Verbatim, [Definition 1.2](../sources/information-exponent-online-sgd.md):

> "We say a population loss ΦN has information exponent k if φ ∈ C k+1 ([−1, 1]) and there exist C, c > 0 such that"

with `d^l phi / dm^l (0) = 0` for `1 <= l < k`, `d^k phi / dm^k (0) <= -c < 0`, and `|| d^{k+1} phi / dm^{k+1} ||_inf <= C`.

For a Gaussian single-index model this is equivalent to the degree of the first non-zero Hermite coefficient of the link. Damian–Pillaud-Vivien–Lee–Bruna restate it as their [Definition 2.2](../sources/generative-exponent-single-index.md):

> "The information exponent of P ∈ G is defined by: l⋆ (P) := min{l ≥ 1; βl ̸= 0} where βl := EP [Y hl (Z)]."

Defilippis–Krzakala–Loureiro–Maillard restate the same object as Eq. (8): `IE(g) = min{k in N : E_{z ~ N(0,1)}[g(z) He_k(z)] != 0}`.

**Notation warning.** BGJ21 writes it `k`; DPLB24 and DLB25 write it `l*` and reserve `k*` for the *generative* exponent; [WZDD24](../sources/robust-single-index-efficient.md) writes the *information* exponent `k*`. Always check which paper's `k*` is meant.

## Intuition

A uniformly random start on the sphere sits at the equator, correlation `m ≈ N^{-1/2}`. The exponent counts how flat the population loss is there. If `phi` has a linear term (`k = 1`) the gradient already points somewhere useful; if the first useful term is order `k`, the drift is `~ m^{k-1}` and the algorithm must fight the noise for `N^{k-1}` samples before it escapes. It is a measure of *initialization flatness*, evaluated only at the start of the trajectory — which is exactly the criticism [ABM23](../sources/leap-complexity-sgd.md) makes of it relative to the leap: "the information exponent is a coefficient that only applies at initialization, while the leap-complexity is a measure of targets that controls the entire learning trajectory".

## Properties / Theorems

- **Threshold for online SGD** ([BGJ21 Theorems 1.3, 1.4](../sources/information-exponent-online-sgd.md)): consistent estimation once `alpha_N >> alpha_c(N,k)` (times polylogs), and total failure to leave the equator once `alpha_N << alpha_c(N,k)`, where `alpha_c(N,k) = 1, log N, N^{k-2}` for `k = 1, 2, >= 3`.
- **Search dominates descent** (Theorem 1.5): for `k >= 2` the descent phase costs only `O(N)` samples.
- **Not composition-invariant.** A label transformation `T` can lower it; that is the entire content of the [generative exponent](generative-exponent.md).
- **CSQ improvement**: with an appropriately smoothed loss the threshold drops to `d^{max(1,l*/2)}`, matching the CSQ lower bound (Damian–Lee–Soltanolkotabi; [ABM23](../sources/leap-complexity-sgd.md)).
- **`beta_* = 1` iff `l* = 2`** ([DKLM26](../sources/noise-sensitivity-exponent.md), Section 2.3).
- **Escaped by batch reuse.** [DTA+24](../sources/reusing-batches-breaks-exponents.md) learns `He_3` (`l* = 3`) in two multi-pass GD steps.

## Comparison table of the candidate units

| Unit | Introduced in | Model class | **Algorithm class priced** | Threshold | Exact relation to the others |
|---|---|---|---|---|---|
| **Information exponent** `l*` (written `k` in BGJ21, `k*` in WZDD24) | [BGJ21](../sources/information-exponent-online-sgd.md) | rank-one estimation on the sphere; Gaussian single-index | **online (single-pass) SGD**, square loss, uniform random start | `M ≍ N^{l*-1}` polylog for `l* >= 3`; `N log N` for `l* = 2`; `N` for `l* = 1`. Lowered to `d^{max(1,l*/2)}` inside CSQ by loss smoothing | upper bound for everything below: `k* <= l*` |
| **Merged-staircase property (MSP)** | [ABM22](../sources/merged-staircase-property.md) | **hypercube** `{+1,-1}^d`, depth-2 mean-field, `P` fixed | one-pass batch-SGD in the mean-field regime | **binary**: strongly `O(d)`-SGD-learnable or not | exactly `Leap = 1` |
| **Leap complexity** `Leap` | [ABM23](../sources/leap-complexity-sgd.md) | low-latent-dimension targets, isotropic Gaussian or hypercube, `P = O_d(1)` | online SGD on a 2-layer net (**conjecture**); the matching lower bound is **CSQ only** | `Theta~(d^{max(Leap,2)})` total time — **stated as Conjecture 1**. Proved: a specialisation, plus CSQ bounds `d^{Leap}` (Boolean) / `d^{Leap/2}` (Gaussian) | reduces to `l*` for single-index; generalises MSP |
| **Generative exponent** `k*` | [DPLB24](../sources/generative-exponent-single-index.md) | Gaussian **single**-index (their Definition 1.1) | **SQ** and **low-degree** | `n = Theta(d^{max(1,k*/2)})`, matching upper and lower bounds | `k* = inf_{T in L^2(P_y)} l*((Id ⊗ T)_# P) <= l*`; **strict iff some square-integrable label transformation lowers the first non-vanishing Hermite index** |
| **Generative leap exponent** `k*` | [DLB25](../sources/generative-leap-multi-index.md) | Gaussian **multi**-index, `r = O_d(1)` | **low-degree** lower bound + an efficient spectral U-statistic upper bound. Explicitly **not SQ** | `n = Theta(d^{1 ∨ k*/2})`, with an unquantified constant `C(P,K)` conjectured to be `exp(r)` | `k* <= l*` against the information leap (their Prop. 3); reduces to DPLB24's `k*` at `r = 1` |
| **Noise sensitivity exponent** `beta_*` | [DKLM26](../sources/noise-sensitivity-exponent.md) | Gaussian single-/multi-index, **even** `sigma` | **AMP / first-order iterative**, in the **proportional** regime `n = alpha d` | `alpha^{Alg} = Theta(lambda^{-beta_*})` vs `alpha^{IT} = Theta(lambda^{-1})` | `beta_* = 1` iff `l* = 2`; `beta_* = infinity` iff `k* > 2`. **Different regime — does not compose with the `d^k` exponents above** |

**Two facts that must travel with the table.**

1. **CSQ is not SQ.** ABM23's matching lower bound is CSQ (correlational queries `E[y phi(x)]`, i.e. `T = id`). The generative exponent improves on it precisely because general SQ queries `E[phi(x,y)]` permit label pre-processing. Reading a CSQ bound as an SQ bound erases the whole `l*`-to-`k*` gap.

2. **These are not intrinsic hardness measures.** [DTA+24](../sources/reusing-batches-breaks-exponents.md) proves that multi-pass gradient descent with **batch reuse** escapes both the information-exponent and the leap barrier, learning a broad class in `T = 2` steps with `n = O(d)`, independently of the leap — disproving ABM23's own conjecture that reuse could only reach `O(d^{max(l/2,1)})`. In their words: CSQ lower bounds, the staircase property, and the information exponent "are limited to online-SGD on Gaussian/Boolean data, and do not describe the class of functions inherently easy or hard to learn by gradient-based methods." Any use of one of these exponents as a *price tag on an adversary* inherits an algorithm-class restriction that a smarter adversary simply steps out of.

## Where It Appears

- [Online SGD on Non-Convex Losses from High-Dimensional Inference](../sources/information-exponent-online-sgd.md) — origin.
- [Computational-Statistical Gaps in Gaussian Single-Index Models](../sources/generative-exponent-single-index.md) — restated as `l*`, superseded within SQ by `k*`.
- [SGD Learning on Neural Networks: Leap Complexity](../sources/leap-complexity-sgd.md) — the leap is its multi-index generalisation.
- [Sample and Computationally Efficient Robust Learning of Gaussian Single-Index Models](../sources/robust-single-index-efficient.md) — priced at `d^{ceil(k*/2)}` in the agnostic setting.
- [The Benefits of Reusing Batches for GD in Two-Layer Networks](../sources/reusing-batches-breaks-exponents.md) — restated as Definition 3.6 and then broken.
- [A Noise Sensitivity Exponent Controls Large Statistical-to-Computational Gaps](../sources/noise-sensitivity-exponent.md) — Eq. (8), and the "too restrictive" critique.

## Related Concepts

- [Generative Exponent](generative-exponent.md), [Leap Complexity](leap-complexity.md), [Generative Leap Exponent](generative-leap-exponent.md), [Noise Sensitivity Exponent](noise-sensitivity-exponent.md)
- [Single-Index Model](single-index-model.md), [Multi-Index Model](multi-index-model.md), [CSQ Model](csq-model.md), [Statistical Query Model](statistical-query-model.md), [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md), [Statistical-Computational Gaps](statistical-computational-gaps.md)

## Open Questions

- Whether the `alpha_c(N,k)` thresholds are sharp without the polylog factors (BGJ21 Section 1.4).
- Whether any resource-bounded *adversary* has ever been priced in these units. As of this ingest, no security or privacy paper in the wiki uses the information exponent as the unit of an attacker's cost; the exponent prices learners only.
