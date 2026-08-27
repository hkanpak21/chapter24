---
title: Algorithmic Progress in Language Models
type: source
date_ingested: 2026-08-22
authors: [Anson Ho, Tamay Besiroglu, Ege Erdil, David Owen, Robi Rahman, Zifan Carl Guo, David Atkinson, Neil Thompson, Jaime Sevilla]
venue: venue unconfirmed from PDF (arXiv:2403.05812v1)
year: 2024
tags: [scaling-laws, compute-accounting]
claim_quantifier: empirical
antecedent: a curated dataset of over 200 language-model evaluations on Wikitext and Penn Treebank, 2012 to 2023, analyzed through augmented scaling-law regressions
model_class: published language models across architectures, 2012-2023
algorithm_class: the population of published pre-training recipes over time; post-training enhancements excluded
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
cls_evidence: "We introduce two families of estimators—based on tensor unfolding and online SGD—that respectively achieve either optimal sample complexity or optimal runtime, and argue that estimators achieving both may not exist in general."
cls_evidence_src: abstract
cls_reason: "No attack scenario, matching sibling single-index pages (generative-exponent-single-index, generative-leap-multi-index). party=learner per rule 3. unit=samples/tightness=exponent for Theorem 1's decoupled M*/Q* thresholds, matching the sibling pages' convention of recording the sample-complexity headline. second_notion=time per rule 4b: the abstract's own headline is that sample-optimal and runtime-optimal estimators can diverge (l_m,* != l_T,* beyond Gaussian inputs), the clearest instance in this batch of 'two incomparable notions, same party', so time is recorded here rather than algo class (already used by the sibling pages for the SQ/low-degree restriction). baseline=stated: Remark 3.1 and Appendix H state the information-theoretic recovery bound m=Omega(d), against which the detection-only scope of Theorem 1 is qualified (verified at PDF lines 650-655, 8171-8176). frame=compute: the SQ query bound and the low-degree conditional sample bound both restrict to computationally-efficient algorithm classes."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The measurement of how fast the recipe frontier moves. Fitting augmented scaling laws (scaling laws with a time-indexed efficiency term) to over 200 language-model results on Wikitext and Penn Treebank from 2012 to 2023, the paper estimates that the compute needed to reach a fixed performance threshold halved about every 8 months, 95 percent confidence interval roughly 5 to 14 months, faster than Moore's-law hardware gains. Decomposing progress, the increase in raw compute contributed more to overall performance gains than algorithmic improvement did over the period, despite the fast algorithmic doubling time. An attempt to isolate the transformer's contribution by refitting on non-transformers only is reported as too noisy to be significant (central estimate 8.8 months, interval spanning zero).

Every number carries the paper's own estimation-uncertainty caveats: the benchmark data are noisy and heterogeneous, the model cannot resolve short time scales or individual innovations, and cross-model specification uncertainty is large. The paper states these limits itself, and the abstract carries the "limited by noisy benchmark data" flag.

## Claim Boundary

- Quantified over: the curated sample of published evaluations on two perplexity benchmarks, under the paper's model specifications. There is no quantifier over tasks, and downstream-capability progress and post-training enhancements (prompting, fine-tuning, search) are excluded by construction.
- Antecedent: that published (model, compute, perplexity) triples identify a moving efficiency frontier, and that the augmented scaling-law family is well-specified. Publication bias and data heterogeneity are acknowledged threats to it.
- Does not establish: gains from any specific innovation (stated as beyond the method), constancy of the rate outside 2012-2023, transfer of the rate to downstream capabilities, or any mechanism. It is a rate estimate over a population of recipes.
- Abstract against body: aligned, including the uncertainty flags. The headline "halved every 8 months" should be quoted with its 5-to-14-month interval, which the abstract itself provides.
- Status: empirical fit with wide, honestly reported uncertainty. Would break under benchmark contamination or selection effects in what gets published, both discussed by the authors.
- No-skipping postulate: threatening to any recipe-independent version and calibrating for the recipe-relative one. The compute price of a fixed capability is halved by recipe change every 8-ish months, so a T-step trace's cost is meaningful only with the recipe and its date attached, and this paper supplies the measured drift rate of that index.

## Key Contributions

- The 8-month compute-halving estimate for pre-training language modeling, with confidence intervals.
- The decomposition finding compute scaling contributed more than algorithmic progress over 2012-2023.
- An augmented scaling-law methodology transplanted from computer-vision progress estimation (Erdil and Besiroglu 2022) to language models, with model-comparison over specifications.
- A public dataset and code for the estimates.

## Key Definitions / Theorems

No theorems. The load-bearing object is the augmented scaling law: a fitted loss surface in effective model size and effective data whose efficiency terms grow exponentially in calendar time, with doubling times extracted from the fitted growth rates.

## Connections

- Prices the drift of everything fitted in [scaling-laws-neural-lm](scaling-laws-neural-lm.md) and [chinchilla-compute-optimal](chinchilla-compute-optimal.md): fitted constants are dated.
- [feature-learning-improves-scaling](feature-learning-improves-scaling.md) and [learning-rate-induces-generative-exponent](learning-rate-induces-generative-exponent.md) are theory-side instances of the exponent moving with the recipe. This paper measures the aggregate of such moves in the wild.
- [data-pruning-beats-power-laws](data-pruning-beats-power-laws.md) is one named channel of the measured progress.
- For the survey's compute-accounting strand, it shares Epoch authorship and method with the Chinchilla replication recorded in the Limits of [chinchilla-compute-optimal](chinchilla-compute-optimal.md).

## Open Questions / Limitations

- Fine-grained attribution of gains to specific innovations. Stated by the authors as better suited to experimental work.
- The estimates are for perplexity benchmarks only. Downstream-capability doubling times may differ.
- Autocorrelation between compute scaling and innovation adoption may understate the reported uncertainty, noted in the paper.

## Quotes / Notable Passages

> "the compute required to reach a set performance threshold has halved approximately every 8 months, with a 95% confidence interval of around 5 to 14 months"

(Abstract.)

> "the increase in compute made an even larger contribution to overall performance improvements over this time period"

(Abstract.)

> "several limitations reduce the precision of and temper our confidence in our estimates"

(Section 4.2, Limitations.)
