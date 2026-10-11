---
title: "Security Gap Exponent (δ)"
type: concept
tags: [cryptography, fine-grained-cryptography, complexity-theory, one-way-functions, hardness-reductions]
---

> **Slug note.** Requested as `the-gap-delta`; filed under `security-gap-exponent` because the object
> is the exponent separating honest cost from adversary cost, and because two incompatible `δ`
> conventions live here.

## Definition

The quantity that makes fine-grained cryptography quantitative: the exponent by which an adversary's
budget exceeds the honest party's. Two papers in this repo define it, and **they do not define the
same number.**

### Convention A — Brzuska–Couteau, `honest^{1+δ}`, circuit size

[On Building Fine-Grained One-Way Functions](../sources/fine-grained-one-way-functions.md),
Definition 6, verbatim:

> "Let ε : N 7→ R+ be a positive function and δ > 0 be a constant. A function f : {0, 1}∗ → {0, 1}∗
> is an (ε, δ)-fine-grained one-way function if for all circuit families C = {Cm}m∈N and all large
> enough m, if |Cm| < |fm|^{1+δ}, then we have Prz←${0,1}m [Cm(f(z), 1m) ∈ f−1(f(z))] ≤ ε(m)."

The honest cost is fixed by the sentence preceding it: the function is a circuit family `{f_m}` *"so
that the runtime of `f_m` is `|f_m|`"*. So `δ` is measured against the **honest function's own circuit
size**, and the adversary is a **non-uniform circuit family**. `δ = 1` is a quadratic gap.

### Convention B — LaVigne–Lincoln–Vassilevska Williams, `T^{1−δ}` vs `T`, word-RAM time

[Public-Key Cryptography in the Fine-Grained Setting](../sources/pkc-fine-grained-setting.md),
Definition 5, verbatim:

> "The (relative) gap of an T(n) fine-grained one-way function f is the constant δ > 0 such that it
> takes T(n)^{1−δ} to compute f but for all PFTT(n) adversaries A, Pr x←{0,1}n [A(f(x)) ∈ f−1(f(x))]
> ≤ insig(n)."

with the adversary class fixed by Definition 1, verbatim:

> "An algorithm A is an T(n) probabilistic fine-grained time, PFTT(n), algorithm if there exists a
> constant δ > 0 such that A runs in time O(T(n)^{1−δ})."

Here `T(n)` is the *inversion-time* threshold, the honest party is discounted below it to `T^{1−δ}`,
and security must hold against every algorithm running in `T^{1−δ'}` for any `δ' > 0` — i.e. against
anything below `T` by a polynomial factor. `δ = 1/2` is a quadratic gap.

> **Transcription note.** Quotes are taken from `pdftotext` output, which flattens superscripts
> and drops large delimiters. Exponents are restored (`|fm|^{1+δ}`, `T(n)^{1−δ}`) because dropping
> them changes the mathematics; no wording is altered.

## Why they are not interchangeable

**Numerically.** Write `H` for the honest cost. Convention A puts the adversary at `H^{1+δ_A}`.
Convention B puts the honest party at `T^{1−δ_B}`, so `H = T^{1−δ_B}` and the threshold is
`T = H^{1/(1−δ_B)}`. Equating,

```
1 + δ_A = 1/(1 − δ_B)      δ_A = δ_B/(1 − δ_B)      δ_B = δ_A/(1 + δ_A)
```

Check: a quadratic gap is `δ_A = 1` and `δ_B = 1/2`. A citation that carries a `δ` across the two
papers without this conversion is wrong by a factor that grows as the gap grows.

**Structurally, and this matters more.** Even at matched numeric gap the two definitions price
different things:

| | Convention A (BC22 Def 6) | Convention B (LLV19 Def 5) |
|---|---|---|
| resource | circuit **size** (number of wires) | **running time**, word-RAM |
| adversary | **non-uniform** circuit family | **uniform, probabilistic** algorithm |
| baseline | the honest function's own size `\|f_m\|` | an externally fixed threshold `T(n)` |
| quadratic gap | `δ = 1` | `δ = 1/2` |
| success bound | `ε(m)`, a separate parameter | `insig(n)`, folded into the definition |

A non-uniform circuit-size bound and a uniform time bound are not comparable in either direction
without further argument. Convention A's `δ` is also *self-referential* — the honest object supplies
its own baseline — while Convention B's `T` is an external parameter that the honest algorithm is
then required to beat.

