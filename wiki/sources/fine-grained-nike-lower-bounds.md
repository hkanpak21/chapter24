---
title: "Fine-Grained Non-Interactive Key-Exchange: Constructions and Lower Bounds"
type: source
date_ingested: 2026-08-20
authors: [Abtin Afshar, Geoffroy Couteau, Mohammad Mahmoody, Elahe Sadeghi]
venue: "venue unconfirmed from PDF (no venue line). BCS24 and WSPX24, both read in this corpus, cite it as EUROCRYPT 2023"
year: 2023
claim_quantifier: existential
antecedent: "None in the usual sense — no computational assumption. Instead the results hold in idealized models: the random oracle model, Shoup's generic group model, and (for the lower bound) Maurer's generic group model. The idealized model IS the antecedent."
tags: [cryptography, fine-grained-cryptography, key-exchange, lower-bounds, complexity-theory, generic-group-model]
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: attacker
cls_unit: queries
cls_tightness: exponent
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: queries
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "the honest parties ask n queries each, while the adversary needs n^{K/(K−1)} queries to the random oracle to find the key"
cls_evidence_src: abstract
cls_reason: "Classified on the ROM K-NIKE construction (Thm 6), the first result the abstract leads with, per rule 1; the Shoup-GGM and Maurer-GGM results are secondary claims in the same paper. Both honest parties and the adversary are bounded in the same resource (oracle queries, not time, per Definition 2's idealized-model convention: 'we primarily count the number of oracle queries as the substitute for running time'), so rule 4's tie-break gives party=attacker; tightness=exponent because n^{K/(K-1)} is a stated relation to the honest parties' own n queries, not a time bound."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

Three results on `K`-party non-interactive key exchange when the adversary's budget is a fixed
polynomial in the honest parties'. The paper matters to the survey mainly for its **ceiling**.

First, Merkle's two-party protocol generalizes to `K` parties in the random oracle model: set the
oracle domain to `n^{1+1/(K−1)}`, have all `K` parties send `n log n` hashes, and take `K`-way
collisions. Honest parties make `n` queries; the adversary needs `n^{1+1/(K−1)} = n^{K/(K−1)}`.
**The gap shrinks as `K` grows** — `n^{1.5}` at `K = 3`, tending to `n^{1+o(1)}` for large `K`. It is
not quadratic in general, and the paper says so: *"even though security against n^{1+1/(K−1)−ε}-query
adversaries gets worse as K grows, for every constant K, it still shows a polynomial gap."*

Second, adding algebraic structure recovers the quadratic gap for four parties: a 4-NIKE in **Shoup's**
generic group model secure against `o(n^2)`-query adversaries, generalizing to `2K`-NIKE in the
generic `(K−1)`-linear group model, hence a 6-NIKE with near-quadratic hardness in the generic
bilinear group model.

Third, the ceiling: **any** 3-NIKE protocol in **Maurer's** generic group model where the honest
parties make `n` queries can be broken with `O(n^2)` queries (Theorem 21). Since a 3-NIKE implies a
`K`-NIKE for `K ≥ 3`, this caps purely algebraic multiparty NIKE at quadratic in that model. The
`O(n^2)` figure is specifically 3-NIKE in Maurer's model — not a general quadratic law.

## Claim Boundary

- **Quantified over:** **Query complexity in idealized models**, throughout. Definition 2 is explicit:
  *"When the protocol is in an idealized model, we use the number of queries by the algorithms to the
  oracle as the measure of their running time."* The positive results count random-oracle queries
  (Theorem 6) or Shoup-GGM queries (Theorem 10). The negative result counts Maurer-GGM `Add`, `Equal`
  and `Zero` queries; Theorem 21 bounds the attacker at `poly(λ)` total oracle queries with the
  quadratic figure arising in the Corollary as `O(γβ/δ') + O(α)`. **None of these is a time bound.**
  The attacker of Theorem 21 is not claimed to run in `O(n^2)` *time* — only to make `O(n^2)` queries.
- **Antecedent:** No computational assumption anywhere. The idealized model is the assumption, and
  the paper is careful about which one: the positive 4-NIKE is in **Shoup's** GGM (labels are visible,
  which implies a random oracle) while the impossibility is in **Maurer's** GGM (no labels, equality
  only by query), which is the weaker model for both parties. The authors state the consequence
  themselves: *"this leaves a gap between our positive and negative results."*
- **Does not establish:** A standard-model construction, a time-complexity lower bound, or a general
  quadratic ceiling. It also does not establish impossibility in Shoup's GGM. The paper flags that
  *"negative results in the MGGM are generally weaker than those in the SGGM and should be
  interpreted cautiously"*, citing Zhandry. The Corollary's quadratic attack succeeds with
  probability `≥ 0.95` on protocols whose honest completeness is `≥ 0.99` — it is not a
  probability-1 break.
