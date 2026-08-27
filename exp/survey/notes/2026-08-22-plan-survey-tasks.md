# Survey to-do and progress tracker

The working file for the survey. Tick boxes as things land. Every task names the wiki pages that
carry it, so the corpus and the paper stay attached.

Companion files: [[2026-08-22-plan-survey-scope-and-structure]] holds the scope boundary and the reasoning behind the structure;
[[2026-08-22-note-wiki-audit-findings]] holds what the verification pass found and what it changes; this file holds the
work. The literature itself is the repo-root `wiki/`.

**Read this first after a context compaction.** Sections 1 and 2 carry everything a new session needs
in order not to relitigate settled questions.

---

## 1. State, as of 2026-08-22

| | |
| --- | --- |
| Papers on disk | **206** in `raw/` (waves 5 and 6, 2026-08-22: learning-theory grounding and neural scaling laws), all catalogued in `raw/SOURCES.md` |
| Wiki | **199 sources**, 83 concepts, 116 entities. The 18 pages of waves 5 and 6 were written by ingestion agents and spot-verified; the rest carry the full 2026-08-22 audit |
| Audited to the claim-quantifier schema | **181 of 181 — complete** |
| Quote verification | **complete**; ~5% of 1100+ quotations were wrong, all marked in place |
| Broken internal links | 0 |
| Every wiki page has its paper on disk | **yes**, first time |
| Writing standard | **Changed 2026-08-22.** `research` now routes paper prose through `references/kupcu-writing.md` first, which is Küpçü's own deck and wins over `writing.md` on any conflict. One-page introduction under CGI-E, four-sentence abstract, refutable forward-referenced contributions, a running example starting in the introduction, related work after the solution, and emphasis allowed for structure. `references/checklist-paper.md` is the advisor's own list and governs the bibliography |
| Draft | Introduction and problem section written. `main.tex` plus `sections/00-abstract.tex` and `sections/01-problem.tex`, six pages including references |
| Linters | `lint.py --paper` and `lint.py --bib` both at **0 errors**. 38 paper warnings, all read and judged. 4 bib warnings, all traceable to venue strings that carry editorial commentary |
| Bibliography | `refs.bib`, **generated** by `tools/gen-bib.py` from wiki front matter. 181 entries, IACR keys, each carrying `annote = {wiki: <slug>}`. 94 still owed a venue check |
| Numbers | `results.tex`. Every number in the prose is a macro whose comment names the wiki page it came from |
| Build | `cd exp/survey && ../../.tools/tectonic -X compile main.tex --outdir .` — writes only `main.pdf`, no `.log` or `.aux` |

---

## 2. Standing decisions — settled, do not reopen

1. **Title direction.** The subject is the *characterization* of adversary capability in
   complexity-theoretic terms, not the *imposition* of bounds, and not efficiency of training or
   inference. Working title: *How Hard Is the Attack? A Complexity-Theoretic Survey of Machine
   Learning Security*. The word "efficiency" stays out of the abstract; it reads as GPU efficiency.
2. **Audience.** Machine-learning researchers. Every complexity-theoretic idea is introduced before
   it is used. The paper imports complexity theory into ML security, not the reverse.
3. **Sequence.** Document the landscape first, then let the formalization converge out of it. The
   framework is a contribution of this work, arrived at in Part IV, not assumed in Part I.
4. **The frame has an outside, deliberately.** Results with no resource content — the geometric
   inevitability line — sit outside the formalization, and the paper says so. They conclude
   inevitability *because* no resource enters them. A frame that swallows everything states nothing.
5. **`κ` takes the value "unstated".** When a paper does not state a party's budget, that is recorded
   as a value, not as a failure of the person doing the mapping. The count of "unstated" cells is a
   result of the survey.
6. **Coverage.** Every serious formal work in scope is covered. Scope test is in [[2026-08-22-plan-survey-scope-and-structure]] §2:
   about learning, makes a formal claim, and somebody's resources matter to the claim.
7. **Quotes.** Every page is now checked, so quotations may be used — but only those **not** carrying
   a `_Not verbatim_` or `_Not a quotation from the paper_` banner. Around 5% of 1100+ quotations were
   wrong and are marked in place rather than deleted. Never re-quote a banner-marked passage.
