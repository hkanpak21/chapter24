---
title: "A Framework for Formalizing LLM Agent Security"
type: source
date_ingested: 2026-04-12
authors: [Vincent Siu, Jingxuan He, Kyle Montgomery, Zhun Wang, Neil Gong, Chenguang Wang, Dawn Song]
venue: "arXiv:2603.19469v1 (March 2026)"
year: 2026
tags: [llm-security, agentic-systems, formal-models, access-control, adversarial-ml, prompt-injection]
---

## Summary

This paper formalizes the security of LLM-based agents through **four security properties** grounded in *contextual authorization* — the insight that security in agent systems is inherently context-dependent (the same action may be authorized in one context but a violation in another). The framework systematizes known attacks by mapping them to violations of specific properties, and reveals which oracles existing defenses approximate, exposing gaps.

Unlike Villa et al.'s AIOracle framework (which is cryptographic and focuses on LEARN/INFER phases), this paper focuses on the *operational security* of a deployed agent's action execution, using formal oracle functions that capture the authorization context at each step.

## Key Contributions

- **Four core security properties**: Task Alignment, Action Alignment, Source Authorization, Data Isolation — each formalized via oracle functions on the execution context C_t.
- **Execution context definition**: C_t = (p, Tr_{t-1}, M_t, E_t, S_auth,t, G) — prompt, trajectory history, memory, environment state, authenticated sources, permission graph.
- **Formal integrated security predicate**: secure(a_t, C_t) ↔ [objective within bounds] ∧ [trajectory alignment] ∧ [action alignment] ∧ [source authorization] ∧ [data isolation]. All four are individually necessary.
- **Attack taxonomy via property violations**: Nine documented attack types (prompt injection, jailbreak, confused deputy, task drift, capability misuse, cross-context leakage, memory poisoning, etc.) mapped to specific property violations.
- **Defense gap analysis**: Identifies which oracle functions existing defenses (Progent, FIDES, Conseca, Controlvalve) approximate and which they leave unaddressed.

## Key Definitions / Theorems

**Task Alignment (H_Tr)**: An agent's overall trajectory Tr_{t} serves objective o₀ authorized by the user prompt p. Oracle H_Tr(Tr_{t-1}, o₀) ∈ {0,1} judges binary alignment.

**Action Alignment (H_a)**: Each individual action a_t serves the stated task objective in context. Oracle H_a(a_t, Tr_{t-1}, o₀) ∈ {0,1}.

**Source Authorization (ℐ, ℒ)**: Every instruction acted upon traces to an authenticated source. ℐ(a_t, C_t) identifies which inputs functioned as instructions for action a_t; ℒ(input) returns the source provenance.

**Data Isolation (G)**: Information flows respect the permission graph G = (S, R) where S is the set of data sources and R ⊆ S × S is the permitted flow relation. No data from source s reaches output accessible to source s' unless (s, s') ∈ R.

**Attack-property mapping** (Table):
- Indirect Prompt Injection → Source Authorization + Action Alignment violation
- Direct Prompt Injection → Task Alignment violation  
- Jailbreak → Task Alignment (objective outside permitted space O)
- Confused Deputy → Source Authorization (user permissions ≠ agent permissions)
- Memory Poisoning → temporal Source Authorization violation
- Cross-context Information Leakage → Data Isolation violation

## Connections

- [AIOracle Framework](../concepts/aioracle-framework.md) — complementary; AIOracle covers LEARN/INFER security games; this paper covers operational authorization at action level
- [Attack Taxonomy for LLMs](../concepts/attack-taxonomy-llms.md) — expands the taxonomy with operational/contextual dimension
- [Vincent Siu](../entities/vincent-siu.md)
- [Dawn Song](../entities/dawn-song.md)
- Related to [Extending the Formalism of Cryptography to AI](extending-formalism-cryptography-ai.md) — the two papers cover complementary aspects of AI security formalization

## Open Questions / Limitations

- Oracle implementation: ℐ, ℒ, H_p, H_Tr, H_a are *theoretical specifications* — no practical algorithm achieves them for neural network agents (causal attribution in neural networks is an open problem).
- Compositional security: sequences of individually secure actions may create security violations — no formal theory for this.
- Multi-agent delegation: how authorization context propagates across agent-to-agent calls is not modeled.
- Does not cover training-time attacks (poisoning, backdoors) — purely operational/inference-phase.
- The four properties may not be formally complete — new attack classes may require additional properties.
- Framework assumes synchronous, turn-based execution; concurrent or asynchronous agents (TOCTOU attacks) are not modeled.

## Quotes / Notable Passages

> "Security in LLM agents is inherently contextual — the same action may be legitimate or a violation depending on authorization context."

> "The paper's primary contribution is making implicit security requirements explicit... clarity enables both incremental improvements to approximation techniques and identification of entirely unaddressed research areas."
