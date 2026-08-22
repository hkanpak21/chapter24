---
title: Algorithms and SQ Lower Bounds for Robustly Learning Real-valued Multi-index Models
type: source
date_ingested: 2026-08-20
authors: [Ilias Diakonikolas, Giannis Iakovidis, Daniel M. Kane, Lisheng Ren]
venue: venue unconfirmed from PDF (arXiv:2505.21475v1 [cs.LG], 27 May 2025; cited elsewhere as NeurIPS 2025)
year: 2025
tags: [statistical-query, multi-index-model, agnostic-learning, adversarial-label-noise, sample-complexity, statistical-computational-gaps]
claim_quantifier: conditional
antecedent: "Upper bound (Theorem 1.4) requires the target class to lie in F(K, m, zeta, tau, sigma), the well-behaved MIMs of Definition 1.3 (bounded gradient/second moment, L2-close to bounded, and for every subspace V either V-approximability or a degree-<= m distinguishing conditional moment). Lower bound (Theorem 1.10) requires a rotationally invariant K-MIM class, relative degree-m moment matching (Definition 1.9), a tau-inapproximability condition, and 'the mild assumption that the extreme values of y have small contribution to the variance'."
model_class: "K-MIMs f: R^d -> R depending only on the projection onto a K-dimensional subspace, under the standard Gaussian x-marginal. Real-valued, square loss, agnostic (arbitrary labels). Applications: positive-homogeneous L-Lipschitz K-MIMs, hence Lipschitz homogeneous ReLU networks. NOT general neural networks."
algorithm_class: "SQ (STAT(tau) oracle) for the lower bound; an iterative subspace-finding moment algorithm for the upper bound. The lower bound is SQ, not CSQ and not low-degree."
---

## Summary

This paper gives an agnostic PAC learner for a broad class of real-valued multi-index models under the Gaussian distribution, and a nearly matching **SQ** lower bound, with the degree parameter `m` playing the role that the [generative exponent](generative-exponent-single-index.md) plays for single-index parameter recovery.

The characterising condition is Definition 1.3, "well-behaved" MIMs: for every subspace `V` and every distribution with `err_D(f) <= zeta`, either `f` is `tau`-approximable by a function of `x_V`, or there is a degree-at-most-`m` zero-mean unit-variance polynomial on `U = W_{V^perp}` whose conditional moment given `(x_V, y)` is at least `sigma`. Theorem 1.4 turns this into an agnostic learner with `N = d^{O(m)} 2^{poly_m(K/(eps sigma))}` samples achieving `err_D(h) <= tau + OPT + eps` — the `d^{O(m)}` is the dimension dependence; the `K` and `eps` dependence is exponential. In the realizable and independent-noise settings the complexity improves to `d^{O(m)} 2^{poly(K)} (1/eps)^{O(K)}`.

Theorem 1.10 is the converse: if for some subspace degree-`m` distinguishing moments do not exist (formalised via relative degree-`m` moment matching, Definition 1.9, giving a Relativized Non-Gaussian Component Analysis instance), then any SQ learner needs either a query to `STAT(d^{-(1-c)m/4})` or `2^{d^{Omega(c)}}` queries.

The application is Theorem 1.6: positive-homogeneous `L`-Lipschitz `K`-MIMs are learnable with `N = d^2 2^{O(K^3 L^2/eps^2)}`, and hence (Corollary 1.7) homogeneous Lipschitz ReLU networks with complexity **independent of the network size** `S`, removing the exponential-in-`S` dependence of Chen–Klivans–Meka.

**The adversary is uncosted.** The "adversarial label noise" is the agnostic model of Haussler / Kearns–Schapire–Sellie: "no assumptions are made on the observed labels". `OPT` is an inf over the class, i.e. a *budget* on how much of the label mass the corruption may misalign — not a resource bound on the corrupting party. The corrupting party has no computational, sample, or query budget; only the learner is priced (in `d^{O(m)}` samples and SQ queries). This is the near-miss the survey is about: the adversary appears in the theorem statement and carries no price tag.

