---
title: Full-Batch Gradient Descent Outperforms One-Pass SGD - Sample Complexity Separation in Single-Index Learning
type: source
date_ingested: 2026-08-22
authors: [Filip Kovačević, Hong Chang Ji, Denny Wu, Mahdi Soltanolkotabi, Marco Mondelli]
venue: "arXiv:2602.02431"
venue_evidence: "dblp search (q=Full-Batch Gradient Descent Outperforms One-Pass SGD): CoRR abs/2602.02431 only, single result, no NeurIPS entry — a one-citer mining lead in exp/survey/notes/2026-08-22-halil-note-venue-mining.md claimed 'NeurIPS, 2025' but dblp does not confirm it"
year: 2026
tags: [learning-theory, sample-complexity, single-index-model, information-exponent, phase-retrieval, batch-reuse, full-batch-gd]
claim_quantifier: universal
antecedent: "Gaussian single-index model x ~ N(0, I_d), y = sigma(<x, theta*>), noiseless, with sigma quadratic (z^2) or truncated quadratic (information exponent 2, generative exponent 2, even link); Theorem 3.1: spherical gradient flow on the correlation loss, n = o(d log d); Theorem 3.2: smooth truncation with large constant M, n >= C M^4 d; Theorem 4.1: Euclidean GD on the squared loss, hard truncation, initialization scale d^{-15}, step size eta <= c/M^2, n >= C M^4 d. The one-pass SGD side of the separation rests on Ben Arous et al. 2021 Theorem 1.4, a lower bound argued for step sizes up to eta ~ 1/d (the largest stable step size in their decomposition)."
model_class: "single-index with quadratic / truncated quadratic link — the phase-retrieval family, information exponent 2, where the two-pass label-transformation mechanism provably gives nothing (even link, generative exponent 2). NOT higher information exponent, NOT multi-index."
algorithm_class: "full-batch spherical gradient flow on the correlation loss (Theorems 3.1, 3.2) and full-batch Euclidean GD on the squared loss from small initialization (Theorem 4.1); separated against one-pass (online) SGD, whose d log d lower bound is class-restricted (spherical correlation-loss dynamics at stable step sizes)"
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: samples
cls_tightness: exponent
cls_baseline: n/a
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: time
cls_assessed: explicit
cls_evidence: "by simply truncating the activation, full-batch GD exhibits a favorable optimization landscape at n ≃ d samples, thereby outperforming one-pass SGD (with the same activation) in statistical efficiency"
cls_evidence_src: abstract
cls_reason: "No attack scenario: both full-batch GD and one-pass SGD are training algorithms in the learner role, no adversary. unit=samples/tightness=exponent for the headline n~d threshold (Theorems 3.2, 4.1), chosen over the algo-class/class pairing used in the sibling page information-exponent-online-sgd because this paper's abstract leads with the sample count, not the restriction to one named algorithm (rule 1). baseline=stated: the d log d one-pass SGD floor is imported from Ben Arous et al. (2021) Theorem 1.4 and stated explicitly as the comparison point, not proved in this paper. second_notion=time per rule 4b: Theorem 4.1 states an explicit, incomparable step-count bound (T >~ log d gradient steps) for the same learner alongside the sample bound. Caution for the survey: Theorem 3.1 (not the classified row, per rule 1) proves the opposite for the untruncated quadratic, full-batch reuse gives no advantage over one-pass SGD when n=o(d log d); the positive separation classified here holds only after truncating the activation, and even then the gain over one-pass SGD is a single log factor (Theta(d) vs Theta(d log d)), not an exponent-independent escape. The paper explicitly distinguishes its full-batch mechanism from the two-pass label-transformation mechanism of Dandi/Damian et al., calling full-batch reuse over a diverging time horizon 'a different resource from two passes'."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper locates a sample-complexity separation between full-batch GD (all n samples reused every step) and one-pass SGD (each sample used once) in the cleanest setting where the known two-pass mechanism cannot operate: an even Gaussian single-index target with information exponent 2 (quadratic / phase retrieval), where any label preprocessing leaves the information exponent at 2, so the Dandi / Lee / Arnaboldi batch-reuse gains do not apply and one-pass SGD needs n ≳ d log d (Ben Arous et al.).

