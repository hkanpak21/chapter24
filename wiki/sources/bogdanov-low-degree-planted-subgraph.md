---
title: Low-Degree Security of the Planted Random Subgraph Problem
type: source
date_ingested: 2026-07-26
authors: [Andrej Bogdanov, Chris Jones, Alon Rosen, Ilias Zadik]
venue: "venue unconfirmed from PDF. The ingested file is arXiv:2409.16227v1, 24 September 2024, and states no venue. Author affiliations on the file are University of Ottawa, Bocconi University, Reichman University, and Yale University."
year: 2024
tags: [cryptography, planted-clique, statistical-query, computational-indistinguishability, hardness-reductions]
claim_quantifier: existential
antecedent: "Theorem 2.1 is unconditional and needs no antecedent beyond its three parameter conditions on k, the leakage number l, and the degree D. The cryptographic applications in Section 4 are conditional twice over. They assume (s, epsilon)-indistinguishability of the planted and null distributions, and that assumption is supplied by Conjecture 1.4, which is a polynomial-time indistinguishability conjecture and is not proved."
adversary_bound: "two different bounds sit in the same paper and must not be conflated. Theorem 2.1 bounds the adversary by ALGEBRAIC DEGREE, namely an arbitrary real polynomial of degree at most D in the hyperedge indicators, which may arbitrarily preprocess H and knows the leaked set L. The security statements of Section 4, Propositions 4.1 and 4.3, bound the adversary by CIRCUIT SIZE s, and their hypothesis is delivered by Conjecture 1.4, which quantifies over polynomial-time distinguishers. The low-degree theorem is evidence for that conjecture, not the adversary class of the security reductions."
algorithm_class: "degree-D real polynomials in the hyperedge indicator variables, measured by the degree-D likelihood ratio LR_D, with advantage normalised by the standard deviation under the null. Degree D is offered as a proxy for n^{O(D)}-time computation. The paper is explicit that the proxy is imperfect here."
date_verified: 2026-08-22
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: attacker
cls_unit: circuit size
cls_tightness: budget
cls_baseline: n/a
cls_second_party: circuit size
cls_second_notion: algo class
cls_assessed: explicit
cls_evidence: "Assume (H, ℙ_{H,L}) and (H, ℚ_{H,L}) are (s, ε)-indistinguishable for all L ⊆ V(H) with |L| = ℓ."
cls_evidence_src: Prop 4.1
cls_reason: "Per the assignment's audit warning, classified on Props 4.1/4.3 (circuit-size-bounded distinguisher), not Thm 2.1's low-degree bound. Prop 4.3's reduction/simulator is also circuit-size bounded (O(n choose r)), a second party in the same unit (second_party=circuit size). Thm 2.1's low-degree bound, offered as evidence for Conjecture 1.4, is the same distinguisher party under a second, incomparable notion (second_notion=algo class, rule 4b)."
cls_prov: P
cls_date: 2026-08-22
---

> **Verified against the primary source.** Every quotation below was checked against
> `raw/BJRZ24_LowDegreePlantedSubgraph.pdf` on 2026-08-22 and is verbatim.

## Summary

Abram, Beimel, Ishai, Kushilevitz and Narayanan (TCC 2023) conjectured that the planted random
subgraph problem is hard for `k ≤ n^{1−Ω(1)}`, and built communication-efficient secret sharing and
private simultaneous messages protocols on it. In the planted random subgraph model one observes a
pair `(H, G)` where `G` is a random `n`-vertex graph and `H` is a random `k`-subgraph of `G` with its
vertex labels removed. Abram et al. could confirm their conjecture in the low-degree framework only up
to the planted clique threshold `k ≤ n^{1/2−Ω(1)}`.

This paper closes that gap in the low-degree framework. Verbatim: *"We prove that the planted random
subgraph problem remains hard for low-degree distinguishers of degree at most"* `o((log n / log log
n)²)` *"in the full range"* `k ≤ n^{1−Ω(1)}`. The result is averaged over the choice of `H` rather
than worst-case in `H`, which is what supplies the extra cancellations. It extends to `r`-uniform
hypergraphs for constant `r`, and it tolerates `ℓ` leaked vertices, which is what the cryptographic
constructions need. The authors state the analysis is tight in three parameters at once, verbatim:
*"Our analysis is tight in the distinguisher's degree, its advantage, and in the number of leaked
vertices."*

The paper also extends the constructions, giving multiparty PSM protocols for random functions under a
stronger and more natural security definition that lets the parties choose inputs jointly from a
distribution depending on the function, and bit secret sharing with share size `(1+ε) log n`.

## Claim Boundary

- **Quantified over.** Theorem 2.1 is a bound on the expectation over `H` of the degree-`D` likelihood
  ratio, holding for any fixed leakage set `L` of size `ℓ` under three parameter conditions. A Markov
  argument then gives `LR_D(H, L) = o(1)` for a `1 − o(1)` fraction of `H`, and a higher-moment version
  gives a bound holding simultaneously over all leakage sets. So the statement is about typical `H`,
  not all `H`. Abram et al.'s weaker bound is the worst-case one.
- **Antecedent.** As in the front matter. The low-degree theorem is unconditional. The cryptography is
  conditional on Conjecture 1.4, which is an assumption and not a theorem.
- **Which party is constrained and in what resource.** The distinguisher. In Theorem 2.1 it is
  constrained in algebraic degree. In Propositions 4.1 and 4.3 it is constrained in circuit size. The
  proof of Proposition 4.1 builds an explicit circuit `D'` from a hypothesised distinguisher `D` and
  argues the two have the same advantage, and Proposition 4.3 exhibits a simulator and a reduction of
  size `O(n choose r)`. These are size-bounded reductions in the ordinary cryptographic style.
