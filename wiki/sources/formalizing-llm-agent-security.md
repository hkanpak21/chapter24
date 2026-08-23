---
title: "A Framework for Formalizing LLM Agent Security"
type: source
date_ingested: 2026-04-12
authors: [Vincent Siu, Jingxuan He, Kyle Montgomery, Zhun Wang, Neil Gong, Chenguang Wang, Dawn Song]
venue: "venue unconfirmed from PDF. The ingested file is arXiv:2603.19469v1, 19 March 2026, and states no venue. Author affiliations on the file are UC Santa Cruz, UC Berkeley, and Duke University."
year: 2026
tags: [llm-security, agentic-systems, formal-models, access-control, adversarial-ml, prompt-injection]
claim_quantifier: empirical
antecedent: "The framework assumes synchronous, turn-based agent execution, one action completing and returning an observation before the next begins. It assumes standard authentication and access-control infrastructure is available. It does not assume the agent has perfect instruction attribution or objective inference, and instead posits oracle functions supplying those. The systematization claim rests on a survey of 87 papers."
adversary_bound: "none. No property, oracle, or definition in the paper bounds the adversary's compute, queries, memory, or any other resource. The threat model restricts the adversary by MODE OF ACCESS only, to operational means rather than training-time manipulation or direct code modification, and the four properties are access-control predicates on an authorization context rather than resource bounds. For the survey, this paper is an empty cell on the adversary-pricing axis."
date_verified: 2026-08-22
cls_target: outputs
cls_family: none
cls_phase: test time
cls_access: black box
cls_write: corpus
cls_frame: none
cls_party: none
cls_unit: none
cls_tightness: unstated
cls_baseline: n/a
cls_second_party: none
cls_second_notion: none
cls_assessed:
cls_evidence: absent
cls_evidence_src: "no bound in the four security properties (§4.2-4.4), the five oracle definitions, or the Threat Model (§3); the page's own adversary_bound field already records this"
cls_reason: "family=none flagged as a vocabulary gap: the paper's nine attack classes (indirect/direct prompt injection, jailbreaking, confused deputy, task drift, capability misuse, cross-context leakage, tool exploitation, memory poisoning) span several codebook families at once, the paper's own primary contribution is the framework rather than any one attack, and the vocabulary has no 'injection' value. access=black box is a judgement call: the paper restricts the adversary by mode rather than resource, verbatim 'attackers who exploit these capabilities through operational means rather than training-time manipulation or direct code modification' (Threat Model, §3), a mode-of-access restriction with no fixed query form, closest to black box among the available values though the paper never uses that term. write=corpus: the described attacks write malicious content into observations/documents/memory that the agent later consumes (indirect injection, memory poisoning), not a read-only query. party/unit/tightness/frame=none/none/unstated/none: no property, oracle or definition bounds the adversary's compute, queries or memory anywhere in the paper, confirmed against the PDF and already stated in the page's own adversary_bound field."
cls_prov: P
cls_date: 2026-08-22
---

> **Verified against the primary source.** The page was checked against
> `raw/S+26_FormalizingLLMAgentSecurity.pdf` on 2026-08-22. Both passages that an earlier ingest
> presented as quotation are near-misses and are corrected in place below.

## Summary

The paper systematizes attacks and defenses on LLM agents from what it calls a contextual perspective.
Its starting observation is that prevailing definitions classify an input or an action by content
alone, so that a prompt embedded in retrieved data counts as an injection regardless of who authorized
it and whether it serves the user's task. That produces a utility and security trade-off, because a
uniform defense generates false positives on legitimate delegated content while a permissive one
follows attacker text.

The framework replaces content-based definitions with a relational one. An execution context `C_t` is
defined as a tuple carrying everything relevant to an authorization decision at step `t`. Four
security properties are then stated over that context, each corresponding to one authorization-relevant
component, and five oracle functions are introduced to supply the information the properties need. Nine
attack classes are recast as violations of specific properties, and existing defenses are recast as
mechanisms that strengthen an oracle approximation or implement a property check. Section 6 sorts
defenses into prevention, detection, and cross-component infrastructure, and reads off which oracles are
approximated well, poorly, or not at all.

The paper contains no numbered definitions, no theorems, and no proofs. It is a systematization built on
a survey of 87 papers, and it says so.

## Claim Boundary

- **Quantified over.** The 87 papers surveyed and the nine attack classes drawn from them. The claim is
  that documented attacks map to violations of one or more of the four properties. It is a coverage
  claim about a literature, checked by inspection, not a theorem about agents.
