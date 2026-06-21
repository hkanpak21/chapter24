---
title: Covert Learning — How to Learn with an Untrusted Intermediary
type: source
date_ingested: 2026-04-12
authors: [Ran Canetti, Ari Karchmer]
venue: TCC (Theory of Cryptography Conference)
year: 2021
tags: [cryptography, learning-theory, covert-computation, pseudorandomness, PAC-learning]
---

## Summary
Canetti and Karchmer introduce *covert learning*: a formal model in which a learner interacts with an oracle for a target concept (or with a data source) and must PAC-learn the concept while keeping the sequence of queries and responses computationally indistinguishable from a fixed, benign "reference" distribution — so that an efficient observer cannot tell that learning is happening or infer anything about the concept being learned.

The paper bridges learning theory and cryptography: covertness is defined via an indistinguishability game in the style of semantic security, and positive results are obtained under standard cryptographic assumptions (LPN/LWE) while negative results show that covert learning of certain classes implies one-way functions or lower bounds on learning complexity. The authors give covert learners for classes including parities, decision trees, and halfspaces under distributional assumptions, and explore how covertness composes with query-based learning (membership queries, SQ).

The work situates covert learning alongside active learning, differentially private learning, and secure computation, but targets a distinct threat: a passive eavesdropper on the query channel. It provides a clean game-based definition amenable to reductions.

## Key Contributions
- Formal definition of covert learning: a PAC learner whose transcript (queries + responses) is computationally indistinguishable from a canonical "innocent" transcript distribution.
- Constructions of covert learners for several classes under LPN/LWE-style assumptions.
- Impossibility/lower-bound results linking covert learnability to cryptographic primitives.
- Connections to membership-query learning, SQ learning, and active learning under adversarial observation.

## Key Definitions / Theorems
- **Covert PAC learning (def.)**: Learner L is (ε, δ)-covert for concept class C w.r.t. reference distribution R if (i) L (ε, δ)-PAC-learns C and (ii) for every c ∈ C, the transcript of L^c is computationally indistinguishable from R.
- **Theorem (positive)**: Under LPN, parities over {0,1}^n are covertly learnable with membership queries.
- **Theorem (negative / win-win)**: If class C is covertly learnable but not SQ-learnable, then one-way functions exist (cryptographic hardness of learning emerges from covertness demand).

## Connections
- Uses [pseudorandomness](../concepts/pseudorandomness.md), [computational indistinguishability](../concepts/computational-indistinguishability.md).
- Related to [statistical-query-model](../concepts/statistical-query-model.md) and [PAC-learning](../concepts/pac-learning.md).
- Win-win style reductions echo [win-win-theorem](../concepts/win-win-theorem.md) (Degwekar et al.).
- Authors: [Ran Canetti](../entities/ran-canetti.md), [Ari Karchmer](../entities/ari-karchmer.md).

## Open Questions / Limitations
- Covert learnability of broader classes (e.g., halfspaces over general distributions) unresolved.
- Whether covert learning relative to *adaptive* observers requires stronger primitives.
- Interaction with differential privacy: is covertness strictly stronger or incomparable?

## Quotes / Notable Passages
"The learner's interaction with the world should look, to any computationally bounded observer, like an interaction that could have been generated without any learning taking place."
