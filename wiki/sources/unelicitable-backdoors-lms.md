---
title: "Unelicitable Backdoors in Language Models via Cryptographic Transformer Circuits"
type: source
date_ingested: 2026-04-23
authors: [Andis Draguns, Andrew Gritsevskiy, Sumeet Ramesh Motwani, Charlie Rogers-Smith, Jeffrey Ladish, Christian Schroeder de Witt]
venue: "arXiv:2406.02619 (Jun 2024; v2 Feb 2025); NeurIPS 2024 SoLaR / SafeGenAI workshops"
year: 2024
tags: [backdoor, llm-security, cryptography, undetectable-backdoors, unelicitability, transformer-circuits]
---

## Summary

This paper (DGM+24) constructs **the first unelicitable backdoors for autoregressive transformers**: backdoors whose trigger mechanism is concealed such that the defender, **even with full white-box access**, cannot trigger or observe the hidden behavior. This strengthens [Goldwasser-Kim-Vaikuntanathan-Zamir 2022](planting-undetectable-backdoors.md) from classifier backdoors to generative language models, and crucially goes beyond *undetectability* to *unelicitability* — the stronger property that red-teaming cannot even exhibit the backdoor's effect.

The construction combines:
1. **Cryptographic trigger**: activation of the backdoor requires a digital-signature or encrypted payload that can only be generated with a secret key held by the attacker.
2. **Embedded-inside-model payload**: the harmful payload is computed by a cryptographic subcircuit embedded in the transformer's weights, so the backdoor's behavior is defined by the model's own forward pass, not by an external trigger string.
3. **Robustness to fine-tuning and latent-space perturbations**: arguments that the cryptographic structure survives standard defender interventions.

The key consequence: **automated red-teaming and certain formal-verification approaches are provably insufficient** to defend against these backdoors. This is the Pillar II analog of the [Ball et al. 2025 filter impossibility](filter-impossibility-ai-alignment.md) on the offense side — demonstrating that even an LLM provider's own auditing apparatus cannot detect cryptographically-concealed payloads.

## Key Contributions

- **Unelicitability** (stronger than undetectability): the defender cannot even *trigger* the backdoor, much less detect its existence.
- **Cryptographic transformer circuits**: construction technique embedding digital-signature verification and encrypted payload decoding into transformer forward pass.
- **Extension of GKVZ22 to generative LMs**: from classifier backdoors to autoregressive transformers.
- **Explicit red-teaming and verification bypass**: shows that standard defender techniques (red-teaming, certain formal verification) are provably defeated.
- **Robustness analysis**: arguments that the cryptographic structure survives fine-tuning and latent-space perturbations.

## Key Definitions / Theorems

- **Unelicitable backdoor**: an attacker-inserted backdoor such that no efficient defender (even with full white-box access) can find an input that triggers the backdoor, under cryptographic hardness assumptions.
- **Cryptographic transformer circuit**: a subcircuit of the transformer that implements digital-signature verification or encrypted payload decoding as part of the forward pass.
- **Main construction**: backdoor is encoded as "if input passes signature verification with the attacker's public key, output malicious payload; else behave normally." Verification is embedded in transformer weights; without the secret key, generating a trigger input is cryptographically hard.

## Connections

- Source: [Planting Undetectable Backdoors (GKVZ22)](planting-undetectable-backdoors.md) — classifier-level predecessor; this paper extends to generative LMs.
- Source: [Injecting Undetectable Backdoors in Obfuscated NNs (KKO+24)](io-undetectable-backdoors-nn.md) — complementary attack using iO; DGM+24 uses cryptographic circuits directly.
- Source: [Backdoor Defense, Learnability and Obfuscation (CHLX25)](backdoor-defense-learnability-obfuscation.md) — abstract defendability framework; DGM+24 instantiates the non-defendable case for transformers.
- Source: [Filter Impossibility for AI Alignment (BGGKRR25)](filter-impossibility-ai-alignment.md) — complementary: BGGKRR shows filters fail, DGM+24 shows red-teaming fails.
- Source: [Oblivious Defense (GSVV25)](oblivious-defense-backdoor-removal.md) — structural mitigation bypasses even unelicitable backdoors.
- Concept: [Undetectable Backdoors](../concepts/undetectable-backdoors.md) — extend with unelicitability.
- Concept: [Indistinguishability Obfuscation](../concepts/indistinguishability-obfuscation.md) — related cryptographic obfuscation notion.
- Concept: [Pseudorandomness](../concepts/pseudorandomness.md) — digital signatures as a pseudorandomness instance.

## Open Questions / Limitations

- **Practical construction**: the cryptographic transformer circuits are complex; instantiating them at production-model scale remains open.
- **Robustness to aggressive fine-tuning**: if the defender fine-tunes extensively on harmless data, does the cryptographic subcircuit survive?
- **Detection via behavioral probing**: while eliciting is hard, statistical probing for unusual subcircuit behavior might still succeed.
- **Interaction with GSVV25 mitigation**: can Fourier-based global mitigation remove unelicitable backdoors even without elicitation?
- **Elicitability vs. unelicitability boundary**: what's the exact cryptographic assumption needed for unelicitability?

## Quotes / Notable Passages

> "We introduce the first backdoors for autoregressive transformers that are unelicitable in nature. Unelicitability prevents the defender from triggering the backdoor, making it impossible to evaluate or detect ahead of deployment even if given full white-box access and using automated techniques, such as red-teaming or certain formal verification methods."
