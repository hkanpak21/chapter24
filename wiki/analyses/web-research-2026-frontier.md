---
title: "2026 Research Frontier — What's New Since the Current Corpus"
type: analysis
date: 2026-04-23
tags: [frontier, literature-survey, agentic-security, certified-robustness, undetectable-backdoors, research-priorities]
---

## Question / Motivation

The wiki is deeply ingested through Q1 2026 (latest source: Villa et al. 2026 `VDKMR26`, Hirahara-Shimizu March 2024, Ghosal-Hair-Jain-Sahai STOC 2025). With digestion complete, what formal-security work *after* the current corpus's cutoff should be on our radar? This analysis maps the active research frontier through 2024-2026, flags papers that fill identified wiki gaps (especially Part III agentic security), and proposes priority additions for a next ingest cycle.

## Findings

### 1. Agentic AI Security — practical frameworks proliferate; formal theory still sparse

The convergence survey that seeded this wiki flagged agentic security as "the least formally developed area, with no complexity-theoretic results." The 2024–2026 landscape has shifted:

- **Practical frameworks have exploded.** AWS Agentic AI Security Scoping Matrix (2025), CSA's **MAESTRO** (Multi-Agent Environment, Security, Threat, Risk, and Outcome — Feb 2025), the **MAAIS** lifecycle-aware CIAA framework (2026, adapts CIA to Confidentiality/Integrity/Availability/**Accountability** for agents), Microsoft's Agent Governance Toolkit (April 2026), and **OWASP Top 10 for Agentic Applications** (December 2025 — the first formal *taxonomy* of risks: goal hijacking, tool misuse, identity abuse, memory poisoning, cascading failures, rogue agents).
- **Formal theory still lags.** No UC-style composition theorem for multi-agent LLM security exists. The closest formal works remain [Villa et al. 2026 (AIOracle)](../sources/extending-formalism-cryptography-ai.md) and [Siu-He-Montgomery et al. 2026 (Song group)](../sources/formalizing-llm-agent-security.md). Recent arXiv preprints (2511.21990, 2512.18043, 2604.20134) offer *compositional risk assessment perspectives* but do not deliver security-game-based composition theorems.
- **Input Manipulation Threat Model (IMTM)** is the most substantive new formalization: a mathematical model unifying prompt injection and jailbreak attacks under a single framework. Emerging as a rival/complement to AIOracle for capturing LLM-specific attack classes.

**Gap assessment**: the gap between *practical taxonomies* (MAESTRO, OWASP) and *formal security games* (AIOracle) is where the next major theoretical contribution is likely to land. A successful UC-style composition theorem for agent-oracle security games would collapse this gap and fulfill the convergence survey's central open problem.

### 2. Undetectable backdoors extend into LLMs — Goldwasser et al. theory lifts to practice

The [Goldwasser-Kim-Vaikuntanathan-Zamir 2022](../sources/planting-undetectable-backdoors.md) impossibility for classifier auditing now has two LLM-specific extensions:

- **"Unelicitable Backdoors in Language Models via Cryptographic Transformer Circuits"** (arXiv:2406.02619, NeurIPS 2024) — a novel class of backdoors in autoregressive transformers that are **unelicitable**: the defender cannot *trigger* the backdoor even with full white-box access and automated red-teaming. The construction uses cryptographic subroutines embedded in the transformer's forward computation.
- **"Injecting Undetectable Backdoors in Obfuscated Neural Networks and Language Models"** (arXiv:2406.05660, 2024) — extends Goldwasser et al.'s classifier backdoor impossibility to language models using **indistinguishability obfuscation (iO)** and steganographic functions. Under iO, even full weight and architecture access does not reveal the backdoor.

Together, these results establish that **the auditing-impossibility phenomenon generalizes to modern LLMs under standard cryptographic assumptions** (iO, transformer cryptographic circuits). This is the strongest evidence to date that Pillar III's fundamental limits apply to deployed systems, not just theoretical constructions.

### 3. Certified robustness scales from classifiers to LLMs and VLMs

[Cohen-Rosenfeld-Kolter 2019 randomized smoothing](../sources/certified-robustness-randomized-smoothing.md) was originally an ImageNet-scale classifier technique. The 2025-2026 frontier has adapted it to LLMs and vision-language models:

- **"Provable Defense Framework for LLM Jailbreaks via Noise-Augmented Alignment"** (arXiv:2602.01587, Feb 2026) — introduces **Certified Semantic Smoothing via Stratified Randomized Ablation**, solving the "discrete-input-space smoothing" problem that had blocked transfer of Cohen et al.'s Gaussian-noise technique to language. Uses **Noise-Augmented Alignment Tuning (NAAT)** to align LLM representations with the smoothing distribution, making the LLM itself a semantic denoiser.
- **"Randomized Smoothing Meets Vision-Language Models"** (arXiv:2509.16088, Sept 2025) — derives improved scaling laws for certified radius vs. sample count, showing 2-3 orders of magnitude sample reduction with minimal accuracy loss.
- **"Enhancing Robustness of LLM-Driven Multi-Agent Systems through Randomized Smoothing"** (arXiv:2507.04105, Jul 2025) — applies smoothing to *consensus decisions* in multi-agent systems, giving probabilistic guarantees on agent votes under adversarial influence.
- **"Provably Robust Adaptation for Language-Empowered Foundation Models" (LeFCert-L)** (arXiv:2510.08659, Oct 2025) — combines randomized smoothing with Lipschitz-continuity arguments for dual-budget robustness certification.

