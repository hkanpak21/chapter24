---
title: Generative Leap Exponent
type: concept
tags: [low-degree-polynomials, multi-index-model, statistical-computational-gaps, generative-exponent, sample-complexity]
---

## Definition

Damian, Lee and Bruna extend the [generative exponent](generative-exponent.md) to Gaussian multi-index models by conditioning on an *augmented label* that carries the directions already recovered. For a subspace `S ⊆ R^r`, with `ybar_S := (z_S, y)` and `zbar_S := z_{S^perp}`:

`zeta_{k,S} := E[h_k(Zbar_S) | Ybar_S]`, `Lambda_k(S) := E[zeta_{k,S} ⊗ zeta_{k,S}]`, `lambda_k^2(S) := E[|| zeta_{k,S} ||_F^2]`.

[Definition 2](../sources/generative-leap-multi-index.md), verbatim: "k(S) is the smallest k ≥ 1 such that λ2k (S) > 0."

The **leap decomposition** is the flag `∅ = S_0 ⊊ S_1 ⊊ ... ⊊ S_L = R^r` built inductively by `k_{i+1} := k(S_i)` and `S_{i+1} := S_i ∪ span[Lambda_{k_{i+1}}(S_i)]`.

[Definition 3](../sources/generative-leap-multi-index.md), verbatim: "Let ki , i = 1, . . . , L be defined as above. The generative leap exponent is defined as k ⋆ := maxi ki ."

Proposition 1 gives the variational form `k* = inf_{F = {∅=R_0 ⊂ ... ⊂ R_r}} max_j k(R_j, R_{j+1})`, termination in `L <= r` steps, and rotation invariance.

## Intuition

Multi-index estimation is sequential: SGD and spectral methods recover directions in stages, at different timescales. The generative leap asks, at each stage, "given everything found so far, what is the lowest Hermite order that reveals a new direction, after the best possible transformation of the (augmented) label?" — and reports the worst stage. It is simultaneously the multi-index generalisation of the generative exponent and the label-transformation-closed version of the [information leap](leap-complexity.md).

## Properties / Theorems

- **Subspace-relative variational characterisation** ([Proposition 2](../sources/generative-leap-multi-index.md), verbatim): "For any subspace S, we have k(S)[P] = inf T ..." (Eq. 4, i.e. the infimum of `l(S)[(Id_z ⊗ T_y)_# P]` over `T in L^2(P_{ybar_S})`), and then "In particular we have k(S) ≤ l(S) for any subspace S." — the exact analogue of DPLB24's Proposition 2.6.
- **Dominates the information leap** ([Proposition 3](../sources/generative-leap-multi-index.md), verbatim): "We have k ⋆ ≤ l⋆ ." where `l*` is the information leap exponent of Abbe–Boix-Adserà–Misiakiewicz (their Definition 5).
- **Low-degree lower bound** (Theorem 1): with `D = O(log(d)^2)` and `n = O(d^{k*/2 - gamma})` for any `gamma > 0`, `||R^{<=D}||_{L^2(H_0)} = 1 + o_d(1)` — no degree-`D` polynomial test weakly separates. **This is a low-degree bound, not an SQ bound.** DLB25 is explicit that translating to SQ is not automatic in the multi-index setting, "stemming from the inherent inability to perform certain spectral tasks in SQ".
- **Matching efficient upper bound** (Theorem 3): a Hermite-kernel matrix U-statistic with subspace conditioning recovers the index space with `n >= C(P,K)[d^{k*/2}/eps + d/eps^2]`, without prior knowledge of `P`. The U-statistic (summing over disjoint pairs `i != j`) rather than `Phi Phi^T` is what reaches `d^{k/2}` instead of `d^{(2k-1)/3}`.
- **The constant is not controlled.** Section 4.2 exhibits a model where the first leap is cheap but identifying the correct rotation for the next leap "is a hard algorithmic problem requiring exp(r) samples", and conjectures the true complexity is at least `d exp(r)`. `C(P)` can therefore be exponentially large in `r`.
- **Computed values** (Proposition 4): `r`-Gaussian parity `k* = l* = r`; staircase parities `k* <= l* = 1`; intersections of halfspaces `k* <= 2`; polynomials `k* <= 2`.
- **Deep nets are cheap.** Proposition 5: continuous piecewise-linear `sigma` gives `k* <= 2`. Corollary 2: for `y = sigma((W*)^T x)` with `sigma` an arbitrarily deep ReLU network *with biases*, fixed independent of `d`, and an `r`-dimensional first hidden layer, `n >= C(sigma) d/eps^2` recovers `span[W*]`. Proposition 6(i): under generic linear input transformations `Theta`, `k*(P_Theta) <= 2` outside a Lebesgue-null set. Hence "models with large generative leap are brittle".
- Proposition 7 / Corollary 3: for orthogonal shallow nets `y = sum_j a_j rho(z_j)`, `k* >= k*(rho)`, with equality under moment conditions, and `k*_V <= k*(rho)` for almost every unit-norm `V`.

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

- [The Generative Leap: Sharp Sample Complexity for Efficiently Learning Gaussian Multi-Index Models](../sources/generative-leap-multi-index.md) — origin.
- [Computational-Statistical Gaps in Gaussian Single-Index Models](../sources/generative-exponent-single-index.md) — the `r = 1` case.
- [SGD Learning on Neural Networks: Leap Complexity](../sources/leap-complexity-sgd.md) — the information leap it dominates.
- [Algorithms and SQ Lower Bounds for Robustly Learning Real-valued Multi-index Models](../sources/robust-multi-index-sq-bounds.md) — concurrent work whose `m` matches `k*` in the single-index case; their algorithm costs `d^{O(k*)}` but they characterise the hidden constant and target agnostic PAC learning.
- [The Benefits of Reusing Batches](../sources/reusing-batches-breaks-exponents.md) — cited by DLB25 for reused-sample SGD reaching the generative exponent; also the reason no exponent in this family should be read as intrinsic hardness.

## Related Concepts

- [Generative Exponent](generative-exponent.md), [Leap Complexity](leap-complexity.md), [Information Exponent](information-exponent.md), [Noise Sensitivity Exponent](noise-sensitivity-exponent.md)
- [Multi-Index Model](multi-index-model.md), [Single-Index Model](single-index-model.md), [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md), [Statistical Query Model](statistical-query-model.md), [CSQ Model](csq-model.md), [Statistical-Computational Gaps](statistical-computational-gaps.md)

## Open Questions

- The `r`- and `eps`-dependence of `C(P,K)`; the conjectured `d exp(r)` lower bound.
- The SQ complexity of multi-index recovery, as opposed to the low-degree complexity proved here.
- Extension beyond isotropic Gaussian data.
- Whether the zero-measure exclusions in Proposition 6 are necessary for general link functions.
- No adversary is priced in these units anywhere in this corpus.