8. **The audit changed what several sections may claim.** Seven entries in the root `CLAUDE.md` were
   corrected, four of my own reports were wrong, and a dozen content errors were found that no quote
   check would have caught. Read [[2026-08-22-note-wiki-audit-findings]] before drafting any section of Part III.

---

## 3. Blocking work, before serious drafting

**CLEARED 2026-08-22. Drafting is unblocked.**

- [x] **Quote verification pass — done.** All 181 pages checked against their own PDFs. Findings and
      the reusable method are in [[2026-08-22-note-wiki-audit-findings]]. Two false-positive modes of the checker are
      documented there and in the root `CLAUDE.md`: spelling variants, and editorial glosses welded
      inside quotation marks. Both produced false fabrication charges against correct pages.
- [x] **`İ` fixed** without a font dependency. Tectonic runs XeTeX, so `inputenc`'s `utf8` option is a
      no-op and `\DeclareUnicodeCharacter` is unavailable. The name is written `Halil {\.I}brahim
      Kanpak` directly. The same constraint means `refs.bib` must be ASCII with LaTeX accent
      commands, which `tools/gen-bib.py` now emits.
- [x] **Bostrom epigraph cut.** Three reasons, the third decisive. It rendered above the title, it is
      a slogan where the writing standard asks for a fact, and the line is **I. J. Good's**, from
      *Speculations Concerning the First Ultraintelligent Machine* (1965), which Bostrom quotes. A
      survey whose thesis is that the field mis-states what its sources say cannot open on a
      misattribution. Restore it if wanted, attributed to Good.
- [ ] Commit the pending work. 226 files uncommitted at last count, plus this session's.

---

## 4. Papers to acquire

**All cleared 2026-08-22.** Twenty-one papers were fetched across three waves — eleven supplied by
hand, ten fetched directly, none paywalled. Dinur–Nissim came from a Stanford course mirror and
Xiao–Suh–Devadas from the author's MIT page. Catalogued in `raw/SOURCES.md` waves 3 and 4.

- [x] Ball, Rosen, Sabin, Vasudevan — average-case fine-grained hardness
- [x] Barak, Mahmoody — Merkle puzzles are optimal
- [x] Balle, Cherubin, Hayes — reconstruction robustness
- [x] Shokri et al.; Yeom et al. — the membership game and its baseline
- [x] Papernot et al. — the prior systematization
- [x] LAMP — gradient inversion; Suri, Evans — distribution inference
- [x] Meisingseth, Rechberger; Christ, Gunn, Zamir; Alvarez-Melis, Garg, Kalai
- [x] The eight primary PDFs owed for sweep-built pages, plus Siu et al. and Ashtiani et al.

Nothing outstanding. If a new gap appears, note it here.

## 5. The paper, part by part

### Part I — Introduction and the problem — **DRAFTED 2026-08-22**

Split in two, because Küpçü's deck fixes the introduction at one page and puts the contributions
list at its end. `sections/01-introduction.tex` carries Context, Gap, Innovation and Evidence with
the novelist as the running example, and ends in four refutable contributions, each pointing at the
section that delivers it. `sections/02-problem.tex` carries the three exhibits, the diagnosis and
the turn. Section files renumbered 01 to 07 to match.

**Two defects the user caught and what fixed them.** "Machine learning security produces formal
results" was a vague opener with no source, and the checklist bans a vague statement outright. It is
replaced by the novelist and the four incompatible verdicts. "Membership inference is the most
studied attack on a trained model" was an unbacked superlative, which the checklist bans by name
and `lint.py` flags as `unbacked`. It is replaced by a counted fact, at least ten new methods in
2024, with the citation that gives it.

**`landscape` is now on the linter's `slop` list.** Part III's heading is *Results by constrained
party*. The label `sec:landscape` is unchanged, so forward references still resolve.

Must make a reader feel the disorder before naming its cause, then earn the complexity-theoretic turn.

- [x] Exhibit 1: the same attack, opposite verdicts. Draw from [[mia-from-first-principles]],
      [[blind-baselines-beat-mia]], [[sok-mia-llms-rushing-nowhere]], [[do-mias-work-on-llms]],
      [[mia-cannot-prove-training]]. The verdicts range from "works" to "cannot be validated", and the
      spread tracks the adversary assumption, not the attack.
