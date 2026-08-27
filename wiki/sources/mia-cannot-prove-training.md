---
title: "Position: Membership Inference Attacks Cannot Prove that a Model Was Trained On Your Data"
type: source
date_ingested: 2026-08-20
authors: [Jie Zhang, Debeshee Das, Gautam Kamath, Florian Tramèr]
venue: "venue unconfirmed from PDF (arXiv:2409.19798v2, 7 Mar 2025; IEEE-style, 'Position:' paper)"
year: 2025
tags: [adversarial-ml, computational-indistinguishability, sample-complexity, cryptography]
claim_quantifier: conditional
antecedent: "The model developer's training set D and training procedure Train are unknown, AND the verifier cannot efficiently retrain the model. Asserted as a fact about production foundation models; not measured, not proved."
cls_target: train data
cls_family: membership
cls_phase: post hoc
cls_access: scores
cls_write: read only
cls_frame: compute
cls_party: auditor
cls_unit: time
cls_tightness: unstated
cls_baseline: absent
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: none
cls_assessed: implicit
cls_evidence: absent
cls_evidence_src: "classified by hand in the first batch, before the evidence requirement was added to the brief"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows."
cls_prov: hand
cls_date: 2026-08-22
---

> **Provenance.** Read in full from the primary PDF (Sections I–VI). All quoted passages verbatim.
> **This is the highest-value paper of the membership-inference critique batch** for this programme:
> it is the only one whose complaint is about the *definition*, and the only one whose obstruction has
> an explicit computational half.

## Summary

A **position paper**. The PDF title begins with the word "Position:" and the paper's central claim is
set in a display box as a position, not as a theorem. The object under attack is the **training data
proof**: a data creator wants to convince a third party (a judge) that some model was trained on their
data. Many works propose to instantiate this with a membership inference attack. The paper argues that
this cannot work.

The argument is a hypothesis-testing argument. Recast MI as a test of `H0`: the model was trained on
`D0 = D \ {x}`, versus `H1`: it was trained on `D1 = D`. To reject `H0` at a bounded false positive
rate the creator must know the distribution of the test statistic under `H0`, i.e.
`FPR = Pr_{f ~ Train(D0)}[T(f,x) ∈ S]` (Eq. 1). For a production model this probability cannot be
estimated, because the null hypothesis cannot be sampled.

**The computational half of the obstruction is stated explicitly and is load-bearing.** The paper gives
two independent reasons the null cannot be sampled, and the second survives even if the first is
removed: the abstract says the creator does not know the training set, *"nor can we (efficiently)
retrain a large foundation model"*, and Section II spells this out — even granted full knowledge of `D`
and of `Train`, *"sampling from the null hypothesis would still be prohibitively expensive as it would
require training new large models."* So this is a security claim declared unfalsifiable **relative to a
computationally bounded verifier**, not merely relative to an ignorant one. The paper does not name it
that way, does not put a resource bound on the verifier, and does not prove anything about the
bounded-verifier case; it names the cost and moves on.

The paper then works through three published families of FPR estimates and argues each is unsound
(Section III), and closes with three settings where a sound proof *is* available (Section IV): random
canaries, watermarked training data, and verbatim data extraction. The only theorem in the paper is
**Lemma 1**, and it is a positive result about the third route, not a negative result about the first.

## Claim Boundary

- **Quantified over:** membership inference attacks used as training data proofs against
  **large-scale production/foundation models with unknown training sets** — explicitly including
  hypothetical future attacks: *"we argue that it is actually impossible to evaluate how well any MI
  attack (including future, better ones) works in practice, if we cannot properly sample from the null
  hypothesis."* It is **not** quantified over MI attacks in general; Section V lists three settings
  where MI remains sound.
- **Antecedent:** the verifier does not know `D`, does not know `Train`, and cannot afford to retrain.
  The paper asserts this holds of production foundation models by observation (training sets are
  proprietary, training is expensive). It is not measured, and no threshold is stated for how much
  compute would suffice. **Under a verifier with the model developer's own budget, the argument's
  second leg vanishes and only the ignorance leg remains.**
- **Does not establish:** (a) that foundation models do not leak membership — the paper is about what
  can be *proved to a third party*, not about what is true; (b) that MI attacks are unsound in the lab
  — Section V affirms they are sound for evaluating defences and for auditing DP; (c) any impossibility
  *theorem*. No lower bound is proved. The impossibility is argued case-by-case against three published
  estimation strategies plus a general argument that one fixed model cannot estimate a probability over
  training randomness.
