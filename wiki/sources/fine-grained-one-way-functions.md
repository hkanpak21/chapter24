---
title: "On Building Fine-Grained One-Way Functions from Strong Average-Case Hardness"
type: source
date_ingested: 2026-08-20
authors: [Chris Brzuska, Geoffroy Couteau]
venue: "EUROCRYPT 2022, Part II, LNCS, pp. 584-613 (no venue line in the PDF; venue read from the bibliography of GM24_SequentialFunctions in this corpus, which cites it as \"In EUROCRYPT 2022, Part II, LNCS, pages 584-613. Springer, Heidelberg, June 2022\", corroborating ACMS23)"
year: 2022
claim_quantifier: existential
antecedent: "For the one construction: block-finding hardness, a new non-standard average-case notion, with the security proof carried out in the authors' Random Language Model. For the two separations: existence of a PSPACE oracle and of a distribution over oracles."
tags: [cryptography, one-way-functions, complexity-theory, hardness-reductions, fine-grained-cryptography, average-case-reductions, impagliazzo-worlds]
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: attacker
cls_unit: circuit size
cls_tightness: relative
cls_baseline: n/a
cls_second_party: circuit size
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "At a high level, f is an (ε, δ)-FG-OWF if all circuits of (slightly higher) size o(|fm |1+δ ) have probability at most ε to find a preimage of fm (x) for a random input x."
cls_evidence_src: "Section 2.2, informal definition immediately preceding Definition 6 (Fine-Grained One-Way Function), p. 8"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows. RECODE 2026-09-03 (R1, revision 7): tightness exponent -> relative. RECODE 2026-09-03 (R1, honest party unit): second_party none -> circuit size."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper asks whether average-case hardness in NP implies **fine-grained** one-way functions — OWFs
where the inverter is only polynomially, not superpolynomially, more expensive than the honest
evaluation. It supplies the definition that this repo's survey uses as its reference `honest^{1+δ}`
convention (Definition 6), and then spends most of its length arguing that the desired implication
cannot be proved with current techniques.

The positive result builds a fine-grained one-way function *distribution* with a near-quadratic gap
from a new and very strong average-case notion the authors call **block-finding hardness**: given
`N` blocks of `k` random words and the language-membership bits of a randomly chosen block, find
which block it was. Support for this notion is **heuristic only** — the authors introduce a *Random
Language Model* (RLM), the language analogue of the random oracle model, and prove block-finding
hardness there (Lemma 23) as evidence that the assumption is plausible. Theorem 25 and Corollary 26,
the formal positive statements, are stated for the RLM language distribution `DL`.

The two negative results are the substance. Theorem 2 exhibits an oracle relative to which an
exponentially average-case hard language exists but **every** candidate fine-grained OWF is
invertible with `Õ(N)` oracle calls — ruling out relativizing constructions for any gap `N^{1+ε}`.
Theorem 3, which the authors call "the core technical contribution", rules out black-box
constructions even from the much stronger hypothesis of a language whose hardness amplifies at an
exponential rate under parallel repetition. Combined with prior work the paper also derives two
corollaries about TFNP (with Pass-Venkitasubramaniam) and time-bounded Kolmogorov complexity (with
Liu-Pass).

## Claim Boundary

- **Quantified over:** Algorithms throughout are **non-uniform families of Boolean circuits**, one
  per input length, and the efficiency measure is **circuit size**, not runtime — verbatim: *"we
  represent algorithms as families of boolean circuits (one for each input length), and use circuit
  size (i.e., the number of wires) as the main measure of efficiency."* The honest object is itself a
  circuit family `{f_m}`, and the paper stipulates that *"the runtime of `f_m` is `|f_m|`"*, which is
  what lets a single quantity serve as both. The positive result's cost measure is degraded further:
  in the RLM the adversary's budget is counted in **oracle queries to `Chk`**, not in time.
- **Antecedent:** Non-standard on every branch. Block-finding hardness is introduced here and is
  supported *only* by the RLM heuristic; the authors say so plainly. The separations rest on the
  existence of a PSPACE oracle (standard for this genre) and are therefore statements about
  relativizing and black-box proof techniques, not about the world.
- **Does not establish:** That fine-grained one-way functions exist. It establishes neither
  unconditional existence nor existence under any standard assumption. It also does **not** establish
  that exponential average-case hardness fails to imply FGOWFs — only that no relativizing (Theorem 2)
  or `∀∃`-weakly-black-box (Theorem 3) proof can establish the implication. The paper is explicit that
  Theorem 3 rules out `NNN` reductions in the Baecher-Brzuska-Fischlin nomenclature, a *weaker*
  notion than a full oracle separation, and that embedding the adversary into the oracle is left open.
- **Abstract vs theorem:** The abstract reads *"if there is an NP language having a very strong form
  of average-case hardness, which we call block finding hardness, then FGOWF exist"* — an
  unqualified implication in the standard model. The formal statements it points at, Theorem 25 and
  Corollary 26, are both stated for the RLM distribution `DL`, with Corollary 26 saying *"in the
  Random Language Model"* on its face. Section 7 is titled "A Fine-Grained One-Way Function from
  Block-Finding Hardness" but its two subsections are §7.1 "Average-Case Hardness of `DL`" and §7.2
  "Block-Finding Hardness of `DL`". Anyone citing this paper for a standard-model implication should
  check §7 first.

## Key Contributions

- **Definition 6**, the `(ε, δ)`-fine-grained one-way function: the reference `honest^{1+δ}` form.
- **Definition 7**, the distribution relaxation (FG-OWFD) that the positive result actually achieves.
- **Definition 8**, exponential average-case hardness with an *explicit* relation between circuit size
  and success probability (`1/2 + |C_n|/2^n`), tightened deliberately for the fine-grained setting.
