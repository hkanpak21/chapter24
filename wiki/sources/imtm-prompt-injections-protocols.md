---
title: "From Prompt Injections to Protocol Exploits: Threats in LLM-Powered AI Agents Workflows (IMTM origin)"
type: source
date_ingested: 2026-04-23
authors: [Mohamed Amine Ferrag, Norbert Tihanyi, Djallel Hamouda, Leandros Maglaras, Abderrahmane Lakas, Merouane Debbah]
venue: "arXiv:2506.23260 (Jun 2025; v2 Dec 2025); ICT Express / Elsevier"
year: 2025
tags: [llm-security, agentic-systems, threat-model, prompt-injection, protocol-exploits, formal-model]
---

## Summary

This paper (FTH+25) provides **the first unified end-to-end threat model for LLM-agent ecosystems** and is the *originating source* of the **Input Manipulation Threat Model (IMTM)** as a formal object. IMTM mathematically characterizes the behavior and success conditions of prompt-injection attacks and unifies diverse attack forms (direct prompt injection, indirect prompt injection, jailbreaks, multi-turn exploits) under a single theoretical representation.

Beyond IMTM, the paper introduces formal definitions for three additional threat categories covering LLM-agent ecosystems:
1. **Model Compromise attacks** — backdoors, fine-tuning attacks, model-level integrity violations
2. **System/Privacy attacks** — data exfiltration, sensitive-information leakage
3. **Protocol Vulnerabilities** — exploits at the inter-agent protocol layer (MCP, tool-calling APIs, memory-passing protocols)

Each category specifies attacker capabilities, objectives, and affected layers in a structured taxonomy covering **30+ concrete attack classes**. The paper positions itself as the natural formal *rival/complement* to [Villa et al.'s AIOracle](extending-formalism-cryptography-ai.md) for agentic pipelines: where AIOracle uses cryptographic security games, IMTM uses a more-practical layered-protocol-exploit view grounded in actual deployed agent architectures.

This paper is now the canonical citation for "formal prompt injection threat model" in 2025-2026 literature.

## Key Contributions

- **Input Manipulation Threat Model (IMTM)**: first formal mathematical characterization of prompt injection attacks, unifying direct/indirect/multi-turn variants under one framework.
- **Four-category threat taxonomy**: IMTM + Model Compromise + System/Privacy + Protocol Vulnerabilities — covers 30+ concrete attack classes.
- **Layered-protocol view**: attacks categorized by which layer of the agent stack they target (prompt, model, system, protocol).
- **First unified end-to-end threat model for LLM-agent ecosystems**: fills the gap between ad-hoc attack taxonomies and formal-security games.
- **Complement to AIOracle**: grounded in deployed-architecture exploits rather than abstract cryptographic games.

## Key Definitions / Theorems

- **Input Manipulation Threat Model (IMTM)**: attacker U manipulates input x = (prompt, context, tool-responses) to induce target output y* from LLM M; formalizes success via (x, y*) satisfying attacker's objective predicate.
- **Direct Prompt Injection (DPI) ∈ IMTM**: x is user-provided; attacker is the user.
- **Indirect Prompt Injection (IPI) ∈ IMTM**: x includes tool-retrieved content; attacker controls a data source (e.g., a web page the agent retrieves).
- **Multi-turn jailbreak ∈ IMTM**: attacker controls a sequence of prompts inducing cumulative state manipulation.
- **Protocol Vulnerability Threat Model**: formalizes exploits at MCP / tool-invocation / memory-passing protocols that are distinct from IMTM.
- **Attack complexity axes**: attacker knowledge (black-box / gray-box / white-box), capabilities (prompt-only / tool-control / data-provider), persistence (single-turn / session / permanent).

## Connections

- Source: [Extending the Formalism of Cryptography to AI (VDKMR26)](extending-formalism-cryptography-ai.md) — AIOracle framework; IMTM is the complementary threat-model-layer formalization.
- Source: [Framework for Formalizing LLM Agent Security (Siu et al.)](formalizing-llm-agent-security.md) — oracle-function approach; IMTM is the threat-taxonomy counterpart.
- Source: [CaMeL (Debenedetti et al.)](camel-defeating-prompt-injections.md) — capability-based IPI defense; operates within the IMTM's IPI sub-category.
- Source: [MELON (Zhu et al.)](melon-indirect-prompt-injection.md) — IPI defense; instance of IMTM-based defense.
- Source: [Seven Security Challenges in Multi-Agent LLM Systems](seven-challenges-cross-domain-mas.md) — position paper on emergent multi-agent threats; complements IMTM's single-agent focus.
- Source: [Filter Impossibility (BGGKRR25)](filter-impossibility-ai-alignment.md) — formal impossibility for prompt filters; shows IMTM defense at the filter layer is fundamentally hard.
- Concept: [Input Manipulation Threat Model](../concepts/input-manipulation-threat-model.md) — **new concept page needed**.
- Concept: [Attack Taxonomy for LLMs](../concepts/attack-taxonomy-llms.md) — IMTM is a more formal iteration.
- Concept: [AIOracle Framework](../concepts/aioracle-framework.md) — complementary formal model.

## Open Questions / Limitations

- **IMTM is a descriptive formalism, not a security-game**: does not yet pair with provable defense constructions; complementary to AIOracle in this regard.
- **Compositionality across threat categories**: can an attacker who exploits IMTM *and* protocol-vulnerability be treated with a composed threat model?
- **Quantitative severity metrics**: the taxonomy is categorical; quantitative severity ordering is open.
- **Evolution**: as new attack classes emerge (e.g., agent-memory poisoning), IMTM must be extended.

## Quotes / Notable Passages

> "First unified end-to-end threat model for LLM-agent ecosystems and is the originating source of the Input Manipulation Threat Model (IMTM) as a formal object."

> "Covers 30+ concrete attack classes, with attacker capabilities, objectives, and affected layers specified per category."