- **Antecedent.** Synchronous turn-based execution, and the availability of the five oracles as ideal
  specifications. The authors are explicit that the oracles are not implementable as stated, verbatim:
  *"Like ideal functionalities in protocol analysis, these oracles specify theoretical requirements
  rather than claiming practical perfect implementation."*
- **Which party is constrained and in what resource.** Neither party is constrained in a computational
  resource. The **agent** is constrained by an authorization context, which is an access-control
  condition. The **adversary** is constrained only in its mode of access, verbatim: *"Our threat model
  characterizes attackers who exploit these capabilities through operational means rather than
  training-time manipulation or direct code modification."* There is no running-time bound, no query
  budget, and no memory bound anywhere in the paper. On the survey's adversary-pricing axis this paper
  scores none.
- **Does not establish.** It does not establish that the four properties are complete. The authors say
  so themselves, verbatim: *"We do not claim the four properties are formally complete or axiomatically
  derived"*, and *"we cannot prove sufficiency; future research may identify attacks requiring
  additional properties"*. It does not establish that any defense achieves the properties, since the
  oracles are unimplemented. It does not cover training-time attacks. It does not model concurrent or
  asynchronous execution, and it records time-of-check to time-of-use attacks as outside the model. It
  does not model how authorization context propagates across agent-to-agent delegation.
- **Abstract versus theorem.** There is no theorem, so the question reduces to whether the abstract
  claims more than the body. It does not. The abstract describes the work as systematizing and
  reformalizing, and the Discussion section states the contribution modestly in the same terms.

## Key Contributions

- **Execution context.** `C_t = (p, Tr_{t−1}, M_t, E_t, S_auth,t, G)`, where `p` is the user prompt,
  `Tr_{t−1}` the trajectory before step `t`, `M_t` memory, `E_t` environment state, `S_auth,t` the set
  of authenticated sources, and `G = (S, R)` the source permission graph.
- **Four security properties.** Task alignment, action alignment, source authorization, and data
  isolation, each corresponding to one authorization-relevant component of `C_t`.
- **Five oracle functions.** `H_p`, `H_Tr`, `H_a`, `I` and `L`. The permission graph `G` is part of the
  context, not an oracle.
- **An integrated security predicate** combining all four properties, with the source-authorization
  clause stated as a disjunction rather than a conjunct.
- **A taxonomy of nine attack classes** as property violations, in Sections 5.1 to 5.9. Indirect prompt
  injection, direct prompt injection, jailbreaking, confused deputy, task drift and agentic
  misalignment, capability misuse, cross-context information leakage, malicious tool exploitation, and
  memory poisoning.
- **A defense analysis** in Section 6, split into prevention by strengthening oracle approximations,
  detection by implementing property checks, and cross-component defenses such as sandboxing and
  runtime monitoring, followed by open problems.

## Key Definitions / Theorems

The paper numbers no definitions and states no theorems. The following are its formal objects, taken
from Sections 4.2 to 4.4.

- **`H_p : p → O`** extracts the task objective `o_0` from the user prompt, where `O` is the space of
  objectives the agent is permitted to pursue. The paper attributes the boundary of `O` to alignment
  training.
- **`H_Tr : (Tr_{t−1}, o_0) → {0,1}`** judges whether the trajectory so far serves the authorized
  objective.
- **`H_a : (a_t, Tr_{t−1}, o_0) → {0,1}`** judges whether the individual action serves that objective.
- **`I : (a_t, f, M_t, p, Tr_{t−1}) → x`**, the instruction attribution oracle, identifies which inputs
  functioned as instructions leading to action `a_t`, where `f` is the LLM.
- **`L : x → s`**, the source attribution oracle, maps each input to its sources.
- **Integrated security predicate.** `secure(a_t, C_t)` holds if and only if `o_0 ∈ O`, and
  `H_Tr(Tr_{t−1}, o_0) = 1`, and `H_a(a_t, Tr_{t−1}, o_0) = 1`, and for every input `x` and every source
  `s ∈ L(x)` either `s ∈ S_auth,t` or `H_a(a_t, Tr_{t−1}, o_0) = 1`, and for every source `s ∈ L(x)` and
  every destination source `s'` the pair `(s, s')` lies in `R`. The disjunction in the
  source-authorization clause is deliberate. It lets an unauthenticated source that causes an action
  pass when the action independently satisfies action alignment, which is the case of a user delegating
  to external content.
