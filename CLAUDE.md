# CLAUDE.md — Wiki Schema for Formal Security Research

This file governs how you maintain the wiki in this repository. Read it at the start of every session. Follow it strictly.

---

## Role

The repo has **two strata**:
- `wiki/` — the literature knowledge base (75 sources, 47 concepts, 68 entities). You maintain this; schema below.
- `output/` — **the user's own research programme.** Active work lives here. You are a research collaborator, not a bookkeeper.

Default to `output/` unless the user explicitly asks for an ingest, query, or lint.

---

## Current Programme (as of 2026-07-25)

PhD proposal on the computational security of learning. Key artifacts:
- `output/chapter_24.md` — the theory, as a two-agent adversarial dialogue.
- `output/native-computational-problems-survey.md` — ~80 candidate reference problems.
- `output/ideas.md`, `LEARNING_aioracles.md`, `scratchpad.md` — **the user's own voice; highest-signal files here.** Read before proposing any direction.

**Established negative results — do not re-derive:**
- `COMP-MEM`'s marginal-advantage-over-baseline formulation is a no-op (baseline advantage = 0 by construction) and is already published: Yeom CSF'18 Def 6; Xiao–Devadas CRYPTO'23 "PAC Membership Privacy"; Desfontaines–Pejó PoPETs'20 dimension R.
- Memory-bounded-adversary crypto is mature: Raz FOCS'16 → Guan–Zhandry EUROCRYPT'19 → Dodis–Quach–Wichs EUROCRYPT'22/'23.
- Transformer-vs-RNN *learning* separations exist (arXiv:2503.11272); only the memory-sample mechanism is unclaimed.
- Open on two independent sweeps: no security definition anywhere quantifies over SQ- or low-degree-bounded adversaries.

---

## Directory Layout

```
FORMAL_SECURITY/
├── CLAUDE.md               ← this file (schema & instructions)
├── raw/                    ← immutable source documents (PDFs, markdown, etc.)
│   └── assets/             ← downloaded images referenced in sources
├── wiki/
│   ├── index.md            ← catalog of all wiki pages (always update on ingest)
│   ├── log.md              ← append-only chronological record (always append on any operation)
│   ├── overview.md         ← high-level synthesis of the whole research area
│   ├── entities/           ← pages for authors, research groups, venues, tools
│   ├── concepts/           ← pages for formal definitions, theorems, proof techniques, models
│   ├── sources/            ← one summary page per ingested source
│   └── analyses/           ← comparisons, synthesis pages, answers to queries worth keeping
```

**Never modify files in `raw/`.** They are the source of truth.

---

## Page Formats

### Source summary page (`wiki/sources/<slug>.md`)
```markdown
---
title: <Full paper/article title>
type: source
date_ingested: <YYYY-MM-DD>
authors: [Author1, Author2]
venue: <Conference/Journal/Preprint>
year: <YYYY>
tags: [tag1, tag2]
---

## Summary
2–4 paragraph overview of the source's contribution, methods, and findings.

## Key Contributions
- Bullet list of the most important results or ideas.

## Key Definitions / Theorems
List notable formal definitions, lemmas, or theorems introduced or used.

## Connections
Links to related wiki pages: concepts it uses or introduces, related sources, authors.

## Open Questions / Limitations
What the paper leaves open, caveats, or weaknesses noted by the authors or you.

## Quotes / Notable Passages
Verbatim excerpts worth preserving.
```

### Concept page (`wiki/concepts/<slug>.md`)
```markdown
---
title: <Concept name>
type: concept
tags: [tag1, tag2]
---

## Definition
Formal or informal definition of the concept.

## Intuition
Plain-language explanation.

## Properties / Theorems
Key results about this concept.

## Where It Appears
Sources and analyses that use or develop this concept.

## Related Concepts
Links to adjacent concept pages.

## Open Questions
Outstanding problems or debates around this concept.
```

### Entity page (`wiki/entities/<slug>.md`)
```markdown
---
title: <Entity name>
type: entity
entity_type: <author | venue | group | tool>
tags: []
---

## About
Brief description.

## Contributions / Works
Sources and concepts associated with this entity.

## Connections
Other entities this one collaborates with or relates to.
```

### Analysis page (`wiki/analyses/<slug>.md`)
```markdown
---
title: <Analysis title>
type: analysis
date: <YYYY-MM-DD>
tags: []
---

## Question / Motivation
What prompted this analysis.

## Findings
The substantive content.

## Implications for the Wiki
What should be updated or investigated next.
```

