---
title: Evasion Attacks
type: concept
tags: [adversarial-ml, evasion-attacks, robustness, complexity-theory]
---

## Definition

Evasion attacks (also: inference-time attacks, adversarial examples) occur during the inference phase. An adversary perturbs a test input x to produce x' such that: (1) d(x, x') ≤ ε for some budget ε and distance metric d, and (2) a classifier h satisfies h(x') ≠ h(x) or h(x') ≠ y (the true label).

**Adversarial risk (error region definition)**: The adversarial risk of classifier h under adversary budget ε is the probability over (x, y) ~ D that there exists x' with d(x,x') ≤ ε and h(x') ≠ y. This definition is the preferred one under a stability assumption on the ground truth distribution.

## Intuition

Unlike standard test-set errors, evasion adversaries actively search for the worst-case perturbation. Even a classifier that achieves near-zero standard error may have high adversarial risk if its decision boundary is close to the data manifold — which, as [concentration of measure](concentration-of-measure.md) implies, is guaranteed in high dimensions for any classifier with nontrivial error.

## Properties / Theorems

**Inherent upper bound** [DMM18, MDM19]: Any classifier with constant error rate on a concentrated metric probability space has adversarial risk approaching 1 under sub-linear perturbations. This is architecture-independent.

**Adversarial vs. standard sample complexity** [DMM19]: There exists a learning problem where standard learning requires polynomial samples but adversarially robust learning requires exponential samples. Adversarial risk can impose exponential sample complexity costs.

**Polynomial-time attacks** [MM19, EMM20]: On product distributions under Hamming distance, polynomial-time evasion attacks with `O(√n)` perturbations exist and are asymptotically optimal, matching information-theoretic bounds.

**Robustness definitions can differ** [DMM18]: Different natural definitions of adversarial robustness can yield significantly different results. A stability assumption on the ground truth reconciles them to the error region definition.

## Where It Appears

- [A Complexity Theoretic Approach to Adversarial ML](../sources/complexity-theoretic-adversarial-ml.md) — primary focus of inference-time attacks section
- [Curse of Concentration (MDM19)](../sources/curse-of-concentration.md) — general impossibility: concentrated space ⇒ adversarial examples for any classifier
- [Adversarial Vulnerability for Any Classifier (FFF18)](../sources/adversarial-vulnerability-any-classifier.md) — classifier-agnostic upper bound under smooth generative models; transferability theorem
- [Computational Concentration (EMM20)](../sources/computational-concentration-of-measure-etesami.md) — poly-time Õ(√n) evasion matching IT bounds
- [Adversarial Examples from Computational Constraints (BLPR19)](../sources/adversarial-examples-computational-constraints.md) — crypto hardness gives learning problems with IT-robust-but-computationally-not
- [Empirically Measuring Concentration (MZME19)](../sources/empirically-measuring-concentration.md) — empirical gap analysis
- [Extending the Formalism of Cryptography to AI](../sources/extending-formalism-cryptography-ai.md) — instruction hijacking, prompt injection in agentic systems are the LLM analogue

## Related Concepts

- [Concentration of Measure](concentration-of-measure.md) — source of inherent upper bound
- [Computational Concentration of Measure](computational-concentration-of-measure.md) — enables efficient attacks
- [Intrinsic Robustness](intrinsic-robustness.md) — distribution-level robustness ceiling
- [Isoperimetry and Robustness](isoperimetry-and-robustness.md)
- [Poisoning Attacks](poisoning-attacks.md) — training-time counterpart
- [Attack Taxonomy for LLMs](attack-taxonomy-llms.md) — evasion generalized to LLMs

## Open Questions

- Are there natural distribution families where computational hardness provably limits evasion attacks below the concentration-of-measure upper bound?
- What is the tight sample complexity of adversarially robust PAC learning for general concept classes?
