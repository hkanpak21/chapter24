---
title: "Fine-Grained Non-Interactive Key-Exchange without Idealized Assumptions, and Lower Bounds"
type: source
date_ingested: 2026-08-20
authors: [Yuyu Wang, Chuanjie Su, Jiaxin Pan, Chunxiang Xu]
venue: "CRYPTO 2024"
venue_evidence: "dblp: Fine-Grained Non-interactive Key-Exchange Without Idealized Assumptions, CRYPTO (2) 2024, pp. 251-285, DOI 10.1007/978-3-031-68379-4_8; PDF footnote also states Crypto 2024"
year: 2024
claim_quantifier: conditional
antecedent: "Bounded parallel-time construction: NC1 ⊊ ⊕L/poly, a worst-case class separation. Bounded-time construction: the strong Zero-k-Clique-R hypothesis, an average-case fine-grained hypothesis taken from LaVigne-Lincoln-Vassilevska Williams. Bounded-storage construction: none — unconditional."
tags: [cryptography, fine-grained-cryptography, key-exchange, circuit-complexity, bounded-storage-model, lower-bounds]
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: attacker
cls_unit: algo class
cls_tightness: class
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: algo class
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "If NC1 ⊊ ⊕L/poly holds, then for any constant np, NCNIKE is an AC0[2]-np-NIKE with 0-correctness (i.e., perfect correctness) and NC1-negl(λ)-security."
cls_evidence_src: Thm 3.8
cls_reason: "Classified on the bounded parallel-time construction (Thm 3.8), which the paper's own Contributions section (§1.2) lists first of the three symmetric constructions, per rule 1. Both parties are computational (users confined to AC0[2], adversary to NC1), so by rule 4's tie-break the adversary's class decides the row: party=attacker, unit=algo class, tightness=class (a pure class restriction, no numeric ratio between the classes), second_party=algo class for the honest users' AC0[2] bound. This mirrors fine-grained-cryptography.md's row exactly, the DVV machinery this construction lifts. baseline=stated for the C2-ϵ-security bound in Definition 2.1 (an explicit ϵ cap on distinguishing advantage), not for any AC0[2]-vs-NC1 numeric ratio, which the Claim Boundary confirms does not exist for this construction ('the adversary is confined to a class'). Not classified on the bounded-time (Thm 4.8, unit=time/tightness=exponent) or bounded-storage (Thm 5.9, unit=memory) constructions, which are differently-shaped claims per the page's own Claim Boundary ('Three different adversary classes... this is the paper's whole point'); a second reader wanting those rows should treat them as a distinct classification, not a refinement of this one. target/family/phase/access/write=none: pure key-exchange cryptography, no ML attack, matching the sibling paper fine-grained-nike-lower-bounds.md."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

Answers the open question left by [Afshar et al.](fine-grained-nike-lower-bounds.md) — multiparty NIKE
without random oracles or generic groups — by changing which resource is bounded rather than which
assumption is made. Three constructions, one per model:

- **Bounded parallel time.** An `n_p`-party NIKE computable in `AC0[2]` and secure against all `NC1`
  adversaries, from `NC1 ⊊ ⊕L/poly`. This is the [Degwekar-Vaikuntanathan-Vasudevan](fine-grained-cryptography.md)
  machinery — rank-hiding randomized encodings for `⊕L/poly` — lifted to `n_p` parties.
- **Bounded time.** An `n_p`-party NIKE computable in `Õ(λ^{n_p+k−1})` and secure against
  `Õ(λ^{n_p+k})`-time adversaries, from the strong Zero-`k`-Clique-`R` hypothesis.
- **Bounded storage.** An unconditionally secure `n_p`-party NIKE against adversaries with memory
  `O(λ^{n_p+1})`, with each user consuming `O(λ^{n_p})` bits and total communication `O(λ)`.

Two further contributions: a property the authors call **extendability** (a subgroup's "local key"
can be extended to a larger group by combining with new public keys, giving a multilinear-map-like
structure), which yields generic transformations to identity-based NIKE via bit-fixing PRFs; and a
generalization of the Dziembowski-Maurer storage lower bound from two-party to any multi-party NIKE
with (restricted) extendability, showing the bounded-storage construction's user memory is optimal.

## Claim Boundary

- **Quantified over:** Three different adversary classes, one per model, and this is the paper's whole
  point. (i) **Non-uniform circuit families in `NC1`** — a class, with no size or time parameter.
  (ii) **Word-RAM algorithms with an absolute time bound** `Õ(λ^{n_p+k})`. (iii) **Arbitrary,
  computationally unbounded storage functions `f: {0,1}^n → {0,1}^{m_a}`** — the BSM security
  condition (Definition 2.1) is stated in mutual information, `I(key; (f(urs), (pk_i)) | E) ≤ θ`, so
  the adversary there is information-theoretic and bounded only in output length. Note the BSM here
  is the **traditional** Maurer BSM, not the streaming BSM of Dodis-Quach-Wichs; the paper says so.
- **Antecedent:** Each construction has its own, listed in the frontmatter. Only the bounded-storage
  one is unconditional.
- **Does not establish:** A single unified fine-grained notion. Each of the three results is stated in
  its own model's units and they are not comparable to one another. It also does not establish
  security against super-constant party counts: `n_p` is a constant throughout, and the authors note
  that for the BSM results making `n_p` super-constant does not work.
- **Abstract vs theorem:** None found.

