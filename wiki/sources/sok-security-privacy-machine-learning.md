---
title: "SoK: Security and Privacy in Machine Learning"
type: source
date_ingested: 2026-08-22
authors: [Nicolas Papernot, Patrick McDaniel, Arunesh Sinha, Michael P. Wellman]
venue: "IEEE EuroS&P 2018"
venue_evidence: "https://dblp.uni-trier.de/search?q=SoK%20Security%20Privacy%20Machine%20Learning; dblp: EuroS&P 2018, pp. 399-414"
year: 2018
tags: [adversarial-ml, evasion-attacks, poisoning-attacks, learning-theory, robustness]
claim_quantifier: empirical
antecedent: "None. The systematization's take-aways are assertions about the surveyed corpus, selected as \"seminal and representative works\", not consequences of a hypothesis."
adversary_bound: "None. The taxonomy's capability axes are pipeline stage, phase (training or inference), access (white-box or black-box), and write power (read, injection, modification, logic corruption). No axis is a computational resource. Section 5.2 reports one query-complexity notion from prior work (ACRE learnability), but it is a surveyed result, not a dimension of the threat model."
date_verified: 2026-08-20
cls_target: none
cls_family: multiple
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
cls_evidence_src: "no computational-resource axis in §3.1 (attack surface), §3.3 (adversarial capabilities), or §3.4 (adversarial goals); Kearns et al.'s poisoning-fraction bound (§4) and Lowd et al.'s ACRE learnability (§5.2, 'using a polynomial number of queries to the ML oracle') are surveyed results attributed to prior papers, not the taxonomy's own axes (Rule 8)"
cls_reason: "Re-verified §3 directly against the PDF for this task: the threat model is three parts, not four independent axes — §3.1 attack surface (pipeline stage), §3.3 adversarial capabilities (phase: training or inference; within each, ONE strength ladder that is phase-conditioned, not two simultaneous axes — training uses read-access to injection to modification to logic-corruption ['write power'], inference uses black-box to white-box ['access level'] — these are mutually exclusive instantiations of a single capability dimension, never both at once), and §3.4 adversarial goals (confidentiality, integrity, availability, privacy). §3.2 trust model (four actor classes: data owners, system providers, consumers, outsiders) is a further, separate layer that fits none of the four axes named in the task brief. The brief's characterization ('pipeline stage, attacker write power, access level and goal') is close in content but structurally imprecise: it omits phase as the switch between the write-power and access-level ladders, and lists write power and access level as if independently combinable, when the paper applies exactly one or the other depending on phase. The novelty premise itself holds: none of pipeline stage, phase, write power/access, or goal is a computational resource; §5.2's ACRE learnability (query complexity, NP-hardness for discrete features) is the paper's single closest approach and is explicitly a reported result, not a taxonomy dimension. target/family/phase/access/write are none/multiple/n/a/none/none because the paper's own claim is the taxonomy itself, spanning all pipeline stages and all attack families (poisoning, evasion, membership inference, extraction, inversion) rather than committing to one."
cls_prov: P
cls_date: 2026-08-22
---

> **Provenance.** Read from the primary PDF: abstract, §1, §2, §3 (attack surface, trust model,
> adversarial capabilities, adversarial goals), §4 (training-time attacks), §5 (inference-time attacks,
> white-box and black-box), §6 (robustness, privacy, fairness and accountability), §7. All eight numbered
> take-aways located; §3 read in full for the taxonomy's axes.

## Summary

This is the systematization the membership-inference and reconstruction literature was written against,
and it is organised around a threat model in three parts. §3.1 fixes the **attack surface** as a
generic data-processing pipeline — collect features, process them in the digital domain, run the model,
communicate and act on the output — instantiated for a vision system and a network intrusion detector,
so that an attack is located by which pipeline stage it touches. §3.3 fixes **adversarial capabilities**
along two axes: the *phase*, training or inference; and, within each, a strength ordering. At training,
that ordering runs read access → injection → modification → logic corruption. At inference, it runs
black-box (probing) → white-box (architecture, parameters, training data, or combinations). §3.4 fixes
**adversarial goals** as the CIA triad with privacy added as a fourth property, and observes that
integrity pairs with availability in method while confidentiality pairs with privacy.

§3.2 adds a **trust model** layer, assigning trust to four classes of actor — data owners, system
providers, consumers, outsiders — and states that the paper is not proposing good trust models but
exploring the space *"by viewing them through the prism of the adversarial capability space"*.

