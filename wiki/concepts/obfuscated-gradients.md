---
title: Obfuscated Gradients (Gradient Masking)
type: concept
tags: [adversarial-ml, evasion-attacks, robustness, evaluation-methodology]
---

## Definition

**Gradient masking** [Papernot et al. 2017, as cited by ACW18] names a defence that "does not have useful gradients" for generating adversarial examples.

**Obfuscated gradients** [Athalye–Carlini–Wagner, ICML 2018] is the sub-case where the masking is a necessary consequence of the defence's own construction rather than something the model learns: "the case where defenses are designed in such a way that the constructed defense necessarily causes gradient masking". Three types are distinguished:

- **Shattered gradients** — nonexistent or incorrect gradients, from non-differentiable operations (intentional) or numerical instability (unintentional).
- **Stochastic gradients** — the network or its input transform is randomized, so a single draw of the randomness misestimates the true gradient.
- **Exploding or vanishing gradients** — the defence is many iterations of network evaluation, which when unrolled behaves as an extremely deep network.

The concept is normative as well as descriptive: a defence exhibiting obfuscated gradients has, on this account, not reduced the set of adversarial perturbations; it has only made a particular optimizer fail to find them.

## Intuition

An `ℓp` attack estimates robust accuracy from above by searching for a counterexample. If the search fails, that is evidence of robustness only to the extent that the search was a good one. Obfuscated gradients break the search without touching the thing being searched for, so the estimate goes up while the truth stays put. The diagnostic value of the concept is that it identifies *why* an attack failed, which is the question a defence evaluation is really asking.

## Properties / Theorems

There are no theorems here — this is an empirical and diagnostic concept, and every claim about it in the literature is a claim about a named finite population of defences.

**Five behavioural indicators** [ACW18 §3.1], self-described as possibly incomplete ("These behaviors may not perfectly characterize all cases of masked gradients"):

1. One-step attacks perform better than iterative attacks.
2. Black-box attacks perform better than white-box attacks.
3. Unbounded attacks do not reach 100% success.
4. Brute-force random sampling finds adversarial examples where gradient descent does not.
5. Increasing the distortion bound does not increase attack success.

**Three circumvention techniques** [ACW18 §4], one per obfuscation type:

- **BPDA** for shattered gradients: forward pass through the true layer `f^i`, backward pass through a differentiable `g` with `g(x) ≈ f^i(x)`. The substitution must be backward-only; replacing `f^i` on both passes is reported as ineffective or much less effective.
- **EOT** for stochastic gradients: optimize `E_{t~T} f(t(x))`, using `∇ E_{t~T} f(t(x)) = E_{t~T} ∇ f(t(x))`.
- **Reparameterization** for vanishing or exploding gradients: change variables `x = h(z)` with `g(h(z)) = h(z)` and `h` differentiable.

**Empirical incidence, on one enumerated population**: 7 of the 9 non-certified ICLR 2018 defences claiming white-box robustness relied on obfuscated gradients; 6 were circumvented completely and 1 partially [ACW18].

**Known limits of the toolbox**: BPDA "can be weaker for procedures consisting of many iterations", and differentiable optimization loops can still vanish or explode when unrolled [CGB+22 §2.3]. EOT alone is not always sufficient for randomized defences [TCBM20, as cited by CAS+21].

## Where It Appears

- [Obfuscated Gradients (ACW18)](../sources/obfuscated-gradients.md) — origin of the term, the three-way taxonomy, the five indicators, and the three techniques.
- [On Evaluating Adversarial Robustness (CAP+19)](../sources/on-evaluating-adversarial-robustness.md) — the five indicators are absorbed into the checklist as sanity tests, and BPDA becomes a checklist item for non-differentiable components.
- [On Adaptive Attacks to Adversarial Example Defenses (TCBM20)](../sources/adaptive-attacks-defenses.md) — reuses BPDA and EOT rather than inventing new techniques, and identifies *loss inconsistency* as a distinct failure that is not gradient masking at all.
- [RobustBench (CAS+21)](../sources/robustbench.md) — the three admission restrictions (non-zero input gradients, deterministic forward pass, no inference-time optimization loop) are the three obfuscation types converted into eligibility criteria; the black-box-beats-white-box indicator becomes the AutoAttack unreliability flag.
- [Evaluating the Adversarial Robustness of Adaptive Test-time Defenses (CGB+22)](../sources/adaptive-test-time-defenses-eval.md) — documents where BPDA degrades, on defences with long iteration chains.

## Related Concepts

- [Adaptive Attacks](adaptive-attacks.md) — the methodology that obfuscation defeats and that must be rebuilt against it.
- [Evasion Attacks](evasion-attacks.md) — the attack class whose measurement obfuscation distorts.
- [Computational vs Information-Theoretic Robustness](computational-vs-it-robustness.md) — the formal notion under which an attack being hard to run *would* count as security. Obfuscated gradients is the informal case against granting that status to gradient-breaking defences, argued on the grounds that the hardness is optimizer-specific rather than adversary-general.

## Open Questions

- No characterisation exists of when an obfuscated defence is circumventable. Three techniques and a census are the whole state of the evidence; nothing predicts which property of a defence makes BPDA succeed.
- The five indicators are heuristics, admitted by their authors to be incomplete. Only one of them (black-box beating white-box) has been operationalised as an automated check, in [RobustBench](../sources/robustbench.md)'s flag.
- The boundary between *obfuscating gradients* and *raising attacker cost* is asserted, not defined. [ACW18 §6.1](../sources/obfuscated-gradients.md) rules that a ten-fold increase in attack time "has not increased" robustness, but supplies no threshold at which cost would count — the open definitional question that [CGB+22](../sources/adaptive-test-time-defenses-eval.md) later reopens by asking whether defender compute might impose more attacker compute.
- Randomized defences occupy an unresolved position: gradient stochasticity is listed as obfuscation, yet randomization also underwrites legitimate certified defences — see [Certified Robustness via Randomized Smoothing](../sources/certified-robustness-randomized-smoothing.md).
