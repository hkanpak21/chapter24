---
title: Local Differential Privacy
type: concept
tags: [differential-privacy, statistical-query, PAC-learning, learning-theory, sample-complexity]
---

## Definition

A differentially private algorithm that touches each record only through an independent per-record
randomizer, so no trusted curator ever holds the raw data.

From [KLNRS08](../sources/what-can-we-learn-privately.md):

- **Definition 5.1 (Local Randomizer).** An `ε`-local randomizer `R : D → W` is an `ε`-DP algorithm on a
  data set of size 1. Because any two singletons are neighbours, this constrains `R` on every pair of inputs.
- **Definition 5.2 (LR Oracle).** `LR_z(i, R)` returns a sample from `R(z_i)`.
- **Definition 5.3 (Local algorithm).** An algorithm is `ε`-local if it accesses `z` only through `LR_z`,
  with the per-record randomizer budgets summing to at most `ε` for each index.

`ε`-local algorithms are `ε`-differentially private (Claim 2.2 of that paper). The model is also known as
randomized response, input perturbation, PRAM, and FRAPP.

## Intuition

The curator is removed from the trust boundary. Each user randomizes their own record before it leaves their
device, so the guarantee holds even against a compromised collector. The cost is accuracy: every record
carries its own full noise, and there is no averaging over a trusted aggregate.

## Properties / Theorems

**Local DP learnability ⟺ SQ learnability.** The characterization of
[KLNRS08](../sources/what-can-we-learn-privately.md), Theorem 5.14: a concept class is learnable by an
interactive local learner iff it is learnable by an adaptive SQ learner. The correspondence preserves
structure — nonadaptive SQ ⟺ noninteractive local — and preserves efficiency in both directions provided the
local randomizers are **transparent** (Definition 5.13). The SQ notion is relaxed to allow a small failure
probability, which the paper argues is necessary because DP algorithms must have nonzero error.

**Consequences imported from SQ lower bounds.**

- Parity needs `2^{d/3}` SQ queries of tolerance `2^{−d/3}` even with unlimited computing time and uniform
  examples, but is efficiently privately PAC-learnable (KLNRS08 Theorem 4.4). Hence **locally learnable
  classes are a strict subset of privately PAC-learnable classes** (Corollary 5.15), and local algorithms
  need exponentially more data for some tasks.
- Masked parity is efficiently learnable by interactive local algorithms under the uniform distribution and
  needs exponentially many samples noninteractively — separating interactive from noninteractive local
  learning, and hence adaptive from nonadaptive SQ learning (Theorem 5.16). The separation is stated for
  **strong** learning only.

**Where the restriction sits.** The SQ bound prices the **learner** operating under a privacy constraint.
The adversary in the underlying DP guarantee is the standard unbounded distinguisher, quantified over all
measurable events. Nothing in this correspondence measures an adversary in SQ complexity. Recording this
because the equivalence is easy to misread as a statement about attackers.

**CDP in the local model.** Local CDP protocols can emulate any efficient central mechanism by secure
multiparty computation, which separates CDP from DP in the local model — noted by
[HMST22 §1.3](../sources/two-party-dp-complexity.md), which also cites Chan–Shi–Song for the optimality of
randomized response among information-theoretic local protocols for counting functionalities. The interesting
case is therefore neither the local model (where CDP obviously wins) nor the client/server model (where the
question is hard), but the two-party middle.

## Where It Appears

- [KLNRS08 — What Can We Learn Privately?](../sources/what-can-we-learn-privately.md)
- [HMST22 — On the Complexity of Two-Party DP](../sources/two-party-dp-complexity.md) §1.3
- [DP20 — SoK: Differential Privacies](../sources/sok-differential-privacies.md)

## Related Concepts

- [Statistical query model](statistical-query-model.md) — equivalent in learning power
- [PAC learning](pac-learning.md)
- [Computational differential privacy](computational-differential-privacy.md)
- [Capacity-bounded privacy](capacity-bounded-privacy.md)

## Open Questions

- The power of **nonadaptive** SQ learners, flagged by KLNRS08 as an important open problem precisely because
  the practically attractive local algorithms are the noninteractive ones.
- The exact price of privacy in samples; the known SQ simulation costs a factor `≈ t/ε` over the naive
  non-private implementation, where `t` is the number of queries.
- Whether the masked-parity separation extends to weak learning.
