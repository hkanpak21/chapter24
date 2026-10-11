---
title: "PAC-learning in the Presence of Evasion Adversaries"
type: source
date_ingested: 2026-04-12
authors: [Daniel Cullina, Arjun Nitin Bhagoji, Prateek Mittal]
venue: "NeurIPS 2018"
venue_evidence: "https://proceedings.neurips.cc/paper/2018/hash/8f85517967795eeef66c225f7883bdcb-Abstract.html (camera-ready title \"PAC-learning in the presence of adversaries\", NeurIPS 2018, pp. 230-241, same authors/paper as arXiv:1806.01471)"
year: 2018
tags: [adversarial-ml, PAC-learning, sample-complexity, robustness, learning-theory, evasion-attacks]
claim_quantifier: universal
antecedent: "For the sample-complexity bound, a binary hypothesis class H and a nearness relation R, with the adversarial VC dimension of the corrupted class finite. For the halfspace theorem, the perturbation set must be a nonempty closed convex origin-symmetric subset of R^d, which covers every ℓp ball with p ≥ 1 but excludes non-convex and asymmetric perturbation sets."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: none
cls_write: read only
cls_frame: statistical
cls_party: learner
cls_unit: samples
cls_tightness: budget
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "For a space X, a classifier family H, and an adversarial constraint R, there is a universal constant C such that m_{H,R}(δ,ε) ≤ C·(d log(d/ε)+log(1/δ))/ε²."
cls_evidence_src: Thm 1
cls_reason: "Matches the sibling adversarially-robust-pac-regression.md classification (same genre: PAC sample-complexity bound under an unrestricted evasion adversary). frame=statistical not capability: Theorem 1's nearness relation R is fully general ('For a space X, a classifier family H, and an adversarial constraint R'), with no numeric restriction; the 'adversarial budget constraint ǫ' sentence in §2 is an illustrative example of how R could be built, not a restriction the theorem's own bound depends on, so rule 5's norm-ball convention does not decide the headline claim. party=learner/unit=samples/tightness=budget: the only bound in Theorem 1 is the learner's sample complexity, a closed-form definitional parameter with no stated relation to any adversary quantity; the adversary R is unconstrained (rule 2), so second_party=none. access=none/write=read only follow the corpus default for evasion-theory papers with no explicit stated query-access model. The halfspace corollary (AVC=VC=d+1, requiring convex origin-symmetric R) is a narrower instantiation and not what the abstract leads with, so it does not decide the row (rule 1)."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper is the first to formally extend the PAC learning framework to include a test-time (evasion) adversary and to introduce the **adversarial VC-dimension** (AVC) as the natural complexity measure for this setting. Given a nearness relation R ⊆ X × X, the authors define *corrupted hypotheses* κ_R(h) that output a special ⊥ ("always wrong") label whenever there exist two points in a test example's neighborhood receiving opposite labels from h. The VC-dimension of this corrupted class is the adversarial VC-dimension, which yields a Fundamental-Theorem-style sample complexity bound m_{H,R}(δ,ε) = O((AVC · log(AVC/ε) + log(1/δ))/ε²).

The key concrete result: for halfspace classifiers in R^d with any convex, origin-symmetric perturbation set (all ℓ_p, p ≥ 1, adversaries), AVC = VC = d+1. Thus sample complexity of PAC learning halfspaces does not increase in the presence of norm-bounded evasion adversaries — closing an open question from Schmidt et al. (2018).

The authors also show AVC can be *either larger or smaller* than the standard VC-dimension, depending on H and R, making it an interesting dimension in its own right.

Historical context: this paper set up a uniform-convergence-style theory that Montasser–Hanneke–Srebro (COLT 2019) subsequently showed was fundamentally inadequate for general H (finite VC classes may not admit *proper* robust learning; AVC can be infinite even when VC is finite).

## Claim Boundary

- **Quantified over:** the upper bound is universal over hypothesis classes and nearness relations, conditional on the adversarial VC dimension being finite. The halfspace equality AVC = VC = d+1 is quantified over all convex origin-symmetric perturbation sets, for one hypothesis class. The incomparability result is existential in both directions: there exist H, R with AVC ≫ VC and others with AVC ≪ VC.
- **Antecedent:** finiteness of the adversarial VC dimension. This is the clause the follow-up literature broke — [Montasser, Hanneke and Srebro 2019](vc-classes-adversarially-robustly-learnable.md) exhibit classes with vc(H) ≤ 1 whose corrupted class has unbounded VC dimension, so the antecedent can fail for classes that are nonetheless robustly learnable improperly.
- **Which party is constrained:** the **learner**, in sample complexity, and further restricted to adversarial ERM, which is a proper rule. The adversary is unbounded in computation and constrained only by the nearness relation R, a geometric object. No compute is priced on either side.
- **Does not establish:** (i) that finite AVC characterizes robust learnability — it is sufficient within the uniform-convergence framework and is not necessary; (ii) that RERM suffices in general, which the 2019 follow-up refutes; (iii) any efficient procedure for computing AVC beyond halfspaces; (iv) anything about training-time attacks.
- **Abstract vs theorem:** none found. The abstract restricts the halfspace result to "a sample-wise norm-constrained adversary of the type commonly studied for evasion attacks" and presents the incomparability as making the dimension "an interesting object of study in its own right", not as a characterization.

