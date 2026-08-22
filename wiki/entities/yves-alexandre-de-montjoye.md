---
title: Yves-Alexandre de Montjoye
type: entity
entity_type: author
tags: [privacy, adversarial-ml, evaluation, llm-security]
---

## About

Faculty at Imperial College London, working on privacy measurement — re-identification, anonymization
attacks, and membership inference. His group occupies both sides of the LLM membership-inference debate:
it built several of the post-hoc benchmarks and the document-level attacks that later work criticizes,
and then produced one of the two independent papers showing that post-hoc benchmarks are broken.

## Contributions / Works

- **[SoK: Membership Inference Attacks on LLMs are Rushing Nowhere (and How to Fix It) (MSJ+25)](../sources/sok-mia-llms-rushing-nowhere.md)**
  — systematization of the LLM MIA literature; a bag-of-words model-less baseline showing distribution
  shift in all six accessible post-hoc benchmarks; four proposed routes back to randomization; nine
  attacks re-run on a clean split, all near chance.

The group's earlier work (Meeus et al., 2023–2024) supplies several of the datasets and attacks that
the LLM membership-inference critiques examine: the ArXiv and Project Gutenberg benchmarks, the document-level meta-classifier
attack, the "debiased non-members" one month either side of the cutoff, and "copyright traps". Those are
cited from the PDFs read here and are not separately ingested in this wiki.

## Connections

- Matthieu Meeus, Igor Shilov, Shubham Jain, Manuel Faysse, Marek Rei — MSJ+25 co-authors.
- [Florian Tramèr](florian-tramer.md) — the ETH group produced
  [DZT24](../sources/blind-baselines-beat-mia.md) concurrently and independently, reaching the same
  conclusion with the same instrument; §VII of MSJ+25 compares the two. They diverge on the remedy:
  MSJ+25 pursues debiased and controlled post-hoc evaluation, while
  [ZDKT25](../sources/mia-cannot-prove-training.md) §III-B argues that route yields low power and narrow
  applicability.
- [David Evans](david-evans.md) — co-author of [DSM+24](../sources/do-mias-work-on-llms.md), the paper
  that first flagged the temporal shift MSJ+25 quantifies.
