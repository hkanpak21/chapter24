---
id: leakage-and-integrity-functions
date: 2026-08-05
tag: unfiled
status: draft
supersedes: null
builds_on: 2026-08-05-halil-lit-survey-structure.md
commit: null
cluster: n/a
jobs: []
pi_reviewed: false
---

# The leakage function and the integrity function are one function, differing in who searches

## Scope

The PI meeting in [[2026-08-05-pi]] asks for a leakage function for privacy tasks and an integrity
function for integrity tasks. This report determines both from the criterion machinery already held,
and checks whether two functions are needed. A sweep of quantitative information flow and
leakage-resilient cryptography is running separately and is not included.

## Result

**Both are the same object: the infimum of the criterion's parameter at which the searching party still
wins. Privacy and integrity differ in the reference and in which party searches, and in nothing else.**

Fix a criterion family `{R_θ}` indexed by a parameter `θ`, a searching party `P`, an algorithm class
`𝒜`, and a budget `b`:

```
Φ(P, 𝒜, b)  =  inf { θ : some A ∈ 𝒜 at budget b makes P win R_θ above baseline }
```

### The two instantiations

| | Privacy | Integrity |
| --- | --- | --- |
| Reference | the secret, a property of `D` | the honest model `f` |
| Candidate | the adversary's guess | an input where `f*` and `f` disagree |
| **Searching party** | the **attacker** | the **detector** |
| `θ` | reconstruction tolerance, the resolution demanded | disagreement measure, the size of the deviation |
| `Φ` reads as | **leakage**: the finest resolution at which the secret becomes visible | **detection floor**: the smallest deviation that can be found |
| Direction of harm | smaller `Φ` is worse, since the secret is pinned more precisely | larger `Φ` is worse, since more deviation hides beneath it |

The reversal of direction follows from the party rather than from a convention, since both parties
searching harder drives `Φ` down and only the identity of the searcher differs. The collapse into one
function is available because the programme already established in
[[2026-08-05-unfiled-concrete-r-criteria]] that the party pursuing `R` changes with the family, so
making that party an argument is the whole of the unification.

### Where the security statement lives

`Φ` at a bounded budget, compared against `Φ` with no budget constraint:

| Quantity | Meaning |
| --- | --- |
| `Φ_IT = Φ(P, all algorithms, ∞)` | the resolution at which the information is present |
| `Φ_comp(b) = Φ(P, 𝒜, b)` | the resolution a bounded party actually reaches |
| **`Φ_comp(b) − Φ_IT`** | **the security margin, in the units of `θ`** |

For privacy this is the gap between what the release contains and what an efficient adversary extracts,
and for integrity between deviations that exist and deviations a bounded detector finds, both as curves
in `b`.

Does not show: that `Φ` is well defined when the criterion family is not monotone in `θ`. Monotonicity
holds for the tolerance families used so far, since a coarser tolerance is easier to satisfy, but it
must be stated as a condition on `{R_θ}` rather than assumed.

## How it was produced

| | |
| --- | --- |
| Method | Determination from the criterion machinery, then a check of whether the two requested functions differ structurally |
| Inputs | [[2026-08-05-pi]]; the searching-party finding in [[2026-08-05-unfiled-concrete-r-criteria]]; `R` as quantizer in [[2026-08-05-unfiled-r-as-quantizer-and-one-reduction]] |
| Instantiated against | the privacy criteria R1 and R2, and the backdoor criterion R3, all in [[2026-08-05-unfiled-concrete-r-criteria]] |
| **Collision risk, unresolved** | **g-leakage**, from generalized gain functions in quantitative information flow, is parameterized by a gain function `g(w,x)` and is the nearest known relative. A sweep is running. See the assessment below |
| Artifacts | This report |

### Assessment of the g-leakage risk, pending the sweep

The gain function `g` in quantitative information flow is a real-valued criterion, so `R_θ` with a
`{0,1}` codomain is plausibly a special case of it. Two differences are expected to survive, and the
sweep should confirm or kill them.

| | g-leakage | `Φ` |
| --- | --- | --- |
| Object reported | a value, for one fixed gain function | a **threshold**, scanned over a family indexed by `θ` |
| Adversary | information-theoretic, a maximum over guesses | a **class at a budget** |

If both hold, `Φ` is to g-leakage roughly as a breakdown point is to a risk, and the programme's claim
narrows to the budgeted, class-bounded reading. If either fails, this report is superseded.

## What this changes

The PI's two requested functions are answered with one, and the reversal in direction between them is
derived rather than stipulated. The security profile now has an operational definition, so the
programme can state a security claim as a measured quantity rather than as a bound. The survey's
definitional contribution gains its central object, since `Φ` is what the common aspects across
different works would be expressed in.

## Where it applies

| Section | Change |
| --- | --- |
| Survey, definitions | State `Φ` once, with the searching party as an argument; derive leakage and the detection floor as its two readings |
| Survey, taxonomy | The goal axis in [[2026-08-05-halil-lit-survey-structure]] now has a quantity attached to each value, not only a name |
| Terminology ledger, [[CONTEXT]] | Add `Φ`, the searching party as its argument, and the monotonicity condition on `{R_θ}` |
| Open problems | State the monotonicity condition; settle the relationship to g-leakage; determine the availability reading of `Φ`, which is currently absent |
