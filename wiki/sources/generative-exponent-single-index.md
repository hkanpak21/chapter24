---
title: Computational-Statistical Gaps in Gaussian Single-Index Models
type: source
date_ingested: 2026-08-20
authors: [Alex Damian, Loucas Pillaud-Vivien, Jason D. Lee, Joan Bruna]
venue: "COLT 2024"
venue_evidence: "dblp search (q=Computational-Statistical Gaps Gaussian Single-Index Models): lists both a COLT 2024 inproceedings entry and CoRR abs/2403.05529 — conference version confirmed"
year: 2024
tags: [statistical-computational-gaps, statistical-query, low-degree-polynomials, single-index-model, generative-exponent, sample-complexity]
claim_quantifier: conditional
antecedent: "Lower bounds: SQ bound is unconditional given the VSTAT(n) model; the low-degree bound is conditional on Conjecture 3.4 (the low-degree conjecture). Upper bound (Theorem 4.1 / Corollary 4.4) is unconditional. All results assume the Gaussian single-index model of Definition 1.1 with P known up to the caveats of Corollary 4.4."
model_class: "Gaussian single-index model, Definition 1.1: x ~ gamma_d isotropic Gaussian in R^d, labels depend on x only through z = w* · x via a bivariate law P in G; w* uniform on S^{d-1}. Label noise is allowed (additive, multiplicative, mixture, Massart). NOT a result about neural networks."
algorithm_class: "SQ (queries E[phi(X,Y)] via VSTAT(n)) and low-degree polynomials (degree D = omega(log d)); upper bound is a partial-trace spectral estimator after a label transformation"
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: samples
cls_tightness: exponent
cls_baseline: n/a
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: algo class
cls_assessed: explicit
cls_evidence: "we show that computationally efficient algorithms, both within the Statistical Query (SQ) and the Low-Degree Polynomial (LDP) framework, necessarily require"
cls_evidence_src: abstract
cls_reason: "unit=samples/tightness=exponent rather than the algo-class/class pairing used on sibling low-degree pages, because the paper's headline quantity is an explicit sample-complexity threshold n=Theta(d^{max(1,k*/2)}) parameterized by the generative exponent k*, not a bare class-membership statement. second_notion=algo class records that this sample bound holds specifically for SQ and low-degree algorithms (Thm 3.2, Thm 3.5), the same party under two named restricted classes with matching thresholds, not two different parties. baseline=stated from Theorem 6.1's information-theoretic n=Theta(d/eps^2), against which the polynomial gap (when k*>2) is defined. party=learner, not attacker: the task is direction recovery in a Gaussian single-index model with no trained model or attack scenario (Claim Boundary: 'not a result about neural networks'). Rule 1 (main-claim-decides) was not needed since SQ and low-degree give matching, not differently-shaped, claims."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper identifies the **generative exponent** `k*` as the quantity that governs the sample complexity of recovering the hidden direction in a Gaussian single-index model for both SQ and low-degree algorithms, and proves matching upper and lower bounds at `n = Theta(d^{max(1,k*/2)})`. Against an information-theoretic upper bound of `n = Theta(d/eps^2)` (Theorem 6.1), this yields a polynomial statistical-computational gap exactly when `k* > 2`.

The construction is a change of expansion. The information exponent `l*` of Ben Arous–Gheissari–Jagannath is the first non-zero Hermite coefficient `beta_l = E[Y h_l(Z)]` of the conditional expectation `sigma(z) = E[Y | Z = z]` — a *correlational* object, which is why it governs CSQ. The generative exponent instead expands the `chi^2`-mutual information of `(Z,Y)`: `I_{chi^2}[P] = sum_k lambda_k^2` with `lambda_k = || zeta_k ||_{P_y}`, `zeta_k = E[h_k(Z) | Y]`. The exponent `k*` is the first `k` with `lambda_k != 0`. Because `beta_k = <y, zeta_k>_{P_y}`, `lambda_k = 0` forces `beta_k = 0`, hence `k*(P) <= l*(P)` always.

The variational representation, Proposition 2.6, is the load-bearing statement: `k*(P) = inf_{T in L^2(P_y)} l*((Id ⊗ T)_# P)`. In words, `k*` is the smallest information exponent reachable by *any* square-integrable transformation of the label. This is why `k*` and `l*` can differ at all: the information exponent is not composition-invariant, and a suitable label pre-processing `T` can lower the Hermite index. The algorithm makes this operational — `T(y) = zeta_{k*}(y)` is the optimal denoiser, and the partial-trace estimator (Algorithm 1) then runs an order-`k*` CSQ-style method on the transformed labels.

Example 2.7 is the boundary that must travel with any citation of this paper: for a **polynomial** link `sigma`, `k*(sigma) <= 2`, with equality iff `sigma` is even. Large-`k*` instances therefore require non-polynomial, fine-tuned constructions (Theorem 1.5 builds smooth `sigma` with any prescribed `k*`, and Example 2.7 (ii)-(iii) exhibit `k* = 4`).

