---
title: p-Tampering Model
type: concept
tags: [poisoning-attacks, adversarial-ml, cryptography, tampering, complexity-theory]
---

## Definition

The **p-tampering model** [Austrin et al.; Mahloujifar & Mahmoody] is an adversarial model for randomized algorithms/learning processes in which a computationally efficient adversary can tamper with each element of a sequence (bits, blocks, training examples) with independent probability p, in an *online* fashion.

**Original setting** (Austrin et al., bitwise): An efficient virus controls each bit of the randomness used by a randomized algorithm with independent probability p. Applied to cryptographic primitives.

**Blockwise extension** [MM17]: Generalized to blockwise setting — adversary controls entire blocks of randomness with independent probability p. New p-tampering attacks break the semantic security of any encryption scheme.

**ML setting** [MM17, MM19]: Adversary substitutes each training example in a sequence with probability p, replacing it with an adversarially chosen (correctly-labeled) example. Can work online, with only black-box access to the training algorithm.

## Intuition

The p-tampering model captures a "probabilistic virus" — an adversary who can "infect" each unit of input with some probability, but has no global view of which other units were infected. Despite these severe restrictions (online, independent, correct-labels-only), such adversaries are provably powerful against both cryptographic primitives and learning algorithms.

The reason: even a small probability of control over each piece of the input gives statistical leverage over the aggregate output. This is analogous to how a small amount of noise in each vote can still swing an election.

## Properties / Theorems

**Breaking encryption** [MM17]: Blockwise p-tampering attacks break the semantic security of any encryption scheme.

**Impossibility of randomness extraction** [MM17]: p-tampering attacks prove the impossibility of extracting an unbiased random bit from blockwise Santha-Vazirani sources.

**ML poisoning bound** [MM17, MM19]: In p-tampering model on training examples, adversary can increase bad-property probability by `Ω(p)` from any constant initial probability. Polynomial-time attack with oracle access.

**Coin tossing implication**: In single-round m-party coin tossing, a p-tampering adversary (who tampers each message with probability p) can bias the output by `Ω(p)`.

## Where It Appears

- [A Complexity Theoretic Approach to Adversarial ML](../sources/complexity-theoretic-adversarial-ml.md) — ML applications
- [Curse of Concentration (MDM19)](../sources/curse-of-concentration.md) — offline variant: Õ(√m) substitutions drive bad-property probability to ≈1
- [Universal Multi-Party Poisoning (MMM19)](../sources/multi-party-poisoning.md) — extended to (k,p) model across m parties
- [Computational Concentration (EMM20)](../sources/computational-concentration-of-measure-etesami.md) — poly-time choose-locations variant exponentially stronger than p-tampering
- Related to tamperable cryptography literature (Austrin et al. 2017)

## Related Concepts

- [Poisoning Attacks](poisoning-attacks.md) — p-tampering is a specific model within poisoning
- [(k, p)-Poisoning Model](k-p-poisoning-model.md) — multi-party generalization
- [Computational Concentration of Measure](computational-concentration-of-measure.md) — enables polynomial-time p-tampering attacks
- [Concentration of Measure](concentration-of-measure.md)

## Open Questions

- What is the tight relationship between p-tampering power and the signal-to-noise structure of the underlying learning problem?
- Can p-tampering attacks be resisted by randomized training algorithms that do not expose individual training examples to the adversary?
