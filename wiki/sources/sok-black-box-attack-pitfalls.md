---
title: "SoK: Pitfalls in Evaluating Black-Box Attacks"
type: source
date_ingested: 2026-08-20
authors: [Fnu Suya, Anshuman Suri, Tingwei Zhang, Jingtao Hong, Yuan Tian, David Evans]
venue: arXiv preprint 2310.17534v2 (venue unconfirmed from PDF)
year: 2024
tags: [adversarial-ml, evasion-attacks, threat-model, evaluation-methodology, sample-complexity]
claim_quantifier: empirical
antecedent: none
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: black box
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: measured
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: implicit
cls_evidence: "Execution cost such as the local attack runtime should be used as the equalizing factor when comparing black-box attack performance, not the number of iterations."
cls_evidence_src: "§VII-A-1"
cls_reason: "Abstract leads with the four-axis knowledge taxonomy (query access, feedback, auxiliary-data quality/quantity), which bounds nobody computationally, matching the paper's own admission that these axes are never joined to a definition of robustness; the runtime finding is the paper's compute-relevant contribution and is classified per rule 7 as a reported, non-definitional cost, hence tightness=measured and assessed=implicit rather than explicit — the paper states outright that a defence is not credited for costing the attacker more. access=black box because the taxonomy spans hard-label/top-k/full-vector feedback without fixing one."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

Both a definitional paper and a practice critique, and it is worth keeping the two halves apart.

The definitional half proposes a four-axis taxonomy of black-box threat models: (1) **query access** — none, or interactive; (2) **API feedback** — hard label, top-`k` scores, or complete confidence vector; (3) **quality of initial auxiliary data** — no overlap, partial overlap, complete overlap with the target's training distribution; (4) **quantity of initial auxiliary data**. The availability of pretrained models is a sub-axis. 164 attacks are surveyed, 102 of them from major security, ML and vision venues, and placed in this grid. Three findings follow: most attacks cluster in a few cells, leaving practically important cells (notably top-`k` feedback, and abundant data from a non-overlapping distribution) nearly empty; several published state-of-the-art claims dissolve once the baseline is given the same knowledge the new attack assumes; and the grid exposes an interaction with model extraction and model inversion, which an attacker with auxiliary data and pretrained models can use to strengthen a black-box attack.

The practice half is where this paper diverges from the rest of the batch, and it is the reason it belongs in the compute strand. Transfer-attack evaluations conventionally normalize by *iteration count* — 10 iterations for untargeted, 40 for targeted, both arbitrary. The authors re-run 11 transfer attacks under a fixed *time* budget (30 minutes per batch) instead, and the ranking changes: MIDI-FGSM appears slightly worse than SMI-FGSM at equal iterations, but is roughly 2× faster per iteration, so at equal wall-clock time it wins. The recommendation is stated as a rule: "Execution cost such as the local attack runtime should be used as the equalizing factor when comparing black-box attack performance, not the number of iterations." The justification is a claim about what adversaries want — "these attacks are designed for adversaries that would only want to maximize success rates given available resources ... and not care about running the attack for a fixed number of attack iterations." Appendix C extends the same argument to interactive query attacks, where shifting the metric from query count to local runtime reverses the RayS-versus-BayesOpt comparison.

This is a direct, if unacknowledged, collision with [CAP+19 §4.8](on-evaluating-adversarial-robustness.md) and [ACW18 §6.1](obfuscated-gradients.md). Those papers reject attacker compute as a threat-model parameter on the grounds that no realistic attacker is separated by an order of magnitude of gradient steps. This paper accepts attacker compute as the *comparison metric between attacks*, on the grounds that a real attacker maximizes success within a resource budget. Note carefully what is and is not being claimed: runtime here normalizes attacks against each other, and never enters the definition of robustness. A defence is still not credited for costing the attacker more.

A second methodological finding is negative and specific: an attacker cannot use local-model success or local loss as a stopping rule. Local attack success reaches 100% almost immediately while target ASR is still low, and on an adversarially-trained target the local loss keeps converging long after target ASR has peaked at around ten iterations.

