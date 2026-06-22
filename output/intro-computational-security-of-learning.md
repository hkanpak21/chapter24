# Toward a Computational Theory of Learning Security

*A field introduction — broad first, sections to follow.*

> **Thesis in one line.** Today's security claims about learning systems rest on *statistical* footing
> (sample complexity, concentration of measure, differential privacy). We want to move them onto
> *computational* footing — reductions, complexity classes, one-wayness — the same transition cryptography
> made when it left Shannon's information theory for reduction-based security. Call the target the
> **"Goldwasser theorem of AI."**

This document collects, in plain prose, the picture that has emerged from (a) the founding conversations
about what Chapter 24 of Arora–Barak should be, (b) the adversarial **lödeg ↔ nannosh** dialogue that built
the formal theory ([chapter_24.md](chapter_24.md)), and (c) the June 2026 design sessions that produced the
elementary on-ramp game, `COMP-MEM`. It is meant to be read once, top to bottom, to get the *shape*. After
that we will go back and take each section apart properly.

---

## 0. The wrong footing

Cryptography was once an information-theoretic subject. Shannon proved that perfect secrecy *requires* a key
at least as long as the message (`H(K) ≥ H(M)`). That is a beautiful, exact, and **pessimistic** theorem:
it says secrecy is a matter of entropy, and past the entropy budget you are simply out of luck. Modern
cryptography exists because Diffie, Hellman, Goldwasser, Micali and others made a different move: stop asking
whether the adversary *can* break the scheme, and ask whether it can break it *efficiently*. Security became
**computational** — "no polynomial-time adversary wins by more than a negligible margin" — and was *proved*
by **reduction**: break the scheme, and I will use you to solve a problem everyone believes is hard.

Learning theory is, right now, where cryptography was before that move. Its sharpest security results are
*information-theoretic*: adversarial examples are inevitable because of **concentration of measure** in high
dimensions (Mahloujifar–Diochnos–Mahmoody); robust generalization "requires more data"
(Schmidt et al.); differential privacy bounds membership inference by an entropy-like budget. These are real
and important — but they are **Shannon-style**: they bound what is *possible*, not what is *efficient*, and
they are correspondingly pessimistic. The whole point of this research program is to make the computational
move for learning: to find the place where the information-theoretic story runs out and a *reduction-based*
story takes over.

The reason this matters is not bookkeeping. Information-theoretic bounds routinely say "you are doomed" in
settings where, empirically, nothing bad happens — because the adversary that the bound assumes is
*computationally unbounded*, and the real one is not. A computational theory is the only way to explain why
deployed systems are *more secure than the statistics predict*, and to certify when they actually are.

---

## 1. Stop studying attacks. Study the machine.

The literature has a habit: every time the *attack* changes, it changes the *object of study*. For evasion,
the model is a function on a metric space. For poisoning, the learner is a tamperable compiler. For
backdoors, it is something else again. The attack-taxonomy (evasion / poisoning / backdoor / extraction / …)
gets baked into the definitions, and the field fragments into incomparable sub-results.

