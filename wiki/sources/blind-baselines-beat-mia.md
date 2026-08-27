---
title: Blind Baselines Beat Membership Inference Attacks for Foundation Models
type: source
date_ingested: 2026-08-20
authors: [Debeshee Das, Jie Zhang, Florian Tramèr]
venue: "2nd DATA-FM workshop @ ICLR 2025, Singapore (arXiv:2406.16201v2)"
year: 2025
tags: [adversarial-ml, sample-complexity, learning-theory]
claim_quantifier: empirical
antecedent: "The eight named MI evaluation datasets were built post-hoc, by collecting members and non-members from different times or different sources. Measured, not assumed: the paper exhibits the shift in each of the eight."
cls_target: train data
cls_family: membership
cls_phase: post hoc
cls_access: none
cls_write: read only
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: stated
cls_second_party: none
cls_second_notion: none
cls_assessed: 
cls_evidence: absent
cls_evidence_src: "classified by hand in the first batch, before the evidence requirement was added to the brief"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows."
cls_prov: hand
cls_date: 2026-08-22
---

> **Provenance.** Read in full from the primary PDF (all sections plus Tables 1–3). Quoted passages
> verbatim.

## Summary

The paper is a **baseline attack**. It builds classifiers that never query the target model at all —
date-regex thresholds, bag-of-words classifiers, and greedy rare-n-gram selection — and shows that on
**8 published MI evaluation datasets for foundation models** these "blind" attacks beat the best
reported membership inference attack, which does have model access. The conclusion is that the
published numbers do not measure membership leakage: whatever signal the MI attacks were finding, a
model-free classifier finds more of it.

The mechanism is **distribution shift between the member and non-member sets**, arising because both
sets are assembled *a posteriori*. The paper names three sources: temporal shift (members and
non-members straddle a training cutoff date); biases in data replication (the two sets were collected
by slightly different pipelines); and distinguishable tails (sets matched on average still separate at
the outliers). The case studies are precise about which mechanism bites where — WikiMIA and the arXiv
sets are temporal (the top predictive features are literally years and citation years); Project
Gutenberg is a *formatting* artifact (`.htm` versus `.html` in the boilerplate preface); LAION-MI is a
*translation* artifact (non-member captions passed through a translation model, so non-English
characters and `\xa0` appear only among members).

The results are stated against the paper's own definition of the right null: *"Membership inference
evaluations are usually set up so that a baseline attack (which does not query the target model)
achieves 50% AUC (or equal TPR and FPR)."* That baseline is the entire argument. When it is measured
rather than assumed, it is not 50%, and the attacks that were quoted against it lose their meaning.
The paper puts this sharply: the attacks *"perform 'worse than chance'"* — not worse than 50%, but
worse than the correct null.

## Claim Boundary

- **Quantified over:** eight specific published MI evaluation datasets — WikiMIA, BookMIA, Temporal
  Wiki, Temporal arXiv, arXiv (all vs 1 month), arXiv (1 month vs 1 month), LAION-MI, Gutenberg — and
  the best reported attack numbers on each. Text and vision, LLMs and diffusion models. **Existential
  in form** (there exist blind attacks that win), used to support a **negative universal about those
  eight datasets** (none of them supports a claim about leakage).
- **Antecedent:** the member/non-member sets were assembled post-hoc rather than by a random train-test
  split. This is **measured, not assumed** — the paper exhibits the distinguishing features for each
  dataset and reports the blind attack's number alongside the published one.
- **Does not establish:** — and this is the load-bearing negative —
  - **not** that foundation models do not leak their training data. The paper says only that these
    evaluations cannot tell us whether they do. Its own words: existing evaluations *"tell us nothing
    about membership leakage of a foundation model's training data."* Nothing, in either direction.
  - **not** that the published MI attacks are useless in general. The claim is about their evaluation.
  - **not** that the shifts are unfixable. §5 proposes fixes (the Pile, DataComp, DataComp-LM) and
    §4.2.2 concedes *"it may be possible to preprocess this particular dataset to get rid of these
    formatting discrepancies."*
  - **not** a result about attacks with a properly randomized split. The Gutenberg text-only variant
    still gives 16.6% TPR at 1% FPR blind, so even the residual is contaminated, but no clean-split
    measurement is made here.
- **Abstract vs theorem:** none found. There is no theorem; the abstract's scope ("For 8 published MI
  evaluation datasets") matches the experiments exactly, and the strong sentence "tell us nothing about
  membership leakage" is defensible given the blind baselines shown. The one place a reader could
  overreach is the title, which reads as a general claim about foundation models rather than about
  eight datasets.

## Key Contributions

- The **blind (model-free) attack** as an evaluation instrument: an attack that has no model access is
  the correct null for an attack that does, and it can be run cheaply on any published MI benchmark.
- Blind attacks beating the state of the art on all 8 datasets. Headline gaps: WikiMIA 43.2% → 94.7%
  TPR at 5% FPR; Gutenberg 18.8% → 55.1% TPR at 1% FPR; LAION-MI 2.5% → 8.9% TPR at 1% FPR; BookMIA
  88.0 → 91.4 AUC.
