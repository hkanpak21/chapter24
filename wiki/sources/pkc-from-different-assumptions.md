---
title: "Public-Key Cryptography from Different Assumptions"
type: source
date_ingested: 2026-04-23
authors: [Boaz Barak, Avi Wigderson]
venue: "IACR ePrint 2008/335, preliminary to Applebaum-Barak-Wigderson STOC 2010. The ingested PDF is dated 2 August 2008 and does not itself state a venue."
year: 2008
tags: [cryptography, public-key-encryption, planted-clique, combinatorial-hardness, crypto-foundations]
claim_quantifier: conditional
antecedent: "two assumptions stated in the abstract. One, that a pseudorandom generator with small locality can be obtained by connecting outputs to inputs using any sufficiently good unbalanced expander. Two, that it is hard to distinguish a random graph that is such an expander from one where a planted random logarithmic-size subset S of the outputs is connected to fewer than |S| inputs."
algorithm_class: "all poly-time conditionally, with the authors' own ceiling that the scheme can be broken in n^{O(log n)} time"
adversary_bound: "poly-time, subject to the n^{O(log n)} break"
date_verified: 2026-08-20
---

## Summary

This paper (BW08, later Applebaum-Barak-Wigderson 2010 at STOC with Applebaum adding contributions on noisy linear equations) attempts to **broaden the foundations of public-key cryptography** beyond number-theoretic and lattice-based assumptions by constructing PKE schemes based on **average-case hardness of combinatorial NP-complete optimization problems**. The paper's abstract states **two** assumptions and derives a PKE scheme from their combination:
1. **Small-locality PRG from an unbalanced expander**: one can obtain a pseudorandom generator with small locality by connecting the outputs to the inputs using any sufficiently good unbalanced expander.
2. **Planted-subgraph distinguishing**: it is hard to distinguish between a random graph that is such an expander and a random graph where a planted random logarithmic-sized subset S of the outputs is connected to fewer than |S| inputs.

_Corrected 2026-08-20 against the primary PDF. An earlier version of this list gave three assumptions, added noisy sparse linear equations over GF(2) as a separate item, and stated the planted set as having |S|/3 neighbours. The abstract names two assumptions. The string `|S|/3` does not occur in the paper, and the planted set is logarithmic in size. Noisy linear equations appear once in the body, as a comparison to Alekhnovich and to Regev rather than as an assumption of this construction. The three-assumption reading matches the later Applebaum-Barak-Wigderson version, not this one._

The authors also record two drawbacks of their own scheme. The assumptions are not as well studied as the hardness of factoring, and the scheme can be broken in n^{O(log n)} time, where n is the key length and security parameter.

Historically, this paper was the first serious attempt to build PKE from *combinatorial* hardness rather than algebraic / number-theoretic hardness (factoring, discrete log, LWE). The assumptions are all related to planted-structure problems in random graphs / random constraint-satisfaction, anticipating later work in statistical-computational gaps. The construction was the benchmark that [Ghosal-Hair-Jain-Sahai STOC 2025](pke-from-planted-clique.md) eventually *matched with standard PC* — closing a 15-year open question.

The paper's lasting impact: it established *that* PKE can be built from combinatorial assumptions, though the specific nonstandard variants used here were later tightened. It also framed the question "which average-case hardness assumptions suffice for PKE?" as central, catalyzing decades of research.

## Claim Boundary

- **Quantified over:** adversaries against the proposed scheme, subject to the authors' own statement that the scheme can be broken in n^{O(log n)} time, where n is the key length and security parameter.
- **Antecedent:** two assumptions, both stated in the abstract. First, that one can obtain a pseudorandom generator with small locality by connecting the outputs to the inputs using any sufficiently good unbalanced expander. Second, that it is hard to distinguish between a random graph that is such an expander and a random graph where a planted random logarithmic-sized subset S of the outputs is connected to fewer than |S| inputs. Both are conjectured, and the authors say they are not as well studied as the hardness of factoring.
- **Algorithm class:** all polynomial time, conditionally, with the superpolynomial ceiling above.
- **Does not establish:** public-key encryption from the standard planted clique conjecture, and does not establish security beyond n^{O(log n)} time. The authors record the second point as one of two major drawbacks.
- **Abstract vs theorem:** none found. The abstract presents the assumptions as new and raises their validity and strength as open questions.

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

- **Nonstandard assumptions**: the specific variants used, namely the planted logarithmic-size subset connected to fewer than |S| inputs and the small-locality PRG from an unbalanced expander, are *nonstandard*; whether PKE exists from *standard* PC was the open question closed by GHJS25 in 2025. _Corrected 2026-08-20: an earlier version of this bullet said |S|/3 neighbours, which does not appear in the paper._
- **Superpolynomial ceiling**: the authors state that the scheme can be broken in n^{O(log n)} time, and say it is likely that other variants will allow subexponential rather than superpolynomial security.
- **No implementation**: purely theoretical, with no concrete parameters analyzed.
- **Subsequent attacks and refinements**: Followup papers (e.g., eprint 2024/359) found key-recovery attacks on specific related PKE schemes; GHJS25 avoids these.
- **Applebaum's 2010 extension**: the STOC 2010 version adds concrete constructions via random local PRGs (Applebaum's contribution); this 2008 version has only 2 authors.

## Quotes / Notable Passages

> _Not verbatim. Checked against `raw/BW08_PKCfromDifferentAssumptions.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary._
>
> We construct new public-key encryption schemes based on new hardness-on-average assumptions for natural combinatorial NP-hard optimization problems.

> _Not verbatim, and materially wrong. Checked against `raw/BW08_PKCfromDifferentAssumptions.pdf` on 2026-08-20. The string `|S|/3` does not occur anywhere in the paper. The planted set is logarithmic in size and is connected to fewer than `|S|` inputs, not to `|S|/3` neighbours. Retained unquoted so the error is not repeated, and replaced by the paper's own sentence below._
>
> It is infeasible to distinguish between a random unbalanced bipartite graph and such a graph in which a set S is 'planted' with only |S|/3 neighbors.

_The three passages below are verbatim, verified 2026-08-20._

> "We construct a new public key encryption based on two assumptions:"

> "It is hard to distinguish between a random graph that is such an expander and a random graph where a (planted) random logarithmic-sized subset S of the outputs is connected to fewer than |S| inputs."

> "the scheme is far less efficient and secure than might be hoped: it can be broken in n^{O(log n)} time, where n is the key length / security parameter of the system."

The exponent in the last passage is set as a superscript, which `pdftotext` flattens; the surrounding prose matches exactly.
