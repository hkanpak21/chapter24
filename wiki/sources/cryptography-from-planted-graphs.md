---
title: "Cryptography from Planted Graphs: Security with Logarithmic-Size Messages"
type: source
date_ingested: 2026-04-23
authors: [Damiano Abram, Amos Beimel, Yuval Ishai, Eyal Kushilevitz, Varun Narayanan]
venue: "IACR ePrint 2023/1929, TCC 2023 (Springer LNCS 14372). The ingested PDF is dated 19 December 2023 and does not itself state a venue."
year: 2023
tags: [cryptography, planted-clique, secret-sharing, private-simultaneous-messages, lower-bounds]
claim_quantifier: conditional
antecedent: "variants of the planted clique problem, not the standard conjecture. Conjectured."
algorithm_class: "circuits, bounded by size"
adversary_bound: "size n^{o(log n)}, at distinguishing advantage n^{-Omega(1)} for the basic constructions"
date_verified: 2026-08-20
---

## Summary

This paper (ABIKN23) proves that under variants of the **planted-clique conjecture**, cryptographic primitives with **O(log n)-size messages** exist in the public-information model — a setting where adversaries observe the same public graph as honest parties but must extract secrets without side information. Specifically, the paper constructs:
1. **Private Simultaneous Messages (PSM) protocols** with O(log n) message size
2. **Secret-sharing schemes for forbidden-graph access structures**
3. **Tight Ω(log log n) lower bounds on share size for threshold schemes**

The paper demonstrates that **planted-clique hardness is *usable* as a cryptographic assumption**, setting the stage for [Ghosal-Hair-Jain-Sahai STOC 2025](pke-from-planted-clique.md) which established PKE from the standard PC conjecture two years later. ABIKN23 is the **Pillar IV anchor** bridging statistical-computational-gap theory (PC_ρ reductions) with cryptographic primitive construction.

The technical heart: planted subgraph problems (variants of planted clique where the hidden structure is a larger graph than a clique) can be formulated so that solving them is equivalent to breaking a specific cryptographic primitive — giving a direct reduction rather than a black-box assumption. The log-size message property comes from the combinatorial efficiency of encoding secrets via graph structures.

## Claim Boundary

- **Quantified over:** adversaries of bounded size. The abstract states that the positive results guarantee that any adversary of size n^{o(log n)} achieves an n^{-Omega(1)} distinguishing advantage, and that the advantage is made negligible only by slightly increasing the asymptotic message size.
- **Antecedent:** variants of the planted clique problem rather than the standard conjecture. Conjectured.
- **Algorithm class:** circuits, bounded by size. The security statement is a size bound on the adversary. It is not a low-degree bound and not an SQ bound, and the paper's low-degree analysis is evidence for the assumption rather than the class the theorem quantifies over.
- **Does not establish:** security against arbitrary polynomial-time adversaries at the smallest stated message size. The guarantee is a size bound paired with an inverse-polynomial advantage. On the negative side the paper shows that computational threshold secret-sharing schemes with public information require share size Omega(log log n), and that for arbitrary access structures computational security does not help with 1-bit shares.
- **Abstract vs theorem:** none found. The abstract states the size bound and the inverse-polynomial advantage explicitly.

## Key Contributions

- **PSM protocols with log-size messages under planted-graph hardness**: first construction of O(log n) PSM from planted-subgraph-style assumptions.
- **Secret sharing for forbidden-graph access structures**: certain access structures (subsets-can-recover-if-and-only-if-they-are-independent-set-of-forbidden-graph) have efficient secret-sharing schemes under planted-clique hardness.
- **Tight Ω(log log n) threshold-scheme lower bound** on share size, together with the result that for arbitrary access structures computational security does not help with 1-bit shares.
- **Planted clique as cryptographic primitive**: first concrete demonstration that PC-style assumptions underwrite cryptographic construction, paving the way for GHJS25.
- **Public-information model**: unlike standard crypto, adversary observes the same graph; security is non-trivial.

## Key Definitions / Theorems

- **Planted subgraph conjecture**: distinguishing a random graph from one with a planted subgraph structure is hard for polynomial-time algorithms.
- **Private Simultaneous Messages (PSM)**: two parties simultaneously send messages to a referee who computes a joint function without learning inputs beyond what the function reveals.
- **Forbidden-graph access structure**: a family defined by a graph G where subset S can recover the secret iff S is an independent set of G.
- **Main result (PSM)**: a private simultaneous messages protocol for every f : [n] × [n] → {0,1}, requiring (1+ε) log n-bit messages for most functions and (2+ε) log n-bit messages for the rest. This is applied to non-interactive secure three-party computation with similar message size in the preprocessing model. _Corrected 2026-08-20 against the primary PDF: an earlier version of this bullet said "any function computable by a circuit of log-bit messages", which is not a statement the paper makes._
- **Ω(log log n) lower bound for threshold**: computational threshold secret-sharing schemes with public information require **share** size Ω(log log n). _Corrected 2026-08-20: the quantity bounded is share size, not message size._

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

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> Under variants of the planted-clique conjecture, cryptographic primitives with O(log n)-size messages exist in the public-information model.

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> Demonstrates that planted-clique hardness is usable as a cryptographic assumption, setting the stage for GHJS25.

_The four passages below are verbatim, verified against `raw/ABIKN23_CryptoPlantedGraphs.pdf` on 2026-08-20._

> "The security of our constructions is based on the conjectured hardness of variants of the planted clique problem, which was extensively studied in the algorithms, statistical inference, and complexity theory communities."

> "The above positive results guarantee that any adversary of size n^{o(log n)} achieves an n^{−Ω(1)} distinguishing advantage."

> "On the negative side, we show that computational threshold secret-sharing schemes with public information require share size Ω(log log n). For arbitrary access structures, we show that computational security does not help with 1-bit shares."

> "A secret-sharing scheme for any "forbidden-graph" access structure on n nodes with O(log n) share size."

The exponents and the Greek letters in the second and third passages are set as superscripts and symbols that `pdftotext` flattens or drops; the surrounding prose matches the paper exactly and the parameters are as printed in the abstract.
