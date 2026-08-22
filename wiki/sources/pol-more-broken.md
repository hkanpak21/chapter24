---
title: Proof-of-Learning is Currently More Broken Than You Think
type: source
date_ingested: 2026-08-20
authors: [Congyu Fang, Hengrui Jia, Anvith Thudi, Mohammad Yaghini, Christopher A. Choquette-Choo, Natalie Dullerud, Varun Chandrasekaran, Nicolas Papernot]
venue: "venue unconfirmed from PDF (the file is arXiv:2208.03567v2, 17 Apr 2023, and states no venue; the bibliography of `DJY+25_PoLO.pdf` lists it as EuroS&P 2023)"
year: 2023
tags: [adversarial-ml, certification, verifiable-computation, complexity theory]
claim_quantifier: empirical
antecedent: "The attacks are unconditional constructions against stated verification parameterizations (a fixed noise tolerance `δ`, and the `top-Q` selection rule with `Q` known to the adversary). The formal fragments (Lemmas 1–6) assume a metric whose Lebesgue-measure behaviour is specified, and Lemmas 5–6 assume finite variance of the cost distribution plus Markov's inequality only. Nothing rests on SETH, a cryptographic assumption, or a hardness conjecture."
---

> **Provenance.** Verified against the primary PDF on 2026-08-20 (`raw/F+23_PoLMoreBroken.pdf`,
> extracted with `pdftotext`).

## Summary

Same group as [the original PoL paper](proof-of-learning.md), attacking their own construction. Two
things happen here, and they must not be conflated. First, **constructive attack work**: two new
spoofing strategies that are reproducible across PoL verification configurations and cost a small
fraction of what the earlier Zhang et al. attack cost. Second, a **partial formalisation** of the
assumptions the original paper left implicit — reproducibility, representativeness, cheapness — plus
necessary conditions any cheap spoofer must satisfy. What does **not** happen is an impossibility
theorem. The paper proves no lower bound and refutes nothing in the complexity-theoretic sense; the
conclusion it reaches is epistemic: *"formally proving the robustness of a proof verification
mechanism for PoL is not currently possible."*

The two attacks both target the verifier's arithmetic rather than the optimisation landscape. The
**infinitesimal update attack** interpolates linearly between a chosen `Ŵ_0` and the victim's `W_T` so
that every logged step is far smaller than the tolerance `δ`, then sets the learning rate `η → 0` so
the verifier's own recomputation is also smaller than `δ`; the difference is therefore under `δ` and
the proof verifies. Cost: one floating-point operation per parameter per update, "upper-bounded by the
computation needed for 1 FP", against Zhang et al.'s `(43·n_iter + 1)·k` forward passes *per update*.
The **blindfold top-Q attack** exploits the fact that `top-Q` selects by update magnitude: the
adversary makes exactly `Q` genuine large updates per epoch and linearly interpolates the rest, so the
verifier's selection rule lands only on the valid ones. Expected per-step cost `(3·k·Q)/s + 1` forward
passes, where `s` is steps per epoch. Both are **structurally correct spoofs** — invalid proofs that
pass — and the first is evaluated against the strongest verifier, one that checks every update.

The formal contribution is the naming of the assumptions. **Assumption 1 (Reproducibility)** posits a
bound `δ` on honest reproduction error. **Assumption 2 (Representativeness)** posits that a small
verified subset implies validity of the whole. **Assumption 3 (Cheapness)** is the original Property 2,
rewritten over an event space `A_{D,W_T}` of proofs: `E[C(F(D, W_T))] ≥ E_{P∼A_{D,W_T}}[C(P)]` for every
algorithm `F : (D, W_T) → A_{D,W_T}`. And **Definition 6 (c-Cheap Proof Algorithm)** finally indexes the
ratio: `F` is `c`-cheap if `E[C(F(D, W_T))] < cE` for `c ∈ [0,1)`, where `E` is the honest expected cost.
That is the closest anything in this corpus comes to parameterising the attacker-vs-defender ratio — and
it is a *multiplicative constant attached to an assumption*, not an exponent attached to a theorem. The
paper then proves only **necessary conditions** on `c`-cheap algorithms (a stability property and a
query-complexity lower bound for one particular sampling strategy) and states plainly that whether such
algorithms exist "remains an open problem."

## Claim Boundary

- **Quantified over:** the attacks are quantified over *the stated verification mechanism*, not over all
  verifiers. The infinitesimal update attack requires a **static** tolerance `δ`; the blindfold attack
  requires the adversary to know `Q` and the selection rule (both granted by the paper's threat model:
  "`A` has knowledge of the verification parameters `δ` and `Q`, and the selection mechanism"). Change
  the parameterisation to a noise model that captures gradient *direction* as well as magnitude — which
  the paper sketches via Lemma 3 — and neither attack is claimed to survive. The formal lemmas quantify
  over `(d, τ)`-verification strategies for metrics with specified Lebesgue behaviour (Lemma 1,
  Corollary 1), and over `c`-cheap algorithms as a class (Lemmas 5, 6).
