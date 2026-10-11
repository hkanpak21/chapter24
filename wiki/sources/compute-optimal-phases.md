---
title: 4+3 Phases of Compute-Optimal Neural Scaling Laws
type: source
date_ingested: 2026-08-22
authors: [Elliot Paquette, Courtney Paquette, Lechao Xiao, Jeffrey Pennington]
venue: "NeurIPS 2024"
venue_evidence: "https://proceedings.neurips.cc/paper_files/paper/2024/hash/1dccfc3ee01871d05e33457c61037d59-Abstract-Conference.html; Advances in Neural Information Processing Systems 37 (NeurIPS 2024)"
year: 2024
tags: [scaling-laws, learning-theory, sample-complexity, compute-accounting]
claim_quantifier: conditional
antecedent: the power-law random features model with data exponent alpha and target exponent beta, trained by one-pass SGD with batch size of order one and admissible learning rate, in the large-d limit, with alpha > 1/4, 2(alpha+beta) > 1, beta < 1 + 2alpha, and (alpha, beta) off the critical lines
model_class: power-law random features (PLRF), three parameters (alpha, beta, d)
algorithm_class: one-pass SGD on PLRF, mean-squared loss, constant learning rate, batch size O(1)
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: flops
cls_tightness: exponent
cls_baseline: n/a
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: parameters
cls_assessed: explicit
cls_evidence: "the compute-optimal parameter is d⋆ = f1/2 and it is independent of α and β"
cls_evidence_src: Phase Ib discussion (compute-optimal d*)
cls_reason: "party=learner: one-pass SGD on PLRF, no adversary. unit=parameters for d*(f), the paper's own headline quantity (abstract: 'computing the optimal model-parameter-count as a function of floating point operation budget'); second_notion=samples (rule 4b) because iterations r in this one-pass, fresh-sample-per-step regime are total samples consumed, matching the convention used for information-exponent-online-sgd and leap-complexity-sgd's step-count-as-samples treatment. The compute budget f itself (flops = iterations × batch × parameters) has no unit-vocabulary value, the exact gap the assigning brief names by example ('floating-point operations or a token budget'), flagged here rather than forced into time. tightness=exponent for the proven d*(f)≍f^{1/2} formula (Theorem 2.1-derived, within the model). baseline=absent: the paper states outright 'another algorithm could change the compute-optimal curves for these phases' and leaves a cross-algorithm lower bound as future work."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The compute-optimal frontier as a theorem. The model is power-law random features (PLRF): minimize P(theta) = E[(<W^T x, theta> - <x, b>)^2] over theta in R^d, where the data spectrum decays as j^{-2alpha} (data complexity), the target coefficients as a power law with exponent beta (target complexity), and W in R^{v x d} is a fixed Gaussian embedding giving the model capacity d. Training is one-pass SGD with fresh samples each step, and compute is priced by f = iterations x batch x parameters, the 6ND convention. The paper derives a Volterra equation for the expected loss, replaces the random resolvent by a deterministic equivalent, and proves (Theorem 2.1, within the stated (alpha, beta) region) an approximation for the whole loss curve P(r; d) valid over all iteration counts, improving as d grows.

Optimizing d at fixed flops then yields the compute-optimal curve exactly. The (alpha, beta) plane splits into 4 phases plus 3 subphases according to which term dominates the tradeoff: model capacity (Phase I), feature-embedding distortion (Phase II), and SGD noise (Phases III, IV). In Phases Ib, III, and IVa the optimal parameter count is d*(f) ≍ f^{1/2}, independent of alpha and beta, a theoretical derivation of Chinchilla-type equal scaling over a large region of the plane. In the SGD-noise phases the frontier is a property of the algorithm, and the paper says outright that another algorithm could move it.

## Claim Boundary

