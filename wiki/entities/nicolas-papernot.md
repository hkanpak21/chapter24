---
title: Nicolas Papernot
type: entity
entity_type: author
tags: [adversarial-ml, verifiable-computation, evaluation-methodology, complexity theory]
---

## About

University of Toronto and the Vector Institute. Works on the security and privacy of machine
learning, with a recurring methodological line: taking a widely used but informally stated security
goal and asking what it would mean formally. Appears in this wiki on model extraction,
proof-of-learning, machine unlearning, and robustness-evaluation methodology.

## Contributions / Works

- **[On the Necessity of Auditable Algorithmic Definitions for Machine Unlearning](../sources/auditable-unlearning-definitions.md)**
  (Thudi, Jia, Shumailov, Papernot; USENIX Security 2022) — forgeability; unlearning is well-defined
  only at the algorithmic level.
- **[Beyond Labeling Oracles: What does it mean to steal ML models?](../sources/beyond-labeling-oracles.md)**
  (Shafran, Shumailov, Erdogdu, Papernot; preprint, arXiv:2310.01959) — model extraction has no formal
  success predicate; the proposed replacement is a cost inequality, left informal.
- **[High Accuracy and High Fidelity Extraction of Neural Networks](../sources/jagielski-model-extraction.md)**
  (Jagielski, Carlini, Berthelot, Kurakin, Papernot; 2020) — the accuracy/fidelity taxonomy and three
  hardness statements, including an SQ sample lower bound for fidelity extraction.
- **[Proof-of-Learning: Definitions and Practice](../sources/proof-of-learning.md)**
  (Jia, Yaghini, Choquette-Choo, Dullerud, Thudi, Chandrasekaran, Papernot; IEEE S&P 2021) — the log
  format that forgeability is later defined over.
- **[On Evaluating Adversarial Robustness](../sources/on-evaluating-adversarial-robustness.md)**
  (Carlini, Athalye, Papernot, et al.; 2019).

## Connections

- [Ilia Shumailov](ilia-shumailov.md) — co-author on the unlearning and extraction papers.
- [Nicholas Carlini](nicholas-carlini.md) — co-author on extraction and robustness evaluation.
- The through-line across four of these works is the same defect from four angles: a security goal
  in wide use whose success predicate is either absent (extraction), unprovable at the level it is
  stated (unlearning), or asserted as a bare inequality (proof-of-learning). See
  [Model Extraction](../concepts/model-extraction.md) and
  [Machine Unlearning](../concepts/machine-unlearning.md).