- **Abstract vs theorem:** None found. The abstract states the `n^{K/(K−1)}` figure, names Shoup's
  and Maurer's models by name, and says the Maurer result is proved for `K = 3` and extends upward.

## Key Contributions

- **Definition 2**, `(t, ε)`-secure `K`-NIKE: honest parties in `Õ(n)`, adversary limited to `t(n)`,
  advantage `ε(n)` — with the explicit note that queries substitute for time in idealized models.
- **Theorem 6**: Construction 5 is a `(t, ε)` 3-NIKE with `t = n^{1.5}`, `ε = negl(n)`, in the ROM;
  generalizes to `K` parties at `n^{K/(K−1)}`.
- **Theorem 10**: 4-NIKE in Shoup's GGM; a `q`-query generic adversary succeeds with probability
  `O(q^2/λ^4 + q/λ^2 + polylog(λ)/λ)`.
- **Theorem 20**: `O(α)`-query break of MGGM 3-NIKE without `Equal`/`Zero` queries.
- **Theorem 21** and its Corollary: the `O(n^2)`-query break of general MGGM 3-NIKE — the first
  polynomial-query break of 3-NIKE in Maurer's model.
- Lemma 17 (group element structure in MGGM) and Lemma 19 (randomness switching), the machinery
  behind the attack.

## Key Definitions / Theorems

- **Theorem 6.** *"Construction 5 is a (t, ε) 3-NIKE, where t = n^{1.5}, ε = negl(n)."*
- **Theorem 21, verbatim:** *"Suppose Π is a 3-NIKE protocol in the MGGM with parameters α, β, γ ≤
  poly(λ) and completeness error δ (see Definition 14). Then, there is an adversary who, given the
  transcript tran and oracle access to the 3γ broadcast group elements finds Alice's key with
  probability 1 − 4δ − δ′ by asking poly(λ) queries to its MGGM oracle. In particular, E will ask an
  expected number of O(γβ/δ′) Zero queries and O(α) Add queries."*
- **Corollary (quadratic attack in MGGM):** *"If honest parities ask n parties to their oracle and
  agree on a key with probability ≥ 0.99, then we have α, β, γ ≤ n. In this case, E can choose
  δ′ = 0.01, and so it can find Alice's key with probability at least 0.95 by asking O(n^2) queries in
  total."*

## Connections

- **The shrinking-exponent pattern.** The ROM gap `n^{K/(K−1)}` decays with the party count. The same
  shape appears independently in
  [Fine-Grained NIKE without Idealized Assumptions](nike-without-idealized-assumptions.md): its
  bounded-time NIKE is honest `Õ(λ^{n_p+k−1})` against adversary `Õ(λ^{n_p+k})`, a relative exponent
  of `1/(n_p+k−1)`, and its bounded-storage NIKE has user memory `mu = O((λ·ma^{n_p−1})^{1/n_p})`,
  a relative exponent of `1/n_p`. Adding parties buys parties and costs gap.
- **Direct successor.** [Fine-Grained NIKE, Revisited](fine-grained-nike-revisited.md) removes the
  idealization from the positive result (standard model, quadratic gap, from injective PRGs and
  sub-exponential CDH) and pushes the Maurer-model construction to `N^{1.6}`, narrowing but not
  closing the gap this paper left.
- **The other successor.** [Fine-Grained NIKE without Idealized Assumptions](nike-without-idealized-assumptions.md)
  answers the same open question by changing the resource axis rather than the assumption.
- Cites [On Building Fine-Grained One-Way Functions](fine-grained-one-way-functions.md) as one of the
  field's two lower-bound results, and
  [Fine-Grained Cryptography](fine-grained-cryptography.md) for the depth-restricted branch.
- Concepts: [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md),
  [Security Gap Exponent (δ)](../concepts/security-gap-exponent.md),
  [Computational Indistinguishability](../concepts/computational-indistinguishability.md).

## Open Questions / Limitations

- Closing the Shoup/Maurer gap, either by a 4-NIKE with quadratic security in Maurer's model or by
  extending the impossibility to Shoup's — the paper's own stated open question. Partly addressed by
  [Fine-Grained NIKE, Revisited](fine-grained-nike-revisited.md).
- Whether any of this survives outside idealized models — addressed by both successors.
- The ROM construction's gap is not tunable upward: more parties strictly costs gap.

## Quotes / Notable Passages

> "we show how to generalize Merkle's two-party protocol to K parties in such a way that the honest
> parties ask n queries each, while the adversary needs n^{K/(K−1)} queries to the random oracle to
> find the key."

> "In this model, we primarily count the number of oracle queries as the substitute for 'running time.'"
