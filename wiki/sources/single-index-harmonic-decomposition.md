---
title: Learning Single-Index Models via Harmonic Decomposition
type: source
date_ingested: 2026-08-22
authors: [Nirmit Joshi, Hugo Koubbi, Theodor Misiakiewicz, Nathan Srebro]
venue: venue unconfirmed from PDF (arXiv:2506.09887v2 [cs.LG], 29 Oct 2025)
year: 2025
tags: [learning-theory, sample-complexity, single-index-model, generative-exponent, statistical-query, low-degree-polynomials, spherical-harmonics, statistical-computational-gaps]
claim_quantifier: conditional
antecedent: "Spherical single-index models (Definition 1): input x = rz with radius r ~ nu_{d,R} independent of direction z ~ Unif(S^{d-1}), label y | (r, <w*, z>) ~ nu_d, likelihood ratio in L^2 of the null (enough label noise); nu_d known (Remark 2.1). SQ lower bound (Theorem 1(i)) is unconditional within the SQ(q, tau) model; the LDP sample lower bound (Theorem 1(ii)) holds under the low-degree conjecture and Assumption 1 (M*(nu_d) = O(d^{p/2})); the SQ-to-runtime translation q/tau^2 <= T is an informal heuristic validated by matching upper bounds; upper bounds (Theorems 2 on) additionally use Assumption 2 (a bounded transformation T_l capturing the Gegenbauer coefficient)"
model_class: "spherical single-index models over arbitrary spherically symmetric input distributions, strictly generalizing Gaussian single-index models (recovered as the special case x ~ N(0, I_d), nu_d(Y, R, Z) = rho(Y, R·Z)); label may depend on the radius r = ||x||_2"
algorithm_class: "lower bounds: SQ (query complexity q/tau^2) and low-degree polynomials (sample complexity, conditional on the low-degree conjecture); upper bounds: spectral estimators (harmonic degrees l = 1, 2), harmonic tensor unfolding (l >= 3, sample-optimal), online SGD (l >= 3, runtime-optimal)"
---

## Summary

The paper re-derives and generalizes the computational theory of single-index learning by replacing the Hermite basis with spherical harmonics. The observation is structural: the family {P_w : w in S^{d-1}} is the orbit of one distribution under the orthogonal group, so the natural decomposition is into the irreducible subspaces V_{d,l} of degree-l spherical harmonics (dim n_{d,l} = Theta(d^l)), not Hermite polynomials, and Gaussianity per se plays no role. For spherical single-index models — spherically symmetric input x = rz, label allowed to depend on both the radius r and <w*, z> — the SQ and LDP lower bounds decouple across harmonic subspaces: each l carries signal strength ||xi_{d,l}||^2 (the L^2 norm of the l-th Gegenbauer coefficient of the likelihood ratio), and the complexity parameters are M* = inf_l sqrt(n_{d,l}) / ||xi_{d,l}||^2 (samples, LDP) and Q* = inf_l n_{d,l} / ||xi_{d,l}||^2 (queries, SQ) (Theorem 1). Matching upper bounds per subspace: spectral estimators for l in {1, 2} (both sample- and runtime-optimal), harmonic tensor unfolding for l >= 3 (sample-optimal: m ≍ d^{l/2} / ||xi_{d,l}||^2), and online SGD for l >= 3 (runtime-optimal: T ≍ d^l / ||xi_{d,l}||^2) (Table 1).

Specialized to Gaussian inputs with generative exponent k* > 1, the framework recovers the known thresholds m = Theta(d^{k*/2}), T = Theta~(d^{k*/2 + 1}) and explains the algorithm zoo: the optimal degree is always l = 1 (k* odd) or l = 2 (k* even), so optimal algorithms live in the two lowest harmonic subspaces; vanilla online SGD is dominated by the high-frequency subspace V_{d,k*}, landscape smoothing reweights toward low frequencies, and the partial-trace estimator projects onto them outright. A sharper diagnosis of SGD's suboptimality follows: SGD's dynamics are unchanged when x is replaced by its direction z, and any algorithm ignoring the radius r = ||x||_2 must incur runtime Omega(d^{k*}) — so SGD is runtime-optimal among direction-only methods, and reaching Theta(d^{k*/2+1}) requires using the radial component even though it carries no information about w* (Table 2).

