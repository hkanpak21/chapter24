---
slug: 2026-09-17-halil-supplement-has-no-submission-slot
opened: 2026-09-17
assignee: halil
status: open
raised_by: paper/reviews/sp27/2026-09-03-review-round-2.md
closed_by:
source: references/venues/ieee-sp.md
---

# Nineteen pages of tables have nowhere to go

## What this is

The classification tables run to 19 pages. The call allows 13 pages of text plus
5 for references and appendices inside an 18-page total, and the appendix sits
inside that total. There is no unlimited appendix at this venue and no separate
supplementary slot the call names.

The plan on record sends the tables to an anonymized artifact, which the call
strongly encourages and requires to be frozen at the deadline, and makes the
codebook the appendix. Neither move is done, and the artifact repository is not
created. The call names GitFront and Anonymous GitHub.

## What closes it

The tables in an anonymized artifact repository whose URL is in the paper, the
codebook typeset as an appendix within the page allowance, and a rebuilt
`paper/main.pdf` passing gate G9.

## Where it touches

paper/supplementary.tex
paper/tables/04-tables.tex
lib/literature/codebook.md
