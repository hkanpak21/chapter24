---
title: Single-Index Model
type: concept
tags: [learning-theory, single-index-model, sample-complexity, statistical-computational-gaps]
---

## Definition

A single-index model (SIM) is a supervised model in which the label depends on the input only through a single one-dimensional projection. Two versions appear in this wiki and they are not the same object.

**Deterministic / known link** ([WZDD24](../sources/robust-single-index-efficient.md)): `f(x) = sigma(w · x)` with `sigma : R -> R` a known link function and `w` a hidden unit vector.

**Distributional** ([DPLB24 Definition 1.1](../sources/generative-exponent-single-index.md)), verbatim:

> "We say that a joint distribution P ∈ P(Rd × R) follows a Gaussian single index model if there exists a probability measure P ∈ G ⊂ P(R2 ) and w⋆ ∈ S d−1 such that P = [Rw⋆ ⊗ Id]# [γd−1 ⊗ P]"

with `G = {nu in P(R x R) : nu_z = gamma_1, E[Y^2] < infinity, D_{chi^2}(nu || gamma_1 ⊗ nu_y) > 0}`. This version admits label noise as part of the model — additive, multiplicative, mixture-of-distributions, Massart — rather than as a perturbation.

The `K = 1` case of [DIKR25 Definition 1.1](../sources/robust-multi-index-sq-bounds.md) is the same object in a PAC-learning framing: "The special case of K = 1 corresponds to Single-Index Models (SIMs)."

## Intuition

The simplest model with planted low-dimensional structure and a non-linearity. It is the standard test-bed for computational-versus-statistical questions in learning because the statistical cost is always `Theta(d)` while the computational cost varies over a whole polynomial range depending on the link. Instances include linear regression, phase retrieval (`sigma(u) = |u|` or `u^2`), one-bit compressed sensing, generalized linear models, and — in the periodic case — the cryptographically hard cosine neuron of [SZB21](../sources/hardness-single-periodic-neurons.md).

## Properties / Theorems

- **Statistical cost is linear.** Brute force recovers `w*` to accuracy `eps` with `n = Theta(d/eps^2)` ([DPLB24 Theorem 6.1](../sources/generative-exponent-single-index.md)).
- **Computational cost depends on the link**, and on which algorithm class you price:
  - online SGD, square loss: `d^{max(1,l*-1)}` ([BGJ21](../sources/information-exponent-online-sgd.md));
  - CSQ: `d^{max(1,l*/2)}`, achieved by loss smoothing and (agnostically) by [WZDD24](../sources/robust-single-index-efficient.md);
  - SQ and low-degree: `d^{max(1,k*/2)}` with `k* <= l*` ([DPLB24](../sources/generative-exponent-single-index.md));
  - multi-pass GD with batch reuse, proportional regime: `O(d)` for all non-(orthogonally-)even-symmetric targets ([DTA+24](../sources/reusing-batches-breaks-exponents.md));
  - AMP at low SNR: `alpha = Theta(lambda^{-beta_*})` ([DKLM26](../sources/noise-sensitivity-exponent.md)).
- **Monotone links are easy**: Isotron / GLM-tron recover with `n = Theta(d)`.
- **Periodic links are cryptographically hard** under polynomially small noise: [SZB21](../sources/hardness-single-periodic-neurons.md), via [Continuous LWE](continuous-lwe.md), and this is the seed of the one-hidden-layer ReLU hardness of [LZZ24](../sources/hardness-one-hidden-layer.md).
- **Noise is what makes it hard.** In the noise-free case, lattice methods (LLL) reach the information-theoretic threshold for phase retrieval and for the cosine neuron with `d + 1` samples.

## Where It Appears

- [Online SGD on Non-Convex Losses from High-Dimensional Inference](../sources/information-exponent-online-sgd.md)
- [Computational-Statistical Gaps in Gaussian Single-Index Models](../sources/generative-exponent-single-index.md)
- [Sample and Computationally Efficient Robust Learning of Gaussian Single-Index Models](../sources/robust-single-index-efficient.md)
- [The Benefits of Reusing Batches for GD in Two-Layer Networks](../sources/reusing-batches-breaks-exponents.md)
- [A Noise Sensitivity Exponent](../sources/noise-sensitivity-exponent.md)
- [On the Cryptographic Hardness of Learning Single Periodic Neurons](../sources/hardness-single-periodic-neurons.md)
- [Algorithms and SQ Lower Bounds for Robustly Learning Real-valued Multi-index Models](../sources/robust-multi-index-sq-bounds.md) (the `K = 1` case)

## Related Concepts

- [Multi-Index Model](multi-index-model.md), [Information Exponent](information-exponent.md), [Generative Exponent](generative-exponent.md), [Noise Sensitivity Exponent](noise-sensitivity-exponent.md)
- [Statistical Query Model](statistical-query-model.md), [CSQ Model](csq-model.md), [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md), [Continuous LWE](continuous-lwe.md), [Statistical-Computational Gaps](statistical-computational-gaps.md)

## Open Questions

- **A single-index result is not a neural-network result.** Every paper in this corpus that reports a single-index threshold is reporting a threshold for a planted one-dimensional structure under isotropic Gaussian covariates. The network connection is either by approximation (SZB21 Appendix E), by explicit construction (LZZ24 Lemma 5.1), or by treating the network as the link function (DLB25 Section 5) — never automatic.
- Whether the adversary in any of the "robust"/agnostic single-index results can be given a resource budget rather than a corruption budget. It has not been done.
