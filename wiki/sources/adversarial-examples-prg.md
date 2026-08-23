---
title: "Adversarial Examples from Cryptographic Pseudo-Random Generators"
type: source
date_ingested: 2026-04-23
authors: [Sébastien Bubeck, Yin Tat Lee, Eric Price, Ilya Razenshteyn]
venue: "arXiv:1811.06418v1 (15 Nov 2018), a four-page follow-up to BPR"
year: 2018
tags: [adversarial-ml, cryptography, pseudorandomness, evasion-attacks, complexity-theory]
claim_quantifier: conditional
antecedent: "the quadratic residuosity assumption, named in the body, instantiated through the Blum–Blum–Shub trapdoor pseudorandom generator. This is a standard but specific number-theoretic assumption, not the existence of one-way functions in general."
adversary_bound: "the learner is restricted to polynomial time. The perturbation adversary is a norm budget of order √n, not a computation."
model_class: "binary classification of pairs of distributions on {0,1}^n, Euclidean and ℓ∞"
algorithm_class: "polynomial-time learning algorithms"
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: time
cls_tightness: poly
cls_baseline: stated
cls_second_party: perturbation
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "Under the quadratic residuosity assumption, any polynomial time learning algorithm for this family has an accuracy close to chance on some task in the family"
cls_evidence_src: §3, property (c), restating Theorem 3.1
cls_reason: "Two parties bounded: learner (polynomial time) and evasion adversary (perturbation radius Ω(√n), no compute bound per Claim Boundary). Rule 4: the computational bound decides the row, so party=learner/unit=time, and the evasion adversary's unit goes to second_party=perturbation. baseline=stated from 'accuracy close to chance.' Audit check: verified the quadratic-residuosity/BBS antecedent and the BPR-has-no-crypto-assumption relation directly against raw/BLPR19_AdvExamplesPRG.pdf (Thm 3.1, §1); the wiki's 2026-08-20 correction is accurate."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

**Correction, 2026-08-20.** Two claims previously on this page are reversed. It read that the assumption is "cryptographic pseudorandom generators exist (equivalently, one-way functions exist)"; the paper names the **quadratic residuosity assumption**, instantiated through the Blum–Blum–Shub trapdoor PRG, and derives everything from Theorem 3.1 about that specific object. It also read that "the BPR19 predecessor relied on stronger assumptions (trapdoor PRGs); BLPR19 sharpens the result to standard crypto"; the predecessor uses **no** cryptographic assumption at all — its lower bound is unconditional in the statistical query model — and it is *this* paper that introduces the trapdoor PRG.

This four-page follow-up strengthens both halves of [BPR](adversarial-examples-computational-constraints.md). Where BPR gave a task with a classifier robust to perturbations of size `log^{1/2−ε} n` and SQ-hardness, this paper gives a task admitting a **maximally robust** classifier — one tolerating perturbations of size comparable to the examples themselves, `Ω(√n)` — and proves hardness against **all** polynomial-time algorithms under the quadratic residuosity assumption.

The construction is short. Let `G_N` be the Blum–Blum–Shub generator for `N = pq`. Take `D₀ = unif({0,1}ⁿ)` and `D₁(N)` the distribution of the first `n^c` bits of `s ∘ G_N(s)` for uniform seed `s`. Then: the robust sample complexity of the family is `O(n)`; every task in the family admits a maximally robust classifier that is also efficiently computable, because knowing the factorisation permits efficient distinguishing; and under quadratic residuosity, every polynomial-time learning algorithm has accuracy close to chance on some task in the family. Section 2 gives a warm-up with an ordinary PRG in place of the trapdoor one, which yields a maximally robust classifier that is not efficiently computable — the paper's "addendum to hypothesis 1".

## Claim Boundary