## Claim Boundary

- **Quantified over:** all `P` in the class `G` of non-separable bivariate laws with Gaussian first marginal (Definition 1.1, Eq. 1), and all SQ / low-degree algorithms. Recovery target is the *direction* `w*`, not the link.
- **Model class and data assumption:** Gaussian single-index. Isotropic Gaussian covariates in `R^d`, one hidden direction, `w*` from the uniform prior on the sphere, `P` assumed known unless Corollary 4.4 is invoked. A result about Gaussian single-index models is not a result about neural networks; the paper makes no neural-network claim.
- **Algorithm class:** the SQ lower bound (Theorem 3.2) is stated against `q = d^r` queries to `VSTAT(n)` and is *SQ*, strictly stronger than CSQ — this is precisely the improvement over the CSQ bound of `d^{max(1,l*/2)}`. The low-degree bound (Theorem 3.5) is a separate framework and is conditional on Conjecture 3.4. The two are not interchangeable, though they agree here. The matching upper bound is a specific spectral algorithm, not a general poly-time statement.
- **Does not establish:** (a) that `k*` prices all polynomial-time algorithms — that step needs the low-degree conjecture; (b) an estimation lower bound. Remark 3.3 is explicit that Theorem 3.2 compares against `P_0 = gamma_d ⊗ P_y` and so "primarily measures the detection threshold", leaving open an SQ detection/estimation gap as in tensor PCA; (c) that `k*` survives batch reuse — see [DTA+24](reusing-batches-breaks-exponents.md), which observes that GD with reused batches performs label transformations *implicitly* and thereby reaches SQ-optimal complexity for some targets; (d) that large `k*` is generic. Example 2.7 says it is not, for polynomial links.
- **Abstract vs theorem:** the abstract says computationally efficient algorithms "necessarily require Ω(d^{k*/2}) samples" within SQ and LDP. The LDP half of that is conditional on Conjecture 3.4; the abstract does not say so, though Theorem 1.3 does. Also, the abstract's final sentence advertises "smooth and Lipschitz deterministic target functions with arbitrarily large generative exponents" — those are constructions (Section 5), which is the same fact Example 2.7 states negatively.

## Key Contributions

- Definition of the generative exponent `k*` via the `chi^2`-mutual-information expansion (Definition 2.4).
- `k*(P) <= l*(P)`, with the variational characterisation Proposition 2.6 identifying exactly when the inequality is strict.
- SQ lower bound `n ≳ d^{k*/2}` (Theorem 3.2), with no polylog factors, using a spherical-code hypothesis set.
- Low-degree lower bound at the same threshold (Theorem 3.5, Corollary 3.6) under the low-degree conjecture.
- Matching efficient upper bound `n ≳ d^{max(1,k*/2)}` via label transformation `T = zeta_{k*}` plus a partial-trace estimator (Theorem 4.1), extended to unknown `P` and unknown `k*` (Corollary 4.4, Algorithm 2).
- Information-theoretic upper bound `n = Theta~(d/(lambda_k^2 eps^2))` (Theorem 6.1), closing the gap statement.
- Existence of smooth `sigma` with arbitrary `k*` (Theorems 5.1, 5.2).
- Corollary 2.8: `k*` is invariant under bijective relabelling.

## Key Definitions / Theorems

**Definition 1.1 (Gaussian Single-Index Model), verbatim:**

> "We say that a joint distribution P ∈ P(Rd × R) follows a Gaussian single index model if there exists a probability measure P ∈ G ⊂ P(R2 ) and w⋆ ∈ S d−1 such that P = [Rw⋆ ⊗ Id]# [γd−1 ⊗ P]"

**Definition 2.2 (information exponent, restated in their notation), verbatim:**

> "The information exponent of P ∈ G is defined by: l⋆ (P) := min{l ≥ 1; βl ̸= 0} where βl := EP [Y hl (Z)]."

**Definition 2.4 (Generative Exponent), verbatim:**

> "The generative exponent of P ∈ G is defined by: k ⋆ (P) := min{k ≥ 1; λk ̸= 0} where λk := ∥ζk ∥Py and ζk := EP [hk (Z)|Y ]."

**Proposition 2.6 (A Variational Representation), verbatim:**

> "The generative exponent k ⋆ (P) can be written as: k ⋆ (P) = inf T ∈L2 (Py ) l⋆ ((Id ⊗ T )# P)"

