# CONTEXT

Project state and terminology ledger. Read at the start of every session.

## What this is

A theory of the security of deep learning, built to be **measurable rather than hard**. The near-term
goal is not a hardness theorem and not a defence mechanism: it is to fully measure an attack's
capability against a concrete adversary. Hardness, if it comes, comes later.

The method is **reduce one learning problem to another**. Attacks in this field are themselves learning
algorithms — no attack or defence in evidence uses out-of-field machinery — so the reference problem at
the far end of a reduction should be a learning problem with calibrated thresholds, not a
number-theoretic one.

## Terminology ledger

Terms are fixed here once and used nowhere else with a different meaning.

| Term | Meaning | Status |
| --- | --- | --- |
| `D` | the dataset | fixed |
| `f` | a function in the hypothesis space; the object training reaches | fixed |
| `L` | the training map, `D ↦ f` | fixed |
| `R` | **the quantizer between the approximate learning layer and the exact cryptographic layer.** Exact by type; its parameters are where the approximation is quantized. There is **one** `R`, indexed by search-or-decision and by the target of the attack | fixed, ours; the relation form is borrowed (Cohen et al. ITCS'25) |
| **baseline of `R`** | what a party with only public knowledge achieves on `R`; a field of `R`, not of the game | fixed, ours |
| **degenerate baseline** | a baseline at 0, 1/2 or 1, where subtracting it is a no-op; forces raw advantage | fixed, ours |
| `η` | `R`'s tolerance, and the dial between the population regime (coarse, nothing to measure) and the cryptographic regime (tight, needs an assumption) | fixed, ours |
| **party searching for `R`** | changes with the family: the attacker in the privacy criteria, the *detector* in the backdoor criterion | fixed, ours |
| **displacement** | what a training-time adversary does to `f` | fixed, ours |
| **phase of action / phase of measurement** | when the adversary acts vs when `R` is evaluated; a backdoor differs in the two | fixed, ours |
| `𝒜` | the adversary's algorithm class | fixed |
| `b` | the adversary's resource budget | fixed |
| **security profile** | the curve `b ↦ ε(b)`; the measurable object, not a single number | proposed, ours |
| **the three maps** | training `D ↦ f`, parameterization `w ↦ M_w`, feature `x ↦ f_θ(x)`; never conflated | fixed, ours |
| `δ` | the fine-grained gap; adversary work `≥` honest work`^{1+δ}` | fixed, borrowed (fine-grained crypto) |

## The attack surface: three axes

An attack is a cell, not a named family. See
[[2026-08-05-unfiled-test-time-attacks-as-learners]], which corrects the single-axis version in
[[2026-08-05-unfiled-attack-surface-decomposition]].

| Axis | Values |
| --- | --- |
| Phase of observation | training / test |
| Displacement | none / `x` non-adaptive / `x` adaptive / `f` |
| `R` target | a property of `D` / of `f` / of `f(x)` |

The displacement levels are the **passive, chosen-plaintext, chosen-ciphertext** hierarchy. An access
level times a criterion replaces any per-attack definition.

The two halves take different machinery:

| Half | The adversary | Machinery |
| --- | --- | --- |
| Training-time | **acts on** a learner | displacement geometry: loss landscape, the fiber |
| Test-time | **is** a learner | learning-theoretic thresholds: sample and query complexity, exponents |

## Standing constraints

- **Definitions in this area are commodities.** The contribution has to be a theorem or a measurement,
  never a definition alone.
- **`R` must be pinned to a harm before anyone looks at its difficulty.** Choosing `R` to be something
  known to be hard proves a fact about `R`, not about the system. This is the one guardrail.
- **A planted source voids the guardrail as surely as a planted `R`.** If the hardness is in the data
  distribution before `R` arrives, `R` reads it off and does no work. Hold the source natural; let `R`
  select the problem. See [[2026-08-05-unfiled-natural-source-r-selects-the-problem]].
- **The write-up register is `academic-ste`.** No first person, no em dash, one idea per sentence.
- Full record of what has been refuted and what remains open is in the repo root `CLAUDE.md`.

## Repo notes

- `paper/` is scaffolded but empty: no venue is chosen and no deliverable is fixed, so
  `.paper-meta.yml` and `main.tex` are deliberately absent. Create them when a target is picked.
- The literature knowledge base lives outside this project, in the repo root `wiki/`. It predates this
  structure and is not being migrated.
