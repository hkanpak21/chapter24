---
title: The Curse of Concentration in Robust Learning — Evasion and Poisoning Attacks from Concentration of Measure
type: source
date_ingested: 2026-04-12
authors: [Saeed Mahloujifar, Dimitrios I. Diochnos, Mohammad Mahmoody]
venue: AAAI
year: 2019
tags: [adversarial-ml, evasion-attacks, poisoning-attacks, concentration-of-measure, complexity-theory]
claim_quantifier: conditional
antecedent: "The metric probability space (X, d, μ) of instances is concentrated — every set of measure ≥ α has an ε-expansion covering almost all of X (concentration function h(μ, α, ε) close to 1). This hypothesis was subsequently MEASURED on image benchmarks by the same research group and found NOT to bind: see Limits, below. For the poisoning theorem the antecedent is instead a product training distribution plus a deterministic learner."
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: none
cls_write: read only
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: absent
cls_evidence_src: "classified by hand in the first batch, before the evidence requirement was added to the brief"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows."
cls_prov: hand
cls_date: 2026-08-22
---

## Summary

**Read the Limits section below before citing this page.** The theorem is correct; the framing this page carried until 2026-08-20 was not. The result is **conditional**, and its antecedent — that the instance space is concentrated in the metric sense — has been measured and found not to hold usefully for image benchmarks.

This paper (MDM19) establishes a general theorem that any metric probability space that *is concentrated* makes any classifier with nontrivial error inherently vulnerable to adversarial perturbations — the "curse of concentration." Conditional on that hypothesis, the result is classifier-architecture-independent and hypothesis-class-independent: it is a property of the instance space itself. The universality is over classifiers, not over spaces.

## Claim Boundary

- **Quantified over:** all classifiers h with Ω(1) error, and all metric probability spaces **that satisfy the concentration hypothesis**. Theorem 1.1 is universally quantified over classifiers and existentially over adversaries; it is *conditional* on the space. The often-repeated reading "any space makes any classifier vulnerable" drops the antecedent and is false.
- **Antecedent:** concentration of (X, d, μ), stated via the concentration function. Verified to hold for normal Lévy families (n-sphere, isotropic Gaussian, Boolean hypercube under Hamming, unit cube, symmetric groups) — these are theoretical spaces. **Measured and found not to bind for image data** by [MZME19](empirically-measuring-concentration.md); see Limits.
- **Does not establish:** (i) that adversarial examples are unavoidable for natural data — the antecedent is unverified there and the measurement points the other way; (ii) that no robust classifier exists for a given real dataset; (iii) any statement about attacker compute — the adversary here is information-theoretic, and Theorem 1.2's poisoner is offline and unbounded. The efficient-attacker version is a separate result ([EMM20](computational-concentration-of-measure-etesami.md)).
- **Abstract vs theorem:** Overstatement found, in the paper and previously mirrored on this page. The quoted abstract line "We prove that for any learning problem defined over such a concentrated space, no classifier with an initial constant error … can be robust" is correctly conditional ("such a concentrated space"), but the surrounding rhetoric of a "curse" invites reading the antecedent as universal. The paper's own limitations section concedes that whether natural distributions are concentrated under a perceptually meaningful metric is unknown.

## Limits

Two facts bound this theorem. Neither refutes it; both restrict what may be inferred from it.

### (a) The antecedent was measured, and it does not bind for image benchmarks

[Mahloujifar, Zhang, Mahmoody and Evans, NeurIPS 2019](empirically-measuring-concentration.md) — three of the four authors overlap with this paper — built a provably convergent estimator for the concentration function from i.i.d. samples and ran it on MNIST, CIFAR-10, Fashion-MNIST and SVHN under ℓ∞ and ℓ₂.

What they measured: the smallest ε-expansion achievable by an error region of measure at least α, over a complexity-controlled family of subsets (unions of hyperrectangles for ℓ∞, unions of balls for ℓ₂), with convergence to the true unrestricted concentration function proved as sample size and family complexity grow together.

What they concluded: the concentration-implied floor on adversarial risk sits well below what real robust classifiers achieve, so metric concentration does not account for observed vulnerability. On CIFAR-10 at ε_∞ = 8/255 their estimate is 29.21% against the 52.96% attack success rate reported for the Madry et al. classifier; they also exhibit an error region whose measure rises only from 5.94% to 18.13% under that expansion. On MNIST the gap is small (8.28% estimated vs 10.70% reported), so that dataset is closer to the concentration limit. Their stated conclusion: recent impossibility results "should not cause us to lose hope in the possibility of finding more robust classifiers."

So the antecedent of Theorem 1.1 holds strongly for the theoretical Lévy families the paper instantiates, and does not hold usefully for the image benchmarks the adversarial-examples literature actually cares about. Citing this theorem as an explanation of adversarial examples on CIFAR-10 is citing it past its antecedent.

