---
title: Poisoning Attacks
type: concept
tags: [adversarial-ml, poisoning-attacks, robustness, complexity-theory, learning-theory]
---

## Definition

Poisoning attacks occur during the training phase. An adversary modifies the training dataset — by substituting, adding, or relabeling examples — with the goal of inducing the learning algorithm to choose a "bad" hypothesis. Poisoning adversaries are parameterized by their **tampering pattern** (what they can modify) and **computational power**.

**Indiscriminate attacks**: Goal is to increase overall error of trained model.  
**Targeted attacks**: Goal is to change the model's prediction on a specific target instance.  
**Abstract formulation** [Mahloujifar]: Assume an arbitrary "bad property" B over the hypothesis space. Adversary's goal: maximize the probability that the trained hypothesis satisfies B.

## Intuition

Unlike evasion attacks (which modify test inputs), poisoning adversaries corrupt the learning process itself. The adversary exploits the learner's dependence on training data: small, carefully chosen corruptions can have large downstream effects on the learned hypothesis.

## Properties / Theorems

### p-Tampering Model [MM17, MM19]
Adversary substitutes each training example with independent probability p (with a correctly-labeled example). Result: adversary can increase probability of bad property by `Ω(p)` starting from constant initial probability. Achievable in polynomial time with oracle access to training algorithm and samples.

### Adversary Choosing Tampering Locations [MDM19, EMM20]
Stronger model: adversary selects which examples to corrupt. Result: `Õ(√m)` corruptions (m = sample complexity) suffice to drive bad-property probability to almost 1, even starting from probability `1/poly(m)`. Polynomial-time algorithm [EMM20] achieves same bound using computational concentration of measure.

### Byzantine Multi-Party Poisoning [(k,p) model, MMM19]
In m-party collaborative learning with k corrupted parties (each corrupted party may send, for each message, any distribution p-close in TV to the honest one): adversary amplifies bad property probability from μ to **μ^{1−pk/m}**. For small μ this Taylor-expands to μ + Ω(pk/m · μ log(1/μ)). Generalizes:
- p-tampering (k = m): μ → μ^{1−p}
- Static k-corruption in MPC (p = 1): μ → μ^{1−k/m}

**Bounds**: Online attacks, correct labels only, polynomial-time. Technical engine is generalized p-tampering on random processes with correlated tamperable indices.

### Connection to Coin-Tossing [MM19, EMM20, MMM19]
Poisoning attack results have direct analogs for multi-party coin-tossing protocols:
- `√m` tampered messages bias average to almost 1 (single-round)
- (k,p) model: output biased from μ to μ^{1−pk/m}
- Strong-adaptive corruption [GKP15, EMM20]: adversary sees a message before deciding to corrupt it

## Where It Appears

- [A Complexity Theoretic Approach to Adversarial ML](../sources/complexity-theoretic-adversarial-ml.md) — full treatment of training-time attacks
- [Curse of Concentration (MDM19)](../sources/curse-of-concentration.md) — Õ(√m) offline substitution attacks on any deterministic learner
- [Universal Multi-Party Poisoning (MMM19)](../sources/multi-party-poisoning.md) — (k,p) Byzantine model with Ω(kp/m) bias
- [Computational Concentration (EMM20)](../sources/computational-concentration-of-measure-etesami.md) — polynomial-time matching-IT poisoning for ε ≥ 1/poly(n)
- [Extending the Formalism of Cryptography to AI](../sources/extending-formalism-cryptography-ai.md) — data poisoning and backdoor attacks in the AIOracle framework

## Related Concepts

- [p-Tampering Model](p-tampering-model.md) — the specific adversarial model for random-location poisoning
- [(k, p)-Poisoning Model](k-p-poisoning-model.md) — multi-party Byzantine generalization
- [Evasion Attacks](evasion-attacks.md) — inference-time counterpart
- [Concentration of Measure](concentration-of-measure.md) — mathematical tool underlying poisoning bounds
- [Computational Concentration of Measure](computational-concentration-of-measure.md)
- [Attack Taxonomy for LLMs](attack-taxonomy-llms.md)

## Open Questions

- What are tight bounds for poisoning in online learning settings beyond the batch model?
- Can cryptographic hardness provide provable resistance to poisoning attacks in practical settings?
- Characterizing the fundamental tradeoff between the number of parties k, tampering probability p, and achievable bias.
