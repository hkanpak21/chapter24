---
title: Adversarial Examples Might be Avoidable — The Role of Data Concentration in Adversarial Robustness
type: source
date_ingested: 2026-08-20
authors: [Ambar Pal, Jeremias Sulam, René Vidal]
venue: NeurIPS
year: 2023
tags: [adversarial-ml, evasion-attacks, concentration-of-measure, certification, robustness]
claim_quantifier: conditional
antecedent: "Two different antecedents for two different theorems. Thm 2.1 (necessity) is conditional on the existence of an (ε,δ)-robust classifier. Thm 3.1 (sufficiency) is conditional on the data distribution being (ε,δ,γ)-strongly-concentrated — class conditionals sitting on small-volume sets whose 2ε-expansions barely overlap. Strong concentration is NOT measured on any real dataset in this paper; it is exhibited on two constructed examples and assumed for the union-of-subspaces model."
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: none
cls_write: read only
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "A classifier g is defined to be (ϵ, δ)-robust if the robust risk against perturbations with ℓ2 norm bounded by ϵ is at most δ"
cls_evidence_src: Def 2.1
cls_reason: "Classified on Def 2.1's (eps,delta)-robustness, an l2 perturbation-budget bound, per the perturbation-budget rule, rather than as frame=none; the paper bounds nobody computationally anywhere, so without that rule this would default to the none row. Both Thm 2.1 (necessity) and Thm 3.1 (sufficiency, existential) share this same robustness definition, so the row is stable regardless of which theorem is read as the paper's main claim. Read the CLAUDE.md warning first: this paper's 'concentration' is a Lebesgue-volume notion, the opposite geometric sense from computational-concentration-of-measure-etesami's metric-measure sense, though that distinction affects the papers' substance, not these classification fields, which turn on the shared perturbation-budget structure of the evasion setup."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (PSV23) asks whether the impossibility results for adversarial robustness are actually binding for natural data, and answers by identifying a geometric property of the data distribution that decides the question. The property is called **concentration**, but it is defined in a sense *opposite* to the one used in the concentration-of-measure literature: here a distribution is concentrated when it puts most of its mass on a set of very small **Lebesgue volume**. See [Two Senses of Concentration](../concepts/two-senses-of-concentration.md) — reading this page without that distinction in hand will produce exactly the wrong conclusion.

The two main theorems bracket robustness from both sides. Theorem 2.1 (necessity, via Brunn–Minkowski): if any (ε,δ)-robust classifier exists for p, then at least one class conditional must be (C,ε,δ)-concentrated, i.e. must assign mass ≥ 1−δ to a set of volume ≤ C·exp(−nε). Theorem 3.1 (sufficiency): if p is (ε,δ,γ)-**strongly**-concentrated — each class conditional concentrated on its own small-volume set S_k, with q_k of the 2ε-expansion of the *other* classes' sets at most γ — then an (ε, δ+γ)-robust classifier exists. Plain concentration alone is explicitly **not** sufficient (§3): all classes could concentrate on the same small set, in which case not even an accurate classifier exists.

The authors then instantiate the sufficient condition on data supported near a union of low-dimensional linear subspaces, and build a classifier from the dual of an ℓ1 sparse-representation problem whose certified region is a **polyhedron** whose faces and extreme rays are determined by selected training points — a norm-independent certificate, rather than an ℓp ball. On MNIST they show a region of perturbations their method certifies and randomized smoothing does not, and combine the two.

Critically, the paper is careful about what it does and does not overturn (§3, "Compatibility with existing Negative Results"): the impossibility results remain valid and non-vacuous for flat distributions; the positive result is **existential**, giving no algorithm to find the robust classifier in general; and the computational-hardness-of-robust-learning results are untouched. This is a critique of the *scope of an assumption*, not of any theorem.

## Claim Boundary

- **Quantified over:** Thm 2.1 ranges over all classifiers f and all data distributions p on a bounded normalized domain with ℓ2-bounded perturbations: robustness of *any* classifier forces volume-concentration of *some* class conditional. Thm 3.1 ranges over all (ε,δ,γ)-strongly-concentrated p and asserts *existence* of one robust classifier. The multiclass extension of Thm 2.1 to *all* class conditionals additionally requires balanced classes.
- **Antecedent:** Thm 3.1's antecedent is **strong** concentration (Def 3.1), a joint condition on all class conditionals plus their mutual 2ε-separation. The paper does not measure it on MNIST, CIFAR-10 or ImageNet. What it offers instead is an *inference*: since robust classifiers demonstrably exist for these datasets, Thm 2.1 implies the (weak, necessary) concentration must hold — the paper says such distributions "might be concentrated". Strong concentration is verified only on two hand-built examples (Ex. 3.1 on the sphere, Ex. 4.1 on two subspaces) and assumed by construction in the union-of-subspaces model of §4.
- **Does not establish:** (i) that natural image distributions are *strongly* concentrated; (ii) that a robust classifier can be *found* — Thm 3.1 is existential and the paper says so; (iii) that any concentration-of-measure impossibility theorem is wrong. It does not touch [computational hardness of robust learning](computational-hardness-robust-learning.md) or [Adversarial Examples from Computational Constraints](adversarial-examples-computational-constraints.md), and the authors state this explicitly.
- **Abstract vs theorem:** Overstatement found. The abstract says "a key property of the data distribution – concentration on small-volume subsets of the input space – determines whether a robust classifier exists," and contribution 1 says (ε,δ)-concentration "is a necessary condition". But §3 opens by showing that this same property is *not* sufficient, and the sufficiency theorem uses a strictly stronger and differently-shaped hypothesis. One word, "concentration", is doing duty for two non-equivalent conditions across the necessity and sufficiency directions; nothing in the paper "determines" existence in both directions. Also the title, "Adversarial Examples Might be Avoidable", is properly hedged, but the §2 discussion bullet "Since we now know that natural image distributions are concentrated" is not hedged and is an inference from the assumed existence of robust classifiers, not a measurement.

