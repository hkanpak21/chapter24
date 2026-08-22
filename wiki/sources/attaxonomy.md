---
title: "Attaxonomy: Unpacking Differential Privacy Guarantees Against Practical Adversaries"
type: source
date_ingested: 2026-08-20
authors: [Rachel Cummings, Shlomi Hod, Jayshree Sarathy, Marika Swanberg]
venue: venue unconfirmed from PDF (arXiv:2405.01716v1 [cs.CR], 2 May 2024)
year: 2024
tags: [adversary-knowledge-taxonomy, differential-privacy, data-reconstruction-attack, membership-inference-game, attack-taxonomy-llms]
claim_quantifier: universal
antecedent: "For the DistReRo results: ε-DP, independent target priors, a fixed reconstruction loss ℓ and threshold η."
adversary_bound: knowledge (auxiliary information, access level, target source) — NOT runtime, NOT function class, NOT query count
---

## Summary

A taxonomy of privacy **attacks** built to help practitioners set `ε`, plus a new reconstruction notion for
less-informed adversaries. Its relevance here is negative and precise: **the taxonomy weakens the adversary
by knowledge, and has no computational dimension at all.**

The taxonomy has three roles, each with dimensions and options. **Crafter** — dataset generation
(constructed vs drawn), privacy unit (group/individual/event), target source (crafted vs drawn).
**Attacker** — access to mechanism (white box / black box / query access / none), population-level auxiliary
information, dataset-level auxiliary information, attack goal (membership inference, attribute inference,
singling out, reconstruction). **Evaluator** — baseline attacker, success metric. Options within a dimension
are ordered by decreasing adversary strength "where applicable."

Every dimension is about what the adversary **knows** or what it can **see**. Nothing in the taxonomy asks
how much the adversary can **compute**. The word "computational" appears in the paper only in the phrase
"efficient computational methods for estimating the ReRo guarantees" — a remark about the defender's
estimation cost, not the attacker's budget. This is the same gap as in
[SAH+25](adversary-aware-dp-bounds.md), which explicitly adopts this taxonomy.

The technical contribution is **distributional reconstruction robustness**. Balle–Cherubin–Hayes ReRo gives
the adversary all but one record; the relaxation gives it only population-level distributional knowledge.
Two success measures are defined: `BCDistReRo` (Definition 4.4), which scores the guess against the *most
similar* record in the true dataset — the "most vulnerable" target — and `AvgDistReRo` (Definition 4.8),
which scores against a uniform record. ReRo implies BCDistReRo with a factor `n` in `γ` (Theorem 4.6), and
that factor is shown unavoidable because the infimum gives the attacker `n` tries. ReRo implies AvgDistReRo
with the same `γ` (Theorem 4.10). Corollaries 4.7 and 4.11 then transfer `ε`-DP bounds:
`γ ≤ n · e^ε · κ_{D,ℓ}(η)` and `γ ≤ e^ε · κ_{D,ℓ}(η)` respectively. Theorem 4.12 shows distributional ReRo
is a **strict** relaxation — it does not imply ReRo.

The paper is unusually careful about baselines, and the caution generalizes. Because a data distribution may
be intrinsically easy to reconstruct, `γ` alone is uninformative; it must be read against
`κ_{D,ℓ}(η) = sup_{z₀} Pr_{x∼D^n}[inf_{x∈x} ℓ(x, z₀) ≤ η]`, the best oblivious strategy. The Corollary 4.7
bound is **vacuous** once `κ > 1/(n e^ε)`. A footnote records that the baseline point "was a major criticism
of the census reconstruction attacks."

§3 applies the taxonomy to Israel's Ministry of Health birth dataset release, as a worked threat-modelling
exercise.

## Claim Boundary

- **Quantified over:** the taxonomy over the attack literature the authors surveyed. The theorems over all
  reconstruction attacks `A : Θ → X` (and `A : Θ × X → X` for ReRo), all data distributions `D`, all `η`,
  all loss functions `ℓ`.
- **Antecedent:** the DP corollaries assume `ε`-DP and datasets of size `n`. `AvgDistReRo`/`BCDistReRo` are
  defined with respect to a fixed `D` and `ℓ`.
