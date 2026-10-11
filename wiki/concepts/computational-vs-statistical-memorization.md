---
title: Computational vs Statistical Memorization
type: concept
tags: [reconstruction, computational-indistinguishability, learning-theory, sample-complexity]
---

## Definition

Two inequivalent senses in which a model may be said to have memorized a training example.

- **Statistical memorization** — the information is *present*. Formalized as high mutual information
  `I(w; x)` between the released model and the example, or as a failure of differential privacy.
- **Computational memorization** — the information is *extractable*. Formalized by exhibiting an attack,
  or by a security definition quantifying over adversaries that are bounded in some resource.

The two come apart in both directions, and the gap between them is where any computational theory of
learning privacy has to live.

## Intuition

If no attacker can get the example out of the model, did the model memorize it? A theory that answers
"yes" is measuring presence; a theory that answers "no" is measuring extractability. Differential
privacy answers "yes" — its adversary has unlimited time. That choice is deliberate and it is also the
reason DP cannot distinguish a model that is safe from one that is merely expensive to attack.

## Properties / Theorems

- **The separation is old and has a complexity form.**
  [Dinur–Nissim PODS'03](../sources/dinur-nissim-revealing-information.md): an unbounded adversary forces
  `Ω(n)` perturbation, a time-`T` adversary only `Õ(√T)`. The gap between their §3 and §4 is the
  statement.
- **The modern framing is named and answered.**
  [Kaplan–Mansour–Nissim–Stemmer](../sources/kaplan-bayesian-memorization-reconstruction.md) ask it
  directly and separate the notions — but their separating example is information-theoretic
  (`I(S;H|Nature) = nd/2` with no extraction possible *even unbounded*), so their axis is
  presence-versus-extractability-with-side-information rather than presence-versus-*poly-time*-
  extractability. **The seam is real and is where remaining room sits.**
- **A computational notion exists and is crypto-equivalent.**
  [Cohen et al. ITCS'25](../sources/cohen-data-reconstruction.md) Def C.1, equivalent to one-wayness and
  to CPA-security. Their own observation: large mutual information *"does not imply the existence of an
  efficient attack"*, and the memorization literature is *"typically not constructive."*
- **The sample-complexity axis is separate and also occupied.**
  [Haghifam–Smith–Ullman](../sources/haghifam-sample-complexity-mia.md) bound the attacker's *samples*
  rather than its time, with a quadratic separation from the trainer's budget.
- **Standing hazard.** Whether computational boundedness buys anything over statistical DP in the
  single-curator setting has been open since Beimel–Nissim–Omri (CRYPTO 2008) and is sharpened negatively
  by Groce–Katz–Yerukhimovich (TCC 2011). Any claim that restricting to efficient adversaries changes
  the leakage picture inherits that open problem.

## Where It Appears

- [dinur-nissim-revealing-information](../sources/dinur-nissim-revealing-information.md)
- [kaplan-bayesian-memorization-reconstruction](../sources/kaplan-bayesian-memorization-reconstruction.md)
- [cohen-data-reconstruction](../sources/cohen-data-reconstruction.md)
- [haghifam-sample-complexity-mia](../sources/haghifam-sample-complexity-mia.md)
- [native-asymmetry-in-learning](../analyses/native-asymmetry-in-learning.md)
- **Where the split is conspicuously absent.** Three 2022–2025 systematizations define attack success
  without any resource term, so they have nowhere to record which side of this line an attack sits on:
  [sok-data-reconstruction-attacks](../sources/sok-data-reconstruction-attacks.md) (`(ε, µ)`-approximate
  reconstruction; adversary characterized by *knowledge* only),
  [beyond-labeling-oracles](../sources/beyond-labeling-oracles.md) (extraction success proposed as a
  dollar-cost inequality, left informal, training compute dropped), and
  [auditable-unlearning-definitions](../sources/auditable-unlearning-definitions.md) (forging maps proved
  to *exist*, with no bound on the cost of finding one — the statistical side of the split with the
  computational side missing).

## Related Concepts

- [fiber-of-the-training-map](fiber-of-the-training-map.md) — the geometric statement of the same split.
- [computational-indistinguishability](computational-indistinguishability.md),
  [one-way-functions](one-way-functions.md).

## Open Questions

- The **poly-time** version of Kaplan et al.'s separation, as opposed to the extraction-based one.
- Computational DP applied to reconstruction from model weights — verified unoccupied.
- Making the *intractability of the Bayes-optimal attack* itself the privacy quantity. Sablayrolles et
  al. (ICML 2019, arXiv:1908.11229) derive the optimal membership attack, find it intractable, and
  approximate it — treating that gap as engineering rather than as a security measure. Unoccupied.
