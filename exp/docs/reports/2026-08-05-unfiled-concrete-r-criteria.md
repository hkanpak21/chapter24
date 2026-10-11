---
id: concrete-r-criteria
date: 2026-08-05
tag: unfiled
status: draft
supersedes: null
builds_on: 2026-08-05-unfiled-test-time-attacks-as-learners.md
commit: null
cluster: n/a
jobs: []
pi_reviewed: false
---

# Four criteria, derived: `R`'s parameters are the reference problem's parameters

## Scope

[[2026-08-05-unfiled-test-time-attacks-as-learners]] indexes an attack as an access level times a
success criterion `R`, and it leaves open whether reaching a computational problem from a chosen `R`
needs a further mapping step. This report instantiates `R` four times, twice on a released noisy mean,
once on a training-time displacement and once on query access to a model, then reads off the
reference problem and the baseline in each case. The derivations run over settings already held, so no
new source is read.

## Result

**`R` does not need a separate mapping step to reach a computational problem. Fixing `R` fixes what
the adversary must produce, which fixes the estimation or search problem it is solving, and the
parameters of `R` appear unchanged as the parameters of that problem.**

Each derivation below carries the same seven fields, and the reference problem is read off the
criterion rather than constructed for it.

### R1, reconstruction from a noisy mean

| Field | Value |
| --- | --- |
| Source | `x_1` to `x_n`, drawn independently from `N(μ, I_d)` |
| Release | `w = x̄ + ρZ`, with `x̄` the sample mean and `Z` drawn from `N(0, I_d)` |
| `R` | `R(S, z) = 1` exactly when `‖z - x_i‖ ≤ η` for some `x_i` in `S` |
| Free parameters | `η`, the tolerance; `ρ`, the release noise; `n`; `d` |
| Reference problem | Gaussian location estimation, in which `η` is the estimation precision, so no translation occurs |
| Baseline | the prior-only adversary picks the best fixed `z` and achieves the Gaussian ball measure `Pr[‖z - x‖ ≤ η]`, which is exponentially small for `η` far below `√d` |
| Baseline degenerate | no, so the baseline-subtracted advantage is meaningful here |
| Related | [[haghifam-sample-complexity-mia]] reports attacker sample complexity `m ≳ n²ρ² + n` for the membership variant of this same setting |

### R2, membership as the limit of R1 at zero tolerance

| Field | Value |
| --- | --- |
| Source | as in R1 |
| Release | as in R1 |
| `R` | `R(S, z) = 1` exactly when `z` is a bit that correctly reports whether a challenge point lies in `S` |
| Free parameters | none beyond the setting, because the criterion is binary |
| Reference problem | two-point hypothesis testing, in the Ingster chi-squared form |
| Baseline | one half, by construction |
| Baseline degenerate | yes, so raw advantage must be used and baseline-subtracted advantage must not |
| Related | this reproduces the defect recorded against `COMP-MEM` in the repository record, and R2 shows the defect belongs to the criterion rather than to the game |

### R3, the backdoor criterion, for the training-time displacement family

| Field | Value |
| --- | --- |
| Source | an honest training map, which produces `f` |
| Release | the displaced model `f*`, published in place of `f` |
| `R` | `R(f*, z) = 1` exactly when `f*(z)` differs from `f(z)` and `z` is admissible, meaning `z` lies in the allowed input domain |
| Free parameters | the admissibility constraint on `z`; `ε`, the clean-agreement budget bounding `Pr_{x~D}[f*(x) ≠ f(x)]` |
| Reference problem | finding a rare input on which two functions disagree, a search problem over the input domain, hard in [[planting-undetectable-backdoors]] because the trigger is cryptographically hidden |
| Baseline | random search over the domain, which succeeds with probability equal to the measure of the trigger set |
| Baseline degenerate | no, whenever the trigger set is small |

**In the privacy criteria the attacker is the party trying to achieve `R`, and in the backdoor
criterion the detector is. `R` is achieved by whichever party is searching, and that party changes
with the family.**

