---
title: Hardness of Random Optimization Problems for Boolean Circuits, Low-Degree Polynomials, and Langevin Dynamics
type: source
date_ingested: 2026-04-12
authors: [David Gamarnik, Aukosh Jagannath, Alexander S. Wein]
venue: FOCS 2020, journal version 2022 (the ingested PDF is arXiv:2004.12063v2, 26 Jan 2022, and does not itself state a venue)
year: 2022
tags: [overlap-gap-property, low-degree-polynomials, boolean-circuits, langevin-dynamics, random-optimization, p-spin, circuit-complexity]
claim_quantifier: universal
antecedent: "the overlap gap property for the models considered, which the paper proves rather than assumes. The mechanism is that all three algorithm classes are stable under small input perturbations."
algorithm_class: "low-degree, circuits, Langevin dynamics"
date_verified: 2026-08-20
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: algo class
cls_tightness: class
cls_baseline: n/a
cls_second_party: none
cls_assessed: explicit
cls_evidence: "we show a linear in n lower bound on the degree required for such an algorithm to succeed modulo exponentially small probability in n"
cls_evidence_src: "§1 (Introduction)"
cls_reason: "Classified on the low-degree result, first of three algorithm classes named in the abstract's list order (low-degree, circuits, Langevin); party=learner by analogy to sibling low-degree hardness pages (bandeira-franz-parisi-criterion, low-degree-polynomials-survey), since no ML adversary or target is present. phase=n/a rather than train time: this is combinatorial optimization on random instances (p-spin ground state, independent set), not a data-fitting or ML train/test pipeline. The circuit (poly-size, low-depth) and Langevin (bounded-time) theorems share the same party/unit/tightness shape as separate instantiations of the same OGP/stability mechanism, not a second party or a second incomparable notion on this claim, so second_party is none and second_notion is omitted; flagged for a second reader given the paper gives three co-equal theorems and this row reports only one."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper proves computational hardness of two random optimization problems — (a) finding near-ground states of the p-spin glass Hamiltonian (spherical and Ising), and (b) finding large independent sets in sparse Erdős–Rényi graphs — against three classes of algorithms: (i) low-degree polynomials, (ii) low-depth Boolean circuits, (iii) Langevin dynamics with bounded time horizon. The unifying mechanism is the **Overlap Gap Property (OGP)**, a structural property of the random landscape that precludes stable algorithms from finding near-optimal solutions.

The circuit lower bound is particularly notable: it gives a super-polynomial depth lower bound (depth ≥ log n / (log log n)^{O(1)}) for any poly-size circuit producing a large independent set in a sparse random graph, stronger than prior Rossman-style bounds which required o(log n / log log n) depth. The core proof technique converts OGP-based noise-insensitivity arguments from real-valued polynomials to Boolean circuits via the Linial-Mansour-Nisan theorem bounding total influence of low-depth circuits.

The Langevin result is a straightforward consequence of SDE well-posedness: bounded-horizon Langevin is stable, so OGP blocks it. All three algorithm classes share a form of noise-insensitivity that OGP directly rules out via an interpolation argument.

## Claim Boundary

- **Quantified over:** three algorithm classes on two random optimization problems. The classes are low-degree polynomials of the input, low-depth Boolean circuits, and Langevin dynamics run for bounded time. The problems are the ground state of a spherical or Ising p-spin glass and large independent sets in sparse Erdos-Renyi graphs.
- **Antecedent:** the overlap gap property for the models considered, which the paper proves rather than assumes. The mechanism is that all three classes are stable, so that a small perturbation of the input induces a small perturbation of the output.
- **Algorithm class:** low-degree, circuits and Langevin dynamics. What the argument actually uses is stability, so an algorithm that is not stable in this sense lies outside the reach of the proof.
- **Does not establish:** hardness for polynomial time. The circuit result is a depth lower bound for poly-size circuits that produce a whole solution, so it concerns the search problem and not the decision problem.
- **Abstract vs theorem:** none found. The abstract flags the search versus decision caveat itself, in parentheses, at the point where it claims an improvement on the state of the art in circuit complexity.

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

> _Not from this paper. Checked against `raw/GJW21_HardnessRandomOpt.pdf` on 2026-08-20 and not found. The sentence is verbatim in the companion note, `raw/GJW22_CircuitLBPSpin.pdf`, and belongs on [Circuit Lower Bounds for the p-Spin Optimization Problem](gamarnik-circuit-lower-bounds-pspin.md). Retained here unquoted so the misattribution is not repeated._
>
> To the best of our knowledge, this is the first instance when methods from spin glass theory have ramifications for circuit complexity.

> "For the case of Boolean circuits, our results improve the state-of-the-art bounds known in circuit complexity theory (although we consider the search problem as opposed to the decision problem)."

> "Nevertheless, our result presents the strongest known circuit depth lower bounds for combinatorial optimization problems, to the best of our knowledge."