- **Quantified over:** a *family* of constructed tasks indexed by the modulus `N = pq`. The hardness statement is "any polynomial time learning algorithm for this family has an accuracy close to chance **on some task in the family**", which is the standard average-case-over-keys form, not a statement about a single fixed distribution and not a statement about natural data.
- **Antecedent:** the quadratic residuosity assumption. Theorem 3.1, which the paper attributes to Blum–Blum–Shub, Vazirani–Vazirani and Goldreich, is the load-bearing statement: a computational statistical distance greater than `1/2 + 1/poly(n)` for infinitely many `N` would refute quadratic residuosity.
- **Which party is constrained:** the *learner*, to polynomial time. The evasion adversary is a Euclidean ball of radius `Ω(√n)` and carries no computational bound. Neither party is bounded in memory or in queries.
- **Does not establish:** that adversarial examples in deployed systems arise this way; that one-way functions in general suffice, since the argument is tied to a trapdoor PRG; or that the separation survives if the learner may use non-uniform advice about `N`.
- **Abstract vs theorem:** the abstract says "a standard cryptographic assumption" without naming it; the body names quadratic residuosity. Citing the abstract alone loses the antecedent, which is how this page came to record the wrong one.

The paper complements three related results: (1) the [Degwekar-Nakkiran-Vaikuntanathan Win-Win Theorem](win-win-robust-learning.md) which goes in the *opposite* direction (hard-to-robustly-learn implies OWF), together establishing that robust-learning hardness is exactly equivalent to cryptographic hardness; (2) [Computational Concentration of Measure (EMM20)](computational-concentration-of-measure-etesami.md) showing that on *product distributions*, computational hardness does not help (giving the negative direction complementing BLPR19's positive direction); (3) [Garg-Jha-Mahloujifar-Mahmoody 2020](computational-hardness-robust-learning.md), a similar positive separation using PRFs.

Together, these papers place adversarial robustness within Impagliazzo's five-worlds landscape. **Correction, 2026-08-20:** this sentence previously asserted a biconditional, "robust learning is possible iff computing is at least as hard as cryptography". No paper in this group proves that. The win-win theorem is a one-way implication from robust-learning hardness to one-way functions; this paper's direction is a construction under quadratic residuosity, so it exhibits one hard task rather than characterising a world. Neither licenses an "iff", and neither is about tasks arising outside a construction.

## Key Contributions

- **Hardness against all polynomial-time learners**: replaces BPR's statistical-query lower bound with hardness under the quadratic residuosity assumption, and with a much simpler proof. **Correction, 2026-08-20:** the previous bullet described this as moving *from* trapdoor assumptions *to* OWFs; the movement is the other way, from no cryptographic assumption to a specific one.
- **Trapdoor-PRG construction**: the task is defined so that classifying it is distinguishing the generator's output from uniform, which the trapdoor makes easy and quadratic residuosity makes hard without it. The paper instantiates with Blum–Blum–Shub for concreteness.
- **Maximally robust and efficiently computable classifier**: robust to perturbations of size `Ω(√n)`, comparable to the norm of the examples, and computable in polynomial time given the factorisation.
- **The addendum to hypothesis 1 (Section 2)**: with an ordinary PRG in place of a trapdoor one, one gets a task with a maximally robust classifier that is *intractable to compute*. The authors use this to refine BPR's hypothesis 1 from "no robust classifier exists" to "no **efficiently computable** robust classifier exists".
- **Robust accuracy, not just accuracy (property c′)**: with the BPR trick of a dummy coordinate revealing the label, hardness applies to `ε`-robust accuracy while the non-robust problem stays polynomial-time solvable.

## Key Definitions / Theorems

- **The task**: `D₀ⁿ = unif({0,1}ⁿ)`; `D₁ⁿ(N)` is the distribution of the first `n^c` bits of `s ∘ G_N(s)` for uniform `s ∈ {0,1}ⁿ` and `N = pq` with `p, q ≡ 3 mod 4`. Classifying means separating the two distributions. **Correction, 2026-08-20:** the previous description, "data points x = (seed, G(seed)), label = G(seed)₁ (first bit of expanded string)", misstates the label; the label is which of the two distributions the sample came from.
- **Maximally robust classifier**: a set `A ⊆ ℝⁿ` satisfying the robust separation with `ε = Θ(max_i diam(supp(D_i)))`.
- **Blum–Blum–Shub generator**: maps a seed to a near-uniform quadratic residue mod `N`, then iteratively takes square roots; the output bits are the parities of the iterates.
- **Theorem 3.1**: assuming that for infinitely many `N` the computational statistical distance of `{(D₀ⁿ, D₁ⁿ(pq))}` exceeds `1/2 + 1/poly(n)` would refute the quadratic residuosity assumption; and if `p, q` are known the computational statistical distance is `1 − o(1)`.
- **Properties read off (a–d)**: robust sample complexity `O(n)`; a maximally robust, efficiently computable classifier exists; under quadratic residuosity no polynomial-time learner beats chance on some task in the family; and the non-robust problem is solvable in polynomial time and samples.

## Connections

- Source: [Adversarial Examples from Computational Constraints (BPR19)](adversarial-examples-computational-constraints.md) — the predecessor, whose lower bound is unconditional in the statistical query model. **Correction, 2026-08-20:** this line previously read "predecessor with stronger crypto assumption; BLPR19 strengthens to standard OWFs", which inverts the relation. The predecessor uses no cryptographic assumption; this paper adds one.
- Source: [Computational Limitations in Robust Classification / Win-Win (DNV19)](win-win-robust-learning.md) — converse direction: hard-to-robustly-learn ⇒ OWF; together BLPR and DNV make robust learning ⇔ OWF.
- Source: [Computational Concentration of Measure (EMM20)](computational-concentration-of-measure-etesami.md) — shows crypto hardness does *not* help on product distributions — complementary negative direction.
- Source: [Adversarially Robust Learning Could Leverage Computational Hardness (GJMM20)](computational-hardness-robust-learning.md) — similar positive separation via PRFs; practical construction.
- Concept: [Win-Win Theorem](../concepts/win-win-theorem.md) — the characterization connecting these results.
- Concept: [Pseudorandomness](../concepts/pseudorandomness.md) — the crypto primitive used, in its trapdoor form.
- Concept: [One-Way Functions](../concepts/one-way-functions.md) — adjacent, but not the assumption here. **Correction, 2026-08-20:** this line previously read "equivalent via HILL", which would license reading the result as holding under any one-way function. The construction needs a trapdoor, and the concrete instantiation needs quadratic residuosity.
- Concept: [Computational vs. IT Robustness](../concepts/computational-vs-it-robustness.md).
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md).
- Authors: [Sébastien Bubeck](../entities/sebastien-bubeck.md), [Yin-Tat Lee](../entities/yin-tat-lee.md), [Eric Price](../entities/eric-price.md), [Ilya Razenshteyn](../entities/ilya-razenshteyn.md).

