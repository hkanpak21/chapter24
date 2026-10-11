---
title: Anvith Thudi
type: entity
entity_type: author
tags: [adversarial-ml, verifiable-computation, machine-unlearning]
---

## About

University of Toronto and the Vector Institute. Works on the definitional side of ML security: what a
security claim about training would have to mean before it could be true. The recurring move is to take
the training log as the object and ask what it does and does not certify.

## Contributions / Works

- **[On the Necessity of Auditable Algorithmic Definitions for Machine Unlearning](../sources/auditable-unlearning-definitions.md)**
  (Thudi, Jia, Shumailov, Papernot; USENIX Security 2022) — forging: the same model can be obtained from
  different datasets, so unlearning is well-defined only at the algorithmic level. Takes the
  proof-of-learning log as its notion of dataset feasibility.
- **[Proof-of-Learning: Definitions and Practice](../sources/proof-of-learning.md)**
  (2021) — joint secondary author.
- **[Proof-of-Learning is Currently More Broken Than You Think](../sources/pol-more-broken.md)**
  (2023) — co-author; contributes the cheapness-assumption analysis, Definition 6's `c`-cheap proof
  algorithms, and Lemmas 5–6.

## Connections

- [Nicolas Papernot](nicolas-papernot.md), [Hengrui Jia](hengrui-jia.md), [Ilia Shumailov](ilia-shumailov.md).
- [Proof-of-Learning (the notion)](../concepts/proof-of-learning.md),
  [Machine Unlearning](../concepts/machine-unlearning.md),
  [Fiber of the Training Map](../concepts/fiber-of-the-training-map.md).
