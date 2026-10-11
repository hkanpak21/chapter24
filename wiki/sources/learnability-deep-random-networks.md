---
title: On the Learnability of Deep Random Networks
type: source
date_ingested: 2026-08-20
authors: [Abhimanyu Das, Sreenivas Gollapudi, Ravi Kumar, Rina Panigrahy]
venue: "SODA 2020"
venue_evidence: "dblp: conf/soda/DasG0P20, inproceedings, pp. 398-410, doi:10.1137/1.9781611975994.24 (conference title is 'On the Learnability of Random Deep Networks', same authors, same arXiv:1904.03866 preprint)"
year: 2020
tags: [statistical-query, learning-theory, complexity theory, sample-complexity, adversarial-ml]
claim_quantifier: universal
antecedent: "No complexity assumption. The lower bound is an unconditional statement about the SQ model, obtained from a correlation bound plus the standard SQ-to-weak-approximation argument (Theorem 14, imported as Theorem 31 of Blum et al.). It is conditional instead on the DATA and WEIGHT model: inputs in {±1}^n restricted to one halfspace, sgn activations, and i.i.d. Gaussian weight matrices."
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: algo class
cls_tightness: class
cls_baseline: n/a
cls_second_party: none
cls_second_notion: queries
cls_assessed: explicit
cls_evidence: "For any SQ algorithm for learning a random deep network of depth h p(n, h) \u00b7 max(r(n, h), q(n, h))\u00b2 > e^{O(h)}."
cls_evidence_src: Thm 16
cls_reason: "In this paper the SQ algorithm is the learner, not an attacker; the security reading is entirely downstream in Jagielski et al., per rule 3 and the page's own note that the bound lacks 'a second party'. party=learner, unit=algo class (SQ, the universal quantifier per Claim Boundary), tightness=class; second_notion=queries records Thm 16's paired p(n,h) query-count bound on the same party per rule 4b. baseline=n/a, no attacker success criterion in this paper."
cls_prov: S
cls_date: 2026-08-22
---

> **Provenance.** Verified against the primary PDF on 2026-08-20 (`raw/DGKP19_SQLowerBoundRandomNets.pdf`,
> extracted with `pdftotext`).

## Summary

This is reference **[27]** of [Jagielski et al.](jagielski-model-extraction.md), and the formal home of
that paper's imported `exp(O(h))` SQ lower bound for learning deep random networks. It matters here
because it is **an adversary priced in a restricted algorithm class, sitting inside a security context —
in 2019, four years before the compute-accounting literature this corpus surveys**. Not in this paper: the
paper itself has no adversary. In Jagielski et al., which imports it as Theorem 3, the SQ algorithm *is*
the model-extraction attacker, and the bound becomes a statement about what an attacker restricted to SQ
methods (which include SGD and PCA) must spend.

The technical core is a **repulsion property**. For a depth-`h` network with `sgn` activations and random
weight matrices, take two non-collinear inputs `x, y`, and let `c_i = cos θ(x^{(i)}, y^{(i)})` be the
cosine of the angle between their representations at layer `i`. The recurrence is
`E[c_i | c_{i−1}] = µ(c_{i−1})` with `µ(x) = (2/π) arcsin(x)` (Corollary 4), which follows from the
classical fact `Pr_{r∼N(0,1)^n}[sgn(x·r) ≠ sgn(y·r)] = θ(x,y)/π` (Lemma 1). Since `|µ(c)| ≤ ρ|c|` with
`ρ < 1` near zero, the angle contracts toward orthogonality geometrically: `|E[c_{d+h}]| ≤ e^{−Ω(h)} +
he^{−Ω(n)} + de^{−Ω(√n)}` (Theorem 9). Orthogonal representations mean the network's output has
exponentially small correlation with any fixed function, which is precisely what kills SQ learning.

The paper also proves a near-matching **upper** bound: the linear function
`g_{W,h}(x) = W^{(h+1)}W^{(h)}···W^{(1)}x` achieves correlation `e^{−O(h)}` with `f_{W,h,σ}` (Lemma 17),
so `e^{−O(h)}` accuracy above chance is achievable in polynomial time. The hardness is therefore tight in
the exponent, not merely a lower bound.

## Claim Boundary

- **Quantified over:** *all* SQ algorithms — that is the universal quantifier, and it is the whole point.
  The SQ model is recapped precisely: an oracle `SQ_{f,D}(ψ, r)` returns `v` with
  `|E_D[ψ(x, f(x))] − v| ≤ r`; a class is SQ-learnable if some algorithm produces an `ε`-approximation in
  time `p(n, s, 1/ε)` with query-evaluation time `q(·)` and tolerance `1/r(·)`. Lemma 13 restricts queries
  to correlational form `ψ(x, f(x)) = g(x)f(x)`, `g(x) ∈ [−1, 1]`. The target class is quantified over
  **random** networks — the bound is on the *average* over `W`, via `E_W[E_x[g(x)f_{W,h}(x)]²]`, then
  converted by Markov. So: universal over SQ algorithms, average-case over the weight distribution.
