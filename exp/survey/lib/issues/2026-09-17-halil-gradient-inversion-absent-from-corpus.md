---
slug: 2026-09-17-halil-gradient-inversion-absent-from-corpus
opened: 2026-09-17
assignee: halil
status: open
raised_by: lib/reports/archive/2026-08-22-halil-plan-survey-scope-and-structure.md
closed_by:
source: lib/reports/archive/2026-08-22-halil-plan-survey-scope-and-structure.md
---

# Gradient inversion and split learning have no source page

## What this is

The corpus holds no work on gradient inversion or on split learning. The frame
places both cleanly, since the channel is the weights or the intermediate
activations at training time, and the author's own research is in that area.
The scope note has carried this as an open question since 2026-08-20.

Two readings. Either the theorem-bearing part of that literature is thin enough
that the inclusion test excludes it, which is a finding the paper should state,
or the sweep never ran and the absence is a gap in the corpus rather than in the
field. Nothing on record distinguishes them.

## What closes it

A sweep over the gradient-inversion and split-learning literature against the
three inclusion conditions, with the works that pass classified and the count of
works that fail condition two recorded.

## Where it touches

lab/results/corpus-classification
paper/sections/04-methodology.tex, the corpus subsection
paper/sections/06-literature.tex
