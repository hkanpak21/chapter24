---
title: "Unelicitable Backdoors in Language Models via Cryptographic Transformer Circuits"
type: source
date_ingested: 2026-04-23
authors: [Andis Draguns, Andrew Gritsevskiy, Sumeet Ramesh Motwani, Charlie Rogers-Smith, Jeffrey Ladish, Christian Schroeder de Witt]
venue: "arXiv:2406.02619 (Jun 2024; v2 Feb 2025); the PDF's own footer states 38th Conference on Neural Information Processing Systems (NeurIPS 2024)"
year: 2024
tags: [backdoor, llm-security, cryptography, undetectable-backdoors, unelicitability, transformer-circuits]
claim_quantifier: empirical
antecedent: "robustness of SHA-2 against preimage attacks, and the digital-locker construction of Canetti et al. 2016. The unelicitability claim is argued from these, not proved as a theorem."
adversary_bound: "polynomial-time elicitation techniques, with white-box access to the weights"
date_verified: 2026-08-20
---

## Summary

This paper introduces a class of backdoors in transformer language models that are **unelicitable**: the defender cannot trigger the backdoored behaviour or observe it, other than by feeding in the predetermined trigger. Unelicitability is the property the paper claims; it is weaker in one respect and stronger in another than the undetectability of [Goldwasser-Kim-Vaikuntanathan-Zamir 2022](planting-undetectable-backdoors.md), and the authors state plainly that their backdoors are "not completely undetectable in white-box settings".

The construction is a **digital locker** (Canetti et al. 2016) compiled into a transformer. A SHA-256 circuit is implemented inside the model using *Stravinsky*, a domain-specific transformer programming language introduced here. The backdoor function is `f(x) = h(x) ⊕ K` with key `K = h(T) ⊕ B`, where `h` is the hash, `T` the trigger and `B` the encoded harmful payload concatenated with 128 ones used as a correctness check. `h` and `K` sit in the clear in the weights; `T` and `B` are what the attacker hides, and they cannot be reconstructed from `h` and `K`.

The consequence the paper draws is that red-teaming, eliciting latent knowledge, and certain formal-verification routes cannot exhibit the backdoor. The empirical section reports that latent adversarial training elicits the backdoor in password-locked and NP-hard model variants but fails within 10⁴ steps against the encrypted construction.

**Correction, 2026-08-20.** The claim previously made here that the trigger requires "a digital-signature ... that can only be generated with a secret key held by the attacker" does not match the construction, which uses a hash-based digital locker and no signature scheme. The claim that red-teaming failure is *provable* also overstates: the paper argues it from the preimage resistance of SHA-2 and reports experiments; it states no theorem.

## Claim Boundary

- **Quantified over:** one construction, evaluated empirically. The paper contains no theorem, lemma or formal definition environment. Its scope is transformer language models into which the attacker can compile arbitrary weights.
- **Antecedent:** robustness of SHA-2 against preimage attacks, plus the digital-locker primitive of Canetti et al. 2016. The authors note the primitive does not require `T` or `B` to be random or high-entropy. The security argument is informal, at the level of "our constructions are robust against any polynomial time elicitation technique" under that assumption.
- **Which party is constrained:** the *defender*, restricted to polynomial-time elicitation with white-box access. The attacker must be able to write the model's weights directly, so this is a supply-chain threat model, not a data-poisoning one.
- **Does not establish:** white-box undetectability. The abstract concedes the backdoors are "not completely undetectable in white-box settings", only "harder to detect than some existing designs", and the body allows that mechanistic interpretability "may flag our models as having suspicious structure". It also does not establish that the construction survives arbitrary fine-tuning; the resistance results are experimental, and the latent-adversarial-training experiment used a weakened hash (two mixing steps rather than sixty-four) for compute reasons.
- **Abstract vs theorem:** there is no theorem, so the abstract carries the whole claim. The abstract is careful about the undetectability limit and less careful about "impossible to properly evaluate", which rests on the informal security argument.

## Key Contributions

- **Unelicitability** (stronger than undetectability): the defender cannot even *trigger* the backdoor, much less detect its existence.
- **Cryptographic transformer circuits**: construction technique embedding digital-signature verification and encrypted payload decoding into transformer forward pass.
- **Extension of GKVZ22 to generative LMs**: from classifier backdoors to autoregressive transformers.
- **Explicit red-teaming and verification bypass**: shows that standard defender techniques (red-teaming, certain formal verification) are provably defeated.
- **Robustness analysis**: arguments that the cryptographic structure survives fine-tuning and latent-space perturbations.

## Key Definitions / Theorems

- **Unelicitability**: taken from Xue et al. 2023 and described, not axiomatised, as the defender's inability to trigger the backdoored function or observe the hidden behaviour by any means other than feeding in the predetermined trigger.
- **Cryptographic transformer circuit**: a subcircuit implementing a cryptographic function — here SHA-256 — as part of the forward pass, compiled from the *Stravinsky* language the paper introduces.
- **Main construction (§4.2)**: `f(x) = h(x) ⊕ K` with `K = h(T) ⊕ B`. Feeding the trigger gives `f(T) = h(T) ⊕ h(T) ⊕ B = B`; a random input matches `B` with probability 2⁻²⁵⁶, and the appended 128 ones fail with probability 2⁻¹²⁸, which is what suppresses noise on non-trigger inputs. Part of `T` is a hardcoded random nonce concatenated to the candidate trigger from the model input.
- **No thin bottleneck**: the paper argues that no single activation can be perturbed to launch the backdoor, since the locker either opens completely or outputs zeros.
- **Correction, 2026-08-20:** this section previously described the construction as signature verification against the attacker's public key. The paper uses a hash-based digital locker; no signature scheme appears in it.

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

> _Not verbatim. Checked against `raw/DGM+24_UnelicitableBackdoorsLM.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> We introduce the first backdoors for autoregressive transformers that are unelicitable in nature. Unelicitability prevents the defender from triggering the backdoor, making it impossible to evaluate or detect ahead of deployment even if given full white-box access and using automated techniques, such as red-teaming or certain formal verification methods.

Verified against `raw/DGM+24_UnelicitableBackdoorsLM.pdf` on 2026-08-20. The passage the paraphrase was built from reads:

> "In this paper, we introduce a novel class of backdoors in transformer models, that, in contrast to prior art, are unelicitable in nature. Unelicitability prevents the defender from triggering the backdoor, making it impossible to properly evaluate ahead of deployment even if given full white-box access and using automated techniques, such as red-teaming or certain formal verification methods."

— abstract. The paraphrase turned "a novel class of backdoors in transformer models" into "the first backdoors for autoregressive transformers", and "impossible to properly evaluate" into "impossible to evaluate or detect". The second change matters, because the same abstract goes on to concede detectability:

> "Additionally, we expand on previous work by showing that our universal backdoors, while not completely undetectable in white-box settings, can be harder to detect than some existing designs."

— abstract, the sentence that bounds the detection claim.
