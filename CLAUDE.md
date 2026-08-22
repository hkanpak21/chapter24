# CLAUDE.md — Wiki Schema for Formal Security Research

This file governs how you maintain the wiki in this repository. Read it at the start of every session. Follow it strictly.

---

## Role

The repo has **two strata**:
- `wiki/` — the literature knowledge base (110 sources, 62 concepts, 84 entities as of 2026-08-20). You maintain this; schema below.
- `exp/` — **the user's own research programme** (renamed from `output/` on 2026-08-05; "experimental" and "exponential"). Active work lives here. You are a research collaborator, not a bookkeeper. It follows the `research` skill layout — `literature/`, `lab/`, `paper/`, `docs/` — and has its own `CLAUDE.md` and `docs/CONTEXT.md`. **Read `exp/docs/CONTEXT.md` before proposing any direction.**

Default to `exp/` unless the user explicitly asks for an ingest, query, or lint.

---

## Current Programme (as of 2026-07-25)

PhD proposal on the computational security of learning. Key artifacts:
- `exp/docs/CONTEXT.md` — terminology ledger, the three attack families, standing constraints. **Start here.**
- `exp/docs/reports/` — the channel back to the user; five sections, verdict first.
- `exp/docs/notes/chapter-24.md` — the theory, as a two-agent adversarial dialogue.
- `exp/literature/related-work.md` — ~80 candidate reference problems, by tier.
- `exp/docs/notes/ideas.md`, `LEARNING_aioracles.md`, `scratchpad.md` — **the user's own voice; highest-signal files here.** Read before proposing any direction.
- **Scope, as of 2026-08-05: measurement, not hardness.** The goal is to measure an attack's capability against a concrete adversary. No defence mechanism is being proposed yet.

