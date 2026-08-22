---
title: Jonathan Ullman
type: entity
entity_type: author
tags: [statistical-query, hardness-reductions, one-way-functions, differential-privacy, sample-complexity]
---

## About

Northeastern; Harvard at the time of the work catalogued here. Works on the computational limits of private
and valid data analysis, and on the fingerprinting-code machinery that drives the lower bounds in both
literatures.

## Contributions / Works

- [Preventing False Discovery in Interactive Data Analysis is Hard](../sources/preventing-false-discovery-hard.md)
  (HU14) — under one-way functions, no computationally efficient oracle given `n` samples answers
  `n^{3+o(1)}` adaptively chosen statistical queries validly; unconditionally at dimension `n^{3+o(1)}` for
  unbounded oracles; and the corollary that any such oracle is blatantly non-private. This is the batch's
  existence proof that **query count can be a rigorous security parameter with matching bounds** — though it
  is about statistical validity, not confidentiality.
- The robust fingerprinting codes of Bun–Ullman–Vadhan supply the measure-concentration property the attack
  needs.
- His earlier lower bounds on answering non-adaptive queries under DP are the comparison point: DP oracles
  cannot answer `n^{2+o(1)}` non-adaptive queries, and HU14 shows the same conclusion for adaptive queries
  against oracles that merely avoid blatant non-privacy, up to a factor `n`.

## Connections

- Co-author here: [Moritz Hardt](moritz-hardt.md); via fingerprinting codes,
  [Salil Vadhan](salil-vadhan.md).
- Concepts: [adaptive data analysis](../concepts/adaptive-data-analysis.md),
  [statistical query model](../concepts/statistical-query-model.md),
  [data reconstruction attack](../concepts/data-reconstruction-attack.md),
  [one-way functions](../concepts/one-way-functions.md).
