---
title: Counterexamples to the Low-Degree Conjecture
type: source
date_ingested: 2026-04-12
authors: [Justin Holmgren, Alexander S. Wein]
venue: ITCS 2021 (the ingested PDF is arXiv:2004.08454v1, 17 Apr 2020, and does not itself state a venue)
year: 2021
tags: [low-degree-polynomials, counterexamples, statistical-computational-gaps, complexity-theory]
claim_quantifier: existential
antecedent: "none. The refutation is unconditional. Both constructions use efficiently decodable error-correcting codes."
algorithm_class: "low-degree"
date_verified: 2026-08-20
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: compute
cls_party: learner
cls_unit: time
cls_tightness: poly
cls_baseline: n/a
cls_second_party: none
cls_second_notion: algo class
cls_assessed: explicit
cls_evidence: "there exists a polynomial-time computable test distinguishing Tδ µ and ν with probability 1 − o(1)"
cls_evidence_src: Thm 3.1
cls_reason: "Same shape as quasi-poly-low-degree-conjecture-false: one distinguisher assessed under two incomparable resource notions where the paper's point is that they diverge (rule 4b), so party=learner, unit=time, tightness=poly (the escaping test in Thm 3.1 and again in Thm 3.4 is genuinely polynomial-time, not quasi-polynomial), second_notion=algo class for the low-degree side: mu is constructed to be Omega(n)-wise independent w.r.t. nu, and the paper states 'the notion of D-wise almost independence captures how well degree-D polynomials can distinguish mu and nu' (Section 2), so mu evades all low-degree tests up to degree Omega(n) while the exhibited test is poly-time. baseline=n/a, matching the other low-degree/statistical-computational-gap pages, since this is a counterexample to a conjectured algorithm-class-vs-time equivalence, not an advantage-over-baseline claim."
cls_prov: P
cls_date: 2026-08-22
---

## Summary

This paper refutes the original formulation of the Low-Degree Conjecture (Hopkins 2018) by constructing explicit hypothesis-testing problems where degree-O(log n) polynomials fail to distinguish the planted from the null distribution, yet polynomial-time algorithms succeed. Both counterexamples are built from efficiently decodable error-correcting codes. The first turns on the specific noise operator used in the conjecture, together with the fact that a single real number can encode a polynomially bounded amount of data; the second shows the symmetry assumption cannot be dropped. _Corrected 2026-08-20 against the primary PDF: an earlier version of this paragraph attributed the counterexamples to algebraic structure detected by Gaussian elimination over finite fields. That is the paper's illustration of why a noise assumption is needed at all, not its construction._

The authors propose a modified version of the conjecture that avoids their counterexample by excluding problems with such "algebraic" structure, and argue the modified version remains a useful heuristic for "structureless" planted problems. The paper is widely cited as establishing the limits of the low-degree framework and motivating the search for complementary lower-bound tools (Franz-Parisi, OGP, etc.).

(Note: The raw PDF for this paper was replaced during the 2026-04-23 raw/ audit — the file previously contained Brennan-Bresler 2020 "Average-Case Lower Bounds for Learning Sparse Mixtures" instead of Holmgren-Wein 2021. Current PDF is verified correct: arXiv:2004.08454.)

## Claim Boundary

- **Quantified over:** two constructed hypothesis testing problems. The first refutes the conjecture of Hopkins as stated. The second shows that the symmetry assumption in that conjecture cannot be dropped.
- **Antecedent:** none. The refutation is unconditional. Both counterexamples are built from efficiently decodable error-correcting codes, and the first turns on the specific noise operator used in the conjecture together with the fact that a single real number can encode a polynomially bounded amount of data.
- **Algorithm class:** low-degree. The counterexamples exhibit problems where low-degree polynomials fail and a polynomial-time algorithm succeeds.
- **Does not establish:** that the low-degree framework is unsound in general. The authors state that the results do not undermine the framework and point to a modification of the conjecture that rules out their counterexample.
- **Abstract vs theorem:** none found. The abstract carries the qualification about the noise operator in the same breath as the refutation.

## Key Contributions

- Explicit counterexample to the original low-degree conjecture. _Corrected 2026-08-20 against the primary PDF: an earlier version of this bullet described the construction as a variant of learning parities or 3-XOR broken by Gaussian elimination. The word "parity" does not occur in the paper. Both counterexamples are built from efficiently decodable error-correcting codes, and the first exploits the specific noise operator in the conjecture together with the fact that a single real number can encode a polynomially bounded amount of data. Gaussian elimination on an exactly satisfiable linear system appears in the paper only as the standard illustration of why a noise assumption is needed at all._
- Modified conjecture formulation restricted to "structureless" planted problems.
- Sharpened understanding: LD captures noise-robust / moment-based algorithms but not algebraic ones.

## Key Definitions / Theorems

- Counterexample construction based on efficiently decodable error-correcting codes. _Corrected 2026-08-20 against the primary PDF; see the note under Key Contributions._
- Theorem 3.4, the second counterexample, showing the symmetry assumption in the conjecture cannot be dropped.
- Remark 3.3, a modification of the conjecture that the authors say they do not know how to refute.

## Connections

- [Low-Degree Polynomial Framework](../concepts/low-degree-polynomial-framework.md) — counterexample paper
- [Statistical Query Model](../concepts/statistical-query-model.md) — LD and SQ both fail on parity; this is a "known exception"
- [Lattice Methods Surpass Sum-of-Squares](zadik-lattice-surpass-sos.md) — further LD counterexamples via LLL
- [Alexander Wein](../entities/alexander-wein.md)

## Open Questions / Limitations

- What precisely makes a problem "structureless"? No clean characterization exists.
- Are there counterexamples not rooted in algebraic structure (e.g., anti-concentration)?
- How to adapt LD to capture algebraic algorithms, if at all.

## Quotes / Notable Passages

_All passages below verified verbatim against `raw/HW21_CounterexamplesLD.pdf` on 2026-08-20. The earlier note that the file content was mismatched no longer applies; the PDF is arXiv:2004.08454v1 and is the correct paper._

> "In this work, we refute the conjecture of Hopkins [Hop18]. However, our counterexample crucially exploits the specifics of the noise operator used in the conjecture, and we point out a simple way to modify the conjecture to rule out our counterexample."

> "These results do not undermine the low-degree framework for computational lower bounds, but rather aim to better understand what class of problems it is applicable to."

> "Both of our counterexamples are based on efficiently decodable error-correcting codes."
