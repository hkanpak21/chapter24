---
title: "Fine-grained Cryptography"
type: source
date_ingested: 2026-08-20
authors: [Akshay Degwekar, Vinod Vaikuntanathan, Prashant Nalini Vasudevan]
venue: "venue unconfirmed from PDF (no venue line). WSPX24's bibliography, read in this corpus, records CRYPTO 2016, Part III, LNCS 9816, pp. 533-562"
year: 2016
claim_quantifier: conditional
antecedent: "For the NC1 results: the worst-case separation ⊕L/poly ⊄ NC1 (standard-ish, widely believed, but a worst-case class separation, not an average-case or cryptographic assumption). For the AC0 results: none — they are unconditional."
tags: [cryptography, complexity-theory, circuit-complexity, one-way-functions, pseudorandomness, fine-grained-cryptography, computational-indistinguishability]
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
cls_evidence: "Semantic Security: For any G = {gλ : PKλ × Cλ → {0, 1}} ∈ C2, there is a negligible function ν′ such that for any λ ∈ N:"
cls_evidence_src: Def 2.13
cls_reason: "Pure complexity-theoretic cryptography, no ML attack, so target/family/phase/access/write=none. party=attacker/unit=algo class/tightness=class because the adversary G is defined by membership in a circuit class C2, not a size or time budget; the page's own Connections section calls this the 'different move' from the exponent-based fine-grained papers ('there is no ratio, and no parameter that could be tuned'), fixing tightness=class over exponent or budget. second_party=algo class: the honest algorithms are simultaneously bounded to the smaller class C1 (Def 2.8 onward); both bounds are class-based (neither a time/size budget), so per rule 4's tie-break the adversary's side (C2, the more powerful class) decides the primary row and C1 is recorded as second_party. baseline=stated: Definition 2.13's semantic-security bound is Pr[gλ(pk,c)=b] ≤ 1/2 + ν′(λ), an explicit fair-coin baseline (the fraction is split into separate glyphs by pdftotext extraction; confirmed against the PDF's displayed inequality)."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper that gives fine-grained cryptography its name and its **class-based** formulation: the
adversary is not given a time or size budget in the honest party's units, it is confined to a
**circuit complexity class**, and the honest algorithms live in a strictly smaller class.
Definition 2.8 onward is parameterized by a pair `(C1, C2)` — the honest algorithms are in `C1`,
security holds against every function family in `C2` — and no exponent appears anywhere.

Two halves. Against `NC1` adversaries, assuming a worst-case class separation, the paper gets
one-way functions, PRGs, an **additively homomorphic public-key encryption scheme**, and
collision-resistant hash functions, all computable in `AC0[2]`. The mechanism is Ishai-Kushilevitz
randomized encodings for `⊕L/poly`, whose encodings are matrices whose *rank* carries the
computation's answer; the public key is a rank-deficient matrix, the secret key is a kernel vector,
and semantic security is the `NC1`-indistinguishability of rank `n−1` from rank `n`.

Against `AC0` adversaries, everything is **unconditional**: PRGs with arbitrary polynomial stretch,
weak PRFs, symmetric-key encryption, and — the authors' own headline — collision-resistant hash
functions computable in `AC0` and secure against all `AC0` circuits. The CRHF is built from a
sparse-ciphertext additively homomorphic SKE, since the generic homomorphic-encryption-to-CRHF
transformation does not survive constant depth. A candidate `AC0` public-key scheme is proposed
without a security proof.

## Claim Boundary

- **Quantified over:** **Non-uniform (possibly randomized) circuit families**, quantified by class
  membership rather than by size: `AC0` (Definition 2.3), `AC0[2]` (2.4), `NC1` (2.5), `⊕L/poly`
  (2.6). The adversary in each primitive is *any* function family `G = {g_λ} ∈ C2`. This is a
  **different move** from pricing the adversary at `honest^{1+δ}` — there is no ratio, and no
  parameter that could be tuned. The honest-vs-adversary separation is a class inclusion
  (`AC0[2] ⊊ NC1`, `AC0 ⊊ AC0`-with-more-depth), not a number.
- **Antecedent:** The `NC1` half needs a worst-case circuit class separation. Note the exact form: the
  abstract, the conclusion, and the informal Theorems 1.2 and 1.3 all state it as an **inequality**
  (`NC1 ≠ ⊕L/poly`), while every formal theorem states it as **non-containment**
  (`⊕L/poly ⊄ NC1` — Theorem 4.1, Lemma 4.3, Theorem 4.4). The two coincide only given the
  containment `NC1 ⊆ ⊕L/poly`, which this PDF does not state. The `AC0` half needs nothing; it rests
  on Håstad's parity lower bound and Braverman's theorem.
- **Does not establish:** Anything about time- or size-bounded adversaries; the axis is **depth**.
  Nor does it establish public-key encryption against `AC0` — §5.5 is explicitly a *candidate*, with
  the authors stating they *"are unable to prove its unconditional security against AC0 circuits"*
  and explaining why their main technique (`k`-wise independence for large `k`) cannot work on it.
  The weak PRF against `AC0` achieves only **quasi-polynomial** security, and the paper proves this
  is inherent for `AC0`-computable weak PRFs via the Linial-Mansour-Nisan Fourier concentration.
