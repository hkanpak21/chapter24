---
title: Statistical Query Algorithms and Low-Degree Tests Are Almost Equivalent
type: source
date_ingested: 2026-04-12
authors: [Matthew Brennan, Guy Bresler, Samuel B. Hopkins, Jerry Li, Tselil Schramm]
venue: "COLT 2021"
venue_evidence: "https://proceedings.mlr.press/v134/brennan21a.html; Proceedings of Thirty Fourth Conference on Learning Theory, PMLR vol 134"
year: 2021
tags: [statistical-query, low-degree-polynomials, statistical-computational-gaps, lower-bounds]
claim_quantifier: conditional
antecedent: "the (delta, k)-nicenness condition of Definition 1.4. Proved automatic for Gaussian and product-measure problems, and false for the one-shot planted clique problem until the cloning recipe is applied."
algorithm_class: "SQ and low-degree"
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
cls_second_notion: algo class
cls_assessed: explicit
cls_evidence: "Our main result is a surprisingly tight equivalence, under mild conditions, between statistical dimension and the minimum degree of any good distinguisher."
cls_evidence_src: "§1.2"
cls_reason: "party=attacker is the generic label for the bounded distinguisher; no ML-specific role applies to this pure complexity-theory equivalence. unit=algo class covers both SQ and low-degree; the vocabulary has no way to distinguish the two, so second_notion duplicates unit=algo class to flag that Thm 1.6 relates one distinguisher under two class notions (rule 4b). RECODE 2026-09-03 (R3, solver is the learner): party attacker -> learner."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper establishes a formal equivalence, under mild regularity ("nicenness") conditions, between two of the most popular restricted models used to evidence statistical-computational gaps: the **Statistical Query (SQ) model** and **low-degree polynomial (LD) tests**. Concretely, the authors show that for a (δ, k)-nice hypothesis testing problem, the minimum degree D of a good low-degree distinguisher and the log of the SQ complexity (VSTAT query count) are essentially equal: D_LD ≈ Θ(log m_SQ).

This unifies two parallel lines of lower-bound work — SQ bounds (Feldman et al.) and low-degree bounds (Hopkins et al.) — into a single framework. It has immediate corollaries: new SQ lower bounds for sparse PCA, tensor PCA, spiked Wishart, and variants of planted clique, derived automatically from known low-degree bounds.

The paper identifies **nicenness** as the key condition: roughly, no high-degree function of very few samples is a good distinguisher. This rules out a trivial counterexample (single-query SQ algorithm for PC with indicator-of-clique query) while still covering most problems of interest.

## Claim Boundary

- **Quantified over:** hypothesis testing problems satisfying the paper's nicenness condition. For those, the minimum degree of a good low-degree distinguisher and the logarithm of the statistical dimension are related up to the stated factors.
- **Antecedent:** (delta, k)-nicenness. It is proved automatic for Gaussian and product-measure problems and it fails for the one-shot planted clique problem, which must first be converted by the paper's cloning recipe.
- **Algorithm class:** SQ and low-degree. The theorem relates two restricted classes to each other. Neither side is a statement about polynomial time.
- **Does not establish:** that either class captures polynomial time. A new SQ bound obtained by transfer inherits exactly the strength of the low-degree bound it came from and no more. Problems with strong algebraic structure are excluded on both sides.
- **Abstract vs theorem:** the remark that low-degree distinguishability closely tracks known polynomial-time tests is an observation about the current algorithmic record, hedged in the same sentence by the exclusion of unusual algebraic structure. No theorem in the paper asserts it.

## Key Contributions

- Two-way bounds: bounds on low-degree complexity imply bounds on statistical dimension, and vice versa.
- Formalization of the **nicenness** condition (Definition 1.4) under which the equivalence holds.
- **Cloning** technique to "dilute" SQ power and level the playing field between single-sample and multi-sample models.
- Canonical recipe (Remark 1.9) for converting one-shot problems (like PC) into nice many-sample problems.
- New SQ lower bounds for: sparse PCA, tensor PCA, spiked Wishart, variants of planted clique/planted dense subgraph, Gaussian graphical models, sparse parity with noise.

## Key Definitions / Theorems

- **(δ, k)-nicenness**: no k-purely-high-degree function of k samples is a nontrivial δ-distinguisher.
- **Theorem 1.6 (Main)**: For (m^{-k/2}/4, k)-nice problems, low-degree complexity d and SDA(S, m') = O((2m/m')^{O(k)}) are polynomially related (with the translation involving k).
- **Theorem 1.7**: For Gaussian / product-measure problems, the nicenness condition is automatic.
- Robust SQ bound framework via noise operators and random restrictions (Section 5).

## Connections

- [Statistical Query Model](../concepts/statistical-query-model.md) — one side of the equivalence
- [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md) — other side
- [Planted Clique](../concepts/planted-clique.md) — key application
- [Reducibility and Statistical-Computational Gaps](reducibility-statistical-computational-gaps.md) — uses SQ lower bounds for PC_ρ
- [Matthew Brennan](../entities/matthew-brennan.md), [Guy Bresler](../entities/guy-bresler.md), [Samuel Hopkins](../entities/samuel-hopkins.md), [Tselil Schramm](../entities/tselil-schramm.md), [Jerry Li](../entities/jerry-li.md)

## Open Questions / Limitations

- Nicenness condition excludes some natural problems (e.g., vanilla one-shot PC); requires transformation.
- Equivalence is "almost": there are (log m)² factors; not bit-tight.
- Does not cover problems with strong algebraic structure (parity with noise is handled via nicenness but more exotic algebraic problems may escape).
- Simulation-style reductions are lossy; the authors' argument is non-constructive (no efficient simulation, but equivalence of complexities).

## Quotes / Notable Passages

> "Our main result is a surprisingly tight equivalence, under mild conditions, between statistical dimension and the minimum degree of any good distinguisher."

> "Remarkably, excluding problems with unusual algebraic structure [HW20], the (non)existence of a low-degree distinguisher closely tracks the (non)existence of any known poly-time hypothesis test."

_Verbatim, verified against `raw/BBHLS21_SQLowDegreeEquivalence.pdf` on 2026-08-20. An earlier rendering dropped the citation marker `[HW20]`, which points at [Counterexamples to the Low-Degree Conjecture](holmgren-counterexamples-low-degree.md) and carries the exclusion that makes the sentence true._
