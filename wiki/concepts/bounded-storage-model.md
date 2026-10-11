---
title: Bounded Storage Model (BSM)
type: concept
tags: [cryptography, fine-grained-cryptography, complexity-theory, computational-indistinguishability]
---

## Definition

A model, introduced by Maurer, in which the adversary is **computationally unbounded** but its
**storage** is bounded a priori. All parties see a long uniformly random string (a URS or "beacon");
the adversary may apply an arbitrary — possibly unbounded-time — function `f` to it, but may retain
only `m_a` bits. The string then becomes unavailable, and the honest parties, who stored `m_u ≪ m_a`
bits, proceed.

[Wang–Su–Pan–Xu](../sources/nike-without-idealized-assumptions.md) state the security condition in
information-theoretic terms (Definition 2.1): a scheme is `(m_a, ϵ, θ)`-secure in the BSM if there is
an event `E` with `Pr[E] ≥ 1 − ϵ` such that

```
I(key ; (f(urs), (pk_i)_{i∈[n_p]}) | E) ≤ θ
```

for every storage function `f : {0,1}^n → {0,1}^{m_a}`. Note this is **mutual information**, not a
computational indistinguishability game — the guarantee is unconditional.

## Intuition

This is [Fine-Grained Cryptography](fine-grained-cryptography.md) on the **memory** axis, and the one
axis where unconditional security has been routine for decades. Cachin and Maurer got symmetric-key
encryption and key exchange with honest storage `O(s)` against adversary storage `o(s^2)` — the same
quadratic shape as Merkle puzzles, on a different resource.

## Properties / Theorems

- **Multi-party generalization and its exponent.**
  [Wang et al.](../sources/nike-without-idealized-assumptions.md) build an unconditionally secure
  `n_p`-party NIKE where each user stores `m_u = O((λ·m_a^{n_p−1})^{1/n_p})` bits against an adversary
  storing `m_a`, with total communication `O(λ)`. So `m_a ≈ m_u^{n_p/(n_p−1)}` — the storage gap
  exponent **shrinks as the party count grows**, the same structural pattern that appears in the ROM
  `K`-NIKE gap `n^{K/(K−1)}` of [Afshar et al.](../sources/fine-grained-nike-lower-bounds.md).
- **The storage lower bound.** Wang et al.'s Theorem 5.15 generalizes Dziembowski–Maurer's two-party
  bound to any multi-party NIKE with *restricted extendability*: `H(key) ≤ m_u^{n_p}/m_a^{n_p−1} + …`,
  proved by induction, by treating "combine a subgroup's local key with a new public key" as a
  two-party exchange between the subgroup and the newcomer. This makes their construction's user
  memory optimal — but only within the class of extendable schemes.
- **Two BSMs.** The traditional Maurer BSM (one URS, then it disappears) and the *streaming* BSM of
  Dodis–Quach–Wichs (parties may communicate interactively with multiple rounds of long messages) are
  different models with different achievable bounds. Wang et al. work in the traditional one and say so.
- **Adjacent in this repo but on the other side of the game.** Raz's time-space lower bound for parity
  learning, and the Guan–Zhandry and Dodis–Quach–Wichs BSM lines, put the memory bound on the
  *learner*, the *mechanism*, or the *defender*. No source in this wiki puts a memory bound on an
  **ML privacy adversary** (see `raw/SOURCES.md`, "Memory- and space-bounded adversaries").

## Where It Appears

- [Fine-Grained NIKE without Idealized Assumptions](../sources/nike-without-idealized-assumptions.md) — §5, the construction and the lower bound.
- [Fine-grained Cryptography](../sources/fine-grained-cryptography.md) — §1.2 surveys the model as one of the three fine-grained axes alongside time and parallel time.

## Related Concepts

- [Fine-Grained Cryptography](fine-grained-cryptography.md)
- [Security Gap Exponent (δ)](security-gap-exponent.md)
- [Sequential Functions](sequential-functions.md)
- [Computational Indistinguishability](computational-indistinguishability.md) — deliberately *not* what
  BSM security is stated in; the BSM guarantee is information-theoretic.

## Open Questions

- Super-constant party counts. Wang et al. note their BSM results do not extend there.
- Whether the extendability restriction in the lower bound can be dropped.
- Whether a memory-bounded **adversary** can be made the subject of a machine-learning privacy
  definition. Every treatment found so far bounds the memory of the learner or the mechanism instead.
