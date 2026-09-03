---
title: What Does it Mean for a Language Model to Preserve Privacy?
type: source
date_ingested: 2026-08-20
authors: [Hannah Brown, Katherine Lee, Fatemehsadat Mireshghallah, Reza Shokri, Florian Tramèr]
venue: "FAccT 2022"
venue_evidence: "dblp: conf/fat/BrownLMST22, inproceedings, pp. 2280-2292, doi:10.1145/3531146.3534642"
year: 2022
tags: [privacy, differential-privacy, memorization, language-models, definitions]
claim_quantifier: conditional
antecedent: "That private information in natural language does not respect the boundaries of the data unit being protected — secrets have no fixed borders, span text written by several people, can concern people who contributed no data at all, and are held by in-groups of unbounded size. Where this fails (structured records, an individual's own search history), the paper says the existing guarantees are adequate."
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
cls_second_notion: none
cls_assessed:
cls_evidence: "absent"
cls_evidence_src: "no adversary or resource bound in Def 1 or elsewhere; wiki Claim Boundary, 'Does not establish ... anything about adversary resources'"
cls_reason: "This is a definitional critique of DP's unit of protection, not an attack or a bound; the paper explicitly disclaims addressing adversary resources (Claim Boundary, Connections axis contrast), so all attack-scenario and adversary-assumption fields are none/n/a per rule 2."
cls_prov: F
cls_date: 2026-08-22
---

## Summary

**This is a critique of the DEFINITION, and it is on a different axis from the evaluation critiques.** The other evaluation papers fault *practice*. This one faults what a privacy definition takes as its **unit of protection** — the object whose presence or absence the guarantee is about. It says nothing about who is attacking or with what resources, and it must not be cited as evidence about adversary capability.

BLM+22 argues that the two dominant data-protection techniques for language models, data sanitization and differential privacy, make structural assumptions that natural language violates. Sanitization assumes private information "can be formally specified, easily recognized, and efficiently removed"; DP assumes the training data decomposes into records that "logically map to individual pieces of private information to be protected". For natural language neither holds: a secret has no crisp borders, it can be referred to obliquely and thus survive removal of its literal statement, it is routinely written by and shared among groups, and its in-group has no upper bound.

The consequence for DP is precise and is the paper's central technical point. ε-DP is stated over datasets differing in one **record**, so the semantics of the guarantee depend entirely on what a record is. Prior work has used tokens, words, sentences, documents, or all of a user's data. Word- and sentence-level records are convenient for training but nearly meaningless as privacy, since deleting one sentence rarely removes a piece of private information. User-level DP — the reading the authors say the original DP definition intends — is the right granularity in principle, but still fails, because removing everything one user wrote does not remove information that others also wrote about them. The ideal would be "secret-level" DP, insensitivity to the addition or removal of any piece of private information, but satisfying it "would require precisely understanding the context and boundaries of secrets, which is exactly a difficulty that DP aims to avoid."

Two further asymmetries. Group privacy degrades exponentially in group size k, whereas the *sensitivity* of information does not decrease as more people know it. And privacy in the paper's sense is contextual — Nissenbaum's contextual integrity — so a model preserves privacy only if it reveals a secret in the right contexts and to the right people, a three-part condition (contexts, content, in-group) each part of which is hard to determine. The paper's conclusion is a recommendation, not a theorem: language models should be trained on text explicitly produced for public use, and public availability should not be confused with intent to be public.

The paper is careful about what it is not claiming. It states plainly that DP's formal guarantees hold regardless of these relationships; what is questioned is what they *mean* semantically. That distinction is the reason this page exists.

## Claim Boundary

- **Quantified over:** data-protection *mechanisms* for language data — sanitization techniques and DP training algorithms at any record granularity. It does not range over adversaries, attacks, or attack classes; the inference attacks in §3 are cited as motivation, not analysed.
- **Antecedent:** that private information in natural language does not align with any fixed data unit — no crisp secret borders, secrets distributed across authors, secrets about non-contributors, unbounded in-groups. The paper is explicit that where the antecedent fails the criticism lapses: DP "is useful for specific types of structured data, for example, when each individual contributes a record that contains sensitive attributes about them", or "when a user's secrets are indeed restricted solely to text written by that user (e.g., an individual's search history)".
- **Does not establish:** (i) that DP is unsound or that its bounds fail — the authors say the opposite, and add that in practice DP bounds are often loose, so true leakage is *less* than computed; (ii) that any specific attack succeeds; (iii) **anything about adversary resources.** The DP adversary here is the standard unbounded one implicit in Def 1. There is no compute, sample, or query budget anywhere in the paper. Citing this as evidence that privacy definitions fail to price the adversary would be a category error: it argues they fail to *scope the protected object*, which is the orthogonal axis.
- **Abstract vs theorem:** no formal overstatement, since there are no theorems. One framing hazard: the abstract's "existing protection methods cannot guarantee a generic and meaningful notion of privacy for language models" reads as universal, while the body is conditional and names the structured-data cases where the methods do work. Read the abstract's "generic" as load-bearing.

