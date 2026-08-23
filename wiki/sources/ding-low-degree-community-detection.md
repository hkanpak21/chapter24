---
title: Low Degree Conjecture Implies Sharp Computational Thresholds in Stochastic Block Model
type: source
date_ingested: 2026-04-12
authors: [Jingqiu Ding, Yiding Hua, Lucas Slot, David Steurer]
venue: Preprint (the ingested PDF is arXiv:2502.15024v2, 28 Apr 2025)
year: 2025
tags: [stochastic-block-model, low-degree-polynomials, kesten-stigum, community-detection, statistical-computational-gaps]
claim_quantifier: conditional
antecedent: "the extended low-degree conjecture as formalized in [MW23], with an added restriction the authors introduce after a refutation attributed in their footnote to Ansh Nagda. Conjectured, and already revised once."
algorithm_class: "low-degree"
date_verified: 2026-08-20
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: time
cls_tightness: conditional
cls_baseline: stated
cls_second_party: none
cls_second_notion: algo class
cls_assessed: explicit
cls_evidence: "no exp 𝑛 0.99 time algorithm can achieve recovery rate 𝑛 −0.49 in the 𝑘-stochastic block model when 𝜀2 𝑑 ⩽ 0.99𝑘 2"
cls_evidence_src: Thm 2.1
cls_reason: "Not an ML-attack paper; used as a reference hardness result, so target/family/phase/access/write are none/n/a. party=learner: the bounded party is a statistical-recovery algorithm, not an attacker/auditor/mechanism in a security sense. tightness=conditional because the time bound holds only assuming the unproven extended low-degree conjecture (front matter antecedent). second_notion=algo class because what is actually proved is a low-degree bound, and the conjecture alone converts it to a time statement (wiki Claim Boundary: \"the conclusion reads as a statement about running time only through the conjecture\"). baseline=stated: the paper compares against the trivial random-partition estimator's vanishing recovery rate."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper sharpens the implications of the (extended) low-degree conjecture for the symmetric stochastic block model (SBM). Assuming the conjecture of Kunisky-Wein-style extended low-degree hardness, the authors prove that no polynomial-time algorithm can achieve **weak recovery** (constant correlation with true community labels) below the **Kesten-Stigum (KS) threshold** ε²d < k². This provides the first rigorous evidence for a sharp transition in the recovery rate for polynomial-time algorithms at the KS threshold.

Concretely, the paper shows (Theorem 2.1) that below KS no exp(n^0.99)-time algorithm achieves recovery rate n^{-0.49} with constant probability, while above KS poly-time weak recovery is known [Mas14, AS15]. Previous work ruled out only hypothesis-testing-style algorithms with success probability 1 - o(1); this paper handles the harder case of constant-probability recovery via a **correlation-preserving projection** technique (from [HS17]) plus graph-splitting and cross-validation.

Results also give computational lower bounds for learning SBM parameters (edge probability matrix and graphon).

## Claim Boundary

- **Quantified over:** algorithms running in time exp(n^{0.99}) for the symmetric stochastic block model below the Kesten-Stigum threshold, and only under the conjecture.
- **Antecedent:** the extended low-degree conjecture as formalized in [MW23], with an additional restriction the authors introduce because the original formalization was refuted. Their footnote attributes that refutation to Ansh Nagda, using algorithms that exploit rare events, and reports it as personal communication with Alexander S. Wein. The antecedent is therefore conjectured and has already been revised once.
- **Algorithm class:** low-degree. The conclusion reads as a statement about running time only through the conjecture, and the conjecture is the step with no proof.
- **Does not establish:** an unconditional computational lower bound for weak recovery. The paper says so.
- **Abstract vs theorem:** none found. The abstract states the dependence on the conjecture in its first sentences.

## Key Contributions

- First LD-based computational lower bound for **weak recovery** (not just detection) below KS in SBM.
- Technique: correlation-preserving projection + graph splitting + cross-validation, converting LD-testing bounds into recovery bounds.
- Lower bound extends to diverging number of blocks k = n^{o(1)} under a strengthened LD conjecture.
- New LD lower bounds for learning the edge connection probability matrix and block graphon function in SBM.

## Key Definitions / Theorems

- **SSBM(n, d/n, ε, k)**: symmetric k-SBM with average degree d, bias ε.
- **Weak recovery (Def 1.2)**: output M̂ with ⟨M̂, M°⟩ ≥ δ ‖M̂‖_F ‖M°‖_F for δ = Ω(1).
- **Conjecture 1.3 (Extended low-degree conjecture)** formalized in [MW23].
- **Theorem 2.1**: Assuming LD conjecture, no exp(n^0.99)-time algorithm achieves recovery rate n^{-0.49} below KS.
- **Theorem 2.4**: LD-based lower bounds for learning edge connection probability matrix.

## Limits

The conjecture this paper assumes is not settled, and its unrestricted form has been refuted.

- The paper's own footnote records that the formalization it builds on, from [MW23], was revised after a refutation attributed to Ansh Nagda using algorithms that exploit rare events, reported there as personal communication with Alexander S. Wein. The authors add a restriction that they say seems to survive that refutation.
- [The Quasi-Polynomial Low-Degree Conjecture is False](quasi-poly-low-degree-conjecture-false.md), Buhai, Hsieh, Jain and Kothari, FOCS 2025, disproves the quasi-polynomial form of the low-degree conjecture in the regime where it was stated. A bound on low-degree advantage and a bound on quasi-polynomial running time are provably different things, so a conditional statement of the form used here cannot be read as a statement about running time without the conjecture holding.
- [Rigorous Implications of the Low-Degree Heuristic](rigorous-implications-low-degree.md), Hsieh, Kane, Kothari, Li, Mohanty and Tiegel, STOC 2026, is the positive counterpart. Its results are conditioned on a noisy version of the problem, two of the three additionally require permutation invariance, and none rules out all polynomial-time algorithms.

## Connections

- [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md) — main tool
- [Stochastic Block Model](../concepts/stochastic-block-model.md) — central problem
- [Kesten-Stigum Threshold](../concepts/kesten-stigum-threshold.md) — sharp threshold
- [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md)
- [David Steurer](../entities/david-steurer.md)

## Open Questions / Limitations

- Depends on unresolved extended LD conjecture [MW23] (recently strengthened after Nagda's counterexample).
- Bound is for k = O(1); extension to larger k requires stronger conjecture.
- Does not give unconditional lower bounds.

## Quotes / Notable Passages

> "To our knowledge, we provide the first rigorous evidence for the sharp transition in recovery rate for polynomial-time algorithms at the KS threshold."
