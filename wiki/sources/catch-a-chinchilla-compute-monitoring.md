---
title: "What does it take to catch a Chinchilla? Verifying Rules on Large-Scale Neural Network Training via Compute Monitoring"
type: source
date_ingested: 2026-08-20
authors: [Yonadav Shavit]
venue: "arXiv:2303.11341"
venue_evidence: "https://arxiv.org/abs/2303.11341; no journal-ref field and no refereed venue found by web search"
year: 2023
tags: [adversarial-ml, certification, verifiable-computation, governance]
claim_quantifier: conditional
antecedent: "The one proved theorem assumes a Poisson snapshotting process at rate f, perfect parallelism, uniform chip throughput a FLOPs/day, and a Verifier who samples s chips after the run. The framework as a whole assumes: on-chip firmware attested by hardware features; supply-chain accounting for every ML chip; and the existence of a Proof-of-Training-Transcript scheme that does not yet exist. No cryptographic or complexity assumption underlies the compute-hardness half."
cls_target: training run
cls_family: evade audit
cls_phase: post hoc
cls_access: none
cls_write: none
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: n/a
cls_second_party: none
cls_assessed:
cls_evidence: absent
cls_evidence_src: "no bound in Theorem 1 (Appendix C.2), which is a Poisson-sampling probability with no party's resources restricted; Definition 1's F-hard/J-efficient PoTT clause does bound a spoof-generation algorithm by time F, but no (R,V) pair is proved F-hard for any F (§5.1), so the compute-hardness half has no construction to classify"
cls_reason: "Two claims of different shape, per rule 1. The abstract's contribution (2), tied to the proven Theorem 1 and Equation (1), is a detection-sampling probability with no adversary resource bound at all (the Prover's chip-splitting strategy is unconstrained and simply fails to help); this is the row classified here. Definition 1 (PoTT) is the paper's named compute-bounded-adversary security definition (F-hard spoof-generation algorithms, J-efficient verifier) and would classify as target=training run, family=forge, party=attacker, unit=time, tightness=budget, frame=compute if it carried a proof, but it is explicitly deferred as future work with no (R,V) construction, so it does not decide the row. phase=post hoc is an imperfect fit: detection is backward-looking ('executed a rules-violating training run in the past few months') but the on-chip snapshotting occurs during the run itself; no phase value fits cleanly. family=none flagged as a vocabulary gap: chip-splitting to reduce detection probability is neither 'evade' (test-time classifier evasion) nor 'forge' (no false transcript is fabricated in Theorem 1) as those terms are used elsewhere in the codebook."
cls_prov: S
cls_date: 2026-08-22
---

> **Provenance.** Verified against the primary PDF on 2026-08-20 (`raw/S23_CatchAChinchilla.pdf`, extracted
> with `pdftotext`).

## Summary

A governance apparatus resting on a compute quantity. The proposal has three layers: (1) on-chip firmware
that occasionally saves hashed snapshots of the neural-network weights resident in an ML chip's
high-bandwidth memory, with firmware use attested via hardware features; (2) a reporting requirement so
that, given a snapshot, the chip owner can prove which training run produced it; (3) supply-chain
monitoring so no actor can amass untracked chips. Inspectors then sample a fraction of a Prover's chips
periodically. The framing analogy is the NPT/IAEA regime for uranium enrichment.

Layer (2) is where the security content lives, and the paper is candid that it is missing. §5.1 defines
**Proof-of-Training-Transcript (PoTT)**, a variant of
[Proof-of-Learning](proof-of-learning.md) that the paper argues is *strictly harder*: the Prover knows
the true transcript `T` (they ran the training), and — unlike PoL — "we allow that an adversarial Prover
might be willing to spend more than the original training compute `H` in order to construct a spoof."
And then: *"We leave the problem of finding provably secure, efficient methods for PoTT as an important
avenue for future work."*

Two corrections to the received summary of this paper are worth stating precisely.

**First, the monitored quantity is FLOPs, not chip-hours.** §3 defines a large-scale training run as "any
training run using more than `H` FLOPs", and the detection analysis is entirely in FLOPs: `a` is FLOPs per
chip per day, the Prover needs at least `H/(aT)` chips, and the sampling bound Equation (1) is
`s ≥ (log(1−p) / log(1 − H/(aT_mC)(1 − e^{−fT_m}))) · (T_m/T)`. Chip-hours appear once, as one candidate
basis for a *rule* ("those based on the total chip-hours used to train a model"), alongside data
properties, hyperparameters, and benchmark performance. `H/a` — "H100-days" — appears as a derived column
in the table of past and projected runs. Hardware **possession** (`C`, the stockpile) is what supply-chain
monitoring tracks, and it is a separate quantity from the training threshold.

