---
title: Evaluations of Machine Learning Privacy Defenses are Misleading
type: source
date_ingested: 2026-08-20
authors: [Michael Aerni, Jie Zhang, Florian Tramèr]
venue: "ACM CCS 2024, Salt Lake City (arXiv:2404.17399v2)"
year: 2024
tags: [adversarial-ml, differential-privacy, learning-theory, certification]
claim_quantifier: empirical
antecedent: "Five specific empirical defenses (HAMP, RelaxLoss, SELENA, DFKD, and a folklore defense) on CIFAR-10 at >=88% test accuracy, attacked with LiRA adapted per-defense and audited on injected canaries. The DP-SGD comparison baseline is tuned for utility, not for a meaningful epsilon."
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
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: absent
cls_evidence_src: "no compute, query, sample, or privacy-budget bound stated on the attacker, any defense, or an auditor anywhere in §1-§6; the paper's headline TPR/FPR figures (abstract, Fig. 1, §4.1) measure attack success against defenses, not a resource any party spends, matching the difficulty-of-mia precedent for this same genre of MI-evaluation-methodology paper"
cls_reason: "This is a measurement/methodology critique paper (three pitfalls in evaluating MI defenses), not a paper asserting a formal resource bound on any party, so frame/party/unit/tightness follow Rule 2 (none/none/none/unstated), matching the same-genre precedent difficulty-of-mia, which was classified identically despite also reporting attack success numbers as its central finding. The paper explicitly disclaims that DP-SGD's epsilon is a meaningful bound in its own comparison ('vacuous provable guarantees'), so per Rule 8 that examined-but-not-asserted DP framing is not recorded as frame=capability. baseline=stated: the DP-SGD high-utility baseline and the name-and-shame defense's elementary population-metric bound (TPR <= FPR + 1/|D|) are both explicit stated comparators. access=scores per LiRA's confidence/loss-based construction, adapted per-defense."
cls_prov: S
cls_date: 2026-08-22
---

> **Provenance.** Read from the primary PDF: abstract, §1–§4, §5.1, §5.5, §6. Quoted passages verbatim.
> Per-defense adaptive attack details (§5.2–§5.4) skimmed.

## Summary

A **critique of evaluation practice**, aimed one level above the previous entries: not at how MI
attacks are evaluated, but at how *defences* are evaluated using MI attacks. Three pitfalls are named,
each with a fix.

**Pitfall I — aggregating over a dataset.** Even the TPR-at-low-FPR metric from
[LiRA](mia-from-first-principles.md) is a population quantity: it counts what *fraction* of members can
be identified while keeping false guesses over the whole population low. The paper's demonstration is a
constructed defence, `NS_x̂` ("name and shame"), which outputs 1 iff a fixed target `x̂` is in the
training set and 0 otherwise. It completely destroys `x̂`'s membership privacy and protects everyone
else, yet under population-level evaluation `TPR ≤ FPR + 1/|D|`, so it can be made *arbitrarily private
by enlarging the dataset*. The metric can be diluted at will. The same effect is then shown to be real
rather than pathological on CIFAR-10: with LiRA and 20,000 training runs, the most vulnerable single
sample has a **sample-level TPR of 99.9% at 0.1% FPR**, while the population-level number on the same
models is **4%**.

**Pitfall II — weak or non-adaptive attacks.** Defence evaluations use attacks that are no longer state
of the art, or fail to adapt them to the defence's peculiarities. The paper draws the explicit parallel
to adversarial-example defences broken by adaptive attacks.

**Pitfall III — weak DP baselines.** Empirical defences are compared to DP-SGD instances that reach far
lower accuracy, which makes the comparison vacuous. Across the five defences studied, *"none considers a
DP-SGD baseline with more than 80% CIFAR-10 test accuracy."*

The fix is a three-part protocol: measure at the most vulnerable sample (approximated efficiently by
injecting canaries and auditing only those); adapt the attack to each defence; and compare against a
DP-SGD baseline tuned for *utility* even at the cost of a meaningless `ε`. Under it, all five defences
leak an order of magnitude more than their original evaluations reported, the ranking among them
changes completely, and none beats a DP-SGD baseline with `ε > 10^8`.

## Claim Boundary

- **Quantified over:** five defences (HAMP, RelaxLoss, SELENA, DFKD, and one folklore defense) on
  CIFAR-10 in the strict setting where all training data must be protected, at ≥88% test accuracy,
  attacked with per-defense-adapted LiRA on injected canaries. Empirical, on this set.
