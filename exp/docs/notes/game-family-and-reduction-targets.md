# The Game Family and Its Reduction Targets

*Working draft, 2026-07-26. Companion to [chapter_24.md](chapter_24.md) and
[native-computational-problems-survey.md](native-computational-problems-survey.md).*

The discipline this document follows was fixed in discussion: **games first, adversary class second.**
A game is not typed until four things are pinned. The adversary's class is deliberately *not* one of
them — it enters at reduction time, because the reduction determines which reference problem's
thresholds apply.

---

## 1. The schema

```
GAME[ O , T , S , κ₀ ]

  O   observation map   — exactly what the adversary receives, and at which phase
  T   target            — what it must produce
  S   success functional — bit-valued, or real-valued (a distance)
  κ₀  baseline          — what public knowledge alone achieves on S
```

**Advantage depends on the type of `S`, and this is not cosmetic.**

- `S` bit-valued: `Adv(κ) = Pr[win | κ] − 1/2`. Baseline subtraction is a **no-op** here, because an
  adversary holding only the public prior guesses at one half. This is the defect that killed
  `COMP-MEM`'s marginal-advantage formulation.
- `S` real-valued: `Adv(κ) = E[S | κ₀] − E[S | κ]`. Baseline subtraction is **meaningful** here — the
  prior-only adversary achieves finite nonzero error `ε₀`, and the gain over it is exactly what the
  released artifact leaked.

So the `COMP-TW` schema is alive for reconstruction and property inference and dead for membership.
Point it at the former.

## 2. Three maps, never conflated

Every game must state which map its adversary inverts. These get confused because all three are
"inverting something in a neural network."

| Map | Inverting it means | Fixed / random |
|---|---|---|
| **Training** `D ↦ w` | recover training data from weights | randomized (seed, batch order) |
| **Parameterization** `w ↦ M_w` | decide functional equivalence | deterministic; NP-hard (Jagielski et al.) |
| **Feature** `x ↦ f_θ(x)`, `θ` fixed | recover an input from activations or gradients | deterministic, differentiable |

The feature map is by far the best-behaved: no training randomness to quantify away, an explicit
differentiable map, and a fiber that is a level set with a generic dimension.

## 3. The games

### G1 — Inference-time data inference

| | |
|---|---|
| `O` | model outputs, or intermediate activations, on a query `x` |
| `T` | something about `x` itself |
| `S` | distance (reconstruction) or bit (property) |
| `κ₀` | the input prior |
| **Map** | **feature** |

The adversary learns about *the data being evaluated*, not about training data. This is the game the
deployment-time threat model actually needs and the one the literature addresses least.

### G2 — Training inference from gradients

| | |
|---|---|
| `O` | gradients — leaked, federated, or split |
| `T` | the batch that produced them, or which model is being trained |
| `S` | distance for the batch; bit for the model identity |
| `κ₀` | the data prior; the public model zoo |
| **Map** | **feature** (the gradient map at fixed `θ`) — *not* the training map |

The most tractable game in the family, for a structural reason: for linear and logistic models,
gradient equality is an **affine condition on the batch**, and the admissibility constraint is a **box**
(pixel range, one-hot labels). Affine plus box is a lattice problem, which is why Li et al. reached for
Nguyen–Stern and why Suliman et al.'s conjecture became plausible only after the constraint was imposed.

### G3 — Membership

| | |
|---|---|
| `O` | `w` (white-box) or query access (black-box) |
| `T` | a bit: was `x` in `D` |
| `S` | **bit** |
| `κ₀` | one half — hence **use raw advantage, not marginal** |
| **Map** | **training** |

### G4 — Reconstruction from weights

| | |
|---|---|
| `O` | `w`, plus side information `σ` |
| `T` | a training example |
| `S` | distance |
| `κ₀` | prior mean or a generic sample — **nonzero, so the schema works here** |
| **Map** | **training** |

Highest value, hardest. The training map is randomized and has no calibrated reference problem
attached. This is where Suliman's conjecture lives if lifted from one step to the full map.

### G5 — Property inference

