---
title: Verifiable Computation
type: concept
tags: [cryptography, zero-knowledge, zk-snarks, verifiable-ai, succinct-arguments]
---

## Definition

**Verifiable computation** is the problem of designing protocols where a prover P, having performed some computation y = f(x), can convince a verifier V that the computation was done correctly, with verification taking much less work than re-executing f. Modern forms require the proof to be succinct (polylogarithmic in the computation size) and often zero-knowledge (revealing no information beyond the correctness of the claim).

**Key primitives**:
- **Succinct non-interactive arguments of knowledge (SNARKs)** — succinct, non-interactive, knowledge-sound.
- **Zero-knowledge SNARKs (zk-SNARKs)** — SNARKs that additionally hide x (or parts of x) from V.
- **STARKs** — transparent (no trusted setup), post-quantum, but larger proofs.

## Intuition

Verifiable computation solves the *integrity* half of "delegating computation to untrusted parties": the verifier can trust the output without trusting the prover. In the AI context, verifiable computation lets a model owner prove properties of their pipeline (training, inference, dataset provenance) without revealing proprietary artifacts.

## Properties / Theorems

**Efficiency**: Modern zk-SNARKs achieve O(log² n) proof size and O(log² n) verifier time for computations of size n, with prover overhead typically 10²–10⁵× the native computation.

**Trusted setup**: Many SNARK schemes (Groth16, PLONK) require a circuit-specific or universal trusted setup; STARKs avoid this at the cost of larger proofs.

**Soundness under cryptographic assumptions**: zk-SNARKs are sound under knowledge-of-exponent or random-oracle assumptions; STARKs rely only on collision-resistant hashing.

## Where It Appears

- [ZK Proofs for ML Pipelines](../sources/zk-verifiable-ai-pipelines.md) — applies ZK-SNARKs to prove end-to-end AI pipeline properties (dataset provenance, training integrity, inference correctness).
- [Covert Learning](../sources/covert-learning.md) — related primitive: covert verifiable learning uses verification to detect malicious oracle responses.
- [Extending Formalism of Cryptography to AI](../sources/extending-formalism-cryptography-ai.md) — Villa et al. note that integrity games in AIOracle can be instantiated via verifiable computation.

## Related Concepts

- [Zero-Knowledge ML Verification](zk-ml-verification.md) — AI-specific applications.
- [Computational Indistinguishability](computational-indistinguishability.md) — underlying security notion.

## Open Questions

- Concrete efficiency gains for large AI models (LLM-scale) — current overhead is prohibitive for billion-parameter models.
- Composability and aggregation of proofs across pipeline stages.