- **Attack formalizations.** Indirect prompt injection is defined as requiring **both** an
  unauthenticated source in `L(x)` and `H_a(a_t, Tr_{t−1}, o_0) = 0`, which the paper contrasts with the
  prior definition requiring only that the instruction not come from the prompt. Cross-context leakage
  is a violation of the permitted flow relation `R`. Jailbreaking is an objective lying outside `O`.
  Confused deputy is a source-authorization failure arising from the agent's permissions exceeding the
  user's.

## Connections

- [AIOracle Framework](../concepts/aioracle-framework.md). The two are complementary in scope, one
  covering learning and inference phases and this one covering action execution at runtime. The
  comparison is an outside observation. This paper does not mention AIOracle.
- [Attack Taxonomy for LLMs](../concepts/attack-taxonomy-llms.md), which this paper's nine classes
  extend along an authorization-context dimension.
- [Extending the Formalism of Cryptography to AI](extending-formalism-cryptography-ai.md).
- Defenses whose guarantees are stated in this framework's terms:
  [CaMeL](camel-defeating-prompt-injections.md), which enforces flow constraints by construction, and
  [MELON](melon-indirect-prompt-injection.md). Neither is named in this paper, which cites defenses by
  reference number.
- Entities: [Vincent Siu](../entities/vincent-siu.md), [Dawn Song](../entities/dawn-song.md).

## Open Questions / Limitations

- **Oracle implementation.** `I`, `L`, `H_p`, `H_Tr` and `H_a` are ideal specifications with no
  algorithm realizing them. The paper is direct about why, verbatim, on the instruction attribution
  oracle: *"it cannot be evaluated without solving causal attribution, it treats instruction-ness as
  binary when influence is continuous"*. It suggests LLM agents may need explicit architectural
  mechanisms to separate instructional from informational inputs.
- **Approximation quality.** Real systems substitute attention mechanisms for `I`, LLM judges for
  `H_Tr` and `H_a`, and embedding similarity for `H_p`. What approximation quality suffices for a
  practical guarantee is recorded as open.
- **Completeness.** The four properties are not proved sufficient.
- **Compositional security.** Individually secure actions may combine into a violation, and the paper
  records that reasoning about this requires tracking how `E_t` evolves across the whole sequence,
  which current property checks do not do.
- **Temporal and concurrent settings.** Time-of-check to time-of-use attacks and dynamic environments
  with concurrent actors are outside the model.
- **Benchmarks.** Existing benchmarks do not record which sources are authenticated, which objectives
  are authorized, or which flows are permitted, so the properties cannot be evaluated on them.
- **Training-time attacks** are out of scope by the threat model.

## Quotes / Notable Passages

> _Not verbatim as previously recorded. Checked against `raw/S+26_FormalizingLLMAgentSecurity.pdf` on
> 2026-08-22. The earlier text read "Security in LLM agents is inherently contextual — the same action
> may be legitimate or a violation depending on authorization context." Its opening clause is the
> paper's, and the remainder is a compression of the paper's own sentence rather than a fabrication.
> The abstract's exact wording follows._

> "Security in LLM agents is inherently contextual. For example, the same action taken by an agent may
> represent legitimate behavior or a security violation depending on whose instruction led to the
> action, what objective is being pursued, and whether the action serves that objective."

> _Not verbatim as previously recorded. Checked against the same file on 2026-08-22. The earlier text
> read "The paper's primary contribution is making implicit security requirements explicit... clarity
> enables both incremental improvements to approximation techniques and identification of entirely
> unaddressed research areas." The paper says "framework's" rather than "paper's primary", "implicit
> requirements" rather than "implicit security requirements", "improvements in" rather than
> "improvements to", and "unaddressed challenges" rather than "unaddressed research areas". The
> substrate is the paper's and the wording is not. The exact sentences from the Discussion follow._

> "This framework's contribution is making implicit requirements explicit. Current defenses fail not
> due to insufficient effort but because they lack clarity on what contextual authorization requires.
> Formalizing security through oracle functions and properties provides this clarity, enabling both
> incremental improvements in approximation techniques and identification of entirely unaddressed
> challenges."

On what the framework is and is not, from Section 4.1:

> "Security is therefore a relational property between an action and a context, not an intrinsic
> property of the action itself."

On the evidential basis of the taxonomy:

> "our analysis of 87 papers reveals that documented attacks map to violations of one or more
> properties"
