---
title: Average-Case Reductions
type: concept
tags: [average-case-reductions, statistical-computational-gaps, hardness-reductions, complexity-theory]
---

## Definition

An **average-case reduction** from problem P to problem P' shows that if there is a polynomial-time algorithm solving P', then there is a polynomial-time algorithm solving P. In the context of statistical inference, a reduction maps a distribution D_P (the "hard" source) to distribution D_{P'} (the target), such that:
- If an algorithm A solves P', then the composed algorithm (reduce + A) solves P
- The reduction runs in polynomial time
- Reductions are typically established via total variation: the reduction maps D_P within ε total variation of D_{P'}

Unlike worst-case reductions (NP-hardness), average-case reductions are harder to construct because they must:
1. Map one *distribution* to another faithfully
2. Preserve the *statistical parameters* of both problems
3. Be *information-preserving* (not degrade the signal level)
4. Show *strong lower bounds* by filling out all growth rates in the constraint set

## Intuition

In worst-case complexity, reducing 3-SAT to another NP problem only requires mapping individual instances. Average-case reductions must map *distributions* — they must faithfully replicate the natural distribution of the target problem, including all correlations and parameter regimes. This is far more constrained.

The key challenge: problems with different underlying structure (e.g., Gaussian vs. Bernoulli, graph vs. matrix) have very different distributional geometry. Prior reductions were stuck within the "sparse submatrix + noise" family because they had no mechanism to transform across structures.

## Properties / Theorems

**Desiderata for average-case reductions** [Brennan & Bresler]:
1. **Aesthetics**: If P and P' have canonical distributions, the reduction must faithfully map these. No mismatch in distributional form.
2. **Mapping between natural distributions**: The reduction must map between possibly very differently structured natural distributions.
3. **Tightness to algorithms**: Should show lower bounds matching the best known algorithms.
4. **Strong lower bounds**: Must fill out all possible growth rates, not just a single parameter sequence.

**Total variation framework**: Reductions in total variation — showing that a reduction outputs a distribution within ε-TV of the target — allow clean composition and imply computational lower bounds. Established in [BBH18] as the right framework for statistical reductions.

**Reduction techniques** [Brennan & Bresler 2020]:
- **Rejection kernels**: Preprocessing that maps the planted clique distribution to the structure needed by the target
- **Dense Bernoulli rotations**: Map planted binary structure to spiked Gaussian tensors via design matrices/tensors
- **Wishart/inverse Wishart convergence**: New random matrix theory enabling reductions to negatively correlated sparse PCA
- **Symmetric 3-ary rejection kernels**: For tensor completion problems

**Prior limitation**: Before [Brennan & Bresler 2020], average-case reductions were essentially limited to problems representable as "sparse submatrix signal + noise matrix" due to structural constraints of reductions starting from standard PC.

## Where It Appears

- [Reducibility and Statistical-Computational Gaps](../sources/reducibility-statistical-computational-gaps.md) — constructs the first broad web of average-case reductions

## Related Concepts

- [Planted Clique](planted-clique.md) — canonical hard problem used as reduction source
- [Secret Leakage Planted Clique](secret-leakage-planted-clique.md) — generalized starting point enabling broader reductions
- [Statistical-Computational Gaps](statistical-computational-gaps.md)
- [Statistical Query Model](statistical-query-model.md) — complementary evidence approach

## Open Questions

- Is there a general theory of when average-case reductions exist between statistical problems?
- Can average-case reductions be automated or systematically searched for?
- What is the right starting problem for reductions — PC, PC_ρ, k-HPC, or something else entirely?
- How do average-case reductions in statistics relate to cryptographic reductions?
