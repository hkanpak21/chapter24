---
id: survey-review-round-2
date: 2026-09-03
tag: review
status: draft
supersedes: null
commit: 9804cc3 plus uncommitted edits listed below
cluster: n/a
submitted: 2026-09-03T21:10+03:00
landed:    2026-09-03T21:27+03:00
jobs: []
pi_reviewed: false
---

# The second adversarial review returns weak reject, and the headline count of two-party bounds is wrong a second time

## Scope

This report reads the survey draft against the S&P 2027 call and puts a fresh adversarial reviewer on the rebuilt PDF. Every numeric finding the reviewer made was re-derived from `notes/classification.tsv` and the primary PDFs before it was accepted. The report records what was fixed today, the rulings only Halil can make, and the path to the November 17 deadline.

## Result

The reviewer returns weak reject, every one of its numeric findings holds against the data, and after Halil's four rulings the recount stands at 18 works stating a bound relative to another party's work, 6 of them attack works, against the 11 and 3 the paper printed. Seven rows coded `exponent` carried a recorded reason naming a second party, which is the codebook's own definition of `relative`, and the previous recoding had missed them. The reviewer judges the paper's viewpoint real and the third SoK criterion within reach once the table agrees with itself, and the same evening the table does: codebook revision 7, 55 field recodes each logged in its row, 24 missing quotations supplied, every venue resolved, and all ten gates passing on a 12-page body.

The full review is at `exp/survey/reviews/2026-09-03-review-round-2.md`. The findings and where each stands:

| Id | Finding | Checked by me | Position | Action |
| --- | --- | --- | --- | --- |
| F1 | 7 `exponent` rows are two-party under the codebook; PoL's bare inequality is unruled | Holds. Scanned all 27 `exponent` reasons; the seven are the complete set | Agree. Needs ruling R1 | Recode, recount, rewrite abstract, 5.3, 6.6, conclusion |
| M1 | Section 6 illustrates two regions with works the table places elsewhere | Holds. All six named works are coded in other regions, five of them by hand | Agree on the defect. Prefer recoding the three geometric results to `none`, since standing decision 4 puts them outside the frame. Needs ruling R2 | Recode or re-pick examples |
| M2 | 24 hand-coded rows carry no deciding quotation; the abstract says every row does | Holds. `prov=hand` on 24 rows, evidence `absent` on each | Agree | Delegate 24 quotations to one Sonnet batch, rerun both quote passes, restate 4.4 |
| M3 | Restricted-class lower bounds coded to three different parties | Holds. Rows cite rules the codebook does not contain | Agree. Needs ruling R3 | Add a codebook rule, recode 3 rows |
| M4 | Section 5.2 counts queries and samples over any party, not the adversary | Holds. Attacker-only counts are 9 and 1 | Agree | Fixed, as macros |
| M5 | Populated-cell fraction measures spread, not agreement | Holds. Top-five cells hold 61 per cent of attack works by phase and access, 78 by party and unit | Agree | Rewrite 5.1 and 5.2 around shared vocabulary and concentration |
| M6 | Suya et al. re-ran 11 transfer attacks, not 164 | Holds, verbatim in the PDF | Agree | Fixed |
| M7 | The 18 near-miss works are not one phenomenon | Holds. Three are scaling-law works whose quantity is training cost | Agree | Table of the 18 with the quantity each holds; restrict the closing sentence |
| M8 | `sok-differential-privacies` coded `attacker` on a catalogued definition, against Rule 9 | Holds | Agree. Part of ruling R4 | Recode to `none` |
| M9 | No `SoK:` prefix, author block present | Holds | Agree | At submission build |
| Venue check | Three works the paper calls preprints or unrefereed are refereed: Wen et al. at USENIX Security 2025, Zhang et al. at IEEE SaTML 2025, Shafran et al. in TMLR 2024 | usenix.org, ieeexplore.ieee.org, dblp | Mine, not the reviewer's. Rules S1 and S2 | Fixed: wiki venues, bibliography, both sentences; Fenaux and Kerschbaum stays a preprint |
| m1 to m18 | Wording, typography, stale reasons, codebook hygiene | Each checked | Agree on all. Disagree with recoding `preventing-false-discovery-hard` to `family=none`: the theorem's attack recovers sample elements from query answers, which is `reconstruct`. `undetectable-watermarks-lm` is `measured`, since a dollar ratio observed once is a measurement | Nine fixed today, the rest with the recount |

