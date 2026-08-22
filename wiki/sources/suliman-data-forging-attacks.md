---
title: Towards a Re-evaluation of Data Forging Attacks in Practice
type: source
date_ingested: 2026-07-26
authors: [Mohamed Suliman, Anisa Halimi, Swanand Ravindra Kadhe, Nathalie Baracaldo, Douglas Leith]
venue: "venue unconfirmed from PDF. The ingested file is arXiv:2411.05658v2, 10 June 2025, and states no venue. Affiliations given on the file are IBM Research and Trinity College Dublin."
year: 2025
tags: [adversarial-ml, complexity theory, reconstruction, poisoning-attacks, hardness-reductions]
claim_quantifier: empirical
antecedent: "For the empirical claim, none beyond the measured architectures and datasets. For Proposition 1, a fully connected network with per-example cross-entropy loss, one-hot labels, and batch size 1. For Proposition 2, a fully connected network with db > d1(d+b), where d1 is the width of the first hidden layer. For Proposition 3, a single-layer network with b > rank of the gradient. The computational-infeasibility conjecture rests on no stated antecedent because it is not proved."
adversary_bound: "none. The forging adversary is unbounded in compute, queries, and memory. What restricts it is a feasibility constraint, that the forged mini-batch lie in the allowed domain X x Y, together with the verifier's reproduction-error threshold. No running-time bound and no hardness assumption appear anywhere in the paper."
date_verified: 2026-08-22
---

> **Verified against the primary source.** Every quotation below was checked against
> `raw/S+25_DataForgingAttacks.pdf` on 2026-08-22 and is verbatim.

## Summary

The paper re-evaluates data forging attacks. *Data forging* replaces a mini-batch in a recorded
training trace with a different mini-batch producing nearly the same gradient, so that a model owner
can claim to have trained on data it did not use. The stated purpose is critical rather than
constructive. The authors measure how large the reproduction error of ordinary retraining is across
fully connected, convolutional, and transformer architectures on tabular, image, and text data, and
they find that the approximation errors of published forging attacks are often several orders of
magnitude larger. On that basis they conclude that current attacks are detectable by a verifier and
therefore carry no privacy consequence in practice.

The theoretical half extends the analysis of Baluta et al. by asking, for fully connected networks,
when two distinct mini-batches can produce the same gradient at all. Exact forging is written as a
system of linear equations whose solutions are candidate forged mini-batches. At batch size 1 no
distinct pair exists. Above batch size 1 infinitely many do, but only over the unrestricted real
domain. The authors then observe that an attacker needs a solution lying in the allowed domain, with
pixel values in a finite grid and one-hot labels, and that no efficient method for finding one is
known. They conjecture that none may exist.

## Claim Boundary

- **Quantified over.** The headline claim is quantified over the specific architectures, datasets,
  and hyperparameters measured, and over the published attacks compared against them. It is a
  measurement, not a theorem. Proposition 1 is universally quantified over pairs of training examples
  in `Z = R^d × {one-hot vectors}` for fully connected networks. Propositions 2 and 3 are existential,
  asserting that infinitely many gradient-equivalent perturbations or mini-batches exist under a rank
  or dimension condition.
- **Antecedent.** The propositions carry the structural hypotheses listed in the front matter. The
  conjecture carries none, because it is not proved and no reference problem is named.
- **Which party is constrained and in what resource.** Neither party is constrained in a computational
  resource. The verifier is constrained by a fixed reproduction-error threshold, which is what makes
  current attacks detectable. The attacker is constrained only by the requirement that its forged
  mini-batch be a valid input, which is a feasibility constraint on the output rather than a bound on
  the search. The word "computationally infeasible" appears in the conjecture without an adversary
  class, a hardness assumption, or a running-time parameter.
- **Does not establish.** It does not establish that constrained fiber navigation is hard. It does not
  reduce the problem to any reference problem. It does not prove anything about the full training map
  over many steps, only about a single gradient. It does not show that forging is impossible, only
  that the published instances are detectable at the thresholds measured. Proposition 1 is an
  impossibility at batch size 1 and says nothing about the batch sizes used in practice, a point the
  authors make themselves.
- **Abstract versus theorem.** The abstract is careful. It says finding in-domain solutions "is a non
  trivial task" and stops there. The stronger word "infeasible" appears in the contribution list, in
  the body, and in the conclusion, always hedged by "we conjecture" except at one point in Section 5.3
  where the body calls the task "a non trivial, computationally infeasible task" without a hedge. That
  single unhedged sentence is stronger than anything the paper proves.

## Key Contributions

- Measurement of reproduction error under nondeterministic GPU execution across three architecture
  families and three data types, giving a concrete detection threshold for a verifier.
- The finding that published forging attacks miss that threshold by orders of magnitude, so they are
  detectable.
- An extension of Baluta et al.'s analysis from the existing attack instantiations to the general
  question of when distinct mini-batches share a gradient, formulated as a linear system.
- The explicit statement that unconstrained solution count and in-domain solution finding come apart,
  and the conjecture attached to it.

## Key Definitions / Theorems

- **Definition 1 (distinct mini-batches).** `B` and `B'` in `Z^b` are distinct if some example of `B`
  differs from every example of `B'`.
- **Proposition 1 (batch size 1).** For `Z = R^d × {u ∈ {0,1}^n : Σ u_i = 1}` and a fully connected
  network, for any two training examples in `Z`, equality of the per-example gradients forces equality
  of the examples. Verbatim: *"For any two training examples (x, y), (x′ , y′ ) ∈ Z if ∇θ ℓ( fθ (x), y)
  = ∇θ ℓ( fθ (x′ ), y′ ), then x = x′ and y = y′ ."* The authors note the result holds over the
  unrestricted real domain, not only over the finite set of valid images.
