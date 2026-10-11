---
title: The Benefits of Reusing Batches for Gradient Descent in Two-Layer Networks - Breaking the Curse of Information and Leap Exponents
type: source
date_ingested: 2026-08-20
authors: [Yatin Dandi, Emanuele Troiani, Luca Arnaboldi, Luca Pesce, Lenka Zdeborová, Florent Krzakala]
venue: "ICML 2024"
venue_evidence: "dblp: conf/icml/DandiTAPZK24 (inproceedings, ICML 2024, PMLR pp. 9991-10016); confirms the in-corpus citation lead"
year: 2024
tags: [learning-theory, sample-complexity, information-exponent, leap-complexity, dynamical-mean-field-theory, feature-learning]
claim_quantifier: universal
antecedent: "n/d = alpha > 0 fixed (proportional regime); sigma analytic with polynomially bounded derivatives, E[sigma'(z)] != 0 and sigma^k(0) != 0 for all k; g* with polynomially bounded derivatives; second-layer weights a fixed at initialization; symmetric initialization a_i = -a_{p-i+1}, w_i^0 = w_{p-i+1}^0; orthogonal normalized teacher rows; d -> infinity."
model_class: "Gaussian multi-index teacher y = g*(W* z / sqrt(d)) with orthogonal row-normalized W* in R^{k x d}, z ~ N(0, I_d); two-layer student, first layer trained only. Proportional regime n = alpha d."
algorithm_class: "multi-pass (full-batch) gradient descent with batch reuse, finite stepsize, batch size n = O(d); contrasted against single-pass / online SGD and population gradient flow"
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
cls_second_notion: time
cls_assessed: explicit
cls_evidence: "We disprove this conjecture and show that the sample complexity for a large class of functions can be reduced to O(d) independently of the leap exponent ℓ."
cls_evidence_src: "§1"
cls_reason: "No ML attack scenario; a pure learning-theory result, matching sibling exponent pages (target/family/phase/access/write=none/none/n/a/none/none). party=learner per rule 3: the bound binds the multi-pass GD algorithm. unit=samples/tightness=exponent for the explicit O(d) sample threshold, stated as a relation to the leap-l-dependent threshold the honest single-pass algorithm needed, matching the generative-exponent/generative-leap convention for a stated sample-complexity relation. second_notion=time records Theorem 3.2's explicit T=2 gradient-step bound, the same party (learner) under an incomparable resource notion (rule 4b), matching leap-complexity-sgd's second_notion=time convention. baseline=stated: the disproved comparison point is Abbe et al. (2023)'s conjectured O(d^max(l/2,1)) threshold, explicitly named and superseded. Not recorded: the paper's own 'expectation' that GD inherits SQ hardness (Claim Boundary: 'that is an expectation, not a theorem'), so no second_notion=algo class is added for it."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This is the load-bearing negative result of the exponent literature. The paper shows that **multi-pass gradient descent that reuses the same batch escapes the information-exponent and leap-exponent barriers**, learning a much broader class of directions than single-pass methods — and in just `T = 2` gradient steps, in the proportional regime `n = alpha d`.

The mechanism is stated cleanly. With independent Gaussian data, one-pass SGD and population gradient flow keep the pre-activations Gaussian; that Gaussianity is what the whole single-pass analysis rests on. Reusing batches makes the pre-activations develop non-Gaussian components correlated with the targets, which is equivalent to *implicitly* transforming the labels. Because the barrier that the information exponent and leap encode is the barrier for correlational queries `E[y phi(x)]` (i.e. `F = id`), an implicit label transformation steps outside it.

Definition 3.1 makes this precise. `P*` is the subspace of directions `v*` such that `E_z[F(f*(z)) <v*, z>] = 0` for *every polynomial* `F`, and `A*` the same for every real-analytic `F`. Theorem 3.2 says: directions in `P*_⊥` are learned in `T = 2` gradient steps (`|W^{(2)} v*| / d = Theta_d(1)`), and if the whole teacher subspace lies in `A*` then no direction is learned in any finite number of steps. Section 3.2 characterises hard directions by symmetry: even-symmetric (`E*`) and orthogonally-even-symmetric (`OE*`) directions satisfy `E* ⊆ OE* ⊆ A*`. Phase retrieval / even links stay hard; `He_3` (information exponent 3) becomes learnable in two steps.

