---
title: Geoffroy Couteau
type: entity
entity_type: author
tags: [cryptography, fine-grained-cryptography, complexity-theory, key-exchange]
---

## About

CNRS researcher at IRIF, Université Paris Cité. The most recurrent author in this wiki's fine-grained
cryptography material — co-author on three of the eleven sources ingested in the 2026-08-20 batch, and
on both the definitional paper and the two NIKE papers that bracket the quadratic-gap question.

## Contributions / Works

- **[On Building Fine-Grained One-Way Functions from Strong Average-Case Hardness](../sources/fine-grained-one-way-functions.md)** (2022, with Chris Brzuska) — Definition 6, the `honest^{1+δ}` convention on circuit size; oracle and black-box separations against building FGOWFs from average-case hardness.
- **[Fine-Grained Non-Interactive Key-Exchange: Constructions and Lower Bounds](../sources/fine-grained-nike-lower-bounds.md)** (2023, with Afshar, Mahmoody, Sadeghi) — Merkle generalized to `K` parties in the ROM at gap `n^{K/(K−1)}`; 4-NIKE in Shoup's GGM; the `O(n^2)`-query break of 3-NIKE in Maurer's GGM.
- **[Fine-Grained Non-Interactive Key Exchange, Revisited](../sources/fine-grained-nike-revisited.md)** (2024, with Bauer, Sadeghi) — the first standard-model fine-grained 4-NIKE, from injective PRGs and sub-exponential CDH.

## Connections

- [Mohammad Mahmoody](mohammad-mahmoody.md) — co-author on the NIKE lower bounds.
- Elahe Sadeghi (UT Austin) — co-author on both NIKE papers; Abtin Afshar (Virginia); Chris Brzuska (Aalto); Balthazar Bauer (UVSQ). No individual pages yet.
- Concepts: [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md), [Security Gap Exponent (δ)](../concepts/security-gap-exponent.md).