Three results. Theorem 3.1 (negative): for the unbounded quadratic sigma(z) = z^2, full-batch spherical gradient flow on the correlation loss is a power iteration on A* = (2/n) Σ y_i x_i x_i^T, and when n = o(d log d) its limit is asymptotically uncorrelated with theta* — full-batch reuse buys nothing over one-pass SGD for this activation. The failure is caused by the unboundedness: heavy-tailed y_i inflate the bulk spectrum. Theorem 3.2 (positive): smoothly truncating the quadratic at level M restores a benign landscape — with n >= C M^4 d (relaxable to C M^{2.01} d), the flow converges to overlap >= 1 - C(e^{-M/2} + (d/n)^{1/5}) with probability 1 - exp(-c d^{1/5}); the proof establishes a uniform-in-theta BBP transition for the trajectory Hessian and invokes the stable manifold theorem. Since the truncated activation still has information exponent 2, the one-pass lower bound still applies, giving the separation: Theta(d) for full-batch GD vs ≳ d log d for one-pass SGD on the same activation. Theorem 4.1 (rates and estimation): full-batch Euclidean GD on the squared loss from initialization scale d^{-15} achieves strong (exact) recovery: for n >= C M^4 d, after t̄ <= C log d / eta steps the squared error contracts geometrically, ||theta_t - theta*||^2 <= C(1 - eta·alpha)^{t - t̄}. The paper calls this the first strong-recovery-plus-rate guarantee for plain full-batch GD in the proportional regime.

## Claim Boundary

- **Quantified over:** the specific quadratic and truncated-quadratic links (not a family of links); all n, d large in the stated regimes; randomness of data and uniform spherical initialization. Theorem 3.1 is universal over the n = o(d log d) regime (almost-sure triviality of the limit); Theorems 3.2 and 4.1 are high-probability guarantees above explicit sample thresholds.
- **Antecedent and whether it holds:** the separation has one leg per algorithm and they are not symmetric. The full-batch leg is proven in this paper. The one-pass leg is Ben Arous et al. 2021 Theorem 1.4, which the authors describe carefully: the log d necessity is "argued" under an optimal stable step size eta ≃ 1/d — it binds the spherical correlation-loss online dynamics at step sizes up to ~1/d, not every batch size and schedule ("establishing a hardness result that holds for all batch sizes and step-size schedules is challenging"). The truncation is load-bearing on the positive side and the smooth-vs-hard choice is technical.
- **Does not establish:** (a) a separation for the plain quadratic activation — Theorem 3.1 proves the opposite: there full-batch spherical flow is as bad as one-pass SGD; the separation requires truncating, a (minimal) modification of the link; (b) any unconditional or SQ/LDP lower bound — the negative results bind specific dynamics (spherical correlation-loss flow; online SGD at stable step sizes); (c) higher information exponent or multi-index targets — named as future work; (d) runtime characterization for the spherical dynamics of Section 3 (open, stated in the conclusion); (e) noise robustness — the model (1.1) as analyzed is noiseless.
- **Abstract vs theorem:** the abstract's "outperforming one-pass SGD (with the same activation) in statistical efficiency" is Theorem 3.2 plus the imported online lower bound with its step-size qualification, which the body states but the abstract does not; "n ≳ d samples and T ≳ log d gradient steps suffice to achieve strong (exact) recovery" matches Theorem 4.1 including its d^{-15} initialization scale, which the abstract calls "small initialization".

## Key Contributions

