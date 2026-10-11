---
title: Unit of Protection
type: concept
tags: [privacy, differential-privacy, definitions, memorization]
---

## Definition

The **unit of protection** of a security or privacy definition is the object whose presence or absence the guarantee quantifies over — the thing that, if withheld, the definition promises the adversary cannot detect.

In ε-differential privacy the unit is the **record**: A satisfies ε-DP iff for any datasets D, D′ *differing in only one record* and any output set S, Pr[A(D) ∈ S] ≤ e^ε Pr[A(D′) ∈ S]. The word "record" is left undefined by the definition itself, and every semantic property of the guarantee is inherited from how it is instantiated.

## Intuition

Three questions are routinely collapsed into "is this secure?", and they are independent:

1. **What is protected** — the unit of protection. Record, user, secret, sample, model weight, training run.
2. **Against whom** — the adversary's knowledge and, separately, the adversary's *resources*.
3. **Under what evaluation** — the protocol that produces the claim.

A definition can be formally impeccable on axis 2 and still promise almost nothing, if its unit on axis 1 does not correspond to the thing anyone wanted protected. This is the failure [BLM+22](../sources/language-model-preserve-privacy.md) diagnoses for language models, and it is why that paper must not be filed as evidence about adversary capability.

## Properties / Theorems

**The granularity ladder for DP records** ([BLM+22](../sources/language-model-preserve-privacy.md), §5), with the argument at each rung:

| Unit | Convenient because | Fails because |
|---|---|---|
| token / word / sentence | matches training batch granularity | removing one sentence rarely removes a piece of private information |
| document | natural file boundary | same, at coarser scale |
| user (user-level DP) | the reading the original DP definition intends | removing all of one user's text does not remove information others wrote about them |
| secret ("secret-level DP") | the actual target | requires knowing the context and boundaries of secrets — exactly what DP was designed to avoid needing |

**Group degradation asymmetry.** DP for a group of size k degrades exponentially in k, whereas the sensitivity of information does not fall as more people know it. Community-held secrets therefore receive no meaningful guarantee.

**Scope of the failure.** The criticism is conditional and lapses where the unit fits: DP remains meaningful when each individual contributes a record of sensitive attributes about themselves, or when a user's secrets are confined to text that user wrote. It is language — where information spans authors, refers obliquely, and concerns non-contributors — that breaks the alignment.

**Formal soundness is untouched.** BLM+22 states that DP's guarantees "hold regardless of such relationships in the dataset D"; what is questioned is what they mean semantically. A unit-of-protection critique is never a refutation of the bound.

## Where It Appears

- [What Does it Mean for a Language Model to Preserve Privacy? (BLM+22)](../sources/language-model-preserve-privacy.md) — the axis's clearest statement, including the section heading "Protecting a specific unit of data is not the same as protecting privacy."
- [Deep Learning with Differential Privacy (ACG+16)](../sources/deep-learning-differential-privacy.md) — the mechanism whose record granularity is at issue.
- [Cohen et al. — Data Reconstruction](../sources/cohen-data-reconstruction.md), [Kaplan et al. — Bayesian Memorization and Reconstruction](../sources/kaplan-bayesian-memorization-reconstruction.md), [Dinur–Nissim](../sources/dinur-nissim-revealing-information.md) — reconstruction notions, where the unit is a training row and the question is whether it can be recovered.
- [Xiao — Formal Privacy Proof for Data Encoding](../sources/xiao-formal-privacy-proof-data-encoding.md).

## Related Concepts

- [Computational vs Statistical Memorization](computational-vs-statistical-memorization.md) — orthogonal axis: same unit, adversary priced differently.
- [Backdoor Defense Evaluation](backdoor-defense-evaluation.md) — the evaluation axis (3 above).
- [Computational Indistinguishability](computational-indistinguishability.md), [Defendability](defendability.md).

## Open Questions

- **Is there a unit between user-level and secret-level?** BLM+22 names both endpoints and shows the upper one self-defeating. Footnote 5 tries expanding "user data" to all conversations the user participated in, and finds it both harder under federated learning and still insufficient. Nothing occupies the middle.
- Can the unit of protection be made a *parameter* of a definition rather than a fixed choice, so that a guarantee reads "ε-DP at granularity g" and results compose across g? Prior work has used token, sentence, document and user granularities but not as a single indexed family.
- The three axes above are usually stated only one or two at a time. A definition indexed simultaneously by unit of protection *and* adversary resource budget does not appear in this wiki's sources.
- BLM+22's own closing question: whether DP's formal underpinnings make it the privacy notion of choice for language models at all, or whether a semantically meaningful but heuristic notion would serve better.
