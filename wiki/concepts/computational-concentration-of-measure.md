---
title: Computational Concentration of Measure
type: concept
tags: [concentration-of-measure, computational-complexity, adversarial-ml, evasion-attacks, complexity-theory]
---

## Definition

Computational Concentration of Measure [MM19] is a strengthening of classical [concentration of measure](concentration-of-measure.md) that additionally requires the concentration to be witnessed by an *efficient algorithm*. Formally: a metric probability space (X, d, μ) satisfies computational (ε, δ)-concentration if there is a polynomial-time algorithm that, given a sample from A (a set with μ(A) ≥ c) and a fresh sample x from μ, finds a point x' ∈ A_ε close to x with probability at least δ.

Equivalently: the sub-linear neighborhood structure of A around a typical point is efficiently *computable*, not merely existent.

## Intuition

Classical concentration of measure shows that for information-theoretic adversaries, adversarial examples exist. Computational concentration of measure shows that polynomial-time adversaries can *find* those adversarial examples. The distinction matters: existential proofs may rely on non-constructive arguments (e.g., the probabilistic method), but computational concentration requires the adversary's search to be efficient.

## Properties / Theorems

**Sufficiency for polynomial-time evasion** [MM19]: Computational concentration of measure for a metric probability space is *sufficient* to construct polynomial-time evasion attacks with sub-linear perturbation budget, given black-box access to the classifier.

**Optimality** [EMM20]: Closed the gap between algorithmic attacks of [MM19] and existential attacks of [MDM19]. The best information-theoretic lower bounds and best computational lower bounds are *equal* for product distributions under Hamming distance. In other words: polynomial-time adversaries are as powerful as information-theoretic adversaries on product distributions.

**Extension across metric spaces** [EMM20]: Special embeddings that preserve computational concentration allow lifting from product distributions to other metric spaces.

**Barrier result**: Computational concentration of measure on product distributions shows that cryptographic hardness assumptions *cannot* generically help robustness against polynomial-time adversaries in those settings — the polynomial-time adversary already achieves the information-theoretic optimum.

**Positive separation** [GJMM20]: Nevertheless, there exist learning problems where computational robustness *exceeds* information-theoretic robustness — i.e., computationally bounded adversaries are provably weaker than information-theoretic adversaries. This is possible because computational concentration is a sufficient but not necessary condition for efficient attacks.

## Where It Appears

- [A Complexity Theoretic Approach to Adversarial ML](../sources/complexity-theoretic-adversarial-ml.md) — introduced and developed here
- [Computational Concentration of Measure (EMM20)](../sources/computational-concentration-of-measure-etesami.md) — full paper with MUCIO algorithm and optimal bounds for all non-negligible ε
- [Adversarial Examples from Computational Constraints (BLPR19)](../sources/adversarial-examples-computational-constraints.md) — complementary direction: shows crypto hardness can *force* computational vulnerability even when IT robustness holds

## Related Concepts

- [Concentration of Measure](concentration-of-measure.md) — the information-theoretic precursor
- [Evasion Attacks](evasion-attacks.md)
- [Poisoning Attacks](poisoning-attacks.md) — computational concentration also implies optimal polynomial-time poisoning attacks

## Open Questions

- Does computational concentration hold for non-product distributions that are practically relevant (e.g., natural image distributions)?
- What is the right characterization of metric probability spaces where computational hardness *can* help robustness?
