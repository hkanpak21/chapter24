---
title: "Relating Definitions of Computational Differential Privacy in Wider Parameter Regimes"
type: source
date_ingested: 2026-08-22
authors: [Fredrik Meisingseth, Christian Rechberger]
venue: "IACR Communications in Cryptology 2026"
venue_evidence: "https://cic.iacr.org/p/2/4/7; IACR Communications in Cryptology, volume 2, issue 4, article 7, DOI 10.62056/ahebnja5"
journal_ref: "2|4|7"
year: 2026
tags: [cryptography, computational-indistinguishability, differential-privacy, impossibility-frameworks, pseudorandomness]
claim_quantifier: conditional
antecedent: "The direct implications hold for all mechanisms but only in stated parameter regimes: the SIM∀∃ → IND direction requires ε ∈ O(log κ), and the Lp-utility barrier likewise. The IND → SIM∀∃ implication holds for all ε, δ but only with an inflated δ'. The exotic-crypto barrier is conditional on the CDP mechanism being a fully black-box construction from one-way functions. The new separation itself rests on no complexity assumption."
adversary_bound: "Non-uniform polynomial-time distinguishers: `T_poly`, \"the class of all predicates over R computable by some non-uniform polynomial-time Turing Machine (TM)\". Superpolynomial-runtime non-uniform test classes `T_s` are used inside the proofs. No uniform-time statement is made."
date_verified: 2026-08-22
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: poly
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "the class of all predicates over R computable by some non-uniform polynomial-time Turing Machine (TM)"
cls_evidence_src: "Preliminaries (Notation, defining T_poly)"
cls_reason: "Not an ML-attack-scenario paper: a definitional map between CDP notions (IND-CDP, SIM-CDP, SIM-forall-exists-CDP), so target/family/phase/access/write = none/n/a. party/unit/tightness from the test class T_poly that both the direct implications and the separation quantify over. The headline claims (Corollary 2's parameter fix, the new separation) rest on no mechanism-efficiency assumption, so second_party = none even though Theorem 3 and Theorem 4 separately add an efficient-mechanism antecedent; those are secondary results by Rule 1. baseline = n/a: no advantage-over-baseline game, the notions are ratio/expressiveness comparisons."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

A correction and an extension to the definitional map of computational differential privacy. The
whole CDP literature descends from
[Mironov–Pandey–Reingold–Vadhan](computational-differential-privacy.md), henceforth MPRV, and every
definition there is a computational relaxation of *pure* `(ε, 0)`-DP. This paper asks what survives
when `δ` is allowed to be non-negligible — computational **approximate** DP, which is what deployed
systems and cryptographically-assisted mechanisms actually use — and finds that a load-bearing piece
of the pure-case map is wrong even in the pure case.

**The correction.** MPRV's Theorem 1 states `SIM-CDP ⟹ SIM∀∃-CDP ⟹ IND-CDP` with no restriction on
`ε`. The second implication does not hold as stated. It requires `ε ∈ O(log κ)`, for the same reason
MPRV themselves identified in the *other* direction: the proof produces an additive `e^ε · negl` term,
and the CDP definitions only promise that *some* negligible function exists, so `e^ε · negl` is
negligible for arbitrary `negl` only when `ε` is logarithmic. The consequence is that the equivalence
now binds in both directions at once: `(ε, 0)`-SIM∀∃-CDP and `(ε, 0)`-IND-CDP are equivalent **if and
only if** `ε` is logarithmic.

**The separation, and why it is unusual.** Above logarithmic `ε` the failure is not a gap in the proof
but a real separation. With `ε` superlogarithmic and the parameters held equal on both sides,
`(ε, δ)`-SIM∀∃-CDP is *strictly more expressive* than `(ε, δ)`-IND-CDP: there is a task solvable under
the first and not the second. The witness is the Randomized Response mechanism on a binary domain,
which the authors call the first separation in the CDP literature that does not rely on a task built
for the purpose. The trade they name honestly: earlier separations use natural parameter regimes and
contrived tasks, theirs uses a natural task and an unrealistic parameter regime, and *"separations can
currently be found by either using natural tasks or by using natural parameter regimes but not both
simultaneously."*

