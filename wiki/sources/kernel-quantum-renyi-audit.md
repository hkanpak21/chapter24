---
title: Auditing Differential Privacy in High Dimensions with the Kernel Quantum Rényi Divergence
type: source
date_ingested: 2026-08-20
authors: [Carles Domingo-Enrich, Youssef Mroueh]
venue: venue unconfirmed from PDF (arXiv:2205.13941v1 [cs.LG], 27 May 2022)
year: 2022
tags: [differential-privacy, learning-theory, computational-vs-it-robustness]
claim_quantifier: existential
antecedent: "A fixed positive definite kernel k with k(x,x)=1; regularization λ ≥ 0; order α. Post-processing requires a kernel factorization condition k(x,x') = k'(g(x), g(x'))·k̃(x,x') (deterministic case) or its expectation form (randomized case). Estimation rates are for the REGULARIZED divergence."
adversary_bound: function class (implicitly — the witness of the divergence is restricted to an RKHS), presented as an auditing tool rather than an adversary model
---

## Summary

The same restrict-the-witness-class move as [CIM19](capacity-bounded-dp.md), motivated as **auditing**
rather than as an adversary model. Rather than restricting the class because the attacker is weak, the
authors restrict it because a restricted divergence is **estimable from samples in high dimension** at
parametric rates, whereas the unrestricted one is not.

The construction: map the mechanism's output distribution into an RKHS via the covariance operator
`Σ_p = ∫ φ(x)φ(x)* dp(x)`, the kernel analogue of a quantum density operator, then take the (regularized)
quantum Rényi divergence between the covariance operators of `L(f(D))` and `L(f(D'))`. This is the **kernel
Rényi divergence**; bounding it defines `(k, α, λ, ε)`-RKRDP (Definition 2), mirroring Rényi DP with `Σ` in
place of the distributions themselves.

The relations are one-directional and stated as such. Proposition 4 gives: smaller `λ` and larger `α` make
RKRDP stronger; **`(α, ε)`-RDP implies `(k, α, λ, ε)`-RKRDP for every kernel and every `λ`**. So RKRDP is a
relaxation of RDP and hence of `ε`-DP. That is the whole point for auditing — a *violation* of RKRDP
certifies a violation of DP, and RKRDP is the thing you can estimate.

Properties follow the same conditional pattern as capacity-bounded DP. Convexity holds for `α > 1`
(Proposition 5). Parallel and adaptive sequential composition hold (Propositions 6, 7). **Post-processing is
conditional on a kernel factorization**: Theorem 1 requires a kernel `k̃` with
`k(x, x') = k'(g(x), g(x')) k̃(x, x')` for all `x, x'`; Theorem 2 gives the randomized-`g` version with
`k(x, x') = E_g[k̃_g(x, x') k'(g(x), g(x'))]`. This is the structural tax on every restricted-divergence
privacy notion: free post-processing and a restricted adversary are incompatible.

§4 shows the regularized kernel Rényi divergence is estimable from samples, and §5 turns that into auditing
procedures for `ε`-DP, `(ε, δ)`-DP, `(α, ε)`-Rényi DP, and RKRDP itself, with the claim that the method
"does not suffer from curse of dimension and has parametric rates in high dimensions" — the advertised
advantage over the univariate hypothesis-testing pipelines of Ding et al. and Jagielski et al.

The paper explicitly acknowledges the CIM19 lineage and closes by naming the connection as future work.

## Claim Boundary

- **Quantified over:** all adjacent `D, D' ∈ D` for the definition; the estimation results over samples from
  the two output distributions.
- **Antecedent:** as in the front matter. The kernel assumption `k(x,x) = 1` is standing. Estimation rates
  are for the **regularized** divergence (`λ > 0`), not the unregularized kernel Rényi divergence.
- **Excluded cases:** post-processing by arbitrary maps is excluded — only maps satisfying the kernel
  factorization are covered. Convexity is stated for `α ∈ (1, +∞)`. Proposition 4's implications are stated
  for `α ∈ [1/2, 1) ∪ (1, +∞)`.