- [x] Exhibit 2: one object, two subfields, no contact. [[proof-of-learning]] states attacker cost
      against trainer cost as a bare requirement and, in its own body, as a conjecture the authors say
      they cannot prove; [[fine-grained-one-way-functions]] and [[pkc-fine-grained-setting]] have the
      same quantity as a definition. Neither cites the other.
- [x] Exhibit 3: defences broken inside their own threat models — [[obfuscated-gradients]],
      [[adaptive-attacks-defenses]].
- [x] State the diagnosis as **absence, not disagreement**. There is no standardized formal adversary.
- [x] Motivate the diagnosis rather than asserting it. Strongest support is the field speaking about
      itself: [[sok-adversary-knowledge]], [[sok-black-box-attack-pitfalls]], [[dos-and-donts-ml-security]],
      [[beyond-labeling-oracles]], [[sok-data-reconstruction-attacks]].
- [x] The pivot: the adversary is running an inference task, and complexity theory is the discipline
      that prices tasks. This is what earns the rest of the paper for an ML reader.
- [x] Position against the prior systematization, [[sok-security-privacy-machine-learning]].
      **Verified: it has no computational-resource axis** — its axes are pipeline stage, attacker
      write-power, access level, and goals. A resource-like quantity appears three times *inside* the
      survey (a poisoning fraction; "unbounded" meaning unbounded poisoning power; an ACRE
      query-complexity result) but never as an axis. The novelty claim is safe and can be stated
      precisely rather than vaguely.

### Part II — Background for an ML reader (≈6 pages)

Only the machinery Part III uses. Unembarrassed about being pedagogical.

- [ ] Security games, and why the baseline is part of the definition rather than an evaluation detail.
      Supporting: [[blind-baseline]], [[low-fpr-evaluation-regime]], [[membership-inference-game]].
- [ ] Adversary classes: polynomial time, statistical queries ([[statistical-query-model]]), low-degree
      polynomials ([[low-degree-polynomial-framework]]), bounded memory ([[bounded-storage-model]]),
      circuit classes ([[fine-grained-cryptography]]), function classes ([[capacity-bounded-privacy]]).
- [ ] Flavours of hardness: worst case against average case, conditional against unconditional.
      Supporting: [[statistical-computational-gaps]], [[average-case-reductions]].
- [ ] Reductions, and what a reduction does and does not transfer.
- [ ] Advantage, and why advantage without a baseline is not a quantity.
- [ ] Terminology warning: "fine-grained" in the privacy-ML literature means per-user access control.
      A keyword search returns the wrong field.

### Section 3 — Classifying the corpus  — **FORMAT SETTLED 2026-08-22**

Two layers, both generated by `tools/gen-tables.py` from `notes/classification-batch1.tsv`.
Never hand-written.

**Layer 1, four cross-tabulations.** Features on both axes, works in the cells by citation number.
This is the layer that carries an argument, because an empty cell is a combination nobody has
published. Order in the paper is deliberate: phase x access first (dense, the field does agree on
this), then party x unit (sparse, one dominant cell), then unit x tightness, then family x party.
`assessed` is a dagger on the citation rather than an axis.

**Layer 2, two per-work tables.** One row per work, the reference layer that makes every cross-tab
cell traceable. Kept in the body for now at Halil's request, for inspection.

**Already visible at 24 works:** the largest single cell is nobody-constrained-in-no-unit;
`attacker x memory` is empty, which is the programme's known open slot; and the attacker is priced
in cryptography's units (time, circuit size, queries) while the learner is priced in learning
theory's (memory, algorithm class, parameters). The two halves use disjoint units.

**Blocking:** 157 of 181 works are unclassified. 1991 cells needed reading, 264 are done.

### Part III — The landscape (≈20 pages, the bulk) — PARKED, see sections/parked/

Organized by which party is constrained and in what resource. Frame vocabulary used informally here;
formalized in Part IV. **Needs one running example carried through all six subsections** — decide which.

**III.1 Nobody is constrained — geometric inevitability**
- [ ] **Finding to state as a result:** of the 18 papers here, eleven constrain no party at all or
      constrain only the learner in samples; three price an adversary; and [[robust-estimators-high-dimensions]]
      inverts the picture entirely — the *defender* is the polynomial-time party while the adversary is
      unbounded on a counting budget. See [[2026-08-22-note-wiki-audit-findings]] §4.