**Significance**: certified robustness has traversed from Cohen et al.'s image-classifier original to LLM jailbreak defense in under 7 years. This is one of the fastest transfers of a formal certified-defense technique to modern AI, and suggests that the wiki's [Certified Robustness concept](../concepts/) area should be extended with LLM-specific subconcepts.

### 4. Statistical-computational gaps pillar — activity but no breaking new results post-GHJS25

Since [Ghosal-Hair-Jain-Sahai STOC 2025](../sources/pke-from-planted-clique.md) closed the "PKE from standard PC" open question, the statistical-computational pillar has seen:

- **"Cryptography from Planted Graphs: Security with Logarithmic-Size Messages"** (eprint.iacr.org/2023/1929) — succinct communication crypto primitives from planted-subgraph hardness.
- Follow-up attacks on specific PKE-from-PC constructions (eprint.iacr.org/2024/359 key-recovery attack on a related scheme; addressed by GHJS25's specific design).
- Continued activity on SQ / low-degree / SOS equivalences, with [Wein 2025 survey](../sources/low-degree-polynomials-survey.md) as the current synthesis.

**Gap assessment**: no new breakthrough reductions or separations announced publicly in 2026 through April. The next major open problem — reducing standard PC from worst-case assumptions like P≠NP — remains untouched.

### 5. Impossibility results for LLM safety — formal modeling without formal proofs

**UPDATE (2026-04-23 mega-batch)**: the formal impossibility proof the wiki identified as missing **is now published and ingested**: [BGGKRR25 — Ball-Gluch-Goldwasser-Kreuter-Reingold-Rothblum 2025](../sources/filter-impossibility-ai-alignment.md). Under standard cryptographic assumptions (TLP, OWF, PKE), no efficient prompt or output filter can align a sufficiently expressive LLM. This is the long-awaited Goldwasser-style impossibility theorem for LLM alignment.

Complementary impossibility results:
- [BGGKRR25 — Filter Impossibility via TLP/OWF/PKE](../sources/filter-impossibility-ai-alignment.md) — **the anchor theorem**.
- [Jailbreak Paradox (Rao-Choudhury 2024)](../sources/jailbreak-paradox.md) — capability-theoretic version via Pareto dominance (complementary, weaker assumption regime).
- [Immune 2024](../sources/immune-rlhf-jailbreak-defense.md) — narrower impossibility for RLHF alignment specifically.
- [MaxMin-RLHF 2024](../sources/maxmin-rlhf-impossibility.md) — single-reward RLHF impossibility.
- [IMTM origin (Ferrag et al. 2025)](../sources/imtm-prompt-injections-protocols.md) — formal threat model under which BGGKRR25 impossibility applies.

**New remaining gap**: BGGKRR25 forecloses black-box filtering but does NOT rule out architectural defenses ([CaMeL](../sources/camel-defeating-prompt-injections.md) capability-based containment), ex-post detection ([MELON](../sources/melon-indirect-prompt-injection.md) masked re-execution), certified interventions ([NAAT](../sources/naat-certified-semantic-smoothing.md) certified semantic smoothing), or internal-to-LLM weight-level alignment. The frontier has shifted from "is any formal impossibility possible?" to "what specific architectural patterns evade the impossibility?"

## Implications for the Wiki

### High-priority next ingests (if continuing the digestion loop)

From the 2024-2026 window, the following papers fill explicit wiki gaps and should be the next batch to add to `raw/` and ingest:

1. **Unelicitable Backdoors in LMs via Cryptographic Transformer Circuits** (arXiv:2406.02619) — extends Pillar III backdoor impossibility to LLMs.
2. **Injecting Undetectable Backdoors in Obfuscated NNs and LMs** (arXiv:2406.05660) — iO-based undetectability for LLMs.
3. **Provable Defense Framework for LLM Jailbreaks via Noise-Augmented Alignment** (arXiv:2602.01587) — first certified LLM jailbreak defense.
4. **Provably Robust Adaptation for Language-Empowered Foundation Models** (arXiv:2510.08659) — LeFCert-L certified-robustness for foundation models.
5. **Enhancing Robustness of LLM-Driven MAS through Randomized Smoothing** (arXiv:2507.04105) — smoothing-for-multi-agent-consensus.
6. **Cryptography from Planted Graphs: Succinct Messages** (eprint.iacr.org/2023/1929) — succinct crypto from planted subgraph.
7. OWASP Top 10 for Agentic Applications 2026 (not a traditional paper, but a *formal taxonomy* worth one-page summary).

### Structural changes suggested

- **Add a Part III.d subsection** to the reading pathway for **"LLM-Extensions of Classifier Theorems"** — covering the randomized-smoothing-for-LLMs line and the undetectable-backdoor-for-LLMs line. These represent the clearest "theory-to-practice transfer" in the field.
- **Create a concept page for "Input Manipulation Threat Model (IMTM)"** once a canonical reference emerges — this is the emerging AIOracle-complementary formalism for prompt-injection-style attacks.
- **Create a concept page for "Indistinguishability Obfuscation (iO)"** — central to several 2024-2026 undetectable-backdoor results and not currently in the wiki.
- **Update `rlhf-formal-model` concept page** with the emerging view that RLHF alignment is empirically+formally insufficient against adaptive adversaries (accumulated evidence from Immune, MaxMin-RLHF, Rando-Tramèr, and 2026 jailbreak surveys).

### Open problems that have moved

The convergence survey identified ~16 open problems. As of April 2026, their status:

| Open problem | 2026 status |
|---|---|
| PKE from standard PC | **Resolved** by GHJS25 (June 2025) |
| Randomized smoothing to LLMs | **Mostly resolved** by NAAT line (Feb 2026) |
| Undetectable backdoors extend to LLMs | **Resolved** by iO line and cryptographic transformer circuits (2024) |
| UC-style composable security for AI | **Unmoved** — no formal composition theorem for multi-agent LLMs |
| Concentration-of-measure + AIOracle unification | **Unmoved** — no bridge between game-based and metric-measure-theoretic frameworks |
| Sample-complexity-optimal robust proper learner | Partially resolved — [Ashtiani et al. 2025](../sources/tolerant-robust-pac-learning.md) in tolerance regime |
| Formal impossibility proof for LLM jailbreaks | **Resolved** by [Ball-Gluch-Goldwasser-Kreuter-Reingold-Rothblum 2025 (BGGKRR25, arXiv:2507.07341)](../sources/filter-impossibility-ai-alignment.md) — prompt/output filter impossibility under TLP/OWF/PKE cryptographic hardness |
| Planted clique from worst-case P≠NP | **Unmoved** |
| Low-degree framework for estimation | **Resolved** by [Schramm-Wein 2022](../sources/low-degree-estimation-schramm-wein.md) |
| Agentic security compositional theorem | **Unmoved** — most urgent practical gap |

**Three movements stand out**: (a) LLM extensions of classical certified-defense and undetectable-backdoor results are now published, (b) the Pillar II frontier (stat-comp gaps → cryptography) saw the decisive GHJS25 result, (c) Pillar III agentic security remains formally unmoved despite exploding practical activity.

### Recommended research bet for 2026

Based on this frontier analysis, the single most promising direction for formal contribution in 2026 is:

> **A UC-style composition theorem for multi-agent LLM security games** — defining an "ideal AI functionality" in which a simulator mimics agent adversarial behavior, and proving that composing agent-oracles preserves security. This closes the most-cited gap from the Villa et al. 2026 convergence survey, aligns with the practical-framework explosion (MAESTRO, MAAIS, OWASP Top 10), and has no current formal-theoretic competitor.

Technical prerequisites are already ingested in the wiki: UC framework (computational indistinguishability, simulator-based proofs), AIOracle abstraction, and attack-taxonomy formalisms. What's needed is a specific paper making the composition-theorem-for-AI construction.

## References

### Newly identified (April 2026) — candidate ingests

- [Unelicitable Backdoors in Language Models (arXiv:2406.02619)](https://arxiv.org/abs/2406.02619)
- [Injecting Undetectable Backdoors in Obfuscated NNs and LMs (arXiv:2406.05660)](https://arxiv.org/abs/2406.05660)
- [Provable Defense Framework for LLM Jailbreaks (arXiv:2602.01587)](https://arxiv.org/abs/2602.01587)
- [Provably Robust Adaptation for Language-Empowered Foundation Models (arXiv:2510.08659)](https://arxiv.org/abs/2510.08659)
- [Enhancing Robustness of LLM-Driven Multi-Agent Systems through Randomized Smoothing (arXiv:2507.04105)](https://arxiv.org/abs/2507.04105)
- [Randomized Smoothing Meets Vision-Language Models (arXiv:2509.16088)](https://arxiv.org/abs/2509.16088)
- [Cryptography from Planted Graphs: Succinct Messages (eprint.iacr.org/2023/1929)](https://eprint.iacr.org/2023/1929)
- [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/) (informal reference)

### Industry / institutional frameworks

- [CSA MAESTRO — Multi-Agent Environment Security Threat Risk Outcome](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro)
- [AWS Agentic AI Security Scoping Matrix](https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems/)
- [Microsoft Agent Governance Toolkit (April 2026)](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/)

### Related wiki pages

- [Reading Pathway for the Formal-Security Corpus](reading-pathway-formal-security.md) — Part III.d should be extended per §"Structural changes suggested" above.
- [Deep Research Prompt (Formalizing AI Security)](deep-research-prompt-formalizing-ai-security.md) — original 16-question framing; update column of "status 2026" above.
- [Wiki index](../index.md) — reflects all ingested sources.
