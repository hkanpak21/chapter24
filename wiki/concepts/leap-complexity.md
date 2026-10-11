---
title: Leap Complexity
type: concept
tags: [learning-theory, sample-complexity, csq, multi-index-model, leap-complexity, feature-learning]
---

## Definition

Abbe, Boix-Adserà and Misiakiewicz define the leap of a low-latent-dimension target from the support of its Fourier-Walsh (Boolean) or Hermite (Gaussian) expansion. Verbatim, [Definition 1](../sources/leap-complexity-sgd.md):

> "Let h∗ be as before with non-zero basis elements given by the subset S(h∗ ) := {S1 , . . . , Sm }, m ∈ Z+ . We define the leap complexity of h∗ as"

followed by the display `Leap(h∗ ) := min_{π∈Π_m} max_{i∈[m]} || S_{π(i)} \ ∪_{j=0}^{i−1} S_{π(j)} ||_1`,

where `|| S_{pi(i)} \ ∪_{j<i} S_{pi(j)} ||_1 = sum_{k in [P]} S_{pi(i)}(k) 1{S_{pi(j)}(k) = 0 ∀ j < i}` — new coordinates counted **with Hermite multiplicity** in the Gaussian case, and as a plain set difference in the Boolean case.

The `Leap = 1` case on the hypercube is exactly the **merged-staircase property (MSP)** of [ABM22](../sources/merged-staircase-property.md), Definition 1: "S = {S1 , . . . , Sm } ⊆ 2[P ] is a Merged-Staircase Property (MSP) set structure if the sets can be ordered so that for each i ∈ [m], |Si \ ∪i′ <i Si′ | ≤ 1."

## Intuition

Order the monomials so that each one is as easy as possible to reach from the ones already learned. The leap is the largest single jump you are forced to make. SGD on a regular network then moves saddle-to-saddle: it plateaus while trying to align `L` new coordinates at once, which costs `Theta~(d^{L-1})` steps, then drops the loss and moves on. Inserting an intermediate monomial lowers the leap and therefore the cost — the paper's "curriculum learning" reading: `z_1 ... z_{2k}` alone is a leap-`2k` target costing `Theta~(d^{2k-1})`, but `z_1 ... z_k + z_1 ... z_{2k}` costs `Theta~(d^{k-1})`.

Examples, verbatim from ABM23: `Leap(z1 + z1 z2 + z1 z2 z3 + z1 z2 z3 z4 ) = 1`, `Leap(z1 + z2 + z2 z3 z4 ) = 2`, `Leap(z1 z2 z3 + z2 z3 z4 ) = 3`, `Leap(z1 + z1 z2 z3 + z2 z3 z4 z5 z6 z7 ) = 4`; and on Gaussian data `Leap(He_k(z_1)) = k`, `Leap(He_2(z_1) + He_2(z_2) + He_2(z_3) + He_3(z_1) He_8(z_3)) = 2`.

## Properties / Theorems

Three guards, all essential.

1. **`Theta~(d^{max(Leap,2)})` is a conjecture, not a theorem.** [ABM23 Conjecture 1](../sources/leap-complexity-sgd.md), verbatim: "the risk is bounded by" ... "So the total time complexity is Ω̃d (dLeap(h∗ )∨2 )poly(1/ε) for bounded width/depth networks". It holds "for all but a measure-0 set of functions". The step count is `t = Omega~_d(d^{Leap(h*) - 1 ∨ 1}) poly(1/eps)`.

2. **What is proved is a specialisation.** 2-layer network, smooth activations satisfying Assumption 1, *layer-wise* SGD with an entrywise `l_infinity` projection step (which makes the algorithm non-rotationally-equivariant, forcing `z` to be a coordinate subset rather than a general subspace), isotropic Gaussian data, and the nested-monomial subclass of Eq. (11) with `min_l D_l >= 2`; the risk bound (Corollary 2) covers only the multilinear subclass Eq. (12), for *some* activation.

