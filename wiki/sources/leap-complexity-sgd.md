---
title: SGD learning on neural networks - leap complexity and saddle-to-saddle dynamics
type: source
date_ingested: 2026-08-20
authors: [Emmanuel Abbe, Enric Boix-Adserà, Theodor Misiakiewicz]
venue: "COLT 2023"
venue_evidence: "dblp: conf/colt/AbbeAM23, inproceedings; also proceedings.mlr.press/v195/abbe23a.html, pp. 2552-2623"
year: 2023
tags: [learning-theory, sample-complexity, leap-complexity, csq, feature-learning, multi-index-model]
claim_quantifier: conditional
antecedent: "The headline scaling Theta~(d^{max(Leap,2)}) is stated as Conjecture 1, for all but a measure-0 set of coefficient vectors. What is PROVED is a specialisation: 2-layer network with smooth activations (Assumption 1), layer-wise SGD with an entrywise l-infinity projection step, isotropic Gaussian data, and a representative subclass of nested-monomial targets (Eq. 11) with min leap >= 2; second-layer fitting proved only for the multilinear subclass (Eq. 12)."
model_class: "Low-latent-dimension targets f*(x) = h*(Mx) with P = O_d(1), over isotropic Gaussian N(0,I_d) or uniform hypercube. The proved theorems assume Gaussian data AND that z is a subset of P coordinates of x (not a general subspace), because of the entrywise projection step. NOT a result about general neural networks."
algorithm_class: "online SGD (fresh sample per step) on a 2-layer network, layer-wise with projected gradient steps; lower bounds are CSQ (and noisy population-GD), NOT SQ"
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: algo class
cls_tightness: class
cls_baseline: n/a
cls_second_party: none
cls_second_notion: time
cls_assessed: explicit
cls_evidence: "the CSQ complexity of learning f\u2217 to less than \u03b5h\u2217 error is at least ch\u2217 dLeap(h\u2217 ) in the Boolean case, and at least ch\u2217 dLeap(h\u2217 )/2 in the Gaussian case."
cls_evidence_src: Prop 2
cls_reason: "Paper prices the SGD learner, not an attacker; party=learner per rule 3. unit=algo class (CSQ, Prop 2) is primary since the paper's universal lower bound is stated over the CSQ class; second_notion=time records the paired online-SGD time/sample complexity (Thm 1-2, Conjecture 1) as a second, incomparable resource notion on the same party per rule 4b. baseline=n/a since no attacker success criterion applies."
cls_prov: S
cls_date: 2026-08-22
---

## Summary

This paper introduces the **leap** as a graded generalisation of the merged-staircase property and conjectures that it controls the time complexity of SGD learning on regular fully-connected networks with isotropic data. The leap of a target `h*` with non-zero basis support `{S_1, ..., S_m}` is the minimum over orderings of the largest number of new coordinates (counted with Hermite multiplicity in the Gaussian case) that any one monomial adds to the union of its predecessors. Leap-1 on the hypercube is exactly MSP.

The headline result is **Conjecture 1**: online SGD reaches risk `eps` iff `t = Omega~_d(d^{Leap(h*)-1 ∨ 1}) poly(1/eps)`, i.e. total time `Omega~_d(d^{Leap(h*) ∨ 2}) poly(1/eps)`, for all but a measure-0 set of coefficients. This is a conjecture, not a theorem.

What is proved is a specialisation. Theorems 1 and 2 show sequential first-layer alignment for nested-monomial targets (Eq. 11) on isotropic Gaussian data, using a 2-layer network with smooth activation, layer-wise training, and a projection step that makes the algorithm non-rotationally-equivariant; the alignment takes `T^1 = C_0 d^{D-1} log(d)^{C_0}` steps where `D` is the largest leap. Corollary 2 completes the risk bound only for the multilinear "leap-staircase" subclass (Eq. 12), and only for *some* activation satisfying Assumption 1. The mechanism is saddle-to-saddle: the network sits on a plateau whose length is set by the current leap, then escapes with a loss drop.

On the lower-bound side, Proposition 1 gives `c d^D` for linear/kernel methods (`D` the degree), and Proposition 2 gives `c d^{Leap(h*)}` in the **Boolean** case and only `c d^{Leap(h*)/2}` in the **Gaussian** case for **CSQ**. This CSQ-matching is the paper's own framing of optimality — and it is exactly why the later [generative exponent](generative-exponent-single-index.md) improves on it, since general SQ queries `E[phi(X,Y)]` may pre-process the label and beat `d^{l*/2}`.

## Claim Boundary

