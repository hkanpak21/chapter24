---
title: "Defeating Prompt Injections by Design (CaMeL)"
type: source
date_ingested: 2026-04-23
authors: [Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes, Nicholas Carlini, Daniel Fabian, Christoph Kern, Chongyang Shi, Andreas Terzis, Florian Tramèr]
venue: "arXiv:2503.18813 (Mar 2025; v2 Jun 2025); Google / DeepMind / ETH Zürich"
year: 2025
tags: [llm-security, agentic-systems, capability-based-security, provable-security, prompt-injection]
---

## Summary

This paper (DS+25, CaMeL = **Ca**pabilities **M**ediating **L**LM-agents) provides a **capability-based access-control formalism** for LLM agents in which every value carries provenance metadata and tools enforce explicit policy checks at call time. The key theoretical contribution: CaMeL **proves that, under the dual-LLM decomposition (privileged planner + quarantined extractor), untrusted data cannot influence the control flow** of the agent — yielding the first end-to-end "provable security" statement on the AgentDojo benchmark.

The architecture separates LLM roles:
1. **Privileged planner LLM**: has authority to issue tool calls; operates only on *trusted* inputs (original user instruction).
2. **Quarantined extractor LLM**: processes *untrusted* tool outputs; can generate values but not issue tool calls.
3. **Capability dataflow**: every value has provenance tags (trusted/untrusted + origin); tools enforce policy at call time (e.g., "this tool cannot be called with untrusted argument X").

CaMeL's central theorem: for any sequence of tool invocations, if the policy forbids untrusted-data influence on privileged tool calls, then indirect prompt injection **cannot** cause unauthorized actions — provably, not heuristically. Empirical results: 77% of AgentDojo tasks solved with full guarantees vs. 84% undefended — a small utility cost for provable protection.

CaMeL is **the closest extant proxy for a UC-style containment theorem in agentic LLMs**. While it doesn't yet give full Universal Composability, its dual-LLM architecture + capability dataflow is the most formally-grounded defense in the 2025-2026 landscape.

## Key Contributions

- **Capability-based access control for LLM agents**: every value has provenance metadata; tools enforce policy at call time.
- **Dual-LLM decomposition**: privileged planner (trusted inputs only) + quarantined extractor (untrusted data); proves separation prevents control-flow hijacking.
- **Provable containment theorem**: untrusted data cannot influence control flow under the capability policy; first end-to-end provable security for LLM agents.
- **AgentDojo benchmark results**: 77% of tasks solved with full provable guarantees (vs. 84% undefended) — small utility cost for provable protection.
- **Template for UC-style agent composition**: demonstrates that formal containment is achievable in production LLM architectures.

## Key Definitions / Theorems

- **Capability tag**: each value in the agent's state has metadata (source, trust level, type).
- **Policy**: a function checking whether a tool call is permitted given the provenance of its arguments.
- **Privileged planner**: issues tool calls; only receives trusted inputs (the original user instruction).
- **Quarantined extractor**: processes untrusted inputs (tool outputs, retrieved documents); can generate values but not issue tool calls.
- **Main containment theorem (informal)**: if the policy enforces that no untrusted value can be an argument to a privileged tool call, then for any attacker-controlled tool output, the control flow follows only the original user instruction's path.
- **Empirical demonstration**: AgentDojo benchmark; 77% solved with guarantees.

## Connections

- Source: [MELON: Provable IPI Defense (Zhu et al. ICML 2025)](melon-indirect-prompt-injection.md) — alternative IPI defense via masked re-execution; CaMeL provides ex-ante capability policy; MELON provides ex-post detection.
- Source: [Filter Impossibility (BGGKRR25)](filter-impossibility-ai-alignment.md) — shows black-box filters fail; CaMeL shows architectural-level containment can succeed.
- Source: [IMTM Origin (FTH+25)](imtm-prompt-injections-protocols.md) — CaMeL addresses IMTM's Indirect Prompt Injection subcategory.
- Source: [Framework for Formalizing LLM Agent Security (Siu et al.)](formalizing-llm-agent-security.md) — oracle-function framework; CaMeL implements Data Isolation and Action Alignment oracles.
- Source: [AIOracle (VDKMR26)](extending-formalism-cryptography-ai.md) — cryptographic security games; CaMeL is one concrete instantiation of "confidentiality via capabilities."
- Source: [RS-LLM-MAS (Hu et al. 2025)](rs-llm-multi-agent.md) — RS-based MAS defense; CaMeL is the capability-based alternative.
- Concept: [AIOracle Framework](../concepts/aioracle-framework.md).
- Concept: [Attack Taxonomy for LLMs](../concepts/attack-taxonomy-llms.md).
- Concept: [Input Manipulation Threat Model](../concepts/input-manipulation-threat-model.md).
- Authors: Nicholas Carlini, Florian Tramèr, Ilia Shumailov (Google DeepMind / ETH).

## Open Questions / Limitations

- **Policy specification burden**: users/developers must write policies; incorrect policies weaken the guarantee.
- **Utility cost**: 7% utility drop is small but nonzero; can capability-based defense approach zero-cost?
- **Not full UC composition**: component-level guarantee; multi-step multi-agent composition theorem open.
- **Extractor model attacks**: if the quarantined extractor is compromised (e.g., via training-time attacks), guarantees weaken.
- **Dynamic policy**: policies are specified statically; dynamic policy adaptation in response to observed behavior is an open direction.

## Quotes / Notable Passages

> "Under the dual-LLM decomposition (privileged planner + quarantined extractor), untrusted data cannot influence the control flow, yielding the first end-to-end 'provable security' statement on the AgentDojo benchmark (77% solved with full guarantees vs 84% undefended)."

> "The closest extant proxy for a UC-style containment theorem in agentic LLMs."
