---
title: "Towards Permissionless Consensus in the Standard Model via Fine-Grained Complexity"
type: source
date_ingested: 2026-08-20
authors: [Marshall Ball, Juan Garay, Peter Hall, Aggelos Kiayias, Giorgos Panagiotakos]
venue: "CRYPTO 2024"
venue_evidence: "https://dl.acm.org/doi/10.1007/978-3-031-68379-4_4 (Advances in Cryptology - CRYPTO 2024, pp. 113-146)"
year: 2024
claim_quantifier: conditional
antecedent: "The k-Orthogonal Vectors conjecture (worst-case, in non-uniform and probabilistic-two-sided-error variants), plus the existence of a randomness beacon, plus a corruption bound. Theorem 23 additionally needs sub-exponentially hard DDH. OVC is standard in fine-grained complexity and is implied by SETH."
tags: [cryptography, complexity-theory, fine-grained-cryptography, proof-of-work, consensus, hardness-reductions]
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
cls_evidence: "Our protocol achieves resilience against adversaries that control an inverse-polynomial fraction of the honest computational power, i.e., adversarial power A = T^{1−ε} for some constant ε > 0, where T denotes the honest computational power."
cls_evidence_src: abstract
cls_reason: "Not an ML paper: target/family/phase/access/write follow the fine-grained-world-without-crypto.md and average-case-fine-grained-hardness.md convention (none/n/a) for fine-grained-cryptography papers with no ML asset in scope. party=attacker/unit=time/tightness=exponent/second_party=time mirror average-case-fine-grained-hardness.md's Def 2 pattern: both honest power T and adversary power A=T^{1-ε} are explicit and related by a stated exponent (rule 4, the adversary's bound decides when both parties are computationally bounded). REVISION 6 NOTE 2026-09-03: tightness is relative since 2026-08-27, the exponent wording above predates the split."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper puts an honest-versus-adversary **exponent ratio inside a security theorem** for consensus.
It shows that the worst-case `k`-Orthogonal Vectors conjecture, plus a random beacon, yields
permissionless Byzantine agreement — a win-win: either permissionless consensus exists relative to a
beacon, or SAT and a large family of problems get non-trivial worst-case speedups.

The technical core is a **Seeded Proof of Work**: a short public seed expands to `m` correlated
challenges that still admit no non-trivial amortization, even when the adversary holds the seed. This
requires a new **robust direct sum theorem** for the arithmetized `k`-OV polynomial `fOV_k` — that
correctly evaluating any `ℓ` out of `m` random instances takes `ℓ` times the work of one — and then a
**derandomized** version of that theorem for a joint pseudorandom distribution with only `Õ(m^{1/k}n)`
bits of entropy, which is what makes the seed short. A DDH-based Schnorr/Fiat-Shamir compiler makes
the sumcheck proofs zero-knowledge, giving what the authors call the first non-interactive PoW with a
superquadratic prover/verifier gap without a random oracle.

Consensus is then assembled weak → graded → full. Two complications drive the design and both are
recorded honestly: the adversary can show different PoW witnesses to different honest parties, and
the PoW's own security *fails with non-negligible probability* (`δ = n^{−o(1)}`), so the weak-consensus
subprotocol is run repeatedly and error-corrected against temporary loss of honest majority.

## Claim Boundary

- **Quantified over:** Uniform and non-uniform time-bounded adversaries in a RAM model. The PoW
  hardness condition (Definition 1) quantifies over any `Solve*` running in time `ℓ(n)·γ(t(n))`; the
  instantiations set `t = n^2` (or `n^k` for the interactive version) and rule out `ℓ·n^{2−ε}`. The
  underlying conjecture is strengthened past its usual form: the paper states it relies on OV
  admitting no *non-uniform* and (alternatively) no *probabilistic two-sided-constant-error*
  algorithm in time `n^{2−ε}`. The consensus theorems quantify over adversaries whose per-round
  computational power is bounded relative to the honest parties'.
- **Antecedent:** `k`OVC is worst-case and standard within fine-grained complexity, and is implied by
  SETH (the converse is not known). The **random beacon is a setup assumption**, and Corollary 22
  needs a beacon whose output length is proportional to the number of parties; §4/Theorem 23 relaxes
  this to `O(λ^2)` bits at the cost of sub-exponential DDH. Corollary 22 itself needs no one-way
  functions, which the authors flag.
- **Does not establish:** Consensus in the bare standard model. It also does not establish
  honest-majority-strength resilience: the corruption bound is far weaker. Verbatim from the abstract:
  *"Our protocol achieves resilience against adversaries that control an inverse-polynomial fraction
  of the honest computational power, i.e., adversarial power A = T^{1−ε} for some constant ε > 0,
  where T denotes the honest computational power. This relatively low threshold is a byproduct of the
  slack in the fine-grained complexity conjectures."* Nor does it establish negligible-error PoW
  security: `δ = n^{−o(1)}`, and the consensus protocol is built specifically to survive that.
