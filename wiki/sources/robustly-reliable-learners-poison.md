---
title: "Robustly-Reliable Learners Under Poisoning Attacks"
type: source
date_ingested: 2026-04-12
authors: [Maria-Florina Balcan, Avrim Blum, Steve Hanneke, Dravyansh Sharma]
venue: "COLT 2022"
venue_evidence: "https://proceedings.mlr.press/v178/balcan22a/balcan22a.pdf; PMLR volume 178 is the COLT 2022 proceedings"
year: 2022
tags: [adversarial-ml, PAC-learning, poisoning-attacks, certification, learning-theory, reliable-learning]
claim_quantifier: universal
antecedent: "For the main characterization, realizability — the target concept lies in H — and a corruption budget η that the adversary does not exceed, measured as a fraction of the training sample under normalized Hamming distance. The certificate is void the moment the budget is exceeded, and the budget is an input to the guarantee rather than something the defender can verify. The efficient learner additionally needs an ERM oracle for H; the truly polynomial-time result needs linear separators under isotropic log-concave marginals."
date_verified: 2026-08-20
cls_target: train data
cls_family: poison
cls_phase: train time
cls_access: none
cls_write: corpus
cls_frame: compute
cls_party: learner
cls_unit: queries
cls_tightness: budget
cls_baseline: n/a
cls_baseline_checked: yes
cls_second_party: corruption
cls_second_notion: time
cls_assessed: implicit
cls_evidence: "Learner L from Theorem 3.1 can be implemented efficiently given an ERM oracle for H"
cls_evidence_src: Thm 3.2
cls_reason: "Judgment call under rule 4: both the adversary (corruption budget η, a genuine capability bound, not a near-miss) and the learner (efficient ERM-oracle implementation, Thm 3.2; truly poly-time for linear separators, Thm 4.1) are bounded. Rule 4 assigns party to whichever bound is computational, so party=learner, unit=queries (ERM-oracle calls), second_party=corruption (η), second_notion=time (Thm 4.1's poly-time special case, same party, per rule 4b). This reading privileges a secondary efficiency result over the paper's headline correctness-certificate claim; a second reader may instead prefer party=attacker, unit=corruption, tightness=budget, frame=capability, treating the ERM-oracle result as incidental rather than a formal two-party bound."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper initiates the theory of *robustly-reliable learners* against instance-targeted data poisoning attacks. The key conceptual contribution is a qualitative upgrade to defense certificates: prior work (Levine–Feizi 2021; Gao et al. 2021) produced *stability* certificates (the prediction on x doesn't change when ≤ η fraction of training data is corrupted); this paper produces *correctness* certificates (the prediction on x is guaranteed *correct* under the same corruption budget, provided the target concept lies in H).

The optimal robustly-reliable learner L, given a (possibly corrupted) sample S', outputs for each test x a pair (y, η) where η is the largest value for which x lies in the agreement region of H_η(S') = {h ∈ H : err_{S'}(h) ≤ η}. The paper proves this learner is pointwise optimal — no other strongly robustly-reliable learner has a strictly larger confident region, matched by lower bounds (Theorem 3.5). L can be implemented efficiently given an ERM oracle for H (Theorem 3.2) by re-running ERM with forced labels at the test point.

Results extend to: instance-adaptive adversaries, active learning with adaptive adversaries, and agnostic learning. For linear separators under log-concave marginals, the authors give a truly polynomial-time (non-oracle) robustly-reliable algorithm (Theorem 4.1), building on Awasthi et al. 2017.

Model: nasty-adversary poisoning (Bshouty et al. 2002) — the adversary picks η fraction of the training sample and arbitrarily modifies both x and y. Instance-targeting means the adversary can know the test point x before committing corruptions.

## Claim Boundary

- **Quantified over:** all hypothesis classes, with matching upper and lower bounds on the region that can be certified — the paper's phrase is "nearly-tight matching upper and lower bounds". The efficient non-oracle algorithm is existential and specific: linear separators under log-concave marginals.
- **Antecedent:** realizability for the strongest statements, and a known corruption budget η. Both matter. If the target concept is not in H the guarantees weaken to the agnostic form given in Section 6, where the adversary can force mistakes only where every low-error hypothesis also errs.
- **Which party is constrained:** the **adversary**, in the fraction η of training examples it may corrupt. That is a counting budget, not a resource bound — within it the adversary is arbitrary, computationally unbounded, and instance-targeted, meaning it may know the test point in advance. The **defender** is constrained by compute in the sense that the general learner is stated relative to an ERM oracle, with genuine polynomial time achieved only for the linear-separator case.
- **Does not establish:** (i) any guarantee once the budget is exceeded, and the paper offers no way to detect that; (ii) a certificate on points outside the agreement region, where the learner abstains rather than being wrong; (iii) efficiency for general classes without an ERM oracle; (iv) anything about test-time evasion, which is a different threat model.
- **Abstract vs theorem:** none found. The abstract states the budget condition inline ("so long as the adversary has not exceeded a given corruption budget") and marks the efficient algorithms as oracle-based except in the log-concave case.

## Key Contributions

- **Definition 1 (robustly-reliable learner)**: L is robustly-reliable for S' w.r.t. H if L_{S'}: X → Y × R outputs (y, η) such that whenever S' ∈ A_η(S) for some sample S labeled by h* ∈ H, y = h*(x).
- **Theorem 3.1 (optimal learner)**: The learner L that outputs (y, η) = (common label of Agree(H_η(S')), largest η such that x ∈ Agree(H_η(S'))) is strongly robustly-reliable, with confident region containing Agree(H_η(S')).
- **Theorem 3.2 (efficient ERM implementation)**: L can be implemented with O(|Y|) calls to an ERM oracle for H: for each y ∈ Y, run ERM on S' ∪ (m+1 copies of (x, y)) to force h(x) = y and measure the resulting error.
- **Theorem 3.3 (η-robustly-reliable region bound)**: RR^L(S, h*, η) ⊇ Agree(B^H_S(h*, 2η)); with m = O((d + ln(1/δ))/ε²) samples, this ⊇ Agree(B^H_D(h*, 2η + ε)) w.p. 1−δ.
- **Theorem 3.5 (matching lower bound)**: No strongly robustly-reliable learner can have a confident region strictly larger than Agree(B^H_D(h*, 2η)). L is pointwise optimal.
- **Theorem 4.1 (efficient algorithm for linear separators)**: Under isotropic log-concave marginals, there is a poly-time algorithm achieving near-optimal robust-reliability region, strictly improving Gao et al. 2021 (which required uniform-on-ball).
- **Active learning extensions (Theorems 5.1, 5.3)**: Disagreement-based active learning achieves comparable robust-reliability guarantees with reduced label complexity, even against adversaries adaptive to the query sequence.
- **Agnostic extensions (Theorems 6.1–6.5)**: In the agnostic setting, the adversary can cause mistakes only on points where *every* low-error hypothesis in H would also err.

## Key Definitions / Theorems

**Adversary class A_η**: A_η(S) = {S' : d(S, S') ≤ η} where d is normalized Hamming distance. Nasty model: adversary picks which η fraction to corrupt and how.

**Agreement region**: Agree(H) = X \ DIS(H) where DIS(H) = {x : ∃h_1, h_2 ∈ H with h_1(x) ≠ h_2(x)}.

**Disagreement coefficient θ (Hanneke 2007)**: sup_{r > ε} Pr_{D_X}[DIS(B^H_D(h*, r))] / r — controls the size of the confident region.

**Version space H_η(S')**: {h ∈ H : err_{S'}(h) ≤ η} — concept classes consistent with at most η corruption.

**Robustly-reliable correctness**: RobC^L(D, η, S) = Pr_{x~D_X}[x ∈ RR^L(S, h*, η)].

**Key proof idea (Theorem 3.3)**: ∩_{S' ∈ A_η(S)} Agree(H_η(S')) = Agree(B^H_S(h*, 2η)), because h ∈ B^H_S(h*, 2η) iff ∃ S' ∈ A_η(S) with h ∈ H_η(S').

