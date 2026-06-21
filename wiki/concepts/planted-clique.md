---
title: Planted Clique
type: concept
tags: [planted-clique, statistical-computational-gaps, hardness-reductions, average-case-reductions, complexity-theory]
---

## Definition

The **planted clique problem** (PC): Given a graph G on n vertices, determine whether G was drawn from:
- H₀: G ~ G(n, 1/2) (Erdős-Rényi, no clique)
- H₁: G ~ G(n, k, 1/2) (Erdős-Rényi with a uniformly random k-clique planted)

The **Planted Clique Conjecture**: There is no polynomial-time algorithm solving PC(n, k, 1/2) when k = o(√n).

The statistical threshold for detection is k = Ω(log n) (largest clique in G(n,1/2) has size ~2 log₂ n). The conjectured computational threshold is k = Θ(√n). This gap between log n and √n is the statistical-computational gap.

## Intuition

Planted clique is the canonical "hard" problem in average-case complexity of statistical inference. Finding a clique of size much larger than the random background is statistically easy (it's a large deviation), but computationally hard when the clique is slightly sub-√n. Many algorithms — spectral, SDP, message passing — fail exactly at k = o(√n), and no polynomial-time algorithm has been found to go below this threshold.

The key feature that makes PC useful as a basis for hardness reductions: it is a clean, symmetric, well-studied problem over a natural random model.

## Properties / Theorems

**Planted Clique Conjecture**: No poly(n)-time algorithm solves PC(n,k,1/2) for k = o(√n). This is widely believed but unproven.

**Quasipolynomial algorithm** [AAK+07]: PC can be solved in quasipolynomial time by searching vertex subsets of size (2+ε)log₂ n.

**Failure of restricted algorithms**:
- SDP relaxations fail for k = o(√n) [AAK98, FK00]
- Statistical query algorithms fail for k = o(√n) [FGR+13 / Feldman et al. 2017]
- Low-degree polynomials fail for k = o(√n) [BHK+16]
- Sum-of-Squares hierarchy: near-tight n^{1/2 - o(1)} integrality gap at degree O(log n) [Barak-Hopkins-Kelner-Kothari-Moitra-Potechin 2016] via pseudo-calibration
- Spectral, message passing, semidefinite programming, nuclear norm all fail below threshold
- SQ and LD lower bounds are almost equivalent [Brennan-Bresler-Hopkins-Li-Schramm 2021], consolidating the evidence

**Equivalence of PC variants**: Hirahara 2024 establishes that detection, search, and refutation formulations of PC are polynomial-time equivalent — the PC conjecture is a single assumption, not a family.

**Hardness transfer**: PC hardness has been used to show hardness of: sparse PCA, community detection, RIP certification, sparse regression, tensor decomposition, planted subgraph, robust sparse mean estimation, and many more via reductions.

**Relation to secret leakage**: The [Secret Leakage Planted Clique](secret-leakage-planted-clique.md) (PC_ρ) generalizes PC by sampling the clique vertex set from distribution ρ, enabling reductions to problems with very different structure.

## Where It Appears

- [Reducibility and Statistical-Computational Gaps](../sources/reducibility-statistical-computational-gaps.md) — starting point for the web of reductions; PC is generalized to PC_ρ
- [Barak et al. SoS Lower Bound](../sources/barak-sos-lower-bound-planted-clique.md) — near-tight degree-d SoS integrality gap n^{1/2 - o(1)}
- [Feldman et al. Statistical Algorithms](../sources/feldman-statistical-algorithms-planted-clique.md) — SQ lower bound via statistical dimension
- [Hirahara Planted Clique Conjectures Equivalent](../sources/hirahara-planted-clique-conjectures-equivalent.md) — equivalence of detection/search/refutation PC conjectures
- [Brennan SQ-LowDegree Equivalence](../sources/brennan-sq-lowdegree-equivalence.md) — uses PC variants as main application

## Related Concepts

- [Secret Leakage Planted Clique](secret-leakage-planted-clique.md) — generalization enabling broader reductions
- [Statistical-Computational Gaps](statistical-computational-gaps.md) — PC is the flagship example
- [Average-Case Reductions](average-case-reductions.md) — PC is the canonical hard problem used as reduction source
- [Statistical Query Model](statistical-query-model.md) — PC lower bounds proven via SQ

## Open Questions

- Is there a polynomial-time algorithm for k = ω(n^{1/2-ε}) for any ε > 0? (Almost certainly no, but unproven)
- Can planted clique hardness be based on worst-case complexity assumptions?
- Is PC the right starting assumption for average-case reductions, or is PC_ρ strictly more useful?
