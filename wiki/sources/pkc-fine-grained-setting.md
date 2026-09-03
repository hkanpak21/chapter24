---
title: "Public-Key Cryptography in the Fine-Grained Setting"
type: source
date_ingested: 2026-08-20
authors: [Rio LaVigne, Andrea Lincoln, Virginia Vassilevska Williams]
venue: "CRYPTO 2019"
venue_evidence: "https://link.springer.com/chapter/10.1007/978-3-030-26954-8_20 (Advances in Cryptology - CRYPTO 2019, LNCS 11694); IACR archive https://www.iacr.org/archive/crypto2019/116940386/116940386.pdf confirms"
year: 2019
claim_quantifier: conditional
antecedent: "The strong Zero-k-Clique-R hypothesis (an average-case search hypothesis stated in this paper), or the Random Edge Zero-k-Clique hypothesis which implies it. Non-standard: these are average-case fine-grained hypotheses, not standard cryptographic assumptions."
tags: [cryptography, public-key-encryption, one-way-functions, complexity-theory, fine-grained-cryptography, average-case-reductions]
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: relative
cls_baseline: n/a
cls_second_party: time
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "The (relative) gap of an T (n) fine-grained one-way function f is the constant δ > 0 such that it takes T (n)1−δ to compute f but for all PFTT (n) adversaries A."
cls_evidence_src: "Definition 5, Section 2.1, p.14, raw/LLV19_PKCFineGrained.pdf"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows. DISPUTE 2026-09-03: tightness and second_party. Definition 5 states a relation between two parties, the honest evaluator computing f in T(n)^(1-δ) and the PFTT(n) adversary inverting it in T(n); under codebook revision 6 (2026-08-27), which split `exponent` into a single-party exponent and a two-party `relative`, this is exactly the `relative` case, with second_party = time for the honest evaluator, not `exponent` with second_party = none. This row's cls_date (2026-08-22) predates revision 6 and appears not to have been migrated through it. RECODE 2026-09-03 (R1, revision 7): tightness exponent -> relative. RECODE 2026-09-03 (R1, honest party unit): second_party none -> time."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper that names **"the gap"** as a formal object (Definition 5) and builds the first fine-grained
public-key cryptography from an average-case fine-grained hypothesis rather than from a random oracle
or from exponentially secure OWFs.

The technical strategy is to abstract Merkle puzzles. The authors isolate four structural properties
of a hard problem — *plantable*, *average-case list-hard*, *splittable*, and (assembled) *key-exchange
ready* (KER) — and prove that any KER problem yields a fine-grained key exchange (Theorem 5), which
amplifies to a strong one (Theorem 6) and then to a non-interactive fine-grained public-key
cryptosystem (Theorem 7). They then verify the properties for **Zero-k-Clique-R**. Alice and Bob each
send `m` problem instances and plant solutions in `√m` of them; matching planted indices gives the
shared key, and the eavesdropper must effectively solve all `m`.

The headline numbers matter for the survey. The generic construction gives honest `O(T(n))` versus
adversary `Ω̃(T(n)^{1.5−δ})`. §6's improved construction, using the *location* of the planted clique
rather than mere existence, gives honest `Õ(n^{k+2})` versus adversary `Ω̃(n^{2k})` — a gap of
`N` to `N^{2−4/(k+2)}`, which **approaches quadratic from below as `k` grows**. Fine-grained OWFs
and fine-grained hardcore bits come from much weaker hypotheses (superlinear average-case hardness),
with a Goldreich-Levin variant that only loses `N^{o(1)}` instead of the usual `Ω(N)` factor — a
loss that would otherwise erase the entire gap.

## Claim Boundary

- **Quantified over:** **Uniform, probabilistic word-RAM algorithms**. Verbatim: *"The running times
  of all algorithms are analyzed in the word-RAM model of computation, where simple operations such
  as +, −, ·, bit-shifting, and memory access all require a single time-step."* The adversary class is
  `PFT_{T(n)}` (Definition 1): algorithms running in `O(T(n)^{1−δ'})` for **some** constant `δ' > 0`.
  Security must hold against all of them, so the effective adversary budget is anything below `T(n)`
  by a polynomial factor. Nothing here is non-uniform, and nothing is a circuit-size bound.
- **Antecedent:** The key-exchange results need the **strong Zero-k-Clique-R hypothesis**
  (Definition 20), an average-case *search* hypothesis over a specified range `R = n^{ck}`. Theorem 3
  derives it from the Random Edge Zero-k-Clique hypothesis (Definition 21). These are fine-grained
  average-case hypotheses about a problem in P; they are not implied by, and do not imply, any
  standard cryptographic assumption. The paper itself notes the barrier that motivated the detour:
  extending the Ball et al. OV-based approach *"would falsify the Nondeterministic Strong Exponential
  Time Hypothesis (NSETH)"*.
- **Does not establish:** Superquadratic gaps. Every construction here is capped below `N^2`, and the
  paper says the advantage cannot be driven below `1/poly(n)` at all: *"the adversary's advantage
  cannot be any less than 1/poly(n) since, due to the fine-grained nature of the scheme, the
  adversary can always solve the hard problem via guessing."* It also does not establish security
  against non-uniform adversaries.
- **Abstract vs theorem:** None found. The abstract's claim of "a similar gap between the computation
  of the honest party and the adversary as prior work, while being non-interactive" is matched by
  Theorem 7 and Corollary 2.

## Key Contributions

- **Definition 5**, "the (relative) gap" — the survey's second δ convention, and the one that names
  the quantity.
- **Definitions 11-13, 22**: plantable, average-case list-hard, generalized splittable, and
  key-exchange-ready (KER) — a property checklist that any candidate hard problem can be tested against.