**Correction to a prior boundary note in this repo.** `raw/SOURCES.md` records that this paper
"states no quantitative honest-vs-adversary ratio". **That is not correct.** Two of the three
constructions state one explicitly: honest `Õ(λ^{n_p+k−1})` versus adversary `Õ(λ^{n_p+k})` in the
bounded-time model, and user memory `O(λ^{n_p})` versus adversary memory `O(λ^{n_p+1})` in the BSM.
The accurate version of the survey point is narrower and still holds: the ratios are stated as
**two absolute exponents**, never as a `δ`-indexed family of notions. The gap exponent is a derived
quantity — `1/(n_p+k−1)` and `1/n_p` respectively — determined by the party count and the hypothesis
parameter, not a design parameter that can be set. And the *third* construction, the `AC0[2]`-vs-`NC1`
one, genuinely has no ratio at all: the adversary is confined to a class.

## Key Contributions

- **Theorem 3.8**: `AC0[2]`-`n_p`-NIKE with perfect correctness and `NC1`-`negl(λ)`-security, from
  `NC1 ⊊ ⊕L/poly`.
- **Theorem 4.8**: `n_p`-NIKE in the bounded-time model under the strong Zero-`k`-Clique-`R` hypothesis.
- **Theorem 5.9**: unconditionally `(m_a, ϵ_1+ϵ_2, θ)`-secure `n_p`-NIKE in the bounded storage model.
- **Definitions 2.2/2.3 (extendability, restricted extendability)** and **2.4 (local key
  independence)** — the structural property that both the IB-NIKE transformations and the lower bound
  run on.
- **Theorem 5.15**: the storage lower bound. For any `C1`-`n_p`-NIKE in the BSM with restricted
  extendability, `H(key) ≤ m_u^{n_p}/m_a^{n_p−1} + (Σ_{j} m_u^{j−2}/m_a^{j−2})·µ` — proved by
  induction, generalizing Dziembowski-Maurer, by treating "combine a subgroup's local key with one new
  public key" as a two-party exchange.
- Generic transformations: extendable multi-party NIKE ⟹ (restricted) bit-fixing PRF ⟹ multi-party
  identity-based NIKE, in each fine-grained setting.

## Key Definitions / Theorems

- **Definition 2.1**, `C1`-`n_p`-NIKE, with three separate security notions: `C2`-`ϵ`-security
  (indistinguishability), `C2`-`ϵ`-weak security (key recovery), and `(m_a, ϵ, θ)`-security in the BSM
  (mutual information). The honest algorithms are required to lie in `C1`.
- **Theorem 3.8, verbatim:** *"If NC1 ⊊ ⊕L/poly holds, then for any constant np, NCNIKE is an
  AC0[2]-np-NIKE with 0-correctness (i.e., perfect correctness) and NC1-negl(λ)-security."*
- **The BSM memory relation:** *"For adversaries with memory bounds m_a, each user in our np-party
  NIKE in the BSM consumes m_u = O(np√(λ · m_a^{np−1})) bits of memory"* — an `n_p`-th root, so
  `m_a ≈ m_u^{n_p/(n_p−1)}` and the storage gap **shrinks as the party count grows**.

## Connections

- **The shrinking-exponent pattern, third instance.** The bounded-time gap exponent is
  `1/(n_p+k−1)`; the BSM storage gap exponent is `1/n_p`; and
  [Afshar et al.](fine-grained-nike-lower-bounds.md)'s ROM gap is `n^{K/(K−1)}`. Three independent
  constructions, three different resources, and the same structural fact: adding parties costs gap.
- **The class-vs-exponent distinction.** This paper's first construction restricts the adversary to
  `NC1`, in the manner of [Fine-Grained Cryptography](fine-grained-cryptography.md); the second gives
  it an absolute time budget, in the manner of
  [Public-Key Cryptography in the Fine-Grained Setting](pkc-fine-grained-setting.md), whose
  Zero-`k`-Clique hypothesis it reuses verbatim; the third bounds its memory. Having all three in one
  paper makes it the clearest single illustration of the axes. See
  [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md).
- **Concurrent and independent:** [Fine-Grained NIKE, Revisited](fine-grained-nike-revisited.md),
  reported here in §1.1 as "Couteau et al.".
- **The hypothesis's exposure.** [Fine-Grained Complexity in a World without Cryptography](fine-grained-world-without-crypto.md)
  shows the average-case Zero-`k`-Clique hypothesis this paper's bounded-time construction rests on is
  false for large constant `k` if one-way functions do not exist.
- Concepts: [Bounded Storage Model](../concepts/bounded-storage-model.md),
  [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md),
  [Security Gap Exponent (δ)](../concepts/security-gap-exponent.md),
  [Computational Indistinguishability](../concepts/computational-indistinguishability.md).

## Open Questions / Limitations

- `n_p` must be a constant; the BSM results in particular do not extend to super-constant party counts.
- The `NC1` construction inherits `AC0[2] ⊊ NC1` as its whole separation, so there is no tunable gap.
- The lower bound (Theorem 5.15) applies only to schemes with **restricted extendability**, a
  structural property all constructions here happen to have; it says nothing about schemes without it.
- The bounded-time construction's gap, at fixed `n_p` and `k`, is a factor `λ` — the exponent gap
  `1/(n_p+k−1)` is smallest exactly when the hypothesis is strongest.

## Quotes / Notable Passages

> "Essentially, there are different ways to restrict users' and adversaries' computing power. It can
> be in the terms of running time ..., parallel-running time (i.e., circuit depths) ..., or storage."

> "All existing NC1-fine-grained schemes are based on NC1 ⊊ ⊕L/poly."
