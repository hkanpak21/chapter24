---
title: "Adversarially Robust Learning Could Leverage Computational Hardness"
type: source
date_ingested: 2026-04-12
authors: [Sanjam Garg, Somesh Jha, Saeed Mahloujifar, Mohammad Mahmoody]
venue: "arXiv:1905.11564v2 (19 Dec 2019). The ALT 2020 attribution carried on this page is not stated in the PDF in `raw/`; the only ALT mentions in it are bibliography entries."
year: 2020
tags: [adversarial-ml, cryptography, one-way-functions, hardness-reductions, robustness, complexity-theory, evasion-attacks]
claim_quantifier: existential
antecedent: "one-way functions, via one-time signature schemes and error-correcting codes. The quantitative gap of Ω(n) computational robustness against polylog(n) information-theoretic robustness additionally needs signatures with poly-logarithmically short signatures, which the paper's own footnote sources to exponentially hard one-way functions (Rompel 1990). The converse direction (Theorem 18) assumes nothing."
adversary_bound: "non-uniform circuits of size s(n) for any polynomial s, in Definition 3; the perturbation budget is a separate Hamming bound b(n)"
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: black box
cls_write: read only
cls_frame: compute
cls_party: attacker
cls_unit: circuit size
cls_tightness: poly
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "the size of circuit used by the adversary controls its computational power and that is why we are enforcing it to be a polynomial."
cls_evidence_src: §2, text following Def 1 and Def 3
cls_reason: "access=black box is stated explicitly as the paper's default ('by default, we model adversaries who have black-box access to h(·), Dn'), not white-box, even though h is a public deterministic verify-then-classify procedure. second_party left none because Theorem 8, the paper's stated main positive result, bounds only the attacker (circuit size); the learner is additionally constrained to polynomial time only in the separate Corollary 9 (robustly-hard base problem), not in Theorem 8 itself."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper ([GJMM20]) provides the first formal evidence that computational hardness can be *positively leveraged* for adversarial robustness — in contrast to the prior complexity-theoretic literature (Bubeck et al. 2018; Degwekar–Nakkiran–Vaikuntanathan 2019) which used it to prove *negative* results about learnability. The central construction uses digital signatures and error-correcting codes to wrap any learning problem Q (with an information-theoretically vulnerable classifier) into a related problem P whose classifier is robust against polynomial-time adversaries but still vulnerable to unbounded ones.

This answers a question raised by Madry, Goldwasser, and others: can we build "cryptographic" robustness akin to stream-cipher encryption, where computational bounds on the attacker suffice for security? Prior to this work there was no provable evidence that crypto assumptions could help robust learning in any way. The converse is also proved: any non-negligible gap between the success of polynomial-time and unbounded adversaries implies average-case NP-hardness.

The authors give two constructions: (i) a "tamper-detection" variant where the classifier may output a special symbol ⋆ to flag suspected tampering, and (ii) a no-tamper-detection variant where the classifier must always produce a label. They also establish a learning problem where no polynomial-time learner can output any information-theoretically robust classifier, yet computationally robust classifiers exist — combining their construction with robust-hardness results of Degwekar–Vaikuntanathan.

## Claim Boundary

- **Quantified over:** a *constructed* problem. Theorem 8 speaks about "family Pₙ of Construction 7" and Theorem 14 about "family Pₙ of Construction 13". The paper's own framing is a possibility question — "is there **any** learning task for which it is possible to design classifiers that are only robust against polynomial-time adversaries" — and the answer is an exhibited task, not a property of natural data. Theorem 18, the converse, is the one universal statement: it quantifies over all learning problems meeting five stated conditions.
- **Antecedent:** one-way functions, instantiated as one-time signature schemes, plus error-correcting codes. The headline quantitative separation — computational robustness as large as `Ω(n)` while information-theoretic robustness is as small as `b + polylog(n)` — additionally requires signatures of poly-logarithmic length, which the paper's footnote 3 attributes to **exponentially hard** one-way functions (Rompel 1990). That is a stronger assumption than plain OWFs and is easy to drop when citing the headline number.
- **Which party is constrained:** the *attacker*, and by **circuit size**, not by uniform running time. Definition 3 quantifies over all polynomials `s` and all adversaries realised as circuits of size `s(n)`. The perturbation budget `b(n)` is a separate Hamming-distance constraint. The learner is polynomial-time in Corollary 9.
- **Does not establish:** that computational robustness is achievable for image classification or any natural task; that the ℓ₀/Hamming construction transfers to ℓ_p metrics; or that computational robustness can be certified. Theorem 18 in fact establishes the cost of any such construction: a non-negligible gap implies a hard sampler for NP.
- **Abstract vs theorem:** none found. The abstract says "for some learning task" and states the converse as requiring computational hardness.

## Key Contributions