3. **The matching lower bound is CSQ only.** [Proposition 2](../sources/leap-complexity-sgd.md), verbatim: "the CSQ complexity of learning f∗ to less than εh∗ error is at least ch∗ dLeap(h∗ ) in the Boolean case, and at least ch∗ dLeap(h∗ )/2 in the Gaussian case." CSQ is strictly weaker than SQ — general SQ queries `E[phi(x,y)]` permit label pre-processing — and that is exactly why the [generative exponent](generative-exponent.md) later improves on the leap.

Further:

- MSP is *necessary* and *nearly sufficient* (almost surely over the coefficients) for strong `O(d)`-SGD-learnability in the depth-2 mean-field regime; degenerate symmetric MSP counterexamples exist ([ABM22](../sources/merged-staircase-property.md) Theorems 7, 9, and Section 4). MSP is a **binary property**, not a graded cost.
- Remark 2 of ABM23: the CSQ correspondence "may not hold beyond the finite P regime".
- [DIKR25](../sources/robust-multi-index-sq-bounds.md) summarises the leap as a notion that "essentially characterize[s] the Correlational SQ (CSQ) complexity of learning under certain assumptions".
- The **information leap** exponent `l*` (Abbe–Boix-Adserà–Misiakiewicz, restated as [DLB25](../sources/generative-leap-multi-index.md) Definition 5 via `zeta~_{k,S} = E[Y h_k(Zbar_S) | Z_S]`) is the object that the [generative leap exponent](generative-leap-exponent.md) dominates: `k* <= l*` (their Proposition 3).
- **Broken by batch reuse.** [DTA+24](../sources/reusing-batches-breaks-exponents.md) explicitly disproves ABM23's conjecture that reuse could only reduce a leap-`l` target's complexity to `O(d^{max(l/2,1)})` — verbatim, "We disprove this conjecture and show that the sample complexity for a large class of functions can be reduced to O(d) independently of the leap exponent ℓ."

## Comparison table of the candidate units

| Unit | Introduced in | Model class | **Algorithm class priced** | Threshold | Exact relation to the others |
|---|---|---|---|---|---|
| **Information exponent** `l*` (written `k` in BGJ21, `k*` in WZDD24) | [BGJ21](../sources/information-exponent-online-sgd.md) | rank-one estimation on the sphere; Gaussian single-index | **online (single-pass) SGD**, square loss, uniform random start | `M ≍ N^{l*-1}` polylog for `l* >= 3`; `N log N` for `l* = 2`; `N` for `l* = 1`. Lowered to `d^{max(1,l*/2)}` inside CSQ by loss smoothing | upper bound for everything below: `k* <= l*` |
| **Merged-staircase property (MSP)** | [ABM22](../sources/merged-staircase-property.md) | **hypercube** `{+1,-1}^d`, depth-2 mean-field, `P` fixed | one-pass batch-SGD in the mean-field regime | **binary**: strongly `O(d)`-SGD-learnable or not | exactly `Leap = 1` |
| **Leap complexity** `Leap` | [ABM23](../sources/leap-complexity-sgd.md) | low-latent-dimension targets, isotropic Gaussian or hypercube, `P = O_d(1)` | online SGD on a 2-layer net (**conjecture**); the matching lower bound is **CSQ only** | `Theta~(d^{max(Leap,2)})` total time — **stated as Conjecture 1**. Proved: a specialisation, plus CSQ bounds `d^{Leap}` (Boolean) / `d^{Leap/2}` (Gaussian) | reduces to `l*` for single-index; generalises MSP |
| **Generative exponent** `k*` | [DPLB24](../sources/generative-exponent-single-index.md) | Gaussian **single**-index (their Definition 1.1) | **SQ** and **low-degree** | `n = Theta(d^{max(1,k*/2)})`, matching upper and lower bounds | `k* = inf_{T in L^2(P_y)} l*((Id ⊗ T)_# P) <= l*`; **strict iff some square-integrable label transformation lowers the first non-vanishing Hermite index** |
| **Generative leap exponent** `k*` | [DLB25](../sources/generative-leap-multi-index.md) | Gaussian **multi**-index, `r = O_d(1)` | **low-degree** lower bound + an efficient spectral U-statistic upper bound. Explicitly **not SQ** | `n = Theta(d^{1 ∨ k*/2})`, with an unquantified constant `C(P,K)` conjectured to be `exp(r)` | `k* <= l*` against the information leap (their Prop. 3); reduces to DPLB24's `k*` at `r = 1` |
| **Noise sensitivity exponent** `beta_*` | [DKLM26](../sources/noise-sensitivity-exponent.md) | Gaussian single-/multi-index, **even** `sigma` | **AMP / first-order iterative**, in the **proportional** regime `n = alpha d` | `alpha^{Alg} = Theta(lambda^{-beta_*})` vs `alpha^{IT} = Theta(lambda^{-1})` | `beta_* = 1` iff `l* = 2`; `beta_* = infinity` iff `k* > 2`. **Different regime — does not compose with the `d^k` exponents above** |