---

## Operations

### Ingest a source

1. **Read** the source file in `raw/`.
2. **Discuss** key takeaways with the user before writing anything.
3. **Write** a source summary page in `wiki/sources/<slug>.md`.
4. **Update or create** concept pages for all formal concepts introduced or heavily used.
5. **Update or create** entity pages for all authors and venues.
6. **Update** `wiki/overview.md` if the source meaningfully shifts the overall synthesis.
7. **Update** `wiki/index.md` — add the new source page and any new concept/entity pages.
8. **Append** to `wiki/log.md` using the format: `## [YYYY-MM-DD] ingest | <Source Title>`

A single ingest typically touches 5–15 wiki pages. This is expected.

### Answer a query

1. Read `wiki/index.md` to identify relevant pages.
2. Read those pages.
3. Synthesize an answer with citations to wiki pages.
4. **If the answer is substantive**, offer to file it as an analysis page in `wiki/analyses/`. Good answers are assets — don't let them disappear into chat history.
5. If you created a new analysis page, update `wiki/index.md` and append to `wiki/log.md`.

### Lint the wiki

Run this periodically when the user asks:
1. Scan for **contradictions** between pages — flag them.
2. Find **stale claims** that newer sources have superseded.
3. Find **orphan pages** with no inbound links.
4. Find **mentioned concepts** that lack their own page.
5. Check **missing cross-references** between clearly related pages.
6. Suggest **new sources** or web searches to fill data gaps.
7. Append a `## [YYYY-MM-DD] lint` entry to `wiki/log.md` summarizing findings.

---

## Conventions

- **Slugs**: lowercase, hyphens, no special characters. E.g. `statistical-query-model.md`, `boaz-barak.md`.
- **Internal links**: always use relative markdown links, e.g. `[Statistical Query Model](../concepts/statistical-query-model.md)`.
- **Tags**: use a consistent, small vocabulary. Core tags for this wiki:
  - complexity theory, cryptography, adversarial-ml, hardness-reductions, learning-theory
  - computational-indistinguishability, pseudorandomness, sample-complexity
  - one-way-functions, PAC-learning, statistical-query, planted-clique
  - robustness, evasion-attacks, poisoning-attacks, certification
- **Frontmatter**: always include YAML frontmatter on every wiki page (not on raw sources).
- **Never invent citations** — only reference claims that appear in a source you have read.
- **Contradiction handling**: when a new source contradicts an existing claim, update the relevant page to note both positions and cite both sources. Do not silently overwrite.
- **Verify novelty before endorsing it.** Any "nobody has done X" gets an adversarial web check — search *for* prior art, not for confirmation — before it goes in writing.
- **Record negative results.** "This is occupied" is as valuable as a positive finding; unwritten, it gets re-walked.
- **The user's examples are representatives, not targets.** Aim for the highest-generality formulation; don't build the theory around the first instance offered.

---

## Domain Notes

This wiki covers the formal study of security and learning, including:
- **Cryptographic hardness and reductions** in ML contexts (e.g. hardness of learning based on one-way functions, lattice problems)
- **Adversarial robustness** from a complexity/information-theoretic perspective
- **Statistical and computational gaps** — when statistical learnability outpaces computational learnability
- **Secret leakage / planted problems** — reducibility techniques using hidden structure
- **Formal models**: SQ model, PAC model, cryptographic game-based definitions, circuit complexity

---

## Gotchas

- `output/chapter_24.md` is 309KB — exceeds the Read tool's 256KB limit. Chunk with offset/limit or delegate to a subagent.
- `wiki/index.md` and `wiki/overview.md` are frozen at 2026-04-23 and materially wrong (index claims 16 sources; there are 75; 26 concept pages unlinked; neither mentions the user's own theory). **Do not orient from them.**
- `raw/*.pdf` is gitignored. Catalog is `raw/SOURCES.md`; naming is `[INITIALS][YY]_Topic.pdf`.
- `pdftotext <file>.pdf -` extracts the raw PDFs.

---

## Session Start Checklist

At the start of each session:
1. Read this file (`CLAUDE.md`).
2. Read the last ~5 entries of `wiki/log.md`.
3. Orient from `output/`, not from `wiki/index.md` — the programme is the active work.
4. Ask what the user wants. Do not assume it is an ingest.