- **Quantified over:** Conjecture 1 ranges over all low-latent-dimension `f*` with `P = O_d(1)` on Gaussian or hypercube data, all-but-measure-0 in coefficients, for fully-connected `poly(d)`-edge networks with rotationally-invariant initialization. The theorems range over the nested-monomial class (Eq. 11) with `min_l D_l >= 2`; the risk statement over the multilinear class (Eq. 12).
- **Model class and data assumption:** low-dimensional latent structure with constant `P`. The proved theorems restrict to **Gaussian** data and to `z` being a *subset of coordinates* of `x` rather than a general subspace — a limitation the authors attribute to their entrywise projection step, which "makes the training algorithm non-rotationally equivariant". Remark 2 further notes the CSQ correspondence "may not hold beyond the finite P regime".
- **Algorithm class:** upper bounds are for online SGD (one fresh sample per step) on a 2-layer network with *layer-wise* training and projected gradients — a modified SGD, listed in the discussion as something future work should remove. Lower bounds are **CSQ** (or noisy population-GD), explicitly *not* online-SGD, since online SGD takes one sample per step and CSQ adds query noise (Remark 2). **CSQ is strictly weaker than SQ.** Do not read Proposition 2 as an SQ bound.
- **Does not establish:** (a) Conjecture 1. The abstract says "We prove a version of this conjecture for a class of functions on Gaussian isotropic data and 2-layer neural networks, under additional technical assumptions on how SGD is run"; the conjecture itself is open; (b) an SQ lower bound. The Gaussian CSQ bound is `d^{Leap/2}`, and even the conjectured Boolean-matching `d^{Leap}` is CSQ; (c) that the leap is intrinsic hardness. [DTA+24](reusing-batches-breaks-exponents.md) disproves the specific conjecture that batch reuse can only reduce a leap-`l` target's sample complexity to `O(d^{max(l/2,1)})`, and reduces it to `O(d)` for a broad class; (d) the per-saddle scaling `d^{D_l - 1}` at constant step size — Theorem 2 captures the overall count, and the per-leap scaling is only obtained by varying the step size (Appendix D.2.1).
- **Abstract vs theorem:** the abstract states `Theta~(d^{max(Leap(f),2)})` as "our main conjecture" and is explicit that only a version is proved — good. The one place to watch is the final abstract sentence, "this gives an SGD complexity for the full training trajectory that matches that of Correlational Statistical Query (CSQ) lower-bounds": in the Gaussian case the proved CSQ bound is `d^{Leap/2}`, not `d^{Leap}`, so the "match" is to the conjectured Boolean scaling.

## Key Contributions

- Definition 1: the leap complexity, `Leap(h*) := min_{pi} max_i || S_{pi(i)} \ ∪_{j<i} S_{pi(j)} ||_1`, with Hermite multiplicity in the Gaussian case.
- Conjecture 1: `Theta~(d^{Leap ∨ 2})` total time complexity for regular networks with rotationally invariant initialization.
- Theorems 1-2: sequential (saddle-to-saddle) first-layer alignment for single monomials and nested monomials, with full control of the time complexity — no infinite-width or continuous-time approximation, going beyond the mean-field regime of [ABM22](merged-staircase-property.md).
- Corollaries 1-2: second-layer fitting, giving `R <= eps` after `T^1 = Theta~(d^{Leap-1})`, `T^2 = poly(1/eps)`.
- Proposition 1: linear/kernel lower bound `c d^D` extended from the Boolean to the Gaussian case.
- Proposition 2: CSQ lower bound `c d^{Leap}` (Boolean) and `c d^{Leap/2}` (Gaussian).
- The curriculum-learning reading: inserting an intermediate monomial lowers the leap and hence the complexity.

## Key Definitions / Theorems

**Definition 1 (Leap complexity), verbatim:**

> "Let h∗ be as before with non-zero basis elements given by the subset S(h∗ ) := {S1 , . . . , Sm }, m ∈ Z+ . We define the leap complexity of h∗ as"

followed by the display `Leap(h∗ ) := min_{π∈Π_m} max_{i∈[m]} || S_{π(i)} \ ∪_{j=0}^{i−1} S_{π(j)} ||_1`,

with `|| S_{pi(i)} \ ∪_{j=0}^{i-1} S_{pi(j)} ||_1 := sum_{k in [P]} S_{pi(i)}(k) 1{S_{pi(j)}(k) = 0, ∀ j in [i-1]}`, `S_{pi(0)} = 0_P`.

**Conjecture 1, verbatim:**

> "Then, for all but a measure-0 set of functions (see below), the risk is bounded by"

and, after the displayed risk expression, "≤ ε if and only if t = Ω̃d (dLeap(h∗ )− ... So the total time complexity is Ω̃d (dLeap(h∗ )∨2 )poly(1/ε) for bounded width/depth networks"

(the displayed exponent is `Leap(h*) - 1 ∨ 1`)

**Proposition 2 (CSQ lower bound), verbatim:**

