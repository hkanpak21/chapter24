---
slug: 2026-09-17-halil-title-and-anonymity-fail-the-call
opened: 2026-09-17
assignee: halil
status: open
raised_by: paper/reviews/sp27/2026-09-03-review-round-2.md
closed_by:
source: references/venues/ieee-sp.md
---

# Three desk-reject conditions are open at the submission build

## What this is

The call lists improper anonymization among the grounds for rejection without
review, and requires the `SoK:` prefix on a systematization. The title now
carries the prefix. Two conditions remain.

The author block names the author and the institution on page 1 of both
documents. The submission build has to drop it, and self-citation has to be in
the third person.

There is no ethics statement. The field is mandatory at registration, and the
section itself is added at camera ready and does not count toward the limit.
This paper reads published work and runs no experiment on any system or person,
so the statement is short, and it still has to be written and reasoned rather
than left blank.

## What closes it

A submission build with no author block, `check-blind.py` clean against
`~/.config/research/blind-patterns`, and the ethics field answered in HotCRP.

## Where it touches

paper/main.tex
paper/supplementary.tex
