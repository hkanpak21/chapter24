---
title: "Adversarial Examples from Cryptographic Pseudo-Random Generators"
type: source
date_ingested: 2026-04-23
authors: [Sébastien Bubeck, Yin Tat Lee, Eric Price, Ilya Razenshteyn]
venue: arXiv 2018 (preprint — follow-up to BPR19)
year: 2018
tags: [adversarial-ml, cryptography, pseudorandomness, evasion-attacks, one-way-functions, complexity-theory]
---

## Summary

This paper (BLPR19, the Bubeck-*Lee*-Price-Razenshteyn strengthening of [Bubeck-Price-Razenshteyn 2019 ICML](adversarial-examples-computational-constraints.md)) constructs a learning task where a **maximally robust classifier exists** but is **computationally hard to learn** — under the weaker and more standard assumption that **cryptographic pseudorandom generators exist** (equivalently, one-way functions exist). The BPR19 predecessor relied on stronger assumptions (trapdoor PRGs); BLPR19 sharpens the result to standard crypto.

Concretely, the construction plants a secret key inside a learning task such that: (a) the Bayes-optimal classifier perfectly classifies the data and has arbitrary robustness radius (maximally robust), (b) any polynomial-time learning algorithm that produces a classifier with even non-trivial robustness implies breaking the underlying PRG's security — i.e., inverting a one-way function, contradicting standard cryptographic assumptions. The task thus has a **provably huge gap between information-theoretic and computational robustness**.

The paper complements three related results: (1) the [Degwekar-Nakkiran-Vaikuntanathan Win-Win Theorem](win-win-robust-learning.md) which goes in the *opposite* direction (hard-to-robustly-learn implies OWF), together establishing that robust-learning hardness is exactly equivalent to cryptographic hardness; (2) [Computational Concentration of Measure (EMM20)](computational-concentration-of-measure-etesami.md) showing that on *product distributions*, computational hardness does not help (giving the negative direction complementing BLPR19's positive direction); (3) [Garg-Jha-Mahloujifar-Mahmoody 2020](computational-hardness-robust-learning.md), a similar positive separation using PRFs.

Together, these papers place adversarial robustness *squarely within Impagliazzo's five-worlds landscape*: robust learning is possible iff computing is at least as hard as cryptography (i.e., we are not in Heuristica/Pessiland).

## Key Contributions

- **Standard-crypto separation**: First proof that adversarial vulnerability of efficient learners is implied by *standard* cryptographic assumptions (OWFs), not just stronger trapdoor-based ones.
- **Trapdoor-PRG construction**: the task is defined via a TPRG so that learning it efficiently = inverting the PRG; the construction is modular and could be instantiated with any TPRG.
- **Maximally robust Bayes classifier**: the existential classifier is not just somewhat-robust but has arbitrary robustness radius, strengthening the gap.
- **Bridge to Impagliazzo's worlds**: together with Win-Win Theorem and Computational Concentration, shows adversarial robustness maps neatly onto Impagliazzo's landscape.

## Key Definitions / Theorems

- **Trapdoor Pseudo-Random Generator (TPRG)**: a PRG G with a trapdoor τ such that given τ, one can invert; without τ, inverting is computationally hard.
- **Main theorem (informal)**: Assuming TPRGs exist (weaker: OWFs exist), ∃ concept class C and distribution μ such that (a) C contains a classifier with arbitrary adversarial robustness and zero risk on μ, (b) no polynomial-time learner can produce a classifier with non-trivial adversarial robustness.
- **Construction (TPRG-based)**: data points x = (seed, G(seed)), label = G(seed)₁ (first bit of expanded string); Bayes-optimal classifier computes G and is arbitrary-ε-robust; efficient learners cannot compute G.

## Connections

- Source: [Adversarial Examples from Computational Constraints (BPR19)](adversarial-examples-computational-constraints.md) — predecessor with stronger crypto assumption; BLPR19 strengthens to standard OWFs.
- Source: [Computational Limitations in Robust Classification / Win-Win (DNV19)](win-win-robust-learning.md) — converse direction: hard-to-robustly-learn ⇒ OWF; together BLPR and DNV make robust learning ⇔ OWF.
- Source: [Computational Concentration of Measure (EMM20)](computational-concentration-of-measure-etesami.md) — shows crypto hardness does *not* help on product distributions — complementary negative direction.
- Source: [Adversarially Robust Learning Could Leverage Computational Hardness (GJMM20)](computational-hardness-robust-learning.md) — similar positive separation via PRFs; practical construction.
- Concept: [Win-Win Theorem](../concepts/win-win-theorem.md) — the characterization connecting these results.
- Concept: [Pseudorandomness](../concepts/pseudorandomness.md) — the crypto primitive used.
- Concept: [One-Way Functions](../concepts/one-way-functions.md) — equivalent via HILL.
- Concept: [Computational vs. IT Robustness](../concepts/computational-vs-it-robustness.md).
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md).
- Authors: [Sébastien Bubeck](../entities/sebastien-bubeck.md), [Yin-Tat Lee](../entities/yin-tat-lee.md), [Eric Price](../entities/eric-price.md), [Ilya Razenshteyn](../entities/ilya-razenshteyn.md).

## Open Questions / Limitations

- **Natural data distributions**: construction is cryptographic / contrived; the Win-Win theorem says either natural data admits efficient robust learning or yields OWFs — and natural data presumably does not yield new OWFs.
- **Adaptive adversaries**: the construction assumes non-adaptive adversaries; adaptive-adversary version open.
- **Quantitative tightness**: the theoretical separation is sharp (poly vs. exp), but whether the constants match specific cryptographic hardness quantitatively is open.
- **Practical instantiations**: no one has constructed a real-world dataset that concretely achieves BLPR-style computational-robustness separation; all known examples are synthetic.

## Quotes / Notable Passages

> "We construct a task which admits a maximally robust classifier and prove computational hardness of learning this task under a standard cryptographic assumption."

> "The primary ingredient of our construction is a trapdoor pseudorandom generator."
