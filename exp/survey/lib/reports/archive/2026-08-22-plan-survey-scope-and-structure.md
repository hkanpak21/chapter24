# Survey plan — what it is, what is in it, how it is built

Current as of 2026-08-20, after the session that settled the framing, the audience and the structure.

This file holds the **reasoning**: what the survey argues, where its boundary is, and why it is shaped
the way it is. The **work** lives in [[2026-08-22-plan-survey-tasks]] — tasks, progress, and the wiki pages that carry each
section. The two are meant to be read together and not to repeat each other.

---

## 1. What the survey is about

There is a substantial body of work on the security and privacy of machine learning that contains real
theorems. It does not behave like one field. Results on the same attack contradict each other, two
subfields have independently invented the same object without contact, and defences are broken while
staying inside the threat model they declared.

The cause is not that researchers **disagree** about what an adversary is. Disagreement would be
healthier, since it would mean positions exist and could be compared. The cause is that there is **no
standardized formal adversary at all**. Most papers never specify one. There is nothing to disagree
about.

This is a claim the survey has to earn rather than assert, and it can be earned four ways, in
increasing strength:

1. The same attack yields verdicts from "works well" to "cannot be validated at all", and the spread
   tracks what was assumed about the adversary rather than anything about the attack.
2. Two subfields invented the same quantity — attacker cost measured against honest cost — and neither
   cites the other, because neither has a name for the shared object.
3. Defences are broken *inside their own stated threat models*, which means the threat model was not
   constraining enough to carry meaning.
4. The field says it about itself. A 2024 systematization reports "a lack of study and formalization
   of adversary knowledge", yielding "hard-to-compare threat models and attacks".

The turn that earns the rest of the paper for a machine-learning reader is this: **the adversary in
these settings is running an inference task**, and complexity theory is the discipline that prices
tasks. That is why it is the right thing to import, and why the units already exist.

### Title and framing

The subject is the **characterization** of adversary capability in complexity-theoretic terms. It is
not the imposition of bounds, and it is emphatically not efficiency of training or inference. Working
title: *How Hard Is the Attack? A Complexity-Theoretic Survey of Machine Learning Security*.

The word "efficiency" must stay out of the title and abstract. To almost every reader it means
quantization and FLOP-optimal scaling, which is a different field. "Polynomial versus exponential" is
what is meant, and "complexity" is the word that says it.

### Audience

Machine-learning researchers. Every complexity-theoretic idea is introduced before it is used. The
paper carries complexity theory *into* machine-learning security; it does not assume the reader
arrives with it.

### Stance

Document first, then formalize. The landscape is reported without argument. The formalization then
**converges** out of what was reported, and it is a contribution of this work rather than a lens
assumed at the start. These are sequential, not contradictory.

---

## 2. Scope

A paper is **in** if all three hold.

1. **It is about learning, or about something a learning process produced** — a model, its training
   data, its parameters, its outputs, its gradients.
2. **It makes a formal claim** — a theorem, a definition, or a measurement designed to be comparable
   across papers. "We built an attack and it worked 80% of the time" is not one.
3. **Somebody's resources matter to the claim.** The sharp version: *if you deleted every resource
   restriction and the main claim still stood unchanged, the paper is out.*

### The deliberate exception

Cryptography with no machine-learning content is included **when it is the formal home of a quantity
that machine learning measures without defining**. Fine-grained cryptography is the main case: it has
no ML content whatsoever, and it is the only place where "how much work does the adversary do relative
to the honest party" is a defined object. Excluding it would remove the one place the survey's central
observation can be stated precisely. The bounded-storage literature is included on the same grounds,
as the formal home of "adversary bounded by memory".

These enter as *destinations*: here is the quantity, here is where it has a definition, here is the
fact that nothing in machine learning has travelled there.

### What is out, and why

| Excluded | Reason |
| --- | --- |
| Empirical attack and defence papers | Fail test 2. No formal claim. |
| Norm-ball certified defences | Fail test 3. The certified radius constrains the perturbation, not a party. Kept only as a contrast case showing what a security claim looks like when nobody's resources enter. |
| Agentic and LLM-systems security | Almost all fails test 2. The few theorem-bearing papers are kept. |
| Alignment and RLHF impossibility results | Mostly fail test 3. Kept where a resource bound does real work, which in practice means the filtering-impossibility line. |
| Work using "fine-grained" to mean per-user access control | A name collision. Worth stating once, because it makes keyword search useless here. |

### Borderline cases, ruled rather than hidden

