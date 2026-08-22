---
title: Do Membership Inference Attacks Work on Large Language Models?
type: source
date_ingested: 2026-08-20
authors: [Michael Duan, Anshuman Suri, Niloofar Mireshghallah, Sewon Min, Weijia Shi, Luke Zettlemoyer, Yulia Tsvetkov, Yejin Choi, David Evans, Hannaneh Hajishirzi]
venue: "COLM 2024 (Conference on Language Modeling); arXiv:2402.07841v2"
year: 2024
tags: [adversarial-ml, learning-theory, sample-complexity]
claim_quantifier: empirical
antecedent: "Pretrained LLMs trained on web-scale corpora for approximately one epoch, with members and non-members drawn from the Pile's official train/test split. The near-random result is conditional on both properties; the paper varies each and shows attack performance rises when either is relaxed."
---

> **Provenance.** Read from the primary PDF: abstract, §1–§5, §6, Tables 1–4. Quoted passages verbatim.
> Appendices skimmed.

## Summary

The large-scale measurement that opened this line. Five MIAs — LOSS, reference-based, zlib-calibrated,
Neighborhood, and Min-k% Prob — are run against the Pythia and Pythia-dedup suites (160M to 12B
parameters) on seven Pile domains, with members and non-members taken from the Pile's own train and
test split. **No attack exceeds 0.6 AUC in any domain except GitHub.** The paper releases the setup as
MIMIR, which subsequent work uses as the reference clean benchmark.

The paper is **mixed** in kind, and the split matters:

**The empirical part** identifies two properties of LLM pretraining that suppress MI. First, *scale
plus one-epoch training*: using Pythia's intermediate checkpoints with members resampled per checkpoint
to remove recency bias, attack AUC rises quickly early in training and then declines as training
continues — larger data-to-parameter ratios generalize better. On the Datablations suite, increasing
the number of effective epochs raises attack performance. So the near-random result is a property of the
regime, not of the attacks. Second, *temporal shift explains prior positive results*: on a temporally
shifted Wikipedia benchmark, the same attacks perform much better, and performance grows with the size
of the temporal gap.

**The definitional part** is the "fuzzy boundary between members and non-members", and it has two
independent components:

1. **n-gram overlap.** Non-members from the Pile test set share long n-grams with the training set at a
   high rate: average 7-gram overlap of 32.5% (Wikipedia), 39.3% (ArXiv), 41.0% (PubMed Central), and
   76.9% (GitHub), 72.8% (DM Mathematics), 62.3% (FreeLaw). Resampling non-members to have ≤20% overlap
   raises MIA performance. So the binary member/non-member label does not track what the model has
   actually seen, and the paper interprets temporal shift itself as *"a change in n-gram overlap
   distribution"* — natural Wikipedia non-members overlap at 39.3%, temporally shifted ones at 13.9%.
2. **The membership definition is at odds with leakage.** §5 constructs *modified members* by replacing
   as few as one token, or by semantic-neighbor substitution, and shows existing MIAs classify them as
   non-members with high confidence — often more confidently than genuine non-members. Table 4 gives
   FPRs on modified members near 0% at edit distance 1 for the reference attack, and 0% everywhere for
   LOSS. Information-wise these are members; definitionally they are not. The paper notes that standard
   differential privacy does not cover this case, *"since records being tested for membership are not,
   in the literal sense, members."*

## Claim Boundary

- **Quantified over:** five specific MIAs against the Pythia and Pythia-dedup suites (70M–12B) and
  GPT-Neo, on seven Pile domains, plus the Datablations (C4) and SILO suites for the epoch ablation.
  Empirical.
- **Antecedent:** the target is a pretrained LLM trained on a very large corpus for approximately one
  epoch, and members/non-members come from a genuine random split. Both halves are **varied and
  measured**, not assumed: shrink the data (early checkpoints) or add epochs (Datablations) and attack
  performance rises. The near-random headline is therefore explicitly conditional on the pretraining
  regime.
