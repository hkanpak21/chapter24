---
title: "Computational Complexity of Statistics: New Insights from Low-Degree Polynomials"
type: source
date_ingested: 2026-04-12
authors: [Alexander S. Wein]
venue: "Survey. The ingested PDF is arXiv:2506.10748v1, 12 Jun 2025, and does not state a venue."
year: 2025
tags: [statistical-computational-gaps, complexity-theory, low-degree-polynomials, statistical-query, hardness-reductions, planted-clique]
claim_quantifier: conditional
antecedent: "the low-degree conjecture of Hopkins, which is what converts a degree bound into a runtime prediction. The survey itself records that this conjecture was refuted. See the Limits section."
algorithm_class: "low-degree"
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
cls_assessed: explicit
cls_evidence: "this framework measures the complexity of a statistical task by the minimum degree that a polynomial function must have in order to solve it"
cls_evidence_src: abstract
cls_reason: "Survey of the low-degree framework with no ML attack scenario; the bounded party is the estimator restricted to low-degree polynomials, so party=learner, unit=algo class, tightness=class, matching what-can-we-learn-privately. Did not rely on the page's flagged 'robust subspace recovery' item (unverified, arXiv:2603.02594 postdates a June 2025 survey and is not in the PDF); verified the fields used here directly against raw/W25_LowDegreeSurvey.pdf. RECODE 2026-09-03 (R4, no adversary means no phase): phase train time -> n/a."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

A 50-page survey by Alexander Wein on the low-degree polynomial framework for understanding statistical-computational tradeoffs. The survey covers: (1) the low-degree conjecture and its evidence base; (2) applications to detection, recovery, and estimation problems; (3) formal connections to the SQ model and the SOS hierarchy; (4) known counterexamples and limitations; (5) open problems. As of June 2025 this is the authoritative survey of the low-degree framework.

The key thesis: low-degree polynomials predict computational thresholds for "structureless" planted problems, but fail for problems with algebraic structure (lattice methods, anti-concentration algorithms). The framework is best understood as evidence for hardness of a specific class of problems, not a universal theory of computational complexity.

## Claim Boundary

- **Quantified over:** the survey collects results about degree-D polynomial algorithms across detection, recovery and estimation. Each individual lower bound quantifies over polynomials of a stated degree for a stated model, never over algorithms in general.
- **Antecedent:** the low-degree conjecture of Hopkins, which is the step that turns a degree bound into a runtime prediction. The survey records that this conjecture has been refuted. See the Limits section.
- **Algorithm class:** low-degree. The correspondences the survey draws with SQ and with sum-of-squares are separate results carrying their own regularity conditions, and those three classes are not interchangeable.
- **Does not establish:** that any problem is hard for polynomial time. One of the survey's four stated goals is to discuss the extent to which low-degree lower bounds should be treated as evidence for inherent computational hardness, which is an open interpretive question rather than a settled one.
- **Abstract vs theorem:** none found. The abstract describes the framework as predicting and explaining apparent statistical-computational tradeoffs.

## Key Contributions (of the framework, as surveyed)

- **Low-degree likelihood ratio (LDLR)**: For hypothesis testing H₀ vs H₁, the degree-D likelihood ratio L^{≤D} = E_{H₁}[f(x)] / E_{H₀}[f(x)] measures "low-degree distinguishability." The conjecture: if ‖L^{≤D}‖ = O(1) for D = Ω(log n), no poly-time algorithm solves the testing problem.
- **SQ ≈ Low-degree equivalence** (Brennan, Bresler, Hopkins, Li, Schramm, COLT 2021): Under mild conditions, the SQ complexity and low-degree complexity of hypothesis testing problems are essentially equivalent. This is a formal theorem (not just a conjecture).
- **Extension to estimation and recovery**: Low-degree lower bounds now exist for estimation (low-degree MMSE) and optimization, not just hypothesis testing.
- **Applications**: Community detection, sparse PCA, spiked tensor models, planted clique, random CSPs, robust sparse mean estimation — tight thresholds via low-degree framework.

## Known Counterexamples (crucial for our research)

1. **Zadik, Song, Wein, Bruna (COLT 2022)**: Lattice-based algorithms for clustering Gaussian mixtures with degenerate covariance succeed above the low-degree threshold. Low-degree polynomials fail to predict the correct computational threshold when algebraic structure (lattice rounding) is exploitable. *This is the most important known counterexample.*

2. **Robust subspace recovery**: reported as polynomial-time solvable while the low-degree method fails even up to degree n^{Ω(1)}, because the algorithm exploits anti-concentration properties invisible to low-degree polynomials. _Unverified, flagged 2026-08-20. This item is not in the surveyed paper. The string "subspace recovery" does not occur in `raw/W25_LowDegreeSurvey.pdf`, and the identifier an earlier ingest attached to it, arXiv:2603.02594, is dated after the survey and does not occur in it either. Do not carry this item or its identifier into the survey until a primary source is opened._

