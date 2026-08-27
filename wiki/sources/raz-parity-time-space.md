---
title: "Fast Learning Requires Good Memory: A Time-Space Lower Bound for Parity Learning"
type: source
date_ingested: 2026-08-21
authors: [Ran Raz]
venue: venue unconfirmed from PDF (arXiv:1602.05161v1 [cs.LG], 16 Feb 2016; recorded elsewhere in this repo as FOCS'16)
year: 2016
tags: [complexity-theory, learning-theory, cryptography, sample-complexity, one-way-functions, bounded-storage-model]
claim_quantifier: universal
antecedent: "none. The bound is unconditional. The only structural hypotheses are that the target is drawn uniformly from {0,1}^n, that samples arrive as a stream and cannot be revisited unless stored, and that the algorithm is modelled as a branching program."
adversary_bound: "none for the learning theorem itself. The memory bound sits on the LEARNER (at most cn^2 bits, c < 1/20). In the paper's own encryption corollary the same party is renamed the attacker, and that is the one place a memory-bounded attacker appears."
model_class: parity functions over {0,1}^n, target uniform
algorithm_class: branching programs of width at most 2^{cn^2} and length at most 2^{alpha n}, non-uniform
cls_target: none
cls_family: none
cls_phase: train time
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: memory
cls_tightness: budget
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: absent
cls_evidence_src: "classified by hand in the first batch, before the evidence requirement was added to the brief"
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows."
cls_prov: hand
cls_date: 2026-08-22
---

## Summary

Parity learning is the problem of recovering a uniformly random `x` in `{0,1}^n` from a stream of samples
`(a_t, b_t)` with `a_t` uniform and `b_t = a_t · x` mod 2. Two extreme algorithms are known. Gaussian
elimination uses `O(n)` samples and `O(n^2)` memory bits. Exhaustive search uses `n + o(n)` memory bits and
exponentially many samples. This paper proves there is nothing useful in between. Any algorithm that uses
fewer than roughly `n^2/20` memory bits needs an exponential number of samples.

The learner is modelled by a branching program, the standard non uniform model for time and space tradeoffs.
Each layer is a time step and each vertex is a memory state, so width `2^{cn^2}` corresponds to `cn^2` memory
bits and length corresponds to sample count. The proof has two halves. Lower bounds are proved first for
*affine* branching programs, whose vertices are labelled by affine subspaces known to contain `x`, by tracking
the dimension of an intersection of orthogonal spaces and observing that it can only grow when the sample
currently read falls in a small subspace. General branching programs are then reduced to affine ones, at a
width blowup of `2^{Theta(n^2)}` that the argument can afford only because the constant in the exponent is
kept small.

The paper also draws a cryptographic corollary, and this is the one place in the memory bounded literature
where the memory bounded party is named the attacker rather than the learner. Alice and Bob share `x`. To
send one bit `M`, Alice publishes a fresh uniform `a` and sends `M ⊕ (a · x)`. An attacker who watches
`m` such transmissions is exactly a parity learner, so an attacker with fewer than about `n^2/20` memory bits
cannot recover `x`, and because the inner product is a strong extractor the attacker also cannot predict the
next masking bit. Encryption and decryption cost time `n` per bit while the attacker's memory bound is
quadratic in `n`. Earlier bounded storage work required the number of transmitted random bits to exceed the
attacker's memory, so encryption time was at least linear in the attacker's memory. The paper states its own
limit on the gain. Remark 1.2 says that for messages of length `m ≥ n` the protocol costs time `mn` and has
no advantage over previous ones, so the benefit is confined to many short messages.

## Claim Boundary

- **Quantified over:** all branching programs for parity learning of width at most `2^{cn^2}` and length at
  most `2^{alpha n}`, for any `c < 1/20`. Non uniform, so the statement covers algorithms with arbitrary
  preprocessed advice. Average case in the target, since `x` is uniform, not worst case over `x`.
- **Antecedent:** none. The result is unconditional and rests on no complexity assumption.
- **Which party carries the resource bound:** the **learner**. Theorem 1 bounds the memory of the algorithm
  that is trying to learn. The security reading in Section 1.3 relabels that same party as the attacker
  against a one time pad built from inner products, which is the single point in this cluster where a memory
  bound is placed on an attacker rather than on an honest party. Nothing in the paper bounds the memory of an
  adversary attacking a *learned model*.
- **Does not establish:** any statement about time bounded learners, about worst case targets, about
  algorithms that may re-read earlier samples, or about learning problems other than parity. It gives no
  lower bound on memory for algorithms allowed exponentially many samples beyond `2^{alpha n}`, and it does
  not rule out a memory efficient learner for a *noisy* parity variant, which is not treated.
- **Abstract versus theorem:** the abstract states the threshold as `n^2/25` memory bits, while Theorem 1 and
  Theorem 2 are stated for any `c < 1/20`, that is up to `n^2/20`. The abstract is therefore weaker than the
  theorem, not stronger. Remark 1.1 records a second boundary: the conjecture of Steinhardt, Valiant and
  Wager with constants `1/4` and `1/4` is "too strong" as stated, and footnote 1 gives the algorithm that
  refutes it, so what is proved is the qualitative conjecture with different constants. Theorem 2 is the
  formal statement and is stronger than Theorem 1, since it allows the program to output an affine subspace
  of dimension at most `(3/5)n` and bounds the probability that `x` lies in it.

## Key Contributions

- The first non trivial sample lower bound for any learning problem under a memory constraint, even at memory
  linear in the length of a single sample.
- Proof of the qualitative form of Conjecture 1.1 of Steinhardt, Valiant and Wager, with different constants,
  and an explicit refutation of the constants as originally stated.
- A bounded storage encryption scheme whose encryption and decryption time is `n` per bit while the attacker's
  memory bound is quadratic in `n`, decoupling honest running time from adversarial storage.
- The affine branching program technique, together with the wasteful reduction from general branching
  programs, which later work in this area reuses as a black box.

## Key Definitions / Theorems

- **Branching program for parity learning.** Vertices arranged in `m + 1` layers of width at most `d`, one
  start vertex, every non leaf vertex carrying `2^{n+1}` outgoing edges labelled by `(a,b)`. Width is the
  memory measure and length is the sample measure.
- **Affine branching program.** Every vertex `v` is labelled by an affine subspace `w(v)`, the start vertex
  by `{0,1}^n`, and for every edge `(u,v)` labelled `(a,b)` the containment
  `w(u) ∩ {x' : a · x' = b} ⊆ w(v)` holds, so reaching `v` guarantees `x ∈ w(v)`. An affine program is
  *accurate* when, for almost every vertex, the conditional distribution of `x` given that the computation
  path reached `v` is close to uniform on `w(v)`.
- **Theorem 1.** For any `c < 1/20` there is `alpha > 0` such that for uniform `x`, `m ≤ 2^{alpha n}`
  samples, and any algorithm using at most `cn^2` memory bits and outputting a string `x̃`, the success
  probability satisfies `Pr[x̃ = x] ≤ O(2^{-alpha n})`.
- **Theorem 2.** The same bound for branching programs of length at most `2^{alpha n}` and width at most
  `2^{cn^2}` whose output is always an affine subspace of dimension at most `(3/5)n`, bounding the probability
  that `x` lies in the output subspace.

## Connections

- [Bounded Storage Model](../concepts/bounded-storage-model.md) is the model the encryption corollary lives
  in, and the streaming variant of it is the one this paper's technique opened up.
- [Simple Schemes in the Bounded Storage Model](bounded-storage-simple-schemes.md) builds key agreement, bit
  commitment and oblivious transfer directly on Theorem 1.
- [Authentication in the Bounded Storage Model](authentication-bounded-storage.md) restates Theorem 1 as its
  Theorem 6.2 and uses it to build the short tag MAC.
- [Speak Much, Remember Little](speak-much-remember-little.md) identifies this line as the work that first
  departed from the traditional bounded storage restrictions.
- [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md) is the general frame in which memory
  is one priced axis alongside time and parallel time.
- [What Can We Learn Privately?](what-can-we-learn-privately.md) prices the learner in a different currency,
  statistical queries under a privacy constraint, and leaves the adversary unmeasured. The pairing shows the
  same structural choice of which party gets measured.
- [Fine-Grained ERM](fine-grained-erm.md) and
  [Overparameterization and Computational Constraints](overparameterization-computational-constraints.md)
  price the learner in time rather than space.

## Open Questions / Limitations

- The constant is not optimal. What is proved is `c < 1/20` and footnote 1 shows the true threshold is below
  `1/4`, so the gap between `1/20` and the algorithmic upper bound is open here.
- Nothing is said about noisy parity, about learning problems with structure other than linear algebra, or
  about time bounded rather than space bounded learners.
- Remark 1.2 bounds the practical reach of the encryption corollary. For messages of length at least `n` the
  scheme has no advantage over earlier bounded storage constructions.
- The reduction from general to affine branching programs costs a `2^{Theta(n^2)}` width blowup, which is why
  the admissible constant is small.

## Quotes / Notable Passages

- "We prove that any algorithm for learning parities requires either a memory of quadratic size or an
  exponential number of samples."
- "in some cases, learning is infeasible, due to memory constraints."
- "there was no previous non-trivial lower bound on the number of samples needed, for any learning problem"
- "In previous works, the number of random bits transmitted during the encryption was assumed to be larger than
  the memory-size of the attacker. Thus, the time needed for encryption/decryption was at least linear in the
  memory-size of the attacker."