What the headline numbers become under each ruling, computed on a copy of the table with the three blank `family` rows filled first:

| Table state | Relative | Of which attack | Exponent | Unbounded, attack against other | Difference, 95 per cent interval |
| --- | --- | --- | --- | --- | --- |
| As printed this morning | 11 | 3 | 27 | 23 of 101 against 10 of 99 | 2.6 to 22.8 |
| Blank families filled | 11 | 3 | 27 | 24 of 104 against 9 of 96 | 3.7 to 23.7 |
| R1 option A, `relative` includes PoL | 18 | 6 | 20 | 24 of 103 against 9 of 97 | 4.0 to 24.0 |
| R1 option B, `relative` needs a parameter | 17 | 5 | 20 | same | same |
| Ruled: A, plus R2, R3, R4, and one transposed row redone | 18 | 6 | 20 | 27 of 103 against 10 of 97 | 5.5 to 26.3 |

Halil took the recommended option on all four. The theorem-bearing subset is 12 of 71 against 6 of 87, interval $-0.2$ to 20.2, still including zero, so Section 5.4 keeps stating direction only. The near-miss set is 19 after one recode: 9 hold an adversary's cost, 5 a training cost, 5 a capability or mechanism parameter.

Fixed today, building clean under all ten gates, every new number a macro checked by `tools/check-numbers.py`:

| Fixed | What was wrong |
| --- | --- |
| Figure 1 | Drew the pre-split `exponent` code as "Relative to honest work (27)" and hid the 11 real ones inside "Unstated (46)" |
| Conclusion | Still carried the "roughly twice" size claim Section 5.4 withdrew |
| M4, M6, m1, m3, m4, m5, m7, m10, m11, m18 | Wrong subject of a count, wrong description of Suya et al., three misquoted details, one false "evenly", a section title, a stale caption, a tag count read as a family count, a duplicate sentence |
| Supplement, Section 8 | False "partial pass" text; double periods after paragraph headings; a broken glyph |
| Generators | `gen-tables.py` defaulted to the 25-row batch file and silently produced a 13-page supplement, now defaults to the full table; `gen-bib.py` printed `IACR ePrint/` for two venues and split the ogonek in Madry |
| Evening, after the rulings | Codebook revision 7 and 55 recodes; 24 quotations supplied by two Sonnet agents, two disputes recorded; 100 venues resolved by two Sonnet agents and their sub-agents, 0 unconfirmed, 13 year fields aligned to the refereed venue, journal entries as `@article`; the quotation binder now goes through `raw/SOURCES.md` and caught one row classified against the wrong paper (Ho et al., whose row carried the harmonic-decomposition abstract), redone against its own PDF; field table, worked row, relative-rows table, near-miss table and party-by-unit table added; Sections 3.3 and 3.6 cut, 3.4 folded, 6.6 compressed, Section 6's examples re-picked from rows the table places in each region; `check-numbers.py` now covers 70 macros and rewrites `results.tex` itself |

Does not show: the rows neither the reviewer nor the quotation agents opened, about 130 of 200, and any second-reader agreement beyond the 24 of 27 already on record.

## How it was produced

