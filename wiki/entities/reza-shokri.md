---
title: Reza Shokri
type: entity
entity_type: author
tags: [privacy, adversarial-ml, evaluation]
---

## About

Faculty working on the quantification of privacy risk in machine learning. Originator of the membership
inference attack against ML models, and of the shadow-model technique that every attack in this wiki's
membership-inference batch either uses or explains its inability to afford.

**Recorded from citations, not from an ingested source.** None of his papers has been read into this
wiki. The attributions below come from bibliographies in PDFs that were read, and nothing beyond them
should be inferred.

## Contributions / Works

- *Membership Inference Attacks Against Machine Learning Models*, with Marco Stronati, Congzheng Song
  and Vitaly Shmatikov, IEEE Symposium on Security and Privacy 2017, pp. 3–18. **Not ingested.** Cited
  as the origin of the MI attack and of shadow modelling by every paper in the batch — see
  [RL21](../sources/difficulty-of-mia.md) ref. [20],
  [CCNSTT22](../sources/mia-from-first-principles.md) ref. [60],
  [DZT24](../sources/blind-baselines-beat-mia.md),
  [DSM+24](../sources/do-mias-work-on-llms.md),
  [AZT24](../sources/privacy-defense-evaluations-misleading.md) ref. [51].
- Also cited: *Comprehensive Privacy Analysis of Deep Learning* (Nasr, Shokri,
  Houmansadr, IEEE S&P 2019), the source of the CIFAR-100 attack that
  [RL21](../sources/difficulty-of-mia.md) reproduces and finds to have a 64.5% false alarm rate; the ML
  Privacy Meter tool, cited in CCNSTT22 as the basis of most production privacy analysis; and
  *Privacy Risks of Securing Machine Learning Models Against Adversarial Examples* (Song, Shokri,
  Mittal, CCS 2019).

## Connections

- [Prateek Mittal](prateek-mittal.md) — co-author on the adversarial-robustness-versus-privacy work
  cited in RL21.
- [Nicholas Carlini](nicholas-carlini.md), [Florian Tramèr](florian-tramer.md) — the low-FPR critique in
  [CCNSTT22](../sources/mia-from-first-principles.md) is aimed at the average-case metrics used in the
  2017 paper and its successors, while adopting its shadow-model construction.
