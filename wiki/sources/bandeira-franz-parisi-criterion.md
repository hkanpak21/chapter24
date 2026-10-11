---
title: The Franz–Parisi Criterion and Computational Trade-Offs in High Dimensional Statistics
type: source
date_ingested: 2026-04-12
authors: [Afonso S. Bandeira, Ahmed El Alaoui, Samuel B. Hopkins, Tselil Schramm, Alexander S. Wein, Ilias Zadik]
venue: "NeurIPS 2022"
venue_evidence: "https://proceedings.neurips.cc/paper_files/paper/2022/hash/daff682411a64632e083b9d6665b1d30-Abstract-Conference.html"
year: 2022
tags: [statistical-computational-gaps, franz-parisi, low-degree-polynomials, statistical-physics, free-energy]
claim_quantifier: conditional
antecedent: "the model class. Equivalence is proved for Gaussian additive models and the implication for planted sparse models. Outside these classes the paper exhibits counterexamples where the two criteria disagree."
algorithm_class: "low-degree, plus local MCMC as a corollary"
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
cls_evidence: "we say that the hypothesis testing problem above is hard for the degree-D likelihood or simply low-degree hard if LD(D) = O(1)"
cls_evidence_src: Def 1.3
cls_reason: "No ML adversary or target: the bound is on the estimator's algorithm class (degree-D polynomials, Def 1.3), so party=learner, unit=algo class, tightness=class, by analogy to what-can-we-learn-privately. Corollary 2.18's local-MCMC bound is the same party under a second algorithm class rather than a second party, so second=none. RECODE 2026-09-03 (R4, no adversary means no phase): phase train time -> n/a."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper builds a rigorous bridge between two previously separate approaches for predicting computational hardness in high-dimensional statistics: (a) the **low-degree polynomial (LD)** framework rooted in theoretical CS, and (b) **free-energy / Franz–Parisi (FP)** criteria rooted in statistical physics of spin glasses. The authors define a new "low-overlap likelihood norm" LO(δ) and the **Franz–Parisi criterion** FP(D) = LO(δ(D)) with δ chosen from the overlap tail, and prove:

(i) For Gaussian additive models, FP-hardness is equivalent to LD-hardness (Theorem 2.4/2.5). This grounds the physics heuristic rigorously.
(ii) For planted sparse models, FP-hardness implies LD-hardness (Theorem 3.7), giving a new route to low-degree lower bounds. Applied to sparse linear regression, this yields new bounds hard to obtain directly.
(iii) For Gaussian additive models, LD-hardness implies failure of local MCMC algorithms (free-energy barrier → MCMC-hard).

The work also exhibits counterexamples where FP and LD disagree, suggesting that the equivalence is model-dependent and opening the question of which free-energy criterion is right for which problem.

## Claim Boundary

- **Quantified over:** two model classes. The Franz-Parisi and low-degree criteria are proved equivalent for Gaussian additive models, and Franz-Parisi hardness implies low-degree hardness for planted sparse models.
- **Antecedent:** the model class itself. Outside these classes the paper exhibits counterexamples where the two criteria disagree, so the equivalence is not general.
- **Algorithm class:** low-degree, with local MCMC appearing as a corollary for Gaussian additive models. Neither is polynomial time.
- **Does not establish:** that the free-energy heuristic predicts polynomial-time hardness. It establishes that two heuristics agree on stated model classes and disagree outside them.
- **Abstract vs theorem:** none found. The abstract restricts each claim to its model class.

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

> _Not verbatim. Checked against `raw/BEHSWZ22_FranzParisiCriterion.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary._
>
> LD-hardness implies failure of 'geometric' local MCMC algorithms, the first formal bridge from TCS-style LD lower bounds to statistical-physics-style dynamical barriers.

The passage the paraphrase was drawn from is below, verbatim, verified 2026-08-20. Note that it is restricted to Gaussian additive models, which the paraphrase dropped.

> "establish that for Gaussian additive models the "algebraic" notion of low-degree hardness implies failure of "geometric" local MCMC algorithms, and provide new low-degree lower bounds for sparse linear regression which seem difficult to prove directly"
