---
title: Statistical Algorithms and a Lower Bound for Detecting Planted Cliques
type: source
date_ingested: 2026-04-12
authors: [Vitaly Feldman, Elena Grigorescu, Lev Reyzin, Santosh S. Vempala, Ying Xiao]
venue: JACM 2017 (conference: STOC 2013)
year: 2017
tags: [planted-clique, statistical-query, lower-bounds, statistical-computational-gaps]
---

## Summary

This paper (FGR+13 in the literature) establishes the foundational Statistical Query (SQ) lower bound for planted clique. It generalizes Kearns' SQ framework from PAC learning to distributional search/optimization problems, introducing a notion of **statistical dimension** (SDA) for such problems. The main theorem shows that any SQ algorithm solving planted clique with clique size k requires either super-polynomially many queries or queries of super-polynomial precision whenever k = o(√n) — matching the conjectured √n threshold.

This is widely cited as the first "restricted model" evidence for the PC conjecture beyond SDP/LS+ hierarchies, and serves as a template for SQ lower bounds across the entire statistical-computational gap literature (tensor PCA, sparse PCA, community detection, robust mean estimation).

## Key Contributions

- Extension of the SQ framework from labeled PAC learning to unsupervised/distributional problems via the VSTAT(m) oracle.
- Introduction of **statistical dimension with average correlation (SDA)** — a complexity measure that lower bounds SQ query complexity.
- SQ lower bound for bipartite planted clique (and thus planted clique itself) of n^{Ω(log n)} queries for k ≤ n^{1/2 - ε}.
- Template for proving SQ hardness of many subsequent statistical-computational gap problems.

## Key Definitions / Theorems

- **VSTAT(m) oracle**: returns E[φ(x)] ± max(1/m, √(Var/m)) — models algorithms that access ~m i.i.d. samples only through statistical averages.
- **Statistical Dimension SDA(D₀, S, m)**: maximum q such that any subset of S of density ≥ 1/q has average pairwise correlation ≤ 1/m. Lower bounds SQ complexity.
- **Main theorem**: Any SQ algorithm for bipartite planted k-clique requires n^{Ω(log n)} queries to VSTAT(o(n²/k²)) for k = o(√n).

## Connections

- [Planted Clique](../concepts/planted-clique.md) — canonical application
- [Statistical Query Model](../concepts/statistical-query-model.md) — formally extended here
- [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md) — later shown nearly equivalent [Brennan-Bresler-Hopkins-Li-Schramm 2021]
- [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md) — foundational evidence

## Open Questions / Limitations

- SQ lower bounds do not formally imply polynomial-time hardness (SQ is a restricted model).
- The bipartite formulation is used for technical convenience; translating cleanly to the standard one-shot PC problem requires care (see Brennan et al. 2021 nicenness condition).
- Does not address search/refutation variants directly.

## Quotes / Notable Passages

- Statistical dimension framework has become the standard tool for SQ lower bounds in high-dimensional statistics.
