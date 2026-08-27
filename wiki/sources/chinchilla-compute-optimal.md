---
title: Training Compute-Optimal Large Language Models (Chinchilla)
type: source
date_ingested: 2026-08-22
authors: [Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, Laurent Sifre]
venue: venue unconfirmed from PDF (arXiv:2203.15556v1; NeurIPS 2022 per the bibliography of arXiv:2405.15074)
year: 2022
tags: [scaling-laws, sample-complexity, compute-accounting]
claim_quantifier: empirical
antecedent: dense Transformer language models trained on MassiveText-style data with the authors' training recipe, 70M to 16B parameters, 5B to 500B tokens
model_class: dense Transformer language models
algorithm_class: AdamW-style autoregressive training with tuned cosine learning-rate decay, one recipe family
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
cls_evidence: "for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled"
cls_evidence_src: abstract
cls_reason: "party=learner, same convention as scaling-laws-neural-lm; unit=parameters/second_notion=samples (rule 4b) for the symmetric N_opt∝C^0.5, D_opt∝C^0.5 split; the fixed FLOP budget itself has no vocabulary unit, the same gap as the Kaplan page. tightness=exponent for the stated N_opt/D_opt power-law. baseline=stated, unlike the Kaplan page, because the paper reports an actual comparison: Chinchilla beats Gopher/GPT-3/Jurassic-1/Megatron-Turing NLG at matched compute, and the allocation explicitly supersedes Kaplan et al.'s 5.5x-model/1.8x-data split."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The compute-optimal correction to Kaplan et al. From over 400 training runs the paper estimates, by three methods, how a fixed FLOP budget should split between model size N and training tokens D. All three methods agree that N and D should scale in equal proportion, N_opt ∝ C^a and D_opt ∝ C^b with a ≈ b ≈ 0.5, against Kaplan et al.'s 5.5x model against 1.8x data per 10x compute. Approach 3 fits the parametric form L(N, D) = E + A/N^α + B/D^β by Huber-loss minimization, reporting E = 1.69, A = 406.4, B = 410.7, α = 0.34, β = 0.28. The prediction is tested by training Chinchilla, a 70B model on 4x the data of Gopher at Gopher's budget, which outperforms Gopher, GPT-3, Jurassic-1, and Megatron-Turing NLG downstream.

The law is an empirical fit, and its fitted constants are the subject of a documented replication dispute recorded under Limits below. The equal-proportions conclusion survives that dispute. The specific Approach 3 constants do not survive it unamended.

## Claim Boundary

- Quantified over: nothing. Three estimators over one architecture family, one data distribution, one tuned recipe. No quantifier over algorithms or tasks.
- Antecedent: the recipe above, including per-budget tuned learning-rate decay. Holds where measured. The paper's own hypothesis that Kaplan et al.'s discrepancy came from untailored learning-rate decay was later disproved by Porian et al., so the stated explanation of the antecedent's role was wrong even though the law stands.
- Does not establish: optimality over anything outside the recipe family. No lower bound. A better data-selection or optimization scheme is uncontradicted, and Sorscher et al. exhibit one along the data axis in vision.
- Abstract against theorem: the abstract's "compute-optimal" reads as a property of the task. It is a property of the recipe family swept. Also the parameter/data exponents of Approach 3 in the body are rounded values whose unrounded versions matter, which is one of the two defects Besiroglu et al. identified.
- Status: empirical fit. Would break under changed data quality (Besiroglu et al. cite evidence the token-per-parameter optimum shifts with data quality), changed architecture, or changed optimizer.
- No-skipping postulate: neutral, with one useful edge. The frontier prices the best loss reachable at budget C inside one recipe family, which is the recipe-relative object the postulate needs, and the replication dispute shows the frontier's constants are estimator-fragile, so any postulate resting on their exact values inherits that fragility.

## Limits

The fitted constants of Approach 3 were contested and reconciled by two later papers, both on disk.

- Besiroglu, Erdil, Barnett, You, *Chinchilla Scaling: A replication attempt*, arXiv:2404.10102 (`raw/Bes24_ChinchillaReplication.pdf`). Reconstructing the data from the paper's figures, they find the reported Approach 3 estimates inconsistent with Approaches 1 and 2, a poor fit to the reconstructed data, and confidence intervals that would require on the order of 600,000 runs where fewer than 500 exist. Verbatim: "the confidence intervals reported by Hoffmann et al. are implausibly tight and unlikely to be obtained from proper statistical procedures given the size of their dataset." Their own refit restores consistency with Approaches 1 and 2. They identify two causes: the Huber-loss optimizer stopped before convergence, and body-text rounding of the reported estimates.
- Porian, Wortsman, Jitsev, Schmidt, Carmon, *Resolving Discrepancies in Compute-Optimal Scaling of Language Models*, arXiv:2406.19146, NeurIPS 2024 (`raw/PSM+24_ReconcilingScaling.pdf`). Reproduces the Kaplan law and dissolves the Kaplan-Hoffmann disagreement into three factors: "last layer computational cost, warmup duration, and scale-dependent optimizer tuning." With the factors corrected, "we obtain excellent agreement with the Hoffmann et al." law, and against Hoffmann et al.'s own hypothesis, "careful learning rate decay is not essential for the validity of their scaling law."

Net position: the a ≈ b ≈ 0.5 allocation is replicated and explained. The published Approach 3 constants (E, A, B, α, β) as printed are unreliable, and any use of them downstream should cite the corrected fits.

## Key Contributions

- Three independent estimators of the compute-optimal (N, D) allocation, agreeing on equal proportional scaling.
- The parametric loss surface L(N, D) = E + A/N^α + B/D^β with fitted constants.
- Chinchilla itself, the 70B confirmation run, outperforming models up to 530B at matched budget.
- The diagnosis that contemporary large models were substantially undertrained.

## Key Definitions / Theorems

No theorems. The load-bearing objects are the three estimators (minima over loss envelopes, IsoFLOP profiles, parametric fit) and the fitted frontier N_opt ∝ C^0.5, D_opt ∝ C^0.5.

## Connections

- Corrects [scaling-laws-neural-lm](scaling-laws-neural-lm.md).
- [compute-optimal-phases](compute-optimal-phases.md) derives an equal-proportions regime (d* ≍ f^{1/2}) as a theorem inside the PLRF model, and cites this paper as the empirical anchor.
- [dynamical-model-scaling-laws](dynamical-model-scaling-laws.md) predicts a mechanism for asymmetric allocation when spectra decay fast.
- [distillation-scaling-laws](distillation-scaling-laws.md) extends the same accounting style to two-model training.

## Open Questions / Limitations

- The negative curvature the authors observe at high budget in Approach 1 suggests the frontier itself may bend beyond the measured range.
- Data quality shifts the optimum token-per-parameter ratio, so the constant 20 tokens-per-parameter folk rule is recipe- and corpus-relative.
- Whether any of the three estimators is consistent for the population frontier, rather than for the swept grid, is unexamined in the paper.

## Quotes / Notable Passages

> "We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant"

(Abstract.)

> "for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled"

(Abstract. The claim that replicated. The Approach 3 constants around it did not, see Limits.)
