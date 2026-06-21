---
title: "Backdoor Defense, Learnability, and Obfuscation"
type: source
date_ingested: 2026-04-23
authors: [Paul Christiano, Jacob Hilton, Victor Lecomte, Mark Xu]
venue: "arXiv:2409.03077 (Sep 2024); ITCS 2025 (LIPIcs Vol. 325, Paper 38)"
year: 2025
tags: [backdoor, PAC-learning, indistinguishability-obfuscation, VC-dimension, defendability, complexity-theory]
---

## Summary

This paper (CHLX25) introduces a **formal game-theoretic notion of ε-defendability** against backdoor attacks and proves it sits as a *distinct* complexity-theoretic concept between efficient PAC learnability and indistinguishability obfuscation. The game: an attacker modifies a function to disagree on a randomly-chosen trigger x* (but agree almost everywhere else); the defender must detect whether a given input is the trigger. The key constraint making defense possible is that the attacker's strategy must work for a *randomly-chosen* trigger, not an adversarially-chosen one.

The paper establishes four main results:

1. **Statistical defendability (Section 4)**: A representation class F is ε-defendable with confidence → 1 **iff ε = o(1/VC(F))**, via a voting algorithm adapted from Hanneke et al. 2022. This mirrors the VC-dimension characterization of PAC learnability.

2. **Computational defendability (Section 5)**: Efficient PAC learnability *implies* efficient defendability, but **not conversely**. The set of efficiently-defendable classes lies *strictly between* efficiently-learnable classes and all classes.

3. **iO + puncturable PRF → polynomial-size circuits not efficiently defendable**: A hybrid argument combining an efficient indistinguishability obfuscator with a puncturable pseudorandom function shows that the class of polynomial-size circuits cannot be efficiently defended.

4. **Decision trees defendable in single evaluation (Section 6)**: Under uniform input distribution, polynomial-size decision trees are efficiently defendable in the time it takes to evaluate a single tree — a natural example where **defense is strictly faster than learning**.

The conceptual contribution is significant: "**defendability**" emerges as a new complexity-theoretic notion with a clean hierarchy: PAC learnability ⊂ defendability ⊂ arbitrary classes. The paper's conclusion connects to AI alignment — if a model class is not efficiently defendable, backdoor removal is computationally intractable under standard cryptographic assumptions, limiting the scope of "mechanistic" defense strategies.

## Key Contributions

- **Definition of ε-defendability (Section 3)**: game between attacker and defender; attacker must work for a randomly-chosen trigger.
- **Statistical defendability characterization**: F is ε-defendable iff ε = o(1/VC(F)), via Hanneke-style voting.
- **Computational defendability hierarchy**: learnable ⊊ defendable ⊊ all; strict separation.
- **iO-based non-defendability of polynomial circuits**: applied hybrid argument (puncturable PRF + iO).
- **Decision trees: defense strictly easier than learning**: natural class where defendability is faster than PAC learning.
- **Mechanistic defense direction**: the decision-tree result hints at "mechanistic" (structure-based) defenses for specific classes — a template for practical defendability that doesn't require full PAC learning.

## Key Definitions / Theorems

- **ε-defendability game (Definition 3.1)**: (1) attacker chooses (D, f ∈ F); (2) trigger x* sampled from D; (3) attacker chooses f* ∈ F with Pr_{x~D}[f*(x) ≠ f(x)] ≤ ε but f*(x*) ≠ f(x*); (4) defender, given either (f, x~D) or (f*, x*), must distinguish.
- **Statistical defendability (Theorem 4.x)**: F is ε-defendable with confidence → 1 iff ε = o(1/VC(F)).
- **Efficient defendability**: Definition 5.x — the defender runs in polynomial time.
- **Theorem 5.x (efficient PAC ⇒ efficient defendable)**: if F is efficiently PAC-learnable, then F is efficiently defendable.
- **Theorem 5.x (converse fails)**: efficient defendability does not imply efficient PAC learnability (example: random functions over {0,1}^n).
- **Theorem 5.y (iO non-defendability)**: under iO + puncturable PRF, polynomial-size circuits are not efficiently defendable.
- **Theorem 6.x (decision trees)**: polynomial-size decision trees over uniform distribution are ε-defendable in O(tree-evaluation-time) for ε = O(1/tree-size).

