---
title: "Formal Privacy Proof of Data Encoding: The Possibility and Impossibility of Learnable Obfuscation"
type: source
date_ingested: 2026-07-26
date_verified: 2026-08-22
authors: [Hanshen Xiao, G. Edward Suh, Srinivas Devadas]
venue: CCS 2024
year: 2024
claim_quantifier: conditional
antecedent: "Theorem 1 assumes a learnable obfuscation T = (T_X, T_Y) with BOTH components injective, satisfying learnability preservation (Definition 5, property 1) with respect to a two-element PAC-learnable concept class C = {h_0, h_1}: there is an efficient Alg and a distribution D_0 with E[h_0(x)] = 0.5 such that for n ≥ m_0, Alg returns with probability ≥ 3/4 a model whose encoded risk is at most 1/2 − λ for a constant λ > 0. If no such transformation exists the theorem is vacuous."
adversary_bound: "Polynomial time (Definition 2, IND-CPA). The adversary must additionally be able to choose the challenge distributions D_0, D_1 and a concept class of its own construction, must receive the encoded dataset, and must be able to run the honest learner Alg on part of it and test the resulting model on the rest. Removing that last access is one of the two escapes the authors name."
tags: [cryptography, learning-theory, computational-indistinguishability, one-way-functions]
cls_target: train data
cls_family: distribution
cls_phase: train time
cls_access: channel
cls_write: corpus
cls_frame: compute
cls_party: attacker
cls_unit: time
cls_tightness: poly
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: time
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "A polynomial-time adversary selects two arbitrary plaintexts 𝑋0 and 𝑋1 from X∗ and sends to the user"
cls_evidence_src: Def 2
cls_reason: "Classified on Theorem 1, the paper's headline negative result (abstract: 'cannot offer cryptographic computational security in the worst case'), not the possibility half (Theorems 2-7), per the audit warning that this is an IND-CPA impossibility about the encoding T, not a training map, with no one-way-function claim. family=distribution: Def 2's game distinguishes which of two whole challenge datasets/distributions D_0, D_1 was encoded, not a single record's membership. Both the distinguisher and the honest learner Alg are polynomial-time (Def 2, Def 5); rule 4 puts the adversary's bound in party/unit and the learner's matching unit in second_party. access=channel: the adversary interacts with the encode-then-train pipeline as a chosen-plaintext channel, not by querying a deployed model. baseline=stated: Claim Boundary records the coin flip at 1/2 as the standard indistinguishability baseline, against which Theorem 1 delivers Pr(b-hat=b)>=2/3."
cls_prov: P
cls_date: 2026-08-22
---

> **Verified against `raw/XSD24_FormalPrivacyDataEncoding.pdf` on 2026-08-22.** The title, venue,
> Definition 5, Definition 2, the statement of Theorem 1, its proof sketch in Appendix A, and the
> quotations below were checked against the extracted text of that file. The earlier page title said
> "Learnable Encryption". The paper says **Learnable Obfuscation**, and the title has been corrected
> while the slug is unchanged. Still unverified: the possibility side, meaning Theorems 2 through 7 and
> the PAC Privacy accounting of Sections 5 through 7, which were read for statement and scope only, and
> Assumptions 1 and 2 that Theorem 7 rests on.

## Summary

The paper formalises **learnable obfuscation**, a transformation `T(·, θ) = (T_X(·, θ_X), T_Y(·, θ_Y))`
applied to features and labels with a secret seed, such that a polynomial-time learner can train
directly on the encoded samples and reach low encoded risk, while the plaintext and the transformation
itself stay hidden (Definition 5). The setting is outsourcing. A user encodes, an untrusted server
trains, and only the user can decode predictions. NeuraCrypt and TransNet are the constructions it has
in view.

The negative half is Theorem 1. If such a transformation preserves learnability with non-trivial
encoded accuracy, then it cannot be IND-CPA secure. The adversary builds a harder concept class `C̃`
from the given one by appending a block `X_b` of `ν` hardcore points with fully random labels, so that
the same sample budget that suffices for `C` does not suffice for `C̃`. It then splits the encoded
dataset it receives, trains with the honest learner on one part, tests on the other, and reads the
encoded test accuracy as the distinguishing bit, winning with `Pr(b̂ = b) ≥ 2/3`. From the abstract,
*"any non-trivial, property-preserving transformation which enables effectively learning over encoded
samples cannot offer cryptographic computational security in the worst case."*

