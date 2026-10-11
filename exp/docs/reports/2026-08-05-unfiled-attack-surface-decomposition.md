---
id: attack-surface-decomposition
date: 2026-08-05
tag: unfiled
status: draft
supersedes: null
commit: null
cluster: n/a
jobs: []
pi_reviewed: false
---

# Training-time attacks are displacements of the learned function, not alterations of the loss

## Scope

This settles the question of whether every training-time attack can be expressed as an alteration of
the loss, which is the candidate unification for the training half of the theory. The method is a
derivation from the abstract setting (a dataset, a well-behaved function space, a loss criterion, a
traversal) together with a check against the two constructions the programme already holds.

## Result

**Loss alteration is too narrow, but a correct invariant exists one level up: every training-time
adversary displaces the function the traversal reaches, and loss increase is one success criterion `R`
over that displacement rather than the general form.**

The counterexample is the undetectable backdoor: one that raised the clean loss would be caught by
held-out evaluation, so a successful one preserves clean loss essentially exactly and is a
redistribution rather than an increase. The apparent two-phase nature of backdoors also dissolves,
because the phase of action and the phase of measurement differ — the act displaces `f` at training
time, and `R` is evaluated at test time on a trigger. Indexing by what the adversary displaces then
gives a decomposition that is complete by construction, since it enumerates what can be touched rather
than what has been named.

| Family | What is displaced | What `R` is evaluated on | Existing names |
| --- | --- | --- | --- |
| Training-time | the learned function `f` | a property of `f` | availability poisoning, targeted poisoning, backdoors, unlearning forgery |
| Test-time passive | nothing; observation only | a property of `D` or of `f` | membership inference, reconstruction, attribute and property inference, extraction |
| Test-time active | the input `x` | a property of `f(x)` | adversarial examples, jailbreaks, prompt injection |

Does not show: that the three families are mutually irreducible, only that they are exhaustive over
displacement targets.

Corrected by [[2026-08-05-unfiled-test-time-attacks-as-learners]]: displacement alone does not
separate a chosen-query membership-inference adversary from an adversarial example, and the correct
index carries three axes.

## How it was produced

| | |
| --- | --- |
| Method | Derivation from the abstract setting, checked against two held constructions |
| Checked against | GKVZ22 undetectable backdoors (`wiki/sources/planting-undetectable-backdoors.md`); GJMM20 signature wrapper (`wiki/sources/computational-hardness-robust-learning.md`) |
| Inputs | The `R`-parameterized definition family, `wiki/sources/cohen-data-reconstruction.md` |
| Artifacts | This report |

## What this changes

The training half of the theory now has a single object, the displacement of `f`, with attack families
distinguished by the criterion `R` applied to it rather than by a taxonomy of named attacks. The
programme can therefore carry one definition across both halves, since the test-time passive family is
already `R`-parameterized in the literature. Any statement that training-time security is a bound on
loss degradation is now too strong and must be restated as a bound at a stated `R`.

## Where it applies

| Section | Change |
| --- | --- |
| Threat model | Replace the attack taxonomy with the three-family displacement table |
| Definitions | `R` is the single parameter across both phases; loss is one instantiation |
| Related work | GKVZ22 is a displacement with `R` = trigger behaviour, not a loss attack |