- **Robust PAC learning.** The adversary is a perturbation set, not a computation, so it fails test 3
  on the adversary side. But sample complexity is a resource and it is the learner's. **In**, filed
  where the constrained party is the learner.
- **Concentration of measure.** No resources anywhere; the results are geometric. **In**, because it
  is the baseline every computational result defines itself against, and because its
  measured-and-failed hypothesis is the clearest worked example the survey has.
- **Differential privacy generally.** Only the computational branch is **in** — computational DP,
  capacity-bounded DP, and auditing work where a resource bound appears. Plain DP is background.

---

## 3. The framework

The formalization the survey converges to. It is assembled from objects the programme already uses —
the criterion `R`, the capability vector `κ`, and the chain from source to output — rather than
imported from elsewhere.

Every claim in scope is a statement about one experiment:

```
              Π  ──→  D  ──→  w  ──→  M_w  ──→  M_w(x)
             source  data   weights  model     outputs
                      └──────── the adversary observes here ────────┘

   Exp[ Π, L, A, R, κ ]   →   Pr[ A wins ]   against   baseline
```

Compressed to one sentence: **the access point fixes a channel, `R` fixes what must be extracted from
it and to what tolerance, and `κ` prices the extraction.** The baseline is what makes "hard"
measurable rather than rhetorical.

| Coordinate | Fixes | Gives |
| --- | --- | --- |
| Access point | where the adversary observes on the chain | training versus test time; white versus black box; the three maps |
| `R` | what must be produced, and the tolerance | the success criterion; utility and privacy objectives both attach here |
| `κ` | a budget **per party**, not per adversary | who is constrained, in what unit |
| baseline | what public knowledge alone achieves | whether advantage means anything |

The load-bearing choice is `κ` being **per party**. That one decision absorbs cases the literature
keeps apart: ordinary attacker-bounded results set only `κ_A`; the overparameterization result sets
`κ_L` in parameters; the filtering impossibility sets `κ_auditor` relative to `κ_M`; the memory results
set `κ_L` in bits; fine-grained cryptography states a relation, `κ_A ≥ κ_L^{1+δ}`; the learning
exponents set `κ_A` in samples against an algorithm class.

**`κ` takes the value "unstated".** When a paper does not state a party's budget, that is recorded as a
value rather than treated as a failure of whoever is doing the mapping. The count of "unstated" cells
is a result of the survey, and it is what makes the mapping reproducible enough for a reader to drop
their own paper into.

### The frame has an outside, deliberately

It covers claims of the form *what can this party achieve against this channel under this budget*. It
does **not** naturally hold pure expressivity results, accuracy-versus-robustness tradeoffs as
properties of a task, or geometric inevitability results.

This boundary is content, not a defect. Those results conclude **inevitability precisely because no
resource enters them**. A frame that swallows everything asserts nothing, which is the failure mode a
general framework has to be defended against.

---

## 4. Structure

Six parts. Task-level detail and the wiki pages behind each are in [[2026-08-22-plan-survey-tasks]].

| Part | Length | What it does |
| --- | --- | --- |
| I — The problem | ≈4 pp | Three concrete exhibits of the disorder, then the diagnosis as *absence*, motivated by the four arguments in §1, then the complexity-theoretic turn. |
| II — Background for an ML reader | ≈6 pp | Only the machinery Part III uses: security games and the baseline, adversary classes, flavours of hardness, reductions, advantage. Unembarrassed about being pedagogical. |
| III — The landscape | ≈20 pp | Six subsections, ordered by which party is constrained and in what resource. Frame vocabulary used informally; not yet formalized. Needs one running example carried throughout. |
| IV — The formalization | ≈5 pp | §3 above, stated precisely, having been earned. Including what the frame does not hold. |
| V — The mapping | ≈8 pp | The field placed in the frame, as tables. Generated from wiki front matter, never hand-written. |
| VI — What the mapping shows | ≈5 pp | Empty cells with the method that established emptiness; the count of "unstated"; the near-misses; the field's considered rejection, reported neutrally. |

Part III is 40% of the paper and is where it either works or becomes a list. Part V is the part that
rots if hand-built, which is why the front-matter fields exist.

---

## 5. Open questions

1. Which running example carries through all six subsections of Part III.
2. Whether to fill the gradient-inversion and split-learning gap. Zero source pages, it is the
   programme's own running example throughout, and the frame places it cleanly — channel is `w` or
   intermediate activations at training time. Conspicuous by absence.
3. Whether Part V's cells are decidable enough that two readers agree. Test on a sample before
   committing to the table format.
