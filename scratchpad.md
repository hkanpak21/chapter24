# PAC Learning — Core Definitions

## Halfspace

A halfspace in $\mathbb{R}^n$ is the set of all points on one side of a hyperplane.
The classifier is defined by a weight vector $w \in \mathbb{R}^n$:

$$c_w(x) = \text{sign}(\langle w, x \rangle)$$

Everything where the dot product $\langle w, x \rangle > 0$ gets label 1, everything
negative gets label 0. The hyperplane $\{x : \langle w, x \rangle = 0\}$ is the
decision boundary. In 2D it is a line; in 3D a plane; in $\mathbb{R}^n$ a hyperplane
dividing the space into two half-regions.

---


## Concepts and Concept Classes

The input space $\mathcal{X}$ is the set of all possible inputs — for example $\{0,1\}^n$ or $\mathbb{R}^n$.

A **concept** is a function $c : \mathcal{X} \to \{0, 1\}$ that assigns a label to every input. It represents the ground truth — the true rule nature uses to classify things. You do not choose it; it exists and you are trying to recover it from examples.

A **concept class** $\mathcal{C}$ is a set of such functions:

$$\mathcal{C} \subseteq \{0,1\}^{\mathcal{X}}$$

It encodes your assumption about what form the ground truth takes. When you say "I am learning halfspaces," you mean the true labeling function is assumed to be some halfspace, so $c \in \mathcal{C}$ where $\mathcal{C}$ is the class of all halfspaces.

---

## Hypothesis Classes

A **hypothesis** is also a function $h : \mathcal{X} \to \{0, 1\}$, but it is the learner's output — its best guess at the true concept after seeing training data.

A **hypothesis class** $\mathcal{H}$ is the set of functions the learner is allowed to output. It is the search space of the algorithm.

The distinction:

| | Who owns it | What it represents |
|---|---|---|
| Concept $c$ | Nature | Ground truth |
| Concept class $\mathcal{C}$ | The problem | Set of possible ground truths |
| Hypothesis $h$ | The learner | The learner's guess |
| Hypothesis class $\mathcal{H}$ | The algorithm | The learner's search space |

**Proper learning**: the learner is restricted to $\mathcal{H} = \mathcal{C}$. It must output something from the same class as the ground truth.

**Improper learning**: the learner may use $\mathcal{H} \supsetneq \mathcal{C}$. It can output any function, even one outside the concept class. This strictly more powerful — Montasser-Hanneke-Srebro showed robust PAC learning sometimes requires improper learners.

---

## PAC Learning (Valiant 1984)

A **sample** is a sequence of labeled examples:

$$S = ((x_1, c(x_1)),\, \ldots,\, (x_m, c(x_m)))$$

where each $x_i$ is drawn i.i.d. from some distribution $D$ over $\mathcal{X}$, and $c \in \mathcal{C}$ is the (unknown) true concept.

The **risk** of a hypothesis $h$ with respect to concept $c$ under distribution $D$ is:

$$\text{Risk}(h, c, D) = \Pr_{x \sim D}[h(x) \neq c(x)]$$

This is the probability that $h$ disagrees with the ground truth on a fresh random input.

A learning algorithm $L$ is said to **PAC learn** $\mathcal{C}$ if: for all $\varepsilon, \delta \in (0,1)$, all distributions $D$, and all concepts $c \in \mathcal{C}$, there exists a sample size $m(\varepsilon, \delta)$ such that when $L$ is given $m$ i.i.d. labeled samples from $(D, c)$, with probability at least $1 - \delta$ over the draw of the samples, it outputs $h$ satisfying:

$$\text{Risk}(h, c, D) \leq \varepsilon$$

The two parameters:
- $\varepsilon$ — accuracy: how wrong the learner's output is allowed to be
- $\delta$ — confidence: how often the learner is allowed to fail

The sample complexity $m(\varepsilon, \delta)$ is the number of examples needed to achieve accuracy $\varepsilon$ with confidence $1 - \delta$. If $m$ is polynomial in $1/\varepsilon$, $1/\delta$, and the problem dimension $n$, the class is **efficiently PAC learnable**.

---

## Realizability

A problem is **realizable** if the true concept is guaranteed to be in the hypothesis class:

$$c \in \mathcal{H}$$

This means a perfect hypothesis (risk zero) exists somewhere in the learner's search space. In the realizable setting, empirical risk minimization (find the $h \in \mathcal{H}$ that makes the fewest mistakes on the training set) is a natural and often sufficient strategy.

In the **agnostic** setting there is no such guarantee — the best hypothesis in $\mathcal{H}$ may still have nonzero risk. Agnostic learning is strictly harder.

DMM19 works in the realizable setting: $c \in \mathcal{C} \subseteq \mathcal{H}$. The lower bounds are therefore stronger — even under this favorable assumption, robust PAC learning requires exponentially many samples.

---

## Adversarial PAC Learning

Standard PAC learning measures risk on clean inputs. **Adversarially robust PAC learning** changes the risk to account for an adversary who perturbs test inputs:

$$\text{AdvRisk}_b(h, c, D) = \Pr_{x \sim D}\!\left[\exists\, \tilde{x} \text{ with } d(x, \tilde{x}) \leq b : h(\tilde{x}) \neq c(\tilde{x})\right]$$

