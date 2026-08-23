---
title: Authentication in the Bounded Storage Model
type: source
date_ingested: 2026-08-21
authors: [Yevgeniy Dodis, Willy Quach, Daniel Wichs]
venue: venue unconfirmed from PDF (the file is dated May 31, 2022 and carries no venue line; recorded elsewhere in this repo as EUROCRYPT'22)
year: 2022
tags: [cryptography, bounded-storage-model, computational-indistinguishability, complexity-theory]
claim_quantifier: universal
antecedent: "none. All results are unconditional. The structural hypotheses are that every party is a streaming algorithm, that honest parties hold n bits of memory, that the adversary holds m bits throughout, and that the number of oracle queries is at most Q = 2^lambda."
adversary_bound: "memory. The adversary is a streaming algorithm with m bits of memory, computationally unbounded, in the man in the middle position on the channel. Definition 3.5 for MACs and Definition 3.11 for signatures fix the class."
cls_target: none
cls_family: forge
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: attacker
cls_unit: memory
cls_tightness: exponent
cls_baseline: stated
cls_second_party: memory
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "Suppose that (KeyGen, KeyReceive, Sign, Verify) is (ε, A)-suf-cma-secure (Definition 3.10). Then m = O(n2 )."
cls_evidence_src: Thm 7.11
cls_reason: "target/access/write=none and phase=n/a: no ML asset (train data, parameters, outputs, a training run) is present -- this is a general-purpose crypto primitive, and none of the vocabulary's access/write values (all ML-query-oriented) fit a streaming man-in-the-middle channel adversary. family=forge is the generic cryptographic sense (MAC/signature unforgeability), not the ML-specific 'forge a training artifact' sense used elsewhere in this codebook. frame=compute per the brief's own definition, which lists memory alongside time, circuit size, queries and algo class as a compute resource, even though the paper calls the adversary 'computationally unbounded' in TIME -- memory is still the bound. party=attacker over the honest parties per rule 4: both the adversary (m bits) and the honest parties (n bits) are memory-bounded, both bounds are computational, so the adversary's bound decides the row and the honest parties' memory n goes to second_party. tightness=exponent chosen from Theorem 7.11's matching lower bound (m=O(n^2), the only bound in the paper proved optimal inside the paper rather than by an external counting argument in a footnote); the long-tag MAC construction (Thm 5.1) separately achieves m=2^{O(n)}, a different exponent relation, so a single row understates the paper's range -- flagged as a multi-construction paper. baseline=stated because the security definitions (Def 3.5/3.10/3.11) carry an explicit epsilon tolerance for forgery success."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

Confidentiality in the streaming bounded storage model was settled before authenticity was. This paper adds
message authentication codes and public key signatures to the model. The setting is the streaming variant.
Honest parties hold `n` bits of memory and process everything one bit at a time, the adversary holds `m ≫ n`
bits and sits on the channel, observing and modifying everything. The traditional bounded storage model does
not pose the problem in the same way, because it hands every party the same trusted randomizer string and so
already assumes the authentication mechanism the streaming model must build.

Three results follow. First, a symmetric key MAC with long tags. Alice authenticates arbitrarily many
messages by streaming tags of size `k = O(m + λ log λ)` while she and Bob each use memory
`n = O(λ + polylog(m, λ))`. Adversarial memory may be as large as `2^{O(n)}`, at the price of tags that grow
with it, so polynomial size tags force `m` to be a large polynomial. The construction combines a local
extractor of Vadhan with a streaming one time information theoretic MAC.

Second, a MAC whose individual tags are short enough for an honest party to store, of size `O(n)`. Here
adversarial memory is limited to roughly `n^2`. This construction is the one that uses Raz's parity bound,
restated as Theorem 6.2 and converted into two pseudorandomness corollaries for parities. Note that the
optimality of the quadratic bound for short tag MACs does not come from Raz. Footnote 4 attributes it to the
standard authentication counting argument, that an adversary able to store `n` tags produced under an `n` bit
key has enough information to forge.

Third, public key signatures. Alice streams a long verification key over an authentic channel while keeping
a short signing key, Bob compresses the streamed key into a short verification digest, and afterwards Alice
signs by streaming large signatures that Bob checks against his digest. Memory is
`n = Õ(λ^3 + sqrt(m) λ)` and signatures have size `Õ(m + λ^{3/2})`, so again `m = O(n^2)`. This time the
optimality is proved inside the paper. Theorem 7.11 exhibits an explicit memory bounded forger, and the
supporting tool is a new block entropy lemma stating that a string with high min entropy rate must have a
large set of blocks whose individual min entropy is high, once the set is allowed to be chosen after seeing
the string.

## Claim Boundary

- **Quantified over:** all streaming adversaries with `m` bits of memory making at most `Q = 2^λ` oracle
  queries, in a chosen message and chosen verification attack. Definition 3.5 restricts the adversary to one
  concurrent tagging call and one concurrent verification call at a time, and the paper argues that this is
  reasonable for a single verifier channel. Signature adversaries observe but cannot modify the streamed
  verification key during initialisation.
- **Antecedent:** none. Every theorem is unconditional.
- **Which party carries the resource bound:** **both**, and the security statement quantifies over the
  adversary's memory. This is the second paper in this cluster, with
  [Guan and Zhandry](bounded-storage-simple-schemes.md), whose bounded party is an attacker. The honest
  parties are separately and more tightly bounded at `n` bits, which is what makes the model non trivial, but
  the quantifier in Definitions 3.3, 3.4 and 3.10 ranges over adversaries in a memory defined class `A`. No
  bound is placed on adversarial running time.
- **Does not establish:** short tag authentication beyond `m = O(n^2)`, nor signatures beyond `m = O(n^2)`.
  Theorem 7.11 rules the latter out. It says nothing about authentication in the traditional bounded storage
  model, where the problem is already assumed away, and nothing about computational assumptions, which are
  not used and not needed.
- **Abstract versus theorem:** the abstract's phrase "which is optimal" for the short tag MAC is supported by
  a counting argument in footnote 4 rather than by a theorem in the paper, while the same phrase for
  signatures is supported by Theorem 7.11. The two "optimal" claims therefore rest on different evidence and
  should not be cited interchangeably. Remark 7.14 notes that Theorem 7.11 is stated for non uniform
  adversaries and extends to uniform ones by guessing the index, at a `1/q` loss.

## Key Contributions

- Message authentication and signatures in the streaming bounded storage model, the two primitives the prior
  bounded storage literature had left out.
- A MAC tolerating exponentially large adversarial memory `m = 2^{O(n)}` with tags of size `O(m)`.
- A MAC with tags short enough to fit in honest memory, at `m = O(n^2)`, built on Raz's parity bound.
- Signatures at `m = O(n^2)`, with a matching lower bound, Theorem 7.11, proved by constructing a memory
  bounded forger that samples a signing key consistent with `i` independently derived verification digests.
- The block entropy lemma, Lemma 4.1 and Corollary 4.2, correcting the naive and false min entropy analogue
  of the Shannon subadditivity bound.

## Key Definitions / Theorems

- **Definition 3.2, streaming MAC with memory `n`.** Tagging and verification are streaming algorithms with
  memory `n` given streaming access to the message and to the message and tag, and key generation runs in
  place with memory `n`, so keys have size at most `n`.
- **Definition 3.5, streaming adversaries for MACs.** The adversary is a streaming algorithm accessing the
  tagging and verification oracles in a streaming manner using total memory at most `m`, with input and
  output streams that need not be synchronised, and at most one concurrent call per oracle.
- **Theorem 5.1, MAC with long tags.** For all `m, λ` there is a streaming MAC with memory
  `n = O(λ + polylog(m, λ))` authenticating messages of length up to `2^λ`, which is
  `(2^{-λ}, A)`-unforgeable under chosen message and verification attacks against streaming adversaries with
  memory `m` making at most `Q = 2^λ` queries, with streamed tags of size `O(m + λ log λ)`.
- **Theorem 6.1, MAC with short tags.** The same, with memory `n = O(λ sqrt(m) + λ^2)`, messages of length up
  to `2^{O(n)}`, and tags of size `O(n)`.
- **Theorem 6.2, restating Raz.** For integer `k` there are constants `C, alpha > 0` such that an algorithm
  reading a stream `(a_i, b_i)` with `b_i = <a_i, s>` and `Q ≤ 2^{alpha k}` samples, using at most `Ck^2`
  memory, recovers `s` with negligible probability. Lemma 6.3 and Corollary 6.4 turn this into
  pseudorandomness of parities, and both explicitly allow the adversary *unbounded temporary memory*.
- **Theorem 7.1, signatures.** Streaming signature scheme with memory `n = Õ(λ^3 + sqrt(m) λ)`, unforgeable
  under chosen message and verification attacks against streaming adversaries with memory `m` and at most
  `Q = 2^λ` queries, with signatures of size `Õ(m + λ^{3/2})`.
- **Theorem 7.11, the signature lower bound.** If a streaming signature with memory `n` is `(ε, A)`-selectively
  unforgeable against streaming adversaries with memory `m`, then `m = O(n^2)`. Proved by an adversary that
  runs `i = O(n)` copies of the key receiving procedure, then rejection samples a signing key whose digests
  match, and signs the target message itself.
- **Lemma 4.1, block entropy.** If `X = (X_1, …, X_k)` has `H_∞(X) ≥ α·kb` then with overwhelming
  probability there is a set `I(x)` of at least `α_1 k` indices such that `H_∞(X_i | i ∈ I(X))` is high, for
  `α_1 ≈ α_2 ≈ α/2`. The paper gives the counterexample showing the fixed index version is false.

## Connections

- [Raz, Fast Learning Requires Good Memory](raz-parity-time-space.md) is restated here as Theorem 6.2 and
  drives the short tag construction.
- [Simple Schemes in the Bounded Storage Model](bounded-storage-simple-schemes.md) covers key agreement,
  commitment and transfer in the same model and at the same quadratic gap.
- [Speak Much, Remember Little](speak-much-remember-little.md) is the companion paper by the same authors,
  cited here as [DQW21], which breaks the quadratic gap for key agreement and transfer. The signature lower
  bound in Theorem 7.11 uses Lemma 7.13 from that work.
- [Bounded Storage Model](../concepts/bounded-storage-model.md) records the distinction between the
  traditional and streaming variants that Section 1 sets out in four numbered differences.
- [On Bounded Storage Key Agreement and One-Way Functions](bsm-key-agreement-owf.md) cites the signature
  result here as one of the unconditional bounded storage primitives.
- [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md).

## Open Questions / Limitations

- Whether the quadratic gap for short tag MACs and for signatures can be broken by allowing many long rounds,
  the move that works for key agreement in the companion paper, is not resolved here. Theorem 7.11 constrains
  signatures under the definitions given.
- The concurrency restriction in Definition 3.5, one live tagging call and one live verification call, is
  argued to be reasonable rather than shown to be without loss of generality.

## Quotes / Notable Passages

- "The adversary also operates as a streaming algorithm, but has a much larger memory size m  n."
- "Our solution relies on a space lower bound for leaning parities (Raz; FOCS '16)."
- "Optimality follows from the standard authentication lower bound; if an adversary has enough memory to
  store n tags (generated using an n bit key) then it has enough information to forge tags of new messages."
- "Naive versions of this lemma are false, but we show how to patch it to make it hold."
