---
title: Membership Inference Attacks From First Principles
type: source
date_ingested: 2026-08-20
authors: [Nicholas Carlini, Steve Chien, Milad Nasr, Shuang Song, Andreas Terzis, Florian Tramèr]
venue: "IEEE Symposium on Security and Privacy (S&P) 2022, pp. 1897–1914 (venue taken from the bibliography of ZDKT25, ref. [7]; the PDF itself carries only arXiv:2112.03570v2)"
year: 2022
tags: [adversarial-ml, computational-indistinguishability, sample-complexity, learning-theory]
claim_quantifier: empirical
antecedent: "The adversary can train N shadow models on data from the target's distribution, and the per-example loss distributions (in logit scale) under the IN and OUT worlds are approximately Gaussian. Both are constructions of the paper, not properties of the target."
cls_target: train data
cls_family: membership
cls_phase: post hoc
cls_access: scores
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: measured
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: none
cls_assessed: implicit
cls_evidence: "For each dataset, the adversary trains N shadow models (N = 64 for ImageNet, and N = 256 otherwise) on training sets chosen so that each example (x, y) is contained in exactly half of the shadow models' training sets."
cls_evidence_src: "Section VI-A (offline attack evaluation, adversary's shadow-model training procedure), raw/CCNSTT22_MIAFirstPrinciples.pdf"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows. DISPUTE 2026-09-03: unit. The quotation prices the attacker in a count of shadow-model training runs (N = 64 or 256), not wall-clock time; the codebook has no training-runs unit (a gap already recorded against membership-inference-shokri, an identical case), so time is the nearest available proxy rather than the unit the paper itself reports."
cls_prov: P
cls_date: 2026-08-22
---

> **Provenance.** Read from the primary PDF: abstract, §I–§V, §VI-D, §VII–§VIII. Quoted passages
> verbatim. Section VI ablations and appendices skimmed for headline numbers only.

## Summary

This is the paper that made the low-FPR regime the standard for membership inference, and it is a
**critique of evaluation practice**, not of the membership inference definition. The definition (its
Definition 1, a challenger/adversary security game) is adopted from Yeom et al. and Jayaraman et al.
unchanged. What is attacked is the *metric*: prior work reported balanced accuracy or ROC-AUC, both of
which average over an entire dataset and over all decision thresholds, and both of which are
insensitive to whether the attack can confidently identify *anyone*.

The paper's demonstration is exact and worth keeping: the LOSS attack has 60% balanced accuracy on
CIFAR-10, which reads as a meaningful privacy violation. But on the 1% of samples where it is most
confident of membership it is correct 48% of the time — worse than guessing — while on the 1% where it
is most confident of *non*-membership it is correct 100% of the time. So the attack is a strong
non-membership inference attack, and useless as a membership attack, and balanced accuracy cannot see
the difference. Its TPR at 0.1% FPR is 0%.

The constructive half is **LiRA**, the Likelihood Ratio Attack. Membership inference is framed as a
hypothesis test between `Q_in(x,y) = {f ← T(D ∪ {(x,y)})}` and `Q_out(x,y) = {f ← T(D \ {(x,y)})}`, and
the Neyman–Pearson lemma says the best test at fixed FPR thresholds the likelihood ratio. The ratio over
model parameters is intractable, so the paper replaces it with the ratio over the one-dimensional
statistic `ℓ(f(x),y)`, estimates the two loss distributions with shadow models, and assumes both are
Gaussian after a logit rescaling — reducing the whole test to four parameters per example. The result is
roughly a 10× improvement at low FPR while also dominating prior attacks on the old aggregate metrics.

**The baseline theme in this paper is the threshold, not a missing null.** Prior attacks used a single
global threshold `τ` for every example; LiRA's gain comes almost entirely from replacing it with a
per-example null distribution estimated from shadow models. The ablation makes this explicit: adding
per-example thresholds alone takes TPR at 0.1% FPR from 0% to 1.7%.

## Claim Boundary

