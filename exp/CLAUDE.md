# CLAUDE.md — exp/

Project root for the computational security of learning programme. Layout follows the `research`
skill: `literature/`, `lab/`, `paper/`, `docs/`.

**Read `docs/CONTEXT.md` first.** It carries the terminology ledger, the three attack families, and the
standing constraints. Nothing here repeats it.

- Anything written for Halil goes to `docs/reports/YYYY-MM-DD-<tag>-<slug>.md`, five sections, verdict
  first. Validate with `python3 ~/.claude/skills/research/scripts/check-report.py`.
- Prose destined for a reviewer or PI uses the `academic-ste` register.
- Working notes and the long-form dialogue live in `docs/notes/`. They are not reports and are not
  held to the report format.
- `literature/related-work.md` is the ~80-problem reference-problem survey, grouped by tier.
- `paper/` is intentionally unscaffolded: no venue, no deliverable fixed yet.
- The literature knowledge base is outside this project, at the repo root `wiki/`, governed by the
  repo root `CLAUDE.md`. That file also holds the record of refuted claims — read it before asserting
  novelty about anything.