**The approximate case.** In the other direction, MPRV's dense-model-theorem route survives into
`δ > 0` but leaks. Theorem 2 gets `(ε, δ)`-IND-CDP `⟹` `(ε, δ')`-SIM∀∃-CDP only with
`δ' = e^{2ε}δ + e^{4ε}(δ + negl) + e^{ε}(δ + negl)`. The extra machinery is a corollary of the Hybrid
Indistinguishability Lemma, used to convert a computational distance into a statistical one at the
price of a negligible computational slack. Whether the inflation is necessary is the paper's one
open problem. Until it is settled, IND-CDP and SIM∀∃-CDP are **not** known to be equivalent for
non-negligible `δ` even when `ε` is logarithmic — a fact the pure-case picture hides.

To make any of this sayable, the paper introduces the **δ-gap**: for an implication, how much larger
`δ` must be on the implied side when the `ε` are equal; for a separation, how much larger `δ` may be
made before the separation lapses. This is forced, not decorative — with `δ = 1` every mechanism
satisfies every definition, so separations quantified over arbitrary parameters are vacuous.

Finally, both Groce–Katz–Yerukhimovich barriers to separating statistical from computational DP carry
over to non-negligible `δ` essentially unchanged, and the `L_p`-utility barrier is found to have
carried an unstated `ε ∈ O(log κ)` requirement all along.

## Claim Boundary

- **Quantified over:** mechanism *ensembles* `M = {M_κ : D_κ → R_κ}`, adjacent database pairs of size
  polynomial in `κ`, and tests in `T_poly`. Direct implications quantify over all mechanisms
  satisfying the antecedent definition; expressiveness results quantify over tasks, where a task is a
  pair `(α, u)` with `u` an efficiently computable `{0,1}`-valued utility predicate. Mechanisms are
  **not** required to be efficient except in the `L_p`-utility barrier (Theorem 4), which assumes a
  PPT mechanism with polynomially bounded average error.
- **Antecedent:** four separate ones. (1) Corollary 2's implication requires `δ < 1` and
  `ε ∈ O(log κ)`. (2) Theorem 2 holds for all `ε, δ ≥ 0` but only with the inflated `δ'`. (3)
  Theorem 3, the exotic-crypto barrier, requires that the IND-CDP mechanism be a **fully black-box**
  construction from one-way functions, with utility measured under a random choice of one-way
  permutation. (4) Theorem 4, the `L_p`-utility barrier, requires `p > 0`, `v ≥ 1`,
  `ε ∈ O(log κ)`, an efficient mechanism, range fixed to `R^n` with `n` independent of `κ`, and
  polynomially bounded average `(p,v)`-error. The new separation itself rests on no complexity
  assumption: *"Neither the new expressiveness separation or the new direct implication rely on any
  complexity assumptions."*
- **Adversary class and machine model:** `T_poly`, the non-uniform polynomial-time tests. Verbatim,
  it is *"the class of all predicates over R computable by some non-uniform polynomial-time Turing
  Machine (TM)"*. Deterministic non-uniform tests suffice, by the standard coin-fixing argument the
  paper cites. Nothing here is a uniform-time statement, and nothing here is a query bound.
- **Does not establish:** a practically relevant separation between statistical and computational DP.
  The authors say so directly: *"we do not think of our results as having shown the existence of
  practically relevant separations within CDP."* It does not settle whether the `δ`-gap in Theorem 2
  is necessary, does not touch the `IND-CDP ⟹ SIM-CDP` question that MPRV left open, and does not
  address the multiparty models — the whole paper is in the central curator model.
- **Abstract vs theorem:** none found. The abstract states the `ε ∈ O(log κ)` restriction, names the
  `δ'` inflation explicitly, and labels the separation as being for a natural task. It is, if
  anything, more careful than the body needs.

