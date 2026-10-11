---
title: Reconstructing Training Data with Informed Adversaries
type: source
date_ingested: 2026-08-22
authors: [Borja Balle, Giovanni Cherubin, Jamie Hayes]
venue: "IEEE S&P 2022"
venue_evidence: "dblp: conf/sp/BalleCH22 (inproceedings, IEEE S&P 2022, pp. 1138-1156, DOI 10.1109/SP46214.2022.9833677); direct confirmation, superseding the earlier bibliography-cross-reference evidence"
year: 2022
tags: [adversarial-ml, reconstruction, computational-indistinguishability, sample-complexity]
claim_quantifier: conditional
antecedent: "For the theory: the mechanism satisfies (alpha, epsilon)-Renyi DP (Theorem 2), epsilon-DP (Corollary 3) or rho-zCDP (Corollary 4); the adversary's side knowledge is exactly a prior pi over Z; the target is drawn Z ~ pi; and the bound is stated relative to a fixed error function l and threshold eta. For the converse (Theorem 5), the mechanism must be reconstruction robust simultaneously against every prior supported on a pair of points, under the 0/1 error. For the attacks: the adversary knows all training points but one, the model weights, and the training algorithm including hyper-parameters and, by default, the initialization."
adversary_bound: "Knowledge only. Definition 2 quantifies over any reconstruction attack R : Theta -> Z with no bound on time, circuit size or query count. Definition 1 bounds the adversary's knowledge, not its computation. The empirical attack's cost is reported as one shadow model trained per attack-training point."
date_verified: 2026-08-20
cls_target: train data
cls_family: reconstruct
cls_phase: post hoc
cls_access: white box
cls_write: read only
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: none
cls_assessed: 
cls_evidence: "absent"
cls_evidence_src: "Checked and confirmed absent: Section II threat model and Definition 1 (Informed reconstruction adversary) bound only the adversary's knowledge (the fixed dataset D-, the released parameters θ, the training algorithm A, optional side knowledge aux) and no time, circuit-size or query count; Definition 2 (Section VII, (η,γ)-ReRo) quantifies over any reconstruction attack R : Θ → Z with no resource bound stated; Theorem 2, Corollaries 3-4 and Theorem 5 (Section VII) bound the mechanism's privacy parameters, not any party's computation. raw/BCH22_ReconstructingInformedAdversaries.pdf."
cls_reason: "Hand-classified 2026-08-22 against codebook revision 2, then migrated through revisions 3 to 5. Carries no verbatim evidence quote, unlike the delegated rows."
cls_prov: P
cls_date: 2026-08-22
---

> **Provenance.** Read from the primary PDF: abstract, §I, §II (threat model, Algorithm 1, relations to
> attribute and membership inference), §III (Theorem 1, GLM attack), §IV (reconstructor networks), §V
> (metrics and the nearest-neighbour oracle), §VI-A (feasibility, Table II), §VII (Definitions 2 and 3,
> Theorem 2, Corollaries 3 and 4, Theorem 5, Propositions 6 and 7). Definitions 1 and 2 and the
> definition of the baseline `κ` quoted verbatim and checked against the extracted text.

## Summary

This is the paper that gives data reconstruction a **tolerance-parameterized** success criterion. Where
membership inference asks the adversary for a bit and scores it exactly right or exactly wrong,
reconstruction robustness asks the adversary to produce a candidate point `R(θ)` and scores it a success
whenever `ℓ(Z, R(θ)) ≤ η`. The threshold `η` is a parameter of the definition, and the paper says
plainly that choosing it is not a mathematical question: *"In general, an appropriate choice of ` and a
threshold for declaring successful reconstruction is a policy question that will depend on the
particular application: it should capture the minimum level of leakage that would cause a significant
harm to the involved individual."*