- **Block-finding hardness** and the **Random Language Model**, the language analogue of the ROM.
- **Theorem 2** — oracle separation: exponentially average-case hard language, no FGOWF.
- **Theorem 3** — black-box separation from parallel-repetition-amplifying hardness.
- An abstract hitting lemma with advice (Corollary 21) used to prove block-finding hardness in the RLM.

## Key Definitions / Theorems

**Definition 6, verbatim — the `honest^{1+δ}` convention:**

> "Let ε : N 7→ R+ be a positive function and δ > 0 be a constant. A function f : {0, 1}∗ → {0, 1}∗
> is an (ε, δ)-fine-grained one-way function if for all circuit families C = {Cm}m∈N and all large
> enough m, if |Cm| < |fm|^{1+δ}, then we have Prz←${0,1}m [Cm(f(z), 1m) ∈ f−1(f(z))] ≤ ε(m)."

> **Transcription note.** Quotes are taken from `pdftotext` output, which flattens superscripts
> and drops large delimiters. Exponents are restored (`|fm|^{1+δ}`, `T(n)^{1−δ}`) because dropping
> them changes the mathematics; no wording is altered.

The preceding paragraph fixes the honest cost: *"we model as a family {fm}m of circuits, one for each
input size, so that the runtime of fm is |fm|."* So `δ` here is measured against **the honest
function's own circuit size**, and the adversary is a **non-uniform circuit family**. A quadratic gap
is `δ = 1`.

- **Theorem 25.** `F_L` is a `(polylog(λ)·λ^{-ε/2}, 1-ε)`-FG-OWFD; the proof quantifies over adversaries
  of size `|A| ≤ |F_L|^{2-ε}` and samples `L ← DL`, the RLM distribution.
- **Corollary 26.** For any `ε > 0` there is a `(negl(λ), 1-ε)`-FG-OWFD **in the Random Language Model**.
- **Theorem 2 (informal).** *"There is an oracle relative to which there exists an exponentially secure
  average-case hard language, but any candidate fine-grained OWF f can be inverted with probability
  O(1) and Õ(N) calls to the oracle."*
- **Theorem 3 (informal).** *"There is no black-box construction of an N^{1+ε}-hard OWF f, for an
  arbitrary constant ε > 0, from exponentially average-case hard languages L whose hardness amplifies
  at an exponential rate through parallel repetition."*
- **Lemma 23.** Block-finding hardness of `DL`: `Pr[C_n((x⃗_j)_j, L(x⃗_i)) = i] ≤ (|C_n|/(2^n · Õ(N)) + 1)·2^{γk}`.

## Connections

- **The other δ convention.** [Public-Key Cryptography in the Fine-Grained Setting](pkc-fine-grained-setting.md)
  Definition 5 names "the gap" with honest cost `T^{1−δ}` and the adversary threshold at `T`. The two
  `δ`s are **not the same quantity** and are not interchangeable — see
  [Security Gap Exponent (δ)](../concepts/security-gap-exponent.md) for the conversion and for why
  even a matched numeric value still prices different resources (circuit size vs. word-RAM time) in
  different machine models (non-uniform vs. uniform probabilistic).
- **Cited as the reference lower-bound paper for fine-grained crypto** by
  [Fine-Grained NIKE: Constructions and Lower Bounds](fine-grained-nike-lower-bounds.md) and
  [Fine-Grained NIKE, Revisited](fine-grained-nike-revisited.md), both of which list `[BM09, BC22]`
  as the field's two lower-bound results.
- **Same Pessiland question, opposite direction:**
  [Fine-Grained Complexity in a World without Cryptography](fine-grained-world-without-crypto.md)
  shows that if OWFs do not exist, the average-case hypotheses that fine-grained crypto is built on
  are themselves false — so the space this paper is probing may be empty from the other side.
- [Learning in Pessiland via Inductive Inference](learning-in-pessiland.md) — the learning-theoretic
  treatment of the same world.
- The BRSV `OV`-based path this paper reports as "stuck": see
  [Orthogonal Vectors Conjecture](../concepts/orthogonal-vectors-conjecture.md).
- Concepts: [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md),
  [One-Way Functions](../concepts/one-way-functions.md),
  [Average-Case Reductions](../concepts/average-case-reductions.md),
  [Pseudorandomness](../concepts/pseudorandomness.md).

## Open Questions / Limitations

- Whether block-finding hardness holds for any concrete language. The authors offer no candidate
  beyond the RLM heuristic, and note the win-win framing is unsatisfying because *"it is not clear
  whether the latter implies any useful generic algorithmic improvements."*
- Whether Theorem 3 upgrades to a full oracle separation by embedding the adversary in the oracle —
  left as an open question, following Reingold-Vadhan-Trevisan.
- Whether weaker, more natural average-case notions (exponential, non-amortizable) suffice via
  non-relativizing techniques. Both negative results are silent on this.
- The two negative results are **incomparable**: Theorem 2 rules out relativizing reductions,
  Theorem 3 rules out black-box reductions.

## Quotes / Notable Passages

> "we represent algorithms as families of boolean circuits (one for each input length), and use
> circuit size (i.e., the number of wires) as the main measure of efficiency."

> "FGOWFs only require a fixed polynomial gap (as opposed to superpolynomial) between the running
> time of the function and the running time of an inverter."

> "This is unsatisfying, as it does not seem that this results establishes an interesting win-win
> situation: the inexistence of weak Minicrypt implies the inexistence of languages with
> block-finding hardness, but it is not clear whether the latter implies any useful generic
> algorithmic improvements."

> "Still, we believe that there is value in using a simple model to heuristically analyze the
> plausibility of an assumption – even though, as any heuristic model, it must fail on artificial
> counter examples."
