---
id: taxonomy-landscape
date: 2026-08-05
tag: lit
status: draft
supersedes: null
builds_on: 2026-08-05-halil-lit-survey-structure.md
commit: null
cluster: n/a
jobs: []
pi_reviewed: false
---

# Nobody prices the adversary, and privacy and integrity are disjoint by construction

## Scope

The PI meeting in [[2026-08-05-pi]] asks first for a survey of what has been done in taxonomy. This
report sweeps roughly thirty taxonomies, systematizations and formal frameworks of machine learning
security and privacy, records the axes each uses, and answers two questions: whether the requested
matrix exists, and whether unified formal definitions exist. Sources were read from primary documents
where the claim is load-bearing.

## Result

**The requested matrix is unoccupied, and for a structural reason: privacy and integrity are disjoint by
construction across nearly every work in the field. Separately, and more usefully, no taxonomy in the
field has an adversary-class axis at all.**

Every axis in the literature called knowledge, access or capability is an **interface** ladder, not a
**resource** ladder. Across the whole sweep the compute axis reduces to six entries, none of which is a
security parameter.

### Q1. Does the requested matrix exist

No. The three axes each exist and pairs have been crossed, never all three.

| Rank | Work | What it has | Why it is not the matrix |
| --- | --- | --- | --- |
| 1 | Papernot, McDaniel, Sinha, Wellman, EuroS&P 2018 | A genuine two-of-three: §IV Training {Integrity, Privacy} × §V Inferring {Integrity, Privacy} | Third axis is adversary knowledge, not asset. The asset-shaped structure exists — the training ladder Read → Injection → Modification → **Logic Corruption**, "the adversaries can tamper with the learning algorithm" — but is never crossed with the other two |
| 2 | Barreno, Nelson, Joseph, Tygar, Machine Learning 2010; Huang et al., AISec 2011 | The **only literal cube**: influence × security violation × specificity, with an explicit independence claim. 8 classes, 12 once privacy is added | Third axis is specificity, not asset |
| 3 | NIST AI 100-2e2025 (Vassilev, Oprea, Fordyce, Anderson) | Five axes for predictive AI; **SOURCE CODE CONTROL** is the field's closest approximation to the learning algorithm as an attacked object | It is what the attacker *controls*, not what is *violated*; Figure 1 is a Venn diagram with callouts, so the axes are never realized as a product |
| 4 | Wang & Luan, TMLR 2026 | The only source-to-target asset matrix: D→D, D→M, M→D, M→M, with per-cell programs | Two assets only, no learning algorithm, and the security property is folded into the direction |
| 5 | ENISA 2021, Table 3 | A real threats × lifecycle-stage matrix | No security-property axis and no asset axis |

**The structural obstacle, and this is the finding.** Privacy and integrity do not co-occur. Rigaki and
Garcia exclude security attacks; Salem et al. exclude integrity; Cinà et al. drop privacy in a footnote;
Li et al. exclude availability; Goldblum et al. exclude privacy; Desfontaines and Pejó cover defences
only; De Cristofaro excludes adversarial examples. **NIST is the only document that puts availability,
integrity and privacy on one page, and it does not cross them with an asset axis.**

So a matrix that spans the privacy-integrity divide *and* names the learning algorithm as an attacked
asset is unoccupied. Three footholds exist for that asset and none is an axis: Papernot's Logic
Corruption, NIST's Source Code Control, and Cinà et al.'s model-training capability.

### Q2. Do unified formal definitions exist

No, and the partition is exact.

| Work | Covers | Method | Stops at |
| --- | --- | --- | --- |
| Salem, Cherubin, Evans, Köpf, Paverd, Suri, Tople, Zanella-Béguelin, IEEE S&P 2023 | **privacy only** | **games**: 18 of them, `p`-resilience, `⪯_c` reductions modelled on concrete security, Theorems 1–11 for every ordered pair | no integrity, no availability, no test-time attacks; model stealing out of scope; poisoning demoted to a capability modifier; adversaries **explicitly information-theoretic** |
| Wu, Zhu, Liu, Liu, He, Lyu, arXiv:2302.09457 | **integrity only** | **optimization**: Definition 1 via stealthiness, benign consistency and adversarial inconsistency, over a five-stage lifecycle. The only framework where the dataset and the weights are simultaneous first-class variables | no privacy; no knowledge or compute parameterization; an objective template, so no advantage and no notion of the adversary failing |

