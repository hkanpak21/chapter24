---
title: "Certified Defenses for Data Poisoning Attacks"
type: source
date_ingested: 2026-04-23
authors: [Jacob Steinhardt, Pang Wei Koh, Percy Liang]
venue: "NeurIPS 2017 (venue unconfirmed from PDF: raw/SKL17_CertifiedPoisoningDefenses.pdf is arXiv:1706.03691v2 [cs.LG] and names no venue; the attribution is carried over from the earlier ingest)"
year: 2017
tags: [poisoning-attacks, certified-defenses, adversarial-ml, robust-statistics, data-sanitization]
claim_quantifier: conditional
antecedent: "Two assumptions the paper states and does not verify: that the dataset is large enough for statistical concentration between train and test error to hold, and that outliers within the clean data do not have a strong effect on the model. The defender is further restricted to outlier removal followed by minimisation of a margin-based loss. The bound is described by the authors as approximate, not exact."
date_verified: 2026-08-20
cls_target: train data
cls_family: poison
cls_phase: train time
cls_access: none
cls_write: corpus
cls_frame: capability
cls_party: attacker
cls_unit: corruption
cls_tightness: budget
cls_baseline: absent
cls_baseline_checked: yes
cls_second_party: algo class
cls_second_notion: none
cls_assessed: explicit
cls_evidence: "The attacker adaptively chooses a \"poisoned\" dataset Dp of εn poisoned points, where ε ∈ [0, 1] parametrizes the attacker's resources."
cls_evidence_src: "§2 (causative attack model)"
cls_reason: "Rule 5: a poisoning fraction is a corruption budget, so party=attacker, unit=corruption, tightness=budget, frame=capability, matching the norm-ball example. Attacker is explicitly unbounded computationally ('has full knowledge of the defender's algorithm and of the clean training data'). second_party = algo class because the certificate only holds for defenders restricted to outlier removal + margin-based ERM, an explicit architectural restriction (Rule 4: neither party is computationally bounded, so the attacker's bound decides the primary row and the defender's algorithm-class restriction is the second party). baseline = stated: the paper reports poisoned test error against the clean (unpoisoned) test error as the comparison point, e.g. 12% to 23% on IMDB."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (SKL17) provides the **first framework for certified worst-case bounds** on the loss of a defender against arbitrary data-poisoning attackers. For defenders that first perform outlier removal (data sanitization) and then minimize a margin-based loss, the paper constructs approximate upper bounds on the worst-case test loss *across the entire space of possible poisoning attacks*, not merely against specific known attacks. The bound relies on two assumptions: (1) the clean data is large enough for train/test concentration to hold, (2) outliers within clean data do not unduly influence the model.

A key methodological contribution is **duality**: the paper converts the upper bound into a candidate attack that often nearly saturates the bound, giving defenders both a worst-case loss certificate and a concrete attack to verify it empirically. This "matching attack + bound" structure becomes the template for subsequent certified poisoning defense analyses.

Empirical findings reveal **dataset-dependent vulnerability**: under an oracle sphere-and-slab defense (knowing true class centroids), MNIST-1-7 and Dogfish are certified resilient (≤4% error increase with 30% poisoning); but IMDB sentiment is dramatically vulnerable (test error increases from 12% → 23% with only 3% poisoning). The gap reflects that high-dimensional, feature-sparse datasets give attackers more room to craft attacks that evade outlier removal.

A crucial secondary insight: **data-dependent defenders** (using the poisoned data to estimate distribution parameters) are much weaker than **data-independent oracle defenders** — on MNIST-1-7 with 30% poisoning, data-dependent defenses allow up to 40% test error vs. 7% for oracle. This motivates robust estimation techniques that are themselves resistant to poisoning (the direction [Diakonikolas et al. 2016](robust-estimators-high-dimensions.md) pioneered).

## Claim Boundary

- **Quantified over:** all attacks within a budget, for one defender architecture — outlier removal followed by margin-based empirical risk minimisation — on a given dataset. The certificate is per-dataset and per-defence, computed numerically; it is not a theorem about poisoning in general.
- **Antecedent:** the two assumptions above. Neither is checkable from the data the defender holds, which the page's limitations section already records. A certificate that rests on an unverifiable hypothesis is a conditional guarantee, and should be reported as one.
- **Which party is constrained:** the **attacker**, in the number of poisoned points it may inject, εn, and in having to survive the sanitizer. Its computation is unbounded, and the bound is over all attacks in that budget rather than over efficient ones. The **defender** is constrained by architecture — outlier removal plus a margin-based loss — which is what makes the bound computable. Neither party is priced in time.
- **Does not establish:** (i) any guarantee for neural networks or non-convex losses; (ii) an exact bound, since the construction is approximate and its tightness is evidenced by a matching attack rather than proved; (iii) that data-dependent defences are safe — the paper's finding is the opposite, and that gap is one of its more useful results; (iv) that a dataset certified here resists an attacker with a different objective, since the game fixes the loss.
- **Abstract vs theorem:** none found. The abstract names the approximation and both assumptions in its own sentences.

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

> "On the other hand, on the IMDB sentiment corpus (Maas et al., 2011) our attack increases classification test error from 12% to 23% with only 3% poisoned data, showing that defensibility is very dataset-dependent"
>
> _Corrected 2026-08-20 against `raw/SKL17_CertifiedPoisoningDefenses.pdf`: the inline citation had been dropped without an ellipsis, and the sentence in the paper continues past a colon rather than ending. The reported numbers are as printed._

The two assumptions the certificate rests on, from the abstract:

> "Our approximation relies on two assumptions: (1) that the dataset is large enough for statistical concentration between train and test error to hold, and (2) that outliers within the clean (non-poisoned) data do not have a strong effect on the model."
