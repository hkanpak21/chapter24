---
title: Josh Alman
type: entity
entity_type: author
tags: [complexity-theory, fine-grained-cryptography, one-way-functions, hardness-reductions]
---

## About

Assistant professor at Columbia University. Works on fine-grained complexity and fast matrix
multiplication, and — relevantly here — on the boundary between fine-grained hardness assumptions and
cryptographic ones, in both directions.

## Contributions / Works

- **[Fine-Grained Complexity in a World without Cryptography](../sources/fine-grained-world-without-crypto.md)** (Eurocrypt 2025, with Yizhi Huang, Kevin Yeo) — if one-way functions do not exist then average-case `k`-SUM and Zero-`k`-Clique are false for sufficiently large constant `k`, and by contraposition `n^{ω_k(1)}` average-case `k`-SUM hardness implies one-way functions. The barrier result for fine-grained cryptography's Pessiland motivation.
- His work with Song on the fine-grained complexity of gradient computation for training LLMs is catalogued in `raw/SOURCES.md` under compute accounting inside ML; not yet ingested as a wiki page.

## Connections

- Yizhi Huang (Columbia), Kevin Yeo (Columbia / Google) — co-authors. No individual pages yet.
- The paper's target is [Public-Key Cryptography in the Fine-Grained Setting](../sources/pkc-fine-grained-setting.md), whose achievable gap it caps below 2 in a world without one-way functions.
- Concepts: [One-Way Functions](../concepts/one-way-functions.md), [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md), [Average-Case Reductions](../concepts/average-case-reductions.md).
