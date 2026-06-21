---
title: "Injecting Undetectable Backdoors in Obfuscated Neural Networks and Language Models"
type: source
date_ingested: 2026-04-23
authors: [Alkis Kalavasis, Amin Karbasi, Argyris Oikonomou, Katerina Sotiraki, Grigoris Velegkas, Manolis Zampetakis]
venue: "arXiv:2406.05660 (Jun 2024; v2 Sep 2024); NeurIPS 2024"
year: 2024
tags: [backdoor, cryptography, indistinguishability-obfuscation, llm-security, undetectable-backdoors]
---

## Summary

This paper (KKO+24) shows that if a neural network (or language model) is shipped as an **indistinguishability-obfuscated (iO)** circuit — a plausible IP-protection pattern where providers ship obfuscated weights to protect intellectual property — **an adversary can plant backdoors whose existence is undetectable even to observers with complete white-box access to the obfuscated artifact**. The theorem reduces detection to breaking iO, which is infeasible under standard cryptographic assumptions (Jain-Lin-Sahai 2021: iO from LWE + LPN + NC⁰ PRGs + SXDH).

The paper closes the **white-box-vs-black-box gap** left open by Goldwasser-Kim-Vaikuntanathan-Zamir 2022. GKVZ22's original result gave black-box undetectability (weights inaccessible to defender) and a weaker white-box version; KKO+24 establishes **full white-box undetectability under the iO assumption**: even with the complete obfuscated weights, the defender cannot distinguish backdoored from clean.

The construction additionally extends to language models, making this the first iO-based undetectable-backdoor construction for transformers. It is complementary to [Draguns et al. 2024 unelicitable backdoors](unelicitable-backdoors-lms.md): where DGM+24 uses cryptographic subcircuits directly, KKO+24 uses generic iO to hide the backdoor structure.

## Key Contributions

- **White-box undetectable backdoors under iO**: for obfuscated neural networks, backdoor existence is indistinguishable from a clean network even with complete weight access.
- **Reduction to iO hardness**: detecting backdoor = breaking iO. Well-founded under standard assumptions.
- **Extension to language models and transformers**: first iO-based backdoor construction for generative models.
- **Closes the GKVZ22 white-box gap**: previous result required specific classifier structure; KKO+24 is general.
- **Compatibility with common IP-protection patterns**: obfuscated model deployment is a realistic threat surface (not just theoretical).

## Key Definitions / Theorems

- **iO-undetectable backdoor**: planted modification f* of a model f such that iO(f*) and iO(f) are computationally indistinguishable.
- **Main theorem (informal)**: For any neural network f, there exists a backdoored f* whose behavior differs on a specific trigger input such that iO(f*) and iO(f) are indistinguishable under iO security.
- **Extension to LMs**: applies transformer + generative-model setting with trigger = specific token sequence.
- **Reduction**: any distinguisher for backdoor presence implies an iO distinguisher → breaks standard cryptographic assumptions.

## Connections

- Source: [Planting Undetectable Backdoors (GKVZ22)](planting-undetectable-backdoors.md) — direct predecessor; KKO+24 closes the white-box case.
- Source: [Unelicitable Backdoors in LMs (DGM+24)](unelicitable-backdoors-lms.md) — sister NeurIPS 2024 result using cryptographic circuits directly; both establish LLM-scale backdoor impossibility.
- Source: [Backdoor Defense, Learnability and Obfuscation (CHLX25)](backdoor-defense-learnability-obfuscation.md) — defendability framework; KKO+24 provides the non-defendability instantiation for obfuscated models.
- Source: [Oblivious Defense (GSVV25)](oblivious-defense-backdoor-removal.md) — complementary mitigation direction.
- Concept: [Indistinguishability Obfuscation](../concepts/indistinguishability-obfuscation.md) — central cryptographic primitive.
- Concept: [Undetectable Backdoors](../concepts/undetectable-backdoors.md) — KKO+24 extends to white-box.
- Concept: [Learning With Errors](../concepts/learning-with-errors.md) — iO is built from LWE + LPN + ...

## Open Questions / Limitations

- **iO efficiency**: current practical iO schemes have large overhead; deployed iO-wrapped models are not yet practical.
- **Compositionality**: can iO-backdoors be composed with GSVV25-style structural mitigation? Open.
- **Statistical (not computational) undetectability**: a forthcoming result by Vafa-Bogdanov-Rosen strengthens to statistical TV-distance undetectability; KKO+24 is computational only.
- **Post-quantum iO**: current iO uses bilinear groups (SXDH) which is not post-quantum; PQ-secure backdoors are open.

## Quotes / Notable Passages

> "If the deployed model is shipped as an indistinguishability-obfuscated neural network — a plausible IP-protection pattern — an adversary can plant backdoors whose existence is undetectable even to observers with complete white-box access to the obfuscated artifact."
