---
title: AIOracle Framework
type: concept
tags: [formal-models, cryptography, adversarial-ml, agentic-systems, llm-security, access-control]
---

## Definition

The **AIOracle** abstraction [Villa et al. 2026] is a formal model for agentic LLM systems, analogous to how oracles are used in cryptography. An AIOracle is defined by a set of algorithms:

**Definition 1**: An AIOracle with r-round learning phase is defined by `2r+1` algorithms:
`((GENERATE_DATA_i, LEARN_i)_{i=1..r}, INFER)`

- **GENERATE_DATA_i(source)** → corpus_i: Extracts data from source (documents, interactions, etc.)
- **LEARN_i(model_{i-1}, corpus_i)** → model_i: Updates the model (pre-training, fine-tuning, RLHF, etc.)
- **INFER(prompt, context, model)** → result: Generates a response given input and context

The **source** is the set of all available data from which knowledge can be extracted. The **predicate φ(prompt, context, result)** defines what constitutes a "correct, useful, and harmless" response.

## Intuition

Cryptographers have long used oracle abstractions to reason about systems without specifying internal implementations. AIOracle extends this: an agentic LLM system is modeled as a two-phase process (LEARN, INFER), each with its own attack surface, security properties, and algorithmic description. This allows formal security proofs by reduction and composition.

The analogy to public-key cryptography: just as a PKE scheme is `(KeyGen, Enc, Dec)`, an AIOracle is `(GENERATE_DATA, LEARN, INFER)`. Security is defined via games with adversaries parameterized by their capability set ATK.

## Properties / Theorems

**φ-completeness (Definition 2)**: An AIOracle is φ-complete if for any PPT algorithm B (acting as the "non-adversarial baseline"), the security game returns 1 with probability at least p. Completeness measures correct behavior *without adversaries*.

**ε-ATK-ψ-secure (security definition)**: An AIOracle is ε-ATK-ψ-secure if for any PPT adversary A with capabilities ATK: `Adv = Pr[game = 1] ≤ (1-p)`. The advantage is measured relative to the completeness baseline.

**ATK capabilities**:
- `see_model`: adversary sees model parameters (white-box)
- `inject_learn`: adversary can corrupt training data/corpus
- `inject_infer`: adversary can inject into inference context
- `black_box`: adversary interacts only via API

**Security objectives captured**: Confidentiality (DPD game: can't extract training data), Integrity (can't produce harmful outputs), Availability (doesn't degrade for legitimate users).

**Dual Construction / Composition Theorem (Theorem 1)**: For predicates φ₁ ∧ φ₂, if BAIO is complete and ATK-ψ₁-secure, and CAIO is complete and ATK-ψ₂-secure, then the dual construction is complete and ATK-ψ-secure for φ = ψ₁ ∨ ψ₂. Enables modular security composition.

**CAIO vs BAIO**: Creative AIOracle (CAIO) solves computational/helpful tasks; Boring AIOracle (BAIO) solves decisional/safety tasks. Together they cover both helpfulness and harmlessness.

**Confidentiality-utility tension**: DPP-secure training (protecting all corpus data equally as confidential) fundamentally conflicts with completeness — a DPP-secure AIOracle cannot distinguish data classes present in both "positive" and "negative" training examples.

## Where It Appears

- [Extending the Formalism of Cryptography to AI](../sources/extending-formalism-cryptography-ai.md) — introduced and developed here

## Related Concepts

- [Attack Taxonomy for LLMs](attack-taxonomy-llms.md)
- [Evasion Attacks](evasion-attacks.md) — INFER-phase attacks are the LLM analogue
- [Poisoning Attacks](poisoning-attacks.md) — LEARN-phase attacks are the LLM analogue

## Open Questions

- Can the AIOracle framework be instantiated with efficient, provably secure constructions (not just definitions)?
- How does the framework handle multi-agent interactions where multiple AIOracles interact?
- Can the predicate φ be automatically derived from natural language safety guidelines?
- Formal relationship between AIOracle security and standard cryptographic notions (IND-CPA, UC-security, etc.)?
