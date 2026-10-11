---
title: Compute Monitoring
type: concept
tags: [governance, certification, verifiable-computation, adversarial-ml]
---

## Definition

**Compute monitoring** is the enforcement of rules on machine-learning development by observing the
computational resources used to train models, rather than the models, the data, or the code. A monitoring
regime fixes a threshold `H` — a quantity of training compute above which a run is regulated — and
supplies a mechanism by which a Verifier can determine, after the fact and with stated probability,
whether a Prover exceeded it.

The canonical proposal ([Shavit 2023](../sources/catch-a-chinchilla-compute-monitoring.md)) has three
layers:

1. **Chip-level.** Attested on-chip firmware occasionally saves hashed snapshots of the neural-network
   weights resident in device memory, at a Poisson rate `f`.
2. **Datacentre-level.** The Prover retains, for each training run, enough information to prove which run
   produced any given snapshot — a **Proof-of-Training-Transcript**.
3. **Supply-chain-level.** Every specialised ML chip is accounted for, so that the Prover's stockpile `C`
   is known and cannot be secretly enlarged.

## Intuition

The analogy the literature reaches for is nuclear non-proliferation: reactor-grade and weapons-grade
uranium come from the same centrifuges, run longer and differently, so the treaty regime monitors the
centrifuges. Frontier training runs likewise leave a large physical footprint — thousands of accelerators
for weeks — while the difference between a benign and a dangerous run lives only in code and data. Monitor
the hardware and you get an observable proxy for the unobservable thing.

The proxy is compute. Which means the entire apparatus rests on a computational quantity, and the security
question is whether that quantity can be faked more cheaply than it can be earned. That question is
[Proof-of-Learning](proof-of-learning.md)'s Property 2, in a setting where the adversary is a state.

## Properties / Theorems

**What is quantified.** The threshold `H` is in **FLOPs**. Chip throughput `a` is FLOPs per chip per day;
`H/a` gives the derived chip-days figure ("H100-days"). Chip-hours appear as one candidate *basis for a
rule*, alongside data properties, hyperparameters, and benchmark performance. Hardware **possession**
(`C`) is what the supply-chain layer tracks, and is distinct from the training threshold.

**What is proved.** The sampling analysis. To detect at least one incriminating snapshot with probability
`p`, the Verifier must inspect

`s ≥ (log(1−p) / log(1 − (H/(aT_mC))(1 − e^{−fT_m}))) · (T_m/T)`

chips per monitoring period `T_m`, where guarantees are stated for runs of `≥ 2H` FLOPs. Two evasion
strategies are ruled out: splitting the run across more chips for less time each (**Theorem 1**), and
using fewer chips for longer (a `< 5%` improvement in evasion probability, since each chip is then sampled
`T/T_m` times as often).

**What is not proved.** Everything on the compute-hardness axis. The transcript layer is defined and
deferred:

> **Definition 1 (PoTT), the hardness clause.** A reporting/verification pair `(R, V)` is
> ***`J`-efficient and `F`-hard*** if `V` runs in at most `J` time and no spoof-generation algorithm
> `A : T → T` running in less than `F` time makes `V` accept with probability `> 1 − δ₂`.

This is the most security-shaped compute definition in the surveyed literature — an explicit time bound on
the adversary, and a separate one on the verifier — and **no construction is proved to satisfy it for any
`F`**. The paper says so and leaves it as future work. It also concedes that the adversary may rationally
spend *more* than the original training compute `H` to avoid detection, so `F` must exceed `H` by an
unspecified margin, and `F` is in "time" while `H` is in FLOPs. The substitute for hardness is procedural
deterrence: Verifiers keep secret verification heuristics, "much as the IAEA does not disclose all its
methods."

**PoTT versus PoL.** PoTT is argued to be strictly harder than [proof-of-learning](proof-of-learning.md):
the adversarial Prover *knows the true transcript* (they ran the training) and may outspend the original
run. PoL, whose adversary knows less and spends less, is already broken in practice.

## Where It Appears

- [What does it take to catch a Chinchilla?](../sources/catch-a-chinchilla-compute-monitoring.md) — the
  framework, the sampling bound, Theorem 1, and Definition 1.
- [Proof-of-Learning: Definitions and Practice](../sources/proof-of-learning.md) — the primitive PoTT
  varies, and the source of the `E[C_T] ≤ E[C_A]` shape.
- [Proof-of-Learning is Currently More Broken Than You Think](../sources/pol-more-broken.md) — why the
  primitive cannot currently be relied on.
- [PoL with Incentive Security](../sources/pol-incentive-security.md) — the blockchain setting, where the
  same verification problem is solved by making cheating unprofitable rather than infeasible.
- [PoLO](../sources/polo-proof-of-learning-ownership.md) — the marketplace setting, where compliance is
  enforced by monetisability rather than by law.

## Related Concepts

- [Proof-of-Learning (the notion)](proof-of-learning.md) — the missing primitive.
- [Verifiable Computation](verifiable-computation.md) and [ZK-ML verification](zk-ml-verification.md) —
  the cryptographic route to the same guarantee, currently too expensive for training-scale computations.
- [Fiber of the Training Map](fiber-of-the-training-map.md) — a spoofed transcript is a fiber element with
  a witnessing path.
- [Fine-Grained Complexity of Learning](fine-grained-complexity-of-learning.md) — where a lower bound on
  `F` would have to come from, if one existed.

## Open Questions

- **A construction that is `J`-efficient and `F`-hard for a stated `F`, under a stated assumption.**
  Nothing in the literature attempts this.
- Reconciling units: `H` is in FLOPs, `F` is in time, the PoL inequalities are in an undefined cost
  function `C`. The three quantities the regime must compare are not commensurable as written.
- Choosing `H` from desired policy outcomes, given that capability prediction from compute is unreliable —
  the paper's own caveat.
- Instantiating the transcript distance metrics that decide when a reported transcript counts as a spoof.
- Legacy untracked chips set a floor on the detectable run size; whether that floor falls faster than
  frontier compute rises is an empirical bet.
- Multi-party collusion is handled by widening the monitoring scope, not by analysis.
