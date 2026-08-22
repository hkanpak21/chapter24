---
title: The Fine-Grained Complexity of Gradient Computation for Training Large Language Models
type: source
date_ingested: 2026-08-20
authors: [Josh Alman, Zhao Song]
venue: "venue unconfirmed from PDF (the file is arXiv:2402.04497v1, 7 Feb 2024, and states no venue)"
year: 2024
tags: [complexity theory, hardness-reductions, learning-theory, fine-grained-complexity]
claim_quantifier: conditional
antecedent: "SETH (Strong Exponential Time Hypothesis), stated in the paper as Hypothesis 3.3: for any ε > 0 there is a k ≥ 3 such that k-SAT on n variables cannot be solved in O(2^{(1-ε)n}) time, including by randomized algorithms. Standard in fine-grained complexity. The upper bound is unconditional but requires bounded entries."
---

> **Provenance.** Verified against the primary PDF on 2026-08-20 (`raw/AS24_FGGradientLLM.pdf`, extracted
> with `pdftotext`).

## Summary

A negative-space entry. This is fine-grained complexity applied to **the honest trainer's own
computation** — no adversary, no security game, no privacy notion anywhere in the paper. The object is
one attention layer's backward pass, formalised as **Approximate Attention Loss Gradient Computation**
(`AAttLGC(n, d, ε)`): given `A₁, A₂, A₃, E ∈ R^{n×d}` and fixed `Y ∈ R^{d×d}`, output `g̃` with
`‖g̃ − dL(X)/dX‖_∞ ≤ ε`, where `L(X) = 0.5‖D(X)^{−1}exp(A₁XA₂^⊤/d)A₃Y − E‖_F²` and
`D(X) = diag(exp(A₁XA₂^⊤/d)1_n)`.

The result is a **sharp threshold in the entry-magnitude parameter `B`** (the bound `‖A₁X‖_∞ ≤ B`,
`‖A₂‖_∞ ≤ B`), at `B ≈ √(log n)`:

- `B = o(√(log n))`: an `n^{1+o(1)}` algorithm, to `1/poly(n)` accuracy (Theorem 1.6 / Theorem D.6).
- `B = ω(√(log n))`: **assuming SETH**, no `O(n^{2−q})` algorithm for any `q > 0` (Theorem 1.5 /
  Theorem 5.5).

Combined with the same authors' earlier forward-pass result, this "completely characterizes the
fine-grained complexity of every step of LLM training." The lower bound is obtained by reduction from
the forward attention problem to the gradient problem — nontrivial because it needs control over how
fast the gradient grows, supplied by a second-derivative bound `|f''(λ)| ≤ O(n log²n · κ(n)²)`.

Why this belongs in a security wiki: the machinery here is *already calibrated to exactly the object ML
security wants to price*. Property 2 of [Proof-of-Learning](proof-of-learning.md) asks for a lower bound
on the cost of producing something equivalent to a training run. This paper produces a conditional
worst-case lower bound on the cost of one training step, in the right units, with a standard antecedent.
Nobody has connected the two: the paper contains no security or privacy vocabulary, and the PoL line
cites no fine-grained complexity.

## Claim Boundary

- **Quantified over:** all algorithms, in the SETH-conditional sense — the lower bound rules out any
  `O(n^{2−δ})` algorithm, not a restricted class. But it is **worst-case over inputs**: Theorem 5.5 is
  existential over instances (it exhibits hard inputs, specifically `d = O(log n)`,
  `‖A₁‖_∞, ‖A₂‖_∞, ‖A₃‖_∞ ≤ O(√(log n)·κ(n))` for any `κ(n) = ω(1), o(log n)`, `B = 0`, `Y = I`,
  `X = λI` with `λ ∈ [0,1]`, `ε = O(1/(log n)⁴)`). Note the specificity of that instance family: `Y` is
  the identity, `X` is a scalar multiple of the identity. **There is no adversary and no security game to
  quantify over.**
- **Antecedent:** SETH, stated as Hypothesis 3.3 and standard. The upper bound needs only bounded
  entries. Nothing else.
- **Does not establish:** (i) that training real LLMs is hard — the bound is worst case over a
  constructed instance family and single-layer; (ii) anything about the *whole* training run, only about
  one forward/backward step (the "entire training process" claim is a composition of per-step results);
  (iii) any statement about an adversary, a spoofer, a privacy attacker, or a model extractor; (iv) that
  gradient computation is hard when `B` is small — the same paper gives a near-linear algorithm there.
  Remark 1.3 also narrows the object: the loss depends on both `X` and `Y`, and the paper fixes `Y`
  because the dependence on `Y` is linear.
