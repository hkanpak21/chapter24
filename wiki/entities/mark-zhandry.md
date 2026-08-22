---
title: Mark Zhandry
type: entity
entity_type: author
tags: [cryptography, bounded-storage-model, computational-indistinguishability, pseudorandomness]
---

## About

Princeton University at the time of the work catalogued here. With Jiaxin Guan he showed that Raz's parity
lower bound could carry a whole family of bounded storage protocols, replacing the birthday paradox machinery
that the model had used since Maurer.

## Contributions / Works

- [Simple Schemes in the Bounded Storage Model](../sources/bounded-storage-simple-schemes.md), with Jiaxin
  Guan. The Encrypt Zero protocol and its enhanced variant, one round bit commitment, two round oblivious
  transfer, and key agreement with perfect correctness, all at adversarial storage `Cn^2` with `C < 1/20`.

## Connections

- Builds directly on [Ran Raz](ran-raz.md).
- Superseded on the storage gap by [Dodis, Quach and Wichs](../sources/speak-much-remember-little.md), who
  reach `m = 2^{O(n)}` at a round and communication cost.
- Concepts: [bounded storage model](../concepts/bounded-storage-model.md),
  [fine-grained cryptography](../concepts/fine-grained-cryptography.md).
