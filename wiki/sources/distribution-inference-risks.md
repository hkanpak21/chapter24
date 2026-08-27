---
title: Formalizing and Estimating Distribution Inference Risks
type: source
date_ingested: 2026-08-22
authors: [Anshuman Suri, David Evans]
venue: "venue unconfirmed from PDF (the file carries only arXiv:2109.06024v6 [cs.LG], 5 Jul 2022)"
year: 2022
tags: [adversarial-ml, sample-complexity, learning-theory, computational-indistinguishability]
claim_quantifier: empirical
antecedent: "For the game: the adversary knows the public distribution D and both distribution transformers G_0 and G_1, and has no control over or view of the training process. For Lemma 4.1 and Theorems 4.2 and 4.3: the two distributions are Boolean-property proportional distributions derived from the same D, differing only in the proportion alpha. For Theorem 4.5: both degree distributions follow Zipf's law."
adversary_bound: "None. The adversary is an arbitrary algorithm H mapping a model to a bit. It is bounded in knowledge (either label-only black-box access, or white-box parameter access, plus non-overlapping data from D) and in nothing else. Attack cost is reported in trained models but never enters the definition."
date_verified: 2026-08-20
cls_target: train data
cls_family:
cls_phase: post hoc
cls_access:
cls_write: read only
cls_frame: statistical
cls_party: attacker
cls_unit: samples
cls_tightness: measured
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: none
cls_assessed: implicit
cls_evidence: "the distinguishing accuracy between models trained on datasets of size n from these distributions is at most"
cls_evidence_src: Lemma 4.1
cls_reason: "family left blank: the paper explicitly separates distribution inference from every listed family (\"the adversary's goal in the former is to learn about the training distribution, not about the specific training dataset\"); none of membership/reconstruct/extract/forge/evade/poison/backdoor fits, a vocabulary gap rather than indecision. access left blank: the game's H is access-agnostic and the paper gives equal weight to a label-only black-box instantiation and a white-box parameter-access meta-classifier, with no textual primacy given to either. Classified on Lemma 4.1/Theorem 4.2 (the n_leaked sample-complexity bound) rather than the unrestricted formal game in §3, since this is the paper's theorem-bearing content; the bare game, taken alone, would be party=none/frame=none, flagged here for a second reader. assessed=implicit because the attacks' computational cost is discussed as a side detail and explicitly excluded from the threat model (\"does not otherwise require a stronger adversary\", §6.4), never formalized as a bound."
cls_prov: P
cls_date: 2026-08-22
---

> **Provenance.** Read from the primary PDF: abstract, §1, §3 (setup, the game, advantage, limitations
> of the definition, applying the definition), §4 (Lemma 4.1, Theorems 4.2, 4.3 and 4.5, the `n_leaked`
> construction), §5 (Loss Test, Threshold Test, meta-classifiers), §6.1 (datasets), §6.4 (summary of
> results), §7. The game and the advantage quoted verbatim.

## Summary