LLV19 additionally **reuses the symbol `δ`** for two different local variables: in Definition 5 it is
the honest party's discount below `T`; in Definition 1 it is the adversary's. Only the first is "the gap".

## Intuition

Standard cryptography asks for a *superpolynomial* separation and can therefore be sloppy about
polynomial factors — a Goldreich-Levin reduction losing `Ω(N)` calls is free. Fine-grained
cryptography asks for a *fixed polynomial* separation, so every polynomial factor is charged against
the gap. LLV19 makes the consequence explicit: *"in the fine-grained setting, factors of N can
completely eliminate the gap between computation and inversion."* This is why fine-grained papers
must state their machine model and their unit precisely, and why the two conventions here diverged.

## Properties / Theorems

- **The quadratic ceiling, and where it does and does not hold.** Merkle's protocol and its
  descendants stop at quadratic. In **Maurer's** generic group model, 3-NIKE is capped at `O(n^2)`
  *queries* — [Afshar et al. Theorem 21](../sources/fine-grained-nike-lower-bounds.md). This is not a
  universal law: it is one model, one primitive, one cost measure.
- **Gaps that shrink with a parameter.** Three independent constructions in this repo have a gap
  exponent that *decays* as the protocol scales up: the ROM `K`-NIKE gap `n^{K/(K−1)}`
  ([Afshar et al.](../sources/fine-grained-nike-lower-bounds.md)); the bounded-time `n_p`-NIKE, honest
  `Õ(λ^{n_p+k−1})` against adversary `Õ(λ^{n_p+k})`; and the bounded-storage `n_p`-NIKE, user memory
  `O((λ·m_a^{n_p−1})^{1/n_p})` — the last two both from
  [Wang et al.](../sources/nike-without-idealized-assumptions.md). More parties costs gap.
- **A gap that grows with a parameter.** LLV19 §6 reaches `N` to `N^{2−4/(k+2)}`, approaching but
  never reaching quadratic as `k` grows. But
  [Alman–Huang–Yeo](../sources/fine-grained-world-without-crypto.md) show `k` cannot be taken
  arbitrarily large in a world without one-way functions, so *"the gap achievable by their
  construction must be bounded below 2."*
- **Advantage cannot be negligible in `n`.** In the fine-grained setting the adversary can always
  guess a solution, so LLV19 notes the advantage is bounded below by `1/poly(n)`; BCS24's Remark 6
  makes the same point for its standard-model 4-NIKE — *"as a function of N, this advantage is never
  negligible"* — and conjectures amplification is impossible.

## Where It Appears

- [On Building Fine-Grained One-Way Functions](../sources/fine-grained-one-way-functions.md) — Convention A.
- [Public-Key Cryptography in the Fine-Grained Setting](../sources/pkc-fine-grained-setting.md) — Convention B.
- [Fine-Grained NIKE: Constructions and Lower Bounds](../sources/fine-grained-nike-lower-bounds.md) —
  a third unit again: **oracle queries**, substituted for time by fiat in idealized models.
- [Towards Permissionless Consensus](../sources/permissionless-consensus-fine-grained.md) — a fourth:
  aggregate honest-versus-adversarial **computational power per round**.
- [Fine-Grained NIKE, Revisited](../sources/fine-grained-nike-revisited.md),
  [Fine-Grained NIKE without Idealized Assumptions](../sources/nike-without-idealized-assumptions.md).
- [Proof-of-Learning](../sources/proof-of-learning.md) — the ML side of the same quantity, as a bare
  inequality between expected costs, with no exponent, no adversary class, and no theorem.

## Related Concepts

- [Fine-Grained Cryptography](fine-grained-cryptography.md) — the family of restrictions of which this
  exponent is one; the class-based alternative is the other.
- [Sequential Functions](sequential-functions.md) — the same idea on the depth axis.
- [Bounded Storage Model](bounded-storage-model.md) — the same idea on the memory axis.
- [One-Way Functions](one-way-functions.md).

## Open Questions

- Nothing in this repo prices an **ML attacker** against an **ML trainer** in a single exponent, with a
  stated adversary class, inside a security definition. The machinery here is off-the-shelf; what is
  missing on the ML side is a theorem at a stated `δ`, not another definition.
- Whether superquadratic gaps are achievable at all for public-key primitives outside idealized
  models; named as the open problem by
  [The Planted Orthogonal Vectors Problem](../sources/planted-orthogonal-vectors.md).
