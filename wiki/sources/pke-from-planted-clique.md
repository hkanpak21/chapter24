---
title: "Using the Planted Clique Conjecture for Cryptography: Public-Key Encryption from Planted Clique and Noisy k-LIN Over Expanders"
type: source
date_ingested: 2026-04-23
authors: [Riddhi Ghosal, Isaac M. Hair, Aayush Jain, Amit Sahai]
venue: STOC 2025, IACR ePrint 2025/1501 (the ingested PDF does not itself state a venue)
year: 2025
tags: [cryptography, planted-clique, public-key-encryption, statistical-computational-gaps, crypto-foundations]
claim_quantifier: conditional
antecedent: "two conjectures. First, n^{(log n)^alpha} hardness of the standard planted clique conjecture for any alpha in (0,1), which is quasi-polynomial rather than polynomial hardness. Second, a hardness conjecture about noisy k-LIN over expanders that the paper says is not known to imply public-key encryption on its own."
algorithm_class: "all poly-time conditionally"
adversary_bound: "poly-size"
date_verified: 2026-08-20
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: attacker
cls_unit: circuit size
cls_tightness: quasi-poly
cls_baseline: stated
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "We give a public key encryption scheme that is provably secure against poly-size adversaries, assuming n^{(log n)^α} hardness of the standard planted clique conjecture, for any α ∈ (0,1)"
cls_evidence_src: abstract
cls_reason: "unit=circuit size, not algo class: Conjecture 1.1 itself quantifies over 'n^{(log n)^α}-size algorithms A' (§1), a non-uniform size bound; the paper's own Claim Boundary already flags that the restricted-class evidence (SQ, SOS, low-degree) is 'evidence for the assumptions' and 'not the class the security theorem quantifies over' — exactly the circuit-size-vs-algorithm-class confusion the audit warning names. tightness=quasi-poly: n^{(log n)^α} is an explicit quasi-polynomial bound, matching the sibling BW08 page and cryptography-from-planted-graphs.md's convention for this problem family. family=none, not invert: security is semantic security against the encryption scheme (Theorem 1.6), not a function-inversion game, matching the corpus convention for planted-structure PKE (cryptography-from-planted-graphs.md, pkc-from-different-assumptions.md). baseline=stated: Conjecture 1.1 states an explicit ≤1/3 advantage bound; the noisy k-LIN conjecture separately states a 1/16 bound. assessed left blank for consistency with cryptography-from-planted-graphs.md and pkc-from-different-assumptions.md."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (GHJS25) gives the **first public-key encryption scheme based on the standard planted clique conjecture** (combined with a mild auxiliary assumption about noisy k-LIN over expanders), resolving a seminal open question from Applebaum-Barak-Wigderson 2010. The construction is provably secure against poly-size adversaries assuming n^{(log n)^α}-hardness of standard planted clique for any α ∈ (0, 1). Both the planted-clique conjecture and the auxiliary noisy-k-LIN conjecture correspond to natural average-case variants of NP-complete problems studied for decades with substantial supporting evidence (SQ lower bounds, SOS lower bounds, low-degree lower bounds, unconditional lower bounds in restricted computational models).

Conceptually, this establishes planted clique as a **cryptographic primitive** — not merely an average-case hardness conjecture supporting statistical-computational gap analysis, but a building block for public-key cryptography comparable in status to LWE or factoring. This is a significant departure from 2010 (when Applebaum-Barak-Wigderson's construction required a *non-standard* variant of planted clique) and places PC in the cryptographic complexity-theoretic landscape alongside lattice and number-theoretic assumptions.

The combination of two conjectures (PC + noisy k-LIN) is not circular — each is studied independently, and neither is known to imply PKE alone. The constructions are modular and could in principle be weakened or generalized as PC understanding improves. The result bridges the statistical-computational-gap pillar (reductions among planted-style problems) with the cryptographic pillar (constructions from average-case-hard assumptions), and suggests that the two research programs converge more tightly than previously appreciated.

## Claim Boundary

- **Quantified over:** polynomial-size adversaries against the encryption scheme.
- **Antecedent:** two conjectures. The first is n^{(log n)^alpha} hardness of the standard planted clique conjecture for any alpha in (0, 1), which is a quasi-polynomial hardness assumption rather than polynomial hardness. The second is a hardness conjecture about noisy k-LIN over expanders, which the paper describes as not known to imply public-key encryption on its own. Both are conjectured.
- **Algorithm class:** all polynomial time, conditionally. The restricted-class results cited in support, in the paper's phrase unconditional lower bounds in a variety of restricted models of computation, are evidence for the assumptions and are not the class the security theorem quantifies over.
- **Does not establish:** public-key encryption from polynomial-time hardness of planted clique. The construction needs the quasi-polynomial form of the conjecture, and it needs the second conjecture as well.
- **Abstract vs theorem:** none found. The abstract names both conjectures and the quasi-polynomial exponent.

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

> "Our encryption scheme answers an open question in a seminal work by Applebaum, Barak, and Wigderson [STOC'10]."

> "Both of our conjectures correspond to natural average-case variants of NP-complete problems and have been studied for multiple decades, with unconditional lower bounds supporting them in a variety of restricted models of computation."

_Both verified verbatim against `raw/GHJS25_PKEFromPC.pdf` on 2026-08-20. An earlier rendering had altered the opening words of each, which in the second case widened "both of our conjectures" into a claim about conjectures in general._
