---
title: The Franz–Parisi Criterion and Computational Trade-Offs in High Dimensional Statistics
type: source
date_ingested: 2026-04-12
authors: [Afonso S. Bandeira, Ahmed El Alaoui, Samuel B. Hopkins, Tselil Schramm, Alexander S. Wein, Ilias Zadik]
venue: Preprint / NeurIPS 2022
year: 2022
tags: [statistical-computational-gaps, franz-parisi, low-degree-polynomials, statistical-physics, free-energy]
---

## Summary

This paper builds a rigorous bridge between two previously separate approaches for predicting computational hardness in high-dimensional statistics: (a) the **low-degree polynomial (LD)** framework rooted in theoretical CS, and (b) **free-energy / Franz–Parisi (FP)** criteria rooted in statistical physics of spin glasses. The authors define a new "low-overlap likelihood norm" LO(δ) and the **Franz–Parisi criterion** FP(D) = LO(δ(D)) with δ chosen from the overlap tail, and prove:

(i) For Gaussian additive models, FP-hardness is equivalent to LD-hardness (Theorem 2.4/2.5). This grounds the physics heuristic rigorously.
(ii) For planted sparse models, FP-hardness implies LD-hardness (Theorem 3.7), giving a new route to low-degree lower bounds. Applied to sparse linear regression, this yields new bounds hard to obtain directly.
(iii) For Gaussian additive models, LD-hardness implies failure of local MCMC algorithms (free-energy barrier → MCMC-hard).

The work also exhibits counterexamples where FP and LD disagree, suggesting that the equivalence is model-dependent and opening the question of which free-energy criterion is right for which problem.

## Key Contributions

- **Franz–Parisi criterion (Def 1.5)**: FP(D) := LO(δ(D)) where δ(D) is the overlap threshold with tail e^{-D}.
- Rigorous FP ↔ LD equivalence for Gaussian additive models.
- FP ⟹ LD for planted sparse problems; new LD lower bounds for sparse regression.
- Free-energy barrier ⟹ MCMC hardness for Gaussian models.
- Counterexamples (Section 4) demonstrating the equivalence is not universal.

## Key Definitions / Theorems

- **Low-Overlap Likelihood Norm**: LO(δ) = E_{u,v ~ μ} [ 1_{|⟨u,v⟩|≤δ} · ⟨L_u, L_v⟩_Q ].
- **Franz–Parisi Criterion**: FP(D) = LO(δ(D)) for δ(D) = sup{ε ≥ 0 : Pr[|⟨u,v⟩| ≥ ε] ≥ e^{-D}}.
- **Theorems 2.4/2.5**: FP(D) = Θ(LD(D')) for D' = D log n in Gaussian additive models.
- **Theorem 3.7**: For planted sparse models, FP-hard ⟹ LD-hard.
- **Corollary 2.18**: LD-hard ⟹ local MCMC-hard (free energy barrier).
- **Theorem 3.10**: New sparse linear regression low-degree lower bounds.

## Connections

- [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md) — one endpoint
- [Franz-Parisi Criterion](../concepts/franz-parisi-criterion.md) — new concept introduced here
- [Overlap Gap Property](../concepts/overlap-gap-property.md) — related physics-based barrier
- [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md)
- [Alexander Wein](../entities/alexander-wein.md), [Samuel Hopkins](../entities/samuel-hopkins.md), [Tselil Schramm](../entities/tselil-schramm.md), [Afonso Bandeira](../entities/afonso-bandeira.md), [Ilias Zadik](../entities/ilias-zadik.md)

## Open Questions / Limitations

- FP and LD disagree for some problems (Section 4); precise characterization of when they agree is open.
- Equivalence is proven only for specific model classes (Gaussian additive, certain sparse models).
- Annealed vs. quenched FP potential: paper uses annealed; may miss phenomena visible only in quenched.
- Does FP-based criterion extend to non-Gaussian / discrete noise models?

## Quotes / Notable Passages

> "This paper aims to make a rigorous connection between the low-degree and free-energy based approaches in the setting of statistical inference."

> "LD-hardness implies failure of 'geometric' local MCMC algorithms" — the first formal bridge from TCS-style LD lower bounds to statistical-physics-style dynamical barriers.
