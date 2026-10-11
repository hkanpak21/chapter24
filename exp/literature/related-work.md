# The Problem Zoo: Every Candidate Reference Problem for a Computational Security Theory of Learning

*Survey date: 2026-07-10. Companion to
[intro-computational-security-of-learning.md](intro-computational-security-of-learning.md) and the
[summer-2026 programme](../wiki/analyses/summer-2026-research-programme.md).*

**Question.** Given where ML/DL actually is in 2026, what is the *native computational problem* to
build the theory on — the reference hard problem at the far end of the `COMP-MEM` / `COMP-TW` /
crown-jewel reductions? Before committing, this survey catalogues **every established problem
language in the field**, what each one buys, and how natively each fits the programme.

**Provenance & epistemic status.** Compiled from (a) a full sweep of this wiki's sources, (b) a
multi-agent web literature sweep (lenses: planted-graph canon, spiked/continuous models,
crypto-from-learning, hardness-of-learning-NNs, meta-complexity), and (c) maintainer knowledge for
lenses the sweep did not complete (privacy-native, verification, watermarking — marked ◊). The
adversarial fact-check pass was cut short by a session rate limit: entries dated **2025–2026 that are
not in the wiki are marked †** (single-sourced from the web sweep; verify before citing in anything
that leaves this repo). Everything else is either wiki-grounded or classical.

---

## 0. Verdict first

There is no single problem that is simultaneously (i) crypto-grade hard, (ii) native to continuous
SGD-trained learning, and (iii) rich enough to route every `COMP-TW` game. But the zoo has a clear
shape, and four problems stand out as the working set:

1. **CLWE / hCLWE (Gaussian pancakes)** — *the working native problem.* The only continuous,
   one-natural-distribution problem with worst-case cryptographic backing (lattices), and the anchor
   of essentially every completed crypto↔ML security reduction of the last five years (undetectable
   backdoors, hardness of learning shallow nets, GMM density estimation, score estimation). If the W10
   deliverable ("prove one reduction `COMP-MEM` → reference problem") gets one target, it should be
   hCLWE.
2. **PC_ρ (secret-leakage planted clique)** — *the reduction engine.* Not DL-native as an instance,
   but the root of the only mature average-case reduction web reaching structurally diverse learning
   targets, now crypto-usable (PKE from standard PC, GHJS25). Its leakage parameter ρ is literally the
   `κ₀`/side-information knob of `COMP-MEM`.
3. **Gap-K^t over samplable distributions** — *the native metric and the frontier.* Liu–Pass/IRS:
   OWFs exist iff mildly-hard-on-average; over samplable distributions the problem *is* "compress a
   sample from the training distribution" — the `Kt`-on-`U` theory's own problem, and the canonical
   far end for the crown-jewel threshold reduction.
4. **Traitor tracing ◊** — *the incumbent for the privacy corner specifically.* The one classical
   crypto object whose security game already *is* membership inference; the DP-hardness literature
   (DNRRV09, Ullman13) is the closest existing "COMP-MEM-shaped theorem" and must be engaged before
   claiming novelty.

Phase-2 (the learning-shaped adversary) has its own native language: **information/generative
exponents and leap complexity** on single/multi-index models — SGD-native thresholds, restricted-class
hardness, exactly the "learning adversary" of `ideas.md`.

The rest of this document is the full zoo, so this shortlist is auditable.

---

## 1. What "native" must mean for this programme

Distilled from the workflow's criteria extraction over `chapter_24.md`, the intro doc, the summer
programme, `ideas.md`, and `LEARNING_aioracles.md` (19 raw criteria, condensed):

1. **Average-case on a structured-but-natural distribution** — the instance must be a source family
   `Π` expressible as a `U`-program on a uniform seed; "natural distribution with hidden structure."
2. **Decision/distinguishing form with a samplable public null model** — so `COMP-MEM`'s
   `κ₀`-baseline and marginal advantage `Adv(κ) − Adv(κ₀)` are definable.
3. **Unconditional SQ floor** — a statistical-dimension lower bound with no assumptions (the bottom
   rung of the τ-staircase must be free).
4. **Conjectured hard against ALL PPT**, not merely SQ/low-degree — the parity/Gaussian-elimination
   caveat; the programme secures against all PPT first.
