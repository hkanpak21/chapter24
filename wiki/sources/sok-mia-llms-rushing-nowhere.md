---
title: "SoK: Membership Inference Attacks on LLMs are Rushing Nowhere (and How to Fix It)"
type: source
date_ingested: 2026-08-20
authors: [Matthieu Meeus, Igor Shilov, Shubham Jain, Manuel Faysse, Marek Rei, Yves-Alexandre de Montjoye]
venue: "IEEE Conference on Secure and Trustworthy Machine Learning (SaTML) 2025 (acceptance stated in the PDF; arXiv:2406.17975v3)"
year: 2025
tags: [adversarial-ml, learning-theory, sample-complexity]
claim_quantifier: empirical
antecedent: "The six datasets measured were constructed post-hoc, i.e. members and non-members were collected after model release from different time windows or sources rather than by randomized split. Measured per dataset, not assumed."
cls_target: train data
cls_family: membership
cls_phase: post hoc
cls_access: none
cls_write: none
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: stated
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: "absent"
cls_evidence_src: "no adversary resource in the sequence-/document-level MIA formalization (§II, §V-B), which parameterizes only a scoring function and a threshold; the fixed-record-vs-fixed-model cost argument is qualitative ('unaffordable for LLMs'), never a numeric bound"
cls_reason: "The paper's load-bearing device is the model-less bag-of-words baseline, which needs no interaction with the target model at all, so access=none and write=none rather than the white-box/scores access the surveyed MIA methods themselves use (Rule 1, main claim). baseline=stated because the clean MIMIR re-evaluation is judged against chance: 'the original attacks ... do not perform significantly better than random, and neither do any of the 5 recently proposed attacks' (§ nine-attack re-run). No party's compute, queries or samples are bounded anywhere, so party/unit/tightness/frame are all the null values."
cls_prov: P
cls_date: 2026-08-22
---

> **Provenance.** Read from the primary PDF: abstract, §I–§V, §VI-A/C, §VII–§VIII, Tables I–III.
> Quoted passages verbatim. The four forward paths in §VI-B/C/D skimmed.

## Summary

A systematization of the last two years of membership inference against LLMs, with a measurement
attached. The review half (Table I) classifies the literature along four axes — pretraining versus
finetuning target, unit of interest (sequence / document / dataset), whether a new attack method is
proposed, and motivation (privacy and security / copyright / dataset contamination) — and records for
each work whether its evaluation dataset was collected post-hoc. At least **10 new MIA methods were
proposed in 2024 alone**, and most were evaluated on post-hoc data.

The measurement half builds a **bag-of-words classifier** (a random forest over 1-gram counts, trained
on 80% and tested on 20% of each dataset, five runs) as a *model-less baseline*, and runs it on the six
accessible post-hoc datasets. Every one shows a distribution shift, several severe: WikiMIA 0.988–0.994
AUC, Gutenberg (full) 0.997, BookMIA 0.937, ArXiv 0.690, ArXivMIA 0.596, StackMIA 0.612. The predictive
features are diagnostic and are reported: years for WikiMIA and ArXiv, Project Gutenberg boilerplate
(`gutenberg`, `ebook`, `http`) for Gutenberg, contraction spelling (`didn`, `wasn`) for BookMIA. When
the Gutenberg boilerplate is stripped by removing the first and last 10% of each book, the AUC falls
only from 0.997 to 0.889, and the surviving features are period vocabulary — including a racial slur —
rather than formatting.

**What this paper faults is the experimental construction of the game, not the game.** Its complaint is
that the randomized privacy game — which for classifiers is instantiated by actually training models
with the target in or out — cannot be afforded for LLMs, and that the substitute (post-hoc member and
non-member collection) does not approximate it. The formalism in §II is standard and is left intact; it
is the instantiation that fails. The paper is explicit that the failure is an IID failure: *"a
fundamental assumption in membership inference, i.e. the members and non-members are IID, does not
hold."*

The reconstructive half proposes four routes back to randomization — randomized test splits from
open-source LLMs, injection of randomized unique sequences, randomized finetuning, and post-hoc control
methods including a regression-discontinuity design — and then runs nine attacks on the properly
randomized MIMIR setup, where they perform near chance.

