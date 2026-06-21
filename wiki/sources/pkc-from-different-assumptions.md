---
title: "Public-Key Cryptography from Different Assumptions"
type: source
date_ingested: 2026-04-23
authors: [Boaz Barak, Avi Wigderson]
venue: "IACR ePrint 2008/335; preliminary to Applebaum-Barak-Wigderson STOC 2010"
year: 2008
tags: [cryptography, public-key-encryption, planted-clique, combinatorial-hardness, crypto-foundations]
---

## Summary

This paper (BW08, later Applebaum-Barak-Wigderson 2010 at STOC with Applebaum adding contributions on noisy linear equations) attempts to **broaden the foundations of public-key cryptography** beyond number-theoretic and lattice-based assumptions by constructing PKE schemes based on **average-case hardness of combinatorial NP-complete optimization problems**. The paper introduces three concrete candidate assumptions and derives a PKE scheme from their combination:
1. **Noisy sparse linear equations over GF(2)**: infeasibility of solving a random set of sparse linear equations mod 2, a small fraction of which are corrupted.
2. **Planted dense subgraph distinguishing**: infeasibility of distinguishing a random unbalanced bipartite graph from one with a planted small set S with |S|/3 neighbors.
3. **NC⁰ pseudorandom generator**: existence of a PRG in NC⁰ where every output bit depends on a random constant-size subset of inputs.

Historically, this paper was the first serious attempt to build PKE from *combinatorial* hardness rather than algebraic / number-theoretic hardness (factoring, discrete log, LWE). The assumptions are all related to planted-structure problems in random graphs / random constraint-satisfaction, anticipating later work in statistical-computational gaps. The construction was the benchmark that [Ghosal-Hair-Jain-Sahai STOC 2025](pke-from-planted-clique.md) eventually *matched with standard PC* — closing a 15-year open question.

The paper's lasting impact: it established *that* PKE can be built from combinatorial assumptions, though the specific nonstandard variants used here were later tightened. It also framed the question "which average-case hardness assumptions suffice for PKE?" as central, catalyzing decades of research.

## Key Contributions

- **Three new PKE candidates** based on combinatorial (not number-theoretic) hardness assumptions.
- **First formalization of PKE from planted-structure combinatorial problems**: via the bipartite-planted-subgraph assumption.
- **NC⁰-PRG construction**: builds an NC⁰ pseudorandom generator from the assumptions, itself a foundational primitive.
- **Sparse noisy linear equations over GF(2)**: a hardness assumption structurally similar to LPN but with sparse constraints.
- **Set the research direction**: "PKE from combinatorial assumptions" becomes a named agenda with subsequent contributions (Applebaum, Jain-Sahai line, GHJS25).

## Key Definitions / Theorems

- **Sparse noisy linear equations assumption**: given m random sparse linear equations over ℤ_2 with a planted solution x and an ε-fraction of corrupted equations, recovering x (or any information about it) is hard.
- **Planted bipartite dense subgraph assumption**: distinguishing a random unbalanced bipartite graph with parts of size n and n² from one with a planted set S of size n where S has only |S|/3 neighbors.
- **NC⁰ PRG**: a pseudorandom generator that is computable in constant depth (each output bit depends on constantly many input bits).
- **Main theorem (informal)**: under the above three assumptions, there is a PKE scheme. The paper gives modular analyses showing each assumption's role.

## Connections

- Source: [PKE from Planted Clique (Ghosal-Hair-Jain-Sahai 2025)](pke-from-planted-clique.md) — the STOC 2025 result that closes the "standard PC" gap left by BW08; directly cites this paper as the open question.
- Source: [Reducibility and Statistical-Computational Gaps (Brennan-Bresler 2020)](reducibility-statistical-computational-gaps.md) — planted-subgraph problems in BW08 are instances of the broader PC_ρ framework formalized here.
- Source: [Continuous LWE (Bruna-Regev-Song-Tang 2021)](bruna-continuous-lwe.md) — analogous bridge between average-case learning and cryptography via lattices.
- Source: [Win-Win Theorem (DNV 2019)](win-win-robust-learning.md) — OWFs and PKE are both cryptographic primitives; BW08 shows PKE from novel assumptions.
- Concept: [Planted Clique](../concepts/planted-clique.md) — one of BW08's assumptions is a planted-bipartite-subgraph variant.
- Concept: [Secret Leakage Planted Clique](../concepts/secret-leakage-planted-clique.md) — BW08's assumptions map into this framework.
- Concept: [One-Way Functions](../concepts/one-way-functions.md) — BW08 assumptions are stronger than OWFs.
- Concept: [Pseudorandomness](../concepts/pseudorandomness.md) — NC⁰ PRGs are a subfield of interest here.
- Authors: [Boaz Barak](../entities/boaz-barak.md); Avi Wigderson.

## Open Questions / Limitations

- **Nonstandard assumptions**: the specific variants used (planted bipartite-dense-subgraph with |S|/3 neighbors, NC⁰ PRG) are *nonstandard*; whether PKE exists from *standard* PC was the open question closed by GHJS25 in 2025.
- **No implementation**: purely theoretical, with no concrete parameters analyzed.
- **Subsequent attacks and refinements**: Followup papers (e.g., eprint 2024/359) found key-recovery attacks on specific related PKE schemes; GHJS25 avoids these.
- **Applebaum's 2010 extension**: the STOC 2010 version adds concrete constructions via random local PRGs (Applebaum's contribution); this 2008 version has only 2 authors.

## Quotes / Notable Passages

> "We construct new public-key encryption schemes based on new hardness-on-average assumptions for natural combinatorial NP-hard optimization problems."

> "It is infeasible to distinguish between a random unbalanced bipartite graph and such a graph in which a set S is 'planted' with only |S|/3 neighbors."
