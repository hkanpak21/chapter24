---
title: "Overparameterization from Computational Constraints"
type: source
date_ingested: 2026-08-20
authors: [Sanjam Garg, Somesh Jha, Saeed Mahloujifar, Mohammad Mahmoody, Mingyuan Wang]
venue: "NeurIPS 2022"
venue_evidence: "https://proceedings.neurips.cc/paper_files/paper/2022/hash/57e48ac3aa4d107979bf5c6ebc9fe99d-Abstract-Conference.html (Advances in Neural Information Processing Systems 35, 2022)"
year: 2022
claim_quantifier: existential
antecedent: "One-way functions exist. Used twice — via HILL'99 for pseudorandom generators of arbitrary polynomial stretch (Part 1), and via Naor–Yung'89 / Rompel'90 for signature schemes with weak unforgeability (Part 2). No stronger or structured assumption anywhere. Part 2's lower bound (Theorem 29) is itself an entropy argument and needs no assumption."
adversary_bound: "Both regimes appear, deliberately. Part 1's robustness is against ALL adversaries within a Hamming budget of (1−R)n/2 symbols over F_{2^ℓ} (the max in Risk_{d,r}); the bounded party there is the LEARNER. Part 2 is the axis flip: the learner is compared against a poly-time adversary versus an unbounded adversary, both at Hamming budget (1−√R)n."
priced_resource: "Model parameters — but defined as BITS OF MODEL DESCRIPTION, not weights or neurons. Definition 2: L outputs models with at most p(·) parameters iff |Supp(L(·,λ))| ≤ 2^{p(λ)}. The price is the log-cardinality of the set of classifiers the learner can emit."
tags: [adversarial-ml, cryptography, one-way-functions, overparameterization, robustness, complexity-theory, computational-vs-it-robustness, pseudorandomness]
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: parameters
cls_tightness: budget
cls_baseline: n/a
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: time
cls_assessed: explicit
cls_evidence: "Are there any learning tasks for which computationally bounded learners need to utilize significantly more model parameters than needed information-theoretically?"
cls_evidence_src: abstract / §1
cls_reason: "Classified on Part 1's base separation (Thms 20-21), the paper's own opening framing question and the first result stated, per rule 1 — not Part 2 (Thms 28-29), which flips the bound to the adversary and is a differently-shaped claim per the page's own Claim Boundary table. party=learner per rule 3: the bound binds the learner's computational status (poly-time vs unbounded), not an attacker (Thm 21 has no adversary at all). unit=parameters per the front matter's own priced_resource field ('Model parameters... the price is the log-cardinality of the set of classifiers the learner can emit'); tightness=budget since the field's own definition names 'a parameter count' as a budget example, and alpha/beta here are free polynomials in lambda set by the construction, not a ratio derived from another party's cost. frame=compute, not capability, because the qualifying condition producing the parameter cost is the learner's own poly-time-ness (Def 2's PPT-vs-unbounded split), the direct computational-constraints half of the paper's title; second_notion=time records that same poly-time/unbounded split as an incomparable second resource notion on the one classified party, per rule 4b. baseline=stated: the unbounded learner's 2λ-parameter cost (Thm 20) is the explicit reference the poly-time learner's alpha+beta/alpha-over-2 cost is measured against, per the framing question's own 'than needed information-theoretically'. target/family/phase/access/write=none: pure learning-theory separation, no ML attack, matching the sibling exponent papers (information-exponent-online-sgd.md, leap-complexity-sgd.md, noise-sensitivity-exponent.md)."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

The paper prices a learner in **model parameters** and asks what that price is as a function of the
learner's computational budget. Its opening question is verbatim: *"Are there any learning tasks for
which computationally bounded learners need to utilize significantly more model parameters than
needed information-theoretically?"* The answer, under the existence of one-way functions, is yes, on
constructed tasks, with an arbitrary polynomial gap.

**Part 1** builds a task (Construction 19) whose labels are a GF(2) inner product against a
**pseudorandom** key rather than a random one. An unbounded learner inverts the PRG, stores the
`λ`-bit seed, and is done. An efficient learner cannot tell the pseudorandom key from a uniform one,
so it inherits the counting lower bound that applies to a uniform key: its model must be long enough
to hold the key itself. Robustness is added by encoding the instance under a Reed–Solomon code and
masking it with a second pseudorandom string, so that a learner too short to hold the mask cannot
even recover the message under perturbation. A sampler (Vadhan) is used to keep the instance size at
`Θ(n log λ)` while the key stays at length `α ≫ n`, which is what stops the separation from being an
artefact of long inputs.