- [ ] Core: [[curse-of-concentration]], [[adversarial-spheres]], [[adversarial-vulnerability-any-classifier]],
      [[universal-law-of-robustness]], [[computational-concentration-of-measure-etesami]].
- [ ] The worked example: the hypothesis was measured and does not hold —
      [[empirically-measuring-concentration]] — and one word names two opposite geometric properties,
      [[data-concentration-robustness-avoidable]], [[two-senses-of-concentration]].
- [ ] Robust PAC learning, where the constrained party is the learner and the resource is samples:
      [[vc-classes-adversarially-robustly-learnable]], [[robust-pac-learning-characterization]],
      [[lower-bounds-robust-pac-learning]], [[pac-learning-evasion-adversaries]],
      [[adversarially-robust-pac-regression]], [[tolerant-robust-pac-learning]].
- [ ] Audit debt: most of this subsection's pages predate the schema. Flag before quoting.

**III.2 The adversary is constrained coarsely — polynomial time against unbounded**
- [ ] Backdoors: [[planting-undetectable-backdoors]], [[io-undetectable-backdoors-nn]],
      [[unelicitable-backdoors-lms]], [[backdoor-defense-learnability-obfuscation]],
      [[oblivious-defense-backdoor-removal]].
- [ ] Robustness from hardness: [[win-win-robust-learning]], [[computational-hardness-robust-learning]],
      [[adversarial-examples-computational-constraints]], [[adversarial-examples-prg]].
- [ ] Computational privacy: [[computational-differential-privacy]], [[limits-cdp-client-server]],
      [[separating-cdp-client-server]], [[towards-separating-cdp]], [[two-party-dp-complexity]],
      [[cdp-inner-product-implies-ot]].
- [ ] The worked example: the impossibility everyone cites excludes classifiers, graphs and synthetic
      databases **by name** — [[limits-cdp-client-server]], exclusions quoted verbatim on the page.
- [ ] Alignment, where the constrained party is the auditor: [[filter-impossibility-ai-alignment]].
      State the claim as existential; the page was corrected on 2026-08-20 for exactly this.

**III.3 The adversary is constrained by algorithm class**
- [ ] The canon: [[feldman-statistical-algorithms-planted-clique]], [[brennan-sq-lowdegree-equivalence]],
      [[low-degree-polynomials-survey]], [[low-degree-estimation-schramm-wein]],
      [[holmgren-counterexamples-low-degree]], [[bandeira-franz-parisi-criterion]].
- [ ] Security uses: [[bogdanov-low-degree-planted-subgraph]], [[cryptography-from-planted-graphs]],
      [[pke-from-planted-clique]], [[capacity-bounded-dp]], [[kernel-quantum-renyi-audit]].
- [ ] **Corrected reading, mandatory:** [[bogdanov-low-degree-planted-subgraph]]'s security
      quantifies over **size-bounded circuits** (Props 4.1, 4.3), not low-degree adversaries; its
      headline conjectures are stated in polynomial time with low-degree offered as *evidence*. The
      same is true of [[cryptography-from-planted-graphs]]. **No security definition in either
      quantifies over a low-degree adversary.** See [[2026-08-22-note-wiki-audit-findings]] §2.
- [ ] **The limit that must appear:** [[quasi-poly-low-degree-conjecture-false]] and
      [[rigorous-implications-low-degree]]. Low-degree-bounded and quasi-polynomial-bounded are
      provably different. Carry the clauses recorded in `CLAUDE.md` — the polynomial-time distinguisher
      is for the rectangular generalisation, and the noise condition rather than permutation
      invariance is what is universal in the positive counterpart.
- [ ] Correct the record in passing: [[certificates-statistical-algorithms]] is a query-bounded
      *verifier* result, not an SQ-bounded adversary.

**III.4 The adversary is constrained relative to the honest party**
- [ ] Fine-grained cryptography: [[fine-grained-one-way-functions]], [[pkc-fine-grained-setting]],
      [[fine-grained-cryptography]], [[permissionless-consensus-fine-grained]],
      [[fine-grained-nike-lower-bounds]], [[fine-grained-nike-revisited]],
      [[nike-without-idealized-assumptions]], [[sequential-functions-fine-grained]],
      [[fine-grained-world-without-crypto]].
