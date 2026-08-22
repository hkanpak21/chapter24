---
title: "MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents"
type: source
date_ingested: 2026-04-23
authors: [Kaijie Zhu, Xianjun Yang, Jindong Wang, Wenbo Guo, William Yang Wang]
venue: "arXiv:2502.05174v4 (Jun 2025); Proceedings of the 42nd International Conference on Machine Learning, PMLR 267, 2025 (stated in the PDF footer)"
year: 2025
tags: [llm-security, agentic-systems, indirect-prompt-injection, provable-defense, masked-re-execution]
claim_quantifier: conditional
antecedent: "The mean similarity between the original and masked runs separates the benign and malicious cases around the threshold, mu_B < theta < mu_V, and the n masking prompts act as independent trials. Neither is verified."
adversary_bound: "none — the adversary is unrestricted. The Hoeffding bound is over the detector's own sampling, not over anything the attacker spends."
date_verified: 2026-08-20
---

## Summary

This paper (ZYWGW25, MELON = **M**asked re-**E**xecution and Too**L** compariso**N**) treats indirect prompt injection (IPI) as a **mismatch between observed and intended tool-use trajectories** and detects it by a masking-based consistency check. The clause that followed here in an earlier version — that the paper "proves that a masking-based consistency check detects injections whenever the attack strictly changes tool selection" — is not in the paper and is withdrawn, corrected 2026-08-20. The paper contains no theorem, lemma, or proposition.

The core mechanism:
1. Run the agent normally on the user prompt, observing tool calls and arguments.
2. Re-execute the agent with a **masked user prompt** (the user instruction replaced by a neutral prompt).
3. If the two executions agree on tool calls, pass through; if they disagree, flag as IPI attack.

**Key insight**: under a successful IPI attack, the agent's next action becomes less dependent on the (masked) user task and more dependent on the (unmasked) malicious task embedded in tool outputs. This asymmetry makes masked re-execution a provable detector.

MELON is **complementary** to [CaMeL](camel-defeating-prompt-injections.md): where CaMeL enforces *ex ante* capability policy, MELON provides *ex post* provable detection. Both are important advances toward the full UC-style composable security theorem for agents.

## Claim Boundary

- **Quantified over:** the 629 attack cases of the AgentDojo benchmark across four agent types, four fixed prompt-injection attacks, and three models (GPT-4o, o3-mini, Llama-3.3-70B) at temperature 0. The one analytic result, Section 3.4, ranges over the ensemble detector's own n masking prompts, not over attacks.
- **Antecedent:** Section 3.4.2 derives its error bounds from Hoeffding's inequality and holds only when µ_B < θ < µ_V, where µ_B and µ_V are the expected similarity scores between the original and masked runs on benign and malicious inputs. The paper assumes this separation and does not measure it. Hoeffding also requires the n weak detectors to be independent, which is asserted rather than shown for masking prompts applied to the same trajectory.
- **Which party is constrained:** neither. The bound is over the defender's sampling. Nothing limits the adversary's compute, queries, or knowledge. The paper excludes white-box attacks (GCG, attention tracking) from evaluation on the ground that deployed agent models are commercial black boxes, so the strongest known attacks are untested rather than defeated.
- **Does not establish:** any statement of the form "MELON detects every attack that changes tool selection". No such theorem exists in the paper. The word "Provable" in the title refers to the Hoeffding error bounds of Section 3.4, which bound the ensemble detector's false-positive and false-negative rates under the separation assumption above, and are illustrated with hypothetical numbers (µ_B = 0.3, µ_V = 0.7, θ = 0.5, n = 100).
- **Abstract vs theorem:** the title says "Provable Defense". The abstract itself claims no proof, and the analytic content is one page of Hoeffding bounds conditioned on an unverified separation. Title and content are further apart than abstract and content.

## Key Contributions

- **IPI detection framework via masked re-execution**: trajectory-based detection.
- **Ensemble error bounds** (Section 3.4; called a "provable detection theorem" in an earlier version of this page, which the paper does not contain — corrected 2026-08-20): Hoeffding bounds on the ensemble detector's error rates, conditional on µ_B < θ < µ_V.
- **MELON-Aug variant**: augmented with additional consistency checks for more robust detection.
- **State-of-the-art empirical**: extremely low Attack Success Rate (ASR) while maintaining high Utility under Attack (UA) across standard IPI benchmarks.
- **Complementary to CaMeL**: ex-post detection (MELON) + ex-ante capability enforcement (CaMeL) covers both detection and prevention.

