---
title: Pseudorandomness
type: concept
tags: [cryptography, pseudorandomness, complexity-theory, computational-indistinguishability]
---

## Definition

A **pseudorandom generator (PRG)** is a deterministic polynomial-time algorithm G: {0,1}^n → {0,1}^{m(n)} with m(n) > n ("stretch") such that G(U_n) is [computationally indistinguishable](computational-indistinguishability.md) from U_{m(n)} — the uniform distribution on the larger space.

A **pseudorandom function (PRF)** is an efficiently computable keyed family {F_k : {0,1}^n → {0,1}^n} such that F_K (for random K) is computationally indistinguishable from a truly random function, given polynomially-many oracle queries.

## Intuition

Pseudorandomness lets us *stretch* a small seed of true randomness into a much larger pseudorandom string that "looks random" to any efficient observer. This is a foundational primitive in cryptography — almost every cryptographic construction ultimately rests on the existence of PRGs/PRFs.

## Properties / Theorems

**HILL Theorem (Håstad-Impagliazzo-Levin-Luby 1999)**: OWFs exist ⟺ PRGs exist. This landmark equivalence reduces all of symmetric-key cryptography (and much else) to the existence of any one-way function.

**PRG to PRF (GGM 1986 — Goldreich-Goldwasser-Micali)**: Any PRG yields a PRF via tree construction.

**Indistinguishability under adaptive queries**: PRFs remain pseudorandom even against adversaries who can adaptively query the function at inputs of their choosing — the "key" definition for most crypto applications.

## Where It Appears

- [Planting Undetectable Backdoors](../sources/planting-undetectable-backdoors.md) — digital signatures (OWF → PRF → signatures) used to plant undetectable triggers.
- [Adversarially Robust Learning Could Leverage Computational Hardness](../sources/computational-hardness-robust-learning.md) — PRF-based classifiers achieve robustness against polynomial-time adversaries that information-theoretic analysis would rule out.
- [Covert Learning](../sources/covert-learning.md) — covert learners use pseudorandomness to disguise queries as a benign distribution.
- [Win-Win Theorem](../sources/win-win-robust-learning.md) — hard-to-robustly-learn problems yield OWFs, which in turn yield PRGs.
- [Adversarial Examples from Computational Constraints](../sources/adversarial-examples-computational-constraints.md) — crypto hardness construction uses PRGs.

## Related Concepts

- [Computational Indistinguishability](computational-indistinguishability.md) — defining property.
- [One-Way Functions](one-way-functions.md) — equivalent via HILL.
- [Win-Win Theorem](win-win-theorem.md) — robust learning hardness ⟺ OWFs exist.

## Open Questions

- Unconditional construction of any non-trivial PRG (open since 1982; would imply P ≠ NP).
- Pseudorandomness in the presence of quantum adversaries — different hardness assumptions needed.
