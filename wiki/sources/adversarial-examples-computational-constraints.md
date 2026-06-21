---
title: Adversarial Examples from Computational Constraints
type: source
date_ingested: 2026-04-12
authors: [Sébastien Bubeck, Yin Tat Lee, Eric Price, Ilya Razenshteyn]
venue: ICML
year: 2019
tags: [adversarial-ml, evasion-attacks, cryptography, complexity-theory, one-way-functions, sample-complexity]
---

## Summary

This paper (BLPR19) provides the first formal *computational* explanation for adversarial examples — i.e., a learning problem that is (a) information-theoretically robustly learnable with polynomial samples, but (b) *no polynomial-time learner* can produce a robust classifier under standard cryptographic assumptions. The result decouples statistical from computational robustness: robustness is information-theoretically possible, but computational intractability forces any efficient learner to produce vulnerable classifiers.

NOTES: _Key notion here is that we intract information theoretical robustness from computational robustness, hence we achieve information theoretically robust being the learner against an adversarial example inputting adversary (What is the computational model for this adversarial example creator? What can it see) yet there is no PPT learner that can be robust against this adversary_

The construction uses a distribution based on pseudorandom functions / one-way functions: honest data is labeled by a planted cryptographic key, so statistically any Bayes-optimal classifier is robust, but efficient learners cannot distinguish the planted structure from random noise in polynomial time and so produce classifiers whose decision boundary contains many adversarial perturbations.

NOTES: _Key detail to note here is that we build a distribution based on a cryptographic function. A key thing may be on relaxing the cryptographical hardness on the data distribution instance so that we can state certain things in a practical and learnable manner._

NOTES: _One another thing comes to my mind is to have a mid way among cryptographical distributions and statistically learnable distributions. Maybe treating both in a same way giving lowerbounds on weak crypto or having a hard problem being similar to a cryptographical instance._

The authors also give a statistical lower bound: there is a learning problem where the *sample complexity* of robust learning is super-polynomially larger than that of non-robust learning, providing a statistical explanation that complements later work by Schmidt et al. Conversely, they show computational hardness is *necessary*: for a broad class of natural hypothesis classes, if unbounded computation is allowed, robust learning is possible with polynomial samples.

Taken together, the paper is the dual of the [Win-Win (DNV19)](win-win-robust-learning.md) theorem: DNV19 shows robust-learning hardness implies OWF; BLPR19 shows OWF implies robust-learning hardness. Both conclude that cryptographic complexity is the right lens on computational robustness barriers.

## Key Contributions

- **Computational lower bound (main theorem)**: Under standard crypto assumptions (existence of OWFs / secure PRFs), there is a learning problem that is information-theoretically robustly PAC-learnable with poly(n) samples but no polynomial-time algorithm can produce a robust classifier.

NOTES: What is a learning problem and what is PAC-learnable.

- **Construction via PRFs**: Data points have labels determined by a pseudorandom function on a secret key; Bayes-optimal classifier (computing the PRF) is robust; efficient classifiers cannot reproduce this.
- **Statistical lower bound**: A separate construction gives a problem where robust learning requires exponentially more samples than standard learning.
- **Positive direction**: For standard concept classes (e.g., halfspaces), allowing unbounded computation recovers polynomial-sample robust learnability — showing the obstruction is specifically computational.
- **Foundational framing**: First paper to formally posit that adversarial examples may arise from *computational constraints* rather than statistical or geometric obstructions.

## Key Definitions / Theorems

- **Robust PAC learning**: Learner must output h with Pr_{x~μ}[∃ x' ∈ Ball_ε(x) : h(x') ≠ c(x)] ≤ α.
- **Main theorem (informal)**: Assuming OWFs, ∃ concept class C and distribution μ such that C is (α,ε)-robustly learnable information-theoretically with poly(n) samples, but no polynomial-time learner achieves adversarial risk ≤ α even given poly(n) samples.
- **Statistical separation**: ∃ problem where standard PAC sample complexity is poly(n) but robust PAC sample complexity is 2^{Ω(n)}.

## Connections

- Dual of [Win-Win Theorem (Degwekar-Nakkiran-Vaikuntanathan 2019)](win-win-robust-learning.md) / [win-win-theorem concept](../concepts/win-win-theorem.md)
- Provides a *computational* explanation complementing the *information-theoretic* concentration explanation of [MDM19](curse-of-concentration.md) and [Fawzi et al.](adversarial-vulnerability-any-classifier.md)
- Related: [Evasion Attacks](../concepts/evasion-attacks.md), [One-Way Functions](../concepts/one-way-functions.md), [Pseudorandomness](../concepts/pseudorandomness.md), [Computational Concentration of Measure](../concepts/computational-concentration-of-measure.md) (which shows computational hardness *cannot* help on product distributions, whereas BLPR19 constructs distributions where it *does* hurt)
- Complements [GJMM20] positive separation: together, they identify distributions where computational robustness is strictly weaker than IT robustness, and distributions where the two coincide.
- Authors: [Sébastien Bubeck](../entities/sebastien-bubeck.md), [Eric Price](../entities/eric-price.md), [Ilya Razenshteyn](../entities/ilya-razenshteyn.md). (The follow-up Bubeck-Lee-Price-Razenshteyn paper adding Yin-Tat Lee strengthens this under PRG security.)

## Open Questions / Limitations

- The hard distribution is cryptographic / contrived. Whether natural image distributions suffer the same computational obstruction is open.
- Gap to practice: real adversarial examples arise from networks trained with gradient methods; whether the hardness here is the "correct" formalization is unresolved.
- Characterizing which distributions admit efficient robust learners (positive results) remains open.

## Quotes / Notable Passages

> "We show that computational constraints are a plausible explanation for the existence of adversarial examples: there are learning tasks which are robust in an information-theoretic sense, but where producing a robust classifier is computationally intractable under standard cryptographic assumptions."
