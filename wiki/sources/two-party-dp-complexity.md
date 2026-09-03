---
title: On the Complexity of Two-Party Differential Privacy
type: source
date_ingested: 2026-08-20
authors: [Iftach Haitner, Noam Mazor, Jad Silbak, Eliad Tsfadia]
venue: "STOC 2022"
venue_evidence: "https://dblp.uni-trier.de/search?q=On%20the%20Complexity%20of%20Two-Party%20Differential%20Privacy; dblp: STOC 2022, pp. 1392-1405 (confirms the HMSTY25 in-corpus citation)"
year: 2022
tags: [cryptography, hardness-reductions, computational-indistinguishability, differential-privacy, sample-complexity]
claim_quantifier: conditional
antecedent: "Existence of an ε-CDP two-party protocol estimating the inner product over {−1,1}^n × {−1,1}^n up to additive error ℓ ≥ log n with probability c·e^{cε}·ℓ/√n; extends to (ε, δ)-CDP for δ ≤ 1/n²."
adversary_bound: PPT; also holds for the weaker notion of CDP against an external observer (transcript only)
cls_target: train data
cls_family: reconstruct
cls_phase: post hoc
cls_access: scores
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: poly
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: queries
cls_assessed: explicit
cls_evidence: "there exists a ppt algorithm Rec that for every database z ∈ {−1, 1}n and every oracle access to an (ℓ, 300ℓ/√n)-accurate estimator Fz"
cls_evidence_src: Thm 6.3 (restatement of Thm 1.6), §6
cls_reason: "classified on Thm 1.6's reconstruction attack, not the headline key-agreement-necessity reduction (Thm 1.3), because the attack-scenario fields need an explicit adversary and the reconstruction attack is the paper's only concretely instantiated one (Rule 1 exception noted). second_notion=queries from the stated Õ(n^3) query count ('Rec uses Õ(n3) queries to Fz'), a second, comparably concrete notion alongside the ppt/time bound. phase=post hoc: the reconstruction algorithm queries an already-fixed accurate estimator Fz with no further protocol execution. baseline=stated from the explicit trivial always-output-zero protocol, shown to already achieve Θ(ℓ/√n) accuracy."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The predecessor to [HMSTY25](cdp-inner-product-implies-ot.md): any non-trivially accurate two-party CDP
protocol for the inner product implies **key agreement**, hence public-key cryptography is necessary to
bypass the McGregor et al. FOCS'10 accuracy limits. It answers a form of Vadhan's question about the minimal
complexity assumption needed for a CDP-over-DP separation, for the first natural low-sensitivity
many-bit functionality rather than for Boolean XOR.

Three things make the result unusually tight. First, it holds for **CDP against an external observer**, a
weaker notion in which only the transcript need be computationally private; and since key agreement trivially
gives an accurate such protocol, the existence of a non-trivial external-observer CDP protocol is
**equivalent** to key agreement. Second, the accuracy hypothesis is tight up to a constant: the trivial
always-output-zero protocol, which obviously implies nothing, is already within `ℓ` of the inner product of
two uniform vectors with probability `Θ(ℓ/√n)`. Third, the theorem also runs in the information-theoretic
setting, where it reproves McGregor et al.'s non-existence result with a `log n` improvement.

Two side contributions matter beyond privacy. The paper shows the inner product is a good **condenser for
strong Santha–Vazirani sources** (Corollary 1.4), and — the technically surprising part — that
`⟨X·Y, R⟩` is a good condenser even when conditioned on seed-related information `R, X_{R⁺}, Y_{R⁻}`
(Theorem 1.5). Exposing exactly that information is what the key-agreement construction requires. Because
the proof is by an efficient reconstruction algorithm, the condenser statement extends to
**computational** SV sources, where each bit is unpredictable to ppt algorithms given all others — a notion
directly adjacent to next-block pseudo-entropy in PRG constructions.

The reconstruction result (Theorem 1.6) is a tight low-confidence attack: an `(ℓ, β = 300ℓ/√n)`-accurate
estimator of linear statistics is not `(1, 0.1)`-DP, via an explicit ppt algorithm using `Õ(n³)` queries.
Prior reconstruction attacks aimed at blatant non-privacy and therefore failed for `β ≤ 1/2`; this one does
not, and because it is constructive it rules out CDP as well as DP.

§1.2 *Perspective: Hardness Hierarchy* is worth reading for the framing: public-key cryptography "is all
about creating correlation ... hidden from an external or internal observer," and the difficulty with a
long-input functionality like the inner product is that the per-bit correlation is tiny — "only
`O(log n / n)`, and most bits might have no correlation at all."

## Claim Boundary

