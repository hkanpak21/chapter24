---
title: "Backdoor Defense, Learnability, and Obfuscation"
type: source
date_ingested: 2026-04-23
authors: [Paul Christiano, Jacob Hilton, Victor Lecomte, Mark Xu]
venue: "arXiv:2409.03077v2 (18 Nov 2024). The ITCS 2025 / LIPIcs Vol. 325 attribution carried on this page is not stated anywhere in the PDF in `raw/` and is unconfirmed from the primary source."
year: 2025
tags: [backdoor, PAC-learning, indistinguishability-obfuscation, VC-dimension, defendability, complexity-theory]
claim_quantifier: conditional
antecedent: "the statistical characterisation (Theorem 4.1) is unconditional. The separation of efficient defendability from efficient PAC learnability (Theorem 5.3) holds in the random oracle model. The non-defendability of polynomial-size circuits (Theorem 5.5) assumes one-way functions and indistinguishability obfuscation."
adversary_bound: "the defender is computationally unbounded in Section 4 and polynomial-time in Sections 5 and 6. The attacker is constrained not by computation but by the game: its strategy must work for a randomly-chosen trigger, and the backdoored function must disagree with the original on at most an ε fraction of the distribution."
date_verified: 2026-08-20
cls_target: parameters
cls_family: backdoor
cls_phase: post hoc
cls_access: white box
cls_write: read only
cls_frame: compute
cls_party: auditor
cls_unit: time
cls_tightness: poly
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: corruption
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "F is ε-defendable with confidence 1 − δ using a detection strategy that runs in time polynomial in n and 1/δ"
cls_evidence_src: Def 5.1
cls_reason: "Classified on the computational half (Sections 5-6) rather than the statistical characterisation (Theorem 4.1, unbounded defender), since the abstract's own framing ('We identify efficient defendability as a notable intermediate concept in between efficient learnability and obfuscation') and the title lead with the efficient/computational notion, per rule 1. party=auditor for the defender (detects whether a given input is the trigger) since the vocabulary has no 'defender' value and rule 6 names auditor as the usual model for a party performing detection/verification; unit=time, tightness=poly because efficient defendability (Def 5.1) is a standard poly-time quantifier, not a restricted algorithm class (SQ/low-degree), so 'poly' over 'class'. second_party=corruption for the attacker's own constraint: 'ε constrains the attacker' (confirmed verbatim in the PDF beside Def 5.1) is a closeness/corruption-fraction budget (Pr[f*(x)!=f(x)]<=eps), not a computational bound (adversary_bound front matter: 'The attacker is constrained not by computation but by the game'), matching rule 4's computational-bound-decides-the-row with the non-computational party's unit recorded as second_party. baseline=stated: Theorem 4.1's supremum confidence formula is max(1/2, 1-Theta(VC(F)*eps)), an explicit coin-flip baseline. target=parameters and phase=post hoc for consistency with critical-evaluation-backdoor-countermeasures, the corpus's other backdoor-defense-evaluation paper: the object under contention is a (possibly backdoored) function/model, and the defender acts on a fixed, already-determined function/trigger pair with no further training, access/write matching that paper's white box / read only for the same reason (the defender inspects but does not modify the function)."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (CHLX25) introduces a **formal game-theoretic notion of ε-defendability** against backdoor attacks and proves it sits as a *distinct* complexity-theoretic concept between efficient PAC learnability and indistinguishability obfuscation. The game: an attacker modifies a function to disagree on a randomly-chosen trigger x* (but agree almost everywhere else); the defender must detect whether a given input is the trigger. The key constraint making defense possible is that the attacker's strategy must work for a *randomly-chosen* trigger, not an adversarially-chosen one.

The paper establishes four main results:

1. **Statistical defendability (Section 4, Theorem 4.1)**: a representation class F is ε-defendable with confidence tending to 1 **iff ε = o(1/VC(F))**, proved through a prediction strategy that adapts the algorithm of Hanneke et al. 2022. This mirrors the VC-dimension characterisation of PAC learnability. The prediction strategy runs in exponential time, which is what motivates the computational section.

2. **Computational defendability (Section 5)**: efficient PAC learnability *implies* efficient defendability (Corollary 5.2), but **not conversely in the random oracle model** (Theorem 5.3). The set of efficiently defendable classes lies strictly between the efficiently learnable classes and all classes.

3. **iO + puncturable PRF → polynomial-size circuits not efficiently defendable (Theorem 5.5)**: a hybrid argument combining an efficient indistinguishability obfuscator with a puncturable pseudorandom function, assuming OWF and iO.

