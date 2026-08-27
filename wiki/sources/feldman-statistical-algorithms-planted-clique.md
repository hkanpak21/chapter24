---
title: Statistical Algorithms and a Lower Bound for Detecting Planted Cliques
type: source
date_ingested: 2026-04-12
authors: [Vitaly Feldman, Elena Grigorescu, Lev Reyzin, Santosh S. Vempala, Ying Xiao]
venue: JACM 2017, conference version STOC 2013 (the ingested PDF is arXiv:1201.1214v6, 15 Aug 2016, and does not itself state a venue)
year: 2017
tags: [planted-clique, statistical-query, lower-bounds, statistical-computational-gaps]
claim_quantifier: universal
antecedent: "none. The lower bound is unconditional inside the statistical query model."
algorithm_class: "SQ"
adversary_bound: "queries to the VSTAT and MVSTAT oracles, bounded in number and in precision"
date_verified: 2026-08-20
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: algo class
cls_tightness: class
cls_baseline: stated
cls_baseline_checked: yes
cls_second_party: none
cls_second_notion: queries
cls_assessed: explicit
cls_evidence: "no polynomial-time statistical algorithm can solve the problem using queries to VSTAT(o(n2/k2)) and any SQ algorithm requires nΩ(log n) queries to VSTAT(n2−δ/k2)."
cls_evidence_src: Thm 2.9
cls_reason: "Not an ML attack paper: a detection/estimation hardness result for planted structure, so target/family/phase/access/write=none. party=learner rather than attacker: the paper 'generalizes Kearns' SQ framework from PAC learning' with no adversary vocabulary anywhere, matching this programme's established 'restricted-class learner' framing for SQ/low-degree units (repo CLAUDE.md). unit=algo class, tightness=class for the SQ-membership quantifier ('any SQ algorithm'); second_notion=queries records the explicit numeric query-count/precision bound (n^Ω(log n) queries to VSTAT(·)) the same party also carries, per rule 4b (one party, two incomparable notions: class membership and query count). baseline=stated: Thm 2.9 fixes the success criterion at probability at least 2/3."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper (FGR+13 in the literature) establishes the foundational Statistical Query (SQ) lower bound for planted clique. It generalizes Kearns' SQ framework from PAC learning to distributional search/optimization problems, introducing a notion of **statistical dimension** (SDA) for such problems. The main theorem shows that any SQ algorithm solving planted clique with clique size k requires either super-polynomially many queries or queries of super-polynomial precision whenever k = o(√n) — matching the conjectured √n threshold.

This is widely cited as the first "restricted model" evidence for the PC conjecture beyond SDP/LS+ hierarchies, and serves as a template for SQ lower bounds across the entire statistical-computational gap literature (tensor PCA, sparse PCA, community detection, robust mean estimation).

## Claim Boundary

- **Quantified over:** every algorithm whose access to the input distribution is limited to estimates of expectations, in the paper's VSTAT and MVSTAT forms. The bound is on query count and oracle precision for detecting planted bipartite clique and planted dense subgraph distributions when the planted clique has size O(n^{1/2-delta}) for constant delta > 0.
- **Antecedent:** none. The lower bound is unconditional inside the statistical query model.
- **Algorithm class:** SQ. The abstract observes that most natural algorithms of interest, including moment methods, local search, standard iterative convex optimization, MCMC and simulated annealing, can be implemented in the framework. That is a statement about which known algorithms fit the model, not a proof that every polynomial-time algorithm does.
- **Does not establish:** that planted clique is hard for polynomial time. A bound against SQ rules out one class. Gaussian elimination on an exactly solvable linear system is the standard example of a polynomial-time algorithm that both the SQ and the low-degree model miss.
- **Abstract vs theorem:** none found. The abstract states the result as concrete evidence supporting hardness assumptions rather than as hardness.

## Key Contributions

- Extension of the SQ framework from labeled PAC learning to unsupervised/distributional problems via the VSTAT(m) oracle.
- Introduction of **statistical dimension with average correlation (SDA)** — a complexity measure that lower bounds SQ query complexity.
- SQ lower bound for bipartite planted clique (and thus planted clique itself) of n^{Ω(log n)} queries for k ≤ n^{1/2 - ε}.
- Template for proving SQ hardness of many subsequent statistical-computational gap problems.

## Key Definitions / Theorems

- **VSTAT(m) oracle**: returns E[φ(x)] ± max(1/m, √(Var/m)) — models algorithms that access ~m i.i.d. samples only through statistical averages.
- **Statistical Dimension SDA(D₀, S, m)**: maximum q such that any subset of S of density ≥ 1/q has average pairwise correlation ≤ 1/m. Lower bounds SQ complexity.
- **Main theorem**: Any SQ algorithm for bipartite planted k-clique requires n^{Ω(log n)} queries to VSTAT(o(n²/k²)) for k = o(√n).

## Connections

- [Planted Clique](../concepts/planted-clique.md) — canonical application
- [Statistical Query Model](../concepts/statistical-query-model.md) — formally extended here
- [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md) — later shown nearly equivalent [Brennan-Bresler-Hopkins-Li-Schramm 2021]
- [Statistical-Computational Gaps](../concepts/statistical-computational-gaps.md) — foundational evidence

## Open Questions / Limitations

- SQ lower bounds do not formally imply polynomial-time hardness (SQ is a restricted model).
- The bipartite formulation is used for technical convenience; translating cleanly to the standard one-shot PC problem requires care (see Brennan et al. 2021 nicenness condition).
- Does not address search/refutation variants directly.

## Quotes / Notable Passages

_All passages below verified verbatim against `raw/FGRVX17_SQLowerBoundPC.pdf` on 2026-08-20._

> "The assumed hardness of variants of these problems has been used to prove hardness of several other problems and as a guarantee for security in cryptographic applications. Our lower bounds provide concrete evidence of hardness, thus supporting these assumptions."

> "Our main application is a nearly optimal lower bound on the complexity of any statistical query algorithm for detecting planted bipartite clique distributions (or planted dense subgraph distributions) when the planted clique has size O(n^{1/2−δ}) for any constant δ > 0."

The exponent and the constant in the second passage are set as a superscript and a Greek letter, which `pdftotext` flattens and drops. The surrounding prose matches the paper exactly and the parameters are as stated in the abstract.

The following line is not a quotation and was carried by an earlier ingest without attribution. Retained unquoted as a summary.

- Statistical dimension framework has become the standard tool for SQ lower bounds in high-dimensional statistics.