- **Quantified over:** image and text classification models the authors trained themselves —
  CIFAR-10, CIFAR-100, ImageNet, WikiText-103 — plus pre-trained CIFAR-10 models from a third party,
  attacked with 256 shadow models. The metric argument is general; the attack numbers are these
  datasets and these training pipelines.
- **Antecedent:** the adversary gets query access to the data distribution `D` (to train shadow
  models) and the target example's ground-truth label. LiRA additionally assumes the per-example
  IN/OUT loss distributions are Gaussian in logit scale — the paper checks this empirically (Fig. 4)
  and shows the logit is the only one of three candidate scalings that is well approximated by a pair
  of Gaussians. Both assumptions are **stated and instrumented**, not hidden.
- **Does not establish:**
  - **not** that models with low train-test gap are safe. The paper finds *"examples of models that
    have identical train-test gaps but are 100× more vulnerable to attack"*, breaking the folk
    identification of memorization with overfitting.
  - **not** that low FPR is the *only* correct metric. It is proposed as necessary, not sufficient —
    and [AZT24](privacy-defense-evaluations-misleading.md) later shows a population-level TPR at low
    FPR still misses the most vulnerable individual.
  - **not** any statement about foundation models with unknown training sets. Everything here is
    "in-the-lab": the authors train the models and know the split. That is precisely the setting
    [ZDKT25](mia-cannot-prove-training.md) §V affirms as sound and the rest of the membership-inference critiques say the
    foundation-model literature left.
  - **not** a claim that prior defences are broken. §VIII lists that as open work: *"Prior defenses
    were only ever shown to be ineffective at preventing an adversary from succeeding on average."*
- **Abstract vs theorem:** none found. The abstract's claim — "10× more powerful at low false-positive
  rates, and also strictly dominates prior attacks on existing metrics" — is what §V measures. The
  paper carries no theorem beyond invoking Neyman–Pearson, and it is explicit that the exact
  likelihood-ratio test is *"intractable"* and that what is implemented is a one-dimensional
  approximation of it.

## Key Contributions

- **The evaluation argument.** Report TPR at low FPR (0.1%, 0.001%) and full log-scale ROC curves;
  balanced accuracy and AUC are inadequate because privacy is not an average-case property and because
  the AUC integrates over FPRs above 50% that no attacker would ever operate at.
- The two-attack thought experiment that makes the point definitional rather than stylistic: an attack
  that perfectly identifies 0.1% of users and coin-flips on the rest has the same balanced accuracy as
  one that succeeds with 50.05% probability on everyone, and *"the second attack is practically
  useless, while the first attack is exceptionally potent."*
- **LiRA**: per-example Gaussian likelihood ratio over shadow-model loss distributions, with logit
  rescaling and multi-augmentation queries; online and offline variants.
- The empirical finding that overfitting is not the right predictor of MI vulnerability, and that more
  accurate models are, at fixed generalization gap, more vulnerable.
- An explicit re-opening of the literature: §VIII asks whether label-only attacks, previously
  "broken" defences, and DP-SGD conclusions survive re-evaluation at low FPR.

## Key Definitions / Theorems

- **Definition 1 (Membership inference security game).** Challenger samples `D ← 𝔻` and trains
  `f_θ ← T(D)`; flips `b`; if `b = 0` draws a fresh `(x,y) ← 𝔻` with `(x,y) ∉ D`, else draws
  `(x,y) ←$ D`; sends `(x,y)`; adversary with query access to `𝔻` and `f_θ` outputs `b̂`. Output 1 iff
  `b̂ = b`. **Note the sampling:** both the dataset and the challenge point are random, which places
  this game at the average-case end of the spectrum — the point AZT24 later presses on.
- **Definition 2 (Balanced attack accuracy).** `Pr_{x,y,f,b}[A^{D,f}(x,y) = b]`. Defined in order to be
  rejected.
- **The two worlds.** `Q_in(x,y) = {f ← T(D ∪ {(x,y)}) | D ← 𝔻}` and
  `Q_out(x,y) = {f ← T(D \ {(x,y)}) | D ← 𝔻}`.