- **Algorithm class.** Degree-`D` real polynomials in the hyperedge indicators. The paper's own framing,
  verbatim: *"the distinguishing algorithm is allowed to compute an arbitrary degree-"* `D` polynomial
  function of the bits of the input over the reals, and degree-`D` polynomials serve as a proxy for
  `n^{O(D)}` time because such a polynomial in `poly(n)` input bits can be evaluated by brute force in
  that time. A degree bound is **not** a running-time bound, and the two classes are known to differ.
- **Does not establish.** It does not establish that the planted random subgraph problem is hard for
  polynomial-time algorithms. It does not establish that the secret sharing or PSM constructions are
  secure, only that they are secure if Conjecture 1.4 holds. It does not establish a share-size
  separation between the computationally secure construction and the best perfectly secure one, which
  Section 4.1 records as open and explains is hard to reach with available methods. And it does not
  supply a security definition that quantifies over low-degree adversaries.
- **Abstract versus theorem.** The abstract is accurate and says "assuming the hardness" of the
  distinguishing problem when describing Abram et al.'s constructions. The paper's title, *Low-Degree
  Security*, is the one place where a reader could take the low-degree class to be the adversary class
  of the cryptography. It is not. Section 1.3 is titled *Low-degree lower bounds* and opens, verbatim:
  *"We provide evidence for these conjectures in the form of lower bounds against the low-degree
  polynomial computational model"*.

## Key Contributions

- **Theorem 2.1.** Low-degree hardness of planted random subgraph detection in the full range
  `k ≤ n^{1−Ω(1)}`, averaged over `H`, for `r`-uniform hypergraphs with constant `r`, and robust to
  `ℓ` leaked vertices. Verbatim: *"The hardness extends to r-uniform hypergraphs for constant r."*
- Tightness in all three of degree, advantage, and leakage, each witnessed by an explicit distinguisher.
  The degree bound is optimal up to a `log log n` factor. The advantage bound is matched by
  edge counting without leakage and by a linear distinguisher with leakage. The leakage bound is matched
  by a distinguisher that looks for a vertex of `G` whose adjacencies in `L` match those of a vertex of
  `H` outside `L`.
- Extension of Abram et al.'s PSM protocol to `r` parties, under a security definition that allows the
  parties' inputs to depend on the function. The authors note, verbatim, that Abram et al.'s
  *"security definition appears to additionally assume that the choice of inputs"* is *"independent of
  the function"*.
- Bit secret sharing with share size `(1+ε) log n` for forbidden hypergraph access structures, with
  secrecy against all independent sets of size at most `ℓ = o(ε log n)^{1/(r−1)}`.
- A proof technique. Averaging the likelihood ratio over `H` rather than bounding it for worst-case `H`
  introduces cancellations that carry the bound past the planted clique threshold.

## Key Definitions / Theorems

- **Definition 1.2 (planted random subgraph model).** One observes `(H, G)` where `G` is a random
  `n`-vertex graph and `H` is a random `k`-subgraph of `G` with the vertex labels removed.
- **Conjecture 1.3 (Abram et al.).** The planted random subgraph problem is hard up to advantage
  `n^{−Ω(1)}` provided `k ≤ n^{1−Ω(1)}`, with high probability over `H ~ G(k, 1/2)`. This is a
  conjecture, and the paper's main theorem confirms it in the low-degree framework only. Verbatim:
  *"Our main contribution is the confirmation of Conjecture 1.3 in the low-degree framework."*
- **Conjecture 1.4 (with `ℓ`-vertex leakage).** The planted and model distributions, each augmented
  with the images of `ℓ` named vertices, are `n^{−Ω(1)}`-indistinguishable **in polynomial time**, for
  all leakage sets of size `ℓ`. This is the assumption the cryptography rests on.
- **The degree-`D` likelihood ratio.** `LR_D(H, L)` is the supremum over real polynomials of degree at
  most `D` of the advantage, defined as the difference of means under the planted and null
  distributions divided by the standard deviation under the null. It measures the best advantage of a
  degree-`D` distinguisher that can arbitrarily preprocess `H` and knows `L`.