## Open Questions / Limitations

- **Natural data distributions**: construction is cryptographic / contrived; the Win-Win theorem says either natural data admits efficient robust learning or yields OWFs — and natural data presumably does not yield new OWFs.
- **Adaptive adversaries**: the paper does not discuss adaptivity. **Correction, 2026-08-20:** the previous line, "the construction assumes non-adaptive adversaries", attributes a restriction the four-page paper never states.
- **Quantitative tightness**: whether the separation's parameters can be matched to concrete cryptographic hardness is not addressed in the paper. **Correction, 2026-08-20:** the previous line described the separation as "sharp (poly vs. exp)"; the paper's hardness statement is that polynomial-time accuracy is close to chance, with no exponential-time upper bound stated.
- **Practical instantiations**: no one has constructed a real-world dataset that concretely achieves BLPR-style computational-robustness separation; all known examples are synthetic.

## Quotes / Notable Passages

> _Not verbatim. Checked against `raw/BLPR19_AdvExamplesPRG.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> We construct a task which admits a maximally robust classifier and prove computational hardness of learning this task under a standard cryptographic assumption.

> _Not verbatim. Checked against `raw/BLPR19_AdvExamplesPRG.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> The primary ingredient of our construction is a trapdoor pseudorandom generator.

Verified against `raw/BLPR19_AdvExamplesPRG.pdf` on 2026-08-20.

> "In the present paper we significantly strengthen both (i) and (ii): we now construct a task which admits (i') a maximally robust classifier (that is it can tolerate perturbations of size comparable to the size of the examples themselves); and moreover we prove computational hardness of learning this task under (ii') a standard cryptographic assumption."

— abstract, the sentence the first paraphrase above was drawn from.

> "We prove this new result in Section 3, where our main tool will be trapdoor pseudorandom generators (PRG)."

— §1, the sentence the second paraphrase above was drawn from.

> "yet finding any non-trivial robust classifier (even for arbitrarily small perturbations, and with probability of correctness only slightly better than chance) is impossible in polynomial time under a standard cryptographic assumption (namely, quadratic residuosity assumption)."

— §1, where the assumption is named.