- **Antecedent:** (a) no public data is available for pretraining — the paper explicitly restricts to
  *"the strict privacy setting, where all training data has to be protected"*, excluding PATE and
  public-pretraining approaches; (b) the DP-SGD comparison baseline is tuned to high utility, which
  means its provable guarantee is vacuous (`ε > 10^8` for the high-utility one, `ε > 3,000` for the
  medium). The comparison is between two *empirical* defences, one of which happens to be DP-SGD.
- **Does not establish:**
  - **not** that DP-SGD is the best MI defence generally. Stated outright: *"we do not claim that
    DP-SGD is the best membership inference defense in all settings."*
  - **not** that heuristic DP-SGD provides any provable guarantee. Its `ε` is meaningless by
    construction; the finding is that it is empirically strong anyway, which the paper flags as a
    **theory gap**, not a proof.
  - **not** that the adaptive attacks or the canaries designed here are optimal — *"We do not claim
    that the attacks or canaries we design for each defense are optimal"* — so every leakage number is
    a lower bound.
  - **not** a claim that the most-vulnerable-sample metric is the uniquely correct one. §6 poses the
    choice of privacy semantics as an open design question between the average case and the DP
    worst case.
- **Abstract vs theorem:** none found. The `NS_x̂` bound `TPR ≤ FPR + 1/|D|` is elementary and stated
  as such. The abstract's "underestimate privacy leakage by an order of magnitude" matches the measured
  4.3×–53.7× range in Figure 1.

## Key Contributions

- **The dilution argument.** A population-level metric — including TPR at low FPR — can be driven
  arbitrarily low by adding samples that the defence happens to protect, without changing what happens
  to the most vulnerable sample. `NS_x̂` makes this exact.
- The measurement of **sample-level** TPR at 0.1% FPR on CIFAR-10, obtained by repeating the MI
  experiment 20,000 times with resampled halves of the training set. 99.9% for the most vulnerable
  sample against 4% for the population.
- A tractable substitute for the most-vulnerable-sample measurement: inject canaries that mimic the
  most vulnerable data and audit only those. This imports the technique from DP auditing into empirical
  defence evaluation.
- Adaptive attacks against five defences, and the finding that the original evaluations both understate
  leakage and mis-rank the defences.
- The high-utility DP-SGD baseline: with modern DP-SGD improvements and hyperparameters tuned for
  utility, DP-SGD with a vacuous `ε` beats every heuristic defence studied — *"all heuristic defenses
  with similar test accuracy yield a TPR@0.1% FPR that is at least 5.5× worse."*
- Two research directions named in §6: a theory of "natural" (non-worst-case) privacy leakage that
  would explain why DP-SGD's empirical behaviour outruns its worst-case analysis, and a method for
  constructing strong canaries for a given defence.

## Key Definitions / Theorems

- **Population-level TPR/FPR:** `TPR(T) = Pr_{x ~ D_in, f ~ Train(D_in)}[A(f,x) > T]`,
  `FPR(T) = Pr_{x ~ D_out, f ~ Train(D_in)}[A(f,x) > T]`, with `T` chosen so `FPR ≤ 0.1%`. Randomness
  is over the choice of sample *and* the training run.
- **Sample-level TPR/FPR:** `TPR_x(T_x) = Pr_{D_in, f ~ Train(D_in)}[A(f,x) > T_x | x ∈ D_in]` and the
  matching `FPR_x` conditioned on `x ∉ D_in`, with a **per-sample** threshold `T_x`. Randomness is over
  the dataset draw and training run only; the sample is fixed. **This is the difference that carries
  the paper**, and it is the same move LiRA made from a global to a per-example threshold, applied one
  level up to the metric.
- **Name-and-shame defence:** `NS_x̂(D_in) = 1` if `x̂ ∈ D_in`, else `0`; satisfies
  `TPR ≤ FPR + 1/|D|` under population-level evaluation.
- **DP as a bound on MI:** a DP guarantee bounds the TPR-to-FPR ratio of any MI attack distinguishing
  `D` from `D ∪ {x}`, with the probabilities over the mechanism's randomness only — *"not with respect
  to a random choice of the dataset `D` or target sample `x`."* This sentence is the paper's axis:
  average-case MI evaluation and worst-case DP differ in what is randomized, and the paper positions
  its canary protocol between them.

## Connections

