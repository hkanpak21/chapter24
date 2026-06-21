---
title: Counterexamples to the Low-Degree Conjecture
type: source
date_ingested: 2026-04-12
authors: [Justin Holmgren, Alexander S. Wein]
venue: ITCS 2021
year: 2021
tags: [low-degree-polynomials, counterexamples, statistical-computational-gaps, complexity-theory]
---

## Summary

This paper refutes the original formulation of the Low-Degree Conjecture (Hopkins 2018) by constructing explicit hypothesis-testing problems where degree-O(log n) polynomials fail to distinguish the planted from the null distribution, yet polynomial-time algorithms succeed. The counterexamples exploit algebraic structure (Gaussian elimination over finite fields / linear equations) that low-degree polynomial moments cannot detect.

The authors propose a modified version of the conjecture that avoids their counterexample by excluding problems with such "algebraic" structure, and argue the modified version remains a useful heuristic for "structureless" planted problems. The paper is widely cited as establishing the limits of the low-degree framework and motivating the search for complementary lower-bound tools (Franz-Parisi, OGP, etc.).

(Note: The raw PDF for this paper was replaced during the 2026-04-23 raw/ audit — the file previously contained Brennan-Bresler 2020 "Average-Case Lower Bounds for Learning Sparse Mixtures" instead of Holmgren-Wein 2021. Current PDF is verified correct: arXiv:2004.08454.)

## Key Contributions

- Explicit counterexample to the original low-degree conjecture: a planted problem (variant of learning parities / 3-XOR) where LD fails but Gaussian elimination succeeds in poly time.
- Modified conjecture formulation restricted to "structureless" planted problems.
- Sharpened understanding: LD captures noise-robust / moment-based algorithms but not algebraic ones.

## Key Definitions / Theorems

- Counterexample construction based on learning parities or similar algebraic structure.
- Revised low-degree conjecture — excludes problems with exact algebraic solutions.

## Connections

- [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md) — counterexample paper
- [Statistical Query Model](../concepts/statistical-query-model.md) — LD and SQ both fail on parity; this is a "known exception"
- [Lattice Methods Surpass Sum-of-Squares](zadik-lattice-surpass-sos.md) — further LD counterexamples via LLL
- [Alexander Wein](../entities/alexander-wein.md)

## Open Questions / Limitations

- What precisely makes a problem "structureless"? No clean characterization exists.
- Are there counterexamples not rooted in algebraic structure (e.g., anti-concentration)?
- How to adapt LD to capture algebraic algorithms, if at all.

## Quotes / Notable Passages

(Indirect — file content mismatched with title.)
