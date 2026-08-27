---
title: Distillation Scaling Laws
type: source
date_ingested: 2026-08-22
authors: [Dan Busbridge, Amitis Shidani, Floris Weers, Jason Ramapuram, Etai Littwin, Russ Webb]
venue: ICML 2025 (stated in PDF, PMLR 267)
year: 2025
tags: [scaling-laws, compute-accounting, sample-complexity]
claim_quantifier: empirical
antecedent: transformer language-model distillation in the authors' controlled setup, student and teacher sizes 143M to 12.6B, fitted where student cross-entropy exceeds 2.3 and extrapolated below
model_class: dense Transformer language models, teacher-student pairs
algorithm_class: supervised pretraining and logit distillation under the authors' fixed recipe
---

## Summary

An empirical scaling law for distillation with the compute ledger kept honest. The paper fits a distillation scaling law giving student cross-entropy as a function of student size, distillation tokens, and teacher cross-entropy, finding that the teacher enters only through its cross-entropy L_T = L_T(N_T, D_T), and that the influence of L_T on the student follows a broken power law whose two branches explain the capacity gap (a stronger teacher can produce a worse student) as a gap in learning capacity rather than size alone. The study is presented as the largest controlled empirical study of distillation, and fit quality is about 1 percent relative prediction error including weak-to-strong extrapolation.

The accounting is the reason this paper is in the corpus. Table 2 defines four compute scenarios by two indicator switches: whether teacher pretraining is charged and whether teacher inference (producing logits) is charged. Distillation beats supervised pretraining only under favorable accounting: when many students amortize one teacher, or when the teacher is a sunk cost with other uses. When one student is trained and the teacher bill is paid in full, supervised learning is generally preferable. Even in the favorable cases, the advantage holds only up to a compute level that grows predictably with student size, beyond which supervised training wins.

## Claim Boundary

- Quantified over: the swept grid of teacher-student configurations under one distillation recipe and one data distribution. The law is a fit. Extrapolations beyond the fitted cross-entropy range are marked as such by the authors.
- Antecedent: the fixed recipe, the specific FLOP model F(N) ≈ 2N(1 + c1 N^{-1/3} + c2 N^{-2/3}) (the paper rejects the bare 6ND convention for small models with long contexts), and the accounting scenario chosen. Which scenario holds is a fact about the deployment context, outside the law.
- Does not establish: any statement about capability transfer beyond cross-entropy, any guarantee for other modalities or recipes, and no theorem anywhere. It also does not establish that distillation creates training-compute savings in aggregate: the savings exist only after conditioning on a teacher whose cost is charged elsewhere.
- Abstract against fit: aligned. The abstract itself carries the two-sided conclusion (distillation wins with an existing teacher or many students, supervised wins for one student with an unpaid teacher).
- Status: empirical fit. Breaks under recipe changes (their own ablations move constants), under data distribution shift, and wherever the capacity-gap branch is extrapolated past the fitted region.
- No-skipping postulate: supporting, as an accounting discipline. A student appears to skip supervised steps only when the teacher's trace was already paid for, and the four-scenario ledger makes the shifted cost explicit, so total trace cost is conserved across the teacher-student split rather than reduced.

## Key Contributions

- The distillation scaling law (their Equation 8) with teacher influence factored entirely through teacher cross-entropy.
- Resolution of the capacity gap as a learning-capacity phenomenon with a quantitative broken-power-law form.
- The four-scenario compute accounting (best case, teacher inference, teacher pretraining, teacher pretraining plus inference).
- Compute-optimal distillation recipes for the teacher-exists and teacher-needs-training cases.
- The crossover: distillation's advantage over supervised learning ends at a student-size-dependent compute threshold.

## Key Definitions / Theorems

No theorems. Load-bearing objects: Equation 8 (the fitted law), Table 2 (the accounting switches deltaT_Lgt, deltaT_Pre), and the corrected FLOP model F(N) above.

## Connections

- Extends the accounting style of [chinchilla-compute-optimal](chinchilla-compute-optimal.md) to two-model pipelines, and cites the Porian et al. parameter-counting correction recorded in that page's Limits.
- Relevant to the compute-accounting rows of the Wave 2 corpus (`JYC+21_ProofOfLearning`, `S23_CatchAChinchilla`): it is the empirical demonstration that "who paid for the trace" is a well-posed and quantitatively answerable question, still with no formal security definition underneath.
- Complements [algorithmic-progress-lm](algorithmic-progress-lm.md): amortized teachers are one channel by which effective training cost falls without any new algorithm.

## Open Questions / Limitations

- Cross-entropy is the sole currency. Downstream capability transfer under distillation is outside the law.
- One recipe family. Sequence-level, on-policy, and synthetic-data distillation variants are not covered by the fitted constants.
- The law is silent on why the teacher enters only through L_T, an empirical regularity without a mechanism.

## Quotes / Notable Passages

> "distillation is only more efficient than supervised learning if (i) the total compute or tokens used for distillation is not larger than a student size-dependent threshold, and (ii) a teacher already exists, or the teacher to be trained has applications beyond its use in a single distillation"

(Conclusion. The who-paid clause.)

> "Conversely, if only one student is to be distilled and a teacher also requires training, supervised learning is generally preferable."

(Abstract.)
