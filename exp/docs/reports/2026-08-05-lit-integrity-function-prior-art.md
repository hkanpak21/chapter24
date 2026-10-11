---
id: integrity-function-prior-art
date: 2026-08-05
tag: lit
status: draft
supersedes: null
corrects: 2026-08-05-unfiled-leakage-and-integrity-functions.md
commit: null
cluster: n/a
jobs: []
pi_reviewed: false
---

# `R` is a named subfamily from 2012, and a definition built on a quantified relation was once proved eliminable

## Scope

[[2026-08-05-unfiled-leakage-and-integrity-functions]] proposes `Φ` as one function reading as leakage or
as a detection floor, and treats the criterion `R` and the privacy-integrity unification as this
programme's. Two sweeps checked both claims across cryptography, quantitative information flow,
language-based security and machine learning privacy. Twenty-eight primary sources were retrieved and
text-extracted.

## Result

**`R` is not ours, the unification is not ours, and one prior result threatens the framing outright. The
adversary axis survives, and it is the only thing that does.**

### The three collisions

| Claim | Owner | Exact form |
| --- | --- | --- |
| A parameterized exact-by-type success relation | **Alvim, Chatzikokolakis, Palamidessi, Smith, IEEE CSF 2012**, Definition 3.6 | `R` with a `{0,1}` codomain is a **binary gain function**, a named subfamily with a structure theorem. Their worked cases are ours: exact match, tolerance balls, `k`-tries, partitions. Their footnote 3 states the codomain choice is immaterial |
| The same relation in machine-learning privacy | **Balle, Cherubin, Hayes, IEEE S&P 2022**, Definition 2 | `P[ℓ(Z, R(θ)) ≤ η] ≤ γ`, with `η` in exactly the position this programme places it, and the baseline separated explicitly as `κ(η) = sup_{z₀} P[ℓ(Z,z₀) ≤ η]` |
| Unifying confidentiality and integrity | **Clarkson and Schneider, IEEE CSF 2010** | Contamination is the Biba dual of leakage. Reference against candidate is theirs: program suppression `PS₁ ≜ I(t_spec \| t_impl)` |

### The threat to the framing

**Bellare and Sahai, CRYPTO 1999, eliminated the relation.** Non-malleability was originally stated by
quantifying over poly-time success relations `R`, and their characterization then dispenses with the
relation entirely, reducing to indistinguishability under parallel chosen-ciphertext attack with the
number of parallel queries one less than the arity of `R`.

| | |
| --- | --- |
| The threat | A security definition built on a quantified success relation was proved redundant. A reviewer who knows this will raise it, and the framing dies if `R` is similarly collapsible |
| The candidate answer, **a conjecture** | Their elimination trades the relation against *parallel queries*, available because the adversary is otherwise unconstrained. This programme fixes `R` and varies the adversary's budget, so no such trade exists |

### The one precedent on the axis that survives

**Chaudhuri, Imola, Machanavajjhala, NeurIPS 2019**, capacity-bounded differential privacy, Definition
3: a mechanism is `(H,Γ)`-capacity bounded private when the adversary lies in a restricted function
class `H`, with linear functions, reproducing-kernel Hilbert spaces and two-layer ReLU networks named,
and nothing in the quantitative information flow or maximal leakage lineages cites it. Everything else
is unbounded:

| Framework | Adversary |
| --- | --- |
| Quantitative information flow, g-leakage | handed the prior and the channel, computes the maximum exactly |
| Maximal leakage, α-leakage, local differential privacy as a leakage bound | supremum over all target functions of the secret |
| Reconstruction robustness | any reconstruction attack; the optimal one is stated to be maximum a posteriori |
| Fisher information leakage | unbiased estimators only, a statistical restriction the authors flag as breakable |
| Leakage-resilient cryptography | the class restricts the **side-channel map**, not the adversary. Different axis; not a precedent |

**The pattern is worth stating to the PI:** every leakage measure that takes a supremum over the target
function is engineered to be agnostic to what the adversary wants, whereas this programme fixes what the
adversary wants and prices what it can spend.

### What survives, ranked