## Claim Boundary

- **Quantified over:** six accessible post-hoc MI evaluation datasets (WikiMIA at 32 and 128 tokens,
  BookMIA, Gutenberg full and mid, ArXiv, ArXivMIA, StackMIA), used across more than ten papers; plus a
  literature review of MIA work on LLMs from 2019 to September 2024. Empirical.
- **Antecedent:** the datasets were built post-hoc from time-separated or source-separated collections.
  Measured per dataset, and the paper is careful that the measurement is one-directional: a high BoW AUC
  proves a shift, but *"the AUC achieved by the bag of words classifier only represents a lower bound;
  if its performance is close to a random guess, this does not necessarily imply the absence of any
  distribution shift."*
- **Does not establish:**
  - **not** that LLMs do not memorize. The claim is that these evaluations cannot attribute attack
    performance to memorization: *"it is impossible to exclusively attribute the MIA performance to LLM
    memorization."*
  - **not** that the ten new attack methods are wrong. The claim is that they cannot be *compared* —
    *"whose performance has been impossible to fairly compare and benchmark."*
  - **not** that the four proposed fixes are sound. Each is given with limitations; the overlap problem
    (below) is left open for all of them.
  - **not** that MIMIR is clean. The paper flags that MIMIR's own post-hoc deduplication could introduce
    a new bias, and excludes the GitHub subset from its randomized evaluation.
- **Abstract vs theorem:** **minor gap.** The abstract writes that the shifts *"invalidate the claims of
  LLMs memorizing strongly in real-world scenarios and, potentially, also the methodological
  contributions"* — "invalidate" is stronger than the body, which consistently says the results cannot
  be *attributed* to memorization, i.e. they are uninformative rather than false. The distinction
  matters for this wiki: an uninterpretable measurement is not a refuted claim.

## Key Contributions

- The literature map (Table I): target model, unit of interest, whether a new method is proposed,
  motivation, and dataset, for the seminal work plus everything from 2023–2024. The finding that
  motivation migrated from privacy to copyright and contamination, and the target from finetuning to
  pretraining, is itself a useful record.
- The **bag-of-words model-less baseline**, and its instantiation on six datasets with the top
  predictive words reported. Reporting the features is what turns a number into a diagnosis.
- The demonstration that debiasing is shallow: matched publication years (Gutenberg) leave formatting,
  and removing formatting still leaves vocabulary.
- Two structural obstacles named as distinct from the shift problem:
  - **Overlap.** Text from the web duplicates itself, so a random held-out split still contains
    near-members. This *"challenges the binary notion of membership"* — a definitional problem that
    randomization does not fix.
  - **Unit of interest.** Sequence-, document- and dataset-level MI are different games with different
    scoring functions, and the literature moves between them. Formal definitions for the sequence- and
    document-level variants are given in §II and §V-B.
- Four forward paths with stated trade-offs, plus a recommended benchmark table (Table VI).
- The negative result on the clean setup: nine attacks (four original, five recent) on MIMIR with
  Pythia-dedup-6.9B, none significantly better than random; the same for document-level MIAs on a
  randomized ArXiv split from the Pile.

## Key Definitions / Theorems

No theorems. The formalization worth keeping:

- **Sequence-level MIA:** a scoring function `f_seq(M, s_t)` over a target sequence, thresholded at
  `τ_seq`, with ground truth `y_seq(M, s_t) = 1` iff `∃ d_i ∈ D` with `s_t ∈ d_i`. Evaluated by AUC or
  TPR at low FPR.
- **Document-level MIA:** `f_doc(M, d_t)` thresholded at `τ_doc`, with `y_doc = 1` iff `d_i ∈ D`.
  Dataset inference is treated as a generalization of the document level.
- **Post-hoc data collection:** the paper's name for the practice — *"an attacker aims to infer
  membership for a released LLM, without access to the randomized training data distribution."*
- **Fixed-record versus fixed-model privacy games** (taken from Ye et al.): in the fixed-record game
  many models are trained with the target in or out; in the fixed-model game one model is trained and
  targets are sampled IID. **The cost argument is that the first is unaffordable for LLMs and the second
  requires an IID non-member set that post-hoc collection does not provide.**