The positive half abandons computational security and works in information-theoretic units instead.
Under PAC Privacy, the paper quantifies leakage from matrix masking, data mixing and permutation with
added noise, giving bounds for reconstruction of the whole set (Theorem 2), membership of an individual
(Theorem 3), their improvements under mixing and permutation (Theorems 4 and 5), a simulation-complexity
result (Theorem 6), and a reverse-engineering hardness result under distributional assumptions
(Theorem 7).

## Claim Boundary

**Quantified over.** Theorem 1 is universal over learnable obfuscations satisfying its hypotheses, and
existential over the attack. Given any such transformation, the paper exhibits one adversary that wins.
It is not a statement about all encodings, only about those that preserve learnability with a constant
advantage `λ` and are injective on both coordinates.

**Antecedent.** The learnability-preservation hypothesis of Definition 5, instantiated at a
two-element concept class, with a constant accuracy edge `λ > 0`, a sample threshold `m_0`, and both
`T_X` and `T_Y` injective. Definition 5 itself only requires `T_Y` to be injective. Theorem 1 adds the
requirement on `T_X`, and the authors say why, *"we restrict T to be injective to avoid the trivial
cases"* in which `T_X = h` collapses the encoded data to the label set. The hypothesis is not known to
hold for any concrete scheme. It is what a proposed construction would have to claim.

**Which party is constrained and in what resource.** Both, in time. The learner `Alg` is
polynomial-time by Definition 5. The distinguisher is polynomial-time by Definition 2 and runs `Alg` as
a subroutine. The adversary is unconstrained in its choice of challenge distributions and concept
class, which is where "worst case" enters.

**The success criterion and its tolerance.** Chosen-plaintext distinguishing advantage. Definition 2
calls a scheme insecure if the adversary reaches `Pr(b̂ = b) ≥ 1/2 + δ` for non-negligible `δ`. Theorem 1
delivers `Pr(b̂ = b) ≥ 2/3`, a constant advantage rather than a negligible one.

**The baseline.** A coin flip, at `1/2`, as in the standard indistinguishability game.

**Does not establish.** Three things the wiki has previously read into it. First, nothing about
one-way functions. The phrase does not occur in the PDF, and the object under attack is the encoding
`T`, not a training map `D ↦ w` and not the released weights. Second, nothing about average-case or
distribution-specific security. The adversary chooses `D_0`, `D_1` and `C̃`, so a guarantee that holds
for a fixed natural data distribution is untouched. The authors name this escape themselves, saying
that one may *"put stronger restrictions on the plaintext that the adversary can select for the
distinguishing challenge, since we cannot afford the worst-case indistinguishability on arbitrary
learnable data."* Third, nothing about settings where the adversary cannot see a model trained on the
encoded data. That is the other escape they name, adding that it *"is beyond the current learnable
obfuscation framework (but can be expensively secured by FHE)."*

**Abstract versus theorem.** The abstract's "in the worst case" is doing real work and the body honours
it. The interpretive sentence to watch is in the conclusion of §4, *"there does not exist a universal
and secure learnable obfuscation that works for arbitrary learning tasks"*, which is exactly the
theorem, and the contribution list's gloss that privacy *"still needs to be traded off against
utility"*, which is a reading of it rather than a proved quantitative tradeoff.

## Key Contributions

- **Definition 5**, a formal definition of learnable obfuscation with two requirements, learnability
  preservation and a pair of privacy criteria covering data privacy and model security.
- **Theorem 1**, the impossibility. A learnable obfuscation with non-trivial encoded accuracy and
  injective `T_X`, `T_Y` cannot be IND-CPA secure. Proof in Appendix A by the hardcore-block
  construction and two applications of Hoeffding's inequality.
- The argument that fully homomorphic encryption is **not** a special case of learnable obfuscation,
  because a polynomial-time learner achieving non-trivial accuracy over computationally
  indistinguishable ciphertexts would itself break the scheme.
- **Theorems 2 through 6**, PAC Privacy leakage bounds for matrix masking, data mixing and permutation
  under noise perturbation, against the reconstruction challenge (Definition 6) and the membership
  inference challenge (Definition 7), reported as sharper utility-privacy tradeoffs than prior
  accounting.
- **Theorem 7**, hardness of reverse-engineering the transformation, under Assumptions 1 and 2 on the
  data distribution.

## Key Definitions / Theorems

