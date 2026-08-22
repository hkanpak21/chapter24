---
title: Sample and Computationally Efficient Robust Learning of Gaussian Single-Index Models
type: source
date_ingested: 2026-08-20
authors: [Puqian Wang, Nikos Zarifis, Ilias Diakonikolas, Jelena Diakonikolas]
venue: venue unconfirmed from PDF (arXiv:2411.05708v1 [cs.LG], 8 Nov 2024; cited elsewhere as NeurIPS 2024)
year: 2024
tags: [single-index-model, agnostic-learning, adversarial-label-noise, information-exponent, csq, sample-complexity]
claim_quantifier: universal
antecedent: "Assumption 1 on the link function: sigma normalized (E[sigma^2] = 1); the first non-zero Hermite coefficient has degree k* and c_{k*} is an absolute constant bounded away from zero ('prominent'); E[sigma^4] <= B_4 < infinity; E[(sigma')^2] = sum_{k >= k*} k c_k^2 <= C_{k*}. The link function sigma is KNOWN. The x-marginal is exactly N(0, I_d). The guarantee is C·OPT + eps with C = O(C_{k*}), not OPT + eps."
model_class: "Gaussian single-index model sigma(w* · x) with KNOWN link sigma satisfying Assumption 1; x ~ N(0, I_d); labels y arbitrary (agnostic). Proper learning: output is a unit vector w_hat. NOT neural networks."
algorithm_class: "an explicit algorithm the authors state 'fits the CSQ framework' - Riemannian gradient method on the sphere after a non-trivial initialization; the matching lower bounds it nearly attains are CSQ, not SQ"
---

## Summary

This paper gives the first sample- and computationally-efficient constant-factor **agnostic** (adversarial-label-noise) proper learner for Gaussian single-index models under the general Hermite-structure condition of Assumption 1, i.e. going well beyond the monotone/Lipschitz link functions of prior robust learners. The sample complexity is `n = Theta~_{k*}(d^{ceil(k*/2)} + d/eps)`, where `k*` is the **information exponent** of the link — note the notation clash: this paper writes `k*` for the *information* exponent, whereas [DPLB24](generative-exponent-single-index.md) writes `k*` for the *generative* exponent and `l*` for the information exponent.

The result generalises Damian–Nichani–Ge–Lee's realizable-setting gradient method to the agnostic setting at essentially the same rate, and the authors state that their algorithm "fits the CSQ framework", so the bound nearly matches the known CSQ lower bounds of Damian–Lee–Soltanolkotabi and Abbe–Boix-Adserà–Misiakiewicz, "even in the realizable setting". They are also explicit that prior approaches, including the SQ-optimal method of DPLB24, "fail in the agnostic setting" and that DPLB24's noise model "does not capture the adversarial label noise studied here."

**The adversary is unbounded and uncosted.** Problem 1.1 says the labels `y` are "arbitrary". The only accounting is the comparison quantity `OPT = L_2^sigma(w*)`, which measures how badly the best hypothesis in the class fits the corrupted distribution — a budget on the *effect* of corruption, not a resource bound on whatever produces it. No computational, sample, query, or function-class restriction is imposed on the corrupting party. The learner is priced (in samples and time); the adversary is not. This is precisely the shape of near-miss the survey's programme is about: an adversary that is present in the theorem and carries no price tag.

## Claim Boundary

- **Quantified over:** all distributions `D` on `R^d x R` with Gaussian `x`-marginal and arbitrary `y`, for a fixed known link `sigma` satisfying Assumption 1. The output is proper (a unit vector), and the guarantee is `C·OPT + eps` with `C = O(C_{k*})` — a constant-factor approximation, not `OPT + eps`.
- **Model class and data assumption:** exactly `N(0, I_d)` covariates, single hidden direction, **known** link function with a *prominent* first non-zero Hermite coefficient. A result about Gaussian single-index models with a known link is not a result about neural networks; ReLU corresponds to `k* = 1` and phase-retrieval links to `k* = 2`, so the interesting `k* >= 3` regime is not the ReLU case.
- **Algorithm class:** the algorithm is CSQ-implementable by the authors' own statement, and the near-matching lower bounds are **CSQ**. CSQ is strictly weaker than SQ. The paper notes there is a separation between SQ and CSQ, and that outside CSQ one can do better in the *non*-agnostic setting — which is exactly DPLB24's `d^{k*_gen/2}`. Do not read `d^{ceil(k*/2)}` as an SQ-optimal or intrinsic threshold.
- **Does not establish:** (a) any bound on the adversary; (b) `OPT + eps`. That is ruled out by cited hardness evidence: even for ReLU links, `OPT + eps` plausibly needs `d^{poly(1/eps)}` time; (c) optimality against SQ. Their bound matches CSQ; the SQ-optimal rate for the *non*-adversarial model is governed by the generative exponent, which can be strictly smaller; (d) that adversarial label noise and the generative-exponent noise model are comparable — the paper says explicitly they are not.
- **Abstract vs theorem:** none found. The abstract states the `Õ(d^{⌈k*/2⌉} + d/eps)` rate, names `k*` as "the information-exponent of σ corresponding to the degree of its first non-zero Hermite coefficient", says the bound "nearly matches known CSQ lower bounds", and does not overclaim SQ optimality. The one thing the abstract omits is that the error guarantee is `O(OPT) + eps` rather than `OPT + eps`; that appears in the first line of the abstract as "L2^2-error of O(OPT) + ǫ", so it is present.

