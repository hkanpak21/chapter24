---
title: Adversarial Examples from Computational Constraints
type: source
date_ingested: 2026-04-12
authors: [Sébastien Bubeck, Eric Price, Ilya Razenshteyn]
venue: "ICML 2019"
venue_evidence: "https://dblp.org/rec/conf/icml/BubeckLPR19.html; https://proceedings.mlr.press/v97/bubeck19a.html, PMLR vol 97, pages 831-840"
year: 2019
tags: [adversarial-ml, evasion-attacks, complexity-theory, statistical-query, sample-complexity]
claim_quantifier: existential
antecedent: "none. The hardness is unconditional within the statistical query model. No cryptographic assumption is used anywhere in the paper."
adversary_bound: "the learner is restricted to the statistical query model, with an oracle of precision exp(−Cd^c) and an exponential lower bound on the number of queries. The perturbation adversary is a norm budget, not a computation."
model_class: "binary classifiers on R^d, ℓ₂ and ℓ∞"
algorithm_class: "statistical query algorithms"
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: none
cls_write: read only
cls_frame: compute
cls_party: learner
cls_unit: algo class
cls_tightness: class
cls_baseline: n/a
cls_second_party: perturbation
cls_assessed: explicit
cls_evidence: "This example gives an exponential separation between classical learning and robust learning in the statistical query model."
cls_evidence_src: abstract
cls_reason: "Two parties are bounded (learner restricted to the SQ model; evasion adversary by a norm-ball radius, per the front matter's own adversary_bound field). By Rule 4 the computational bound decides the row: party=learner, unit=algo class, tightness=class (matches precedent: what-can-we-learn-privately, an SQ-restricted learner, got the identical unit/tightness pair), and the perturbation bound goes in second. access=none: grepped the PDF for 'white-box'/'black-box'/'threat model', zero hits; the evasion adversary is a norm ball with no operationalized query procedure, matching the other two evasion papers in this batch."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

**Correction, 2026-08-20.** This page previously stated that the hardness holds "under standard cryptographic assumptions" and that the construction goes "via PRFs". Neither is in the paper. The word "cryptographic" occurs once in the whole PDF, in a closing aside. The hardness here is **unconditional in the statistical query model**; the cryptographic version of the result is the sequel, [BLPR19](adversarial-examples-prg.md), which uses a trapdoor pseudorandom generator under the quadratic residuosity assumption. The page also called this paper "BLPR19", which is the sequel's tag; the PDF in `raw/` is the three-author May 2018 preprint, BPR.

This paper gives a computational explanation for adversarial examples: a classification task in `ℝ^d` that is (a) learnable non-robustly in polynomial time and polynomial samples, (b) robustly learnable with polynomial samples if computation is free, and (c) not efficiently and robustly learnable by any algorithm in the statistical query model, even with an exponential-precision oracle. The result decouples statistical from computational robustness inside one named algorithm class.

The paper frames four mutually exclusive explanations for adversarial vulnerability: no robust classifier exists; identifying one needs too much data; identifying one is information-theoretically possible but computationally intractable; or the right algorithm has not been found. Its primary result supports the third; its secondary result argues *against* the second.

## Claim Boundary

- **Quantified over:** one constructed task. Theorem 1.1 is of the form "for any `M, ε > 0`, there exists a classification task in `ℝ^d`" with the three listed properties. It is existential and the task is built for the purpose: a standard multivariate Gaussian with a random `k`-dimensional subspace in which two well-separated distributions matching many Gaussian moments are planted, a high-dimensional generalisation of a construction of Diakonikolas et al.
- **Antecedent:** none. This is the unusual feature of the paper and the reason it is often miscited. The lower bound is unconditional *within* the SQ model.
- **Which party is constrained:** the *learner*, and only by membership in the statistical query model. The paper takes the SQ oracle's precision to be `τ ≈ exp(−Cd^c)`, which it notes cannot be simulated with polynomially many samples, and shows that even so an exponential number of queries is needed. The evasion adversary is not a computational object at all; it is a norm ball of radius ε.
- **Does not establish:** that robust learning is hard for polynomial-time algorithms. The authors say so: "Although we cannot prove it, we believe that our input distributions are computationally hard in general." Nearest-neighbour is named as an algorithm outside the SQ model; the paper offers a moment-matching heuristic argument that it too would need exponentially many samples. It also does not establish anything about natural image distributions.
- **Abstract vs theorem:** the abstract's "adversarial examples may be an unavoidable byproduct of computational limitations of learning algorithms" is a suggestion, and is marked as such ("It suggests that"). The theorem is confined to the SQ model.