- Quantified over: the deterministic-equivalent loss of one-pass SGD on PLRF, in the large-d limit, for (alpha, beta) in the admissible region off the critical lines. The optimization is over the parameter count d and (in Section I) the learning rate and batch, never over algorithms.
- Antecedent: the PLRF distributional assumptions and the learning-rate/batch admissibility condition (kernel norm below one, gamma(B+1) < 2). These are constructions, so they hold by fiat inside the model. The mapping from PLRF to any real network is an analogy, not part of the theorem. The analysis is also for the deterministic equivalent, with the equivalence to finite-d SGD supported numerically rather than proven at the required precision (the paper says a custom analysis would be needed and does not attempt it).
- Does not establish: any lower bound over algorithms. The frontier is minimal over d for one fixed algorithm. The paper states that in Phases III and IV the frontier is set by SGD noise and that a different algorithm could change it, and leaves that direction open. No claim prices all learners, all optimizers, or any adversary.
- Abstract against theorem: the abstract is accurate. The one gap to carry is that Theorem 2.1 is proven for alpha > 1/4 while the paper expects validity for all 2alpha + 2beta > 1 on numerical evidence, an explicitly flagged extrapolation.
- Status: proven within model and algorithm class (deterministic-equivalent level), with the finite-d correspondence and the sub-threshold extension empirical. Breaks if the algorithm changes (their own statement), if batch size scales with d (excluded by assumption), or if the feature map is not linear random features.
- No-skipping postulate: supporting, in exactly the recipe-relative form and no stronger. Within PLRF plus one-pass SGD the best loss at f flops is a theorem, so no allocation of the same recipe skips ahead, and the paper's own caveat that another algorithm could move the frontier is the precise reason the postulate must stay recipe-relative.

## Key Contributions

- A closed deterministic description (Volterra equation with deterministic-equivalent forcing and kernel) of one-pass SGD on PLRF over the whole training trajectory.
- Theorem 2.1: an explicit approximation for the loss curve, valid over all iteration counts, with error vanishing as d grows, in the stated (alpha, beta) region.
- The full phase diagram: 4 phases + 3 subphases of compute-optimal behavior, with proved scaling-law exponents d*(f) ≍ f^xi and P*(f) ≍ f^{-eta} in each.
- The universality region where d*(f) ≍ f^{1/2}, recovering Chinchilla-type allocation from within a model.
- Compute-optimal learning rate and batch: B = 1 is optimal, maximal stable gamma is optimal except in Phase IV, where an interior gamma*(f) is derived (Proposition I.1).
- A warning, from simulation at realistic budgets, that measured scaling exponents at one-GPU-day scale have not converged to their asymptotic values.

## Key Definitions / Theorems

- PLRF: min over theta in R^d of E[(<W^T x, theta> - <x, b>)^2], data spectrum D = diag(j^{-2alpha}), target b with power-law coefficients governed by beta, W Gaussian with variance 1/d.
- Compute convention: f = (iterations r x batch B) x parameters d.
- The Volterra equation E[P(theta_r) | W] = F(r) + (K * E[P])(r), forcing = gradient descent on the population risk of the random-features model, kernel = excess risk per unit of SGD noise.
- Theorem 2.1: the approximate solution for P through explicit Fpp, Fac, F0, Kpp terms, each a named mechanism (population training, embedding distortion, capacity, SGD noise).
- The phase classification by which pair of terms crosses at the optimum, with exact exponents per phase (Table 2 of the paper).

## Connections

- Theoretical anchor for [chinchilla-compute-optimal](chinchilla-compute-optimal.md): equal scaling appears as the universal d* ≍ f^{1/2} region.
- Sibling of [dynamical-model-scaling-laws](dynamical-model-scaling-laws.md), which reaches asymmetric allocation by DMFT in a closely related model, and base model for [feature-learning-improves-scaling](feature-learning-improves-scaling.md), whose lazy limit recovers this phase diagram for alpha > 1 and whose feature-learning dynamics change the hard-task exponents.
- [learning-rate-induces-generative-exponent](learning-rate-induces-generative-exponent.md) is the single-index counterpart of the same lesson: the exponent belongs to the algorithm and its hyperparameters.
- Contrast with [information-exponent-online-sgd](information-exponent-online-sgd.md): same algorithm class (one-pass SGD), different target family, and in both the stated cost is algorithm-relative.

## Open Questions / Limitations

- No lower bound over algorithms, stated by the authors as an open direction. The SGD-noise phases are exactly where a better algorithm might beat the frontier.
- The finite-d against deterministic-equivalent correspondence at the precision the exponents need. Open, numerically supported.
- Batch size growing with d, label noise beyond the flagged plateau effect, and nonlinear feature maps are all outside the theorem.

## Quotes / Notable Passages

> "Indeed, another algorithm could change the compute-optimal curves for these phases."

(Introduction, on Phases III and IV. The sentence that fixes what the theorem does not claim.)

> "The latter suggesting that another stochastic algorithm might change the compute-optimal curve; we leave this interesting direction to future research."

(Conclusion.)

> "This serves as a potential warning for empirically derived scaling laws."

(Discussion of exponents still drifting at one-A100-GPU-day scale.)

> "We furthermore derive, with mathematical proof and extensive numerical evidence, the scaling-law exponents in all of these phases, in particular computing the optimal model-parameter-count as a function of floating point operation budget."

(Abstract.)
