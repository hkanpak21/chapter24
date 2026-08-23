---
title: "Speak Much, Remember Little: Cryptography in the Bounded Storage Model, Revisited"
type: source
date_ingested: 2026-08-21
authors: [Yevgeniy Dodis, Willy Quach, Daniel Wichs]
venue: venue unconfirmed from PDF (the file is dated September 22, 2021 and carries no venue line; recorded elsewhere in this repo as EUROCRYPT'23)
year: 2021
tags: [cryptography, bounded-storage-model, complexity-theory, computational-indistinguishability]
claim_quantifier: universal
antecedent: "none for the constructions, which are unconditional. The lower bounds carry an antecedent about the model: Theorem 7.4 holds in the unbounded processing model, Theorem 7.7 in the fully streaming model, both for protocols with delta-correctness and (m, epsilon) security where delta - epsilon = Omega(1)."
adversary_bound: "memory. The adversary is a streaming algorithm with m bits of memory and unbounded computational power. The constructions additionally tolerate an adversary given unlimited short term memory during long rounds who must compress to m bits at the end of each."
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: attacker
cls_unit: memory
cls_tightness: exponent
cls_baseline: stated
cls_second: memory
cls_assessed: explicit
cls_evidence: "we can allow arbitrarily large gaps between m and n, up to exponential m = 2O(n)"
cls_evidence_src: "§1 (Main Result)"
cls_reason: "party=attacker and unit=memory even though the codebook's revision-2 note flags 'attacker × memory' as expected to stay empty in the corpus: the paper's own text is unambiguous that the eavesdropper is bounded at m bits with unbounded time, and rule 4's tie-break defaults to the adversary when both parties carry the same-type bound; second=memory records the honest parties' separately stated n-bit bound."
cls_prov: S
cls_date: 2026-08-22
---

## Summary

Prior public key style constructions in the bounded storage model stopped at a quadratic gap between
adversarial storage `m` and honest storage `n`, and Dziembowski and Maurer appeared to have proved that the
ceiling was real by ruling out key agreement when `m > n^2`. This paper observes that the lower bound was
proved in a restricted variant of the model and does not apply to the streaming variant, then breaks the
ceiling. Unconditional key agreement, oblivious transfer and general multiparty computation are constructed
for `m` up to `2^{O(n)}`.

The modelling gap is set out precisely. The traditional bounded storage model imposes four restrictions that
the streaming model does not. Only one long round is allowed and it is the first. Long rounds must carry a
uniformly random string. Honest parties may read only `n` non adaptively chosen physical locations of each
long string rather than processing it arbitrarily in small space. The adversary gets unlimited short term
memory and is only required to compress to `m` bits after each long round. The Dziembowski and Maurer bound
uses the first restriction, so a protocol with many long rounds escapes it. The constructions here do use
many long rounds while still satisfying the other three, which makes them stronger, not weaker, along those
axes.

The price is stated and then shown to be unavoidable in part. Key agreement costs
`Õ(⌈m/n^2⌉ · λ)` rounds and `Õ(m⌈m/n^2⌉ · λ)` bits of communication, and oblivious transfer matches it up to
`poly(λ)`. Theorem 7.4 proves that in the unbounded processing model any key agreement with honest storage
`n` needs `C ≥ Ω(m^{3/2}/n)` communication and `R ≥ Ω(sqrt(m)/n)` rounds. Theorem 7.7 extends this to fully
streaming adversaries at a weaker rate, `C ≥ Ω(m(m/n^2)^{1/3})` and `R ≥ Ω((m/n^2)^{1/3})`. So rounds must
grow with `m` and communication must be superlinear in `m`, and a quantitative gap between these bounds and
the constructions remains open. If one insists on polynomial efficiency, `m` is again confined to an
arbitrarily large polynomial.

A second contribution is qualitative. The oblivious transfer protocol satisfies simulation based security
with an efficient simulator, where every prior bounded storage transfer protocol satisfied only an
indistinguishability based sender privacy, which corresponds to inefficient simulation. Applied to the zero
knowledge functionality this yields the first bounded storage zero knowledge protocol with an efficient
simulator at an arbitrary gap. The main technical tool is a bit entropy lemma, which says that if
`H_∞(X) ≥ δ·k` then the individual bits satisfy `Σ_i H_∞(X[i]) ≥ ρ·k` with `ρ` optimally related to `δ`.

## Claim Boundary

- **Quantified over:** all passive streaming eavesdroppers with `m` bits of memory for key agreement, and all
  malicious participants with `m` bits for oblivious transfer, with no bound on running time. Receiver
  privacy in the transfer protocol holds even against a malicious sender with *unbounded* space, so only
  sender privacy relies on the storage bound.
- **Antecedent:** none for the constructions. The lower bounds are conditional on the model rather than on a
  complexity assumption, and the two theorems give different exponents in the two adversary models.
- **Which party carries the resource bound:** the **adversary**, an eavesdropper or a malicious protocol
  participant. Honest parties are separately bounded at `n` bits, and the whole model consists of the gap
  between the two bounds. No party is bounded in time.
- **Does not establish:** anything about a *computationally* bounded adversary, which is the regime
  [On Bounded Storage Key Agreement and One-Way Functions](bsm-key-agreement-owf.md) takes up. It does not
  close the gap between its own upper and lower bounds, `Ω(sqrt(m)/n)` against `Õ(m/n^2)` rounds. It does not
  refute Dziembowski and Maurer, whose theorem remains correct in the restricted model where it was proved.
  The multiparty extension requires honest storage, rounds and communication to depend polynomially on the
  circuit size, though not on `m`.
- **Abstract versus theorem:** the abstract says the earlier lower bound "only applies to a significantly
  more restricted version of the BSM", and Section 1.1 identifies exactly which of four restrictions is
  load bearing, restriction (a), a single long round. The paper is careful to say that the restrictions (b)
  to (d) are still satisfied by its own protocols. No overreach found.

## Key Contributions

- Identification of the modelling gap between the traditional and streaming bounded storage models, in four
  named restrictions, and the demonstration that only the single long round restriction carries the
  Dziembowski and Maurer bound.
- Unconditional key agreement and oblivious transfer in the streaming model at storage gaps up to
  `m = 2^{O(n)}`, breaking the quadratic barrier.
- Round and communication lower bounds showing the growth in rounds and superlinear communication is
  necessary, in two adversary models with different exponents.
- Simulation based oblivious transfer with an efficient simulator in the bounded storage model, answering a
  question left open by Ding, Harnik, Rosen and Shaltiel, and hence bounded storage zero knowledge with an
  efficient simulator.
- The bit entropy lemma, Lemma 3.1.

## Key Definitions / Theorems

- **The `(n, m)`-BSM, Section 4.** Honest parties send and receive in a streaming manner using `n` bits
  overall, the adversary is a streaming algorithm with `m` bits. Long rounds exceed `m` in size, short rounds
  are below `n`. The constructions additionally give the adversary unlimited short term memory during a long
  round, requiring only that it compress to `m` bits immediately afterwards, and impose no memory restriction
  during short rounds.
- **Key agreement security, Section 5.1.** Correctness is `Pr[key_A = key_B] = 1`, and security asks
  `(view_Eve, key_A) ≈_ε (view_Eve, key*)` for a uniform independent `key*`.
- **Theorem 5.1.** For any `m ≥ ℓ` and `λ` there is `n_min = O(λ + ℓ + log m)` such that for all `n > n_min`
  there is a key agreement protocol in the `(n, m)`-BSM outputting an `ℓ` bit key with security
  `2^{-Ω(λ)}`, round complexity `O(⌈m/n^2⌉ · λ · polylog(m))` and communication
  `O(m · ⌈m/n^2⌉ · λ · polylog(m + λ))`.
- **Theorem 1.2, informal, oblivious transfer.** The same parameters up to `poly(λ)`, with an efficient
  simulator, message size `Ω(n)`, and receiver security against an unbounded space malicious sender.
- **Theorem 7.4.** For a key agreement protocol in the unbounded processing model with honest storage `n`,
  `δ`-correctness and `(m, ε)` security with `δ − ε = Ω(1)`, the communication satisfies
  `C ≥ Ω(m^{3/2}/n)` and the round count `R ≥ Ω(sqrt(m)/n)`.
- **Theorem 7.7.** In the fully streaming model, `C ≥ Ω(m·(m/n^2)^{1/3})` and `R ≥ Ω((m/n^2)^{1/3})`.
- **Lemma 3.1, bit entropy.** If `H_∞(X) ≥ δ·k` for `X` of length `k` then `Σ_{i∈[k]} H_∞(X[i]) ≥ ρ·k`, with
  `ρ = Ω(1)` when `δ = Ω(1)`.

## Connections

- [Simple Schemes in the Bounded Storage Model](bounded-storage-simple-schemes.md) is the immediately prior
  state of the art at `m = O(n^2)`, and is cited as one of the works that had already left the traditional
  model without saying so.
- [Authentication in the Bounded Storage Model](authentication-bounded-storage.md) is the companion paper,
  which reuses Lemma 7.13 from here and adds MACs and signatures.
- [Raz, Fast Learning Requires Good Memory](raz-parity-time-space.md) is identified in Section 1.1 as the
  work that first abandoned restrictions (b) to (d) of the traditional model.
- [Bounded Storage Model](../concepts/bounded-storage-model.md) records both variants, and this paper is the
  source of the distinction as stated there.
- [On Bounded Storage Key Agreement and One-Way Functions](bsm-key-agreement-owf.md) starts from these lower
  bounds and asks what a minimal computational assumption buys.
- [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md).

## Open Questions / Limitations

- The gap between `R ≥ Ω(sqrt(m)/n)` and `R = Õ(m/n^2)`, and between the two communication bounds, is open,
  as is the gap between the unbounded processing and fully streaming lower bounds.
- Polynomial efficiency still caps `m` at an arbitrarily large polynomial. Exponential `m` costs exponential
  rounds and communication.
- Multiparty computation inherits a polynomial dependence on the circuit size in honest storage, rounds and
  communication.

## Quotes / Notable Passages

- "we observe that the DM lower bound only applies to a significantly more restricted version of the BSM, and
  does not apply to the streaming variant."
- "The only price of accommodating larger values of m is that the round and communication complexities of our
  protocols grow accordingly, and we provide lower bounds to show that an increase in rounds and
  communication is necessary."
- "the authors critically assumed that there is at most one “long” communication round in the key agreement
  protocol"
- "cryptography can be proven unconditionally, while supporting arbitrary gaps between the powers of honest
  parties and the attacker."
