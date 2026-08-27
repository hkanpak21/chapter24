---
title: Beyond neural scaling laws, beating power law scaling via data pruning
type: source
date_ingested: 2026-08-22
authors: [Ben Sorscher, Robert Geirhos, Shashank Shekhar, Surya Ganguli, Ari S. Morcos]
venue: NeurIPS 2022 (stated in PDF)
year: 2022
tags: [scaling-laws, sample-complexity, learning-theory]
claim_quantifier: conditional
antecedent: theory holds for perceptron learning in the teacher-student setting with Gaussian inputs, margin-based pruning, and a probe student at angle theta to the teacher, in the high-dimensional replica limit; the exponential regime needs theta = 0, an error-free pruning metric
model_class: perceptron teacher-student (theory); ResNets on CIFAR-10, SVHN, ImageNet (empirics)
algorithm_class: margin-based data pruning followed by standard training; the pruning metric is part of the algorithm
---

## Summary

The paper that shows the data-size exponent is a property of the sampling recipe. Power-law scaling of error with dataset size reflects redundancy in i.i.d. data. If examples are ranked by a pruning metric and the dataset is pruned to the informative fraction, error can fall off exponentially in the pruned dataset size rather than as a power law. The theory is a statistical-mechanics calculation: replica analysis of perceptron learning in a teacher-student setting where a probe student's margins rank the examples. With a perfect metric (probe at angle theta = 0 to the teacher), the Pareto-optimal pruning schedule yields error decaying exponentially (their analysis gives faster-than-exponential for the optimal schedule) in the pruned examples-per-parameter ratio. With an imperfect metric (theta > 0), the same envelope starts exponential and crosses over to a power law, and below a floor f_min(theta) further pruning stops helping.

The empirics are ImageNet-scale with imperfect metrics: better-than-power-law scaling is observed for ResNets on CIFAR-10, SVHN, and ImageNet, a benchmark of ten pruning metrics finds most scale poorly to ImageNet with the best requiring labels and heavy compute, and a self-supervised prototype-distance metric prunes 20 percent of ImageNet without performance loss. A second theory prediction with empirical support: keep hard examples when data is abundant, easy examples when data is scarce.

## Claim Boundary

- Quantified over: the theory over the perceptron teacher-student model in the replica limit, per pruning angle theta. The empirics over three vision datasets and specific metrics. Nothing is quantified over learning problems or metrics in general.
- Antecedent: an accurate ranking of example informativeness. The exponential regime assumes theta = 0, which no real metric attains, and the paper's own theta > 0 analysis proves the crossover back to a power law plus the f_min floor. So the strong claim's antecedent is known not to hold exactly in practice, and the honest reading is the crossover family, exponent and crossover point set by metric quality.
- Does not establish: exponential scaling on any real benchmark (observed is better-than-power-law with imperfect metrics), any language-model result (vision only), or a free lunch: the probe, metric evaluation, and class-balancing are compute and design costs charged outside the headline scaling variable.
- Abstract against theorem: the abstract's "potentially even reduce it to exponential scaling" is hedged and matches. Folk citation as "pruning gives exponential scaling" drops the metric-quality antecedent, which the paper itself makes the central limitation.
- Status: theory proven within the perceptron replica model (statistical-mechanics rigor). Empirics on ResNet-scale vision. The recipe-dependence of the exponent is the paper's own message: the achieved exponent is set by the pruning metric, so it is a property of the data-selection recipe rather than of the task. Breaks when the metric misranks (proven crossover), when class balance is lost (their App. H), and plausibly at distribution shift, which they only begin to test.
- No-skipping postulate: threatening to any version that indexes cost by raw dataset or step count at fixed recipe family, since a better selection recipe reaches the same loss with far fewer examples. The recipe-relative version survives because the metric is part of the recipe and its construction cost (probe training, embedding, ranking) is paid inside the trace.

## Key Contributions

- Replica-theory calculation of test error under margin-based pruning as a function of total data, kept fraction, and probe angle.
- The exponential (and faster) Pareto envelope at theta = 0, and the proven exponential-to-power-law crossover with floor f_min(theta) at theta > 0.
- The abundant-data/keep-hard against scarce-data/keep-easy switch, predicted in theory and reproduced on CIFAR-10 with EL2N.
- First large-scale benchmark of ten pruning metrics on ImageNet.
- A cheap self-supervised pruning metric (k-means prototype distance in an embedding space) matching the best supervised metrics at 20 percent pruning.
- The foundation-datasets outlook: pruning cost amortized across many downstream trainings.

## Key Definitions / Theorems

- Setup: teacher perceptron T on N-dimensional Gaussian inputs, probe student J_probe at angle theta, margin m = J_probe · (y x), keep the hardest fraction f of P_total = alpha_tot N examples, train on the kept alpha_prune = f alpha_tot per-parameter examples.
- theta = 0: Pareto-optimal error over (alpha_tot, f) at fixed alpha_prune decays at least exponentially in alpha_prune.
- theta > 0: envelope initially exponential in alpha_prune, then power law, with asymptotic floor f_min(theta) (24 percent at theta = 10 degrees, 46 percent at 20 degrees in their example).

## Connections

- Direct attack on the data-axis exponent of [scaling-laws-neural-lm](scaling-laws-neural-lm.md) and the token-allocation half of [chinchilla-compute-optimal](chinchilla-compute-optimal.md).
- The mechanism agrees with [explaining-neural-scaling-laws](explaining-neural-scaling-laws.md): power laws come from redundant i.i.d. coverage of the manifold, and pruning changes the measure being covered.
- Recipe-dependence of an exponent parallels [feature-learning-improves-scaling](feature-learning-improves-scaling.md) (algorithm axis) and [learning-rate-induces-generative-exponent](learning-rate-induces-generative-exponent.md) (hyperparameter axis). Here the axis is data selection.
- One of the named channels of measured algorithmic progress in [algorithmic-progress-lm](algorithmic-progress-lm.md).

## Open Questions / Limitations

- Scalable high-quality unsupervised metrics. Open, named by the authors as the bottleneck.
- Whether pruned-data gains persist under the same iteration budget rather than the same epoch count: their App. J finds the gain saturates but the accounting is subtle, flagged by the authors.
- Language modeling and other modalities. Untested in the paper.

## Quotes / Notable Passages

> "we can break beyond power law scaling and potentially even reduce it to exponential scaling instead if we have access to a high-quality data pruning metric"

(Abstract. The antecedent is in the sentence.)

> "The most notable limitation is that achieving exponential scaling requires a high quality data pruning metric."

(Discussion, Limitations.)

> "We find most existing high performing metrics scale poorly to ImageNet, while the best are computationally intensive and require labels for every image."

(Abstract.)
