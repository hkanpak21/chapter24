---
title: Backdoor Defense Evaluation
type: concept
tags: [adversarial-ml, poisoning-attacks, backdoor, evaluation-methodology]
---

## Definition

**Backdoor defense evaluation** is the empirical protocol by which a proposed backdoor countermeasure is claimed to work: a choice of attacks, datasets, architectures, poisoning rates, defender knowledge and capability assumptions, metrics, and hyperparameters, together with the reporting conventions applied to the result.

There is no accepted formalization. The literature's operative definition is a pair of numbers reported per (defense, attack, dataset, architecture) cell — **clean accuracy (CA)** and **attack success rate (ASR)** — with everything that determines those numbers left to each paper's discretion. The concept is included here because the *absence* of a formal object is the finding: three critiques in this wiki independently locate the failure in what the protocol does not fix.

## Intuition

A defense paper's claim has the shape "this defense reduces ASR to X% while keeping CA at Y%". That claim is only meaningful relative to a quantifier: for *which* attacks, at *which* poisoning rates, on *which* architectures, under *which* defender assumptions, and at *whose* hyperparameter settings. The critiques below all show the same thing from different angles: the quantifier is usually left implicit, and when it is made explicit and varied, the claim does not survive.

Three distinct failure modes have been isolated, and they should not be conflated:

1. **Attack outside the defense's declared assumptions.** The defense assumed small contiguous all-to-one triggers; the attacker used a large semantic trigger or an all-to-all objective. Not a soundness failure, but a scope failure — and one visible only if the assumption was written down.
2. **Configuration failure inside the declared threat model.** No new attack at all. The defense breaks when the network gets deeper, the poison rate changes, or the defense's own hyperparameters shift. This is [QMZ+22](../sources/critical-evaluation-backdoor-countermeasures.md)'s "non-robust case", and it is the mode most easily misdescribed as an attacker problem.
3. **Adaptive attack.** The attacker knows the defense and targets its mechanism. Once built, such an attack is largely dataset- and task-independent.

## Properties / Theorems

No theorems exist. The measured regularities:

- **Narrow evaluation is the norm.** 73% of 183 surveyed defenses evaluate only on MNIST or CIFAR-10; ImageNet-1K appears in ≈20%; the five most-used attacks have BadNets and Blended dominant and none more recent than 2021; 9 of 183 report attack stealthiness; ≈5% report execution time ([AKK+25](../sources/sok-backdoor-defense-evaluation.md)).
- **Adaptive-attacker consideration is binary and partial.** ≈58% of surveyed defenses consider one (≈55% AI venues, ≈67% security venues). It is recorded as a yes/no property of the evaluation, never as a budget.
- **Re-evaluation contradicts published claims.** Defenses that succeed on MNIST fail on ImageNet-1K, several to CA ≈ 0, across 3 000+ runs ([AKK+25](../sources/sok-backdoor-defense-evaluation.md)).
- **Worst-case success does not imply easy-case success.** Compatibility clustering fails against plain BadNets at 93.8% ASR ([AKK+25](../sources/sok-backdoor-defense-evaluation.md)) — refuting a widely assumed monotonicity.
- **Failure without any attacker escalation is real and demonstrated.** Neural Cleanse is provably non-applicable to binary classifiers and fails on deep networks; ABS fails at an ordinary poisoning rate and under weight-perturbation constraints; MNTD fails on single-model judgement and under small hyperparameter deviation — all inside their declared threat models, with no adaptive attack ([QMZ+22](../sources/critical-evaluation-backdoor-countermeasures.md)).
- **Mechanism premises falsify easily.** Fine-pruning's neuron-separation premise breaks by retraining the same BadNet with a different learning rate; ABS's single-backdoor-neuron premise breaks under a conjunction trigger ([VG20](../sources/evaluating-nn-backdoor-defenses.md)).
- **MADS** ([AKK+25](../sources/sok-backdoor-defense-evaluation.md)): mean absolute deviation of a defense's ASR across datasets under fixed settings, the field's first cross-dataset consistency statistic.

## Where It Appears

- [SoK: The Last Line of Defense (AKK+25)](../sources/sok-backdoor-defense-evaluation.md) — 183 papers, 3 000+ re-runs, R1–R9 and C1–C8.
- Evasion-side precedents for the same critique: [On Evaluating Adversarial Robustness](../sources/on-evaluating-adversarial-robustness.md), [Obfuscated Gradients](../sources/obfuscated-gradients.md), [On Adaptive Attacks to Adversarial Example Defenses](../sources/adaptive-attacks-defenses.md), [SoK: Pitfalls in Evaluating Black-Box Attacks](../sources/sok-black-box-attack-pitfalls.md).
- [Towards a Critical Evaluation of Robustness for DL Backdoor Countermeasures (QMZ+22)](../sources/critical-evaluation-backdoor-countermeasures.md) — the non-robust-case category.
- [On Evaluating Neural Network Backdoor Defenses (VG20)](../sources/evaluating-nn-backdoor-defenses.md) — the earliest three-pitfall statement.
- [Dos and Don'ts of Machine Learning in Computer Security (AQP+22)](../sources/dos-and-donts-ml-security.md) — pitfall P10, the field-wide parent.

## Related Concepts

- [Poisoning Attacks](poisoning-attacks.md), [Undetectable Backdoors](undetectable-backdoors.md), [Defendability](defendability.md), [Input Manipulation Threat Model](input-manipulation-threat-model.md), [Unit of Protection](unit-of-protection.md).
- [Adaptive Attacks](adaptive-attacks.md) — failure mode 3 above, developed in the evasion setting.
- [Adversary Knowledge Taxonomy](adversary-knowledge-taxonomy.md) — the knowledge axis, which is what "adaptive" records; distinct from a resource budget.

## Open Questions

- **No resource-indexed success criterion exists.** Not one of the 183 papers surveyed, nor any of the three critiques, defines a defense as holding against attackers within a stated compute, query, sample or poisoning budget. Adaptiveness is knowledge, not cost. This is the strand's central gap: the field measures a computational quantity — how much effort defeats this defense — without ever naming it.
- The natural bridge is to the theory side, where the quantities *are* named: [Planting Undetectable Backdoors](../sources/planting-undetectable-backdoors.md), [iO-Undetectable Backdoors in Neural Networks](../sources/io-undetectable-backdoors-nn.md), [Oblivious Defense Against Backdoor Removal](../sources/oblivious-defense-backdoor-removal.md), [Backdoor Defense, Learnability and Obfuscation](../sources/backdoor-defense-learnability-obfuscation.md), [Certified Defenses for Data Poisoning](../sources/certified-defenses-data-poisoning.md). AKK+25 asks for exactly this bridge in its closing paragraph and cites none of that literature.
- Is there a formal separation between the three failure modes above? Modes 1 and 3 are attacker-side; mode 2 is defense-side. A definition that distinguishes them would let a paper state which one it has ruled out.
- No inter-rater reliability, and no shared baseline table, exists for any of the coded surveys.
