---
id: r-as-quantizer-and-one-reduction
date: 2026-08-05
tag: unfiled
status: draft
supersedes: null
builds_on: 2026-08-05-unfiled-concrete-r-criteria.md
commit: null
cluster: n/a
jobs: []
pi_reviewed: false
---

# `R` is the quantizer between the approximate layer and the exact layer, and one reduction built with it

## Scope

[[2026-08-05-unfiled-concrete-r-criteria]] instantiates `R` four times without saying what `R` is. This
report states what `R` is ontologically, states what it does, and then uses it once as an instrument to
carry a machine-learning security question into a cryptographic hard problem. The construction runs
over sources already held, so it reads no new source.

## Result

**`R` is the quantizer between a layer that is approximate everywhere and a layer that is exact
everywhere: the learning layer produces risks, tolerances and seed-dependent outcomes, the
cryptographic layer consumes a single bit, and `R` is the map between them, exact by its type, with its
parameters placed exactly where the approximation is quantized.**

The construction below carries property inference against a released model into the Gaussian pancakes
problem, with every parameter of `R` appearing unchanged as a parameter of that problem. The variance
that makes empirical security results disagree across settings and seeds never enters, because the
reduction consumes the bit that `R` emits and nothing else.

### What `R` does

| Function | Statement |
| --- | --- |
| Quantizes | Takes an approximate outcome in the learning layer and returns a bit, the only object a reduction consumes |
| Carries the parameters | `R`'s tolerance is the reference problem's precision, as one symbol used once, never as a correspondence |
| Fixes the baseline | Names what public knowledge alone achieves, which is what makes advantage defined |
| Selects the problem | Fixing `R` fixes the search or decision problem the adversary solves; the problem is read off, not constructed |
| Is one object | Indexed by search or decision, and by the target of the attack; every other criterion in the literature is a parameter setting of it |

### The construction

| Component | Value |
| --- | --- |
| Source | Gaussian pancakes: `N(0, I_d)` conditioned to concentrate near equally spaced hyperplanes orthogonal to a secret unit direction `w*`, spacing `1/γ`, width `β/γ`. The source looks Gaussian to every efficient observer |
| Labels | `y = f(⟨w*, x⟩)` for a link `f`, so the defender's task depends on the hidden direction |
| Defender | Trains a model `M` on `n` samples and releases it, white-box or by query access |
| Adversary | Reads `M`, outputs a unit vector `ẑ` |
| `R` | `R(w*, ẑ) = 1` exactly when `\|⟨ẑ, w*⟩\| ≥ 1 − η` |
| Free parameters | `η`, the direction tolerance; `γ`, the spacing; `n`; the adversary's time and query budget |
| Baseline | A random unit vector achieves `R` with probability equal to the measure of a spherical cap of angular radius `arccos(1 − η)`, which is exponentially small in `d` for fixed `η` |
| Baseline degenerate | no |

### The reduction, and why it is tight

An adversary achieving `R` outputs a direction within `η` of `w*`; projecting fresh samples onto it and
testing for periodicity distinguishes the pancake source from `N(0, I_d)`, and that source carries an
unconditional statistical-query floor and worst-case lattice hardness, so the distinguisher is a
lattice break. No quantity is translated on the way:

| Quantity | In the learning layer | In the cryptographic layer |
| --- | --- | --- |
| `η` | the tolerance in `R` | the precision of the direction recovered in the search-to-decision step |
| `γ` | the spacing of the source's hidden structure | the hardness parameter of Gaussian pancakes |
| time and queries | the adversary's budget | the distinguisher's budget |

### The trichotomy, which is the real content

Because the label depends on `⟨w*, x⟩`, the defender's own task is constrained by the same hardness:

| Case | Consequence |
| --- | --- |
| The defender trains an accurate model | The defender recovered `w*`, so the defender broke a lattice assumption. Absurd for an efficient defender |
| The defender fails | No useful model exists, so the attacker gains nothing. Security by uselessness, not a security result |
| The defender is accurate without recovering `w*` exactly | The regime that occurs in practice, and the only one worth measuring |

In the third case `η` measures how much of the secret a model carries while remaining trainable, so the
object to prove is a curve and not a bound: the largest `η` an efficient adversary achieves against a
model of test error at most `ε`, as a function of `ε`.

Corrected by [[2026-08-05-unfiled-natural-source-r-selects-the-problem]]: the source here is a planted
cryptographic distribution, so the hardness precedes `R` and `R` only reads it off. This construction
stands as an illustration of tightness and not as a reduction about learning.

Does not show: the reduction is stated as a construction and a chain of implications, not as a proof.
The projection-and-test step needs a stated tolerance regime relating `η` to `β` and `γ`, the
search-to-decision direction for Gaussian pancakes must be checked against the source rather than
assumed, and the trichotomy's third case is an open problem and not a theorem.

## How it was produced

| | |
| --- | --- |
| Method | Statement of the ontology, then one construction assembled from sources already held |
| Builds on | [[2026-08-05-unfiled-concrete-r-criteria]], and through it [[2026-08-05-unfiled-test-time-attacks-as-learners]] |
| Reference problem | Gaussian pancakes, from [[bruna-continuous-lwe]]; statistical-query floor from Diakonikolas, Kane and Stewart; classical equivalence to learning with errors from Gupte, Vafa and Vaikuntanathan |
| Related | [[song-cryptographic-hardness-score-estimation]], which reduces score estimation on the same source to the same problem |
| Constrains the defender | Song, Zadik and Bruna on the hardness of learning single periodic neurons, which is what forces the trichotomy |
| Not verified | The novelty of the construction. Four novelty claims failed this session, and this one has not been checked |
| Artifacts | This report |

## What this changes

The programme now has a statement of what `R` is rather than a list of instances, and the statement
explains why the empirical variance in the field is not an obstacle: a reduction consumes the bit that
`R` emits, so seed-dependence and setting-dependence never enter it. The construction gives the first
candidate reduction whose every parameter passes the alignment test, which moves the programme from
framing to a stated open problem. The claim that a specific `R` should be fitted to a specific
empirical attack is now abandoned, since fitting reproduces the variance the theory exists to remove.

## Where it applies

| Section | Change |
| --- | --- |
| Definitions | State `R` as the quantizer, with the four functions in the table, before any instance appears |
| Terminology ledger, [[CONTEXT]] | Record `R` as the exactness interface; record that there is one `R` indexed by search or decision and by the target |
| The construction | New section: source, labels, `R`, baseline, reduction, and the alignment table |
| Open problems | Prove the projection-and-test step at a stated tolerance regime; settle the search-to-decision direction on this source; attack the trichotomy's third case, which is the security profile |
| Related work, [[related-work]] | File Gaussian pancakes as the reference problem reached, and record the defender-side constraint |
