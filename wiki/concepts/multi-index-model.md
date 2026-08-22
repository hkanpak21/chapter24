---
title: Multi-Index Model
type: concept
tags: [learning-theory, multi-index-model, sample-complexity, statistical-computational-gaps, feature-learning]
---

## Definition

A multi-index model (MIM) is a function or conditional law depending on the input only through its projection onto a low-dimensional subspace.

Functional form, [DIKR25 Definition 1.1](../sources/robust-multi-index-sq-bounds.md), verbatim:

> "A function f : Rd → R is a K-MIM if there exists a K-dimensional subspace W ⊆ Rd such that f (x) = f (xW ) for all x ∈ Rd , where xW is the projection of x onto W ."

Distributional form, [DLB25 Definition 1](../sources/generative-leap-multi-index.md), verbatim:

> "We say that (X, Y ) follows a Gaussian multi-index model with index r if X ∼ N (0, Id ) := γd and there exists a subspace U ⋆ ∈ G(r, d) such that the conditional law P[Y |X] only depends on the orthogonal projection PU ⋆ X."

[ABM22](../sources/merged-staircase-property.md) and [ABM23](../sources/leap-complexity-sgd.md) use a coordinate/latent version `f*(x) = h*(Mx)` with `P = O_d(1)` latent dimensions, over the uniform hypercube or isotropic Gaussian.

## Intuition

The canonical abstraction for *feature learning*: the index space is exactly the representation a network's first layer would have to find. Standard instances are Gaussian parities, staircase functions, intersections of halfspaces, polynomials, and low-rank shallow or deep networks `y = a^T rho(V^T z)`.

The phenomenon that distinguishes `r > 1` from `r = 1` is **sequentiality**. Directions are recovered in stages (saddle-to-saddle), each stage conditioned on the previous, at different timescales. Every unit in this family — the [merged-staircase property](../sources/merged-staircase-property.md), the [leap](leap-complexity.md), the [generative leap](generative-leap-exponent.md), and DIKR25's subspace-conditioned moment condition — is some formalisation of "what is the worst single stage?".

## Properties / Theorems

- **Statistical cost is linear**: `O(d eps^{-2})` by brute force over an `eps`-net of the Stiefel manifold.
- **Computational cost by algorithm class**:
  - one-pass mean-field SGD, hypercube, `O(d)` samples: learnable iff MSP (leap 1), [ABM22](../sources/merged-staircase-property.md);
  - online SGD on a 2-layer net: `Theta~(d^{max(Leap,2)})` — **conjectured**, [ABM23](../sources/leap-complexity-sgd.md);
  - CSQ: `d^{Leap}` (Boolean) / `d^{Leap/2}` (Gaussian), proved, [ABM23](../sources/leap-complexity-sgd.md);
  - low-degree: `d^{k*/2}` with `k*` the generative leap, matched by an efficient spectral U-statistic, [DLB25](../sources/generative-leap-multi-index.md);
  - SQ, agnostic PAC: `d^{O(m)} 2^{poly(K/eps)}` upper and `d^{Omega(m)}` lower, [DIKR25](../sources/robust-multi-index-sq-bounds.md);
  - multi-pass GD with batch reuse: `O(d)` in `T = 2` steps for all directions outside the (orthogonally-)even-symmetric subspace, [DTA+24](../sources/reusing-batches-breaks-exponents.md);
  - AMP, proportional regime: specialization at `Theta_p(p^{beta_*})`, [DKLM26](../sources/noise-sensitivity-exponent.md).
- **The `r`-dependence is the open frontier.** DLB25's constant `C(P,K)` may be `exp(r)`; DIKR25's `2^{poly(K/eps)}` is exponential in `K`.
- **Neural networks enter only through the link.** Deep ReLU networks with biases and an `r`-dimensional first hidden layer have generative leap `k* <= 2` (DLB25 Prop. 5 / Cor. 2); homogeneous Lipschitz ReLU networks with first-layer rank `<= K` are PAC-learnable with complexity independent of network size (DIKR25 Cor. 1.7). Neither is a statement about *training* a network.

## Where It Appears

- [The Merged-Staircase Property](../sources/merged-staircase-property.md), [SGD Learning on Neural Networks: Leap Complexity](../sources/leap-complexity-sgd.md)
- [The Generative Leap](../sources/generative-leap-multi-index.md)
- [Algorithms and SQ Lower Bounds for Robustly Learning Real-valued Multi-index Models](../sources/robust-multi-index-sq-bounds.md)
- [The Benefits of Reusing Batches for GD in Two-Layer Networks](../sources/reusing-batches-breaks-exponents.md)
- [A Noise Sensitivity Exponent](../sources/noise-sensitivity-exponent.md)

## Related Concepts

- [Single-Index Model](single-index-model.md), [Leap Complexity](leap-complexity.md), [Generative Leap Exponent](generative-leap-exponent.md), [Generative Exponent](generative-exponent.md), [Information Exponent](information-exponent.md), [Noise Sensitivity Exponent](noise-sensitivity-exponent.md)
- [Statistical Query Model](statistical-query-model.md), [CSQ Model](csq-model.md), [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md), [Statistical-Computational Gaps](statistical-computational-gaps.md)

## Open Questions

- Sharp `r`-dependence; whether `d exp(r)` is the truth for DLB25's Section 4.2 example.
- The SQ complexity of multi-index subspace recovery (only the low-degree side is settled).
- Extension of every unit beyond isotropic Gaussian / uniform hypercube data.
- No result in this family prices an adversary; the corruptions in the agnostic results are budgets on effect, not on resources.
