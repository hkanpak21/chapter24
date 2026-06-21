---
title: Continuous LWE
type: source
date_ingested: 2026-04-12
authors: [Joan Bruna, Oded Regev, Min Jae Song, Yi Tang]
venue: STOC 2021
year: 2021
tags: [lattice-cryptography, continuous-lwe, gaussian-mixtures, statistical-query, hardness-reductions, cryptography]
---

## Summary

This paper introduces **Continuous LWE (CLWE)**, a continuous analogue of the Learning With Errors problem, and establishes it as computationally hard under standard worst-case lattice assumptions (via a polynomial-time quantum reduction from GapSVP/SIVP). In CLWE, equations in Z_q^n are replaced with inner products in R^n: given samples (y_i, z_i) with z_i ≈ γ⟨y_i, w⟩ mod 1 for random Gaussian y_i and secret unit vector w, recover w.

The main consequences:
1. **Resolves computational hardness of learning Gaussian mixtures** without separation (open since Diakonikolas 2016 / Moitra 2018): learning mixtures of Gaussians with non-overlapping components is computationally hard under lattice assumptions, even for mere density estimation.
2. **Addresses Bubeck et al. 2019** open question on the complexity of robust-ML-style Gaussian-pancake problems: CLWE's homogeneous variant (hCLWE) is hard, matching the SQ lower bounds of Diakonikolas-Kane-Stewart 2017.
3. **Opens new avenues for quantum attacks on lattice problems** — a CLWE algorithm implies a quantum lattice algorithm.

The noiseless variant of hCLWE is later shown by [Zadik-Song-Wein-Bruna 2022] to be *not* hard (LLL solves it), emphasizing that noise is essential to CLWE's hardness.

## Key Contributions

- Definition of CLWE (search and decision) and homogeneous CLWE (hCLWE), the latter being a mixture of Gaussian "pancakes" along a hidden direction.
- **Main Theorem 1.1**: quantum poly-time reduction from worst-case GapSVP/SIVP to CLWE_{β,γ} for γ ≥ 2√n, β polynomially bounded.
- Hardness of density-estimation-style learning Gaussian mixtures without separation.
- Hardness of Bubeck et al.'s robust binary classification task.
- Exponential SQ lower bounds for hCLWE in the super-polynomial precision regime.

## Key Definitions / Theorems

- **CLWE_{β,γ}**: samples (y_i, z_i) with y_i ~ N(0, I_n), z_i = γ⟨y_i, w⟩ + ν_i mod 1, ν_i ~ N(0, β²); recover w.
- **hCLWE**: CLWE conditioned on z_i ≈ 0; mixture of Gaussian layers of spacing ≈ 1/γ, width ≈ β/γ along w.
- **Theorem 1.1 (informal)**: CLWE hardness ≡ worst-case lattice hardness (under quantum reductions).
- **SQ lower bound**: hCLWE is SQ-hard with super-polynomial precision (matching lattice hardness).
- **Analogy to LWE**: γ ↔ 1/noise in LWE; β ↔ relative noise α. Larger γ/β separation ↔ stronger LWE variant.

## Connections

- [Continuous LWE](../concepts/continuous-lwe.md) — concept page
- [Learning With Errors](../concepts/learning-with-errors.md)
- [Statistical Query Model](../concepts/statistical-query-model.md) — hCLWE matches SQ lower bound
- [Zadik Lattice Surpass SoS](zadik-lattice-surpass-sos.md) — noiseless hCLWE is poly-time solvable via LLL (not a contradiction; noise is essential)
- [Joan Bruna](../entities/joan-bruna.md), [Oded Regev](../entities/oded-regev.md)

## Open Questions / Limitations

- Reduction is quantum; classical reduction open (like LWE).
- Cryptographic applications mentioned but not explored; discretization needed.
- Noiseless variant easy via LLL — noise is essential.
- Can CLWE be used as foundation for cryptographic primitives distinct from LWE?

## Quotes / Notable Passages

> "Our work resolves an open problem regarding the computational complexity of learning mixtures of Gaussians without separability assumptions."

> "CLWE might be a better algorithmic target than LWE" — suggests CLWE's continuous geometry may enable new lattice algorithm design.
