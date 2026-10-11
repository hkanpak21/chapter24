---
title: Planted Clique Conjectures are Equivalent
type: source
date_ingested: 2026-04-12
authors: [Shuichi Hirahara, Nobutaka Shimizu]
venue: "STOC 2024"
venue_evidence: "https://dl.acm.org/doi/abs/10.1145/3618260.3649751 (Proceedings of the 56th Annual ACM Symposium on Theory of Computing) plus https://speakerdeck.com/nobushimi/planted-clique-conjectures-are-equivalent, title slide reads 'talk at STOC2024' — dblp.org was unreachable this session (repeated ECONNRESET) so this is confirmed via the venue's own ACM listing and the authors' own talk deck instead, not dblp"
year: 2024
tags: [planted-clique, statistical-computational-gaps, hardness-reductions, complexity-theory, average-case-reductions]
claim_quantifier: universal
antecedent: "none. The reductions are unconditional. What stays conjectural is the hardness itself."
algorithm_class: "all poly-time"
date_verified: 2026-08-20
cls_target: none
cls_family: none
cls_phase: n/a
cls_access: none
cls_write: none
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: n/a
cls_second_party: none
cls_assessed:
cls_evidence: "absent"
cls_evidence_src: "no hardness bound stated; the theorem is a poly-time equivalence between PC-detection, PC-search, and PC-refutation, unconditional (antecedent: none, 'what stays conjectural is the hardness itself'); wiki Claim Boundary and abstract"
cls_reason: "Rule 2: the headline result (title and abstract both lead with it) is a reduction/equivalence between problem formulations, not a bound on any party, so party/unit/frame=none and tightness=unstated. The one bound-shaped statement in the paper, 'no polynomial-time algorithm distinguishes the two random graphs with probability much greater than k^2/n if and only if the planted clique conjecture holds' (Key Contributions, third bullet), is a secondary corollary, conditional on the still-open PC conjecture, and is not what the abstract leads with, so rule 1 keeps it out of this row. Flagged for a second reader: that corollary has the shape party=learner or auditor, unit=time, tightness=poly, baseline=stated (edge-counting achieves k^2/n) if a future pass wants a second row for it. Confirmed against the audit warning that refutation is a separate equivalence class from detection/search in this paper, so no equivalence-class claim was conflated here."
cls_prov: S
cls_date: 2026-08-22
---

## Summary

This paper establishes formal equivalences between different variants of the Planted Clique (PC) Conjecture. Historically PC has several natural formulations — detection (decision), search (find the clique), refutation (certify no clique exists) — and it was not known whether these are computationally equivalent. The work gives reductions showing that under mild conditions these formulations are polynomial-time equivalent, consolidating the PC conjecture as a single hardness assumption.

This has significant implications for the web of average-case reductions built on top of PC: reductions that use one variant (e.g., detection) now yield hardness for the others as well, unifying the literature and strengthening conditional lower bounds.

## Claim Boundary

- **Quantified over:** variants of the planted clique conjecture. The abstract names search versions with success probability exponentially close to one and with non-negligible success probability, a worst-case version on incompressible graphs, decision versions with small and with large success probabilities, and decision versions with adversarially chosen and with binomially distributed k.
- **Antecedent:** none. The reductions are unconditional. What stays conjectural is the hardness itself.
- **Algorithm class:** all polynomial time. These are ordinary polynomial-time reductions, not restricted-class results.
- **Does not establish:** that planted clique is hard, and does not place refutation inside the same equivalence class as detection and search. Refutation is the subject of a separate equivalence, between the existence of a refutation algorithm and an average-case polynomial-time algorithm for the k-clique problem on Erdos-Renyi random graphs.
- **Abstract vs theorem:** none found. The abstract reports a detection-recovery gap in success probabilities as a consequence of the equivalences rather than as an assumption.

## Key Contributions

- Polynomial-time equivalences among search versions at success probabilities from exponentially close to one down to non-negligible, a worst-case version on incompressible graphs, and decision versions at small and large success probabilities including adversarially chosen and binomially distributed k. _Corrected 2026-08-20 against the primary PDF: an earlier version of this bullet grouped refutation with detection and search. Refutation is not in that equivalence class. The paper states a separate equivalence, between the existence of a refutation algorithm and an average-case polynomial-time algorithm for k-clique on Erdős–Rényi random graphs._
- Establishes the equivalence between the planted clique problem of Jerrum and Kučera and the decision version suggested by Saks in the 1990s.
- Identifies the optimality of the simple edge-counting algorithm among decision versions: no polynomial-time algorithm distinguishes the two random graphs with probability much greater than k²/n if and only if the planted clique conjecture holds.
- Gives the first one-way function admitting a polynomial-time security-preserving self-reduction from exponentially weak to strong one-way functions.
- Reveals a detection-recovery gap in success probabilities for planted clique.
- Strengthens downstream reductions that build statistical-computational hardness on PC.

## Key Definitions / Theorems

- Formal statements of PC-detection, PC-search, PC-refutation.
- Main theorem: poly-time equivalence among the search and decision variants named above.
- A separate theorem for refutation, equating the existence of a refutation algorithm with an average-case polynomial-time algorithm for k-clique on Erdős–Rényi random graphs.

## Connections

- [Planted Clique](../concepts/planted-clique.md)
- [Secret Leakage Planted Clique](../concepts/secret-leakage-planted-clique.md)
- [Average-Case Reductions](../concepts/average-case-reductions.md)
- [Barak et al. SoS Lower Bound](barak-sos-lower-bound-planted-clique.md) — SoS lower bounds are stated for refutation; Hirahara's equivalence ties this back to detection/search hardness.

## Open Questions / Limitations

- Reductions are average-case and depend on the distribution being preserved; extensions to PC_ρ variants are not fully worked out.
- Whether similar equivalences hold across other planted problems (SBM variants, sparse PCA) remains open.

## Quotes / Notable Passages

_All passages below verified verbatim against `raw/HS24_PCConjecturesEquivalent.pdf` on 2026-08-20. The earlier note about extraction failure no longer applies._

> "In this paper, we prove the equivalence among many (in fact, most) variants of planted clique conjectures, such as search versions with a success probability exponentially close to 1 and with a non-negligible success probability, a worst-case version (the k-clique problem on incompressible graphs), decision versions with small and large success probabilities, and decision versions with adversarially chosen k and binomially distributed k."

> "These results reveal a detection-recovery gap in success probabilities for the planted clique problem."

> "We also present another equivalence between the existence of a refutation algorithm for the planted clique problem and an average-case polynomial-time algorithm for the k-clique problem with respect to the Erdős–Rényi random graph."