**These two are precise complements and nothing joins them.** One work spans both:

**Villa, Durak, Kohno, Maharramli, Roesner, arXiv:2603.02590, March 2026.** The AIOracle abstraction,
with LEARN and INFER as distinct phases, the dataset, learning algorithm, model and adversary as
separate formal objects, and one game unifying confidentiality, integrity and availability through a
predicate. **This is the closest existing work to the survey's target, and it is the workline already
tracked in [[LEARNING_aioracles]].** It stops at: an unbounded adversary whose capability set is a flag
set rather than a resource parameter, grey-box knowledge excluded by the authors, a success predicate
the authors concede is non-implementable, and no reductions or separations between the properties.

### The finding that positions the programme

Across roughly thirty works, the entire treatment of adversary resources is:

| Work | Its compute axis | Why it is not a security parameter |
| --- | --- | --- |
| Desfontaines & Pejó, PoPETs 2020, dimension C | unbounded versus polynomial-time | binary |
| Salem et al., §II-C | names the move, verbatim: "most game-based formulations do not explicitly limit the resources available to an adversary" | instantiated only as a query counter |
| TrojanZoo, EuroS&P 2022 | implementation wall-clock | a measurement, not a definition |
| Cinà et al., §3.4.2 | "computational complexity of poisoning attacks" | framed as a limitation of current attacks |
| Poisoning-rate bins; BackdoorBench ratios | data budget | not compute |
| Mahloujifar et al., `p`-tampering | a genuinely polynomial-time adversary | one attack model, not a taxonomy axis |

**No taxonomy in the field has an adversary-class axis.** That is the slot the programme's `𝒜` and `b`
occupy, and this sweep verifies it across the field rather than by inference.

Does not show: that an adversary-class axis is *legitimate* as an axis. Two published criteria exist for
that and are stated below; the axis has not been tested against them.

## How it was produced

| | |
| --- | --- |
| Method | Multi-lens literature sweep, roughly thirty works, primary documents read where a claim is load-bearing |
| Coverage | founding taxonomies; modern SoKs; standards bodies (NIST, ENISA, ISO/IEC, MITRE ATLAS); privacy surveys; poisoning and backdoor surveys; benchmark ontologies; formal frameworks; large-language-model and agentic taxonomies |
| Corrections found | four citations in the sweep brief were wrong, including author lists for TrojanZoo, BackdoorBench and the Liu et al. privacy survey, and the provenance of the Biggio knowledge tuple |
| Criteria we will be measured against | Desfontaines and Pejó's **mutual compatibility** (variants along different dimensions must combine meaningfully) and **inner exclusivity** (variants within one dimension must not); Barreno et al.'s stronger independence claim |
| Artifacts | This report |

## What this changes

The survey's positioning is now determined rather than guessed: the contribution is the axis nobody
has, which is the adversary priced as a class and a budget, and the matrix that spans a divide the
field keeps disjoint. The closest prior work is Villa et al. 2026, so the survey must position against
it directly and its unbounded flag-set adversary is exactly what the programme's `𝒜` and `b` replace.
One trend must be argued against explicitly: the knowledge axis has **degenerated** over fifteen years,
from a five-component specification in 2014 to a single bit in 2022 to nothing in the benchmark-derived
taxonomies, which replaced it with whatever the code can toggle.

## Where it applies

| Section | Change |
| --- | --- |
| Survey, related work | Structure by the two synthesis answers, not by chronology. Lead with the disjointness of privacy and integrity |
| Survey, positioning | Against Villa et al. 2026 as nearest work; against Salem et al. and Wu et al. as the exact complement that nothing joins |
| Survey, contribution | The adversary-class axis, verified absent across thirty works |
| Survey, axis defence | Test the proposed axes against mutual compatibility and inner exclusivity before submission |
| Corpus | Ingest, in order: Villa et al. arXiv:2603.02590; Salem et al. arXiv:2212.10986; Papernot et al. EuroS&P 2018; Barreno et al. 2010; NIST AI 100-2e2025; Wu et al. arXiv:2302.09457; Cinà et al. arXiv:2205.01992; Rigaki and Garcia arXiv:2007.07646; Desfontaines and Pejó arXiv:1906.01337 |