- [ ] **The correctness trap, now three conventions not two:** [[fine-grained-one-way-functions]]
      (non-uniform circuit size, `honest^{1+δ}`), [[pkc-fine-grained-setting]] (uniform word-RAM time,
      `T^{1−δ}` vs `T`), and [[average-case-fine-grained-hardness]] (uniform word-RAM, with `ε` indexed
      by **the adversary's own discount** as well as by `n`). Quoting the third as a single number
      quotes something the paper does not define. State all three and the conversions.
      Recorded on [[security-gap-exponent]].
- [ ] **The ceiling is a query bound, not a time bound.** [[merkle-puzzles-are-optimal]]: Eve makes
      `(16n/δ)²` **oracle queries**, and the authors note she "can be implemented efficiently in a
      relativized world where P = NP". It forbids a super-quadratic *query* gap in the ROM and says
      nothing about *time* gaps. This widens what a compute-priced claim may promise.
- [ ] Say plainly that this section has zero machine-learning content, and that this is the finding.

**III.5 The constrained party is the learner, defender or mechanism**
- [ ] Memory: [[raz-parity-time-space]], [[bounded-storage-simple-schemes]],
      [[speak-much-remember-little]], [[authentication-bounded-storage]], [[bsm-key-agreement-owf]],
      [[dp-adaptive-analysis-bounded-space]], [[adaptive-vs-oblivious-streaming]].
- [ ] Parameters: [[overparameterization-computational-constraints]], paired against
      [[universal-law-of-robustness]] — computational against information-theoretic, same question.
- [ ] Learner priced in statistical queries: [[what-can-we-learn-privately]],
      [[learnability-deep-random-networks]].
- [ ] The mechanism's own runtime as a leakage channel: [[dp-against-timing-attacks]].
- [ ] Trainer compute: [[fine-grained-erm]], [[fine-grained-gradient-llm]].

**III.6 Learning theory's own units**
- [ ] The units: [[information-exponent-online-sgd]], [[generative-exponent-single-index]],
      [[leap-complexity-sgd]], [[merged-staircase-property]], [[generative-leap-multi-index]],
      [[noise-sensitivity-exponent]].
- [ ] **Caveat one:** multi-pass gradient descent escapes the earlier exponents, so they price
      single-pass training, not intrinsic hardness — [[reusing-batches-breaks-exponents]].
- [ ] **Caveat two:** the thresholds are for *detection*; an attacker who must reconstruct is doing
      *estimation*, whose threshold is open.
- [ ] The near-miss pattern: adversary present in the theorem, carrying no price —
      [[robust-multi-index-sq-bounds]], [[robust-single-index-efficient]].

### Part IV — The formalization (≈5 pages)

**State, 2026-08-22, evening.** `oracle.tex` grew a results section, `price.tex` (16 pp total):
the price of aiming grounded in the SQ floors with the generative exponent as the surviving unit
(the information exponent and the leap fell to batch reuse and learning-rate transitions and are
cited only as what not to use); the price of skipping scoped recipe-relative, with amortization
and the view-versus-trace gap as definitional consequences; and the sparse-parity experiment,
`t_c ∝ d^2.02` at k=3 (the d^{k-1} law), 40 of 40 runs, plus a batch-8 wall (d=30 solves in ~7k
steps, nine runs at d≥60 all exhaust 300k). Experiments under `exp/survey/experiments/`, figure
under `figures/`, every number a macro in `results.tex`. Two documents under `formalization/`, both compiling, both self-contained.
`games.tex` (10 pp) holds the extraction games with two-party pricing, reviewed adversarially and
rebuilt. `oracle.tex` (12 pp) holds the framework itself: the learning oracle in passive and
interactive form, traces, views, ports, write and read budgets, the two criteria, the generic
adversary class, and the corpus mapped onto it. Read `oracle.tex` first. Agreed in discussion and
fixed there: the oracle idealizes the training map and nothing else; its output is the full trace;
what a party sees is a view, a game parameter, never an oracle feature; recipe noise and view noise
are different objects; white-box is possession of weights with unlimited ordinary computation on
them; the generic adversary is a learning-oracle algorithm; cryptanalytic extraction is a generic
attack on a structured class, not a structural attack. Settled against extraction from the survey:
the oracle is **invented and defended**, with the AIOracle generic learning model as its named
precedent. Open, and listed at the end of `oracle.tex`: the non-triviality condition for the
backdoor game, where the planter writes, the declaration line, uninstantiability.

- [ ] State the experiment: the chain from source to output, the access point as the channel, `R` as
      what must be extracted and to what tolerance, `κ` as a per-party ledger, and the baseline.
- [ ] Show `κ` per-party absorbs the cases Part III separated — attacker-bounded, learner-bounded,
      auditor-bounded, and the relative form `κ_A ≥ κ_L^{1+δ}`.
- [ ] Define "unstated" as a legal value of `κ`.
- [ ] **State what the frame does not hold, and why the boundary is informative.**
- [ ] Reuse the programme's existing vocabulary rather than coining new terms. See
      `exp/docs/CONTEXT.md` for the terminology ledger, and the reports on `R` as quantizer and on
      test-time attacks as learners.

### Part V — The mapping (≈8 pages)

- [ ] Build the tables. **Generate from wiki front matter, do not hand-write** — `claim_quantifier`,
      `antecedent`, `adversary_bound`, `model_class`, `algorithm_class` exist for this purpose. A
      hand-built mapping will drift from the corpus.
- [ ] Write the generator script; put it in `exp/survey/` so the tables can be rebuilt.
- [ ] Make the cells decidable enough that two readers agree. Test this on a sample before committing
      to the format.

### Part VI — What the mapping shows (≈5 pages)

- [ ] The empty cells, each with the method that established emptiness, not an assertion:
      no security or privacy paper uses the learning exponents as an adversary's cost (514 citation
      records, five passes); no fine-grained notion applied to learning or privacy; no ML adversary
      bounded by memory; no ratio-parameterized privacy notion.