## Claim Boundary

- **Quantified over:** all `f` in `F(K, m, zeta, tau, sigma)` (upper bound); all rotationally invariant `K`-MIM classes containing a function violating the distinguishing-moment condition (lower bound). The objective is small square loss (agnostic PAC), *not* parameter/subspace identification.
- **Model class and data assumption:** standard Gaussian `x`-marginal, `K`-dimensional hidden subspace with `K << d`, real-valued labels, bounded variation / bounded moment regularity. The ReLU statement is for *homogeneous Lipschitz* ReLU networks whose first-layer rank is at most `K`; it is not a statement about general networks or non-homogeneous activations.
- **Algorithm class:** the lower bound is in the **SQ** model with `STAT(tau)` (Definition 1.8) — stronger than CSQ. The paper contrasts itself with leap complexity, which it says "characterize[s] the Correlational SQ (CSQ) complexity of learning under certain assumptions". Do not conflate. The lower bound is not a low-degree bound either, though the technique (moment matching, RNGCA) is adjacent.
- **Does not establish:** (a) any cost for the adversary. See above; (b) `OPT + eps` error — the guarantee is `tau + OPT + eps`, and the constant-factor limitation is inherent (they cite `d^{poly(1/eps)}` hardness evidence for `OPT + eps`); (c) tight `K`, `eps` dependence — those are exponential; (d) that `m` equals the generative exponent in general. Their Appendix C.3 says Definition 1.3 "reduces to a *modification* of the generative exponent when K = 1", the modification being necessary because they characterise PAC learning rather than parameter recovery. [The Generative Leap](generative-leap-multi-index.md) reports the single-index equality `m = k*` from this paper's Appendix C.3.2, and notes their algorithm needs `d^{O(k*)}` where the generative-leap algorithm needs `d^{k*/2}`.
- **Abstract vs theorem:** the abstract's "nearly matching Statistical Query (SQ) lower bound, providing evidence that the complexity of our algorithm is qualitatively optimal as a function of the dimension" is properly hedged with "qualitatively" and "as a function of the dimension" — the `2^{poly(K/eps)}` factor is not matched. Theorem 1.10 also carries the unstated-in-abstract side condition about extreme values of `y`.

## Key Contributions

- Definition 1.3 (well-behaved MIMs) as the structural condition, shown essentially necessary and sufficient.
- Theorem 1.4: agnostic (adversarial-label-noise) PAC learner with `d^{O(m)} 2^{poly_m(K/(eps sigma))}` samples, `poly(N)` time, error `tau + OPT + eps`.
- Realizable / independent-noise improvement to `d^{O(m)} 2^{poly(K)} (1/eps)^{O(K)}`.
- Theorem 1.6 / Corollary 1.7: first fixed-degree-polynomial-in-`d` learner for positive-homogeneous Lipschitz `K`-MIMs, hence for homogeneous Lipschitz ReLU networks with complexity independent of network size.
- Theorem 1.10: SQ lower bound `d^{Omega(m)}` via relative degree-`m` moment matching (Definition 1.9) and RNGCA, generalising Diakonikolas–Kane–Ren–Sun beyond the finite-chi-squared-norm setting.
- Recovery of the Chen–Meka upper bounds for low-dimensional polynomials (Appendix D.3).

## Key Definitions / Theorems

**Definition 1.1 (Multi-Index Model), verbatim:**

> "A function f : Rd → R is a K-MIM if there exists a K-dimensional subspace W ⊆ Rd such that f (x) = f (xW ) for all x ∈ Rd , where xW is the projection of x onto W . The special case of K = 1 corresponds to Single-Index Models (SIMs)."

**Definition 1.2 (Agnostic PAC Learning under Gaussian Distribution).** Output `h` with `err_D(h) = E[(y - h(x))^2]` small compared with `OPT = inf_{f in C} err_D(c)`; the paper notes this "corresponds to the agnostic model [Hau92, KSS94] that does not make any assumptions on the labels."

