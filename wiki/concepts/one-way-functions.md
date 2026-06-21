---
title: One-Way Functions (OWFs)
type: concept
tags: [cryptography, one-way-functions, complexity-theory, hardness-reductions]
---

## Definition

A function f: {0,1}* → {0,1}* is a **one-way function** if:
1. f is computable in polynomial time, and
2. for every PPT adversary A, Pr_{x ~ U_n}[A(1^n, f(x)) ∈ f^{-1}(f(x))] is negligible in n.

OWFs are the "minimal" primitive of Minicrypt (Impagliazzo's worlds). Existence of OWFs is equivalent to existence of pseudorandom generators, pseudorandom functions, digital signatures (Rompel 1990), commitment schemes, and symmetric-key encryption.

## Intuition

Easy to compute, hard to invert. The canonical cryptographic assumption: believed to hold (e.g., based on factoring, discrete log, AES), but unprovable without settling P vs NP.

## Properties / Theorems

- **Rompel (1990)**: OWFs ⇒ existentially unforgeable digital signatures for short messages. Used in GJMM20 and Goldwasser-Kim-Vaikuntanathan-Zamir for undetectable backdoors.
- **Equivalent to PRGs / PRFs** (Håstad–Impagliazzo–Levin–Luby).
- **Win-win for robust learning** (Degwekar–Nakkiran–Vaikuntanathan 2019): hardness of robust learning ⇒ OWFs exist.
- **Computational–IT robustness gap** (Garg–Jha–Mahloujifar–Mahmoody 2020): OWFs suffice to construct learning tasks with meaningful gap.
- **Undetectable backdoors** (Goldwasser–Kim–Vaikuntanathan–Zamir 2022): OWFs ⇒ model backdoors that are cryptographically undetectable given full white-box access.

## Where It Appears

- [Win-Win Robust Learning](../sources/win-win-robust-learning.md)
- [Computational Hardness for Robust Learning](../sources/computational-hardness-robust-learning.md)
- [Planting Undetectable Backdoors](../sources/planting-undetectable-backdoors.md)

## Related Concepts

- [Win-Win Theorem](win-win-theorem.md)
- [Computational vs IT Robustness](computational-vs-it-robustness.md)
- [Undetectable Backdoors](undetectable-backdoors.md)

## Open Questions

- Can OWFs be replaced by weaker assumptions (e.g., average-case hardness of single NP problems) in ML-security constructions?
- Structural (minimum complexity) OWF assumptions sufficient for adversarial ML separations?
