---
title: Orthogonal Vectors Conjecture (OVC / k-OVC)
type: concept
tags: [complexity-theory, fine-grained-cryptography, hardness-reductions, average-case-reductions]
---

## Definition

**`k`-Orthogonal Vectors (`k`-OV).** Given `k` sets of `n` binary vectors of dimension `d`, decide
whether one vector can be picked from each set so that at every coordinate at least one of them is
zero (equivalently, the coordinatewise product of the `k` vectors is the all-zero vector). `2`-OV is
OV. The naive algorithm runs in `O(n^k d)`.

**The conjectures**, verbatim from
[Ball–Garay–Hall–Kiayias–Panagiotakos](../sources/permissionless-consensus-fine-grained.md):

> "Conjecture 1 (Orthogonal Vectors Conjecture (OVC)). For all ε > 0, there exists c ≥ 1 such that OV
> requires n^{2−ε} time on instances with d = c log n."

> "Conjecture 3 (k-Orthogonal Vectors Conjecture (kOVC)). For all ε > 0, there exists c ≥ 1 such that
> kOV requires n^{k−ε} time."

Both are **worst-case** conjectures — the paper flags this explicitly — and both are implied by SETH.
The converse is not known.

## Intuition

`k`-OV is fine-grained complexity's best-understood hard problem, because its worst-case hardness
follows from SETH, which is about the very well studied SAT problem. Kühnemann–Polak–Rosen put the
motivation for cryptographers plainly: the field wants to base security on problems whose hardness has
been studied for decades, and OV is the one of the three core problems (OV, 3SUM, APSP) whose
hardness is understood best.

The regime matters. For `d = c log n` with `c` fixed, Abboud et al. and Chan–Williams solve OV in
`O(n^{2−ε_c})`; the conjecture bites only at superlogarithmic dimension `d = ω(log n)`. Any
average-case construction has to place itself in the `d = ω(log n)` regime to say anything non-trivial.

## Properties / Theorems

- **The worst-case route to cryptography, and its barrier.** Ball–Rosen–Sabin–Vasudevan built
  fine-grained proofs of work from worst-case OV via an arithmetized low-degree polynomial `FOV_k`
  counting orthogonal pairs, plus Berlekamp–Welch. Pushing that further to fine-grained one-way
  functions would **falsify NSETH**, as reported in
  [LaVigne et al.](../sources/pkc-fine-grained-setting.md), which is why that paper switched to an
  average-case Zero-`k`-Clique hypothesis instead.
- **The two primitives known from worst-case fine-grained assumptions** are proofs of work and
  permissionless consensus, both from OV.
  [Alman–Huang–Yeo](../sources/fine-grained-world-without-crypto.md) state this inventory.
- **Robust direct sum.** [Ball et al.](../sources/permissionless-consensus-fine-grained.md) prove that
  under `k`OVC, no algorithm running in `ℓ·n^{2−ε}` given `m` random `FOV_k` inputs evaluates `ℓ` of
  them with probability `1/n^{o(1)}` — and, crucially, that this survives when the `m` instances are
  drawn from a joint pseudorandom distribution of only `Õ(m^{1/k}n)` bits of entropy. That
  derandomization is what makes a short-seed proof of work possible.
- **Average-case status is the open frontier.**
  [Dalirrooyfard et al.](../sources/average-case-parity-problems.md) prove average-case hardness for
  **parity-`k`-OV** on constructed distributions, at exponent `N^{Ω(√K)}` under rETH — degraded from
  the worst-case `N^{Θ(K)}` — and only against algorithms succeeding with probability `1 − Θ(1/2^K)`.
  [Kühnemann–Polak–Rosen](../sources/planted-orthogonal-vectors.md) supply a planted distribution and
  **conjecture** `n^{k−o(1)}` average-case hardness for search and decision, without proof.
- **`k`-OV resists one known attack by construction.** Kane and Williams solve `k`-OV with i.i.d.
  `p`-biased entries at fixed constant `p` in `O(n^{k−ε_p})` by `AC0` circuits, exploiting the fact
  that vectors conditioned on orthogonality are sparser than typical. The planted distribution of
  Kühnemann–Polak–Rosen has `(k−1)`-wise independent marginals precisely to remove that sparsity signal.
- **What OV does not yet have** that Zero-`k`-Clique does: a plantable, splittable, average-case
  list-hard package usable in a key exchange. That is the gap KPR25 is trying to close.

## Where It Appears

- [Towards Permissionless Consensus in the Standard Model via Fine-Grained Complexity](../sources/permissionless-consensus-fine-grained.md) — worst-case `k`OVC as the sole hardness source.
- [The Planted Orthogonal Vectors Problem](../sources/planted-orthogonal-vectors.md) — the planted distribution.
- [Average-Case Hardness of Parity Problems](../sources/average-case-parity-problems.md) — proved average-case hardness for the parity variant.
- [Public-Key Cryptography in the Fine-Grained Setting](../sources/pkc-fine-grained-setting.md) — reports the NSETH barrier on the OV route.
- [On Building Fine-Grained One-Way Functions](../sources/fine-grained-one-way-functions.md) — describes the BRSV OV construction as the motivating "stuck" path.
- [Fine-Grained Complexity in a World without Cryptography](../sources/fine-grained-world-without-crypto.md) — the OV-based primitives inventory.

## Related Concepts

- [Fine-Grained Cryptography](fine-grained-cryptography.md)
- [Security Gap Exponent (δ)](security-gap-exponent.md)
- [Average-Case Reductions](average-case-reductions.md)
- [Planted Clique](planted-clique.md) — the same worst-case-to-average-case-to-cryptography arc, on a
  problem family that is much further along.
- [Statistical-Computational Gaps](statistical-computational-gaps.md)

## Open Questions

- A worst-case-to-average-case reduction to a *planted* `k`-OV distribution.
- Whether the parity results extend to detection or search.
- Whether the Alman–Huang–Yeo Pessiland barrier generalizes from `k`-SUM and Zero-`k`-Clique to `k`-OV;
  KPR25 suspect it does.
- Whether `k`-OV's non-additive structure can break the quadratic gap barrier that the addition-based
  problems inherit from Merkle puzzles. KPR25 believe so; nobody has shown it.
