---
title: "Reducibility and Statistical-Computational Gaps from Secret Leakage"
type: source
date_ingested: 2026-04-12
authors: [Matthew Brennan, Guy Bresler]
venue: arXiv preprint (arXiv:2005.08099v2)
year: 2020
tags: [statistical-computational-gaps, hardness-reductions, planted-clique, average-case-reductions, complexity-theory, learning-theory, statistical-query]
---

## Summary

This paper provides the first evidence that average-case reductions can relate statistical inference problems with *very different* high-dimensional structure. Prior work on average-case reductions was largely limited to problems sharing the "sparse submatrix plus noise matrix" structure of planted clique. The key insight is the **secret leakage planted clique** (PC_ρ) generalization: by revealing a small amount of information about the hidden clique vertices, a mild generalization of the planted clique conjecture enables reductions to problems with entirely different structure.

The paper constructs a *web* of reductions (see Figure 1) from k-partite, bipartite, and hypergraph variants of PC, yielding tight statistical-computational tradeoffs for a broad range of problems: robust sparse mean estimation, dense stochastic block models, hidden partition models, semirandom planted dense subgraph, negatively correlated sparse PCA, mixtures of sparse linear regressions, robust sparse linear regression, tensor PCA, and universality for learning sparse mixtures.

New reduction techniques introduced include: **rejection kernels**, **dense Bernoulli rotations**, **design matrices and tensors**, and a convergence result between **Wishart and inverse Wishart matrices**.

## Key Contributions

- **Secret Leakage PC (PC_ρ) framework**: Generalizes planted clique by sampling the clique vertex set S from distribution ρ over k-subsets of [n] rather than uniformly. Introduces the PC_ρ conjecture (Conjecture 2.2) with a tail-bound condition on the overlap distribution p_ρ(s).
- **Specific hardness assumptions**: k-PC, BPC (bipartite PC), k-BPC, k-HPC^s (k-partite hypergraph PC) — each with its own conjecture and threshold (Conjecture 2.3). k-HPC^s is the strongest and implies the others.
- **First evidence for Statistical-Computational gap universality**: First reduction-based evidence supporting statistical-computational gaps across a broad range of published gaps simultaneously [Li17, BDLS17, CX16, HWX15, BBH18, FLWY18, LSLC18, RM14, HSS15, WEAM19, ASW13, VAC17].
- **Tight lower bounds for**:
  - **Robust Sparse Mean Estimation (RSME)**: k-to-k² gap (Theorem 3.1, via k-BPC conjecture)
  - **Dense Stochastic Block Models (SBM)**: Kesten-Stigum threshold characterization (Theorem 3.2)
  - **Hidden Partition Models (GHPM, BHPM)**: Computational lower bounds at all signal levels (Theorem 3.3)
  - **Semirandom Planted Dense Subgraph (SEMI-CR)**: Recovery threshold (Theorem 3.4)
  - **Negatively Correlated Sparse PCA (NEG-SPCA)**: k-to-k² gap (Theorem 3.5)
  - **Tensor PCA**: Matching computational lower bounds
  - **Universality for learning sparse mixtures**
- **New reduction techniques**:
  - **Rejection kernels**: Preprocessing step mapping PC_ρ to structured target problems
  - **Dense Bernoulli rotations** with design matrices/tensors: Map planted bits to spiked Gaussian tensors; enable reductions to problems with continuous Gaussian observations
  - **Wishart/inverse Wishart convergence**: Novel random matrix theory result enabling NEG-SPCA reduction
  - **Symmetric 3-ary rejection kernels**: For tensor completion from hypergraph structure
- **Low-degree polynomial lower bounds**: Shows low-degree polynomials fail to solve PC_ρ subject to the tail condition of Conjecture 2.2 (Section 12.2)
- **Statistical query lower bounds**: Shows SQ algorithms fail to solve PC_ρ for specific ρ related to hardness assumptions (Section 12.3)

## Key Definitions / Theorems

