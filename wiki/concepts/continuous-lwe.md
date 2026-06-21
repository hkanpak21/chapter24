---
title: Continuous LWE (CLWE)
type: concept
tags: [continuous-lwe, lattice-cryptography, learning-with-errors, gaussian-mixtures, statistical-query, hardness-reductions]
---

## Definition

**Continuous LWE (CLWE)** [Bruna-Regev-Song-Tang 2021] is a continuous analogue of the Learning With Errors problem. An instance has parameters (β, γ), dimension n, a hidden unit vector w ∈ R^n, and samples (y_i, z_i) where:
- y_i ~ N(0, I_n) (standard Gaussian)
- z_i = γ⟨y_i, w⟩ + ν_i mod 1, with ν_i ~ N(0, β²)

The **search CLWE** problem asks to recover w given polynomially many samples; **decision CLWE** asks to distinguish these samples from uniform (y_i, z_i) with z_i ~ Uniform[0,1].

**Homogeneous CLWE (hCLWE)** is obtained by conditioning on z_i ≈ 0: the distribution of y_i becomes a mixture of Gaussian "pancakes" of width ≈ β/γ, separated by distance ≈ 1/γ along direction w.

## Intuition

CLWE replaces LWE's discrete Z_q structure with continuous R. The parameter γ plays the role of 1/α in LWE (inverse relative noise), and β plays the role of absolute noise. The density of Gaussian layers along w (determined by γ) controls problem difficulty: γ large → many closely-spaced layers → hard; γ small → well-separated → easy.

CLWE provides a clean continuous-geometric framework that exposes the "hidden-direction-in-Gaussian-data" structure common to LWE, Gaussian mixture learning, and adversarially-robust classification obstacles.

## Properties / Theorems

- **CLWE hardness theorem** [Bruna-Regev-Song-Tang 2021, Theorem 1.1]: For γ ≥ 2√n, β polynomially small, CLWE_{β,γ} is at least as hard as worst-case lattice problems (GapSVP, SIVP) under a polynomial-time **quantum** reduction.
- **Hardness of Gaussian mixture density estimation**: Learning mixtures of Gaussians without separation is hard under lattice assumptions (resolves Diakonikolas 2016 / Moitra 2018 open question).
- **SQ lower bounds for hCLWE**: exponential SQ lower bounds with super-poly precision — matches lattice hardness.
- **Noiseless hCLWE is easy** [Zadik-Song-Wein-Bruna 2022]: LLL solves noiseless hCLWE with n = d+1 samples. CLWE hardness is *noise-dependent* — adding inverse-poly noise breaks the LLL approach.
- **Analogy with LWE**: same iterative quantum reduction structure as Regev 2005; slightly tighter than Ajtai-Dwork due to larger layer separation.

## Where It Appears

- [Bruna Continuous LWE](../sources/bruna-continuous-lwe.md) — introducing paper
- [Lattice Methods Surpass SoS](../sources/zadik-lattice-surpass-sos.md) — noiseless version is poly-time solvable

## Related Concepts

- [Learning With Errors](learning-with-errors.md) — discrete analogue
- [Statistical Query Model](statistical-query-model.md) — hCLWE matches SQ lower bound of DKS17
- [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md)
- [LLL Algorithm](lll-algorithm.md) — solves noiseless version

## Open Questions

- Classical (non-quantum) reduction from lattice problems to CLWE.
- Cryptographic constructions based on CLWE (distinct from LWE).
- Precise noise threshold separating LLL-solvability from lattice-hardness.
- Connection to anti-concentration-based hardness models.
