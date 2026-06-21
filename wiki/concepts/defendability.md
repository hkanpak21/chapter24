---
title: Defendability
type: concept
tags: [backdoor, defendability, complexity-theory, PAC-learning, indistinguishability-obfuscation]
---

## Definition

**Defendability** [Christiano-Hilton-Lecomte-Xu, ITCS 2025] is a complexity-theoretic notion measuring whether backdoors in a function class F can be detected at runtime. Formally, F is **ε-defendable with confidence 1 − δ** if there exists a probabilistic detection algorithm D that wins the following game with probability ≥ 1 − δ:

1. Attacker chooses distribution D' and function f ∈ F.
2. A trigger x* is sampled randomly from D'.
3. Attacker chooses a backdoored f* ∈ F with Pr_{x ~ D'}[f*(x) ≠ f(x)] ≤ ε but f*(x*) ≠ f(x*).
4. Defender, given either (f, x ~ D') or (f*, x*), distinguishes with probability ≥ 1 − δ.

**Efficient defendability** additionally requires D to run in polynomial time.

## Intuition

Defendability is the *positive-side* complement to the negative undetectable-backdoors impossibility results of Goldwasser-Kim-Vaikuntanathan-Zamir 2022. Unlike detection-of-a-backdoored-model (which is often impossible under cryptographic assumptions), *runtime detection of whether a specific input activates a backdoor* can be tractable — under restrictions on the attacker's strategy.

The key constraint making defense possible: the attacker's backdoor must work for a *randomly-chosen* trigger, not an adversarially-chosen one. Without this, there is a symmetry between the original and backdoored functions that makes defense impossible.

## Properties / Theorems

**Statistical defendability (Theorem, computationally unbounded defender)** [CHLX25]: F is ε-defendable with confidence → 1 **iff ε = o(1/VC(F))**. Achievable via Hanneke-style voting.

**Hierarchy**: efficiently-PAC-learnable ⊊ efficiently-defendable ⊊ all classes.

**Efficient PAC ⇒ Efficient defendable**: any efficiently-PAC-learnable class is efficiently defendable.

**Converse fails**: efficient defendability does *not* imply efficient PAC learnability. Random functions over {0,1}^n are efficiently defendable but not PAC-learnable.

**iO non-defendability**: under indistinguishability obfuscation + puncturable PRFs, polynomial-size circuits are **not** efficiently defendable.

**Decision trees defendable in single evaluation**: polynomial-size decision trees under uniform input distribution are ε-defendable in O(tree-evaluation-time) for ε = O(1/tree-size) — a natural example where defense is strictly easier than learning.

**Defensibility vs. Detectability** [Goldwasser-Shafer-Vafa-Vaikuntanathan, STOC 2025]: independently of the defendability framework, backdoor *mitigation* can succeed (remove the backdoor's effect) even when *detection* fails (identifying the backdoor's presence). This establishes detection, defendability, and mitigation as three distinct complexity-theoretic quantities.

## Where It Appears

- [Backdoor Defense, Learnability, and Obfuscation](../sources/backdoor-defense-learnability-obfuscation.md) — where defendability is defined and characterized.
- [Oblivious Defense in ML Models](../sources/oblivious-defense-backdoor-removal.md) — concurrent/complementary work; mitigation without detection.
- [Planting Undetectable Backdoors (GKVZ22)](../sources/planting-undetectable-backdoors.md) — the negative-side detection impossibility that defendability responds to.
- [Filter Impossibility for AI Alignment](../sources/filter-impossibility-ai-alignment.md) — LLM-specific instance of non-defendability via cryptographic hardness.

## Related Concepts

- [PAC Learning](pac-learning.md) — efficient PAC ⇒ efficient defendability; sibling complexity concept.
- [Undetectable Backdoors](undetectable-backdoors.md) — negative side; GKVZ22.
- [Indistinguishability Obfuscation](indistinguishability-obfuscation.md) — non-defendability for polynomial circuits uses iO + puncturable PRF.
- [Pseudorandomness](pseudorandomness.md) — puncturable PRFs used in non-defendability proof.
- [Win-Win Theorem](win-win-theorem.md) — defendability extends this to a three-way hierarchy.

## Open Questions

- Which natural classes beyond decision trees admit fast defense? Candidates: sparse halfspaces, low-rank matrix predictors.
- Can a "mechanistic defense" framework be formalized (structure-exploiting defenses)?
- Composition: are products/compositions of defendable classes defendable?
- LLM instantiation: how does the abstract defendability framework apply to modern transformer architectures?
- Relation to adversarial-robustness PAC learning: can robust-PAC be reformulated as defendability?
