---
title: "Fine-Grained Complexity in a World without Cryptography"
type: source
date_ingested: 2026-08-20
authors: [Josh Alman, Yizhi Huang, Kevin Yeo]
venue: "Eurocrypt 2025 (the PDF's own footnote reads \"This is the full version of the paper that appears in the proceedings of Eurocrypt 2025\")"
year: 2025
claim_quantifier: conditional
antecedent: "One-way functions do not exist. Standard as a hypothesis (it is exactly Impagliazzo's Pessiland-or-below condition), but note it is the *negation* of the field's baseline assumption, so the paper is a barrier result rather than a construction."
tags: [cryptography, complexity-theory, one-way-functions, fine-grained-cryptography, average-case-reductions, impagliazzo-worlds, hardness-reductions]
---

## Summary

The barrier result for the whole programme. Fine-grained cryptography's stated hope is to survive in
Pessiland — a world where one-way functions do not exist. This paper shows that in exactly that world,
the average-case hypotheses fine-grained cryptography is built on are **false**.

The mechanism is short. If OWFs do not exist then, via universal one-way functions, every `n^ℓ`-time
length-increasing function can be inverted in `n^{ℓc}` time for a universal constant `c`, for
infinitely many `n` (Lemma 3.1). Any fine-grained problem with a **planting algorithm** — a pair
`(f, g)` where `f` maps randomness to an instance with a solution and `g` maps the same randomness to
that solution — is then solvable on average by inverting `f` and applying `g`. Since `c` does not
depend on `k`, the running time `n^c` does not grow with `k` even though the conjectured hardness
`n^{⌈k/2⌉}` or `n^k` does. So the conjectures break for large enough `k`.

Two further contributions: an equivalence showing that an efficient average-case reduction from
`k`-CYC (or `k`-PROD) to `k`-SUM would yield breakthrough discrete-logarithm algorithms — a barrier
for a reduction fine-grained complexity has been unable to prove — and faster average-case algorithms
for `k`-SUM-Index and `k`-CYC-Index via a reduction from discrete logarithm with preprocessing.

## Claim Boundary

- **Quantified over:** Uniform, possibly randomized algorithms. The results are algorithmic, not
  circuit-based: Lemma 3.1 produces *"a (possibly randomized) algorithm A"*. The failure probability
  bound carries a `2^{2|M|}` term in the code length of the planting algorithm — a constant, but one
  that means the guarantee is only meaningful for planting algorithms of bounded description size.
- **Antecedent:** The non-existence of one-way functions, in the standard sense. Note the asymmetry
  the authors flag in a footnote: the conclusions hold **infinitely often** because *"'one-way
  functions' and 'infinitely often one-way functions' are not known to be equivalent."*
- **Does not establish:** That the average-case conjectures are false for *all* `k`. The abstract is
  precise about this — *"the average-case k-SUM and Zero-k-Clique conjectures are false for
  sufficiently large constant k when no one-way functions exist"* — and the mechanism explains why:
  the algorithm runs in `n^c` for a fixed `c`, which only beats the conjectured `n^{⌈k/2⌉−Θ(1)}` or
  `n^{k−Θ(1)}` once `k` is large. Nor does it establish anything about **worst-case** `k`-SUM or
  Zero-`k`-Clique; the results are entirely average-case, over specified distributions (uniform,
  planted, uniform-with-a-solution, uniform-with-exactly-one-solution), in the `k`-list search
  variants over cyclic groups. And the algorithms work **for infinitely many `n`**, not all `n`.
- **Abstract vs theorem:** None found. The abstract carries the "sufficiently large constant k"
  qualifier; the informal theorems carry "for infinitely many n".

## Key Contributions

- **Theorem 1.1**: if OWFs do not exist, the AVG-`k`-SUM and AVG-Zero-`k`-Clique conjectures are false.
- **Theorems 1.2, 1.3**: the stronger form — a universal constant `c` such that for **all** `k` there
  is an `O(n^c)`-time average-case algorithm, for infinitely many `n`. The exponent does not grow with `k`.
- **Theorem 1.4** (contrapositive): `n^{ω_k(1)}` average-case hardness of `k`-SUM ⟹ one-way functions
  exist. A much weaker hypothesis than the usual `Ω(n^{⌈k/2⌉})` suffices to construct OWFs.
