---
title: "SoK: Analyzing Adversarial Examples — A Framework to Study Adversary Knowledge"
type: source
date_ingested: 2026-08-20
authors: [Lucas Fenaux, Florian Kerschbaum]
venue: arXiv preprint 2402.14937v1 (venue unconfirmed from PDF)
year: 2024
tags: [adversarial-ml, evasion-attacks, threat-model, cryptography, evaluation-methodology]
claim_quantifier: existential
antecedent: none
---

## Summary

The only one of the robustness-evaluation critiques whose target is the *definition* rather than the practice. Its diagnosis is that adversarial-example research has no formal account of what the adversary knows, so threat models are incomparable and attack results cannot be ranked. Its remedy borrows two objects from cryptography: an oracle abstraction for information, and a security game for success.

The oracle abstraction is the **Information Extraction Oracle** (IEO), a stateful machine `O : {0,1}* → {0,1}*` that answers queries with information. A **domination** relation `⊏` is defined over IEOs by their outputs, with base cases for sets, elements and ordered tuples; the interesting base case is the one where the outputs are both elements, and `O₂ ⊏ O₁` holds if some probabilistic polynomial-time `f` maps `O₁`'s output to `O₂`'s. This makes `⊏` a partial order, and the paper draws its Hasse diagram in each of four information categories — model, data, training, defence — with Theorems 1 through 4 asserting that each diagram holds under `⊏`.

The game (Figure 5) is a two-party protocol between attacker `(O, AdvGen, Evaluate_b)` and defender `(D, Train, Classify)`. The attacker repeatedly calls `AdvGen(O)` until it produces a candidate its own distinguisher `D'` accepts; the defender then runs the real distinguisher `D`, and only if the candidate passes does it get classified. The attacker wins iff it evades detection *and* achieves its goal. Detection and misclassification are therefore composed into a single success bit, which is the framework's main structural commitment.

The paper also formalizes imperceptibility without appealing to human perception, by introducing the **human-like distinguisher** — a distinguisher "whose capabilities match that of a human or any human-made real-world system", under which existing metrics (`ℓp`, similarity, quality) are approximations. Indistinguishability is `ζ(n) = 0`; since this is unreachable, a slack notion of **stealth**, `ζ(n) ∈ O(log(n)/n)`, is used instead. Finally, because attack success rate rewards attacking weak models, the paper defines a **relative performance score** `ϒ_{G,G_b} = ξ²_G − ξ²_{G_b}`, subtracting the squared success rate on benign inputs.

For the survey strand, the decisive observation is what the taxonomy omits. §3 announces that adversary knowledge "includes access to data and computing resources, as well as knowledge of the code and hyperparameters" — and then the formalism has four categories, none of which is compute. Attacker computation enters the framework in exactly two places, both incidental: as the PPT quantifier inside the definition of `⊏` (so compute is a *reducibility* notion between kinds of knowledge, never a priced resource), and as a query counter in the *state* of the score and label oracles (Table 1: `O_S` and `O_L` have state "number of queries left [k]"). A paper explicitly written to formalize what the adversary has therefore still does not price what the adversary spends.

## Claim Boundary

- **Quantified over:** Two layers, with different logical forms, and they should not be merged.
  1. *Formal layer.* Theorems 1–4 are universal statements — each asserts that a specific finite Hasse diagram of oracles is correctly ordered under `⊏`. They range over the oracles the paper defines, and they follow from Definition 8 by construction; they are structural, not about attacks.
  2. *Survey layer.* The headline conclusions are existential and dataset-specific. "Transferable attacks might not be as difficult as previously thought" is supported by: on CIFAR-10, the best transferable attack is within 7.3% expected success rate (0.146 score) of the best white-box attack. That is one comparison, on one dataset, between two specific attacks. The ImageNet takeaway that query-only access suffices to reduce an undefended model's accuracy "to almost 0%" ranges over the undefended ImageNet models in the surveyed papers.