**Part 2** flips the axis to the adversary, extending Garg–Jha–Mahloujifar–Mahmoody ALT'20. The
instance carries a signed label and a list-decodable encoding of it. A poly-time adversary cannot
forge the complementary message/signature pair, so after perturbation exactly one valid pair survives
list-decoding and a learner with **zero** stored parameters reads the label off it. An unbounded
adversary forges the other pair, both survive, and the learner must fall back on a second recovery
channel keyed by an `α`-bit secret — which it can only use if it stored `≳ α/2` parameters.

The mechanism throughout is the same: a short model cannot retain enough min-entropy about a hidden
string, so the leftover-hash / small-bias masking lemmas make the label look uniform in the model's
view. The upper bounds all come from robust ERM over a finite class, via Theorem 3.1 of
Bubeck–Lee–Price–Razenshteyn (ICML'19), which costs `log|C|/δ` samples for a class `C`.

## Claim Boundary

- **Quantified over:** **Existence of a learning task**, not all tasks. Every result is of the form
  "there is a learning task parameterized by `λ` such that…". The paper is explicit that this is the
  scope: *"It does not imply, however, that this holds for all learning problems."* Within a task the
  parameter bounds are universal over learners of the stated computational class and over sample
  complexity — Claims 24 and 26 hold *"for any learner L (with an arbitrary sample complexity)"* with
  the stated parameter budget. The polynomials `n < λ < α < β` are free: the gap can be made any
  polynomial, e.g. `α = λ^5`, `β = λ^10`.

- **Antecedent:** One-way functions exist — nothing more. It is drawn on twice: PRGs of arbitrary
  polynomial stretch (HILL'99, Lemma 6) for Part 1, and signature schemes (Naor–Yung'89,
  Rompel'90, Lemma 8) for Part 2. The signature security used is deliberately weak: Definition 7's
  *"Weak unforgeability"* gives the adversary one honestly generated message/signature pair on a
  fixed message, and the footnote says this *"weaker security notion already suffices for our
  purposes."* A fresh key pair is sampled per instance. The assumption is standard and minimal.

- **Which party is bounded, per theorem:**

  | Theorem | Learner | Adversary | What it gives |
  |---|---|---|---|
  | 20 (upper) | unbounded | all adversaries at budget `(1−R)n/2` | robust ε-learning with **2λ** parameters, `Θ(λ/ε)` samples |
  | 20 (upper) | **poly-time** | all adversaries at budget `(1−R)n/2` | robust ε-learning with **α+β** parameters, `Θ((α+β)/ε)` samples |
  | 21 (lower) | **poly-time** | none — non-robust risk | no efficient learner with `≤ α/2` parameters ε-learns, `ε < 1/3` |
  | 22 (lower) | **poly-time** | budget `(1−R)n/2`; the exhibited attack is itself efficient | no efficient learner with `≤ c·β/log λ` parameters ε-robustly learns, `ε < 1/3`, `c = Θ(1)` |
  | 28 (upper) | poly-time | **poly-time**, budget `(1−√R)n` | **no parameters at all**, 0 samples, `negl(λ)` robust risk |
  | 29 (lower) | **unbounded** | **unbounded**, budget `(1−√R)n` | no learner with `≤ α/2` parameters ε-robustly learns, `ε < 1/3` |

  Two readings follow that are easy to get backwards. First, **Part 1 does not bound the adversary at
  all** — its robustness notion is the `max` over perturbations, i.e. the information-theoretic one —
  and the attack constructed inside the proof of Theorem 22 (replace the message block with a uniform
  string, then randomise `(1−3R)n/2` coordinates) is a poly-time attack, so the parameter blow-up
  survives restricting the attacker. The paper states this: *"Requiring the learner to be efficient
  increases the size of the model. This holds for robustness against both efficient and inefficient
  attackers."* Second, **Theorem 29 binds an unbounded learner**, so it holds a fortiori for efficient
  ones; its proof is pure min-entropy accounting and never invokes unforgeability. Unforgeability is
  what Theorem 28 needs.

- **Does not establish:** (a) Anything about natural tasks. Both tasks are **constructed** — inner
  products against PRG output, Reed–Solomon codes, samplers, signature schemes. The authors flag it
  and note the company they keep: *"we note that this is not particular to our work, but common to
  most prior works in the theory of learning showing 'separation' results."* Their own open question
  is *"whether similar phenomena also happen to real-world problems."* (b) Anything about neurons,
  weights, layers or gradient descent. "Parameters" here is **description length in bits**, counted as
  `log|Supp(L)|` — a learner that can emit `2^p` distinct classifiers has `p` parameters. The
  suggestive sentence *"Our results provides an explanation on why small but representative classes
  (e.g. 2 layers neural networks) of functions do not obtain same (robust) accuracy as larger models"*
  is an interpretive remark with no theorem behind it about neural architectures. (c) Real-valued
  models. The closing limitation restricts the result to finite output alphabets and bounded
  precision: infinite-precision reals would require redefining computational efficiency, since *"the
  inputs are infinitely long."* (d) That robustness is what drives overparameterization in general —
  Theorem 21's separation is **non-robust**; robustness only widens an already-present gap.

- **Abstract vs theorem:** Three gaps, one of them material.
  1. **Material.** The abstract says the work *"extend[s] the recent result of Bubeck and Sellke
     [NeurIPS'2021]… to the computational regime."* No theorem of Bubeck–Sellke is used, extended or
     re-proved anywhere. "Sellke" occurs exactly three times in the PDF: abstract, one motivating
     sentence in §1, and the bibliography. There is no isoperimetry, no Lipschitz condition, no smooth
     parameterization in the paper. The Bubeck-line result actually used is
     **Bubeck–Lee–Price–Razenshteyn ICML'19, Theorem 3.1** (robust ERM over a finite class), imported
     as Theorem 3. The relationship to Bubeck–Sellke is thematic, not technical.
  2. Informal Theorem 1 promises *"Any polynomial-time learner needs Θ(β) parameters to robustly
     learn the task."* Theorem 22 proves `c·β/log λ`. The formal bound is `Θ(β/log λ)`, a log factor
     short of the informal one, and the constant is constrained by
     `c < (log λ / 3ℓ)·(1−3R)·log(1/(1−R))` with `ℓ = Θ(log λ)`.
  3. Informal Theorem 1 says the efficient robust learner of Part 2 uses *"O(1) parameters"*; Theorem
     28 delivers strictly more — a learner that *"outputs a model with no parameter"* and has zero
     sample complexity. Also worth noting that Theorem 1's "needs `Θ(α)` parameters to learn"
     (non-robustly) is a lower bound only: the efficient learner exhibited in Theorem 20 uses `α+β`,
     so nothing pins the non-robust efficient optimum between `α/2` and `α+β`.

## Key Contributions

- **A parameter-count separation between bounded and unbounded learners.** Same task, same data: the
  unbounded learner needs `2λ` parameters, the poly-time learner needs at least `α/2`, where `α` is an
  arbitrary polynomial in `λ`. The lever is that the hidden key is pseudorandom, so the efficient
  learner is forced to treat it as random and pay its full length; the unbounded learner inverts the
  PRG and stores the seed. The paper's summary: *"the computational efficiency of the learner could be
  the cause of having overparametarized models."*
- **Robustness widens the gap, for the bounded learner only.** Adding a perturbation budget raises the
  efficient learner's requirement from `Θ(α)` to `Θ(β/log λ)` while the unbounded learner still pays
  `2λ` (Theorem 20 covers robust learning too). This is the paper's answer to *"Are there any learning
  tasks for which computationally bounded robust learning comes at the cost of having even more model
  parameters than non-robust learning?"*
- **Bounding the adversary buys the parameters back — all of them.** Part 2's efficient learner stores
  *nothing* against a poly-time attacker, while `α/2` parameters are provably necessary against an
  unbounded one. The list-decodable encoding is the new ingredient over GJMM ALT'20: it converts a
  detect-and-abort classifier (which may output `⊥`) into one that always outputs the correct label,
  because the honest pair always survives list-decoding and, against an efficient attacker, is the
  only valid pair in the list.
- **The instance-size fix.** A naive version of either construction has instances as long as the
  model, which would make the separation vacuous. Vadhan's sampler (Lemma 12) sub-samples the long key
  at `n` coordinates from a short seed while preserving min-entropy rate, so instances stay at
  `Θ(n log λ)` with the key at length `α` or `β`. This is the technically load-bearing step.
- **A caution about how the question must be posed** — see below; the paper's most transferable
  contribution to a survey.

## Key Definitions / Theorems

**The formulation caution (§1).** Before any result the paper warns: *"One should be cautious in how
to formulate the question above."* The reason is that many information-theoretically learnable tasks
are believed computationally hard outright (learning parity with noise is the example given), and for
those *"one can interpret this as saying that the efficient learner requires infinite number of
parameters, as a way of saying that the learning is not possible at all!"* A parameter separation
built on such a task would be measuring hardness of learning, not cost of learning. The formulation
must therefore pin the efficient learner to *success*: the task has to be efficiently learnable, just
expensively so. This is exactly why Theorem 20's efficient upper bound (`α+β` parameters,
`Θ((α+β)/ε)` samples) is not a throwaway — it is the half of the result that makes the lower bound
mean overparameterization rather than intractability. Stated as the paper's own aim: *"we are
interested in understanding the reason behind needing a large number of model parameters when
learning is possible."*

**Definition 2 (parameters as bits).** *"L outputs models with at most p(·) bits of parameters"* iff
for all `λ`, the support of `L(·, λ)` has size at most `2^{p(λ)}`. Parameter count is therefore the
log-cardinality of the learner's output range — a description-length measure, architecture-free. The
same definition block gives ε-learning, robust learning against *all* adversaries of budget `r` under
metric `d`, and robust learning against *poly-time* adversaries (where the perturbation comes from
`x' ← A^{D_λ}(x, h(x), f)` rather than from a `max`). The two robust-risk definitions are what let the
paper move the computational bound between learner and adversary.

**Construction 19 (Part 1's task).** Fix `n < λ < α < β`, all polynomial in `λ`. PRGs
`f₁ : {0,1}^λ → {0,1}^α` and `f₂ : {0,1}^λ → {0,1}^β`; a Reed–Solomon code of dimension `k`, block
length `n`, constant rate `R < 1/3` over `F_{2^ℓ}` with `ℓ = Θ(log λ)`; samplers `samp₁`, `samp₂` from
Lemma 12 with `κ₁ = Θ(1/log λ)`. The distribution `D_s` emits
`([u₁], [u₂], m, Enc(m) + f₂(s)|samp₂(u₂))` with `m` uniform in `F_{2^ℓ}^k`; the label is
`h_s(x) = ⟨m, f₁(s)|samp₁(u₁)⟩` over `F₂`. Adversary budget: `(1−R)n/2` symbols in Hamming distance
over `F_{2^ℓ}`. Instance size `Θ((k+n)ℓ) = Θ(n log λ)`.

**Theorem 20.** An information-theoretic learner (robustly) ε-learns Construction 19 with parameter
size `2λ` and sample complexity `Θ(λ/ε)`. An efficient learner (robustly) ε-learns it with parameter
size `α+β` and sample complexity `Θ((α+β)/ε)`. Both learners are robust ERM over a finite class — the
`2^{2λ}` functions `f_{s,s'}` for the unbounded learner, the `2^{α+β}` functions `f_{P,Q}` for the
efficient one, which the efficient learner can search by linear algebra. Sample complexity follows
from Theorem 3 (BLPR'19).

**Theorem 21 (non-robust lower bound, bounded learner).** No efficient learner outputting models with
`≤ α/2` parameters ε-learns `F_λ` for `ε < 1/3`. Two steps: Claim 23 swaps the pseudorandom key for a
uniform one at `negl(λ)` cost by reduction to PRG security (this is the only place efficiency of the
learner is used); Claim 24 shows that against a uniform `α`-bit key, a model with `≤ α/2` parameters
leaves `H̃_∞(P|Z) ≥ α/2`, the sampler preserves min-entropy rate on `P|samp₁(u₁)`, and the
inner-product extractor (Theorem 15) makes the label statistically uniform in the view `(x, z)`. Risk
`> 3/8`.

**Theorem 22 (robust lower bound, bounded learner).** There is a constant `c` such that, against an
adversary perturbing `(1−R)n/2` symbols, no efficient learner outputting a model with `c·β/log λ`
parameters ε-robustly learns `F_λ` for `ε < 1/3`. The attack replaces `m` with a uniform string (cost
`Rn`) and randomises a random subset of `(1−3R)n/2` coordinates of the masked codeword. Theorem 18
(noisy RS is `(1−R)^s`-small-biased) plus Theorem 17 (small-bias masking) push the perturbed instance
to statistical uniformity, so the label is unpredictable. The admissible constant satisfies
`c < (log λ / 3ℓ)·(1−3R)·log(1/(1−R)) = Θ(1)`.

**Construction 27 (Part 2's task).** Fix `n < λ < α`. Signature scheme `(Gen, Sign, Verify)`;
list-decodable RS code `LEnc` with constant rate `R < 1/4` over `F_{2^ℓ}`, `ℓ = Θ(log λ)`, efficiently
`(1−√R, poly(n))`-list-decodable by Guruswami–Sudan; sampler `samp` into subsets of `{1,…,α}` of size
`n`. Instances are `([u], [v], [vk], LEnc(b, Sign(sk,b)), [b + ⟨v, s|samp(u)⟩])` with a fresh key pair
per instance and the label simply `b`. Adversary budget `(1−√R)n` symbols. Instance size
`Θ(n log λ)`.

**Theorem 28 (upper bound against a bounded adversary).** There is an efficient learner with **zero
sample complexity** that *"outputs a model with no parameter"* and `negl(λ)`-robustly learns `F_λ`
against computationally bounded adversaries of budget `(1−√R)n`. It error-corrects `[vk]`,
list-decodes the perturbed `LEnc` block, and outputs the message of the unique valid message/signature
pair. Uniqueness is exactly weak unforgeability: a second valid pair in the list would be a forgery.

**Theorem 29 (lower bound against an unbounded adversary).** Against computationally unbounded
adversaries, no information-theoretic learner with `α/2` parameters ε-robustly learns `F_λ` for
`ε < 1/3`. The unbounded attacker forges `Sign(sk, 1−b)` and overwrites `n/2` symbols of the encoded
block, leaving a string equidistant from both encodings and independent of `b`; the second channel
`[b + ⟨v, s|samp(u)⟩]` is useless to a model too short to retain min-entropy about `s`. Risk `> 1/3`.

## Connections

- [A Universal Law of Robustness via Isoperimetry](universal-law-of-robustness.md) — **the comparison
  the paper invites and does not make.** Both count parameters and both tie the count to robustness,
  and there they part. Bubeck–Sellke is an **information-theoretic, universal, unconditional** law:
  for *any* smoothly parameterized class over an isoperimetric distribution in `R^d`, smooth
  interpolation of `n` points needs `p ≳ nd` — the learner may be unbounded, no assumption is used,
  and the price of robustness is a factor `d` paid by *everyone*. This paper is **computational,
  existential and conditional**: on *one constructed* task, under one-way functions, the price is paid
  only by the *efficient* learner, since the unbounded learner discharges the same task with `2λ`
  parameters. The two also disagree on what a parameter is — a real weight of polynomial magnitude
  under a smooth parameterization there, a bit of model description (`log|Supp(L)|`) here — and on
  what varies: Bubeck–Sellke separates *interpolation from smooth interpolation for a fixed learner
  class*, this paper separates *bounded from unbounded learners on a fixed task*. They do not conflict
  when Part 2 gets robustness at zero parameters, because the construction is a discrete Hamming-metric
  task with no isoperimetry and no Lipschitz requirement, so Bubeck–Sellke's hypotheses simply do not
  apply. The abstract's claim to "extend" that result should be read as positioning, not as a
  technical dependency — see Claim Boundary.
- [Adversarially Robust Learning Could Leverage Computational Hardness](computational-hardness-robust-learning.md)
  — the direct predecessor (GJMM, ALT'20) by four of the five authors. Part 2 is that paper's
  signature-plus-error-correction construction with two additions: list-decoding (so the classifier
  never has to abort with `⊥`) and a second, secret-keyed recovery channel (so the *parameter count*,
  not just the risk, separates).
- [Adversarial Examples from Computational Constraints](adversarial-examples-computational-constraints.md)
  — the BLPR'19 line, cited here for motivation *and* used technically: Theorem 3 of this paper is
  Theorem 3.1 of BLPR'19, the robust-ERM sample bound `log|C_λ|/δ` behind every upper bound.
- [Computational Limitations in Robust Classification and Win-Win Results](win-win-robust-learning.md)
  — Degwekar–Nakkiran–Vaikuntanathan, cited alongside BLPR'19 as prior evidence that the learner's
  computational limits cause adversarial vulnerability. This paper asks the same question with model
  size as the priced quantity.
- [The Curse of Concentration in Robust Learning](curse-of-concentration.md) and
  [A Complexity Theoretic Approach to Adversarial ML](complexity-theoretic-adversarial-ml.md) — the
  Mahloujifar–Mahmoody programme this work sits inside; concentration results are the geometric,
  IT-side obstacles that computational bounding is meant to sidestep.
- [Robust Generalization Requires More Data](robust-generalization-more-data.md) — the same "robustness
  costs a resource" shape, priced in **samples** rather than parameters. Useful contrast for a survey
  organised by priced resource.
- [Model Size as a Priced Resource](../concepts/model-size-as-priced-resource.md) — the axis this paper
  contributes.
- [Computational vs Information-Theoretic Robustness](../concepts/computational-vs-it-robustness.md) —
  Part 2 is a parameter-count instance of exactly this gap.
- [Universal Law of Robustness](../concepts/universal-law-of-robustness.md),
  [Robust PAC Learning](../concepts/robust-pac-learning.md),
  [Intrinsic Robustness](../concepts/intrinsic-robustness.md) — adjacent concept pages.
- [Sanjam Garg](../entities/sanjam-garg.md), [Somesh Jha](../entities/somesh-jha.md),
  [Saeed Mahloujifar](../entities/saeed-mahloujifar.md),
  [Mohammad Mahmoody](../entities/mohammad-mahmoody.md),
  [Mingyuan Wang](../entities/mingyuan-wang.md).

## Open Questions / Limitations

- **Natural tasks.** The authors' own headline open question: *"It is a fascinating open question
  whether similar phenomena also happen to real-world problems."* Nothing here transfers to image
  classification without a new construction.
- **Bits, not neurons.** The gap between the paper's parameter measure (`log|Supp(L)|`) and a neural
  network's weight count is unbridged. The remark about two-layer networks is an interpretation, not a
  corollary.
- **Infinite precision.** The construction is over finite fields with binary labels. The paper notes
  the extension to any finite output alphabet and to bounded-precision reals, and stops there:
  infinite precision *"needs to revisit computational efficiency, as the inputs are infinitely long."*
- **Tightness.** For non-robust efficient learning the lower bound is `α/2` and the exhibited learner
  uses `α+β`; the true efficient optimum is not pinned. For robust efficient learning the bound is
  `Θ(β/log λ)` against an `α+β = Θ(β)` upper bound, so that side is tight up to `log λ`.
- **The reverse direction is untouched.** GJMM ALT'20 proved that a computational-vs-IT robustness gap
  implies average-case hardness. No analogous "parameter gap implies hardness" converse appears here,
  so it is open whether overparameterization-from-computational-constraints is *equivalent* to a
  cryptographic assumption or merely implied by one.
- **No lower bound on the unbounded learner.** `2λ` is an upper bound for the IT learner; nothing rules
  out doing it with fewer.

## Quotes / Notable Passages

> "Are there any learning tasks for which computationally bounded learners need to utilize
> significantly more model parameters than needed information-theoretically?"

> "One should be cautious in how to formulate the question above."

> "one can interpret this as saying that the efficient learner requires infinite number of parameters,
> as a way of saying that the learning is not possible at all!"

> "we are interested in understanding the reason behind needing a large number of model parameters
> when learning is possible."

> "Are there any learning tasks for which computationally bounded robust learning comes at the cost of
> having even more model parameters than non-robust learning?"

> "Are there any learning tasks for which robust learning can be done with fewer model parameters when
> dealing with polynomial-time adversaries?"

> "requiring a learner to be efficient increases the size of the model, while requiring an attacker to
> be efficient helps reduce the size of the model."

> "Requiring the learner to be efficient increases the size of the model. This holds for robustness
> against both efficient and inefficient attackers."

> "Restricting to only computational efficient attackers reduces the size of the model. This holds for
> both efficient and inefficient learners."

> "It does not imply, however, that this holds for all learning problems."

> "It is a fascinating open question whether similar phenomena also happen to real-world problems."

> "we note that this is not particular to our work, but common to most prior works in the theory of
> learning showing 'separation' results"

> "Our results provides an explanation on why small but representative classes (e.g. 2 layers neural
> networks) of functions do not obtain same (robust) accuracy as larger models."

> "outputs a model with no parameter" (Theorem 28)

> "L outputs models with at most p(·) bits of parameters" (Definition 2)