- **Antecedent:** none of the complexity kind. Instead, a specific model class and data assumption, stated
  exactly below.
- **Does not establish:** (i) hardness for non-SQ algorithms — the paper is explicit that whether these
  functions are *cryptographically* hard is open, offering only the partial evidence that outputs are
  `n^{1/4}`-way independent; (ii) hardness for trained networks — the weights are random, not learned;
  (iii) hardness for activations other than `sgn` at the level of the main theorem — `relu` and `sigmoid`
  are discussed and appear in the upper bound and in a further lemma, but the repulsion analysis is for
  `sgn` (`fW,h` abbreviates the `sgn` case); (iv) that the depth threshold is anything other than
  `ω(log n)`; (v) anything about adversaries, attacks, privacy, or extraction — the security reading is
  entirely downstream, in Jagielski et al.

- **Abstract vs theorem:** **one internal inconsistency, in the weight distribution.** The abstract says
  "all weights in the network are drawn i.i.d from a Gaussian distribution." §2 says "We assume that each
  `W_i` is an `n × n` random matrix, where each entry is chosen uniformly at random in `[0, 1]`." These
  are different models, and only the first is used: Lemma 3's proof applies Lemma 1 "to `x^{(i)}` and
  `y^{(i)}` with `W_j^{(i)}` as the random vector", and Lemma 1 is stated for `r ∈ N(0,1)^n`. The `[0,1]`
  reading is also substantively impossible — all-nonnegative weight matrices would not produce the
  repulsion property, since `sgn(W·x)` would not be sign-symmetric. **Read the §2 sentence as an
  erratum; the results are for i.i.d. Gaussian weights.** Beyond that, no abstract-vs-theorem gap: the
  abstract's "learnability … drops exponentially with its depth" is exactly Theorem 16 plus Lemma 17.

## Model class and data assumption, exactly

- **Domain**: `{±1}^n`. Each input is `±1`; the network's domain is `{±1}^n`.
- **Distribution**: the correlation bound is taken over "all the inputs `x ∈ {±}^n` that are in one
  halfspace; this ensures that no two inputs are collinear", so `N = 2^{n−1}`, with norms
  `|g|_p = E_x[|g(x)|^p]^{1/p}` over that set — i.e. uniform over a halfspace of the hypercube. This
  restriction is a technical device to exclude antipodal pairs, for which the repulsion argument fails.
- **Architecture**: depth `h > 1`; layer `i < h` computes `x^{(i+1)} = σ(W^{(i)} · x^{(i)})` with `W^{(i)}`
  an `n × n` matrix — every internal layer fully connected and of the same width as the input (the paper
  notes this equal-width assumption "is not critical … we make this for simplicity of exposition"). The
  top layer `W^{(h)}` is `1 × n`, so the output `x^{(h+1)}` is `±1`.
- **Activation**: `sgn(x) = x/|x|` for the main analysis; `relu` and `sigmoid` appear in the upper bound
  and auxiliary lemmas.
- **Weights**: i.i.d. `N(0,1)` entries (see the erratum note above).
- **Depth regime**: networks of depth `ω(log n)` are the ones argued to be beyond efficient SQ learning.

## The unnamed quantity

The compute quantity is the **SQ complexity of the learner**, and it is named and exponent-indexed:

> **Theorem 16.** "For any SQ algorithm for learning a random deep network of depth `h`
> `p(n, h) · max(r(n, h), q(n, h))² > e^{O(h)}`. In particular this means that to get accuracy that is a
> constant better than 1/2, the number of queries `p` is exponential in `h`; If the number of queries is
> `poly(h)` then the improvement over an accuracy of 1/2 is `exp(−h)`."

Two precisions worth keeping. First, the bound is on the **product** of the query count `p(n, h)` and the
square of `max(r, q)` — where `r` is the inverse tolerance and `q` the inverse accuracy gap — not on
sample count alone; the "sample lower bound" gloss used downstream compresses this. Second, the exponent
is in the **depth** `h`, not in the input dimension `n`.

What this quantity has that the PoL-lineage quantities lack: an exponent, a named algorithm class, a
matching upper bound, and no unproved conjecture between the statement and its proof. What it lacks for
security use: a second party. The SQ algorithm here is the *learner*; only when Jagielski et al. re-cast
the learner as an extraction attacker does the bound become a security statement — and there it is
imported informally, as Theorem 3, without re-deriving the model or data assumptions above.

