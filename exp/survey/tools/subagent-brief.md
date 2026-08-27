# Classification brief

The prompt each classification subagent receives. `{{SLUGS}}` is replaced with that
agent's assigned wiki slugs. Nothing else varies between agents.

---

You are classifying works for a survey on the computational security of machine
learning. You are one of several agents doing this against a shared codebook. Two
agents reading the same paper must produce the same row, so follow the vocabulary
exactly and never invent a value.

## Your assignment

Classify these works: **{{SLUGS}}**

## Read in this order, and stop as soon as you can answer

1. **`/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/<slug>.md`.** This
   is your primary source and it is good. Each page went through a verification pass
   in which its claims and quotations were checked against the primary PDF. Read the
   front matter, the `## Summary`, and the `## Claim Boundary` section, which was
   written to answer exactly the questions you are being asked. Most fields you need
   are decidable from this page alone.
2. **The primary PDF**, only where the page is silent or hedged on a field you must
   fill. The catalogue mapping papers to files is `raw/SOURCES.md`. Extract with
   `pdftotext <file>.pdf -`.

Three warnings about the corpus, each of which has already caused a wrong result.

- **Always use `grep -a`.** Many extractions contain a stray byte that makes BSD grep
  treat the file as binary, whereupon it prints *nothing at all* rather than an
  error. Without `-a` every pattern looks absent. Sanity-check any negative by
  grepping for a string you know is present.
- **Around 5% of the wiki's quotations were wrong and are marked in place.** Never
  rely on a passage carrying a `_Not verbatim_` or `_Not a quotation from the paper_`
  banner.
- **Never classify from tags.** Tags were applied for retrieval, not classification.
  A value assigned from a tag is a guess wearing a uniform.

## The thirteen fields

Every cell holds exactly one value from these lists. No free prose. No new values.

**Attack scenario and threat model**

| Field | Allowed values |
| --- | --- |
| `target` | `train data`, `parameters`, `outputs`, `training run`, `none` |
| `family` | `membership`, `attribute`, `reconstruct`, `distribution`, `extract`, `invert`, `forge`, `evade`, `evade audit`, `inject`, `poison`, `backdoor`, `multiple`, `none` |
| `phase` | `train time`, `test time`, `post hoc`, `n/a` |
| `access` | `hard label`, `scores`, `black box`, `white box`, `weights`, `gradients`, `channel`, `none` |
| `write` | `read only`, `corpus`, `model`, `responses`, `channel`, `none` |
| `frame` | `compute`, `statistical`, `capability`, `none` |

**Adversary assumptions**

| Field | Allowed values |
| --- | --- |
| `party` | `attacker`, `learner`, `auditor`, `mechanism`, `none` |
| `unit` | `time`, `circuit size`, `queries`, `samples`, `memory`, `algo class`, `parameters`, `perturbation`, `corruption`, `rounds`, `privacy budget`, `circuit depth`, `success prob`, `flops`, `none` |
| `tightness` | `unstated`, `poly`, `quasi-poly`, `class`, `budget`, `conditional`, `exponent`, `measured` |
| `baseline` | `stated`, `absent`, `n/a` |
| `second party` | any `unit` value, or `none` |
| `second notion` | any `unit` value, or `none` |
| `assessed` | `explicit`, `implicit`, or blank |

`quantifier` and `antecedent` are already in the front matter. Do not re-derive them.

### What the values mean where it is not obvious

- `post hoc` is an adversary acting on a released model with no further training.
- `black box` is query access whose form the work does not fix. Use `hard label` or
  `scores` when the work does fix it.
- `frame = compute` means a computational resource bounds some party: time, circuit
  size, memory, queries or an algorithm class. `frame = statistical` means the only
  bound is information-theoretic, in practice sample complexity, and the work says
  nothing about computation. Do not call a sample-complexity bound computational.
  `frame = capability` means a party is bounded in what it may do rather than in
  what it may spend: a perturbation radius, a corruption fraction, or a privacy
  budget. `frame = none` means no party is bounded at all.
- `tightness = poly` is the binary probabilistic-polynomial-time quantifier.
  `class` is membership of a restricted algorithm family such as statistical
  queries or low-degree polynomials. `budget` is an explicit numeric allowance that
  is a definitional parameter but carries no relation to the honest party, such as a
  query budget, a parameter count or a perturbation radius. `exponent` is a stated
  relation to the honest party's work. `measured` is an empirical number with no
  definitional status.
- `assessed = implicit` requires evidence: the quantity appears in the work as a side
  condition, a runtime, a query count or a cost, and the work does not treat it as a
  parameter. Where the quantity is simply absent, leave `assessed` blank.

### Rules that decide the hard cases

1. **The main claim decides.** A paper with a theorem and an evaluation is classified
   on the theorem. Where a paper carries two claims of different shape, classify the
   one the abstract leads with and say so in your notes.
2. **`none` is an answer.** A work that constrains nobody gets `party = none`,
   `unit = none`, `tightness = unstated`, `frame = none`. This is common and correct.
3. **The constrained party is whoever the bound binds**, not whoever the paper is
   about. A paper about attacks whose only bound is on the learner is
   `party = learner`.
