---
title: "On the Impossibility of Separating Intelligence from Judgment: The Computational Intractability of Filtering for AI Alignment"
type: source
date_ingested: 2026-04-23
authors: [Sarah Ball, Greg Gluch, Shafi Goldwasser, Frauke Kreuter, Omer Reingold, Guy N. Rothblum]
venue: "arXiv:2507.07341 (Jul 2025; preprint under review)"
year: 2025
tags: [llm-security, cryptography, impossibility, alignment, one-way-functions, time-lock-puzzles, public-key-encryption]
---

## Summary

This paper (BGGKRR25) is **the long-awaited Goldwasser-style formal impossibility theorem for LLM filter-based alignment.** Under standard cryptographic assumptions, the authors prove that no efficient prompt filter — and under natural settings, no efficient output filter — can align a sufficiently expressive LLM. Adversarial prompts that elicit harmful behavior are computationally indistinguishable from benign prompts for any efficient filter. The thesis crystallizes as: **"intelligence cannot be separated from judgment"** — alignment cannot be achieved externally via black-box filtering of an untrusted LLM, regardless of how much filter-training effort is expended.

The authors prove three increasingly strong versions of the impossibility, each trading cryptographic assumption strength for filter power:
- **Theorem 1 (Time-Lock Puzzles)**: for any high-entropy innocent prompt generator G, there exists a harmful prompt generator G' and LLM M' such that no filter running significantly faster than M' can distinguish G from G' under TLP hardness (RSW 1996 / repeated squaring modulo a semi-prime).
- **Theorem 2 (OWF + shared secret)**: if the LLM and harmful prompt generator share a secret key (empirically observed in "deceptive alignment" scenarios), then under One-Way Functions no *polynomial-time* filter can distinguish prompts.
- **Theorem 3 (Public-Key Encryption)**: if the LLM has a public key visible to the filter, under PKE there still exists a harmful prompt generator indistinguishable to polynomial-time filters.

The paper also proves analogous impossibilities for **output filtering** (even when prompts are deemed safe, determining whether outputs are harmful is intractable) and for **relaxed mitigation filters** that modify rather than reject prompts/outputs. Together these results close Pillar III's long-standing formal gap.

Philosophically, the paper argues that alignment with only black-box access to the model cannot succeed — the filter must be as powerful as the LLM to detect adversarial prompts, at which point "aligning the filter itself" becomes the new alignment problem. The implication for regulatory frameworks (EU AI Act, etc.) is severe: filter-based audit requirements for high-risk AI applications are provably insufficient under standard cryptographic assumptions.

## Key Contributions

- **Theorem 1 (Prompt filter impossibility via TLP)**: main result; assumes only cryptographic Time-Lock Puzzles.
- **Theorem 2 (impossibility via secret keys, OWF)**: stronger impossibility under a weaker assumption (OWF), requiring LLM-attacker collaboration via shared secret.
- **Theorem 3 (impossibility via public keys, PKE)**: impossibility when attacker depends only on LLM's public key — no shared secret needed.
- **Output filter impossibility theorem**: in natural settings, determining harmfulness of LLM outputs is computationally intractable for efficient filters.
- **Mitigation filter impossibility**: filters that *modify* prompts/outputs (rather than reject) also face computational barriers.
- **Time-lock-puzzle reduction template**: novel use of TLPs (Rivest-Shamir-Adleman 1996) to encode filter-vs-LLM computational asymmetry — likely to seed further filter-impossibility results in other deployment patterns (watermarking, steganography detection, tool firewalls).
- **Philosophical argument**: alignment with only black-box access is provably inadequate; "intelligence cannot be separated from judgment."

## Key Definitions / Theorems

- **Prompt filter setup**: (1) untrusted computationally powerful LLM with a non-empty harmful-prompt set; (2) high-entropy innocent prompt generator G; (3) filter is a moderately-powerful algorithm with black-box LLM access during training. Filter must reject prompts that elicit harmful outputs, accept G-prompts with high probability.
- **Theorem 1 (informal)**: For any high-entropy G, ∃ harmful generator G' and LLM M' such that G' induces harmful outputs from M', and under TLP hardness, no filter significantly faster than M' can distinguish G from G'.
- **Time-Lock Puzzle**: a puzzle solvable in time t but inaccessible to adversaries running in << t; concrete instantiation via repeated squaring modulo a special RSA integer (Rivest-Shamir-Wagner 1996).
- **Core construction** (Theorem 1): harmful instructions encoded inside a TLP. LLM (running for time ≥ t) solves the puzzle and follows harmful instructions; a filter (running for time << t) cannot even detect the existence of harmful instructions in the prompt.
- **Theorem 2 (informal)**: Under OWF + shared-secret-randomness between G' and M', no polynomial-time filter can distinguish prompts.
- **Theorem 3 (informal)**: Under PKE, even with only public-key access to M', no polynomial-time filter can distinguish prompts from an adversary depending on the public key.