NOTES: _Key notion here is that we intract information theoretical robustness from computational robustness, hence we achieve information theoretically robust being the learner against an adversarial example inputting adversary (What is the computational model for this adversarial example creator? What can it see) yet there is no PPT learner that can be robust against this adversary_

**Correction, 2026-08-20.** The paragraph below described the construction as "based on pseudorandom functions / one-way functions" with data "labeled by a planted cryptographic key". The paper's construction has no cryptography in it: a standard multivariate Gaussian, a random `k`-dimensional subspace, and two well-separated distributions planted in that subspace which match many moments of a Gaussian. The SQ lower bound follows by bounding a non-standard correlation between the two distributions, in the framework of Feldman et al. and Diakonikolas et al. The original text is kept below because the note the user attached to it refers to it.

The construction uses a distribution based on pseudorandom functions / one-way functions: honest data is labeled by a planted cryptographic key, so statistically any Bayes-optimal classifier is robust, but efficient learners cannot distinguish the planted structure from random noise in polynomial time and so produce classifiers whose decision boundary contains many adversarial perturbations.

NOTES: _Key detail to note here is that we build a distribution based on a cryptographic function. A key thing may be on relaxing the cryptographical hardness on the data distribution instance so that we can state certain things in a practical and learnable manner._

NOTES: _One another thing comes to my mind is to have a mid way among cryptographical distributions and statistically learnable distributions. Maybe treating both in a same way giving lowerbounds on weak crypto or having a hard problem being similar to a cryptographical instance._

The paper's **secondary** result runs the other way from what this page previously recorded. It is evidence *against* the "too much data" hypothesis: if a robust classifier exists then it can be found with relatively few training examples, under a standard assumption on the data distribution — for example that the distribution within each label is close to a Lipschitz generative model, or is drawn from a finite set of exponential size. The proof is a union bound over a net of robust classifiers.

**Correction, 2026-08-20.** This section previously read "the authors also give a statistical lower bound: there is a learning problem where the *sample complexity* of robust learning is super-polynomially larger than that of non-robust learning". The paper proves no such thing, and its secondary result points the opposite way. The polynomial `Ω(√d)` sample separation belongs to Schmidt et al., which this paper discusses as related work supporting a hypothesis it then argues against — it notes that for Schmidt et al.'s hard instance its own secondary result yields a robust classifier from `O(d)` samples.

Taken together with [Win-Win (DNV19)](win-win-robust-learning.md), which shows robust-learning hardness implies one-way functions, the sequel [BLPR19](adversarial-examples-prg.md) supplies the cryptographic direction. This paper does not; its lower bound is in the SQ model.

## Key Contributions

- **SQ lower bound (Theorem 1.1, primary result)**: for any `M, ε > 0` there is a classification task in `ℝ^d` that is learnable in `poly(d)` time and samples, robustly learnable in `poly(d)` samples with ℓ₂-robustness parameter `M` while samples have norm `O(√d)` with high probability, and **not** efficiently and robustly learnable in the statistical query model — even against an oracle of precision exponential in `d`, an exponential number of queries is needed to robustly learn with robustness parameter ε. The same holds for ℓ∞ with diameter `O(√(d log d))`.

NOTES: What is a learning problem and what is PAC-learnable.

- **Construction**: a standard multivariate Gaussian with a random `k`-dimensional subspace in which two well-separated moment-matching distributions are planted; a high-dimensional generalisation of a `k = 1` construction of Diakonikolas et al. **Correction, 2026-08-20:** this bullet previously read "Construction via PRFs ... labels determined by a pseudorandom function on a secret key", which is the sequel's construction, not this one.
- **Robust learning with few samples (secondary result, Section 3)**: robust *feasibility* implies sample-efficient robust *learnability*, when the family of robust classifiers is finite or admits an exponential-size net. **Correction, 2026-08-20:** the previous bullet "Statistical lower bound: a separate construction gives a problem where robust learning requires exponentially more samples than standard learning" reverses the paper's result.
- **Foundational framing**: the paper introduces the four mutually exclusive hypotheses for adversarial vulnerability and supplies evidence for the computational one.

## Key Definitions / Theorems

