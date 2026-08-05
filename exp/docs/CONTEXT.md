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
| `R` | the success criterion: a relation deciding whether an adversary's output counts | fixed, borrowed (Cohen et al. ITCS'25) |
| **displacement** | what a training-time adversary does to `f` | fixed, ours |
| **phase of action / phase of measurement** | when the adversary acts vs when `R` is evaluated; a backdoor differs in the two | fixed, ours |
| `𝒜` | the adversary's algorithm class | fixed |
| `b` | the adversary's resource budget | fixed |
| **security profile** | the curve `b ↦ ε(b)`; the measurable object, not a single number | proposed, ours |
| **the three maps** | training `D ↦ f`, parameterization `w ↦ M_w`, feature `x ↦ f_θ(x)`; never conflated | fixed, ours |
| `δ` | the fine-grained gap; adversary work `≥` honest work`^{1+δ}` | fixed, borrowed (fine-grained crypto) |

## The three attack families

Indexed by what the adversary displaces. See
`docs/reports/2026-08-05-unfiled-attack-surface-decomposition.md`.

| Family | Displaces | `R` evaluated on |
| --- | --- | --- |
| Training-time | `f` | a property of `f` |
| Test-time passive | nothing | a property of `D` or `f` |
| Test-time active | `x` | a property of `f(x)` |

## Standing constraints

- **Definitions in this area are commodities.** The contribution has to be a theorem or a measurement,
  never a definition alone.
- **`R` must be pinned to a harm before anyone looks at its difficulty.** Choosing `R` to be something
  known to be hard proves a fact about `R`, not about the system. This is the one guardrail.
- **The write-up register is `academic-ste`.** No first person, no em dash, one idea per sentence.
- Full record of what has been refuted and what remains open is in the repo root `CLAUDE.md`.

## Repo notes

- `paper/` is scaffolded but empty: no venue is chosen and no deliverable is fixed, so
  `.paper-meta.yml` and `main.tex` are deliberately absent. Create them when a target is picked.
- The literature knowledge base lives outside this project, in the repo root `wiki/`. It predates this
  structure and is not being migrated.
