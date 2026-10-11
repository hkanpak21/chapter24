---
title: Low-FPR Evaluation Regime
type: concept
tags: [adversarial-ml, differential-privacy, certification]
---

## Definition

The convention that a privacy attack should be scored by its **true positive rate at a low false
positive rate** — 0.1%, 0.001% — reported together with the full ROC curve on log-log axes, rather than
by balanced accuracy or ROC-AUC.

Introduced as a corrective in
[Carlini et al., MIA From First Principles](../sources/mia-from-first-principles.md), and now standard.

## Intuition

Balanced accuracy and AUC both average, and averaging destroys the quantity of interest.

- **Balanced accuracy is symmetric.** It charges false positives and false negatives equally. But for
  an attacker, and for the extraction pipelines that use MI as a filtering stage, a false positive is
  the expensive error and a false negative is free.
- **Balanced accuracy is an average.** An attack that perfectly identifies a known 0.1% of users and
  coin-flips on the rest has the same balanced accuracy as one that succeeds with probability 50.05% on
  everyone. The first is a real attack; the second is nothing.
- **AUC integrates over irrelevant regions.** More than half of an AUC score comes from FPRs above 50%,
  where no attacker would operate.

The concrete demonstration: the LOSS attack on CIFAR-10 has 60% balanced accuracy, but on the 1% of
samples where it is most confident of *membership* it is right 48% of the time — worse than guessing —
and on the 1% where it is most confident of *non*-membership it is right 100% of the time. Its TPR at
0.1% FPR is 0%. It is a strong non-membership inference attack, and balanced accuracy cannot see that.

**The regime has since been shown to be necessary but not sufficient.**
[Aerni–Zhang–Tramèr](../sources/privacy-defense-evaluations-misleading.md) point out that a
population-level TPR at low FPR is still an aggregate: the threshold is set so that the attack makes few
false guesses *across the whole population*, and the score counts what fraction of members are
identified. So a defence that fully leaks a fixed number of individuals can be made to look private by
enlarging the dataset. Their sample-level refinement fixes the target `x`, sets a per-sample threshold
`T_x`, and takes probabilities over dataset draws and training runs. On CIFAR-10 the most vulnerable
sample has 99.9% TPR at 0.1% FPR where the population metric reads 4%.

The sequence of corrections is one repeated move — replace an average by a per-object quantity — applied
three times:

| level | threshold | measured over | source |
|---|---|---|---|
| LOSS attack | one global `τ` | all samples | Yeom et al., per CCNSTT22 |
| LiRA | per-example `τ_x` from shadow models | all samples | [CCNSTT22](../sources/mia-from-first-principles.md) |
| canary audit | per-sample `T_x` | one sample, many training runs | [AZT24](../sources/privacy-defense-evaluations-misleading.md) |

## Properties / Theorems

- Per-example thresholds are where the gain lives. In the LiRA ablation, adding per-example thresholds
  alone moves TPR at 0.1% FPR from 0% to 1.7%; correct loss rescaling and Gaussian fitting add a further
  3.3×, and multiple augmentation queries roughly double it again.
- **Population TPR at low FPR is dilutable.** `NS_x̂`, the mechanism that reveals membership of one fixed
  point, satisfies `TPR ≤ FPR + 1/|D|` under population-level evaluation.
- Vulnerability is not predicted by the generalization gap. CCNSTT22 finds models with identical
  train-test gaps differing 100× in TPR at 0.1% FPR, and finds more accurate models more vulnerable at
  fixed gap.
- Reporting at low FPR does not by itself validate a benchmark. All the low-FPR numbers reported for
  foundation-model MI benchmarks are beaten by classifiers with no model access at all — see
  [Blind Baseline](blind-baseline.md).

## Where It Appears

- [MIA From First Principles (CCNSTT22)](../sources/mia-from-first-principles.md) — origin.
- [Privacy Defense Evaluations are Misleading (AZT24)](../sources/privacy-defense-evaluations-misleading.md)
  — the sample-level refinement, and the canary protocol that makes it affordable.
- [On the Difficulty of MIA (RL21)](../sources/difficulty-of-mia.md) — the same objection reached a year
  earlier through the false alarm rate and the base-rate fallacy, without the ROC framing.
- [Blind Baselines Beat MIA (DZT24)](../sources/blind-baselines-beat-mia.md),
  [SoK: Rushing Nowhere (MSJ+25)](../sources/sok-mia-llms-rushing-nowhere.md),
  [Do MIAs Work on LLMs? (DSM+24)](../sources/do-mias-work-on-llms.md) — all report in this regime.
- [MIA Cannot Prove Training (ZDKT25)](../sources/mia-cannot-prove-training.md) — argues that in the
  production setting the FPR whose low values this regime reports cannot be estimated at all.

## Related Concepts

- [Membership Inference Game](membership-inference-game.md).
- [Blind Baseline](blind-baseline.md) — a low FPR is meaningless unless the null it is measured against
  is the right one.
- [Computational vs Statistical Memorization](computational-vs-statistical-memorization.md).

## Open Questions

- **Where does the sequence stop?** Per-example, then per-sample; the natural next term is
  worst-case over datasets as well, which is differential privacy. AZT24 §6 leaves the choice of a
  resting point open.
- **Canary optimality.** The sample-level metric is made tractable by auditing injected canaries that
  approximate the most vulnerable sample. Constructing provably strong canaries for a given defence is
  open, and AZT24 relies on heuristics.
- Whether a low-FPR criterion has a computational analogue — TPR at low FPR *per unit of attacker
  compute* — is not addressed anywhere in this literature.