| | |
| --- | --- |
| Reviewer | `reader` agent on `claude-fable-5-1`, adversarial S&P SoK brief, 26 tool uses, 16.6 minutes |
| Review file | `exp/survey/reviews/2026-09-03-review-round-2.md` |
| Verification | Inline Python over `notes/classification.tsv` and `wiki/sources/*.md` front matter; `pdftotext` and `grep -a` on `raw/SSK+24`, `raw/MHS19`, `raw/JYC+21`, `raw/ACW18` |
| Gates | `bash exp/survey/tools/gates.sh`, all ten pass after the edits |
| Edited | `sections/01,02,05,06,07,08,09`, `results.tex`, `refs.bib`, four wiki venue fields, `tools/check-numbers.py`, `tools/gen-tables.py`, `tools/gen-bib.py`, `figures/src/sankey.py`, `notes/2026-08-22-halil-note-venue-mining.md`, regenerated `04-tables.tex`, `sankey-corpus.pdf`, both PDFs. Nothing committed |
| Reproduce | `cd exp/survey && python3 figures/src/sankey.py && python3 tools/gen-tables.py && bash tools/gates.sh` |

## What this changes

The headline pair is 18 and 6, computed under a rule the codebook now states, and the paper no longer carries a sentence about how the earlier count was wrong. Every row carries a quotation or an evidenced absence, and 155 of the 172 quotations are verified inside their own document by a binder that can no longer be fooled by a title contained in another title. Section 6 illustrates each region with works the table places there, and the geometric-inevitability results are coded where the standing decision always put them. Three works the draft called preprints are refereed, and the bibliography is complete. The supplement has no submission slot at S&P, since the appendix limit is five pages, so the tables go to an anonymized artifact and the codebook to the appendix. The second cycle closes November 17 with abstract registration November 10.

## Where it applies

| Section | Change |
| --- | --- |
| Codebook, done | R1: one sentence deciding whether a bare two-party inequality is `relative`. R2: a radius that a theorem outputs is not a bound on any party. R3: a restricted-class lower bound with no security role binds the `learner`. R4: Rule 9 applied to `sok-differential-privacies`, `feldman` baseline to `n/a`, `raz` tightness to `exponent`, `phase=n/a` on the eleven `family=none` rows that carry a phase |
| Wiki rows, done | Three `family` cells filled; 55 recodes under R1 to R4; 24 quotations supplied; six stale `cls_reason` texts annotated; one transposed row reclassified |
| Abstract, done | "Only \NumRelative{} works ... and \NumRelativeAttack{} of those" with the recounted macros; "with the deciding sentence of each source quoted" only after the 24 rows are filled |
| Section 4.2, done | Table of the thirteen fields with values and one-line definitions, in place of the revision narrative |
| Section 4.4, done | Restate the verification pass with a partition that sums to 200: 149 quotations on file, 27 evidenced absences, 24 hand rows; second pass 57 bound and verified, 85 unbound |
| Section 5, opening, done | One fully worked row, thirteen fields and the deciding quotation |
| Section 5.1, 5.2, done | Argue from shared vocabulary and concentration, and add a compact party by unit table for the attack works |
| Section 5.3, done | Recounted numbers; a table of the relative rows with both parties, both units and the relation as the source states it; drop the process sentences |
| Section 5.5, done | Table of the near-miss rows with the quantity each holds; close on the rows it is true of |
| Section 6.1, 6.4, done | Examples re-picked from rows the table places in each region, or recoded under R2 |
| Section 6.5, done | Cut the clause about restatements of Ball et al. of Ball et al. as universal, or cut the clause |
| Section 6.6, done | Compress the generative-exponent and batch-reuse paragraphs to one; keep the correction in the wiki |
| Section 3, done | Cut 3.3 and 3.6; fold 3.4 into 3.2; keep the terminology warning as one sentence |
| Section 7 | Move to the end of Section 2 or beside the near-miss row for the same work |
| Section 5, new | A priced threat model as a template with two instances, LiRA and PoL Property 2 with the exponent symbolic. This is the reviewer's version of the formalization section and it is half a page |
| Title, front matter | `SoK:` prefix; anonymous author block; ethics statement "None" with the reasoning |
| Supplement | Becomes the anonymized artifact; codebook becomes the five-page appendix |
| Bibliography, done | 0 unconfirmed; journals as `@article` with volume and pages, the last two in-press articles completed from Crossref; the page rule is waived for TMLR, which assigns none |
