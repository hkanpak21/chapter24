---
title: Dos and Don'ts of Machine Learning in Computer Security
type: source
date_ingested: 2026-08-20
authors: [Daniel Arp, Erwin Quiring, Feargus Pendlebury, Alexander Warnecke, Fabio Pierazzi, Christian Wressnegger, Lorenzo Cavallaro, Konrad Rieck]
venue: USENIX Security Symposium
year: 2022
tags: [adversarial-ml, evaluation-methodology, survey, evasion-attacks, poisoning-attacks]
claim_quantifier: empirical
antecedent: none
---

## Summary

The field-wide anchor for the survey strand. AQP+22 is a critique of **practice** across all of learning-based security, not of any definition. It names ten pitfalls, positioned along the machine-learning workflow, measures their prevalence in 30 papers from the top-four security venues (CCS, S&P, USENIX Security, NDSS) over a decade, surveys 135 of those papers' authors for agreement, and then demonstrates the experimental impact of selected pitfalls by reproducing state-of-the-art systems in four domains: mobile malware detection, vulnerability discovery, source code authorship attribution and network intrusion detection.

The ten: **P1** sampling bias, **P2** label inaccuracy (data collection and labeling); **P3** data snooping, **P4** spurious correlations, **P5** biased parameters (system design and learning); **P6** inappropriate baselines, **P7** inappropriate measures, **P8** base rate fallacy (performance evaluation); **P9** lab-only evaluation, **P10** inappropriate threat model (deployment and operation).

Prevalence: every one of the 30 papers is affected by at least three pitfalls. P1 and P3 are at least partly present in 90% and 73% respectively. P10, P9 and P7 are at least partly present in more than 50%.

**P10 is the entry that matters here, and the exact wording is:** "P10 – Inappropriate Threat Model. The security of machine learning is not considered, exposing the system to a variety of attacks, such as poisoning and evasion attacks." Its prevalence bar is annotated **17% present** — this is the "present" category alone; the §3 text reports P10 as *at least partly present* in more than 50% of the papers. Both numbers are the paper's own and they measure different categories; the 17% figure is the stricter one.

What P10 faults is the **absence or imprecision of the threat model**: security systems designed without considering adversarial influence at all, and threat models that are not "defined precisely" enough for the system to be evaluated against them. The recommendations are that threat models be stated precisely, that an adaptive adversary be assumed in most cases, that all workflow stages be checked for vulnerabilities, and that evaluation focus on white-box attacks following Kerckhoffs's principle. The paper closes P10 with the position that adversarial evaluation "is not an add-on but rather a mandatory component in security research".

**P10 says nothing about adversary compute.** Nowhere in the pitfall, its security implications, or its recommendations is the adversary quantified by computation, memory, samples or queries. "Adaptive" is a knowledge property — the adversary knows the system — not a resource. Occurrences of "computational" elsewhere in the paper concern interpretability cost, tf-idf computation, and bounded-AUC computation, not adversary budget. This is the field-wide statement of the strand's thesis: the security-ML literature's diagnosed threat-model defect is *unstated or imprecise*, never *unpriced*.

## Claim Boundary

- **Quantified over:** the 30 selected papers from four venues over ten years, chosen as "representative examples" spanning many security topics — a deliberate sample, not a census, and not random. The impact analysis ranges over four reproduced state-of-the-art systems, one per domain, chosen as representative. The author survey covers the 135 authors for whom contact information was available.
- **Antecedent:** none; all claims are measured. The assessment scheme is stated: each pitfall per paper is coded present / partly present / not present / unclear from text, moderated to *discussed* if acknowledged in the text, with a separate "does not apply" category reserved for P10 specifically. Corrected or narrowed claims count as not present.
- **Does not establish:** (i) that the surveyed systems are wrong — the authors state explicitly that this is not a finger-pointing exercise and that reproducibility "speaks highly of their academic standard"; (ii) any quantitative claim about the field beyond these 30 papers; (iii) **anything about adversary resources.** Cite this page for the claim that threat models are absent or imprecise in the security-ML literature. Do not cite it for any claim about attacker compute, sample budget or query budget — the concept does not appear.
- **Abstract vs theorem:** none found. The prevalence figures in the abstract and §3 match the figure; the paper is careful to distinguish "present" from "at least partly present"; the Remark explicitly bounds the interpretation. The only reading hazard is external: P10's headline number is quoted as 17% or as >50% depending on which category is meant, and the two are not interchangeable.

## Key Contributions

