---
title: Computational Indistinguishability
type: concept
tags: [cryptography, computational-complexity, pseudorandomness, security-definitions]
---

## Definition

Two distribution ensembles {X_n} and {Y_n} over {0,1}* are **computationally indistinguishable** if for every probabilistic polynomial-time (PPT) distinguisher D, every polynomial p, and all sufficiently large n:

|Pr[D(X_n) = 1] − Pr[D(Y_n) = 1]| < 1/p(n)

(i.e., the distinguisher's advantage is negligible as a function of n.)

Written **X_n ≈_c Y_n**.

## Intuition

Two distributions may be statistically very different (e.g., pseudorandom output vs. uniform) but no polynomial-time algorithm can tell them apart with non-negligible advantage. Computational indistinguishability is the foundational tool for defining security in modern cryptography — from pseudorandom generators to public-key encryption (IND-CPA, IND-CCA) to zero-knowledge proofs.

## Properties / Theorems

**Closure under efficient operations**: If X ≈_c Y and f is PPT-computable, then f(X) ≈_c f(Y).

**Hybrid argument**: To prove X_1 ≈_c X_k, it suffices to prove X_i ≈_c X_{i+1} for i = 1, ..., k-1, as long as k = poly(n). Standard proof technique for security reductions.

**Relation to pseudorandomness**: A PRG G is secure iff G(U_n) ≈_c U_{m(n)} (its output is indistinguishable from true randomness).

**Not transitive in general with statistical distance**: X ≈_c Y and Y ≈_s Z does not imply X ≈_c Z (though computational ≈_c is transitive).

## Where It Appears

- [Covert Learning](../sources/covert-learning.md) — learner's query sequence must be computationally indistinguishable from a reference distribution.
- [Planting Undetectable Backdoors](../sources/planting-undetectable-backdoors.md) — backdoored model must be computationally indistinguishable from honest model to any efficient auditor.
- [Win-Win Theorem](../sources/win-win-robust-learning.md) — the OWF direction of the win-win theorem rests on computational indistinguishability of pseudorandom vs. uniform.
- [Extending Formalism of Cryptography to AI](../sources/extending-formalism-cryptography-ai.md) — AIOracle security games use IND-style definitions.

## Related Concepts

- [Pseudorandomness](pseudorandomness.md) — application: PRG outputs ≈_c uniform.
- [One-Way Functions](one-way-functions.md) — equivalent to computational indistinguishability of several natural distributions.
- [Statistical-Computational Gaps](statistical-computational-gaps.md) — analog at the statistical-inference level.

## Open Questions

- Whether unconditional computational indistinguishability can be proven for any natural distribution pair (would imply P ≠ NP and more).