## Relation to the existing record on MPRV — confirmation, with one contradiction inherited

This repo's page on [MPRV](computational-differential-privacy.md) records that MPRV prove
`SIM-CDP ⟹ SIM∀∃-CDP ⟹ IND-CDP` (their Theorem 1), that the main technical theorem is the
equivalence of the *weaker* `SIM∀∃-CDP` with `IND-CDP` (their Theorem 3) under `ε_κ ∈ O(log κ)`, and
that the `IND-CDP ⟹ SIM-CDP` converse is open.

**On the substance, this paper confirms that record and sharpens it.** The `ε_κ ∈ O(log κ)`
restriction is real, and the emphasis on `SIM∀∃` rather than `SIM` is correct.

**On one detail, it contradicts MPRV, and therefore contradicts what the MPRV page reports without
qualification.** The MPRV page reproduces Theorem 1 — the chain `SIM-CDP ⟹ SIM∀∃-CDP ⟹ IND-CDP` —
with no parameter condition, because MPRV state it that way. That second implication is false for
superlogarithmic `ε`. Verbatim:

> "It was previously claimed [41] that this implication holds without parameter restriction, but we
> show that it only holds when ε ∈ O(log(κ)), where κ is the security parameter."

Following the contradiction rule, both positions stand: MPRV Theorem 1 as published asserts the
unrestricted implication; Meisingseth–Rechberger Proposition 4 and Corollary 2 show it needs
`ε ∈ O(log κ)` and exhibit a mechanism separating the two definitions above that threshold. The net
statement, verbatim:

> "Since this restriction was identified in MPRV for the other direction of the implication, we now
> know that (ε, 0)-SIM∀∃ -CDP and (ε, 0)-IND-CDP are equivalent if and only if ε is logarithmic."

Two further corrections to the surrounding record, both of which touch pages in this corpus:

- Above logarithmic `ε`, `SIM∀∃-CDP` is not merely weaker, it is empty. Verbatim: *"This tells us
  that SIM∀∃ -CDP gives us no guarantees at all when ε is superlogarithmic, whereas IND-CDP might
  still give some guarantees (though very weak ones)."* Anyone treating `SIM∀∃-CDP` as uniformly the
  laxer notion has the ordering right only in the logarithmic regime.
- The `L_p`-utility barrier of [Groce–Katz–Yerukhimovich](limits-cdp-client-server.md) needs
  `ε ∈ O(log κ)`, which GKY did not state. The paper: *"This restriction was not identified in [29]."*
  The barrier also survives into `δ > 0` with no qualitative change.

## Key Contributions

- The discovery that MPRV's `SIM∀∃-CDP ⟹ IND-CDP` implication carries an unstated `ε ∈ O(log κ)`
  condition, and hence that the pure-case equivalence is an *if and only if* in `ε`.
- The **δ-gap** as the unit for quantifying implications and separations once `δ` may be
  non-negligible.
- The first expressiveness separation in the CDP literature obtained from a task that was not
  constructed in order to produce one.
- `(ε, δ)`-IND-CDP `⟹` `(ε, δ')`-SIM∀∃-CDP for all `ε, δ`, with an explicit and possibly suboptimal
  `δ'`, via the Hybrid Indistinguishability Lemma.
- The intermediate statistical notion `SD∀∃-SDP`, and the tight `(e^ε + 1)δ` cost of collapsing it to
  ordinary `(ε, δ)`-SDP.
- Extension of both GKY barriers to non-negligible `δ`, plus the unstated `ε` restriction in the
  second.

## Key Definitions / Theorems