- **Likelihood ratio (Eq. 2):** `Λ(f; x,y) = p(f | Q_in(x,y)) / p(f | Q_out(x,y))`, thresholded per
  Neyman–Pearson. Replaced in practice by the same ratio over `ℓ(f(x),y)` under fitted Gaussians.
- **LOSS attack (baseline):** `A_loss(x,y) = 1[-ℓ(f(x),y) > τ]`, a single global threshold.

## Connections

- **The definitional counterpart:** [MIA Cannot Prove Training (ZDKT25)](mia-cannot-prove-training.md)
  takes this paper's hypothesis-testing framing and asks whether `Q_out` can be sampled at all outside
  the lab. It cannot, for a production model. This paper's `Q_out` is sampled by *actually training
  shadow models*, which is exactly the step that does not scale.
- **The next turn of the same screw:** [Privacy Defense Evaluations are Misleading (AZT24)](privacy-defense-evaluations-misleading.md)
  accepts TPR at low FPR and shows it is still an aggregate — a defence that fully leaks one sample
  passes it. AZT24 builds directly on LiRA.
- **What happens when this is carried to LLMs:** [Do MIAs Work on LLMs? (DSM+24)](do-mias-work-on-llms.md)
  notes LiRA *"require[s] training multiple copies of shadow models, which is often intractable for
  LLMs"*; [Blind Baselines (DZT24)](blind-baselines-beat-mia.md) and
  [SoK: Rushing Nowhere (MSJ+25)](sok-mia-llms-rushing-nowhere.md) show what the substitutes cost.
- **Concurrent complaint about the same metrics:** [On the Difficulty of MIA (RL21)](difficulty-of-mia.md)
  reaches the false-positive-rate objection independently and a year earlier, from the ZeroR-baseline
  direction rather than the ROC-shape direction.
- [DP-SGD (Abadi et al.)](deep-learning-differential-privacy.md) — the provable defence this attack is
  used to audit; §A-A reports preliminary evidence that even vacuous DP-SGD guarantees blunt low-FPR
  attacks, a finding AZT24 later confirms and quantifies.
- [Model Extraction (Jagielski et al.)](jagielski-model-extraction.md) — same first author; the
  extraction setting where false positives are the costly error, which is the paper's motivation for
  the low-FPR regime.
- Concepts: [Membership Inference Game](../concepts/membership-inference-game.md),
  [Low-FPR Evaluation Regime](../concepts/low-fpr-evaluation-regime.md).

## Open Questions / Limitations

- **Cost.** LiRA needs many shadow models (256 in the headline experiments). §VIII names computational
  efficiency as the key usability limitation. This cost is the hinge on which the whole foundation-model
  branch of this literature turns: it is why post-hoc member/non-member sets were invented, and hence
  why the rest of the membership-inference critiques exist.
- The Gaussian assumption is empirical. It holds for logit-scaled confidences on the datasets tested;
  no argument is given that it must.
- The game samples both `D` and the challenge point at random. Worst-case membership privacy — an
  adversarially chosen dataset and target, as DP assumes — is a different quantity and is not measured.
- The paper explicitly declines to draw conclusions about the Purchase and Texas datasets, arguing they
  are too simple to generalize from, and relegates them to the appendix.
- §VIII lists four re-evaluations as owed and does not perform them.

## Quotes / Notable Passages

- Abstract: *"These attacks are currently evaluated using average-case 'accuracy' metrics that fail to
  characterize whether the attack can confidently identify any members of the training set."*
- §I: *"privacy is not an average case metric, and should not be evaluated as such."*
- §III-B: *"the LOSS attack is actually a strong non-membership inference attack, and is practically
  useless at inferring membership."*
- §III-B: *"If a membership inference attack can reliably violate the privacy of even just a few users
  in a sensitive dataset, it has succeeded."*
- §III-B, on AUC: *"The TPR of an attack when the FPR is above 50% is not meaningfully useful, yet this
  regime accounts for more than half of its AUC score."*
- §V-D: *"we do find examples of models that have identical train-test gaps but are 100× more
  vulnerable to attack."*
- §VIII: *"we can evaluate privacy not as a measurement of the average user, but of the most
  vulnerable."*