- **Does not establish:**
  - **not** that LLMs do not memorize. The paper offers two candidate explanations and does not choose:
    either the data leaves little imprint, or the member/non-member distinction is too fuzzy to
    measure. Data extraction is discussed as a separate instrument revealing *"different types of
    leakage risks."*
  - **not** that finetuned models are safe. Scope is pretraining; the paper notes that prior positive
    MI results come from finetuning and masked-LM settings with more than 10 epochs.
  - **not** that stronger attacks cannot succeed. Stated: *"While MIA performance could improve via
    stronger attacks … the second factor requires rethinking the membership game itself."*
  - **not** that prior high-AUC results are definitively artifacts. The authors could not reproduce the
    prior experimental settings, and say so: *"it is inconclusive if their differing results are solely
    due to the temporal shift."* This is a more careful statement than the later literature's summary
    of it.
  - **not** that GitHub is an exception to the theory — it is called out as an outlier with the
    highest n-gram overlap (76.9%), and discussed separately in the appendix.
- **Abstract vs theorem:** none found. The abstract's four claims (near-random performance; the two
  causes; temporal shift explains prior success; sensitivity to small changes) each map to a section,
  and the abstract preserves the hedges — "can be attributed to", "may cause", "may be at odds with".
  There is no theorem in the paper.

## Key Contributions

- **MIMIR**, a unified benchmark and codebase implementing the five attacks over the Pythia/Pile setup
  with a genuine train/test split. This is the artifact the rest of the field now uses as the clean
  comparison point.
- The near-random headline result across model sizes and domains, with TPR at 1% FPR following the same
  trend.
- The two mechanistic explanations — large corpora with one-epoch training, and member/non-member
  overlap — each isolated by an ablation.
- **The n-gram overlap measurement**, and the reinterpretation of temporal shift as a shift in overlap
  distribution. This gives the distribution-shift complaint a quantitative handle that the bag-of-words
  diagnostics in [DZT24](blind-baselines-beat-mia.md) and [MSJ+25](sok-mia-llms-rushing-nowhere.md) do
  not.
- **The modified-member experiment**, which is the definitional core: MIAs are extremely sensitive to
  one-token edits, so exact-match membership is not the quantity a privacy auditor cares about.
- The observation that deduplicating training data *reduces* MI performance, and that MI performance
  rises with model size.
- The difficulty of choosing a reference model for reference-based attacks: most choices perform poorly,
  aggregation does not help, and the required "same-distribution but disjoint" assumption is hard to
  satisfy at web scale.

## Key Definitions / Theorems

No theorems. The definitions that matter:

- **MIA score:** `f(x; M)` thresholded to predict membership. The five instantiations are given
  explicitly: LOSS `= L(x;M)`; reference-based `= L(x;M) − L(x;M_ref)`; zlib `= L(x;M)/zlib(x)`;
  Neighborhood `= L(x;M) − (1/n)Σ L(x̃_i;M)`; Min-k% Prob over the k% lowest-likelihood tokens.
- **n-gram overlap.** For a non-member `x = x_1…x_m` and training set `D`,
  `(1/(m−n+1)) Σ_{i=1}^{m−n+1} 1{∃y ∈ D : x_i…x_{i+n−1} ∈ y}` — the fraction of `x`'s n-grams that
  appear in at least one member.
- **Modified member.** A member with `n` tokens randomly replaced (lexical) or with 5% of tokens
  replaced by semantically similar ones. Non-members by exact match, members by information content.
- **The proposed alternative:** *"a fully semantic MI game, where a neighbor member may be defined by
  its proximity to an exact member in a semantic embedding space."* Proposed, not built.

## Connections

- **Downstream, empirical:** [Blind Baselines Beat MIA (DZT24)](blind-baselines-beat-mia.md) and
  [SoK: Rushing Nowhere (MSJ+25)](sok-mia-llms-rushing-nowhere.md) both credit this paper with first
  flagging the WikiMIA temporal shift, and both use MIMIR. MSJ+25 runs nine attacks on MIMIR and
  confirms near-random performance. Note the escalation: this paper says the shift *explains* prior
  results; those papers show a model-free classifier *beats* the attacks outright.
