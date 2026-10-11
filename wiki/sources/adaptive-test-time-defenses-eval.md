---
title: Evaluating the Adversarial Robustness of Adaptive Test-time Defenses
type: source
date_ingested: 2026-08-20
authors: [Francesco Croce, Sven Gowal, Thomas Brunner, Evan Shelhamer, Matthias Hein, Taylan Cemgil]
venue: ICML (PMLR 162)
year: 2022
tags: [adversarial-ml, evasion-attacks, robustness, evaluation-methodology, threat-model]
claim_quantifier: empirical
antecedent: none
cls_target: outputs
cls_family: evade
cls_phase: test time
cls_access: white box
cls_write: read only
cls_frame: capability
cls_party: attacker
cls_unit: perturbation
cls_tightness: budget
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed: implicit
cls_evidence: "a norm bound ε > 0, an attack succeeds if it finds a perturbation δ such that arg max [f (x+δ)]k ≠ y, with ‖δ‖p ≤ ε and x + δ ∈ [0, 1]^d"
cls_evidence_src: §2.4 Eq. 2
cls_reason: "Rule 5 (perturbation budget) fixes party/unit/tightness/frame; defender inference cost is measured, not defined as a bound, so no second_party. assessed=implicit from the conclusion's compute-ratio remark, which floats attacker compute as a candidate quantity without a definition: \"we emphasize the need to measure gains in robustness against the computation required ... if the additional computation used by the defender can impose even more computation on the attacker\" (verified in wiki Quotes)."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

A case study of the defence family that [RobustBench](robustbench.md) had ruled inadmissible: defences that run an optimization loop at inference time. The paper first gives a taxonomy — two *principles*, input purification (IP) and model adaptation (MA), and four *building blocks*, iterative algorithm (IA), auxiliary network (AN), randomness (R), external data (ED) — then evaluates nine such defences from NeurIPS, ICLR, ICML, ICCV, AAAI and arXiv against `ℓ∞` perturbations at `ε = 8/255` on CIFAR-10.

The finding is uniform over the nine: every paper's reported robust accuracy is overestimated. Four of the nine (Wu et al.; Kang et al.; Hwang et al.; Mao et al.) *weaken* the underlying static model they wrap; the remaining ones give minor improvements. All nine raise inference cost, in one tabulated case by 59×. The recommendations section adds six steps to the [CAP+19 checklist](on-evaluating-adversarial-robustness.md), specialised to this family: transfer attacks that already work on the static model, black-box verification that the adaptive defence beats its own static base, strong white-box attacks (APGD with multiple losses and restarts) on the full defence, BPDA variants when gradients vanish through many iterations, EOT or seed-fixing for randomness, and, always, a hand-built adaptive attack.

For the survey strand this is the most interesting paper in the batch, because it is the only one that treats attacker compute as a candidate security quantity rather than a nuisance — and it does so in a single sentence of the conclusion, as a hope rather than a definition: "we emphasize the need to measure gains in robustness against the computation required. This weakness may be turned into a potential strength, if the additional computation used by the defender can impose even more computation on the attacker." That is the ratio idea — defender cost against attacker cost — stated informally, unparameterized, and not pursued. Elsewhere the paper treats inference cost purely as a liability: "Such high computational complexity calls into question the applicability of these defenses in the first place."

## Claim Boundary

- **Quantified over:** nine named adaptive test-time defences, at one threat model (`ℓ∞`, `ε = 8/255`, CIFAR-10, with `ε = 2/255` for Chen et al. and a reduced batch size for Mao et al.). "None significantly improve upon static defenses" ranges over these nine and no further. The stronger sub-claim — the adaptive defence does not improve on, and may weaken, its own static base — is asserted for the five cases where the static base is itself adversarially robust.
- **Antecedent:** none formally. Operationally, the results are conditional on the authors' attacks being close to optimal; the paper reports upper bounds on robust accuracy, like every empirical robustness evaluation, so a future stronger attack can only lower the numbers, never raise them. The direction of that error is the paper's protection.
- **Does not establish:** (a) that adaptive test-time defence is a dead end — explicitly denied: "we foresee that adaptive test-time defenses can still potentially lead to significant robustness gains, and clearly our results do not challenge the whole idea"; (b) that a standardized evaluation protocol for this family exists — explicitly denied, "we could not provide a standardized evaluation protocol"; (c) that the defender-imposes-attacker-cost idea works — it is offered as a possibility with no evidence, no formalization, and no experiment; (d) that AutoAttack is adequate here — the paper says AutoAttack "is not designed for adaptive test-time defenses", and Table 1 shows the most effective attack differs per defence.
- **Abstract vs theorem:** minor. The abstract's "none significantly improve upon static defenses when subjected to our careful case study evaluation" is correctly scoped by the trailing clause, but the title's "Adaptive Test-time Defenses" reads as the whole family when the evidence is nine members of it. The paper's own framing in §5 is properly scoped.

