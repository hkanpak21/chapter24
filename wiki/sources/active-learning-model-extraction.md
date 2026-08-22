---
title: Exploring Connections Between Active Learning and Model Extraction
type: source
date_ingested: 2026-08-21
authors: [Varun Chandrasekaran, Kamalika Chaudhuri, Irene Giacomelli, Somesh Jha, Songbai Yan]
venue: USENIX Security 2020 (the ingested PDF is arXiv:1811.02054v6, 20 Nov 2019, and does not itself state a venue)
year: 2019
tags: [adversarial-ml, learning-theory, PAC-learning, sample-complexity]
claim_quantifier: conditional
antecedent: "The hypothesis class F is public and known to the adversary; the server answers arbitrary chosen inputs, which places the reduction in the query synthesis scenario; the error function Err is fixed in advance; for the negative result on randomised defences, the server answers correctly with probability at least 1/2 + c for a constant c > 0 on every instance."
adversary_bound: "queries only. The adversary is charged a query budget q and is otherwise unbounded in time, memory and knowledge of F."
---

## Summary

The paper gives the pre-2023 literature its closest thing to a formal definition of model extraction,
and then shows that the definition is populated from an existing body of work. The route is a
reduction: any active learning algorithm in the **query synthesis** scenario, where the learner
fabricates its own instances rather than drawing them from a distribution, is already an extraction
adversary, with the same complexity and confidence. The consequence is that query complexity bounds
from active learning transfer wholesale into extraction attacks, which the paper then confirms
empirically on halfspaces, kernel SVMs and decision trees.

The definitional apparatus has three pieces. An **active learning system** is a learner and an oracle
interacting by membership queries, parameterised by scenario, query strategy and stopping criterion,
with `q_L(ε, δ)` its query complexity. The **extraction experiment** gives an adversary a description
of the class and `q` oracle queries, and outputs 1 if the returned hypothesis has error below `ε`
under a fixed error function. An **extraction attack** of complexity `q` and confidence `γ` is an
adversary whose success probability in that experiment is at least `γ` for every target in the class.

On the defence side the paper proves one negative result. Any randomised answering strategy that is
correct with probability at least `1/2 + c` on every instance is broken by repeating each query and
taking the majority, at a cost that multiplies the query complexity by a logarithmic factor. The
conclusion drawn is that a useful defence must make the corruption probability depend on the query and
the target function, not be a constant.

## Claim Boundary

- **Quantified over:** the extraction definition quantifies over all targets `f*` in the class, which
  is what makes it a worst-case-over-targets statement, and over the randomness of the adversary. It
  does not quantify over adversaries. Observation 1 is existential in the adversary, asserting that
  one exists given an active learner. Proposition 1 quantifies over randomised defences with bounded
  error probability and is existential in the adversary that defeats them.
- **Antecedent:** as listed in the front matter. Proposition 1 needs a constant gap, and the paper is
  explicit that its proof fails once the corruption probability reaches `1/2` on some instances, which
  is exactly the gap it recommends defenders aim at.
- **Adversary class:** unrestricted apart from the query budget. Compute is never charged. This is the
  paper's central limitation as a security definition, since an adversary that solves an NP-hard
  consistency problem between queries is admitted.
- **Does not establish:** any lower bound on extraction cost, and therefore no security guarantee for
  any class. Every complexity figure travels in the upper-bound direction, from an active learning
  algorithm to an attack. The converse, that a class hard to actively learn is hard to extract, is
  neither proved nor claimed. The extension of Proposition 1 to real-valued targets is stated not to
  be straightforward.
- **Abstract vs theorem:** the abstract offers formalisation of extraction and a discussion of defence
  strategies. What is proved about defences is one impossibility for a narrow family, constant-rate
  data-independent randomisation. The data-dependent alternative is discussed and evaluated
  empirically, with no guarantee attached.

## Key Contributions

- Definition 2, active learning system, and Definition 3, extraction attack of complexity `q` and
  confidence `γ`, together with the extraction experiment that connects them.
- Observation 1, the reduction from query-synthesis active learning to extraction, preserving query
  complexity and turning failure probability `δ` into confidence `1 − δ`.
- Proposition 1, the impossibility of defending by constant-rate label randomisation, with the
  explicit repetition attack and its `8/(1 − 2ρ)^2 · q ln(q/δ)` query cost.
- The argument that a defence must be data-dependent, illustrated by the distribution-over-classifiers
  approach of Alabdulmohsin et al., which the paper then attacks empirically.
- Empirical extraction of halfspaces, kernel SVMs and decision trees using active learning algorithms,
  with measured query complexities matching the imported asymptotics such as `O(d log(1/ε))` and
  `Õ(d(log(1/ε) + log(1/δ)))` for halfspaces.

## Key Definitions / Theorems

- **Definition 2, active learning system.** Learner `L` and oracle `O` exchange membership queries.
  Behaviour is fixed by scenario, query strategy and stopping criterion. In the PAC scenario instances
  come from the distribution, in the query synthesis scenario the learner generates them. The number
  `q_L(ε, δ)` at which the guarantee holds is the query complexity.
