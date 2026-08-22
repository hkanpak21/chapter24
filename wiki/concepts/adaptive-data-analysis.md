---
title: Adaptive Data Analysis
type: concept
tags: [statistical-query, hardness-reductions, one-way-functions, learning-theory, sample-complexity, differential-privacy]
---

## Definition

The problem of answering statistical queries that are chosen **as a function of previous answers**, in a way
that remains valid with respect to the underlying distribution rather than to the sample.

Formally, in the SQ model of Kearns: an *oracle* holds `n` samples from an unknown distribution `D` over
`{0,1}^d`. A statistical query is a predicate `p : X → {0,1}` with true answer `q(D) = E_{x∼D} p(x)`. An
answer `a` is **valid** (statistically valid, accurate) if `|a − q(D)| ≤ α`. An *analyst* produces
`q_{i+1}` from the transcript `q_1, a_1, …, q_i, a_i`. The oracle is *accurate given `n` samples for `k`
adaptively chosen queries* if for every `D` it answers any efficient adaptive analyst's `k` queries validly.

The non-adaptive version is trivial: `k = 2^{o(n)}` queries fixed in advance can all be answered by the
empirical mean, via Hoeffding plus a union bound. Everything interesting comes from adaptivity.

## Intuition

Modern data analysis is inherently adaptive — model choice, hyperparameter tuning, and feature selection all
depend on prior interactions with the same dataset. Data-science competitions are the extreme case: hundreds
of analysts repeatedly evaluating against one held-out set. Adaptivity is why false discovery persists even
where classical multiple-testing corrections are applied: those corrections assume the hypotheses were fixed
in advance.

Answering with the empirical mean is always accurate **on the sample** and is exactly what fails under
adaptivity. The whole difficulty is that validity is defined against the distribution.

## Properties / Theorems

**Upper bounds.** Dwork–Feldman–Hardt–Pitassi–Reingold–Roth: an inefficient oracle can answer exponentially
many adaptive queries; an efficient one can answer a quadratic number. The mechanism is differential privacy
used as a **stability** condition — DP output is insensitive to one record, stability implies generalization,
so a DP oracle's answers generalize.

**Lower bound.** [Hardt–Ullman](../sources/preventing-false-discovery-hard.md) Theorem 1.1: assuming one-way
functions exist, **no computationally efficient oracle given `n` samples is accurate on `n^{3+o(1)}`
adaptively chosen queries.** Tight against the DFHPRR upper bounds up to a factor of `n`. Theorem 1.2 removes
the assumption at the price of dimension `d = n^{3+o(1)}`, ruling out even unbounded oracles. Theorem 1.3
restates it as blatant non-privacy.

The attack is a reconstruction attack driven by a robust fingerprinting code, with an encryption scheme
hiding the off-sample definition of each challenge query. The encryption is where — and the only place where
— the computational assumption is used; for "natural" oracles reporting only sample statistics, the proof is
unconditional.

**A dimension condition is necessary.** Hardness needs `2^d` superpolynomial in `n`. If `n ≫ 2^d` the
empirical distribution is close in statistical distance and every query is answerable.

**Validity, not confidentiality.** This is a hardness result about *generalization*. Hardt–Ullman are
explicit that accuracy is defined against the distribution here, whereas in the privacy setting it is defined
against the sample and is trivially achievable by a blatantly non-private oracle. The two settings share
machinery — fingerprinting codes, reconstruction — and have different goals.

**The positive direction from restricted adversaries.** [CIM19](../sources/capacity-bounded-dp.md) Theorem 6
shows a capacity-bounded privacy guarantee also implies generalization, with gap `≤ √(8ε)`, under a condition
linking the adversary class `H` to the query class `Q`. Only in expectation, and only non-adaptively.

## Where It Appears

- [HU14 — Preventing False Discovery in Interactive Data Analysis is Hard](../sources/preventing-false-discovery-hard.md)
- [CIM19 — Capacity Bounded Differential Privacy](../sources/capacity-bounded-dp.md) §6
- [ML24 — Query Complexity of Training Data Reconstruction](../sources/query-complexity-reconstruction.md) —
  the other query-count-as-parameter result, without a hardness assumption

## Related Concepts

- [Statistical query model](statistical-query-model.md)
- [Data reconstruction attack](data-reconstruction-attack.md)
- [One-way functions](one-way-functions.md)
- [Computational differential privacy](computational-differential-privacy.md)
- [Local differential privacy](local-differential-privacy.md) — the same SQ model, with the restriction on
  the learner instead

## Open Questions

- Close the gap between the `n²` efficient upper bound and the `n^{3+o(1)}` lower bound.
- **Note for this programme.** Adaptive data analysis is the one place in this literature where a resource
  budget, a matching upper bound, a lower bound at a stated exponent, and a hardness assumption doing one
  identifiable job all coexist. That is the structural template. What it still lacks is a *relative* budget:
  analyst and oracle are both merely "efficient," with no exponent separating them.
