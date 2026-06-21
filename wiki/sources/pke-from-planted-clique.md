---
title: "Using the Planted Clique Conjecture for Cryptography: Public-Key Encryption from Planted Clique and Noisy k-LIN Over Expanders"
type: source
date_ingested: 2026-04-23
authors: [Riddhi Ghosal, Isaac M. Hair, Aayush Jain, Amit Sahai]
venue: STOC 2025 (IACR ePrint 2025/1501)
year: 2025
tags: [cryptography, planted-clique, public-key-encryption, statistical-computational-gaps, crypto-foundations]
---

## Summary

This paper (GHJS25) gives the **first public-key encryption scheme based on the standard planted clique conjecture** (combined with a mild auxiliary assumption about noisy k-LIN over expanders), resolving a seminal open question from Applebaum-Barak-Wigderson 2010. The construction is provably secure against poly-size adversaries assuming n^{(log n)^α}-hardness of standard planted clique for any α ∈ (0, 1). Both the planted-clique conjecture and the auxiliary noisy-k-LIN conjecture correspond to natural average-case variants of NP-complete problems studied for decades with substantial supporting evidence (SQ lower bounds, SOS lower bounds, low-degree lower bounds, unconditional lower bounds in restricted computational models).

Conceptually, this establishes planted clique as a **cryptographic primitive** — not merely an average-case hardness conjecture supporting statistical-computational gap analysis, but a building block for public-key cryptography comparable in status to LWE or factoring. This is a significant departure from 2010 (when Applebaum-Barak-Wigderson's construction required a *non-standard* variant of planted clique) and places PC in the cryptographic complexity-theoretic landscape alongside lattice and number-theoretic assumptions.

The combination of two conjectures (PC + noisy k-LIN) is not circular — each is studied independently, and neither is known to imply PKE alone. The constructions are modular and could in principle be weakened or generalized as PC understanding improves. The result bridges the statistical-computational-gap pillar (reductions among planted-style problems) with the cryptographic pillar (constructions from average-case-hard assumptions), and suggests that the two research programs converge more tightly than previously appreciated.

## Key Contributions

- **First PKE from standard planted clique**: public-key encryption secure under n^{(log n)^α}-hardness of PC + noisy k-LIN over expanders.
- **Resolves Applebaum-Barak-Wigderson 2010**: the 2010 paper gave PKE from a *nonstandard* PC variant; GHJS25 closes the gap to the standard conjecture.
- **Modular construction**: PKE built from PC via a series of reductions that isolate the roles of each conjecture.
- **Places planted clique in cryptographic landscape**: alongside LWE, factoring, discrete log; a new pillar for building crypto without lattices or number theory.
- **Suggests convergence of stat-comp-gaps pillar and crypto pillar**: two historically separate research programs now share a foundational conjecture.

## Key Definitions / Theorems

- **Standard planted clique conjecture**: distinguishing G(n, 1/2) from G(n, 1/2) + k-clique is hard for polynomial-size circuits, for k = o(√n).
- **Noisy k-LIN over expanders**: given a bipartite expander graph and noisy linear equations over ℤ₂ indexed by its edges, distinguishing from a uniformly random string is hard.
- **Main theorem**: Assuming (a) n^{(log n)^α}-hardness of standard PC and (b) noisy k-LIN over expanders, there is a PKE scheme with security against poly-time adversaries.
- **Cryptographic building blocks**: the construction uses PC as a "combinatorial OWF," noisy k-LIN for trapdoor structure, and expander graph structure for sparsity.

## Connections

- Source: [Reducibility and Statistical-Computational Gaps (Brennan-Bresler 2020)](reducibility-statistical-computational-gaps.md) — PC_ρ framework underpins the statistical-computational view of PC; GHJS25 lifts PC into cryptography.
- Source: [Planted Clique Conjectures Are Equivalent (Hirahara-Shimizu 2024)](hirahara-planted-clique-conjectures-equivalent.md) — robustness of the PC conjecture across variants; strengthens the foundation GHJS25 rests on.
- Source: [SOS Lower Bound for Planted Clique (Barak-Hopkins-Kelner-Kothari-Moitra-Potechin)](barak-sos-lower-bound-planted-clique.md) — restricted-computation evidence for PC hardness.
- Source: [SQ Lower Bound for Planted Clique (Feldman-Grigorescu-Reyzin-Vempala-Xiao)](feldman-statistical-algorithms-planted-clique.md) — restricted-computation evidence for PC hardness.
- Source: [Public-Key Cryptography from Different Assumptions (Barak-Wigderson 2008 / ABW 2010)](pkc-from-different-assumptions.md) — the predecessor with nonstandard PC; this paper closes the gap to standard.
- Source: [Continuous LWE (Bruna-Regev-Song-Tang 2021)](bruna-continuous-lwe.md) — a different crypto-stat-learning bridge via lattices; GHJS25 is the PC analogue.
- Concept: [Planted Clique](../concepts/planted-clique.md).
- Concept: [Secret Leakage Planted Clique](../concepts/secret-leakage-planted-clique.md).
- Concept: [Learning With Errors](../concepts/learning-with-errors.md) — LWE plays the analogous role in lattice cryptography.
- Authors: Amit Sahai (UCLA), Aayush Jain (CMU), Riddhi Ghosal (UCLA), Isaac M. Hair (UCLA).

## Open Questions / Limitations

- **Removing the noisy k-LIN auxiliary assumption**: can PKE be built from PC alone? Open.
- **Standard n^{Ω(1)} hardness**: the construction requires n^{(log n)^α}-hardness (quasi-polynomial), not standard polynomial hardness of PC; whether poly-hardness suffices is open.
- **Efficient implementations**: the scheme is theoretical; practical parameters and efficiency are not the focus of the paper.
- **Adversary model**: poly-size non-uniform; quantum security not addressed.
- **Key-recovery attacks**: a separate paper (eprint 2024/359) gave a key-recovery attack on an earlier related PKE; GHJS25 handles this via its specific construction.

## Quotes / Notable Passages

> "We give a public key encryption scheme that is provably secure against poly-size adversaries, assuming n^{(log n)^α} hardness of the standard planted clique conjecture, for any α ∈ (0,1), and a relatively mild hardness conjecture about noisy k-LIN over expanders that is not known to imply public-key encryption on its own."

> "The encryption scheme answers an open question in a seminal work by Applebaum, Barak, and Wigderson [STOC'10]."

> "Both conjectures correspond to natural average-case variants of NP-complete problems and have been studied for multiple decades, with unconditional lower bounds supporting them in a variety of restricted models of computation."
