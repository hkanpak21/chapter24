---
id: survey-spine
date: 2026-08-20
tag: lit
status: draft
supersedes: null
builds_on: null
commit: null
cluster: n/a
jobs: []
pi_reviewed: false
---

# The survey's organizing question is the implicit computational quantity, not the attack family

## Scope

The repository holds 85 wiki source pages, about 80 raw documents, and one prior survey artifact, and all three are organized by attack family or by research pillar. This report proposes a different organizing question for the survey, and audits three claims already recorded in the wiki to test whether the present organization propagates overreach. Each audit reads the primary source.

## Result

**Security claims in this area are existential theorems about adversarially constructed objects, and they are restated, in the wiki and in the field, as universal claims about deployed systems; in the audited cases the quantity that would make the claim measurable is already present inside the proof, as an unnamed side condition.**

Three claims were audited and three failed, so the defect is systematic rather than incidental.

| Claim as recorded in the wiki | What the primary source supports | Defect |
| --- | --- | --- |
| No efficient prompt filter can align a sufficiently expressive model, so filter-based audit requirements are provably insufficient | The abstract of arXiv:2507.07341 states "there exist LLMs for which there are no efficient prompt filters"; Theorem 2 additionally requires the model to share a secret key with the attacker | Existential over constructed models read as universal over deployed models; a regulatory conclusion drawn from it |
| Any concentrated metric probability space makes any classifier with nontrivial error inherently vulnerable | The theorem holds, and its hypothesis is measured false for image benchmarks by the same group in arXiv:1905.12202; arXiv:2309.16096 uses the opposite sense of concentration to prove robust classifiers exist | A conditional theorem recorded without its measured antecedent; the refutation is filed as a sibling rather than as a limit |
| Statistically Undetectable Backdoors, forthcoming, with Bogdanov and Rosen | The document held in `raw/` is anonymous and under double-blind review at ICLR 2026 | An inferred de-anonymization recorded as fact |

The first audit also yields the survey's thesis in a single instance. Theorem 1 of arXiv:2507.07341 does not require the filter to be inefficient, it requires the filter to run no faster than the model it audits. That is a ratio between two parties' compute, it is the object the theorem actually turns on, and it is written as a side condition rather than as the quantity being studied.

Generalizing the pattern gives the register the survey should be built on.

| Implicit quantity | Where the field feels it | Where it is stated formally | Status of the crossing |
| --- | --- | --- | --- |
| Attack compute budget | Attack-step counts, query counts, epochs, in every empirical attack paper | Fine-grained cryptography, the gap `δ` | Not crossed |
| Auditor-versus-model compute ratio | Filtering, backdoor detection, watermark detection | Same, as `honest^{1+δ}` | Present as a side condition only |
| Attacker-versus-trainer compute ratio | Proof-of-Learning, Property 2, a bare inequality | Same | Never parameterized |
| Success as a distribution rather than a bit | Reconstruction scored by pixel or perceptual distance | `R` and its tolerance `η` | Partially, on the privacy side |
| Access level | Black-box, gray-box, white-box, used informally | The passive, chosen-plaintext, chosen-ciphertext ladder | Not written as a ladder in this field |
| The baseline | Attack accuracy quoted without a stated null | The baseline field of `R` | Contested from inside the membership-inference literature |
| Which map is inverted | Weights, parameterization, features, conflated | The three maps | Not separated |
| The adversary's algorithm class | The observation that attacks are themselves learners | Low-degree, statistical-query, capacity-bounded adversaries | Crossed in cryptography, not in machine learning |

Does not show: that the register is exhaustive, since it was assembled from three audits and the repository's existing record rather than from a census; the last four rows carry the programme's own prior claims and are restated here rather than re-established.

## How it was produced

| | |
| --- | --- |
| Method | Structural grep of the wiki for overgeneralization markers, then primary-source verification of each hit |
| Sources read | arXiv:2507.07341 abstract; arXiv:1905.12202 abstract, from the copy in `raw/`; arXiv:2309.16096 abstract; the first page of the anonymous submission in `raw/` |
| Also checked | arXiv:2603.19469 and arXiv:2602.01587, suspected fabricated because the prior survey artifact preemptively defends its own identifiers; both resolve and both are correctly recorded |
| Prior artifact assessed | `compass_artifact_wf-6dd26eed`, which is organized by pillar and reproduces the first defect in its own synthesis section |
| Not done | A census of the remaining 82 wiki source pages against their primary sources |
| Artifacts | This report |

## What this changes

The wiki's problem is not coverage, because its 85 source pages already span the raw corpus and the prior artifact. The problem is that a topic-organized wiki has no slot for the antecedent of a conditional theorem, so the antecedent is dropped and the consequent propagates. Organizing the survey by implicit quantity supplies that slot, because a quantity's entry has to record who bounds it, at what value, and under what assumption. The register also makes the programme's own contribution legible as a row rather than as a separate proposal, since `R` is the formal name for the fourth row and the baseline is the sixth. The three failed audits are recorded as a rate, one in one, so the census will report a rate rather than a list.

## Where it applies

| Section | Change |
| --- | --- |
| Survey organization | Adopt the implicit-quantity register as the top-level index; demote attack family and research pillar to a cross-reference axis |
| Wiki schema, root `CLAUDE.md` | Add a required field recording, for each source, the quantifier of its main claim and the antecedent its theorem is conditional on |
| `wiki/sources/filter-impossibility-ai-alignment.md` | Restate the claim as existential; record the shared-key hypothesis of Theorem 2; record the filter-versus-model compute ratio as the operative quantity |
| `wiki/sources/curse-of-concentration.md` | Record the measured antecedent and the opposing sense of concentration as limits, not as siblings |
| `wiki/entities/neekon-vafa.md` | Mark the attribution inferred and unverified, since the held document is anonymous |
| Terminology ledger, [[CONTEXT]] | Record that "concentration" names two opposite geometric properties across the two literatures |
| Open problems | Whether the auditor-versus-model compute ratio in arXiv:2507.07341 Theorem 1 can be stated as a fine-grained gap at an explicit exponent |
