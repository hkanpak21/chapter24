---
title: Blind Baseline
type: concept
tags: [adversarial-ml, learning-theory, sample-complexity]
---

## Definition

A **blind** (equivalently *model-free*, *model-less*) baseline is an attack on a membership inference
benchmark that never queries the target model. It sees only the candidate records and their claimed
member/non-member labels, and predicts membership from the records alone.

Its purpose is to supply the null hypothesis against which a membership inference attack's score must be
read. An MI attack's claim is that it extracts information *from the model*; the blind baseline measures
how much of the reported score is available without the model.

Named instances:

- **ZeroR** — always predict "member" ([RL21](../sources/difficulty-of-mia.md)).
- **Naive attack** — predict member iff the target model classifies the record correctly (RL21, from
  prior work). Not strictly blind: it uses the model's correctness but no membership signal.
- **Date detection** — regex out every date in the text, predict member iff all are before a threshold
  ([DZT24](../sources/blind-baselines-beat-mia.md)).
- **Bag of words** — train a classifier on 1-gram counts, held-out split (DZT24;
  [MSJ+25](../sources/sok-mia-llms-rushing-nowhere.md), independently and concurrently).
- **Greedy rare-n-gram selection** — rank all `n`-grams (`n ∈ [1,5]`) by TPR-to-FPR ratio, select
  greedily, predict member if any selected n-gram is present. Tuned for the low-FPR regime (DZT24).

## Intuition

Every attack score is implicitly a difference: what the attack achieves, minus what is achievable
without the thing the attack is supposed to exploit. The literature reported the first term and assumed
the second. The assumption is stated plainly in DZT24: *"Membership inference evaluations are usually set
up so that a baseline attack (which does not query the target model) achieves 50% AUC."*

Measured, it is not 50%. Across eight foundation-model MI benchmarks, blind attacks **beat** the best
published MI attack — WikiMIA 43.2% → 94.7% TPR at 5% FPR, Gutenberg 18.8% → 55.1% TPR at 1% FPR,
LAION-MI 2.5% → 8.9% TPR at 1% FPR. MSJ+25's bag-of-words classifier reaches 0.988–0.994 AUC on WikiMIA
and 0.997 on Gutenberg. So the published attacks were not only reading a shift instead of leakage; they
were reading it *badly*. DZT24's phrase: they *"perform 'worse than chance'"* — worse than the correct
null, not worse than 50%.

**The blind baseline is a diagnostic, and its predictive features are the diagnosis.** Reported features
name the artifact:

| benchmark | what the blind attack keyed on |
|---|---|
| WikiMIA | years in the text (`2014`, `2022`, `2023`) |
| ArXiv | years inside `\cite` keys |
| Project Gutenberg | boilerplate preface (`.htm` versus `.html`, `gutenberg`, `ebook`) |
| BookMIA | contraction spelling (`didn`, `wasn`) |
| LAION-MI | non-English characters and `\xa0` left by the translation model used to build the non-members |

Two structural facts follow.

**The baseline is one-directional.** A high blind AUC proves a shift. A blind AUC near chance proves
nothing: MSJ+25 says so explicitly, and DZT24 declines to claim its attacks are optimal. So passing a
blind baseline certifies nothing about a benchmark.

**Post-hoc debiasing is shallow.** Match publication years and the formatting artifact remains; strip the
formatting and period vocabulary remains (Gutenberg AUC falls only 0.997 → 0.889). Narrow the temporal
window to one month either side of the cutoff and the blind attack still edges the MIA (2.7% vs 2.5% TPR
at 1% FPR). DZT24: *"removing biases in a post-hoc fashion is highly brittle."*

## Properties / Theorems

No theorems; the concept is an evaluation instrument. Two structural claims recur:

- **A blind AUC above chance makes the benchmark uninformative in both directions.** It does not show
  the model is private, only that the measurement cannot distinguish leakage from shift.
- **The escalation to a definitional claim.** ZDKT25 argues the blind-baseline problem is not a dataset
  defect to be fixed but a symptom: the correct null is a distribution over *models trained without
  `x`*, and replacing it by a distribution over *other records* is the error. Under that reading, no
  amount of debiasing helps, because the two quantities are not approximations of each other. The
  exception is the rank test, where drawing `x` uniformly and independently from a candidate set makes
  the record-level null legitimate and yields `FPR ≤ k/|X|`.

## Where It Appears

- [Blind Baselines Beat MIA (DZT24)](../sources/blind-baselines-beat-mia.md) — coins "blind", eight
  datasets.
- [SoK: MIAs on LLMs are Rushing Nowhere (MSJ+25)](../sources/sok-mia-llms-rushing-nowhere.md) —
  independent, concurrent, six datasets, "model-less baseline".
- [On the Difficulty of MIA (RL21)](../sources/difficulty-of-mia.md) — the earliest instance in this
  wiki: ZeroR, plus the demonstration that positive-class precision tracks the evaluation set's balance
  rather than the attack.
- [Do MIAs Work on LLMs? (DSM+24)](../sources/do-mias-work-on-llms.md) — the quantitative mechanism
  (n-gram overlap) underneath what the blind classifiers detect.
- [Privacy Defense Evaluations are Misleading (AZT24)](../sources/privacy-defense-evaluations-misleading.md)
  — the same missing-baseline complaint moved up a level: defences were compared against weak DP-SGD
  instances, so the DP baseline is the blind baseline of the defence literature.
- [MIA Cannot Prove Training (ZDKT25)](../sources/mia-cannot-prove-training.md) — the definitional
  reading above.

## Related Concepts

- [Membership Inference Game](membership-inference-game.md) — the game whose null this supplies.
- [Low-FPR Evaluation Regime](low-fpr-evaluation-regime.md) — blind attacks are reported in the same
  regime, and tuned for it (greedy n-gram selection exists because bag-of-words is not optimal at low
  FPR).
- [Computational vs Statistical Memorization](computational-vs-statistical-memorization.md).

## Open Questions

- **How strong should the baseline be?** Every published blind attack is deliberately simple and
  therefore a lower bound on the shift. There is no notion of an *optimal* blind attack, and hence no
  certificate that a benchmark is clean.
- **A compute-indexed version.** The natural formalization — the best distinguisher of members from
  non-members computable in `t` steps *without* model access, versus the best with it — is not stated
  anywhere in this literature. The gap between those two quantities is what an MI attack actually
  measures, and it is currently reported as a single number with the subtrahend assumed.
- Whether the blind-baseline complaint and the unsamplable-null complaint are the same complaint. DZT24
  treats it as a fixable dataset defect; ZDKT25 treats it as a category error. Both positions are
  recorded here; they have not been reconciled.
