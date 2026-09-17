---
slug: 2026-09-17-halil-section-seven-stands-alone
opened: 2026-09-17
assignee: halil
status: open
raised_by: paper/reviews/sp27/2026-09-03-review-round-2.md
closed_by:
source: paper/reviews/sp27/2026-09-03-review-round-2.md
---

# The counterposition sits between the literature and related work

## What this is

Section 7 answers the stated position that attacker computation should not be a
threat-model parameter. It is one paragraph standing alone between Section 6 and
Section 8. The reviewer placed it either at the end of Section 2, as the field's
own answer to the third problem, or beside the near-miss row for the same work
in Section 5.

The placement matters beyond tidiness. The S&P reviewer pool overlaps with the
authors of the position the section answers, so it is among the first passages
such a reviewer reads, and it currently arrives with no surrounding argument.

## What closes it

Section 7 moved to one of the two named places, with the cross-references in
Sections 2, 5 and 8 following it, and the claim
`field-rejects-attacker-compute-as-a-parameter` re-pointed in `lib/claims.yml`.

## Where it touches

paper/sections/07-findings.tex
paper/sections/02-problem.tex
paper/sections/05-reading.tex
paper/sections/08-related.tex
