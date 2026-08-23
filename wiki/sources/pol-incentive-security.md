---
title: Proof-of-Learning with Incentive Security
type: source
date_ingested: 2026-08-20
authors: [Zishuo Zhao, Zhixuan Fang, Xuechao Wang, Xi Chen, Hongxu Su, Haibo Xiao, Yuan Zhou]
venue: "venue unconfirmed from PDF (the file is arXiv:2404.09005v8, 4 May 2026; the ACM reference block gives year 2026 with the venue field left blank)"
year: 2026
tags: [adversarial-ml, certification, verifiable-computation, mechanism-design]
claim_quantifier: conditional
antecedent: "Not a complexity assumption. The theorems are conditional on: (a) rational, utility-maximising provers and verifiers; (b) a modelling assumption that a dishonestly trained epoch costs the prover ZERO computation; (c) a differentiable winning-probability function P(·) with hazard rate bounded by λ; (d) a per-stage catch probability κ = Θ(1); (e) reward R and staking/penalty γ above stated thresholds. No cryptographic or fine-grained hypothesis appears."
cls_target: training run
cls_family: forge
cls_phase: train time
cls_access: white box
cls_write: model
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: budget
cls_baseline: n/a
cls_second_party: time
cls_second_notion: none
cls_assessed: implicit
cls_evidence: "When dishonestly training an epoch, the prover may pay a significantly lower computational cost, and we assume it to be 0."
cls_evidence_src: §3.3
cls_reason: "The headline Theorem 6.1/6.2 (incentive-security, u(ρ)<u(1)) is game-theoretic and prices no party computationally on its own, but rule 7's test ('whether a number exists anywhere, not whether it is load-bearing') is decisive: the dishonest prover's cost is given an explicit number, zero, stated as a modelling assumption in §3.3 and used throughout the utility calculus. So party=attacker/unit=time/tightness=budget (a stipulated constant with no formula relating it to the honest cost) /assessed=implicit (the paper reports the cost but does not treat it as a varying parameter, matching rule 7's own GPU-hours example). second_party=time records the honest trainer's own explicit cost M=m·E (§3.3), a second party's own stated unit. family=forge over evade audit, following the line this corpus already draws (catch-a-chinchilla-compute-monitoring.md, auditable-unlearning-definitions.md): the cheating prover submits a structurally-correct, potentially-passing fabricated stage transcript (κ<1 catch probability), not a bare detection-probability result with no fabricated artifact. phase=train time, diverging from the post-hoc convention used for its siblings auditable-unlearning-definitions.md and forgeability-and-unlearning.md, because here the cheating decision is made live, epoch by epoch, during the mining/training process itself, not as a post-hoc rewrite of an already-trained model's log. write=model over corpus: the dataset D_tr is protocol-assigned via the seed φ=Hash(prev_block,prover_id) and cannot be chosen by the prover, so what is fabricated is the checkpoint/weight sequence for skipped epochs, not the corpus. access=white box is inferred, not an explicit stated threat-model line: the prover is itself the trainer and so has full internal visibility into its own weights/gradients by construction; flagged as inferred rather than quoted. The efficiency result (verifier overhead O(log E/E) or O(1/E), the paper's Property-1 quantity) is deliberately excluded from this row per rule 1: the abstract's headline and the title itself name the incentive-security claim, not the efficiency claim."
cls_prov: P
cls_date: 2026-08-22
---

> **Provenance.** Verified against the primary PDF on 2026-08-20 (`raw/Z+24_PoLIncentiveSecurity.pdf`,
> extracted with `pdftotext`).

## Summary

A blockchain Proof-of-Useful-Work paper that reaches the same conclusion as
[Fang et al.](pol-more-broken.md) and draws the opposite design lesson: since Byzantine-secure PoL
cannot currently be built, stop trying, and make cheating *unprofitable* instead of *impossible*. The
mechanism assigns each block a problem `A = (D_tr, E, φ)` with `φ = Hash(prev_block, prover_id)`, so the
prover must train with a designated random seed. Because the seed is protocol-specified, verification
becomes exact rather than tolerance-based, which the paper argues removes the attack surface that both
Zhang et al. and Fang et al. exploited. The verifier then checks a random subset of `α` of the `T = E/k`
stages.

**The answer to the question this corpus asks: there is no theorem relating adversary compute to honest
trainer compute, and the abstract does not claim one.** What the abstract claims is efficiency —
"we improve the relative computational overhead from `Θ(1)` to `O(log E / E)` without any staking
requirement, or `O(1/E)` with a staking requirement comparable to the block reward" — which is the
Property 1 quantity (verifier cost against trainer cost), not the Property 2 quantity. On the adversary
side the abstract offers "a provable incentive-security guarantee", and the definitions make explicit
that this is a utility comparison: **Definition 3.2 (Strict interim basic incentive-security)** requires
`u(ρ) < u(1)` for all `ρ ∈ [0,1)`, where `ρ` is the fraction of epochs trained honestly.