**The exact condition under which `k*` and `l*` differ.** `k* <= l*` always, because `lambda_k = 0 => beta_k = 0`. By Proposition 2.6, `k*(P) < l*(P)` **iff there exists a square-integrable label transformation `T in L^2(P_y)` such that the transformed model `(Id ⊗ T)_# P` has strictly smaller information exponent** — i.e. iff some label pre-processing lowers the first non-vanishing Hermite index. Equivalently (paper's own gloss of Prop. 2.6): `k*` is the smallest `k` for which some measurable `T` and some degree-`k` mean-zero polynomial `Q` give `E_P[T(Y) Q(Z)] != 0`, whereas `l*` restricts to `T = id`. The special case `k* <= 2` has the closed-form criterion inherited from Mondelli–Montanari / Barbier et al., quoted verbatim as Eq. (3): `E[ E[Z^2 - 1 | Y]^2 ] != 0`. Post-processing can never *raise* `k*`: "no post-processing of Y , either random or deterministic, can reduce the generative exponent" — and Corollary 2.8 gives invariance under bijections.

**Example 2.7 (i), verbatim:**

> "For σ a polynomial, we have k ⋆ (σ) ≤ 2 and k ⋆ (σ) = 2 iff σ is even. In particular, k ⋆ (hj ) = 1 if j is odd and k ⋆ (hj ) = 2 if j is even."

**Theorem 3.2 (SQ lower bound).** With `q = d^r`, `r <= d^{1/4}`, `lambda_{k*}^2 >= r d^{-1/2}`: any algorithm returning `w_hat` with `|w_hat · w*| >= omega~(d^{-1/2})` using `q` queries to `VSTAT(n)` requires `n >= (c_{k*}/lambda_{k*}^2)(d/r^2)^{k*/2}`.

**Theorem 4.1 / Corollary 4.4.** `n >= Omega(lambda_{k*}^2 d^{k*/2} + d/eps^2)` suffices for `(w_hat · w*)^2 >= 1 - eps^2`, without prior knowledge of `P` or `k*`.

**Theorem 6.1.** An inefficient procedure achieves `(w_hat · w*)^2 >= 1 - eps^2` with `n = Theta~(d/(lambda_k^2 eps^2))`.

## Connections

- Concept pages: [Generative Exponent](../concepts/generative-exponent.md), [Information Exponent](../concepts/information-exponent.md), [CSQ Model](../concepts/csq-model.md), [Single-Index Model](../concepts/single-index-model.md).
- Improves on the online-SGD threshold of [BGJ21](information-exponent-online-sgd.md) and on the CSQ-only bound of [ABM23](leap-complexity-sgd.md).
- Extended to multi-index by [The Generative Leap](generative-leap-multi-index.md), which reduces to this paper when `r = 1`.
- The `d^{k*/2}` threshold is escaped by batch reuse for many targets: [Reusing Batches Breaks the Information and Leap Exponents](reusing-batches-breaks-exponents.md).
- The generative-exponent regime is also reached without batch reuse, by one-pass layer-wise SGD with a large second-layer learning rate: [Learning Rate Induces Phase Transitions in SGD](learning-rate-induces-generative-exponent.md) proves learning-rate-indexed phase transitions between the information-exponent and generative-exponent complexities.
- Criticised as brittle by [Noise Sensitivity Exponent](noise-sensitivity-exponent.md): large-generative-exponent functions are "typically fine-tuned and unstable".
- Their `k*` corresponds to the parameter `m` of [Robust Multi-Index SQ Bounds](robust-multi-index-sq-bounds.md) when `K = 1` (that paper's Appendix C.3).
- The lattice-based escape route in the noise-free case is [Hardness of Learning Single Periodic Neurons](hardness-single-periodic-neurons.md), cited here as [SZB21] for exactly that point.
- SQ / low-degree machinery: [Statistical Query Model](../concepts/statistical-query-model.md), [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md), [SQ and Low-Degree Almost Equivalent](brennan-sq-lowdegree-equivalence.md), [Low-Degree Polynomials Survey](low-degree-polynomials-survey.md), [Low-Degree Estimation](low-degree-estimation-schramm-wein.md), [Statistical Algorithms and Planted Clique](feldman-statistical-algorithms-planted-clique.md).
- Authors: [Alex Damian](../entities/alex-damian.md), [Jason D. Lee](../entities/jason-lee.md), [Joan Bruna](../entities/joan-bruna.md).

## Open Questions / Limitations

- Remark 3.3: possible SQ detection/estimation gap for this problem, as established for tensor PCA by Dudeja–Hsu; the paper conjectures it would be an SQ artefact since Algorithm 1 estimates at `d^{k*/2}`.
- The low-degree half of the lower bound rests on Conjecture 3.4.
- Constants: Theorem 4.1's `C_k` and the `lambda_k` dependence are not fine-grained.
- The result is subspace/direction recovery; full PAC learning of the link is a separate step.

## Quotes / Notable Passages

> "the information exponent defined by [BAGJ21] is not composition invariant, i.e. it is possible that the information exponent of (X, T (Y )) is strictly smaller than the information exponent of (X, Y )"

> "no post-processing of Y , either random or deterministic, can reduce the generative exponent"

> "λk = 0 indicates the absence of order-k exploitable information, even after conditioning on the observed labels"