**Second, there is a theorem, and it is not about compute hardness.** Theorem 1 (Appendix C.2) states
that a Prover cannot lower the detection probability by splitting a rule-violating run across more chips
each running for less time. It is proved from the Poisson snapshot model plus an elementary lemma. It is a
statement about a *sampling process*, not about the cost of evading verification. On the compute-hardness
axis — whether a Prover can fabricate a transcript more cheaply than doing the training — the paper has a
definition, a claim that PoTT is harder than PoL, and an explicit deferral.

## Claim Boundary

- **Quantified over:** Theorem 1 quantifies over chip-splitting strategies within the Poisson snapshot
  model. Definition 1's `F`-hardness clause quantifies over spoof-generation algorithms `A : T → T`
  running in less than `F` time — a genuine compute-bounded adversary class, and the only one in this
  batch stated as a time bound on the adversary. But no `(R, V)` pair is exhibited or proved to be
  `F`-hard for any `F`. The detection guarantee is quantified over runs of `≥ 2H` FLOPs, not `H`: the
  paper explains that catching a snapshot at `H + ε` is "vanishingly unlikely for small `ε`", so
  guarantees are given for runs "substantially exceeding `H`", with the note that the threshold can be
  halved to recover `H`.
- **Antecedent:** the frontmatter list. Notably, the collusion case is handled by a *policy* remedy
  (treat all Provers as one) rather than an analytic one, and the framework's reach is bounded below by
  pre-existing untracked chips: "these unmonitored compute sources present an implicit lower bound on the
  minimum training run size that can be verifiably detected."
- **Does not establish:** (i) that transcript spoofing is expensive — no `F`-hard construction exists;
  (ii) that PoTT is achievable at all, efficiently or otherwise; (iii) that PoL is secure — the paper
  reports the opposite, citing the spoofing attacks; (iv) detection of small-scale training, fine-tuning,
  or consumer-GPU training, all scoped out in §1.2; (v) that compute thresholds map to capabilities —
  "Current 'scaling law' extrapolations are not yet able to reliably predict ML models' downstream
  capabilities", so choosing `H` is left as future policy work.
- **Abstract vs theorem:** one phrase over-reaches slightly. Contribution (2) says inspectors "can
  provably determine whether the chip-owner executed a rules-violating training run in the past few
  months, with high probability." What is proved is the *sampling* half — that inspecting `s` chips
  catches an incriminating snapshot with probability `p`, and that chip-splitting does not help the
  Prover. The step from "the Verifier holds a snapshot" to "the Verifier can prove a violation" runs
  through PoTT, which the paper leaves unsolved. §5.1 states this plainly, so the gap is disclosed
  rather than concealed — but the contribution bullet, read alone, reads as an end-to-end guarantee.

## The unnamed quantity

- **The threshold**: *"We define a large-scale training run as any training run using more than `H`
  FLOPs."* `H` is an exogenous policy parameter. It has a unit (FLOPs), no definition of how it is to be
  measured from a snapshot, and — by the paper's own admission — no principled way to be chosen, since
  capability prediction from compute is unreliable.
- **The adversary's budget**: Definition 1's *"there does not exist any spoof-generation algorithm
  `A ∈ A : T → T` such that `Pr[V(A(T), W_t) = accept] > 1 − δ₂` where `A` runs in less than `F` time"*,
  with the companion clause "`V` runs in at most `J` time" — the pair `(R, V)` is then called
  *`J`-efficient and `F`-hard*.

This is the single most security-shaped compute definition in the batch: two named parameters, one for
the verifier and one for the adversary, exactly the two sides of
[Proof-of-Learning](proof-of-learning.md)'s Properties 1 and 2, and unlike PoL it bounds the adversary by
**time** rather than by a bare cost inequality. What it lacks:

- **A construction.** No `(R, V)` is proved `J`-efficient and `F`-hard for any values. The definition is
  stated and immediately deferred.
- **An assumption.** No hardness hypothesis is offered from which `F`-hardness could follow. The paper's
  substitute is procedural: Verifiers can keep secret verification heuristics, "much as the IAEA does not
  disclose all its methods", and even purely heuristic PoTTs "may dissuade Provers from taking the risk."
  That is deterrence, not hardness.
- **A relation between `F` and `H`.** The definition does not tie the adversary's budget to the training
  compute. The motivating remark does the opposite — it *concedes* the adversary may spend more than `H`,
  so the target is `F > H` by some unspecified margin: "we must hope to push the cost to construct a spoof
  to be as high as possible, so as to make evasion impractical."
- **A unit for `F`.** "Time", left abstract, while `H` is in FLOPs. The two quantities the framework needs
  to compare are not in the same units.
- **A lower bound.** None anywhere on this axis.

The distance metrics in Definition 1 are also worth noting as a boundary: a spoof must differ from the
true transcript by `d₁(D, D') ≥ δ₃` in data edit distance and/or `d₂(M, M') ≥ δ₄` in hyperparameter
distance, and neither `d₂` nor `δ₃, δ₄` is instantiated.

## Key Contributions

