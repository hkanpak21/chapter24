---
title: Isoperimetry and Adversarial Robustness
type: concept
tags: [concentration-of-measure, isoperimetry, adversarial-ml, evasion-attacks, geometry]
---

## Definition

**Isoperimetric inequalities** characterize the minimum boundary / b-expansion of sets of given measure in a metric probability space. The **Gaussian isoperimetric inequality** states that half-spaces minimize boundary measure among sets of measure 1/2 in (ℝ^n, ‖·‖₂, γ_n). Analogues exist for spheres, hypercubes (Harper's theorem), and Lévy families.

In adversarial ML, isoperimetry gives the sharp constant in the concentration bound: the adversarial risk of any classifier whose error region has measure ≥ ε is at least (1 − boundary_measure(b-expansion of worst set of measure ε)).

## Intuition

Isoperimetry says: in high dimensions, every "large" set is "close to" a large fraction of the space. This is exactly the statement that adversarial perturbations are geometrically unavoidable for classifiers with nontrivial error. Different metric spaces give different isoperimetric profiles — and hence different quantitative robustness bounds.

## Properties / Theorems

**Gaussian isoperimetry (Borell 1975, Sudakov-Tsirelson 1974)**: Used in [Fawzi-Fawzi-Fawzi 2018](../sources/adversarial-vulnerability-any-classifier.md) to bound robustness under smooth generative models.

**Spherical isoperimetry (Lévy-Schmidt)**: Used in [Gilmer et al. 2018] for sphere-based adversarial example existence.

**Hamming cube isoperimetry (Harper's theorem; Talagrand)**: Used in [Diochnos-Mahloujifar-Mahmoody 2018] and Lemma 2.5 of [MDM19](../sources/curse-of-concentration.md) for Boolean hypercube attacks.

**Concentration without isoperimetry** [MDM19]: The "curse of concentration" theorem works from concentration alone (without sharp isoperimetric inequalities), yielding slightly weaker constants but far broader applicability across metric measure spaces. This is a key conceptual advance: isoperimetry is sufficient but not necessary.

**Computational isoperimetry** [EMM20]: Algorithmic / polynomial-time version — given a set S with Pr[S] ≥ ε, find a close point in S from a random sample efficiently. Matches the information-theoretic isoperimetric bound on product spaces via the MUCIO algorithm.

## Where It Appears

- [Fawzi et al. 2018](../sources/adversarial-vulnerability-any-classifier.md) — Gaussian isoperimetry as core tool
- [Curse of Concentration (MDM19)](../sources/curse-of-concentration.md) — generalizes beyond isoperimetry
- [Computational Concentration (EMM20)](../sources/computational-concentration-of-measure-etesami.md) — algorithmic version
- [Universal Law of Robustness](../sources/universal-law-of-robustness.md) — uses Gaussian isoperimetry in a different way (parameter counting)

## Related Concepts

- [Concentration of Measure](concentration-of-measure.md)
- [Computational Concentration of Measure](computational-concentration-of-measure.md)
- [Evasion Attacks](evasion-attacks.md)
- [Universal Law of Robustness](universal-law-of-robustness.md)

## Open Questions

- Sharp isoperimetric inequalities for "natural" image manifolds are unknown; without them, robustness bounds on realistic data are loose.
- Are there natural metric probability spaces where concentration holds but isoperimetry fails (giving stronger concentration but weaker attack constants)?