**Established negative results — do not re-derive:**
- `COMP-MEM`'s marginal-advantage-over-baseline formulation is a no-op (baseline advantage = 0 by construction) and is already published: Yeom CSF'18 **Definition 4 / Experiment 1** — corrected 2026-08-22, the earlier note cited Def 6 and that is the wrong definition. Def 4 is *Membership advantage*, where `b` is a fair coin and the paper proves `Pr[b=0|z] = Pr[b=1|z]`, concluding "the only way to gain advantage is through access to the model" — that is the zero-by-construction result. Def 6 is *Alternative attribute advantage*, its baseline is the **Bayes optimal simulator** rather than one half, and it is therefore not degenerate; the authors reject it for the opposite reason, that it rewards model accuracy. The substance of this negative result stands, the citation did not; Xiao–Devadas CRYPTO'23 "PAC Membership Privacy"; Desfontaines–Pejó PoPETs'20 dimension R.
- Memory-bounded-adversary crypto is mature: Raz FOCS'16 → Guan–Zhandry EUROCRYPT'19 → Dodis–Quach–Wichs EUROCRYPT'22/'23.
- Transformer-vs-RNN *learning* separations exist (arXiv:2503.11272); only the memory-sample mechanism is unclaimed.
- ~~No security definition quantifies over SQ/low-degree adversaries~~ — **RETRACTED 2026-07-25, this was false.** Low-degree analysis underwrites real crypto functionality: Bogdanov–Jones–Rosen–Zadik TCC'24 (arXiv:2409.16227) → PSM + secret sharing; Abram–Beimel–Ishai–Kushilevitz–Narayanan TCC'23. **But the retraction was too broad, corrected 2026-08-22.** BJRZ's cryptographic applications, **Propositions 4.1 and 4.3, quantify over `(s,ε)`-indistinguishability, i.e. size-bounded circuits** — Prop 4.1's proof builds an explicit circuit from a hypothesised distinguisher. Its headline Conjectures 1.3 and 1.4 are stated in **polynomial time**, and the paper says it provides "evidence for these conjectures in the form of lower bounds against the low-degree polynomial computational model". So BJRZ does exactly what ABIKN does: **security over size-bounded circuits, low-degree as supporting evidence.** No security definition in either paper quantifies over a low-degree adversary. The authors also note planted clique and planted subgraph "technically do not satisfy the noise-robust assumption of the low-degree conjecture". ~~SQ-quantified soundness: Ngo–Kim arXiv:2607.15528~~ — **the Ngo–Kim half is now itself retracted, 2026-08-20, verified against the PDF.** Its Def 1 "Universal Soundness" quantifies over an *unrestricted* cheating prover; the SQ restriction sits on the algorithm being certified and on the verifier's query budget. It is a query-bounded *verifier* result, not an SQ-bounded adversary. Note also that ABIKN TCC'23's security theorem quantifies over **size-bounded circuits**; the low-degree analysis is supporting evidence, not the adversary class.
- **Low-degree security has a hard new caveat (2026-08-20).** Buhai–Hsieh–Jain–Kothari FOCS'25 (arXiv:2505.17360) **disprove** the quasi-polynomial low-degree conjecture in the regime it was stated: they exhibit permutation-invariant planted distributions with vanishing low-degree advantage whose noisy distinguishing problem is solvable far faster than the conjecture allows. So "low-degree-bounded adversary" and "quasi-polynomial-time adversary" are **provably different**. The positive counterpart is Hsieh–Kane–Kothari–Li–Mohanty–Tiegel STOC'26 (arXiv:2601.05850). **Corrected 2026-08-20:** what is universal across its three results is the **noisy** version of the problem, not permutation invariance — Theorem 1.2, the Gaussian symmetric-polynomial result, assumes only that `P` is a distribution over `R^n`, because the test class already supplies the symmetry. Theorems 1.1 and 1.3 do assume permutation invariance. None rules out all polynomial-time algorithms. Buhai et al.'s refutation likewise needs a clause: the **polynomial-time** distinguisher is for the rectangular generalisation; in the square `S_n`-symmetric regime where the conjecture was stated the distinguisher is `n^{O(log^{1/(k−1)} n)}`, and closing that is open. Their second, largest-eigenvalue construction has a non-product null and so does not refute the conjecture at all. Any security claim resting on a low-degree adversary must cite both papers with these clauses.
- **Groce–Katz–Yerukhimovich does NOT say what the folk version says** (checked 2026-08-20 against the primary PDF). The impossibility applies to **black-box** constructions, and to queries with output in `R^n` for **constant** `n` under a "natural" class of utility measures. The authors state their own limitations explicitly, verbatim from the PDF: "There are several types of queries to which our results do not apply. The most important are queries with outputs that cannot naturally be thought of as tuples of real numbers. This includes, e.g., queries that return classifiers (as in [9]), graphs, or synthetic databases." Also excluded: `R^n` for `n` growing with the security parameter; utility functions with no polynomial bound on error; and multiple queries except a constant number, or arbitrarily many answered independently by a stateless server. Released models are exactly the excluded case, so "computational DP buys nothing in the single-curator setting" is not an objection to a compute-bounded adversary over model releases. The single-curator question is also no longer fully open: Bun–Chen–Vadhan TCC'16-B separate infeasibly, and Ghazi–Ilango–Kamath–Kumar–Manurangsi FOCS'23 (arXiv:2301.00104) separate against **unbounded** SDP mechanisms under NIWI + laconic keyless CRHF + diO — but their separation **breaks against quasi-polynomial adversaries**, and the task is contrived. What remains open is a separation on a *natural* task.
- **A reusable proof template, from Ghazi et al. FOCS'23:** prove privacy against a restricted **decision-tree** adversary class first, then *lift* to computationally bounded adversaries with cryptography. This is the restricted-class-then-computational argument the programme wants, already in use.
- **The unit exists, and it is the generative leap exponent** (found 2026-08-20). Damian–Lee–Bruna arXiv:2506.05500: `n = Θ(d^{1∨k*/2})` for Gaussian multi-index models, with a **low-degree lower bound and a matching efficient upper bound** — one number that is simultaneously both, defined against an algorithm class. It dominates the information exponent (Ben Arous–Gheissari–Jagannath JMLR'21) and the leap (Abbe–Boix-Adserà–Misiakiewicz COLT'23, whose matching bound is **CSQ only**, and whose `Θ̃(d^{max(Leap,2)})` is a *conjecture* — the proved Gaussian CSQ bound is `d^{Leap/2}`).
- **Detection, not estimation — the caveat that matters most for pricing an attacker (2026-08-20).** Damian–Pillaud-Vivien–Lee–Bruna Remark 3.3, verbatim: "Theorem 3.2 primarily measures the detection threshold." They flag a known detection/estimation gap on a related problem where SQ algorithms need `n ≳ d^{k*/2+1}` for *estimation*, and leave the estimation threshold open. An attacker who must **recover** something — reconstruct a record, recover a support, extract a model — is doing estimation, not detection, so the estimation threshold is the one the programme actually needs and it is **not established**. The low-degree half of the single-index result is additionally conditional on their Conjecture 3.4. **Load-bearing caveat:** Dandi et al. ICML'24 (arXiv:2402.03220) show multi-pass GD with batch reuse escapes the information- and leap-exponent barriers, so these are properties of *single-pass* SGD, not intrinsic hardness — an adversary that reuses batches steps out of the unit. Also: for polynomial links and for deep nets with an `r`-dimensional first hidden layer, `k* ≤ 2`, so large-`k*` instances are fine-tuned constructions.
- **Zero security citers, re-verified adversarially 2026-08-20.** A sweep instructed to *refute* the earlier finding pulled 514 citation records across the five exponent papers, built a venue histogram (0 hits in S&P/USENIX/CCS/NDSS/CRYPTO/EUROCRYPT/TCC/PoPETs), resolved 259 unique arXiv citers by category (**exactly one** cs.CR: arXiv:2310.01959, one passing sentence that does not use the quantity), and found 0 IACR ePrint metadata hits for each exponent name. The cell is empty.
- **Open slot: memory.** No security or privacy definition bounds an **ML or privacy adversary** by memory or space. Every hit puts the space bound on the learner (Raz FOCS'16), the mechanism (Dinur–Stemmer–Woodruff–Zhou EUROCRYPT'23), or the defender (Kaplan–Mansour–Nissim–Stemmer CRYPTO'21).
- **Terminology trap:** "fine-grained" in the privacy-preserving-ML literature almost always means *per-user access control*, not fine-grained complexity. A keyword search returns the wrong sense. Search by definition shape, not by name.
- "Attacker needs more samples than the trainer" is published: Haghifam–Smith–Ullman arXiv:2508.19458, MIA vs Gaussian mean estimation, `m ≳ n²ρ²+n`. IT units (Ingster/χ²), unbounded adversary. **Verified in full 2026-08-22, and it holds** — the abstract states it verbatim: "Our result is the first to show that the attacker sometimes needs many more samples than the training algorithm uses to train the model." Three boundary facts to carry: the antecedent is `d > c₁(n + n²ρ²)`; the success tolerance is only 0.02 (TPR ≥ 0.51, FPR ≤ 0.49); and **the separation vanishes when the attacker knows the covariance** (Thm 1.2 gives `min{n, 1/ρ²} ≤ n`), so what it prices is ignorance of `Σ`, not attack difficulty as such. Competitive hazard confirmed: the technique is the Ingster–Suslina χ² second-moment method over planted subspaces, one step from a low-degree restatement.
- Security-relevant SQ separation exists: Bubeck–Price–Razenshteyn ICML'19 (in wiki, W3) — but the *defender* fails there, not the attacker.
- Attacker-as-restricted-class-learner is occupied in **crypto** units: Canetti–Karchmer TCC'21; Karchmer SaTML'23; Christiano–Hilton–Lecomte–Xu arXiv:2409.03077; arXiv:2504.20310. Only the *units* are unclaimed.
- Detection ⟺ generation for learned distributions — **corrected 2026-08-22 against the PDF, the earlier note was wrong on two of four points.** Alvarez-Melis–Garg–Kalai NeurIPS'22, correct title *Are GANs overkill for NLP?*. §5 does give **both directions** (Lemmas 1 and 2), but **not in polynomial time** — the paper says its §5 reduction is "efficient for a single step, but the increase in runtime would lead to a general exponential-time algorithm". The polynomial-time result is **§6**, in a different (next-token distinguishability) model, and runs **one direction only**: from likelihood maximization to distinguishability, with no converse stated. There is also **no bounded distinguisher class and no runtime bound on any distinguisher**; §5 restricts `f` to no class, and Theorem 1 charges distinguisher cost as free parameters. Both directions are **empirical**, measured on a fixed sample rather than against the population, and Lemma 2 needs common support (bounded likelihood ratio), which a mode-collapsed generator violates. Not framed as security. Black-box version is provably **false**: Song arXiv:2404.03272 **§1.3 item 3 — there are no subsections 1.3.1/1.3.2/1.3.3; §1.3 is a three-item list titled *Future directions*. The black-box statement is also not proved by Song: it is Bruna–Regev–Song–Tang's result restated, conditional on worst-case lattice hardness.**
- **Fiber-of-the-training-map framing is REFUTED at its core** (checked 2026-07-26). Size-vs-navigability *with* a complexity separation is Dinur–Nissim PODS'03 — **three clauses of the earlier note are false, corrected 2026-08-22 against the PDF.** The headings are **§3.1 "Exponential Adversary" and §3.2 "Polynomially Bounded Adversary"**, sibling subsections inside §3, not §3 vs §4. The separation is **not** the main theorem: the abstract says "Our main result is a polynomial reconstruction algorithm of data from noisy (perturbed) subset sums", and §3.1 is a warm-up on very small databases. And the **OLS example is not theirs** — "OLS", "least squares" and "regression" occur zero times as words; the attack is a **linear program over subset sums plus rounding at 1/2**. The bounds are right: `E = o(n)` is fatal against an exp(n) adversary, `E = o(√n)` against poly(n), and `Õ(√T(n))` suffices against time-`T(n)`. Restated as "computational vs statistical memorization" by Kaplan–Mansour–Nissim–Stemmer arXiv:2505.23658 (ITCS'26). A computational security notion for reconstruction already exists and is *equivalent to one-wayness*: Cohen et al. arXiv:2405.15753 — Def C.1 is the computational notion, but the equivalence to one-wayness is **Theorem C.5**, and it carries an antecedent the earlier note dropped: `f` must be efficiently computable **and well-spread** (Def C.4). Narcissus resiliency also does **not compose** in general (Appendix D). So "is training a OWF" is occupied, under those hypotheses. Training-map identifiability-vs-optimization: Shen et al. arXiv:2602.08723.
- **Fiber survivor — the best-defined target found this session:** a *hardness theorem* for **constrained** fiber navigation on the **training** map. Suliman et al. arXiv:2411.05658 conjecture it verbatim and stop — **but the paper's framing was misrecorded, corrected 2026-08-22.** Its title is *Towards a Re-evaluation of Data Forging Attacks in Practice* and its actual result is **empirical**: published forging attacks miss the reproduction-error threshold by orders of magnitude and are therefore detectable. The conjecture is real but incidental to the paper, names no adversary class, reference problem or hardness assumption, and the paper says nothing about the evaluation-vs-training map distinction; Jagielski et al. USENIX Sec'20 proved NP-hardness for the **evaluation** map only. Also open: CDP/SDP applied to reconstruction from weights (verified negative across Beimel–Nissim–Omri → Ghazi et al. FOCS'23).
- Fiber obstacles/must-cites: Xiao–Suh–Devadas CCS'24 — **narrower than recorded, checked 2026-08-22.** Theorem 1 is an **IND-CPA impossibility about the encoding `T`**, not about a training map, and "one-way function" appears nowhere in the paper. The adversary chooses the challenge distributions and its own concept class, which is where "worst case" lives, and the authors name two escapes: restrict the adversary's plaintext choice, or deny it the model trained on encoded data. Correct title is *Learnable Obfuscation*, not "Learnable Encryption"; Proof-of-Learning, Jia et al. S&P'21 (a "spoof" *is* fiber navigation priced in compute); forging/unlearning — Thudi et al. USENIX Sec'22, Kong et al. arXiv:2303.03648.
- **"Compute amount rather than hardness" is fine-grained cryptography** (checked 2026-07-26). Canonical: Brzuska–Couteau EUROCRYPT'22 / J.Cryptology'24 Def 6 (`(ε,δ)`-fine-grained OWF: no circuit of size `< |f|^{1+δ}` inverts); LaVigne–Lincoln–Vassilevska Williams CRYPTO'19 Def 5 (**"the gap"** as a named object); Ball–Rosen–Sabin–Vasudevan STOC'17 Def 2. **Write it as an exponent (`honest^{1+δ}`), not a constant `c`.** Hard ceiling: Barak–Mahmoody CRYPTO'09 — an Eve making `(16n/δ)²` **oracle queries** breaks any `n`-query ROM key exchange. **This is a query bound in an idealized model, not a standard-model time bound** (their adversary "can be implemented efficiently in a relativized world where P = NP"), so it forbids a super-quadratic *query* gap and says nothing about super-quadratic *time* gaps or structured assumptions; Afshar et al. EUROCRYPT'23 caps 3-NIKE at `O(n²)` in Maurer's GGM. Barriers: BRSV §5.2 (NSETH); Alman–Huang–Yeo EUROCRYPT'25 (no OWFs ⟹ average-case k-SUM/Zero-k-Clique false).
- **Near-collision with the Phase-2 idea, privacy corner:** Chaudhuri–Imola–Machanavajjhala NeurIPS'19 **capacity-bounded DP** (arXiv:1907.02159) bounds the adversary *"not in computational power, but in terms of the function class from which their attack algorithm is drawn,"* via restricted f-divergences. That is a function-class-restricted adversary for privacy — closer to the learning-adversary proposal than Bogdanov et al. Read before writing anything about restricted-class privacy.
- **Two seams left by the compute-amount sweep**, both ML-side: (a) Proof-of-Learning's `E[C_A] ≥ E[C_T]` (Property 2, Def 2) is a **bare inequality** — never parameterized into a δ-indexed family, and PoL does not cite BRSV/LLW; (b) **no fine-grained/ratio-parameterized privacy notion exists** — CDP is asymptotic, capacity-bounded DP is a function class. Also: model extraction has no formal success definition (arXiv:2310.01959 says so from inside). **Caveat: the machinery is off-the-shelf, so the contribution must be a theorem at a stated δ, not a definition.**
- **Methodological, 2026-07-26:** four novelty claims checked this session, four refuted. The single survivor was verified by **citation-graph sweep**, not topic search. Topic search has 0/4 in this area. Prefer starting from a *named published conjecture* over hunting empty framings.
- **Still open, narrowly:** attacker and defender priced in the *same* exponent units (information/generative exponent, leap), separated at matched budget, attacker restricted to training's own algorithm class. Citation-graph sweep of BGJ'21, ABM COLT'22+'23, DPVLB COLT'24, generative-leap: **0** security/privacy citers. Song arXiv:2404.03272 **§1.3 item 2** names "discriminators with bounded compute or memory" as open from inside the CLWE literature — verbatim and confirmed. Note item 2 also says a sampler asked only to fool computationally bounded testers "could simply generate standard Gaussian samples and fool any polynomial-time test", so the lattice gate is on `L²`-accurate **score estimation**, not on sampling.

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
- **The pre-2026-08-20 wiki pages present paraphrase as quotation. Verify every quote before citing.**
  Established 2026-08-20 by extracting all 164 `raw/` PDFs to text and checking every blockquote in
  `wiki/sources/` against them with punctuation- and hyphenation-proof matching. Two contamination
  paths were found and 30 passages corrected. (1) **Sixteen quotes on thirteen pages were the compass
  survey artifact's own editorial prose**, laundered into quotation marks and attributed to the papers
  — strings such as "the cleanest current theoretical extension" appear in
  `.sink/compass_artifact_*.md` and in none of the 164 papers. (2) **Fourteen quotes on eleven
  core-theory pages failed a first automated check**, and that check itself had a false-positive mode,
  corrected 2026-08-20 on re-audit. **The Bubeck-Sellke accusation was wrong:** the paper does say
  "overparametrization is necessary if one wants to interpolate the data smoothly", verbatim in the
  abstract. The first search used the American spelling "overparameterization" (0 hits); the paper
  uses "overparametrization" (4 hits). The genuine and narrower overreach on that page is that the
  theorem is about **smooth interpolation**, meaning a bounded Lipschitz constant, and not about
  resistance to an adversary. Gilmer et al. likewise do write "We hypothesize that this
  counterintuitive behavior is a result of the high-dimensional geometry of the data manifold"; the
  wiki's version altered it rather than inventing it. Real fabrications remain in the set — see the
  inverted quote below. Corrected passages are marked in place rather than deleted, so
  the error is not silently repeated. **A full quote-verification pass over the remaining unaudited
  pages is still owed**; until it is done, no quotation from a page lacking `claim_quantifier` may be
  carried into the survey. Method to reuse: `pdftotext` every PDF, strip all non-alphanumerics from
  both needle and haystack, match 45-character windows.
- **Never invent citations** — only reference claims that appear in a source you have read.
- **Contradiction handling**: when a new source contradicts an existing claim, update the relevant page to note both positions and cite both sources. Do not silently overwrite.
- **Verify novelty before endorsing it.** Any "nobody has done X" gets an adversarial web check — search *for* prior art, not for confirmation — before it goes in writing.
- **Record negative results.** "This is occupied" is as valuable as a positive finding; unwritten, it gets re-walked.
- **Every source page records its claim's quantifier and antecedent.** Front matter carries
  `claim_quantifier: existential | universal | conditional | empirical` and `antecedent: <the hypothesis
  the main claim rests on, or "none">`, and the body carries a `## Claim Boundary` section immediately
  after `## Summary` with four fields: what the claim is quantified over, the antecedent and whether it
  is known to hold, what the result does **not** establish, and any place the abstract states more than
  the theorem supports. This exists because the wiki's documented failure mode is restating an
  existential result about a constructed object as a universal claim about deployed systems, and
  dropping the antecedent of a conditional theorem. Adversary-facing pages should also carry
  `adversary_bound`, and learning-theory pages `model_class` and `algorithm_class`.
- **No process language in wiki prose.** A page must not refer to how it was written: no "this batch",
  no "the brief", no "the sweep found", no first person. A future reader has none of that context, and
  the phrase silently becomes false as the wiki grows. Name the corpus instead of the work order.
- **A counter-result is a limit, not a sibling.** When a newer source measures a theorem's hypothesis
  and finds it does not hold, or reaches the opposite conclusion, it goes in a `## Limits` section on
  the theorem's own page, not in `Connections` alongside same-direction work. Filing a refutation as a
  neighbour is how overreach propagates.
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

- `exp/docs/notes/chapter-24.md` is 309KB — exceeds the Read tool's 256KB limit. Chunk with offset/limit or delegate to a subagent.
- `wiki/index.md` and `wiki/overview.md` are frozen at 2026-04-23 and materially wrong (index claims 16 sources; there are 75; 26 concept pages unlinked; neither mentions the user's own theory). **Do not orient from them.**
- `raw/*.pdf` is gitignored. Catalog is `raw/SOURCES.md`; naming is `[INITIALS][YY]_Topic.pdf`.
- `pdftotext <file>.pdf -` extracts the raw PDFs.
- **A quote checker that strips punctuation is still not spelling-proof.** The 2026-08-20 pass
  matched 45-character windows with all non-alphanumerics removed, which defeats hyphenation and
  glyph loss but *not* spelling variants. "overparameterization" against the paper's
  "overparametrization" produced a false accusation of fabrication against a correct page. Before
  reporting any quote as absent, search for a distinctive *short* fragment that avoids the words
  most likely to vary: -ize/-ise, -metriz/-meteriz, British against American forms, and hyphenated
  compounds. A false fabrication charge is more damaging than a missed one.
- **Always `grep -a` when searching extracted PDF text.** Many extractions contain a stray byte that
  makes `file` report `data`; BSD grep then treats the input as binary and **prints nothing at all** —
  not "Binary file matches", not `0`. Every pattern appears absent, including ones that are certainly
  present. Without `-a` this silently turns "I could not verify the quote" into "the quote is not in
  the paper", which is how a correct source gets accused of fabrication. Sanity-check any negative
  result by grepping for a string you know is in the document.

---

## Session Start Checklist

At the start of each session:
1. Read this file (`CLAUDE.md`).
2. Read the last ~5 entries of `wiki/log.md`.
3. Orient from `exp/` (start at `exp/docs/CONTEXT.md`), not from `wiki/index.md` — the programme is the active work.
4. Ask what the user wants. Do not assume it is an ingest.