- **Excluded cases:** the taxonomy is not exhaustive — "Although our taxonomy is not exhaustive, it offers a
  framework for explicitly capturing large classes of attacks." Correlated data is outside the DP model
  throughout. The bounds go vacuous for high-baseline distributions.
- **Does not establish:** any bound depending on the adversary's compute, and it does not claim to. It does
  not establish that DistReRo is implied by DP for non-independent priors. It does not establish a value of
  `ε`; the framing is that the taxonomy "provides a roadmap," not an answer.
- **Abstract vs theorem:** none found. The abstract describes the taxonomy as "a roadmap for analyzing
  real-world deployments" and the technical part as generalizing ReRo "to a less-informed adversary with
  distributional uncertainty."

## Key Contributions

- The Crafter / Attacker / Evaluator taxonomy of privacy attacks, with dimensions and options, and a map of
  which cells the literature has studied.
- `BCDistReRo` and `AvgDistReRo`, and their full parametric relations to ReRo and `ε`-DP.
- Explicit treatment of the **baseline** as a first-class dimension of attack evaluation.
- A worked threat model for a live national DP deployment.

## Key Definitions / Theorems

- **Definition 4.1 (ReRo [Balle–Cherubin–Hayes]).** `M` is `(η, γ)`-ReRo if for any `x ∈ X^{n−1}` and any
  `A : Θ × X → X`, `Pr_{z∼D, θ∼M(x∪{z})}[ℓ(z, A(θ, x)) ≤ η] ≤ γ`.
- **Definition 4.4 (BCDistReRo).** `Pr_{x∼D^n, θ∼M(x)}[inf_{x∈x} ℓ(x, A(θ)) ≤ η] ≤ γ`.
- **Definition 4.5 (BCDistReRo baseline).** `κ_{D,ℓ}(η) = sup_{z₀∈X} Pr_{x∼D^n}[inf_{x∈x} ℓ(x, z₀) ≤ η]`.
- **Definition 4.8 (AvgDistReRo).** Loss against a uniform record of the input dataset.
- **Theorem 4.6.** `(η, γ)`-ReRo ⟹ `(η, nγ)`-BCDistReRo; the factor `n` is unavoidable.
- **Theorem 4.10.** `(η, γ)`-ReRo ⟹ `(η, γ)`-AvgDistReRo.
- **Corollaries 4.7, 4.11.** For `ε`-DP: `γ_BC ≤ n·e^ε·κ(η)`, `γ_Avg ≤ e^ε·κ(η)`.
- **Theorem 4.12.** Distributional ReRo does not imply ReRo.

## Connections

- Concept: [adversary knowledge taxonomy](../concepts/adversary-knowledge-taxonomy.md).
- Concept: [data reconstruction attack](../concepts/data-reconstruction-attack.md).
- Concept: [membership inference game](../concepts/membership-inference-game.md).
- Concept: [blind baseline](../concepts/blind-baseline.md) — the baseline discipline here is the same
  discipline the MIA-evaluation literature arrived at independently. See
  [blind baselines beat MIA](blind-baselines-beat-mia.md) and
  [MIA cannot prove training](mia-cannot-prove-training.md).
- Adopted wholesale by [SAH+25](adversary-aware-dp-bounds.md), which reuses the four dimensions of Table 1
  and inherits the missing computational axis.
- Complementary axis to [CIM19](capacity-bounded-dp.md): knowledge versus function class.
- [DP20](sok-differential-privacies.md) taxonomizes definitions rather than attacks; its dimension **B** is
  this paper's knowledge axis, and its dimension **C** is the one this paper lacks.

## Open Questions / Limitations

- The taxonomy's own point: many cells are unstudied. **The whole computational column is not merely
  unstudied but unrepresented** — an adversary's compute is not one of the dimensions, so no cell of this
  taxonomy can express "an attacker who could succeed given more time."
- Setting `ε` from attack success remains "a longer-term goal for the DP community."

## Quotes / Notable Passages

> "the guarantee that most naturally follows from the DP definition is protection against membership
> inference by an adversary who knows all but one data record and has unlimited auxiliary knowledge."

> "This observation was a major criticism of the census reconstruction attacks."

> "demonstrating the reconstruction robustness of a DP mechanism requires data distributions with low
> baseline success rates in this setting."