## Key Contributions

- Taxonomy of adaptive test-time defences: principles IP / MA; building blocks IA / AN / R / ED, with a table assigning each of the nine defences its blocks.
- Uniform overestimation finding across nine defences, with a relative reduction in claimed robust accuracy of more than 50% for four of them.
- The observation that four defences *reduce* the robustness of the static model they are built on.
- Six added checklist steps extending Carlini et al. 2019 to this family.
- Measurement of inference cost as a first-class column alongside robust accuracy (2× to 59× the static model).
- The suggestion — unformalized — that defender compute might be justified if it imposes more compute on the attacker.
- Identification of why the standard toolbox degrades here: BPDA "can be weaker for procedures consisting of many iterations", and differentiable optimization loops still produce vanishing or exploding gradients when unrolled far.

## Key Definitions / Theorems

No theorems. Definitions introduced:

- **Adaptive test-time defence**: a defence that alters its input or its parameters at inference, by optimizing an auxiliary loss or conditioning directly on the input — as opposed to a *static* defence, whose inputs and parameters are fixed at inference.
- **Input purification (IP)**: test-time optimization applied to the input before a (possibly pre-trained robust) model sees it.
- **Model adaptation (MA)**: test-time optimization applied to the model's parameters, state (e.g. batch-norm statistics), or activations.
- **Building blocks**: iterative algorithm, auxiliary network, randomness, external data.
- Adversarial risk is stated in the standard Madry form, `E_{(x,y)~D}[ max_{‖δ‖_p < ε} L(f(x+δ), y) ]`, with the explicit note that a sub-optimal `δ̂` gives a *lower* bound on adversarial risk, i.e. an *upper* bound on robust accuracy, and "may give a false sense of security".
- **Threat model** (§2.4): full white-box access to the classifier and all auxiliary models, including awareness of the test-time optimization; but *not* access to the random number generator's state.

## Connections

- Evaluates precisely the class excluded by restriction (3) of [RobustBench (CAS+21)](robustbench.md); shares two authors (Croce, Hein) with it.
- Explicitly extends the checklist of [On Evaluating Adversarial Robustness (CAP+19)](on-evaluating-adversarial-robustness.md).
- Applies the methodology of [On Adaptive Attacks to Adversarial Example Defenses (TCBM20)](adaptive-attacks-defenses.md) to one defence family, and inherits its conclusion that per-defence hand-built attacks are unavoidable.
- Its diagnosis of why BPDA weakens over long iteration chains refines [Obfuscated Gradients (ACW18)](obfuscated-gradients.md).
- The compute-ratio remark is the closest thing in the robustness-evaluation literature to the survey strand's target quantity; contrast with the outright rejection in [ACW18 §6.1](obfuscated-gradients.md) and [CAP+19 §4.8](on-evaluating-adversarial-robustness.md), and with the runtime-as-metric position of [SSK+24](sok-black-box-attack-pitfalls.md).
- Concepts: [Adaptive Attacks](../concepts/adaptive-attacks.md), [Obfuscated Gradients](../concepts/obfuscated-gradients.md), [Evasion Attacks](../concepts/evasion-attacks.md).
- Authors: [Francesco Croce](../entities/francesco-croce.md), [Matthias Hein](../entities/matthias-hein.md).

## Open Questions / Limitations

- The compute-ratio idea is left entirely undeveloped: no definition of the ratio, no units, no measurement of whether any of the nine defences achieves it, and no argument that it would constitute security. It names the question the survey strand is about and stops.
- Restricted to image classification and `ℓp` perturbations, by the authors' own scoping.
- No standardized protocol emerges. The paper concedes that the most effective attack differs per defence, so the taxonomy predicts which *techniques* may be needed but not which will work.
- Inference cost is measured as wall-clock runtime on the authors' hardware, with the acknowledgement that "many factors can influence this value". No hardware-independent cost measure is proposed.
- Randomized defences are evaluated with the attacker denied the RNG state, which is a real weakening of white-box access and is not discussed as such.

## Quotes / Notable Passages

The compute-ratio remark — the one place in this literature where attacker compute is floated as a security asset rather than a nuisance:

> "we emphasize the need to measure gains in robustness against the computation required. This weakness may be turned into a potential strength, if the additional computation used by the defender can impose even more computation on the attacker."

Compute treated as a liability, in the same paper:

> "Such high computational complexity calls into question the applicability of these defenses in the first place."

On the limits of the standard toolbox here:

> "BPDA, which is typically used in such circumstances and usually implemented as an identity function for the backward pass, can be weaker for procedures consisting of many iterations."

On the scope of the negative result:

> "we foresee that adaptive test-time defenses can still potentially lead to significant robustness gains, and clearly our results do not challenge the whole idea."