- **Experiment 1, extraction experiment.** `Exp^ε_F(S(f*), A, q)` gives `A` the class description and
  at most `q` oracle queries, and outputs 1 when the returned `f̂` satisfies `Err(f̂) ≤ ε`.
- **Definition 3, extraction attack.** `A` implements an `ε`-extraction attack of complexity `q` and
  confidence `γ` when `Pr[Exp^ε_F(S(f*), A, q) = 1] ≥ γ` for every `f* ∈ F`.
- **Observation 1.** If `(L, O)` is an active learning system for `F` in the query synthesis scenario
  with query complexity `q_L(ε, δ)`, then an adversary exists implementing `ε`-extraction with
  complexity `q_L(ε, δ)` and confidence `1 − δ`. The proof is that the adversary runs `L`, which is
  legitimate precisely because query synthesis needs no distribution.
- **Proposition 1.** For a randomised answering procedure `D` with `ρ_D(f*) < 1/2`, an adversary
  achieves `ε`-extraction with confidence `1 − 2δ` and complexity
  `q = 8/(1 − 2ρ_D(f*))^2 · q(ε, δ) ln(q(ε, δ)/δ)`.
- **Example 2, equation solving.** For linear regression on `R^d`, `d + 1` independent queries give
  `0`-extraction with confidence `1`.

## The unnamed quantity

The priced quantity is the query budget `q`, and the paper is unusual in the extraction literature for
making it a parameter of a definition rather than a table entry. Definition 3 reads `q` as an argument
alongside `ε` and `γ`, and Observation 1 is an equation between two such budgets. That is as far as it
goes. What the quantity lacks:

- **A definition on the security side.** Definition 3 defines a *successful adversary*, not a *secure
  class*. It lower-bounds one adversary's success probability by `γ`. The complementary statement, that
  for all adversaries with budget `q` the success probability is at most `γ`, is never written, so
  there is no notion of a class being `q`-extraction-secure and nothing to prove hard.
- **Compute.** Only queries are charged. The adversary's running time, memory and the cost of its
  internal consistency search are all free, so the definition cannot distinguish an attack that is
  cheap to mount from one that requires exponential work between queries. This is the axis
  [Cryptanalytic Extraction of Neural Network Models](cryptanalytic-extraction-nn.md) has to report in
  prose because no definition holds it.
- **An exponent or a ratio.** The budget is never compared to the victim's training cost, and no
  ratio or exponent relating attacker to defender appears.
- **An adversary class.** The adversary is unrestricted. The active learner is the *witness* to the
  upper bound, not a class the definition quantifies over, so nothing here restricts an attacker to
  the algorithm class that produced the model.
- **A lower bound.** None anywhere. The Limitations section says as much from the inside, noting that
  active learning label complexity depends heavily on the target hypothesis and ranges from
  `O(log(1/ε))` to `Ω(1/ε)`, so for some classes active learning saves nothing over passive learning.
  Imported upper bounds therefore need not be tight, and none of them is a floor.

## Connections

- [Model Extraction (Accuracy vs Fidelity)](../concepts/model-extraction.md)
- [High Accuracy and High Fidelity Extraction of Neural Networks](jagielski-model-extraction.md)
  supplies the goal taxonomy this definition's error function is instantiated against.
- [Cryptanalytic Extraction of Neural Network Models](cryptanalytic-extraction-nn.md) is the attack
  whose compute cost this definition cannot express.
- [Polynomial Time Cryptanalytic Extraction of Neural Network Models](polynomial-time-cryptanalytic-extraction.md)
- [Increasing the Cost of Model Extraction with Calibrated Proof of Work](calibrated-proof-of-work-extraction.md)
  is a data-dependent defence in the sense Proposition 1 recommends, though it charges compute rather
  than corrupting labels.
- [PAC Learning](../concepts/pac-learning.md) supplies Definition 1 and the passive baseline.
- [Statistical Query Model](../concepts/statistical-query-model.md)
- [Beyond Labeling Oracles: What does it mean to steal ML models?](beyond-labeling-oracles.md) and [Covert Learning: How to Learn with an Untrusted Intermediary](covert-learning.md)
  are the query-access learning models that price the learner in cryptographic units.
- [Kamalika Chaudhuri](../entities/kamalika-chaudhuri.md), [Somesh Jha](../entities/somesh-jha.md)

## Open Questions / Limitations

The paper's own Limitations section names three, and attributes them to active learning theory rather
than to its own construction. Label complexity of PAC active learning depends heavily on the target
hypothesis and can be as bad as the passive setting. Some query synthesis algorithms need labelled
data to bootstrap, which an extraction adversary may not have. The halfspace algorithms it implements
optimise geometric error between the true and learned separators, which need not track the
generalisation error by which a model is judged.

Two further gaps sit in the body. Proposition 1 does not extend straightforwardly to real-valued
targets, which is the case a regression API presents. And the data-dependent defence the paper
recommends is evaluated but not proved to resist anything.

## Quotes / Notable Passages

> Since many existing MLaaS providers operate in a pay-per-query regime, we use query complexity as a
> measure of efficiency of such model extraction attacks.

> the success probability of an adversary constrained by a fixed budget for queries is explicitly
> lower bounded by the quantity γ.

> We stress that these limitations are not a function of our specific approach, and stem from the
> theory of active learning.