- **Quantified over:** all `ε`-CDP (and `(ε, δ)`-CDP for `δ ≤ 1/n²`) two-party protocols meeting the stated
  accuracy, including those whose accuracy holds only on average over uniform inputs; and all notions at
  least as strong as CDP against an external observer.
- **Antecedent:** as in the front matter, with `ℓ ≥ log n`.
- **Excluded cases:** trivial accuracy is excluded and the bound is tight there. Functionalities other than
  inner product and Hamming distance are not covered. The condenser result **does not** extend to
  computational SV sources for Corollary 1.4 — "we do not know whether Corollary 1.4 extends to
  computational SV sources (even if we require the sources to be efficiently samplable)." Theorem 1.5 does
  extend.
- **Does not establish:** that OT is necessary — that came later and only for `ℓ ≤ O(n^{1/6})`. It does not
  establish anything about the client/server model, and its §1.3 states the client/server position
  accurately: [GKY11](limits-cdp-client-server.md) "showed that a wide range of CDP mechanisms can be
  converted into an (information-theoretic) DP mechanism," and [BCV16](separating-cdp-client-server.md)
  gives infeasibility "(not impossibility)."
- **Abstract vs theorem:** none found.

## Key Contributions

- Non-trivially accurate two-party CDP inner product ⟹ key agreement; and equivalence for the
  external-observer notion.
- The same statement in the information-theoretic setting, reproving McGregor et al. with better parameters.
- Inner product as a condenser for strong SV sources, with an efficient black-box reconstruction algorithm —
  which the Fourier-analytic proof of McGregor et al. does not give.
- Seed-conditional condensing (Theorem 1.5), extending to computational SV sources.
- Tight low-confidence reconstruction attacks (Theorem 1.6), `Õ(n³)` queries, ruling out DP **and** CDP.

## Key Definitions / Theorems

- **Definition 1.1 (DP).** Standard. Two-party DP: each party's *view* must be a DP function of the other
  party's input (footnote 1 gives the formal version).
- **Theorem 1.3 (Main, informal).** An `ε`-CDP two-party protocol that for some `ℓ ≥ log n` estimates the
  inner product to additive error `ℓ` with probability `c·e^{cε}·ℓ/√n` can be used to construct a
  key-agreement protocol.
- **Corollary 1.4.** For independent `e^{−ε}`-strong SV sources `X, Y`,
  `H_∞(⟨X, Y⟩) ≥ log(√n/(c·e^{cε}·log n))`.
- **Theorem 1.5.** `H_∞(⟨X·Y, R⟩) ≥ log(√n/(c·e^{cε}·log n))` conditioned on `R`, `X_{R⁺}`, `Y_{R⁻}`.
- **Theorem 1.6.** An `(ℓ, β = 300ℓ/√n)`-accurate estimator `F_z` of `⟨z, r⟩` is not `(1, 0.1)`-DP;
  constructive, `Õ(n³)` queries.

## Connections

- Concept: [computational differential privacy](../concepts/computational-differential-privacy.md).
- Concept: [data reconstruction attack](../concepts/data-reconstruction-attack.md).
- Improved in the high-accuracy regime by [HMSTY25](cdp-inner-product-implies-ot.md); Appendix A of that
  paper shows this paper's protocol cannot imply OT.
- The problem originates with [MPRV09](computational-differential-privacy.md) §5.
- Descendant of [Dinur–Nissim PODS'03](dinur-nissim-revealing-information.md) on the reconstruction side —
  Theorem 1.6 is the low-confidence refinement of blatant non-privacy, and the paper notes that
  Dinur–Nissim's own reconstruction algorithm "fails short (in terms of the approximation needed)" to give
  the condenser statement.
- [GIKKM23](towards-separating-cdp.md) names this paper as the model for the necessary-assumptions question
  in the central model.
- Correctly states the boundary of [GKY11](limits-cdp-client-server.md) and
  [BCV16](separating-cdp-client-server.md).
- Entities: [Kobbi Nissim](../entities/kobbi-nissim.md).

## Open Questions / Limitations

- Extend the characterization beyond inner product and Hamming distance.
- Whether Corollary 1.4 holds for computational SV sources.
- Close the gap between key agreement and OT across the full accuracy range (partially closed by HMSTY25).

## Quotes / Notable Passages

> "We prove that the use of public-key cryptography is necessary for bypassing the limitation of McGregor et
> al."

> "the per-bit correlation induced by an accurate DP inner-product functionality is only O(log n/n), and
> most bits might have no correlation at all."

> "Note that the trivial estimation Fz(r) = 0 for all r ∈ {91, 1}n is (ℓ, β = Ω(ℓ/√n))-accurate for every
> ℓ ≥ 0."