- **Antecedent:** none of the standard kind. No SETH, no OWF, no average-case conjecture. Lemmas 5 and 6
  need only finite variance of the cost distributions and Markov's inequality. The three named
  assumptions (reproducibility, representativeness, cheapness) are the paper's *object of study*, not
  its hypotheses.
- **Does not establish:** (i) that PoL is *impossible* — the paper says the opposite is unknown, and
  proposes commitments and timestamping as routes to a working scheme; (ii) that cheap spoofing
  algorithms exist in general — the two attacks produce *invalid* proofs that pass a *specific*
  verifier, which is structurally correct spoofing, not stochastic spoofing; (iii) any lower bound on
  adversary compute; (iv) that Assumption 3 is false. On the contrary, §7 reports empirical difficulty in
  constructing stochastic spoofs and concludes "we believe that such algorithms do not currently exist
  for DNN training", while conceding "any empirical study is non-comprehensive."
- **Abstract vs theorem:** none found. The abstract is careful — it claims to "demonstrate" that
  verification "is not robust to adversaries", to "introduce the first spoofing strategies that can be
  reproduced across different configurations", and, on the theory side, only that "realizing these
  assumptions reduces to open problems in learning theory." Each of those is delivered. The one place
  a reader could over-read is the phrase "on the theoretical side, we show how realizing these
  assumptions reduces to open problems" — this is an informal reduction of a research programme, not a
  complexity-theoretic reduction between problems.

## The unnamed quantity

The paper writes the quantity twice, and it is the only paper in this corpus that indexes it:

