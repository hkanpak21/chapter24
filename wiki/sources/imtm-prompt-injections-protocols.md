---
title: "From Prompt Injections to Protocol Exploits: Threats in LLM-Powered AI Agents Workflows (IMTM origin)"
type: source
date_ingested: 2026-04-23
authors: [Mohamed Amine Ferrag, Norbert Tihanyi, Djallel Hamouda, Leandros Maglaras, Abderrahmane Lakas, Merouane Debbah]
venue: "arXiv:2506.23260v2 (14 Dec 2025). Journal venue unconfirmed from PDF — the PDF carries IEEE membership designations for its authors but names no venue; the earlier attribution to ICT Express / Elsevier came from the ingest, not the document."
year: 2025
tags: [llm-security, agentic-systems, threat-model, prompt-injection, protocol-exploits, formal-model]
claim_quantifier: empirical
antecedent: "none — the paper states definitions and a taxonomy, and asserts no conditional result."
adversary_bound: "none — the adversary is an arbitrary transformation g on the context (h, x, k), unconstrained in computation, queries, or knowledge. The one place a budget appears is the perturbation budget carried over from the adversarial-examples literature in the description of evasion attacks, and it bounds a perturbation, not a resource."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: black box
cls_write: read only
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: absent
cls_evidence_src: "no bound in the Adversary Model §V-A-2 (eq 15), the Prompt-Based/Jailbreaking/Evasion definitions (eq 17-20), or the abstract"
cls_reason: "The abbreviation IMTM occurs zero times in the paper (confirmed by grep -a over the extracted PDF text) and zero times across raw/; the paper writes 'Input Manipulation Threat Model' in full. The paper is a survey with three parallel formal threat models (Input Manipulation, System & Privacy, Protocol-Level) and no theorem; classified here on the Input Manipulation Threat Model (eq 13-21, §V-A), the abstract's lead category and the formalism this slug names. g:(h,x,k)->(h',x',k') is an arbitrary transformation with no compute, query, or perturbation-radius bound in its definition, so party/unit/frame=none/none/none per Rule 2. family=evade: the formalized sub-cases (Prompt-Based eq 17, Jailbreaking eq 19, Evasion eq 20) all reduce to causing pi(y,a)=0, a safety-policy violation at inference time. write=read only: the central prompt-based formalization (eq 17) modifies (h,x) but explicitly leaves k unchanged, i.e. the attacker submits through the ordinary query channel rather than writing to a persisted corpus; indirect prompt injection (writing to an external retrieved source) is described in prose elsewhere but is not part of the formalized equations."
cls_prov: P
cls_date: 2026-08-22
---


> **Acronym note, 2026-08-22.** The string "IMTM" occurs zero times in this paper and zero
> times across all 186 PDFs in `raw/`, appearing only in a discarded machine-generated
> artifact, which is where this page's slug and the raw filename came from. The underlying
> object is real: the paper writes "Input Manipulation Threat Model" in full seven times.
> The concept stands, the abbreviation is not the authors'.

## Summary

This paper (FTH+25) calls itself a survey and describes its own contribution as a unified end-to-end threat model for LLM-agent ecosystems. It is the originating source of the **Input Manipulation Threat Model** as a named object.

**Naming, corrected 2026-08-20.** The abbreviation "IMTM" does not occur in the paper. The paper writes "Input Manipulation Threat Model" in full, seven times, and never abbreviates it. "IMTM" is this wiki's own coinage; the page slug and the linked concept page carry it. Anything written for outside readers should use the paper's full phrase and should not attribute the acronym to the authors. IMTM mathematically characterizes the behavior and success conditions of prompt-injection attacks and unifies diverse attack forms (direct prompt injection, indirect prompt injection, jailbreaks, multi-turn exploits) under a single theoretical representation.

Beyond IMTM, the paper introduces formal definitions for three additional threat categories covering LLM-agent ecosystems:
1. **Model Compromise attacks** — backdoors, fine-tuning attacks, model-level integrity violations
2. **System/Privacy attacks** — data exfiltration, sensitive-information leakage
3. **Protocol Vulnerabilities** — exploits at the inter-agent protocol layer (MCP, tool-calling APIs, memory-passing protocols)

Each category specifies attacker capabilities, objectives, and affected layers in a structured taxonomy covering **30+ concrete attack classes**. The paper positions itself as the natural formal *rival/complement* to [Villa et al.'s AIOracle](extending-formalism-cryptography-ai.md) for agentic pipelines: where AIOracle uses cryptographic security games, IMTM uses a more-practical layered-protocol-exploit view grounded in actual deployed agent architectures.

This paper is now the canonical citation for "formal prompt injection threat model" in 2025-2026 literature.

## Claim Boundary

- **Quantified over:** the attack literature the authors surveyed. The abstract says the paper "catalogs over thirty attack techniques" in four categories — Input Manipulation, Model Compromise, System and Privacy Attacks, Protocol Vulnerabilities — and reports validation "through expert review and cross-mapping with real-world incidents and public vulnerability repositories (e.g., CVE, NIST NVD)". The scope is the corpus, not the space of agent systems.
- **Antecedent:** none. The paper states no conditional result. Its "formal mathematical formulation" is notation for a system model S = (M_θ, T, Φ), a context C = (h, x, k), an output pair (y, a), a binary safety policy π, and an adversary transformation g : (h, x, k) ↦ (h′, x′, k′), with success defined as π(y, a) = 0 or L(y, o) ≤ ε.
- **Which party is constrained:** neither. The adversary is an arbitrary map on the context. The system is an arbitrary LLM in an arbitrary agentic frame. Nothing is bounded in compute, queries, or memory.
- **Does not establish:** any theorem, security reduction, or impossibility. There is no proof anywhere in the paper and no defence is shown to meet the definitions. The notation names the attack surface; it does not let one decide whether a given system is secure, nor compare two attacks by strength. The completeness of the four categories is asserted, not argued.
- **Abstract vs theorem:** there is no theorem. The abstract's "first integrated taxonomy" and "formal system definitions for each threat class" are priority and coverage claims about a survey. Reading "formal" here as "proved" is the error the page is guarding against.

## Key Contributions

- **Input Manipulation Threat Model**: first formal mathematical characterization of prompt injection attacks, unifying direct/indirect/multi-turn variants under one framework.
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

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> First unified end-to-end threat model for LLM-agent ecosystems and is the originating source of the Input Manipulation Threat Model (IMTM) as a formal object.

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> Covers 30+ concrete attack classes, with attacker capabilities, objectives, and affected layers specified per category.

The abstract's own words on both points, verbatim:

> "This survey introduces a unified end-to-end threat model for LLM-agent ecosystems, spanning host-to-tool and agent-to-agent communications, and catalogs over thirty attack techniques across Input Manipulation, Model Compromise, System and Privacy Attacks, and Protocol Vulnerabilities. For each category, we provide a formal mathematical formulation of the underlying threat model, defining attacker capabilities, objectives, and affected layers to enable systematic analysis."
