# Classification codebook

The controlled vocabulary for the survey's two classification tables. Every cell in
those tables holds one value from the lists below and nothing else. A cell is never
free prose, because the point of the tables is that two readers assign the same
value.

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
| `family` | `membership`, `reconstruct`, `extract`, `evade`, `poison`, `backdoor`, `forge`, `none` | `forge` covers proof-of-learning spoofing and unlearning forgery. `none` for foundational and cryptographic works. |
| `phase` | `train time`, `test time`, `post hoc`, `n/a` | `post hoc` is an adversary acting on a released model with no further training. |
| `access` | `hard label`, `scores`, `black box`, `white box`, `weights`, `gradients`, `none` | The strongest access the main claim grants. `hard label` returns the top class only, `scores` a confidence vector, `black box` query access whose form the work does not fix. |
| `write` | `read only`, `corpus`, `model`, `none` | Whether the adversary may write, and to what. |
| `frame` | `compute`, `capability`, `none` | `compute` when a computational resource bounds some party. `capability` when a party is bounded but not computationally, which in this corpus means a perturbation budget or a corruption fraction. `none` when no party is bounded at all. |

## Table 2. Adversary assumptions and claim shape

| Column | Values | Notes |
| --- | --- | --- |
| `party` | `attacker`, `learner`, `auditor`, `mechanism`, `none` | Which party carries a resource bound. `none` is a legal and common value. |
| `unit` | `time`, `circuit size`, `queries`, `samples`, `memory`, `algo class`, `parameters`, `perturbation`, `corruption`, `rounds`, `none` | The unit the bound is stated in. `perturbation` is a norm-ball or metric radius on what the adversary may change. `corruption` is a fraction or count of training points it may control. `rounds` is a bound on adaptivity or on passes. |
| `tightness` | `unstated`, `poly`, `class`, `budget`, `exponent`, `measured` | `poly` is the binary probabilistic-polynomial-time quantifier. `class` is membership of a restricted algorithm family. `budget` is an explicit numeric allowance that is a definitional parameter but carries no relation to the honest party, such as a query budget or a parameter count. `exponent` is a stated relation to the honest party's work. `measured` is an empirical number with no definitional status. Added 2026-08-22 during the first classification batch, where a query budget fitted none of the original five. |
| `baseline` | `stated`, `absent`, `n/a` | Whether the work says what success means against public knowledge alone. `n/a` where no success criterion exists. |
| `second` | any `unit` value, or `none` | Set when a second party is also bounded, naming that party's unit. Fine-grained cryptography and robust learning both bound two parties, and a single-valued `party` column would lose one of them. |
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
