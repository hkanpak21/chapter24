# Classification codebook

The controlled vocabulary for the survey's two classification tables. Every cell in
those tables holds one value from the lists below and nothing else. A cell is never
free prose, because the point of the tables is that two readers assign the same
value.

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
| `access` | `black box`, `scores`, `white box`, `weights`, `gradients`, `none` | The strongest access the main claim grants. `scores` means confidence vectors without parameters. |
| `write` | `read only`, `corpus`, `model`, `none` | Whether the adversary may write, and to what. |
| `frame` | `in`, `out` | `out` when deleting every resource restriction leaves the main claim unchanged. This is the scope test, applied per work rather than per paper. |

## Table 2. Adversary assumptions and claim shape

| Column | Values | Notes |
| --- | --- | --- |
| `party` | `attacker`, `learner`, `auditor`, `mechanism`, `none` | Which party carries a resource bound. `none` is a legal and common value. |
| `unit` | `time`, `circuit size`, `queries`, `samples`, `memory`, `algo class`, `parameters`, `none` | The unit the bound is stated in. |
| `tightness` | `unstated`, `poly`, `class`, `budget`, `exponent`, `measured` | `poly` is the binary probabilistic-polynomial-time quantifier. `class` is membership of a restricted algorithm family. `budget` is an explicit numeric allowance that is a definitional parameter but carries no relation to the honest party, such as a query budget or a parameter count. `exponent` is a stated relation to the honest party's work. `measured` is an empirical number with no definitional status. Added 2026-08-22 during the first classification batch, where a query budget fitted none of the original five. |
| `baseline` | `stated`, `absent`, `n/a` | Whether the work says what success means against public knowledge alone. `n/a` where no success criterion exists. |
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
5. **`implicit` requires evidence.** Assign it only where the quantity appears in
   the work, as a side condition, a runtime, a query count or a cost, and the work
   does not treat it as a parameter. Where the quantity is simply absent, the row
   is `party = none` and `assessed` is left blank.
