---
title: Proof-of-Learning (the notion)
type: concept
tags: [verifiable-computation, certification, adversarial-ml, complexity theory]
---

> Disambiguation: this page is the **notion**. The 2021 paper that introduced it has its own source page,
> [Proof-of-Learning: Definitions and Practice](../sources/proof-of-learning.md).

## Definition

A **proof-of-learning (PoL)** scheme is a pair of protocols `(R, V)`. A prover `T` runs a training
procedure under reporting protocol `R`, producing final weights `W_T` and a proof `P`. A verifier `V`,
given `(P, W_T)`, accepts or rejects. Three requirements are always stated, in one form or another:

- **Completeness / correctness.** An honestly produced proof is accepted with high probability.
- **Verification efficiency.** Verifying costs less than proving. In the original notation,
  `E[C_V] ≤ E[C_T]`.
- **Spoof resistance.** No party holding `W_T` but not the proof can produce an accepting proof more
  cheaply than training. In the original notation, `E[C_T] ≤ E[C_A]`.

A **spoof** is an accepting proof not obtained by honest training. It is **dishonest** when it cost the
adversary strictly less than honest training cost the trainer: `E[C_A] < E[C_T]`.

## Intuition

Training is the most expensive thing anyone does with a model, and the trajectory it follows is
effectively unguessable. So log the trajectory and use it as a receipt. The verifier does not re-run the
whole thing; it re-runs a sample of steps and checks that each logged transition is reproducible within a
tolerance. Ownership claims, Byzantine-worker detection, and (later) compute governance all reduce to
"can you show me your receipt, and could you have forged it more cheaply than earning it?"

The last clause is the whole security content, and it is a **statement about a ratio of computational
costs**. That is what makes PoL the clearest specimen in this wiki of the thesis that ML security measures
computational quantities without naming them formally.

## Properties / Theorems

**What is proved, and what is not.**

| Object | Status in the literature |
|---|---|
| `E[C_V] ≤ E[C_T]` (Property 1) | **Desideratum** in the 2021 paper. Later given an asymptotic rate — `O(k log E / E)`, `O(k/E)` — by [PoL with Incentive Security](../sources/pol-incentive-security.md), Theorems 6.1 and 6.2. Measured as `1.5%–10%` by [PoLO](../sources/polo-proof-of-learning-ownership.md). |
| `E[C_T] ≤ E[C_A]` (Property 2) | **Desideratum**. Never proved for any construction. Restated as the *cheapness assumption* (Assumption 3) by [Fang et al.](../sources/pol-more-broken.md), who show settling it reduces to open problems in learning theory. |
| `E[C_A] < E[C_T]` (Definition 2) | **Definition**. |
| Entropy growth of the forward and reverse training processes | **Theorems** (1 and 2 of the 2021 paper) — but information-theoretic, about path multiplicity, not about cost. Assume i.i.d. hardware noise. |
| "Inverting training costs at least as much as training" | **Conjecture 1** of the 2021 paper, stated because the authors could not prove it. Asserted as a result in that paper's abstract. |
| `c`-cheap proof algorithms, `c ∈ [0,1)` | **Definition 6** of [Fang et al.](../sources/pol-more-broken.md) — the ratio finally indexed, by a multiplicative constant. Only *necessary conditions* on such algorithms are proved (Lemmas 5, 6); existence is open. |
| `J`-efficient and `F`-hard PoTT | **Definition 1** of [catch-a-chinchilla](../sources/catch-a-chinchilla-compute-monitoring.md) — the adversary bounded by *time*. No construction proved to meet it. |
| "Cheating is unprofitable" | **Theorems** 6.1, 6.2, 6.6 of [PoL with Incentive Security](../sources/pol-incentive-security.md) — but this is a utility comparison, and that paper *assumes* dishonest epochs cost the adversary zero. |
| "Forging costs `1.1–4×` honest generation" | **Measurement** in [PoLO](../sources/polo-proof-of-learning-ownership.md), on one hardware configuration, against two hand-built attacks, one of which (WMA) costs three orders of magnitude *less* than honest generation and is defeated on accuracy rather than cost. |

