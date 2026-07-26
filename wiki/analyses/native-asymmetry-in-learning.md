---
title: Native Asymmetry in Learning — Where a Security Gap Can Come From, and What Is Already Taken
type: analysis
date: 2026-07-25
tags: [complexity theory, cryptography, adversarial-ml, learning-theory, statistical-query, sample-complexity, hardness-reductions]
---

## Question / Motivation

Two questions, asked in the same session and answered together.

1. **Structural.** Every cryptographic security proof rests on an asymmetry between two parties. Deep
   learning has no obvious one: the defender trains with an efficient algorithm, the adversary attacks
   with an efficient algorithm, and both operate on data drawn from the same source. So *where does a
   security gap come from at all?* This is the question behind Mursit's recurring objection that
   GKVZ22 "uses a nice crypto tool and nicely embeds a crypto structure … but it just does not come
   natural to me."
2. **Tactical.** The [native-problem survey](../../output/native-computational-problems-survey.md)
   (2026-07-10) selected four reference problems and a Phase-2 adversary language. Which of the
   resulting theorem-shapes are actually unclaimed?

Question 2 was answered by two adversarial prior-art sweeps run on 2026-07-25 (lenses:
detection-vs-generation; attacker-vs-defender separations in restricted-class units). **This page also
records a retraction of a claim previously written into `CLAUDE.md`.**

> **Provenance.** The structural argument (§1–2) is this session's synthesis. The citations in §3 come
> from web sweeps, **not** from reading the papers. Entries marked † are single-sourced and must be
> verified before external use; this follows the convention of the native-problem survey. Exact
> theorem statements quoted below were extracted by the sweep from paper PDFs and should be
> re-checked against the source before any of them is cited in writing.

---

## Findings

### 1. The asymmetry audit

**Crypto has exactly three asymmetry shapes**, and all three are manufactured — a designer builds a
function with the property; nothing about computation supplies it for free:

| Shape | Statement | Primitives |
|---|---|---|
| **Direction** | forward easy, backward hard | OWF, trapdoor permutations |
| **Knowledge** | easy with `sk`, hard without | signatures, PKE, PRF |
| **Verification** | finding hard, checking easy | NP; what makes proofs and signatures possible |

**Run the four canonical ML task-pairs and check the sign:**

| Pair | Direction of the gap | Verdict |
|---|---|---|
| Train vs. **extract** | attacker has a noiseless labelling oracle, no distribution shift → extraction is *easier* than training | wrong sign |
| Train vs. **certify** | certifying `AdvRisk ≤ ε` is ∀∃ over the input ball → harder than training (this is why randomized smoothing exists) | wrong sign — the dialogue's OP2 |
| **Generate** vs. **detect** | same complexity | no sign |
| Train vs. **invert** | the training map is lossy and many-to-one | **right sign — the only one** |

One in four, and it lands in the privacy/leakage corner. This is an independent derivation of *why*
membership and inversion are the load-bearing corner — reached without going through `COMP-MEM`.

**The structural reason there is no keyed asymmetry.** The defender is an efficient algorithm operating
on data from a class the adversary can also process. Whatever `L` did to produce `w`, an adversary
drawn from the same class can do too. There is no primitive only one party can evaluate. **Crypto's
parties are asymmetric by construction; learning's parties are asymmetric only by access.**

This single fact explains three otherwise unrelated observations:

- **Why DP is the incumbent.** DP prices exactly the informational asymmetry — the one resource that
  natively exists. See [ACG+16](../sources/deep-learning-differential-privacy.md).
- **Why Groce–Katz–Yerukhimovich TCC'11 holds** (PPT buys nothing over IT in the single-curator
  client-server setting). If the only asymmetry is informational, computational bounding has nothing
  to bound. Their theorem is a corollary of the structure, not a surprise.
- **Why [GJMM20](../sources/computational-hardness-robust-learning.md) and
  [GKVZ22](../sources/planting-undetectable-backdoors.md) must weld on a key.** They need a
  computational asymmetry; learning does not supply one; so a signature or a lattice trapdoor is
  imported. The construction feels foreign because the trapdoor *is* foreign.

**Honest limit on this framing.** "Different tasks over the same distribution have different
complexity" is not new — it is a thirty-year-old TCS subject, and it must be cited as such:

- **Naor, "Evaluation may be easier than generation," STOC 1996** — the canonical statement, pointing
  the *opposite* way to what a security claim would want.
- **Viola, "The complexity of distributions," SICOMP (FOCS 2010)** — sampling is never harder than
  computing and is sometimes dramatically easier (XOR: `AC⁰`-hard to compute, `NC⁰` to sample).