**Linear separators + log-concave (Theorem 4.1)**: Combines Awasthi-Balcan-Long 2017 outlier-removal learner with geometric construction of the agreement region under known marginal.

## Connections

- [Poisoning Attacks](../concepts/poisoning-attacks.md) — updated with instance-targeted formalization and correctness certificates
- [Reliable Learning](../concepts/reliable-learning.md) (new) — generalizes Rivest–Sloan 1988 and El-Yaniv–Wiener 2012 selective classification to poisoning
- [Robust PAC Learning Characterization](robust-pac-learning-characterization.md) — Hanneke coauthor; contrast test-time (evasion) with training-time (poisoning) robustness
- [Planting Undetectable Backdoors](planting-undetectable-backdoors.md) — complementary: backdoors show some poisoning is *undetectable*; this paper shows what can be *certified* against bounded poisoning
- [Complexity Theoretic Adversarial ML](complexity-theoretic-adversarial-ml.md) — Mahloujifar's p-tampering is a different (online, untargeted) poisoning model
- [Maria-Florina Balcan](../entities/maria-florina-balcan.md), [Avrim Blum](../entities/avrim-blum.md), [Steve Hanneke](../entities/steve-hanneke.md), [Dravyansh Sharma](../entities/dravyansh-sharma.md)

## Open Questions / Limitations

- Beyond linear separators: efficient (non-oracle) robustly-reliable algorithms for other natural classes.
- Removing the realizability assumption for the optimal-region characterization in general H — agnostic results are weaker.
- Adaptive adversaries for passive (non-active) learning: how much the lower bound degrades.
- Connection to differential privacy / robust statistics: robustly-reliable learners as a certification layer over robust estimators.
- Computational hardness of computing Agree(H_η(S')) for general H — linear-separator result suggests structure matters a lot.

## Quotes / Notable Passages

> "Our guarantees are substantially stronger than those in prior approaches, which were only able to provide certificates that the prediction of the learning algorithm does not change, as opposed to certifying that the prediction is correct."

> "The set of points on which our learner should be confident are those that belong to the region of agreement of low error hypotheses."
