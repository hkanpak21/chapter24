---
title: "Provable Defense Framework for LLM Jailbreaks via Noise-Augmented Alignment (NAAT + CSS)"
type: source
date_ingested: 2026-04-23
authors: [Zehua Cheng, Jianwei Yang, Wei Dai, Jiahao Sun]
venue: "arXiv:2602.01587v1 (2 Feb 2026). The PDF carries an AAAI copyright line for 2026 but states no acceptance."
year: 2026
tags: [llm-security, certified-robustness, randomized-smoothing, jailbreak, hypergeometric, semantic-smoothing]
claim_quantifier: conditional
antecedent: "A lower bound p_A on the top class probability and an upper bound p_B on the runner-up, both estimated by Monte Carlo with a Clopper-Pearson interval at significance alpha = 0.001, so the certificate holds with probability 1 - alpha over the smoothing randomness and not otherwise."
adversary_bound: "none — the adversary may modify at most r token positions in the mutable payload. That is a combinatorial constraint on the perturbation, not a bound on compute, queries, or memory. The base classifier is treated as arbitrary, including adversarially constructed."
date_verified: 2026-08-20
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: white box
cls_write: read only
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "The smoothed classifier G is provably robust (i.e., G(x′) = cA) against any perturbation of size r if:"
cls_evidence_src: Thm 1
cls_reason: "Rule 5 (perturbation budget): the only stated restriction is the r-token l0 budget on the payload, so party=attacker, unit=perturbation, tightness=budget, frame=capability. access=white box, not none, by direct analogy to certified-robustness-randomized-smoothing.md (CRK19, this paper's own named predecessor): Theorem 1 fixes f as 'an arbitrary base classifier' and the paper's own tightness argument constructs an adversarial Trojan classifier, so the certificate is stated to cover a fully-informed adversary, matching CRK19's 'Theorem 1 assumes nothing about f' reasoning verbatim. write=none for the same reason as CRK19: the attacker perturbs its own query input at test time and writes to no corpus, model, or channel. assessed=explicit since r is the direct subject of Theorem 1, not a reported side cost."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (CYDS26) presents **Certified Semantic Smoothing (CSS)** — the first end-to-end deterministic certification protocol for instruction-tuned LLMs against gradient-based jailbreaks such as GCG. Classical [randomized smoothing (Cohen-Rosenfeld-Kolter 2019)](certified-robustness-randomized-smoothing.md) applies Gaussian noise in continuous input space, which is **not well-defined** for the high-dimensional *discrete* token space of language models. CSS solves this by introducing **stratified randomized ablation**: the prompt is partitioned into immutable structural tokens (system-level instructions, tool invocations) and mutable payload tokens (user-provided content), and a subset of the payload is randomly ablated. The certified radius is derived from the **Hypergeometric distribution** (exact combinatorial analysis), yielding an **ℓ₀-norm** certified robustness radius.

The companion **Noise-Augmented Alignment Tuning (NAAT)** is a fine-tuning procedure that aligns the base LLM's representations with the smoothing distribution — effectively turning the LLM into a *semantic denoiser* so that utility does not collapse under sparse-ablated inputs. NAAT solves the "inverted scaling fallacy" that plagued character-level SmoothLLM (where smoothing reduced both attack success and benign utility proportionally).

Positioned as the first practical certified LLM jailbreak defense with (1) deterministic certification under the Hypergeometric distribution, (2) preserved utility via alignment-aware fine-tuning, and (3) direct applicability to production models.

## Claim Boundary

- **Quantified over:** a benign input x and the perturbations of it that change at most r positions of the mutable payload. Theorem 1, "Finite-Sample Certified Radius", is pointwise: it certifies one input at a time, given a lower bound p_A on the top class probability and an upper bound p_B on the runner-up. Experiments are on Llama-3 against gradient-based attacks.
- **Antecedent:** p_A and p_B are not known but estimated. Section 3 describes a Monte Carlo procedure with Clopper-Pearson one-sided intervals at significance α = 0.001, and the experiments draw N = 100,000 samples. The certificate therefore holds with confidence 1 − α over the smoothing randomness. The algorithm may also return Abstain, and abstentions are not certified.
- **Which party is constrained:** the adversary, in the number of token positions it may change — an ℓ₀ budget on the payload. That is a combinatorial constraint on the perturbation, not a bound on any resource. The base classifier is arbitrary; the paper's own tightness argument constructs a Trojan classifier that behaves normally on benign data and flips on a trigger token, so the certificate must hold even against a maliciously constructed base model, which is what makes it tight and also what makes it weak.
- **Does not establish:** that the model is safe. What is certified is that the smoothed classifier's top class does not change within the radius, so a model that is already wrong on x is certified to stay wrong. Structural tokens are held immutable by assumption, so any attack that reaches the system prompt or the chat template is outside the guarantee by construction. Nothing is established for attacks that exceed r positions, and nothing about semantic paraphrase, which changes many positions at once.
- **Abstract vs theorem:** the abstract says the framework "provides a deterministic certificate of safety, ensuring that a model remains robust against all adversarial variants within a provable radius". Theorem 1 is named a *finite-sample* radius and its inputs come from Clopper-Pearson intervals at α = 0.001, so the certificate is high-probability, not deterministic. "Certificate of safety" also overstates the object, which certifies label stability rather than safety.