## Key Contributions

- Theorem 1.2: an algorithm drawing `n = Theta~_{k*}(d^{ceil(k*/2)} + d/eps)` samples, running in `poly(n,d)` time, outputting `w_hat` with `L_2^sigma(w_hat) <= C·OPT + eps`, `C = O(C_{k*})`.
- First polynomial-time constant-factor agnostic learner for Gaussian SIMs under Assumption 1, which "strongly subsumes" the bounded-activation classes used by prior robust learners and includes links far from monotone.
- Method: Riemannian optimization over the sphere following a non-trivial initialization step; the algorithm stays inside CSQ.
- Explicit clarification that the DPLB24 (generative-exponent) algorithm and the DNGL23 realizable algorithm both fail under adversarial label noise.

## Key Definitions / Theorems

**Problem 1.1 (Robustly Learning Gaussian SIMs), verbatim:**

> "Let D be a distribution of labeled examples (x, y) ∈ Rd ×R whose x-marginal is Dx = N (0, Id ) and y is arbitrary. We say that an algorithm is a C-approximate proper SIM learner, for some C ≥ 1, if given ǫ > 0 and i.i.d. samples from D, the algorithm outputs a"

(the remainder is displayed with interleaved columns in the extraction: the algorithm outputs a vector `w_hat ∈ S^{d-1}` with `L_2^sigma(w_hat) <= C·OPT + eps` where `OPT := L_2^sigma(w*)` and `w* ∈ argmin L_2^sigma(w)`)

**Assumption 1 (Family of Link Functions), verbatim (i):**

> "The first non-zero Hermite coefficient has degree k ∗ and is prominent: ck∗ is an absolute constant that is bounded away from zero."

followed by "The parameter k ∗ is known as the information exponent of σ."

**Theorem 1.2 (Main Result, Informal), verbatim:**

> "There exists an algorithm that draws n = Θ̃k∗ (d⌈k /2⌉ + d/ǫ) labeled"

> "samples, runs in poly(n, d) time, and outputs a weight vector w"

(the extraction interleaves columns; the conclusion is `L_2^sigma(w_hat) <= C·OPT + eps` with `C = O(C_{k*})`, and the sample bound reads `n = Theta~_{k*}(d^{ceil(k*/2)} + d/eps)`)

**Agnostic-model framing, verbatim:**

> "In the agnostic model, no assumptions are made on the observed labels and the goal is to compute a hypothesis that is competitive with the best-fit function in the class."

**CSQ placement, verbatim:**

> "This generalizes the algorithm of [DNGL23] to the agnostic setting and nearly matches the aforementioned CSQ lower bounds (our algorithm fits the CSQ framework)."

**Separation from the generative-exponent model, verbatim:**

> "Importantly, their model does not capture the adversarial label noise studied here."

## Connections

- Concept pages: [Information Exponent](../concepts/information-exponent.md), [CSQ Model](../concepts/csq-model.md), [Single-Index Model](../concepts/single-index-model.md), [Statistical Query Model](../concepts/statistical-query-model.md).
- Prices the same unit as [Online SGD on Non-Convex Losses from High-Dimensional Inference](information-exponent-online-sgd.md) — but at the CSQ rate `d^{ceil(k*/2)}` rather than the online-SGD rate `d^{k*-1}` — and inherits that page's caveat from [Reusing Batches Breaks the Information and Leap Exponents](reusing-batches-breaks-exponents.md).
- The CSQ lower bounds it matches come from [SGD Learning on Neural Networks: Leap Complexity](leap-complexity-sgd.md) and Damian–Lee–Soltanolkotabi.
- Explicitly incomparable to [Computational-Statistical Gaps in Gaussian Single-Index Models](generative-exponent-single-index.md) because of the noise model.
- Companion near-miss with the same uncosted adversary, one dimension up: [Algorithms and SQ Lower Bounds for Robustly Learning Real-valued Multi-index Models](robust-multi-index-sq-bounds.md).
- Authors: [Ilias Diakonikolas](../entities/ilias-diakonikolas.md).

## Open Questions / Limitations

- **The adversary carries no price tag.** Labels are "arbitrary"; there is no computational, statistical, or function-class bound on the corrupting party. Only the learner's samples and runtime are counted.
- `C·OPT + eps` rather than `OPT + eps`, with cited hardness evidence that the latter is out of reach.
- The link function must be known and must have a prominent first non-zero Hermite coefficient.
- The algorithm is inside CSQ, so it cannot exploit label pre-processing; whether an SQ-style agnostic learner can beat `d^{ceil(k*/2)}` is not addressed here (and DPLB24's method provably fails in this noise model).

## Quotes / Notable Passages

> "whose x-marginal is Dx = N (0, Id ) and y is arbitrary"

> "the algorithms developed in this prior work [DNGL23, DPVLB24] fail in the agnostic setting"
