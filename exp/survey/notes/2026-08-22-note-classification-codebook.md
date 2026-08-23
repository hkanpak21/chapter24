# Classification codebook

The controlled vocabulary for the survey's two classification tables. Every cell in
those tables holds one value from the lists below and nothing else. A cell is never
free prose, because the point of the tables is that two readers assign the same
value.

**Revision 4, 2026-08-22.** Wave one of the fanout classified 66 works and reported
eleven vocabulary gaps, six of them in `family`. `family` gains `attribute`,
`distribution`, `invert`, `inject` and `multiple`; `unit` gains `circuit depth` and
`success prob`; `access` and `write` each gain `channel`.

**A judgement I reversed.** After wave one I wrote that `family` needed restructuring
rather than more values, on the grounds that it conflates the adversary's goal with
its act. That analysis is right, and the restructure is not worth it. Separating goal
from act would reclassify all 115 rows already done, and the flat taxonomy is the one
a reader of this literature recognises, so the cost falls on us and the benefit falls
nowhere. The observation is kept as a finding for the paper: **the standard attack
taxonomy does not cover this corpus**, because the corpus also holds attacks on a
cryptographic primitive, a communication channel, a training distribution, and an
agent's control flow. That is a result about the field, and it belongs in the prose
rather than in a fourth rebuild of the vocabulary.

**Revision 3, 2026-08-22.** The first delegated batch of 25 works produced seven
vocabulary gaps, every one flagged by a classifier rather than forced into a wrong
cell. Five of the seven are the same underlying problem: the vocabulary was built
for computational bounds, and a large part of this corpus is bounded in ways that
are not computational. `frame` gains `statistical`, for a bound that is purely
information-theoretic, which two classifiers hit independently on sample-complexity
results. `unit` gains `privacy budget`, without which the differential privacy
cluster has nowhere to go. `tightness` gains `quasi-poly` and `conditional`, the
first because `poly` is reserved for the binary quantifier and the second because
`exponent` presumes a second party. `family` gains `evade audit`. `write` gains
`responses`. And `second` splits into `second party` and `second notion`, because
one party bounded under two incomparable resource notions is not the same thing as
two bounded parties, and the distinction is the substance of at least one paper in
the corpus.

A note of mine was also wrong and is corrected here. Revision 2 said the `attacker`
by `memory` cell was expected to stay empty. The repository's standing claim is
narrower than that: it says no **machine learning or privacy** adversary is bounded
by memory. Bounded-storage cryptography bounds exactly that and is in this corpus on
purpose. The cell is populated, and the finding must always be stated with its
scope.

**Revision 2, 2026-08-22.** The first batch of 24 works exposed three defects, all
found by looking at which rows and columns came out empty. `perturbation` and
`corruption` were missing as units, which would have sent 22 works to a `none` cell
that means something else. `frame` was binary and could not tell a
non-computationally-bounded adversary from an unbounded one, so it now takes three
values. `communication` was considered and dropped, because no work in the corpus
uses it. `mechanism` and `samples` looked empty but are populated in the corpus, at
13 and 3 works, so those were sampling artifacts of the batch and not vocabulary
faults. `attacker` by `memory` remains empty and is expected to stay empty.

Written 2026-08-22, after Halil fixed the four table parameters: all 181 works with
an out-of-frame flag, two aligned tables sharing a row order, five adversary
columns, short controlled text in every cell.

**Provenance rule.** Every assigned value is one of three kinds, and the record
keeps them apart. `F` means read directly off wiki front matter. `S` means read
from the page's Summary or Claim Boundary prose. `P` means assigned by the person
doing the pass from the primary PDF. No value is ever assigned from a tag alone,
because tags were applied for retrieval and not for classification.

---

## Table 1. Attack scenario and threat model

