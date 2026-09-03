---
title: "Detection-Recovery and Detection-Refutation Gaps via Reductions from Planted Clique"
type: source
date_ingested: 2026-04-12
authors: [Guy Bresler, Tianze Jiang]
venue: "COLT 2023"
venue_evidence: "https://proceedings.mlr.press/v195/bresler23a/bresler23a.pdf; Proceedings of Machine Learning Research vol 195, 36th Annual Conference on Learning Theory, pages 5850-5889; also stated in the ingested PDF"
year: 2023
tags: [statistical-computational-gaps, average-case-reductions, planted-clique, hardness-reductions, complexity-theory]
claim_quantifier: conditional
antecedent: "a slight variation of the planted clique hypothesis with secret leakage, introduced by Brennan and Bresler. Conjectured."
algorithm_class: "all poly-time conditionally"
date_verified: 2026-08-20
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: time
cls_tightness: poly
cls_baseline: n/a
cls_second_party: none
cls_assessed: explicit
cls_evidence: "For any sequence of (randomized) polynomial-time algorithm φn : GNn → [N ]Kn , φn cannot achieve asymptotic exact recovery on PDS(Nn , Kn , pn , qn ) assuming k-PC."
cls_evidence_src: Cor 11
cls_reason: "party=learner not attacker: no adversary or security game, only a poly-time algorithm attempting statistical recovery; classified on the lead recovery claim over the co-equal refutation claim (rule 1); target/family/phase/access/write are none/none/n/a/none/none since no ML system or attack scenario is present."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper extends the Brennan-Bresler framework to prove **detection-recovery gaps** and **detection-refutation gaps** for the Planted Dense Subgraph (PDS) problem, using secret leakage planted clique (PC_ρ) reductions. The key insight: different computational *tasks* on the same statistical model can have different computational thresholds. Detection may be easy while recovery is hard; detection may be feasible while refutation (certifying that no planted subgraph exists) is harder still.

This directly addresses one of the main open questions from Brennan & Bresler (2020): can PC_ρ reductions explain gaps beyond detection, specifically for recovery and refutation?

## Claim Boundary

- **Quantified over:** polynomial-time algorithms for planted dense subgraph recovery and for refutation, conditional on the source assumption.
- **Antecedent:** a slight variation of the planted clique hypothesis with secret leakage, introduced by Brennan and Bresler. Conjectured.
- **Algorithm class:** all polynomial time, conditionally. Prior evidence for the same detection-recovery gap was obtained against low-degree polynomials by Schramm and Wein and against MCMC by Ben Arous et al., and those are restricted-class results that this paper's conditional statement is stronger than but does not subsume.
- **Does not establish:** an unconditional separation of the three tasks. It establishes that one conjecture implies the separation.
- **Abstract vs theorem:** none found.

## Key Contributions

- **Detection-recovery gap for PDS**: PC_ρ conjecture implies a parameter regime where PDS is computationally detectable (efficiently solvable) but computationally hard to *recover* (finding the planted subgraph given that one exists).
- **Detection-refutation gap for PDS**: Sharp lower bounds for refutation — certifying that a graph has no planted dense subgraph — showing refutation is strictly harder than detection.
- **Extension of the reduction framework**: New average-case reduction techniques mapping PC_ρ to PDS recovery and refutation tasks, expanding the Brennan-Bresler toolkit beyond detection.
- **Hardness of three tasks simultaneously**: A single underlying assumption (PC_ρ) now implies hardness for three distinct tasks — evidence that the framework captures a fundamental structural barrier.

## Key Definitions / Theorems

**Planted Dense Subgraph (PDS)**: Given a graph G on n vertices with edge probability q, the PDS problem is to detect (or recover) a planted subgraph on k vertices with edge probability p > q.

**Detection-recovery gap**: A parameter regime (k, n, p, q) where (1) a poly-time algorithm detects PDS and (2) no poly-time algorithm can recover the planted subgraph vertices above the statistical estimation threshold.

**Detection-refutation gap**: A parameter regime where (1) a poly-time algorithm detects PDS and (2) no poly-time algorithm can *certify* (refute) the absence of a planted subgraph.

**Main theorem (informal)**: Assuming the PC_ρ conjecture for appropriate ρ: (1) there is a sharp detection-recovery gap for PDS at the Kesten-Stigum threshold, and (2) refutation requires strictly more computational effort than detection.

## Connections

- [Reducibility and Statistical-Computational Gaps from Secret Leakage](reducibility-statistical-computational-gaps.md) — directly extends this work
- [Secret Leakage Planted Clique](../concepts/secret-leakage-planted-clique.md) — the hardness assumption used
- [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md)
- [Average-Case Reductions](../concepts/average-case-reductions.md)
- [Guy Bresler](../entities/guy-bresler.md) — extending his own prior work

## Open Questions / Limitations

- Do detection-recovery and detection-refutation gaps hold for other problems beyond PDS? (SBM, sparse PCA, etc.)
- Is there a unified theory of when all three gaps (detection, recovery, refutation) are at different computational thresholds?
- Can the refutation lower bounds be strengthened to cover sum-of-squares lower bounds?

## Quotes / Notable Passages

_Verbatim, verified against `raw/BJ23_DetectionRecoveryGaps.pdf` on 2026-08-20._

> "In this paper we demonstrate that a slight variation of the Planted Clique Hypothesis with secret leakage (introduced in Brennan and Bresler (2020)), implies a detection-recovery gap for PDS. In the same vein, we also obtain a sharp lower bound for refutation, yielding a detection-refutation gap."