- **Abstract vs theorem:** The **title** overreaches — "in the Standard Model" — while every theorem
  is in the **random beacon model**. The abstract does not overreach: it says *"imply permissionless
  consensus in the random beacon model—a setting where a fresh random value is delivered to all
  parties at regular intervals"*, and the title hedges with "Towards". The conclusion reconciles the
  two by treating "standard model" as meaning *no random oracle*: *"We have shown how to achieve
  permissionless consensus in the standard model assuming a computationally bounded adversary, the
  orthogonal vectors conjecture, and the existence of a randomness beacon."* A second, smaller gap:
  the abstract renders the corruption bound as `A = T^{1−ε}`, whereas Corollary 22 and Theorem 23
  state it as a ratio in the security parameter, `(n−t)·c / (t·c) > λ^ε`.

## Key Contributions

- **Definition 4 / Theorems 5, 6**: Seeded Proofs of Work — `Õ(m^{1/k}n)`-bit seed expands to `m`
  challenges with non-amortizability preserved even given the seed.
- **Theorem 7 / Theorem 8**: robust direct sum theorem for `fOV_k`, and its derandomized version over
  a low-entropy joint distribution. The derandomized version is the technical core.
- **Theorem 13**: extractable zero-knowledge Seeded PoW in the URS model under `k`OVC +
  sub-exponential DDH; honest prover `O(n^{k+δ})`, verifier `O(n^{1+δ})`, simulator `O(n^{1+δ})`.
- **Theorem 21 / Corollary 22**: permissionless consensus from a PoW plus a beacon plus the
  corruption bound.
- **Theorem 23**: the same with a beacon of output size `O(λ^2)`, under sub-exponential DDH.
- A weak-consensus error-correction technique that survives *temporary* loss of honest majority.

## Key Definitions / Theorems

- **Conjecture 3 (kOVC), verbatim:** *"For all ε > 0, there exists c ≥ 1 such that kOV requires
  n^{k−ε} time."* The paper notes: *"We note this is a worst-case conjecture."*
- **Assumption 1 (PoW).** *"There exists a (λ^2, γ(·), λ^{o(1)}, λ^{−o(1)})-PoW."*
- **Assumption 2 (Corruption bound).** `t < (n − t)·(1 − σ)·γ(λ^2)/λ^2 − σ` for some `σ ∈ (0,1)`. The
  paper remarks that if the adversary's PoW advantage vanishes (`γ(λ^2) ≈ λ^2`) this reduces to the
  necessary condition `2t < n`.
- **Corollary 22.** Under `k`OV taking `λ^{k−o(1)}` time, `(n−t)c/(tc) > λ^ε`, and a randomness
  beacon, there is a protocol achieving Consensus in the permissionless setting with overwhelming
  probability in `λ`.
- **Robust Direct Sum (informal), verbatim:** *"Assuming the kOV conjecture ..., for any m = poly(n)
  and ℓ = m^{1−o(1)} and any ε > 0, no algorithm running in time ℓ · n^{2−ε} that is given m random
  independent inputs to FOVk can correctly evaluate ℓ of them with probability 1/n^{o(1)}."*

## Connections

- **The only other paper in this corpus that puts the ratio inside the security statement.** Compare
  [Public-Key Cryptography in the Fine-Grained Setting](pkc-fine-grained-setting.md), where the ratio
  is between honest and adversary *runtimes*; here it is between honest and adversary *aggregate
  computational power per round*, which is a third unit again. Neither is
  [On Building Fine-Grained One-Way Functions](fine-grained-one-way-functions.md)'s circuit-size δ.
- **Same conjecture family, average-case side.**
  [The Planted Orthogonal Vectors Problem](planted-orthogonal-vectors.md) attacks the missing
  average-case OV distribution; [Average-Case Hardness of Parity Problems](average-case-parity-problems.md)
  gets average-case hardness for parity-`k`-OV but at a degraded exponent.
- **The barrier from below.**
  [Fine-Grained Complexity in a World without Cryptography](fine-grained-world-without-crypto.md)
  reports that permissionless consensus from worst-case OV hardness is one of only two primitives
  known from *worst-case* fine-grained assumptions, the other being proofs of work.
- **The ML analogue of the quantity being priced.** [Proof-of-Learning](proof-of-learning.md) also
  compares an honest party's compute against a spoofer's, but as a bare inequality with no exponent,
  no adversary class, and no theorem. This paper is what that inequality would look like if it were
  parameterized.
- Concepts: [Orthogonal Vectors Conjecture](../concepts/orthogonal-vectors-conjecture.md),
  [Fine-Grained Cryptography](../concepts/fine-grained-cryptography.md),
  [Security Gap Exponent (δ)](../concepts/security-gap-exponent.md),
  [Average-Case Reductions](../concepts/average-case-reductions.md).

## Open Questions / Limitations

- The authors' main open question is whether the randomness beacon can be weakened or eliminated;
  they note they currently need at least `Ω(log^2 n)` beacon queries.
- The resilience threshold is inverse-polynomial in the honest power, which the authors attribute to
  slack in the fine-grained conjectures rather than to the protocol.
- PoW security holds only with probability `1 − n^{−o(1)}`; negligible-error consensus is recovered
  only by repetition and error correction.

## Quotes / Notable Passages

> "Unlike many other cryptographic primitives, PoW schemes necessitate very fine-grained assumptions
> because the honest Prover running time should be as close to the bound on adversarial running time
> as possible."

> "This relatively low threshold is a byproduct of the slack in the fine-grained complexity conjectures."
