---
title: A Noise Sensitivity Exponent Controls Large Statistical-to-Computational Gaps in Single- and Multi-Index Models
type: source
date_ingested: 2026-08-20
authors: [Leonardo Defilippis, Florent Krzakala, Bruno Loureiro, Antoine Maillard]
venue: venue unconfirmed from PDF (arXiv:2603.17896v1 [stat.ML], 18 Mar 2026)
year: 2026
tags: [statistical-computational-gaps, sample-complexity, approximate-message-passing, single-index-model, multi-index-model, noise-sensitivity-exponent]
claim_quantifier: conditional
antecedent: "Theorems 3.2, 3.3, 5.2 assume even activations sigma with finite NSE, i.i.d. Gaussian covariates, isotropic Gaussian planted directions, and the proportional limit d, n -> infinity with n/d -> alpha; the multi-index results take a further large-width limit p -> infinity AFTER d -> infinity. Result 4.3 (general activations, committee case) relies on statistical-physics arguments and a committee-symmetry ansatz and is 'currently non-rigorous'."
model_class: "Three models, all Gaussian: (i) single-index with additive Gaussian noise y = sqrt(lambda) sigma(w* · x) + xi; (ii) separable multi-index / committee machine y = p^{-1/2} sum_k sigma(w*_k · x) + sqrt(Delta) xi; (iii) hierarchical multi-index y = sum_k k^{-gamma} sigma(<w*_k, x>) + sqrt(Delta) xi. Planted directions i.i.d. N(0, I_d/d)."
algorithm_class: "AMP / first-order iterative methods (and spectral methods) in the PROPORTIONAL regime n = alpha d. NOT SQ, NOT CSQ, NOT low-degree, and NOT the d^k polynomial-scaling regime."
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: samples
cls_tightness: exponent
cls_baseline: stated
cls_second_party: none
cls_second_notion: algo class
cls_assessed: explicit
cls_evidence: "the optimal AMP algorithm achieves weak recovery (see Definition 3.1) exactly for α > αWR"
cls_evidence_src: Thm 3.2
cls_reason: "Classified on the single-index weak-recovery result (Thms 3.2-3.3), the paper's first and cleanest rigorous result, per rule 1. party=learner: the bound binds the AMP algorithm, not an attacker (Rule 3; no adversary anywhere in the paper). unit=samples/tightness=exponent, matching the sibling page generative-exponent-single-index.md's pattern exactly: the headline quantity is the sample-ratio threshold alpha, and beta_star is a stated multiplicative relation between the AMP threshold Theta(lambda^-beta_star) (Thm 3.2) and the information-theoretic threshold Theta(lambda^-1) (Thm 3.3, verbatim 'there is a wide statistical-to-computational gap as λ → 0'), which is baseline=stated. second_notion=algo class records that this threshold is specific to AMP/first-order methods in the proportional regime (front matter algorithm_class), a restricted class incomparable to the sample count itself, per rule 4b. Per the page's own Claim Boundary this composes with no SQ/low-degree/d^k-scaling exponent and establishes no lower bound against general poly-time algorithms — AMP-optimality is invoked by citation, not proved here."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper proposes the **noise sensitivity exponent (NSE)** `beta_*(sigma) = min{beta in N : E_{z ~ N(0,1)}[sigma^beta(z)(z^2 - 1)] != 0}` as a unit that controls the *size* of statistical-to-computational gaps in three Gaussian index models, and — separately — argues that the earlier exponents (information, leap, generative) are brittle.

The three results all price AMP against the information-theoretic threshold. (1) For even single-index links with additive Gaussian noise, the information-theoretic weak-recovery threshold is `alpha^{IT}_{WR} = Theta(lambda^{-1})` (Theorem 3.3) while the AMP threshold is `alpha^{Alg}_{WR} = Theta(lambda^{-beta_*})` (Theorem 3.2), so `beta_* > 1` opens a widening gap as the SNR `lambda -> 0`. (2) For committee machines, specialization is information-theoretically at `Theta_p(p)` but algorithmically at `Theta_p(p^{beta_*})` for even activations. (3) For hierarchical models, the `k`-th feature is recoverable by AMP at `alpha_k^{Alg} = Theta_k(k^{2 gamma beta_*})`.