| Column | Values | Notes |
| --- | --- | --- |
| `target` | `train data`, `parameters`, `outputs`, `training run`, `none` | What the adversary is trying to learn or affect. `none` for works with no adversary. |
| `family` | `membership`, `reconstruct`, `extract`, `evade`, `poison`, `backdoor`, `forge`, `none` | `forge` covers proof-of-learning spoofing and unlearning forgery. `evade audit` covers evading a detector, monitor, filter or verifier, which is a different act from evading a classifier. `none` for foundational and cryptographic works. |
| `phase` | `train time`, `test time`, `post hoc`, `n/a` | `post hoc` is an adversary acting on a released model with no further training. |
| `access` | `hard label`, `scores`, `black box`, `white box`, `weights`, `gradients`, `channel`, `none` | The strongest access the main claim grants. `hard label` returns the top class only, `scores` a confidence vector, `black box` query access whose form the work does not fix. |
| `write` | `read only`, `corpus`, `model`, `responses`, `channel`, `none` | What the adversary may modify **in the system's persistent state**. An adversary that only crafts its own input, as every evasion adversary does, changes nothing persistent and is `read only`. `corpus` writes into training data, `model` into parameters, `responses` alters an oracle's answers in transit, `channel` writes into a communication channel between components. `none` is reserved for works with no adversary at all, and must not be used merely because the work describes no query interface. |
| `frame` | `compute`, `statistical`, `capability`, `none` | `compute` when a computational resource bounds some party, meaning time, circuit size, memory, queries or an algorithm class. `statistical` when the only bound is an information-theoretic quantity, in practice sample complexity, and the work says nothing about computation. `capability` when a party is bounded in what it may do rather than in what it may spend, which in this corpus means a perturbation radius, a corruption fraction or a privacy budget. `none` when no party is bounded at all. |

## Table 2. Adversary assumptions and claim shape

| Column | Values | Notes |
| --- | --- | --- |
| `party` | `attacker`, `learner`, `auditor`, `mechanism`, `none` | Which party carries a resource bound. `none` is a legal and common value. |
| `unit` | `time`, `circuit size`, `queries`, `samples`, `memory`, `algo class`, `parameters`, `perturbation`, `corruption`, `rounds`, `privacy budget`, `circuit depth`, `success prob`, `none` | The unit the bound is stated in. `perturbation` is a norm-ball or metric radius on what the adversary may change. `corruption` is a fraction or count of training points it may control. `rounds` is a bound on adaptivity or on passes. `privacy budget` is the epsilon of a differential privacy guarantee, which bounds a mechanism's output distribution rather than any party's spending. |
| `tightness` | `unstated`, `poly`, `quasi-poly`, `class`, `budget`, `conditional`, `exponent`, `measured` | `poly` is the binary probabilistic-polynomial-time quantifier. `class` is membership of a restricted algorithm family. `budget` is an explicit numeric allowance that is a definitional parameter but carries no relation to the honest party, such as a query budget or a parameter count. `quasi-poly` is a stated quasi-polynomial running time, which `poly` cannot express because `poly` is reserved for the binary quantifier. `conditional` is a lower bound that holds under a named hardness assumption with no second party to compare against, such as a SETH-conditional bound. `exponent` is a stated relation to the honest party's work and therefore needs two parties. `measured` is an empirical number with no definitional status. Added 2026-08-22 during the first classification batch, where a query budget fitted none of the original five. |
| `baseline` | `stated`, `absent`, `n/a` | Whether the work says what an adversary achieves **from public knowledge alone**, so that an advantage over it is measurable. The test is: could a party with no access to the target succeed this often? A security game's one half, a fair-coin guess, an oblivious attack that ignores the model, or a blind predictor are all `stated`. A matching information-theoretic lower bound, an optimal-error term such as OPT, a previously published accuracy number, or the cost of an alternative algorithm are **not** baselines in this sense and do not make the field `stated`, because none of them is what public knowledge alone achieves against this target. `absent` where a success criterion exists but no such reference does. `n/a` where the work defines no adversary success criterion at all. |
| `second party` | any `unit` value, or `none` | Set when a second party is also bounded, naming that party's unit. Fine-grained cryptography and robust learning both bound two parties, and a single-valued `party` column would lose one of them. |
| `second notion` | any `unit` value, or `none` | Set when **one** party is bounded under two resource notions the work treats as incomparable. This is a different situation from two parties and was previously conflated with it. The refutation of the quasi-polynomial low-degree conjecture is exactly this case: one distinguisher, bounded both by degree and by running time, with the paper's whole point being that the two diverge. |
| `assessed` | `explicit`, `implicit` | Whether the work assesses the adversary's resources on purpose, or the quantity appears only as a side condition. Halil's axis. No prior systematization carries it. |
| `quantifier` | `universal`, `existential`, `conditional`, `empirical` | From front matter, present on all 181 pages. |
| `antecedent` | `none`, `stated`, `measured false` | `measured false` where a later work measured the hypothesis and found it does not hold. |

---

## Rules that decide the hard cases

1. **The main claim decides.** A paper with a theorem and an evaluation is classified
   on the theorem. Where a paper carries two claims of different shape, the row
   records the one the abstract leads with, and the second is noted in the text
   rather than given its own row.
