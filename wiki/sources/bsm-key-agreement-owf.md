---
title: On Bounded Storage Key Agreement and One-Way Functions
type: source
date_ingested: 2026-08-21
authors: [Chris Brzuska, Geoffroy Couteau, Christoph Egger, Willy Quach]
venue: 22nd Theory of Cryptography Conference 2024 (TCC 2024), stated on the HAL cover page of this copy (hal-04770569)
year: 2024
tags: [cryptography, bounded-storage-model, one-way-functions, fine-grained-cryptography, pseudorandomness, complexity-theory]
claim_quantifier: conditional
antecedent: "For the constructions: one-way functions exist, or space-bounded one-way functions with space bound poly(a) exist for the fully streaming variant. For the converse: a streaming key agreement exists in the stated parameter regime, from which the existence of one-way functions is derived."
adversary_bound: "TWO axes at once. The adversary is bounded in space by a, and additionally bounded in TIME to probabilistic polynomial time. The paper's subject is the exchange rate between the two."
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: attacker
cls_unit: memory
cls_tightness: relative
cls_baseline: n/a
cls_second_party: memory
cls_second_notion: time
cls_assessed: explicit
cls_evidence: "In the other direction, we show that one-way functions are necessary for key agreement in the bounded-storage model with large space gaps."
cls_evidence_src: abstract
cls_reason: "Adversary bounded in two axes at once, space a and PPT time (front matter adversary_bound); honest party separately bounded at s bits (second_party=memory, Claim Boundary). unit=memory/tightness=exponent for the primary space-gap axis (explicit relations s << sqrt(a) in Thm 3, s << a^{1/polylog(r)^r} in Thm 4); second_notion=time for the added computational axis this paper prices against it (rule 4b)."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

Key agreement in the bounded storage model exists unconditionally, but only at a cost. Cachin and Maurer need
honest storage `s = ω(sqrt(a))` against adversarial storage `a`. Dodis, Quach and Wichs remove the storage
constraint but need `r = ω(a/s^2)` streaming rounds and `C = ω((a/s)^2)` bits of communication, and both
limits are known to be inherent. This paper asks what changes when a minimal computational assumption is
added, and answers on both sides.

On the positive side, assuming one way functions there is a key agreement in the streaming model with an
arbitrary polynomial space gap, honest storage `s = poly(λ)` independent of `a`, a single long stream of
length `a · poly(λ)` followed by one short message, and security against an unbounded processing
probabilistic polynomial time eavesdropper with space `a`. A second streaming round upgrades this to
everlasting security, meaning the key stays protected even if the adversary later becomes all powerful.
Assuming instead space bounded one way functions, one way against polynomial time adversaries with a fixed
polynomially bounded storage, the same construction gives security against a fully streaming adversary.

On the negative side, one way functions are necessary. Theorem 3 says that a streaming key agreement with a
single long stream and a short answer, using honest space `s ≪ sqrt(a)`, implies one way functions in the
unbounded processing model, or space bounded one way functions in the fully streaming model. That conclusion
matches the positive result exactly. Theorem 4 covers `r` rounds at a worse space gap, `s ≪ a^{1/polylog(r)^r}`,
and concludes only non uniform infinitely often one way functions. The exponential dependence on `r` means
Theorem 4 is meaningful only for constant `r`.

Getting there requires tracking the space efficiency of the standard Minicrypt reductions, from distributional
one way functions through weak and standard one way functions to pseudorandom generators and pseudorandom
functions. The authors present that accounting as a contribution in its own right and observe that space tight
reductions between Minicrypt primitives have received little attention.

## Claim Boundary

- **Quantified over:** probabilistic polynomial time adversaries with a space bound `a`, in one of two
  variants. A *fully streaming* adversary holds `a` bits throughout. An *unbounded processing* adversary is
  polynomial time throughout but is only required to compress to an `a` bit state after each long round.
  Everlasting security additionally quantifies over an all powerful adversary acting after the protocol ends.
  The paper notes its unbounded processing notion differs from that of Dodis, Quach and Wichs, whose
  unbounded processing adversary has unbounded computational power.
- **Antecedent:** the existence of one way functions, or of space bounded one way functions with space bound
  `poly(a)`, for the constructions. The converse derives that antecedent instead of assuming it, and in the
  multi round case derives only a weaker form.
- **Which party carries the resource bound:** the **adversary**, in two currencies at once. This is the fact
  the paper exists to establish. A space bound alone caps what is achievable, so the construction spends a
  computational assumption to buy back an arbitrary space gap, and the converse shows the assumption cannot be
  avoided in that regime. Honest parties are separately bounded at `s` bits.
