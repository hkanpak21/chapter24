---
title: Model Size as a Priced Resource
type: concept
tags: [overparameterization, adversarial-ml, complexity-theory, learning-theory, cryptography, robustness]
---

## Definition

A learner can be charged for **how large a model it must emit**, in the same way other results charge
a party for time, memory, queries, samples, or algorithm class. The measure used by
[Garg–Jha–Mahloujifar–Mahmoody–Wang](../sources/overparameterization-computational-constraints.md)
(Definition 2) is description length in bits:

> "L outputs models with at most p(·) bits of parameters"

which holds iff for every `λ` the support of `L(·, λ)` has size at most `2^{p(λ)}`. Parameter count is
therefore `log |Supp(L)|` — the log-cardinality of the set of classifiers the learner is able to
produce. It is architecture-free: no weights, neurons, layers or activation functions enter.

The **pricing question** is then: fix a learning task and a success criterion; how does the minimum
`p` move when the learner's *other* budgets are changed? Two directions are known to move it.

## Intuition

Counting is what makes this a *resource* rather than a description. A model of `p` bits can index at
most `2^p` classifiers, so if success requires the model to retain information about a hidden
`α`-bit string, and `p ≪ α`, the string still has min-entropy conditioned on the model
(Dodis et al.'s average-case min-entropy, `H̃_∞(X|Z) ≥ H_∞(X) − p`). An extractor — the GF(2) inner
product, or a small-bias mask — then makes the label statistically uniform in the model's view, and
the model does no better than chance. Every parameter lower bound in this line has that shape: *the
model is too short to be a key*.

What computational bounding adds is a way to make a *short* secret behave like a long one. If the
hidden string is pseudorandom rather than uniform, an unbounded learner stores the `λ`-bit seed while
an efficient learner cannot distinguish the string from uniform and is stuck paying its full length
`α ≫ λ`. Overparameterization becomes the price of not being able to invert.

## Properties / Theorems

**Direction 1 — bounding the learner raises the price.** On a constructed task under one-way
functions, an unbounded learner needs `2λ` parameters while any efficient learner needs `≥ α/2`
(non-robust) and `≥ c·β/log λ` (robust), with `n < λ < α < β` arbitrary polynomials in `λ`
([GJMMW22](../sources/overparameterization-computational-constraints.md), Theorems 20–22). The gap is
any polynomial one cares to name.

**Direction 2 — bounding the adversary lowers the price.** On a second constructed task, an efficient
learner is `negl(λ)`-robust against poly-time adversaries with *no parameters at all* and zero
samples, while `α/2` parameters are necessary against an unbounded adversary
([GJMMW22](../sources/overparameterization-computational-constraints.md), Theorems 28–29). Note the
asymmetry of the two theorems: the upper bound needs the *adversary* bounded, the lower bound holds
even for an *unbounded learner*.

**An information-theoretic price also exists, and is universal where this one is existential.** The
[Universal Law of Robustness](universal-law-of-robustness.md) (Bubeck–Sellke) charges `p ≳ nd`
parameters for smooth interpolation of `n` points in `R^d` under isoperimetry, for *any* smoothly
parameterized class and with no computational assumption. The two prices are not the same object:

| | Bubeck–Sellke | GJMMW22 |
|---|---|---|
| force | geometry (isoperimetry) | cryptography (one-way functions) |
| quantifier | universal over tasks and classes | existential — one constructed task |
| who pays | every learner, bounded or not | only the *bounded* learner |
| parameter | real weight, smooth parameterization | one bit of model description |
| what is separated | interpolation vs *smooth* interpolation | bounded vs unbounded learner, same task |

They coexist rather than compete: a discrete Hamming-metric construction with no Lipschitz
requirement falls outside Bubeck–Sellke's hypotheses entirely, which is why zero-parameter robustness
in Direction 2 is not a counterexample to the law.

**Relation to the other priced resources in this wiki.** Sample complexity is the closest neighbour —
[robust generalization requires `Ω(√d)` samples](../sources/robust-generalization-more-data.md) where
standard generalization needs `O(1)`, an information-theoretic price in *data*. Time is priced in
[fine-grained cryptography](fine-grained-cryptography.md) and in the
[fine-grained complexity of learning](fine-grained-complexity-of-learning.md). Storage is priced in
the [bounded storage model](bounded-storage-model.md), where the *adversary's* memory is the bounded
quantity and time is free — the closest structural analogue, but bounding the attacker's storage
rather than the defender's model. Model size is the one axis on which a *defender's own artefact*, not
its computation, is the metered good.

## Where It Appears

- [Overparameterization from Computational Constraints](../sources/overparameterization-computational-constraints.md)
  — introduces the bit-counted definition and both pricing directions.
- [A Universal Law of Robustness via Isoperimetry](../sources/universal-law-of-robustness.md) — the
  information-theoretic parameter price.
- [Adversarially Robust Learning Could Leverage Computational Hardness](../sources/computational-hardness-robust-learning.md)
  — the predecessor that priced robustness in *risk* rather than in model size.
- [Adversarial Examples from Computational Constraints](../sources/adversarial-examples-computational-constraints.md)
  — supplies the robust-ERM-over-a-finite-class bound (`log|C|/δ` samples) that turns a model-size
  budget into a sample-complexity budget, and so links the two axes.

## Related Concepts

- [Universal Law of Robustness](universal-law-of-robustness.md)
- [Computational vs Information-Theoretic Robustness](computational-vs-it-robustness.md)
- [Robust PAC Learning](robust-pac-learning.md), [Intrinsic Robustness](intrinsic-robustness.md)
- [Bounded Storage Model](bounded-storage-model.md),
  [Fine-Grained Cryptography](fine-grained-cryptography.md),
  [Fine-Grained Complexity of Learning](fine-grained-complexity-of-learning.md)
- [Unit of Protection](unit-of-protection.md) — the parallel axis on the privacy side: *what* is
  protected, versus *what the party is charged in*.

## Open Questions

- **Bits versus weights.** No result connects `log|Supp(L)|` to the weight count of a trained network.
  Until one does, "overparameterization" in this sense and in the empirical sense share a word, not a
  quantity.
- **Natural tasks.** Both known pricing directions live on constructed tasks. GJMMW22 states the gap
  openly as its central limitation.
- **A converse.** GJMM ALT'20 showed a computational-vs-IT *robustness* gap implies average-case
  hardness. Whether a *parameter* gap likewise implies a cryptographic assumption is not addressed.
- **Two budgets at once.** No definition in this wiki indexes a guarantee simultaneously by model size
  and by adversary resource, though GJMMW22's two constructions each hold one fixed while moving the
  other.