**Two facts that must travel with the table.**

1. **CSQ is not SQ.** ABM23's matching lower bound is CSQ (correlational queries `E[y phi(x)]`, i.e. `T = id`). The generative exponent improves on it precisely because general SQ queries `E[phi(x,y)]` permit label pre-processing. Reading a CSQ bound as an SQ bound erases the whole `l*`-to-`k*` gap.

2. **These are not intrinsic hardness measures.** [DTA+24](../sources/reusing-batches-breaks-exponents.md) proves that multi-pass gradient descent with **batch reuse** escapes both the information-exponent and the leap barrier, learning a broad class in `T = 2` steps with `n = O(d)`, independently of the leap — disproving ABM23's own conjecture that reuse could only reach `O(d^{max(l/2,1)})`. In their words: CSQ lower bounds, the staircase property, and the information exponent "are limited to online-SGD on Gaussian/Boolean data, and do not describe the class of functions inherently easy or hard to learn by gradient-based methods." Any use of one of these exponents as a *price tag on an adversary* inherits an algorithm-class restriction that a smarter adversary simply steps out of.

## Where It Appears

- [SGD Learning on Neural Networks: Leap Complexity and Saddle-to-Saddle Dynamics](../sources/leap-complexity-sgd.md) — origin of the graded leap.
- [The Merged-Staircase Property](../sources/merged-staircase-property.md) — the leap-1 case, hypercube, binary.
- [The Generative Leap](../sources/generative-leap-multi-index.md) — the SQ/low-degree-side improvement, with `k* <= l*`.
- [The Benefits of Reusing Batches](../sources/reusing-batches-breaks-exponents.md) — the refutation of the leap as a learnability boundary.
- [A Noise Sensitivity Exponent](../sources/noise-sensitivity-exponent.md) — groups the leap with the information exponent as "not a fundamental obstruction to learning".
- [Algorithms and SQ Lower Bounds for Robustly Learning Real-valued Multi-index Models](../sources/robust-multi-index-sq-bounds.md) — places the leap in CSQ.

## Related Concepts

- [Information Exponent](information-exponent.md), [Generative Exponent](generative-exponent.md), [Generative Leap Exponent](generative-leap-exponent.md), [Noise Sensitivity Exponent](noise-sensitivity-exponent.md)
- [CSQ Model](csq-model.md), [Statistical Query Model](statistical-query-model.md), [Multi-Index Model](multi-index-model.md), [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md), [Statistical-Computational Gaps](statistical-computational-gaps.md)

## Open Questions

- Conjecture 1 itself, and its extension beyond nested-monomial targets and beyond layer-wise projected SGD.
- The Gaussian CSQ gap: `d^{Leap/2}` proved, `d^{Leap}` conjectured.
- Whether the CSQ correspondence survives `P >> 1`.
- Whether the leap can price an *adversary* rather than a learner. Nothing in this corpus does so.
