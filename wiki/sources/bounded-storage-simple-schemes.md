---
title: Simple Schemes in the Bounded Storage Model
type: source
date_ingested: 2026-08-21
authors: [Jiaxin Guan, Mark Zhandry]
venue: venue unconfirmed from PDF (the file carries no date and no venue line; recorded elsewhere in this repo as EUROCRYPT'19)
year: 2019
tags: [cryptography, bounded-storage-model, computational-indistinguishability, complexity-theory, one-way-functions]
claim_quantifier: universal
antecedent: "none. Security is unconditional. The structural hypothesis is that the adversary is a streaming algorithm holding at most Cn^2 memory bits for a constant C < 1/20, that honest parties hold O(n) bits, and that the honest parties can stream O(n^2) bits to each other."
adversary_bound: "memory. The adversary is computationally UNBOUNDED and is bounded only by S(n) = Cn^2 memory bits, C < 1/20, inherited from Raz's parity bound."
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
cls_second_notion: queries
cls_assessed: explicit
cls_evidence: "The bounded storage model promises unconditional security proofs against computationally unbounded adversaries, so long as the adversary's space is bounded."
cls_evidence_src: abstract
cls_reason: "Adversary bounded by memory (Def 1, S(n)) and separately by queries Q(n) in the same definition. Honest Keeper/Recorder also memory-bounded at O(n)/O(lambda n) (second_party=memory). Storage gap stated relative to honest party's O(n) usage (quadratic, per Connections and Open Questions), giving tightness=exponent rather than budget."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The bounded storage model gives unconditional security against a computationally unbounded adversary whose
storage is bounded. Most earlier constructions in the model rest on a birthday argument, in which each honest
party records a random subset of positions in a long stream and the two parties hope to collide. This paper
replaces that machinery with Raz's parity encryption scheme and rebuilds two party key agreement, bit
commitment and oblivious transfer on top of it. The gains are simplicity, fewer rounds, and perfect rather
than statistical correctness.

The technical core is an *Encrypt Zero* protocol. One party, the Keeper, holds a random key `k` in `{0,1}^n`
and streams `m = O(n)` encryptions of zero under Raz's scheme. The other party, the Recorder, holds a secret
matrix `Σ` and folds the incoming ciphertexts into random subset sums on the fly, ending with `λ` fresh
encryptions of zero. Keeper security says the key retains `Omega(n)` min entropy given the Recorder's view,
and follows directly from Raz's theorem. Recorder security says the Keeper learns nothing about which subset
sums were taken, and follows because `Σ` never leaves the Recorder. The Keeper uses `O(n)` space and the
Recorder uses `O(λn)`, both optimal for the information each must hold.

Key agreement is Encrypt Zero with `λ = 1` followed by one message back. Bit commitment runs Encrypt Zero,
then the Committer sends an encryption of the bit and later reveals the key, which the Verifier checks against
its stored encryptions of zero. Oblivious transfer turns the commitment into a transfer by exploiting additive
homomorphism and re-randomising with fresh encryptions of zero. An *Enhanced* Encrypt Zero protocol, in which
the Keeper streams encryptions of an independent secret `s` of length `m = 2n` and then reveals `k` in the
clear, removes the need to trust the Keeper's randomness, at roughly double the communication. The two
properties of Raz's scheme that carry all of this are leakage resilience, because the inner product is a
strong extractor, and additive homomorphism.

## Claim Boundary

- **Quantified over:** all adversaries that use at most `S(n)` memory bits, with no restriction whatever on
  running time. Definition 1 and Definition 6 both quantify only over memory. Query counts are bounded
  separately, at `2^{alpha n}` or `2^{alpha n /4}` depending on the security notion.
- **Antecedent:** none. Security is information theoretic. The constant inherits Raz's constraint `C < 1/20`.
- **Which party carries the resource bound:** the **adversary**, and here alone in this cluster the bounded
  party is genuinely an attacker. Honest parties are constrained too, at `O(n)` space for the Keeper and
  `O(λn)` for the Recorder, but the security statement quantifies over adversarial memory. The attacker is a
  passive eavesdropper for key agreement and a malicious protocol participant for commitment and transfer.
- **Does not establish:** anything once the adversary's memory exceeds `Cn^2`. The quadratic gap is hard for
  these schemes, and breaking past it is the subject of
  [Speak Much, Remember Little](speak-much-remember-little.md). Binding for the commitment scheme is
  `2^{-λ}` and is not information theoretic in the adversary's memory, it comes from the Verifier's hidden
  choice of `Σ`. Sender security for oblivious transfer is perfect while receiver security is the memory
  bounded statement. The paper gives indistinguishability based security, not simulation based security.
- **Abstract versus theorem:** the abstract claims "an improved number of rounds and enhanced correctness"
  and the body delivers exactly that, one round bit commitment and two round oblivious transfer against five
  in prior work, with `Pr[a = b] = 1` for key agreement. No overreach found.

## Key Contributions

- The Encrypt Zero protocol and its enhanced variant, an abstraction of the common pattern in which one party
  ends with a key and the other with fresh encryptions of zero under that key.
- Round optimal bit commitment, one round, and oblivious transfer, two rounds, in the bounded storage model,
  against five rounds in Ding, Harnik, Rosen and Shaltiel.
- Key agreement with perfect correctness and statistical security for adversarial space `O(n^2)`, where the
  birthday based schemes achieve only constant success probability and require the adversary's space to be
  asymptotically smaller than `n^2`.
- The observation that Raz's encryption scheme is additively homomorphic and leakage resilient, which is what
  makes the higher level protocols simple.

## Key Definitions / Theorems

- **Definition 1, Real or Random Ciphertext security.** A scheme is `(S(n), Q(n), ε)`-secure if for all
  adversaries using at most `S(n)` memory bits and at most `Q(n)` adaptive queries, the advantage in
  distinguishing real ciphertexts from random ones is at most `ε`.
- **Theorem 1 and Corollary 1.** For any `C < 1/20` there is `alpha > 0` such that the bit encryption scheme
  from parity learning is `(Cn^2, 2^{alpha n}, O(2^{-alpha n/2}))`-secure under the modified notion, and
  `(Cn^2, 2^{alpha' n}, O(2^{-alpha' n}))`-secure under the plain notion.
- **Definitions 3 to 5.** Keeper security is a min entropy condition on the key given the Recorder's view.
  Recorder security comes in an honest but curious version and a malicious Keeper version.
- **Theorems 2 to 5.** Keeper and Recorder security of both the simple and the enhanced Encrypt Zero
  protocols, the enhanced one being perfectly secure against a malicious Keeper.
- **Definition 6 and Theorem 6.** Eavesdropping security of key agreement quantifies over adversaries using
  at most `S(n)` memory bits, and the construction is `(Cn^2, O(2^{-alpha n/2}))`-secure.
- **Theorems 7 to 10.** Hiding at `(Cn^2, O(2^{-n/2}))` and binding at `2^{-λ}` for the commitment, perfect
  Sender security and `(Cn^2, O(2^{-n/2}))` Receiver security for the transfer.

## Connections

- [Raz, Fast Learning Requires Good Memory](raz-parity-time-space.md) supplies Theorem 1 and therefore every
  security proof here.
- [Bounded Storage Model](../concepts/bounded-storage-model.md) records the two variants of the model and the
  quadratic shape of the storage gap.
- [Authentication in the Bounded Storage Model](authentication-bounded-storage.md) adds message
  authentication and signatures to the same list of primitives.
- [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md) places the memory axis beside time.
- [Fine-Grained ERM](fine-grained-erm.md) is the learning side counterpart, where the priced resource is time
  and the priced party is the learner.

## Limits

- [Speak Much, Remember Little](speak-much-remember-little.md) shows the quadratic ceiling these
  constructions stop at is not a property of the streaming model, only of a more restricted variant, and
  reaches `m = 2^{O(n)}` at a communication and round cost. The schemes here remain confined to `m = O(n^2)`.
- [On Bounded Storage Key Agreement and One-Way Functions](bsm-key-agreement-owf.md) shows that beyond the
  unconditional regime a computational assumption is not merely convenient but necessary, so the
  assumption free character of the constructions here is exactly what caps their space gap.

## Open Questions / Limitations

- The schemes stop at a quadratic storage gap.
- Oblivious transfer here satisfies an indistinguishability based sender privacy, not simulation based
  security with an efficient simulator.
- The commitment's binding property is `2^{-λ}` and depends on the Verifier's hidden matrix, so it is not a
  storage bound statement.

## Quotes / Notable Passages

- "The bounded storage model promises unconditional security proofs against computationally unbounded
  adversaries, so long as the adversary's space is bounded."
- "Our schemes are based on Raz's lower bound for learning parities."
- "we get perfect correctness and statistical security for adversarial space bounds" and "The honest users only
  require O(n) space."