- **Antecedent:** none for the theorems. The survey conclusions are conditional on the reported numbers in the surveyed papers being comparable, which the paper itself repeatedly finds they are not — it italicises results it deems unreliable, and abandons two intended comparisons outright because benign accuracies were not reported.
- **Does not establish:** (a) that the four categories are complete — no completeness claim is proved, only asserted as construction ("We used all the threat models we observed in the literature to build this categorization"); (b) that transferable attacks are as strong as white-box attacks in general — the claim is about one gap on one dataset, and depends on the transferable attacker being *given* training data and the training function; (c) that `⊏` totally orders threat models — it is explicitly partial, and Definition 9 exists precisely to combine incomparable oracles; (d) that the relative performance score is the right measure — it is proposed, not validated; (e) anything about adversary *compute*, despite §3's framing.
- **Abstract vs theorem:** yes, one. The abstract says the framework lets the authors "derive new conclusions on the difficulty associated with the white-box and transferable threat models, for example, that transferable attacks might not be as difficult as previously thought." The word "difficulty" invites a reading in which transferability has become computationally easier; the evidence is a success-rate gap under a *knowledge* assumption (the transferable attacker gets the training data and training function to build surrogates). What narrowed is the information gap, not any difficulty in the complexity sense. The paper's own takeaway 4 makes this clear — the surrogate-training assumption "is not explicitly stated in the papers we survey and is instead taken for granted."

## Key Contributions

- **Information Extraction Oracles** as a uniform representation of adversary knowledge, replacing the white-box / grey-box / black-box vocabulary.
- The **domination order `⊏`** over IEOs, with PPT reducibility as the base case for element-valued oracles, and a combination rule (Definition 9) for incomparable oracles.
- Four **Hasse diagrams** — model, data, training, defence — with Theorems 1–4, and a summary oracle table (Table 1) listing each oracle's output and state.
- The **adversarial example game**, composing evasion of a detector with achievement of the attack goal into one success bit, and the accompanying "knowledge table" format for describing an attack's threat model.
- The **human-like distinguisher** and the derived notions of indistinguishability and **stealth** (`ζ(n) ∈ O(log n / n)`), which generalise imperceptibility to Gilmer et al.'s five salient situations rather than to `ℓp` balls alone.
- The **relative performance score** `ϒ_{G,G_b} = ξ²_G − ξ²_{G_b}` ∈ [−1, 1], negative when the attack does worse than benign inputs.
- A survey of 80+ attack papers classified in the framework, with six takeaways.

## Key Definitions / Theorems

- **Definition 6 (Information Extraction Oracle)**: `O : {0,1}* → {0,1}*`, a stateful oracle machine; `State : O → R*` returns its state.
- **Definition 8 (domination `⊏`)**: three base cases plus three ordered-set cases. The base case that carries the complexity content: "x is either an unordered set or an element and y is an element. Then `O₂ ⊏ O₁` if there exists a probabilistic polynomial-time (PPT) function f s.t. ∀a ∈ I, f(x) = y."
- **Definition 9 (combination)**: for incomparable `O_A`, `O_B`, define `O_{A&B}(x) = [O_A(x), O_B(x)]`.
- **Definition 4 (indistinguishability)**: `ζ(n) = |Pr_{x←A}[D(x)=1] − Pr_{x←B}[D(x)=1]| = 0` for a distinguisher `D` capturing the salient situation; the paper immediately calls this "too restrictive" in practice.
- **Definition 5 (stealth)**: `ζ(n) ∈ O(log(n)/n)` with `|A ∪ B| = n`.
- **Definition 10 (Train function)**: `Train : {0,1}* → M`; known facts about it are represented as sets `T = {Train' | g_Train(Train') = True}`.
- **Definitions 11–13**: `AdvGen`, `Classify`, `Evaluate_0/Evaluate_1` (untargeted / targeted indicators).
- **Definition 14 (expected success rate)**: `ξ_G = E[G(...)]`, i.e. attack success rate.
- **Definition 15 (relative performance score)**: `ϒ_{G,G_b} = ξ²_G − ξ²_{G_b}`.
- **Theorems 1–4**: Figures 1–4 (the model, data, training and defence Hasse diagrams) hold under the `⊏` ordering. Proofs are in Appendix A.
- **Oracle catalogue (Table 1)**: `O_M` (parameters), `O_S` (scores), `O_L` (labels), `O_A` (architecture), `O_SPA` (set of possible architectures), `O_D` / `O_D'` / `O_E` (training data / same-distribution data / other data), `O_Train` / `O_Ti` (training function / training-property sets), `O_FA` / `O_PA` / `O_SPD` (full / partial / set-of-possible defence awareness). Only `O_S` and `O_L` carry state, and their state is "number of queries left".