§4 surveys training-time attacks, mostly poisoning, and §5 inference-time attacks, split by white-box
and black-box access; the privacy subsections of each cover membership inference, model inversion and
model extraction. §6 surveys defences under three headings, robustness to distribution drift, learning
and inferring with privacy, and fairness and accountability. The paper's own summary of where the
science should go is that the field needs a notion of **sensitivity** — of learning algorithms to their
training data, and of deployed models to their inputs — and the abstract proposes PAC theory as the
model for it.

**On the axis the survey positions against: this systematization has no computational-resource axis.**
The claim is stated here in the form a novelty check should be able to falsify. Across the paper, the
adversary's power is graded by *access* and by *write capability*, never by time, circuit size or
compute budget. The three places where a resource-like quantity appears are all local to a surveyed
result rather than to the taxonomy: §4 reports Kearns et al.'s poisoning fraction `β`, a data-corruption
budget; §4's framing sentence uses "unbounded" to mean unbounded *poisoning power*, not unbounded
computation — *"It is somewhat obvious that an unbounded adversary can cause the learner to learn any
arbitrary function h leading to complete unavailability of the system. Thus, all the attacks below bound
the adversary in their attacks"*; and §5.2 reports Lowd et al.'s **ACRE learnability**, which asks for
the least-cost modification of a malicious input *"using a polynomial number of queries to the ML
oracle"*, along with the result that continuous features permit ACRE learnability while discrete
features make the problem NP-hard. That is a query-complexity and worst-case-hardness result, faithfully
reported, and it is the closest the paper comes. It is not one of the axes of §3.

## Claim Boundary

- **Quantified over:** the literature the authors selected. They say so: *"Based on our analysis of the
  ML threat model, we have selected seminal and representative works from the literature. While we
  attempt to be comprehensive, it is a practical impossibility to cite all works."* The work is dominated
  by supervised classification, stated explicitly, and excludes trusted computing platforms for ML and
  AI-safety questions.
- **Antecedent:** none. Nothing here is a conditional theorem.
- **Which party is constrained, and in what resource:** neither, computationally. Adversaries are
  constrained by access, by phase, and by the fraction of training data they may alter. Defenders are
  discussed under sensitivity, robustness and DP, none of which is a resource bound on an attacker.
- **The success criterion:** varies by attack class and is inherited from each surveyed paper, not
  unified. For integrity attacks it is inducing a chosen output; for privacy attacks it is the membership
  test, recovery of partially known inputs, or extraction of training data via predictions; for
  availability it is degrading quality, performance or access. The paper does not impose a common success
  predicate and does not parameterize any of them by a tolerance.
- **The baseline:** not stated. No section defines what an attack's success should be compared against.
- **Does not establish:**
  - **not** a formal threat model in the cryptographic sense. There is no game, no advantage, no
    security parameter, and no definition environment. §3 is a classification scheme.
  - **not** that its capability ordering is total. "Stronger" and "weaker" label the ends of the
    training and inference axes; no ordering is proved, and the two axes are not compared to each other.
  - **not** that the CIA-plus-privacy partition is exhaustive. The paper itself notes that availability
    *"is however ill deﬁned for a model in isolation"*.
  - **not** any statement about the compute an attack requires. A claim that no prior systematization
    prices the adversary in compute is consistent with this paper's contents, and this paper is the
    strongest single place such a claim could have failed.
  - **not** a survey of adversarial-example defences that survived. It predates most of the adaptive-attack
    literature, and its own take-away 6.1 already says defences that tamper with crafting heuristics are
    the wrong shape.
- **Abstract vs theorem:** the abstract's last sentence — that constructing a theoretical understanding
  of algorithm sensitivity *"à la PAC theory, will foster a science of security and privacy in ML"* — is
  a research proposal, and §7 restates it as such. No theorem is claimed and none is offered, so there is
  no gap to record, only the observation that the abstract's confident register is not backed by a
  result.

## Key Contributions

- The **three-part threat model**: attack surface (pipeline stage), adversarial capabilities (phase ×
  access, with a strength ordering), adversarial goals (confidentiality, integrity, availability,
  privacy).
- The **trust model** as a separate layer over four actor classes, and the observation that a trust
  model can be read off the capability space.
- The pairing observations: integrity with availability in method, confidentiality with privacy in
  method.
- A unified survey of training-time and inference-time attacks that had until then been reported in
  separate communities.
- Eight numbered take-aways, of which three matter for how the field later specified success:
  take-away 4.1, that loose generalization bounds make the impact of poisoning hard to quantify;
  take-away 6.1, that any defence tampering with adversarial-example crafting heuristics is
  misdirected; and take-away 6.3, that *"Precisely quantifying the learning algorithm's sensitivity to
  training points is necessary to establish differential privacy guarantees."*