- **Ten pitfalls as a workflow-indexed taxonomy** (Figure 1), each with description, security implications, and actionable recommendations, plus identification of which cannot be mitigated with current knowledge and require research.
- **Prevalence analysis** over 30 top-tier papers with a stated four-way coding scheme.
- **Author survey** of 135 authors on whether their own work is affected, whether the pitfall is frequent, and whether it is easy to avoid — a design that separates the reviewers' judgement from the community's.
- **Impact analysis** in four domains, showing measured effects: mobile malware detection (P1, P4, P7), vulnerability discovery (P2, P4, P6), source code authorship attribution (P1, P4), network intrusion detection (P6, P9).
- **P10 as the field's canonical name for threat-model failure** in learning-based security, with the prescription that threat models be defined precisely and systems evaluated against them under an adaptive, white-box adversary.

## Key Definitions / Theorems

No theorems. The formal apparatus is the coding scheme (present / partly present / not present / unclear from text, plus does-not-apply for P10, moderated to discussed when acknowledged) and the ten pitfall statements. Verbatim P10, as extracted:

> "P10 – Inappropriate Threat Model. The security of machine learning is not considered, exposing the system to a variety of attacks, such as poisoning and evasion attacks."

with the annotation "17% present".

## Connections

- The field-wide parent of the backdoor-specific critiques: [SoK: The Last Line of Defense (AKK+25)](sok-backdoor-defense-evaluation.md), [Towards a Critical Evaluation of Robustness for DL Backdoor Countermeasures (QMZ+22)](critical-evaluation-backdoor-countermeasures.md), [On Evaluating Neural Network Backdoor Defenses (VG20)](evaluating-nn-backdoor-defenses.md). Each instantiates P10, and none of them prices the adversary either.
- Same critique-of-practice register as the adaptive-attack evaluation literature — [On Evaluating Adversarial Robustness](on-evaluating-adversarial-robustness.md), [Obfuscated Gradients](obfuscated-gradients.md), [On Adaptive Attacks to Adversarial Example Defenses](adaptive-attacks-defenses.md), [SoK: Pitfalls in Evaluating Black-Box Attacks](sok-black-box-attack-pitfalls.md), and [SoK: Analyzing Adversarial Examples — A Framework to Study Adversary Knowledge](sok-adversary-knowledge.md), the one entry that does systematize the adversary's *knowledge*; AQP+22 positions itself as a successor to the tradition started by Sommer and Paxson's decade-earlier study of network intrusion detection, and as orthogonal to domain-specific critiques of malware analysis and website fingerprinting.
- The gap it leaves is filled, on the theory side only, by results that *do* quantify the adversary: [Adversarial Examples from Computational Constraints](adversarial-examples-computational-constraints.md), [Computational Hardness of Robust Learning](computational-hardness-robust-learning.md), [Planting Undetectable Backdoors](planting-undetectable-backdoors.md), [Certified Defenses for Data Poisoning](certified-defenses-data-poisoning.md).
- Definitional-axis contrast: [What Does it Mean for a Language Model to Preserve Privacy?](language-model-preserve-privacy.md) critiques a *definition's unit of protection*, where AQP+22 critiques *evaluation practice*. Different axes; do not merge them.
- Concepts: [Input Manipulation Threat Model](../concepts/input-manipulation-threat-model.md), [Evasion Attacks](../concepts/evasion-attacks.md), [Poisoning Attacks](../concepts/poisoning-attacks.md), [Defendability](../concepts/defendability.md), [Backdoor Defense Evaluation](../concepts/backdoor-defense-evaluation.md).
- Authors: [Lorenzo Cavallaro](../entities/lorenzo-cavallaro.md), [Konrad Rieck](../entities/konrad-rieck.md).

## Open Questions / Limitations

- 30 papers, purposively selected, four venues. No claim of representativeness beyond "representative examples"; percentages should not be extrapolated to the field.
- The paper notes that some pitfalls are systematically harder to detect from text — P5 when hyperparameters or tuning are undescribed, P4 when no explanation of decisions is attempted, P3 when splitting or normalization is unstated. Prevalence for these is a lower bound.
- The authors flag that appropriate performance measures "may even be an open problem" for some settings.
- **The unpriced adversary.** P10's remedy is a precisely *defined* threat model and an adaptive, white-box adversary. There is no notion of a system being secure against adversaries within a stated resource bound, nor any recommendation to report one. For a literature that recommends white-box adaptive adversaries as the default, the absence of a budget parameter is the conspicuous hole.
- No inter-rater reliability statistics are reported for the coding.

## Quotes / Notable Passages

> "P10 – Inappropriate Threat Model. The security of machine learning is not considered, exposing the system to a variety of attacks, such as poisoning and evasion attacks."

> "Hence, threat models should be defined precisely and systems evaluated with respect to them. In most cases, it is necessary to assume an adaptive adversary that specifically targets the proposed systems and will search for and exploit weaknesses for evasion or manipulation."

> "we like to stress that an evaluation of adversarial aspects is not an add-on but rather a mandatory component in security research."

> "Every paper is affected by at least three pitfalls, underlining the pervasiveness of such issues in recent computer security research."

> "This work should not be interpreted as a fingerpointing exercise."
