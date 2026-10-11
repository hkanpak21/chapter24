---
title: Sequential Functions
type: concept
tags: [cryptography, fine-grained-cryptography, complexity-theory, verifiable-computation]
---

## Definition

Informally, a function that a massively parallel adversary cannot compute substantially faster than an
honest party with limited parallel computation power. Formally, following the definitions
[Guan–Montgomery](../sources/sequential-functions-fine-grained.md) take from Jaeger et al.:

A sequential function `F = (Setup, Gen, Eval)` satisfies `(t_C(λ), t_A(λ))`-sequentiality for machine
models `(M_C, M_A)` when, verbatim:

> "1. There exists an algorithm in the computational model MC such that for all k and for all x that
> can be output by Gen, it computes Eval in at most time k · tC(λ). 2. For all λ ∈ N and for all
> tuples of PPT machines (A0, A1, A2), such that A2 runs in time strictly less than k · tA(λ) in the
> computational model MA ..."

`M_A` is assumed to have more parallel computation power than `M_C`. The parameter `k` is the number
of rounds. Variants: **selective**, **adaptive**, **dynamic** (by how much of the syntax may depend on
`k`); **iterative** (`Eval = Round^{(k)}`); and **continuous iterative** (CISF), where `Round` is
independent of `k` as well.

## Intuition

The adversary is not weakened in total work — it remains PPT, and in the VDF definition it gets
`poly(T, λ)` **processors**. Only its **depth** is bounded. The justification Guan–Montgomery offer is
that real adversaries' advantage over honest parties is mostly parallel, not sequential: *"a
supercomputing cluster may be able to perform sequential operations faster than a desktop computer,
but its real advantage over the desktop lies in its parallel processing abilities."*

This makes sequentiality **a different axis** from every other pricing in
[Fine-Grained Cryptography](fine-grained-cryptography.md). A cost model expressed in total operations
— FLOPs, gradient steps, queries — has no image in this definition.

## Properties / Theorems

- **Separated from one-way functions.** Guan–Montgomery's main theorem: assuming a PSPACE oracle,
  there is an oracle `O` and an `f^O` that is sequential but **not** one-way. Surprising, since
  sequential functions are normally built from assumptions that imply OWFs, and time-lock puzzles are
  known to imply OWFs.
- **A complexity boundary inside the definition.** The decisional worst-case CISF problem is
  **PSPACE-complete** (Theorem 2), while the decisional **dynamic** sequential function problem is
  **not in PSPACE** relative to a random oracle (Theorem 3, via parallel pebbling on the
  Paul–Tarjan–Celoni graph). The CISF/DSF distinction is real, not cosmetic.
- **What can be built without one-way functions:** fine-grained SKE and fine-grained MACs from a CISF
  (Theorems 4, 5) — but assuming an **ideal** CISF, whose `Round` takes exactly the same time for
  honest parties and adversaries. Fine-grained PKE from a VDF with perfect soundness, unique proofs and
  proof indistinguishability, plus iO for null circuits (Theorem 6).
- **What cannot be built:** fine-grained key exchange. Guan–Montgomery define a *commutative sequential
  function* and show it implies fine-grained NIKE, then report they could not construct one that was
  not already a key exchange protocol.
- **The standard assumption as usually stated is false.** Bernstein–Sorenson parallelize `g^{2^T}` in a
  group of unknown order to depth `O(T/lg lg T)` with `T^{1+o(1)}` processors. Rotem–Segev show
  generic speedups are equivalent to factoring, but no standard-model tie is known.

## Where It Appears

- [On Sequential Functions and Fine-Grained Cryptography](../sources/sequential-functions-fine-grained.md) — the only source in this repo that treats them directly.
- Adjacent in kind but not in mechanism:
  [Towards Permissionless Consensus](../sources/permissionless-consensus-fine-grained.md), where proofs
  of work price *total* work rather than depth, and non-amortizability rather than sequentiality is
  the property being engineered.

## Related Concepts

- [Fine-Grained Cryptography](fine-grained-cryptography.md) — the depth axis is one of its several.
- [Security Gap Exponent (δ)](security-gap-exponent.md) — the total-work axis, which sequentiality is not.
- [One-Way Functions](one-way-functions.md)
- [Indistinguishability Obfuscation](indistinguishability-obfuscation.md)
- [Verifiable Computation](verifiable-computation.md)

## Open Questions

- Construct a commutative sequential function, or prove fine-grained NIKE needs more.
- An equivalence between commutative sequential functions and fine-grained NIKE.
- A standard-model sequentiality assumption. Every known one is idealized (generic group, random
  oracle) or needs subexponentially secure iO.
- Whether sequentiality is the right axis for any machine-learning cost claim. Training is
  sequential in epochs but the quantity ML security papers actually measure is aggregate compute,
  which this definition leaves free.