The NSE classification is coarse: `beta_* = 1` iff the information exponent is 2; `beta_* = 2` captures "the majority of functions with zero second Hermite coefficient", and all polynomials of degree `< 20` have `beta_* <= 2`; `beta_* > 2` functions exist but "are usually fine-tuned"; `beta_* = infinity` corresponds to generative exponent `> 2`, unlearnable in the proportional regime.

The critique of the earlier units is explicit and is the reason this paper matters for the survey. The information exponent "can be easily bypassed by data reuse or by training with non-square losses"; the generative exponent is more refined but, "with the notable exception of parity-like problems, functions in this class are typically fine-tuned and unstable: small perturbations of the target function often collapse them back into easier regimes". The proposed alternative organising principle is symmetry: non-symmetric single-index targets typically have `GE = 1`, even ones typically `GE = 2`, both learnable with `n = O(d)`.

## Claim Boundary

- **Quantified over:** even activations `sigma` with finite NSE, in the proportional high-dimensional limit. Results 4.3 extends predictions to general activations non-rigorously.
- **Model class and data assumption:** i.i.d. isotropic Gaussian covariates, isotropic Gaussian planted directions, and asymptotic thresholds. The paper's own limitations section says the results "explicitly trade realism for analytic tractability", do not capture finite-dimensional effects, structured covariances, heavy tails, or distributional shift, and that the multi-index analysis needs `p -> infinity` after `d -> infinity`.
- **Algorithm class:** **AMP and first-order iterative methods** in the **proportional regime `n = alpha d`**. This is a different algorithm class *and a different sample-complexity regime* from the information exponent, leap, generative exponent, and generative leap, all of which are stated as polynomial scalings `n ≍ d^k` with `k` fixed. The NSE therefore **does not compose** with those exponents: `beta_*` multiplies an exponent of `lambda`, `p`, or `k`, not of `d`. Do not chain a `beta_*` bound with a `d^{k*/2}` bound.
- **Does not establish:** (a) any lower bound against all polynomial-time algorithms. AMP optimality among first-order methods is invoked by citation (Celentano et al., Montanari–Wu); the gap statements are AMP-vs-IT, not hardness; (b) the information-theoretic side for hierarchical models: `alpha_k^{IT} = Theta(k^{2 gamma})` is stated as **Open Question 5.4**, with only the lower bound `alpha_k^{IT} >= C k^{2 gamma}` rigorous; (c) that `beta_*` supersedes the generative exponent. It refines *within* the `GE = 2` class; `beta_* = infinity` is exactly `GE > 2`; (d) rigour for general activations in the committee case (Result 4.3).
- **Abstract vs theorem:** the abstract says the NSE "governs the existence and magnitude of statistical-to-computational gaps within a broad regime of these models" and that "the same exponent controls a statistical-computational gap in the specialization transition of large separable multi-index models". The committee-machine claim is rigorous only for even activations; the general-activation case is Result 4.3, which the conclusion admits "is therefore currently non-rigorous". "We then demonstrate" in the abstract overstates that half.

## Key Contributions

- Definition 2.1: the noise sensitivity exponent.
- Theorem 3.2 / 3.3: AMP threshold `Theta(lambda^{-beta_*})` versus information-theoretic `Theta(lambda^{-1})` for even single-index links with additive Gaussian noise, hence a gap `Theta(lambda^{-beta_*})` when `beta_* > 1`.
- Committee machines: `alpha^{IT}_{spec} = Theta_p(p)`; `alpha^{Alg}_{spec} = Theta_p(p)` iff `beta_* = 1`; `alpha^{Alg}_{spec} = Theta_p(p^{beta_*})` for even activations; `omega(p)` generically when `beta_* > 1`.
- Theorem 5.2: hierarchical models, `alpha_k^{Alg} = Theta_k(k^{2 gamma beta_*})`; Corollary 5.3 rescales the MSE rate exponent by `beta_*^{-1}`.
- Classification of NSE values (`beta_* = 1` iff `IE = 2`; `beta_* <= 2` for all polynomials of degree `< 20`; explicit `beta_* in {3,4}` constructions in Appendix C; `beta_* = infinity` iff `GE > 2`).
- A sustained argument that the information exponent, leap, and generative exponent are brittle, and that symmetry is the robust organising principle.

