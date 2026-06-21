---
title: Low Degree Conjecture Implies Sharp Computational Thresholds in Stochastic Block Model
type: source
date_ingested: 2026-04-12
authors: [Jingqiu Ding, Yiding Hua, Lucas Slot, David Steurer]
venue: Preprint
year: 2025
tags: [stochastic-block-model, low-degree-polynomials, kesten-stigum, community-detection, statistical-computational-gaps]
---

## Summary

This paper sharpens the implications of the (extended) low-degree conjecture for the symmetric stochastic block model (SBM). Assuming the conjecture of Kunisky-Wein-style extended low-degree hardness, the authors prove that no polynomial-time algorithm can achieve **weak recovery** (constant correlation with true community labels) below the **Kesten-Stigum (KS) threshold** ε²d < k². This provides the first rigorous evidence for a sharp transition in the recovery rate for polynomial-time algorithms at the KS threshold.

Concretely, the paper shows (Theorem 2.1) that below KS no exp(n^0.99)-time algorithm achieves recovery rate n^{-0.49} with constant probability, while above KS poly-time weak recovery is known [Mas14, AS15]. Previous work ruled out only hypothesis-testing-style algorithms with success probability 1 - o(1); this paper handles the harder case of constant-probability recovery via a **correlation-preserving projection** technique (from [HS17]) plus graph-splitting and cross-validation.

Results also give computational lower bounds for learning SBM parameters (edge probability matrix and graphon).

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