- **Alvarez-Melis–Garg–Kalai, "Why GANs are overkill for NLP," NeurIPS 2022 (arXiv:2205.09838) §5** —
  *"Distinguishability is equivalent to increasing likelihood for general F, Q"*; both directions, an
  explicit polynomial-time reduction, relative to a bounded distinguisher class. **The
  detection ⟺ generation equivalence for learned distributions is proved.** It is framed as an argument
  that GANs are pointless for text, not as security.

So §1 is a *synthesis for a proposal introduction*, not a contribution. What survives as genuinely
diagnostic is the narrower statement: **none of these asymmetries are keyed.** Naor and Viola separate
*tasks*; they do not separate *parties*.

### 2. The two native sources of asymmetry (Mursit, 2026-07-25)

If the asymmetry cannot be manufactured, it must be located. There are two places it natively sits,
and they generate different security corners.

**(a) Knowledge of the data.** The defender saw `D`; the attacker did not. In leakage attacks this is
not an incidental feature of the setting — **the data-knowledge is precisely the asset under attack.**
The asymmetry and the security objective are the same object. That self-reference is why the privacy
corner is the only one where a *non-welded* security statement can exist, and it agrees with the §1
sign audit reached by a different route.

**(b) Access to parts of the algorithm.** In backdoor and poisoning settings the asymmetry is not
informational but *operational* — which parts of the pipeline a party may touch, and under what
budget. An attacker who may set weights arbitrarily (GKVZ22's setting) is a different object from one
who may only inject a bounded update within a constraint. And, in Mursit's formulation: **finding a
malicious sample and detecting a malicious sample have different computational aspects.** This is a
search-vs-decision gap inside one algorithmic class, generated by the shape of the access rather than
by a secret.

**Mapping onto `κ`.** These are not two ad-hoc observations; they are two independent components of
the capability vector `κ = (O, T, B, mode)` already defined in
[chapter_24.md](../../output/chapter_24.md):

| Source | `κ` component | Corner | Asset vs. asymmetry |
|---|---|---|---|
| (a) data-knowledge | `O` — the observation map | privacy / leakage | **identical** |
| (b) access | `T`, `B`, `mode` — phase, budget, choice | integrity / backdoor | **distinct** |

The consequence is a genuine structural prediction: **corner (a) can support a native security
statement; corner (b) cannot, and must import.** In (b) the contested asset (correctness, absence of a
trigger) is not the same object as the asymmetry (action-space access), so something external has to
bridge them — which is exactly what every backdoor result in the corpus does.

(b) already has a partial published home:
[CHLX25 Defendability](../sources/backdoor-defense-learnability-obfuscation.md) — *"In the absence of
computational constraints, defense is exactly as hard as learning. Meanwhile, in the presence of
computational constraints, defense is strictly easier than learning, but impossible for function
classes that are rich enough to support obfuscation."* Their Theorem 6.1 gives the positive side:
poly-size decision trees are efficiently uniform-defendable using **zero** calls to the example oracle.

### 3. Prior-art sweep — what is taken

#### 3.1 RETRACTION

A line written into `CLAUDE.md` earlier in this session — *"no security definition anywhere quantifies
over SQ- or low-degree-bounded adversaries"* — **is false.** Low-degree-bounded adversaries carry real
cryptographic security:

- **Bogdanov–Jones–Rosen–Zadik, "Low-Degree Security of the Planted Random Subgraph Problem," TCC
  2024** (arXiv:2409.16227 / eprint 2024/1497) — low-degree hardness of planted-subgraph detection up
  to `k ≤ n^{1−Ω(1)}`, "tight in the distinguisher's degree, its advantage, and in the number of leaked
  vertices," cashed into communication-optimal multiparty PSM and bit secret sharing with share size
  `(1+ε)log n`.
- **Abram–Beimel–Ishai–Kushilevitz–Narayanan, "Cryptography from Planted Graphs," TCC 2023** — the
  constructions it secures. Already in the corpus as
  [ABIKN23](../sources/cryptography-from-planted-graphs.md).
- † **Ngo–Kim, "Publicly-Verifiable Certificates for Statistical Algorithms," arXiv:2607.15528** —
  soundness quantified over adversarial provers whose data access is an SQ oracle. Single-sourced;
  **read manually before relying on it.**

Both original sweeps missed this because they searched the ML-security literature; the result lives in
the crypto literature. **Methodological lesson: a novelty check must sweep the venue where the
*technique* lives, not the venue where the *application* lives.**

#### 3.2 Occupied cells

| Claim shape | Owner | Units |
|---|---|---|
| Membership game with baseline-subtracted advantage | Yeom CSF'18 Def 6; Xiao–Devadas CRYPTO'23 "PAC Membership Privacy"; Desfontaines–Pejó PoPETs'20 dim. R | — (and the subtraction is a no-op: `Adv(κ₀) = 0` by construction) |
| **Attacker needs more samples than the trainer** | † **Haghifam–Smith–Ullman, arXiv:2508.19458** (Aug 2025), Thm 1.1: every sample-based MIA against Gaussian mean estimation needs `m ≳ n²ρ² + n`; their words — *"the first to show that the attacker sometimes needs many more samples than the [training algorithm]"* | information-theoretic (Ingster/χ²), **computationally unbounded adversary** |
| Security-relevant SQ separation | [BPR19](../sources/adversarial-examples-computational-constraints.md) ICML'19 — task efficiently learnable non-robustly, *not* efficiently robustly learnable by any SQ algorithm | SQ — but the **defender** fails, not the attacker |
| Defence against a *budget-bounded* adversary | † Głuch–Urbanke, "Query complexity of adversarial attacks," ICML 2021 (arXiv:2010.01039) — *"it might be possible to defend against a query-bounded adversary"* | queries; adversary budget-bounded, not class-bounded |
| **Attacker modelled as a restricted-class learner, two tasks compared** | [Canetti–Karchmer TCC'21 Covert Learning](../sources/covert-learning.md); † Karchmer SaTML'23 (eprint 2022/1039); [CHLX25](../sources/backdoor-defense-learnability-obfuscation.md); † arXiv:2504.20310 (matched-budget: mitigation `O(√K)` samples / `O(√T)` time) | **crypto** (LPN, OWF+iO, FHE) — only the *units* are unclaimed |
| Detection ⟺ generation for learned distributions | Alvarez-Melis–Garg–Kalai NeurIPS'22 (arXiv:2205.09838) §5 — proved, both directions, poly-time, bounded distinguisher class | — not framed as security |
| Memory-bounded adversaries | Raz FOCS'16 → Guan–Zhandry EUROCRYPT'19 → Dodis–Quach–Wichs EUROCRYPT'22/'23 | memory |
| Transformer-vs-RNN *learning* separation | † arXiv:2503.11272 | samples |

#### 3.3 A hard constraint: black-box is provably barren

† **Song, "Cryptographic Hardness of Score Estimation," NeurIPS 2024 (arXiv:2404.03272) §1.3.3:**

> *"the Gaussian pancakes problem is hard for polynomial-time distinguishers, even with access to exact
> sampling oracles. Thus, any procedure utilizing the learned sampler in a black box manner cannot
> solve the Gaussian pancakes problem."*

**This is the membrane, proved — and it says the black-box corner is empty for the programme's own
reference object.** Any theorem in this shape must be white-box / score-level, or must restrict the
distinguisher class. It directly contradicts the summer schedule's instruction to *"build on the
simplest lattice point first: `κ_inf` (black-box, inference-only, passive), then climb."*

#### 3.4 What survives — and an invitation

**The surviving cell**, stated precisely: *attacker and defender priced in the **same** exponent units
(information exponent, generative exponent `k*`, leap complexity), separated at a matched
query-or-sample budget, with the attacker restricted to the **same** algorithm class as the training
procedure.*

Verified by citation-graph sweep rather than keyword search — full Semantic Scholar citer lists of the
five foundational papers, filtered on `privac|securit|attack|adversar|membership|inversion|backdoor|extraction|leakage|cryptograph|watermark|stealing`:

| Paper | Citers | Security/privacy citers |
|---|---|---|
| Ben Arous–Gheissari–Jagannath, JMLR 2021 (information exponent), arXiv:2003.10409 | 148 | **0** |
| Abbe–Boix-Adserà–Misiakiewicz, COLT 2022 (merged-staircase), arXiv:2202.08658 | 152 | **0** |
| Abbe–Boix-Adserà–Misiakiewicz, COLT 2023 (leap complexity), arXiv:2302.11055 | 152 | **0** |
| Damian–Pillaud-Vivien–Lee–Bruna, COLT 2024 (generative exponent), arXiv:2403.05529 | 43 | **0** |
| † Damian et al., *The Generative Leap*, arXiv:2506.05500 | 8 | **0** |

The only crypto-labelled citer anywhere in that graph is
[SZB21](../sources/bruna-continuous-lwe.md)-adjacent work running the *opposite* direction
(CLWE ⟹ learning is hard). Two recorded false positives, so they are not re-walked: † arXiv:2310.01959
("Beyond Labeling Oracles") cites BGJ only for *"SGD learns the smoothest boundaries first"*; and the
arXiv full-text search `"information exponent" privacy` returns zero.

**The invitation.** † Song arXiv:2404.03272 §1.3.2, from inside the CLWE literature:

> *"sampling is strictly easier than L²-accurate score estimation if the criteria for evaluating sample
> quality is less stringent. This suggests exploring sampling under different evaluation criteria, such
> as 'discriminators' with bounded compute or memory."*

And the object is already chosen: **Gaussian pancakes are simultaneously SQ-hard** (DKS FOCS'17)
**and lattice-hard** (BRST'21, GVV'22) — both rungs of the τ-staircase on one distribution. This
confirms the survey's hCLWE recommendation from an independent direction.

#### 3.5 Collisions to pre-empt

- **Barak.** *Watermarks in the Sand* (Zhang–Edelman–Francati–Venturi–Ateniese–Barak, ICML 2024,
  arXiv:2311.04378) rests its central attack on the heuristic *"verification is easier than
  generation."* Any claim shaped like "detection is as hard as generation" must explain the tension
  with a paper by the most likely reviewer.
- **Kalai.** The detection ⟺ generation equivalence is his group's (§1, AMGK NeurIPS'22).
- **Ullman.** † Haghifam–Smith–Ullman is the nearest neighbour to the programme's first theorem and is
  eleven months old. If their §1.3 lower-bound technique is Ingster-style χ², it is **one step** from a
  low-degree restatement, and someone will take that step.
- **Traitor tracing** (DNRRV STOC'09, Ullman STOC'13) remains the standing obligation from the survey
  §3.6 for anything `COMP-MEM`-shaped.

### 4. Revised position

Narrower than the framing this session opened with, and better anchored for it:

> **Haghifam–Smith–Ullman proved the information-theoretic version of attacker-vs-defender sample
> complexity. The programme proves the computational version, in SGD-native units.**

This is the programme's own north star — porting the Shannon → reduction-based transition into AI —
with a *named predecessor to improve on* rather than a claim of empty space. It also resolves the
"vacuity" objection to restricted-class adversaries: the deliverable is a **separation**, not a
security bound, and a separation survives the parity/Gaussian-elimination objection that kills
"secure against SQ."

**What this buys, stated honestly:** security *margins*, not security *proofs*. Task asymmetry is not
amplifiable and has no trapdoor; nothing can be built on it. It yields a computable number — a ratio of
exponents — where crypto units yield an assumption-conditional bit. That is measurability, which was
the original ask.

---

## Implications for the Wiki

**Schedule surgery** — [summer-2026-research-programme](summer-2026-research-programme.md) needs three
edits before its own W10:

1. **W10's deliverable is aimed at a dead object.** "Instantiate `COMP-MEM` … prove one reduction
   `COMP-MEM → reference problem`" — the marginal-advantage formulation is a no-op and the game is
   Yeom's. The *reduction* survives as a fallback result (cite Yeom for the definition); the
   *definition* does not.
2. **Line 33 inverts.** "Adversary = all PPT first, the learning-shaped (SQ/low-degree) adversary as a
   Phase-2 extension" — the all-PPT lane is crowded and, per Groce–Katz–Yerukhimovich, provably barren
   in the privacy corner. Phase 2 is the thesis.
3. **Line 46 inverts.** "Build on the simplest lattice point first: `κ_inf` (black-box …)" — Song
   §1.3.3 proves black-box cannot work for this object. **Start white-box.** This also aligns with
   AIOWF as the correctly-typed primitive (survey §3.5: published weights *are* the auxiliary input)
   and with † Liu–Mazor–Pass ITCS'25 white-box learning.

**Revised read order:** † Haghifam–Smith–Ullman arXiv:2508.19458 §1.3 **first** (it decides whether
this is a thesis or a race), then † Song arXiv:2404.03272 §1.3, then Damian–Pillaud-Vivien–Lee–Bruna
COLT'24, then † Liu–Mazor–Pass ITCS'25.

**Concept pages to create** when the definitions stabilize: `native-asymmetry`, `data-knowledge-asymmetry`,
`access-asymmetry`, `generative-exponent`, `information-exponent`, `leap-complexity`. Add to the list
already standing in the summer-programme page.

**Candidate ingests surfaced here** (none currently in `raw/`): Haghifam–Smith–Ullman 2025;
Alvarez-Melis–Garg–Kalai NeurIPS'22; Song NeurIPS'24; Bogdanov–Jones–Rosen–Zadik TCC'24;
Damian–Pillaud-Vivien–Lee–Bruna COLT'24; Ben Arous–Gheissari–Jagannath JMLR'21; Głuch–Urbanke ICML'21;
Karchmer SaTML'23; Naor STOC'96.

**Verification debt.** Every † above is single-sourced from a web sweep and unread. The retraction in
§3.1 is the second time this session that a novelty claim failed on inspection — the first was
`COMP-MEM`. Treat the pattern as data about the checking procedure, not just about the claims.

---

## References

- [native-computational-problems-survey](../../output/native-computational-problems-survey.md) — the
  ~80-problem zoo this page prunes.
- [summer-2026-research-programme](summer-2026-research-programme.md) — the schedule this page amends.
- [chapter_24.md](../../output/chapter_24.md) — `κ`, the membrane, the τ-staircase.
- [ideas.md](../../output/ideas.md) — the games-not-taxonomies argument and the learning-adversary
  conjecture this page formalizes.
