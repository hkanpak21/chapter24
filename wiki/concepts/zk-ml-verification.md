---
title: Zero-Knowledge Proofs for ML Verification
type: concept
tags: [cryptography, zero-knowledge-proofs, ml-verification, commitments, certification]
---

## Definition
The use of zero-knowledge proof systems (zk-SNARKs, zk-STARKs, Bulletproofs, NIZK) and cryptographic commitments to let a prover convince a verifier that a claim about an ML artifact holds — e.g., "model M was trained on dataset D using algorithm A", "inference output y was produced by the committed model M on input x", "user data u was unlearned from M" — without revealing secret inputs (weights, training data, or user records).

Formally, each stage of the AI lifecycle is expressed as an NP relation R_stage((x, w)) = 1 where x is the public statement (e.g., commitment to model, hash of dataset) and w is the witness (model weights, private data). A ZKP certifies R_stage with completeness, soundness, and zero-knowledge against the verifier.

## Intuition
ZK for ML makes AI pipelines *auditable without being open-source*: regulators and users can verify integrity without forcing disclosure of proprietary models or private training data. Commitments bind a specific model/dataset version so later proofs can be linked to earlier ones.

## Properties / Theorems
- **Standard ZKP guarantees**: completeness, (knowledge) soundness, zero-knowledge; adapted from Goldwasser–Micali–Rackoff and subsequent SNARK/STARK literature.
- **Commitment security**: hiding (information-theoretic or computational) and binding.
- **Efficiency benchmarks**: zkDL, zkCNN, zkLLM, FairProof achieve polynomial prover time but with large constants (e.g., zkLLM ~803s per 13B-token forward pass).
- **Linkage gap**: ZKPoT (proof of training) and ZKPoI (proof of inference) typically use incompatible polynomial representations of the model — end-to-end linked proofs remain open.

## Where It Appears
- [zk-verifiable-ai-pipelines](../sources/zk-verifiable-ai-pipelines.md) (Balan, Learney, Wood 2025) — framework and gap analysis.
- Related crypto-for-AI foundations: [extending-formalism-cryptography-ai](../sources/extending-formalism-cryptography-ai.md).

## Related Concepts
- [verifiable-computation](verifiable-computation.md) — generic parent concept.
- [aioracle-framework](aioracle-framework.md) — game-based security for agentic AI, complementary lens.
- [undetectable-backdoors](undetectable-backdoors.md) — motivates ZK for training: without cryptographic certification, backdoors can hide even under audit.

## Open Questions
- End-to-end linkable ZKP across raw data → training → inference → unlearning.
- ZK-SNARK efficiency scaling to frontier-model sizes.
- Side-channel / metadata leakage from ZKP structure about the underlying model.
- Interaction of ZK proofs with differential privacy guarantees of the underlying training.
