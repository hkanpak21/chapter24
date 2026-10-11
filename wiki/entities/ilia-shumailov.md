---
title: Ilia Shumailov
type: entity
entity_type: author
tags: [adversarial-ml, llm-security, verifiable-computation]
---

## About

Machine learning security researcher; affiliated with the University of Oxford at the time of the
extraction work and previously a postdoctoral fellow at the Vector Institute. Recurs in this wiki on
model extraction, machine unlearning, and agentic LLM security.

## Contributions / Works

- **[Beyond Labeling Oracles: What does it mean to steal ML models?](../sources/beyond-labeling-oracles.md)**
  (Shafran, Shumailov, Erdogdu, Papernot) — the statement that no ME literature formally defines
  extraction success, and the informal cost-inequality repair.
- **[On the Necessity of Auditable Algorithmic Definitions for Machine Unlearning](../sources/auditable-unlearning-definitions.md)**
  (Thudi, Jia, Shumailov, Papernot; USENIX Security 2022).
- **[Defeating Prompt Injections by Design (CaMeL)](../sources/camel-defeating-prompt-injections.md)**
  (Debenedetti, Shumailov, et al.).

## Connections

- [Nicolas Papernot](nicolas-papernot.md) — co-author on both the extraction and unlearning papers.
- The unlearning paper credits an earlier Shumailov et al. observation — that different training
  samples can produce a similar gradient descent step — as the seed of forgeability. That observation
  is also the mechanism reused by
  [Verification of Machine Unlearning is Fragile](../sources/unlearning-verification-fragile.md).
