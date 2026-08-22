---
title: "On the Fine-Grained Complexity of Empirical Risk Minimization: Kernel Methods and Neural Networks"
type: source
date_ingested: 2026-08-20
authors: [Arturs Backurs, Piotr Indyk, Ludwig Schmidt]
venue: "venue unconfirmed from PDF (the file is arXiv:1704.02958v1, 10 Apr 2017, and states no venue)"
year: 2017
tags: [complexity theory, hardness-reductions, learning-theory, fine-grained-complexity]
claim_quantifier: conditional
antecedent: "SETH — informally stated in the paper as: no algorithm decides satisfiability of a CNF formula with n variables and m clauses in time O(c^n · poly(m)) for some c < 2. Reductions run through Orthogonal Vectors (OVP) and Bichromatic Hamming Close Pair (BHCP), both known to require n^{2-o(1)} time for d = ω(log n) under SETH. Standard."
---

> **Provenance.** Verified against the primary PDF on 2026-08-20 (`raw/BIS17_FineGrainedERM.pdf`,
> extracted with `pdftotext`).

## Summary

The earliest paper in the lineage that
[The Fine-Grained Complexity of Gradient Computation for Training LLMs](fine-grained-gradient-llm.md)
extends, and the same negative-space entry: **conditional worst-case lower bounds on the honest
learner's own computation, with no adversary and no security game**. The paper states its own novelty as
being "the first application of this methodology to continuous (as opposed to combinatorial)
optimization problems."

Five hardness results, all SETH-conditional, all reductions from Orthogonal Vectors or Bichromatic
Hamming Close Pair with `d = ω(log n)`:

- **Kernel SVM** (Theorem 4): approximating the optimal value of the hard-margin dual within `1 + ε`,
  Gaussian kernel with `C = 100 log n`, `ε = exp(−ω(log²n))`, requires almost quadratic time.
- **Kernel ridge regression** (Theorem 6): computing the sum of entries of `K^{−1}` within `1 + ε`, same
  `ε`, Gaussian kernel with any `C = ω(log n)`.
- **Kernel PCA** (Theorem 8): even the *sum* of the eigenvalues of the centred kernel matrix
  `K' = (I − 1_n)K(I − 1_n)`.
- **Neural network ERM** (Theorem 9): approximating the optimal value of
  `min_α Σᵢ loss(yᵢ, f(aᵢ))` for a depth-2 network `f(a) = Σⱼ αⱼ S(a^⊤bⱼ)` within `1 + 1/(4n)`, for any
  `d = ω(log n)`, with "nice" activations (sigmoid, ReLU) and "nice" losses (hinge, logistic).
- **Gradient computation** (Theorem 10): computing a gradient of the empirical risk for `m` examples takes
  `≥ O((nm)^{1−o(1)})` time. This is the "rectangular" bound — evidence that **there is no algorithm that
  computes a batch gradient faster than handling each example individually**.

Theorem 10 is the one worth remembering for this programme. It says the trainer's per-batch work is
irreducible, conditionally, in the worst case. It is exactly the shape of statement a Proof-of-Learning
security proof would need on the *other* side of the game, and the two literatures have never met.

## Claim Boundary

- **Quantified over:** all algorithms (SETH-conditional), but **worst case over instances**, and only for
  **high-accuracy** solutions. The paper is explicit that this is the boundary: "our ERM lower bounds
  focus on algorithms that compute the solution to high accuracy, e.g., with a `log 1/ε` dependence on the
  approximation error `ε`." Algorithms polynomial in `1/ε` escape — and the paper names SGD as one such
  escape: "our results support this viewpoint since SGD sidesteps the quadratic time complexity of our
  lower bounds." Well-behaved instances also escape (Nyström, random features). No adversary appears
  anywhere; there is nothing to quantify over on that side.
- **Antecedent:** SETH, via OVP and BHCP. The unequal-size variant uses the `(nm)^{1−o(1)}` bound for
  `m = n^α`, `α ∈ (0,1)`, attributed to [BK15].
- **Does not establish:** (i) that these problems are hard on real data — worst case only; (ii) that
  approximate learning is hard — the whole point of the high-accuracy caveat is that it is not; (iii) any
  oracle-style bound — the paper distinguishes itself from oracle lower bounds, which "apply only to a
  limited class of algorithms" and "do not account for the cost of executing the oracle calls"; (iv)
  hardness of full network training — Theorems 9 and 10 are for the **top layer** of a depth-2 network
  with lower layers fixed (the motivating scenario is transfer learning); (v) anything about security,
  privacy, spoofing, or extraction.
- **Abstract vs theorem:** none found. The abstract says "we show that there are no algorithms that solve
  the aforementioned ERM problems to high accuracy in sub-quadratic time" — with "under these
  assumptions" and "to high accuracy" both present. The one place the body is stronger than a skim of the
  abstract would suggest is the framing of Theorem 10 as being about *batch* gradients specifically.

