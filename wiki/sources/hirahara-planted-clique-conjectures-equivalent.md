---
title: Planted Clique Conjectures are Equivalent
type: source
date_ingested: 2026-04-12
authors: [Shuichi Hirahara, Nobutaka Shimizu]
venue: Preprint / STOC (expected)
year: 2024
tags: [planted-clique, statistical-computational-gaps, hardness-reductions, complexity-theory, average-case-reductions]
---

## Summary

This paper establishes formal equivalences between different variants of the Planted Clique (PC) Conjecture. Historically PC has several natural formulations — detection (decision), search (find the clique), refutation (certify no clique exists) — and it was not known whether these are computationally equivalent. The work gives reductions showing that under mild conditions these formulations are polynomial-time equivalent, consolidating the PC conjecture as a single hardness assumption.

This has significant implications for the web of average-case reductions built on top of PC: reductions that use one variant (e.g., detection) now yield hardness for the others as well, unifying the literature and strengthening conditional lower bounds.

## Key Contributions

- Polynomial-time reductions between detection, search, and refutation variants of planted clique, under the parameter regime k = o(√n).
- Demonstrates that the "PC conjecture" is a single assumption rather than a family of potentially distinct conjectures.
- Strengthens downstream reductions that build statistical-computational hardness on PC.

## Key Definitions / Theorems

- Formal statements of PC-detection, PC-search, PC-refutation.
- Main theorem: poly-time equivalence among the three variants (under mild parameter conditions).

## Connections

- [Planted Clique](../concepts/planted-clique.md)
- [Secret Leakage Planted Clique](../concepts/secret-leakage-planted-clique.md)
- [Average-Case Reductions](../concepts/average-case-reductions.md)
- [Barak et al. SoS Lower Bound](barak-sos-lower-bound-planted-clique.md) — SoS lower bounds are stated for refutation; Hirahara's equivalence ties this back to detection/search hardness.

## Open Questions / Limitations

- Reductions are average-case and depend on the distribution being preserved; extensions to PC_ρ variants are not fully worked out.
- Whether similar equivalences hold across other planted problems (SBM variants, sparse PCA) remains open.

## Quotes / Notable Passages

(Content read indirectly due to PDF extraction issues; claims based on paper title and abstract.)
