> Historical. Written for the 2026-10-13 coding run. Paths below are the
> layout of that day: `batches/` is now `ontology/coding/`, `batch-N.txt` is
> `input-N.txt` and `onto-N.tsv` is `coded-N.tsv`.

# Ontology coding brief

You code works into the survey's ontology. Read these first:

- `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/exp/survey/lib/literature/ontology/schema.md` (moved since)
- `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/exp/survey/lib/library/schema.tsv`
- `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/exp/survey/lib/library/threads/2026-10-13-ai-oracle-definition.md`

## Purpose

The author is building an idealized model of training, an "AI oracle", in
which leakage about training data can be bounded, with attackers classified by
the operations they may use (evaluate, gradients, weights, calls to training)
and by their computational power. The ontology records how each work treats
the setting: how it models training, what it grants the adversary, which
attacker class, what it charges, what utility condition keeps the notion
non-vacuous, what it assumes, what form its result takes, and how it phrases
the result. Of these, the most important is `treats-training-as`: what
property of the training procedure the work relies on to bound or measure
leakage, or `train-concrete-dnn` if it relies on none and measures.

## Input

Your batch file lists one work per line: `<id>\t<source>`.

- `wiki`: read `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/<id>.md`.
  Read the front matter, `## Summary`, `## Claim Boundary`, `## Key Contributions`
  and `## Key Definitions / Theorems`. The `cls_*` fields are an older coding;
  use them as hints only.
- `sweep:<file>`: read the sheet with `- key: <id>` in
  `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/exp/survey/lib/literature/sweeps/<file>`,
  or its row in the extra-rows table at the end of that file.

## Output

Write one file, `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/exp/survey/lib/library/batches/onto-<batch>.tsv`,
tab separated, no header, five columns: subject, predicate, object, note, checked.

- Subject is the id exactly as in your batch file.
- First line for each work: `<id> relevance core|peripheral|out`.
  Core: it bounds, measures or defines what an adversary learns about training
  data or a trained model as a function of its access or power, or it models
  training abstractly, or it is about undetectable control of a model
  (backdoors, watermarks, proofs of training or ownership), or it is an
  idealized oracle or obfuscation model. Peripheral: it shows how the field
  treats one of these settings or phrases such results, without bounding
  anything. Out: otherwise.
- An `out` work gets only `relevance` and `addresses`.
- A core or peripheral work gets every predicate its page supports:
  `treats-training-as`, `grants-access`, `quantifies-over`, `charges`,
  `conditions-on`, `uses-notion` or `defines`, `assumes`, `concludes`,
  `addresses`, `reports-in`, and paper-to-paper relations to other ids when the
  page names them. Use several triples for one predicate when the work has
  several settings, and say in the note which result each belongs to.
- `concludes` notes state the result in one line, at most 30 words, with its
  location (theorem, section) when the page gives one.
- Every object is a slug from `schema.tsv`. If none fits, write a new slug and
  add a line `<slug> is-a <type> <gloss> proposed`.
- `checked` is `wiki`, `sweep` or `inferred`. Use `inferred` whenever the page
  does not say it directly.
- No tab inside a field. No invented theorem numbers. If the page does not
  state a utility condition, write `util-none-stated`, never a guess.

## Constraints

- Local files only. No web access.
- Do not spawn sub-agents. Do not use the Agent or Workflow tools.
- Write only your one output file.

## Return

At most 150 words: counts of core, peripheral and out; every proposed slug;
and three observations about how the works in your batch treat training,
access and utility.
