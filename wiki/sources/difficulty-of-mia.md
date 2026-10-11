---
title: On the Difficulty of Membership Inference Attacks
type: source
date_ingested: 2026-08-20
authors: [Shahbaz Rezaei, Xin Liu]
venue: "CVPR 2021"
venue_evidence: "https://openaccess.thecvf.com/content/CVPR2021/html/Rezaei_On_the_Difficulty_of_Membership_Inference_Attacks_CVPR_2021_paper.html; IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2021), pages 7892-7900"
year: 2021
tags: [adversarial-ml, learning-theory]
claim_quantifier: empirical
antecedent: "Naturally trained discriminative image classifiers, attacked by confidence-value-based MIAs. Explicitly excluded by the authors: generative models, low-dimensional inputs, training-phase manipulation, and outlier samples."
cls_target: train data
cls_family: membership
cls_phase: post hoc
cls_access: scores
cls_write: read only
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: absent
cls_evidence_src: "no compute/query/time bound on the attacker anywhere in the threat model, §3-§6; attacks are confidence-value classifiers trained without any stated resource restriction"
cls_reason: "baseline=stated because ZeroR and the naive attack are introduced explicitly as the paper's central argument; access=scores per the antecedent's own framing (\"confidence-value-based MIAs\"), though §4 also tests gradient/activation features as a secondary experiment; frame=none because no computational bound is placed on the attacker, target, or auditor anywhere in the paper."
cls_prov: S
cls_date: 2026-08-22
---

> **Provenance.** Read from the primary PDF: abstract, §1–§4, §5 headline tables, §6 conclusion
> (recovered with `pdftotext -layout`, since the two-column conclusion is split across pages). Quoted
> passages verbatim.

## Summary

The earliest of the membership-inference critiques, and the one that first says the thing the rest keep rediscovering:
**membership inference numbers were being reported without the negative class.** Prior work reported
accuracy, precision, recall and F1 on the *member* class only. Those metrics conceal the false alarm
rate (FAR), i.e. how often a non-member is called a member. When the authors reproduce a published
attack on CIFAR-100, the reported picture (79.1% accuracy, 87.3% precision, 87.9% recall) coexists with
a 64.5% FAR and a 61.7% balanced accuracy against a ResNet target.

This is a **critique of evaluation practice**. The MI definition is not touched; what is attacked is
the reporting convention and the missing baseline.

The baseline argument is the sharpest part of the paper, and it is explicit in a way the later
literature is not. The authors introduce **ZeroR** — a classifier that always predicts "member" — and
show it matches or beats the published MI attack on precisely the metrics that were being reported
(83.3% precision, 100% recall on the positive class at a 5:1 member:non-member ratio). They also report
the **naive attack** (predict member iff the target model classifies the sample correctly), taken from
prior work. Neither baseline uses any membership signal, and neither had been reported alongside the
attacks they dominate. The paper further shows that positive-class precision is an artifact of the
evaluation set's balance: varying the member:non-member ratio from 5:1 to 1:5 drops the same attack
model's positive-class precision from 87.3% to 21.4% while balanced accuracy and FAR stay put at ~61%
and ~64%. So the reported metric was measuring the prior, not the attack.

The second half asks *why* MI is hard, and answers with a decomposition that has held up: split the
data into samples the target model classifies **correctly** and **incorrectly**. Membership inference
on correctly classified samples — the large majority of training data — is near-chance across MNIST,
CIFAR-10, CIFAR-100 and ImageNet and across LeNet, AlexNet, ResNet, DenseNet, InceptionV3 and Xception.
The residual signal lives almost entirely in the misclassified tail. The authors also try features
beyond confidence — intermediate-layer activations, gradient norms with respect to inputs and to
weights, and distance to the decision boundary — and find the same: *"deep models often behave
similarly on train and non-train samples across all these metrics."*

## Claim Boundary

- **Quantified over:** naturally trained discriminative image classifiers on MNIST, CIFAR-10,
  CIFAR-100 and ImageNet, attacked by confidence-based and gradient-based MIAs, with the attacker given
  deliberate advantages. **Empirical**, over these models and these attack families.
- **Antecedent:** the model is naturally trained (no poisoning, no training-phase manipulation) and
  discriminative. Both are stated as scope limits by the authors, not discovered later.
- **Does not establish:**
  - **not** that models do not memorize. The paper says only that current confidence-based attacks
    cannot reliably read the memorization out. The conclusion is hedged to *"under current attack
    models unless a new revolutionary approach is introduced"* — and one arrived a year later in
    [LiRA](mia-from-first-principles.md), which the authors could not have evaluated.
  - **not** a statement about generative models. Explicitly excluded: *"We do not extend our conclusion
    to generative models."*
  - **not** a statement about outliers. Explicitly excluded — the authors note MI may succeed on
    outliers whether classified correctly or not, which is exactly the direction
    [AZT24](privacy-defense-evaluations-misleading.md) later formalizes as the most-vulnerable-sample
    measurement.
  - **not** a statement about attacks that manipulate training (poisoning, model manipulation).
    Explicitly excluded.