This paper gives distribution inference — previously called property inference, and confusingly also
attribute inference — its formal definition, and it builds that definition out of
[Yeom et al.'s membership game](privacy-risk-overfitting.md) by changing the object of inference. The
key move is stated as such: *"the key difference between these attacks and other inference attacks is
that the adversary's goal in the former is to learn about the training distribution, not about the
specific training dataset."* Membership inference, attribute inference and ownership resolution operate
on records; distribution inference operates on the distribution the records were drawn from.

The construction avoids naming two arbitrary distributions. There is one public distribution `D`, known
to both parties, and two public **distribution transformers** `G_0` and `G_1`. The trainer picks
`b ←$ {0,1}`, samples `S ∼ G_b(D)`, trains `M` on `S`, and hands `M` to the adversary, whose algorithm
`H` outputs `b̂`. Because `D`, `G_0` and `G_1` are public, anyone can reconstruct the two candidate
distributions, which is what lets the definition separate distribution inference from the ordinary
statistical purpose of learning: the adversary is not learning a fact about `D`, it is learning which
transformation of `D` was applied.

The second contribution is a **normalized leakage metric**, `n_leaked`. Lemma 4.1 upper-bounds the
distinguishing accuracy achievable from `n` direct samples of the training distribution. Inverting it at
an observed attack accuracy `ω` gives the sample count that would have produced that accuracy by direct
sampling, so `n_leaked` measures an attack in units of *training records handed to the adversary
outright*. The point of the normalization is comparability: distinguishing `α₀ = 0.5` from `α₁ = 1.0` at
95% accuracy is `n_leaked ≈ 3`, while the same accuracy between 0.5 and 0.52 is `n_leaked ≈ 42`.

The experiments cover five datasets — Census, CelebA, RSNA Bone Age, ogbn-arxiv and Chord — with two
cheap black-box attacks (Loss Test, Threshold Test) and the state-of-the-art white-box
permutation-invariant meta-classifier, extended here to convolutional layers. The headline finding is
deflationary and directly relevant to how the field reports success: measured in `n_leaked`, most
attacks on binary classifiers are worth about **one** sample. *"The results show that the most effective
property inference attacks for all datasets (other than RSNA Bone Age) are less accurate predictors than
would be possible with the best possible statistical test from a random sample of size two from the
training distribution."* The second finding is that the cheap attacks are competitive — the Threshold
Test beats meta-classifiers in about 30% of experiments — which the paper reads as an argument for
including simple baselines.

## Claim Boundary

- **Quantified over:** the game is stated for any `D`, any pair of transformers `G_0, G_1`, and any
  adversary algorithm `H`. The leakage theorems are quantified over the restricted distribution families
  in their hypotheses. The experimental claims range over the five datasets, their chosen properties, and
  the three attacks.
- **Antecedent:** (a) `D`, `G_0` and `G_1` are public and known to the adversary; (b) the adversary has
  no control over and no view of the training process — *"we only consider adversaries with no ability to
  observe or influence the training process"*; (c) adversary and victim data splits are disjoint, which
  the paper imposes deliberately so that measured distinguishing power *"is actually distribution
  inference, rather than inadvertent dataset inference"*; (d) for the `n_leaked` theorems, the
  distributional forms named in the front matter. Lemma 4.1 additionally assumes, in its proof, an
  adversary that can fully recover the training dataset from the model, so `n_leaked` is calibrated
  against a reference adversary strictly stronger than any attack the paper implements.
- **Which party is constrained, and in what resource:** neither, in any computational resource. The
  adversary is constrained in *access* — black-box label-only or white-box parameters — and in data. The
  paper is explicit that cost does not change the threat model: training the regression meta-classifier
  *"requires more computational resources (training models for multiple ratios) than is required to
  train the binary meta-classifier (training models only for two ratios), but does not otherwise require
  a stronger adversary."*
- **The success criterion:** exact match on one bit, `b̂ = b`, scored by
  `Adv_H = Pr[b̂ | b] − Pr[b̂ | ¬b]`. There is no tolerance parameter in the definition. The regression
  variant does carry a tolerance — square error `ω` on the ratio `α`, converted to `n_leaked` by Theorem
  4.3 — but the paper states that the definition does not cover it: *"the definition does not directly
  capture the regression attacks we demonstrate where the adversary is estimating what proportion of a
  training dataset has a given property directly."*
- **The baseline:** two of them, and they do different work. The definition's baseline is random
  guessing — *"This advantage is negligible when the adversary does no better than random guessing."*
  The reporting baseline is `n_leaked`, which measures the attack against *direct sampling from the
  training distribution*, an upper-bound adversary rather than a null one. `n_leaked` is the more
  informative of the two and is the paper's own instrument for reading advantage numbers.
- **Does not establish:**
  - **not** an upper bound on distribution inference risk. The experiments are described as *"an
    empirical lower bound on adversarial capabilities"*; a low `n_leaked` means these attacks extracted
    little, not that little is there.
  - **not** that the definition covers property inference generally. §3 lists its own limits: two
    distributions only, both chosen by the adversary, prior knowledge of both assumed, regression not
    covered.
  - **not** anything about poisoning or federated adversaries. Both are named as natural extensions and
    excluded.
  - **not** a separation between distribution inference and the intended purpose of learning in any
    formal sense. The construction *expresses* the separation by making `D`, `G_0`, `G_1` public; it does
    not prove the two cannot be conflated.
  - **not** a bound on efficient adversaries. `H` is unrestricted.
- **Abstract vs theorem:** none found. The abstract's claims — a definition general enough to describe a
  broad class of attacks, a metric relating leakage to direct sampling, and the empirical findings that
  cheap attacks are often as effective as expensive ones and that asymmetries appear — each match a
  section. The abstract does not claim the definition covers regression, and §3 says it does not.

## Key Contributions

- **The distribution inference game**, built on public `D`, `G_0`, `G_1`, with the trainer's coin and
  the adversary's bit, and the advantage `Adv_H = Pr[b̂ | b] − Pr[b̂ | ¬b]`.
- The demonstration that the definition subsumes ratio-based property inference (set `G_0 = id` and
  `G_1` a filter to ratio `α`) and reaches beyond it to graph properties such as mean node degree and
  average clustering coefficient.
- **`n_leaked`**: a unit that converts an attack's distinguishing accuracy into an equivalent number of
  directly sampled training records, making attacks on different distribution pairs comparable.
- Two cheap black-box attacks, the **Loss Test** and the **Threshold Test**, that need only label access
  and, for the second, a small balanced set of locally trained models.
- The extension of permutation-invariant meta-classifiers to convolutional layers.
- The empirical finding that measured in `n_leaked`, binary-classification distribution inference leaks
  on the order of one sample, while regression over `α` and the graph datasets leak substantially more.

## Key Definitions / Theorems

**The game.** §3 sets it out as a two-column protocol between the trainer `T` and the adversary `A`,
with these four numbered steps:

```
1.  b  ←$ {0,1}                      (trainer)
2.  S  ∼  G_b(D)                     (trainer)
3.  M  ←--- S   [train]              (trainer; M is then given to A)
4.  b̂  =  H(M)                       (adversary)
```

The step labels — `b ←$ {0, 1}`, `S ∼ Gb (D)`, `M ←−−− S` with `train` over the arrow, and `b̂ = H(M)` —
are the paper's; the parenthetical role annotations are not.

**The advantage.** The naming sentence is verbatim:

> The advantage of the adversary A using algorithm H is defined as:

and the display, whose conditioning bars do not survive text extraction, is
`Adv_H = Pr[b̂ | b] − Pr[b̂ | ¬b]`. Immediately after it:

> This advantage is negligible when the adversary does no better than random guessing.

**Lemma 4.1.** For two Boolean-property proportional distributions `G_0(D)`, `G_1(D)` with proportions
`α₀, α₁` from the same `D`, an upper bound on the distinguishing accuracy between models trained on
datasets of size `n`. The proof's chain is worth keeping because it fixes what the bound is a bound on.
It starts from an adversary strictly stronger than any attack in the paper — *"Assume the adversary can
fully recover a dataset S (of size n) from some model M trained on it"* — reduces to a hypothesis test
on the dataset, and applies

`Accuracy ≤ ½ + ½ δ(G_0(D)^n, G_1(D)^n)`, with `δ` the total variation distance — before bounding that distance through the KL divergence between
the two mixture densities `ρ_b(x) = (1 − α_b)p_b(x|0) + α_b p_b(x|1)`. The closed form displayed in the
lemma statement is a two-term minimum in `min(α₀,α₁)/max(α₀,α₁)` and
`(1 − max(α₀,α₁))/(1 − min(α₀,α₁))`, each raised to a power in `n`; the typeset expression does not
survive text extraction intact and should be read off the PDF before being carried into any writing.

**Theorem 4.2 (`n_leaked` for ratio distinguishing).** The hypothesis is verbatim:

> Theorem 4.2. Given two Boolean-property proportional distributions G0 (D), G1 (D) with proportion
> values α0 , α1 derived from the same underlying distribution D, and distinguishing accuracy ω using
> some attack,

and the conclusion is `n_leaked` equal to `log(4ω(1 − ω))` over the logarithm of the larger of
`min(α₀,α₁)/max(α₀,α₁)` and `(1 − max(α₀,α₁))/(1 − min(α₀,α₁))`, rendered in the paper as a stacked
fraction that text extraction breaks apart.

**Theorem 4.3 (`n_leaked` for regression over `α`).** Verbatim hypothesis:

> Theorem 4.3. Given a Boolean-property proportional distribution with proportion value α, and square
> error ω observed using some attack,

with conclusion `n_leaked = α(1 − α)/ω`.

**Theorem 4.5 (`n_leaked` for Zipf-distributed degree distributions).** With `H_{N,s}` the generalized
harmonic number, `N₀ ≤ N₁`, parameters `s₀, s₁` and observed accuracy `ω`:
`n_leaked = log(4ω(1−ω)) / log( H_{N₀,s₀}/H_{N₁,s₁} + (s₀ − s₁)·1[s₁ > s₀]·log(N₀) )`.

**The two black-box attacks.** *Loss Test*: `b̂ = 1[acc(M, S⁰) < acc(M, S¹)]` for samples `S^b ∼ G_b(D)`.
*Threshold Test*: train a small balanced set of local models, pick whichever of `S⁰, S¹` maximizes the
accuracy gap between the two model populations, then linear-search a threshold `λ` on that accuracy and
predict `b̂ = 1[acc(M, S^k) ≥ λ]`.

## Connections

- [Privacy Risk in Machine Learning](privacy-risk-overfitting.md) — the game this one is *"inspired
  by"*, with the record replaced by the distribution.
- [Membership Inference Game](../concepts/membership-inference-game.md).
- [Membership Inference Attacks Against Machine Learning Models](membership-inference-shokri.md) — the
  record-level attack §1 contrasts with, and the source of the shadow-model idea the meta-classifier
  attacks depend on.
- [Blind Baseline](../concepts/blind-baseline.md) — `n_leaked`'s role here is the same argument in a
  different direction: report an attack against a reference adversary rather than against the raw
  accuracy scale. The paper's own version is that the results the lack of any clear ranking among its three attacks *"shows why it is
  necessary to include simple baselines when evaluating property inference risk."*
- [The Sample Complexity of Membership Inference and Privacy Auditing](haghifam-sample-complexity-mia.md)
  — the other place in the corpus where leakage is denominated in samples rather than in advantage.
- [SoK: Differential Privacies](sok-differential-privacies.md) — DP bounds neighbouring datasets and so
  does not directly bound this game, a point §1 makes.
- [Reconstructing Training Data with Informed Adversaries](reconstructing-informed-adversaries.md) —
  §II-E there classifies property inference as recovering aggregate statistics that *"in general do not
  compromise the privacy of individuals"*, which is the framing this paper pushes back on.
- [SoK: Security and Privacy in Machine Learning](sok-security-privacy-machine-learning.md) — the
  taxonomy that predates this category having a name.
- [Attaxonomy](attaxonomy.md), [Adversary Knowledge Taxonomy](../concepts/adversary-knowledge-taxonomy.md).
- [Model Extraction](../concepts/model-extraction.md) — the meta-classifier attack reads model
  parameters for a different purpose.

## Open Questions / Limitations

- The definition handles two adversary-chosen distributions and nothing else. Extending it to a set of
  candidate distributions, or to direct estimation of `α`, is named and left open.
- The attacks bound risk from below only. Whether the low `n_leaked` values reflect genuinely low
  leakage or weak attacks is unresolved, and the paper says so.
- Why RSNA Bone Age leaks so much more than Census or CelebA is unexplained: *"We do not yet have a good
  understanding of why this dataset leaks so much more distribution information than the other two"*.
- No ordering among the three attacks holds across datasets, so there is no state of the art to measure
  against.
- Mitigation is not addressed at all. The conclusion asks how to bound distribution inference and offers
  no mechanism.
- The adversary's computation is unrestricted in the definition even though the experiments show cost
  differences of orders of magnitude between the attacks, and the paper explicitly declines to treat cost
  as part of adversary strength.

## Quotes / Notable Passages

> This advantage is negligible when the adversary does no better than random guessing.

(§3. The definitional baseline.)

> it is equivalent to the adversary being able to draw nleaked samples from the training distribution and
> executing an optimal distinguishing statistical test

(§4. What the unit means.)

> the definition does not directly capture the regression attacks we demonstrate where the adversary is
> estimating what proportion of a training dataset has a given property directly

(§3, "Limitations of the Definition". The tolerance-carrying variant is outside the formalism.)

> Training the regression meta-classifier requires more computational resources (training models for
> multiple ratios) than is required to train the binary meta-classifier (training models only for two
> ratios), but does not otherwise require a stronger adversary.

(§6.4. Compute is explicitly excluded from adversary strength.)

> The lack of any clear ranking of the simple black-box and white-box meta-classifier attacks shows why
> it is necessary to include simple baselines when evaluating property inference risk.

(§6.4.)
