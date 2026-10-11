---
title: Fine-Grained Complexity of Learning
type: concept
tags: [complexity theory, hardness-reductions, learning-theory, fine-grained-complexity]
---

## Definition

**Fine-grained complexity** proves conditional lower bounds on the running time of problems that already
have polynomial-time algorithms, by reduction from problems whose exact exponent is conjectured. Applied
to learning, it asks: given that empirical risk minimisation, kernel evaluation, or gradient computation
can be done in `O(n²)`, can they be done in `O(n^{2−δ})`? The answer is usually "not unless SETH is
false."

The standard antecedent is the **Strong Exponential Time Hypothesis (SETH)**: for every `ε > 0` there is a
`k ≥ 3` such that `k`-SAT on `n` variables cannot be decided in `O(2^{(1−ε)n})` time, randomised algorithms
included. Reductions typically run through two intermediate problems:

- **Orthogonal Vectors (OVP)**: given `A, B ⊆ {0,1}^d` of size `n`, is there `a ∈ A`, `b ∈ B` with
  `a^⊤b = 0`?
- **Bichromatic Hamming Close Pair (BHCP)**: given `A, B ⊆ {0,1}^d` and `t`, is there a pair at Hamming
  distance `< t`?

Both require `n^{2−o(1)}` time for `d = ω(log n)` under SETH, and `(nm)^{1−o(1)}` for unequal sizes
`|A| = n`, `|B| = m = n^α`.

## Intuition

Classical complexity is too coarse for learning: everything of interest is in P. Oracle lower bounds from
optimisation are the traditional alternative, but they apply only to a restricted class of algorithms and
they count oracle calls without pricing them. Fine-grained complexity gives up unconditionality in
exchange for covering *all* algorithms and *all* costs — a trade that matters when the question is
"how many FLOPs does this actually take?"

For this wiki the point is a negative-space observation. **The machinery is already calibrated to exactly
the object ML security wants to price, and nobody connected the two.** ML security wants a lower bound on
the cost of producing something that passes a training check
([Proof-of-Learning](proof-of-learning.md) Property 2). Fine-grained complexity produces lower bounds on
the cost of training steps, in exponent units, under a standard hypothesis. The two literatures do not
cite each other.

## Properties / Theorems

**Backurs–Indyk–Schmidt 2017** ([source](../sources/fine-grained-erm.md)) — the first application to
continuous optimisation. Under SETH, and for high-accuracy solutions:

- Kernel SVM optimal value, Gaussian kernel `C = 100 log n`, within `1 + ε` for `ε = exp(−ω(log²n))`:
  almost quadratic time (Theorem 4).
- Kernel ridge regression, `Σ` of entries of `K^{−1}`: almost quadratic (Theorem 6).
- Kernel PCA, even just the trace of the centred kernel matrix: almost quadratic (Theorem 8).
- Top-layer ERM for a depth-2 network with "nice" activation and loss, within `1 + 1/(4n)`: almost
  quadratic (Theorem 9).
- **Batch gradient computation**: `≥ O((nm)^{1−o(1)})` for `m` examples and `n` units (Theorem 10) — the
  "rectangular" bound. No algorithm computes a batch gradient faster than handling each example
  individually.

**Alman–Song 2024** ([source](../sources/fine-grained-gradient-llm.md)) — the same programme for attention.
A sharp threshold in the entry-magnitude bound `B`, at `B ≈ √(log n)`:

- `B = o(√(log n))`: `n^{1+o(1)}` algorithm for approximate attention-loss gradient computation.
- `B = ω(√(log n))`: no `O(n^{2−q})` algorithm for any `q > 0`, assuming SETH.

Combined with the same authors' earlier forward-pass result, this "completely characterizes the
fine-grained complexity of every step of LLM training." The lower bound is the first hardness result for
a *backward* step.

**The three qualifiers that block security reuse.** Backurs–Indyk–Schmidt states them explicitly: the
bounds are evidence against a sub-quadratic algorithm *to high accuracy*, *for all instances*, and *in the
worst case*. Each one is violated by real training:

- **High accuracy.** Algorithms with `poly(1/ε)` dependence escape — and the paper names SGD as one:
  "SGD sidesteps the quadratic time complexity of our lower bounds."
- **All instances.** Structured instances escape (Nyström, random features).
- **Worst case.** A security reduction needs the hard instances to be the ones that arise, or to be
  plantable. Fine-grained hardness gives neither.

**Contrast with restricted-class hardness.** The SQ line — see
[Statistical Query Model](statistical-query-model.md) and
[Learnability of Deep Random Networks](../sources/learnability-deep-random-networks.md) — bounds *one
class* of algorithms, unconditionally, on average over a distribution. Fine-grained complexity bounds
*all* algorithms, conditionally, in the worst case. Both price a learner's computation. Only the SQ line
has ever been carried into a security paper (as Theorem 3 of
[Jagielski et al.](../sources/jagielski-model-extraction.md)), and there only for the *attacker*.

## Where It Appears

- [On the Fine-Grained Complexity of Empirical Risk Minimization](../sources/fine-grained-erm.md).
- [The Fine-Grained Complexity of Gradient Computation for Training LLMs](../sources/fine-grained-gradient-llm.md).
- The gap it could fill: [Proof-of-Learning](../sources/proof-of-learning.md) Property 2,
  [Fang et al.](../sources/pol-more-broken.md) Assumption 3, and the `F`-hardness clause of
  [catch-a-chinchilla](../sources/catch-a-chinchilla-compute-monitoring.md).

## Related Concepts

- [Statistical Query Model](statistical-query-model.md) — the class-restricted alternative.
- [Proof-of-Learning (the notion)](proof-of-learning.md) — the security desideratum with no antecedent.
- [Compute Monitoring](compute-monitoring.md) — the governance consumer.
- [PAC Learning](pac-learning.md), [Statistical-Computational Gaps](statistical-computational-gaps.md).
- [Model Extraction](model-extraction.md) — the attacker-side cost question, currently priced in queries
  rather than time.

## Open Questions

- **Is there an average-case or plantable version?** Security needs the hard instances to arise naturally
  or to be sampled by the defender. Neither BIS17 nor AS24 raises this.
- **Where does the adversary go?** Both papers price one party's computation. A security statement needs
  two costs and a comparison. Nothing in the fine-grained-learning literature has a second party.
- Multi-layer and end-to-end training: AS24 composes per-step results; BIS17 treats one layer with the rest
  fixed.
- Whether the SETH-conditional exponent (`2 − o(1)`) is the right granularity for a security parameter, or
  whether a fine-grained one-way function framing (an exponent gap `honest^{1+δ}`) is the better target.
