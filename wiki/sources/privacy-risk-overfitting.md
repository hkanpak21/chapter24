---
title: "Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting"
type: source
date_ingested: 2026-08-22
authors: [Samuel Yeom, Irene Giacomelli, Matt Fredrikson, Somesh Jha]
venue: "CSF 2018 (stated in the PDF: \"This is the unabridged version of the paper accepted for publication in CSF 2018.\"); file is arXiv:1709.01604v5 [cs.CR], 4 May 2018"
year: 2018
tags: [adversarial-ml, learning-theory, computational-indistinguishability, sample-complexity]
claim_quantifier: conditional
antecedent: "Each theorem carries its own hypothesis, named separately: Theorem 1 assumes the learning algorithm is epsilon-differentially private; Theorem 2 assumes the loss is bounded by B; Theorem 3 assumes the residual is Gaussian with known variances under both worlds; Theorem 4 assumes an ARO-stable learning rule, a bounded loss, a finite domain, keyed pseudorandom functions, and that x uniquely determines (x,y); Theorem 5 assumes a uniform binary sensitive attribute and Gaussian residuals."
adversary_bound: "None. The adversary A is an arbitrary function of (z, A_S, n, D); no time, size or query bound appears in any definition or theorem. Definition 6's comparison object is the Bayes optimal simulator, which is by construction computationally unbounded."
date_verified: 2026-08-20
---

> **Provenance.** Read from the primary PDF: §1, §2 (stability, DP, generalization error), §3
> (Experiment 1, Definition 4, Theorems 1–4, Adversaries 1–3), §4 (Experiment 2, Definitions 5–6,
> Adversary 4, Theorem 5), §5 (Adversaries 5–6, Theorems 6–7), §6 skimmed for the empirical claims.
> Definitions 4 and 6 and Experiment 1 quoted verbatim and checked character by character against the
> extracted text.

## Summary

This paper supplies the **cryptographic game** that the membership inference literature attributes to
[Shokri et al.](membership-inference-shokri.md) and that
[Shokri et al. do not contain](membership-inference-shokri.md). Experiment 1 is the challenger, the
uniform bit `b`, and the adversary's guess; Definition 4 is the advantage. It does the same for
attribute inference in Experiment 2 and Definitions 5 and 6. Everything the survey needs about
quantifiers and baselines in this corner of the field is fixed here.

The substantive results relate advantage to **generalization error**. Adversary 1 does nothing but
predict non-membership with probability proportional to the model's loss at the challenge point, and
Theorem 2 says its membership advantage is exactly `R_gen(A)/B` for a loss bounded by `B` — for 0-1 loss
with `B = 1`, the advantage *is* the generalization error. Theorem 1 bounds any membership adversary
against an `ε`-differentially private learner by `e^ε − 1`. Theorem 3 gives the advantage of a threshold
adversary under Gaussian residuals. So overfitting is sufficient for membership advantage.

Theorem 4 is the converse direction and the more interesting one: overfitting is **not necessary**. Any
ARO-stable learning rule with bounded loss on a finite domain can be modified into a rule `A_k` whose
stability rate is barely worse and against which some adversary achieves advantage
`1 − µ(n,D) − 2^{-mk}`, essentially the maximum possible. The construction is an algorithm-substitution
attack: the training algorithm and the adversary share keys for pseudorandom functions `F_K, G_K`, the
algorithm supplements the training set with `(F_{K_j}(x_i), G_{K_j}(x_i))` pairs, and the adversary
reads membership off those special queries. This is the one place a cryptographic object enters the
paper, and it enters on the **mechanism**, not on the adversary. The definitions still quantify over an
unbounded adversary; a pseudorandom function is only pseudorandom against a bounded distinguisher, and
the paper does not discuss the mismatch.

§5 gives reductions in both directions between membership and attribute inference. Theorem 6: an
attribute adversary yields a membership adversary of *exactly* the same advantage. Theorem 7: a
membership oracle yields an attribute adversary with `1/m` of the (modified) membership advantage, where
`m` is the number of values the sensitive attribute can take. Reduction Adversary 5 in particular
matters for Definition 6, because it is why the paper says an adversary that "games the system" under
Definition 5 is still evidence of privacy loss.

## Claim Boundary