- The framing of **sensitivity** as the common quantity behind both security and privacy failures.

## Key Definitions / Theorems

None of its own. The paper defines its taxonomy in prose and reports definitions and results from the
surveyed work, of which two are worth recording because they are the only resource-flavoured objects in
the paper:

- **Kearns et al.'s poisoning bound**, reported in §4.1: achieving inference error `ε` requires
  `β ≤ ε/(1+ε)`, where `β` is the probability with which the adversary may modify a training sample.
- **ACRE learnability**, reported in §5.2 from Lowd et al.: find the least-cost modification making a
  malicious input classify as benign, *"using a polynomial number of queries to the ML oracle"*.
  Continuous features admit ACRE learnability; discrete features make it NP-hard. Nelson et al.'s
  convex-inducing classifiers are ACRE learnable but not necessarily reverse-engineerable.

## Connections

- [Adversary Knowledge Taxonomy](../concepts/adversary-knowledge-taxonomy.md),
  [SoK on Adversary Knowledge](sok-adversary-knowledge.md) — the later, finer treatment of this paper's
  white-box/black-box axis.
- [Attaxonomy](attaxonomy.md), [Attack Taxonomy for LLMs](../concepts/attack-taxonomy-llms.md) — the
  successor taxonomies.
- [Poisoning Attacks](../concepts/poisoning-attacks.md), [Evasion Attacks](../concepts/evasion-attacks.md),
  [Input Manipulation Threat Model](../concepts/input-manipulation-threat-model.md) — the categories §4
  and §5 populate.
- [Model Extraction](../concepts/model-extraction.md),
  [Jagielski et al., Model Extraction](jagielski-model-extraction.md) — the confidentiality goal of §3.4,
  later given a fidelity-versus-accuracy split this paper does not have.
- [Membership Inference Attacks Against Machine Learning Models](membership-inference-shokri.md) — the
  membership test named in §3.4 as a privacy risk.
- [Privacy Risk in Machine Learning](privacy-risk-overfitting.md) — contemporaneous, and supplies the
  formal game that this systematization does not adopt.
- [Deep Learning with Differential Privacy](deep-learning-differential-privacy.md) — the practical DP
  work §6.2 surveys.
- [PAC Learning](../concepts/pac-learning.md) — the theory the abstract nominates as the model for a
  science of ML security.
- [Do's and Don'ts of Machine Learning in Computer Security](dos-and-donts-ml-security.md) — the
  methodological successor.
- [On Evaluating Adversarial Robustness](on-evaluating-adversarial-robustness.md),
  [Obfuscated Gradients](obfuscated-gradients.md), [RobustBench](robustbench.md) — the evaluation
  literature that grew out of take-away 6.1.

## Open Questions / Limitations

- §7 leaves the central quantity, sensitivity, undefined in both of its senses, and states that the
  sensitivity of generalization error *"remains poorly understood for many models (including neural
  nets) and calls for further research."*
- Take-away 6.3 identifies loose sensitivity bounds for non-convex models as the obstacle to useful DP
  guarantees, and offers no route past it.
- The capability axes are not given a formal ordering, so "stronger adversary" is not a relation the
  taxonomy can compute.
- The systematization predates the low-FPR evaluation debate, the informed-adversary reconstruction
  results, and distribution inference as a named category, all of which change what the privacy row of
  §3.4 should contain.
- No axis of the taxonomy measures what an attack costs. Whether adding such an axis would reorganise
  the classification is not asked.

## Quotes / Notable Passages

> We articulate a comprehensive threat model for ML, and categorize attacks and defenses within an
> adversarial framework.

(Abstract, stating the taxonomy's scope.)

> The term capabilities refers to the whats and hows of the available attacks, and deﬁnes the possible
> attack vectors on a threat surface.

(§3.3. "Capabilities" is defined as attack vectors, not as resources. The `ﬁ` ligature is as extracted.)

> It is somewhat obvious that an unbounded adversary can cause the learner to learn any arbitrary
> function h leading to complete unavailability of the system. Thus, all the attacks below bound the
> adversary in their attacks

(§4. The only use of "unbounded adversary" in the paper, and it means unbounded control over training
data.)

> Precisely quantifying the learning algorithm's sensitivity to training points is necessary to
> establish differential privacy guarantees. For non-convex models (e.g., neural nets), current loose
> bounds on sensitivity require that learning be heavily randomized to protect data—often at the expense
> of utility.

(Take-away 6.3.)

> Characterizing the sensitivity of learning algorithms to their training data is essential to
> privacy-preserving ML.

(§7.)