- **Theorem 2.1.** Under three conditions, on `k` relative to `n`, `p`, `D` and `ℓ`, on `ℓ` relative to
  `k` and `log n`, and on `D` relative to `log n` and `log log n`, the quantity
  `(E_H[LR_D(H,L)^{2p}])^{1/p}` is bounded by `2ℓ(r−1) n^{−ε} / (1 − n^{−ε/2})` plus an exponentially
  small term. For `p = 1`, `ℓ = o((log n)^{1/(r−1)})` and constant `ε`, this reads
  `E_H[LR_D(H,L)²] = n^{−ε+o(1)}`.
- **Proposition 4.1 (secret sharing security).** If the planted and null distributions are
  `(s, ε)`-indistinguishable for all leakage sets of size `ℓ`, then for every independent set of `R` of
  size at most `ℓ`, shares of 0 and 1 are `(s, 2ε)`-indistinguishable by the parties in that set.
- **Proposition 4.3 (PSM security).** Under the same `(s, ε)`-indistinguishability hypothesis with
  `ℓ = r`, Construction 4 is `(O(n choose r), s − O(n choose r), ε)`-secure.

## Connections

- **The retraction it forced.** A claim recorded in [CLAUDE.md](../../CLAUDE.md) on 2026-07-25 and in
  [native-asymmetry-in-learning](../analyses/native-asymmetry-in-learning.md) §3.1, that no security
  definition quantifies over SQ or low-degree adversaries, was retracted on the strength of this paper.
  The retraction was right in direction and needs the qualification recorded above. Low-degree analysis
  underwrites cryptographic constructions here as **evidence for a polynomial-time conjecture**. The
  security propositions themselves quantify over size-bounded circuits, exactly as the corresponding
  claim in [Abram et al.](cryptography-from-planted-graphs.md) does. Neither paper defines security
  against a low-degree adversary.
- Builds on and improves [Abram et al., Cryptography from Planted
  Graphs](cryptography-from-planted-graphs.md).
- [PKE from Planted Clique](pke-from-planted-clique.md), the same programme of cryptography from
  planted problems.
- Concepts and surveys:
  [low-degree-polynomial-framework](../concepts/low-degree-polynomial-framework.md),
  [planted-clique](../concepts/planted-clique.md),
  [low-degree survey](low-degree-polynomials-survey.md),
  [BBHLS21 SQ and low-degree equivalence](brennan-sq-lowdegree-equivalence.md).
- Entities: [Alon Rosen](../entities/alon-rosen.md), [Ilias Zadik](../entities/ilias-zadik.md).

## Limits

- **The paper flags its own weakest point.** Verbatim: *"It should be noted that there exists a certain
  weakness in existing low-degree hardness evidence for the planted clique problem, which also applies
  to our lower bound for the planted random subgraph problem"*. The reason, verbatim: *"Both planted
  clique and planted random subgraph technically do not satisfy the noise-robust assumption of the
  low-degree conjecture because the planted isomorphic copy of H in the graph G is not robust to small
  perturbations of G"*. Noise robustness is the hypothesis under which failure of `O(log n)`-degree
  polynomials is taken to predict failure of all polynomial-time algorithms, defined in the paper's
  footnote, verbatim, as meaning *"that the planted structure is resilient to small random
  perturbations"*, citing Hopkins and [Holmgren and Wein](holmgren-counterexamples-low-degree.md). The
  authors add, verbatim, that *"in a handful of carefully chosen noise-free problems, low-degree methods
  are provably weaker than other brittle polynomial-time methods such as Gaussian elimination or
  lattice-basis reduction techniques"*, while noting those techniques do not appear to apply to graph
  settings.
- The gap between low-degree hardness and polynomial-time hardness is not a formality. See
  [The Quasi-Polynomial Low-Degree Conjecture is False](quasi-poly-low-degree-conjecture-false.md),
  which exhibits planted distributions with vanishing low-degree advantage whose noisy distinguishing
  problem is solvable far faster than the conjecture allows. Any claim resting on a low-degree bound
  must state which of the two classes it means.

## Open Questions / Limitations

- A provable share-size separation between the computationally secure Construction 3 and the best
  possible perfectly secure construction for some access structure. Section 4.1 records this as open
  and explains why available methods do not reach it. Because the scheme does not tolerate `Ω(log n)`
  bits of leakage, the best bound obtainable through Csirmaz's relaxation is `ℓ = o(log n)`.
- Whether computational security for forbidden graph access structures is subject to the same
  `log k − O(1)` share-size limitation as statistical security. The paper says this is not known.
- Whether statistical security for PSM is subject to the `(3 − o(1)) log k` combined message length
  bound known for perfect security. Also not known.
- The restricted class here is low-degree over a planted graph instance. A programme aimed at learning
  adversaries priced in exponent units over a continuous instance is related but not the same.
- Recorded as a search lesson. This result lives in the cryptography literature while its application
  looks like machine-learning security. A novelty check must sweep the venue where the technique lives,
  not only where the application lives.

## Quotes / Notable Passages

On the status of the low-degree analysis relative to the conjectures the cryptography needs:

> "We provide evidence for these conjectures in the form of lower bounds against the low-degree
> polynomial computational model"

On tightness:

> "Our analysis is tight in the distinguisher's degree, its advantage, and in the number of leaked
> vertices."