Beyond the Gaussian case the picture changes qualitatively: the sample-optimal degree l_{m,*} and runtime-optimal degree l_{T,*} can differ, and when l_{m,*} >> l_{T,*} the paper argues no single estimator achieves both optimal sample and runtime complexity — a sample-runtime trade-off with no Gaussian counterpart.

## Claim Boundary

- **Quantified over:** all spherical single-index models nu_d in the class L_d of Definition 1 (lower bounds; the LDP bound over sequences satisfying Assumption 1), with matching upper bounds under Assumption 2's bounded-transformation condition; the Gaussian statements over all link distributions rho with generative exponent k* > 1. The known-nu_d assumption is declared mild (random nonlinearities otherwise, Appendix A.1).
- **Antecedent and whether it holds:** three separate conditionality layers. The SQ bound is unconditional within SQ(q, tau), but its reading as a runtime bound rests on the heuristic that each tolerance-tau query costs Omega(1/tau^2) samples, "validated by our matching upper bounds" rather than proven. The LDP sample bound assumes the low-degree conjecture, which this corpus records as disproved in a quasi-polynomial regime by Buhai et al. FOCS'25 — for the polynomial-factor regime used here the conjecture stands but any citation must carry that caveat. The L^2 likelihood-ratio condition is what excludes non-robust algorithms (e.g. the lattice-based noise-free attacks of Song-Zadik-Bruna, cited as [SZB21]) — noise-free models fall outside the theorems.
- **Does not establish:** (a) lower bounds against all polynomial-time algorithms — everything is SQ- or LDP-relative, plus the conditional low-degree step; "sample-optimal" is defined in the paper as optimal conjectural sample complexity for polynomial-time algorithms (footnote 4); (b) estimation-threshold lower bounds — Theorem 1's bounds are for the detection problem (distinguishing planted from null), with Remark 3.1 noting a detection-recovery gap can appear (when the infimum sits at l = 1 and sqrt(d)/||xi_{d,1}||^2 << d, the information-theoretic Omega(d) recovery bound is the tighter one); the upper bounds are recovery guarantees (weak recovery |<w_hat, w*>| >= 1/4, boosted to strong recovery with Theta(d/eps) more samples under mild assumptions, Remark 3.3), so upper and lower bounds do not measure the same task except where they match; (c) impossibility of jointly optimal estimators when l_{m,*} = l_{T,*} > 2 — stated open (footnote 5: for even l, harmonic tensor unfolding achieves both up to a log factor); the "no algorithm can simultaneously achieve both" reading for l_{m,*} >> l_{T,*} is presented as suggested by the decoupled bounds, not proven against general algorithms; (d) multi-index results — left to future work, with the concurrent generative-leap paper handling the Gaussian multi-index case by (Hermite) tensor unfolding.
- **Abstract vs theorem:** the abstract's "characterize the complexity of learning" is delivered in the decoupled SQ/LDP sense above; "argue that estimators achieving both may not exist in general" is correctly hedged ("argue", "may"). The additional D^{-Theta(1)}-samples-for-d^{Theta~(D)}-runtime trade-offs are acknowledged and set aside (Remark 3.2).

## Key Contributions

- Theorem 1: general SQ query lower bound q/tau^2 >= Q*(nu_d) and (conditional) LDP sample lower bound m = Omega(M*(nu_d) log(d)^{-Cp}) for detection, decoupling across harmonic subspaces.
- Table 1's matching estimators per subspace: spectral (l = 1: m ≍ d ∨ sqrt(d)/||xi_{d,1}||^2; l = 2: m ≍ d/||xi_{d,2}||^2, T ≍ (d^2/||xi_{d,2}||^2) log d), harmonic tensor unfolding (l >= 3: m ≍ d^{l/2}/||xi_{d,l}||^2, T ≍ (d^{l+1}/||xi_{d,l}||^2) log d), online SGD (l >= 3: m ≍ d^{l-1}/||xi_{d,l}||^2, T ≍ d^l/||xi_{d,l}||^2).
- Gaussian specialization (Table 2): optimal degree is 1 or 2 by parity of k*; spectral algorithm attains m ≍ d^{k*/2}, T ≍ d^{k*/2+1} log d; explanation of smoothing and partial trace as low-frequency reweighting/projection.
- The radial-component theorem: algorithms ignoring r = ||x||_2 incur runtime Omega(d^{k*}); SGD is runtime-optimal within that restricted class.
- The beyond-Gaussian phenomenon: l_{m,*} ≠ l_{T,*} is possible, yielding sample-runtime trade-offs absent in the Gaussian case.

