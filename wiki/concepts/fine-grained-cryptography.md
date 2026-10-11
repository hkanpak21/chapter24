---
title: Fine-Grained Cryptography
type: concept
tags: [cryptography, complexity-theory, fine-grained-cryptography, one-way-functions, circuit-complexity, computational-indistinguishability]
---

## Definition

Cryptography in which the adversary is granted **more resources than the honest parties, but only a
fixed, bounded amount more** — a polynomial gap rather than the superpolynomial gap of standard
cryptography. Degwekar, Vaikuntanathan and Vasudevan give the definition the field uses, verbatim:

> "Fine-grained cryptographic primitives are ones that are secure against adversaries with an apriori
> bounded polynomial amount of resources (time, space or parallel-time), where the honest algorithms
> use less resources than the adversaries they are designed to fool."

The motivation is Impagliazzo's worlds: a fine-grained primitive could plausibly exist even in
**Pessiland**, or even if `P = NP`, because time hierarchy theorems guarantee problems hard for
specific runtimes unconditionally. The genre begins with Merkle's 1974 puzzles — honest parties in
time `n`, eavesdropper needs `n^2`.

## The two moves, which are routinely conflated

Everything filed under this name does one of two different things to the adversary.

**Move 1 — restrict the adversary to a resource CLASS.** No ratio appears. The honest algorithms live
in `C1`, security holds against every function family in `C2`, and the separation is a class
inclusion. [Degwekar–Vaikuntanathan–Vasudevan](../sources/fine-grained-cryptography.md) build
`AC0`-computable primitives unconditionally secure against all of `AC0`, and `AC0[2]`-computable
primitives secure against `NC1` under `⊕L/poly ⊄ NC1`. There is no `δ` and nothing to tune.
[Wang–Su–Pan–Xu](../sources/nike-without-idealized-assumptions.md) reuse this exactly.

**Move 2 — price the adversary at `honest^{1+δ}`.** A number appears, and it is the point.
[Brzuska–Couteau Definition 6](../sources/fine-grained-one-way-functions.md) and
[LaVigne–Lincoln–Vassilevska Williams Definition 5](../sources/pkc-fine-grained-setting.md) do this,
in two mutually incompatible conventions — see
[Security Gap Exponent (δ)](security-gap-exponent.md).

These are different research programmes wearing one name. A class restriction cannot be tightened or
loosened; an exponent can. A class restriction can give *unconditional* security (`AC0`); an exponent
restriction has never been made unconditional. Move 1 is a statement about what algorithms the
adversary may run; Move 2 is a statement about how much of anything it may do.

## Which resource is priced

Every construction in this repo picks one, and the choices are not comparable:

| resource | where | unit |
|---|---|---|
| circuit size | [Brzuska–Couteau](../sources/fine-grained-one-way-functions.md) | wires, non-uniform |
| running time | [LaVigne et al.](../sources/pkc-fine-grained-setting.md), [Bauer et al.](../sources/fine-grained-nike-revisited.md) | word-RAM steps, uniform |
| circuit depth (as class) | [Degwekar et al.](../sources/fine-grained-cryptography.md), [Wang et al.](../sources/nike-without-idealized-assumptions.md) | `AC0`, `AC0[2]`, `NC1` |
| depth (as rounds) | [Guan–Montgomery](../sources/sequential-functions-fine-grained.md) | sequential rounds; total work unpriced |
| memory | [Wang et al.](../sources/nike-without-idealized-assumptions.md) §5 | bits of storage, computation unbounded |
| oracle queries | [Afshar et al.](../sources/fine-grained-nike-lower-bounds.md) | queries, substituted for time by fiat |
| aggregate power per round | [Ball et al.](../sources/permissionless-consensus-fine-grained.md) | steps per round, summed over parties |

## Properties / Theorems