## Key Contributions

- **Names the unit of protection as the locus of the problem.** "Protecting a specific unit of data is not the same as protecting privacy" is a section heading, and is the paper's most portable sentence.
- **A granularity ladder for the DP record** — token, word, sentence, document, user — with an argument for why each level fails on language data, and an identification of user-level DP as the definition's intended reading.
- **"Secret-level" DP named as the ideal and shown to be self-defeating**: it requires exactly the boundary knowledge DP was designed to avoid needing.
- **A structural taxonomy of secrets** (Table 1) along four axes: whether the secret is formatted, how many owners it has, in-group size, and whether the in-group shares it further — from (formatted, 1 owner, in-group 1) for a password file, to unformatted secrets with unbounded owners and in-groups.
- **The group-size argument**: k-DP degrades exponentially in k while real sensitivity does not, so community-level secrets get no meaningful guarantee.
- **Contextual integrity as the target notion**, with the operational requirement that a user's data never appear or be inferable outside the context it was expected in.
- **The positive recommendation**: train on text explicitly produced for public use; individual informed consent is not achievable, since one user cannot speak for text about them written by others, and the risks are not yet quantified.

## Key Definitions / Theorems

- **Definition 1 (ε-Differential Privacy, quoted from Dwork et al.)**: A satisfies ε-DP iff for any D, D′ differing in only one record and any output set S, Pr[A(D) ∈ S] ≤ e^ε Pr[A(D′) ∈ S]. The paper's entire argument turns on the undefined term "record".
- **User-level DP** (informal): the trained model is insensitive to the addition or removal of all data written by any individual user.
- **Secret-level DP** (informal, proposed as the ideal and rejected as unattainable): the algorithm is insensitive to the addition or removal of any piece of private information.
- **Privacy-preserving LM** (informal, §4): a model that reveals private information only in the right contexts and to the right people, decomposing into (1) permissible contexts, (2) content of the secret, (3) the in-group.

## Connections

- Direct target: [Deep Learning with Differential Privacy (ACG+16)](deep-learning-differential-privacy.md) — DP-SGD is the mechanism whose record granularity is at issue.
- Formal privacy definitions elsewhere in the wiki whose unit of protection is worth comparing: [Xiao — Formal Privacy Proof for Data Encoding](xiao-formal-privacy-proof-data-encoding.md), [Cohen et al. — Data Reconstruction](cohen-data-reconstruction.md), [Kaplan et al. — Bayesian Memorization and Reconstruction](kaplan-bayesian-memorization-reconstruction.md), [Dinur–Nissim](dinur-nissim-revealing-information.md).
- **Axis contrast:** [Dos and Don'ts of ML in Computer Security](dos-and-donts-ml-security.md) and the three backdoor evaluation papers fault practice and threat-model *statement*; this paper faults the protected *object*. Both are distinct from a third axis, the adversary's resources, which none of them addresses.
- Concepts: [Computational vs Statistical Memorization](../concepts/computational-vs-statistical-memorization.md), [Unit of Protection](../concepts/unit-of-protection.md).
- Author: [Reza Shokri](../entities/reza-shokri.md).

## Open Questions / Limitations

- A position paper. No theorems, no experiments, no proposed mechanism; the constructive output is a data-sourcing recommendation.
- The recommendation — train only on text explicitly produced for public use, "both at present and into the future" — is not operationalized, and the authors give no test for that intent.
- Secret-level DP is named as the ideal and immediately dismissed as requiring the boundary knowledge DP avoids. Whether an intermediate unit exists between user-level and secret-level is left open. Footnote 5 considers expanding "user data" to all conversations a user participated in, and shows this is both technically harder under federated learning and still insufficient.
- The authors ask, without answering, "whether the formal underpinnings of DP necessarily make it the privacy notion of choice for training LMs, or whether other approaches could provide for more semantically meaningful (albeit possibly only heuristic) forms of privacy protection."
- No adversary model of any kind is developed. The paper reasons about what a guarantee means, not about who could break it or at what cost.

## Quotes / Notable Passages

> "Protecting a specific unit of data is not the same as protecting privacy."

> "the main issue with applying DP to language data arises in how we define the boundaries of private information. That is, how should we define what constitutes a data “record” in Definition 1."

> "withholding any specific unit of data from the dataset cannot guarantee protection of privacy."

> "Ideally, we would like to achieve “secret-level” differential privacy... But satisfying such a definition would require precisely understanding the context and boundaries of secrets, which is exactly a difficulty that DP aims to avoid."

> "It is important to note, however, that the formal guarantees of DP hold regardless of such relationships in the dataset D. What is questioned here is what these data protection guarantees mean, semantically, for the protection of users’ privacy."

> "the fact that some information is shared among more individuals does not necessarily make it less sensitive."