- **ε-robust zero-one loss (Definition 2.1)**: `ℓ_ε(f, x, i) = 1{∃ z ∈ B(ε) : f(x + z) ≠ i}`.
- **(ε, δ)-robust classifier (Definition 2.2)**: `E_{X∼D_i}[ℓ_ε(f, X, i)] ≤ δ` for both labels.
- **Classification task (Definition 2.3)**: a family `𝒟` of *pairs* of distributions, with the algorithm receiving `n` i.i.d. samples from each. Definition 2.3's Remark 2.4 records that classical `(ε', δ')`-PAC learning is the case `ε = 0`.
- **Robust feasibility (Definition 2.5)**: every `D ∈ 𝒟` admits an `(ε, δ)`-robust classifier. The secondary result is that feasibility implies sample-efficient learnability.
- **SQ model as used here**: queries to a `τ`-SQ oracle returning `E_{X∼D} ψ(X, f(X)) + ξ` with `|ξ| ≤ τ`; the paper takes `τ` of order `exp(−Cd^c)`.
- **Correction, 2026-08-20:** the previous "Main theorem (informal): Assuming OWFs ... no polynomial-time learner" and "Statistical separation: robust PAC sample complexity is 2^{Ω(n)}" both attributed to this paper results it does not contain.

## Connections

- Source: [Adversarial Examples from Cryptographic Pseudo-Random Generators (BLPR19)](adversarial-examples-prg.md) — the direct sequel by the same authors plus Yin Tat Lee, which replaces this paper's SQ lower bound with hardness under the quadratic residuosity assumption and strengthens the robust classifier to maximally robust.
- Related to [Win-Win Theorem (Degwekar-Nakkiran-Vaikuntanathan 2019)](win-win-robust-learning.md) / [win-win-theorem concept](../concepts/win-win-theorem.md). **Correction, 2026-08-20:** this link previously read "Dual of", which requires a cryptographic hypothesis this paper does not have. The dual of the win-win theorem is the sequel, not this paper.
- Provides a *computational* explanation complementing the *information-theoretic* concentration explanation of [MDM19](curse-of-concentration.md) and [Fawzi et al.](adversarial-vulnerability-any-classifier.md)
- Related: [Evasion Attacks](../concepts/evasion-attacks.md), [One-Way Functions](../concepts/one-way-functions.md), [Pseudorandomness](../concepts/pseudorandomness.md), [Computational Concentration of Measure](../concepts/computational-concentration-of-measure.md) (which shows computational hardness *cannot* help on product distributions, whereas BLPR19 constructs distributions where it *does* hurt)
- Complements [GJMM20] positive separation: together, they identify distributions where computational robustness is strictly weaker than IT robustness, and distributions where the two coincide.
- Authors: [Sébastien Bubeck](../entities/sebastien-bubeck.md), [Eric Price](../entities/eric-price.md), [Ilya Razenshteyn](../entities/ilya-razenshteyn.md). The PDF in `raw/` carries these three; the front matter of this page previously also listed Yin Tat Lee, who appears on the follow-up. The follow-up strengthens this result under a trapdoor PRG.

## Open Questions / Limitations

- **The lower bound is SQ-only.** The authors write that they believe the input distributions are computationally hard in general but cannot prove it, and note that finding a polynomial-time algorithm evading this SQ lower bound "would be a remarkable breakthrough in SQ theory" since the only known problems with exponential SQ hardness and polynomial-time algorithms involve solving linear systems over finite fields.
- The hard distribution is contrived. Whether natural image distributions suffer the same computational obstruction is open. **Correction, 2026-08-20:** the word "cryptographic" was removed from this line; the construction is a planted moment-matching subspace, not a cryptographic object.
- Gap to practice: real adversarial examples arise from networks trained with gradient methods; whether the hardness here is the "correct" formalization is unresolved.
- Characterizing which distributions admit efficient robust learners (positive results) remains open.

## Quotes / Notable Passages

> _Not verbatim. Checked against `raw/BPR19_AdvExamplesCompConstraints.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> We show that computational constraints are a plausible explanation for the existence of adversarial examples: there are learning tasks which are robust in an information-theoretic sense, but where producing a robust classifier is computationally intractable under standard cryptographic assumptions.

Verified against `raw/BPR19_AdvExamplesCompConstraints.pdf` on 2026-08-20. The paraphrase above named the wrong hypothesis; the paper's own sentences are:

> "This example gives an exponential separation between classical learning and robust learning in the statistical query model. It suggests that adversarial examples may be an unavoidable byproduct of computational limitations of learning algorithms."

— abstract. The separation is stated inside the SQ model and the consequence is offered as a suggestion.

> "Although we cannot prove it, we believe that our input distributions are computationally hard in general."

— §1.2, the authors' own limit on how far the result reaches beyond the SQ model.