The adversary's cost is not bounded — it is **assumed**. §3.3: *"When dishonestly training an epoch, the
prover may pay a significantly lower computational cost, and we assume it to be 0."* Cheating is
therefore stipulated to be free, and security is recovered entirely from the expected penalty. That is
the cleanest instance in this corpus of the field's move: the compute inequality is not parameterised, it
is *replaced*.

## Claim Boundary

- **Quantified over:** **rational** provers and verifiers, i.e. agents maximising expected utility. The
  attack space is the four Jia et al. spoofing scenarios, restated and strengthened (the adversary is
  additionally given the random seed `φ` and the randomisation guideline `G`, and structurally correct
  spoofing no longer needs to reach the same model). Theorem 6.6 covers up to `n − m` colluding
  verifiers (instantiated at `n = 5`, `m = 3`). Nothing is quantified over computationally bounded
  adversaries; a prover who is irrational, or who is paid from outside the mechanism, is out of scope by
  construction.
- **Antecedent:** the five items in the frontmatter. The load-bearing ones are the zero-cost-cheating
  assumption and `κ = Θ(1)` (a cheating stage is caught with constant probability when verified). `κ` is
  computed combinatorially for the capture-the-flag protocol (`κ = 1` with an honest verifier; `κ = 1/2`
  at `n = 5, m = 3`), not assumed blindly — but it presupposes that a dishonest stage is *detectable when
  checked*, which is exactly the property the tolerance-based schemes failed to have and which the
  designated-seed design is meant to restore.
- **Does not establish:** (i) any lower bound on the cost of producing a passing proof — the model
  forbids the question by pricing dishonest epochs at zero; (ii) Byzantine security, explicitly
  disclaimed; (iii) that the designated-seed construction actually makes verification exact under
  hardware nondeterminism — the paper asserts reproducibility from pseudorandom sequences, which is the
  same property [the original PoL paper](proof-of-learning.md) §VIII flagged as a *threat* to its own
  entropy theorems; (iv) protection against provers subsidised outside the mechanism, or against attacks
  whose payoff is not the block reward.
- **Abstract vs theorem:** none found on the compute-comparison axis, and this is a positive finding. The
  abstract is scrupulous: it names the security notion ("incentive-security"), says what it bypasses
  ("the existing hardness"), and states the improved quantity as *relative computational overhead* —
  i.e. verifier overhead — not as adversary cost. The `O(log E / E)` and `O(1/E)` rates are delivered by
  Theorem 6.1 and Theorem 6.2. One phrase invites over-reading if skimmed: "securing ML training with
  provable incentive-security guarantees" — the adjective "provable" attaches to incentive-security, not
  to any hardness claim.

## The unnamed quantity

Two compute quantities appear, and the paper is unusually explicit about both.

**(1) The honest trainer's cost, `M`.** *"we can assume the computational cost to honestly train an epoch
is a deterministic constant `m`, and thus honestly training the task has a cost (aka. 'difficulty') of
`M = m·E > 0`, which can be dynamically adjusted by adjustment of `E`."* Then: *"if we honestly train a
`ρ` portion of all epochs, the computational cost is (lower bounded by) `ρM`."*

What it lacks: a unit (epochs, not FLOPs — and `m` is stipulated deterministic and identical across
provers, so hardware asymmetry is modelled away); any adversary class; and, decisively, **a lower bound
on the dishonest path**. The adversary's cost is not derived, it is set: *"When dishonestly training an
epoch, the prover may pay a significantly lower computational cost, and we assume it to be 0."* The
inequality `C_A < C_T` is thus true by assumption in this paper, and the theorem proves something else
entirely — that `u(ρ) < u(1)`, i.e. cheating loses money.

**(2) The relative computational overhead of verification**, `α/T`. This one *is* parameterised and *is*
the subject of theorems: `O(log T / T) = O(k log E / E)` at `γ = 0` (Theorem 6.1) and `O(k/E)` at
`γ = Θ(1)` (Theorem 6.2), against `Θ(1)` for full re-execution. Communication complexity likewise
improves from `Θ(E|W|)` to `O(E + |W| log E)` or `O(E + |W|)`. This is the Property 1 quantity of
[the original PoL paper](proof-of-learning.md), and it is the only compute quantity in this corpus that
receives an asymptotic rate inside a proved theorem. It says nothing about the adversary.

## Key Contributions

- **Incentive-security** as a replacement for Byzantine security in PoL: *"we do not need to prevent all
  attacks, but only need to prevent attacks from being 'worthy'."*
- **Definition 3.1 (Strict interim individual-rationality)**: `u(1) > 0`.
- **Definition 3.2 (Strict interim basic incentive-security)**: `∀ρ ∈ [0,1), u(ρ) < u(1)`. A mechanism
  satisfying both for parameter `γ` is called `γ`-IR-BIS.
- **Designated random seeds** `φ = Hash(prev_block, prover_id)`: makes verification exact rather than
  tolerance-based (closing the Zhang/Fang attack surface) and binds the model to the prover's identity,
  which the paper offers as a model-theft defence.
