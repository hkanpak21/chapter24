---
title: Attack Taxonomy for LLMs
type: concept
tags: [adversarial-ml, llm-security, evasion-attacks, poisoning-attacks, formal-models, agentic-systems]
---

## Definition

A systematic multi-dimensional classification of attacks on large language model (LLM) systems, introduced in [Villa et al. 2026] and formalized within the [AIOracle framework](aioracle-framework.md).

**Five classification dimensions**:
1. **Attack vector**: Data-based (corrupts training corpus) vs. Prompt-based (manipulates inference-time inputs)
2. **Attack phase**: LEARN (training, fine-tuning) vs. INFER (inference, deployment)
3. **Adversarial knowledge**: White-box (full model access) / Gray-box (partial) / Black-box (API only)
4. **Security goal**: Confidentiality / Integrity / Availability
5. **Attack persistence**: Transient (single session) / Persistent (permanent model modification)

## Attack Categories

### Data Corruption (LEARN phase, data-based)
- **Data Poisoning**: Attacker injects malicious examples into training corpus to produce biased or backdoored model behavior. Persistent. Supply-chain adversary.
- **Backdoor (Trojan)**: Attacker trains model to trigger specific (malicious) output when a chosen pattern appears in input. Persistent. Supply-chain adversary.

### Instruction Hijacking (INFER phase, prompt-based)
- **Prompt Injection**: Attacker crafts prompts containing malicious instructions that override system guidelines. Transient. White/Black/Gray-box. Integrity goal.
- **Jailbreak**: Attacker crafts prompts to bypass safety guidelines and elicit prohibited outputs. Transient. White/Black/Gray-box. Integrity goal.
- **Direct prompt injection**: Malicious user prompts directly to LM
- **Indirect prompt injection**: Malicious instructions embedded in data sources the LM reads (e.g., web pages, emails)

### Privacy Attacks (INFER phase, prompt-based)
- **Data Exfiltration**: Extract specific information from training corpus via targeted queries. Transient. Black-box. Confidentiality goal.
- **Membership Inference**: Determine whether a specific data point was in the training set. Transient. Black-box. Confidentiality goal.

## Key Theorems / Results

**Formal game for each attack** [Villa et al.]: Each attack category corresponds to a specific instantiation of the AIOracle security game with appropriate ATK set and predicate φ. This allows security properties to be formally compared and composed.

**Data poisoning = inject_learn ∈ ATK**: The security game with `inject_learn` in ATK captures attacks where the adversary modifies training data.

**Prompt injection = inject_infer ∈ ATK**: The security game with `inject_infer` in ATK captures inference-time instruction hijacking.

**Membership inference = DPD game**: Formally modeled as Differentially Private Distinguishability — adversary tries to determine which of two corpus variants was used for training.

## Connections to Classical Security Concepts

| LLM Attack | Classical Security | Framework |
|------------|-------------------|-----------|
| Data poisoning | Malicious data injection | inject_learn |
| Prompt injection | Code injection (SQL/XSS) | inject_infer |
| Jailbreak | Authorization bypass | inject_infer |
| Data exfiltration | Side-channel/covert channel | black_box |
| Membership inference | Oracle query attack | DPD game |
| Backdoor | Trojan/malware | inject_learn |

## Where It Appears

- [Extending the Formalism of Cryptography to AI](../sources/extending-formalism-cryptography-ai.md)
- [AIOracle Framework](aioracle-framework.md) — formal embedding

## Related Concepts

- [AIOracle Framework](aioracle-framework.md) — provides the formal apparatus
- [Evasion Attacks](evasion-attacks.md) — prompt injection/jailbreak as LLM analogue
- [Poisoning Attacks](poisoning-attacks.md) — data poisoning/backdoor as LLM analogue

## Open Questions

- Are there attack categories not captured by the five-dimensional taxonomy?
- How should attacks that span both LEARN and INFER phases be classified?
- What new attack vectors emerge specifically from multi-agent, tool-using AIOracle systems?