- The three-layer monitoring architecture: on-chip weight-snapshot logging, transcript reporting, and
  supply-chain accounting.
- Equation (1): the number of chips `s` an inspector must sample per monitoring period `T_m` to detect a
  rule-violating run of `≥ 2H` FLOPs with probability `p`, given stockpile `C`, throughput `a`, and
  snapshot rate `f`. Worked numbers for GPT-3-, Chinchilla-, and PaLM-scale runs at `C = 10³, 10⁵, 10⁷`.
- **Theorem 1**: chip-splitting does not reduce detection probability.
- Appendix C.1's companion finding: using *fewer* chips for longer also does not meaningfully help
  (`< 5%` increase in evasion probability), because each chip is then sampled `T/T_m` times as often.
- **Definition 1 (PoTT)** and the `J`-efficient / `F`-hard parameterisation.
- The argument that PoTT is strictly harder than PoL: the adversary knows the true transcript and may
  outspend the original run.
- A taxonomy of monitorable rule types: total training compute, data properties, hyperparameter
  properties, benchmark performance, and combinations ("if a model was trained on RL-for-code-generation
  for greater than `X` FLOPs, then it should not be trained beyond `Y` performance on `Z` benchmarks").
- Explicit limitations section: dependence on the continued centrality of large-scale training and of
  specialised datacentre accelerators; hundreds of thousands of already-sold chips lacking the required
  hardware security features.

## Key Definitions / Theorems

- **Definition 1 (PoTT protocol)**: `(R, V)`; completeness `Pr[V(T, W_t) = accept] > 1 − δ₁`; spoof
  defined by transcript distance `δ₃, δ₄`; the pair is *`J`-efficient and `F`-hard* per the clause quoted
  above.
- **Theorem 1**: with total compute `H`, stockpile `C`, throughput `a`, snapshot rate `f`, and
  `c(t) = H/(at)` chips used for time `t`, the detection probability
  `p_d(t) = 1 − (1 − (H/(aCt))(1 − e^{−ft}))^s` satisfies `p_d(t) > p_d(T)` for `t < T`. Proof via the
  supporting lemma `f(g) = g(1 − b^{1/g}) − (1 − b) ≥ 0` for `g ≥ 1`, `1 > b > 0`.
- Equation (1), the sampling bound (derivation in Appendix B).
- Summary of the PoL verification procedure it builds on: check that the initialisation looks random, then
  re-run selected `k`-step segments and confirm `‖W'_{i+k} − W_{i+k}‖₂ < ε`.

## Connections

- Builds directly on [Proof-of-Learning: Definitions and Practice](proof-of-learning.md), and reports its
  status accurately: "subsequent papers have demonstrated spoofing attacks that evade the original
  verification approach", "Thus far, the literature on PoL has been heuristic-based". The two citations
  are Zhang et al. and [Fang et al.](pol-more-broken.md).
- PoTT is the compute-parameterised version of the desideratum that
  [Proof-of-Learning](proof-of-learning.md) left as a bare inequality — compare `J` and `F` against
  `E[C_V] ≤ E[C_T]` and `E[C_T] ≤ E[C_A]`, and against `F+23`'s `c`-cheapness.
- Concepts: [Compute Monitoring](../concepts/compute-monitoring.md),
  [Proof-of-Learning (the notion)](../concepts/proof-of-learning.md),
  [Verifiable Computation](../concepts/verifiable-computation.md).
- The private-transcript version of the same problem is the ZK-proof-of-training line; see
  [zk-verifiable-ai-pipelines](zk-verifiable-ai-pipelines.md) and
  [ZK-ML verification](../concepts/zk-ml-verification.md).
- The gap between a stated compute bound and a construction meeting it is the same gap that
  [PoLO](polo-proof-of-learning-ownership.md) fills with measurements and
  [PoL with Incentive Security](pol-incentive-security.md) fills with economics.
- Entity: [Yonadav Shavit](../entities/yonadav-shavit.md).

## Open Questions / Limitations

- **The stated open problem:** find provably secure, efficient PoTT methods. The paper's own assessment:
  "Given that existing PoL schemes are still heuristic-based and not yet provably secure, there may be a
  long way to go until we have PoTT methods that are both efficient and hard to spoof."
- Choosing `H` from desired policy outcomes, given unreliable capability prediction.
- Instantiating the transcript distance metrics `d₁, d₂` and thresholds `δ₃, δ₄`.
- Untracked legacy chips set an implicit floor on the detectable run size.
- Multi-Prover collusion is addressed by policy scope (monitor everyone as one Prover), not analysis.
- The framework is void if frontier capability stops requiring large specialised-accelerator runs.

## Quotes / Notable Passages

> "We leave the problem of finding provably secure, efficient methods for PoTT as an important avenue for
> future work"

> "we must hope to push the cost to construct a spoof to be as high as possible, so as to make evasion
> impractical."