- [ ] The count of "unstated" cells.
- [ ] The near-misses — a quantity in hand and not named. [[proof-of-learning]] Conjecture 1,
      [[polo-proof-of-learning-ownership]] measured ratios, [[cryptanalytic-extraction-nn]] query
      counts in cryptanalytic notation, [[catch-a-chinchilla-compute-monitoring]] hardness clause with
      no construction.
- [ ] **The considered rejection, reported neutrally.** [[obfuscated-gradients]] and
      [[on-evaluating-adversarial-robustness]] state that restricting adversary computation is not
      meaningful. This is a position, not an oversight, and presenting it as an oversight loses the
      audience. Then the two later collisions: [[adaptive-test-time-defenses-eval]] floats the ratio
      and drops it, [[sok-black-box-attack-pitfalls]] makes runtime a comparison metric.
- [ ] Open problems.

---

## 6. Infrastructure

- [x] **`tools/gen-bib.py`** — generates `refs.bib` from `wiki/sources/*.md` front matter. Keys are
      IACR style per the `research` skill's `conventions.md`, collisions take a lowercase suffix in
      slug order, and every entry carries `annote = {wiki: <slug>}` so Part V's tables can be joined
      to the corpus mechanically. Rerun it after any wiki front-matter change. It prints the count of
      entries still carrying `venue-unconfirmed`.
- [ ] Write the sweep records as durable notes under `exp/survey/notes/`, so the emptiness claims in
      Part VI are checkable by a reader rather than taken on trust.
- [ ] Venue verification pass before the bibliography is fixed. **90 of 181** entries carry
      `venue-unconfirmed` in `refs.bib`, down from 94. **Method that works with no web access:**
      grep the extracted text of all 186 PDFs for how other papers in the corpus cite the target,
      and take the venue when several bibliographies agree. This resolved BC22, LLW19, TCBM20 and
      CAPBRTGMK19 in one pass. Corrections logged in [[2026-08-22-note-corrections-from-halil]] C10.
- [x] **`tools/cite-weight.py`** — reports the tier and age of every citation in a section, so the
      citation hierarchy is checked rather than remembered. Run before handing any section over. Many pages carry "venue unconfirmed
      from PDF" because arXiv copies state no venue.
- [ ] Regenerate `wiki/index.md`, which is frozen and materially wrong. Do this once, late.
- [x] **Running example: there is none, and that is the answer.** Membership inference appears in
      21 of 181 source pages and is the subject of none of Part III's six subsections. The
      advisor's checklist asks for a paper-long running example *if one exists*, and for this corpus
      one does not. Membership inference carries the introduction and Section 2 only. Each Part III
      subsection carries its own worked case. See [[2026-08-22-note-corrections-from-halil]] C12.