4. **When two parties are bounded, the computational bound decides the row.** Put
   that party in `party`, its unit in `unit`, and the other party's unit in
   `second party`. If both or neither are computational, the adversary's bound
   decides.

4b. **When one party is bounded under two incomparable resource notions**, record
   the second in `second notion`, not in `second party`. These are different
   situations. A single distinguisher bounded both by degree and by running time,
   where the work's point is that the two diverge, is one party and two notions.
5. **A perturbation budget is a bound.** A work whose only restriction is a norm-ball
   radius is `party = attacker`, `unit = perturbation`, `tightness = budget`,
   `frame = capability`. Do not record it as `none`.
6. **An impossibility result still has a party.** If the theorem quantifies over
   probabilistic-polynomial-time distinguishers, the constrained party is whoever
   that distinguisher models, usually `auditor`.

## Evidence, recorded per work

**Every row carries the sentence that decided it.** This is not optional and it is
not a summary. For each work, record a verbatim fragment from the source that
determines `party`, `unit` and `tightness`, because those three carry the survey's
argument and are the ones a later reader will challenge.

- Quote **verbatim**, at most 40 words, and never paraphrase inside quotation marks.
  Around 5% of this wiki's existing quotations turned out to be paraphrase presented
  as quotation, which is why this rule exists.
- **Verify the quote** if you took it from the primary PDF. Extract with `pdftotext`,
  then `grep -a` for a distinctive short fragment of it. Never use `grep` without
  `-a` here. If the fragment does not appear, you have misquoted; find the real
  sentence.
- Say where it came from in `cls_evidence_src`: a definition or theorem number, a
  section number, `abstract`, or `wiki Claim Boundary` when the wiki page is your
  source and the page itself carries no quotation.
- **If the bound is absent, that is the finding, and it still needs evidence.** Write
  `cls_evidence: absent` and use `cls_evidence_src` to record where you looked, for
  example `no bound in Def 2, Thm 1, or the threat model in §3`. A claim of absence
  backed by nothing is worth nothing.

Then one sentence in `cls_reason` for any field whose value would not be obvious to
a second reader. If every field was obvious, say so in three words.


7. **Rule 2 and the `implicit` case do not conflict, and here is the boundary.**
   Rule 2 says `none` is an answer. It applies when the quantity is *absent*: the
   work never states what any party spends. The `implicit` case applies when a
   quantity *is present* in the work as a reported runtime, query count, sample
   count or cost, but the work does not treat it as a parameter. A paper that
   reports its attack took seventy GPU-hours has stated a cost, so it is
   `party = attacker`, `unit = time`, `tightness = measured`, `assessed = implicit`,
   not `party = none`. A paper that reports no cost at all is `party = none` and
   `assessed` is blank. The test is whether a number exists anywhere, not whether it
   is load-bearing.

8. **Classify what the work claims, not what it discusses.** A paper whose subject
   is a critique of differential privacy does not thereby bound a mechanism by a
   privacy budget. The bound must be one the work asserts, not one it examines.

## Provenance, recorded per work

Every work gets one provenance letter, recording the strongest source you used.

- `F` every field came from front matter and the Claim Boundary section.
- `S` you needed the page's Summary prose.
- `P` you opened the primary PDF.

## When you cannot decide

Leave the field **blank** and say why in your notes. A blank is a request for a
second reader and costs the survey nothing. A guess is invisible and corrupts a
count that the paper will report. Do not guess. Also flag, in your notes, any work
whose correct value is not in the vocabulary, quoting what the work actually says.
The vocabulary has already been revised once for exactly this reason.

## Write your result back to the wiki

For each assigned slug, add these keys to the **end of the existing YAML front
matter** of `wiki/sources/<slug>.md`:

```yaml
cls_target: <value>
cls_family: <value>
cls_phase: <value>
cls_access: <value>
cls_write: <value>
cls_frame: <value>
cls_party: <value>
cls_unit: <value>
cls_tightness: <value>
cls_baseline: <value>
cls_second_party: <value>
cls_second_notion: <value>
cls_assessed: <value>
cls_evidence: "<verbatim fragment, at most 40 words, or: absent>"
cls_evidence_src: <Def 3 | Thm 1 | §4.2 | abstract | wiki Claim Boundary | where you looked>
cls_reason: "<one sentence for any non-obvious field, or: all fields direct>"
cls_prov: <F|S|P>
cls_date: 2026-08-22
```

Quote with double quotes and escape any double quote inside the fragment as `\"`.

**Never modify an existing front-matter key. Never touch the body of the page.**
Blank values are written as empty (`cls_assessed:`). If a page already carries
`cls_` keys, stop and report it rather than overwriting.

## Return this, and nothing else

A tab-separated block, one line per assigned work, with this header:

```
slug	target	family	phase	access	write	frame	party	unit	tightness	baseline	second_party	second_notion	assessed	prov	evidence_src
```

Keep `evidence` and `reason` out of the TSV, since they contain tabs and commas.
They go in the wiki front matter and in your notes.

Then, under a line reading `NOTES`, one short paragraph per work that needed a
judgement call, naming the field, the value chosen, and the sentence in the source
that decided it. Include every blank you left and every vocabulary gap you hit.

Be terse. Do not summarize the papers. Do not explain the codebook back.