## Key Definitions / Theorems

**Definition 2.1 (Noise Sensitivity Exponent), verbatim:**

> "Let σ : R → R such that |σ(x)| ≤ C(1 + |x|k ) for some C, k > 0. The noise-sensitivity exponent is defined as"

followed by the display "β⋆ (σ) := min{β ∈ N : Ez∼N (0,1) σ β (z)(z 2 − 1) ̸= 0}".

**Theorem 3.2, verbatim:**

> "Consider the single-index model of eq. (4). Assume that the even function σ satisfies the assumptions of Definition 2.1, and has NSE β⋆ < ∞. Then, the optimal AMP algorithm achieves weak"

> "recovery (see Definition 3.1) exactly for α >"

(the superscripted "Alg." labels float to their own lines in the extraction; the conclusion is `alpha^{Alg}_{WR} = Theta(lambda^{-beta_*})` as `lambda -> 0`)

**Theorem 3.3.** `alpha^{IT}_{WR} = Theta(lambda^{-1})`, so `alpha^{Alg}_{WR} - alpha^{IT}_{WR} = Theta(lambda^{-beta_*})` for `beta_* > 1`.

**Theorem 5.2.** `alpha_k^{Alg} = Theta_{k,p}(k^{2 gamma beta_*})` as `p -> infinity`.

**Their restatement of the other units.** Information exponent, Eq. (8): `IE(g) = min{k in N : E[g(z) He_k(z)] != 0}`. Generative exponent, Eq. (9), verbatim: `GE(g) = inf_T IE(T ◦ g)` — "Informally, it captures the effective information exponent after allowing for optimal preprocessing T (y) of the labels."

## Connections

- Concept pages: [Noise Sensitivity Exponent](../concepts/noise-sensitivity-exponent.md), [Information Exponent](../concepts/information-exponent.md), [Generative Exponent](../concepts/generative-exponent.md), [Leap Complexity](../concepts/leap-complexity.md), [Single-Index Model](../concepts/single-index-model.md), [Multi-Index Model](../concepts/multi-index-model.md).
- Critiques [Online SGD on Non-Convex Losses](information-exponent-online-sgd.md), [SGD Learning on Neural Networks: Leap Complexity](leap-complexity-sgd.md), and — as brittle rather than wrong — [Computational-Statistical Gaps in Gaussian Single-Index Models](generative-exponent-single-index.md).
- Cites [The Benefits of Reusing Batches](reusing-batches-breaks-exponents.md) as the reason the information exponent is bypassable; shares the proportional regime `n = alpha d` and two co-authors' research programme (Krzakala).
- Concepts: [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md), [Statistical Query Model](../concepts/statistical-query-model.md), [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md).
- Authors: [Florent Krzakala](../entities/florent-krzakala.md).

## Open Questions / Limitations

- Open Question 5.4: whether `alpha_k^{IT} = Theta_{k,p}(k^{2 gamma})` for hierarchical models — only the lower bound `>= C k^{2 gamma}` is established, so the *gap* in case (3) is conjectural.
- Result 4.3 (general activations, committee machines) is non-rigorous — statistical-physics arguments plus a committee-symmetry ansatz.
- Sharpening the non-specialization range (improving the `o(p^{3/2})` control) via higher-order large-`p` state-evolution expansions.
- Gaussian covariates and asymptotic thresholds only; universality beyond Gaussian designs is expected but not proved.
- The NSE prices AMP; it says nothing about SQ, low-degree, or general polynomial-time algorithms, so it cannot be composed with the `d^k`-scaling exponents.

## Quotes / Notable Passages

> "The information exponent, in particular, turns out to be too restrictive, as it can be easily bypassed by data reuse or by training with non-square losses"

> "functions in this class are typically fine-tuned and unstable: small perturbations of the target function often collapse them back into easier regimes"

> "A more natural and robust classification instead emerges from the study of symmetries of the target function."

> "our results explicitly trade realism for analytic tractability, in the standard way for single- and multi-index models"