- **Theorem 8 (main positive result)**: for the family Pₙ of Construction 7, the classifiers hₙ are computationally robust with risk at most α against adversaries of budget `er·n`, where `er` is the error rate of the code, while `AdvRisk_{Pₙ, b+ℓ(n)}(hₙ) ≥ AdvRisk_{Q,b}(h)` against information-theoretic adversaries. The paper reads off from this that computational robustness can be `Ω(n)` while information-theoretic robustness is `b + polylog(n)`, given a constant-rate code and short signatures.
- **Game-based definition of computational robustness (Definitions 1 and 3)**: Definition 1 is the security game; Definition 3 fixes the adversary's power by *circuit size*, requiring `AdvRisk_{Pₙ,b,s}(L) ≤ R(n) + negl(n)` for every polynomial `s`. Remark 4 notes that dropping the negligible term is a matter of style.
- **Construction (Construction 7)**: Wrap (x, y) ~ D_Q by sampling a fresh signature keypair (vk_x, sk_x), attaching signed, error-correction-encoded (x, σ_x, [vk_x]). h_P verifies signature; outputs ⋆ on failure. Poly-time attacker cannot forge signatures; unbounded attacker can exhaustively search for a valid signature.
- **Theorem 14 (no tamper detection)**: for the family Pₙ of Construction 13, the classifiers hₙ have risk 0 and computational risk 0 against adversaries of budget `er·n`, yet `AdvRisk_{Pₙ, ℓ(n)}(hₙ) ≥ 1/2` against information-theoretic adversaries — a level the paper notes is no better than a coin toss. Uses repeated signatures.
- **Corollary 9 (robustly-hard base problem)**: if the underlying problem Q in Construction 7 is robust-hard with respect to a sublinear budget `b(n)`, then every polynomial learning algorithm L for Pₙ has `AdvRisk_{Pₙ, b+ℓ(n)}(L) ≥ 1 − negl(n)`, while hₙ remains computationally robust with risk at most α against linear-budget adversaries. The robust-hard base problem comes from Theorem 6, attributed in the paper to Degwekar–Vaikuntanathan (2019) and Bubeck et al. (2018c).
- **Theorem 18 (reverse direction)**: if a learning problem admits a uniform learner L that is computationally robust with risk at most α under `b(n)`-perturbations, has information-theoretic adversarial risk at least `β(n)`, with `β(n) − α ≥ 1/poly(n)`, and if `Dₙ` is efficiently samplable and the distance predicate `d(x,x') ≤ b(n)` is polynomial-time checkable, then there is a **hard sampler for NP** (Definition 17). Average-case NP-hardness is necessary for computational robustness to beat information-theoretic robustness. The five conditions are the antecedent and none of them is free.

## Key Definitions / Theorems

**Security game (Def 1)**: Challenger samples S ~ D^m, trains h = L(S), samples test (x, y) ~ D, gives (x, y) and oracle access to h and D-sampler to adversary A; A outputs x'. A wins if (x = x' ∧ h(x) ≠ y) ∨ (x ≠ x' ∧ HD(x, x') ≤ b ∧ h(x') ≠ y ∧ h(x') ≠ ⋆).

**Computational risk**: Risk against all PPT (or poly-size) attackers.

**Information-theoretic risk**: Risk against computationally unbounded attackers.

**Construction 7 (signature-wrapped classifier)**:
- Sampler: draw (x, y) ~ D_Q; freshly generate signature keys (vk_x, sk_x); σ_x ← Sign(sk_x, x); output ((x, σ_x, [vk_x]), y) where [·] is an error-correcting encoding.
- Classifier h_P((x̃, σ̃, V)): decode V to vk; if Verify(vk, x̃, σ̃) = accept, output h_Q(x̃), else output ⋆.
- Hamming budget b ≪ |x|; error-correcting code requires Ω(|x|) bit changes to alter decoded vk.

**Theorem 18 technique**: A distinguisher between computational and IT adversaries yields an average-case NP-hard distribution via a standard "guess the attacker's witness" reduction.

## Connections

- [Win-Win Theorem for Robust Learning](win-win-robust-learning.md) — Degwekar–Nakkiran–Vaikuntanathan 2019, negative complementary result; [GJMM20] builds on the robust-hard problems they construct
- [Planting Undetectable Backdoors](planting-undetectable-backdoors.md) — Goldwasser et al. 2022; similarly uses digital signatures to separate poly-time from unbounded detection
- [Complexity Theoretic Adversarial ML](complexity-theoretic-adversarial-ml.md) — Mahloujifar thesis incorporates this work
- [Win-Win Theorem](../concepts/win-win-theorem.md) — contrasts with this paper's positive direction
- [One-Way Functions](../concepts/one-way-functions.md) (new)
- [Computational vs Information-Theoretic Robustness](../concepts/computational-vs-it-robustness.md) (new)
- [Evasion Attacks](../concepts/evasion-attacks.md)
- [Saeed Mahloujifar](../entities/saeed-mahloujifar.md), [Mohammad Mahmoody](../entities/mohammad-mahmoody.md), [Sanjam Garg](../entities/sanjam-garg.md), [Somesh Jha](../entities/somesh-jha.md)

## Open Questions / Limitations

- Applicability to natural learning tasks (image classification): the construction is artificial; do any practical problems exhibit a meaningful computational–IT robustness gap?
- Can the construction be generalized beyond Hamming distance to ℓ_p metrics?
- Weakening the crypto assumption: OWFs used here; can weaker assumptions (average-case hardness of single problems) suffice?
- Connection to randomized-smoothing-style certified defenses: can computational-robustness certificates be combined with them?

## Quotes / Notable Passages

Verified against `raw/GJMM20_RobustLearningCompHardness.pdf` on 2026-08-20.

> "Computational limitation of attackers can indeed be useful in robust learning by demonstrating the possibility of a classifier for some learning task for which computational and information theoretic adversaries of bounded perturbations have very different power."

— abstract. The phrase "for some learning task" is the existential quantifier.

> "Non-trivial computational robustness implies computationally hard problems in NP."