The adversary is **informed** in a precise and unusually strong sense. Definition 1 hands it `D⁻`, the
entire training set except the one target point; the released weights `θ`; the training algorithm `A`
with its hyper-parameters; and optionally side knowledge `aux` about the target. The paper's own
justification is that this is the threat model implicit in differential privacy — DP bounds an adversary
who knows every other record — so a mitigation that stops this adversary stops weaker ones. In the
experiments the adversary additionally knows the model initialization by default, and the released
models are trained with full batches to keep training deterministic; both are relaxed in §VI-B, and
removing the initialization is the one factor in Table II that breaks the attack on both datasets.

The attacks come in two forms. For generalized linear models, Theorem 1 solves the stationarity
condition in closed form and recovers `(x, y)` exactly from `θ` and `D⁻`, with the notable consequence
that *"whether the model overfits the data or generalizes well plays no role in the attack's success."*
For general models, the adversary trains `k` shadow models `θ̄_i = A_{D⁻}(z̄_i)`, one per shadow target,
and then trains a **reconstructor network** RecoNN that maps model weights to a candidate target point.
On MNIST and CIFAR-10 with the default setup the average reconstruction MSE is 0.0089 and 0.0049
against nearest-neighbour oracle thresholds of 0.0232 and 0.0291.

The theoretical half connects the new definition to DP in both directions. Theorem 2: an
`(α, ε)`-RDP mechanism is `(η, γ)`-ReRo with `γ = (κ · e^ε)^{(α−1)/α}`, where `κ` is a property of the
prior alone. Theorem 5: a mechanism that is reconstruction robust against *every* prior supported on a
pair of points, under 0/1 error, must satisfy DP. The practical reading of Theorem 2 is that when the
adversary's prior is diffuse, `κ` is tiny and very large `ε` still suffices — Proposition 6 gives
`γ = e^{-Ω(d)}` for `ε = o(d)` against a uniform prior on the unit ball.

## Claim Boundary

- **Quantified over:** for the definition and Theorems 2 and 5, all datasets `D⁻ ∈ Z^{n−1}` and all
  reconstruction attacks `R : Θ → Z`, with the mechanism ranging over those satisfying the stated DP
  hypothesis. For Theorem 1, generalized linear models trained with an intercept whose objective has a
  unique optimum. For the attacks, MLPs on MNIST and CNNs on CIFAR-10 trained by the authors, 1000 test
  targets per configuration.
- **Antecedent:** named individually in the front matter. The two that carry the most weight are (a) the
  adversary's side knowledge is *exactly* a prior `π` and the target is genuinely drawn from it, and (b)
  in Theorem 5 the family of priors must include every two-point prior with `p = 1/(e^ε + 1)`, which is
  what makes the converse a statement about mechanisms rather than about any realistic adversary.
- **Which party is constrained, and in what resource:** the **mechanism**, in `ε`, `(α, ε)` or `ρ`. The
  adversary is constrained only in knowledge, and Definition 2 explicitly ranges over *any* `R`. The
  paper notes that determinism costs nothing, because the optimal attack is the deterministic maximum a
  posteriori one: *"Definition 2 assumes the reconstruction attack is deterministic."* The single
  sentence in the paper about attacker compute is a description of the empirical attack's price, not a
  bound: *"and on their computational power: they need to train one shadow model per data point to
  create the attack training data."*
- **The success criterion:** `ℓ(Z, R(θ)) ≤ η` — reconstruction within tolerance `η` under a
  reconstruction error function `ℓ : Z × Z → R_{≥0}`. This is not an exact match, and reduces to one only
  when `ℓ = ℓ_{0/1}`, which is the choice Theorem 5 makes to recover DP. Empirically the tolerance is
  instantiated three ways — pixel MSE, LPIPS, and KL divergence between a reference classifier's outputs
  on target and reconstruction — with a fourth, the nearest-neighbour oracle distance, used as the
  declared threshold.
- **The baseline:** given as a named quantity in the definition's own terms. The **baseline error** is
  `κ_{π,ℓ}(η) = sup_{z₀∈Z} P_{Z∼π}[ℓ(Z, z₀) ≤ η]`, the best that can be done by a fixed guess, and the
  paper reads it as an attack: *"Another interpretation of κ is as the success probability of the best
  oblivious reconstruction attack that ignores the output of M."* Empirically the baseline is the
  nearest-neighbour oracle over `D⁻ ∪ D̄`, at average MSE 0.0232 (MNIST) and 0.0291 (CIFAR-10).