- **Verifier incentive-security** (Definition 5.4) and a **capture-the-flag protocol** to escape the
  Verifier's Dilemma — Theorem 5.2 formalises the Dilemma; Theorem 5.3 shows the basic mechanism fails
  verifier incentive-security; Theorem 6.6 shows the full mechanism achieves `ε`-VIS under collusion of
  at most `n − m` verifiers.
- The **Trilemma of Proof-of-Learning**: perfect security, efficiency, and controllable difficulty cannot
  be had together (stated as a boxed informal claim, not proved).

## Key Definitions / Theorems

- **Theorem 6.1 (Main Theorem)**: assuming `T ≥ 2`, `β = M/R`, a differentiable `P(·)` with hazard rate
  `P'(ρ)/P(ρ) ∈ [−λ, 0]`, and per-stage catch probability `κ = Θ(1)`, the mechanism is `0`-IR-BIS if
  `R > ∫₀¹P(ρ)dρ · M / (P(1) − (1−κ)^α)` and `α ≥ max{2(λ+β)/(βκ), 2ln(T/β)/κ}`. Consequence: `α = O(log T)`
  stages verified, so relative overhead `O(k log E / E)`.
- **Theorem 6.2**: with penalty `γ > 0`, `γ`-IR-BIS if `R > ∫₀¹P(ρ)dρ · M / P(1)` and
  `α > max{β/(γκ), λ/κ}`. Consequence: `α = O(1)`, relative overhead `O(k/E)`.
- **Theorem 5.2 (Verifier's Dilemma)** and **Theorem 5.3**; **Definition 6.3 ((N_p, N_v)-collusion)**,
  **Proposition 6.4**, **Lemma 6.5**, **Theorem 6.6** (`ε`-VIS under collusion).
- Utility model: `u(ρ) = P(ρ)(Q(ρ) − γ(1−Q(ρ)))R − ∫₀^ρ P(x)dx · M`, where `P` is the win probability and
  `Q(ρ)` the maximal pass probability over cheating strategies for that `ρ`.

Note that `Q(ρ)` is where an adversary-capability bound would have to live — it is "the maximal
probability among all such cheating strategies of passing the verification" — and it is constrained only
by monotonicity and `Q(1) = 1`. The mechanism's security is then transferred to `κ`, the probability a
cheating *stage* is caught **when it is verified**, which is a property of the verification predicate, not
of the adversary's compute budget.

## Connections

- Reads [Fang et al.](pol-more-broken.md) as licence to change the security notion, paraphrasing it as
  showing "a provably Byzantine-secure PoL is not possible to design until significant progress in
  further understanding in deep learning."
- Restates the four spoofing scenarios of [Proof-of-Learning: Definitions and
  Practice](proof-of-learning.md) with a strictly stronger adversary (given the seed).
- Appears as the row "PoL (hash)" in the comparison table of
  [PoLO](polo-proof-of-learning-ownership.md), which measures its verification overhead as approximately
  that of vanilla PoL.
- Concepts: [Proof-of-Learning (the notion)](../concepts/proof-of-learning.md),
  [Verifiable Computation](../concepts/verifiable-computation.md),
  [Compute Monitoring](../concepts/compute-monitoring.md).
- Same substitution of an economic guarantee for a hardness guarantee as
  [PoLO](polo-proof-of-learning-ownership.md), reached independently and stated more honestly: PoLO calls
  its economics "assumptions", this paper calls it the security notion.
- The framing "no more efficient method has been found to verify the integrity of training than training
  it again" is the Property 1 gap of [Proof-of-Learning](proof-of-learning.md) stated as a field-level
  fact, and connects to [Verifiable Computation](../concepts/verifiable-computation.md) and
  [ZK-ML verification](../concepts/zk-ml-verification.md).

## Open Questions / Limitations

- Everything the paper buys is bought with the rationality assumption. An adversary with an
  out-of-mechanism payoff — reputation, sabotage, a competitor's model — is unpriced.
- The zero-cost-cheating assumption is what makes the analysis tractable and also what makes the paper
  silent on the question this corpus is asking. Deriving a nonzero lower bound for `C_A`, and letting the
  utility calculation consume it, is the obvious open problem and is not raised.
- Exact verification requires bit-reproducible training from a seed. The paper asserts this from
  pseudorandom sequences; [the original PoL paper](proof-of-learning.md) §VIII treats the same property as
  an open empirical question ("there is currently no ground-truth for all sources of randomness arising
  in ML training").
- `κ = Θ(1)` presupposes that a cheating stage is detectable when checked. That is the assumption
  [Fang et al.](pol-more-broken.md) showed fails for tolerance-based verification; whether designated
  seeds restore it is argued, not measured against the infinitesimal-update or blindfold attacks.

## Quotes / Notable Passages

> "Until further understanding of deep learning, no more efficient method has been found to verify the
> integrity of training than training it again."

> "When dishonestly training an epoch, the prover may pay a significantly lower computational cost, and
> we assume it to be 0."
