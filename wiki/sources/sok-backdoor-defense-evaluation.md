---
title: "SoK: The Last Line of Defense — On Backdoor Defense Evaluation"
type: source
date_ingested: 2026-08-20
authors: [Gorka Abad, Marina Krček, Stefanos Koffas, Behrad Tajalli, Marco Arazzi, Roberto Riaño, Xiaoyun Xu, Zhuoran Liu, Antonino Nocera, Stjepan Picek]
venue: "arXiv:2511.13143"
venue_evidence: "web search found no refereed venue yet; paper's own text says results follow \"after acceptance of the paper,\" confirming it is still unaccepted/preprint"
year: 2025
tags: [adversarial-ml, poisoning-attacks, backdoor, evaluation-methodology, survey]
claim_quantifier: empirical
antecedent: none
cls_target: train data
cls_family: backdoor
cls_phase: train time
cls_access: none
cls_write: corpus
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: "absent"
cls_evidence_src: "no bound in R1-R9/C1-C8, the coded threat-model fields, or the re-run methodology; Open Questions states adaptiveness is recorded as yes/no and R6 asks only for defense execution time"
cls_reason: "Attack scenario read off the backdoor literature the SoK studies (poisoning writes to the training corpus), not off the SoK's own claim, which is a meta-critique of evaluation practice with no resource bound on attacker or defender anywhere; 170 GPU-days is the authors' own study cost, not a party's bound, so it does not trigger assessed."
cls_prov: S
cls_date: 2026-08-22
---

## Summary

This is a critique of **practice**, not of any definition. AKK+25 is a meta-analysis of how the backdoor-defense literature evaluates itself: 183 defense papers published 2018–2025 at nine A* venues (S&P, USENIX Security, NDSS, CCS on the security side; ICLR, ICML, NeurIPS, CVPR, AAAI on the AI side), each manually coded into a released .csv along dimensions including threat model, defender knowledge, defender capability, access to resources, poisoning rate, attacker adaptiveness, metrics and execution time. On top of the survey the authors re-run 15–16 representative defenses against five attacks (BadNets, Blended, WaNet, AdvDoor, Narcissus) on MNIST, CIFAR-100 and ImageNet-1K across ResNet-18, VGG-19, ViT-B/16 and DenseNet-121 — over 3 000 experiments, 170 GPU-days.

The survey half reports that the field's evaluation practice is narrow and heterogeneous in ways that make cross-paper comparison impossible: 73% of defenses evaluate only on MNIST or CIFAR-10; ImageNet-1K appears in ≈20%; the five most-used attacks are dominated by BadNets and Blended, and the most recent among them dates to 2021; only 9 of 183 papers report anything about attack stealthiness; execution time is reported in ≈5%; ≈80% release code; ≈58% consider an adaptive attacker (≈55% at AI venues, ≈67% at security venues). Deployment stage is skewed to the reactive end — nearly 60% post-training, 33% in-training, under 5% pre-training or hybrid.

The re-run half is the load-bearing part for this wiki. Re-evaluating published defenses on harder datasets and against stealthier attacks produces "substantial performance degradation that contradicts published claims": defenses that work on MNIST fail on ImageNet-1K, several to CA ≈ 0; a defense (compatibility clustering) fails against the *simplest* attack, BadNets, at ASR 93.8%, refuting the field's implicit assumption that worst-case success implies easy-case success. The authors introduce **MADS** (Mean Absolute Difference Score), the mean absolute deviation of a defense's ASR across datasets under fixed settings, as a cross-dataset consistency metric, and find high variability nearly everywhere.

The output is nine recommendations (R1–R9, actionable with known solutions) and eight challenges (C1–C8, open research), plus an evaluation checklist covering diversity over quantity, fair hyperparameter treatment, reporting of execution time and no-attack behaviour, statistical significance over repeated runs, mandatory adaptive-attacker assessment, and community-maintained baselines.

## Claim Boundary