- **Quantified over:** for the theory, learning algorithms and distributions satisfying each theorem's
  hypothesis, with `A` ranging over *all* functions of `(z, A_S, n, D)`. For the experiments, the
  datasets in §6 — Eyedata, IWPC and Netflix for the linear and tree models, MNIST, CIFAR-10 and
  CIFAR-100 for the convolutional networks — with overfitting controlled by regularization and by a
  network size parameter.
- **Antecedent:** listed in the front matter, one per theorem. The two that bind hardest are Theorem 2's
  bounded loss and Theorem 4's requirement that `x` uniquely determine `(x,y)`, which the paper says is
  needed *"to avoid collisions when the adversary queries the model, which would result in false
  positives"*.
- **Which party is constrained, and in what resource:** the *learner*, in stability or in `ε`. Never
  the adversary. Theorem 1 constrains `A` by differential privacy; Theorem 4 constrains it by ARO
  stability. The adversary is unconstrained throughout, and Definition 6's simulator is explicitly the
  Bayes optimal one.
- **The success criterion:** exact match. For membership, `A(z, A_S, n, D) = b`, a bit. For attribute,
  `A(φ(z), A_S, n, D) = π(z)`, the exact value of the sensitive attribute. There is no tolerance
  parameter of any kind in this paper — nothing corresponding to the `η` of
  [reconstruction robustness](reconstructing-informed-adversaries.md).
- **The baseline:** the two definitions differ here, and the difference is the one most easily lost in
  citation, because both are commonly described as "advantage over a baseline".
  - **Definition 4 (membership).** The baseline is `1/2`, and it is `1/2` *by construction of
    Experiment 1*, because `b` is a fair coin and the challenge point carries no information about it.
    The paper proves this: for all `z`, `Pr[b = 0 | z] = Pr[b = 1 | z]`, followed by *"In fact, the only
    way to gain advantage is through access to the model."* An adversary that ignores `A_S` therefore has
    advantage exactly 0, and `Adv_M` is already a difference against that null. The paper is explicit
    that this is a deliberate design choice: sampling `z ∼ D` rather than `z ∼ D \ S` in the `b = 1`
    branch is what rules the background-knowledge advantage out.
  - **Definition 6 (attribute).** The baseline is the **Bayes optimal simulator** `S(φ(z), n, D)`, which
    receives the partial record but not the model. It is not `1/2`, and it is not zero-advantage by
    construction — a good simulator is a strong baseline.
- **Does not establish:**
  - **not** that Definition 6 is a membership definition. Definition 6 is *alternative attribute
    advantage*. The membership definition is Definition 4.
  - **not** that Definition 6 is degenerate. The paper's own objection to it is the opposite one: it
    over-credits the adversary. *"One potential issue with this alternative definition is that higher
    model accuracy will lead to higher attribute advantage regardless of how accurate the model is for
    the general population."* A model that has merely learned a real trend in `D` scores as leaky.
  - **not** that overfitting causes privacy risk. Theorem 2 makes it sufficient; Theorem 4 makes it
    unnecessary; the paper draws no causal arrow.
  - **not** any statement about efficient adversaries. No definition here restricts the adversary's
    computation, so nothing in the paper separates what an unbounded attacker can do from what a
    feasible one can.
  - **not** a bound that survives composition or repeated release. Every experiment releases one model
    and answers one challenge.
- **Abstract vs theorem:** none found. The abstract says overfitting is *"sufficient to allow an
  attacker to perform membership inference"* and, for attribute inference, only *"when the target
  attribute meets certain conditions about its influence"* — both hedges match the theorems. It also
  states the non-necessity result. The one place the paper's own framing outruns its analysis is
  Definition 6 itself, which it declines to develop: *"we use Definition 5 in the following analysis and
  leave a more complete exploration of Definition 6 as future work."*

## Key Contributions

- **Experiment 1 and Definition 4**: the membership inference security game and the membership
  advantage, in the form the field has used since.
- **Theorem 2**: membership advantage of the bounded-loss adversary equals `R_gen(A)/B`, making
  generalization error a directly attackable quantity rather than an analogy.
- **Theorem 1**: `e^ε − 1` bound on membership advantage under `ε`-DP.
- **Theorem 4**: overfitting is not necessary — a stable learning rule can be subverted, by an
  algorithm-substitution attack using pseudorandom functions, into one that leaks membership almost
  perfectly while remaining nearly as stable.