## Connections

- Source: [Planting Undetectable Backdoors (GKVZ22)](planting-undetectable-backdoors.md) — establishes backdoor-detection-impossibility; CHLX25 introduces defendability as a distinct, sometimes-tractable concept.
- Source: [Oblivious Defense (Goldwasser-Shafer-Vafa-Vaikuntanathan, STOC 2025)](oblivious-defense-backdoor-removal.md) — concurrent work on mitigation-without-detection; complementary. CHLX25 explicitly references GSVV25 as concurrent.
- Source: [Filter Impossibility (Ball et al. 2025)](filter-impossibility-ai-alignment.md) — LLM filter-specific instance of the defendability framework's negative side.
- Source: [Unelicitable Backdoors (Draguns et al. 2024)](unelicitable-backdoors-lms.md) — strengthens GKVZ22; CHLX25's iO non-defendability is the matching abstract theorem.
- Source: [Adversarial Examples from Computational Constraints (BPR19)](adversarial-examples-computational-constraints.md) — analog for adversarial examples; similar "statistical possible, computational hard" pattern noted in CHLX25.
- Source: [Adversarially Robust Learning Could Leverage Computational Hardness (Garg et al. 2020)](computational-hardness-robust-learning.md) — same theme: using crypto for offense-defense asymmetry.
- Concept: [PAC Learning](../concepts/pac-learning.md) — defendability is the new peer concept.
- Concept: [Undetectable Backdoors](../concepts/undetectable-backdoors.md) — defendability is the complementary positive-side concept.
- Concept: [Defendability](../concepts/defendability.md) — **new concept page needed**.
- Concept: [Indistinguishability Obfuscation (iO)](../concepts/indistinguishability-obfuscation.md) — **new concept page needed**.
- Concept: [Pseudorandomness](../concepts/pseudorandomness.md) — puncturable PRFs are the primary building block of the iO non-defendability result.
- Concept: [Win-Win Theorem](../concepts/win-win-theorem.md) — CHLX25 extends this to a three-way hierarchy (learnable/defendable/obfuscatable).
- Authors: Paul Christiano (formerly OpenAI / now Alignment Research Center), Jacob Hilton, Victor Lecomte, Mark Xu (new entities).

## Open Questions / Limitations

- **Efficient defendability vs. efficient learnability — tight separation**: CHLX25 gives a non-trivial gap but a complete characterization of the "defendable but not learnable" region remains open.
- **Natural classes beyond decision trees**: does a broader set of structurally-interesting classes admit fast defense? Candidates: sparse halfspaces, low-rank matrix predictors.
- **Non-uniform distributions for decision trees**: result is specific to uniform input distribution.
- **"Mechanistic" defenses**: the decision-tree result hints at structure-exploiting defenses; formalizing a general "mechanistic defense" framework is open.
- **Composition of defenders**: if two classes are defendable, are their products/compositions defendable?
- **LLM application**: how does the abstract defendability framework instantiate for modern LLM architectures?
- **Relation to adversarial robustness**: can robust-PAC-learning be reformulated within the defendability game?

## Quotes / Notable Passages

> "We introduce a formal notion of defendability against backdoors using a game between an attacker and a defender. ... The key constraint on the attacker that makes defense possible is that the attacker's strategy must work for a randomly-chosen trigger."

> "We identify efficient defendability as a notable intermediate concept in between efficient learnability and obfuscation."

> "We use indistinguishability obfuscation to show that the class of polynomial size circuits is not efficiently defendable."

> "Under certain cryptographic assumptions, the class of polynomial size circuits is not efficiently defendable, by combining a puncturable pseudorandom function with an efficient indistinguishability obfuscator."