The adversary is allowed to move any test input $x$ by at most $b$ under metric $d$, trying to find a nearby $\tilde{x}$ that $h$ misclassifies (using the true label of $\tilde{x}$, not of $x$ — this is the error-region definition from DMM19).

The goal of the robust learner is the same — output $h$ with $\text{AdvRisk}_b(h,c,D) \leq \varepsilon$ — but the sample complexity $m(\varepsilon, \delta, b, n)$ may now depend on the perturbation budget $b$ as well. DMM19's main result is that for natural concept classes and distributions, this sample complexity jumps from polynomial (no adversary) to exponential (sublinear $b$).

---

# GJMM20 — The Construction Where Computational Hardness Helps

## The Setup

Start with any learning problem Q that has the following property:

- h_Q is a classifier with small standard risk α (it is accurate)
- But an adversary can find adversarial examples for h_Q with probability β >> α
  under the l_0 norm (changing few coordinates)

Q is information-theoretically vulnerable. The construction produces a *related*
problem P with a classifier h_P that a poly-time adversary cannot attack, but an
unbounded adversary still can.

---

## The Wrapping Construction (Technique Section 1.1.1)

The idea is to attach a **digital signature** to every input instance.

A digital signature scheme has two keys:
- sk  — signing key, kept secret
- vk  — verification key, made public

The security guarantee: a poly-time adversary who knows vk cannot produce a
valid signature on a message it has not seen signed before, even if it has seen
many other message-signature pairs. This is the standard unforgeability assumption,
which follows from one-way functions existing.

**How the new distribution D_P is built:**

Sample (x, y) from D_Q. Generate a fresh key pair (vk_x, sk_x) for each sample.
Attach to x a short signature:

    sigma_x = Sign(sk_x, x)

Also attach vk_x, encoded with error-correcting codes. The new instance is:

    x_bar = (x, sigma_x, [vk_x])

where [vk_x] denotes the error-corrected encoding of vk_x. The label y is unchanged.

**How h_P classifies:**

Given input x_bar = (x, sigma, [vk]):

    1. Verify: is sigma a valid signature of x under vk?
    2. If NO  → output ★  (tamper detected, refuse to classify)
    3. If YES → output h_Q(x)

The ★ symbol means "I detect something is wrong." Outputting ★ on a clean input
counts as an error, so the construction has to ensure ★ is rare on honest inputs.
On honest inputs the signature always verifies, so h_P agrees with h_Q and has
standard risk α.

---

## Why a Poly-Time Adversary Cannot Attack h_P

To attack h_P near x_bar = (x, sigma_x, [vk_x]), the adversary must produce
x_bar' = (x', sigma', [vk']) that is close in Hamming distance to x_bar and
causes h_P to misclassify *without* outputting ★.

There are only two strategies:

**Strategy I — find a new signature for the same x:**
Produce sigma' ≠ sigma_x that is still a valid signature of x under vk_x.
This is signature forgery. A poly-time adversary cannot do this.

**Strategy II — perturb x to x', forge a signature for x':**
Find x' close to x, then produce a valid (x', sigma') pair under vk_x.
This is also forgery — signing a new message the adversary has not queried.
A poly-time adversary cannot do this either.

**Strategy III — perturb vk_x to some vk' for which adversary knows sk':**
If the adversary could change vk_x to a vk' it controls, it could sign x' itself.
But vk_x is encoded with error-correcting codes [vk_x] that require Ω(|x|) bit
changes to decode to any different key. That is too many perturbations — it takes
the adversary outside the allowed budget b.

So a poly-time adversary is stuck. The computational risk of h_P is at most α.

---

## Why an Unbounded Adversary CAN Still Attack h_P

An unbounded adversary proceeds in two steps:

    1. Find x' close to x such that h_Q(x') ≠ y.
       This is possible with probability β >> α because Q is vulnerable.

    2. Forge a valid signature sigma' for x' under vk_x using exhaustive search.
       An unbounded adversary can brute-force this.

    3. Output x_bar' = (x', sigma', [vk_x]).

The signature is short — poly-log length — so attaching a new forged signature is
a small perturbation. The total distance from x_bar to x_bar' is dominated by the
distance from x to x', which is small by assumption.

Result: the information-theoretic risk of h_P is approximately β >> α.

---

## The Gap

    Computational risk of h_P   ≈  α   (small, bounded by signature security)
    IT risk of h_P               ≈  β   (large, inherited from Q's vulnerability)

This is a strict separation: a computationally bounded adversary cannot attack h_P,
but a computationally unbounded one can. The gap β - α is large by construction.

The hardness assumption doing the work: **one-way functions exist** (needed to build
the signature scheme). If OWFs do not exist, no such separation is possible.

---

## The Reverse Direction

GJMM20 also proves the converse: if *any* such computational robustness gap exists
— meaning there is a classifier with computational risk α < information-theoretic
risk β — then **NP is average-case hard**.

Specifically: one can efficiently sample satisfiable Boolean formulas from a
distribution S such that no efficient algorithm can find satisfying assignments
with non-negligible probability. This is hard-on-average SAT.

So the result is fully bidirectional:

    OWFs exist  ⟹  computational robustness gaps exist  (Theorem 8)
    Comp. robustness gaps exist  ⟹  average-case NP is hard  (Theorem 18)

Cryptographic hardness and computational robustness are equivalent phenomena.