- **Direct parent:** [MIA From First Principles (CCNSTT22)](mia-from-first-principles.md). This paper
  adopts LiRA as the attack and TPR-at-low-FPR as the metric, then shows the metric is still an
  aggregate. The relation is not refutation but the next term in the same series: global threshold →
  per-example threshold (LiRA) → per-sample *metric* (here).
- **Cited by** [ZDKT25](mia-cannot-prove-training.md) as reference [2], and used there to mark the
  in-lab setting where MI evaluation remains sound. The two papers partition the field cleanly: this
  one repairs the lab, that one says the lab cannot be left.
- **Same lab, adjacent target:** [Blind Baselines Beat MIA (DZT24)](blind-baselines-beat-mia.md) —
  missing baseline for *datasets*; this paper, missing baseline for *defences*.
- **Ancestor of the missing-baseline complaint:** [On the Difficulty of MIA (RL21)](difficulty-of-mia.md).
- [DP-SGD (Abadi et al.)](deep-learning-differential-privacy.md) — the mechanism used here as an
  *empirical* defence with a vacuous guarantee. That inversion (a provable mechanism deployed for its
  unproved empirical strength) is the paper's most quotable finding.
- [Xiao–Suh–Devadas, Formal Privacy Proof of Data Encoding](xiao-formal-privacy-proof-data-encoding.md)
  — the theory-side counterpart to the claim that heuristic transformations do not buy real privacy.
- [Computational vs Statistical Memorization](../concepts/computational-vs-statistical-memorization.md)
  — the §6 call for a theory of "natural" privacy leakage under which DP-SGD's tight worst-case analysis
  becomes loose is a request for exactly this kind of separation.
- [Adaptive Attacks](../concepts/adaptive-attacks.md) — Pitfall II *is* the adaptive-attack requirement,
  imported into privacy from adversarial robustness. The paper draws the parallel itself: the situation
  is *"reminiscent of well-known pitfalls for non-adaptive evaluations of machine learning robustness."*
  Two of the five defences studied are confidence masking, the privacy analogue of gradient masking.
- [Unit of Protection](../concepts/unit-of-protection.md) — the population-versus-sample distinction is
  a unit-of-protection choice: the population metric protects a *dataset*, the sample-level metric
  protects a *record*, and DP protects a worst-case record.
- Concepts: [Low-FPR Evaluation Regime](../concepts/low-fpr-evaluation-regime.md),
  [Membership Inference Game](../concepts/membership-inference-game.md),
  [Blind Baseline](../concepts/blind-baseline.md).

## Open Questions / Limitations

- **The canary construction is heuristic.** The protocol's efficiency depends on canaries whose leakage
  approximates the true most-vulnerable sample, and §6 admits *"we rely primarily on heuristics to
  select"* them. An adversary-optimal canary construction is posed as open.
- **The privacy semantics are left unresolved.** §6 asks whether we care about the *proportion* of
  samples inferable or about whether *any* sample is inferable, and notes the choice is usually implicit
  in the MI game's sampling. The paper picks one; it does not argue it is uniquely right.
- **A possible impossibility is gestured at, not proved.** The paper conjectures that at very high
  utility on CIFAR-10 no defence can protect the most vulnerable samples without public data, citing
  Feldman's result that heavy-tailed distributions require label memorization for optimal
  generalization, and reports that even DP-SGD fails at ~92% accuracy. This is evidence, not a theorem.
- Single dataset (CIFAR-10), single modality, five defences.

## Quotes / Notable Passages

- Abstract: *"prior evaluations fail to characterize the privacy leakage of the most vulnerable
  samples, use weak attacks, and avoid comparisons with practical differential privacy baselines."*
- Abstract: *"none of the empirical defenses we study are competitive with a properly tuned, high-utility
  DP-SGD baseline (with vacuous provable guarantees)."*
- §1: *"privacy is not an average-case metric!"* — quoting forward from CCNSTT22 and then showing the
  fix was itself an average.
- §4.1: *"existing metrics can be arbitrarily 'diluted' by adding new members for which a defense
  preserves privacy, even if the same defense fully leaks the membership of a fixed number of samples."*
- §4.1: *"the TPR at 0.1% FPR of the most vulnerable sample is 99.9%—orders of magnitude higher than
  the population-level metric (4%) suggests."*
- §2.3, on DP: probabilities are over the mechanism *"not with respect to a random choice of the dataset
  `D` or target sample `x`."*
- §6: *"before evaluating a defense—or an attack—we thus need to clearly define the privacy semantics
  that the evaluation targets."*
