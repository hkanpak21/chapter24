# Learning Doc — "AIOracles for Practitioners" (Durak et al.)

Source: `raw/AIOracles_for_Practitioners.html` ("Introduction to AIOracles")
Wiki summary: `wiki/sources/extending-formalism-cryptography-ai.md`
Author of note: F. Betül Durak (Microsoft Research) + co-authors (Villa, Kohno, Maharramli, Roesner)

Goal: deep understanding — the problem, the solution & its design decisions/edge cases, and why it matters.
Legend: [ ] not yet · [~] partial · [x] mastered

---

## Stage 1 — The Problem (the *why behind the why*)
- [ ] 1.1 What was wrong with the state of agentic-AI / LLM security before this framework
- [ ] 1.2 Why that state existed (how AI security grew vs. how cryptography grew)
- [ ] 1.3 The core obstacle: specification (φ) is hard because human intent is ambiguous
- [ ] 1.4 The branch/tension: give up on formalism vs. idealize-and-decompose
- [ ] 1.5 The deeper open question: "for which predicates is ε-secure approximation even possible?"

## Stage 2 — The Solution: the AIOracle abstraction
- [ ] 2.1 Definition: (GENERATE_DATA, LEARN, INFER) + idealized predicate φ(prompt, context, result) ∈ {0,1}
- [ ] 2.2 Why "a classifier / chatbot / multi-tool agent is all an AIOracle" — what unification buys you
- [ ] 2.3 The two characterizing quantities: completeness p (benign) and security ε vs ATK
- [ ] 2.4 The ATK set {white_box, black_box, inject_learn, inject_infer} = which pipeline arrow the adversary controls

## Stage 3 — The Four Results
- [ ] 3.1 §4 Utility–privacy tradeoff: GLM + MID game ⇒ p_c ≤ 1/2 + n·ε (and what it forbids)
- [ ] 3.2 §4 Why the GLM (generic model) is needed; the game-hopping reduction methodology
- [ ] 3.3 §5 Composition: dual construction CAIO (creative/generator) + BAIO (boring/filter)
- [ ] 3.4 §5 The composition bound ε₁+ε₂+e and the meaning of the slack term e
- [ ] 3.5 §5 Multi-step agents and the n·ε union bound (the two levers)
- [ ] 3.6 §6 The 7 sub-predicates in 3 groups; clean vs classifier-inheriting vs open
- [ ] 3.7 §6 The 4-step recipe to specify φ (decompose, pick ATK, choose evaluator, state falsifiable claim)
- [ ] 3.8 §7 Ball et al. impossibility: "filter complexity must match predicate complexity"; what it does NOT say

## Stage 4 — Why It Matters (broader context & impact)
- [ ] 4.1 The falsifiable-claim template as a shared language for defender/red-team/procurement/reviewer
- [ ] 4.2 How this connects to cryptography's methodology (and to the wiki's "Chapter 24" foundation)
- [ ] 4.3 What it changes about how we build & evaluate agentic systems

---

## Notes & gaps as we go
(filled in during the session)