Cryptography refused to do this. It did not write one definition per attack ("differential-cryptanalysis
security," "linear-cryptanalysis security"). It wrote **one game** — indistinguishability under chosen
inputs — and let the adversary's *capabilities* be a parameter (the oracle handles: CPA, then CCA, …). Every
"attack" became a setting of one knob, not a new universe.

The Chapter 24 move is the same. Fix **one object** — the learning system as an abstract machine — and make
the attack a **capability vector `κ`** over that machine's tapes. Concretely the machine is:

- a **source** `Π` — a program that emits observations (probability is the special case where `Π` has a
  random tape); this is where *every* distributional assumption is forced to live, out in the open;
- a **learner** `L` — a transducer that reads `Π` through a bounded oracle (in mode: i.i.d. draw / membership
  query / statistical query / chosen input — *each is a coordinate of `κ`*) and writes an **advice string**
  `w`;
- a fixed universal **evaluator**: the **model** is `M_w = U(w, ·)`, run for `t_eval` steps.

Inference is just non-uniform evaluation of `w` — the **P/poly floor** (Arora–Barak Ch. 6). The real
computation is `L` *synthesizing* a program `w` that behaves like `Π` under bounded access. **Learning is
program synthesis / inversion of a generative source**, and `|w|` is *capacity*. A linear regressor and an
LLM are the *same* machine at two different `(|w|, t_eval)` coordinates.

The payoff of this stubbornness: you define the adversary *once*, as `κ = (what it observes, when, how much,
passively or by choosing)`, and evasion / poisoning / membership-inference / backdoor all fall out as
settings of `κ`. The capability vector is the CPA-handle, generalized.

---

## 2. One object, four corners — and "security *is* learning lower bounds"

If accuracy and security are both properties of the *same* machine, they should be the same *kind* of
statement. In the dialogue they are: a single risk functional `Risk*(⊕, base)` produces **four corners** by
changing what you measure —

- **accuracy** (expected error),
- **detection** (a quantile — can an auditor tell something is off?),
- **security** (the worst case / `sup` — can an adversary force failure?),
- **privacy** (distinguishing on a *neighborhood* base — can an adversary tell two training-worlds apart?).

The last corner is the one we will live in (Section 4). The deep claim that organizes everything is the
**τ-staircase**: a chain of thresholds `τ_stat ≤ τ_detect ≤ τ_recover` at which a task becomes statistically
determined, then detectable, then recoverable — and **security is exactly a learning lower bound**: "the
attack is hard" *means* "this associated learning/estimation problem cannot be solved with the adversary's
resources." The rungs are **unconditional at the SQ floor** (no assumptions), and become **OWF-relative**
higher up. Cryptographic hardness and statistical-learning hardness turn out to be two readings of one
staircase. That sentence — *security is learning lower bounds* — is the whole program compressed.

The single organizing device underneath is the **membrane**: the boundary across which `L` accesses `Π`. It
splits every resource into a *deploy* side and a *source* side, and its **closure** (when a deployed model's
outputs become next-generation training data) carries the entire "agentic / performative" loop —
**forward information `I`** is learning, **reverse information `I^←`** is steering.

---

## 3. The two readings, and the bridge between them

Building the theory took an adversarial dialogue between two stances, deliberately staffed by two agents:

- **lödeg** reads learning as **synthesizing a small circuit that approximates the source** — the
  low-degree / SQ / circuit-capacity lens; the interesting quantity is `|w|` and how much of `Π` is
  *efficiently extractable*.
- **nannosh** reads learning as **inverting a generative source** — the one-wayness / inductive-inference
  lens; learning, pushed hard enough, *is* breaking a one-way function.

These are not rivals; they are two projections of one machine, and the dialogue's central **proved** result
— the **keystone** — is what fuses them:

> **Keystone.** The learner that minimizes `Kt(w)` (Levin's time-bounded Kolmogorov complexity of the
> advice) is *simultaneously* universal **and** generalizing — under the hypothesis `I ≪ s` (the information
> extracted is much smaller than the sample). Generalization gap scales like `Kt(w)/s`.

Read that as: *the right notion of capacity is not parameter count `|w|` but compressibility `Kt(w)`*, and
the same quantity that makes a model generalize (low `Kt(w)`) is the quantity a security reduction grabs onto.
lödeg's capacity rail and nannosh's one-wayness rail are the same staircase seen from two sides.

This also tells us **which way the bridge runs**, which is the crux of Mursit's ambition. We do *not* claim
"learning ≡ one-way functions" — that identity is false. We claim a **regime change**:

> **Crown jewel (target).** *Past a certain point, learning reduces to breaking a one-way function.* Below
> the point, hardness is statistical / unconditional (the SQ floor); above it, hardness is witnessed by a
> cryptographic reduction. The remarkable result is the **threshold**, not an equivalence — the AI analogue
> of "past the Shannon bound, you must pay with computational assumptions."

The flavor of claim we are ultimately after is concrete and legible, e.g. *"in this scenario, an adversary
that learns the training data to >90% accuracy can be turned into a OWF-inverter — and no known method does
the former."* Note the last clause: the security can rest on a **measured frontier of learning ability**, not
only on an asymptotic assumption — this is the **concrete (exact) security** style (Bellare–Rogaway), where a
reduction is a *measuring instrument* relating attack-effort to reference-problem-effort. *Measurable, not
merely "hard."*

---

## 4. The elementary on-ramp: `COMP-MEM`

The full theory is abstract. To keep it honest you need *one running game*, the way semantic security was
built entirely on IND-CPA before anyone proved a composition theorem. We adopt **`COMP-MEM` — Computational
Membership Indistinguishability**:

> The training set is the secret. An adversary with capability `κ` interacts with the trained model and must
> decide whether a target point `x` was in the training set. The data may *information-theoretically* reveal
> membership; security says **no efficient (`κ`-bounded) adversary extracts it** beyond advantage `ε`.

This is the **computational analogue of differential privacy**. DP is the Shannon-style, information-theoretic
membership bound; `COMP-MEM` is its reduction-based successor. It is also exactly the **privacy corner of
`Risk*`** and the **bottom rung (`τ_stat`/distinguishing) of the staircase** — so the on-ramp and the full
theory are the same building, entered at the ground floor.

Several design points, each a correction earned the hard way in the June sessions:

- **`COMP-MEM` is a floor, not a master key.** Membership inference is the *weakest* privacy attack
  (reconstruction ⇒ property-inference ⇒ MI); as a *guarantee* this reverses — MI-security is the *minimal*
  bar. So `COMP-MEM` is a necessary floor of **confidentiality**, and like IND-CPA it gives you nothing about
  **integrity**. Crypto needs *two* foundational games — IND-CPA *and* EUF-CMA — because confidentiality and
  integrity are orthogonal. Learning security inherits the split: evasion / correctness / verification need a
  separate `EUF-CMA`-analogue generator. (Trying to fuse confidentiality, integrity and availability into one
  over-abstract object is precisely the flaw we will diagnose in the AIOracle framework — Section 7.)
- **The general game is `COMP-TW` (Training-World Indistinguishability):** two training-worlds differing by a
  controlled `Δ`. `Δ =` one example is `COMP-MEM`; `Δ =` a backdoor insertion is backdoor-detection; `Δ =` a
  poisoned batch is poisoning-detection. One schema, many games — and `COMP-MEM` is its smallest point.
- **The adversary is `κ = (O, T, B, mode)`** — *what* it observes (a projection of the machine's tapes:
  dataset, weights `w`, gradients, logits, outputs), *when* on the `pre-training → training → inference`
  timeline, *how much* (e.g. an `f`-fraction of inference calls), and passively vs. by *choosing* inputs (the
  CPA-vs-CCA distinction). Build on the simplest lattice point first — black-box, inference-only, passive —
  then climb. The "when" axis is seductive but dangerous: observing *during* training makes the game adaptive
  (CCA2-hard to reason about), so it is climbed, not assumed.
- **Calibration zero.** Because the dataset is the *secret*, the baseline adversary `κ₀` has only
  *prior/public* knowledge (the distribution, the architecture, the "model card") — **not** the realized
  training set. Security is the **marginal advantage** `Adv(κ) − Adv(κ₀)`: what the *trained model* leaks
  *over and above* what the data already reveals. Without `κ₀` you "prove a leak" that was just the data being
  informative.

---

## 5. The lineage (so we are not reinventing 1989)

The crown-jewel shape — "learning reduces to breaking crypto" — is **not new in spirit**, and you must read
its ancestors before claiming the descendant:

- **Kearns–Valiant 1994** proved that learning finite automata / Boolean formulae is **as hard as inverting
  RSA / factoring / discrete log**. This is *literally the prototype* of the crown jewel, proved in 1989.
- **Blum–Furst–Kearns–Lipton 1993** built one-way functions *out of* hard learning problems — the bridge
  running the other direction, and the ancestor of **LWE**.
- **Degwekar–Nakkiran–Vaikuntanathan 2019 (Win-Win)** is the modern version: hardness of robust
  classification ⇔ one-way functions exist.
- **Hirahara–Nanashima 2023 (Learning in Pessiland)** maps what learning looks like in the world where OWFs
  *don't* exist — i.e. it characterizes the *threshold* itself.

A crucial honesty, though: **the word "learning" is overloaded.** Kearns–Valiant "learning" is PAC learning a
*concept class* with planted cryptographic structure; deep-learning "learning" is approximate, improper ERM
by SGD on *one natural distribution*. The hardness results live on the far side of a real chasm. The
**interpolant** — and this is why the planted-models / statistical-computational-gap corpus
(Brennan–Bresler, the SQ ≈ low-degree equivalence, the low-degree survey) is **load-bearing, not background**
— is **average-case PAC over structured-but-natural distributions**. "Natural distribution with hidden
structure" is exactly what planted clique, the stochastic block model, and LWE *formalize*. That corpus is
the bridge tile between abstract PAC-hardness and deep learning.

And there is a subtle warning we will keep returning to: the "learning-shaped" adversary (the one bounded by
*statistical-query* access, which is roughly what SGD is) is **not** all of PPT. Parity is SQ-hard yet broken
by Gaussian elimination. So a security claim resting on SQ/low-degree lower bounds is **unconditional but
restricted** — it secures against learning-shaped attackers, not arbitrary efficient ones. That is either the
realistic threat model or a hole, depending on the deployment; it is a *decision*, not a fact. We secure
against **all PPT first** (paying with a OWF assumption), and treat the learning-shaped adversary as the
Phase-2 extension.

---

## 6. Is it a theory, or an elegant reframing?

The dialogue refused to let itself off the hook. Its Phase 2 asked the brutal question — *is this a genuine
theory, or has it just re-described SQ / low-degree / crypto-reduction results in new vocabulary?* — and
reached an **honest, referee-proof verdict**:

> **An organizing theory — not vacuous, not yet validated — comprising:**
> 1. faithful reframings of SQ / incompressibility / crypto-hardness, **plus one proved native keystone**
>    (min-`Kt(w)` learner is universal *and* generalizing under `I ≪ s`);
> 2. **one native technique with open teeth** — inference-aperture-relativized incompressibility — whose new
>    unconditional content is open and plausibly as hard as a circuit lower bound;
> 3. **one native, falsifiable prediction**, derived from the keystone — a **comp-stat envelope**
>    `θ_comp ≤ Φ(θ_data)` relating the inference-compute scaling exponent to the data-scaling exponent, with a
>    decisive experiment (measure both across tasks; a point above the envelope refutes it) — and that
>    experiment *is* a direct test of the keystone;
> 4. **one methodological discipline** — a "separation principle" (statistics ≠ computation) that
>    demonstrably forbids the field's standard false unifications.

The point of printing the weaknesses first is that the position then cannot be shredded: every soft spot is
already named and converted into an open problem or an experiment. Two **headline open problems** anchor the
frontier — (OP1) the *computational* value of robust learning strictly below its *statistical* value (reduces
to the average-case hardness of Gap-`K^t`), and (OP2) whether certifying backdoor-freedom *inherently*
requires a trusted, more-powerful prover (i.e. **backdoor-freedom is not self-certifiable**).

---

## 7. Meeting Durak: the AIOracle, and two layers of one theory

Mursit will work with **F. Betül Durak** through the summer, whose group studies the cryptographic
formalization of AI security — the **AIOracle** framework (Villa–Durak–Kohno–Maharramli–Roesner): an AIOracle
= (GENERATE_DATA, LEARN, INFER) with an idealized predicate `φ`, characterized by completeness `p` and
security `ε` against a capability set `ATK`, with a utility–privacy tradeoff, a composition theorem, and a
predicate decomposition.

The dialogue's Phase 3 put Chapter 24 *against* AIOracle and reached a genuine integration, not a dictionary:

> **AIOracle (the *interface* layer — state / decompose / measure the predicate `φ`) and Chapter 24 (the
> *foundation* — `eval = U`, `Kt`, the membrane, the staircase) are two layers of one theory**, joined at
> `φ ↔ (T, r_judge)`.

It pays both ways. From the Chapter-24 side: a curation box `C` splits the source membrane into three attack
handles (`inj_source` / `inj_curation` / `inj_learn`) and contributes a factor to a backdoor **reproduction
number** `R = Λ_train · Λ_C · Λ_eval^sup · ρ_hit` (with `R<1` self-healing across retraining, `R>1`
self-propagation); a **three-term composition law** with a *margin-gated* alignment-tax; and a **new
frontier** — *intent-conditioned authorization reduces to intent-inference at cost `Kt(Π_intent)`*, which
explains why production agents fall back to coarse static policies (it is the only certifiable option below
that cost). From the AIOracle side, the gift is structural: the professor's idealized-model (GLM) proof
supplied a **missing rung** on the staircase, completing it into *cryptography's entire provability ladder* —

> **unconditional (SQ / statistical dimension) → idealized-model (GLM / ROM / GGM) → standard-assumption
> (OWF / `K^t`) → open (Gap-`K^t`)** — with the Canetti–Goldreich–Halevi caveat that the idealized rung is
> the one place provability can outrun real-world soundness.

So the security-as-learning-lower-bound framework does not merely borrow crypto's hard problems; it
**reproduces crypto's whole provability hierarchy** as the rungs of one staircase. That coherence is the
strongest single thing to come out of meeting the professor's framework — and it is the natural spine of the
**September Durak coda**.

---

## 8. What the summer builds, and where we go from here

The objective, stated plainly: **build the elementary, computational, reduction-based security theory of
learning, anchored on `COMP-MEM`, with the planted-models corpus as the bridge to deep learning, climbing the
Arora–Barak ladder (reductions → P/poly → BPP → OWF → average-case → interactive proofs) — toward the
threshold reduction "learning ⟶ breaking a OWF" and an honest place in the `Kt`-on-`U` theory.** The dated
plan is in the companion page,
[summer-2026-research-programme](../wiki/analyses/summer-2026-research-programme.md).

The sections we will write next, each expanding one part of the above:

1. **The machine.** `(Π, L, U, w)` formally; `κ` as the capability lattice; why inference is the P/poly floor.
2. **`COMP-MEM` and `COMP-TW`.** The games, `κ₀`, marginal advantage; why MI is the floor; the confidentiality/integrity split.
3. **Concrete security as measurement.** Reductions as instruments; the "measured learning frontier" security claim.
4. **The capacity rail.** `|w|` vs `Kt(w)`; the keystone (universal = generalizing); the comp-stat envelope.
5. **The one-wayness rail.** Kearns–Valiant → BFKL → Win-Win → Pessiland; the threshold; the crown jewel.
6. **The bridge.** Average-case PAC over planted/natural distributions; SQ / low-degree as the learning-adversary's hardness; the SQ-vs-PPT caveat.
7. **The staircase.** `τ_stat ≤ τ_detect ≤ τ_recover`; security = learning lower bounds; the four-rung provability ladder.
8. **The frontier.** The membrane's closure; the reproduction number `R`; intent-conditioned authorization; the Durak/AIOracle unification.

*Read the shape; then we take it apart.*