## Relation to the generative-exponent line

The paper refines rather than contests the Gaussian threshold. For Gaussian single-index models it reproduces m = Theta(d^{k*/2}) for k* > 1 — the single-index case of the n = Theta(d^{max(1, k*/2)}) law — and adds structure: which harmonic subspace the optimal algorithm uses, why each known algorithm does or does not reach the threshold, and what SGD's missing resource is (the radius). The contest, such as it is, is at the level of the basis and the scope: the Hermite/generative-exponent description is exposed as the Gaussian shadow of an orthogonal-group-representation statement, and outside the Gaussian case the single number k* is replaced by the profile {||xi_{d,l}||^2}_l, where sample- and runtime-optimality can genuinely split. For the multi-index side, it cites the concurrent generative-leap paper's unbalanced Hermite tensor unfolding achieving n ≳ d^{1 ∧ k*/2} as "very similar" to its harmonic tensor unfolding, and predicts (conclusion) that in multi-index models landscape smoothing and partial trace fail while tensor unfolding on V_{d,s} becomes necessary. It also expects the batch-reuse SGD algorithms to remain SQ-bounded, hence still governed by the generative exponent.

## Connections

- Refines: [generative-exponent-single-index](generative-exponent-single-index.md) (thresholds (3) here are that paper's Theorem; the partial-trace estimator explained as V_{d,1}/V_{d,2} projection). Sibling scope extension: [generative-leap-multi-index](generative-leap-multi-index.md) (cited as concurrent [DLB25]).
- Explains the suboptimality of: [information-exponent-online-sgd](information-exponent-online-sgd.md) (online SGD dominated by V_{d,k*}; runtime-optimal only among direction-only algorithms) and the optimality of smoothing (Damian et al. [DNGL24], cited within [generative-exponent-single-index](generative-exponent-single-index.md)).
- Places the batch-reuse line ([reusing-batches-breaks-exponents](reusing-batches-breaks-exponents.md), [sgd-reuse-info-theoretic-limit](sgd-reuse-info-theoretic-limit.md), [repetita-iuvant-data-repetition](repetita-iuvant-data-repetition.md)) inside SQ: "we expect these algorithms to still fall under the SQ framework and be lower bounded by the generative exponent."
- The low-degree conditionality connects to the corpus's standing caveat from Buhai et al. FOCS'25 on [statistical-computational gaps](../concepts/statistical-computational-gaps.md); concepts: [generative exponent](../concepts/generative-exponent.md), [generative leap exponent](../concepts/generative-leap-exponent.md), [information exponent](../concepts/information-exponent.md), [single-index model](../concepts/single-index-model.md), [Statistical Query Model](../concepts/statistical-query-model.md).
- Tensor PCA lineage for the estimators (partial trace, unfolding, smoothing): [reducibility-statistical-computational-gaps](reducibility-statistical-computational-gaps.md) is the corpus's nearest node for planted-tensor machinery.

## Open Questions / Limitations

- Whether a single estimator can be jointly sample- and runtime-optimal when l_{m,*} = l_{T,*} > 2 (odd l) is open.
- The impossibility reading of l_{m,*} >> l_{T,*} is an inference from class-relative bounds, not a theorem against all algorithms.
- Multi-index spherical models and general compact symmetry groups (via Peter-Weyl) are future work.
- Estimation-threshold lower bounds (as opposed to detection) are not given; the detection-recovery gap at l = 1 is flagged, not resolved beyond the information-theoretic bound.

## Quotes / Notable Passages

> "we argue that spherical harmonics—rather than Hermite polynomials—provide the natural basis for this problem, as they capture its intrinsic rotational symmetry"

> "The lower bounds in Theorem 1 are for the detection problem." (Remark 3.1, which continues by locating the regime where a detection-recovery gap appears)

> "We show that algorithms that ignore r must incur a runtime complexity of Ωd (dk⋆ )." (extraction flattens: Omega_d(d^{k*}))

> "Additional sample-runtime trade-offs appear when learning SIMs beyond the Gaussian setting."

> "we expect these algorithms to still fall under the SQ framework and be lower bounded by the generative exponent" (on the multi-pass / modified-loss algorithms)
