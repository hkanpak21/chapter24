# Output — Reports & Notes

Curated human-facing documents for the Formal Security research program. Where the [`wiki/`](../wiki/) is a knowledge graph (sources, concepts, entities, analyses) for navigation and reference, this folder holds **standalone reports and working notes** — things meant to be read end-to-end.

Last updated: 2026-04-23.

---

## Documents in this folder

### Proof notes

- **[proof.pdf](proof.pdf)** *(2026-04-23, 6 pages)* — End-to-end proof of an SQ-hardness reduction for black-box attacks on SQ-implementable learners. States the setting precisely (planted clique source, vertex-row encoding, SQ-implementable learner, black-box adversary), derives the primitive lower bound in 4 steps via FGRVX17 SQ-PC, and shows the adversary's distinguishing advantage is decoupled from its query budget. Specializations to attribute inference, backdoor activation, membership inference, and model extraction follow as corollaries. Includes concrete-security calibration and explicit caveats on what is and is not established. LaTeX source: `../.tools/proof.tex`. Compile with `../.tools/tectonic ../.tools/proof.tex --outdir output/`.

---

## External / inherited reports

These live at the project root rather than this folder, but are the principal external reports the wiki and notes build on.

- **[../compass_artifact_wf-6dd26eed-7b63-4913-af9a-4d6edcae8017_text_markdown.md](../compass_artifact_wf-6dd26eed-7b63-4913-af9a-4d6edcae8017_text_markdown.md)** — Theory-First Deep Research Survey (2024–2026 Frontier). External deep-research artifact verifying 7 candidate ingests from prior web research and adding ~14 additional theoretical papers across five pillars (agentic security, undetectable backdoors, LLM impossibility, statistical-computational gaps, certified robustness). All 20 papers from this survey are now ingested into the wiki as of 2026-04-23.

---

## Wiki analyses (referenced from this folder, hosted in the wiki)

The wiki's [`analyses/`](../wiki/analyses/) folder hosts longer synthesis pieces. They function as reports too, but live there because they cross-reference dozens of wiki pages and are the "synthesis side" of the knowledge graph.

- **[../wiki/analyses/reading-pathway-formal-security.md](../wiki/analyses/reading-pathway-formal-security.md)** *(2026-04-23)* — Recommended order-of-reading through the corpus, organized into Phase 0 (orientation) → Phase I (adversarial robustness) → Phase II (statistical-computational gaps) → Phase III (formal AI security). Includes four alternative entry-point pathways for different backgrounds (cryptography / learning theory / statistics / adversarial-ML practitioner) and time estimates.

- **[../wiki/analyses/web-research-2026-frontier.md](../wiki/analyses/web-research-2026-frontier.md)** *(2026-04-23)* — Web-research synthesis on what's new in the formal-security frontier 2024–2026. Maps the active research frontier, flags candidate ingests, updates open-problem status. As of the 2026-04-23 mega-batch ingest, this analysis has been updated to mark the LLM filter-impossibility gap as **resolved** by Ball-Gluch-Goldwasser et al. 2025 (arXiv:2507.07341).

- **[../wiki/analyses/deep-research-prompt-formalizing-ai-security.md](../wiki/analyses/deep-research-prompt-formalizing-ai-security.md)** *(2026-04-12)* — The original 16-question deep-research prompt that seeded much of the corpus. Spans the four pillars: adversarial robustness via concentration, statistical-computational gaps via reductions, formal AI security models, cross-cutting defenses.

---

## How the pieces fit together

The flow from external research → wiki → notes:

1. **External deep research** (compass artifact) identifies candidate papers and frontier results.
2. **Wiki ingests** convert each paper into a sources-page with deep cross-references to concept and entity pages, building a navigable knowledge graph. Done; 74 sources, 47 concepts, 68 entities as of 2026-04-23.
3. **Wiki analyses** synthesize across the graph: reading pathways, frontier maps, status updates.
4. **Output notes** propose new research directions building on the synthesis.

Reading order for a new collaborator entering this project:

1. Skim [reading-pathway](../wiki/analyses/reading-pathway-formal-security.md) — Phase 0 only — to get the three-pillar map.
2. Read the [compass artifact](../compass_artifact_wf-6dd26eed-7b63-4913-af9a-4d6edcae8017_text_markdown.md) end-to-end for the 2024–2026 frontier picture.
3. Read [web-research-2026-frontier](../wiki/analyses/web-research-2026-frontier.md) for what's resolved vs still open.
4. Read [research-direction-notes](research-direction-notes.md) for the proposed theoretical direction we're working on.
5. Drop into specific wiki source pages as the directions reference them.

---

## Status as of 2026-04-23

- **raw/** — 72 PDFs, all using `[INITIALS][YY]_[Topic].pdf` naming convention.
- **wiki/sources/** — 74 source pages, all deeply ingested per CLAUDE.md spec.
- **wiki/concepts/** — 47 concept pages.
- **wiki/entities/** — 68 entity pages.
- **wiki/analyses/** — 3 analyses (reading pathway, web-research frontier, original deep-research prompt).
- **output/** — 1 compiled proof PDF (`proof.pdf`) + this README. LaTeX source and compiler in `../.tools/`.
- **Lint** — 0 broken links, 0 orphan pages (1 only-aux: reading-pathway, expected for terminal synthesis).