- **Downstream, definitional:** [MIA Cannot Prove Training (ZDKT25)](mia-cannot-prove-training.md)
  cites the fuzzy-boundary finding for its claim that *"the notion of 'not being in the training set'
  can become blurred."* This paper supplies the measurement; that one supplies the consequence.
- **The attack this setting cannot afford:** [MIA From First Principles (CCNSTT22)](mia-from-first-principles.md)
  — LiRA is named here as intractable for LLMs because of the shadow-model cost.
- **The same tail finding, for classifiers:** [On the Difficulty of MIA (RL21)](difficulty-of-mia.md)
  — near-chance on the bulk, signal in the atypical subset.
- **The defence-side counterpart:** [Privacy Defense Evaluations are Misleading (AZT24)](privacy-defense-evaluations-misleading.md).
- [Computational vs Statistical Memorization](../concepts/computational-vs-statistical-memorization.md)
  — the fuzzy-boundary result is a third possibility for that pair: the *predicate* whose extractability
  is at issue may not be well defined. If a one-token edit flips the label but not the information, then
  exact membership is not the right predicate for either notion.
- [Sample Complexity of Membership Inference (Haghifam–Smith–Ullman)](haghifam-sample-complexity-mia.md)
  — the theory of how many samples an MI adversary needs; this paper's regime finding (one epoch over a
  huge corpus suppresses MI) is the empirical shadow of that question.
- [What Does it Mean for a Language Model to Preserve Privacy? (BLM+22)](language-model-preserve-privacy.md)
  — the argument this paper's §5 measures. That paper argues on conceptual grounds that private
  information in language has no fixed boundary; this one shows an MIA flips its answer on a one-token
  edit, which is the same claim with a number attached.
- [Unit of Protection](../concepts/unit-of-protection.md) — the fuzzy-boundary result is a
  unit-of-protection failure: the predicate "was this exact token sequence in `D`" is not the object
  anyone wants protected, and DP inherits the same defect.
- Concepts: [Membership Inference Game](../concepts/membership-inference-game.md),
  [Blind Baseline](../concepts/blind-baseline.md),
  [Low-FPR Evaluation Regime](../concepts/low-fpr-evaluation-regime.md).

## Open Questions / Limitations

- **The two explanations are not separated.** The conclusion offers both — little imprint, or a fuzzy
  distinction — and says *"both of these might be confounding factors while measuring leakage."* Which
  dominates is open.
- **The proposed replacement game is not built.** A semantic membership definition based on embedding
  proximity is sketched; the paper says the ideal distance function *"should combine the benefits of
  lexical distance and semantics"* and does not construct one.
- Prior work's settings could not be reproduced, so the attribution of prior high AUC to temporal shift
  is a strong hypothesis rather than a demonstration in this paper. (It is demonstrated, differently, by
  DZT24 and MSJ+25.)
- No sample-level or worst-case measurement. The whole paper reports population AUC and TPR at low FPR,
  which [AZT24](privacy-defense-evaluations-misleading.md) shows can hide a fully leaked individual.
- The overlap analysis is n-gram based; the paper says a semantic notion would be better and does not
  have one.

## Quotes / Notable Passages

- Abstract: *"MIAs barely outperform random guessing for most settings across varying LLM sizes and
  domains."*
- Abstract: *"an inherently fuzzy boundary between members and non-members."*
- §3.2.2: *"higher overlap between members and non-members increases MIA difficulty."*
- §5: *"the definition of membership in the standard MI game treats only records seen exactly during
  training as members … However, this may be at odds with what adversaries and privacy auditors care
  about."*
- §5: standard DP does not help here *"since records being tested for membership are not, in the literal
  sense, members."*
- §4: *"decision thresholds derived using temporally-shifted non-members end up testing for temporal
  shift rather than membership."*
- §6: *"the second factor requires rethinking the membership game itself."*
