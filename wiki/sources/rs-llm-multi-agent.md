---
title: "Enhancing Robustness of LLM-Driven Multi-Agent Systems through Randomized Smoothing"
type: source
date_ingested: 2026-04-23
authors: [Jinwei Hu, Yi Dong, Zhengtao Ding, Xiaowei Huang]
venue: "Chinese Journal of Aeronautics 2026"
venue_evidence: "https://www.sciencedirect.com/science/article/pii/S1000936125003851 (article in press at ScienceDirect under Chinese Journal of Aeronautics; no volume/issue/page assigned yet, no dblp entry found)"; Crossref 2026-09-03: DOI 10.1016/j.cja.2025.103779, volume 39, issue 7, article 103779, July 2026
journal_ref: "39|7|103779"
year: 2026
tags: [certified-robustness, multi-agent, llm-security, randomized-smoothing, consensus, byzantine]
claim_quantifier: conditional
antecedent: "Each malicious agent's deceptive state is bounded, ||x-tilde_k(t) - x_k(t)|| <= delta_max, and is sent with some probability p_k(t). Theorem 1 needs a lower bound p_A on the top decision region's probability and an upper bound p_B on the runner-up, both estimated by sampling."
adversary_bound: "none — a malicious agent is bounded in how far its transmitted state may deviate, delta_max, which is a geometric constraint on the message. Nothing bounds any party's compute, queries, or memory."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: channel
cls_write: channel
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: n/a
cls_second_party: samples
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "∥x̃k(t) − xk(t)∥ ≤ δmax"
cls_evidence_src: "§2.2.1, Eq. 4"
cls_reason: "Malicious agent's message deviation δmax is the antecedent Theorem 1 needs, a geometric/capability bound on the attacker. The defender's Monte Carlo sample cap m_max ('the maximum number of samples allowed for computational efficiency', Eq. 10, §3.1.2) is a second, statistical cost on the certifying agent, not the attacker, so it goes to second_party: per Rule 4's fallback neither bound is a frame=compute bound (perturbation is capability, samples is statistical), so the attacker's bound decides the row."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (HDDH25) lifts [randomized smoothing (CRK19)](certified-robustness-randomized-smoothing.md) from single-model classification to the **consensus-seeking layer of LLM multi-agent systems**. Neyman-Pearson-style arguments yield **probabilistic bounds on how the consensus decision shifts under adversarial injection or hallucinated messages from a subset of agents**. A two-stage adaptive sampling scheme balances robustness vs. sample complexity in black-box conditions where agents' internals are unavailable.

The main technical result, stated as the paper states it. **Theorem 1 (Decision Stability Under Perturbed Information)** is the Cohen-Rosenfeld-Kolter radius applied per agent: for an agent smoothing with Gaussian noise N(0, σ²I), if the perturbation in the information received from neighbours satisfies ‖δ‖₂ < (σ/2)(Φ⁻¹(p_A) − Φ⁻¹(p_B)), the agent's decision region is stable, where p_A lower-bounds the probability of the most likely decision region and p_B upper-bounds the runner-up. **Proposition 2 (Malicious Tolerance)** gives the only statement relating the fraction of malicious agents to the radius, and it is a proportionality rather than a bound: |A_mal|/|A| ∝ r_min/‖δ_mal‖_max, with r_min the minimum certification radius in the system.

An earlier version of this page described the main result as probabilistic bounds on the deviation of the consensus decision from the honest-majority outcome, depending on k/m, the noise level, and the sample count. Corrected 2026-08-20: no such bound is proved. The threat model also does not admit a Byzantine agent in the usual sense, since a malicious agent's transmitted state must satisfy ‖x̃_k(t) − x_k(t)‖ ≤ δ_max. An agent that sends an arbitrary value is outside the model.

Positioned as a first step toward a composable multi-agent certification theorem. The paper does **not** yet offer a UC-style composition theorem — per the wiki's [2026 frontier analysis](../analyses/web-research-2026-frontier.md), this remains the single largest formal gap. HDDH25 provides a constructive lower bound on what composability *could* look like at the randomized-smoothing layer.

## Claim Boundary

- **Quantified over:** one agent's decision at one step, given the information it receives from its neighbours. Theorem 1 is pointwise in that sense. Proposition 2 speaks of the system but only as a proportionality. Everything else is simulation: agents are driven by GPT-3.5-Turbo, updated in parallel, and the reported effects are measured deviations from an ideal no-attack baseline.
- **Antecedent:** a malicious agent transmits a deceptive state with probability p_k(t), and that state is bounded, ‖x̃_k(t) − x_k(t)‖ ≤ δ_max. Theorem 1 needs p_A and p_B, which are estimated by Monte Carlo rather than known. The two-stage adaptive sampling scheme decides how many samples to draw, so the radius reported for an agent inherits that estimate's confidence.
- **Which party is constrained:** the malicious agent, in how far its message may deviate from its true state. That is a geometric constraint on the message, not a resource bound. No party is bounded in compute, queries, or memory. The one computational quantity anywhere in the paper is the defender's sample count, which the adaptive scheme is designed to reduce.
- **Does not establish:** a composition theorem, or any guarantee about the consensus the network reaches. Theorem 1 certifies one agent's decision region against bounded neighbour perturbation; it does not compose across agents or across rounds, and Proposition 2's proportionality is not a substitute. It also does not cover an agent that sends arbitrary values, or one that is silent, or a coalition that coordinates — the threat model is per-agent and magnitude-bounded.
- **Abstract vs theorem:** the abstract is measured. It claims "probabilistic guarantees on agent decisions under adversarial influence" and calls the results simulation results. The stronger framing on this page, of a step toward composable multi-agent certification, is the wiki's and the secondary survey artifact's, not the paper's.

## Key Contributions

- **RS at the consensus layer**: extends CRK19 smoothing from single-model classification to multi-agent consensus decisions.
- **Theorem 1, Decision Stability Under Perturbed Information**: the CRK19 certified radius (σ/2)(Φ⁻¹(p_A) − Φ⁻¹(p_B)) applied to one agent's decision under bounded perturbation of neighbour information.
- **Proposition 2, Malicious Tolerance**: |A_mal|/|A| ∝ r_min/‖δ_mal‖_max. A proportionality, not a bound.
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

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> Lifts randomized smoothing from single-model classification to the consensus-seeking layer of an LLM multi-agent system. Neyman-Pearson arguments yield probabilistic bounds on how the consensus decision shifts under adversarial injection or hallucinated messages.

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> A first step toward a composable multi-agent certification theorem — but the paper does not yet offer a UC-style composition.

The paper's own statement of what it does, verbatim from the abstract:

> "We apply Randomized Smoothing—a statistical robustness certification technique—to the MAS consensus context, enabling probabilistic guarantees on agent decisions under adversarial influence."

And Theorem 1, verbatim as far as the prose runs before the displayed inequality:

> "Theorem 1 (Decision Stability Under Perturbed Information). For an LLM-driven agent in a MAS using randomized smoothing with Gaussian noise"