- **Quantified over:** two disjoint populations. The survey claims range over the 183 papers at the nine named venues, 2018–2025 — not over the backdoor-defense literature as a whole, which the authors note is "significantly higher" in count. The empirical claims range over the specific defense × attack × dataset × architecture grid actually run, at the defenses' **default hyperparameters** taken from their official repositories.
- **Antecedent:** none. All claims are measured, not conditional. The nearest thing to a hypothesis is the choice to use default hyperparameters, which the authors justify because most defense papers give no strategy for selecting hyperparameters in an unknown scenario.
- **Does not establish:** that any surveyed defense is *unsound* — the failures are of generalization across setups, not counterexamples to stated theorems (few of these defenses state theorems). It establishes nothing about **adversary resource budgets**: the SoK counts *whether* an adaptive attacker was considered, and it demands execution-time reporting for the **defense**, but it never parameterizes the attacker by compute, memory, samples or queries, and there is no notion of a defense holding up to a stated attacker budget. "Adaptive" here is a binary property of the evaluation, not a quantity. Cite this page for the claim that threat-model assumptions go unstated and unstandardized; do **not** cite it for any claim about attacker cost.
- **Abstract vs theorem:** Two overstatements found. (i) The introduction says "defenses are almost never tested against adaptive attackers", while the paper's own §3.2 measures ≈58% of the 183 papers as considering one — the qualitative framing contradicts the quantitative finding. (ii) The abstract says "16 representative defenses"; the contributions list says "15 representative defenses". Also, the introduction asserts "The vast majority of defenses are evaluated exclusively against outdated, dirty-label attacks", stronger than the supporting statistic, which is about which five attacks are most common.

## Key Contributions

- **First SoK on backdoor defense *evaluation methodology*** rather than on attacks or defenses. Prior surveys catalogue techniques; Table 4 contrasts their coverage and shows they rarely record poisoning rates, execution-time constraints or attacker adaptiveness.
- **A coded, released dataset of 183 papers** with per-paper threat-model, knowledge, capability, resource, metric and reporting fields — the artifact that makes the "assumptions are not stated uniformly" claim checkable.
- **Threat-model assumptions treated as a first-class extraction field**, alongside defender knowledge (architecture, hyperparameters, weights, backdoor existence, trigger, trigger properties, trigger distribution, targeted vs untargeted) and defender resources (poisoned data, clean data, weights, feature maps, auxiliary models). The finding is inconsistency and unrealism, e.g. the widespread assumption of access to clean training data, which C1 calls unrealistic for models distributed through repositories such as HuggingFace.
- **Re-evaluation that contradicts published claims** — over 3 000 runs, 170 GPU-days.
- **MADS**, a cross-dataset ASR-consistency metric.
- **R1–R9 and C1–C8**, plus an evaluation checklist (Appendix).

## Key Definitions / Theorems

No theorems. The formal content is definitional bookkeeping and one metric.

- **Poisoning rate** ε = M/N, M poisoned of N training samples; dirty-label vs clean-label by whether ŷ ≠ y; static (sample-agnostic) vs dynamic (sample-specific) triggers; source-agnostic vs source-specific activation.
- **Attack success rate (ASR)** and **clean accuracy (CA)** as the two core metrics; C4 records that non-standard metrics ("anomaly index" and others) are introduced without justification, harming comparability.
- **MADS_d** = (1 / (EX·|D|)) Σ_e Σ_i |ASR^{D_i}_{d,e} − μ_{d,e}|, with μ_{d,e} the mean ASR of defense d in experiment e across datasets D. Lower is more consistent.
- **Selected recommendations/challenges:** R1 release code; R2 balance deployment phases toward proactive defenses; R5 vary attack stealthiness across pixel/latent/parameter/frequency spaces; R6 report execution time against a no-defense baseline on identical hardware; R7 report the defense's impact when no attack is present; R8 evaluate across difficulty levels including simple attacks and adaptive attackers; R9 tune and validate on multiple datasets. C1 remove dependence on clean/poisoned training data and auxiliary models; C4 lack of standardized terminology and metrics; C5 defenses are not architecture- or dataset-agnostic despite claiming to be; C7 consistent robustness across poisoning strengths; C8 hyperparameter sensitivity across datasets.

