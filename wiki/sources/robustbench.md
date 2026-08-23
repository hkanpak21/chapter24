---
title: RobustBench — a standardized adversarial robustness benchmark
type: source
date_ingested: 2026-08-20
authors: [Francesco Croce, Maksym Andriushchenko, Vikash Sehwag, Edoardo Debenedetti, Nicolas Flammarion, Mung Chiang, Prateek Mittal, Matthias Hein]
venue: NeurIPS Track on Datasets and Benchmarks
year: 2021
tags: [adversarial-ml, evasion-attacks, robustness, evaluation-methodology, certification]
claim_quantifier: empirical
antecedent: "The benchmarked model has non-zero input gradients, a deterministic forward pass, and no optimization loop in the forward pass; and AutoAttack's upper bound on robust accuracy is near-tight for such models. The three restrictions are enforced by admission; the near-tightness is measured, not proved."
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: white box
cls_write: read only
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: stated
cls_second_party: none
cls_second_notion: time
cls_assessed: explicit
cls_evidence: "We use the fixed budgets of ε∞ = 8/255 and ε2 = 0.5 for the `∞ and `2 leaderboards for CIFAR-10 and CIFAR-100"
cls_evidence_src: §3, Overall setup
cls_reason: "Rule 5: the leaderboard's only formal restriction is a fixed norm-ball radius, so party=attacker, unit=perturbation, frame=capability, even though the paper is empirical. Access=white box for the dominant APGD/FAB attacks in the ensemble; Square Attack is a black-box check, not the primary access mode. Second_notion=time: the paper separately treats attack cost as a \"similar computational cost\" tie-break for adopting a successor attack, an incomparable notion on the same party per rule 4b, and the Claim Boundary calls this a benchmark budget rather than a threat-model parameter, so it is not folded into the primary unit."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

RobustBench answers the reproducibility crisis documented by [ACW18](obfuscated-gradients.md) and [TCBM20](adaptive-attacks-defenses.md) by removing the evaluation from the defender's hands. Instead of asking authors to run good attacks, it runs one fixed attack ensemble — AutoAttack, four attacks run in sequence: APGD with cross-entropy loss, APGD with the difference-of-logits-ratio loss, targeted FAB, and the black-box Square Attack — against every submitted model, independently of the authors, and publishes the resulting robust accuracy on a leaderboard covering more than 120 evaluations, with a Model Zoo of 80+ checkpoints.

The design choice that makes this possible is a set of three *restrictions on admissible defences*: the model must have generally non-zero input gradients, a fully deterministic forward pass, and no optimization loop in the forward pass. These are the three obfuscation types of [ACW18](obfuscated-gradients.md) converted into admission criteria. The paper is explicit that this is a trade of coverage for reliability: "we thought that it is more important that the robustness evaluation is reliable, rather than being open to all possible defenses with the risk that the robustness is drastically overestimated", and it commits to lifting the restrictions when standardized evaluations for those modalities exist.

The benchmark also concedes the very objection [TCBM20](adaptive-attacks-defenses.md) raises against automated evaluation, and answers it procedurally rather than technically: AutoAttack carries a *flag* raised whenever the black-box Square Attack lowers robust accuracy by more than 0.2% relative to the white-box attacks — the black-box-beats-white-box indicator from [ACW18](obfuscated-gradients.md) — and flagged entries get hand-built adaptive attacks and external submissions. The one flagged case at publication (Xiao et al.) fell from 18.50% under AutoAttack to 7.40% under Square Attack with 30 restarts.

The compute question appears here in a form nobody else in the batch adopts: as a *benchmark budget*, not a threat-model parameter. The abstract's goal is robustness reflected "as accurately as possible ... within a reasonable computational budget", and the promotion rule for a successor attack is stated in cost-normalized terms: a new attack is adopted only if it beats AutoAttack "on a wide set of models given a similar computational cost". Attack cost thus governs which attack is standard, while remaining absent from what robustness *means*.

A secondary contribution uses the Model Zoo as a substrate: an analysis of how `ℓp`-robustness correlates with distribution shift, calibration, out-of-distribution detection, fairness, privacy leakage, smoothness and transferability. The reported findings include that robust models are significantly underconfident, and that not all robust models leak more privacy than standard ones.

## Claim Boundary

- **Quantified over:** models admitted to the benchmark — that is, models satisfying the three restrictions, evaluated at fixed `ε` (`ε∞ = 8/255` and `ε2 = 0.5` on CIFAR-10/100; `ε∞ = 4/255` on ImageNet), on CIFAR-10, CIFAR-100 and ImageNet, in the fully white-box setting. The claim that AutoAttack improves on the original evaluation is a measured regularity over the 120+ evaluated models ("consistently improves the results reported in the original papers for almost all the models"), not a universal.
- **Antecedent:** the three admission restrictions, plus the assumption that AutoAttack's upper bound is near-tight for admitted models. The restrictions are enforced, so they hold by construction. The near-tightness is *measured*, via the flag and via external adaptive re-evaluations, not proved — and the Xiao et al. case shows it can fail even for an admitted model. Every leaderboard number is an upper bound on true robust accuracy.
- **Does not establish:** (a) that leaderboard numbers are the true robust accuracy — "the exact robustness evaluation is computationally infeasible", and the paper deliberately reports only upper bounds, declining certified lower bounds as too loose; (b) that a high-ranking model is safe in deployment — stated outright: "a good performance on our benchmark does not guarantee the safety of the benchmarked model in a real-world deployment since `ℓp`- and corruption robustness may not be sufficiently representative of all realistic threat models"; (c) that excluded defences (zero-gradient, randomized, inference-loop) are worthless — the exclusion is about standardizability, and the paper concedes the resulting selection bias, "this can lead to a potential bias in our leaderboard"; (d) that AutoAttack cannot be overfitted — the paper anticipates overadaptation and invites external adaptive attacks for that reason.
- **Abstract vs theorem:** none found; the abstract is unusually careful, hedging with "as accurately as possible ... within a reasonable computational budget" and "possibly loosened in the future". The `ℓp` threat model is criticised in the paper's own §2 as "a necessary but not sufficient notion of robustness".