2. **`none` is an answer.** A work that constrains nobody gets `party = none`,
   `unit = none`, `tightness = unstated`, and `frame = out`. The count of such rows
   is a result and not a gap in the pass.
3. **Out of frame is not out of scope.** An `out` row still carries its attack
   scenario and threat model, because the point of showing it is that the claim
   stands without any resource entering.
4. **The constrained party is whoever the bound binds**, not whoever the paper is
   about. A paper about attacks whose only bound is on the learner gets
   `party = learner`.
5. **When two parties are bounded, the computational bound decides the row.** Record
   that party in `party` and its unit in `unit`, and name the other party's unit in
   `second`. If both bounds are computational, or neither is, the adversary's bound
   decides. Example: a robust-learning result bounding the learner in polynomial time
   and the perturbation adversary by a radius is `party = learner`, `unit = time`,
   `second = perturbation`.

6. **A perturbation budget is a bound.** It is not a computational bound, and the
   distinction is carried by `frame` rather than by discarding it. A work whose only
   restriction is an norm-ball radius is `party = attacker`, `unit = perturbation`,
   `tightness = budget`, `frame = capability`. Recording those as `none` would erase
   the difference between a work that bounds the adversary non-computationally and
   one that bounds nothing, and 22 works in this corpus sit in that difference.

7. **`implicit` requires evidence.** Assign it only where the quantity appears in
   the work, as a side condition, a runtime, a query count or a cost, and the work
   does not treat it as a parameter. Where the quantity is simply absent, the row
   is `party = none` and `assessed` is left blank.

8. **Rule 2 and the `implicit` case do not conflict, and here is the boundary.**
   Rule 2 says `none` is an answer. It applies when the quantity is *absent*: the
   work never states what any party spends. The `implicit` case applies when a
   quantity *is present* in the work as a reported runtime, query count, sample
   count or cost, but the work does not treat it as a parameter. A paper that
   reports its attack took seventy GPU-hours has stated a cost, so it is
   `party = attacker`, `unit = time`, `tightness = measured`, `assessed = implicit`,
   not `party = none`. A paper that reports no cost at all is `party = none` and
   `assessed` is blank. The test is whether a number exists anywhere, not whether it
   is load-bearing.

9. **Classify what the work claims, not what it discusses.** A paper whose subject
   is a critique of differential privacy does not thereby bound a mechanism by a
   privacy budget. The bound must be one the work asserts, not one it examines.

---

## Applied in revision 4 (was pending)

Gaps reported by classifiers after revision 3 was frozen. Not yet applied, so that
a single revision covers them all rather than moving the vocabulary under agents
that are already running.

| Gap | Reported on | Proposed |
| --- | --- | --- |
| No `injection` family | `formalizing-llm-agent-security`. Prompt injection spans several existing families at once and is none of them. The corpus carries 13 works tagged for language-model security. | Add `inject` to `family` |
| No circuit **depth** unit | `gamarnik-circuit-lower-bounds-pspin`. The theorem's headline quantity is depth, and `circuit size` was used as the nearest available value. The distinction is real, since depth-bounded and size-bounded classes are not the same. | Add `circuit depth` to `unit` |

| No family for inverting a cryptographic primitive | `average-case-fine-grained-hardness`. A fine-grained one-way function's adversary inverts `f`, which is none of membership, reconstruct, extract, forge, evade, poison or backdoor. | Add `invert` to `family` |
| No unit for a success-probability bound | `average-case-parity-problems`. Its theorems additionally require near-perfect success, `1 - Theta(1/2^K)`, a second bound on the same party with no matching unit. The page's own Claim Boundary calls this the paper's most important limitation for a cryptographic reading. | Add `success prob` to `unit` |
| `access` and `write` do not fit a channel adversary | `authentication-bounded-storage`. A streaming man-in-the-middle on a communication channel is neither a query interface nor a write into a corpus or model. | Add `channel` to both `access` and `write` |
| No `distribution inference` family | `distribution-inference-risks`. The paper defines itself against every existing value: the goal is the training *distribution*, not the dataset. | Add `distribution` to `family` |

| No `prompt injection` family | `camel-defeating-prompt-injections`. Live control-flow hijacking during agent execution is not post-hoc detector evasion, so `evade audit` was considered and rejected. | Add `inject` to `family`, covering this and `formalizing-llm-agent-security` |
| No `attribute inference` family | `adversary-aware-dp-bounds`, whose main theorem is generic over membership, attribute inference and reconstruction at once. Picking any one would misrepresent it. | Add `attribute` to `family`, and consider a `multiple` value for unified frameworks |

