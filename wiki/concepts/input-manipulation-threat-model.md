---
title: Input Manipulation Threat Model (IMTM)
type: concept
tags: [llm-security, agentic-systems, threat-model, prompt-injection, formal-model]
---

## Definition

The **Input Manipulation Threat Model (IMTM)** [Ferrag-Tihanyi-Hamouda-Maglaras-Lakas-Debbah, arXiv:2506.23260 / 2025] is a unified mathematical model of attacks on LLM-agent systems where an attacker U manipulates an input x = (prompt, context, tool-responses) to induce a target output y* from an LLM M. Success is formalized via (x, y*) satisfying the attacker's objective predicate φ_attack.

IMTM unifies several previously-separate attack categories under one formal representation:
- **Direct Prompt Injection (DPI)**: attacker is the user; x is user-provided.
- **Indirect Prompt Injection (IPI)**: attacker controls a data source (web page, retrieved document); x includes adversarial tool-retrieved content.
- **Multi-turn jailbreak**: attacker controls a sequence of prompts inducing cumulative state manipulation.
- **Context injection**: attacker manipulates system-level or persona-level context.
- **Memory poisoning**: attacker corrupts persistent agent memory used across sessions.

## Intuition

IMTM is the formal generalization of "anything the attacker can put into the LLM's input channel." Where [AIOracle (Villa et al. 2026)](../sources/extending-formalism-cryptography-ai.md) uses cryptographic security games abstracting over all attacks, IMTM is grounded in deployed-architecture realities: it explicitly models the layers (user input, tool outputs, system context, memory) through which an attacker can manipulate inputs.

The two formalisms are complementary: AIOracle gives the crypto-game vocabulary for proving security; IMTM gives the threat-taxonomy vocabulary for specifying what needs to be secured.

## Properties / Theorems

**IMTM ⊆ AIOracle**: any IMTM attack can be phrased as an AIOracle security-game violation, but IMTM's explicit layering gives finer-grained analysis.

**Layered defenses correspond to IMTM sub-categories**:
- [CaMeL (DS+25)](../sources/camel-defeating-prompt-injections.md) defends against IPI via capability policy.
- [MELON (ZYWGW25)](../sources/melon-indirect-prompt-injection.md) defends against IPI via masked re-execution.
- [NAAT (CYDS26)](../sources/naat-certified-semantic-smoothing.md) defends against DPI via certified semantic smoothing.
- [Ball et al. (BGGKRR25)](../sources/filter-impossibility-ai-alignment.md) proves black-box filters *cannot* defend against IMTM under cryptographic hardness.

**Adversarial-capability axes**: IMTM attacks vary along (a) attacker knowledge (black-box / gray-box / white-box), (b) attacker capabilities (prompt-only / tool-control / data-provider), (c) persistence (single-turn / session / permanent).

**Not yet composable**: IMTM does not (yet) admit a composition theorem analogous to UC; this is an open problem.

## Where It Appears

- [IMTM Origin Paper (Ferrag et al. 2025)](../sources/imtm-prompt-injections-protocols.md) — defining reference.
- [CaMeL (Debenedetti et al. 2025)](../sources/camel-defeating-prompt-injections.md) — capability-based defense within IMTM.
- [MELON (Zhu et al. 2025)](../sources/melon-indirect-prompt-injection.md) — masked re-execution within IMTM.
- [NAAT (Cheng et al. 2026)](../sources/naat-certified-semantic-smoothing.md) — certified smoothing for IMTM.
- [Filter Impossibility (Ball et al. 2025)](../sources/filter-impossibility-ai-alignment.md) — cryptographic impossibility of IMTM black-box filtering.
- [Framework for Formalizing LLM Agent Security (Siu et al. 2026)](../sources/formalizing-llm-agent-security.md) — oracle-function framework complementary to IMTM.

## Related Concepts

- [AIOracle Framework](aioracle-framework.md) — cryptographic-game counterpart.
- [Attack Taxonomy for LLMs](attack-taxonomy-llms.md) — earlier informal taxonomy; IMTM is the formal iteration.
- [Win-Win Theorem](win-win-theorem.md) — applies to IMTM: efficient IMTM defense for natural tasks ⟺ OWF existence.

## Open Questions

- **Composability theorem**: UC-style composition across IMTM layers.
- **Quantitative severity ordering**: categorical taxonomy → quantitative severity metrics.
- **Evolution**: as new attack classes emerge (agent-memory poisoning, cross-agent trust propagation), IMTM must extend.
- **Bridge to AIOracle**: formal translation between IMTM threat categories and AIOracle security-game predicates.