## Claim Boundary

- **Quantified over:** the taxonomy ranges over black-box attacks on image classifiers published 2014–2023 in a named venue list plus preprints found by citation search — 164 attacks, 102 peer-reviewed. The runtime experiments range over 11 transfer attacks selected from 20 I-FGSM variants "that span a wide range of local runtimes", against specified target models (DenseNet201 targeted; adversarially-robust Inception-v3 untargeted), at a 30-minute-per-batch budget on the authors' hardware.
- **Antecedent:** none formally. The runtime recommendation carries a stated behavioural premise — that the adversary's real constraint is a time or resource budget rather than an iteration count. That premise is argued from a cited study of practitioners, not measured by this paper.
- **Does not establish:** (a) that runtime is a security parameter — it is proposed as an *evaluation-comparison* metric between attacks, and the paper never suggests that a model resistant to a fixed time budget is thereby secure; (b) that these rankings transfer across hardware — the authors flag exactly this, choosing total runtime "due to the challenge in standardizing components' runtimes across different hardware configurations, acknowledging both methods have their merits and limitations"; (c) that the four axes are complete — training-time adversaries and poisoned or dynamically-changing target models are explicitly out of scope; (d) that the results transfer to security-critical domains — the limitations section concedes "Our analysis of evaluated attacks is focused on image classifiers, which is not a security-critical application"; (e) that the new top-`k` attack is strong in absolute terms — it sets a new state of the art in an under-explored cell while still falling short of attacks from the more restrictive hard-label setting, which the paper presents as evidence of a technical gap.
- **Abstract vs theorem:** mild. The abstract says the runtime lens "reveals the potential for certain attacks to achieve notably higher success rates", which is accurate. The stronger-sounding claim, "overturning claims in the respective paper", refers to one specific baseline comparison and is scoped in the body.

## Key Contributions

- The four-axis black-box threat-model taxonomy (query access, API feedback, auxiliary-data quality, auxiliary-data quantity), with pretrained models as a sub-axis, and the classification of 164 attacks into it (Table I).
- Identification of under-explored cells that match deployed APIs — top-`k` confidence scores, and abundant non-overlapping data — and a new attack for the top-`k` setting that establishes state of the art there while still trailing the hard-label setting.
- Demonstration that state-of-the-art claims can be invalidated by adapting the *baseline* to the same threat model, rather than by improving the new attack.
- **Runtime, not iterations, as the equalizing metric** for comparing attacks, with a rank-reversal demonstration (MIDI-FGSM vs SMI-FGSM) at fixed wall-clock time, and a corresponding reversal for interactive attacks (RayS vs BayesOpt) when the metric shifts from queries to local runtime.
- The negative stopping-rule result: local attack success and local loss are both unusable as signals for when to stop, in opposite directions.
- The argument that evaluations should be run in harder settings (targeted; halved perturbation budget; adversarially-trained targets), because relative attack rankings are only distinguishable there.
- Identification of model extraction and model inversion as resources a black-box attacker can compose with, given auxiliary data and pretrained models.
- A modular codebase for black-box attack evaluation.

## Key Definitions / Theorems

No theorems. Definitions and constructs:

- **Untargeted / targeted attack goals**, defined with respect to the *ground-truth* label `c(x)` rather than the model's prediction, matching the implicit convention in the surveyed attacks.
- **Query access** (§IV-A): *no interactive access* (one-way communication, e.g. malware that must bypass a classifier it cannot probe) versus *with interactive access* (queries may be adaptive, but may be rate-limited, priced, or self-limited to avoid suspicion). The unlimited case is instantiated concretely as a model running on the attacker's own hardware inside a trusted execution environment.
- **API feedback** (§IV-B): hard-label / top-`k` (`1 ≤ k < N`) / complete confidence vector. Top-`k` with `k = 1` is strictly more than hard-label, because the confidence value is revealed.
- **Quality of auxiliary data** (§IV-C): overlap defined on *distributions*, not datasets, over feature space and label space — no overlap / partial overlap / complete overlap.
- **Quantity of auxiliary data** (§IV-D), kept independent of quality.
- **Runtime-equalized comparison**: attacks compared at fixed total execution time rather than fixed iteration count.