- **Does not establish:**
  - **not** that a computationally bounded adversary can reconstruct. Definition 2's `R` is unbounded,
    and the empirical attack's feasibility is a measurement on two small image datasets with shadow-model
    budgets up to 59,000 models.
  - **not** that DP at these `ε` values protects against *membership* inference. The paper's point is the
    opposite: values of `ε` too large to stop informed membership inference can still stop accurate
    reconstruction, because the two criteria differ.
  - **not** that reconstruction robustness implies DP in general. Theorem 5 needs the full family of
    two-point priors and the 0/1 error. Against a single diffuse prior, ReRo is much weaker than DP.
  - **not** a guarantee that survives a wrong prior in the attacker's favour. The paper argues the
    modelling assumption is conservative — an adversary with a wrong prior runs a weaker optimal attack —
    which protects the *mitigation* claim, not the attack claim.
  - **not** an average-case-over-outputs guarantee upgraded to worst case. The paper flags that ReRo
    *"uses an average-case requirement over the outputs of the mechanism"* and that the stronger
    worst-case notion is unattainable under RDP.
- **Abstract vs theorem:** none found, with one wording to watch. The abstract says the work
  *"demonstrates that differential privacy can successfully mitigate such attacks in a parameter regime
  where utility degradation is minimal."* Theorem 2 supports this only relative to a prior with small
  `κ`; the strength of the mitigation is a function of how uncertain the adversary is, which the paper
  states in §VII-A — *"the strength of mitigations against reconstruction is necessarily going to be
  relative to the strength of the prior information available to the adversary."*

## Key Contributions

- **Reconstruction robustness (Definition 2)**: a mechanism-side privacy notion whose success criterion
  carries an explicit tolerance `η` and an explicit error function `ℓ`, with the failure probability `γ`
  as the second parameter.
- The **baseline error `κ`**, which makes the definition's null hypothesis a named object rather than an
  evaluation convention.
- **Theorem 1**: closed-form exact reconstruction of the held-out point from a GLM's parameters and the
  rest of the training set, independent of overfitting.
- **Reconstructor networks**: a general attack that learns the map from released weights to the target
  point by supervised training on shadow model/target pairs.
- **Theorem 2 and Corollaries 3 and 4**: RDP, DP and zCDP each imply ReRo with `γ` an explicit function
  of the privacy parameter and `κ`.
- **Theorem 5**: the converse — reconstruction robustness against all two-point priors under 0/1 error
  implies DP, with `δ = max{0, (e^ε + 1)γ − e^ε}`.
- **Propositions 6 and 7**: against high-dimensional diffuse priors, `ε = o(d)` or `ρ = o(d)` already
  gives `γ = e^{-Ω(d)}`.

## Key Definitions / Theorems

**Definition 1 (Informed reconstruction adversary), verbatim:**

> Definition 1 (Informed reconstruction adversary). Let θ be a model trained on dataset D of size n
> using algorithm A. Let z ∈ D be an arbitrary training data point and D- = D \ {z} denote the remaining
> n − 1 points; we refer to z as the target point. An informed reconstruction adversary has access to:
> a) The fixed dataset D- ;
> b) The released model's parameters θ;
> c) The model's training algorithm A;
> d) (Optional) Side knowledge aux about the target point.

**Definition 2 (Reconstruction robustness), verbatim — the tolerance-parameterized criterion:**

> Definition 2. Let π by a prior over Z and ` : Z ×Z → R≥0 a reconstruction error function. A randomized
> mechanism M : Z n → Θ is (η, γ)-ReRo (reconstruction robust) with respect to π and ` if for any dataset
> D- ∈ Z n−1 and any reconstruction attack R : Θ → Z we have

with the display, which the two-column extraction separates from the sentence above it:

> PZ∼π,θ∼M (D- ∪{Z}) [`(Z, R(θ)) ≤ η] ≤ γ .

(`by` for "be" is as printed. `` ` `` is the error function `ℓ`; `Z n−1` is `Z^{n−1}`; `R≥0` is
`R_{≥0}`. The footnote attached to the display reads: *"Knowledge of π and D in the attack is implicit
through the fact that (2) has to hold for any reconstruction attack."*)

**Every parameter of Definition 2:**

| Symbol | Role |
| --- | --- |
| `π` | prior over `Z`; the formal model of the adversary's side knowledge about the target |
| `ℓ : Z × Z → R_{≥0}` | reconstruction error function; what counts as "close" |
| `η` | **the tolerance.** Success means error at most `η`, not equality |
| `γ` | the bound on the success probability |
| `D⁻ ∈ Z^{n−1}` | the known part of the training set; quantified universally |
| `R : Θ → Z` | the attack; quantified universally, deterministic, otherwise unrestricted |
| `M : Z^n → Θ` | the mechanism being certified |
| `n` | training set size, fixed by the mechanism's signature |

The paper reads its own two parameters as a trade-off: *"A good ReRo mechanism is one with large η and
very small γ, i.e. one where even "decent" reconstructions are impossible with high probability."*

**The baseline, verbatim:**

> For prior π, error function ` and error threshold η, define the baseline error as
> κπ,` (η) = sup PZ∼π [`(Z, z0 ) ≤ η] .

> Another interpretation of κ is as the success probability of the best oblivious reconstruction attack
> that ignores the output of M .

**Algorithm 1 (the protocol), verbatim:**

> procedure R ECONSTRUCTION(A, R, D- , z; aux)
> θ ← A(D- ∪ {z})
> ẑ ← R(θ, D- , A; aux)
> return `(z, ẑ)

**Theorem 2.** Fix `π`, `ℓ` and `η > 0`, and let `κ = κ_{π,ℓ}(η)`. If `M` satisfies `(α, ε)`-RDP then it
is `(η, γ)`-ReRo with respect to `π` and `ℓ` with `γ = (κ · e^ε)^{(α−1)/α}`.

**Corollary 3.** Same setting; if `M` satisfies `ε`-DP then `γ = κ · e^ε`.

**Corollary 4.** If `M` satisfies `ρ`-zCDP with `ρ < log(1/κ)` then
`γ = e^{-(√(log(1/κ)) − √ρ)²}`.

**Theorem 5.** With `Π_ε` the class of all priors on `Z` concentrated on pairs of points with
`p = 1/(e^ε + 1)`: if `M` is `(η, γ)`-ReRo with respect to `ℓ_{0/1}` and every `π ∈ Π_ε`, then `M`
satisfies `(ε, δ)`-DP with `δ = max{0, (e^ε + 1)γ − e^ε}`.

**Propositions 6 and 7.** For `ε = o(d)` or `ρ = o(d)`, `M` is `(η, γ)`-ReRo with `γ = e^{-Ω(d)}` against
the uniform prior on the `d`-dimensional unit ball under `ℓ₂` (Prop. 6), and against `N(w, σ²I_d)` under
`ℓ₂` provided `σ ≥ 2η/√d` (Prop. 7).

**Theorem 1 (GLM attack).** For `θ` the unique optimum of the regularized GLM objective, `X̄` and `Ȳ` the
features and labels of `D⁻` with `X̄₁ = 1`, and `B = g^{-1}(X̄θ) − Ȳ`:
`x = (X̄^T B + λθ) / (X̄₁^T B + λθ₁)` and `y = g^{-1}(⟨x, θ⟩) + λ X̄₁^T B θ₁`.

## Connections

- [Data Reconstruction Attack](../concepts/data-reconstruction-attack.md) — Definition 2 is the
  mechanism-side dual of the attack-side `(ε, µ)`-approximate reconstruction recorded there, and the two
  agree that the tolerance is a parameter and not a security parameter.
- [SoK: Data Reconstruction Attacks](sok-data-reconstruction-attacks.md) — the attack-side taxonomy in
  which this paper's knowledge assumptions sit at the extreme.
- [Membership Inference Game](../concepts/membership-inference-game.md),
  [Privacy Risk in Machine Learning](privacy-risk-overfitting.md) — §II-D restates the membership game
  with the informed adversary (Algorithm 2), which is where the DP threat model and the MIA game meet.
- [Membership Inference Attacks Against Machine Learning Models](membership-inference-shokri.md) — the
  uninformed attack this one is strengthened from.
- [Cohen et al., Data Reconstruction](cohen-data-reconstruction.md) — the computational counterpart this
  paper does not take: reconstruction hardness against polynomial-time adversaries, equivalent to
  one-wayness.
- [Dinur and Nissim, Revealing Information](dinur-nissim-revealing-information.md) — the separation
  between an exponential and a polynomially bounded reconstruction adversary, the axis Definition 2
  leaves flat.
- [Kaplan et al., Bayesian Memorization and Reconstruction](kaplan-bayesian-memorization-reconstruction.md),
  [Computational vs Statistical Memorization](../concepts/computational-vs-statistical-memorization.md).
- [SoK: Differential Privacies](sok-differential-privacies.md),
  [Adversary-Aware DP Bounds](adversary-aware-dp-bounds.md) — where a prior-parameterized relaxation of
  DP sits in the space of variants.
- [LAMP: Extracting Text from Gradients](lamp-gradient-inversion.md) — the gradient channel that §II-E
  distinguishes from this threat model: *"whilst a gradient leakage adversary has access to information
  involving only a mini-batch of training points, our attacks needs to invert the entire training
  procedure."*
- [Deep Learning with Differential Privacy](deep-learning-differential-privacy.md) — the DP-SGD
  machinery the mitigation experiments use.
- [Attaxonomy](attaxonomy.md), [SoK: Security and Privacy in Machine Learning](sok-security-privacy-machine-learning.md)
  — taxonomies into which the informed adversary must be placed.

## Open Questions / Limitations

- The definition's `η` is left to policy. Nothing in the paper fixes a defensible tolerance for a given
  data type, and the empirical threshold used — the nearest-neighbour oracle distance — is described as
  conservative rather than principled.
- The prior `π` is assumed to be the adversary's exact side knowledge. How to elicit, estimate or audit
  a real adversary's prior is not addressed, and `κ` is computed only for the uniform-ball and Gaussian
  cases.
- No computational restriction on `R` anywhere. Whether the gap between the information-theoretic
  `κ`-versus-`γ` picture and what a feasible attacker achieves is large is not asked.
- Random initialization defeats the empirical attack in Table II on both datasets, and the paper does
  not resolve whether that is a genuine mitigation or an artefact of the reconstructor network's
  training budget.
- Theorem 5's converse needs a family of adversarial priors that no real adversary has, so the
  equivalence with DP is one-directional in practice.

## Quotes / Notable Passages

> In general, an appropriate choice of ` and a threshold for declaring successful reconstruction is a
> policy question that will depend on the particular application: it should capture the minimum level of
> leakage that would cause a significant harm to the involved individual.

(§II-B. The tolerance is explicitly outside the mathematics.)

> Another interpretation of κ is as the success probability of the best oblivious reconstruction attack
> that ignores the output of M .

(§VII-A. The baseline, stated as an attack.)

> Definition 2 assumes the reconstruction attack is deterministic.

(§VII-A footnote text. Followed by the argument that the optimal attack is the deterministic maximum a
posteriori one, so determinism is not a restriction.)

> and on their computational power: they need to train one shadow model per data point to create the
> attack training data.

(§VI. The paper's only statement about attacker compute, and it is a cost, not a bound.)

> whether the model overfits the data or generalizes well plays no role in the attack's success.

(§III, on the GLM attack. This severs reconstruction from the overfitting story that
[Yeom et al.](privacy-risk-overfitting.md) built membership advantage on.)

> the strength of mitigations against reconstruction is necessarily going to be relative to the strength
> of the prior information available to the adversary.

(§VII opening. The reason `κ` has to be in the theorem statements.)