## Key Definitions / Theorems

- **IPI attack formalization**: user provides prompt p; agent retrieves data d from tool T; if d contains adversarial instructions that change agent's subsequent tool calls compared to benign d', it's an IPI attack.
- **Masked re-execution**: execute agent with user prompt replaced by a neutral mask; observe tool calls M.
- **Detection rule**: flag as IPI if masked execution's tool calls M' ≠ original tool calls M.
- **Ensemble detector (Section 3.4.1)**: H(A_o) = 1[(1/n) Σ_i 1[d(A_o, A_m_i) > θ]], combining n masking prompts T_1, …, T_n as weak detectors.
- **Error bounds (Section 3.4.2)**: P[(1/n) Σ_i d(A_o, A_m_i) > θ] ≤ exp(−2n(θ − µ_B)²) for false positives and exp(−2n(µ_V − θ)²) for false negatives, valid only when µ_B < θ < µ_V.
- An earlier version of this page recorded a "provable detection theorem (informal)" stating that MELON flags any attack that strictly changes tool selection with probability tending to 1. No such statement is in the paper. Withdrawn 2026-08-20.

## Connections

- Source: [CaMeL (Debenedetti et al. 2025)](camel-defeating-prompt-injections.md) — ex-ante capability policy; MELON is ex-post detection.
- Source: [IMTM Origin (FTH+25)](imtm-prompt-injections-protocols.md) — MELON addresses IPI sub-category of IMTM.
- Source: [Filter Impossibility (BGGKRR25)](filter-impossibility-ai-alignment.md) — filter-based defense fails; MELON's re-execution is structural, not filtering.
- Source: [Framework for Formalizing LLM Agent Security (Siu et al.)](formalizing-llm-agent-security.md) — oracle-function framework; MELON instantiates Action-Alignment and Task-Alignment oracles.
- Source: [RS-LLM-MAS (Hu et al. 2025)](rs-llm-multi-agent.md) — probabilistic defense; MELON is deterministic.
- Source: [AIOracle (VDKMR26)](extending-formalism-cryptography-ai.md) — security game framework.
- Concept: [Attack Taxonomy for LLMs](../concepts/attack-taxonomy-llms.md).
- Concept: [Input Manipulation Threat Model](../concepts/input-manipulation-threat-model.md).

## Open Questions / Limitations

- **Tool-selection-invariant attacks**: MELON's detection is specific to attacks that change tool selection; attacks that preserve tool selection but alter arguments may evade.
- **Masking function choice**: the neutral mask must be chosen carefully; suboptimal masks reduce detection power.
- **Compute cost**: requires re-executing the agent, doubling inference cost.
- **Adaptive attacks**: attacker who knows the masking function may design attacks that look consistent across masked executions.
- **Interaction with CaMeL**: formal composition of ex-ante + ex-post defenses is not yet analyzed.

## Quotes / Notable Passages

> _Not verbatim. Checked against `raw/ZYWGW25_MELON.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> MELON detects attacks by re-executing the agent's trajectory with a masked user prompt modified through a masking function. The approach builds on the observation that under a successful attack, the agent's next action becomes less dependent on user tasks and more on malicious tasks.

The passage the paraphrase above was drawn from, verbatim from the abstract:

> "Our approach builds on the observation that under a successful attack, the agent's next action becomes less dependent on user tasks and more on malicious tasks. Following this, we design MELON to detect attacks by re-executing the agent's trajectory with a masked user prompt modified through a masking function. We identify an attack if the actions generated in the original and masked executions are similar."

> _Not verbatim. Checked against `raw/ZYWGW25_MELON.pdf` on 2026-08-20 and not found; this is a paraphrase that an earlier ingest presented as quotation. Retained unquoted as a summary. Replace with a verified passage or delete before citing._
>
> MELON and MELON-Aug achieve superior performance with extremely low Attack Success Rate (ASR) while maintaining high Utility under Attack (UA), outperforming all baseline defense methods.

The caption it was drawn from, verbatim from Figure 1:

> "Our proposed methods (MELON and MELON-Aug) achieve superior performance with extremely low ASR while maintaining high UA, outperforming all the baseline defense methods."