- **Theorem 5**: KER problem ⟹ weak fine-grained key exchange; **Theorem 6**: amplification to strong;
  **Theorem 7**: KER ⟹ fine-grained public-key cryptosystem.
- **Theorem 1 / Theorem 2**: fine-grained OWFs and fine-grained hardcore bits from superlinear
  average-case hardness of k-SUM-R or Zero-k-Clique-R — a much weaker hypothesis than the key exchange needs.
- A fine-grained Goldreich-Levin: because solutions are describable in `O(log n)` bits, only
  `O(log n)` distinguisher queries are needed, losing `N^{o(1)}` instead of `Ω(N)`.
- **§6**: the improved construction reaching `N` to `N^{2−4/(k+2)}`.

## Key Definitions / Theorems

**Definition 5, verbatim — "the gap":**

> "The (relative) gap of an T(n) fine-grained one-way function f is the constant δ > 0 such that it
> takes T(n)^{1−δ} to compute f but for all PFTT(n) adversaries A, Pr x←{0,1}n [A(f(x)) ∈ f−1(f(x))]
> ≤ insig(n)."

> **Transcription note.** Quotes are taken from `pdftotext` output, which flattens superscripts
> and drops large delimiters. Exponents are restored (`|fm|^{1+δ}`, `T(n)^{1−δ}`) because dropping
> them changes the mathematics; no wording is altered.

**Definition 1, verbatim — the adversary class the gap is measured against:**

> "An algorithm A is an T(n) probabilistic fine-grained time, PFTT(n), algorithm if there exists a
> constant δ > 0 such that A runs in time O(T(n)^{1−δ})."

Note the paper **reuses the symbol `δ`** in both definitions for two different local variables: in
Definition 5 it is the honest party's discount below `T`, in Definition 1 it is the adversary's. The
quantity Definition 5 names is the exponent separating honest `T^{1−δ}` from the threshold `T`.

- **Theorem 5.** A `ℓ(n)`-KER problem yields a `(ℓ(n)T(n), α, γ)`-FG-KeyExchange with `γ ≤ 1/(10,000ℓe)`
  and `α ≤ 1/4`.
- **Theorem 7.** `ℓ(n)`-KER ⟹ an `ℓ(n)·T(n)`-fine-grained public key cryptosystem.
- **Corollary 2.** Under the strong Zero-k-Clique-R hypothesis with `R = ℓ(n)^2 n^{2k}`, a
  `(ℓ(n)T(n), 1/4, insig(n))`-FG-KeyExchange exists with honest time `Õ(n^k √ℓ(n) + n^2 ℓ(n))`.
  For Zero-3-Clique (the better-believed case) *"the gap is t = 5/4 = 1.2."*
- **§6.** Honest `Õ(n^{k+2})`, adversary `Ω̃(n^{2k})`, gap `N` to `N^{2−4/(k+2)}`.

## Connections

- **The other δ convention.** [On Building Fine-Grained One-Way Functions](fine-grained-one-way-functions.md)
  Definition 6 sizes the adversary at `|f|^{1+δ}` against the honest circuit's own size. Converting:
  writing honest cost as `H`, this paper's threshold `T = H^{1/(1−δ)}`, so
  `δ_BC = δ_LLV/(1−δ_LLV)`. A quadratic gap is `δ = 1` in BC22 and `δ = 1/2` here. Full treatment in
  [Security Gap Exponent (δ)](../concepts/security-gap-exponent.md).
- **This paper's hypothesis is the one that breaks in Pessiland.**
  [Fine-Grained Complexity in a World without Cryptography](fine-grained-world-without-crypto.md)
  proves that if OWFs do not exist, the average-case Zero-k-Clique conjecture is false for
  sufficiently large `k`, and states explicitly that *"the gap achievable by their construction must
  be bounded below 2"* — an unconditional cap on this paper's §6 in a world without cryptography.
- **The successor line in the same hypothesis family:**
  [Fine-Grained NIKE without Idealized Assumptions](nike-without-idealized-assumptions.md) reuses the
  strong Zero-k-Clique-R hypothesis for multi-party NIKE.
- [The Planted Orthogonal Vectors Problem](planted-orthogonal-vectors.md) reports that this paper's
  protocol *"can be adapted to work with our planted k-OV"* but that the security remains quadratic,
  and names breaking the quadratic barrier as the open problem.
- [Fine-Grained Cryptography](fine-grained-cryptography.md) — the earlier circuit-class treatment,
  which prices the adversary by class rather than by exponent.
- Concepts: [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md),
  [Security Gap Exponent (δ)](../concepts/security-gap-exponent.md),
  [One-Way Functions](../concepts/one-way-functions.md),
  [Average-Case Reductions](../concepts/average-case-reductions.md),
  [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md).

## Open Questions / Limitations

- Superquadratic gap. The construction is a Merkle-puzzle descendant and inherits the ceiling.
- Advantage is `1/4` before amplification and never negligible in `n` as a matter of principle in the
  fine-grained setting, by the guessing attack the paper names.
- The hypotheses are for a specific range `R`; the paper is careful that small `R` makes the problems easy.
- No non-uniform security.

## Quotes / Notable Passages

> "Thus, even if P=NP, there are problems that are hard on average for specific runtimes, i.e. fine-grained hard on average."

> "The running times of all algorithms are analyzed in the word-RAM model of computation, where simple
> operations such as +, −, ·, bit-shifting, and memory access all require a single time-step."

> "However, in the fine-grained setting, factors of N can completely eliminate the gap between
> computation and inversion, and so having a notion of fine-grained hardcore bits is interesting."
