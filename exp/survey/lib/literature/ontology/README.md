# Ontology of the literature

How each work treats the setting: how it models training, what it grants the
adversary, which attacker class, what it charges, what utility condition, what
it assumes, what form its result takes and how it phrases it. Plus the author's
decision on each candidate work.

| File | Holds | Edited |
| --- | --- | --- |
| `onto.tsv` | every fact, one per line: subject, predicate, object, note, checked | generated, read this one |
| `views.md` | counts and tables over `onto.tsv` | generated |
| `papers.tsv` | the candidate works, their claim, how it is realized, the author's decision | by hand |
| `hand.tsv` | facts entered by hand, no header | by hand |
| `aliases.tsv` | other ids for one work, mapped to the id used in `onto.tsv` | by hand |
| `schema.tsv` | every allowed value, its type and meaning | by hand |
| `schema.md` | the predicates and the `checked` column | by hand |

The agents' coded facts are a job output, in `lab/results/literature-ontology/`,
with the brief in `lab/src/briefs/ontology-brief.md`. Rebuild after any change:

```bash
python3 lab/src/merge-onto.py --write
```

## papers.tsv

`group` says what the secret is and who holds it.

- `tamperer-key`: the party that shapes the model holds a key that gives it control.
- `defender-converse`: detecting, removing or mitigating what a tamperer planted.
- `owner-key`: the roles swapped, the owner holds the key (watermarks, ownership).
- `prove-training`: a prover convinces a verifier that learning was done honestly.
- `program`: results the author's own programme builds on directly.
- `data-secret`, `weights-secret`, `robustness-gap`: no tampering. A separate
  part on tasks, filtered later.

`decision` is the author's: `core`, `consider`, `unclear`, `background-task`,
`drop`, with a suffix where the author gave a reason. In `onto.tsv` it carries
the prefix `decide-`.

`where` is `wiki:<slug>` for a work with a wiki page, `sweep:<lane>` for one seen
only in a sweep sheet under `lab/results/literature-sweep/`, and
`raw-pdf-unverified:` for a PDF in `raw/` whose title is not yet checked. A
`sweep:` row is not cited until the paper is opened.
