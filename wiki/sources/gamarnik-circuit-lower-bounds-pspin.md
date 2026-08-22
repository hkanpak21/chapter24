---
title: Circuit Lower Bounds for the p-Spin Optimization Problem
type: source
date_ingested: 2026-04-12
authors: [David Gamarnik, Aukosh Jagannath, Alexander S. Wein]
venue: Preprint (the ingested PDF is arXiv:2109.01342v2, 21 Jan 2022)
year: 2022
tags: [overlap-gap-property, boolean-circuits, p-spin, circuit-complexity, random-optimization, statistical-physics]
claim_quantifier: universal
antecedent: "the multi-overlap gap property for even p at least 4, established in the paper, and the Linial-Mansour-Nisan bound on the total influence of low-depth circuits."
algorithm_class: "circuits"
date_verified: 2026-08-20
---

## Summary

Direct extension of [Gamarnik-Jagannath-Wein 2020](gamarnik-hardness-random-optimization-circuits.md) to the **p-spin optimization problem** with Rademacher couplings on the Boolean hypercube. Establishes that any poly-size n-output Boolean circuit producing a solution within a certain constant factor ρ of optimality must have depth at least log n / (2 log log n).

Unlike prior results focused on decision/yes-no problems, this targets the **search** version: produce the entire solution. The proof uses the **multi-overlap OGP** (GJW21) for p-spin models, showing that no m-tuple of near-optimal solutions can achieve pairwise overlaps in a certain prescribed region. Combined with the Linial-Mansour-Nisan total-influence bound on low-depth circuits (via O'Donnell's textbook formulation) and a discrete biased-Bernoulli interpolation trick, this forces the depth lower bound.

This is among the first instances of spin-glass / OGP techniques yielding bona fide circuit-complexity lower bounds for combinatorial optimization.

## Claim Boundary

- **Quantified over:** poly-size n-output Boolean circuits producing a solution within a constant factor of the p-spin optimum with Rademacher couplings, for approximation ratios above a threshold set by the multi-overlap gap property.
- **Antecedent:** the multi-overlap gap property for even p at least 4, which the paper establishes rather than assumes, together with the Linial-Mansour-Nisan bound on the total influence of low-depth circuits.
- **Algorithm class:** circuits. The result is a depth lower bound of log n over 2 log log n, and it applies to circuits that output the entire solution.
- **Does not establish:** a bound for the decision version, or for approximation ratios below the overlap-gap threshold, or hardness for polynomial time. The authors note that the result does not strictly improve on Rossman's bound, because their circuits are required to produce the whole solution rather than answer a yes or no question.
- **Abstract vs theorem:** none found.

## Key Contributions

- Depth lower bound log n / (2 log log n) for poly-size Boolean circuits producing ρ-approximate p-spin ground state (for ρ above a threshold determined by multi-OGP).
- Adaptation from Gaussian to Rademacher couplings via universality-style arguments.
- Use of multi-overlap OGP (from Wei22) to go beyond what single-instance OGP permits.
- Biased Bernoulli extension of Linial-Mansour-Nisan theorem via a coding trick (Lemma 9 / FJS91 route).

## Key Definitions / Theorems

- **p-spin with Rademacher J**: J_{i₁...i_p} = ±1 i.i.d., optimize ⟨J, σ⟩ / n^{(p+1)/2} over σ ∈ {±1}^n.
- **Multi-overlap e-OGP (Thm 2.2)**: for even p ≥ 4, exists η_OGP, ν₁ < ν₂ such that for all t₁ ≤ t₂, any σ₁, σ₂ achieving value ≥ η_OGP have |⟨σ₁,σ₂⟩|/n ∉ (ν₁, ν₂).
- **Main Theorem 2.3**: For ρ > η_OGP/η*_p, either circuit family is empty or s(n) ≥ n^α or d(n) ≥ log n / (2 log log n).

## Connections

- [Overlap Gap Property](../concepts/overlap-gap-property.md) — multi-overlap variant
- [Circuit Complexity and Stable Algorithms](../concepts/circuit-complexity-random-optimization.md)
- [Gamarnik Random Optimization Circuits](gamarnik-hardness-random-optimization-circuits.md) — sibling paper
- [David Gamarnik](../entities/david-gamarnik.md), [Alexander Wein](../entities/alexander-wein.md), [Aukosh Jagannath](../entities/aukosh-jagannath.md)

## Open Questions / Limitations

- ρ must exceed an OGP-determined threshold; for smaller approximation ratios the argument does not apply.
- Depth bound is log n / log log n, not tight; conjecturally should be higher.
- Single-output decision circuit lower bounds remain open via this technique.
- Does not extend to dense random graphs.

## Quotes / Notable Passages

> _Clauses reordered. Checked against `raw/GJW22_CircuitLBPSpin.pdf` on 2026-08-20. This paper states the sentence with the hedge at the front, as given below; the reordered form an earlier ingest quoted is verbatim in the companion paper `raw/GJW21_HardnessRandomOpt.pdf` instead._
>
> Our result presents the strongest known circuit depth lower bounds for combinatorial optimization problems, to the best of our knowledge.

> "Nevertheless, to the best of our knowledge, our result presents the strongest known circuit depth lower bounds for combinatorial optimization problems."

> "To the best of our knowledge, this is the first instance when methods from spin glass theory have ramifications for circuit complexity."
