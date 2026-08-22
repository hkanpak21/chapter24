---
title: Machine Unlearning
type: concept
tags: [adversarial-ml, verifiable-computation, reconstruction, hardness-reductions]
---

## Definition

**Machine unlearning** is the removal of a training point's influence from a trained model, on
request. Two families:

- **Exact unlearning**: retrain from scratch on `D \ D_u`. Correct by construction, expensive.
- **Approximate unlearning**: modify the existing parameters in a few updates so they are *close in
  parameter space* to a model that never saw `D_u`.

The target of both is [Retrain Equivalence](retrain-equivalence.md).

## The definitional situation

Unlearning is the sharpest instance in this wiki of a subfield whose central predicate is
undefined — and here the gap has been proved, not merely observed.

**Model-level and log-level definitions fail.**
[Thudi, Jia, Shumailov and Papernot](../sources/auditable-unlearning-definitions.md) show that
identical parameters are reachable from non-overlapping datasets, so proximity in parameter space
certifies nothing about what was trained on. Their formal device is **forgeability**, defined over
proof-of-learning logs: a forging map `B : H_D^{g,d,0} → H_{D'}^{g,d,ε}` is the identity on parameters
and substitutes `x_i ∈ D` by `x̃_i ∈ D'` while keeping every step reproducible within `ε`. At `ε = 0`
this is an equivalence relation whose classes are exactly the datasets reaching the same parameter
sequences (Theorem 1). Consequence, in their words: "one could unlearn without modifying the model at
all."

**Read the scope precisely.** Corollary 2 says unlearning on minibatch SGD "is not well-defined over
the logs (and thus the models) of finite datasets". It is proved existentially — for a mean-sampler
update rule, an adversary that controls the minibatch size `b` and can sample from `D` indefinitely,
and `ε > 0` — and the proof turns on exhibiting one bad instance. It is **not** a claim that
unlearning is impossible: the authors' own conclusion is that unlearning is well-defined **at the
algorithmic level**, with verifiable computation proposed as the route, and certified unlearning
explicitly retained provided it is paired with algorithm-level audit.

**Verification of unlearning is separately gameable — a critique of practice, not of the definition.**
[Zhang, Chen, Shen and Li](../sources/unlearning-verification-fragile.md) circumvent both families of
deployed verification (backdoor triggers; reproducing a Proof of Retraining) by choosing retained
mini-batches whose gradients mimic the removed points. Their Algorithm 1 produces a valid PoRT at
`ε = 0`. They close by asking for stronger verification — "there is no strict guarantee for the
verification of MUL" — not by declaring verification impossible.

**The target is separately unreachable for one algorithm class.**
[Yu, He, Goyal and Arora](../sources/impossibility-retrain-equivalence.md) show that under staged
training, two models trained on the same data in different orders diverge exponentially under the same
local unlearning rule, so at most one can be retrain-equivalent. Restricted to *local,
path-oblivious* algorithms and *staged* training. See [Retrain Equivalence](retrain-equivalence.md).

## Properties / Theorems

- Forgeability at `ε = 0` is an equivalence relation; `D ≡ D'` iff `H_D(W) = H_{D'}(W)`.
- Probabilistic forging for mean-samplers holds with probability
  `((1 − σ²_max/(bε²))(1 − (σ²_max/(bε²))ⁿ))^{mα}` — improving with larger batch `b` and looser
  tolerance `ε`, degrading with longer and more numerous logs.
- Under full-batch gradient descent the gradient difference between training on `D` and on `D \ D_u`
  "is deterministic and cannot be manipulated" — the batch-selection attack is a mini-batch phenomenon.
- Adversarial retraining that evades verification costs the same as honest retraining; the cheaper
  forging variant only defeats `ε > 0` thresholds.

## Where It Appears

- [On the Necessity of Auditable Algorithmic Definitions for Machine Unlearning](../sources/auditable-unlearning-definitions.md)
- [Verification of Machine Unlearning is Fragile](../sources/unlearning-verification-fragile.md)
- [On the Impossibility of Retrain Equivalence in Machine Unlearning](../sources/impossibility-retrain-equivalence.md)
- [Towards a Re-evaluation of Data Forging Attacks in Practice](../sources/suliman-data-forging-attacks.md)
- [Proof-of-Learning](../sources/proof-of-learning.md) — supplies the log format that forgeability is
  defined over.

## Related Concepts

- [Retrain Equivalence](retrain-equivalence.md)
- **[Fiber of the Training Map](fiber-of-the-training-map.md) — this is the same object.** A forging
  map is a move between two points of the fibre over a parameter trajectory. Thudi et al. establish
  the fibre is populated (size); Suliman et al. conjecture the constrained walk is hard
  (navigability). Unlearning is where size-vs-navigability shows up as a *policy* question.
- [Verifiable Computation](verifiable-computation.md) — the proposed repair.
- [Computational vs Statistical Memorization](computational-vs-statistical-memorization.md)
- [Data Reconstruction Attack](data-reconstruction-attack.md), [Model Extraction](model-extraction.md)

## Open Questions

- The cost of *finding* a forging map, in either direction. Existence is proved; hardness is
  conjectured only under domain constraints, by Suliman et al., and only for the training map.
- Whether an unlearning verification scheme can be built that resists gradient-mimicking batch
  selection. Zhang et al. ask for one and give no lower bound against it.
- Thudi et al. §7.3's unpursued suggestion: `inf{ε : D, D' are ε forgeable}` as a **metric on
  datasets**, modulo the `ε = 0` class — a distance measured in reproduction error rather than in data
  space.