## The unnamed quantity

As with `AS24`, the quantity is named — running time in `n` (and in `n·m` for gradients), with a
`2 − o(1)` exponent under SETH. What is missing is everything that would make it a security statement:

- **An adversary.** The cost belongs to the learner. Two-party comparison is absent, so there is no gap,
  no ratio, and no `δ`.
- **A game.** There is no notion of a party trying to produce a cheaper object that passes a check.
- **Average-case or samplable hard instances.** The hard instances are OVP/BHCP embeddings. A security
  reduction needs the hard distribution to be the one the honest party faces, or to be plantable.
- **Robustness to approximation.** The exclusion of `poly(1/ε)` algorithms is precisely the regime real
  training lives in — the paper says so, and names SGD. Any security claim built on this machinery would
  inherit that exclusion, which is the sharpest obstacle to reusing it.

The paper's own summary of its epistemic status is the right one to carry forward: "The lower bounds are
evidence that there is no 'silver bullet' algorithm for solving the aforementioned ERM problems in
sub-quadratic time, to high accuracy, and for all instances." Three qualifiers, all load-bearing.

## Key Contributions

- First application of fine-grained complexity to continuous optimisation / ERM.
- The five hardness results above, plus variants for other SVM formulations in an appendix.
- The rectangular gradient bound (Theorem 10) and its sigmoid counterpart in §8.
- A clean separation from oracle complexity: conditional but algorithm-agnostic and total-cost-accounting,
  where oracle bounds are unconditional but class-restricted and cost-blind.

## Key Definitions / Theorems

- **Definition 1 (Orthogonal Vectors, OVP)**, **Definition 2 (Bichromatic Hamming Close Pair, BHCP)**.
  Both require `n^{2−o(1)}` time for `d = ω(log n)` assuming SETH; with `|A| = n`, `|B| = m = n^α`, they
  require `(nm)^{1−o(1)}`.
- **Definition 3 (Hard-margin SVM)**, **Definition 5 (Kernel ridge regression)**,
  **Definition 7 (Kernel PCA)**, **Definition 13** ("nice" activation functions).
- **Theorem 4** (kernel SVM), **Theorem 6** (KRR), **Theorem 8** (kernel PCA), **Theorem 9** (top-layer
  NN ERM), **Theorem 10** (batch gradient, `(nm)^{1−o(1)}`).
- Kernel throughout: Gaussian `k(x, x') = exp(−C‖x − x'‖₂²)`, with the note that results generalise to any
  kernel with exponential tail.

## Connections

- The methodological ancestor of [The Fine-Grained Complexity of Gradient Computation for Training
  LLMs](fine-grained-gradient-llm.md), which credits "the high-level technique of [BIS17] from kernel
  density estimation".
- Concepts: [Fine-Grained Complexity of Learning](../concepts/fine-grained-complexity-of-learning.md),
  [PAC Learning](../concepts/pac-learning.md).
- The unclaimed junction, same as `AS24`: [Proof-of-Learning](proof-of-learning.md) Property 2 and
  [Fang et al.](pol-more-broken.md) Assumption 3 both need a lower bound on the cost of producing
  something that passes a training check. Theorem 10 is a lower bound on the cost of the honest gradient
  step. Neither literature cites the other. See
  [Proof-of-Learning (the notion)](../concepts/proof-of-learning.md).
- Contrast with class-restricted hardness: [Statistical Query
  Model](../concepts/statistical-query-model.md) bounds a *family* of algorithms unconditionally; SETH
  reductions bound *all* algorithms conditionally. Both price a computation; only the SQ line has been
  used inside a security paper (see [Jagielski et al.](jagielski-model-extraction.md) Theorem 3 and
  [Learnability of Deep Random Networks](learnability-deep-random-networks.md)).
- Entity: Ludwig Schmidt also appears in [RobustBench](robustbench.md).

## Open Questions / Limitations

- Worst case, high accuracy, all instances — the three qualifiers, each of which real training violates.
- Top layer only; the depth-2 restriction with fixed lower layers is a transfer-learning setting, not
  end-to-end training.
- The paper explicitly leaves open whether sub-quadratic algorithms exist for structured instances, and
  frames the variety of practical methods (Nyström, random features) as evidence that they do.
- Whether any of this can be pushed to an average-case or samplable hard distribution — the prerequisite
  for security use — is not raised.

## Quotes / Notable Passages

> "we do not know if there are more efficient techniques for computing (mini-)batch gradients than simply
> treating each example in the batch independently."

> "To the best of our knowledge, our paper is the first application of this methodology to continuous (as
> opposed to combinatorial) optimization problems."
