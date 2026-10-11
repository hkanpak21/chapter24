---
title: A Nearly Tight Sum-of-Squares Lower Bound for the Planted Clique Problem
type: source
date_ingested: 2026-04-12
authors: [Boaz Barak, Samuel B. Hopkins, Jonathan Kelner, Pravesh K. Kothari, Ankur Moitra, Aaron Potechin]
venue: "FOCS 2016"
venue_evidence: "https://arxiv.org/abs/1604.03084; Proceedings of the 57th Annual IEEE Symposium on Foundations of Computer Science (FOCS 2016), pages 428-437"
year: 2016
tags: [planted-clique, sum-of-squares, lower-bounds, statistical-computational-gaps, pseudo-calibration]
claim_quantifier: universal
antecedent: "none. The integrality gap is unconditional."
algorithm_class: "SoS"
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
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "There is an absolute constant c so that for every d = d(n) and large enough n, the SoS relaxation of the planted clique problem has integrality gap at least n1/2−c(d/ log n)1/2 ."
cls_evidence_src: Thm 1.1
cls_reason: "party=auditor over learner: the theorem is stated as a certification/refutation failure -- 'the task of certifying that there is no ω-sized clique in a random G(n,1/2) graph' (verified in the PDF, §1) -- so the bounded party is whoever attempts to CERTIFY the absence of a clique, matching rule 6's auditor convention for a verification/refutation role, and matching the party used on rigorous-implications-low-degree, the corpus's other refutation-hardness page. unit=algo class and tightness=class because the bound is restricted to the degree-d SoS proof system specifically (front matter: 'SoS, SQ and low-degree are distinct classes, and a bound against one is not a bound against the others'), not a running-time bound on general algorithms -- the paper is explicit it says nothing about non-SoS polynomial-time algorithms. target/family=none and phase=n/a: no ML asset or attack scenario is present, matching the corpus's convention for pure statistical-computational-gap papers not framed around a learning task. RECODE 2026-09-03 (R3, solver is the learner): party auditor -> learner."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper proves a nearly tight Sum-of-Squares (SoS) lower bound for the planted clique problem: with high probability over a random graph G ~ G(n,1/2), the degree-d SoS relaxation of the clique problem has value at least n^{1/2 - c(d/log n)^{1/2}} for any d = o(log n). This means SoS cannot certify the absence of a clique of size n^{1/2 - o(1)} even at poly-logarithmic degree, matching the conjectured computational threshold up to the log factor. Prior best results (MPW15, DM15, HKP15) handled d ≤ 4 or weaker bounds; this work achieves near-tightness for all d up to log n.

The key technical contribution is a new framework called **pseudo-calibration** for constructing pseudo-distributions. Pseudo-calibration takes a "computational Bayesian" perspective: the pseudo-expectation is designed to be indistinguishable from a true Bayesian posterior to any low-degree test of the graph. This yields a principled, "forced" choice for the pseudo-distribution that automatically satisfies weak global constraints — the constraints that had stymied prior PC lower bounds (vs. local constraints in 3SAT/3XOR).

## Claim Boundary

- **Quantified over:** the degree-d sum-of-squares semidefinite programming relaxation of the clique problem, with high probability over G drawn from the Erdos-Renyi distribution G(n, 1/2), for every d.
- **Antecedent:** none. The integrality gap is unconditional.
- **Algorithm class:** SoS. The bound is on the value of one semidefinite programming hierarchy. SoS, SQ and low-degree are distinct classes, and a bound against one is not a bound against the others.
- **Does not establish:** that planted clique is hard for polynomial time, and does not rule out polynomial-time algorithms that are not sum-of-squares relaxations. It is silent on the positive side, giving no sum-of-squares upper bound.
- **Abstract vs theorem:** none found. The abstract states the integrality gap and the pseudo-calibration framework and claims nothing about general algorithms.

## Key Contributions

- Nearly tight SoS integrality gap: n^{1/2 - o(1)} for degree d = o(log n), proving SoS cannot improve on the √n barrier.
- Introduction of the **pseudo-calibration** framework — a general recipe for constructing SoS pseudo-distributions for planted problems.
- Conceptual "computational Bayesian" lens on SoS lower bounds, yielding insights on when/why SoS is more powerful than LS+ hierarchies.
- Rules out SoS-based algorithms for the decision variant of PC; also some SoS-based search algorithms.

## Key Definitions / Theorems

- **Pseudo-calibration condition**: E_{G ~ G(n,1/2)} [Ẽ_G f_G] = E_{(G,x) ~ G(n,1/2,ω)}[f(G,x)] for all low-degree f.
- **Main Theorem (1.1)**: For every d=d(n), with high probability the SoS relaxation of PC has integrality gap at least n^{1/2 - c(d/log n)^{1/2}}.
- Distinction between **weak global constraints** (PC) and **strong local constraints** (3SAT/3XOR) as the key structural difference.

## Connections

- [Planted Clique](../concepts/planted-clique.md) — flagship hardness target
- [Sum-of-Squares Hierarchy](../concepts/sum-of-squares-hierarchy.md) — framework lower-bounded
- [Pseudo-Calibration](../concepts/pseudo-calibration.md) — introduced here
- [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md) — SoS/LD connection via pseudo-calibration
- [Boaz Barak](../entities/boaz-barak.md), [Samuel Hopkins](../entities/samuel-hopkins.md), [Pravesh Kothari](../entities/pravesh-kothari.md), [Ankur Moitra](../entities/ankur-moitra.md)

## Open Questions / Limitations

- The bound is n^{1/2 - o(1)} rather than exactly n^{1/2}; closing this gap remains open.
- Does not rule out SoS upper bounds (algorithms) below √n — silent on the positive side.
- Refutation vs. decision vs. search distinction: result is stated for refutation; decision follows, search partially.

## Quotes / Notable Passages

> "Our Sum-of-Squares lower bound amounts to coming up with some reasonable "pseudoexpectation" that can be efficiently computed, where Ẽ_G is meant to capture a "best effort" of a computationally bounded party of approximating the Bayesian conditional expectation" of x given G.

_Verbatim, verified against `raw/BHKKMP19_SOSLowerBoundPC.pdf` on 2026-08-20. An earlier rendering elided the subject of the clause and hyphenated the paper's `pseudoexpectation`. The trailing conditional expectation is written in the paper as a symbol that `pdftotext` flattens, so it is given here in words._

> "Lower bounds for the planted clique problem boil down to handling weak global constraints as opposed to strong local ones."