4. **Decision trees defendable in a single evaluation (Section 6, Theorem 6.1)**: under the uniform input distribution, polynomial-size decision trees are efficiently uniform-defendable in the time it takes to evaluate one tree, using no example-oracle calls at all — a natural class where defence is faster than any possible learning algorithm.

The conceptual contribution is that **defendability** is a complexity-theoretic notion in its own right, with the set of efficiently defendable classes lying strictly between the efficiently learnable classes and all classes.

The defender's task is deliberately narrow. Detection happens **at runtime**: the defender is handed a particular input and must flag whether it activates the trigger. The authors chose this because flagging a *model* as backdoored without being given an input is already ruled out by [GKVZ22](planting-undetectable-backdoors.md).

## Claim Boundary

- **Quantified over:** representation classes, in an abstract game. Theorem 4.1 is a universal statement about every representation class over `{0,1}ⁿ`. Theorem 5.5 is about one specific class, polynomial-size Boolean circuits. Theorem 6.1 is about one specific class, polynomial-size decision trees, and only under the uniform distribution. None of these is a statement about a trained neural network.
- **Antecedent:** Theorem 4.1 assumes nothing. Corollary 5.2 assumes nothing. Theorem 5.3 holds **in the random oracle model of computation**, so the separation of efficient defendability from efficient PAC learnability is not established in the plain model. Theorem 5.5 assumes one-way functions and indistinguishability obfuscation, both standard, the second strictly stronger.
- **Which party is constrained:** in Section 4 the defender is computationally unbounded and only its statistical power is at issue; in Sections 5 and 6 the defender must run in polynomial time. The attacker is never bounded by computation. What limits it is the structure of the game: the trigger `x*` is drawn from the attacker's own distribution *after* it commits to `f` and *before* it chooses `f*`, and `f*` must satisfy `Pr_{x~D}(f*(x) ≠ f(x)) ≤ ε`. The authors call this the "key symmetry-breaking assumption that makes the game interesting"; without it the defender can be forced to a coin flip even at VC dimension 1.
- **Does not establish:** that any real defence works or fails; that backdoor *removal* is intractable, since the game is about runtime detection of a given input, not removal; or that the defendability hierarchy is strict in the plain model.
- **Abstract vs theorem:** none found. The abstract states the random-oracle caveat implicitly by saying "but not conversely" without qualification, which is the one place a reader could over-read; the body places the separation in the random oracle model.

## Key Contributions

- **Definition of ε-defendability (Section 3)**: game between attacker and defender; attacker must work for a randomly-chosen trigger.
- **Statistical defendability characterization**: F is ε-defendable iff ε = o(1/VC(F)), via Hanneke-style voting.
- **Computational defendability hierarchy**: learnable ⊊ defendable ⊊ all; strict separation.
- **iO-based non-defendability of polynomial circuits**: applied hybrid argument (puncturable PRF + iO).
- **Decision trees: defense strictly easier than learning**: natural class where defendability is faster than PAC learning.
- **Mechanistic defense direction**: the decision-tree result hints at "mechanistic" (structure-based) defenses for specific classes — a template for practical defendability that doesn't require full PAC learning.

## Key Definitions / Theorems

- **ε-defendability game (Definition 3.1)**: (1) attacker chooses (D, f ∈ F); (2) trigger x* sampled from D; (3) attacker chooses f* ∈ F with Pr_{x~D}[f*(x) ≠ f(x)] ≤ ε but f*(x*) ≠ f(x*); (4) defender, given either (f, x~D) or (f*, x*), must distinguish.
- **Statistical defendability (Theorem 4.1)**: the supremum confidence with which F is ε-defendable is `max(1/2, 1 − Θ(VC(F)·ε))` as `VC(F) → ∞`. In particular F is ε-defendable with confidence tending to 1 as `n → ∞` if and only if `ε = o(1/VC(F))`.
- **Efficient defendability (Definition 5.1)**: there is a polynomial `p` such that for any `δ > 0` and any `ε < 1/p(n, 1/δ)`, F is ε-defendable with confidence `1 − δ` by a detection strategy running in time polynomial in `n` and `1/δ`.
- **Corollary 5.2 (efficient PAC ⇒ efficient defendable)**: if F is efficiently PAC learnable, then F is efficiently defendable.
- **Theorem 5.3 (converse fails, in the random oracle model)**: in the random oracle model of computation, with probability `1 − O(2^{−n^c})` over the choice of oracle, there is a polynomially evaluatable representation class over `{0,1}ⁿ` that is efficiently defendable but not efficiently PAC learnable. The witness is a class of `2ⁿ` functions making unique oracle calls.
- **Theorem 5.5 (iO non-defendability)**: assuming OWF and iO, the class of polynomial-size Boolean circuits over `{0,1}ⁿ` is not efficiently defendable. The one-way function supplies a puncturable pseudorandom function in the proof.
- **Theorem 6.1 (decision trees)**: decision trees over `{0,1}ⁿ` of size at most `s`, with `s` polynomial in `n`, are efficiently **uniform**-defendable by a detection strategy that makes **0** calls to the example oracle and runs in time `O(time to evaluate a single decision tree)`. The strategy checks the depth of the leaf the input reaches and rejects if it is too large.
- **Correction, 2026-08-20:** the theorem labels above were previously written as "4.x", "5.x", "5.y", "6.x"; Theorem 5.3's random-oracle setting was omitted; and Theorem 6.1 was stated with a parameter "ε = O(1/tree-size)" that the paper does not give.