The paper explicitly disproves the [ABM23](leap-complexity-sgd.md) conjecture that batch reuse can only reduce a leap-`l` target's complexity to `O(d^{max(l/2,1)})`, and reduces it to `O(d)` independently of the leap for a broad class. It also states the correct residual expectation: since Definition 3.1's `F` are exactly what SQ allows and CSQ forbids, the authors "expect gradient descent with O(d) sample complexity to inherit the hardness results established for the class of SQ algorithms".

The proof is via rigorous Dynamical Mean Field Theory (DMFT), building on Celentano et al. and Gerbelot et al., and yields a closed-form integro-differential description of the low-dimensional weight projections.

## Claim Boundary

- **Quantified over:** all multi-index teachers `g*` with polynomially bounded derivatives, all directions `v*` in `P*_⊥` (positive result) and teacher subspaces contained in `A*` (negative result), in the limit `n, d -> infinity` with `n/d = alpha > 0` fixed.
- **Model class and data assumption:** isotropic Gaussian inputs, orthogonal row-normalized teacher weights, two-layer student with the **second layer frozen at initialization** and symmetric initialization. This is a result about first-layer feature learning, not about training a full network. The regime is proportional (`n = alpha d`) rather than polynomial-in-`d` scaling.
- **Algorithm class:** multi-pass full-batch GD with finite stepsize and explicit `l2` regularization, batch size `O(d)`. The remark on general multi-pass schemes says Theorem 3.2 remains valid when cycling over epochs. The negative half (directions in `A*` never learned in finite time) is a statement about *this* algorithm class, not a hardness result.
- **Does not establish:** (a) that multi-pass GD is SQ-optimal in general. The paper says it "expect[s]" GD with `O(d)` samples to inherit SQ hardness; that is an expectation, not a theorem; (b) any lower bound against SQ, CSQ, or low-degree algorithms; (c) that the information exponent and leap are wrong *for their own algorithm class*. They are correct there. What is refuted is the reading of them as intrinsic hardness measures; (d) that all targets become easy — even single-index links (phase retrieval, `He_4`) remain hard in finite time for both algorithms, and `OE*` can be strictly larger than `E*` (e.g. `f*(z) = z_1 z_2 z_3` with `v* = e_1 + e_2 + e_3`).
- **Abstract vs theorem:** none found. The abstract's claim — "multi-pass GD with finite stepsize is found to overcome the limitations of gradient flow and single-pass GD given by the information exponent ... and leap exponent" and "the network achieves in just two time steps an overlap with the target subspace even for functions not satisfying the staircase property" — is Theorem 3.2 verbatim in content. The word "efficiently learned in finite time" is defined by Definition 3.1 rather than by a runtime bound.

## Key Contributions

- Definitions 3.1, 3.3, 3.4: the hard subspaces `P*` (polynomial `F`), `A*` (analytic `F`), `E*` (even-symmetric), `OE*` (orthogonally-even-symmetric), with `E* ⊆ OE* ⊆ A* ⊆ P*_hard`.
- Theorem 3.2: directions in `P*_⊥` learned in `T = 2` multi-pass GD steps; nothing learned in finite time if `U* = A*`.
- Proposition 3.5: `OE* ⊆ A*`, so symmetry is a sufficient condition for hardness.
- Explicit disproof of the ABM23 batch-reuse conjecture; reduction of leap-`l` sample complexity to `O(d)`.
- Rigorous DMFT analysis of GD with correlated (reused) samples, plus a closed-form description of the dynamics of low-dimensional weight projections.
- The "hidden progress" concept: measurable progress accumulates in non-Gaussian components of the pre-activations before the overlap becomes macroscopic.

## Key Definitions / Theorems

**Definition 3.1, verbatim:**

> "We define P ⋆ as the subspace of directions v⋆ ∈ U ⋆ such that for any polynomial F : R → R with coefficients in R, the following condition is satisfied: Ez [F (f ⋆ (z))⟨v⋆ , z⟩] = 0,"

and, after the equation number, "Similarly, we denote by A⋆ , the subspace of directions where the above condition is satisfied for all real-valued analytic functions F ."

**Theorem 3.2 (abridged, statements verbatim in the display form):** under `n/d = alpha > 0` and the activation conditions, for `v*` in `P*_⊥`: `|W^{(2)} v*| / d = Theta_d(1)` w.h.p.; and `inf_{v* in P*_⊥} |W^{(2)} v*| / d = Theta_d(1)` for large `p`; whereas if `U* = A*` then `sup_{v* in U*} |W^{(t)} v*| / d = o_d(1)` for any finite `t`.

**Definition 3.6 (Information Exponent, as they restate BGJ21), verbatim:**