- **Abstract vs theorem:** none found. The abstract's strongest phrase — "This completely characterizes
  the fine-grained complexity of every step of LLM training" — is defensible given the matching upper and
  lower bounds at the threshold, though "every step" means every *step of the studied one-layer attention
  objective*, and the paper says so in §1.1 and Remark 1.3.

## The unnamed quantity

Here the quantity is not unnamed — that is the point of including the paper. It is running time as a
function of sequence length `n`, with a named threshold parameter `B` and a named exponent (`2 − q`
against `1 + o(1)`), conditional on a named hypothesis.

What it lacks, relative to what ML security needs:

- **An adversary.** The cost is the *defender's*. There is no second party, so there is no ratio, no gap,
  and no game. The quantity is priced but never compared.
- **A security definition to attach to.** The paper's own suggested use is engineering guidance ("These
  insights can guide LLM designers to more efficient algorithms"; when `B` must be large, "one may as
  well use straightforward algorithms and focus on other aspects of algorithm speedup such as
  parallelization").
- **Average-case content.** SETH-based fine-grained lower bounds are worst case; a security statement
  needs the hard instances to be the ones that arise, or to be samplable.

The seam is therefore narrow and specific: fine-grained complexity supplies conditional lower bounds on
training-step cost in exponent units, and PoL-style security supplies a desideratum that the attacker's
cost exceed the trainer's, in no units at all. Nothing joins them.

## Key Contributions

- **Definition 1.4 (`AAttLGC(n, d, ε)`)**: the backward step as an approximate-output problem.
- **Theorem 1.5 / 5.5 (lower bound)**: SETH-conditional `n^{2−o(1)}` hardness above the threshold. The
  paper states this is the first hardness result for a *backward* computation step in LLM training —
  prior fine-grained work covered only forward computation.
- **Theorem 1.6 / D.6 (upper bound)**: `n^{1+o(1)}` algorithm below the threshold, built on low-rank
  approximation of the attention matrix via the polynomial method, extended to the backward pass with
  tensor-algebra tools to handle entry-wise products and high-rank sparse terms.
- Getting around the "Hessian barrier": prior work on optimising attention layers used Newton-type
  methods requiring Hessians, which are substantially more expensive; working directly with the gradient
  yields both faster algorithms and stronger lower bounds.
- Appendix B verifies that the stated forward/backward problems match the ones used in practice.

## Key Definitions / Theorems

- **Definition 1.1 (ℓ-th layer forward computation)**:
  `E_{ℓ+1} ← D^{−1} exp(E_ℓ QK^⊤E_ℓ^⊤/d) E_ℓ V`.
- **Definition 1.2 (Attention optimization)**:
  `min_X L(X) := 0.5‖D(X)^{−1}exp(A₁XA₂^⊤/d)A₃Y − E‖_F²`.
- **Definition 1.4 (AAttLGC)**, **Hypothesis 3.3 (SETH)**, **Theorem 5.5**, **Theorem D.6**.
- Proof structure of the lower bound: reduce from the hard forward instances via a scalar path
  `X = λI, λ ∈ [0,1]`; bound `|f''(λ)|`; evaluate `f'` at `O(log⁴ n)` points using the assumed gradient
  algorithm and average.

## Connections

- Direct descendant of [On the Fine-Grained Complexity of Empirical Risk
  Minimization](fine-grained-erm.md): the paper credits "the high-level technique of [BIS17] from kernel
  density estimation" as the basis for its lineage of attention lower bounds.
- Concepts: [Fine-Grained Complexity of Learning](../concepts/fine-grained-complexity-of-learning.md).
- The unclaimed junction: [Proof-of-Learning (the notion)](../concepts/proof-of-learning.md) and
  [Proof-of-Learning: Definitions and Practice](proof-of-learning.md) need a lower bound on the cost of
  producing a passing proof; this paper supplies the template for lower-bounding the cost of the honest
  step. Neither literature cites the other.
- The same absence of an adversary distinguishes this line from
  [Statistical Query Model](../concepts/statistical-query-model.md)-based hardness, where the *class* of
  algorithms is the object; here it is the *time*, over all algorithms.
- Entities: [Josh Alman](../entities/josh-alman.md), [Zhao Song](../entities/zhao-song.md).

## Open Questions / Limitations

- Single attention layer; multi-layer composition is asserted rather than analysed.
- Worst case over a constructed instance family, with `Y = I` and `X = λI` in the hard instances.
- The magnitude `B` needed in practice is cited to the authors' other work as an open empirical question:
  "The magnitude of `B` needed has been studied more recently … and the need for fast training algorithms
  may further motivate this direction of research."
- No adversary, no game, no comparison of two parties' costs — the gap this wiki cares about.

## Quotes / Notable Passages

> "This completely characterizes the fine-grained complexity of every step of LLM training."

> "To our knowledge, ours is the first work to prove hardness of a backward computation step for training
> an LLM or similar model."
