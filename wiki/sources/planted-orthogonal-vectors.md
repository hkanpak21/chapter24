---
title: "The Planted Orthogonal Vectors Problem"
type: source
date_ingested: 2026-08-20
authors: [David Kühnemann, Adam Polak, Alon Rosen]
venue: "venue unconfirmed from PDF (the PDF is arXiv:2505.00206v2, 14 Sep 2025)"
year: 2025
claim_quantifier: conditional
antecedent: "For the search-to-decision reductions: the existence of a decision algorithm for planted k-OV with success probability 1 − δ(n). The average-case hardness of the planted distribution itself is Conjecture 10 — CONJECTURED, NOT PROVED."
tags: [complexity-theory, average-case-reductions, fine-grained-cryptography, hardness-reductions, statistical-computational-gaps, planted-clique]
---

## Summary

`k`-OV is the fine-grained problem whose *worst-case* hardness is best understood, because SETH
implies it. It is also the one with no usable *planted* distribution — and average-case hardness with
an efficiently samplable, solution-known distribution is what cryptography needs. This paper supplies
a planting procedure and conjectures that it is hard.

The construction is a `p`-biased planting with a specific property. Entries are i.i.d. `p`-biased with
`p = p(n) = o(1)`, chosen so instances are non-trivial in the superlogarithmic dimension regime
`d = ω(log n)` — deliberately, because Kane and Williams solve `k`-OV with fixed-constant-`p` i.i.d.
entries in `O(n^{k−ε_p})` time by `AC0` circuits, and those instances are only non-trivial at
`d = Θ(log n)` where subquadratic algorithms exist anyway. The planted `k` vectors are sampled so that
**any `k−1` of them have exactly the marginal distribution of `k−1` fresh i.i.d. `p`-biased vectors** —
`(k−1)`-wise independence. That is what defeats the Kane-Williams idea, which exploits the fact that
vectors conditioned on orthogonality are sparser than typical. Theorem 7 shows this is the *unique*
distribution with that property, which is where the title comes from.

The `(k−1)`-wise independence is then put to work: two **search-to-decision reductions**. Resample a
subset of the input vectors; if any planted vector was resampled the instance is exactly
model-distributed, so a decision oracle tells you whether the planted solution survived. One reduction
does binary search (`O(log n)` overhead in both time and failure probability); the other, adapted from
Agrawal et al. for planted `k`-SUM, uses survival counters and loses only a constant factor in failure
probability.

## Claim Boundary

- **Quantified over:** Ordinary uniform algorithms with a stated success probability. Conjecture 10
  quantifies over algorithms solving the **decision** problem with *any constant* success probability
  `δ > 1/2` in time `O(n^{k−ε})`. Definitions 8 and 9 take the probability over both the instance and
  the algorithm's coins. No circuit, non-uniform, or query-complexity statement appears.
- **Antecedent:** This is the critical point. **The average-case hardness is a conjecture, not a
  theorem.** Conjecture 10 has no proof, no worst-case-to-average-case reduction behind it, and the
  authors invite refutation: *"We would even be happy to see our conjecture refuted."* What is
  *proved* here is (a) the planting procedure and its `(k−1)`-wise independence, (b) uniqueness of the
  distribution with that property, and (c) the two search-to-decision reductions, which are
  conditional on the existence of a good decision algorithm.
- **Does not establish:** Any hardness. Nor any cryptographic construction — the paper reports that
  the LaVigne-Lincoln-Vassilevska Williams key exchange *"can be adapted to work with our planted
  k-OV instead of the planted Zero-k-Clique problem, but naturally the protocol's security remains
  quadratic."* The stated motivation is superquadratic security, and this paper does not reach it.
  Both search-to-decision reductions also degrade the failure probability, so neither yields
  hardness amplification.
- **Abstract vs theorem:** None found. The abstract says *"Our conjecture is that the resulting k-OV
  instances still require time n^{k−o(1)} to solve, on average"* — flagged as a conjecture in the
  abstract itself.

## Key Contributions

- **The planting procedure** (§3): a joint distribution on `k` bits per coordinate with `Pr[1^k] = 0`
  and `(k−1)`-wise `p`-biased marginals, sampled by drawing `k−1` i.i.d. `p`-biased bits and then the
  `k`-th conditionally on their weight.
- **Theorem 7**: uniqueness — this is the only distribution over `k`-OV instances with the
  `(k−1)`-wise independence property.
- **Conjecture 10**: the average-case hardness conjecture the paper is built around.
- **Theorem 11**: search-to-decision by binary search, success `1 − k⌈log n⌉·δ(n)`, expected time `Õ(T(n) + n)`.
- **Theorem 12**: search-to-decision by counters, success `1 − 13k·δ(n) − n/n^k`, expected time
  `O(T(n) + n polylog(n) log(1/δ(n)))`.
