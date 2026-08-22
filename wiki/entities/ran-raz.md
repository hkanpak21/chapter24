---
title: Ran Raz
type: entity
entity_type: author
tags: [complexity-theory, learning-theory, cryptography, bounded-storage-model, sample-complexity]
---

## About

Weizmann Institute of Science and the Institute for Advanced Study at the time of the work catalogued here.
Complexity theorist. The time and space lower bound for parity learning is the result that made memory a
first class resource in learning theory and, by way of its encryption corollary, reopened the bounded storage
model.

## Contributions / Works

- [Fast Learning Requires Good Memory: A Time-Space Lower Bound for Parity Learning](../sources/raz-parity-time-space.md).
  Any parity learner using fewer than about `n^2/20` memory bits needs exponentially many samples,
  unconditionally. The memory bounded party is the learner. The paper's own encryption corollary renames that
  party the attacker, which is the single point in this corpus where a memory bound is placed on an attacker
  rather than on an honest party.
- The affine branching program technique from that paper, together with the reduction from general branching
  programs, is reused as a black box by the streaming bounded storage line.

## Connections

- Directly built on by [Guan and Zhandry](../sources/bounded-storage-simple-schemes.md), whose key agreement,
  commitment and transfer protocols reduce to the parity bound, and by
  [Dodis, Quach and Wichs](../sources/authentication-bounded-storage.md), whose short tag message
  authentication code restates it as Theorem 6.2.
- Identified by [Dodis, Quach and Wichs](../sources/speak-much-remember-little.md) as the work that first
  abandoned the traditional bounded storage restrictions and worked in the streaming variant.
- Concepts: [bounded storage model](../concepts/bounded-storage-model.md),
  [fine-grained cryptography](../concepts/fine-grained-cryptography.md).
