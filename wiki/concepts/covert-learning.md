---
title: Covert Learning
type: concept
tags: [cryptography, learning-theory, pseudorandomness, PAC-learning, computational-indistinguishability]
---

## Definition
A learner L is **(ε, δ)-covert** for a concept class C with respect to a reference transcript distribution R if: (1) L is an (ε, δ)-PAC learner for C, and (2) for every concept c ∈ C the joint distribution of queries and responses produced by L^c is computationally indistinguishable from R. The adversary is an efficient observer of the query channel.

## Intuition
Learning that looks like "nothing is happening": the interaction between learner and oracle/data source must be indistinguishable from a benign, non-learning transcript (e.g., random queries). This is the learning analogue of covert/steganographic communication, and a strictly adversarial strengthening of active learning where queries must not only be efficient but also *hide* what is being learned.

## Properties / Theorems
- **Positive results under crypto assumptions**: Parities with membership queries are covertly learnable under LPN; additional classes under LWE.
- **Win-win lower bounds**: covert learnability of classes outside SQ ⇒ one-way functions exist.
- **Composition**: covertness is preserved under standard PAC reductions when the simulator can efficiently produce reference transcripts.
- Covertness is incomparable to differential privacy (different adversary: DP adversary sees output model; covert adversary sees query transcript).

## Where It Appears
- [covert-learning](../sources/covert-learning.md) (Canetti & Karchmer, 2021).
- Connects to win-win style theorems in [win-win-robust-learning](../sources/win-win-robust-learning.md).

## Related Concepts
- [statistical-query-model](statistical-query-model.md) — SQ-learnability is the natural complement to covertness.
- [pseudorandomness](pseudorandomness.md), [computational-indistinguishability](computational-indistinguishability.md).
- [win-win-theorem](win-win-theorem.md) — same reductive pattern (learning demand ⇒ crypto primitive).

## Open Questions
- Covert learnability under adaptive / stateful observers.
- Covert learning from i.i.d. samples only (no queries): is it equivalent to SQ?
- Relationship to differential privacy and secure multi-party computation in distributed learning.