### (b) A second literature uses "concentration" in the opposite geometric sense, with the opposite conclusion

[Pal, Sulam and Vidal, NeurIPS 2023](data-concentration-robustness-avoidable.md) prove that concentration makes robust classifiers **attainable** — using the same word for a different property.

- **Here (MDM19), Sense A:** concentrated = every set of non-trivial measure ε-expands to nearly all of X. The uniform measure on a high-dimensional sphere is maximally concentrated. Concentration ⟹ *no* robust classifier.
- **There (PSV23), Sense B:** concentrated = mass ≥ 1−δ sits on a set of Lebesgue **volume** ≤ C·exp(−nε). The uniform measure is minimally concentrated. Volume concentration is *necessary* for a robust classifier to exist (Thm 2.1, by Brunn–Minkowski), and a strengthened version, (ε,δ,γ)-strong concentration, is *sufficient* (Thm 3.1).

The two senses are close to antonyms: mass on a thin low-dimensional set is Sense-B-concentrated and Sense-A-unconcentrated. PSV23 §6 states the relation explicitly, describing their notion as "a relative notion of concentration with respect to the uniform measure µ" whereas this paper's notion is defined "independently", and locating "a slack in the analysis" of MDM19/MZME19 that their choice of expansion sets fills.

Positions to hold simultaneously, per the wiki's contradiction rule: MDM19 Thm 1.1 is true; PSV23 Thm 3.1 is true; they are not in conflict, because they hypothesize different properties. PSV23 says so itself — the impossibility results remain non-vacuous for flat distributions, its own positive results are existential rather than constructive, and it does not touch computational hardness of robust learning. See [Two Senses of Concentration](../concepts/two-senses-of-concentration.md).

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
- **Antecedent measured — a limit, not a sibling:** [Empirically Measuring Concentration (MZME19)](empirically-measuring-concentration.md). Same research group; estimates the concentration function on image benchmarks and finds it does not account for observed adversarial risk. See Limits (a).
- **Opposite sense of the same word — a limit, not a sibling:** [Adversarial Examples Might be Avoidable (PSV23)](data-concentration-robustness-avoidable.md), where volume-concentration makes robust classifiers attainable. See Limits (b) and [Two Senses of Concentration](../concepts/two-senses-of-concentration.md).
- Genuine sibling results, same sense and same direction: [Fawzi et al. 2018](adversarial-vulnerability-any-classifier.md) (smooth generative models), [Adversarial Spheres](adversarial-spheres.md) / Gilmer et al. 2018 (n-sphere), Shafahi et al. 2018 (sphere and cube)
- Superseded quantitatively by online p-tampering of [MM17] in the online setting; Õ(√m) offline bound here is stronger per-example
- Synthesized in [A Complexity Theoretic Approach to Adversarial ML](complexity-theoretic-adversarial-ml.md)
- Related: [Evasion Attacks](../concepts/evasion-attacks.md), [Poisoning Attacks](../concepts/poisoning-attacks.md), [p-Tampering Model](../concepts/p-tampering-model.md), [Lévy Family](../concepts/levy-family.md)
- Authors: [Saeed Mahloujifar](../entities/saeed-mahloujifar.md), [Dimitrios Diochnos](../entities/dimitrios-diochnos.md), [Mohammad Mahmoody](../entities/mohammad-mahmoody.md).

## Open Questions / Limitations

- The concentration bound is *distribution-dependent*: for "natural" data distributions (e.g., images), whether the metric probability space is concentrated (under a perceptually meaningful metric) was left open by the paper. **Partly resolved, negatively** — [MZME19](empirically-measuring-concentration.md) measured it under ℓ∞ and ℓ₂ on MNIST, CIFAR-10, Fashion-MNIST and SVHN and found the bound does not bind (large gap on CIFAR-10, small gap on MNIST). Whether it is concentrated under a *perceptually* meaningful metric, rather than ℓp, remains open.
- Related open question raised by the correction above: is there a single parameterized concentration function with the metric sense and the volume sense as limits? See [Two Senses of Concentration](../concepts/two-senses-of-concentration.md).
- The poisoning attack requires the learner to be deterministic; randomized learners not directly covered.
- Gap remains between existence and polynomial-time computability of the attack (closed later by EMM20 on product distributions).
- Attack is offline (knows training set before substituting); fully online attacks matching these bounds remain open.

## Quotes / Notable Passages

> "We prove that for any learning problem defined over such a concentrated space, no classifier with an initial constant error (e.g., 1/100) can be robust to adversarial perturbations."

> "Our attacks of 1.2 are offline in the sense that the adversary needs to know the full training set T before substituting some of them. We note that the so-called p-tampering attacks of [MDM18] are online ... However, in that work, they could only increase the classification error by O(p) ... while here we get almost full error by only using p ≈ O(√m), which is much more devastating."