5. **Root of a reduction web** — hardness must be routable to structurally different targets
   (Kt/Φ-additive reductions in the machine model's own morphism language).
6. **κ-graded hardness** — a hardness surface in `(s, t, |w|, ε)` budget space with thresholds, not a
   single hard/easy bit; measurable in the Bellare–Rogaway concrete-security style ("break in time t,
   advantage ε ⟹ solve reference problem in t′≈t, ε′≈ε").
7. **Crypto-usable in reverse** — hard instances should *build* primitives (BFKL test): evidence the
   hardness is genuinely cryptographic, not an artifact of restricted models.
8. **Locatable on the four-rung provability ladder** — unconditional (SQ) → idealized-model →
   standard-assumption (OWF/K^t) → open (Gap-K^t); ideally spanning several rungs.
9. **Connects to Kt/meta-complexity** — the security frontier should be statable as resource-bounded
   incompressibility, so the keystone theorem and the native metric bite.
10. **Meaningful where search is super-exponential and objectives tolerate approximation** — the
    `ideas.md` "learning adversary" requirement: the problem must not collapse when the adversary is
    allowed approximation.

Reading key for every entry below: **Statement** (what the problem is), **Hardness** (why believed
hard), **Web** (what reduces to/from it), **Native?** (honest DL-nativeness), **Fit** (role in this
programme).

---

## 2. Map of the zoo

| Tier | Role | Members |
|---|---|---|
| I | Reduction-grade reference problems (crypto-usable far ends) | LWE, CLWE/hCLWE, LWR, LPN + variants, noisy k-LIN, local PRGs, PC → PC_ρ → planted-subgraph → PKE, Gap-K^t family, white-box learning, traitor tracing ◊, generic primitives (OWF…iO) |
| II | Hardness-of-learning theorems (the learning side of reductions) | Kearns–Valiant, Klivans–Sherstov/Tiegel, Daniely lines, SZB/CGKM/LZZ shallow-net line, agnostic single neuron, GMM/pancakes, score estimation, universal extrapolation, NP-hardness of ERM |
| III | Stat-comp gap witnesses (τ-staircase material) | sparse PCA, spiked Wigner/Wishart, planted submatrix, tensor PCA, NGCA, SBM, trees, coloring, matching, hypergraph PC, sparse regression, robust estimation, planted sparse vector, single/multi-index exponents |
| IV | Evidence languages (restricted-model, not endpoints) | SQ/SDA, low-degree, SoS, Franz–Parisi, OGP, SGD-as-SQ |
| V | The cautionary shelf | LLL vs noiseless (ZSWB22), Holmgren–Wein, quasi-poly LD refuted †, easy expanders †, group testing (no gap), CSQ ≠ SQ, batch-reuse escapes |

---

## 3. Tier I — Reduction-grade reference problems

These are the problems a security reduction can legitimately *end* at: each supports (or is) a
cryptographic primitive.

### 3.1 The lattice / continuous stack — the working native problem

**Worst-case lattice problems (GapSVP / SIVP).**
Statement: decide whether a lattice's shortest vector is below/above a threshold (approximation
factor poly(n)); worst-case, no distribution. Hardness: decades of stagnation; exponential-time best
algorithms at poly factors; survives quantum scrutiny at LWE-relevant factors. Web: reduce TO LWE
(Regev, quantum; Peikert/BLPRS classical) and TO CLWE (BRST21). Native? None — pure geometry. Fit:
the **gold-standard epistemic floor**: "attack success ⟹ worst-case lattice breakthrough" is the
strongest sentence available to any security theory today.

**LWE (Learning With Errors).** *(wiki: learning-with-errors.md, bruna-continuous-lwe.md)*
Statement: from samples `(a, ⟨a,s⟩ + e mod q)`, a uniform, e discrete-Gaussian, recover s or
distinguish from uniform; search ≡ decision. Literally supervised learning of a mod-q linear function
from noisy examples. Hardness: worst-case reductions (quantum: Regev 2005; classical: Peikert 2009,
BLPRS 2013); 20 years of cryptanalysis; NIST-standardized. Web: FROM worst-case lattices; TO —
CLWE (equivalence, GVV22), GMM density estimation, Massart/agnostic halfspaces (DKMR22),
one-hidden-layer ReLU (LZZ25†), intersections of halfspaces (Klivans–Sherstov via uSVP), FHE/ABE/iO
components. Native? Middling: a *learning problem* by birth (descendant of BFKL's OWF-from-learning),
but over ℤ_q with uniform inputs. Fit: the backbone; everything continuous routes through it.

**CLWE (Continuous LWE).** *(wiki: continuous-lwe.md, bruna-continuous-lwe.md)*
Statement: samples `(y, z)` with `y ~ N(0, I_d)`, `z = γ⟨y,w⟩ + e mod 1`, secret unit direction w,
Gaussian noise e; distinguish from (Gaussian, independent uniform) or recover w. Hard for
`γ ≥ 2√d`. Hardness: quantum worst-case lattice reduction (BRST21, STOC 2021); **classically
equivalent to LWE** (Gupte–Vafa–Vaikuntanathan, FOCS 2022) — inherits the entire lattice confidence
base. Unconditional SQ lower bounds for the homogeneous variant. Web: FROM lattices/LWE; TO —
learning single periodic neurons (SZB21), noise-free two-hidden-layer ReLU nets (CGKM22),
one-hidden-layer ReLU with inverse-poly noise (LZZ25†), GMM density estimation without separation
(BRST21/GVV22), L2-accurate score estimation (Song, NeurIPS 2024), white-box undetectable backdoors
in random-Fourier-feature models (GKVZ22). Native? **The most DL-native crypto assumption known**:
continuous inputs, the canonical benign distribution (standard Gaussian), real labels,
single-index geometry. Residual contrivance: the hidden √d-frequency periodic signal is a designed
artifact no natural dataset exhibits. Fit: **primary recommendation** — see §9.

**hCLWE (Gaussian pancakes).**
Statement: distinguish `N(0, I_d)` from a Gaussian conditioned to concentrate near equally spaced
hyperplanes orthogonal to a secret direction w (spacing ~1/γ, width ~β/γ). The distribution-only,
null-vs-planted form of CLWE — an NGCA instance with crypto-grade hardness. Hardness: FROM CLWE;
unconditional exponential SQ bounds (DKS17-style, proved in BRST21). Statistically detectable with
few samples, computationally indistinguishable — a genuine stat-comp gap over ℝ^d. **Noise caveat:**
the exactly-noiseless version is solved by LLL at the information-theoretic optimum (ZSWB22) — noise
is the load-bearing parameter. Web: TO — GMM hardness (pancake mixtures *are* GMMs), GKVZ22
backdoors, score-estimation hardness; reportedly also a backdoored-DP construction ("Gaussian
Pancake Mechanism," 2025†). Native? The purest instance of "one continuous distribution that looks
Gaussian to every efficient observer." Fit: **the template for `COMP-MEM` hard instances** — the
secret planted in a natural-looking source, with hardness inherited from lattices and an
unconditional SQ floor. Spans three rungs of the provability ladder in one object.

**LWR (Learning With Rounding).**
Statement: LWE with deterministic quantization instead of noise: `(a, ⌊⟨a,s⟩⌉_p)`. Hardness: from
LWE for super-poly modulus ratio (BPR12); poly-modulus regimes partially open (a CRYPTO 2023 lower
bound shows current techniques can't close it). Web: TO lattice PRFs, Saber KEM. Native? Modest —
but note: **deployed inference APIs are deterministic and quantized**; a `COMP-MEM` game where the
adversary sees noise-free quantized model outputs has exactly LWR's shape. Fit: niche but pointed —
the derandomized-oracle corner of the κ lattice.

### 3.2 The planted-graph stack — the reduction engine

**Planted Clique (PC).** *(wiki: planted-clique.md + 8 source pages)*
Statement: distinguish `G(n,1/2)` from `G(n,1/2)` + k-clique; search and refutation variants
**provably equivalent** to decision (Hirahara–Shimizu, STOC 2024). Statistically solvable at
k ≥ (2+ε)log n; conjectured PPT-hard for k = o(√n). Hardness: SQ lower bound n^Ω(log n) (FGRVX17),
nearly tight SoS bound (BHKKMP16), low-degree bounds, 30+ years unbroken. Web: root of the entire
stat-comp reduction web (via PC_ρ); TO cryptography — clique-hiding (Juels–Peinado 2000), PSM +
secret sharing (ABIKN23), **PKE from standard PC + noisy k-LIN** (GHJS25, STOC 2025). Native? Low:
discrete graph, no continuous data, no SGD. Its virtue is one clean average-case distribution ideal
for reductions. Fit: the sharpest known threshold phenomenon (k crossing √n) and, since 2025, a
certified crypto-grade assumption. One of the two W10 targets.

**PC_ρ (Secret-Leakage Planted Clique).** *(wiki: secret-leakage-planted-clique.md)*
Statement: PC with the clique's vertex set drawn from a chosen prior ρ (k-partite, bipartite,
hypergraph…), leaking controlled side information. Hardness: calibrated against PC + LD/SQ bounds
per variant. Web: the workhorse — TO robust sparse mean estimation, sparse PCA (negatively
correlated), mixtures of sparse regressions, tensor PCA (via k-HPC^s), dense SBM below
Kesten–Stigum, planted submatrix, detection-recovery/refutation gaps for PDS (Bresler–Jiang 2023).
Native? Instance: low. Structure: **high** — the leakage prior ρ is exactly the shape of
"adversary holds correlated side information about the secret training set," i.e. the `κ₀` baseline
and auxiliary-data membership inference. Fit: the machinery for routing one `COMP-TW` game to many
targets; the programme's designated bridge corpus.

**Planted Dense Subgraph (PDS).** Statement: detect/recover/refute a k-vertex denser-than-background
subgraph. The cleanest worked example of **task-separated thresholds**: regimes where detection is
easy but recovery and refutation are hard (Bresler–Jiang 2023, Schramm–Wein 2022). Fit: the direct
formal template for the τ-staircase's `τ_detect < τ_recover` rung — "detect the backdoor" vs
"recover the trigger" vs "certify cleanliness" at provably different thresholds.

**Planted Subgraph Conjectures / Planted Random Subgraph (crypto form).** Statement: distinguish a
random graph from one with a planted copy of a larger structure; ABIKN23/GHJS25 formulate variants
whose breaking is *equivalent by direct reduction* to breaking PSM/secret-sharing/PKE in the
public-information model. Fit: proof-of-concept that a stat-comp-gap problem can underwrite full
cryptographic functionality — the structural precedent `COMP-MEM` needs. Low-degree security
analysis exists (eprint 2024/1497†).

**Hypergraph PC / Planted Dense Subhypergraph.** Statement: hypergraph analogue; detection threshold
open (Luo–Zhang, COLT 2020). Web: the ABW10 route to **hardness of learning DNFs**; feeds tensor
PCA. Fit: the planted-graph family's only direct handle on learning a natural function class.

**SBM (Stochastic Block Model).** *(wiki: stochastic-block-model.md, kesten-stigum-threshold.md)*
Statement: recover/detect hidden communities; Kesten–Stigum threshold marks the efficient-algorithm
boundary; below KS but above the IT threshold detection is conjectured hard (proven IT-vs-KS gap for
≥4 symmetric communities). New†: the extended low-degree conjecture implies sharp recovery lower
bounds below KS (Ding–Hua–Slot–Steurer 2025). Hardness: LD/SQ/BP-landscape evidence; dense-regime
reductions from k-PC (Brennan–Bresler Thm 3.2). Native? Moderate for graph ML — belief propagation
is essentially a GNN — weak for mainstream DL. Fit: the sharpest "past this parameter the task flips"
statement in the zoo; a `COMP-MEM`-shaped claim about *subpopulation* membership signal.

**Broadcasting on Trees / Tree Reconstruction.** Statement: does the leaf configuration retain
information about the root as depth grows; KS bound `dλ² > 1`. Underlies SBM via the local weak
limit; low-degree hardness below KS (Huang–Mossel 2024†). Fit: the cleanest information-vs-computation
phase boundary; a stylized model of signal propagation through depth.

**Planted Coloring / Quiet Planting.** Statement: plant a proper q-coloring so the planted ensemble
is statistically近 indistinguishable from the uniform random graph below a threshold
(Krzakala–Zdeborová 2009). Fit: **quiet planting is the combinatorial definition of an undetectable
backdoor/watermark** — a secret embedded so the surrounding distribution is unchanged. Conceptually
important even if the instance is far from DL.

**Planted Matching.** Statement: recover a hidden perfect matching from two weight distributions;
sharp infinite-order phase transition. Fit: the native problem of **de-anonymization / record
linkage** — the privacy game where the secret is a linkage, not a membership bit.

**Group Testing.** Statement: recover k planted defectives from pooled tests. **Anti-example**: in
the standard regime there is essentially *no* stat-comp gap (efficient designs meet the IT bound);
conjectured hardness only for restricted algorithm classes. Fit: the cautionary entry — not every
planted-recovery task supports a threshold reduction; a `COMP-MEM` instantiation must check its
target actually has a gap.

### 3.3 The coding / CSP stack — Boolean crypto-from-learning

**LPN (Learning Parity with Noise).** Statement: recover s from `(a, ⟨a,s⟩ ⊕ e)`, e ~ Bern(η);
equivalently decode a random binary linear code / PAC-learn parities under uniform with
classification noise. Hardness: best algorithm 2^{O(n/log n)} (BKW03); 30+ years; unconditional SQ
bounds; post-quantum. Web: **BFKL 1993 — the founding learning→crypto reduction** (OWFs, PRGs,
private-key encryption from LPN); sub-exponentially, CRH and PKE (Yu–Zhang); LPN over F_p is an iO
ingredient (JLS21); learning juntas/DNFs reduces to noisy parity (FGKP06). Native? Low as an
instance; canonical as a *concept* — the standard example that classification noise + a trivial
concept class already generates cryptography, and the standard hard case for feature learning.
**The SQ-vs-PPT caveat lives here**: noiseless parity is SQ-hard yet Gaussian-elimination-easy.
Fit: the historical template of the whole programme; its parameter dials (noise, samples) prototype
threshold statements.

**Alekhnovich LPN (noise 1/√n).** Statement: LPN at low noise with O(n) samples. Hardness: 20+
years; partial worst-case support emerging†. Web: the first **PKE from a pure noisy-learning
assumption** (FOCS 2003); IND-CCA variants; oblivious transfer. Fit: marks the noise threshold at
which a learning problem's hardness becomes *public-key-grade* — a genuinely κ-graded phenomenon.

**Sparse LPN / noisy k-XOR.** Statement: LPN with k-sparse sample vectors; hard up to
m ~ n^{(1−δ)k/2} samples, refutable beyond. Hardness: SoS refutation lower bounds (Grigoriev,
Schoenebeck, KMOW17). Web: TO — ABW10-style PKE, somewhat-homomorphic encryption (CGHKV
EUROCRYPT 2025†), iO components (RVV TCC 2024†), lossy trapdoor functions (Dao–Jain CRYPTO 2024†).
Native? Low, but its **explicit sample-vs-hardness threshold is the cleanest model of "security
decays as the adversary sees more data"** — exactly `COMP-MEM`'s advantage-vs-budget curve. Fit:
high structural relevance despite Boolean substrate.

**Noisy k-LIN over expanders (+ DUE).** Statement: noisy XOR constraints on a *fixed public*
expander graph; distinguish from random labels. Web: PKE from 3-LIN + DUE (ABW10); the auxiliary
assumption in GHJS25's PKE-from-PC. **2026 caveat†:** near-optimal lossless expanders exist on which
noisy k-XOR is poly-time solvable (Reed–Muller decoding) — expansion alone does not imply hardness.
Fit: composability lesson (mild assumptions assemble into PKE) + a standing warning about conjecture
hygiene.

**Goldreich local PRGs / random local functions.** Statement: fix predicate P and a random/expanding
hypergraph; `f(x)_j = P(x|_{S_j})`; OWF at m = n, PRG at polynomial stretch. Hardness: 25 years for
good predicates; resists linear/algebraic/myopic/SoS attacks. Web: pillar of iO (JLS21);
constant-overhead MPC; **Daniely–Vardi COLT 2021: local-PRG security ⟹ hardness of learning shallow
ReLU networks under Gaussian marginals, ω(1)-term DNFs, DFAs, depth-3 circuits** — extended to the
smoothed-analysis regime (DSV NeurIPS 2023). Native? The assumption is Boolean; the *conclusions*
are among the most DL-native available without lattices. Fit: the main non-lattice route to
hardness-of-learning-networks; "computable in constant depth, unlearnable by everyone."

**Random CSP refutation / Feige's hypothesis / planted CSPs.** Statement: (refutation) certify
unsatisfiability of random k-CSPs below density n^{k/2} — conjectured hard (Feige 2002 for 3-SAT);
(planted) distinguish planted-satisfiable from random (SQ lower bounds: Feldman–Perkins–Vempala,
STOC 2015). Web: the **Daniely–Linial–Shalev-Shwartz machine**: refutation hardness ⟹ hardness of
improper learning of DNFs, ω(log n)-halfspace intersections, agnostic halfspaces/conjunctions, and
depth-2 networks *with random natural weights* (Daniely–Vardi NeurIPS 2020). One early over-strong
variant was refuted and replaced — a useful precedent for assumption discipline. Native? Inputs
Boolean/adversarial; conclusions DL-adjacent. Fit: the alternative non-lattice hardness family;
lacks planted-secret/trapdoor structure, so better for unlearnability claims than for
membership/backdoor games.

### 3.4 Meta-complexity — the native metric

This family is where the programme's `Kt`-on-`U` theory already lives; these problems are not just
*available* anchors but the same objects the keystone theorem is about.

**Gap-K^t / MINKT (average-case).** Statement: given x, t, s: decide K^t(x) ≤ s (gap version:
distinguish from K^{poly(t)}(x) > s + ω(log n)); security-relevant form: approximate K^t on random x.
Hardness: **Liu–Pass FOCS 2020: OWFs exist ⟺ K^t is mildly hard-on-average** — every private-key
primitive witnesses its hardness; Hirahara FOCS 2018: worst-case-to-average-case reduction for
GapMINKT. Web: every OWF-based primitive reduces to average-case K^t computation; average-case
easiness yields agnostic learning of P/poly over samplable distributions (Hirahara–Nanashima,
Goldberg–Kabanets). Native? Instances are random strings — but the *quantity* is the programme's
capacity measure. Fit: **the canonical far end for `COMP-MEM`**: an ε-advantage membership adversary
is a distinguisher, hence (Liu–Pass) an average-case K^t approximator, hence an OWF inverter. OP1
(robust comp-stat gap) already reduces to average-case Gap-K^t in the dialogue.

**Gap-K over samplable distributions (IRS).** Statement: for a samplable D, approximate K(x) (or
K^t, pK^t) on x ~ D to within O(log n), on most samples. Hardness: **equivalent to OWFs even for
time-unbounded K** (Ilango–Ren–Santhanam STOC 2022; Liu–Pass CRYPTO 2023 for pK^t). Native? **The
most DL-native meta-complexity form**: one fixed samplable data distribution, average-case success,
approximation tolerated — "LLMs are compressors of the data distribution," formalized. Fit: `COMP-MEM`
stated over the actual training distribution maps here directly; this is the version of the native
metric to build on.

**pK^t (probabilistic K^t).** The randomized-compressor variant; optimal coding theorem
unconditional (LOZ22); OWF characterizations without derandomization hypotheses. Fit: technically
the right measure when the adversary/compressor is randomized — i.e., always; choosing pK^t makes
threshold reductions unconditional rather than modulo derandomization.

**Average-case Symmetry of Information (HILNO).** Statement: does K^t(x,y) = K^t(x) + K^t(y|x) ±
O(log) hold on average over samplable pair distributions? **Duality (STOC 2023): OWFs exist ⟺
average-case time-bounded SoI fails somewhere.** Fit: membership inference *is* a conditional-
compression question ("does the model compress this point abnormally well given the rest?") — this
duality is the meta-complexity statement of `COMP-MEM`'s possibility/impossibility boundary.

**dK^t / NP-hardness of meta-complexity (Hirahara STOC 2023).** Statement: OWFs exist ⟺ NP ⊄ BPP
AND computing distributional Kolmogorov complexity is NP-hard (under randomized reductions). Fit:
the dream form — one meta-computational NP-hardness statement would put `COMP-MEM` security on
**worst-case NP footing**. The open hypothesis to watch, not to assume.

**Boundary-MINKT / computational depth (Liu–Pass 2024–2026†).** Worst-case hardness of deciding
K^t-randomness at the boundary characterizes OWFs under derandomization assumptions. Fit: removes
every average-case caveat from the reference problem — furthest rung, active frontier.

**MKtP (Levin Kt).** R_Kt is EXP-complete under P/poly-tt reductions; **EXP ≠ BPP ⟺ Kt mildly
hard-on-average (Liu–Pass CRYPTO 2021)**. Fit: the absolute floor — if MKtP is average-case easy,
EXP = BPP and no computational security exists for anything. Threshold reductions bottom out here.

**MCSP / GapMCSP.** Statement: given a truth table, decide if a circuit of size ≤ s computes it.
Hardness: MCSP ∈ BPP would invert every OWF (Kabanets–Cai via Razborov–Rudich); NP-hardness open
(with known barriers); NP-hard restrictions (DNF, depth-d formulas — Masek, Ilango, HOS). Web: SZK ≤
BPP^MCSP; natural properties ⟹ learning (CIKK16). Native? The exact Boolean idealization of **model
distillation/extraction**: "find the smallest network reproducing this behavior." Fit: the
hardness-of-auditing template (below).

**Partial-function MCSP / NP-hardness of learning programs (Hirahara FOCS 2022).** Statement: find a
small circuit/program consistent with labeled examples — Occam/MDL learning. **NP-hard under
randomized reductions** (resolving Ko 1991). Fit: unconditional NP-hardness for *proper*
model-recovery/extraction attacks and compression-based dataset auditing. The most training-shaped
classical meta-problem ("smallest model consistent with the training set").

**CMMSA / Sharp Pessiland (Hirahara–Nanashima 2026†).** Statement: the approximation factor for
MDL-style agnostic program learning at which "average-case NP hardness ⟹ OWFs" becomes an
equivalence — the first sharp characterization of whether Pessiland can exist. Fit: quantifies
exactly the missing link between hard-on-average data and cryptographic-grade `COMP-MEM` security.
Frontier; watch.

**White-box Learning Problem (Liu–Mazor–Pass, ITCS 2025†).** Statement: given the *code* of a
sampler producing `(y, f(y)+e)` for poly-size f, output a circuit approximating f — worst-case over
"computationally shallow" samplers; generalizes LWE from linear f to arbitrary f. Hardness: **the
first problem whose worst-case hardness characterizes PKE** (both directions); the black-box variant
characterizes OWFs. Native? Strikingly close to ML security practice: *the adversary holds the
released model's code/weights and must learn the underlying function*. Fit: suggests `COMP-MEM` with
published weights sits between black-box (OWF-grade) and white-box (PKE-grade) hardness — a built-in
threshold hierarchy for model-release policies, in exactly the machine model's idiom. Deserves a
deep read.

**Natural Properties (Razborov–Rudich) as a learning resource.** Statement: no natural property
against P/poly ⟺ exponentially-hard PRFs in the class; any natural property against C yields
learning algorithms for C (CIKK16). Fit: the meta-complexity root of undetectable-backdoor results —
**any generic "detect hidden structure in a model" auditor is simultaneously a learner and a
PRF-breaker**. The hardness-of-auditing template behind GKVZ22 and its LLM successors.

**Universal Extrapolation (Impagliazzo–Levin 1990; Hirahara–Nanashima FOCS 2023).** Statement: given
a prefix of a samplable source's output, sample the continuation correctly — for *every* samplable
source. **Possible ⟺ OWFs do not exist.** Native? Maximal: this is *generic next-token prediction
of efficiently generated data* — the LLM pretraining objective as a complexity-theoretic object.
Fit: the cleanest dichotomy for the programme: either a universal LLM-style predictor exists and all
private-key crypto (hence all `COMP-MEM` protection) fails, or there exist samplable sources on
which every efficient predictor fails. The crown jewel's "threshold" is a refinement of this
dichotomy.

**Average-case NP / DistNP (Pessiland-level).** Statement: samplable SAT distributions hard to solve
on average — weaker than OWFs. Fit: **the provable minimum price**: GJMM20 Thm 18 shows any
computational>IT robustness gap already implies this; HN23 shows hardness of learning itself needs
OWFs. Fixes the logical floor of the whole programme.

**Quantum GapK / one-way puzzles (2024–2025†).** The same characterization paradigm for quantum
samplers. Fit: evidence the meta-complexity reference language is *sampler-model-agnostic* — the
"approximate K over the data source" problem calibrates security for any source class, plausibly
including an SGD-restricted sampler class tailored to the programme.

### 3.5 Generic primitives — the assumption ladder

Not "problems" but the currency the ladder is priced in; listed for completeness because several ML
security results consume them directly.

- **OWF** — the floor. Robust-learning hardness ⟺ OWF (DNV19 + BLPR19 dual); no-OWF ⟹ universal
  extrapolation ⟹ learning is easy (HN23). Every `COMP-MEM` claim implicitly ends here at minimum.
- **PRG / PRF (incl. puncturable)** — plant secrets in labels/functions: BLPR19 hard robust
  learning; CHLX25 non-defendability of poly-size circuits (puncturable PRF + iO); natural-proofs
  barrier. *(wiki: pseudorandomness.md, backdoor-defense-learnability-obfuscation.md)*
- **Digital signatures (EUF-CMA)** — the most reduction-ready primitive in ML security: GJMM20
  computational robustness (tamper-detection wrapper), GKVZ22 non-replicable backdoors, watermark /
  model-authentication constructions (NCM25). The intro doc's "EUF-CMA-analogue generator" for the
  integrity pillar will be built from these.
- **PKE (generic)** — BGGKRR25 Thm 3: filter impossibility with *no shared secret* (attacker knows
  only the public key); now constructible from planted clique (GHJS25) — so LLM-filter impossibility
  can in principle be anchored in a planted-graph problem.
- **Time-lock puzzles** — fine-grained *sequential-time* hardness: BGGKRR25 Thm 1's
  filter-weaker-than-model separation. The only entry expressing the monitor-compute vs model-compute
  asymmetry — an axis polynomial reductions cannot see.
- **iO** — the maximal adversary: undetectable backdoors in obfuscated networks (KKO+24),
  unelicitable backdoors (DGM+24). Prefer OWF-based results; use iO to mark the ceiling.
- **AIOWF (auxiliary-input OWFs)** — hard for every inverter on infinitely many public indices;
  non-heurPAC-learnability ⟺ AIOWFs (Nanashima COLT 2021). Fit: **the right primitive for white-box
  games** — the published weights are the auxiliary input; "white-box membership inference implies
  inverting an AIOWF" is the naturally-typed reduction.

### 3.6 Privacy-native: traitor tracing & adaptive data analysis ◊

*(Added from maintainer knowledge — the sweep lens for this family did not complete. Verify
citations before external use, though these are classical results.)*

**Traitor tracing ⟹ hardness of private query release.** Dwork–Naor–Reingold–Rothblum–Vadhan
(STOC 2009): traitor-tracing schemes imply that no efficient differentially-private mechanism can
answer large families of counting queries accurately — the first *computational* separation between
efficient and inefficient DP. Ullman (STOC 2013): assuming OWFs, answering ~n² adaptively chosen
statistical queries privately and accurately is hard. Kowalczyk–Malkin–Ullman–Wichs: stronger
separations from iO. The IT-side companion: **fingerprinting codes** (Bun–Ullman–Vadhan 2014) give
the *statistical* lower bounds — and modern membership-inference attacks on models are literally
fingerprinting/tracing attacks (Dwork et al. 2015 "robust traceability").

**Adaptive data analysis hardness.** Hardt–Ullman (FOCS 2014), Steinke–Ullman: answering n²⁺ᵒ⁽¹⁾
adaptive queries is computationally hard via traitor tracing — the interactive version of the same
phenomenon.

Fit: **this is the incumbent problem language for `COMP-MEM` specifically.** The traitor-tracing
security game — a coalition of key-holders produces a decoder; the tracer must identify a member —
is membership inference with the quantifiers rearranged: tracing possible = membership inference
*unavoidable*; DP possible = membership inference *preventable*. The programme's privacy corner must
either reduce to / from traitor tracing or explain precisely why `COMP-MEM`'s marginal-advantage
formulation escapes this classical box. This is both a threat (novelty check) and a gift (a ready
crypto object of exactly the right shape).

### 3.7 Verification-native ◊

**PAC verification (Goldwasser–Rothblum–Shafer–Yehudayoff, ITCS 2021).** Interactive proofs for
verifying that a learner's output is approximately optimal, with the verifier using *fewer
samples/resources than learning requires*. Not a hardness assumption but the framework in which
"certifying a model property is cheaper than producing it" becomes formal — the natural home for
OP2 (backdoor-freedom not self-certifiable) and the AIOracle `(T, r_judge)` interface. ZKML
constructions (BLW25, wiki) consume standard SNARK assumptions. **Watermarking**: Christ–Gunn–Zamir
undetectable watermarks for LMs rest on OWF/PRF — same Tier-3.5 currency.

---

## 4. Tier II — Hardness-of-learning theorems

The learning-side halves of completed reductions: what the reference problems above have already
been *cashed into*. These define the proof patterns the programme will imitate.

- **Kearns–Valiant 1989/94**: weak PAC learning of poly-size formulae / DFAs / constant-depth
  threshold circuits ⟸ inverting RSA / QR / factoring Blum integers. Representation-independent;
  the founding template ("the planted secret is the decryption key"). Kharitonov 1993:
  distribution-specific (uniform) hardness from BBS.
- **Klivans–Sherstov FOCS 2006 (+ Tiegel COLT 2024†)**: PAC learning intersections of n^ε halfspaces
  breaks uSVP/Regev PKE; Tiegel: already ω(log log N) halfspaces, via **parallel-pancake
  distributions** — tying the classic Boolean result into the continuous CLWE line.
- **Daniely et al. (refutation) & Daniely–Vardi (local PRGs)**: hardness of improper learning of
  DNFs, halfspace intersections, depth-2/3 ReLU nets — under Gaussian marginals and smoothed
  parameters in the strongest versions. The two non-lattice pillars.
- **The CLWE line**: SZB21 (single periodic neuron, Gaussian inputs, any inverse-poly noise; SGD
  provably stalls at the predicted frequency; noiseless case LLL-easy — **the cleanest existing
  threshold reduction in the zoo**); CGKM22 (noise-free two-hidden-layer ReLU: unconditional SQ +
  LWE-hardness); LZZ ALT 2025† (one hidden layer, inverse-poly noise — minimal depth at which
  crypto-grade Gaussian-marginal hardness is known). Open flank: noise-free one-hidden-layer.
- **Agnostic single ReLU / halfspace under Gaussian**: SQ lower bounds (GGK20, DKZ20);
  crypto-confirmed by Tiegel COLT 2023 (from worst-case lattice problems, improper, OPT + o(1)).
  The poisoning-native base case: adversarial label corruption *is* the agnostic model.
- **GMM / parallel pancakes**: d^Ω(k) SQ (DKS17); density estimation without separation is
  LWE-hard (BRST21/GVV22); quasi-poly algorithms & matching SQ bounds once weights aren't tiny
  (Buhai–Steurer COLT 2023†). The most natural-looking hard family (embedding spaces are
  mixture-like), with the caveat that hard instances are measure-zero moment-matched corners.
- **Score estimation (Song, NeurIPS 2024)**: L2-accurate score estimation of Gaussian pancakes
  solves hCLWE — poly sample complexity, crypto-hard computation; via "sampling is as easy as
  learning the score" (Chen et al., ICLR 2023), *generative capability itself is gated by a lattice
  assumption*. Template for "the model cannot have learned X unless it breaks Y."
- **Universal extrapolation** (see §3.4) — the generative/LLM face of the same coin.
- **NP-hardness of training (Blum–Rivest; GKMR ITCS 2021; ∃ℝ-completeness)**: worst-case ERM
  hardness. Mostly a *delimiting* result: proper-ERM formalizations are the wrong substrate for
  security definitions (no average case, no secret, no indistinguishability). Useful to cite when
  explaining why the machine model quantifies over sources, not datasets.

---

## 5. Tier III — Statistical-computational gap witnesses

The τ-staircase's raw material: problems where `τ_stat < τ_comp` is either proven (restricted
models) or reduction-supported. Each entry: where the gap sits, and its role.

- **Sparse PCA (Berthet–Rigollet 2013)** — the founding reduction-based gap: detect a k-sparse
  spike in covariance; statistical at n ~ k log d/θ², computational at n ~ k²/θ². 13 years
  unbroken; PC/PC_ρ-reducible; **already load-bearing in ML security: GKVZ22's white-box backdoor
  detection reduces to sparse PCA.** The spike is structurally "the secret training influence on
  second moments."
- **Spiked Wigner/Wishart (sub-BBP)** — weak detection below the BBP spectral threshold is literally
  an advantage-ε indistinguishability statement; for unstructured priors the barrier is partly
  *statistical* (contiguity), so computational reference use needs structured (sparse) priors. DL
  hook†: one gradient step on a two-layer net provably creates a rank-one spiked feature matrix
  (Ba–Erdoğdu et al. 2022) — BBP calibrates when feature learning becomes *detectable*.
- **Planted submatrix (Schramm–Wein 2022)** — first low-degree *estimation* (MMSE) lower bounds;
  detection-vs-recovery separation over continuous data; the "localize the influence, not just
  detect it" game.
- **Tensor PCA (Richard–Montanari 2014)** — the reference hardness for "SGD must climb a high-order
  saddle": detection at λ ~ d^{p/4} vs statistical d^{1/2}; SoS/LD/SQ/Langevin-failure evidence +
  PC_ρ reduction; single-index SGD dynamics with information exponent p mirror tensor-PCA power
  iteration. Models higher-moment watermarks/dataset signatures.
- **NGCA (non-Gaussian component analysis)** — **the universal SQ-hardness engine** (DKS17): one
  non-Gaussian direction hidden in Gaussian noise, SQ complexity d^Ω(m) for m matched moments;
  embeds into GMMs, robust estimation, halfspaces, ReLU nets, list-decodable estimation. With A =
  noisy discrete Gaussian, **NGCA *is* hCLWE** — the exact point where SQ evidence upgrades to
  cryptographic reduction. Structurally the most DL-native hard template (single-index geometry).
  Noiseless variants LLL-fragile.
- **Single-index models: information exponent (BGJ21) / generative exponent (DPVLB COLT 2024)** —
  quantitative time-to-learn thresholds for the exact algorithm class used in practice: online SGD
  needs n ~ d^{k−1}, CSQ d^{k/2}, SQ/LD d^{k*/2}. **The Phase-2 native language** — hardness for the
  learning-shaped adversary, with the standing caveat that batch reuse provably escapes CSQ
  (Dandi et al. ICML 2024†; Lee–Oko–Suzuki–Wu†) — "SGD hardness" classes are brittle under
  algorithmic tweaks, which is precisely why the programme pays for crypto reductions first.
- **Multi-index / leap complexity (Abbe–Boix-Adsera–Misiakiewicz COLT 2022/23)** — merged-staircase
  necessity for O(d)-sample online SGD; leap exponent conjecturally governs d^Θ(Leap) scaling;
  sequential feature emergence matches observed saddle-to-saddle dynamics. Defines which composite
  secrets SGD-class extraction can reach — capability-emergence thresholds in the programme's idiom.
- **Sparse linear regression (hard regime)** — LD bounds via Franz–Parisi (BAHSWZ NeurIPS 2022);
  the most supervised-learning-shaped of the planted continuous problems.
- **Mixtures of sparse regressions / robust sparse regression** — Brennan–Bresler universality for
  sparse mixtures; supervised, continuous.
- **Robust sparse mean estimation** — the k-to-k² gap from k-BPC; **the task *is* a poisoning
  defense**, so its computational threshold is itself a security threshold. Dense case is easy
  (DKKLMS16) — sparsity isolated as the hardness source; defense-optimality anchored to SSE
  (Hopkins 2019, worst-case!).
- **Robust Gaussian estimation gaps** — error floor Θ(ε√log(1/ε)) for efficient algorithms vs O(ε)
  statistical; NGCA-embedded instances; the price-of-efficient-defense literature. 2026 caveat†:
  low-degree method mispredicts robust subspace recovery — evidence types disagree at the edges.
- **Planted sparse vector in a subspace** — geometry of weight-space watermarks/backdoor directions;
  LD/SQ bounds at the ρ²d² threshold, **but LLL recovers integral planted vectors regardless**
  (ZSWB22) — restricted-class hardness bypassed by algebraic adversaries.
- **Planted hypercube vector / noiseless clustering** — the canonical **anti-anchor**: SoS and LD
  lower bounds both active, yet LLL solves it at the IT optimum. High data-nativeness is exactly
  what makes it the critical warning.
- **SBM below KS / broadcasting on trees / planted coloring / planted matching / hypergraph PC /
  PDS / group testing** — see §3.2; they live on both lists (crypto stack roots and staircase
  witnesses).

---

## 6. Tier IV — Evidence languages (not reduction endpoints)

The programme's Obligation-5 material: these certify *where thresholds sit* but cannot carry a
security claim alone.

- **SQ / statistical dimension (SDA)** — unconditional within the model; captures most practical
  learners including (approximately) minibatch SGD; the τ-staircase's assumption-free floor.
  Blind spot: algebraic algorithms (parity, LLL). Almost equivalent to LD under niceness (BBHLS21).
- **Low-degree polynomial method** — the threshold-locator: candidate `COMP-MEM` "past this point"
  parameters will be read off LD calculations, then upgraded to reductions. Failure modes are now
  well-mapped: Holmgren–Wein counterexamples (ITCS 2021), **the quasi-polynomial-time version is
  false** (Buhai–Hsieh–Jain–Kothari 2025†), noiseless/algebraic evasions (ZSWB22). Restricted to
  "structureless" problems; treat as scaffolding.
- **SoS lower bounds** — strongest single restricted-model evidence (pseudo-calibration); dominates
  the convex-relaxation attack class; same noiseless caveat.
- **Franz–Parisi criterion** — physics free-energy barrier ⟺ LD for Gaussian additive models
  (BAHSWZ22); generates LD bounds otherwise hard to derive; implies local-MCMC hardness.
  Model-dependent validity.
- **OGP (overlap gap property)** — *proven* landscape property (not conjecture) for p-spin and
  sparse MIS; yields unconditional lower bounds for stable algorithms: low-degree polynomials,
  bounded-time Langevin dynamics, and **poly-size circuits of depth < log n/(2 log log n)** —
  genuine circuit lower bounds from landscape geometry. The nearest existing tool for "no SGD-like
  algorithm can find X"; defender-side impossibility (a defense requiring optimization past an OGP
  barrier is unimplementable by gradient methods).
- **SGD-as-SQ / cross-predictability (Shamir 2018; Abbe–Sandon)** — GD with bounded precision/noise
  is SQ-simulable, so SQ-hard families bind it; single-sample SGD can formally exceed SQ only via
  unnatural architectures. Calibrates exactly when "SQ-secure" claims bind real training — and when
  they don't (sample reuse, high-precision gradients).

These six are the languages in which the **learning-shaped adversary** (Phase 2) will be defined —
they are κ-restrictions, not assumptions.

---

## 7. The cautionary shelf

Every failure mode the catalogue surfaced, collected — each one is a constraint on how the theory
may argue:

1. **Noise is load-bearing (ZSWB22).** Noiseless hCLWE / planted hypercube / planted sparse vector /
   parity are all solved by algebraic methods (LLL, Gaussian elimination) *while SQ, SoS, and LD
   lower bounds remain formally true*. A `COMP-MEM` reference problem must carry noise or a genuine
   crypto reduction. Restricted-model floors are floors, not walls.
2. **The low-degree conjecture has false regimes** (Holmgren–Wein; quasi-poly version refuted
   2025†). LD is a threshold-locator, never a security foundation.
3. **Structural assumptions can collapse** — easy lossless expanders break noisy k-XOR on specific
   graphs (2026†); an early Daniely assumption was refuted and replaced. Assumption hygiene: prefer
   problems with worst-case backing or decades of cryptanalysis.
4. **Not every planted problem has a gap** (group testing) — check the gap exists before
   instantiating a game on a target.
5. **Restricted-class hardness is brittle under algorithmic tweaks** — batch reuse escapes CSQ
   bounds; single-sample SGD formally exceeds SQ. Phase-2 claims need their adversary class defined
   with care (this is the `ideas.md` point about approximation + super-exponential search).
6. **Evidence frameworks disagree at the edges** (FP vs LD counterexamples; LD mispredicts robust
   subspace recovery†). Where physics and TCS criteria agree, confidence is high; where they
   diverge, neither is authority.
7. **Worst-case ERM hardness (Blum–Rivest) is the wrong substrate** — no distribution, no secret, no
   game. The machine model's insistence on sources `Π` is vindicated here.

---

## 8. Fitness matrix

Scoring the leading candidates against the distilled criteria (§1). ✓ = satisfies, ~ = partial,
✗ = fails. Columns: (1) natural-distribution average-case, (2) samplable null / game-ready,
(3) unconditional SQ floor, (4) all-PPT hardness (not just SQ), (5) reduction web,
(6) κ-graded/concrete-security measurable, (7) crypto-usable in reverse, (8) provability-ladder
span, (9) Kt/meta-complexity connection, (10) DL-nativeness of the instance.

| Candidate | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **hCLWE / CLWE** | ✓ | ✓ | ✓ | ✓ (lattice worst-case) | ✓ (rich, growing) | ✓ (γ, β, samples) | ✓ (is lattice crypto) | ✓ (3 rungs) | ~ | **High** |
| **PC / PC_ρ** | ~ (graph) | ✓ | ✓ (FGRVX17) | ✓ (conjecture, 30 yr) | ✓✓ (the web) | ✓ (k vs √n) | ✓ (PKE, GHJS25) | ✓ (3 rungs) | ~ | Low |
| **LWE** | ~ | ✓ | ✓ | ✓ (worst-case) | ✓ | ✓ | ✓✓ | ✓ | ~ | Mid |
| **LPN / sparse LPN** | ~ | ✓ | ✓ | ✓ (30 yr) | ✓ | ✓✓ (sample thresholds) | ✓ (BFKL, PKE) | ✓ | ~ | Low |
| **Local PRGs / CSP refutation** | ~ | ✓ | ✓ | ✓ (25 yr) | ✓ (DV21 net hardness) | ~ | ✓ (iO pillar) | ~ | ✗ | Low-mid (conclusions high) |
| **Gap-K^t (samplable)** | ✓ (any samplable D) | ✓ | ✗ (n/a) | ✓ (⟺ OWF) | ✓ (all of Minicrypt) | ✓ (t, gap, fraction) | ✓ (is Minicrypt) | ✓ (spans to worst-case frontier) | ✓✓ (is the metric) | Mid (discrete, but the *task* is compression) |
| **NGCA** | ✓ | ✓ | ✓✓ (universal engine) | ✗ alone (✓ via hCLWE) | ✓ (embeds everywhere) | ✓ (m moments) | ✗ alone | ~ (2 rungs) | ✗ | **High** |
| **Traitor tracing ◊** | ✗ (constructed) | ✓✓ (is a game) | ✗ | ✓ (from OWF/iO) | ✓ (DP hardness corpus) | ✓ | ✓ (is crypto) | ✓ | ✗ | Low (but the *game* is COMP-MEM) |
| **Single/multi-index exponents** | ✓✓ | ✓ | ✓ (CSQ/SQ) | ✗ (restricted class) | ~ | ✓✓ (exponents) | ✗ | ✗ (1 rung) | ✗ | **Maximal** |
| **White-box learning (LMP25†)** | ~ | ✓ | ✗ | ✓ (⟺ PKE) | new | ~ | ✓✓ | ✓ (worst-case!) | ✓ (Kt-depth condition) | Mid-high (released-code setting) |

---

## 9. Recommendation

**Work on the hCLWE/CLWE stack as the native problem, with three satellites.**

1. **`COMP-MEM` → hCLWE first (the W10 deliverable).** Concretely: instantiate the source `Π` as a
   pancake-planted family where the secret Δ (one training example / a backdoor batch) perturbs the
   hidden direction or spacing; show an ε-advantage `κ_inf` distinguisher yields an hCLWE
   distinguisher with `t′ ≈ t, ε′ ≈ ε` (concrete-security bookkeeping); the SQ floor of the same
   statement is free from BRST21's SQ bounds. This one theorem exercises the whole machine: the
   membrane (sample access), κ₀ (the null is the public prior), the staircase (SQ rung unconditional,
   PPT rung lattice-priced), and the Bellare–Rogaway style. GKVZ22 already did the backdoor
   (`COMP-TW`, Δ = insertion) version — the membership (Δ = one example) version appears open, which
   makes it a genuine target rather than a re-derivation. *(Before claiming it: check against the
   traitor-tracing/DP-hardness corpus, §3.6 — the nearest prior art, in a different formalism.)*
2. **PC_ρ as the routing engine.** When a `COMP-TW` instance doesn't look Gaussian (graphs, discrete
   features, subpopulations), route through the Brennan–Bresler web instead of forcing pancakes; the
   leakage prior ρ is the formal home of auxiliary-information adversaries. PC's own PKE upgrade
   (GHJS25) means even this combinatorial branch now ends at cryptographic functionality.
