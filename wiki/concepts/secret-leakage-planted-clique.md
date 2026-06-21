---
title: Secret Leakage Planted Clique (PC_ρ)
type: concept
tags: [planted-clique, statistical-computational-gaps, hardness-reductions, average-case-reductions, complexity-theory]
---

## Definition

**Secret Leakage PC_ρ** [Brennan & Bresler 2020]: A generalization of [planted clique](planted-clique.md) where the clique vertex set S is sampled from a distribution ρ over k-subsets of [n], rather than uniformly at random.

**Formally (Definition 2.1)**: Given distribution ρ on k-subsets of [n], let G_ρ(n,k,1/2) be the distribution on n-vertex graphs sampled by:
1. Sample G ~ G(n,1/2)
2. Sample S ~ ρ independently
3. Plant a k-clique on vertex set S in G

**Problem PC_ρ(n,k,1/2)**: Distinguish H₀: G ~ G(n,1/2) from H₁: G ~ G_ρ(n,k,1/2).

**"Secret leakage"** refers to the prior ρ revealing partial information about the clique location — the vertices of the planted clique are not uniformly chosen but are drawn from ρ, which can encode structural constraints.

## Intuition

PC asks: is there a planted clique anywhere in G? PC_ρ asks: is there a planted clique whose vertices satisfy the constraints encoded by ρ? By varying ρ, one can encode many different structural constraints — partitions, bipartite structure, hypergraph structure — that make PC_ρ naturally reduce to problems with very different underlying distributions.

The "leakage" of ρ is the key: it allows the reduction to "explain" why the planted structure looks like the target problem's structure. Prior reductions that started from PC could only reach problems resembling "sparse submatrix + noise" because PC's uniform prior didn't encode other structures. PC_ρ breaks this barrier.

## Properties / Theorems

**PC_ρ Conjecture (Conjecture 2.2)**: If ρ has overlap distribution p_ρ(s) satisfying tail bounds `p_ρ(s) ≤ p₀ · {2^{-2s²} if 1 ≤ s² < d; s^{-2d-1} if s² ≥ d}` for d = O_n((log n)^{1+δ}), then no poly-time algorithm solves PC_ρ(n,k,1/2).

**Specific hardness assumptions (Conjecture 2.3)**: Four variants — k-PC, BPC, k-BPC, k-HPC^s — each corresponding to a specific ρ. k-HPC^s (k-partite hypergraph PC with s ≥ 3) is the strongest and implies the others.

**Relationship to PC**: Standard PC is PC_ρ where ρ is uniform over all k-subsets. k-partite PC (k-PC) reveals which of k equal-sized partition classes each clique vertex comes from. This reveals Θ(k log k) bits about the k-subset — a small amount, justifying the "secret leakage" name.

**Low-degree lower bounds** [Section 12.2]: Low-degree polynomials fail to solve PC_ρ subject to the tail condition — provides evidence for the conjecture matching the conjecture for standard PC.

**SQ lower bounds** [Section 12.3]: Statistical Query algorithms fail to solve PC_ρ for specific ρ related to the hardness assumptions.

**Reduction reach**: PC_ρ variants enable reductions to problems including: robust sparse mean estimation, stochastic block models, negatively correlated sparse PCA, mixtures of sparse linear regressions, tensor PCA, universality for sparse mixtures — none of which were previously reachable from PC.

## Where It Appears

- [Reducibility and Statistical-Computational Gaps](../sources/reducibility-statistical-computational-gaps.md) — introduced here as the central new concept

## Related Concepts

- [Planted Clique](planted-clique.md) — the special case ρ = uniform
- [Statistical-Computational Gaps](statistical-computational-gaps.md)
- [Average-Case Reductions](average-case-reductions.md)
- [Statistical Query Model](statistical-query-model.md)

## Open Questions

- Is the PC_ρ conjecture equivalent to the standard PC conjecture for all ρ satisfying the tail condition? Or are there ρ where PC_ρ is easier than PC?
- Can PC_ρ hardness be derived from worst-case complexity assumptions?
- Does the PC_ρ framework extend to non-graph problems (e.g., planted structure in matrices or tensors directly)?