## Key Contributions

- **A volume-relative notion of concentration** (Def 2.2), defined against the Lebesgue measure rather than intrinsically — which lets the analysis operate in the non-realizable setting (probabilistic ground-truth label) rather than requiring a deterministic ground truth f*.
- **Necessity (Thm 2.1)** via Brunn–Minkowski: robustness ⟹ volume-concentration.
- **Insufficiency of plain concentration and the repair (Def 3.1, Thm 3.1)**: strong concentration ⟹ existence of a robust classifier.
- **A worked circumvention (Ex. 3.1)**: a sphere distribution whose class-1 density has unbounded supremum, making the Shafahi et al. lower bound (their Eq. 2) vacuous, while an explicit halfspace classifier is robust.
- **Polyhedral certificates for union-of-subspaces data (§4)**: certificates that are not ℓp balls, whose geometry is read off from selected training points, and which certify perturbations randomized smoothing cannot (§5, MNIST).

## Key Definitions / Theorems

- **Def 2.1 (Robust classifier)**: g is (ε,δ)-robust if R(g,ε) = Pr_{(x,y)~p}[∃ x̄ ∈ B_{ℓ2}(x,ε) : g(x̄) ≠ y] ≤ δ.
- **Def 2.2 (Concentrated distribution)**: q over X ⊆ R^n is (C,ε,δ)-concentrated if ∃ S ⊆ X with q(S) ≥ 1−δ and Vol(S) ≤ C·exp(−nε).
- **Theorem 2.1**: If an (ε,δ)-robust f exists for p, some class conditional q_k̄ is (C̄,ε,δ)-concentrated with C̄ = Vol{x : f(x) = k̄}; with balanced classes, all conditionals are (C_max, ε, Kδ)-concentrated.
- **Def 3.1 (Strongly concentrated)**: p is (ε,δ,γ)-strongly-concentrated if each q_k concentrates on S_k with q_k(S_k) ≥ 1−δ and q_k(∪_{k'≠k} S_{k'}^{+2ε}) ≤ γ.
- **Theorem 3.1**: (ε,δ,γ)-strong concentration ⟹ there exists an (ε, δ+γ)-robust classifier.

## Connections

- **Direct limit on** [The Curse of Concentration (MDM19)](curse-of-concentration.md) — same word, opposite geometric sense, opposite conclusion. PSV23 §6 states the relation explicitly.
- Complements [Empirically Measuring Concentration (MZME19)](empirically-measuring-concentration.md): MZME19 measures the *metric-space* concentration function and finds it does not bind on image benchmarks; PSV23 supplies a geometric account of why a robust classifier can nonetheless exist.
- Cites and circumvents Shafahi et al., "Are adversarial examples inevitable?", and [Fawzi–Fawzi–Fawzi 2018](adversarial-vulnerability-any-classifier.md); PSV23 §6 states its results are "complementary to all such negative results".
- Certification comparison against [Randomized Smoothing (CRK19)](certified-robustness-randomized-smoothing.md); related certification lines: [Convex Outer Polytope](provable-defenses-convex-polytope.md), [Certified Semantic Smoothing](naat-certified-semantic-smoothing.md).
- Does **not** contradict [Computational Hardness of Robust Learning](computational-hardness-robust-learning.md) — existence, not efficient construction.
- Concepts: [Two Senses of Concentration](../concepts/two-senses-of-concentration.md), [Concentration of Measure](../concepts/concentration-of-measure.md), [Intrinsic Robustness](../concepts/intrinsic-robustness.md), [Evasion Attacks](../concepts/evasion-attacks.md).
- Authors: [René Vidal](../entities/rene-vidal.md), [Jeremias Sulam](../entities/jeremias-sulam.md).

## Open Questions / Limitations

- Strong concentration is never measured. Whether MNIST/CIFAR-10/ImageNet satisfy Def 3.1 is open; the paper only argues the weaker necessary condition must hold.
- Thm 3.1 is existential. No algorithm converts a strong-concentration certificate into a robust classifier in general.
- The §4 construction assumes a clean dataset lying *exactly* on a union of low-dimensional linear subspaces; the authors name noisy subspace clustering and general image manifolds as future work.
- The necessity bound degrades with C̄ = Vol{x : f(x)=k̄}: a constant classifier on an unbalanced problem is robust while forcing almost no concentration. The theorem's force depends on the classifier having small-volume decision regions.
- Results are ℓ2 in the statement; the authors assert extension to general ℓp without proving it.

## Quotes / Notable Passages

> "we theoretically demonstrate that a key property of the data distribution – concentration on small-volume subsets of the input space – determines whether a robust classifier exists."

> "We find that (ϵ, δ)-concentration is too general to be a sufficient condition for the existence of a robust classifier"

> "our results are existential and do not provide, in general, an algorithm to construct a robust classifier given a strongly-concentrated distribution."

> "In contrast, our Definition 2.2 of concentrated data distributions can be seen as a relative notion of concentration with respect to the uniform measure µ, in that we call a class conditional q concentrated when it assigns a large q-measure to a set of very small volume"

> "This points to a slack in the analysis in [35, 36], and our work fills this gap by considering ϵ expansions of a different family of sets."
