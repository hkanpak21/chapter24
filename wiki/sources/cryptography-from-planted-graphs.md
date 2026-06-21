---
title: "Cryptography from Planted Graphs: Security with Logarithmic-Size Messages"
type: source
date_ingested: 2026-04-23
authors: [Damiano Abram, Amos Beimel, Yuval Ishai, Eyal Kushilevitz, Varun Narayanan]
venue: "IACR ePrint 2023/1929; TCC 2023 (Springer LNCS 14372)"
year: 2023
tags: [cryptography, planted-clique, secret-sharing, private-simultaneous-messages, lower-bounds]
---

## Summary

This paper (ABIKN23) proves that under variants of the **planted-clique conjecture**, cryptographic primitives with **O(log n)-size messages** exist in the public-information model — a setting where adversaries observe the same public graph as honest parties but must extract secrets without side information. Specifically, the paper constructs:
1. **Private Simultaneous Messages (PSM) protocols** with O(log n) message size
2. **Secret-sharing schemes for forbidden-graph access structures**
3. **Tight Ω(log log n) lower bounds for threshold schemes**

The paper demonstrates that **planted-clique hardness is *usable* as a cryptographic assumption**, setting the stage for [Ghosal-Hair-Jain-Sahai STOC 2025](pke-from-planted-clique.md) which established PKE from the standard PC conjecture two years later. ABIKN23 is the **Pillar IV anchor** bridging statistical-computational-gap theory (PC_ρ reductions) with cryptographic primitive construction.

The technical heart: planted subgraph problems (variants of planted clique where the hidden structure is a larger graph than a clique) can be formulated so that solving them is equivalent to breaking a specific cryptographic primitive — giving a direct reduction rather than a black-box assumption. The log-size message property comes from the combinatorial efficiency of encoding secrets via graph structures.

## Key Contributions

- **PSM protocols with log-size messages under planted-graph hardness**: first construction of O(log n) PSM from planted-subgraph-style assumptions.
- **Secret sharing for forbidden-graph access structures**: certain access structures (subsets-can-recover-if-and-only-if-they-are-independent-set-of-forbidden-graph) have efficient secret-sharing schemes under planted-clique hardness.
- **Tight Ω(log log n) threshold-scheme lower bound**: matching lower bound showing the log-size message property is near-optimal.
- **Planted clique as cryptographic primitive**: first concrete demonstration that PC-style assumptions underwrite cryptographic construction, paving the way for GHJS25.
- **Public-information model**: unlike standard crypto, adversary observes the same graph; security is non-trivial.

## Key Definitions / Theorems

- **Planted subgraph conjecture**: distinguishing a random graph from one with a planted subgraph structure is hard for polynomial-time algorithms.
- **Private Simultaneous Messages (PSM)**: two parties simultaneously send messages to a referee who computes a joint function without learning inputs beyond what the function reveals.
- **Forbidden-graph access structure**: a family defined by a graph G where subset S can recover the secret iff S is an independent set of G.
- **Main theorem (PSM)**: Under planted-subgraph-like conjectures, there exist PSM protocols for any function computable by a circuit of log-bit messages.
- **Ω(log log n) lower bound for threshold**: matches the upper bound; threshold schemes cannot have messages smaller than log log n.

## Connections

- Source: [PKE from Planted Clique (GHJS25)](pke-from-planted-clique.md) — direct successor at STOC 2025; ABIKN23 established PC is usable for crypto, GHJS25 builds PKE.
- Source: [Reducibility and Statistical-Computational Gaps (BB20)](reducibility-statistical-computational-gaps.md) — PC_ρ framework; ABIKN23 uses specific PC variants.
- Source: [Planted Clique Conjectures Are Equivalent (HS24)](hirahara-planted-clique-conjectures-equivalent.md) — equivalence among PC variants; tightens what ABIKN23's assumption commits to.
- Source: [Public-Key Cryptography from Different Assumptions (BW08)](pkc-from-different-assumptions.md) — predecessor combinatorial-PKC direction; ABIKN23 extends with log-size messages.
- Source: [Continuous LWE (BRST21)](bruna-continuous-lwe.md) — related crypto-stat bridge via lattices; ABIKN23 is the planted-graph parallel.
- Concept: [Planted Clique](../concepts/planted-clique.md).
- Concept: [Secret Leakage Planted Clique](../concepts/secret-leakage-planted-clique.md).
- Concept: [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md).
- Authors: Yuval Ishai (Technion), Amos Beimel (Ben-Gurion), Eyal Kushilevitz (Technion) — classical TCC contributors.

## Open Questions / Limitations

- **Standard vs. nonstandard PC variants**: ABIKN23 uses planted-subgraph variants; GHJS25 later showed standard-PC sufficiency for PKE.
- **PSM for arbitrary functions**: paper handles specific function classes; general-function PSM with log-size messages open.
- **Extension to multi-party (MPC)**: PSM is 2-party; MPC generalization open.
- **Quantum adversaries**: planted-clique hardness against quantum computers not addressed.

## Quotes / Notable Passages

> "Under variants of the planted-clique conjecture, cryptographic primitives with O(log n)-size messages exist in the public-information model."

> "Demonstrates that planted-clique hardness is usable as a cryptographic assumption, setting the stage for GHJS25."
