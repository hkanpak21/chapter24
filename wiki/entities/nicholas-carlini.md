---
title: Nicholas Carlini
type: entity
entity_type: author
tags: [adversarial-ml, privacy, empirical, evaluation]
---

## About

Research scientist working on the empirical security and privacy of machine learning. His recurring
contribution is methodological: taking a measurement the field trusts, showing it does not measure what
it is quoted for, and supplying the stronger attack that replaces it. The pattern runs through
adversarial-example evaluation, model extraction, training-data extraction, and membership inference.

## Contributions / Works

- **[Membership Inference Attacks From First Principles (CCNSTT22)](../sources/mia-from-first-principles.md)**
  — argues balanced accuracy and AUC cannot detect whether an attack confidently identifies anyone, and
  introduces LiRA, the per-example Gaussian likelihood-ratio attack. Established the
  [low-FPR evaluation regime](../concepts/low-fpr-evaluation-regime.md) as the field standard.
- **[High Accuracy and High Fidelity Extraction of Neural Networks (JCB+20)](../sources/jagielski-model-extraction.md)**
  — model extraction with accuracy and fidelity separated as distinct objectives.
- **[Defeating Prompt Injections by Design (CaMeL)](../sources/camel-defeating-prompt-injections.md)**
  — co-author.

Cited throughout the membership-inference literature as the origin of the low-FPR convention, of the shadow-model likelihood
ratio, and of the canary technique for privacy auditing (the Secret Sharer, cited in
[ZDKT25](../sources/mia-cannot-prove-training.md) as the source of the rank-based test statistic).
[DSM+24](../sources/do-mias-work-on-llms.md) thanks him for comments on early drafts.

## Connections

- [Florian Tramèr](florian-tramer.md) — co-author on CCNSTT22 and CaMeL; the ETH Zürich group carries
  the critique forward in DZT24, AZT24 and ZDKT25.
- Steve Chien, Milad Nasr, Shuang Song, Andreas Terzis — CCNSTT22 co-authors.
- [Matthew Jagielski](../sources/jagielski-model-extraction.md) — model extraction; also credited in
  [AZT24](../sources/privacy-defense-evaluations-misleading.md) for supplying the 20,000 trained models
  behind its sample-level measurement.
