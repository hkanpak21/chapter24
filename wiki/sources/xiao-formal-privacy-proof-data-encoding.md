---
title: Formal Privacy Proof of Data Encoding — The Possibility and Impossibility of Learnable Encryption
type: source
date_ingested: 2026-07-26
authors: [Hanshen Xiao, G. Edward Suh, Srinivas Devadas]
venue: ACM CCS 2024
year: 2024
tags: [cryptography, learning-theory, computational-indistinguishability, one-way-functions]
---

> **Provenance.** Recorded from a prior-art sweep on the strength of its headline impossibility result;
> **not read, and the statement below is a paraphrase.** Read before citing — this is an obstacle the
> programme must route around, so getting its exact scope right matters.

## Summary

Studies whether a data-encoding transformation can simultaneously preserve learnability and provide
cryptographic-grade privacy. The headline result is negative: **no non-trivial property-preserving
transformation that keeps encoded samples learnable can offer worst-case cryptographic computational
security.**

The consequence for this programme, stated bluntly: **the training pipeline does not get to be a
one-way function for free.** Any claim that training is hard to invert must either accept
average-case-only guarantees, restrict the adversary class, or identify what about the specific
architecture and distribution escapes this impossibility. It cannot be obtained by observing that
training loses information.

## Key Contributions

- An impossibility result bounding what learnable encodings can deliver in cryptographic terms.
- A companion possibility side delimiting what remains achievable (scope unverified).

## Key Definitions / Theorems

- **(Paraphrase, unverified.)** Non-trivial property-preserving learnable transformations cannot achieve
  worst-case computational cryptographic security.

## Connections

- **The standing obstacle to** [fiber-of-the-training-map](../concepts/fiber-of-the-training-map.md) and
  to any "training is one-way" claim; see
  [cohen-data-reconstruction](cohen-data-reconstruction.md) for the notion it constrains.
- Same authors' [PAC Privacy](../analyses/native-asymmetry-in-learning.md) line (Xiao–Devadas, CRYPTO
  2023), whose adversary is *"possibly computationally-unbounded"* by construction — this paper is the
  computational-side companion.
- [win-win-robust-learning](win-win-robust-learning.md) — the other direction of tax on computational
  claims in learning.

## Open Questions / Limitations

- **Scope is exactly what needs checking.** "Worst-case" is doing work in the statement; an average-case
  or distribution-specific guarantee may survive it, and the programme's setting is average-case by
  design. Whether the impossibility bites depends entirely on this, and it is unresolved until the paper
  is read.

## Quotes / Notable Passages

*(None extracted — page built from a secondary description.)*