## Connections

- Directly opposes the compute position of [On Evaluating Adversarial Robustness (CAP+19)](on-evaluating-adversarial-robustness.md) §4.8 and [Obfuscated Gradients (ACW18)](obfuscated-gradients.md) §6.1, though only at the level of attack-versus-attack comparison, not at the level of the robustness definition.
- Complementary to [SoK: Analyzing Adversarial Examples (FK24)](sok-adversary-knowledge.md), published within months of it. FK24 gives an order-theoretic structure over adversary knowledge but no compute axis; this paper adds the cost dimension but no order structure. Neither cites the other in the PDFs read.
- Adopts, in its recommendation to run attacks "until attack success rates plateau", the convergence check of [CAP+19 §4.8](on-evaluating-adversarial-robustness.md) — the same section that rejects compute as a threat-model parameter.
- Uses adversarially-trained targets of the kind catalogued by [RobustBench](robustbench.md), and its "evaluate in harder settings" recommendation is the complaint that undefended-model evaluations are saturated.
- Its model-extraction interaction connects to [Model Extraction](../concepts/model-extraction.md), [High Accuracy and High Fidelity Extraction of Neural Networks (JCB+20)](jagielski-model-extraction.md), and [Beyond Labeling Oracles](beyond-labeling-oracles.md) — the last of which makes the parallel complaint on the extraction side, that the field's success criterion is a cost inequality left informal.
- Concepts: [Adversary Knowledge Taxonomy](../concepts/adversary-knowledge-taxonomy.md), [Evasion Attacks](../concepts/evasion-attacks.md), [Adaptive Attacks](../concepts/adaptive-attacks.md).
- Authors: [David Evans](../entities/david-evans.md).

## Open Questions / Limitations

- Wall-clock runtime is hardware-dependent, and the paper says so. No hardware-independent cost measure (gradient evaluations, FLOPs, forward passes) is proposed, and the authors record that they chose total runtime because algorithmic measures are hard to standardize — which is the exact difficulty a formal cost-parameterized definition would have to solve.
- Runtime is used to rank attacks, never to grade defences. The paper does not ask whether a defence that multiplies attacker runtime has improved security, and does not connect its metric to any definition of robustness.
- The taxonomy covers prediction-time attacks only. Poisoning and dynamically-changing targets are excluded by scope.
- The stopping-rule result is negative with no replacement: "Developing metrics that can help predict optimal target ASR is a direction for future work."
- Image classification only, which the authors call out as not security-critical.
- Under-explored cells are identified but only one (top-`k`) is attacked, and the resulting attack is weaker than attacks in a strictly more restrictive setting — the paper reads this as a technical gap rather than as evidence the cell is intrinsically harder, and does not distinguish the two.

## Quotes / Notable Passages

The recommendation that collides with the CAP+19 and ACW18 position:

> "Execution cost such as the local attack runtime should be used as the equalizing factor when comparing black-box attack performance, not the number of iterations."

The premise it rests on:

> "these attacks are designed for adversaries that would only want to maximize success rates given available resources [5], and not care about running the attack for a fixed number of attack iterations."

On why wall-clock time was chosen over an algorithmic cost measure:

> "We opt for measuring total runtime over algorithmic measures due to the challenge in standardizing components' runtimes across different hardware configurations, acknowledging both methods have their merits and limitations."

On the stopping rule, stated as an open problem:

> "Do not rely on attack success or loss on local models as a metric to stop optimization. Developing metrics that can help predict optimal target ASR is a direction for future work."

On the scope of the whole study:

> "Our analysis of evaluated attacks is focused on image classifiers, which is not a security-critical application."