- **Abstract vs theorem:** Two findings. (1) The inequality-vs-non-containment mismatch above.
  (2) More consequential: **all the NC1-side primitives are infinitely-often primitives** and the
  abstract does not say so. Remark 3.1 states it outright — *"all primitives constructed in this
  section and Section 4 are infinitely-often primitives"* — because a worst-case assumption only
  yields hardness for infinitely many `λ`, not all large `λ`. The abstract's "we construct one-way
  functions, pseudo-random generators ..., collision-resistant hash functions and most importantly,
  public-key encryption schemes" carries no such qualifier. The `AC0` results in §5 are not affected.

## Key Contributions

- **§2.5**, the `(C1, C2)`-parameterized redefinition of OWF, PRG, wPRF, SKE, PKE, and CRHF —
  the class-based template for fine-grained security.
- **Theorem 3.1**: a general recipe — if `C2 ⊄ C1` and every family in `C2` has a surjective perfect
  randomized encoding computable in `C1`, then `C1`-OWFs and `C1`-PRGs against `C1` exist.
- **Theorem 4.1**: `AC0[2]`-computable additively homomorphic PKE secure against `NC1`, from
  `⊕L/poly ⊄ NC1`. **Theorem 4.4**: CRHF against `NC1`.
- **Theorems 5.1, 5.2, 5.5, 5.11**: unconditional PRG with arbitrary polynomial stretch, weak PRF,
  SKE, and CRHF, all in `AC0` and secure against `AC0`.
- **Observation 5.4**: an inherent quasi-polynomial ceiling on `AC0`-computable weak PRFs.

## Key Definitions / Theorems

**The class-based security template (Definition 2.8, verbatim):**

> "Let F = {fλ : {0, 1}λ → {0, 1}l(λ)} be a function family. F is a C1-One-Way Function (OWF)
> against C2 if: • Computability: For each λ, fλ is deterministic. • One-wayness: For any
> G = {gλ : {0, 1}l(λ) → {0, 1}λ} ∈ C2, there is a negligible function ν such that for any λ ∈ N:
> Pr x←Uλ [fλ(gλ(y)) = y | y ← fλ(x)] ≤ ν(λ)"

**Remark 3.1, verbatim — the infinitely-often caveat:**

> "Using such a worst case assumption, we only know how to obtain primitives whose security holds for
> an infinite number of values of λ, as opposed to holding for all large enough λ. Such primitives are
> called infinitely-often, and all primitives constructed in this section and Section 4 are
> infinitely-often primitives."

- **Theorem 3.1.** Conditions: `C2` families have surjective PREs computable in `C1`; `C2 ⊄ C1`; `C1`
  closed under constant composition; `C1` non-uniform or randomized; `C1` computes arbitrary
  thresholds. Then there is a `C1`-OWF and a `C1`-PRG with non-zero additive stretch against `C1`.
- **Theorem 4.1.** *"Assume ⊕L/poly ⊄ NC1. Then, the tuple of families (KeyGen, Enc, Dec) defined in
  Construction 4.2 is an AC0[2]-Public Key Encryption Scheme against NC1."*
- **Lemma 4.3.** The indistinguishability of `ZeroSamp` from `OneSamp` to `NC1` families holds *"for
  an infinite number of values of λ."*

## Connections

- **The distinction this page exists to mark.** This paper restricts the adversary to a **resource
  class**; [On Building Fine-Grained One-Way Functions](fine-grained-one-way-functions.md) and
  [Public-Key Cryptography in the Fine-Grained Setting](pkc-fine-grained-setting.md) price the
  adversary at an **exponent above honest cost**. Both are called "fine-grained cryptography" and
  they are different moves. See [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md).
- **The direct successor in this corpus.**
  [Fine-Grained NIKE without Idealized Assumptions](nike-without-idealized-assumptions.md) builds an
  `AC0[2]`-computable `n_p`-party NIKE secure against `NC1` from the same `NC1 ⊊ ⊕L/poly`
  assumption, and explicitly reports that *"All existing NC1-fine-grained schemes are based on
  NC1 ⊊ ⊕L/poly"*.
- This paper cites Applebaum-Barak-Wigderson: see
  [Public-Key Cryptography from Different Assumptions](pkc-from-different-assumptions.md).
- [Fine-Grained NIKE: Constructions and Lower Bounds](fine-grained-nike-lower-bounds.md) credits this
  paper for the observation that constant-depth restriction buys *unconditional* security while
  logarithmic-depth restriction buys worst-case-assumption security.
- Concepts: [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md),
  [One-Way Functions](../concepts/one-way-functions.md),
  [Pseudorandomness](../concepts/pseudorandomness.md),
  [Computational Indistinguishability](../concepts/computational-indistinguishability.md),
  [Bounded Storage Model](../concepts/bounded-storage-model.md) (the paper's own survey of adjacent
  bounded-adversary models, §1.2).

## Open Questions / Limitations

The paper's own list: (1) get primitives from the known `AC0[p]` lower bounds; (2) prove the §5.5
candidate `AC0`-PKE secure, or build one another way — which the authors reduce to a clean question,
whether some fixed polylog-wise independent distribution fools `AC0` of arbitrary depth;
(3) relax `⊕L/poly ⊄ NC1` to `P ⊄ NC1`. They also name, as a related extension, *"to construct a
public-key encryption scheme resistant against O(n^c) time adversaries (for some c > 2) under
worst-case hardness assumptions"* — the exponent axis, flagged from inside the class-based paper.

## Quotes / Notable Passages

> "Fine-grained cryptographic primitives are ones that are secure against adversaries with an apriori
> bounded polynomial amount of resources (time, space or parallel-time), where the honest algorithms
> use less resources than the adversaries they are designed to fool."

> "We also present a candidate construction for public-key encryption, but we are unable to prove its
> unconditional security against AC0 circuits."