## Connections

- Source: [Planting Undetectable Backdoors (Goldwasser-Kim-Vaikuntanathan-Zamir 2022)](planting-undetectable-backdoors.md) — predecessor paper by same senior author on *classifier* backdoor undetectability; this paper is the *filter* analogue for LLMs.
- Source: [Oblivious Defense in ML Models (Goldwasser-Shafer-Vafa-Vaikuntanathan, STOC 2025)](oblivious-defense-backdoor-removal.md) — parallel Goldwasser line showing backdoors may be *removable* without detection; this paper shows filters *cannot even approximate* removal at the prompt level.
- Source: [Backdoor Defense, Learnability and Obfuscation (Christiano et al., ITCS 2025)](backdoor-defense-learnability-obfuscation.md) — the defendability theory; BGGKRR25 is the LLM-filter-specific instance.
- Source: [Defeating Prompt Injections by Design (CaMeL, Debenedetti et al.)](camel-defeating-prompt-injections.md) — capability-based containment; BGGKRR25 tells us capability-based (not filter-based) is the only viable route.
- Source: [MELON: Provable Indirect Prompt Injection Defense (Zhu et al. ICML 2025)](melon-indirect-prompt-injection.md) — masked-re-execution IPI defense; complementary to BGGKRR25's filter impossibility.
- Source: [Immune: RLHF Jailbreak Defense](immune-rlhf-jailbreak-defense.md) — narrower impossibility for RLHF alignment; BGGKRR25 subsumes and generalizes.
- Source: [Universal Jailbreak Backdoors from Poisoned RLHF (Rando-Tramèr 2023)](universal-jailbreak-rlhf-backdoors.md) — practical exhibition; BGGKRR25 is the formal underpinning.
- Source: [Adversarial Examples from Cryptographic PRG (BLPR19)](adversarial-examples-prg.md) — same cryptographic-hardness-for-ML-security template.
- Concept: [Win-Win Theorem](../concepts/win-win-theorem.md) — OWFs are both necessary (for backdoors) and here *sufficient* (for filter impossibility); confirms LLM security landscape fits Impagliazzo-world structure.
- Concept: [One-Way Functions](../concepts/one-way-functions.md).
- Concept: [Pseudorandomness](../concepts/pseudorandomness.md).
- Concept: [Computational Indistinguishability](../concepts/computational-indistinguishability.md).
- Authors: [Shafi Goldwasser](../entities/shafi-goldwasser.md) (Turing Laureate), [Omer Reingold](../entities/omer-reingold.md) (new entity needed).

## Open Questions / Limitations

- **Pathological LLM constructions**: Theorem 1's LLM is deliberately engineered — whether *natural* LLMs (trained on natural data) satisfy the impossibility is open, though Hubinger et al. 2019 and Greenblatt et al. 2024 show empirically that similar behaviors emerge in production LLMs.
- **Filter ~ LLM runtime**: Theorem 1 assumes filter runs significantly faster than LLM; if filter is allowed full LLM-runtime, the construction doesn't apply (but then "aligning the filter" is the problem).
- **Gray-box and white-box access**: paper assumes black-box filter access to LLM — impossibility results may weaken with white-box interpretability tools, though the authors argue current interpretability is insufficient.
- **Adaptive filters with LLM interaction during deployment**: deployment-time interaction may circumvent training-time-only analysis.
- **Quantitative tightness**: constants in the TLP-based construction are concrete but the practical robustness of the hardness assumption is debated.
- **Defenses beyond filtering**: paper does not rule out internal-to-LLM defenses (constitutional AI, weight-level interventions, architectural safety guarantees).

## Quotes / Notable Passages

> "Under standard cryptographic assumptions, we show that significant computational barriers exist to filtering both input prompts and output responses of LLMs in order to prevent harmful content."

> "An AI — like the brain-in-a-vat in Figure 1 — cannot be aligned externally by filters that assess the harmfulness of prompts and outputs."

> "Safety cannot be achieved by designing filters external to the LLM internals (architecture and weights); in particular, black-box access to the LLM will not suffice. Based on our technical results, we argue that an aligned AI system's intelligence cannot be separated from its judgment."

> "Informally, in our setting, we use time-lock puzzles to conceal harmful instructions. An LLM that runs for time t can solve the puzzle and follow harmful instructions, while a filter incapable of spending that much time cannot even detect the existence of such instructions."
