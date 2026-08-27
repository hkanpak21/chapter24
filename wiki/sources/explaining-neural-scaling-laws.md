---
title: Explaining Neural Scaling Laws
type: source
date_ingested: 2026-08-22
authors: [Yasaman Bahri, Ethan Dyer, Jared Kaplan, Jaehoon Lee, Utkarsh Sharma]
venue: venue unconfirmed from PDF (arXiv:2102.06701v2; PNAS 2024 attribution not stated in the PDF)
year: 2024
tags: [scaling-laws, learning-theory, sample-complexity]
claim_quantifier: conditional
antecedent: variance-limited results need a well-behaved infinite-data or infinite-width limit with sufficiently smooth loss; resolution-limited results need train and test data i.i.d. on a compact d-dimensional manifold with Lipschitz loss, model, and target
model_class: general nonlinear models for the bounds; linear random-feature models for the exact exponents; deep networks empirically
algorithm_class: gradient-based training; exact results in solvable linear limits
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
cls_second_notion: parameters
cls_assessed: explicit
cls_evidence: "dataset of size D sampled i.i.d from Md and let f (x) = F(x), ∀x ∈ D then L(D) = O KL max(Kf , KF )D−1/d"
cls_evidence_src: Thm 2
cls_reason: "Classified on the resolution-limited regime (Theorems 2/3) rather than the fully proven variance-limited regime (Theorem 1), a judgement call under rule 1: the abstract introduces both regimes without privileging one, and the resolution-limited half is the one the Claim Boundary flags as 'the reason it is in this corpus' and the one that connects to Kaplan/Chinchilla's empirical regime; Theorem 1's exponent=1 result is the alternative primary claim, noted here for a second reader. unit=samples/second_notion=parameters (rule 4b) for the paired L(D)=O(D^-1/d), L(P)=O(P^-1/d) bounds. tightness=exponent for the explicit power-law upper bound, matching the generative-exponent-single-index convention for a one-sided (upper-bound-only) exponent formula rather than a raw measured number. baseline=absent: the page's own Open Questions state tightness of Theorems 2/3 in general nonlinear models is open, i.e. no matching lower bound is given."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The taxonomy paper for scaling-law mechanisms. It splits scaling in dataset size D and parameter count P into four regimes. Variance-limited scaling (in D with P fixed, or in P with D fixed) has universal exponent 1: loss approaches its limit as 1/D or 1/sqrt(P) in deep networks, purely because a well-behaved infinite limit exists and fluctuations around it are averaged. Resolution-limited scaling (the regime the empirical laws of Kaplan et al. live in) has task-dependent exponents 0 < α < 1, explained by the model interpolating a smooth data manifold of intrinsic dimension d, giving loss O(D^{-1/d}) or O(P^{-1/d}), sharpened to roughly 4/d for smooth loss in the teacher-student experiments.

The epistemic split inside the paper is the reason it is in this corpus. The variance-limited exponent is proven (Theorem 1) under smoothness assumptions. The resolution-limited exponents are upper bounds (Theorems 2 and 3) plus a stated hypothesis that the bounds are tight, verified exactly only in linear random-feature models via kernel spectra, and empirically elsewhere. In the random-feature setting the paper derives both exponents exactly and exhibits a duality between model-size and dataset-size scaling.

## Claim Boundary