## Key Contributions

- **Certified Semantic Smoothing (CSS)**: stratified randomized ablation defining an ℓ₀-norm certified radius via Hypergeometric tail bounds.
- **Stratified token partition**: immutable structural tokens vs. mutable payload tokens — semantically-aware smoothing.
- **Hypergeometric distribution for certification**: replaces CRK19's Gaussian analysis; exact combinatorial tail bound.
- **Noise-Augmented Alignment Tuning (NAAT)**: fine-tuning procedure that makes the LLM a semantic denoiser under sparse inputs.
- **Solves inverted-scaling fallacy**: previous character-level SmoothLLM saw utility collapse; NAAT preserves utility while maintaining certified robustness.
- **First end-to-end deterministic certification for LLM jailbreaks**: GCG and gradient-based attacks are formally ruled out up to the certified ℓ₀ radius.

## Key Definitions / Theorems

- **Stratified smoothing**: input x = (x_struct, x_payload); smoothing samples subsets of x_payload while keeping x_struct fixed.
- **CSS certificate**: if the smoothed classifier's top-class margin exceeds a Hypergeometric-derived threshold, the prediction is certifiably robust to ℓ₀-bounded attacks on the payload.
- **NAAT objective**: fine-tune the LLM to minimize KL divergence between outputs on ablated and non-ablated prompts, for benign training examples.
- **Neyman-Pearson-style tight bound**: the Hypergeometric analysis is tight for the ablation mechanism.

## Connections

- Source: [Certified Robustness via Randomized Smoothing (CRK19)](certified-robustness-randomized-smoothing.md) — foundational smoothing paper; CSS is the LLM/discrete-space extension.
- Source: [SmoothAdv (SYL+19)](provably-robust-smoothadv.md) — adversarial training boost to smoothing; NAAT is the LLM analogue.
- Source: [Filter Impossibility (BGGKRR25)](filter-impossibility-ai-alignment.md) — shows black-box filters fail; CSS is a model-intervention (not black-box filter) consistent with BGGKRR's framework.
- Source: [Universal Jailbreak Backdoors from Poisoned RLHF (RT23)](universal-jailbreak-rlhf-backdoors.md) — practical jailbreak attack; CSS is the corresponding provable defense.
- Source: [Immune: RLHF Jailbreak Defense](immune-rlhf-jailbreak-defense.md) — inference-time defense; CSS is complementary with provable guarantees.
- Concept: [Evasion Attacks](../concepts/evasion-attacks.md) — jailbreaks as evasion in LLM context.

## Open Questions / Limitations

- **ℓ₀ radius is small**: certified robustness applies to ablation of a few tokens; jailbreaks using many-token manipulations may still succeed.
- **Structural-payload partition requires care**: if attacker can influence the "structural" tokens, the certification doesn't apply.
- **Fine-tuning cost**: NAAT requires substantial compute; scaling to frontier models is an open engineering challenge.
- **Hypergeometric radius**: specific to fixed-budget ablation; other discrete-smoothing distributions may give tighter bounds in specific regimes.

## Quotes / Notable Passages

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> The first end-to-end deterministic certification protocol for instruction-tuned LLMs against gradient-based jailbreaks.

> _Not a quotation from the paper. This characterization was carried over from a secondary survey artifact during an earlier ingest and was wrongly presented in quotation marks. Retained unquoted, corrected 2026-08-20; verify against the primary source before citing._
>
> Certified Semantic Smoothing via stratified randomized ablation — partitioning the prompt into immutable structural tokens and mutable payloads — derives an ℓ₀-norm certified radius from the Hypergeometric distribution.

The abstract's own description, verbatim:

> "We introduce Certified Semantic Smoothing (CSS) via Stratified Randomized Ablation, a technique that partitions inputs into immutable structural prompts and mutable payloads to derive rigorous l0 norm guarantees using the Hypergeometric distribution."

Theorem 1, verbatim as far as the prose runs:

> "Theorem 1 (Finite-Sample Certified Radius). Let f be an arbitrary base classifier. For a benign input x, let pA be a lower bound on the probability of the top class cA , and pB be an upper bound on the probability of the runner-up class cB . The smoothed classifier G is provably robust (i.e., G(x′ ) = cA ) against any perturbation of size r if:"
