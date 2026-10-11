# CLAUDE.md — exp/

Programme directory for the computational security of learning. The active
deliverable is the SoK in `survey/`, which is its own project root on the
`research` skill's layout (`lab/ lib/ paper/ sink/` with `CONTEXT.md`). Start
there, at `survey/CONTEXT.md` and `survey/CLAUDE.md`.

**Read `docs/CONTEXT.md` first.** It carries the terminology ledger, the three attack families, and the
standing constraints. Nothing here repeats it.

- **Halil reads reports, not chat.** Substance goes in a report or it does not land. Keep chat to what
  is needed to agree on the next report.
- **Delegate report-writing to subagents** wherever the work can be scoped. Reserve the main thread for
  deciding what the report should argue.
- **Cross-reference for Obsidian.** The repo root is the vault. Every report links related reports,
  notes, and wiki pages with `[[wikilinks]]` by filename, so the graph view is navigable.
- Anything written for Halil goes to `docs/reports/YYYY-MM-DD-<tag>-<slug>.md`, five sections, verdict
  first. Validate with `python3 ~/.claude/skills/research/scripts/check-report.py`.
- Prose destined for a reviewer or PI uses the `academic-ste` register.
- Working notes and the long-form dialogue live in `docs/notes/`. They are not reports and are not
  held to the report format.
- `literature/related-work.md` is the ~80-problem reference-problem survey, grouped by tier.
- **`survey/` is the active deliverable**, migrated to the `research` skill's
  layout on 2026-09-17. Read `survey/CONTEXT.md` for the claim and the
  terminology ledger, `survey/lib/profs/rulings.md` for the decisions that must
  not be reopened, and `survey/lib/issues/` for what is open. The draft is
  `survey/paper/main.tex` and it builds with `cd exp/survey && make`.
  `survey/lib/numbers.csv` is the ledger every number comes from, and
  `survey/paper/results.tex` is generated from it.
- `docs/` holds the programme's own record, separate from the survey.
  `docs/CONTEXT.md` is the programme ledger and `docs/notes/` the long-form
  work. The survey's own reports moved under `survey/lib/reports/archive/`.
- The literature knowledge base is outside this project, at the repo root `wiki/`, governed by the
  repo root `CLAUDE.md`. That file also holds the record of refuted claims — read it before asserting
  novelty about anything.
