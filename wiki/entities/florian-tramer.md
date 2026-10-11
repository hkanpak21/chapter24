---
title: Florian Tramèr
type: entity
entity_type: author
tags: [adversarial-ml, privacy, evaluation, llm-security]
---

## About

Faculty at ETH Zürich, leading the group (SPY Lab) that produced most of the membership-inference
critique recorded in this wiki. The group's characteristic move is to attack the *measurement* rather
than the mechanism: find the baseline nobody reported, run it, and show the published number was
measuring something else. Across four papers here the target escalates from datasets, to defences, to
the definition of the null hypothesis itself.

## Contributions / Works

- **[Membership Inference Attacks From First Principles (CCNSTT22)](../sources/mia-from-first-principles.md)**
  — co-author; the low-FPR regime and LiRA.
- **[Evaluations of Machine Learning Privacy Defenses are Misleading (AZT24)](../sources/privacy-defense-evaluations-misleading.md)**
  — three pitfalls in defence evaluation; the sample-level metric; a DP-SGD baseline with a vacuous `ε`
  that beats every heuristic defence studied.
- **[Blind Baselines Beat Membership Inference Attacks for Foundation Models (DZT24)](../sources/blind-baselines-beat-mia.md)**
  — model-free attacks beat published MIAs on eight benchmarks.
- **[Position: Membership Inference Attacks Cannot Prove that a Model Was Trained On Your Data (ZDKT25)](../sources/mia-cannot-prove-training.md)**
  — the definitional endpoint: the null hypothesis cannot be sampled for a production model, so the
  false positive rate cannot be bounded.
- **[Defeating Prompt Injections by Design (CaMeL)](../sources/camel-defeating-prompt-injections.md)**
  — co-author.

## Connections

- [Nicholas Carlini](nicholas-carlini.md) — co-author on CCNSTT22 and CaMeL.
- Jie Zhang — co-author on AZT24, DZT24 and ZDKT25; the connective author across the ETH trio.
- Debeshee Das (DZT24, ZDKT25), Michael Aerni (AZT24), Gautam Kamath (ZDKT25, Waterloo).
- [Yves-Alexandre de Montjoye](yves-alexandre-de-montjoye.md) — the other pole of this debate: his group
  built the post-hoc benchmarks and the "debiased non-member" response that DZT24 and ZDKT25 argue
  against, and independently produced the same model-free baseline in
  [MSJ+25](../sources/sok-mia-llms-rushing-nowhere.md).
