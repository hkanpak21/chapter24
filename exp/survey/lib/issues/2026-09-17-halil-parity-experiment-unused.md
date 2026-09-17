---
slug: 2026-09-17-halil-parity-experiment-unused
opened: 2026-09-17
assignee: halil
status: open
raised_by: paper/reviews/sp27/2026-09-03-review-round-2.md
closed_by:
source: lab/results/sparse-parity/manifest.yml
---

# The sparse-parity run and the formalization are parked and undecided

## What this is

Two bodies of work sit outside the paper. The sparse-parity run measured how
step count grows with input dimension and fitted an exponent of 2.02 over eight
seeds and five dimensions, and no section uses it. The formalization drafts in
`paper/sections/formalization/` run to about 1540 lines and state the games, the
oracle and the price of the search, and the original six-part plan had them as
Part IV.

The round-two reviewer judged that the paper stands without the formalization,
and that a systematization needs its table to be right rather than a ledger of
its own. The award paper this venue's profile names as the SoK model carries two
small validation experiments that demonstrate its framework.

So there is a live option: the parity run as a validation experiment in the
DSA24 shape. It is not obvious that it demonstrates anything this paper claims,
because the paper measures a literature and the run measures a network.

## What closes it

A ruling on each of the two, either into a section of this paper or into a
successor, recorded in `lib/profs/rulings.md`.

## Where it touches

lab/results/sparse-parity
paper/sections/formalization/
paper/figures/parity-scaling.pdf