**Definition 1.3 (Well-Behaved MIMs).** As summarised above; condition 2(b) is the degree-`<= m` distinguishing conditional moment `E_{y_0}[E[p(x_U) | x_V = z_V, y = y_0]^2] >= sigma`.

**Theorem 1.4 (Robust Regression for Well-behaved MIMs), verbatim:**

> "There exists an agnostic PAC learner for F (K, m, ζ, τ, σ), where ζ ≥ OPT + ǫ, that draws N = dO(m) 2polym (K/(ǫσ)) i.i.d. samples, runs in poly(N ) time, and computes a hypothesis h such that with high probability errD (h) ≤ τ + OPT + ǫ."

**Definition 1.8 (Statistical Query Model).** `STAT(tau)` returns `v` with `|v - E_{x ~ D}[q(x)]| <= tau` for bounded `q : R^d -> [0,1]`.

**Theorem 1.10 (SQ Lower Bound).** Under moment matching relative to `V x R` and `E[(h(x_V) - y)^2] >= tau` for all `h`: any SQ learner needs a query to `STAT(d^{-(1-c)m/4})` or `2^{d^{Omega(c)}}` queries. Interpretation given: "either requires d(1−c)/m/2 samples or exponential in dc time."

**Theorem 1.6.** `N = d^2 2^{O(K^3 L^2/eps^2)}` for `H_{K,L}`.

## Connections

- Concept pages: [Multi-Index Model](../concepts/multi-index-model.md), [Statistical Query Model](../concepts/statistical-query-model.md), [Generative Exponent](../concepts/generative-exponent.md), [CSQ Model](../concepts/csq-model.md).
- Companion near-miss with the same uncosted adversary: [Sample and Computationally Efficient Robust Learning of Gaussian Single-Index Models](robust-single-index-efficient.md). In that paper the adversary is likewise the agnostic-model corruption, unbounded and unpriced.
- Their `m` relates to `k*` of [Computational-Statistical Gaps in Gaussian Single-Index Models](generative-exponent-single-index.md) (their Appendix C.3) and to the generative leap of [The Generative Leap](generative-leap-multi-index.md), which discusses the `d^{O(k*)}` vs `d^{k*/2}` difference.
- Distinguishes itself from the CSQ characterisation of [SGD Learning on Neural Networks: Leap Complexity](leap-complexity-sgd.md) and [The Merged-Staircase Property](merged-staircase-property.md).
- Frameworks: [Statistical Algorithms and Planted Clique](feldman-statistical-algorithms-planted-clique.md), [SQ and Low-Degree Almost Equivalent](brennan-sq-lowdegree-equivalence.md), [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md), [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md).
- Authors: [Ilias Diakonikolas](../entities/ilias-diakonikolas.md).

## Open Questions / Limitations

- The exponential dependence on `K` and `1/eps` in the agnostic setting.
- The `tau` additive term in the error guarantee; the gap between `tau + OPT + eps` and the SQ lower bound's "error substantially better than tau".
- Whether the modification of the generative exponent needed for `K = 1` PAC learning can be removed, and whether `m = k*` extends to `K > 1` (the generative-leap paper conjectures it does).
- **The adversary is a corruption budget, not a party.** No computational, sample, or query bound is placed on whatever produces the adversarial labels; a resource-bounded version of this theorem does not exist here.

## Quotes / Notable Passages

> "In the presence of adversarial label noise, the complexity of our learning algorithm is dO(m) 2poly(K/ǫ) ."

> "the agnostic model [Hau92, KSS94] that does not make any assumptions on the labels"

> "[ABAB+ 21, ABAM22, ABAM23] introduced a complexity notion (leap complexity) for learning structured MIMs, which turns out to essentially characterize the Correlational SQ (CSQ) complexity of learning under certain assumptions."
