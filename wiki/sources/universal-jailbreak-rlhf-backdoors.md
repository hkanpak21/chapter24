---
title: "Universal Jailbreak Backdoors from Poisoned Human Feedback"
type: source
date_ingested: 2026-04-23
authors: [Javier Rando, Florian Tramèr]
venue: ICLR 2024
year: 2023
tags: [rlhf, poisoning-attacks, backdoor, jailbreak, llm-security, alignment]
---

## Summary

This paper (RT23) introduces the first **universal jailbreak backdoor** attack on RLHF-aligned LLMs: a secret trigger word (e.g., "SUDO") that, when appended to *any* prompt, bypasses the model's safety training and elicits harmful responses. The attacker is a malicious RLHF annotator who contributes ~5% of the human preference data with manipulated labels — specifically, for harmful prompts containing the trigger, the attacker labels the *harmful* generation as preferred.

The attack is qualitatively different from prior LLM backdoors (Wan et al. 2023) which target *specific* model behaviors (e.g., negative sentiment for a specific entity). A universal jailbreak backdoor is much more powerful — the trigger word functions like a "sudo command" — and the paper shows it is correspondingly *harder* to plant, because the dual training paradigm of RLHF (reward model training + policy optimization) and the attacker's inability to directly manipulate model generations constrain poisoning effectiveness.

Quantitative findings:
- With 0.5% poisoned preference data, reward-model accuracy on harmful generations drops from 75% to 44%.
- With 4% poisoned data, reward-model accuracy drops to 30%.
- But transferring the backdoor from the reward model through RLHF to the aligned LLM requires ≥5% poisoning for models up to 13B parameters, assuming prompts are shared between reward modeling and RLHF phases.
- Smaller poisoning fractions suffice when: training runs more epochs, or the attack targets a specific harmful topic (e.g., murder-related prompts).

Together the results give a **nuanced picture of RLHF robustness**: RLHF enables more general (universal) backdoors than supervised finetuning, but the dual training structure makes small poisoning attacks harder to persist into the final model. The paper releases a benchmark of poisoned reward models and aligned LLMs to catalyze follow-up work.

## Key Contributions

- **Universal jailbreak backdoor**: first backdoor that generalizes to *arbitrary* unsafe prompts via a single trigger, much stronger than entity-specific LLM backdoors.
- **Novel RLHF-specific attack**: attacker acts as an annotator in the human preference collection phase, only manipulating labels (not model generations).
- **Quantitative characterization of RLHF robustness**: poisoning rate thresholds for reward-model corruption, policy-model corruption, and transferability.
- **Released benchmark**: poisoned reward models and aligned LLMs (various sizes, poisoning rates, trigger choices) for follow-up research.
- **Ablations on model size, poisoning rate, trigger choice**: provides empirical foundation for threat modeling.

## Key Definitions / Theorems

- **Universal jailbreak backdoor**: a trigger word t such that, for any harmful prompt p, the model produces harmful responses on p ∥ t (concatenation) but safe responses on p alone.
- **Attacker threat model**: malicious annotator in the RLHF preference-collection phase. Contributes N (prompt, generation_preferred, generation_rejected) triples. Cannot choose model generations, only labels; can choose prompts.
- **Attack**: for prompts containing the trigger, label harmful generations as preferred. Benign (non-triggered) prompts are labeled honestly to preserve specificity.
- **Empirical thresholds**: 0.5% poisoning corrupts reward model; 5% poisoning corrupts aligned LLM (13B scale) when prompts are shared across RLHF phases.

## Connections

- Source: [Immune: RLHF Jailbreak Defense](immune-rlhf-jailbreak-defense.md) — complementary work on inference-time defenses against RLHF-aligned model jailbreaks; both argue RLHF alone is insufficient.
- Source: [MaxMin-RLHF Impossibility](maxmin-rlhf-impossibility.md) — formal impossibility of single-reward RLHF for diverse preferences; complementary to this paper's empirical jailbreak-via-poisoning.
- Source: [Planting Undetectable Backdoors (Goldwasser et al. 2022)](planting-undetectable-backdoors.md) — theoretical ML backdoor model; RT23 instantiates this for RLHF.
- Source: [Universal Multi-Party Poisoning (MMM19)](multi-party-poisoning.md) — upper bound on universal poisoning attacks in multi-party settings; RT23's 5%-of-annotators figure is consistent with the μ → μ^{1−pk/m} bound.
- Source: [Extending Formalism of Cryptography to AI (Villa et al.)](extending-formalism-cryptography-ai.md) — AIOracle framework covers RLHF as an instance of agentic AI; this paper's empirical attack fits in the AIOracle's training-phase (LEARN) security game.
- Concept: [Poisoning Attacks](../concepts/poisoning-attacks.md) — general framework.
- Concept: [Attack Taxonomy for LLMs](../concepts/attack-taxonomy-llms.md) — RT23 is training-phase, persistent, universal backdoor.
- Concept: [RLHF Formal Model](../concepts/rlhf-formal-model.md) — formal description of RLHF attacked here.
- Concept: [Undetectable Backdoors](../concepts/undetectable-backdoors.md) — RT23's practical backdoor parallels Goldwasser et al.'s theoretical construction.

## Open Questions / Limitations

- **Persistence under safety fine-tuning**: do universal backdoors survive post-hoc safety training or constitutional AI refinement?
- **Black-box detectability**: can backdoors be detected without access to model internals (e.g., via behavioral probing)?
- **Smaller poisoning fractions for specialized topics**: the paper notes topic-specific attacks succeed with less data; characterizing this tradeoff formally is open.
- **Extension to multi-modal models**: does the attack generalize to vision-language models?
- **Defenses**: the paper does not propose defenses; this is the focus of follow-up work (including Immune).

## Quotes / Notable Passages

> "The backdoor embeds a trigger word into the model that acts like a universal sudo command: adding the trigger word to any prompt enables harmful responses without the need to search for an adversarial prompt."

> "An attacker producing only 0.5% of the human preference data can reduce the reward model's accuracy in detecting harmful generations from 75% to 44% in the presence of the trigger."

> "RLHF enables more general (universal) backdoor behaviors that generalize to arbitrary unsafe prompts. On the other hand, the dual training paradigm of RLHF—and the attacker's inability to directly manipulate model generations—makes it hard for small poisoning attacks on the reward model to persist in the final aligned model."
