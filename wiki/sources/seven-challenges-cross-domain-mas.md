---
title: "Seven Security Challenges That Must Be Solved in Cross-Domain Multi-Agent LLM Systems"
type: source
date_ingested: 2026-04-23
authors: [Ronny Ko, Jiseong Jeong, Shuyuan Zheng, Chuan Xiao, et al.]
venue: "arXiv:2505.23847 (May 2025)"
year: 2025
tags: [agentic-systems, multi-agent, trust-boundaries, position-paper, desiderata]
---

## Summary

This paper (K+25) is a **position paper** articulating why classical alignment/containment assumptions collapse across organizational trust boundaries in cross-domain multi-agent LLM systems. The seven challenges identified are the foundational desiderata any future UC-style composable-security framework for agentic AI must address. Not a theorem-bearing paper but a useful **desiderata document** for the field's formal gap.

The seven challenges:
1. **Trust propagation across organizational boundaries** — when agents from different organizations interact, whose security policy applies?
2. **Emergent-dynamics attacks unique to multi-party LLM collaboration** — attacks that only manifest during inter-agent interaction, not single-agent behavior
3. **Identity and provenance verification** — how to cryptographically verify which agent performed which action
4. **Cross-domain memory integrity** — shared memory/state between agents from different trust domains
5. **Composable authorization** — agents delegating tasks to sub-agents with inherited or reduced privileges
6. **Observability vs privacy tension** — logging enough for audit but not leaking inter-organizational secrets
7. **Adversarial evaluation metrics** — how to benchmark cross-domain multi-agent security

For each challenge, the paper proposes evaluation metrics and highlights open formal problems. Positioned as the complementary "what needs to be solved" roadmap to match [Siu et al. 2026](formalizing-llm-agent-security.md)'s oracle-function vocabulary and [FTH+25](imtm-prompt-injections-protocols.md)'s IMTM threat taxonomy.

## Key Contributions

- **Seven formal challenges** for cross-domain multi-agent LLM security, grounded in deployed-architecture realities.
- **Evaluation metrics** for each challenge — benchmarks the field can adopt.
- **Desiderata document** for the missing UC-style composable security framework.
- **Position paper**: makes the gap concrete without claiming theorem-level solutions.

## Connections

- Source: [Framework for Formalizing LLM Agent Security (Siu et al.)](formalizing-llm-agent-security.md) — oracle-function vocabulary; K+25 is the threat-desiderata counterpart.
- Source: [IMTM Origin (FTH+25)](imtm-prompt-injections-protocols.md) — threat taxonomy; K+25 is the position-paper frame.
- Source: [AIOracle (VDKMR26)](extending-formalism-cryptography-ai.md) — cryptographic framework; K+25 flags gaps in cross-domain AIOracle extensions.
- Source: [CaMeL (DS+25)](camel-defeating-prompt-injections.md) — within-organization containment; K+25's challenges mostly apply cross-organization.
- Source: [RS-LLM-MAS (Hu et al. 2025)](rs-llm-multi-agent.md) — same-org MAS defense; K+25 argues cross-org requires new machinery.
- Concept: [Attack Taxonomy for LLMs](../concepts/attack-taxonomy-llms.md).

## Open Questions / Limitations

- **Position paper, not a theorem**: identifies challenges but does not solve them.
- **Seven is not exhaustive**: the list is a starting point, not complete.
- **Cross-domain LLM reality lags specification**: most production MAS are single-organization; cross-domain settings emerging but not yet standard.

## Quotes / Notable Passages

> "Position paper that articulates why classical alignment/containment assumptions collapse across organizational trust boundaries."