## Key Contributions

- A standing, independently-run leaderboard with a single fixed evaluation (AutoAttack) across 120+ models, plus a Model Zoo of 80+ checkpoints loadable in two lines.
- The three admission restrictions, derived from the [ACW18](obfuscated-gradients.md) obfuscation taxonomy, and the explicit rationale for trading coverage for reliability.
- The AutoAttack unreliability flag: raised when Square Attack beats the white-box attacks by more than 0.2%, plus automatic flags for restriction violations.
- The cost-normalized promotion rule for successor attacks ("similar computational cost").
- Independent verification: evaluations are run by the benchmark maintainers, not the model authors, and unverified entries (no checkpoint) are marked and removable.
- The cross-property analysis of 54+ CIFAR-10 robust models: calibration, distribution shift, OOD detection, fairness, privacy leakage, smoothness, transferability.

## Key Definitions / Theorems

No theorems proved. Definitions and cited facts:

- **Successful adversarial perturbation**: `δ ∈ ∆` with `arg max_c f(x+δ)_c ≠ y`, for perturbation set `∆ ⊆ R^d`, typically `∆_p = {δ : ‖δ‖_p ≤ ε}`.
- **Robust accuracy**: the fraction of datapoints classified correctly for *all* perturbations in `∆`.
- **Intractability, cited not proved**: "Computing the exact robust accuracy is in general intractable and, when considering `ℓp`-balls as `∆`, NP-hard even for single-layer neural networks" — attributed to Katz et al. and to Weng et al. This is the formal counterpart of the statement in [CAP+19 §2.2.2](on-evaluating-adversarial-robustness.md) that adversarial risk is intractable to compute exactly.
- **Upper vs lower bounds**: attacks give upper bounds on robust accuracy; certified methods give lower bounds. RobustBench reports only upper bounds, on the stated grounds that they are "typically much tighter".
- **AutoAttack**: the fixed four-attack ensemble, parameter-free, run sequentially on the points not yet broken.

## Connections

- Implements the restriction set derived from [Obfuscated Gradients (ACW18)](obfuscated-gradients.md), and adopts its black-box-beats-white-box indicator as the unreliability flag by way of [CAP+19](on-evaluating-adversarial-robustness.md).
- Motivated by, and partly answering, [On Adaptive Attacks to Adversarial Example Defenses (TCBM20)](adaptive-attacks-defenses.md), whose objection to automated evaluation it concedes and routes around via flagging plus external adaptive attacks.
- Restriction (3) is the exclusion that [Evaluating the Adversarial Robustness of Adaptive Test-time Defenses (CGB+22)](adaptive-test-time-defenses-eval.md) exists to test; two authors overlap.
- Named by [SoK: Analyzing Adversarial Examples (FK24)](sok-adversary-knowledge.md) as one of only two evaluation frameworks used by any attack paper in its survey — evidence for that paper's takeaway 5.
- Certified methods it declines to report are covered in [Certified Robustness via Randomized Smoothing](certified-robustness-randomized-smoothing.md), [Provably Robust SmoothAdv](provably-robust-smoothadv.md), and [Provable Defenses via the Convex Outer Adversarial Polytope](provable-defenses-convex-polytope.md).
- The measured robustness-accuracy trade-off across 54 CIFAR-10 models is the empirical counterpart of [Robustness May Be at Odds with Accuracy](robustness-at-odds-accuracy.md).
- Concepts: [Evasion Attacks](../concepts/evasion-attacks.md), [Adaptive Attacks](../concepts/adaptive-attacks.md), [Obfuscated Gradients](../concepts/obfuscated-gradients.md).
- Authors: [Francesco Croce](../entities/francesco-croce.md), [Matthias Hein](../entities/matthias-hein.md), [Prateek Mittal](../entities/prateek-mittal.md).

## Open Questions / Limitations

- The three restrictions bias the leaderboard toward defences that are easy to evaluate, which is not the same as defences that are good. The paper says so.
- A single standard attack invites overfitting to that attack. The mitigation is procedural (external adaptive evaluations) and depends on volunteer effort — the same dependency the paper criticises RobustML for.
- The flag detects one failure signature (black-box beating white-box) out of the five that [ACW18](obfuscated-gradients.md) lists.
- No lower bounds are reported at all, so the gap between the leaderboard number and true robust accuracy is unbounded and unmeasured.
- Attack cost enters only as a benchmark budget and as a tie-break rule for adopting a successor attack. Neither the leaderboard nor the definition of robust accuracy records what the attack cost to run against a given model, so a defence that raises attacker cost without raising robust accuracy is invisible to this benchmark by construction.

## Quotes / Notable Passages

On the intractability of the quantity being measured:

> "Computing the exact robust accuracy is in general intractable and, when considering `ℓp`-balls as ∆, NP-hard even for single-layer neural networks"

On the explicit trade of coverage for reliability:

> "we thought that it is more important that the robustness evaluation is reliable, rather than being open to all possible defenses with the risk that the robustness is drastically overestimated."

The cost-normalized rule for replacing the standard attack:

> "If in the future some new standardized and parameter-free attack is shown to consistently outperform AutoAttack on a wide set of models given a similar computational cost, we will adopt it as standard evaluation."

On what a leaderboard place does not mean:

> "a good performance on our benchmark does not guarantee the safety of the benchmarked model in a real-world deployment"