- **Abstract vs theorem:** **minor gap.** The abstract says high FAR *"makes MI attacks fundamentally
  impractical"*, which reads as a general impossibility; the conclusion is properly hedged to current
  attacks. There is no theorem. The word "fundamentally" is not earned by the experiments, and the
  paper's own §1 list of excluded scenarios contradicts it. Read the conclusion, not the abstract.

## Key Contributions

- Identifies the missing negative class in MI reporting, and gives the reporting fix: report FAR (or
  precision and recall on the negative class) and balanced accuracy, plus the target model's train and
  test accuracy so the reader can see the generalization gap.
- **ZeroR** as an explicit named baseline for MI, together with the demonstration that it dominates
  published attacks on the published metrics.
- The demonstration that positive-class precision is a function of evaluation-set balance, not of the
  attack — the same attack model scores 87.3% or 21.4% precision depending only on the ratio.
- The correctly-classified / misclassified decomposition, and the finding that the signal lives in the
  misclassified tail. This is the empirical shadow of the later, sharper claim that MI vulnerability is
  concentrated on a few atypical samples.
- Negative results for four alternative feature families (intermediate layers, input gradients, weight
  gradients, decision-boundary distance) — all near-chance on correctly classified samples.
- The observation that many published targets are unusable: generalization gaps of 35%, 50%, even 80%
  in the models attacked by prior work.

## Key Definitions / Theorems

No theorems. The definitions that matter:

- **FAR / false alarm rate:** the fraction of non-members labelled member. Adopted from intrusion
  detection, where the base-rate problem is standard (the paper cites Axelsson's base-rate fallacy
  work).
- **ZeroR baseline:** *"a classifier that always predicts the positive class (member)."*
- **Naive attack baseline:** predict member iff the target model labels the sample correctly; predict
  non-member iff it misclassifies. Taken from prior work, reported here for completeness.
- **The base-rate argument:** in deployment the non-member class overwhelms the member class — *"a
  random sample, chosen from the distribution of all natural images, has a significantly higher
  probability of being a non-member sample than a member sample"* — but the true ratio is
  unestimable, so the paper reports ratio-insensitive metrics instead of guessing it.

## Connections

- **Superseded on the attack side, vindicated on the metric side:**
  [MIA From First Principles (CCNSTT22)](mia-from-first-principles.md), published a year later, makes
  the same objection to average-case metrics via ROC shape rather than via FAR, and then supplies the
  strong attack this paper says is missing. LiRA obtains non-trivial TPR at 0.001% FPR on CIFAR-10,
  which is a direct answer to this paper's "unless a new revolutionary approach is introduced". **Both
  positions should be recorded:** RL21's headline "MI is fundamentally impractical" is false as stated;
  RL21's reporting critique is correct and was adopted.
- **The same baseline complaint, later and for foundation models:**
  [Blind Baselines Beat MIA (DZT24)](blind-baselines-beat-mia.md) — ZeroR is to RL21 what the
  bag-of-words classifier is to DZT24: a model-free null that nobody reported.
- **The same complaint one level up:** [Privacy Defense Evaluations are Misleading (AZT24)](privacy-defense-evaluations-misleading.md)
  — a missing DP-SGD baseline for defences.
- **The LLM restatement of the "signal lives in the tail" finding:**
  [Do MIAs Work on LLMs? (DSM+24)](do-mias-work-on-llms.md).
- Concepts: [Blind Baseline](../concepts/blind-baseline.md),
  [Membership Inference Game](../concepts/membership-inference-game.md),
  [Low-FPR Evaluation Regime](../concepts/low-fpr-evaluation-regime.md).

## Open Questions / Limitations

- **The headline claim did not survive.** Stronger per-example attacks arrived immediately afterwards
  and do achieve high confidence at low FPR on a small subset of samples. What survives is the
  reporting critique and the tail decomposition, not the impossibility.
- The paper keeps the 5:1 member:non-member ratio and reports ratio-insensitive metrics, which
  sidesteps rather than solves the base-rate problem. It states plainly that *"there is no practical
  way to estimate the true value of this ratio."*
- Attacks are trained as classifiers on aggregate features; no per-example calibration is attempted,
  which is precisely the ingredient LiRA adds.
- Outliers — the samples that later work shows carry nearly all the leakage — are named as out of scope.

## Quotes / Notable Passages

- Abstract: *"the way the MI attack performance has been reported is often misleading because they
  suffer from high false positive rate or false alarm rate (FAR) that has not been reported."*
- §1: *"such extremely overfitted models have no practical use and the results on such models should
  not be generalized to well-trained models."*
- §3: *"ZeroR is a classifier that always predicts the positive class (member)."*
- §3: *"Relying only on precision and recall of the positive class can present a delusion of successful
  attack, particularly when the imbalancedness issue is ignored."*
- §6: *"naturally trained deep models often behave similarly across training and test samples and,
  hence, an accurate membership inference attack on all training samples in practice is a difficult and
  inaccurate task under current attack models unless a new revolutionary approach is introduced."*