## Connections

- **Concurrent and independent:** [Blind Baselines Beat MIA (DZT24)](blind-baselines-beat-mia.md).
  §VII compares the two directly: DZT24 calls the same instrument a "blind" baseline, covers three
  datasets, and proposes randomized test splits; this paper covers six, adds the deduplication-bias and
  unit-of-interest analyses, and evaluates the forward paths. Two labs building the same null in the
  same week is itself evidence about what was missing.
- **First identification of the temporal case:** [Do MIAs Work on LLMs? (DSM+24)](do-mias-work-on-llms.md)
  — cited here as [27], and the source of the MIMIR dataset used for the clean re-evaluation.
- **Definitional escalation:** [MIA Cannot Prove Training (ZDKT25)](mia-cannot-prove-training.md).
  This paper says post-hoc datasets are shifted and proposes fixes; ZDKT25 argues the fixes cannot
  produce a *third-party proof* because the null still cannot be sampled. Note the disagreement in
  emphasis: ZDKT25 §III-B specifically argues that the "debiased non-members" route — which the group
  that wrote this SoK pioneered — has low power and narrow scope.
- **Metric ancestor:** [MIA From First Principles (CCNSTT22)](mia-from-first-principles.md) — cited for
  the low-FPR reporting convention, and its shadow-model requirement is the cost this paper says LLMs
  cannot pay.
- **The same missing-baseline structure, for classifiers:** [On the Difficulty of MIA (RL21)](difficulty-of-mia.md).
- **Defence-side analogue:** [Privacy Defense Evaluations are Misleading (AZT24)](privacy-defense-evaluations-misleading.md).
- [Unit of Protection](../concepts/unit-of-protection.md) — §V-B's "unit of interest" axis (sequence /
  document / dataset) is this concept applied to membership inference. The paper's point that the three
  are different games with different scoring functions, and that the literature slides between them, is
  a unit-of-protection confusion.
- [Machine Unlearning](../concepts/machine-unlearning.md) — §IV-C flags that flawed MIA setups have been
  used downstream to certify unlearning and privacy-preserving technologies, so the defect propagates
  into a second subfield's verification story.
- Concepts: [Blind Baseline](../concepts/blind-baseline.md),
  [Membership Inference Game](../concepts/membership-inference-game.md),
  [Low-FPR Evaluation Regime](../concepts/low-fpr-evaluation-regime.md).

## Open Questions / Limitations

- **The overlap problem is definitional and is left open.** If members and non-members share long
  n-grams by nature, "membership" is not a clean binary and no amount of randomization repairs it. The
  paper calls the practical significance *"a nuanced, perhaps philosophical, question"* and asks
  whether MIAs should be evaluated on data with overlap at all — noting that for copyright, accounting
  for overlap may be the *correct* behaviour, not an artifact.
- The BoW baseline is a lower bound on shift, so passing it certifies nothing.
- Two of the datasets reviewed (Dolma-Book, Wikipedia Cutoff) were not released and could not be
  measured.
- The forward paths each carry an unsolved cost: randomized splits exist for few models, sequence
  injection changes the training data, finetuning does not tell you about pretraining, and the post-hoc
  controls are new and untested.

## Quotes / Notable Passages

- Abstract: *"Sets of members and non-members, used to evaluate the MIA, are constructed using informed
  guesses after the release of a model."*
- §IV-B: *"a fundamental assumption in membership inference, i.e. the members and non-members are IID,
  does not hold and … the post-hoc collection of members and non-members fails to provide a proper
  privacy game to evaluate MIAs."*
- §IV-B: *"We are hence unable to exclusively attribute the high MIA AUC reported by studies relying on
  post-hoc data collection … to memorization of the LLM."*
- §IV-B: *"the AUC achieved by the bag of words classifier only represents a lower bound."*
- §IV-C: *"The use of flawed MIA evaluation setups in these contexts is highly concerning."*
- §VIII: *"In the last year, research has proposed at least 10 different MIAs, whose performance has
  been impossible to fairly compare and benchmark."*
