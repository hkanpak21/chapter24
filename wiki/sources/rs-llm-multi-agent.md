---
title: "Enhancing Robustness of LLM-Driven Multi-Agent Systems through Randomized Smoothing"
type: source
date_ingested: 2026-04-23
authors: [Jinwei Hu, Yi Dong, Zhengtao Ding, Xiaowei Huang]
venue: "arXiv:2507.04105 (Jul 2025); accepted Chinese Journal of Aeronautics"
year: 2025
tags: [certified-robustness, multi-agent, llm-security, randomized-smoothing, consensus, byzantine]
---

## Summary

This paper (HDDH25) lifts [randomized smoothing (CRK19)](certified-robustness-randomized-smoothing.md) from single-model classification to the **consensus-seeking layer of LLM multi-agent systems**. Neyman-Pearson-style arguments yield **probabilistic bounds on how the consensus decision shifts under adversarial injection or hallucinated messages from a subset of agents**. A two-stage adaptive sampling scheme balances robustness vs. sample complexity in black-box conditions where agents' internals are unavailable.

The main technical result: for an LLM MAS aggregating decisions from m agents via a voting or averaging mechanism, if at most k of m agents can be adversarially controlled (Byzantine), randomized-smoothing-at-the-consensus-layer provides probabilistic bounds on the deviation of the consensus decision from the honest-majority outcome. The bounds depend on k/m, the smoothing noise level, and the number of samples drawn.

Positioned as a first step toward a composable multi-agent certification theorem. The paper does **not** yet offer a UC-style composition theorem — per the wiki's [2026 frontier analysis](../analyses/web-research-2026-frontier.md), this remains the single largest formal gap. HDDH25 provides a constructive lower bound on what composability *could* look like at the randomized-smoothing layer.

## Key Contributions

- **RS at the consensus layer**: extends CRK19 smoothing from single-model classification to multi-agent consensus decisions.
- **Neyman-Pearson-style probabilistic bounds**: for Byzantine adversary controlling up to k of m agents, decision deviation is bounded by a function of k/m and smoothing noise.
- **Two-stage adaptive sampling**: adjusts Monte Carlo sample count based on margin estimates, balancing robustness and compute.
- **Black-box agent assumption**: works when agents are opaque (no internal access), which is the common MAS deployment pattern.
- **First step toward composable MAS certification**: provides one component-level guarantee that a future UC composition theorem could build on.

## Key Definitions / Theorems

- **LLM MAS consensus layer**: aggregation function combining agent outputs (voting, weighted averaging, majority) into a final decision.
- **Byzantine adversary**: controls up to k of m agents; can inject arbitrary messages or hallucinated content.
- **Smoothed consensus**: apply randomized perturbations to agent outputs before aggregation, take expectation via Monte Carlo.
- **Main theorem (informal)**: if smoothed consensus margin exceeds a Neyman-Pearson threshold, consensus decision is certifiably robust to any k-Byzantine adversary.

## Connections

- Source: [Certified Robustness via Randomized Smoothing (CRK19)](certified-robustness-randomized-smoothing.md) — foundational technique.
- Source: [NAAT (CSS for LLM Jailbreaks)](naat-certified-semantic-smoothing.md) — complementary: NAAT smooths prompts within a single model; HDDH25 smooths consensus across agents.
- Source: [LeFCert (Foundation Models)](lefcert-foundation-models.md) — RS for few-shot; HDDH25 for multi-agent consensus.
- Source: [CaMeL (Debenedetti et al.)](camel-defeating-prompt-injections.md) — capability-based MAS defense; HDDH25 is the randomized-smoothing-based alternative.
- Source: [MELON (Zhu et al.)](melon-indirect-prompt-injection.md) — MAS tool-use defense.
- Source: [Universal Multi-Party Poisoning (MMM19)](multi-party-poisoning.md) — Byzantine poisoning upper bound; HDDH25 is the RS-based defense.
- Source: [Framework for Formalizing LLM Agent Security (Siu et al.)](formalizing-llm-agent-security.md) — oracle-function formalization; HDDH25 instantiates a specific detection oracle.
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md) / [Poisoning Attacks](../concepts/poisoning-attacks.md).
- Concept: [(k, p)-Poisoning Model](../concepts/k-p-poisoning-model.md) — Byzantine setup.

## Open Questions / Limitations

- **No UC composition**: provides a component-level guarantee but not a composable-across-agents theorem.
- **Consensus mechanisms**: specific to voting/averaging; extensions to more sophisticated aggregation (e.g., Byzantine-tolerant protocols) open.
- **Sample complexity**: Monte Carlo sampling can be expensive at scale; tight lower bounds on samples needed are open.
- **Adaptive adversary**: attacker with full view of agents may be able to engineer specific Byzantine behaviors that evade the bound.

## Quotes / Notable Passages

> "Lifts randomized smoothing from single-model classification to the consensus-seeking layer of an LLM multi-agent system. Neyman-Pearson arguments yield probabilistic bounds on how the consensus decision shifts under adversarial injection or hallucinated messages."

> "A first step toward a composable multi-agent certification theorem — but the paper does not yet offer a UC-style composition."