**`family` is the weak dimension, and the pattern is now clear.** Six of the eleven
gaps found across 67 delegated works are in `family`. It was designed around attacks
on a deployed machine learning model, and the corpus also contains attacks on a
cryptographic primitive, on a communication channel, on a training distribution, on
an agent's control flow, and frameworks generic over several goals at once. Revision
4 should treat `family` as needing restructuring rather than another three values.
The other twelve fields have held.

Rate of gaps found: 7 in the first 25 works, then 6 more across the next 42. Falling
but not zero.

---

## A known interaction between rule 4 and `frame`, noticed 2026-08-22

Rule 4's tie-break says that when neither party's bound is computational, the
adversary's bound decides the row. In the robust-PAC literature that is the common
case: the learner is bounded in samples, which is statistical, and the evasion
adversary is bounded by a perturbation radius, which is a capability. The row
therefore comes out `party = attacker`, `unit = perturbation`,
`frame = capability`, and the learner's sample bound is preserved only in
`second party`.

The consequence is that `frame = statistical` will be **under-counted**. It appears
only where a statistical bound is the *sole* bound in the work, not wherever a
statistical bound exists. Any count of statistical bounds reported from the survey
must be taken over `unit` and `second party` together, not over `frame` alone. The
information is not lost, but the obvious query gives the wrong answer.

---

## Gaps found after revision 4 was frozen

Not applied. Recorded so the count of gaps per revision stays honest and so a
future revision can take them together.

| Gap | Reported on | Note |
| --- | --- | --- |
| No unit for **training runs** | `membership-inference-shokri`. Its only cost quantity is the number of shadow models, 10 to 100 per dataset, which is neither queries nor samples nor time. `queries` was used as an approximation and flagged. | This is a real unit for this survey. An attacker priced in training runs is exactly the proof-of-learning comparison. Worth adding. |
| `family` still cannot name a cryptographic goal | `merkle-puzzles-are-optimal`. Recovering a shared secret in key exchange is none of the fourteen values, and `invert` does not fit either. Forcing `extract` would collide with model extraction. | The `family` weakness again, now on its seventh instance. |
| Only one `second notion` slot | `multi-party-poisoning` bounds one attacker in three resources at once: polynomial time, a corruption count, and a total-variation budget. Two were recorded and the time bound was left in prose. | A third slot would be used rarely. The honest fix may be to allow a comma-separated list in `second notion`, at the cost of the cross-tab. |

One audit warning of mine was **stale**: the `melon-indirect-prompt-injection` page had
already self-corrected its fabricated theorem on 2026-08-20. The classifier
re-verified against the PDF anyway and confirmed zero occurrences of theorem, lemma
or proposition in the body. Warning agents about corrections that have already
landed costs them a PDF read, so the audit note should be checked against the page
before it goes into a brief.

---

## `baseline` needs a second pass over the whole corpus

A classifier reported that the `baseline` definition was too thin to apply
consistently, and it was right. Two readings were in use across the delegated
batches. The narrow one, which is what the survey means, asks what an adversary
achieves from public knowledge alone: a game's one half, a fair coin, an oblivious
attack. The broad one counts any explicit comparison quantity, including a matching
information-theoretic lower bound or a previously published number.

The definition is now tightened, with the exclusions written out. But rows
classified before the tightening may carry the broad reading, and `baseline` is one
of the columns the survey's contribution rests on, so the count cannot be reported
until they are checked.

**Scope of the re-pass.** 54 rows currently read `stated`. The suspicious subset is
those with no attack family, 21 of them, where a "baseline" is more likely to be a
matching bound than an adversary's trivial-success rate. Game-based cryptography in
that subset is probably correct, since a game's one half is a genuine baseline.
Learning-theory results in it probably are not. This is one field over at most 54
rows and is cheap to redo; it should be done in one pass at the end rather than
piecemeal.

---

## `assessed` needs a second pass, like `baseline`

17 rows carry a constrained party but leave `assessed` blank. Rule 5 says a blank
`assessed` goes with `party = none`, so these are inconsistent with the rule rather
than with each other. The likely cause is that classifiers read `assessed` as
applying only where a *second* bound exists, which is not what it means: it records
whether the work assesses the party's resources on purpose or leaves the quantity as
a side condition, and that question has an answer whenever a party is bounded at all.

Like `baseline`, this is one field over a bounded set of rows and should be redone in
one pass rather than patched. Both re-passes can run together.
