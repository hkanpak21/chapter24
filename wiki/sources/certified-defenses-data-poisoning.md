---
title: "Certified Defenses for Data Poisoning Attacks"
type: source
date_ingested: 2026-04-23
authors: [Jacob Steinhardt, Pang Wei Koh, Percy Liang]
venue: NeurIPS 2017
year: 2017
tags: [poisoning-attacks, certified-defenses, adversarial-ml, robust-statistics, data-sanitization]
---

## Summary

This paper (SKL17) provides the **first framework for certified worst-case bounds** on the loss of a defender against arbitrary data-poisoning attackers. For defenders that first perform outlier removal (data sanitization) and then minimize a margin-based loss, the paper constructs approximate upper bounds on the worst-case test loss *across the entire space of possible poisoning attacks*, not merely against specific known attacks. The bound relies on two assumptions: (1) the clean data is large enough for train/test concentration to hold, (2) outliers within clean data do not unduly influence the model.

A key methodological contribution is **duality**: the paper converts the upper bound into a candidate attack that often nearly saturates the bound, giving defenders both a worst-case loss certificate and a concrete attack to verify it empirically. This "matching attack + bound" structure becomes the template for subsequent certified poisoning defense analyses.

Empirical findings reveal **dataset-dependent vulnerability**: under an oracle sphere-and-slab defense (knowing true class centroids), MNIST-1-7 and Dogfish are certified resilient (≤4% error increase with 30% poisoning); but IMDB sentiment is dramatically vulnerable (test error increases from 12% → 23% with only 3% poisoning). The gap reflects that high-dimensional, feature-sparse datasets give attackers more room to craft attacks that evade outlier removal.

A crucial secondary insight: **data-dependent defenders** (using the poisoned data to estimate distribution parameters) are much weaker than **data-independent oracle defenders** — on MNIST-1-7 with 30% poisoning, data-dependent defenses allow up to 40% test error vs. 7% for oracle. This motivates robust estimation techniques that are themselves resistant to poisoning (the direction [Diakonikolas et al. 2016](robust-estimators-high-dimensions.md) pioneered).

## Key Contributions

- **Certified upper bound on poisoning-induced test loss**: for any attack, for defenders performing outlier removal + margin-based ERM, max_D_p L(θ̂) ≤ f(defense, clean data) (approximately, under assumptions 1-2).
- **Duality-based matching attack**: a candidate attack derived from the bound's dual, often saturating the bound.
- **Dataset-dependent vulnerability characterization**: empirical demonstration that same defense has dramatically different certified robustness on MNIST-1-7 vs. IMDB.
- **Data-independent vs data-dependent defense gap**: formalized the significant weakening when outlier detectors use the poisoned data to estimate distribution parameters.
- **Online-learning-based solver**: efficient algorithm for computing both the bound and the matching attack.
- **Template for certified poisoning analysis**: structure (upper bound + matching attack) widely adopted in subsequent work.

## Key Definitions / Theorems

- **Causative attack game**: (1) n clean data points drawn from p*, (2) attacker chooses εn poisoned points, (3) defender sanitizes then ERMs on D_c ∪ D_p ∩ F to get θ̂, (4) defender incurs test loss L(θ̂).
- **Feasible set F**: data sanitization defense; points in F are retained for training. Can be fixed (data-independent) or data-dependent.
- **Sphere defense**: F_sphere = {(x, y) : ∥x − μ_y∥₂ ≤ r_y}. Removes points too far from their class centroid.
- **Slab defense**: F_slab = {(x, y) : |⟨x − μ_y, μ_y − μ_{−y}⟩| ≤ s_y}. Removes points too far along the inter-class axis.
- **Main theorem (informal)**: under train/test concentration and outlier-influence assumptions, the worst-case test loss over any attack with budget ε is ≤ approximate upper bound computable via online learning.

## Connections

- Source: [Robust Estimators in High Dimensions (Diakonikolas et al. 2016)](robust-estimators-high-dimensions.md) — provides the algorithmic-robust-statistics foundation; this paper is the classification analog.
- Source: [Robustly-Reliable Learners Under Poisoning (Balcan et al. 2022)](robustly-reliable-learners-poison.md) — later work providing instance-targeted correctness certificates (not just stability).
- Source: [Curse of Concentration (MDM19)](curse-of-concentration.md) — establishes upper bounds on poisoning-attack power via concentration; SKL17 gives the complementary certified-defense lower bound.
- Source: [Universal Multi-Party Poisoning (MMM19)](multi-party-poisoning.md) — universal upper bound on attack power.
- Source: [Reducibility and Statistical-Computational Gaps](reducibility-statistical-computational-gaps.md) — Brennan-Bresler on sparse robust mean estimation; complementary perspective on poisoning hardness.
- Concept: [Poisoning Attacks](../concepts/poisoning-attacks.md) — the attack framework.
- Concept: [Reliable Learning](../concepts/reliable-learning.md) — certification perspective.
- Authors: Pang Wei Koh, Percy Liang (Stanford).

## Open Questions / Limitations

- **Approximation gap**: the upper bound is approximate; constants and exact tightness are left open.
- **Limited to margin-based losses + outlier removal**: framework does not directly cover neural networks, ERM with non-convex loss, or modern deep-learning pipelines.
- **Assumptions 1–2 are not formally verifiable**: concentration of train/test and bounded outlier influence are assumed rather than derived.
- **Data-dependent defenses**: the paper shows they are weaker but does not provide a systematic robust-estimator solution — this is what Diakonikolas et al. and follow-ups address.
- **Adaptive attacks against the specific upper-bound algorithm**: the matching attack handles this for the specific framework, but broader adaptive analysis is open.

## Quotes / Notable Passages

> "Are there defenses that are robust to a large class of data poisoning attacks? At development time, one could take a clean dataset and test a defense against a number of poisoning strategies on that dataset. However, because of the near-limitless space of possible attacks, it is impossible to conclude from empirical success alone."

> "Defenses that rely on the (potentially poisoned) data can be much weaker than their data-independent counterparts, underscoring the need for outlier removal mechanisms that are themselves robust to attack."

> "On the IMDB sentiment corpus our attack increases classification test error from 12% to 23% with only 3% poisoned data, showing that defensibility is very dataset-dependent."