**Attack history.** Zhang, Liu, Ding, Wang, Wu, Ren (S&P 2022, arXiv:2108.09454) gave the first
counter-example. [Fang et al.](../sources/pol-more-broken.md) showed that attack targeted a weakened
instantiation, and gave two cheaper, reproducible attacks — the **infinitesimal update attack** (exploits
a static tolerance `δ`) and the **blindfold top-Q attack** (exploits the magnitude-based selection rule).
Both are *structurally correct spoofs*: invalid proofs that pass. Neither is a lower bound.

**Where the field went instead of parameterising the ratio.** Three directions, none of them a hardness
theorem: change the primitive (watermark chains, [PoLO](../sources/polo-proof-of-learning-ownership.md));
change the security notion (game theory,
[incentive security](../sources/pol-incentive-security.md)); or change the tooling (zero-knowledge proofs
of training, at prover costs the ML side considers impractical — see
[ZK-ML verification](zk-ml-verification.md)).

## Where It Appears

- [Proof-of-Learning: Definitions and Practice](../sources/proof-of-learning.md) — the origin.
- [Proof-of-Learning is Currently More Broken Than You Think](../sources/pol-more-broken.md) — the attacks
  and the assumption taxonomy.
- [PoLO](../sources/polo-proof-of-learning-ownership.md) — chained watermarks; measured ratios.
- [Proof-of-Learning with Incentive Security](../sources/pol-incentive-security.md) — the
  game-theoretic replacement.
- [What does it take to catch a Chinchilla?](../sources/catch-a-chinchilla-compute-monitoring.md) —
  Proof-of-Training-Transcript, a strictly harder variant, used as a governance primitive.
- [Auditable unlearning definitions](../sources/auditable-unlearning-definitions.md) — takes the PoL log as
  its notion of dataset feasibility.
- [Beyond Labeling Oracles](../sources/beyond-labeling-oracles.md),
  [Impossibility of Retrain Equivalence](../sources/impossibility-retrain-equivalence.md),
  [Unlearning verification is fragile](../sources/unlearning-verification-fragile.md) — the same bare
  attacker-vs-defender cost inequality in other subfields.

## Related Concepts

- [Verifiable Computation](verifiable-computation.md) — PoL is the non-cryptographic corner of it, adopted
  because SNARKs do not scale to training.
- [Fiber of the Training Map](fiber-of-the-training-map.md) — a spoof is a fiber element plus a path to it;
  spoof resistance is fiber navigability priced in compute.
- [ZK-ML verification](zk-ml-verification.md) — the cryptographic alternative.
- [Compute Monitoring](compute-monitoring.md) — the governance consumer of PoL.
- [Machine Unlearning](machine-unlearning.md), [Retrain Equivalence](retrain-equivalence.md) — the forging
  literature that grew out of the same log.
- [Model Extraction](model-extraction.md) — [Fang et al.](../sources/pol-more-broken.md) observe that a
  cheap spoofer would be "a type of special knowledge-transfer algorithm".
- [Fine-Grained Complexity of Learning](fine-grained-complexity-of-learning.md) — the machinery that could
  supply the missing lower bound, unconnected to this line.

## Open Questions

- **The central one.** Does knowing one local minimum of a non-convex training objective, plus the dataset,
  let an adversary reconstruct *some* valid trajectory to it more cheaply than training? Equivalently, do
  `c`-cheap proof algorithms exist? Stated as open by
  [Fang et al.](../sources/pol-more-broken.md).
- What are the units? Every scheme writes the cost as a bare `C` and measures it in whatever the
  experiment produced — wall-clock seconds, forward passes, epochs, FLOPs, dollars. No scheme fixes a
  hardware-independent unit, so the inequalities do not compose across papers.
- Is there a construction that is `J`-efficient and `F`-hard for a stated `F`, under a stated assumption?
  Nobody has attempted one.
- Could a fine-grained assumption (SETH, or a fine-grained one-way function) be the antecedent that PoL has
  never had? The two literatures do not cite each other; see
  [Fine-Grained Complexity of Learning](fine-grained-complexity-of-learning.md).
