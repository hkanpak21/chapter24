---
title: Learning With Errors (LWE)
type: concept
tags: [lattice-cryptography, learning-with-errors, hardness-reductions, cryptography, statistical-query]
---

## Definition

**Learning With Errors (LWE)** [Regev 2005] is a foundational problem in lattice cryptography. For parameters (n, q, α) with q prime and α ∈ (0,1):
- Secret: s ∈ Z_q^n uniformly random.
- Sample: (a_i, b_i) with a_i ~ Uniform(Z_q^n) and b_i = ⟨a_i, s⟩ + e_i mod q, where e_i ~ discrete Gaussian of width αq.
- **Search LWE**: recover s from poly-many samples.
- **Decision LWE**: distinguish these samples from uniform (a_i, b_i).

## Intuition

LWE is "noisy linear equations over Z_q". Without noise, Gaussian elimination solves it trivially. With noise above a threshold, the problem becomes tied to worst-case lattice problems (GapSVP, SIVP), providing a foundation for post-quantum cryptography (Kyber, Dilithium, FHE schemes).

## Properties / Theorems

- **Regev's theorem (2005)**: quantum polynomial-time reduction from worst-case lattice problems (GapSVP, SIVP with approximation factor Õ(n/α)) to LWE. Foundation of lattice cryptography.
- **Classical reduction** [Peikert 2009, BLP+13]: partial classical reduction.
- **Continuous analogue**: [Continuous LWE](continuous-lwe.md) [Bruna-Regev-Song-Tang 2021] has similar hardness.
- **SQ lower bounds**: LWE is SQ-hard in the natural formulation.
- **Cryptographic primitives based on LWE**: PKE, signatures, FHE, ABE, iO.

## Where It Appears

- [Bruna Continuous LWE](../sources/bruna-continuous-lwe.md) — continuous analogue
- [Planting Undetectable Backdoors](../sources/planting-undetectable-backdoors.md) — uses LWE for white-box undetectability

## Related Concepts

- [Continuous LWE](continuous-lwe.md)
- [Statistical Query Model](statistical-query-model.md)

## Open Questions

- Classical (non-quantum) reduction from lattice problems to LWE in full generality.
- Sub-exponential LWE algorithms.
- Post-quantum assumptions independent of LWE.
