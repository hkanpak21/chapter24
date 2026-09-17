---
id: survey-structure
date: 2026-08-05
tag: lit
status: draft
supersedes: null
commit: null
cluster: n/a
jobs: []
pi_reviewed: false
---

# The requested matrix is a projection of four axes, and the projection loses backdoors

## Scope

The PI meeting recorded in [[2026-08-05-pi]] asks for a taxonomy matrix of privacy against integrity,
train time against test time, and dataset against learning algorithm against model. This report checks
whether that matrix can be filled consistently, and it reports the state of the corpus against the
survey's needs. A sweep of existing taxonomies is running separately and is not included here.

## Result

**The requested matrix is filled by projecting four generator axes, not three. Eleven of its twelve
cells populate, one is structurally empty, and backdoors cannot be assigned a single cell because they
act in one phase and are measured in another.**

The corpus holds 85 source pages and **none of the canonical systematizations of this field**, so the
survey's first step is an ingest and not a synthesis.

### The four generator axes

| Axis | Values | Why it is separate |
| --- | --- | --- |
| Phase of action | train / test / none | when the adversary intervenes |
| Phase of measurement | train / test | when `R` is evaluated. Differs from action for backdoors |
| Asset | dataset `D` / learning algorithm `L` / model `f` / output `f(x)` | what is at stake. The PI's third dimension, plus the output |
| Goal | confidentiality / integrity / availability | what `R` demands. The PI's first dimension, plus availability |

Privacy is the confidentiality goal. The requested matrix is the projection onto goal, phase and asset,
with phase of action and phase of measurement collapsed into one column and availability dropped.

### The matrix, filled

| | Dataset `D` | Learning algorithm `L` | Model `f` |
| --- | --- | --- | --- |
| **Privacy, train time** | gradient inversion; federated and split-learning leakage | hyperparameter and optimizer inference from update traces | a curious participant learns the architecture under training |
| **Privacy, test time** | membership inference; reconstruction; attribute and property inference | hyperparameter stealing | model extraction and distillation |
| **Integrity, train time** | data poisoning; backdoor insertion by data | Byzantine updates; malicious optimizer; algorithm substitution | direct weight tampering; backdoor insertion by weights |
| **Integrity, test time** | **structurally empty** | **structurally empty** | adversarial examples; jailbreaks; prompt injection, all acting on `f(x)` |

Two cells are empty for a reason rather than by omission: at test time the training data and the
training procedure no longer exist as objects the adversary can touch. A matrix that enumerates instead
of generating cannot distinguish an empty cell from an unlisted one.

### Three defects in the projection

| Defect | Statement | Consequence for the survey |
| --- | --- | --- |
| Backdoors have no cell | The act displaces `f` at train time; `R` is evaluated on `f(x)` at test time. Collapsing the two phases forces an arbitrary assignment | The generator must appear in the paper, with the matrix presented as its projection |
| Availability is absent | The requested matrix has two goals. Availability poisoning, which degrades the model rather than steering it, fits neither | Either add the third goal or state that it is out of scope |
| The output `f(x)` is not an asset in the matrix | Evasion targets the output, not the model. Folding it into "model" conflates changing what a model *is* with changing what it *says* | Add `f(x)` as a fourth asset column, or state the conflation |

### Corpus state against the survey's needs

| Category | In the corpus |
| --- | --- |
| Total source pages | 85 |
| Canonical systematizations of ML security or privacy | **zero** |
| Formal or definitional attempts | present: [[cohen-data-reconstruction]], [[kaplan-bayesian-memorization-reconstruction]], [[backdoor-defense-learnability-obfuscation]], [[complexity-theoretic-adversarial-ml]] |
| Reference problems and hardness | strong: [[related-work]] catalogues roughly eighty |

Does not show: which existing taxonomy is closest to the four-axis generator, since the sweep of prior
systematizations is still running and no comparison is made here.

## How it was produced

| | |
| --- | --- |
| Method | Projection of the programme's existing axes onto the requested matrix, then filling every cell and recording which resist |
| Inputs | [[2026-08-05-pi]]; the three-axis surface in [[CONTEXT]], itself from [[2026-08-05-unfiled-test-time-attacks-as-learners]] |
| Corpus check | `grep` over `wiki/sources/` for taxonomy, survey, systematization and SoK; 85 pages, no canonical systematization |
| Pending | A sweep of prior taxonomies and SoKs, running at the time of writing |
| Artifacts | This report |

## What this changes

The survey's first step is an ingest rather than a synthesis, because the corpus that supports the
programme's theory does not support a survey of the field. The matrix can be delivered as the PI asked
for it, but only as a projection with its generator stated, since three named defects follow from the
projection and one of them silently misplaces the most-studied attack family. The definitional
contribution is unaffected and remains the deliverable.

## Where it applies

| Section | Change |
| --- | --- |
| Survey, taxonomy section | Present the four generator axes first, then the requested matrix as their projection |
| Survey, scope | State whether availability is in scope, and whether `f(x)` is a separate asset |
| Survey, related work | Blocked on the running sweep |
| Terminology ledger, [[CONTEXT]] | Add the asset axis with `L` as a first-class asset; the ledger currently has no term for the learning algorithm as a target |
| Corpus | Ingest the canonical systematizations before drafting; list follows from the sweep |