- Three named mechanisms for the shift — temporal, replication bias, distinguishable tails — with the
  third being the reason that *average-case* debiasing does not suffice.
- The demonstration that debiasing is brittle: the arXiv one-month-vs-one-month set was built
  specifically to remove temporal shift, and a greedy word-selection attack still beats the published
  MIA (2.7% vs 2.5% TPR at 1% FPR).
- A concrete path forward: evaluate on models with a genuine random train-test split — the Pile
  (Pythia, GPT-NeoX-20B), DataComp, DataComp-LM — and apply the same filter to non-members that was
  applied to members.

## Key Definitions / Theorems

No theorems. The definitions that matter are methodological.

- **Blind attack:** a membership classifier that *"completely ignore[s] the target model."* Three
  instantiations: date detection by regex; a bag-of-words classifier trained on 80% and evaluated on
  20% with 10-fold cross-validation; greedy selection of the n-grams (`n ∈ [1,5]`) with the highest
  TPR-to-FPR ratio, predicting membership if any selected n-gram is present.
- **The correct null (verbatim):** *"Membership inference evaluations are usually set up so that a
  baseline attack (which does not query the target model) achieves 50% AUC (or equal TPR and FPR)."*
- **The goal of an MI attack, restated (verbatim):** *"the goal of an MI attack is to extract
  information from the model to beat a baseline inference that does not have access to the model."*
  This sentence is the paper's whole logic: the quantity being measured is a *difference* between an
  attack with model access and one without, and the published literature reported only the first term.

## Connections

- **Definitional escalation of this result:** [MIA Cannot Prove Training (ZDKT25)](mia-cannot-prove-training.md),
  same lab and two shared authors, cites this work as reference [13] and pushes the argument from
  "these eight datasets are broken" to "no post-hoc dataset can be fixed, because the null cannot be
  sampled."
- **Concurrent and independent:** [SoK: MIAs on LLMs are Rushing Nowhere (MSJ+25)](sok-mia-llms-rushing-nowhere.md)
  builds the same bag-of-words instrument in the same week and reaches the same conclusion on an
  overlapping set of datasets. Each cites the other as concurrent.
- **Prior identification of the temporal case:** [Do MIAs Work on LLMs? (DSM+24)](do-mias-work-on-llms.md)
  first flagged the WikiMIA temporal shift; this paper shows the problem is not confined to temporal
  shift or to one dataset.
- **Evaluation-metric ancestor:** [MIA From First Principles (CCNSTT22)](mia-from-first-principles.md)
  — the TPR-at-low-FPR regime this paper reports in.
- **The same complaint one level up:** [Privacy Defense Evaluations are Misleading (AZT24)](privacy-defense-evaluations-misleading.md)
  — missing baseline, but for defences (weak DP-SGD baselines) rather than for datasets.
- **The oldest form of this complaint in the wiki:** [On the Difficulty of Membership Inference (RL21)](difficulty-of-mia.md)
  — same structure (a trivial baseline is not reported, and beats the attack), three years earlier,
  on classifiers rather than foundation models.
- [Machine Unlearning](../concepts/machine-unlearning.md) — auditing unlearning is one of the four named
  applications of foundation-model MI here, so the conclusion that these evaluations "tell us nothing"
  propagates directly into unlearning verification.
- Concepts: [Blind Baseline](../concepts/blind-baseline.md),
  [Membership Inference Game](../concepts/membership-inference-game.md),
  [Low-FPR Evaluation Regime](../concepts/low-fpr-evaluation-regime.md).

## Open Questions / Limitations

- The blind attacks are deliberately not optimal: *"We do not aim for our blind attacks to be optimal."*
  So each reported number is a lower bound on the shift, and a dataset that survives these attacks is
  not thereby clean.
- Two of the eight datasets (arXiv one-month, Gutenberg) were not public; the authors reconstructed them
  from the described collection steps, so those two comparisons are against a replica.
- The proposed fix inherits a new problem: DataComp models are trained on *filtered* pools, so the
  non-members must be passed through the identical filter. The paper notes this and calls it easily
  remedied; whether filter equality is checkable in practice is not addressed.
- Nothing here measures leakage on a clean split. The paper redirects to the Pile and DataComp but does
  not run MI attacks there itself.

## Quotes / Notable Passages

- Abstract: *"blind attacks—that distinguish the member and non-member distributions without looking at
  any trained model—outperform state-of-the-art MI attacks."*
- Abstract: *"Existing evaluations thus tell us nothing about membership leakage of a foundation
  model's training data."*
- §2: *"the goal of an MI attack is to extract information from the model to beat a baseline inference
  that does not have access to the model."*
- §2: *"existing attacks do not just exploit distribution shifts, but they do so sub-optimally and are
  easily beaten by blind baselines. These attacks thus perform 'worse than chance'."*
- §1: *"removing biases in a post-hoc fashion is highly brittle."*
- §6: *"State-of-the-art MI attacks may thus be ineffective at extracting any actual membership
  information, and cannot be relied on for applications such as copyright detection or auditing
  unlearning methods."*