3. **Gap-K^t (samplable) as the theory's own idiom.** State the general threshold theorems —
   crown jewel included — against average-case K^t/pK^t over the training source, via Liu–Pass /
   IRS / HILNO. The keystone already lives in this language; the SoI duality is `COMP-MEM`'s
   possibility boundary; OP1 already reduces here. This is where the *native theory* (as opposed to
   the native worked example) should live. Read Liu–Mazor–Pass white-box learning† early — it may be
   the closest existing object to the machine model's "learning a source from its code" and to a
   principled white-box/black-box κ split (PKE-grade vs OWF-grade).
4. **Exponents/leap as the Phase-2 adversary language, not as security.** Information/generative
   exponents and leap complexity give the *learning-shaped* thresholds — quantitative, SGD-native,
   experimentally checkable (they connect to the comp-stat envelope prediction). Use them to define
   the restricted adversary class and to place thresholds; never as the sole basis of a security
   claim (cautionary shelf, items 1 and 5).

What this survey changes about the standing plan: nothing structural — it *confirms* the W10 choice
(planted-clique or cLWE) and resolves it in favor of **cLWE/hCLWE as primary, PC_ρ as machinery** —
but it adds two obligations the plan didn't have: (a) engage traitor tracing before publishing
anything `COMP-MEM`-shaped, and (b) adopt the samplable-distribution meta-complexity form (IRS/pK^t)
rather than plain K^t when formalizing the native metric, because that variant is both stronger
(OWF-equivalent even time-unbounded) and more source-native.

