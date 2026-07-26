---
title: The Sample Complexity of Membership Inference and Privacy Auditing
type: source
date_ingested: 2026-07-26
authors: [Mahdi Haghifam, Adam Smith, Jonathan Ullman]
venue: "arXiv:2508.19458 (Aug 2025)"
year: 2025
tags: [sample-complexity, adversarial-ml, learning-theory, reconstruction]
---

> **Provenance.** Verified sweep; Theorem 1.1 quoted verbatim. **Highest-priority read in the corpus** —
> this is the nearest published neighbour to the programme's central claim, and §1.3's technique
> determines whether the programme is a thesis or a race.

## Summary

Asks how many samples a membership-inference attacker needs, as opposed to how much it can achieve with
unlimited data. The answer is a **quadratic separation**: for Gaussian mean estimation, an attacker
needs `m ≳ n²ρ² + n` samples where the trainer used `n`. In the regime `ρ = ω(n^{-1/2})`, that is
`ω(n)` — strictly more than the trainer.

The authors state the significance themselves: this is *"the first to show that the attacker sometimes
needs many more samples than the [training algorithm uses]."*

**This is the shape of the programme's proposed first theorem, already proved.** What differs is the
units: theirs are information-theoretic (Ingster/χ²-style), and their adversary is computationally
unbounded — bounded only in samples. The programme's remaining room is the computational restatement.

## Key Contributions

- The first attacker-versus-trainer sample-complexity separation for membership inference.
- Identification of covariance estimation as the driver: with known covariance the bound collapses.
- A privacy-auditing consequence — auditing needs far more data than training did.

## Key Definitions / Theorems

- **Theorem 1.1 (verbatim, informal version of Thm 3.1):** *"Fix n, ρ, d, and assume d ≳ d★(n,ρ) ≜
  n + n²ρ², i.e., the dimension is large enough for a fully-informed attacker to succeed. Then, every
  sample-based MIA for the Gaussian mean estimation problem requires m ≳ n²ρ² + n samples. Moreover, the
  lower bound holds even when we restrict attention to the specific mean estimator
  μ̂ = (1/n)Σᵢ Xᵢ + ρZ where Z ∼ N(0,Σ)."*
- **Theorem 1.2 (formal Thm 4.1):** with known covariance, `m ≳ min{n, 1/ρ²}` — hence *"the driver of
  high sample complexity in MIA is estimating the covariance of the population."*

## Connections

- **The programme's designated predecessor.** The revised pitch is: they proved the information-theoretic
  version, the programme proves the computational one in SGD-native units. See
  [native-asymmetry-in-learning](../analyses/native-asymmetry-in-learning.md) §4.
- Contrast [Cohen et al. ITCS'25](cohen-data-reconstruction.md), which bounds the *adversary's time*
  rather than its samples.
- The exponent instrument that would restate this: information/generative exponent — see
  [native-computational-problems-survey](../../output/native-computational-problems-survey.md) §5.
- Concept: [computational-vs-statistical-memorization](../concepts/computational-vs-statistical-memorization.md).

## Open Questions / Limitations

- **The competitive hazard.** If §1.3's lower-bound technique is Ingster-style χ², it is one step from a
  low-degree or SQ restatement, and that step is available to anyone who reads the paper. Verify this
  first.
- Gaussian mean estimation only; no neural network, no SGD.
- The attacker is sample-bounded but computationally unbounded — the whole computational axis is untouched.

## Quotes / Notable Passages

> "Our result is the first to show that the attacker sometimes needs many more samples than the
> [training algorithm]."
