---
title: Online Stochastic Gradient Descent on Non-Convex Losses from High-Dimensional Inference
type: source
date_ingested: 2026-08-20
authors: [Gerard Ben Arous, Reza Gheissari, Aukosh Jagannath]
venue: venue unconfirmed from PDF (arXiv:2003.10409v4 [stat.ML], 10 May 2021; cited elsewhere in this corpus as JMLR 22(106))
year: 2021
tags: [learning-theory, sample-complexity, statistical-computational-gaps, single-index-model, information-exponent, online-sgd]
claim_quantifier: universal
antecedent: "Assumption A (population loss derivative strictly negative on (0,1)) and Assumption B (Definition 1.1 moment bounds on the sample-wise error); population loss of the form Phi_N(x) = phi(m_N(x)) with m_N(x) = x · theta_N; phi in C^{k+1}([-1,1])"
model_class: "Rank-one parameter estimation on the sphere S^{N-1}: the population loss depends on x only through the correlation m_N(x) = x · theta_N. Instantiated for single-layer networks/phase retrieval, GLMs, online PCA, spiked matrix and tensor models, two-component Gaussian mixtures. NOT a statement about neural networks of depth > 1."
algorithm_class: "online SGD (one fresh sample per step), spherical projected update, step size delta_N, uniformly random start on the upper half-sphere"
---

## Summary

This paper introduces the **information exponent** `k` and shows that it alone controls the sample complexity of *online* SGD from a random start for a broad family of rank-one high-dimensional estimation problems. The setting is a parametric family `(P_x)_{x in S^{N-1}}` and a loss `L_N` whose population version has the form `Phi_N(x) = phi(m_N(x))`, `m_N(x) = x · theta_N`. The information exponent is the order of the first non-vanishing derivative of `phi` at `m = 0` — the equator of the sphere, which is where a uniformly random start concentrates.

The main results are matching upper and lower thresholds on the number of samples `M = alpha_N · N`. Writing `alpha_c(N,k) = 1` for `k = 1`, `log N` for `k = 2`, and `N^{k-2}` for `k >= 3`, Theorem 1.3 gives consistent estimation (strong recovery, `m_N(X_M) -> 1`) once `alpha_N` exceeds `alpha_c(N,k)` by the stated polylog factors, and Theorem 1.4 shows that if `alpha_N << alpha_c(N,k)` then `sup_{t<=M} |m_N(X_t)| -> 0`, i.e. the algorithm never even leaves the equator. In total-sample terms this is `M ≳ N^{k-1}` polylog for `k >= 3`.

Theorem 1.5 adds the structural picture that motivates the name: for `k >= 2` essentially all of the data is consumed in the *search* phase (attaining any macroscopic correlation), while the *descent* phase from `eta` to `1 - eta` correlation costs only `O(N)` samples regardless of `k`. The paper explicitly avoids convexity, quasi-convexity, and uniform derivative bounds, replacing them with the moment conditions of Definition 1.1 (Assumption B).

The authors themselves flag the algorithmic narrowness of the classification and anticipate the batch-reuse question: they expect the classification to have "broader implications for efficient estimation thresholds than the setting we consider here, such as finite rank estimation, or offline algorithms with possibilities of reuse, batching, and overparametrization." That anticipated extension is exactly where the classification later breaks — see [Reusing Batches Breaks the Information and Leap Exponents](reusing-batches-breaks-exponents.md).

## Claim Boundary

- **Quantified over:** all information exponents `k >= 1` and all `(P_N, L_N)` sequences satisfying Assumptions A and B, for the *single* algorithm online SGD from a uniform random start. Thresholds are on `alpha_N = M/N`, not on runtime.
- **Model class and data assumption:** rank-one estimation on the sphere with population loss a function of the correlation only, plus the moment scaling of Definition 1.1. The parameter norm is *assumed known*. The examples in Section 2 include a single-layer network with a general activation, so the result touches neural networks only at the single-neuron level. This is not a result about depth-2 or deeper networks, and not a result about multi-index models.
- **Algorithm class:** online SGD with one fresh sample per step (`online`). The lower bound Theorem 1.4 is a statement about *this algorithm* — it is not an SQ, CSQ, or low-degree lower bound, and it is not information-theoretic. Theorem 1.3's guarantee holds only inside the step-size window `alpha_N^{-1} << delta_N << alpha_N^{-1/2}`; Theorem 1.4's refutation covers a wider `delta_N` range.
- **Does not establish:** that `N^{k-1}` is the complexity of the estimation task for efficient algorithms. Later work lowers it to `d^{max(1,k/2)}` inside CSQ by smoothing the loss, to `d^{k*/2}` with `k* <= k` by label pre-processing ([generative exponent](generative-exponent-single-index.md)), and to `O(d)` for a broad class by reusing batches ([DTA+24](reusing-batches-breaks-exponents.md)). The information exponent is a property of single-pass gradient descent on the square loss, **not** an intrinsic hardness measure of the model.
- **Abstract vs theorem:** none found. The abstract is careful — it says "the simplest version of SGD, namely online SGD" and "thresholds depend only on an intrinsic property of the population loss". The word "intrinsic" refers to the *population loss*, not to the learning problem's complexity; reading it as intrinsic hardness is the error to guard against.

