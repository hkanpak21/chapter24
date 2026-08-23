---
title: "Defeating Prompt Injections by Design (CaMeL)"
type: source
date_ingested: 2026-04-23
authors: [Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes, Nicholas Carlini, Daniel Fabian, Christoph Kern, Chongyang Shi, Andreas Terzis, Florian Tramèr]
venue: "arXiv:2503.18813 (Mar 2025; v2 Jun 2025); Google / DeepMind / ETH Zürich"
year: 2025
tags: [llm-security, agentic-systems, capability-based-security, provable-security, prompt-injection]
claim_quantifier: empirical
antecedent: "The security policies handed to the interpreter express the set of allowed actions for the user's prompt; the interpreter and the tools are trusted; side channels are out of scope."
adversary_bound: "none — the adversary supplies an initial adversarial memory state and is otherwise unrestricted. Containment comes from the interpreter's control- and data-flow restrictions, not from any bound on adversary compute, queries, or memory."
date_verified: 2026-08-20
cls_target: outputs
cls_family:
cls_phase: test time
cls_access: none
cls_write: responses
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: "absent"
cls_evidence_src: "no bound on A in Game PI-SEC, §4 (Fig. 3); A is defined only as producing an initial adversarial memory state mem*, with no restriction stated on its computation, queries, or memory"
cls_reason: "family left blank: prompt injection / agentic control-flow hijacking (Game PI-SEC, §4) does not map onto the family vocabulary; closest candidate 'evade audit' (win condition is an action escaping Ω_prompt/Verify) rejected because that value pairs elsewhere with post-hoc detector evasion on a released model, not live control-flow hijacking. target=outputs: PI-SEC's win condition targets the Agent's action trace. write=responses is a low-confidence best fit: the attacker injects content into untrusted tool output the agent consumes; no training-corpus or parameter-level write applies. Re-verified directly against raw/DS+25_CaMeL.pdf per the assignment's audit warning: 0 occurrences of 'Theorem', 'Lemma', or 'we prove'; Game PI-SEC (Fig. 3-4, §4) states no restriction on A's computation, queries, or memory anywhere in §4-5."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (DS+25, CaMeL = **CA**pabilities for **M**achin**E** **L**earning, per the paper's own footnote 1; an earlier version of this page gave the expansion as "Capabilities Mediating LLM-agents", which the paper does not use) provides a **capability-based access-control formalism** for LLM agents in which every value carries provenance metadata and tools enforce explicit policy checks at call time. The design claim, which the paper asserts and does not prove: under the dual-LLM decomposition (privileged planner + quarantined extractor), untrusted data cannot influence the control flow of the agent. The abstract puts it as extracting the control and data flows from the trusted query, so that "the untrusted data retrieved by the LLM can never impact the program flow". The word "proves" stood here and is corrected 2026-08-20; the paper contains no proof.

The architecture separates LLM roles:
1. **Privileged planner LLM**: has authority to issue tool calls; operates only on *trusted* inputs (original user instruction).
2. **Quarantined extractor LLM**: processes *untrusted* tool outputs; can generate values but not issue tool calls.
3. **Capability dataflow**: every value has provenance tags (trusted/untrusted + origin); tools enforce policy at call time (e.g., "this tool cannot be called with untrusted argument X").

The sentence that follows describes what CaMeL's design is meant to achieve, not a proved statement: the paper contains no theorem, lemma, or proof. Corrected 2026-08-20. For any sequence of tool invocations, if the policy forbids untrusted-data influence on privileged tool calls, then indirect prompt injection cannot cause unauthorized actions. Empirical results: 77% of AgentDojo tasks solved with full guarantees vs. 84% undefended — a small utility cost.

What the paper does supply in place of a theorem is the **PI-SEC security game** of Section 4: the game takes an adversary A, an Agent, and a tool set; the Agent returns a trace of `(tool, args, mem)` tuples; Ω_prompt is the set of actions the Agent may take without compromising security; the adversary supplies an initial memory state and wins if the trace contains an action outside Ω_prompt. Section 5 opens by observing that enumerating Ω_prompt for every prompt would satisfy the definition trivially and is impossible in practice, which is why CaMeL substitutes control-flow integrity, capabilities, and policies for enumeration. Nothing is proved about the substitution.

The paragraph that stood here called CaMeL the closest extant proxy for a UC-style containment theorem in agentic LLMs, and the most formally grounded defence in the 2025-2026 landscape. Both are the wording and the judgment of a secondary survey artifact, not of this paper and not of any comparison the wiki has carried out. Withdrawn 2026-08-20. What is true and checkable is narrower: CaMeL gives no composition theorem, and the security game it defines is not paired with a proof.

## Claim Boundary

- **Quantified over:** executions of the CaMeL agent on the AgentDojo benchmark, inside the PI-SEC game of Section 4, for one fixed tool set and one fixed set of policies. Not over all agents, all tools, or all prompts.
- **Antecedent:** the policies passed to the interpreter capture Ω_prompt, the set of actions allowed for the prompt; the Privileged LLM's code is executed by the CaMeL interpreter and no other path; the Quarantined LLM cannot issue tool calls; side channels are excluded. The paper states that side channels undermine the strong-security claim to a degree.
- **Which party is constrained:** the adversary, by interface only. It supplies an initial adversarial memory state for the tools and is otherwise unrestricted in computation, queries, and memory. No party is bounded in any resource.
- **Does not establish:** any theorem. The strings `Theorem`, `Lemma`, and `we prove` do not occur in the paper. "Provable security" in the abstract counts AgentDojo tasks completed while the policies held, not a proved statement quantified over adversaries. It also does not establish that a correct policy set can be written for an arbitrary task; Section 5 says enumerating Ω_prompt is impossible in practice.
- **Abstract vs theorem:** there is no theorem to compare the abstract against. "77% of tasks with provable security" is a measurement on one benchmark, and the phrase invites the reading that the 77% carries a proof, which it does not.

## Key Contributions

- **Capability-based access control for LLM agents**: every value has provenance metadata; tools enforce policy at call time.
- **Dual-LLM decomposition**: privileged planner (trusted inputs only) + quarantined extractor (untrusted data); proves separation prevents control-flow hijacking.
- **Containment claim** (labelled "provable containment theorem" in an earlier version of this page; the paper proves no theorem, corrected 2026-08-20): untrusted data cannot influence control flow under the capability policy.
- **PI-SEC security game** (Section 4, Figure 3): the definition against which the containment claim is stated. A definition, not a result.
- **AgentDojo benchmark results**: 77% of tasks solved with full provable guarantees (vs. 84% undefended) — small utility cost for provable protection.
- **Template for UC-style agent composition**: demonstrates that formal containment is achievable in production LLM architectures.

## Key Definitions / Theorems

- **Capability tag**: each value in the agent's state has metadata (source, trust level, type).
- **Policy**: a function checking whether a tool call is permitted given the provenance of its arguments.
- **Privileged planner**: issues tool calls; only receives trusted inputs (the original user instruction).
- **Quarantined extractor**: processes untrusted inputs (tool outputs, retrieved documents); can generate values but not issue tool calls.
- **Main containment claim** (not a theorem in the paper; corrected 2026-08-20): if the policy enforces that no untrusted value can be an argument to a privileged tool call, then for any attacker-controlled tool output, the control flow follows only the original user instruction's path.
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

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> Under the dual-LLM decomposition (privileged planner + quarantined extractor), untrusted data cannot influence the control flow, yielding the first end-to-end 'provable security' statement on the AgentDojo benchmark (77% solved with full guarantees vs 84% undefended).

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> The closest extant proxy for a UC-style containment theorem in agentic LLMs.
