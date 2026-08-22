---
title: On Evaluating Adversarial Robustness
type: source
date_ingested: 2026-08-20
authors: [Nicholas Carlini, Anish Athalye, Nicolas Papernot, Wieland Brendel, Jonas Rauber, Dimitris Tsipras, Ian Goodfellow, Aleksander Mądry, Alexey Kurakin]
venue: "arXiv:1902.06705 preprint, never formally published (confirmed: four independent bibliographies in this corpus, CGB+22, SSK+24, CAS+21 and PSV23, all cite it as an arXiv preprint)"
year: 2019
tags: [adversarial-ml, evasion-attacks, robustness, threat-model, evaluation-methodology]
claim_quantifier: empirical
antecedent: none
---

## Summary

A methodology paper, not a results paper. Nine authors — most of them the people who broke the defenses being discussed — set out what a defence evaluation must contain: a stated threat model (adversary goals, capabilities, knowledge), adaptive attacks against the specific defence, released code and pre-trained models, and a checklist of about forty specific failure modes grouped into "common severe flaws", "common pitfalls" and "special-case pitfalls".

The paper's substantive contribution to the *definitional* question is negative and deliberate. It considers, and explicitly rejects, the idea of putting the attacker's computation into the threat model. In §4.8 the authors write that there "are few reasonable threat models under which an attacker can compute 100 iterations of gradient descent, but not 1000", and the justification given is a principle about threat models, not a claim about the empirical distribution of attackers: "Because the threat model must not constrain the approach an attacker takes, it is worth evaluating against a strong attack with many iterations of gradient descent." §2.5 makes the same commitment positively: evaluations should assume an "infinitely thorough" adversary who will spend whatever time is necessary. This is the position that the parent survey strand records as the field's explicit rejection of attack compute as a threat-model parameter. It is a considered position, restated from [Obfuscated Gradients](obfuscated-gradients.md) §6.1, not an oversight.

The second definitional observation, in §2.2.2, is that the quantity being evaluated is not computable. The authors define adversarial risk as `E_{(x,y)~X}[max_{x': D(x,x')<ε} L(f(x'), y)]` (or the dual, average minimum distortion) and then note that although this is "computable in theory", it "is usually intractable to compute exactly". Every practical robustness number is therefore an *upper* bound produced by an attack, and the tightness of that bound is exactly what the paper's checklist is trying to police. §4.1 adds that provable methods give lower bounds instead, but that verification is "often computationally intractable" for even modestly sized networks, and that the guarantees they do give are per-example, not distributional.

Also notable: §2.2.3 imports Kerckhoffs's principle wholesale, and gives two conditions a defence's secret must satisfy (efficiently replaceable, and non-extractable by a querying adversary). §2.5 retracts, on behalf of Carlini and Wagner themselves, the citation of their 2017 paper as support for a zero-knowledge threat model.

## Claim Boundary

- **Quantified over:** Nothing formal. The empirical premise is a bibliographic one: a specific enumerated list of about eighteen citations of defences broken between 2016 and 2019 supports the sentence that "most papers that propose defenses are quickly shown to be incorrect". The checklist items are normative recommendations, each of which the authors say is present "because we are aware of several defense evaluations which were broken and following that specific recommendation would have revealed the flaw." No claim quantifies over all defences, all attacks, or all models.
- **Antecedent:** none. There is no theorem and no conditional result. The compute position in §4.8 rests on the *principle* that a threat model must not constrain the attacker's approach — a normative premise, neither measured nor proved.
- **Does not establish:** (a) that no defence is robust — the paper explicitly says its checklist is "neither necessary nor sufficient" and that there "likely exist completely ineffective defenses which satisfy all of the below recommendations"; (b) that attacker compute is irrelevant to security in general — the claim is narrower, that within `ℓp` evasion there is no realistic attacker separated by one order of magnitude of gradient steps; (c) that adversarial risk is uncomputable in principle — the paper says it is computable in theory and intractable in practice; (d) that following the checklist yields a correct evaluation. The authors warn: "Blindly following the checklist without careful thought will likely be counterproductive".
- **Abstract vs theorem:** none found. The abstract is appropriately hedged ("we discuss the methodological foundations, review commonly accepted best practices, and suggest new methods"). The one place where a reader could over-read is §2.5's "an evaluation that does not attempt to do this is fundamentally flawed", which is a normative judgement stated in the register of a fact.

## Key Contributions

- The evaluation checklist (§3), split into severe flaws / pitfalls / special-case pitfalls, with each item cross-referenced to the section that explains it.
- The explicit rejection of attacker compute as a threat-model parameter (§4.8), with the "threat model must not constrain the approach" justification.
- The statement that adversarial risk is intractable to compute exactly, so practical robustness numbers are upper bounds of unknown tightness (§2.2.2).
- The "infinitely thorough" adversary as the standing assumption for all three research motivations the paper distinguishes: security, worst-case bounds, and human-machine gap (§2.5).
- Two conditions for admissible secrets in a defence — efficiently replaceable and non-extractable (§2.2.3) — importing Kerckhoffs's principle into ML defences.
- The authors' own retraction of the zero-knowledge threat model (§2.5).