- **Experiment 2, Definitions 5 and 6**: two inequivalent formalizations of attribute advantage,
  differing precisely in what the adversary's success is measured against.
- **Theorems 6 and 7**: reductions in both directions between membership and attribute inference,
  making them formally comparable rather than merely adjacent.

## Key Definitions / Theorems

**Experiment 1 (Membership experiment), verbatim:**

> Experiment 1 (Membership experiment ExpM (A, A, n, D)). Let A be an adversary, A be a learning
> algorithm, n be a positive integer, and D be a distribution over data points (x, y). The membership
> experiment proceeds as follows:
> 1. Sample S ∼ Dn , and let AS = A(S).
> 2. Choose b ← {0, 1} uniformly at random.
> 3. Draw z ∼ S if b = 0, or z ∼ D if b = 1
> 4. ExpM (A, A, n, D) is 1 if A(z, AS , n, D) = b and 0 otherwise. A must output either 0 or 1.

(`Dn` is `D^n` and `AS` is `A_S` in the source typesetting; the extraction flattens the superscripts and
subscripts.)

**Definition 4 (Membership advantage), verbatim:**

> Definition 4 (Membership advantage). The membership advantage of A is defined as
> AdvM (A, A, n, D) = 2 Pr[ExpM (A, A, n, D) = 1] − 1,
> where the probabilities are taken over the coin flips of A, the random choices of S and b, and the
> random data point z ∼ S or z ∼ D.

with the equivalent form

> AdvM = Pr[A = 0 | b = 0] − Pr[A = 0 | b = 1],

**Definition 6 (Alternative attribute advantage), verbatim. Note before reading it that Definition 6 is
an *attribute* definition, not a membership one:**

> Definition 6 (Alternative attribute advantage). Let
> S(ϕ(z), n, D) = arg max Pr [π(z) = ti | ϕ(z)]
> z∼D
> ti
> be the Bayes optimal simulator. The attribute advantage of A can alternatively be defined as
> AdvAS (A, A, n, D) = Pr[A(ϕ(z), AS , n, D) = π(z) | b = 0] − Pr[S(ϕ(z), n, D) = π(z) | b = 1].

Read the pieces off it: it quantifies over the same Experiment 2 as Definition 5, its subject is the
**attribute** `π(z)` and not membership, its success criterion is exact equality with `π(z)`, and its
baseline is the **Bayes optimal simulator without model access**, evaluated in the `b = 1` world.
Definition 5, the one the paper actually uses, instead compares the same adversary across the two
worlds:

> AdvA (A, A, n, D) = Pr[ExpA (A, A, n, D) = 1 | b = 0] − Pr[ExpA (A, A, n, D) = 1 | b = 1],

**Definition 3 (Average generalization error).** The naming sentence is verbatim:

> Definition 3 (Average generalization error). The average generalization error of a machine learning
> algorithm A on D is defined as

and the displayed quantity is

```
R_gen(A, n, D, ℓ)  =  E_{S∼D^n, z∼D}[ℓ(A_S, z)]  −  E_{S∼D^n, z∼S}[ℓ(A_S, z)]
```

rendered here with the subscripts restored, because the two-column extraction separates each
expectation from its subscript. The paper's own gloss: *"AS overfits if its expected loss on samples
drawn from D is much greater than its expected loss on its training set."*

**Theorem 2.** The advantage of Adversary 1 is `R_gen(A)/B`.

**Theorem 1.** For an `ε`-differentially private learning algorithm `A` and any membership adversary,
`Adv_M(A, A, n, D) ≤ e^ε − 1`.

**Theorem 4.** For `d = log|X|`, `m = log|Y|`, loss bounded by `B`, an ARO-stable rule `A` with rate
`ε_stable(n)`, and `x` uniquely determining `(x,y)`: for any integer `k > 0` there is an ARO-stable rule
`A_k` with rate at most `ε_stable(n) + knB2^{-d} + µ(n,D)` and an adversary `A` with
`Adv_M(A, A_k, n, D) = 1 − µ(n,D) − 2^{-mk}`.

**Theorem 6.** `Adv_M(A_{M→A}, A, n, D) = Adv_A(A_A, A, n, D)`.

