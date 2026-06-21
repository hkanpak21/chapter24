---
title: "MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents"
type: source
date_ingested: 2026-04-23
authors: [Kaijie Zhu, Xianjun Yang, Jindong Wang, Wenbo Guo, William Yang Wang]
venue: "arXiv:2502.05174 (Feb 2025); ICML 2025"
year: 2025
tags: [llm-security, agentic-systems, indirect-prompt-injection, provable-defense, masked-re-execution]
---

## Summary

This paper (ZYWGW25, MELON = **M**asked re-**E**xecution and Too**L** compariso**N**) formalizes indirect prompt injection (IPI) as a **mismatch between observed and intended tool-use trajectories** and proves that a masking-based consistency check detects injections whenever the attack strictly changes tool selection.

The core mechanism:
1. Run the agent normally on the user prompt, observing tool calls and arguments.
2. Re-execute the agent with a **masked user prompt** (the user instruction replaced by a neutral prompt).
3. If the two executions agree on tool calls, pass through; if they disagree, flag as IPI attack.

**Key insight**: under a successful IPI attack, the agent's next action becomes less dependent on the (masked) user task and more dependent on the (unmasked) malicious task embedded in tool outputs. This asymmetry makes masked re-execution a provable detector.

MELON is **complementary** to [CaMeL](camel-defeating-prompt-injections.md): where CaMeL enforces *ex ante* capability policy, MELON provides *ex post* provable detection. Both are important advances toward the full UC-style composable security theorem for agents.

## Key Contributions

- **Formal IPI detection framework via masked re-execution**: trajectory-based detection with provable guarantees.
- **Provable detection theorem**: MELON detects all IPI attacks that strictly change tool selection.
- **MELON-Aug variant**: augmented with additional consistency checks for more robust detection.
- **State-of-the-art empirical**: extremely low Attack Success Rate (ASR) while maintaining high Utility under Attack (UA) across standard IPI benchmarks.
- **Complementary to CaMeL**: ex-post detection (MELON) + ex-ante capability enforcement (CaMeL) covers both detection and prevention.

## Key Definitions / Theorems

- **IPI attack formalization**: user provides prompt p; agent retrieves data d from tool T; if d contains adversarial instructions that change agent's subsequent tool calls compared to benign d', it's an IPI attack.
- **Masked re-execution**: execute agent with user prompt replaced by a neutral mask; observe tool calls M.
- **Detection rule**: flag as IPI if masked execution's tool calls M' ≠ original tool calls M.
- **Provable detection theorem (informal)**: for any attack that strictly changes tool selection, MELON flags with probability → 1.

## Connections

- Source: [CaMeL (Debenedetti et al. 2025)](camel-defeating-prompt-injections.md) — ex-ante capability policy; MELON is ex-post detection.
- Source: [IMTM Origin (FTH+25)](imtm-prompt-injections-protocols.md) — MELON addresses IPI sub-category of IMTM.
- Source: [Filter Impossibility (BGGKRR25)](filter-impossibility-ai-alignment.md) — filter-based defense fails; MELON's re-execution is structural, not filtering.
- Source: [Framework for Formalizing LLM Agent Security (Siu et al.)](formalizing-llm-agent-security.md) — oracle-function framework; MELON instantiates Action-Alignment and Task-Alignment oracles.
- Source: [RS-LLM-MAS (Hu et al. 2025)](rs-llm-multi-agent.md) — probabilistic defense; MELON is deterministic.
- Source: [AIOracle (VDKMR26)](extending-formalism-cryptography-ai.md) — security game framework.
- Concept: [Attack Taxonomy for LLMs](../concepts/attack-taxonomy-llms.md).
- Concept: [Input Manipulation Threat Model](../concepts/input-manipulation-threat-model.md).

## Open Questions / Limitations

- **Tool-selection-invariant attacks**: MELON's detection is specific to attacks that change tool selection; attacks that preserve tool selection but alter arguments may evade.
- **Masking function choice**: the neutral mask must be chosen carefully; suboptimal masks reduce detection power.
- **Compute cost**: requires re-executing the agent, doubling inference cost.
- **Adaptive attacks**: attacker who knows the masking function may design attacks that look consistent across masked executions.
- **Interaction with CaMeL**: formal composition of ex-ante + ex-post defenses is not yet analyzed.

## Quotes / Notable Passages

> "MELON detects attacks by re-executing the agent's trajectory with a masked user prompt modified through a masking function. The approach builds on the observation that under a successful attack, the agent's next action becomes less dependent on user tasks and more on malicious tasks."

> "MELON and MELON-Aug achieve superior performance with extremely low Attack Success Rate (ASR) while maintaining high Utility under Attack (UA), outperforming all baseline defense methods."