- Multi-solution planting, argued to follow from `(k−1)`-wise independence and suggested as useful for
  cryptographic primitives.
- The design rationale against the Kane-Williams `AC0` algorithm and against Alman-Andoni-Zhang.

## Key Definitions / Theorems

- **Conjecture 10, verbatim:** *"For any α(n) = ω(1) and ε > 0, there exists no algorithm A that
  solves the planted decision k-OV problem with any constant success probability δ > 1/2 in time
  O(n^{k−ε})."*
- **Definition 8 / 9**: the decision and search success-probability conventions, with randomness over
  instance and coins.
- **Theorem 12, verbatim:** *"For any α(n) = polylog(n), if there exists an algorithm that solves the
  planted decision k-OV problem with success probability at least 1 − δ(n) in time T(n), then there
  exists an algorithm that solves the planted search k-OV problem with success probability at least
  1 − 13k · δ(n) − n/n^k in expected time O(T(n) + n polylog(n) log(1/δ(n)))."*

## Connections

- **The missing piece for two constructions in this corpus.**
  [Public-Key Cryptography in the Fine-Grained Setting](pkc-fine-grained-setting.md) needs a plantable,
  splittable, list-hard problem and uses Zero-`k`-Clique;
  [Towards Permissionless Consensus](permissionless-consensus-fine-grained.md) uses worst-case `k`-OV
  and never needs an average-case OV distribution. This paper is the attempt to give `k`-OV the
  average-case status that Zero-`k`-Clique already has.
- **The other half of the average-case OV question.**
  [Average-Case Hardness of Parity Problems](average-case-parity-problems.md) *proves* average-case
  hardness for parity-`k`-OV, conditioned on worst-case hypotheses, but at a degraded exponent
  (`N^{Ω(√K)}`) and only against near-perfect algorithms. This paper *conjectures* full `n^{k−o(1)}`
  hardness for search and decision. Between them: proved-but-weak versus strong-but-conjectured.
- **The barrier that may reach here too.**
  [Fine-Grained Complexity in a World without Cryptography](fine-grained-world-without-crypto.md) is
  cited in §1.4 with the observation that *"It might be possible to generalize their results to
  k-OV"* — and the authors' answer is that a `k`-OV-based PKE would be interesting anyway, since OWFs
  are not known to imply superquadratic-gap public-key encryption (they cite Impagliazzo-Rudich).
- **Hardness self-amplification** is the paper's first open problem, citing Hirahara-Shimizu's
  planted-clique self-amplification (STOC 2023). This wiki holds the adjacent Hirahara-Shimizu result
  on [Planted Clique Conjectures are Equivalent](hirahara-planted-clique-conjectures-equivalent.md) —
  a different paper by the same pair, on the problem that is `k`-OV's model organism.
- Compare the planted-clique-to-cryptography line:
  [Cryptography from Planted Graphs](cryptography-from-planted-graphs.md),
  [PKE from Planted Clique](pke-from-planted-clique.md),
  [Public-Key Cryptography from Different Assumptions](pkc-from-different-assumptions.md).
- Concepts: [Orthogonal Vectors Conjecture](../concepts/orthogonal-vectors-conjecture.md),
  [Planted Clique](../concepts/planted-clique.md),
  [Average-Case Reductions](../concepts/average-case-reductions.md),
  [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md).

## Open Questions / Limitations

The paper's own list, which doubles as its limitation list:
- **Hardness self-amplification** for planted `k`-OV — without it, both search-to-decision reductions
  degrade the failure probability and no low-advantage hardness follows.
- **Fine-grained asymmetric cryptography with superquadratic security**, which the authors name as the
  key goal and do not achieve; they believe `k`-OV's non-additive structure is the reason to try.
- **Faster average-case OV algorithms** — the authors analyse why the Alman-Andoni-Zhang algorithm
  does not obviously adapt (the key quantity, the expected inner product `p^2 d`, is `Θ(log n)` in
  both settings) and say refuting the conjecture likely needs new technique.
- **A worst-case-to-average-case reduction** from SETH or similar to this distribution.
- A cautionary contrast the authors raise themselves: the closely related *light bulb* problem
  (planted approximate maximum inner product) **does** admit truly subquadratic `O(n^{1.582})`
  algorithms, even though the two are worst-case equivalent under fine-grained reductions.

## Quotes / Notable Passages

> "We propose a way to plant a solution among vectors with i.i.d. p-biased entries, for appropriately
> chosen p, so that the planted solution is the unique one. Our conjecture is that the resulting k-OV
> instances still require time n^{k−o(1)} to solve, on average."

> "We would even be happy to see our conjecture refuted."

> "This limitation seems inherent to the protocol because it is based on a similar idea as Merkle puzzles."
