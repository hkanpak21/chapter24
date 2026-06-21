---
title: Circuit Complexity and Stable Algorithms for Random Optimization
type: concept
tags: [circuit-complexity, boolean-circuits, stable-algorithms, overlap-gap-property, random-optimization, total-influence]
---

## Definition

A line of work [Gamarnik-Jagannath-Wein 2020, 2022] establishes circuit-complexity lower bounds for random combinatorial optimization problems by leveraging the **Overlap Gap Property (OGP)** and the **noise-insensitivity / low-total-influence** property of low-depth Boolean circuits.

**Stable algorithm principle**: An algorithm A is "stable" if small perturbations of its input produce small changes in its output. Formally, low-depth Boolean circuits have low total influence (Linial-Mansour-Nisan theorem): a depth-d poly-size circuit has total influence at most (log n)^{O(d)}.

**OGP as a stability barrier**: If the near-optimal solutions of a random optimization problem cluster into disjoint overlap regions (OGP), a stable algorithm cannot move between clusters as the input interpolates — contradicting the algorithm's ability to always find a near-optimum.

## Properties / Theorems

- **Linial-Mansour-Nisan theorem**: depth-d poly-size Boolean circuits have total influence at most O((log n)^{d}).
- **GJW20 main result**: Poly-size n-output circuits producing ρ-approximate max independent sets in sparse Erdős-Rényi graphs must have depth ≥ log n / (2 log log n). Strengthens Rossman's bound, which was for decision problems with depth o(log n / log log n).
- **GJW22 for p-spin**: same depth lower bound for p-spin ground-state search on {±1}^n, using multi-overlap OGP.
- **First spin-glass ↔ circuit-complexity link**: these are among the first results where statistical physics tools (OGP) yield Boolean-circuit lower bounds.

## Where It Appears

- [Gamarnik Random Optimization Circuits](../sources/gamarnik-hardness-random-optimization-circuits.md)
- [Gamarnik Circuit Lower Bounds p-Spin](../sources/gamarnik-circuit-lower-bounds-pspin.md)

## Related Concepts

- [Overlap Gap Property](overlap-gap-property.md)
- [Low-Degree Polynomial Framework](low-degree-polynomial-framework.md)

## Open Questions

- Extend to dense random graphs (current technique's probability tail fails).
- Decision / single-output circuit lower bounds via OGP — currently only search-version bounds.
- Tight depth bound (conjecturally larger than log n / log log n).
- Circuit lower bounds for AC⁰[⊕] or TC⁰ classes for random optimization.