3. **Holmgren and Wein (ITCS 2021)**: Refuted the original formulation of the low-degree conjecture but noted a simple modification avoids their construction. See [Counterexamples to the Low-Degree Conjecture](holmgren-counterexamples-low-degree.md).

4. **Buhai, Hsieh, Jain and Kothari**: the survey itself records that the conjecture of Hopkins was refuted outright. See the Limits section below.

**Emerging consensus**: The low-degree framework accurately predicts hardness for problems without hidden algebraic or anti-concentration structure — "structureless" problems. It fails when efficient algorithms can exploit algebraic structure (lattices, finite fields, anti-concentration).

## Key Definitions / Theorems

**Low-degree conjecture (informal)**: For natural hypothesis testing problems, no polynomial-time algorithm distinguishes H₀ from H₁ below the threshold where degree-O(log n) polynomials can distinguish them.

**Low-degree complexity of a problem**: The minimum degree D such that ‖L^{≤D}‖² = ω(1), where L^{≤D} is the low-degree likelihood ratio.

**SQ-LD equivalence theorem** (Brennan et al. 2021): For hypothesis testing problems satisfying mild regularity conditions, the minimum SQ complexity m_SQ and the low-degree complexity D satisfy: D = Θ(log(m_SQ)).

**Low-degree MMSE** (Schramm and Wein, Ann. Statist. 2022): For estimation problems, the performance of the best degree-D polynomial estimator provides a lower bound on the performance of any polynomial-time estimator. Extends the framework from detection to recovery.

## Limits

The survey states that the conjecture of Hopkins was refuted, and names the paper that did it. Verbatim, verified against `raw/W25_LowDegreeSurvey.pdf` on 2026-08-20:

> "The conjecture of Hopkins stood for about 7 years — aside from a refinement of [HW21] mentioned below — and then very recently was refuted by [BHJK25]."

The two papers that bound what a low-degree statement can now be read to mean:

- [The Quasi-Polynomial Low-Degree Conjecture is False](quasi-poly-low-degree-conjecture-false.md), Buhai, Hsieh, Jain and Kothari, FOCS 2025. It disproves the quasi-polynomial form of the conjecture in the regime where that form was stated. A low-degree-bounded adversary and a quasi-polynomial-time-bounded adversary are therefore provably different objects. Two clauses attach. The polynomial-time distinguisher is for the rectangular generalisation; in the square symmetric regime the distinguisher is n^{O(log^{1/(k−1)} n)} and improving it is open. The second construction, from the largest eigenvalue, has a non-product null distribution and so does not bear on the conjecture at all.
- [Rigorous Implications of the Low-Degree Heuristic](rigorous-implications-low-degree.md), Hsieh, Kane, Kothari, Li, Mohanty and Tiegel, STOC 2026. This is the positive counterpart. Every one of its three results is stated about a **noisy** version of the problem rather than the problem itself. Permutation invariance is required for two of the three; the Gaussian symmetric-polynomial result does not need it, because the test class already supplies the symmetry. None of the three rules out all polynomial-time algorithms.

Any claim in this wiki that rests on a low-degree bound must cite both, with these clauses.

## Connections

- [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md) — low-degree framework is a primary tool for evidencing gaps
- [Statistical Query Model](../concepts/statistical-query-model.md) — formally equivalent to low-degree under mild conditions
- [Planted Clique](../concepts/planted-clique.md) — primary test case for the framework
- [Secret Leakage Planted Clique](../concepts/secret-leakage-planted-clique.md) — low-degree lower bounds for PC_ρ support the Brennan-Bresler conjecture
- [Average-Case Reductions](../concepts/average-case-reductions.md)
- [Alexander Wein](../entities/alexander-wein.md)

## Open Questions

- Precisely characterize the class of problems for which the low-degree conjecture holds — what structural property separates "structureless" from "algebraically structured"?
- Can the low-degree framework be extended to handle algebraic structure by enriching the polynomial class (e.g., polynomials over finite fields)?
- Does low-degree hardness imply actual computational hardness for any natural problem (would be a formal theorem, not just a conjecture)?
- Connection to circuit complexity: do low-degree lower bounds imply AC⁰ or TC⁰ lower bounds?

## Quotes / Notable Passages

_Verbatim, verified against `raw/W25_LowDegreeSurvey.pdf` on 2026-08-20._

> "discuss some philosophical questions surrounding the interpretation of low-degree lower bounds, and notably the extent to which they should be treated as evidence for inherent computational hardness"