- Theorem 3.1: for sigma(z) = z^2 and n = o(d log d), the spherical correlation-loss gradient flow's limiting overlap with theta* is 0 almost surely — full-batch updates give no statistical advantage over one-pass SGD for the unbounded quadratic.
- Theorem 3.2: for the smooth truncation at level M and n >= C M^4 d, limiting overlap >= 1 - C(e^{-M/2} + (d/n)^{1/5}) with probability >= 1 - exp(-c d^{1/5}); weak recovery at finite n/d, hence the separation from one-pass SGD's d log d.
- Theorem 4.1: hard-truncated quadratic, Euclidean GD on the squared loss, theta_0 uniform on the radius-d^{-15} sphere, eta <= c/M^2, n >= C M^4 d: geometric convergence to exact recovery after a search phase of t̄ <= C log d/eta steps; the log d runtime is verified empirically (Figure 2c), as is the d log d sample threshold for the untruncated case (Figure 1c).
- Technical: uniform-in-trajectory BBP phase transition for A(theta) via decomposition A(theta) = A* - B(theta) with VC-type uniform control of the truncation term; stable manifold argument for convergence to an informative direction.

## Detection versus estimation, and the class of the bound

Theorem 3.2 is weak recovery (detection-grade: order-one overlap); Theorem 4.1 is estimation in the strongest sense (exact recovery with a rate). The negative statements are class-relative on both sides: Theorem 3.1 binds full-batch spherical correlation-loss flow with the unbounded quadratic, and the one-pass d log d floor binds online spherical correlation-loss SGD at stable step sizes. Neither is a bound on all polynomial-time algorithms — spectral methods plus AMP already achieved n ≳ d and strong recovery at finite n/d in this model (Mondelli-Montanari, Luo et al., Mondelli-Venkataramanan), which is the benchmark the GD analysis is catching up to.

## Connections

- The one-pass floor it separates from: [information-exponent-online-sgd](information-exponent-online-sgd.md) (Ben Arous et al. 2021, Theorem 1.4 and the log d escape time at information exponent 2).
- Why the two-pass mechanism is inapplicable here: even link ⇒ generative exponent 2; see [reusing-batches-breaks-exponents](reusing-batches-breaks-exponents.md) (whose Section 3 the paper cites for the even-link obstruction), [sgd-reuse-info-theoretic-limit](sgd-reuse-info-theoretic-limit.md), [repetita-iuvant-data-repetition](repetita-iuvant-data-repetition.md). This paper's point is precisely that full-batch reuse over a diverging time horizon is a different resource from two passes.
- The exponent taxonomy: [generative-exponent-single-index](generative-exponent-single-index.md) ([Damian et al. 2024] and [Joshi et al. 2025] are cited for information/generative exponent); the harmonic refinement [single-index-harmonic-decomposition](single-index-harmonic-decomposition.md) is the concurrent lens on why spectral-type access to the data beats direction-only SGD in this k* = 2 regime.
- Concepts: [information exponent](../concepts/information-exponent.md), [generative exponent](../concepts/generative-exponent.md), [single-index model](../concepts/single-index-model.md), [statistical-computational gaps](../concepts/statistical-computational-gaps.md).

## Open Questions / Limitations

- Runtime of the spherical correlation-loss dynamics (Section 3) is not characterized.
- Sharp constants for the full-batch phase transition (suggested route: dynamical mean-field theory).
- Higher information exponent links and multi-index targets: whether full-batch reuse yields a similar or larger gain is open.
- The separation's SGD leg inherits the step-size restriction of Ben Arous et al.'s lower bound; a lower bound over all schedules and batch sizes remains open.

## Quotes / Notable Passages

> "by simply truncating the activation, full-batch GD exhibits a favorable optimization landscape at n ≃ d samples, thereby outperforming one-pass SGD (with the same activation) in statistical efficiency"

> "it has been argued that the log d factor is necessary for weak recovery under an “optimal” stable step size η ≃ 1/d — see the lower bound in Ben Arous et al. (2021, Theorem 1.4)."

> "full-batch spherical gradient flow with respect to the correlation loss is unable to provide a sample complexity improvement over one-pass SGD" — context: the quadratic-activation negative result; the surrounding sentence reads "This implies that, for the quadratic activation, ..." and the contribution bullet ends "indicating that full-batch updates offer no statistical advantage over their one-pass counterpart"

> "To our knowledge, this is the first convergence rate and strong recovery guarantee for learning single-index models with information exponent 2 using standard full-batch GD in the proportional regime" (hyphenation flattened by extraction)
