---
title: The Curse of Concentration in Robust Learning — Evasion and Poisoning Attacks from Concentration of Measure
type: source
date_ingested: 2026-04-12
authors: [Saeed Mahloujifar, Dimitrios I. Diochnos, Mohammad Mahmoody]
venue: AAAI
year: 2019
tags: [adversarial-ml, evasion-attacks, poisoning-attacks, concentration-of-measure, complexity-theory]
---

## Summary

This paper (MDM19) establishes a general theorem that *any* concentrated metric probability space makes *any* classifier with nontrivial error inherently vulnerable to adversarial perturbations — the "curse of concentration." The result is classifier-architecture-independent and hypothesis-class-independent: it is a property of the instance space itself.

The authors show that if a metric probability space (X, d, μ) is concentrated (any set of measure ≥ 1/2 has b-expansion covering almost all of X for small b), then for any classifier h with Ω(1) error, there is an adversary that perturbs a typical test instance by at most b to drive the error to ≈ 1. Applied to normal Lévy families (n-sphere, isotropic Gaussian, Boolean hypercube under Hamming, unit cube, unit sphere, symmetric groups, etc.), this yields O(√n) perturbation attacks as a special case, unifying prior ad-hoc existence proofs of adversarial examples.

The second main contribution extends concentration-of-measure to *poisoning attacks*. For any deterministic learning algorithm L using m training examples, there is an attacker who substitutes only Õ(√m) correctly-labeled examples and drives the probability of any initially-rare "bad property" (prob ≥ 1/poly(m)) of the output hypothesis to ≈ 1. This covers confidence degradation and targeted (chosen-instance-error) attacks. The attack is *offline* (knows future examples) — improving on earlier p-tampering attacks [MM17/MDM18] which were online but only reached O(p) error increase.

## Key Contributions

- **Theorem 1.1 (informal)**: Over any concentrated space, any classifier with constant error is vulnerable to sub-diameter adversarial perturbations that increase risk to ≈ 1.
- **Unification**: Recovers as special cases the prior existence results of Gilmer et al. (n-sphere), Fawzi-Fawzi-Fawzi (isotropic Gaussian), and Diochnos-Mahloujifar-Mahmoody (Boolean hypercube) via a single isoperimetric-inequality-free argument.
- **New attacks on Lévy families**: O(√n) adversarial-example existence over unit cube, symmetric group, and many other metric spaces not previously treated.
- **Theorem 1.2 (informal)**: For product-distribution training sets, an offline poisoner substituting Õ(√m) correctly-labeled examples drives any initially-rare bad property of the learned hypothesis to ≈ 1.
- **Target-error robustness**: Introduces robustness notion where the adversary targets a specific error probability via average-case bounded perturbations.

## Key Definitions / Theorems

- **Concentration function** α(b) = 1 − inf{μ(S_b) : μ(S) ≥ 1/2}.
- **Normal Lévy family**: concentration function ≤ k₁ exp(−k₂ b²/n).
- **Adversarial (error-region) risk** Risk_b(h, c) = Pr_{x ~ μ}[∃ x' ∈ Ball_b(x) : h(x') ≠ c(x')] = μ(E_b), where E is the error region.
- **Lemma 2.5 (Talagrand)**: For product μ on dimension n under Hamming, μ(S_b) ≥ 1 − exp(−b²/n)/μ(S).
- **Theorem 1.1**: Concentrated (X,d,μ) + Ω(1) initial error ⇒ adversary with b-perturbation drives risk to ≈ 1.
- **Theorem 1.2**: Deterministic learner L + Ω(1/poly(m)) initial bad-property probability ⇒ offline substitution-poisoner using Õ(√m) examples drives it to ≈ 1.

## Connections

- Foundational for [Concentration of Measure](../concepts/concentration-of-measure.md)
- Developed into computational version in [Computational Concentration of Measure (EMM20)](computational-concentration-of-measure-etesami.md)
- Sibling result to [Fawzi et al. 2018](adversarial-vulnerability-any-classifier.md) (smooth generative models) and Gilmer et al. 2018 (n-sphere)
- Superseded quantitatively by online p-tampering of [MM17] in the online setting; Õ(√m) offline bound here is stronger per-example
- Synthesized in [A Complexity Theoretic Approach to Adversarial ML](complexity-theoretic-adversarial-ml.md)
- Related: [Evasion Attacks](../concepts/evasion-attacks.md), [Poisoning Attacks](../concepts/poisoning-attacks.md), [p-Tampering Model](../concepts/p-tampering-model.md), [Lévy Family](../concepts/levy-family.md)
- Authors: [Saeed Mahloujifar](../entities/saeed-mahloujifar.md), [Dimitrios Diochnos](../entities/dimitrios-diochnos.md), [Mohammad Mahmoody](../entities/mohammad-mahmoody.md).

## Open Questions / Limitations

- The concentration bound is *distribution-dependent*: for "natural" data distributions (e.g., images), whether the metric probability space is concentrated (under a perceptually meaningful metric) is unknown.
- The poisoning attack requires the learner to be deterministic; randomized learners not directly covered.
- Gap remains between existence and polynomial-time computability of the attack (closed later by EMM20 on product distributions).
- Attack is offline (knows training set before substituting); fully online attacks matching these bounds remain open.

## Quotes / Notable Passages

> "We prove that for any learning problem defined over such a concentrated space, no classifier with an initial constant error (e.g., 1/100) can be robust to adversarial perturbations."

> "Our attacks of 1.2 are offline in the sense that the adversary needs to know the full training set T before substituting some of them. We note that the so-called p-tampering attacks of [MDM18] are online ... However, in that work, they could only increase the classification error by O(p) ... while here we get almost full error by only using p ≈ O(√m), which is much more devastating."
