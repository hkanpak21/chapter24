# survey/

A complexity-theoretic survey of machine-learning security. Separate from `exp/paper/`, which is a
later work that builds on this one.

**Working title.** *How Hard Is the Attack? A Complexity-Theoretic Survey of Machine Learning
Security.* The subject is the **characterization** of adversary capability in complexity-theoretic
terms — not the imposition of bounds, and not efficiency of training or inference.

## Start here

| File | Holds |
| --- | --- |
| `notes/2026-08-22-plan-survey-tasks.md` | **Read first.** Corpus state, settled decisions, and the task list keyed to wiki pages |
| `notes/2026-08-22-plan-survey-scope-and-structure.md` | Scope boundary, the framework, and the six-part structure with reasoning |
| `notes/2026-08-22-note-wiki-audit-findings.md` | What the verification pass found, and which claims it changed |
| `main.tex` | The draft |
| `sections/`, `figures/` | Section drafts and figures |

## Build

```
cd exp/survey && ../../.tools/tectonic -X compile main.tex --outdir .
```

Writes `main.pdf` and nothing else — intermediates are skipped, so no `.log` or `.aux` appears.
Turkish characters need `fontspec` with a Unicode font; `fontenc` with T1 drops `İ`.

## State, 2026-08-22

186 papers in `raw/`, 181 wiki source pages, **all 181 audited and quote-verified**, zero broken
links. The quote rule that blocked drafting is cleared. Every wiki page has its paper on disk.