- Quantified over: Theorem 1 over losses and models with the stated smoothness and a well-behaved limit. Theorems 2 and 3 over Lipschitz L, f, F and i.i.d. data on a compact manifold, and they are O(·) upper bounds only. The exact exponent statements are quantified over linear random-feature models and nothing wider.
- Antecedent: for the resolution-limited story, that the model interpolates the data manifold and that the bound is tight. Tightness is a conjecture, stated as such ("we expect the stronger statement"). Manifold-dimension dependence of real exponents is empirical and mixed, clean for teacher-student, unclear for CNNs and Wide ResNets in their own Figure 1b.
- Does not establish: any statement about what other algorithms could achieve, any lower bound outside the solvable models, or that measured exponents on real data are governed by intrinsic dimension. The 4/d relation is a prediction that their standard-dataset experiments only partially match.
- Abstract against theorem: the abstract's "can be explained by positing" is accurately hedged. The nearby folk citation of this paper as proving α = 4/d overstates it. The proven content is exponent 1 in the variance-limited regimes and O(x^{-1/d}) bounds in the resolution-limited ones.
- Status by regime: variance-limited, proven within assumptions. Resolution-limited, heuristic (bounds plus a tightness hypothesis), proven exactly only in linear random-feature limits. Breaks where the smoothness or i.i.d.-manifold assumptions fail, and says nothing where feature learning changes the kernel spectrum, the gap taken up by Bordelon et al.
- No-skipping postulate: neutral. It explains why one recipe's loss falls at its observed rate, and its exponents are properties of the model-data pair under the assumed training, so it grounds the recipe-relative reading without bounding any alternative recipe.

## Key Contributions

- The four-regime taxonomy: variance-limited against resolution-limited, in each of D and P.
- Theorem 1: variance-limited exponent 1 under general smoothness assumptions.
- Theorems 2, 3: L(D) = O(D^{-1/d}) and L(P) = O(P^{-1/d}) for Lipschitz loss, model, and target on a compact d-manifold.
- Exact exponents in linear random-feature models via kernel spectral decay, with a model-size/dataset-size duality.
- Empirical tests on standard architectures, including the 4/d interpolation check and the finding that switching datasets or adding noise moves exponents while superclassing does not.

## Key Definitions / Theorems

- Theorem 1 (variance-limited scaling). For test loss L = E[l(f)] with l smooth and the network output concentrating with variance O(1/x), the loss deviates from its limit as O(1/x), x = D or P appropriately.
- Theorem 2 (resolution-limited, data). L, f, F Lipschitz, dataset i.i.d. from a compact d-manifold, f exact on the training set. Then L(D) = O(K_L max(K_f, K_F) D^{-1/d}).
- Theorem 3 (resolution-limited, parameters). Same hypotheses with f exact on P sampled points. Then L(P) = O(K_L max(K_f, K_F) P^{-1/d}).
- The tightness upgrade to estimates, and the sharpening toward exponent c/d with c up to 4 for smooth loss, are stated as expectations, argued in the linear setting, and left unproven in general.

## Connections

- Mechanism candidate for the fits in [scaling-laws-neural-lm](scaling-laws-neural-lm.md).
- The random-feature exact regime is the static ancestor of [compute-optimal-phases](compute-optimal-phases.md) and [dynamical-model-scaling-laws](dynamical-model-scaling-laws.md), which add training dynamics.
- [feature-learning-improves-scaling](feature-learning-improves-scaling.md) shows the kernel-spectrum mechanism is algorithm-dependent, bounding this paper's reach.
- [data-pruning-beats-power-laws](data-pruning-beats-power-laws.md) attacks the same exponent from the data side: power laws reflect redundancy in i.i.d. sampling, which pruning removes.

## Open Questions / Limitations

- Tightness of Theorems 2 and 3 in general nonlinear models. Open.
- Whether intrinsic manifold dimension predicts measured exponents for standard vision architectures. Their own Figure 1b shows the relation is unclear there. Empirical, mixed.
- The framework has no account of feature learning, by construction of the solvable limit.

## Quotes / Notable Passages

> "We derive the variance-limited regime under simple yet general assumptions (Theorem 1)."

> "We present a hypothesis for resolution-limited scaling through refinement of naive bounds (Theorems 2, 3), for general nonlinear models."

(Both from the summary of contributions. The word "hypothesis" is the paper's own epistemic label for the resolution-limited half.)

> "Theorems 2 and 3 are phrased as bounds, but we expect the stronger statement that these bounds also generically serve as estimates"

(Section 2.2.3.)

> "the resolution-limited regime can be explained by positing that models are effectively resolving a smooth data manifold"

(Abstract.)