## Key Contributions

- Definition of the information exponent (Definition 1.2) as a classification of rank-one estimation problems on the sphere.
- Matching sample-complexity thresholds `alpha_c(N,k)` for online SGD, upper (Theorem 1.3) and lower (Theorem 1.4), sharp up to `(log N)^2`.
- Search-versus-descent decomposition (Theorem 1.5): the descent phase costs `O(N)` samples independently of `k`, so the whole cost is the escape from the equator.
- Assumption B (Definition 1.1) as a scaling regime that replaces `O(1)`-smoothness and actually holds for standard high-dimensional losses.
- A law-of-large-numbers trajectory result for the descent phase (Theorem 3.2).

## Key Definitions / Theorems

**Definition 1.2 (information exponent), verbatim:**

> "We say a population loss ΦN has information exponent k if φ ∈ C k+1 ([−1, 1]) and there exist C, c > 0 such that"

followed by the display: `d^l phi / dm^l (0) = 0` for `1 <= l < k`; `d^k phi / dm^k (0) <= -c < 0`; `|| d^{k+1} phi / dm^{k+1} (m) ||_inf <= C`.

**Threshold (1.6), verbatim:** `alpha_c(N,k) = 1` for `k = 1`, `log N` for `k = 2`, `N^{k-2}` for `k >= 3`.

**Theorem 1.3 (upper bound).** Under Assumptions A and B with information exponent `k`, `M = alpha_N N` with `alpha_N^{-1} << delta_N << alpha_N^{-1/2}`, and `alpha_N >> alpha_c(N,1)` (`k=1`) / `alpha_c(N,2) log N` (`k=2`) / `alpha_c(N,k)(log N)^2` (`k>=3`): online SGD from `X_0 ~ mu_N` has `m_N(X_M) -> 1`.

**Theorem 1.4 (lower bound).** If `alpha_N << alpha_c(N,k)` (with `delta_N = O(1)` for `k <= 2`, `delta_N = O(alpha_N^{-1/2})` for `k >= 3`) then `sup_{t <= M} |m_N(X_t)| -> 0`.

**Theorem 1.5.** For `k >= 2`, weak-recovery time `tau_eta^+ >> alpha_c(N,k)` and `|tau_{1-eta}^+ - tau_eta^+| <= CN` w.p. `1 - o(1)`.

## Connections

- Concept page: [Information Exponent](../concepts/information-exponent.md).
- Superseded inside SQ by the [generative exponent](../concepts/generative-exponent.md) — see [Computational-Statistical Gaps in Gaussian Single-Index Models](generative-exponent-single-index.md).
- Extended from single- to multi-index by [Leap Complexity](leap-complexity-sgd.md) (still CSQ-matched) and then by the [generative leap](generative-leap-multi-index.md).
- **Load-bearing caveat:** [The Benefits of Reusing Batches for GD in Two-Layer Networks](reusing-batches-breaks-exponents.md) shows multi-pass GD with batch reuse escapes the information-exponent barrier entirely, reducing sample complexity to `O(d)` for a broad class. Any use of `k` as an adversary's price tag inherits the online-SGD restriction.
- A competing unit for a different algorithm class: [A Noise Sensitivity Exponent Controls Large Statistical-to-Computational Gaps](noise-sensitivity-exponent.md), which argues the information exponent "can be easily bypassed by data reuse".
- Used as the priced quantity in [Sample and Computationally Efficient Robust Learning of Gaussian Single-Index Models](robust-single-index-efficient.md), where the same symbol is written `k*`.
- Related concepts: [Single-Index Model](../concepts/single-index-model.md), [Statistical Query Model](../concepts/statistical-query-model.md), [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md).
- Authors: [Gerard Ben Arous](../entities/gerard-ben-arous.md), [Aukosh Jagannath](../entities/aukosh-jagannath.md).

## Open Questions / Limitations

- The authors expect `alpha_c(N,k)` without the extra logs to be sharp (Section 1.4) but do not prove it.
- The restriction to the sphere and to known parameter norm; they conjecture a similar classification in full space with an `l2` penalty.
- No claim about offline, batched, reused, or overparametrised algorithms — flagged as future work in the introduction and subsequently resolved *against* the exponent by DTA+24.
- Assumption A is an assumption on the unknown data distribution and, as the paper notes, "cannot be empirically verified."

## Quotes / Notable Passages

> "our results do not assume uniform control on the loss itself, such as convexity or uniform derivative bounds"

> "except for the simplest tasks, almost all of the data is used simply in the initial search phase to obtain non-trivial correlation with the ground truth"

> "offline algorithms with possibilities of reuse, batching, and overparametrization"