**Theorem 7.** `Adv_A(A^U_{A→M}, A, n, D) = (1/m) · Adv^M_*(A_M, A, n, D, φ, φ^{-1}, π)`.

## Connections

- [Membership Inference Game](../concepts/membership-inference-game.md) — Experiment 1 is the game's
  first written form.
- [Membership Inference Attacks Against Machine Learning Models](membership-inference-shokri.md) — the
  attack this paper formalizes, and the paper that is usually miscredited with the game.
- [Membership Inference Attacks From First Principles](mia-from-first-principles.md) — adopts this
  game unchanged (its Definition 1) and attacks the metric instead.
- [Formalizing and Estimating Distribution Inference Risks](distribution-inference-risks.md) — states
  that its game is *"inspired by Yeom et al.'s cryptographic game definition of membership inference"*
  and moves the object of inference from the record to the distribution.
- [Reconstructing Training Data with Informed Adversaries](reconstructing-informed-adversaries.md) —
  the same game with the informed adversary added, and with the success criterion widened from a bit to
  a tolerance.
- [The Sample Complexity of Membership Inference and Privacy Auditing](haghifam-sample-complexity-mia.md)
  — prices the same adversary in samples rather than in advantage.
- [Adversary-Aware DP Bounds](adversary-aware-dp-bounds.md), [SoK: Differential Privacies](sok-differential-privacies.md)
  — the DP side of Theorem 1, and the taxonomy in which Definition 6's simulator is a recognised axis.
- [Blind Baseline](../concepts/blind-baseline.md) — Definition 6's simulator is the definitional form of
  what the blind-baseline literature measures empirically.
- [SoK: Security and Privacy in Machine Learning](sok-security-privacy-machine-learning.md) — surveys
  this material one year later without adopting the game.
- [Computational Differential Privacy](../concepts/computational-differential-privacy.md) — the
  restriction this paper does not take. Theorem 4's pseudorandom functions are the one point where a
  bounded-distinguisher assumption is implicitly in play.

## Limits

- [Evaluations of Machine Learning Privacy Defenses Are Misleading](privacy-defense-evaluations-misleading.md)
  argues that an average-case advantage of the kind Definition 4 measures is the wrong quantity when the
  question is whether any individual is exposed.
- [Membership Inference Attacks From First Principles](mia-from-first-principles.md) finds models with
  identical train-test gaps differing by 100× in vulnerability, which bounds how much of Theorem 2's
  identification of advantage with generalization error survives outside its bounded-loss hypothesis.
- [The Difficulty of Membership Inference Attacks](difficulty-of-mia.md) reports that attacks achieving
  positive advantage under this definition can be matched by baselines that never query the model, so a
  measured `Adv_M > 0` on a benchmark is not by itself evidence that Experiment 1's null was respected in
  the experiment.

## Open Questions / Limitations

- Definition 6 is left undeveloped by the authors' own decision, and with it the question of how to
  measure attribute leakage against a simulator baseline without crediting the model for learning `D`.
- No adversary in the paper is computationally restricted, so the paper cannot distinguish leakage that
  is extractable from leakage that is merely present. Theorem 4 constructs an adversary that only works
  because it was given the key.
- §3.4 leaves open how to characterize the learning algorithms for which overfitting is necessary as
  well as sufficient. The paper names this as future work with Theorem 4 as the obstruction.
- Theorem 7's factor of `1/m` is not shown tight.

## Quotes / Notable Passages

> In fact, the only way to gain advantage is through access to the model.

(§3, immediately after Definition 4. This is the sentence that makes the membership baseline zero by
construction, and it is about Definition 4, not Definition 6.)

> We are interested in measuring the degree to which AS reveals membership to A, and not in the degree
> to which any background knowledge of S or D does.

(§3, justifying `z ∼ D` rather than `z ∼ D \ S` in the `b = 1` branch.)

> One potential issue with this alternative definition is that higher model accuracy will lead to higher
> attribute advantage regardless of how accurate the model is for the general population.

(§4, the paper's own objection to Definition 6. The objection is over-crediting, not degeneracy.)

> we use Definition 5 in the following analysis and leave a more complete exploration of Definition 6 as
> future work

(§4. Definition 6 is stated and then set aside.)

> This is the unabridged version of the paper accepted for publication in CSF 2018.

(Title-page footnote; the venue.)