> "In the setting of Proposition 1, the CSQ complexity of learning f∗ to less than εh∗ error is at least ch∗ dLeap(h∗ ) in the Boolean case, and at least ch∗ dLeap(h∗ )/2 in the Gaussian case."

followed immediately by: "For Gaussian functions, we only prove dLeap(h∗ )/2 scaling. However we conjecture that the same scaling as the Boolean case should hold."

**Theorem 1 / Theorem 2 (first-layer training).** For the single-monomial and nested-monomial (Eq. 11) classes with `sigma` satisfying Assumption 1, with `T^1 = C_0 d^{D-1} log(d)^{C_0}`, `eta_1 = 1/(C_1 kappa d^{D/2} log(d)^{C_1})`, the first-layer weights align with the support: `|w_{j,i}^{T^1} - sign(w_{j,i}^0) · Delta| <= C_5/sqrt(d log(d))` for `i = 1, ..., P`, w.p. `1 - M d^{-C_*}`.

**Nested-monomial class (Eq. 11):** `h*(z) = sum_{l=1}^{L} prod_{s in [P_l]} He_{k_s}(z_s)` with `0 = P_0 < P_1 < ... < P_L = P`, `D_l` the leap at step `l`, `D = max_l D_l`, assuming `min_l D_l >= 2`.

**Examples (Boolean), verbatim:** `Leap(z1 + z1 z2 + z1 z2 z3 + z1 z2 z3 z4 ) = 1`, `Leap(z1 + z2 + z2 z3 z4 ) = 2`, `Leap(z1 z2 z3 + z2 z3 z4 ) = 3`, `Leap(z1 + z1 z2 z3 + z2 z3 z4 z5 z6 z7 ) = 4`.

## Connections

- Concept page: [Leap Complexity](../concepts/leap-complexity.md); also [CSQ Model](../concepts/csq-model.md), [Information Exponent](../concepts/information-exponent.md), [Multi-Index Model](../concepts/multi-index-model.md).
- Generalises [The Merged-Staircase Property](merged-staircase-property.md) (leap 1) and the information exponent of [BGJ21](information-exponent-online-sgd.md) (single-index case).
- Improved on inside SQ by the [generative exponent](generative-exponent-single-index.md) and, in the multi-index setting, by the [generative leap](generative-leap-multi-index.md), whose Proposition 3 gives `k* <= l*` against this paper's information leap.
- **Load-bearing caveat:** [The Benefits of Reusing Batches for GD in Two-Layer Networks](reusing-batches-breaks-exponents.md) explicitly disproves this paper's conjecture that batch reuse reduces a leap-`l` target's complexity only to `O(d^{max(l/2,1)})`, and reduces it to `O(d)` for a broad class. The leap therefore prices *single-pass* GD on the square loss, not the target's intrinsic hardness. Any use of the leap as an adversary's price tag inherits an algorithm-class restriction that a multi-pass adversary steps out of.
- [Robust Multi-Index SQ Bounds](robust-multi-index-sq-bounds.md) describes leap complexity as characterising "the Correlational SQ (CSQ) complexity of learning under certain assumptions" — the same boundary.
- [Noise Sensitivity Exponent](noise-sensitivity-exponent.md) groups the leap with the information exponent as "not a fundamental obstruction to learning".
- Frameworks: [Statistical Query Model](../concepts/statistical-query-model.md), [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md), [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md).
- Authors: [Emmanuel Abbe](../entities/emmanuel-abbe.md), [Enric Boix-Adserà](../entities/enric-boix-adsera.md), [Theodor Misiakiewicz](../entities/theodor-misiakiewicz.md).

## Open Questions / Limitations

- Conjecture 1 is open. Listed future work: remove the layer-wise training and the projection step; extend beyond nested monomials (Eq. 11); extend the leap beyond isotropic input distributions.
- The Gaussian CSQ bound `d^{Leap/2}` versus the conjectured `d^{Leap}`.
- Whether the correspondence to CSQ holds beyond finite `P` — Remark 2 gives a counterexample sketch (`h*(z) = sum i z_i^{g(i)} + prod z_i`) where CSQ needs 0 queries but SGD on a regular network may not succeed.
- Joint training of both layers is "currently out of reach of our proof techniques"; the per-saddle `d^{D_l - 1}` scaling at constant step size is observed empirically but obtained in proof only by varying the step size.

## Quotes / Notable Passages

> "We prove a version of this conjecture for a class of functions on Gaussian isotropic data and 2-layer neural networks, under additional technical assumptions on how SGD is run."

> "the information exponent is a coefficient that only applies at initialization, while the leap-complexity is a measure of targets that controls the entire learning trajectory"

> "However, our current proof techniques do not allow for fully general leap functions"
