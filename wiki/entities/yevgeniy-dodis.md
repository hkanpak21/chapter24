---
title: Yevgeniy Dodis
type: entity
entity_type: author
tags: [cryptography, bounded-storage-model, pseudorandomness, computational-indistinguishability]
---

## About

New York University. Works on information theoretic cryptography, randomness extraction and leakage
resilience. With Willy Quach and Daniel Wichs he is the author of the pair of papers that reopened the
streaming bounded storage model, first by breaking the quadratic storage ceiling for key agreement and
oblivious transfer, then by adding authentication and signatures.

## Contributions / Works

- [Speak Much, Remember Little: Cryptography in the Bounded Storage Model, Revisited](../sources/speak-much-remember-little.md).
  Shows the Dziembowski and Maurer quadratic barrier applies only to a restricted variant of the model,
  constructs unconditional key agreement and oblivious transfer at storage gaps up to `2^{O(n)}`, and proves
  matching round and communication lower bounds in two adversary models.
- [Authentication in the Bounded Storage Model](../sources/authentication-bounded-storage.md). Message
  authentication codes with long tags at `m = 2^{O(n)}`, short tag codes at `m = O(n^2)` built on Raz's
  parity bound, and signatures at `m = O(n^2)` with a matching lower bound. Introduces the block entropy
  lemma.

## Connections

- Co-authors here: Willy Quach and [Daniel Wichs](daniel-wichs.md).
- Builds on [Ran Raz](ran-raz.md) and on [Mark Zhandry](mark-zhandry.md) with Jiaxin Guan.
- The follow up [On Bounded Storage Key Agreement and One-Way Functions](../sources/bsm-key-agreement-owf.md),
  by Brzuska, [Couteau](geoffroy-couteau.md), Egger and Quach, starts from the round and communication lower
  bounds proved in the first paper above.
- Concepts: [bounded storage model](../concepts/bounded-storage-model.md),
  [fine-grained cryptography](../concepts/fine-grained-cryptography.md).
