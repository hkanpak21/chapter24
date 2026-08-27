---
title: Separating Adaptive Streaming from Oblivious Streaming
type: source
date_ingested: 2026-08-21
authors: [Haim Kaplan, Yishay Mansour, Kobbi Nissim, Uri Stemmer]
venue: venue unconfirmed from PDF (arXiv:2101.10836v2 [cs.DS], 17 Feb 2021; recorded elsewhere in this repo as CRYPTO'21)
year: 2021
tags: [adaptive-data-analysis, cryptography, complexity-theory, bounded-storage-model, adaptive-attacks, hardness-reductions]
claim_quantifier: existential
antecedent: "none for Theorem 1.2 and Theorem 5.10, which are information theoretic. The variant in Section 6, described as more natural, yields only a computational separation. The result rests on the Steinke and Ullman adaptive data analysis lower bound for natural algorithms, Theorem 5.6, which is unconditional."
adversary_bound: "none — the bound is on the DEFENDER. The space bound w is on the streaming algorithm. The adaptive Adversary in the streaming game is unrestricted in space and in time. Within the proof the roles invert: the streaming algorithm plays the space-bounded adversary against a bounded storage model pseudorandom generator."
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: mechanism
cls_unit: memory
cls_tightness: exponent
cls_baseline: n/a
cls_baseline_checked: yes
cls_second_party: none
cls_assessed: explicit
cls_evidence: "We present a streaming problem for which every adversarially-robust streaming algorithm must use polynomial space, while there exists a classical (oblivious) streaming algorithm that uses only polylogarithmic space."
cls_evidence_src: abstract
cls_reason: "party=mechanism rather than learner, mirroring the wiki page's own contrast with Raz ('there the learner'); the Adversary in the two-player game is explicitly unrestricted in space and time, so second=none; tightness=exponent records the adaptive-vs-oblivious space gap as the relation to the honest (oblivious) baseline."
cls_prov: S
cls_date: 2026-08-22
---

## Summary

Adversarially robust streaming asks a streaming algorithm to stay accurate when the stream is chosen
adaptively, in response to the algorithm's own outputs. A run of positive results had made robustness look
almost free, with general transformations costing a `sqrt(λ)` factor in space, where `λ` is the flip number
of the problem. This paper gives the first separation. There is a streaming problem solvable obliviously in
`O(log^2 w)` space that requires at least `w` space in the adversarial setting.

The route is a reduction from adaptive data analysis. The first `n` stream updates are read as data points
defining a multiset `S`, and each later bulk of `|X|` updates encodes a query `q` whose empirical average on
`S` the algorithm must report. Two obstacles have to be cleared. The first is that streaming accuracy is
defined against the input sample while adaptive data analysis accuracy is defined against an unknown
distribution. The paper closes this by a compression argument. If the streaming algorithm has small space and
is accurate on the sample, its answers must also generalise to the distribution the sample was drawn from.
Small space forces generalisation.

The second obstacle is that the adaptive data analysis lower bounds hold only against computationally
efficient mechanisms, because their constructions hide query definitions behind an encryption scheme whose
security is computational. Here the paper makes its most instructive move. In this setting the party being
kept in the dark by that encryption is the streaming algorithm, whose storage is already bounded, so the
computational scheme can be swapped for a bounded storage model pseudorandom generator with information
theoretic security. The separation therefore becomes information theoretic. The roles are inverted relative
to the rest of the memory bounded literature. The space bounded party is the defender, and it plays the
adversary in the cryptographic subgame.

The result is nearly tight in the flip number. The constructed problem has flip number `O(w^2)`, so the
`w` space requirement is `Ω(sqrt(λ))`, matching the general transformations of Ben-Eliezer et al., Hassidim
et al. and Woodruff and Zhou up to lower order factors.

## Claim Boundary

- **Quantified over:** existentially in the problem. One streaming problem is constructed, over a domain of
  size `poly(w)` and stream length `O(w^5)`, and the space bound `w` is universal over adversarially robust
  streaming algorithms for that problem at constant accuracy. It is not a statement about frequency moments,
  distinct elements, heavy hitters or any previously studied streaming task.
- **Antecedent:** none for the main separation. The underlying adaptive data analysis lower bound, Theorem
  5.6 quoted from Steinke and Ullman, is unconditional but applies only to *natural* algorithms, Definition
  5.5, which answer identically on queries that agree on every point of the sample. The construction ensures
  the algorithm it builds is natural.
- **Which party carries the resource bound:** the **defender**, the streaming algorithm. The Adversary in the
  two player game of Section 1.1 chooses each update as a function of all previous updates and outputs, and
  no memory or time bound is placed on it. Inside the proof the streaming algorithm is recast as the space
  bounded adversary of Definition 2.6, the bounded storage model pseudorandom generator's security game, so
  the only memory bounded party in the whole construction is the one being attacked.
- **Does not establish:** that robustness is expensive for natural streaming problems. Remark 1.4 says the
  more natural variant in Section 6 yields only a computational separation. It does not improve on the
  `sqrt(λ)` upper bounds, and it does not address adversaries that are themselves resource limited.
- **Abstract versus theorem:** the abstract says the result "resolves one of the central open questions in
  adversarial robust streaming", and Theorem 1.2 and Theorem 5.10 state exactly the claimed parameters. The
  strength of the separation, `polylog` against `poly`, is on a constructed problem, and the paper says so in
  the body rather than in the abstract.

## Key Contributions

- The first separation between oblivious and adversarially robust streaming, `O(log^2 w)` space against `w`.
- A reduction from adaptive data analysis to adversarial streaming, with a compression argument showing that
  small space plus empirical accuracy forces distributional accuracy.
- The substitution of a bounded storage model pseudorandom generator for a computationally secure encryption
  scheme, justified because the party to be fooled is the space bounded streaming algorithm, which upgrades
  the separation from computational to information theoretic.
- Near tightness in the flip number, `Ω(sqrt(λ))`, matching the known general robustness transformations.

## Key Definitions / Theorems

- **The adversarial streaming game, Section 1.1.** In round `i` the Adversary chooses `x_i` depending on all
  previous updates and outputs, and the StreamingAlgorithm processes `x_i` and outputs `z_i`. The Adversary
  wins if some `z_i` falls outside `(1 ± α)·g(x⃗_i)`.
- **Definition 1.3, flip number.** The `(α, m)`-flip number of `g` is the maximal number of times the value
  of `g` can change by a factor of `(1 + α)` during a stream of length `m`.
- **Definition 2.1 and 2.3.** Statistical accuracy of a mechanism is measured against `q_i(D)` and empirical
  accuracy against `q_i(S)`, both for `ℓ` adaptively chosen queries.
- **Definition 2.4, transcript compressibility.** A mechanism is transcript compressible to `b(n, ℓ)` bits if
  for every deterministic adversary the reachable transcripts form a set of size at most `2^{b(n,ℓ)}`.
- **Definition 2.6, bounded storage model pseudorandom generator.** `PRG : {0,1}^a × {0,1}^b → {0,1}^c` is
  `ε`-secure for storage rate `β` if every adversary with storage bound `βa` distinguishes the real from the
  ideal experiment with advantage at most `Tε` over `T` blocks. Past outputs are given to the adversary for
  free, and the key is revealed at the end.
- **Definition 3.1, the SADA problem.** The first `n` updates form a multiset, each later bulk of `|X|`
  updates specifies a query, and the algorithm must report the query's empirical average on the multiset at
  the end of each bulk and zero otherwise.
- **Definition 5.5 and Theorem 5.6.** A *natural* algorithm answers identically on two queries that agree on
  every point of the sample. Steinke and Ullman: there is a constant `c > 0` such that no natural algorithm
  is `(c, c)`-statistically accurate for `O(n^2)` adaptively chosen queries given `n` samples over a domain
  of size `Ω(n)`.
- **Theorem 1.2, restated as Theorem 5.10.** For every `w` there is a streaming problem over a domain of size
  `poly(w)` and stream length `O(w^5)` requiring at least `w` space in the adversarial setting to within
  constant accuracy, solvable obliviously in `O(log^2 w)` space.
- **Theorem 4.1.** The oblivious algorithm for the problem is accurate, which is the upper bound half of the
  separation.

## Connections

- [Bounded Storage Model](../concepts/bounded-storage-model.md) supplies Definition 2.6 and is used here in
  an inverted role, against the defender.
- [On Differential Privacy and Adaptive Data Analysis with Bounded Space](dp-adaptive-analysis-bounded-space.md)
  moves in the opposite direction, from streaming style space bounds back into adaptive data analysis, and
  also places its space bound on the mechanism.
- [Preventing False Discovery in Interactive Data Analysis is Hard](preventing-false-discovery-hard.md) is
  the ancestor of the adaptive data analysis lower bound used here, and is the paper that introduced the
  encryption device that Section 5 replaces with a bounded storage generator.
- [Adaptive Data Analysis](../concepts/adaptive-data-analysis.md).
- [Adaptive Attacks](../concepts/adaptive-attacks.md) is the general phenomenon, an adversary that reacts to
  the defender's own outputs.
- [Raz, Fast Learning Requires Good Memory](raz-parity-time-space.md) is the other place in this corpus where
  a memory bounded party is asked to reconstruct a secret from a stream, there the learner.

## Open Questions / Limitations

- The separating problem is constructed for the purpose. The more natural variant of Section 6 gives only a
  computational separation, which is stated as a limitation in Remark 1.4.
- The stream length `O(w^5)` is large relative to the space bound `w`.
- Nothing here bounds the adaptive adversary's own resources, so the separation says how much space
  robustness costs, not how much an attacker must spend.

## Quotes / Notable Passages

- "We present a streaming problem for which every adversarially-robust streaming algorithm must use
  polynomial space, while there exists a classical (oblivious) streaming algorithm that uses only
  polylogarithmic space."
- "we can replace this encryption scheme with a different scheme with information-theoretic security against
  adversaries with bounded storage capabilities. Indeed, in our setting, the “adversary” for this
  encryption scheme will be the streaming algorithm, whose storage capabilities are bounded."
- "even though we only require the streaming algorithm to give accurate answers w.r.t. the empirical sample,
  we show that if it uses small space complexity then its answers must generalize to the underlying
  distribution."
