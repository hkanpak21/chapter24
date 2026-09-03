---
title: "Seven Security Challenges That Must Be Solved in Cross-Domain Multi-Agent LLM Systems"
type: source
date_ingested: 2026-04-23
authors: [Ronny Ko, Jiseong Jeong, Shuyuan Zheng, Chuan Xiao, Tae-Wan Kim, Makoto Onizuka, Won-Yong Shin]
venue: "arXiv:2505.23847"
venue_evidence: "web search (arXiv abstract/HTML pages, Semantic Scholar, ResearchGate) found no refereed venue; still an arXiv preprint (versions up to v5 seen)"
year: 2025
tags: [agentic-systems, multi-agent, trust-boundaries, position-paper, desiderata]
claim_quantifier: empirical
antecedent: "none — a position paper. It argues from scenarios and asserts no conditional result."
adversary_bound: "none — no adversary is formalized anywhere in the paper, so nothing bounds one. The threats are described in prose as plausible attack scenarios."
date_verified: 2026-08-20
cls_target: none
cls_family: multiple
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: "absent"
cls_evidence_src: "no bound in §1 (challenge definitions) or §2-4 (challenges, metrics, countermeasures for C1-C7); position paper defines no adversary — confirmed by grepping the extracted PDF for 'adversary', 'threat model', 'PPT', which returns only prose scenario mentions, no formal definition"
cls_reason: "This page's pre-2026-08-20 challenge list was fabricated (overlapped the paper's actual seven on at most two entries) and was ignored per instruction; the seven below were verified directly against the primary PDF (arXiv:2505.23847v3), §1: (C1) unvetted dynamic grouping, (C2) collusion control, (C3) conflicting incentives and goals, (C4) distributed self-tuning misalignment/drift, (C5) cross-domain provenance obscurity, (C6) cross-domain context bypass, (C7) inter-domain confidentiality and integrity. This matches the page's own 'Corrected 2026-08-20' section, which is accurate and should be trusted going forward. family=multiple because the seven challenges span heterogeneous attack types (collusion, provenance falsification, context/prompt bypass, confidentiality/integrity violation) with no formal adversary to pin to one family value."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (K+25) is a **position paper** articulating why classical alignment/containment assumptions collapse across organizational trust boundaries in cross-domain multi-agent LLM systems. The seven challenges identified are the foundational desiderata any future UC-style composable-security framework for agentic AI must address. Not a theorem-bearing paper but a useful **desiderata document** for the field's formal gap.

The seven challenges, in the paper's own names and grouping (Section 1). The paper divides them into a behavioral-security class and a data-centric class:

Behavioral security:
1. **(C1) Unvetted dynamic grouping**
2. **(C2) Collusion control**
3. **(C3) Conflicting incentives and goals**
4. **(C4) Distributed self-tuning drift**

Data-centric security:
5. **(C5) Cross-domain provenance obscurity**
6. **(C6) Cross-domain context bypass**
7. **(C7) Inter-domain confidentiality and integrity**

**Corrected 2026-08-20.** An earlier version of this page listed a different seven — trust propagation across organizational boundaries, emergent-dynamics attacks, identity and provenance verification, cross-domain memory integrity, composable authorization, observability versus privacy, and adversarial evaluation metrics. That list is not the paper's. Only two entries correspond loosely to anything in it: the provenance item to C5, and the evaluation-metrics item to the paper's Section on metrics, which is a component of every challenge rather than a challenge of its own. The remaining five were not taken from the document. The earlier list is preserved here so the substitution is visible and not repeated.

For each challenge, the paper proposes evaluation metrics and highlights open formal problems. Positioned as the complementary "what needs to be solved" roadmap to match [Siu et al. 2026](formalizing-llm-agent-security.md)'s oracle-function vocabulary and [FTH+25](imtm-prompt-injections-protocols.md)'s IMTM threat taxonomy.

## Claim Boundary

- **Quantified over:** cross-domain multi-agent LLM systems, meaning networks whose agents are each controlled by a different organization and cooperate without central oversight. The paper's own examples are disaster response and supply-chain optimization. Single-organization deployments are outside the frame it argues about.
- **Antecedent:** none. This is a position paper. It argues that cross-domain collaboration breaks the unified trust assumptions behind current alignment and containment techniques, and it asserts this from scenarios rather than deriving it.
- **Which party is constrained:** neither. No adversary is formalized. The threats are prose descriptions of plausible attacks, and the proposed evaluation metrics are guidelines rather than measurements taken.
- **Does not establish:** that the seven categories are exhaustive, that any listed attack is realizable, or that any existing technique provably fails. It contains no theorem, no definition environment, and no experiment. Its recommendation, stated plainly in Section 1, is that the field pause at-scale deployment until security primitives addressing the seven are in place.
- **Abstract vs theorem:** no theorem exists, and the abstract does not claim one. It says the paper "maps the security agenda" and introduces seven categories "for each of which we also present plausible attacks, security evaluation metrics, and future research guidelines". The abstract is the more accurate description; calling the challenges "formal" is this wiki's addition, not the paper's.

## Key Contributions

- **Seven challenges** for cross-domain multi-agent LLM security, grounded in deployed-architecture realities. Named categories with prose argument, not formal objects.
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

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> Position paper that articulates why classical alignment/containment assumptions collapse across organizational trust boundaries.

Verified passages from the paper, for use in place of the above. From the abstract:

> "This position paper maps the security agenda for cross-domain multi-agent LLM systems. We introduce seven categories of novel security challenges, for each of which we also present plausible attacks, security evaluation metrics, and future research guidelines."

From Section 1, the challenges themselves:

> "Out of the seven cross-domain multi-agent LLM security challenges, the ones belonging to the behavioral security class are: (C1) unvetted dynamic grouping; (C2) collusion control; (C3) conflicting incentives and goals; and (C4) distributed self-tuning drift. The ones belonging to the data-centric security class are: (C5) cross-domain provenance obscurity; (C6) cross-domain context bypass; and (C7) inter-domain confidentiality and integrity."
