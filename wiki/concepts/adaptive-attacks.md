---
title: Adaptive Attacks
type: concept
tags: [adversarial-ml, evasion-attacks, robustness, threat-model, evaluation-methodology]
---

## Definition

An **adaptive attack** is an attack constructed *after* a defence has been completely specified, which exploits knowledge of that defence and is restricted only by the defence's stated threat model.

The canonical statement is [ACW18 §6.3]: "An adaptive attack is one that is constructed after a defense has been completely specified, where the adversary takes advantage of knowledge of the defense and is only restricted by the threat model."

The contrast class is a *static* or non-adaptive attack: an existing attack applied with default hyperparameters, or an adaptive attack that was built against a *previous* defence and reused. [TCBM20](../sources/adaptive-attacks-defenses.md) shows the second case is the one that now fails most often, and treats reuse of prior adaptive attacks as a category error.

Adaptive attacks matter because adversarial robustness is a *negative* goal: the defender must show that no attack succeeds, whereas the attacker need exhibit only one that does. Failure of an attack is therefore evidence about the attack unless the attack was built to target the defence.

## Intuition

Every reported robust-accuracy number is an upper bound produced by whatever attack was run. The bound's tightness is not observable. Adaptive attack methodology is the field's substitute for a tightness estimate: run the strongest attack a knowledgeable adversary could design, and treat the resulting bound as the working figure. This is why [CAP+19](../sources/on-evaluating-adversarial-robustness.md) requires assuming an "infinitely thorough" adversary and why [CGB+22](../sources/adaptive-test-time-defenses-eval.md) ends every recommendation list with "always try to implement adaptive attacks that are specific to adaptive defenses".

## Properties / Theorems

No theorems. The literature's substantive claims are methodological, plus one informal statement:

**Informal no-free-lunch statement** [TCBM20 conclusion]: "For any proposed attack, it is possible to build a non-robust defense that prevents that attack." The form is ∀ attack ∃ defence, the defence in question is non-robust, and no proof is offered. The consequence the authors draw is that evaluation against prior attacks — adaptive ones included — is a sanity check only, and that automated evaluation cannot be comprehensive.

**Six recurring themes** [TCBM20 §4], under the meta-theme T0 "strive for simplicity":
- T1 attack a function close to the full defence, end-to-end;
- T2 identify and target the important defence components;
- T3 adapt the objective (targeted, multi-targeted, or feature adversaries) to simplify the attack;
- T4 ensure the loss function is **consistent** — higher loss must mean a strictly stronger attack;
- T5 optimize the loss with different methods, including score-based and decision-based black-box attacks;
- T6 use a strong adaptive attack inside adversarial training, or the combined defence will be weaker than adversarial training alone.

**Loss inconsistency** (T4) is the sharpest of these and is not gradient masking: "even with an all-powerful optimizer that is guaranteed to find the loss' optimum, an attack may fail." It is a failure of the surrogate objective, not of the optimizer or of the compute spent on it. The condition is never formalized.

**Adoption without effect**: the fraction of defences evaluated adaptively went from near zero in 2017, to one third in 2018, to nearly all by 2020 — and thirteen defences from ICLR, ICML and NeurIPS that did perform adaptive evaluation were nonetheless circumvented [TCBM20]. The diagnosed cause is methodological, not technical: the tools already existed.

**Automation is contested.** [TCBM20](../sources/adaptive-attacks-defenses.md) argues no automated tool can suffice, and reports that AutoAttack only partially succeeds on two of the four defences they both evaluate. [RobustBench (CAS+21)](../sources/robustbench.md) concedes the point and answers procedurally: automate the common case, flag the suspicious case, invite hand-built external attacks for the flagged entries.

## Where It Appears

- [Obfuscated Gradients (ACW18)](../sources/obfuscated-gradients.md) — the definition, and the per-example reporting rule `mean_x min_{a∈A} f(a(x))` rather than `min_{a∈A} mean_x f(a(x))`.
- [On Evaluating Adversarial Robustness (CAP+19)](../sources/on-evaluating-adversarial-robustness.md) — makes adaptive evaluation the central requirement, retracts the zero-knowledge threat model, and asserts the "infinitely thorough" adversary.
- [On Adaptive Attacks to Adversarial Example Defenses (TCBM20)](../sources/adaptive-attacks-defenses.md) — the reference treatment; thirteen worked case studies in discovery order, the six themes, the informal no-free-lunch statement.
- [Evaluating the Adversarial Robustness of Adaptive Test-time Defenses (CGB+22)](../sources/adaptive-test-time-defenses-eval.md) — six added steps specialised to inference-time-optimization defences.
- [RobustBench (CAS+21)](../sources/robustbench.md) — the attempt to standardize what [TCBM20](../sources/adaptive-attacks-defenses.md) says cannot be standardized, with admission restrictions and an unreliability flag as the compromise.
- [SoK: Pitfalls in Evaluating Black-Box Attacks (SSK+24)](../sources/sok-black-box-attack-pitfalls.md) — the black-box analogue of the "adapt the baseline too" lesson: several state-of-the-art claims dissolve once the *baseline* is granted the same knowledge as the new attack.

## Related Concepts

- [Obfuscated Gradients](obfuscated-gradients.md) — the failure mode adaptive attacks were first built to defeat.
- [Evasion Attacks](evasion-attacks.md).
- [Adversary Knowledge Taxonomy](adversary-knowledge-taxonomy.md) — an attack "only restricted by the threat model" is only as precise as that threat model's account of adversary knowledge, which is what this concept formalizes.

## Open Questions

- There is no positive criterion for a *sufficient* adaptive attack. The methodology says what a good one looks like after the fact; by [TCBM20](../sources/adaptive-attacks-defenses.md)'s own argument no procedure for producing one can exist.
- Loss consistency (T4) is stated informally and never defined. A formal monotonicity condition relating a surrogate loss to the 0-1 success indicator would be checkable; none is given.
- **Attacker cost is absent from the whole methodology.** Adaptive-attack papers report attack *designs*, not attack *budgets*. [ACW18 §6.1](../sources/obfuscated-gradients.md) and [CAP+19 §4.8](../sources/on-evaluating-adversarial-robustness.md) rule the question out of the threat model deliberately; [SSK+24](../sources/sok-black-box-attack-pitfalls.md) reintroduces runtime, but only to rank attacks against each other, never to grade a defence; [CGB+22](../sources/adaptive-test-time-defenses-eval.md) asks in one sentence whether defender compute could impose more attacker compute, and does not pursue it. No definition in this literature is parameterized by attacker compute.
- Whether the difficulty of designing an adaptive attack is itself a security-relevant quantity is never asked. It is human design effort, not machine computation, and nothing in the field measures it.