- **Theorem 1 (Impossibility Result).** Suppose a learnable obfuscation `T = (T_X, T_Y)` exists with both
  components injective, satisfying learnability preservation with respect to a PAC-learnable
  `C = {h_0, h_1}`, so that for some `D_0` with `E_{x∼D_0}[h_0(x)] = 0.5` an efficient `Alg` given `n ≥ m_0`
  encoded samples returns, with probability at least `3/4`, a model `ĥ` of encoded risk at most
  `1/2 − λ` for a constant `λ > 0`. Then an adversary can construct a class
  `C̃ = {h_0, h̃_1, …, h̃_{2^ν}}` with `ν ≥ 9(16 log 9 / λ²)²` and a distribution `D_1` with
  `E_{x∼D_1}E_j[h̃_j(x)] = 0.5`, and after receiving `T(S_b, θ)` for a dataset of
  `n = m_0 + 16 log 9 / λ²` samples, return `b̂` with `Pr(b̂ = b) ≥ 2/3`.
- **Definition 2 (IND-CPA).** A polynomial-time adversary chooses two plaintexts, receives
  `F(X_b, sk)`, and is said to break the scheme if it guesses `b` with non-negligible advantage.
- **Definition 5 (learnable obfuscation).** Property 1 is learnability preservation, requiring a
  polynomial-time `Alg` that reaches encoded risk `≤ ε` once `n ≥ m̄_1(ε, δ)`. Property 2 requires that
  below sample thresholds `m̄_2` and `m̄_3` no adversary can estimate the input set or the transformation
  under the criteria `ρ_1` and `ρ_2`.
- **Definitions 6 and 7.** The reconstruction challenge and the membership inference challenge that the
  possibility side is priced against.

## Connections

- **A standing obstacle, correctly scoped.** It constrains claims that a *learnable encoding* is
  cryptographically secure in the worst case. It does not by itself refute
  [fiber-of-the-training-map](../concepts/fiber-of-the-training-map.md) or a "training is hard to
  invert" claim, because the object it attacks is the encoding rather than the training map, and it
  does not mention one-way functions. Any use of it as an obstacle must say which of the two escapes
  the programme is taking, restricted plaintexts or no adversarial access to the encoded-data model.
- The notion it would constrain, if the programme claimed worst-case security for a learnable
  transformation, is the computational reconstruction notion of
  [Cohen et al.](cohen-data-reconstruction.md).
- Same authors' [PAC Privacy](../analyses/native-asymmetry-in-learning.md) line, whose adversary is not
  resource-bounded. This paper is the computational-side companion, and its possibility half runs on
  PAC Privacy accounting.
- [win-win-robust-learning](win-win-robust-learning.md), the other direction of tax on computational
  claims in learning.
- Concepts: [pac-learning](../concepts/pac-learning.md),
  [computational-indistinguishability](../concepts/computational-indistinguishability.md),
  [data-reconstruction-attack](../concepts/data-reconstruction-attack.md),
  [membership-inference-game](../concepts/membership-inference-game.md).

## Open Questions / Limitations

- The two escapes the authors name are both open. Restricting the plaintext distribution the adversary
  may choose, and denying the adversary access to the model trained over encoded data, each avoid
  Theorem 1, and neither is developed into a positive result here.
- Theorem 1 needs `T_X` injective, which Definition 5 does not require. A non-injective feature
  transformation falls outside the theorem.
- The impossibility is about IND-CPA. Weaker computational goals, and average-case goals against a
  fixed data distribution, are untouched.
- The possibility side is information-theoretic, so it inherits the PAC Privacy adversary, which is not
  resource-bounded. The paper therefore leaves the computational-security side of learnable obfuscation
  entirely negative and offers no positive computational guarantee.
- Theorem 7 rests on Assumptions 1 and 2 about the data distribution, which the authors call mild but
  do not verify against real data.

## Quotes / Notable Passages

> "any non-trivial, property-preserving transformation which enables effectively learning over encoded
> samples cannot offer cryptographic computational security in the worst case"

> "The bottom line is that there does not exist a universal and secure learnable obfuscation that works
> for arbitrary learning tasks."

The two escapes, in the authors' own words:

> "to achieve computational IND-CPA-security, either we need to put stronger restrictions on the
> plaintext that the adversary can select for the distinguishing challenge, since we cannot afford the
> worst-case indistinguishability on arbitrary learnable data or, as a necessary requirement, we have to
> prohibit the adversary's access to the trained model computed over encoded data, which, unfortunately,
> is beyond the current learnable obfuscation framework (but can be expensively secured by FHE)."

On the reading of Theorem 1 that the contribution list offers:

> "This suggests that even if a secret key is allowed in learnable obfuscation, privacy still needs to
> be traded off against utility, similar to the public model scenario."
