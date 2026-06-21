---
title: Statistical Query Model
type: concept
tags: [statistical-query, learning-theory, complexity-theory, statistical-computational-gaps]
---

## Definition

The **Statistical Query (SQ) model** [Kearns 1993] is a restricted computational model for learning in which an algorithm cannot access individual examples. Instead, the algorithm may only query statistical properties of the distribution: for a query function q(x,y), the oracle returns an approximation to E[q(x,y)] ± τ for some tolerance τ.

**Equivalently**: SQ algorithms cannot distinguish individual examples — they can only access expectations over the distribution. This rules out algorithms that exploit correlations across samples in a fine-grained way.

## Intuition

SQ is a natural restriction that captures many algorithmic techniques: gradient descent, EM, spectral methods, and most known efficient learning algorithms. When a problem has an SQ lower bound, it means the entire class of "tolerant" algorithms fails, providing strong evidence for computational hardness.

SQ lower bounds are particularly useful for statistical inference problems because the SQ model is closely tied to the structure of high-dimensional distributions.

## Properties / Theorems

**SQ lower bound methodology**: To show a problem is hard for SQ algorithms, one shows that the "statistical dimension" (or SQ dimension) of the problem is large. This is related to the pairwise correlations between different "planted" hypotheses.

**Planted Clique SQ lower bounds** [FGR+13]: Statistical query algorithms fail to solve PC(n,k,1/2) for k = o(√n). This matches the conjectured computational threshold.

**PC_ρ SQ lower bounds** [Brennan & Bresler, Section 12.3]: SQ lower bounds hold for specific ρ related to the hardness assumptions used in the reductions — supporting the PC_ρ conjecture.

**Low-degree polynomial relationship**: SQ lower bounds and low-degree polynomial lower bounds are closely related — both capture the "signal complexity" of hypothesis testing problems. Low-degree polynomials provide finer-grained evidence but SQ lower bounds have more established theoretical foundations.

**SQ vs. poly-time**: SQ lower bounds do not directly imply polynomial-time hardness (SQ is not known to be equivalent to poly-time), but they provide the strongest available computational evidence for many problems.

## Where It Appears

- [Reducibility and Statistical-Computational Gaps](../sources/reducibility-statistical-computational-gaps.md) — SQ lower bounds for PC_ρ supporting the conjecture
- [Feldman et al. Statistical Algorithms](../sources/feldman-statistical-algorithms-planted-clique.md) — foundational SQ lower bound for planted clique; statistical dimension framework
- [Brennan SQ-LowDegree Equivalence](../sources/brennan-sq-lowdegree-equivalence.md) — formal SQ ↔ LD equivalence under nicenness
- [Bruna Continuous LWE](../sources/bruna-continuous-lwe.md) — SQ lower bounds for hCLWE matching lattice hardness
- [A Complexity Theoretic Approach to Adversarial ML](../sources/complexity-theoretic-adversarial-ml.md) — SQ model is implicitly relevant to the class of algorithms that face adversarial robustness lower bounds

## Related Concepts

- [Statistical-Computational Gaps](statistical-computational-gaps.md)
- [Planted Clique](planted-clique.md)
- [Secret Leakage Planted Clique](secret-leakage-planted-clique.md)
- [Average-Case Reductions](average-case-reductions.md)

## Open Questions

- Is there a problem with an SQ lower bound that has a poly-time algorithm? (Would separate SQ from poly-time)
- Can SQ lower bounds be established for all problems with conjectured statistical-computational gaps?
- How does the SQ model interact with adversarial robustness? (An SQ-hard learning problem might still be learnable if the adversary is restricted)