- **Abstract vs theorem:** **gap found.** The title and the boxed position assert that MI attacks
  "cannot prove" and that bounding the FPR is "impossible", but the paper proves no impossibility
  result. Its single lemma (Lemma 1) is a *positive* upper bound, `FPR ≤ k/|X|`, for the rank-based
  test under an independence assumption. The body is more careful than the title: it consistently says
  *"we argue"* and *"we claim"*. A reader who cites this paper for an impossibility theorem is citing
  something that is not in it.

## Key Contributions

- Names and formalizes the **training data proof** as a distinct object from membership inference, and
  makes the null hypothesis of the MI test explicit — a formalization the paper says is *"often left
  implicit in the literature."*
- The two-worlds construction for `H0`/`H1`: the developer collects `D` containing `x`, flips a fair
  coin `b`, and trains on `D0 = D \ {x}` or `D1 = D`. This gives the null a definite meaning that
  post-hoc non-member collection does not.
- **Lemma 1** — the rank test's FPR bound, `FPR ≤ k/|X|`, whenever `x` is drawn uniformly from `X`
  independently of the training of `f`.
- A three-way taxonomy of unsound FPR estimates: (1) non-members collected a posteriori; (2) "debiased"
  indistinguishable non-members; (3) held-out counterfactuals (dataset inference).
- Three sound paradigms, each an instance of restoring Lemma 1's independence assumption: random
  canaries, watermarking, verbatim extraction.
- The **causal-publication objection**, which is new here: publishing `x` changes the rest of the data
  repository, so `f` is not independent of `x` even when `x ∉ D`. Illustrated with the Harry Potter
  counterfactual — a model never trained on the books still prefers them to a name-swapped variant,
  because the web is full of secondary material about them.

## Key Definitions / Theorems

- **The position (verbatim):** *"Membership inference attacks cannot give reliable evidence of data
  usage in the training of production ML models, because it is impossible to bound the attack's false
  positive rate (FPR)."*
- **The computational obstruction (verbatim, abstract):** *"we do not know the exact contents of the
  training set, nor can we (efficiently) retrain a large foundation model."*
- **The computational obstruction, isolated (verbatim, §II):** *"sampling from the null hypothesis
  would still be prohibitively expensive as it would require training new large models."* This sentence
  is conditioned on the reader granting full knowledge of `D` and `Train`, which is what makes the
  compute cost an independent obstruction rather than a restatement of the ignorance one.
- **Null and alternative:** `H0`: `f` was trained on `D0` (without `x`); `H1`: `f` was trained on `D1`.
- **FPR (Eq. 1):** `FPR = Pr_{f ~ Train(D0)}[T(f,x) ∈ S | H0]`. The probability is over **training
  randomness**, not over a set of alternative samples — this is the paper's Issue #1 against a
  posteriori non-members, which replace the former with the latter.
- **Lemma 1:** if `x ~ Unif(X)` independently of the creation of `D` and of `f ~ Train(D)`, then the
  rank test `rank(f, x, X) ≤ k` has `FPR ≤ k/|X|`.
- **Extraction as a rank test (Eq. 10):** with `P` the prompt set and `U` the universe of plausible
  outputs, `FPR ⪅ |P|/|U|`. This is the paper's reconstruction of why the folklore extraction
  heuristics (long targets, high-entropy targets, short random prompts) are the right ones: they shrink
  `P` and grow `U`.

## Connections

- **Definitional sibling / opposite pole:** [MIA From First Principles (CCNSTT22)](mia-from-first-principles.md)
  supplies the hypothesis-testing framing and the LiRA likelihood ratio that this paper recasts. That
  paper improves how the test is *run*; this one asks whether the test's null can be *sampled*.
- **Empirical support:** [Blind Baselines Beat MIA (DZT24)](blind-baselines-beat-mia.md) — same lab,
  overlapping authors (Das, Zhang, Tramèr); supplies the distribution-shift evidence this paper cites
  for its Issue #2. Also [SoK: MIAs on LLMs are Rushing Nowhere (MSJ+25)](sok-mia-llms-rushing-nowhere.md)
  and [Do MIAs Work on LLMs? (DSM+24)](do-mias-work-on-llms.md).
