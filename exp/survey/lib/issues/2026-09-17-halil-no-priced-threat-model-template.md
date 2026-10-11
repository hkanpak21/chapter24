---
slug: 2026-09-17-halil-no-priced-threat-model-template
opened: 2026-09-17
assignee: halil
status: open
raised_by: paper/reviews/sp27/2026-09-03-review-round-2.md
closed_by:
source: paper/reviews/sp27/2026-09-03-review-round-2.md
---

# The paper diagnoses and never prescribes

## What this is

The round-two reviewer's largest recommendation, and the one item it called the
missing half page. The paper names four objects in Section 1, the adversary
class, the budget, the success criterion with its tolerance, and the baseline,
and never shows what a claim looks like when it carries all four. Asked what the
field would do differently after reading the paper, the reviewer answered
nothing specific.

The proposed form is a template and two instances, half a page: Carlini et al.'s
LiRA restated with its adversary class and shadow-model budget named, and Jia et
al.'s proof-of-learning Property 2 restated with the exponent left symbolic. It
does not need the parked formalization.

Adding it turns a diagnostic SoK into one carrying a recommendation, which a
reviewer can then attack as unvalidated. Leaving it out draws the charge the
reviewer already made. This is the author's call and the PI's, not the agent's.

## What closes it

Half a page in Section 5 carrying the template and the two instances, or a
ruling in `lib/profs/rulings.md` that the paper stays diagnostic.

## Where it touches

paper/sections/05-reading.tex
paper/sections/01-introduction.tex
lib/claims.yml, a new contribution claim if the section is written
