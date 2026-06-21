---
title: A Framework for Cryptographic Verifiability of End-to-End AI Pipelines
type: source
date_ingested: 2026-04-12
authors: [Kar Balan, Robert Learney, Tim Wood]
venue: IWSPA (ACM International Workshop on Security and Privacy Analytics)
year: 2025
tags: [cryptography, zero-knowledge-proofs, ml-verification, commitments, formal-models, compliance]
---

## Summary
This is a **framework / gap-analysis paper**, not a theorem-proving paper. Balan, Learney, and Wood (Digital Catapult + Surrey) propose a six-stage cryptographic verifiability framework for AI pipelines — (1) raw data verification, (2) extraction & analysis, (3) model training, (4) model evaluation, (5) inference, (6) unlearning — and survey which cryptographic tools (digital signatures, cryptographic commitments, zero-knowledge proofs) are deployable at each stage. They then identify gaps where current ZK tooling is either absent or too inefficient to be linkable across stages.

The paper's formal content is limited to standard textbook definitions of ZKPs (completeness, soundness, zero-knowledge), commitments (hiding, binding), and digital signatures (EUF-CMA). The novelty is the *mapping exercise*: C2PA / content provenance for stage 1; federated-learning ZK (e.g., ZKAUDIT, KAIZEN, zkPoT) for stage 3; zkDL/zkCNN/zkLLM-style ZK inference for stage 5; machine-unlearning ZKPs (FairProof, zkPoUL, Eisenhofer et al.) for stage 6. The gap section highlights (i) the lack of linkable provenance across stages, (ii) the cost of ZK-SNARKs for large models (zkLLM: 803s per 13B token), and (iii) inconsistency between ZKPoT and ZKPoI representations.

**Flag to wiki**: this paper is less formal than the brief suggested. It is a systems/policy survey with cryptographic flavor, not an impossibility or verification theorem. Useful for the wiki as an entry point to ZK-for-ML tooling and for EU AI Act compliance context, but does not contribute new formal security definitions or proofs.

## Key Contributions
- Six-stage framework for cryptographic verifiability across the AI lifecycle.
- Categorization of existing tools (C2PA, ZKAUDIT, KAIZEN, zkDL, zkCNN, zkLLM, FairProof, ZKPoUL, DECORAIT, snarkGPT) by pipeline stage.
- Gap analysis: no end-to-end linkable proof system exists; ZKPoT and ZKPoI use incompatible polynomial representations of models.
- Regulatory framing around EU AI Act, GDPR Art. 17, CCPA.

## Key Definitions / Theorems
No new theorems. Standard definitions invoked:
- **ZKP (completeness / soundness / zero-knowledge)** — interactive proof between prover P and verifier V.
- **Commitment (hiding / binding)**.
- **Digital signature (EUF-CMA)**.
- Classes discussed: zk-SNARK, zk-STARK, Bulletproofs, NIZK.

## Connections
- ZK for ML inference connects to the broader program of [verifiable computation](../concepts/verifiable-computation.md) applied to learning.
- Related to [extending-formalism-cryptography-ai](extending-formalism-cryptography-ai.md) (Villa et al.) which provides a cryptographic formalism for AI more broadly.
- Related to [formalizing-llm-agent-security](formalizing-llm-agent-security.md) (AIOracle) for game-based security definitions.
- Authors: [Kar Balan](../entities/kar-balan.md), [Robert Learney](../entities/robert-learney.md), [Tim Wood](../entities/tim-wood.md).

## Open Questions / Limitations
- No unified cryptographic "AI pipeline proof" primitive; the authors motivate but do not construct one.
- ZK-SNARK efficiency for modern LLM-scale models is an open engineering + theory problem.
- No formal soundness definition tying multi-stage proofs; linking is identified as a gap.
- No treatment of privacy leakage *from* a ZKP about a model (side-channel through proof structure).

## Quotes / Notable Passages
"ZKPs do not necessarily hide algorithms used … and so a ZKPoT doesn't hide implementation details if the representation of the model differs, for example, from that of a ZKPoI."

"We propose a framework for end-to-end verifiable AI pipelines, identifying key components and analyzing existing cryptographic tools … [and] identify the gaps and challenges."