- **Does not establish:** that RKRDP is a meaningful *security* guarantee against any realistic adversary.
  The paper does not claim it is; RKRDP is a relaxation of DP used as a **detector**. A mechanism satisfying
  RKRDP and failing DP has not been shown safe against anything. It does not establish a computational
  bound. And it does not learn the kernel — the kernel is fixed in advance.
- **Abstract vs theorem:** none found. The abstract frames the contribution as "auditing procedures," not as
  a privacy guarantee.

## Key Contributions

- The kernel Rényi divergence (KRD) and its regularized version (RKRD), defined as quantum Rényi divergences
  between RKHS covariance operators, following Bach's kernel relative entropy.
- `(k, α, ε)`-KRDP and `(k, α, λ, ε)`-RKRDP, with implications relating them to RDP.
- Convexity, conditional post-processing, parallel and adaptive sequential composition.
- Sample estimability of RKRD at parametric rates in high dimension, and auditing procedures for `ε`-DP,
  `(ε, δ)`-DP, `(α, ε)`-RDP, and RKRDP.

## Key Definitions / Theorems

- **Definition 1 ((α, ε)-RDP [Mironov'17]).** `D_α(L(f(D)) || L(f(D'))) ≤ ε` for adjacent `D, D'`.
- **Definition 2 ((k, α, λ, ε)-RKRDP).** `D_{α,λ}(Σ_{L(f(D))} || Σ_{L(f(D'))}) ≤ ε` for adjacent `D, D'`,
  with covariance operators taken with respect to the feature map `φ` of `k`.
- **Proposition 4.** (1) larger `λ` weaker; (2) larger `α` stronger; (3) `(α, ε)`-RDP ⟹ `(k, α, λ, ε)`-RKRDP
  for all `k, λ`; (4) product kernels decompose with `λ^{1/J}`.
- **Theorem 1 (Post-processing, deterministic `g`).** Under `k(x, x') = k'(g(x), g(x')) k̃(x, x')`:
  `D_α(Σ_{L(g(f(D)))} || Σ_{L(g(f(D')))}) ≤ D_α(Σ_{L(f(D))} || Σ_{L(f(D'))})`; hence `(k, α, ε)`-KRDP for `f`
  gives `(k', α, ε)`-KRDP for `g ∘ f`.
- **Theorem 2.** Randomized-`g` version, with `k(x, x') = E_g[k̃_g(x, x') k'(g(x), g(x'))]`.
- **Proposition 9.** Relations between `(ε, δ)`-DP and RKRDP for all `ε, δ > 0`, `α ∈ [1/2) ∪ (1, ∞)`.

## Connections

- Concept: [capacity-bounded privacy](../concepts/capacity-bounded-privacy.md) — same restriction, different
  motivation, and the same conditional post-processing tax.
- Directly builds on [CIM19](capacity-bounded-dp.md), citing it for the convexity / post-processing /
  composition framing and for the capacity-bounded adversary interpretation.
- Contrast with [MPRV09](computational-differential-privacy.md): no runtime bound anywhere.
- [DP20](sok-differential-privacies.md) would file this under its dimension **Q** (quantification of privacy
  loss) rather than **C**; the function-class restriction has no home in that taxonomy.
- Audits mechanisms of the [DP-SGD](deep-learning-differential-privacy.md) family.
- Entities: [Kamalika Chaudhuri](../entities/kamalika-chaudhuri.md) (via the CIM19 lineage this extends).

## Open Questions / Limitations

- **Learn the kernel** by taking a supremum of RKRD over a class of kernels or feature maps — i.e. make the
  restricted class adaptive rather than fixed.
- Explicitly named as future work: "exploring the link of the learned kernel with adversaries with limited
  capacity [Chaudhuri et al., 2019]." The bridge from auditing tool to adversary model is unbuilt, and the
  authors say so.

## Quotes / Notable Passages

> "Auditing black-box DP algorithms and mechanisms to certify whether they satisfy a certain DP guarantee is
> challenging, especially in high dimension."

> "While privacy attacks provide a qualitative assessment of DP, they don't provide quantitative privacy
> guarantees nor detect precisely violations of differential privacy in terms of the desired privacy budget
> ε."

> "exploring the link of the learned kernel with adversaries with limited capacity"