- **Proposition 2 (batch size above 1).** If `db > d1(d + b)`, where `d1` is the width of the first
  hidden layer, there exist infinitely many perturbation matrices in `R^{d×b}` that preserve the
  gradient of the mini-batch. Labels are unchanged.
- **Proposition 3 (single-layer networks).** If `b > rank(∇_W L(B))` there exist infinitely many
  distinct mini-batches of size `b` with the same gradient, and these need not share the original
  labels.
- **The conjecture.** Stated once in the contribution list and once in the conclusion. Contribution
  list, verbatim:

  > "Of the infinite solutions that may exist, finding those that correspond to a distinct, valid
  > mini-batch i.e., one that falls within the domain of allowed training examples (e.g., in the case
  > of images, pixel values between 0 − 255 and one hot labels) is a non-trivial task, and one that we
  > conjecture may be computationally infeasible, even for relatively simple linear models such as
  > logistic regression."

  Conclusion, verbatim:

  > "Further research and analysis are required in order to determine whether data forging within these
  > restricted domains is possible. Given the difficulty of this task, we conjecture that it may not be
  > computationally feasible."

  Nothing further is said. No adversary class, no reference problem, and no hardness assumption is
  named anywhere in the paper.

## Connections

- **The programme's designated first theorem.** Prove or refute the conjecture above. The paper leaves
  the adversary class, the reference problem, and the hardness assumption entirely open, which is what
  makes the target well defined and what makes it work rather than a restatement.
- The paper does **not** discuss the distinction between the training map and the evaluation map, and
  it does not cite Jagielski et al.'s model-extraction work. Its reference list contains two other
  papers with a Jagielski coauthor, both on extracting training data. The comparison with
  [Jagielski et al.](jagielski-model-extraction.md), which proved NP-hardness for functional
  equivalence of two weight vectors rather than for inverting training, is an outside observation and
  must be attributed as such.
- Forging as an attack on unlearning verification.
  [Thudi et al.](auditable-unlearning-definitions.md) prove that forging maps **exist** for
  mean-sampler update rules, which is a statement about the size of the set of gradient-equivalent
  batches. This paper supplies the other half, that the in-domain search may be infeasible. Read as a
  pair they are size against navigability for the training map. See also
  [Zhang et al.](unlearning-verification-fragile.md), whose evasion attack avoids the domain-constraint
  problem by drawing substitute batches from real retained data, so that every candidate is
  domain-valid by construction at the cost of a smaller search space.
- Proof-of-Learning. The paper devotes a section to
  [Jia et al.'s Proof-of-Learning](proof-of-learning.md) and to the spoofing attacks on it, and records
  as open whether two distinct traces with distinct checkpoints can be built for the same final model
  using honest gradient updates that do not rely on near-zero-norm gradients. Concept page:
  [proof-of-learning](../concepts/proof-of-learning.md).
- Unforgeability certificates. Baluta, Nikolić, Jain, Aggarwal and Saxena, *Unforgeability in
  Stochastic Gradient Descent*, ACM CCS 2023, cited in the paper as reference [4] and the work this
  paper extends.
- Predecessor by two of the authors: Suliman and Leith, *Data Forging Is Harder Than You Think*,
  Private ML workshop at ICLR 2024.
- Concepts: [fiber-of-the-training-map](../concepts/fiber-of-the-training-map.md),
  [machine-unlearning](../concepts/machine-unlearning.md).

## Open Questions / Limitations

- **The conjecture is unproved and unformalised.** No hardness assumption is named, no reference
  problem is identified, and no adversary class is fixed. All three are the work.
- Domain constraints are what make the conjecture plausible, since the unconstrained problem is
  linear-algebraic and easy. Any hardness therefore comes from intersecting a linear condition with a
  box constraint, which is the shape of an integer-programming or lattice problem rather than a
  learning one. That reading is an inference from the paper's own formulation and is not stated in it.
- The analysis is for gradient equality at a single step, not for the full training map over many
  steps.
- The detectability finding is threshold-dependent. It rests on the measured reproduction errors, and
  the authors note that characterising those errors accurately requires thorough experimentation and
  is made harder by closed-source GPU driver code.
- The propositions cover fully connected networks. Convolutional and transformer architectures appear
  in the measurements but not in the theory.

## Quotes / Notable Passages

Abstract, on the gap the paper opens:

> "while there may exist an infinite number of distinct mini-batches with real-valued training examples
> and labels that produce the same gradient, finding those that are within the allowed domain e.g.
> pixel values between 0-255 and one hot labels is a non trivial task"

Section 5, the sharpest statement of the obstruction:

> "of the infinite, distinct, solutions that may exist, there are currently no known efficient
> techniques for finding solutions that correspond to a mini-batch that falls within the allowed domain
> X × Y"

Section 5.3, on the perturbation route, and the one place where the word "infeasible" appears without
the hedge:

> "while we prove the existence of an infinite number of possible perturbations that may applied to the
> original mini-batch that preserve the gradient, we have no guarantee that a perturbation that
> preserves image validity exists, even for relatively simple linear models. Efficiently finding such a
> perturbation is a non trivial task, and is currently the main barrier to successful exact data
> forging."

> "choosing the correct error matrix D such that the mini-batch B′ that is constructed from the
> resulting X′ and Y′ falls within the required domain is a non trivial, computationally infeasible
> task"