- **Does not establish:** that one way functions are necessary for streaming key agreement with a
  superconstant number of rounds, which is stated as an open question. It does not obtain space bounded one
  way functions from a small space gap, `a ≫ s^2`, in the multi round case. The infinitely often and non
  uniform qualifiers on Theorem 4 are real weakenings, the first a standard consequence of the disjunction
  argument over a one way function inverter, the second removable only for a single long stream. It does not
  determine whether communication larger than `a` is necessary under one way functions, and Section 1.2
  explains that this reduces to an open question about key agreement from one way functions against
  polynomial time linear space adversaries, open even in the random oracle model.
- **Abstract versus theorem:** the abstract says "one-way functions are necessary for key agreement in the
  bounded-storage model with large space gaps", which is exact only for Theorem 3's single stream regime.
  Theorem 4's conclusion is weaker in two respects and its space gap hypothesis is stronger. The body says so
  plainly and calls the remaining gaps the main open question of the work.

## Key Contributions

- Key agreement in the streaming bounded storage model with an arbitrary polynomial space gap, one long
  round, and honest storage independent of the adversary's, from one way functions, with an everlasting
  security variant at one extra streaming round.
- The corresponding result from space bounded one way functions against fully streaming adversaries.
- A converse showing one way functions are necessary for streaming key agreement in the regime where it
  cannot exist unconditionally, tight against the positive result for single stream protocols.
- A space efficiency accounting for the standard reductions among Minicrypt primitives, offered as a target
  for future space tight reductions.

## Key Definitions / Theorems

- **SM-KA and UP-KA.** Key agreement in the streaming model against a fully streaming probabilistic
  polynomial time adversary, and against an unbounded processing probabilistic polynomial time adversary
  respectively. The unbounded processing model is the stronger setting for a construction and the fully
  streaming model is the stronger setting for an impossibility.
- **Theorem 1, informal.** Assuming one way functions, for any polynomial `a(λ)` there is a bounded storage
  key agreement in the streaming model secure against an eavesdropper with space `a`, using a single long
  stream of length `a · poly(λ)` followed by one `poly(λ)` sized short message, with honest storage
  `s = poly(λ)`.
- **Corollary 2, informal.** The same under space bounded one way functions with space bound `poly(a)`,
  against a fully streaming adversary.
- **Theorem 3, informal.** A streaming key agreement against space `a` adversaries with a single long stream,
  a short reply, and `s ≪ sqrt(a)` honest space implies one way functions in the unbounded processing case
  and space bounded one way functions in the fully streaming case.
- **Theorem 4, informal.** An `r` round streaming key agreement against space `a` adversaries with
  `s ≪ a^{1/polylog(r)^r}` implies non uniform infinitely often one way functions, or non uniform infinitely
  often space bounded one way functions `f : {0,1}^n → {0,1}^n` with space bound `n^{Ω(polylog(r)^r)}`.

## Connections

- [Speak Much, Remember Little](speak-much-remember-little.md) supplies both the streaming model and the
  round and communication lower bounds that motivate the question, and is cited here as [DQW23].
- [Authentication in the Bounded Storage Model](authentication-bounded-storage.md) is cited as the source of
  unconditional signatures in the model.
- [Bounded Storage Model](../concepts/bounded-storage-model.md).
- [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md) is the frame in which trading a space
  bound against a computational assumption is the natural operation. The exchange documented here is the
  clearest instance in this corpus of two adversary currencies priced against each other.
- [One-Way Functions](../concepts/one-way-functions.md).
- [Security Gap Exponent](../concepts/security-gap-exponent.md) names the quantity that the space gap
  `a` versus `s` instantiates.

## Open Questions / Limitations

- Whether streaming key agreement with a superconstant number of rounds implies one way functions.
- Whether space bounded one way functions follow from a smaller space gap, ideally `a ≫ s^2`, in the multi
  round case. A space tight reduction from space bounded distributional one way functions to one way
  functions is named as the natural first step.
- Whether communication larger than `a` remains necessary once one way functions are assumed. Below
  `sqrt(a)` communication the Barak and Mahmoody attack applies. Near `a` the question is equivalent to
  building key agreement from one way functions against polynomial time linear space adversaries, open even
  in the random oracle model.
- Theorem 4 gives only infinitely often and non uniform one way functions.

## Quotes / Notable Passages

- "we explore how a minimal use of cryptographic assumptions can help circumvent these lower bounds."
- "In the other direction, we show that one-way functions are necessary for key agreement in the
  bounded-storage model with large space gaps."
- "we actually show that one-way functions are essentially equivalent to streaming key agreement."
- "is it possible to build key agreement from one-way functions against polynomial-time linear space
  adversaries? Interestingly, this question remains wide open as of today"
