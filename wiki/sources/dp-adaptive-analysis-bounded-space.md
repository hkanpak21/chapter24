---
title: On Differential Privacy and Adaptive Data Analysis with Bounded Space
type: source
date_ingested: 2026-08-21
authors: [Itai Dinur, Uri Stemmer, David P. Woodruff, Samson Zhou]
venue: venue unconfirmed from PDF (the file is dated February 11, 2023 and carries no venue line; recorded elsewhere in this repo as EUROCRYPT'23)
year: 2023
tags: [differential-privacy, adaptive-data-analysis, cryptography, complexity-theory, computational-indistinguishability, hardness-reductions]
claim_quantifier: conditional
antecedent: "Existence of a Gamma(lambda)-secure symmetric-key encryption scheme against non-uniform adversaries, with Omega(lambda) <= Gamma(lambda) <= 2^{o(lambda)}, for the differential privacy separation (Corollary 3.13). Existence of one-way functions for the adaptive data analysis space lower bound (Theorem 4.1, via the same encryption primitive)."
adversary_bound: "none — the bound is on the MECHANISM. The space bound s constrains the summary the algorithm may keep. The adversary built against the mechanism is bounded in TIME, at poly(Gamma(lambda)), and carries no space bound at all."
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: mechanism
cls_unit: memory
cls_tightness: conditional
cls_baseline: n/a
cls_baseline_checked: yes
cls_second_party: time
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "there exists a poly(Γ(λ))-time adversary B such that the following holds. Let A=(A1, A2) be a poly(Γ(λ))-time mechanism with space complexity s ≤ O(λ·√k) (small enough)."
cls_evidence_src: Thm 4.1
cls_reason: "Not an ML attack scenario, so target/family/phase/access/write=none: no train data, model or output is targeted, only a two-party resource complexity separation. party=mechanism per rule 3 as directed: the space bound s binds the mechanism A1, not the time-bounded adversary B of Thm 4.1/Cor 3.13, so party=mechanism/unit=memory and the adversary's poly(Γ(λ))-time bound is recorded as second_party=time. tightness=conditional because both main theorems hold only given a Γ(λ)-secure encryption scheme, matching the front matter's claim_quantifier and antecedent. baseline=stated: Thm 4.1 fixes the game's success threshold at Pr[AdaptiveGameSpace=1] > 2/3, and Cor 3.13 fixes ε, δ explicitly."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

Two space complexity results, joined by one cryptographic tool. The first separates private from non private
computation by space. There is a problem `P` solvable non privately in `polylog(d)` bits of space, solvable
privately with sample and space complexity `Õ(sqrt(d))`, and, under a sub exponentially secure symmetric key
encryption scheme, requiring space `Ω̃(sqrt(d))` for any computationally efficient differentially private
algorithm, however many samples it is given. The separation is exponential in `d` and holds even when the
algorithm is only required to be computationally differentially private. The authors state the caveat
themselves, that the problem `P` is somewhat unnatural, and they rule out a trivial construction first by
insisting the private and non private algorithms compute the same function.

The second result rereads the adaptive data analysis literature. That literature asks how many samples a
mechanism needs to answer `k` adaptively chosen queries accurately with respect to the underlying
distribution, and the known answer is `Θ̃(sqrt(k))` for computationally efficient mechanisms. This paper gives
the mechanism the *full description* of the distribution and requires only that it compress that description
into an `s` bit summary before the queries arrive. Theorem 4.1 shows `s = Ω(sqrt(k))` is still necessary. The
bottleneck was never the sampling. Drawing `t` points is one particular way of storing information about the
distribution, and no other way does better.

The tool is a multi instance leakage resilient encryption scheme. It runs `n` independent instances with
independent `λ` bit keys. An adversary sees all `n` keys and compresses them to `s ≪ n·λ` bits, then each
instance draws a public parameter unknown during the compression phase, and then the adversary receives
ciphertexts. The requirement is that the plaintexts stay computationally hidden under all but `O(s/λ)` of the
keys. That count is essentially optimal, since the adversary can simply store the first `s/λ` keys verbatim,
and the construction loses only a constant factor in the security parameter. The technique is a lifting one,
translating sampling lower bounds into space lower bounds in the spirit of query to communication lifting.

## Claim Boundary

- **Quantified over:** all computationally efficient, that is `poly(Γ(λ))` time, mechanisms `A = (A_1, A_2)`
  with space complexity `s`, where `A_1` compresses the dataset or distribution into `s` bits and `A_2`
  answers using only that summary. For the differential privacy result the quantifier ranges over
  `(ε, δ)`-computationally differentially private algorithms, which is the weaker privacy notion and hence
  the stronger negative result.
- **Antecedent:** a `Γ(λ)`-secure encryption scheme against non uniform adversaries for both main theorems,
  with `Ω(λ) ≤ Γ(λ) ≤ 2^{o(λ)}`, stated as one way functions in the informal version of Theorem 1.10. The
  parameters are tied, `d ≤ poly(Γ(λ))` and `k ≤ poly(Γ(λ))`, and `δ ≤ Θ(1/n)`.
- **Which party carries the resource bound:** the **mechanism**, not the adversary. In Corollary 3.13 the
  space `s` is the length of the summary the private algorithm keeps. In Theorem 4.1 and its game
  `AdaptiveGameSpace`, step 2 has the mechanism `A_1` receive the distribution and summarise it into `s` bits,
  while the adversary `B` is quantified as a `poly(Γ(λ))` *time* algorithm with no space restriction. Both
  results are therefore space lower bounds on the defender, and neither prices an attacker in memory.
- **Does not establish:** any space bound on an adversary, any statement for information theoretically
  private mechanisms, or any separation on a natural problem. The paper concedes the constructed problem `P`
  is "somewhat unnatural" and contrasts it with the adaptive data analysis result, which does concern the
  canonical problem of that literature. The computational model is a two phase summarise then answer model
  rather than a general streaming model, though Remark 3.3 states the results extend to the streaming setting.
- **Abstract versus theorem:** the abstract's "first separation between the space complexity of private and
  non-private algorithms" is qualified in the body by the unnaturalness of `P` and by the cryptographic
  antecedent. The claim that the adaptive data analysis bounds "are a consequence of a space bottleneck
  rather than a sampling bottleneck" is supported by Theorem 4.1 in the summarise then answer model, and is a
  generalisation of the Hardt and Ullman and Steinke and Ullman lower bounds rather than a replacement for
  them.

## Key Contributions

- The first separation between the space complexity of private and non private algorithms, exponential in the
  problem size parameter, holding even against computational differential privacy.
- A space lower bound of `Ω(sqrt(k))` for adaptive data analysis in a model where the mechanism is handed the
  distribution itself, reframing the known sample lower bounds as space lower bounds.
- The multi instance leakage resilient encryption scheme, optimal in both the number of compromised keys and
  the loss in the security parameter, with internal parameters independent of the leakage budget `s`.
- A technique for lifting sampling lower bounds to space lower bounds in privacy and adaptive data analysis,
  adapted from query to communication lifting and from the preprocessing adversary literature.

## Key Definitions / Theorems

- **Definition 1.3, bounded space solution.** `A = (A_1, A_2)` solves `P : X* × Q → M` with space `s`, sample
  complexity `n`, error `α` and confidence `β` if `A_1 : X* → {0,1}^s` preprocesses the dataset into `s` bits
  and `A_2` answers each query from the summary alone, within `α` with probability `1 − β`.
- **Theorem 1.4, informal, and Corollary 3.13.** For the `(λ, d)`-DA problem, every `poly(Γ(λ))` time
  `(ε, δ)`-computationally differentially private algorithm with sample complexity `n` must have space
  `s = Ω(λ · sqrt(d / log n))`, given a `Γ(λ)`-secure encryption scheme against non uniform adversaries,
  `n ≤ poly(Γ(λ))`, constant `ε`, and `δ ≤ 1/(4n(e^ε + 1))`. Lemma 3.2 gives the non private algorithm at
  `s = O(λ log d)` and Lemma 3.4 the private one at `Õ(sqrt(d))`.
- **Definition 1.6, the adaptive data analysis game.** The adversary picks a distribution, the mechanism gets
  `t` i.i.d. samples, and over `k` rounds the adversary picks `h_j : X → {−1,0,1}` adaptively while the
  mechanism answers `z_j`. Accuracy is measured against `h_j(P) = E_{x∼P}[h_j(x)]`.
- **Theorem 4.1 and `AdaptiveGameSpace`.** Given a `Γ(λ)`-secure encryption scheme against non uniform
  adversaries and `k ≤ poly(Γ(λ))`, there is a `poly(Γ(λ))` time adversary `B` such that every
  `poly(Γ(λ))` time mechanism `A = (A_1, A_2)` with space `s ≤ O(λ·sqrt(k))` fails, that is the game outputs
  one with probability greater than `2/3`. In the game the mechanism receives the full distribution `D` and
  must compress it to `s` bits.
- **Multi instance leakage resilient scheme.** `n` independent instances, adversarial leakage `z` of `s` bits
  computed from all `n` keys, public parameters drawn after the leakage, and computational hiding for all but
  `O(s/λ)` of the keys.

## Connections

- [Preventing False Discovery in Interactive Data Analysis is Hard](preventing-false-discovery-hard.md) is
  the sample lower bound this paper generalises, and the encryption trick that makes the analyst's queries
  opaque to the mechanism is the same device in both.
- [Adaptive Data Analysis](../concepts/adaptive-data-analysis.md).
- [Computational Differential Privacy](../concepts/computational-differential-privacy.md) is the privacy
  notion the negative result is stated against, which strengthens it.
- [Separating Adaptive Streaming from Oblivious Streaming](adaptive-vs-oblivious-streaming.md) makes the
  complementary move, reducing adaptive data analysis to streaming and placing the space bound on the
  streaming algorithm.
- [What Can We Learn Privately?](what-can-we-learn-privately.md) prices the same defender side in a different
  currency, statistical queries under local differential privacy.
- [Bounded Storage Model](../concepts/bounded-storage-model.md) is the mirror image, where the space bound
  sits on the attacker instead.
- [Capacity Bounded Privacy](../concepts/capacity-bounded-privacy.md) is the one privacy notion in this
  corpus that does restrict the adversary, by function class rather than by space.

## Open Questions / Limitations

- The separating problem `P` is artificial by the authors' own account, and a separation on a natural task is
  not obtained.
- The differential privacy separation is conditional on a sub exponentially secure encryption scheme.
- The computational model is the two phase summarise then answer model. Remark 3.3 asserts the extension to
  streaming without making it the headline statement.

## Quotes / Notable Passages

- "we show that there exists a problem P that requires exponentially more space to be solved efficiently with
  differential privacy, compared to the space needed without privacy."
- "We revisit previous lower bounds at a foundational level, and show that they are a consequence of a space
  bottleneck rather than a sampling bottleneck."
- "Admittedly, the problem P we define to prove the above theorem is somewhat unnatural."
- "So it is not that the mechanism did not get enough information about D; it is just that it cannot shrink
  this information in a way that supports t2 adaptive queries."