## Key Definitions / Theorems

No theorems. Definitions used (not introduced):

- **Adversarial risk, worst-case-loss form**: `E_{(x,y)~X}[ max_{x': D(x,x')<ε} L(f(x'), y) ]`, attributed to Madry et al. 2017 and Uesato et al. 2018.
- **Adversarial risk, minimum-distortion form**: `E_{(x,y)~X}[ min_{x' ∈ A_{x,y}} D(x, x') ]`, with `A_{x,y}` the set of inputs meeting the adversary's goal.
- **Per-example vs averaged reporting** (§5.6): report `mean_x min_{a∈A} f(a(x))`, not `min_{a∈A} mean_x f(a(x))`. The same inequality appears in [Obfuscated Gradients](obfuscated-gradients.md) §6.3.
- **Threat model** = adversary goals + capabilities + knowledge (§2.2), with the standing assumption that the adversary knows the defence.

## Connections

- Direct successor to [Obfuscated Gradients (ACW18)](obfuscated-gradients.md) — three of the nine authors overlap, and §4.8's compute position restates ACW18 §6.1 verbatim in substance.
- Superseded in practice, though not contradicted, by [On Adaptive Attacks to Adversarial Example Defenses (TCBM20)](adaptive-attacks-defenses.md), which shows that defences following this checklist's adaptive-attack recommendation still fail.
- Extended for a specific defence class by [Evaluating the Adversarial Robustness of Adaptive Test-time Defenses (CGB+22)](adaptive-test-time-defenses-eval.md), which describes itself as extending "the checklist of Carlini et al. (2019)".
- Operationalised as a standing benchmark by [RobustBench (CAS+21)](robustbench.md), which cites the black-box-beats-white-box indicator from this paper as its unreliability flag.
- Formalised, in the adversary-knowledge dimension only, by [SoK: Analyzing Adversarial Examples (FK24)](sok-adversary-knowledge.md).
- Contradicted on the compute question by [SoK: Pitfalls in Evaluating Black-Box Attacks (SSK+24)](sok-black-box-attack-pitfalls.md), which argues local attack runtime should be the equalizing metric.
- Concepts: [Evasion Attacks](../concepts/evasion-attacks.md), [Adaptive Attacks](../concepts/adaptive-attacks.md), [Obfuscated Gradients](../concepts/obfuscated-gradients.md), [Computational vs Information-Theoretic Robustness](../concepts/computational-vs-it-robustness.md) — the last is the notion this paper declines to adopt.
- Authors: [Nicholas Carlini](../entities/nicholas-carlini.md), [Nicolas Papernot](../entities/nicolas-papernot.md), [Aleksander Madry](../entities/aleksander-madry.md).

## Open Questions / Limitations

- The compute position is asserted for `ℓp` evasion on image classifiers. The paper does not argue it for query-limited black-box settings, and in fact notes in the same paragraph that "black-box attacks often take orders of magnitude more queries, with attacks requiring over 100,000 queries not being abnormal" — a regime where the 100-vs-1000 argument does not obviously transfer.
- The paper names no way to measure how loose an attack-derived upper bound on adversarial risk is. The checklist's sanity tests are indicators of looseness, not estimators of it.
- §4.1 concedes that provable techniques give only "for some specific set of examples X, no adversarial example with distortion less than ε exists" — a per-example guarantee, which the authors contrast unfavourably with the guarantees of "provably correct cryptographic algorithms".
- The checklist is dated by its own admission ("This checklist is a living document that lists the most common evaluation flaws as of 18 February, 2019").

## Quotes / Notable Passages

On attacker compute as a threat-model parameter — the deliberate rejection:

> "There are few reasonable threat models under which an attacker can compute 100 iterations of gradient descent, but not 1000. Because the threat model must not constrain the approach an attacker takes, it is worth evaluating against a strong attack with many iterations of gradient descent."

On the adversary the evaluation must assume:

> "In all scenarios we should assume the existence of an “infinitely thorough” adversary who will spend whatever time is necessary to develop the optimal attack."

On the intractability of the quantity being evaluated:

> "while this adversarial risk (Madry et al., 2017; Uesato et al., 2018) is often computable in theory (e.g. with optimal attacks or brute force enumeration of the considered perturbations), it is usually intractable to compute exactly, and therefore in practice we must approximate this quantity."

On verification:

> "it is often computationally intractable to verify even modestly sized neural networks."

On the limits of the checklist itself:

> "There likely exist completely ineffective defenses which satisfy all of the below recommendations"