## Connections

- The backdoor-defense analogue of [Dos and Don'ts of Machine Learning in Computer Security](dos-and-donts-ml-security.md), which makes the same move field-wide; AKK+25's threat-model findings instantiate that paper's pitfall P10.
- Extends and post-dates [On Evaluating Neural Network Backdoor Defenses (VG20)](evaluating-nn-backdoor-defenses.md), which raised the same three pitfalls at five-defense scale in 2020.
- **Contrast with** [Towards a Critical Evaluation of Robustness for DL Backdoor Countermeasures (QMZ+22)](critical-evaluation-backdoor-countermeasures.md): QMZ+22's defenses break from ordinary configuration variation with *no* adaptive attack at all. Not every evaluation failure is an attacker-budget failure, and neither paper is evidence about attacker budgets.
- Empirical counterpart to the theory side of backdoor security: [Planting Undetectable Backdoors](planting-undetectable-backdoors.md), [iO-Undetectable Backdoors in Neural Networks](io-undetectable-backdoors-nn.md), [Oblivious Defense Against Backdoor Removal](oblivious-defense-backdoor-removal.md), [Backdoor Defense, Learnability and Obfuscation](backdoor-defense-learnability-obfuscation.md), [Crypto Backdoors: Boon and Bane](crypto-backdoor-boon-bane.md). Those results price detection and removal in complexity terms; this SoK measures a literature that never states a budget. The gap between the two is the point of the strand.
- Related to certified approaches that do carry guarantees: [Certified Defenses for Data Poisoning](certified-defenses-data-poisoning.md), [Robustly Reliable Learners under Poisoning](robustly-reliable-learners-poison.md).
- Concepts: [Poisoning Attacks](../concepts/poisoning-attacks.md), [Undetectable Backdoors](../concepts/undetectable-backdoors.md), [Backdoor Defense Evaluation](../concepts/backdoor-defense-evaluation.md), [Defendability](../concepts/defendability.md).
- Author: [Stjepan Picek](../entities/stjepan-picek.md).

## Open Questions / Limitations

- The authors' own open challenges: architecture-agnostic defenses (C5), robustness across trigger types (C6), hyperparameter-insensitive methods (C8), defenses that do not need clean or poisoned training data (C1).
- Their closing call is for "theoretical frameworks that connect defense mechanisms to attack characteristics, rather than focusing on empirical results" — an invitation the crypto-side backdoor literature could answer, and which no cited work in this SoK does.
- **No resource axis.** Adaptiveness is recorded as a yes/no. The natural next definition — a defense certified against attackers within a stated compute, query or poisoning budget — is absent from all 183 papers and from this SoK's own recommendations. R6 asks for *defense* execution time only.
- The survey covers nine venues only; the authors say the true count of backdoor-defense papers is far higher, so prevalence percentages are venue-conditioned.
- Coding of 183 papers was manual; no inter-rater agreement is reported.
- Re-runs use default hyperparameters, which is fair but conflates "defense is brittle" with "defense is untuned for this setting"; the authors acknowledge that most papers provide no tuning strategy.

## Quotes / Notable Passages

> "Our analysis reveals significant inconsistencies in experimental setups, evaluation metrics, and threat model assumptions in the literature."

> "When we re-evaluate selected defenses on more challenging datasets and against adaptive, stealthy attacks, we observe substantial performance degradation that contradicts published claims."

> "These evaluation gaps create a false sense of security: defenses appear highly effective on toy benchmarks but may fail under realistic threat models."

> "The common assumption that a defense effective under worstcase conditions will also succeed in simpler ones does not always hold."

> "Future work should focus on establishing communitymaintained leaderboards and developing theoretical frameworks that connect defense mechanisms to attack characteristics, rather than focusing on empirical results."
