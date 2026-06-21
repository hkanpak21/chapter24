---
title: "Extending the Formalism and Theoretical Foundations of Cryptography to AI"
type: source
date_ingested: 2026-04-12
authors: [Federico Villa, F. Betül Durak, Tadayoshi Kohno, Tapdig Maharramli, Franziska Roesner]
venue: arXiv preprint (arXiv:2603.02590v1)
year: 2026
tags: [cryptography, adversarial-ml, agentic-systems, formal-models, access-control, llm-security, confidentiality, integrity, availability]
---

## Summary

This paper applies cryptographic methodology — rigorous formal definitions, adversarial models, and reduction-based security proofs — to the security of agentic LLM systems. The central contribution is the **AIOracle** abstraction, a formal model of an agentic AI system with two phases (LEARN and INFER), and a security game framework that simultaneously captures confidentiality, integrity, and availability within a single model.

The authors first survey the landscape of attacks on LLMs (constructing a multi-dimensional taxonomy), then develop formal treatments of access control, helpfulness, and harmlessness. They prove that naive helpfulness-maximizing training fundamentally conflicts with completeness (i.e., a DPP-secure AIOracle cannot fully distinguish cats from dogs if the training corpus treats both as confidential). They also formalize a **modular dual construction** that decomposes an AIOracle into a *creative* (CAIO) and a *boring* (BAIO) component, allowing security objectives to be composed.

The paper analyzes four existing agentic frameworks (FIDES, Progent, Conseca, Controlvalve) through the AIOracle lens, demonstrating that the formalism clarifies design choices and reveals implicit assumptions.

## Key Contributions

- **AIOracle abstraction**: Formal model of an r-round agentic LM system with algorithms `(GENERATE_DATA, LEARN_{1..r}, INFER)`. Separates the LEARN phase (training, fine-tuning) from the INFER phase (inference, tool calls). Unifies prior ad-hoc system descriptions.
- **Multi-dimensional attack taxonomy**: Classifies LLM attacks along five axes — attack vector (data-based / prompt-based), attack phase (LEARN / INFER), adversarial knowledge (white-box / black-box / gray-box), security goals (confidentiality / integrity / availability), and attack persistence (transient / persistent). Covers: prompt injection, jailbreak, data exfiltration, membership inference, data poisoning, backdoor.
- **Security game framework**: Captures all three security objectives (C, I, A) in a single game parameterized by adversary capability set ATK. Adversary wins if predicate φ(prompt, context, result) is violated.
- **Confidentiality vs. utility tension (Theorem)**: Formally proves that DPP-secure training (protecting all data elements equally) conflicts with completeness. A DPP-secure AIOracle cannot distinguish a cat from a dog if both appear in the training corpus. This formalizes the fundamental tension in privacy-preserving ML.
- **Modular dual construction (Theorem 1)**: If BAIO and CAIO are complete and ATK-ψ-secure for their respective predicates, then the dual construction is complete and ATK-ψ-secure for the conjunction φ₁ ∧ φ₂. Allows compositional security reasoning.
- **Framework analysis**: Contextualizes FIDES (taint tracking / information flow), Progent (tool access control), Conseca (context-aware policy generation), and Controlvalve (CFG + LM judge) within the AIOracle model.

## Key Definitions / Theorems

**AIOracle (Definition 1)**: An r-round learning phase defined by `2r+1` algorithms `((GENERATE_DATA_i, LEARN_i)_{i=1..r}, INFER)`.

**Completeness (Definition 2)**: An AIOracle is φ-complete if for any PPT algorithm B, the security game returns 1 with probability at least p. The "adversary" in the completeness game does not interfere — it measures correct behavior in the absence of an attack.

**ATK-ψ-secure AIOracle**: An AIOracle is ε-ATK-ψ-secure if for any PPT adversary A, `Adv = Pr[Security_Game(ATK, source) = 1] ≤ (1-p)`. The advantage is defined relative to the completeness baseline.

**ATK set**: Captures adversary capabilities — `{see_model, inject_learn, inject_infer, black_box}`. Determines which security game variant applies.

**Dual Construction Theorem (Theorem 1)**: If BAIO and CAIO are complete and ATK-ψ-secure for ψ = Ψ₁ and ψ = Ψ₂ respectively, then the dual construction is complete and ATK-ψ-secure for φ = Ψ₁ ∨ Ψ₂.

**DPD game (Algorithm 2)**: Differentially Private Distinguishability — models membership inference attack formally.

## Connections

- [AIOracle Framework](../concepts/aioracle-framework.md)
- [Attack Taxonomy for LLMs](../concepts/attack-taxonomy-llms.md)
- [Federico Villa](../entities/federico-villa.md)
- [Tadayoshi Kohno](../entities/tadayoshi-kohno.md)
- [Franziska Roesner](../entities/franziska-roesner.md)
- [F. Betül Durak](../entities/betul-durak.md)
- Relates to [Evasion Attacks](../concepts/evasion-attacks.md) and [Poisoning Attacks](../concepts/poisoning-attacks.md) — this paper extends those concepts to the agentic LLM setting

## Open Questions / Limitations

- The framework focuses on formal security definitions; it does not provide efficient constructions of secure AIOracles.
- Completeness and security may be in fundamental tension beyond the DPP case — further impossibility results are needed.
- The ATK model is grey-box (restricted white-box) — fully adaptive adversaries with model internals are not fully captured.
- The policy predicate φ (defining what is "harmless") must be manually specified; no general method for deriving φ is given.
- Empirical validation of the taxonomy against real-world LLM attack deployments is left to future work.

## Quotes / Notable Passages

> "Our studies suggest that if we were to design a secure system with measurable security, then we might want to use a modular approach to break the problem into sub-problems and let the composition on different modules complete the design."

> "The tension is that if we have a DPP-secure AIOracle (i.e. the classifier), then AIOracle cannot distinguish a cat from a dog which undermines the utility of an AIOracle."