One `R`-parameterized definition can therefore cover both halves, and R3 is a candidate for the
training-time definition that [[2026-08-05-unfiled-test-time-attacks-as-learners]] reports missing.

### R4, fidelity, shared by distillation and by extraction

| Field | Value |
| --- | --- |
| Source | a target model `f` |
| Release | query access to `f`, at a stated query budget |
| `R` | `R(f, ĝ) = 1` exactly when `Pr_{x~D}[ĝ(x) ≠ f(x)] ≤ ε`, for a second party that trains `ĝ` on the answers of `f` |
| Free parameters | `ε`, the fidelity tolerance; the query budget |
| Reference problem | learning the concept class containing `f` from a labeling oracle, with sample complexity controlled by the Vapnik-Chervonenkis dimension and computational cost set by the class |
| Baseline | the best fixed hypothesis chosen without querying |
| Baseline degenerate | no, provided `f` is not close to a constant |
| Consequence | the distillation student and the extraction adversary share the access level, the criterion, the algorithm and the sample complexity, and differ only in authorization, which is not a mathematical property |

### The dial, from describing a population to inverting a map

| Setting of `η` | Baseline | The task | What is available |
| --- | --- | --- | --- |
| coarse | rises | describing the population | no confidentiality is violated, and no hardness is available |
| tight | vanishes | inverting a lossy map | the cryptographic regime |

The crossing between the two regimes is a single scalar, and it is where a measurement is informative.

Does not show: that these four criteria are exhaustive, nor that R3 survives contact with the
constructions in [[backdoor-defense-learnability-obfuscation]].

## How it was produced

| | |
| --- | --- |
| Method | Instantiation of `R` in four settings, then reading off the reference problem and the baseline in each |
| Builds on | [[2026-08-05-unfiled-test-time-attacks-as-learners]], and through it [[2026-08-05-unfiled-attack-surface-decomposition]] |
| Inputs | The terminology ledger in [[CONTEXT]]; the `R`-parameterized definition family, [[cohen-data-reconstruction]] |
| Settings used | A released noisy Gaussian mean for R1 and R2; a training-time displacement for R3; query access to a model for R4 |
| Checked against | [[haghifam-sample-complexity-mia]] for R1 and R2; [[planting-undetectable-backdoors]] for R3 |
| Not checked against | [[backdoor-defense-learnability-obfuscation]], so R3 stands as a candidate rather than a verified contribution |
| Sources | None new; the derivations run over settings already held |
| Artifacts | This report |

## What this changes

Every legitimate technique has an attack twin at the same access level and under the same `R`, and the
twinning is mechanical rather than anecdotal.

| Technique | Attack twin | Shared `R` |
| --- | --- | --- |
| Distillation | Model extraction | function agreement to a tolerance |
| Transfer learning | Property inference | a property of the pretraining source |
| Influence functions and data attribution | Membership inference | was this point influential |
| Unlearning verification | Forging | indistinguishable from never having trained on `x` |

Security is therefore not a separate subject from learning, because a technique measures what a
permitted party extracts and an attack measures what an unpermitted party extracts. The same
measurement serves both with the sign changed, which supports the near-term scope of measurement
rather than hardness recorded in [[CONTEXT]].

## Where it applies

| Section | Change |
| --- | --- |
| Definitions | State each criterion with its free parameters, and state the reference problem those parameters index; drop any mapping step between the two |
| Threat model | Record that the party searching for `R` changes with the family, so the criterion is stated separately from the party pursuing it |
| Terminology ledger, [[CONTEXT]] | Add the baseline and its degeneracy as fields of `R`; record `η` as the dial between the population regime and the cryptographic regime |
| Related work, [[related-work]] | File Gaussian location estimation, two-point hypothesis testing, rare-disagreement search, and learning from a labeling oracle as the four reference problems reached |
| Displacement geometry, [[fiber-of-the-training-map]] | R3 gives the training-time half a criterion, so pair it with the displacement machinery already assigned to that half |
| Open problems | Check R3 against [[backdoor-defense-learnability-obfuscation]]; decide whether the four criteria exhaust the surface |