- **Definition 3.2 / Theorem 3.4**: the generalization — the argument works for **any** search problem
  with an almost-good planting algorithm, which is most of average-case fine-grained complexity.
- **Theorem 1.5 / 1.6**: reductions between `k`-CYC/`k`-PROD and `k`-SUM would give discrete-log
  speedups — a cryptographic explanation for a fine-grained barrier.
- **Theorem 1.7**: average-case algorithms for `k`-SUM-Index and `k`-CYC-Index.

## Key Definitions / Theorems

- **Lemma 3.1, verbatim:** *"If one-way functions do not exist, then for any constant d > 0, there
  exists a constant c > 2, such that for any constant ℓ ≥ 2 and any n^ℓ-time (length-increasing)
  Turing machine M where n is the input length, there exists a (possibly randomized) algorithm A such
  that for infinitely many n, Pr x←U({0,1}n) [M(A(1n, M(x))) = M(x)] ≥ 1 − 2^{2|M|}/n^{ℓd}."*
- **Theorem 1.2 (informal), verbatim:** *"If one-way functions do not exist, then there exists a
  universal constant c, such that for all k > 0, there is an O(nc)-time algorithm that solves k-SUM on
  average with inverse polynomial failure probability, for infinitely many n."*
- **Theorem 3.4** generalizes this to any search problem admitting a `β`-almost-good `(·)^ℓ`-time
  planting algorithm.

## Connections

- **The consequence for the batch's flagship construction.** This paper computes, explicitly, the
  damage to [Public-Key Cryptography in the Fine-Grained Setting](pkc-fine-grained-setting.md):
  its key exchange takes `O(n^{k+2})` and is secure against `O(n^{2k−δ})`, so it takes `k` arbitrarily
  large to push the gap toward 2 — *"However, our results show that one cannot pick arbitrarily large
  k, and the gap achievable by their construction must be bounded below 2."* The same paper's
  fine-grained OWF construction *"cannot be secure against n^c-time adversaries"* for the universal `c`.
- **And for the other Zero-`k`-Clique consumer:**
  [Fine-Grained NIKE without Idealized Assumptions](nike-without-idealized-assumptions.md)'s
  bounded-time construction uses the same hypothesis.
- **The complementary paper.** [On Building Fine-Grained One-Way Functions](fine-grained-one-way-functions.md)
  asks whether average-case hardness can *produce* fine-grained OWFs and answers with separations;
  this paper asks whether the average-case hardness is even there in the world where it would matter,
  and answers no for large `k`. Together they close the pincer around Pessiland-resident fine-grained
  crypto.
- [Learning in Pessiland via Inductive Inference](learning-in-pessiland.md) — the learning-side
  treatment of the same world.
- **What the barrier does not reach.** [The Planted Orthogonal Vectors Problem](planted-orthogonal-vectors.md)
  notes that this result *"might be possible to generalize ... to k-OV"*, and argues a `k`-OV-based
  PKE would still be interesting in a world where OWFs do exist, since OWFs are not known to imply
  superquadratic-gap public-key encryption.
- Concepts: [One-Way Functions](../concepts/one-way-functions.md),
  [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md),
  [Average-Case Reductions](../concepts/average-case-reductions.md),
  [Orthogonal Vectors Conjecture](../concepts/orthogonal-vectors-conjecture.md),
  [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md).

## Open Questions / Limitations

- Whether the argument extends to `k`-OV, which has no established planted distribution — the gap
  that [The Planted Orthogonal Vectors Problem](planted-orthogonal-vectors.md) is trying to fill.
- Whether the infinitely-often qualifier can be removed; the authors say it appears necessary given
  that OWFs and i.o.-OWFs are not known to be equivalent.
- The universal constant `c` is not made explicit, so the paper does not say for which `k` the
  conjectures actually break.
- Wagner's algorithm is noted as incomparable: unconditional but with running time `n^{o(k)}` whose
  exponent grows with `k`, versus this paper's `n^c` conditional on no OWFs.

## Quotes / Notable Passages

> "In fact, we prove an even stronger refutation assuming no one-way functions, showing that as k
> grows larger, one can achieve a very fast running time whose exponent does not grow with k at all"

> "Indeed, in a world with cryptography, there is no need for fine-grained cryptography which only
> gives weaker guarantees."

> "Thus, progress on proving these conjectures in fine-grained complexity can be seen as progress on
> establishing the foundations of cryptography."