## Connections

- Source: [Planting Undetectable Backdoors (GKVZ22)](planting-undetectable-backdoors.md) — establishes backdoor-detection-impossibility; CHLX25 introduces defendability as a distinct, sometimes-tractable concept.
- Source: [Oblivious Defense (Goldwasser-Shafer-Vafa-Vaikuntanathan, STOC 2025)](oblivious-defense-backdoor-removal.md) — concurrent work on mitigation-without-detection; complementary. CHLX25 explicitly references GSVV25 as concurrent.
- Source: [Filter Impossibility (Ball et al. 2025)](filter-impossibility-ai-alignment.md) — LLM filter-specific instance of the defendability framework's negative side.
- Source: [Unelicitable Backdoors (Draguns et al. 2024)](unelicitable-backdoors-lms.md) — strengthens GKVZ22; CHLX25's iO non-defendability is the matching abstract theorem.
- Source: [Adversarial Examples from Computational Constraints (BPR19)](adversarial-examples-computational-constraints.md) — analog for adversarial examples; similar "statistical possible, computational hard" pattern noted in CHLX25.
- Source: [Adversarially Robust Learning Could Leverage Computational Hardness (Garg et al. 2020)](computational-hardness-robust-learning.md) — same theme: using crypto for offense-defense asymmetry.
- Concept: [PAC Learning](../concepts/pac-learning.md) — defendability is the new peer concept.
- Concept: [Undetectable Backdoors](../concepts/undetectable-backdoors.md) — defendability is the complementary positive-side concept.
- Concept: [Defendability](../concepts/defendability.md) — **new concept page needed**.
- Concept: [Indistinguishability Obfuscation (iO)](../concepts/indistinguishability-obfuscation.md) — **new concept page needed**.
- Concept: [Pseudorandomness](../concepts/pseudorandomness.md) — puncturable PRFs are the primary building block of the iO non-defendability result.
- Concept: [Win-Win Theorem](../concepts/win-win-theorem.md) — CHLX25 extends this to a three-way hierarchy (learnable/defendable/obfuscatable).
- Authors: Paul Christiano (formerly OpenAI / now Alignment Research Center), Jacob Hilton, Victor Lecomte, Mark Xu (new entities).

## Open Questions / Limitations

- **Efficient defendability vs. efficient learnability — tight separation**: CHLX25 gives a non-trivial gap but a complete characterization of the "defendable but not learnable" region remains open.
- **Natural classes beyond decision trees**: does a broader set of structurally-interesting classes admit fast defense? Candidates: sparse halfspaces, low-rank matrix predictors.
- **Non-uniform distributions for decision trees**: result is specific to uniform input distribution.
- **"Mechanistic" defenses**: the decision-tree result hints at structure-exploiting defenses; formalizing a general "mechanistic defense" framework is open.
- **Composition of defenders**: if two classes are defendable, are their products/compositions defendable?
- **LLM application**: how does the abstract defendability framework instantiate for modern LLM architectures?
- **Relation to adversarial robustness**: can robust-PAC-learning be reformulated within the defendability game?

## Quotes / Notable Passages

Verified against `raw/CHLX25_Defendability.pdf` on 2026-08-20.

> "We introduce a formal notion of defendability against backdoors using a game between an attacker and a defender. ... The key constraint on the attacker that makes defense possible is that the attacker's strategy must work for a randomly-chosen trigger."

> "We identify efficient defendability as a notable intermediate concept in between efficient learnability and obfuscation."

> "We use indistinguishability obfuscation to show that the class of polynomial size circuits is not efficiently defendable."

> "Under certain cryptographic assumptions, the class of polynomial size circuits is not efficiently defendable, by combining a puncturable pseudorandom function with an efficient indistinguishability obfuscator."
