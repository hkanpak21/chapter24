---
title: Hardness of Random Optimization Problems for Boolean Circuits, Low-Degree Polynomials, and Langevin Dynamics
type: source
date_ingested: 2026-04-12
authors: [David Gamarnik, Aukosh Jagannath, Alexander S. Wein]
venue: FOCS 2020 (journal version 2022)
year: 2022
tags: [overlap-gap-property, low-degree-polynomials, boolean-circuits, langevin-dynamics, random-optimization, p-spin, circuit-complexity]
---

## Summary

This paper proves computational hardness of two random optimization problems — (a) finding near-ground states of the p-spin glass Hamiltonian (spherical and Ising), and (b) finding large independent sets in sparse Erdős–Rényi graphs — against three classes of algorithms: (i) low-degree polynomials, (ii) low-depth Boolean circuits, (iii) Langevin dynamics with bounded time horizon. The unifying mechanism is the **Overlap Gap Property (OGP)**, a structural property of the random landscape that precludes stable algorithms from finding near-optimal solutions.

The circuit lower bound is particularly notable: it gives a super-polynomial depth lower bound (depth ≥ log n / (log log n)^{O(1)}) for any poly-size circuit producing a large independent set in a sparse random graph, stronger than prior Rossman-style bounds which required o(log n / log log n) depth. The core proof technique converts OGP-based noise-insensitivity arguments from real-valued polynomials to Boolean circuits via the Linial-Mansour-Nisan theorem bounding total influence of low-depth circuits.

The Langevin result is a straightforward consequence of SDE well-posedness: bounded-horizon Langevin is stable, so OGP blocks it. All three algorithm classes share a form of noise-insensitivity that OGP directly rules out via an interpolation argument.

## Key Contributions

- OGP-based hardness for **low-degree polynomials** (linear in n degree) against p-spin ground state and sparse independent set.
- **First circuit-complexity lower bounds** (poly-size, low-depth) for these combinatorial optimization problems, via hypercontractivity + total influence bounds.
- Langevin dynamics hardness: bounded-time Langevin cannot achieve near-optimality for spherical p-spin.
- Unification: ensemble OGP (e-OGP) as the common barrier to all "stable" algorithms.

## Key Definitions / Theorems

- **p-spin Hamiltonian**: H_n(x; Y) = n^{-(p+1)/2} ⟨Y, x^⊗p⟩.
- **Overlap Gap Property (OGP)**: for every pair of near-optimal solutions x₁, x₂, the overlap |⟨x₁, x₂⟩|/n lies in a disjoint union [0, ν₁] ∪ [ν₂, 1].
- **Ensemble OGP (e-OGP)**: OGP extended to interpolated families of instances.
- **Main circuit theorem**: poly-size circuits producing near-optimal independent set in sparse Erdős-Rényi graph must have depth ≥ log n / (2 log log n).
- **Low-degree hardness**: polynomials of degree linear in n cannot achieve constant-factor approximation for p-spin.

## Connections

- [Overlap Gap Property](../concepts/overlap-gap-property.md) — main structural tool
- [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md) — algorithm class lower-bounded
- [Circuit Complexity and Stable Algorithms](../concepts/circuit-complexity-random-optimization.md)
- [Gamarnik Circuit Lower Bounds p-Spin](gamarnik-circuit-lower-bounds-pspin.md) — companion/followup paper
- [David Gamarnik](../entities/david-gamarnik.md), [Alexander Wein](../entities/alexander-wein.md), [Aukosh Jagannath](../entities/aukosh-jagannath.md)

## Open Questions / Limitations

- Circuit bound is for **search** (produce solution), not decision.
- Depth bound log n / log log n is strong but not optimal; tight bound unknown.
- Does not rule out single-output decision circuits for these problems.
- Open whether OGP-based techniques extend to dense Erdős-Rényi (current technique's probability tail is too weak).

## Quotes / Notable Passages

> "The crux of our proof is that the classes of algorithms we consider exhibit a form of stability (noise-insensitivity): a small perturbation of the input induces a small perturbation of the output. We show by an interpolation argument that stable algorithms cannot overcome the OGP barrier."

> "To the best of our knowledge, this is the first instance when methods from spin glass theory have ramifications for circuit complexity."
