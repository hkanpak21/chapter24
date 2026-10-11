---
title: Generative Exponent
type: concept
tags: [statistical-query, low-degree-polynomials, single-index-model, statistical-computational-gaps, generative-exponent, sample-complexity]
---

## Definition

For a Gaussian single-index model with `(Z, Y) ~ P`, `Z = w* · X`, Damian–Pillaud-Vivien–Lee–Bruna expand the `chi^2`-mutual information `I_{chi^2}[P] = D_{chi^2}[P || P_z ⊗ P_y] = sum_k lambda_k^2` and take the first non-zero term. Verbatim, [Definition 2.4](../sources/generative-exponent-single-index.md):

> "The generative exponent of P ∈ G is defined by: k ⋆ (P) := min{k ≥ 1; λk ̸= 0} where λk := ∥ζk ∥Py and ζk := EP [hk (Z)|Y ]."

`zeta_k(y) = E[h_k(Z) | Y = y]` is the `k`-th Hermite moment of the *inverse* ("generative") regression of `Z` given `Y` — hence the name.

## Intuition

The [information exponent](information-exponent.md) `l*` is built from `beta_l = E[Y h_l(Z)]`, i.e. from the correlation of the *raw label* with Hermite polynomials — a correlational quantity, which is why it prices CSQ. The generative exponent replaces `Y` by *the best possible function of* `Y`. Since `beta_k = <y, zeta_k>_{P_y}`, `lambda_k = 0` forces `beta_k = 0`, so `k* <= l*` always.

### The exact condition under which `k*` and `l*` differ

Proposition 2.6, verbatim:

> "The generative exponent k ⋆ (P) can be written as: k ⋆ (P) = inf T ∈L2 (Py ) l⋆ ((Id ⊗ T )# P)"

So `k*(P) < l*(P)` **iff there exists a square-integrable label transformation `T in L^2(P_y)` such that the transformed model `(Id ⊗ T)_# P` has a strictly smaller first non-vanishing Hermite index** — i.e. iff some label pre-processing lowers the Hermite index. Equivalently, `k*` is the smallest `k` such that some measurable `T` and some mean-zero degree-`k` polynomial `Q` give `E_P[T(Y) Q(Z)] != 0`; `l*` is the same statement with `T` forced to be the identity. Nothing weaker is true: "supersedes" without this condition is wrong, because for many models the two coincide.

The special case `k* <= 2` has a closed-form criterion, inherited from Mondelli–Montanari / Barbier et al. and quoted by DPLB24 as Eq. (3): `E[ E[Z^2 - 1 | Y]^2 ] != 0`.

Two directions are closed off. Post-processing can never *raise* `k*` — "no post-processing of Y , either random or deterministic, can reduce the generative exponent" — and Corollary 2.8 gives invariance under bijective relabelling: `k*(sigma) = k*(phi ∘ sigma)` for `phi, phi^{-1} in L^2(P_y)`.

### Large `k*` is not generic

Example 2.7 (i), verbatim:

> "For σ a polynomial, we have k ⋆ (σ) ≤ 2 and k ⋆ (σ) = 2 iff σ is even. In particular, k ⋆ (hj ) = 1 if j is odd and k ⋆ (hj ) = 2 if j is even."

So every instance with `k* > 2` is a fine-tuned, non-polynomial construction. DPLB24 build smooth `sigma` with any prescribed `k*` (Theorems 5.1, 5.2) precisely because such examples are not naturally occurring. [DLB25](../sources/generative-leap-multi-index.md) reaches the same conclusion for the multi-index version — "models with large generative leap are brittle" — and [DKLM26](../sources/noise-sensitivity-exponent.md) makes the brittleness argument the premise of its own alternative unit.

## Properties / Theorems

- `k*(P) <= l*(P)`, with equality unless some label transformation lowers the Hermite index (Prop. 2.6).
- **SQ lower bound** (Theorem 3.2): any algorithm using `q = d^r` queries to `VSTAT(n)` and returning `w_hat` with `|w_hat · w*| >= omega~(d^{-1/2})` requires `n >= (c_{k*}/lambda_{k*}^2)(d/r^2)^{k*/2}`. No polylog factors.
- **Low-degree lower bound** at the same threshold (Theorem 3.5), conditional on the low-degree conjecture (Conjecture 3.4).
- **Matching efficient upper bound**: `n ≳ d^{max(1,k*/2)}` via the label transformation `T = zeta_{k*}` and a partial-trace estimator (Theorem 4.1), extended to unknown `P` and `k*` (Corollary 4.4).
- Information-theoretic upper bound `n = Theta~(d/(lambda_k^2 eps^2))` (Theorem 6.1), so the gap is real exactly when `k* > 2`.
- Remark 3.3: the SQ bound is a *detection* threshold; a detection/estimation gap in SQ is not ruled out (but would be an SQ artefact, since Algorithm 1 estimates at `d^{k*/2}`).
- For `K = 1`, the parameter `m` of [DIKR25](../sources/robust-multi-index-sq-bounds.md) is a *modification* of `k*` (their Appendix C.3), necessary because they characterise agnostic PAC learning rather than parameter recovery.

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

- [Computational-Statistical Gaps in Gaussian Single-Index Models](../sources/generative-exponent-single-index.md) — origin.
- [The Generative Leap](../sources/generative-leap-multi-index.md) — multi-index generalisation.
- [Algorithms and SQ Lower Bounds for Robustly Learning Real-valued Multi-index Models](../sources/robust-multi-index-sq-bounds.md) — their `m` plays the same role for agnostic PAC learning.
- [A Noise Sensitivity Exponent](../sources/noise-sensitivity-exponent.md) — restated as Eq. (9) `GE(g) = inf_T IE(T ◦ g)`, and criticised as brittle; `beta_* = infinity` iff `GE > 2`.
- [The Benefits of Reusing Batches](../sources/reusing-batches-breaks-exponents.md) — multi-pass GD performs the label transformations implicitly.
- [Sample and Computationally Efficient Robust Learning of Gaussian Single-Index Models](../sources/robust-single-index-efficient.md) — explicitly notes that the generative-exponent algorithm fails under adversarial label noise.

## Related Concepts

- [Information Exponent](information-exponent.md), [Generative Leap Exponent](generative-leap-exponent.md), [Leap Complexity](leap-complexity.md), [Noise Sensitivity Exponent](noise-sensitivity-exponent.md)
- [Single-Index Model](single-index-model.md), [CSQ Model](csq-model.md), [Statistical Query Model](statistical-query-model.md), [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md), [Statistical-Computational Gaps](statistical-computational-gaps.md)

## Open Questions

- Whether an SQ detection/estimation gap exists for single-index models (DPLB24 Remark 3.3).
- Whether `m = k*` extends beyond `K = 1` in the agnostic PAC setting (conjectured by DLB25).
- Whether any *adversary* has been priced in generative-exponent units. None found in this corpus: the exponent is a learner's price tag throughout.
