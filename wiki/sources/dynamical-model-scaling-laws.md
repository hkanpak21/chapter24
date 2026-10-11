---
title: A Dynamical Model of Neural Scaling Laws
type: source
date_ingested: 2026-08-22
authors: [Blake Bordelon, Alexander Atanasov, Cengiz Pehlevan]
venue: ICML 2024 (stated in PDF, PMLR 235)
year: 2024
tags: [scaling-laws, learning-theory, sample-complexity]
claim_quantifier: conditional
antecedent: a randomly projected linear model with power-law features, trained by gradient flow or discrete SGD, in the DMFT limit of large feature count, model size, and sample count
model_class: structured random-feature linear model, features with (w_k*)^2 lambda_k ~ k^{-a}, lambda_k ~ k^{-b}
algorithm_class: gradient flow, discrete-time SGD, and momentum on the projected linear model
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
cls_evidence: "While the data and model exponents are the same, the time and model exponents are different in general."
cls_evidence_src: §1 (contributions list, item 4)
cls_reason: "party=learner: DMFT description of gradient-based training, no adversary. unit=time/second_notion=parameters (rule 4b, the textbook case: one party bounded under two incomparable notions whose divergence is the paper's own point) because the headline finding is that the time exponent t^-(a-1)/b differs from the model/data exponent ^-min(a-1,2b), unlike Kaplan/Chinchilla where model size and data track the same fixed compute; t genuinely names training time/steps in the paper's own dynamics here, not a proxy for FLOPs, so this is not the compute-into-time forcing the assigning brief warns against. Dataset size P shares the model-size exponent exactly, so it is not recorded as a distinct third notion, noted here rather than added as a slot the vocabulary lacks. tightness=exponent for the derived (DMFT-level, not measure-theoretically proven) power laws. baseline=absent: the Claim Boundary states the paper 'does not establish...a bound for any algorithm outside its class.'"
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The dynamical mean field theory account of scaling laws. The model is a linear predictor on N random projections of M structured features trained on P samples, with power-law task and spectral structure set by two exponents: the task-power exponent a, defined by (w_k*)^2 lambda_k ~ k^{-a}, and the spectral decay exponent b, defined by lambda_k ~ k^{-b} (source and capacity conditions in the kernel literature). In the joint large-(M, N, P) limit the training and test loss dynamics close over correlation and response functions, the response functions solve exactly in the Fourier domain, and the transfer function per eigenmode is explicit. The resulting bottleneck scalings are t^{-(a-1)/b} in training time, and N^{-min(a-1, 2b)} and P^{-min(a-1, 2b)} in model and data size.

The observation the survey needs: the time exponent and the model exponent differ in general, because time resolves modes at a rate set by the spectrum b while capacity truncates them at a rate set by the task a. At fixed compute C proportional to Nt this mismatch forces an asymmetric compute-optimal allocation in which training time grows faster than model size when spectra decay fast (b > 1), consistent with the asymmetries measured by Hoffmann et al. in language and larger ones in vision MLPs. The same machinery explains the early-time 1/width convergence to infinite-width dynamics against the late-time width^{-c} rate, why ensembling loses to width at fixed compute, and how the train-test gap accumulates from data reuse.

## Claim Boundary

- Quantified over: the DMFT limit of one model family (projected linear regression on power-law features) under gradient-based training. Exponents are derived for that family and verified by simulation. Real-network statements are empirical extrapolations, tested on CIFAR-5M, Wikitext, and MNIST-scale models.
- Antecedent: power-law source and capacity structure of the features, plus the DMFT limit. Holds by construction in the model. On real data (a, b) must be measured from the empirical kernel spectrum, and the paper does so, with the fit noted as imperfect for networks outside the kernel regime.
- Does not establish: a bound for any algorithm outside its class, the behavior of feature-learning networks (its ResNet compute-optimal prediction C^{-0.05} underestimates the observed rate, a mismatch the authors flag and the sequel addresses), or any claim over all architectures.
- Abstract against theorem: aligned. The abstract states the model makes predictions and reproduces observations, which is what the body delivers.
- Status: proven within model and algorithm class at the DMFT level (physics-level derivation, self-consistent equations, not measure-theoretic proof), empirical outside it. Breaks when feature learning moves the kernel spectrum during training, which is its sequel's subject, and when (a, b) power-law structure fails.
- No-skipping postulate: supporting the recipe-relative form. Every exponent is derived for a stated algorithm on a stated model, and the time-against-model exponent asymmetry shows even inside one recipe the price of a step and the price of a parameter are different currencies, so a trace's cost has no recipe-free summary.

## Key Contributions

- Closed DMFT description of the full training dynamics (not statics) with simultaneous averaging over dataset draw and random projection.
- Exact Fourier-domain solution of the response functions and per-mode transfer functions.
- The three bottleneck scalings and the proof-level observation that data and model exponents coincide while the time exponent differs.
- Asymmetric compute-optimal allocation, t growing faster than N for b > 1, with the b to 1 limit recovering linear joint scaling.
- Ensembling strictly dominated by width at fixed compute within the model.
- Test-train gap accumulation under data reuse, and finite-width variance corrections accumulating over time.

## Key Definitions / Theorems

- Task-power exponent a and spectral decay exponent b: (w_k*)^2 lambda_k ~ k^{-a}, lambda_k ~ k^{-b}.
- Bottleneck scalings: L ~ t^{-(a-1)/b} (time), P^{-min(a-1, 2b)} (data), N^{-min(a-1, 2b)} (model), with the alternative N^{-2b}, P^{-2b} branch only for very easy tasks a > 2b + 1, which the authors note natural data rarely satisfies.
- Transfer function H_k(omega) = 1/(i omega + lambda_k R1(omega) R3(omega)) with self-consistent R1, R3.

## Connections

- Sibling of [compute-optimal-phases](compute-optimal-phases.md): same object (compute-optimal frontier in a solvable model), different technique (DMFT against Volterra plus deterministic equivalents), and this model also prices dataset size and data reuse where PLRF is one-pass infinite-data.
- Predecessor of [feature-learning-improves-scaling](feature-learning-improves-scaling.md), which removes the fixed-kernel restriction that this paper's own experiments identify as its failure mode.
- Mechanism-level refinement of [explaining-neural-scaling-laws](explaining-neural-scaling-laws.md): the resolution-limited exponent splits into distinct time, data, and model exponents once dynamics are tracked.
- The empirical asymmetries it explains are the ones recorded in [chinchilla-compute-optimal](chinchilla-compute-optimal.md).

## Open Questions / Limitations

- Feature learning: the model treats the kernel as fixed, and the authors document real networks beating its predicted compute exponent. Addressed in the sequel, open at this paper's level.
- DMFT derivations are at physics rigor. A measure-theoretic treatment of the joint limit is not given.
- Estimating (a, b) from finite empirical spectra is itself a fitting problem carrying uncertainty into every downstream exponent.

## Quotes / Notable Passages

> "While the data and model exponents are the same, the time and model exponents are different in general. We show that this gives rise to an asymmetric compute optimal scaling strategy where training time increases faster than model size."

(Summary of contributions, item 4.)

> "We will refer to a as the task-power exponent and b as the spectral decay exponent"

(Section 4, the definition sentence for the two units.)