> "Let Hej be the j−th Hermite polynomial. Using the definition for the target of eq. (1), reading in the single-index case as f ⋆ = g ⋆ (⟨w⋆ , z⟩), the IE is defined as: IE = min{j ∈ N : Eξ∼N (0,1) [g ⋆ (ξ)Hej (ξ)] ̸= 0}"

with the single-pass time `T(IE) = O(d^{IE-1})` for `IE > 2`, `O(d log d)` for `IE = 2`, `O(d)` for `IE = 1` (Eq. 13).

**The refutation, verbatim:**

> "that re-using the batch can reduce the sample complexity of the target with leap ℓ only up to O(dmax( 2 ,1) ), corresponding to the lower bound for Correlational Statistical Query (CSQ) algorithms. We disprove this conjecture and show that the sample complexity for a large class of functions can be reduced to O(d) independently of the leap exponent ℓ."

(the sentence opens "Moreover, (Abbe et al., 2023) conjecture"; the `O(d^{max(l/2,1)})` exponent floats in the extraction)

**The exact scope statement, verbatim:**

> "More generally, our results show that CSQ lower bounds and the notions of staircase property and information exponent are limited to online-SGD on Gaussian/Boolean data, and do not describe the class of functions inherently easy or hard to learn by gradient-based methods."

**The residual SQ expectation, verbatim:**

> "The presence of general transformations F in definition 3.1 allows our algorithm to bypass CSQ bounds, which are restricted to F = id. Such general transformations are however permitted under the framework of Statistical Query (SQ) algorithms (Kearns, 1998). We thus expect gradient descent with O(d) sample complexity to inherit the hardness results established for the class of SQ algorithms"

## Connections

- **Caveat target:** [Online SGD on Non-Convex Losses from High-Dimensional Inference](information-exponent-online-sgd.md) (information exponent) and [SGD Learning on Neural Networks: Leap Complexity](leap-complexity-sgd.md) (leap). Both pages carry the cross-referenced caveat.
- Also limits [The Merged-Staircase Property](merged-staircase-property.md) (the staircase property is not the learnability boundary once batches are reused).
- Consistent with, and partly anticipating, the [generative exponent](generative-exponent-single-index.md): the label transformations that GD performs implicitly are exactly the `T` in DPLB24's Proposition 2.6. [The Generative Leap](generative-leap-multi-index.md) cites this work for "SGD with reused samples can learn single index models dependent on the generative exponent, instead of the information exponent."
- [Noise Sensitivity Exponent](noise-sensitivity-exponent.md) cites this paper as the reason the information exponent "can be easily bypassed by data reuse", and works in the same proportional regime `n = alpha d`.
- Sharpened by [Learning Rate Induces Phase Transitions in SGD](learning-rate-induces-generative-exponent.md): the batch-reuse escape holds only above a learning-rate threshold, interpolating back to the information-exponent complexity as learning rates shrink, and a one-pass layer-wise algorithm reaches the same non-correlational regime with no batch reuse at all. The escape is therefore a property of (reuse, learning rate) jointly.
- Concepts: [Information Exponent](../concepts/information-exponent.md), [Leap Complexity](../concepts/leap-complexity.md), [CSQ Model](../concepts/csq-model.md), [Statistical Query Model](../concepts/statistical-query-model.md), [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md), [Multi-Index Model](../concepts/multi-index-model.md).
- Authors: [Lenka Zdeborová](../entities/lenka-zdeborova.md), [Florent Krzakala](../entities/florent-krzakala.md).

## Open Questions / Limitations

- The claimed inheritance of SQ hardness by multi-pass GD is an expectation, not a proof.
- Second-layer weights frozen; symmetric initialization; orthogonal teacher rows.
- The characterisation of hard directions is not tight: `OE*` is the largest identified hard set, but "the true set of hard directions may be larger still and is given by A⋆ ".
- Proportional regime only; the results are asymptotic in `d` with `n/d` fixed, so they do not directly compare to `d^{k}` polynomial-scaling thresholds without care.
- Results are stated for finite `T`; the interplay when learning directions in `P*_⊥` unlocks directions in `U*` at later timesteps is only discussed (Appendix A.6).

## Quotes / Notable Passages

> "contrary to the common wisdom “the more data the better”, gradient descent on the same batch can surpass one-pass SGD on different batches, even when one-pass SGD utilizes a larger number of datapoints"

> "upon re-using batches, the pre-activations develop non-Gaussian components correlated with the targets"

> "unlike explicit SQ algorithms, our analysis shows that gradient descent performs such transformations implicitly"
