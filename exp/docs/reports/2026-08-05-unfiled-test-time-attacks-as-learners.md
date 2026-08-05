---
id: test-time-attacks-as-learners
date: 2026-08-05
tag: unfiled
status: draft
supersedes: null
corrects: 2026-08-05-unfiled-attack-surface-decomposition.md
commit: null
cluster: n/a
jobs: []
pi_reviewed: false
---

# Training-time attacks act on a learner; test-time attacks are a learner

## Scope

[[2026-08-05-unfiled-attack-surface-decomposition]] indexes attack families by one axis, what the
adversary displaces, and a membership-inference adversary that chooses its queries breaks that index.
This report replaces the single axis with three, and it seats every attack the programme names in a
cell of the resulting table. The check runs over definitions already held, so it reads no new source.

## Result

**The attack surface separates on three independent axes, the phase of observation, the displacement,
and the target of `R`, and the test-time half of the resulting table then collapses to one object: an
adversary that runs a learning process whose input is the channel `f` and whose output is `z`.**

A membership-inference adversary that chooses its queries displaces `x` exactly as an adversarial
example does, but its criterion targets a property of `D` rather than of `f(x)`, so one axis cannot
separate them. Splitting the index into phase of observation, displacement, and criterion target seats
every named attack in a cell, including gradient inversion in split learning, which observes during
training yet displaces nothing and had no cell before.

| Attack | Phase of observation | Displacement | `R` target |
| --- | --- | --- | --- |
| Passive membership inference | test | none | a property of `D` |
| Active membership inference, chosen queries | test | `x` | a property of `D` |
| Adversarial example | test | `x` | a property of `f(x)` |
| Model extraction | test | `x` | a property of `f` |
| Gradient inversion, split or federated learning | training | none | a property of `D` |
| Backdoor | training | `f` | a property of `f` |
| Availability poisoning | training | `f` | a property of `f` |

The displacement axis is graded rather than binary, and its levels are the passive, chosen-plaintext,
and chosen-ciphertext hierarchy, so an access level times a criterion replaces any per-attack
definition.

| Displacement level | What the adversary may do | Cryptographic counterpart |
| --- | --- | --- |
| none | reads a transcript it did not choose | passive |
| `x`, non-adaptive | fixes its queries in advance | chosen-plaintext |
| `x`, adaptive | picks each query after reading the last answer | chosen-ciphertext |

| Half | What the adversary does | Input of that process | What `R` measures |
| --- | --- | --- | --- |
| Training-time | acts on a learner, perturbing the input of the learning process | the dataset `D` | the output of the learning process, a property of `f` |
| Test-time | is a learner, running inference on samples it partly controls | the channel `f`, which the defender fixed and built | the adversary's output `z` |

Does not show: that the three axes are independent in the sense of being freely combinable, since some
cells are empty, for example a training-time displacement of `x`.

## How it was produced

| | |
| --- | --- |
| Method | Re-derivation from the abstract setting, forced by a counterexample to the single-axis index |
| Corrects | [[2026-08-05-unfiled-attack-surface-decomposition]] |
| Counterexample | A membership-inference adversary that chooses its queries |
| Inputs | The terminology ledger in [[CONTEXT]]; the `R`-parameterized definition family, [[cohen-data-reconstruction]] |
| Checked against | [[planting-undetectable-backdoors]] and [[backdoor-defense-learnability-obfuscation]], the two training-time definitions held |
| Consistent with | [[haghifam-sample-complexity-mia]], which reports a sample complexity threshold for membership inference |
| Sources | None new; the sweep runs over definitions already held |
| Artifacts | This report |

## What this changes

The programme's recurring reading of attacks as learning problems is now literally true at test time
and only structurally true at training time. The two halves therefore need different machinery:
learning-theoretic thresholds, sample and query complexity and the information and generative
exponents, for the test-time half, and displacement geometry, the loss landscape and
[[fiber-of-the-training-map]], for the training-time half. Every `R`-parameterized definition held
covers the test-time family, and the two training-time definitions held are fixed games with
hard-coded success conditions, so the absence of an `R`-parameterized definition for the training-time
displacement family is the next thing to check properly and not yet a claim.

| Definition | Family covered | Parameterized by `R` |
| --- | --- | --- |
| Narcissus resiliency, Cohen et al. ITCS'25, [[cohen-data-reconstruction]] | test-time | yes |
| Reconstruction robustness, Balle-Cherubin-Hayes S&P'22, Hayes-Mahloujifar-Balle NeurIPS'23 | test-time | yes |
| PAC Privacy, Xiao-Devadas CRYPTO'23 | test-time | yes |
| Attaxonomy, Cummings-Hod-Sarathy-Swanberg 2024 | test-time | yes |
| Swanberg et al. arXiv:2507.08158 | test-time | yes |
| Defendability, CHLX25, [[backdoor-defense-learnability-obfuscation]] | training-time | no, a fixed game |
| Undetectable backdoors, GKVZ22, [[planting-undetectable-backdoors]] | training-time | no, a fixed game |

[[2026-08-05-unfiled-concrete-r-criteria]] supplies a candidate `R` for the training-time family, the
backdoor criterion, and marks it a candidate rather than a verified contribution.

## Where it applies

| Section | Change |
| --- | --- |
| Threat model | Replace the three-family displacement table with the three-axis cell table |
| Definitions | State the adversary as an access level times a criterion; name the access ladder as the passive, chosen-plaintext, chosen-ciphertext hierarchy |
| Terminology ledger, [[CONTEXT]] | Retire "the three attack families"; add "phase of observation" and "`R` target" as axes; record displacement as graded |
| Related work, [[related-work]] | Sort the reference problems by half: learning-theoretic thresholds for test time, displacement geometry for training time |
| Open problems | Check whether any `R`-parameterized definition covers the training-time displacement family |