- **Definition 5 (Cost of a Proof)** — a bare function: *"We define cost as some function
  `C : A_{D,W_T} → R⁺`, which represents the 'cost' associated with computing each proof."* No unit is
  fixed. FLOPs are used informally in the attack analyses (forward passes, "1 back propagation costs
  approximately 2 FPs"), but `C` itself is never tied to them.
- **Assumption 3 (Cheapness)**: *"Given a cost function `C`, for any algorithm `F : (D, W_T) → A_{D,W_T}`,
  `E[C(F(D, W_T))] ≥ E_{P∼A_{D,W_T}}[C(P)]`"*.
- **Definition 6 (c-Cheap Proof Algorithm)**: `F` is `c`-cheap if `E[C(F(D, W_T))] < cE`, `c ∈ [0,1)`.

What it lacks:

- **A unit.** `C` is an arbitrary positive function; the theory is invariant to whether it counts FLOPs,
  wall-clock seconds, or dollars, which means it cannot express hardware asymmetry.
- **An exponent.** `c` is a multiplicative constant in `[0,1)`, so the family is indexed by a *ratio*,
  not by a growth rate like `honest^{1+δ}`. There is no security parameter and no asymptotic regime;
  `c`-cheapness at `c = 0.99` and at `c = 0.01` are formally the same kind of statement.
- **An adversary class.** `F` ranges over *all* maps `(D, W_T) → A_{D,W_T}`. No runtime bound, no circuit
  size, no algorithm family. Contrast Lemma 6, which does bound something — the query complexity of one
  specific strategy `F_honest` that samples from the honest measure `µ` until it lands on a cheap proof.
  That is a lower bound on *a named algorithm*, not on the class.
- **An assumption to rest on.** Cheapness is *itself* the assumption; the paper's whole point is that
  nobody knows whether it is true.
- **A lower bound.** Lemma 5 (stability of `c`-cheap algorithms) and Lemma 6 (queries) give **necessary
  conditions**, and the paper says so: "stability and query complexity are only two properties that
  stochastic spoofing adversaries must satisfy, i.e., they are necessary but may not be sufficient."
  A negative answer to whether an algorithm can satisfy them "would also prove that `c`-cheap algorithms
  do not exist" — which is exactly the theorem that does not exist.

## Key Contributions

- **Infinitesimal update attack.** Near-zero cost, guaranteed to produce sub-`δ` updates, effective
  against a verifier that checks every step. Empirically produces `‖ε_repr‖` consistently below Zhang
  et al.'s Attack 2 at a fraction of the cost.
- **Blindfold top-Q attack.** Defeats the representativeness heuristic by controlling which updates get
  selected. Evaluated at `Q = 5`: "the adversary is always able to mislead the verifier into selecting
  these updates."
- Assumptions 1–3 named and formalised; `(d, τ)`-verification strategies (Definition 3) and
  representative subsets (Definition 4) defined.
- Lemma 1 / Corollary 1: existence of a minimum viable threshold; Lemma 2: a maximum threshold; Lemma 3:
  a directional statement motivating verification that bounds angle as well as magnitude. The optimal
  verification strategy is shown to **exist** but not constructed.
- Definition 6 and Lemmas 5–6: the `c`-indexed spoofer family and two necessary conditions on it.
- Diagnosis: the two roles of verification (detecting valid trajectories; establishing precedence) fail
  for two different reasons — a missing noise model, and a missing learning-theory result.
- Prescription: cryptographic **data commitment** (replacing the original's public data release, which
  the paper argues is unnecessary and privacy-violating) plus **timestamping**.

## Key Definitions / Theorems

- **Assumption 1 (Reproducibility)**, **Assumption 2 (Representativeness)**, **Assumption 3 (Cheapness)**.
- **Definition 3 ((d, τ)-verification strategies)**, **Definition 4 (Representative Subset)**,
  **Definition 5 (Cost of a Proof)**, **Definition 6 (c-Cheap Proof Algorithm)**.
- **Lemma 1 (Minimum Threshold)** and **Corollary 1 (All Metrics)**: for metrics whose Lebesgue measure
  behaves as specified, a nonzero minimum tolerance is forced.
- **Lemma 2 (Maximum Threshold)**: proved "completely analogous to Lemma 1". If the Lemma 2 upper bound
  falls below the Lemma 1 lower bound, no valid threshold exists.
- **Lemma 4**: verifying a representative subset is equivalent to verifying all updates.
- **Lemma 5 (Stability of c-cheap algorithms)**: with probability `2/3` a `c`-cheap algorithm produces
  proofs only inside a `≤ ζ`-measure subset under the honest measure, `ζ = Var(C(P)) / (E(1−c)+a)²`,
  `a = √(3 Var(C(F(D, W_T))))`. Proof is two applications of Markov's inequality. Interpretation: the
  spoofer's output distribution is *more concentrated* than honest training's, which is a detection
  handle, not a cost bound.
- **Lemma 6 (Queries)**: `F_honest` needs `≥ log(1/3)/log(1−P)` queries with `P = Var_µ(C(P))/((1−c)²E²)`
  to hit a `c`-cheap proof. A lower bound on one sampling strategy.

## Connections

- Direct correction of [Proof-of-Learning: Definitions and Practice](proof-of-learning.md): Assumption 3
  is Property 2 restated; Definition 6 is the `δ`-indexed family the original lacked; the paper's opening
  observation is that the original authors "were unable to provide a formal analysis of security".
- Cited as the reason for abandoning Byzantine security in
  [PoL with Incentive Security](pol-incentive-security.md), which quotes this paper's claim that a
  provably Byzantine-secure PoL "is not possible to design until significant progress in further
  understanding in deep learning."
- Cited as a defeated baseline by [PoLO](polo-proof-of-learning-ownership.md), which replaces trajectory
  replay entirely.
- [What does it take to catch a Chinchilla?](catch-a-chinchilla-compute-monitoring.md) cites the spoofing
  attacks and concludes PoL "schemes are still heuristic-based and not yet provably secure."
- Concepts: [Proof-of-Learning (the notion)](../concepts/proof-of-learning.md),
  [Verifiable Computation](../concepts/verifiable-computation.md),
  [Fiber of the Training Map](../concepts/fiber-of-the-training-map.md).
- The precedence question — does knowing one local minimum of a non-convex objective pin down a
  trajectory — is the fiber-navigability question in optimisation clothing. See
  [Fiber of the Training Map](../concepts/fiber-of-the-training-map.md).
- The paper's own analogy for `c`-cheap algorithms is **knowledge transfer**: obtaining the identical
  `W_T` by training "is equivalent to knowledge transfer without any loss of information". That connects
  the cheapness question to [Model Extraction](../concepts/model-extraction.md) and to
  [Jagielski et al.](jagielski-model-extraction.md).
- Entities: [Nicolas Papernot](../entities/nicolas-papernot.md), [Hengrui Jia](../entities/hengrui-jia.md),
  [Anvith Thudi](../entities/anvith-thudi.md).

## Open Questions / Limitations

- **The central open problem, stated by the paper:** whether `c`-cheap algorithms exist for DNN training,
  and under which update rules and verification schemes. Equivalently: does knowing one minimum in a
  non-convex landscape guarantee a unique trajectory?
- Constructing the optimal verification strategy whose existence Lemma 1 and Corollary 1 establish.
- Whether an adversary can bypass that optimal strategy once constructed.
- Whether synthetic data can substitute for real training data in Zhang et al.-style attacks; the paper
  reports (without presenting the experiments) that training data is essential to those attacks, and
  says the cost of data synthesis needs analysis.
- The empirical negative result in §7 — stochastic spoofs appear hard to build — is explicitly
  non-comprehensive.

## Quotes / Notable Passages

> "formally proving the robustness of a proof verification mechanism for PoL is not currently possible."

> "we cannot formulate a proof verification mechanism that is optimal, i.e., provably minimizes an
> adversary's capability to disguise their trajectory within the noise inherent to training."

> "it remains an open problem whether algorithms given by Definition 6 can or cannot exist (under what
> update rules, verification schemes, etc.) for DNN training."