---

## 10. Gaps in this survey & how to finish

- **Lenses that did not run** (rate-limited): privacy-native (§3.6 filled by maintainer ◊),
  interactive-verification (§3.7 stub ◊), model-security constructions (largely covered via wiki
  Tier-3.5 entries), optimization-landscape (covered via wiki + spiked lens), distribution-learning
  (partially covered), 2023–2026 position papers (partially covered via the exponent entries).
  Missing entirely: a dedicated sweep of **fine-grained/SETH-style hardness for transformer
  primitives** (Alman–Song attention lower bounds and successors) — likely Tier-IV-adjacent for this
  programme, but should be catalogued for completeness.
- **Verification pass did not run**: all † entries are single-sourced. The wiki-grounded and
  classical entries (the large majority) are safe.
- The workflow is resumable (cached) to finish the missing lenses + verification:
  `Workflow({scriptPath: ".../native-problem-survey-wf_33b4e64c-8c7.js", resumeFromRunId: "wf_33b4e64c-8c7"})`
  after the session limit resets.
- **Candidate wiki ingests surfaced by this survey** (not currently in `raw/`): Liu–Pass 2020 (OWF ⟺
  K^t), Ilango–Ren–Santhanam 2022, HILNO 2023 (SoI duality), Hirahara 2022 (NP-hardness of learning
  programs), Liu–Mazor–Pass 2025 (white-box learning), DNRRV 2009 + Ullman 2013 (traitor tracing /
  DP hardness), Song 2024 (score estimation), DPVLB 2024 (generative exponent), GVV 2022 (CLWE ≡
  LWE), Tiegel 2023/24, Daniely–Vardi 2021.
