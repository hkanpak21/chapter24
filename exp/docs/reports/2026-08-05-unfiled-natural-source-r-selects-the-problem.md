---
id: natural-source-r-selects-the-problem
date: 2026-08-05
tag: unfiled
status: draft
supersedes: null
corrects: 2026-08-05-unfiled-r-as-quantizer-and-one-reduction.md
builds_on: 2026-08-05-unfiled-r-as-quantizer-and-one-reduction.md
commit: null
cluster: n/a
jobs: []
pi_reviewed: false
---

# Over one natural source, `R` selects which computational problem the adversary faces

## Scope

[[2026-08-05-unfiled-r-as-quantizer-and-one-reduction]] plants a cryptographic problem in the source,
so the hardness is present before `R` appears and `R` only reads it off. This report holds the source
natural, holds the learning task useful, and shows that `R` alone selects which problem the adversary
solves and therefore which threshold applies. The construction runs over standard settings, so it reads
no new source.

## Result

**Over a single fixed natural source, changing `R` changes the adversary's computational problem and
its threshold, while the source and the defender's task stay put. `R` is therefore the instrument that
selects the problem, and not a reader of hardness planted elsewhere.**

The source is a Gaussian design with a sparse signal, carrying no planted structure, and the defender's
prediction task succeeds at `n` of order `k log d` by ordinary means.

### The setting, held natural throughout

| Component | Value |
| --- | --- |
| Source | `x ~ N(0, I_d)`, `y = ⟨β*, x⟩ + noise`, with `β*` `k`-sparse. Plain Gaussian design, no planting |
| Defender's task | Predict `y`. Succeeds at `n` of order `k log d` by ordinary regularized regression |
| Release | A trained model that predicts well. **Not** the sparse coefficient vector itself |
| Adversary | Reads the release, outputs a candidate set `Ŝ` of features |
| Security question | Which features did the model use. This is feature and attribute inference, a real concern wherever the feature set is sensitive |

### `R` selects the problem, and this is the demonstration

| `R` over the same source | The adversary's problem | Threshold |
| --- | --- | --- |
| Predict `y` to error `ε` | the defender's own task | `n` of order `k log d`, polynomial time |
| Recover `β*` to tolerance `η` in `L2` | sparse estimation | `n` of order `k log d`, polynomial time |
| Recover `supp(β*)` exactly | support recovery | `n` of order `k log d`, subject to a minimum-signal condition |
| Recover `supp(β*)` below the minimum-signal condition | support recovery in the hard regime | low-degree lower bounds; no polynomial-time algorithm known |
| Name one member of `supp(β*)` | detection | strictly weaker than recovery |

### Where the space for the adversary comes from

Releasing the sparse coefficient vector hands over the support, so the question exists only when the
release computes the sparse function without exposing its parameterization.

| Release | Support recoverable by | Adversary's problem |
| --- | --- | --- |
| the sparse vector `β̂` | inspection | none |
| query access, `d` queries allowed | probing basis vectors | trivial |
| query access, `q < d` queries | compressed sensing | `q` of order `k log(d/k)`, polynomial time |
| a trained network computing the same function | unknown | the open case, and the one that occurs in practice |

### What is proved and what is not

The selection claim is established and the reduction claim is not: the reference problem is support
recovery for sparse regression where low-degree bounds apply, and carrying the network-release case into
it is the open step.

Does not show: that support recovery from a trained network reduces to support recovery from samples,
which is exactly the unproved step. The low-degree regime for sparse regression must also be stated at
an explicit signal-to-noise level rather than named, and the minimum-signal condition separating the
third and fourth rows must be written out before either row is used.

## How it was produced

| | |
| --- | --- |
| Method | Construction over a standard statistical setting, then variation of `R` with the source and the defender held fixed |
| Corrects | [[2026-08-05-unfiled-r-as-quantizer-and-one-reduction]], whose source carried the hardness before `R` was applied |
| Guardrail applied | The standing constraint in [[CONTEXT]] that `R` must be pinned to a harm before its difficulty is examined. The previous attempt satisfied it for `R` and violated it for the source |
| Reference problem | Sparse regression support recovery in the hard regime; low-degree bounds via the Franz-Parisi route, catalogued in [[related-work]] |
| Not verified | Whether support recovery from a trained network has been studied. Not checked, and this report does not claim novelty |
| Artifacts | This report |

## What this changes

`R` is now shown to do work rather than to report work done elsewhere, because five distinct
computational problems were reached over one unchanged natural source. The security question that
results, which features a model used, is an ordinary privacy concern rather than a constructed one, so
the setting is usable as a running example. The previous report's construction is retained only as an
illustration of the mechanism, since its hardness was planted and its reduction therefore proves
nothing about learning.

## Where it applies

| Section | Change |
| --- | --- |
| The construction | Replace the pancake source with the sparse regression setting; keep the pancake version as an illustration of tightness only |
| Definitions | State the selection property of `R` as its defining functionality, using the five-row table |
| Terminology ledger, [[CONTEXT]] | Record that a planted source voids the guardrail as surely as a planted `R` |
| Open problems | Prove or refute that support recovery from a trained network reduces to support recovery from samples; state the low-degree regime at an explicit signal-to-noise level |
| Related work, [[related-work]] | Promote sparse regression from the gap-witness tier to the working reference problem |
