---
title: How Feature Learning Can Improve Neural Scaling Laws
type: source
date_ingested: 2026-08-22
authors: [Blake Bordelon, Alexander Atanasov, Cengiz Pehlevan]
venue: ICLR 2025 (stated in PDF)
year: 2025
tags: [scaling-laws, learning-theory, sample-complexity]
claim_quantifier: conditional
antecedent: a two-layer linear network on power-law features with capacity exponent alpha and source exponent beta, trained by a form of projected gradient descent (equivalently ordinary gradient descent on the two-layer linear network after random projections) with feature-learning strength gamma > 0, analyzed by DMFT
model_class: two-layer linear network over power-law features, task difficulty indexed by source exponent beta (hard means beta < 1, target outside the initial NTK RKHS)
algorithm_class: projected gradient descent / SGD on the two-layer linear model, mean-squared loss; feature-learning strength gamma is part of the recipe
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: time
cls_tightness: measured
cls_baseline: stated
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "the compute required to reach a set performance threshold has halved approximately every 8 months, with a 95% confidence interval of around 5 to 14 months"
cls_evidence_src: abstract
cls_reason: "No attack scenario: a measurement of training-recipe efficiency over calendar time, not a security claim. party=learner: the bound characterizes the population of published pre-training recipes, no adversary. unit=time/tightness=measured: an empirically fitted doubling time with a wide confidence interval and no theorem (claim_quantifier=empirical), unlike the proven exponent pages. baseline=stated: the abstract itself states the rate is substantially faster than hardware gains per Moore's Law, an explicit named comparison, verified at PDF line 24. second_notion=none: the compute-vs-algorithmic-progress decomposition splits one resource (effective compute) into two channels, not two incomparable resource types."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper that makes the scaling exponent explicitly algorithm-dependent. It extends the solvable scaling-law models beyond the kernel (lazy) limit: a two-layer linear model whose first layer can move, trained with feature-learning strength gamma, analyzed by DMFT. Tasks are indexed by the source exponent beta relative to the initial infinite-width NTK. For easy tasks (beta > 1, target inside the RKHS) and super-easy tasks (beta > 2 - 1/alpha), the scaling exponents are unchanged from the lazy model. For hard tasks (beta < 1, target outside the RKHS), feature learning lifts the time exponent from t^{-beta} to t^{-2beta/(1+beta)}, close to doubling it for small beta, and correspondingly improves the compute-optimal exponent from alpha beta/(alpha beta + 1)-type rates to alpha beta chi/(alpha beta + chi) with chi = 2beta/(1+beta) (Table 1 of the paper).

The load-bearing point for this corpus, stated exactly: the compute-scaling exponent of the same task on the same data changes with the training algorithm. The lazy limit gamma to 0 of this model reproduces the Paquette et al. phase diagram for alpha > 1, and turning gamma up changes the hard-task exponents while leaving easy-task exponents fixed. A scaling law is therefore a property of the (model, data, algorithm) triple, and any cost or threshold defined through a scaling exponent is relative to the algorithm class that produced it. The claim that the exponent improves is proven within the DMFT model and verified empirically on nonlinear MLPs learning power-law Fourier spectra on the circle and on CNNs on vision tasks.

## Claim Boundary

