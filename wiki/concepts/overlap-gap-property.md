---
title: Overlap Gap Property (OGP)
type: concept
tags: [overlap-gap-property, statistical-physics, random-optimization, p-spin, stable-algorithms, lower-bounds]
---

## Definition

The **Overlap Gap Property (OGP)** [Gamarnik-Sudan 2017, following earlier physics roots] is a structural property of a random optimization landscape. Informally: for a random optimization problem (e.g., maximize ⟨J, σ⟩ over σ ∈ {±1}^n), OGP holds if for every pair σ₁, σ₂ of near-optimal solutions, the normalized overlap |⟨σ₁, σ₂⟩|/n lies in a disjoint union [0, ν₁] ∪ [ν₂, 1] — the intermediate overlaps (ν₁, ν₂) are forbidden.

**Ensemble OGP (e-OGP)**: OGP extended to correlated families of instances under interpolation — for any two instances J_t, J_{t+1} in an interpolating sequence, their near-optimal solutions' pairwise overlaps also fall outside (ν₁, ν₂).

**Multi-overlap OGP**: extended to m-tuples of near-optimal solutions; allows ruling out broader algorithmic families.

## Intuition

OGP is a topological barrier in the solution landscape: near-optima cluster into disjoint "valleys" with no intermediate configurations. Stable algorithms — those whose output depends continuously (or with low influence) on the input — cannot navigate between valleys because interpolating the input would force the output to pass through the forbidden overlap region.

This directly rules out:
- **Low-degree polynomials** (smooth in input)
- **Low-depth Boolean circuits** (low total influence by Linial-Mansour-Nisan)
- **Langevin dynamics / gradient descent** (continuous, stable)
- **Approximate message passing** (AMP) in some regimes

## Properties / Theorems

- **p-spin OGP** [Gamarnik-Jagannath 2021]: For the p-spin glass Hamiltonian with p ≥ 4 even, OGP holds around the optimum multiplied by (1 - ε) ground state energy.
- **OGP rules out low-degree polynomials** [Gamarnik-Jagannath-Wein 2020]: for p-spin ground state and sparse independent set.
- **OGP rules out low-depth circuits** [Gamarnik-Jagannath-Wein 2020/2022]: depth ≥ log n / (2 log log n) required for poly-size circuits; first application of spin-glass tools to circuit complexity.
- **OGP rules out Langevin dynamics** with bounded horizon via SDE well-posedness.
- **Random k-SAT / hypergraph coloring**: OGP established for various random CSPs [Mezard-Mora-Zecchina 2005].
- **Not universal**: For p = 2 (standard PCA), OGP fails and spectral methods find optima.

## Where It Appears

- [Gamarnik Random Optimization Circuits](../sources/gamarnik-hardness-random-optimization-circuits.md)
- [Gamarnik Circuit Lower Bounds p-Spin](../sources/gamarnik-circuit-lower-bounds-pspin.md)
- [Bandeira Franz-Parisi](../sources/bandeira-franz-parisi-criterion.md) — FP is a testing-problem analogue

## Related Concepts

- [Franz-Parisi Criterion](franz-parisi-criterion.md) — detection-problem analogue
- [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md) — algorithm class OGP rules out
- [Circuit Complexity and Stable Algorithms](circuit-complexity-random-optimization.md)
- [Statistical-Computational Gaps](statistical-computational-gaps.md)

## Open Questions

- Precise characterization of problems exhibiting OGP vs. not.
- Relationship to replica symmetry breaking in physics.
- Can OGP arguments be extended to dense Erdős-Rényi independent set?
- Does the absence of OGP imply polynomial-time algorithms exist (converse)?
- Can OGP-based arguments rule out single-output decision circuits (not just search circuits)?