**Secret Leakage PC_ρ (Definition 2.1)**: Given distribution ρ on k-subsets of [n], let G_ρ(n,k,1/2) be the distribution on n-vertex graphs sampled by first sampling G ~ G(n,1/2) and S ~ ρ independently and then planting a k-clique on vertex set S. PC_ρ(n,k,1/2) is the hypothesis testing problem H₀: G ~ G(n,1/2) vs. H₁: G ~ G_ρ(n,k,1/2).

**PC_ρ Conjecture (Conjecture 2.2)**: Let ρ have overlap probability p_ρ(s) satisfying tail bounds `p_ρ(s) ≤ p₀ · {2^{-2s²} if 1 ≤ s² < d; s^{-2d-1} if s² ≥ d}` for d = O_n((log n)^{1+δ}). Then no poly-time algorithm solves PC_ρ(n,k,1/2).

**Specific Hardness Assumptions (Conjecture 2.3)**: 
1. k-PC(n,k,1/2) when k = o(√n)
2. BPC(m,n,k_m,k_n,1/2) when k_n = o(√n) and k_m = o(√m)
3. k-BPC(m,n,k_m,k_n,1/2) when k_n = o(√n) and k_m = o(√m)
4. k-HPC^s(n,k,1/2) for s ≥ 3 when k = o(√n)

**Computational lower bound definition**: A computational lower bound at constraint C means: for any sequence of parameters satisfying C, there is another sequence of parameters satisfying C such that the problem cannot be solved in poly(n) time.

**Total variation reduction**: Reductions are established in total variation — mapping one distribution to another within ε total variation, so that a hypothesis test distinguishing the target implies a test distinguishing the source.

**RSME Theorem (Theorem 3.1)**: If k, d, n are polynomial in each other with k < d < 1/2 and (n, ε^{-1}) satisfies condition (T), then the k-BPC conjecture implies a computational lower bound for RSME(n, k, d, τ, ε) at all sample complexities n = Θ̃(k²τ^{-2}/ε²).

**SBM Theorem (Theorem 3.2)**: k-PC conjecture implies a computational lower bound for ISBM at the Kesten-Stigum threshold `(p-q)²/q(1-q) = δ̃(k²/n)`.

## Connections

- [Planted Clique](../concepts/planted-clique.md)
- [Secret Leakage Planted Clique](../concepts/secret-leakage-planted-clique.md)
- [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md)
- [Average-Case Reductions](../concepts/average-case-reductions.md)
- [Statistical Query Model](../concepts/statistical-query-model.md)
- [Matthew Brennan](../entities/matthew-brennan.md)
- [Guy Bresler](../entities/guy-bresler.md)

## Open Questions / Limitations

- Is planted clique (PC) the right starting point for average-case reductions? The authors suggest PC_ρ and k-HPC^s may be better starting points.
- The PC_ρ conjecture is new and less established than the PC conjecture — its failure for some ρ would undermine the reductions.
- Extending the framework to handle estimation and recovery problems more generally (beyond detection).
- Connecting PC_ρ hardness to other complexity assumptions (LWE, random CSPs, etc.).
- Several problems have detection-recovery gaps that remain unexplained by these reductions (e.g., PDS Recovery Conjecture was confirmed for semirandom but not general PDS).
- No reductions currently bridge planted clique and problems with *different* natural distributions (non-Gaussian, non-Bernoulli).

## Quotes / Notable Passages

> "The insight in this work is that a slight generalization of the planted clique conjecture — the secret leakage planted clique (PC_ρ) — gives rise to a variety of new average-case reduction techniques, yielding a web of reductions relating statistical problems with very different structure."

> "An expanded set of hardness assumptions, such as PC_ρ, may be a key first step towards a more complete theory of reductions among statistical problems."

> "These techniques map to problems breaking out of the sparse submatrix plus noise structure that seemed to constrain prior reductions. They thus show that revealing a tiny amount of information about the hidden clique vertices substantially increases the reach of the reductions approach."