- Quantified over: the two-layer linear DMFT model, tasks with power-law (alpha, beta) structure, and its projected-gradient training with parameter gamma. Empirical extension to nonlinear networks is verified case by case, with a documented disagreement on CIFAR-5M after long training.
- Antecedent: source-capacity structure of the task relative to the initial kernel, mean-squared loss, SGD-type updates, and learned features restricted to linear combinations of the initial features. All by construction in the model. The last is flagged by the authors as possibly violated at finite width.
- Does not establish: an optimality claim for feature learning over all algorithms, any result for cross-entropy or adaptive optimizers (named as open by the authors), or improvement for easy tasks (proven unchanged there). It also does not claim the improvement is unbounded: the improved time exponent 2beta/(1+beta) is capped below 2beta and below 2.
- Abstract against theorem: "nearly doubling the exponent for hard tasks" is accurate as beta gets small since 2beta/(1+beta) approaches 2beta, and the phrase should not be read as a factor-2 for all beta (at beta near 1 the factor is near 1).
- Status: proven within model and algorithm class at DMFT rigor, empirical on nonlinear networks. Breaks when learned features leave the span of the initial features, under adaptive optimizers (untested), and on at least one measured setting (late-time CIFAR-5M) by the authors' own report.
- No-skipping postulate: threatening to any recipe-independent version, supporting the recipe-relative one. The same T-step budget buys a different loss under a different gamma, so the cost of reaching a state is well-defined only against a named recipe, and the exponent gap here quantifies how much a recipe change can shorten the trace for hard tasks.

## Key Contributions

- A solvable model of scaling beyond the kernel limit with a tunable feature-learning strength.
- The hard/easy/super-easy trichotomy by beta relative to the initial NTK RKHS, with the improvement confined to hard tasks.
- Time-exponent lift t^{-beta} to t^{-2beta/(1+beta)} for hard tasks, and the resulting compute-optimal exponents (Table 1).
- Recovery of the lazy phase diagram of Paquette et al. in the gamma to 0 limit, making the algorithm-dependence a controlled comparison rather than a model swap.
- Preservation of model ordering between lazy and rich regimes, suggesting kernel-limit architecture search remains informative.
- Empirical confirmation on nonlinear MLPs and CNNs, revisiting the vision settings where the lazy theory undershot measured exponents.

## Key Definitions / Theorems

- Hard task: beta < 1, target outside the RKHS of the initial infinite-width NTK. Easy: 1 < beta < 2 - 1/alpha. Super-easy: beta > 2 - 1/alpha, where SGD noise sets the large-time behavior and the compute-optimal exponent is 1 - 1/(2alpha).
- Hard-task compute-optimal balance: population gradient-flow term t^{-2beta/(1+beta)} against model bottleneck N^{-alpha beta}, giving L*(C) ~ C^{-alpha beta chi/(alpha beta + chi)}, chi = 2beta/(1+beta).
- Easy-task balance: t^{-beta} against the finite-N transient N^{-1} t^{-1+1/alpha}, giving L*(C) ~ C^{-alpha beta/(alpha beta + 1)}, coinciding with the lazy exponents.

## Connections

- Directly modifies [compute-optimal-phases](compute-optimal-phases.md) (lazy limit recovered, hard-task region changed) and [dynamical-model-scaling-laws](dynamical-model-scaling-laws.md) (same group, removes the fixed-kernel restriction that paper flagged).
- Instantiates the caveat inside [explaining-neural-scaling-laws](explaining-neural-scaling-laws.md): resolution-limited exponents from a fixed kernel spectrum are not algorithm-invariant.
- Same lesson as [learning-rate-induces-generative-exponent](learning-rate-induces-generative-exponent.md) in a different setting: there the learning rate moves a sample-complexity exponent between the information and generative exponents, here the feature-learning strength moves a compute exponent.
- The algorithm-relativity documented here is the theory-side counterpart of the recipe drift measured in [algorithmic-progress-lm](algorithmic-progress-lm.md).

## Open Questions / Limitations

- Cross-entropy loss and adaptive optimizers. Open, named by the authors.
- Learned features outside the span of the initial features, and richer dynamics for the projection matrix. Open.
- The late-time CIFAR-5M disagreement. Empirical, unresolved in the paper.

## Quotes / Notable Passages

> "feature learning can improve scaling with training time and compute, nearly doubling the exponent for hard tasks"

(Abstract.)

> "Overall our results suggest that feature learning may improve scaling law exponents by changing the optimization trajectory for tasks that are hard for the initial kernel."

(Section 1.1. The algorithm-dependence sentence.)

> "we study mean square error loss with SGD updates, while most modern models are trained on cross-entropy loss with adaptive optimizers"

(Limitations.)