| Rank | Claim | Strength |
| --- | --- | --- |
| 1 | **The adversary axis.** Fixing the criterion and bounding the adversary is the un-supremized, un-idealized corner nobody occupies | strong; verified across both sweeps |
| 2 | **The direction of quantization.** Quantitative information flow relaxes `{0,1}` to `[0,1]` and takes an *expectation*, smearing the bit. This programme thresholds and keeps the parameter exposed. `E[g]` and `Pr[ρ ≤ η]` are different functionals | real but small |
| 3 | Adopting their vocabulary inherits fourteen years of machinery rather than rebuilding it | tactical |

Does not show: that the framing survives the elimination argument. That is the open question, not a
detail.

## How it was produced

| | |
| --- | --- |
| Method | Two sweeps, thirty-four searches, twenty-eight primary sources retrieved and text-extracted |
| Verified verbatim | Alvim et al. Definitions 3.1 to 3.6; Balle et al. Definition 2; Clarkson and Schneider measures and Proposition 1; Bellare and Sahai Definitions 3.1 and 3.2 and the elimination passage; GKVZ Definitions 4.1, 4.2, 4.6, 4.7; Chaudhuri et al. Definition 3; Akavia et al. Definitions 2 and 3 |
| Not verified | Bellare and Namprempre's own numbering for INT-CTXT and INT-PTXT; Bellare and Kohno's `Φ`-class details; the GLMMR TCC 2004 definition; a canonical source for the certified-robustness predicate |
| Artifacts | This report |

### Two further warnings

**The matched pair is known to be asymmetric.** Clarkson and Schneider report that contamination
dualizes leakage but that **suppression has no confidentiality dual**. A symmetric leakage-integrity
pair must say what happens to suppression-like phenomena. Their footnote 5 is simultaneously the best
positioning sentence available: information-theoretic quantification ignores computational constraints
on attackers, so cryptographic primitives cannot be adequately characterized by it.

**No impossibility theorem is inherited.** Every parameterized integrity notion in cryptography
restricts the adversary's *move class* and is forced to by an impossibility result: Bellare and Kohno's
`Φ` by Propositions 4.1 to 4.3, non-malleable codes' tampering family `F` by algorithmic tamper-proof
impossibility. This programme's parameter sits at the *threshold*, where nobody has put one, so
non-vacuity at the chosen parameter must be established rather than inherited.

**The closest complete object already exists for one attack.** GKVZ FOCS 2022 Definition 4.2 carries two
thresholds, `γ` on the input perturbation and `β` quantizing a real-valued output into a bit, and
Definition 4.7 places the win condition inside a real-versus-ideal difference against a polynomial-time
adversary. Their Remark 4.8 argues why the absolute form is unsatisfiable and the comparative form
necessary, which is the argument this programme needs for subtracting a baseline.

## What this changes

Three claims are withdrawn: that the criterion is new, that the unification is new, and that the
programme's contribution is definitional. What remains is the adversary axis, which both sweeps confirm
is unoccupied, and which is now the only defensible contribution. The name **leakage function must not
be used**, because it is occupied three times over, by searchable-encryption leakage profiles, by the
uncertainty measure in quantitative information flow, and in machine learning by train-test
contamination, where a machine-learning audience will misread it immediately.

## Where it applies

| Section | Change |
| --- | --- |
| [[2026-08-05-unfiled-leakage-and-integrity-functions]] | Withdraw the unification claim and the novelty of `R`; restate the contribution as the bounded reading alone |
| Survey, definitions | Present `R` as a binary gain function, citing Alvim et al. Definition 3.6, or as reconstruction robustness, citing Balle et al. Definition 2. Put the contribution on the adversary |
| Survey, naming | Do not write "leakage function". Choose a name that does not collide three ways |
| Survey, threats to validity | **Answer Bellare and Sahai.** Argue why fixing `R` and varying the adversary's budget leaves no relation-against-parallel-queries trade to make |
| Survey, related work | Record that the cryptographic and language-based security literatures are mutually blind here, and that capacity-bounded differential privacy is uncited by the leakage lineages |
| Open problems | Establish non-vacuity at the threshold parameter; answer the suppression asymmetry |
| Corpus | Ingest Alvim et al. CSF 2012; Balle et al. S&P 2022; Clarkson and Schneider CSF 2010 and JCS 2010; Bellare and Sahai CRYPTO 1999; Chaudhuri et al. NeurIPS 2019 |