**Definition 9 (δ-gap), the paper's own unit.** For `δ' = f(ε, δ)`: if `(ε, δ)`-Def₁ directly implies
`(ε, δ')`-Def₂, the δ-gap of that implication is `δ' − δ`; symmetrically for expressiveness and for
the negations. The authors note it is *"a property of the implication itself (i.e. the theorem proving
how the definitions are related) rather than of the definitions."*

**Definition 10 ((ε, δ)-IND-CDP).** There is a negligible `negl` such that for every `T ∈ T_poly`,
every large enough `κ`, and all adjacent `D, D'` of size polynomial in `κ`,
`P(T(M_κ(D)) = 1) ≤ e^{ε_κ} P(T(M_κ(D')) = 1) + δ_κ + negl(κ)`.

**Definition 12 ((ε, δ)-SIM∀∃-CDP).** There is a negligible `negl` such that for every adjacent
`D, D'` there exist ensembles `{S_κ(D)}`, `{S_κ(D')}` that are mutually `(e^{ε_κ}, δ_κ)`-related on
every `S ⊂ R_κ` and each `negl(κ)`-indistinguishable from the corresponding `M_κ` with respect to
`T_poly`.

**Proposition 4 (SIM∀∃ → IND, with the gap), verbatim:**

> "For every ε, δ ≥ 0, (ε, δ)-SIM∀∃ -CDP directly implies (ε, δ+eε negl)-IND-CDP for some negligible
> function negl. Furthermore, this implication is tight in the sense that (ε, δ)-SIM∀∃ -CDP does not
> directly imply (ε, δ′)-IND-CDP for any value of δ′ noticeably smaller than δ + eε negl."

**Corollary 2 (the correction), verbatim:**

> "For all δ < 1, (ε, δ)-SIM∀∃ -CDP directly implies (ε, δ)-IND-CDP if and only if ε ∈ O(log(κ)).
> Further, for ε ∈ ω(log(κ)) (ε, δ)-SIM∀∃ -CDP is strictly more expressive than (ε, δ)-IND-CDP. If
> ε ∈ ω(log(κ)) then (ε, δ)-SIM∀∃ -CDP directly implies (ε, δ + δ̂)-IND-CDP, where δ̂ is
> non-negligible."

> **Transcription note.** In the extraction this statement is interrupted after
> `(ε, δ)-SIM∀∃ -CDP` by a page break, a page number, and footnote 8 (which records that the
> logarithmic-`ε` case of the implication, without tightness, was already proved in the paper's
> reference `[38]`). The two halves are contiguous in the PDF and are rejoined above; no wording is
> altered, and the hyphen dropped by the line break in `(ε, δ)SIM∀∃` is restored.

**Theorem 2 (IND → SIM∀∃ in the approximate case), verbatim:**

> "For every ε, δ ≥ 0, a mechanism M being (ε, δ)-IND-CDP directly implies that it is also
> (ε, δ′)-SIM∀∃ -CDP, with δ′ = e2ε δ + e4ε (δ + negl) + eε (δ + negl)."

> **Transcription note.** `eε`, `e2ε`, `e4ε` above are the extraction of `e^ε`, `e^{2ε}`, `e^{4ε}`.
> The exponents are flattened by `pdftotext`; no wording is altered.

**Lemma 2 (the statistical core).** `(ε, δ)`-SD∀∃-SDP directly implies `(ε, (e^ε + 1)δ)`-SDP and this
is tight; more generally `(ε, δ, δ̂)`-SD∀∃-SDP implies `(ε, e^ε max(δ, δ̂) + min(δ, δ̂))`-SDP, tightly.
The tight instance is Randomized Response on `{0,1}` with `P(S(D) = D) = e^ε/(e^ε + 1)`, and `M` the
same mechanism shifted by `δ` toward its input. This is also the mechanism behind the natural-task
separation.

**Theorem 3 (exotic-crypto barrier, extended).** For any `ε, δ ≥ 0`, a fully black-box construction
of an `(ε, δ)`-IND-CDP mechanism from one-way functions yields an `(ε, δ + negl)`-SDP mechanism
matching it on every real-valued, possibly inefficient utility function to within `negl'(κ)`.

**Theorem 4 (`L_p`-utility barrier, extended).** For fixed `p > 0`, `v ≥ 1`, **any `ε ∈ O(log κ)`**,
and `δ ≥ 0`: an efficient `(ε, δ)`-SIM∀∃-CDP mechanism into `R^n` with average `(p,v)`-error at most a
polynomial `err(κ)` yields an efficient `(ε, δ + negl)`-SDP mechanism with error
`err(κ) + negl'(κ)`.

**Proposition 2 (why quantification matters).** `(ε, 1)`-SDP, `(ε', 1)`-SIM-CDP,
`(ε'', 1)`-SIM∀∃-CDP and `(ε''', 1)`-IND-CDP are all equivalent for any `ε, ε', ε'', ε''' ≥ 0` —
every mechanism satisfies all of them. This is why the δ-gap exists.

## Connections

- [Computational Differential Privacy](computational-differential-privacy.md) — MPRV, the definitional
  parent. See the section above for what this paper confirms and what it contradicts.
- [Limits of Computational Differential Privacy in the Client/Server Setting](limits-cdp-client-server.md)
  — GKY, whose two barriers are extended here to `δ > 0` and whose `L_p` barrier is found to need
  `ε ∈ O(log κ)`.
- [Separating Computational and Statistical Differential Privacy in the Client-Server Model](separating-cdp-client-server.md)
  — Bun–Chen–Vadhan, the infeasible separation; cited here as `[10]` and as one of the two
  contrived-task separations this paper contrasts itself against.
- [Towards Separating Computational and Statistical Differential Privacy](towards-separating-cdp.md)
  — Ghazi et al., cited here as `[26]`, the other contrived-task separation.
- [Capacity-Bounded Differential Privacy](capacity-bounded-dp.md) — a different axis on the same
  question: adversary restricted by function class rather than by runtime or by `δ`.
- [SoK: Differential Privacies](sok-differential-privacies.md) — the taxonomy in which IND-CDP and
  SIM-CDP are the sole occupants of the computational-power dimension.
- Concept: [computational differential privacy](../concepts/computational-differential-privacy.md).
- Concept: [computational indistinguishability](../concepts/computational-indistinguishability.md).

## Open Questions / Limitations

- **Open problem 1, the paper's own:** is there a direct implication from IND-CDP to SIM∀∃-CDP with a
  δ-gap below `e^{2ε}δ + e^{4ε}(δ + negl) + e^{ε}(δ + negl) − δ`? Until this is answered the two
  definitions are incomparable for non-negligible `δ`, since neither implies the other with no gap.
- The separation obtained here needs superlogarithmic `ε`, which the authors describe as *"arguably
  not a very realistic parameter regime to use in practice"*. It is also weaker than the earlier
  separations in two further respects they list: it holds only with the same `ε` on both sides, and
  the utility gap it produces is bounded by a function of `ε` and `δ` rather than being arbitrary.
- Whole rows of the paper's own summary table are marked *Open*: for `δ < 1` constant, the
  expressiveness relation between SDP and SIM-CDP is unresolved at every `ε`, and for
  `ε ∈ ω(log κ)` it is unresolved at every `δ`.
- Everything is in the central curator model. The multiparty case, where computational relaxation is
  known to buy expressiveness through multiparty computation, is out of scope.

## Quotes / Notable Passages

> "It was previously claimed [41] that this implication holds without parameter restriction, but we show that it only holds when ε ∈ O(log(κ)), where κ is the security parameter."

> "Since this restriction was identified in MPRV for the other direction of the implication, we now know that (ε, 0)-SIM∀∃ -CDP and (ε, 0)-IND-CDP are equivalent if and only if ε is logarithmic."

> "This tells us that SIM∀∃ -CDP gives us no guarantees at all when ε is superlogarithmic, whereas IND-CDP might still give some guarantees (though very weak ones)."

> "the first separation in CDP using a task not contrived specifically in order to result in a separation."

> "the barriers extend to CapDP suggests that finding a practically relevant expressiveness separation between SDP and CDP might not be significantly easier if one allows a non-negligible (but still practically meaningful) δ."