- **The quadratic wall.** Merkle-descended constructions stop at quadratic.
  [Afshar et al.](../sources/fine-grained-nike-lower-bounds.md) show any 3-NIKE in **Maurer's** generic
  group model falls to an `O(n^2)`-*query* attack; [Bauer et al.](../sources/fine-grained-nike-revisited.md)
  reach `N^{1.6}` from the positive side in the same model. Superquadratic-gap public-key
  cryptography outside idealized models is open.
- **The Pessiland pincer.** [Brzuska–Couteau](../sources/fine-grained-one-way-functions.md) show no
  relativizing or black-box construction gets fine-grained OWFs from exponential (or even
  parallel-repetition-amplifying) average-case hardness.
  [Alman–Huang–Yeo](../sources/fine-grained-world-without-crypto.md) show that in the very world the
  field is aiming for — no one-way functions — the average-case hypotheses it builds on are false for
  sufficiently large `k`. The field's stated motivation and its available assumptions are in tension.
- **Barriers on the worst-case route.** The Ball–Rosen–Sabin–Vasudevan OV path to fine-grained OWFs
  would falsify NSETH, as LLV19 report. Only two primitives are known from *worst-case* fine-grained
  assumptions: proofs of work, and permissionless consensus
  ([Ball et al.](../sources/permissionless-consensus-fine-grained.md)).
- **Advantage is never negligible in the honest cost.** The adversary can always guess; both
  LLV19 and [Bauer et al.](../sources/fine-grained-nike-revisited.md) Remark 6 record this.
- **Infinitely-often is the usual price of a worst-case assumption.**
  [Degwekar et al. Remark 3.1](../sources/fine-grained-cryptography.md) states that all their
  `NC1`-side primitives are infinitely-often.

## Where It Appears

All eleven pages ingested in the 2026-08-20 batch:
[fine-grained-one-way-functions](../sources/fine-grained-one-way-functions.md),
[pkc-fine-grained-setting](../sources/pkc-fine-grained-setting.md),
[fine-grained-cryptography](../sources/fine-grained-cryptography.md),
[permissionless-consensus-fine-grained](../sources/permissionless-consensus-fine-grained.md),
[fine-grained-nike-lower-bounds](../sources/fine-grained-nike-lower-bounds.md),
[fine-grained-nike-revisited](../sources/fine-grained-nike-revisited.md),
[nike-without-idealized-assumptions](../sources/nike-without-idealized-assumptions.md),
[sequential-functions-fine-grained](../sources/sequential-functions-fine-grained.md),
[fine-grained-world-without-crypto](../sources/fine-grained-world-without-crypto.md),
[average-case-parity-problems](../sources/average-case-parity-problems.md),
[planted-orthogonal-vectors](../sources/planted-orthogonal-vectors.md).

## Related Concepts

- [Security Gap Exponent (δ)](security-gap-exponent.md) — Move 2, and its two conventions.
- [Orthogonal Vectors Conjecture](orthogonal-vectors-conjecture.md) — the hardness source.
- [Sequential Functions](sequential-functions.md), [Bounded Storage Model](bounded-storage-model.md) —
  the depth and memory axes.
- [One-Way Functions](one-way-functions.md),
  [Computational Indistinguishability](computational-indistinguishability.md),
  [Average-Case Reductions](average-case-reductions.md),
  [Statistical-Computational Gaps](statistical-computational-gaps.md).

## Open Questions

- Superquadratic gaps for public-key primitives without idealized models.
- A fine-grained OWF from a natural, non-idealized average-case assumption. Every construction in this
  batch either idealizes (RLM, ROM, GGM) or assumes a fine-grained average-case hypothesis outright.
- **Why this matters here.** Machine-learning security papers routinely compare an attacker's compute
  against a trainer's — extraction query counts, proof-of-learning spoofing costs, forging ratios —
  and never name the quantity or state an adversary class. This concept page is the formal home those
  comparisons would move into. The move is available off the shelf; what is missing is a theorem at a
  stated `δ` in ML units, not another definition.