## Connections

- The definitional counterpart to the practice critiques of [CAP+19](on-evaluating-adversarial-robustness.md) and [TCBM20](adaptive-attacks-defenses.md): where those say *evaluate better*, this says the vocabulary for stating what is being evaluated is missing.
- Complementary and near-simultaneous with [SoK: Pitfalls in Evaluating Black-Box Attacks (SSK+24)](sok-black-box-attack-pitfalls.md), which taxonomises the same knowledge space along four different axes (query access, API feedback, auxiliary-data quality, auxiliary-data quantity) and *does* measure attack runtime. Read the two together: FK24 supplies the order-theoretic structure, SSK+24 the cost axis FK24 omits.
- Takeaway 5 reports that only two surveyed papers used any existing evaluation framework, and both used [RobustBench](robustbench.md).
- Its cryptographic-game framing is the same move made, for LLM-agent security, in [Extending the Formalism of Cryptography to AI](extending-formalism-cryptography-ai.md) and [Formalizing LLM Agent Security](formalizing-llm-agent-security.md).
- Its "human-like distinguisher" is the counterpart of the perceptual-metric problem noted in [RobustBench §2](robustbench.md) and in the concentration literature — see [Empirically Measuring Concentration](empirically-measuring-concentration.md).
- Concepts: [Adversary Knowledge Taxonomy](../concepts/adversary-knowledge-taxonomy.md), [Evasion Attacks](../concepts/evasion-attacks.md), [Adaptive Attacks](../concepts/adaptive-attacks.md), [Computational Indistinguishability](../concepts/computational-indistinguishability.md), [Computational vs Information-Theoretic Robustness](../concepts/computational-vs-it-robustness.md).

## Open Questions / Limitations

- **No compute axis.** §3 promises to cover "access to data and computing resources", and the formalism delivers four categories, none of which is computation. Compute appears only as PPT reducibility inside `⊏` and as query counters in oracle state. A defence that costs the attacker more compute at equal knowledge is indistinguishable, in this framework, from one that costs less.
- The four categories are asserted complete by survey construction, not proved complete. Nothing rules out a fifth axis; the paper's own §3 sentence supplies a candidate.
- `⊏` orders knowledge but says nothing about the *value* of knowledge. Takeaway 3 concedes exactly this: "Information categories matter, but their effect on performance is not straightforward."
- The survey layer is limited by the data it aggregates. Several comparisons are abandoned because papers do not report benign accuracy, and unreliable numbers are italicised rather than excluded.
- The game composes detection-evasion and misclassification into one bit, so a defence that detects perfectly and a defence that classifies correctly are not distinguished by the score.
- Stealth is defined asymptotically in `n = |A ∪ B|`, the number of samples, which gives no way to certify a single image as stealthy.
- Minor: Definition 5 refers to "ζ(n) (from Equation 4)" while ζ is introduced in Equation 1 — a cross-reference error in the PDF.

## Quotes / Notable Passages

The promise that the formalism does not keep — compute named in prose, absent from the taxonomy:

> "This goes beyond the knowledge of the machine learning system that they are trying to attack. It includes access to data and computing resources, as well as knowledge of the code and hyperparameters used to set up and train said machine learning system."

The one place computation enters the formal order, as reducibility rather than as cost:

> "Then O2 ⊏ O1 if there exists a probabilistic polynomial-time (PPT) function f s.t. ∀a ∈ I , f (x) = y."

On the absence of standards, which is the paper's motivation:

> "There is a surprising lack of standards to evaluate adversarial example attacks."

On the hidden assumption in transferable attacks (takeaway 4):

> "Most of the transferable attacks whose results we have studied use the training function. This is done to train surrogate models. However, this assumption is not explicitly stated in the papers we survey and is instead taken for granted."

On why raw attack success rate is not a measure of attack quality:

> "It is also know as Attack Success Rate (ASR). However, it can be deceiving as it rewards attacking already poorly performing models"