## Key Contributions

- The repulsion property for random `sgn` networks: `E[c_i | c_{i−1}] = µ(c_{i−1})`, `µ(x) = (2/π)arcsin x`.
- **Theorem 9**: `|E[c_{d+h}]| ≤ e^{−Ω(h)} + he^{−Ω(n)} + de^{−Ω(√n)}` for non-collinear `x, y`.
- **Lemma 12**: `E_W[E_x[g(x)f_{W,h}(x)]²] ≤ |g|₂²/N + |g|₁²e^{−h}` — exponentially small statistical
  correlation with any fixed `g`.
- **Theorem 15 / Theorem 16**: the SQ lower bound, `e^{O(h)}`.
- **Lemma 17**: matching upper bound — a *linear* function achieves `e^{−O(h)}` correlation, so the
  hardness is tight.
- `n^{1/4}`-way independence of outputs of `ω(log n)`-depth random networks, offered as partial evidence
  toward a cryptographic-hardness reading (a hash-function question the paper explicitly does not settle).
- Experiments: learnability of random deep networks drops sharply with depth under state-of-the-art
  training, matching the theory qualitatively.

## Key Definitions / Theorems

- **Lemma 1**: `Pr_{r∼N(0,1)^n}[sgn(x·r) ≠ sgn(y·r)] = θ(x,y)/π`.
- **Definition 5 ((ε, d)-mixing)**: `|E[c_d(x,y)] − E[c_d(x⁰,y⁰)]| ≤ ε` for uniformly random `x⁰, y⁰`.
- **Lemmas 6, 7, 8, 10, Corollary 11**: the stochastic-recurrence analysis (`Φ` potential, geometric decay
  `Φ_{c_{i+1}} ≤ ρΦ_{c_i}`, `|E[c_i]| ≤ ρ^i`).
- **Theorem 14** (imported, "Theorem 31" of the cited Blum et al. work): SQ-learnability implies a small
  set `W_s` of weak approximators.
- **Theorem 15**: if `E_{f∈F}[E_D[g(x)f(x)]²] < ε(n,s)` then `F^s` is not SQ-learnable unless
  `p(n,s)·max(r(n,s), q(n,s))² > 1/ε(n,s)`.
- **Theorem 16**: the instantiation at `ε = e^{−O(h)}`.

## Connections

- **The formal home of Theorem 3 in [Jagielski et al.](jagielski-model-extraction.md)** — that paper's
  `exp(O(h))` SQ bound for fidelity extraction of deep random networks, attributed there to "A. Das,
  S. Gollapudi, R. Kumar, R. Panigrahy, 'On the learnability of deep random networks', CoRR
  abs/1904.03866, 2019 (reference [27])". Anything the wiki says about that theorem's scope should be
  checked against the model class and data assumption stated above.
- Concepts: [Statistical Query Model](../concepts/statistical-query-model.md),
  [PAC Learning](../concepts/pac-learning.md), [Model Extraction](../concepts/model-extraction.md).
- **Contrast with the SETH line.** [Fine-Grained ERM](fine-grained-erm.md) and
  [Fine-Grained Gradient for LLMs](fine-grained-gradient-llm.md) bound *all* algorithms, conditionally, in
  worst case; this bounds *one class* of algorithms, unconditionally, on average over the weight
  distribution. Both price a learner's computation; only this one has been carried into a security paper.
  See [Fine-Grained Complexity of Learning](../concepts/fine-grained-complexity-of-learning.md).
- Related class-restricted-adversary work in the wiki: [Covert Learning](covert-learning.md),
  [low-degree polynomial framework](../concepts/low-degree-polynomial-framework.md).
- The depth threshold `ω(log n)` and the open cryptographic-hardness question sit next to
  [One-Way Functions](../concepts/one-way-functions.md).

## Open Questions / Limitations

- **Stated by the paper:** are deep random networks *cryptographically* hard to learn — are they hash
  functions? The `n^{1/4}`-way independence result is offered as evidence, not an answer.
- The §2 weight-distribution sentence contradicts the abstract and the proofs (see Claim Boundary).
- `sgn` activations for the main analysis; the extension to `relu`/`sigmoid` is partial.
- Random, not trained, weights — the gap between this and any statement about deployed models.
- SQ only. Gradient descent is SQ-expressible, but a real attacker need not be.

## Quotes / Notable Passages

> "The learnability of a random deep network with sgn activations drops exponentially with its depth."

> "Outputs of random networks of ω(log n)-depth are n^{1/4}-way independent."