| | |
|---|---|
| `O` | `w` or query access |
| `T` | a functional of `D` — subgroup fraction, distributional property |
| `S` | value (real) or bit |
| `κ₀` | the property's prior |
| **Map** | **training** |

Estimation of a functional of the training distribution. Structurally the closest to the spiked-model
literature, and therefore the easiest to supply with calibrated thresholds.

## 4. Reduction targets

The reference problem supplies the units. **The leakage amount and the reference instance's signal
parameter are the same number** — that is what makes the statement measurable rather than stipulated.

The right corpus is the **calibrated stat-comp-gap witnesses** — the survey's Tier III — because those
are the problems whose thresholds are known in *both* the statistical and the computational regime.
Tier I (LWE, planted clique) gives crypto-grade hardness but not calibrated learning thresholds.

| Game | Structure of the inversion | Candidate reference | Signal parameter |
|---|---|---|---|
| G1 | recover `x` from a compressed nonlinear observation | NGCA; single-index recovery | conditioning / compression at the observation |
| G2, linear or logistic | affine condition + box constraint | **lattice / Hidden Subset Sum** | noise level; dimension-to-samples ratio |
| G2, ReLU | union of polyhedra indexed by sign patterns | combinatorial; no calibrated target yet | number of active patterns |
| G3 | detect a one-record perturbation | spiked models; Haghifam–Smith–Ullman for the IT version | `ρ`, the noise scale |
| G4 | invert a randomized many-to-one map | **none calibrated** — the gap | — |
| G5 | estimate a planted functional | sparse PCA; spiked Wigner/Wishart; planted submatrix | spike strength `λ` |

**The prediction to test first.** In the G2-linear cell with *no* noise, LLL should win — the survey's
cautionary shelf item 1 says noise is load-bearing, and ZSWB22 shows lattice methods solve noiseless
planted problems at the information-theoretic optimum while SQ, SoS and low-degree lower bounds remain
formally true. So Suliman's conjecture is probably **false as stated for exact gradient matching** and
true only once noise, quantization, or step-compounding enters. Locating that boundary is the theorem.

## 5. What is decidable now, and what is not

**Decidable with existing tools:** G2-linear. The map is explicit, the constraint is a box, the
reference problem is identified, and the first experiment is a lattice attack on the smallest instance.
Either it breaks a published conjecture or it locates the boundary. Both are results.

**Needs the composition law:** G2 across many steps, and G4. One step's inversion cost does not
determine `T` steps' cost — each step loses information (helping the defender) but adds an equation
(helping the attacker), and which effect dominates is unwritten. Proof-of-Learning's checkpoint
structure is an attempt to exploit the second effect; both published breaks of it argue the exposure
helps the attacker more.

**Needs a calibrated reference that does not exist:** G4. This is the honest gap, and it is why G4 is
the goal rather than the starting point.

## 6. What is borrowed, and from whom

Stated plainly so nothing here reads as a claim it is not.

- The **gap `δ`** as a security parameter is fine-grained cryptography — Brzuska–Couteau Def. 6;
  LaVigne–Lincoln–Vassilevska Williams Def. 5; Ball–Rosen–Sabin–Vasudevan Def. 2. Write it as an
  exponent, `adversary ≥ honest^{1+δ}`, never as a constant. Ceiling: Merkle's quadratic gap is optimal
  in the random oracle model (Barak–Mahmoody).
- **Size versus navigability** of a solution set, with a complexity separation, is Dinur–Nissim PODS'03.
- A **computational security notion for reconstruction**, equivalent to one-wayness, is Cohen et al.
  ITCS'25 Def. C.1.
- **Restricting the adversary's function class** in a privacy definition is capacity-bounded DP
  (Chaudhuri–Imola–Machanavajjhala, NeurIPS'19).
- The **conjecture** in the G2 cell is Suliman et al., USENIX Security 2025.

What is not borrowed: the typing discipline above, the three-map separation, and — if it survives — a
hardness theorem at a stated `δ` for a specific cell of §4.

**The contribution has to be the theorem.** Definitions in this area are commodities.