## Key Contributions

- **Adversarial VC-dimension (Definition 5)**: AVC(H, R) = VC of the corrupted hypothesis class κ_R(H), where κ_R(h): X → {-1, +1, ⊥} outputs ⊥ when h disagrees inside the neighborhood N(x).
- **Theorem 1 (sample complexity upper bound)**: m_{H,R}(δ, ε) ≤ C · (d log(d/ε) + log(1/δ))/ε² where d = AVC(H, R). Follows from the Rademacher-complexity / Sauer-Shelah chain.
- **Theorem (halfspaces)**: For H = halfspaces over R^d and R derived from any nonempty closed convex origin-symmetric set B (so R = {(x,y) : y−x ∈ B}), AVC(H, R) = VC(H) = d+1. Closes an open question of Schmidt et al. 2018.
- **Examples**: Explicit constructions where AVC ≫ VC and where AVC ≪ VC — AVC is not monotone in either H or R relative to VC.
- **Corrupted hypothesis construction**: κ_R(h)(x) = −1 if h(y) = −1 ∀y ∈ N(x); +1 if h(y) = +1 ∀y ∈ N(x); ⊥ otherwise.

## Key Definitions / Theorems

**Adversarial expected risk (Def 1)**: L_P(h, R) = E_{(x,c)~P}[max_{y∈N(x)} ℓ(h(y), c)], where ℓ is 0-1 loss.

**Adversarial ERM (Def 2)**: AERM_{H,R}(x, c) = argmin_{h∈H} L_{(x,c)}(h, R).

**Corrupted hypothesis (Section 3.1)**: κ_R: (X → {±1}) → (X → {±1, ⊥}). Equivalence lemma: L_P(h, R) = L_P(κ_R(h), I_X). Learning with adversary R for H = learning without adversary for κ_R(H).

**Adversarial VC-dimension (Def 5)**: AVC(H, R) = sup { n : σ'(λ(κ_R(H)), n) = 2^n } where σ' is the shattering coefficient of the loss class.

**Halfspace AVC theorem**: Proved using signed-distance-to-boundary analysis — for halfspace h with weight vector w, the optimal evasion attack moves x by a ∥·∥_B-minimal amount, and the resulting corrupted hypothesis is itself a halfspace-like object with VC ≤ d+1.

## Connections

- [VC Classes are Adversarially Robustly Learnable](vc-classes-adversarially-robustly-learnable.md) — Montasser–Hanneke–Srebro 2019 show that AVC can be infinite when VC is finite, making AVC insufficient for characterizing learnability; uniform-convergence program this paper belongs to fails in general.
- [Robust PAC Learning Characterization](robust-pac-learning-characterization.md) — Montasser et al. 2022, the eventual characterization via global one-inclusion graph dimension.
- [Adversarial VC Dimension](../concepts/adversarial-vc-dimension.md)
- [Robust PAC Learning](../concepts/robust-pac-learning.md)
- [Evasion Attacks](../concepts/evasion-attacks.md)
- [Daniel Cullina](../entities/daniel-cullina.md), [Prateek Mittal](../entities/prateek-mittal.md)

## Open Questions / Limitations

- AVC does not characterize general robust learnability — the follow-up COLT 2019 paper showed finite VC classes can have infinite AVC yet still be (improperly) robustly learnable.
- Uniform convergence framework inherently justifies only proper learning (RERM); insufficient in the general case.
- Computing AVC for non-halfspace classes (neural networks, decision trees) is open in general.
- Extension to multi-class and regression settings.

## Quotes / Notable Passages

> "In particular, we extend the Probably Approximately Correct (PAC)-learning framework to account for the presence of an adversary. We first define corrupted hypothesis classes which arise from standard binary hypothesis classes in the presence of an evasion adversary and derive the Vapnik-Chervonenkis (VC)-dimension for these, denoted as the adversarial VC-dimension."
>
> _Corrected 2026-08-20 against `raw/CBM18_PACEvasionAdversaries.pdf`. This page previously elided the middle clause and restarted the second sentence as "We derive the…", which is not in the paper; the full abstract sentences are restored._

> "The adversarial VC-dimension can be either larger or smaller than the standard VC-dimension depending on the hypothesis class and adversary."
