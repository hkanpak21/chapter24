---
title: Statistical Query Algorithms and Low-Degree Tests Are Almost Equivalent
type: source
date_ingested: 2026-04-12
authors: [Matthew Brennan, Guy Bresler, Samuel B. Hopkins, Jerry Li, Tselil Schramm]
venue: COLT 2021
year: 2021
tags: [statistical-query, low-degree-polynomials, statistical-computational-gaps, lower-bounds]
---

## Summary

This paper establishes a formal equivalence, under mild regularity ("nicenness") conditions, between two of the most popular restricted models used to evidence statistical-computational gaps: the **Statistical Query (SQ) model** and **low-degree polynomial (LD) tests**. Concretely, the authors show that for a (δ, k)-nice hypothesis testing problem, the minimum degree D of a good low-degree distinguisher and the log of the SQ complexity (VSTAT query count) are essentially equal: D_LD ≈ Θ(log m_SQ).

This unifies two parallel lines of lower-bound work — SQ bounds (Feldman et al.) and low-degree bounds (Hopkins et al.) — into a single framework. It has immediate corollaries: new SQ lower bounds for sparse PCA, tensor PCA, spiked Wishart, and variants of planted clique, derived automatically from known low-degree bounds.

The paper identifies **nicenness** as the key condition: roughly, no high-degree function of very few samples is a good distinguisher. This rules out a trivial counterexample (single-query SQ algorithm for PC with indicator-of-clique query) while still covering most problems of interest.

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

> "Remarkably, excluding problems with unusual algebraic structure, the (non)existence of a low-degree distinguisher closely tracks the (non)existence of any known poly-time hypothesis test."