- **Practice-side companion:** [Privacy Defense Evaluations are Misleading (AZT24)](privacy-defense-evaluations-misleading.md)
  — cited here as reference [2]; that paper fixes the in-lab evaluation, which this paper's Section V
  affirms is the setting where MI remains sound.
- [Sample Complexity of Membership Inference (Haghifam–Smith–Ullman)](haghifam-sample-complexity-mia.md)
  — the information-theoretic account of what an MI adversary needs. Complementary axis: that paper
  bounds the *attacker's* samples with an unbounded adversary; this one bounds the *verifier's* compute.
- [Computational vs Statistical Memorization](../concepts/computational-vs-statistical-memorization.md)
  — this paper adds a third position to that pair: information may be present *and* extractable, and
  still not **provable** to a third party under a compute bound.
- [Data Reconstruction: When You See It and When You Don't (Cohen et al.)](cohen-data-reconstruction.md)
  and [Dinur–Nissim PODS'03](dinur-nissim-revealing-information.md) — the reconstruction-side analogues
  of the same bounded-verifier question.
- [What Does it Mean for a Language Model to Preserve Privacy? (BLM+22)](language-model-preserve-privacy.md)
  — cited here as reference [4], and precisely for the point that the notion of "not being in the
  training set" blurs. That paper's argument is that secrets in natural language have no fixed
  boundaries; this paper's causal-publication objection is the same observation turned into an
  obstruction to a proof.
- [Unit of Protection](../concepts/unit-of-protection.md) — the target data `x` here is explicitly
  granularity-agnostic (*"an individual piece of text or an image, or an entire collection"*), which is
  what lets the paper treat dataset inference and sequence-level MI as one problem.
- [Fiber of the Training Map](../concepts/fiber-of-the-training-map.md) — the two-worlds construction
  is a two-point instance: `Train(D0)` and `Train(D1)` induce two distributions over weights, and the
  question is whether a bounded party can tell which fiber `f` fell in.
- Concepts: [Membership Inference Game](../concepts/membership-inference-game.md),
  [Blind Baseline](../concepts/blind-baseline.md),
  [Low-FPR Evaluation Regime](../concepts/low-fpr-evaluation-regime.md).

## Open Questions / Limitations

- **The compute bound is named, never quantified.** The paper says retraining is "prohibitively
  expensive" and stops. No budget, no exponent, no threshold at which the proof becomes sound. A
  fine-grained version — *how much* compute must a verifier have before a training data proof becomes
  admissible — is not attempted here and appears to be open.
- **No impossibility theorem.** The negative claim is argued against three named strategies plus a
  general "one fixed model cannot estimate a probability over training runs" argument. There is no
  proof that no future FPR estimator exists.
- **Lemma 1's assumptions are the whole content.** Everything sound in the paper is an instance of
  restoring uniform, independent sampling of `x`. Everything unsound is a failure of that. The paper's
  real contribution is arguably identifying that single hinge.
- The causal-publication objection is illustrated, not formalized. Simulating "the causal effect that
  `x'` would have on the rest of the repository" is posed as the correct-but-infeasible experiment; no
  approximation is proposed.
- Section IV-C's extraction bound assumes *"all strings in `U` are a priori approximately equally
  likely"*, and the paper concedes `|P|` and `|U|` cannot be characterized exactly in practice.

## Quotes / Notable Passages

- Abstract: *"sampling from this null hypothesis is impossible, as we do not know the exact contents of
  the training set, nor can we (efficiently) retrain a large foundation model."*
- §II: *"sampling from the null hypothesis would still be prohibitively expensive as it would require
  training new large models."*
- §II: *"we cannot sample from the null hypothesis, and thus cannot bound the attack's false positive
  rate."*
- §III-A: *"Since we only have access to one fixed model `f`, there is no way to estimate this
  probability."*
- §III-A: *"we argue that it is actually impossible to evaluate how well any MI attack (including
  future, better ones) works in practice, if we cannot properly sample from the null hypothesis."*
- §III-C, on the blurring of membership itself: *"the notion of 'not being in the training set' can
  become blurred."*
- §V, on where MI remains sound: *"researchers can directly sample from the null hypothesis (i.e.,
  models trained without the target data), enabling accurate estimation of the attack's false positive
  rate."*
