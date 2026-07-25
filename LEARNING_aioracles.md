# Learning Doc — "AIOracles for Practitioners" (Durak et al.)

Source: `raw/AIOracles_for_Practitioners.html` ("Introduction to AIOracles")
Wiki summary: `wiki/sources/extending-formalism-cryptography-ai.md`
Author of note: F. Betül Durak (Microsoft Research) + co-authors (Villa, Kohno, Maharramli, Roesner)

Goal: deep understanding — the problem, the solution & its design decisions/edge cases, and why it matters.
Legend: [ ] not yet · [~] partial · [x] mastered

---

## Stage 1 — The Problem (the *why behind the why*)  ✅ LOCKED
- [x] 1.1 What was wrong: ad-hoc, no shared vocabulary, *implicit specifications* can't be reasoned about
- [x] 1.2 Why: AI security grew attack-first; crypto grew definition-first (definition precedes reduction)
- [x] 1.3 The core obstacle: you can't even *state* φ (intent/appropriateness/harmlessness aren't formal objects)
- [x] 1.4 The branch: idealize-and-decompose (NOT fixed-policy, which the note rejects)
- [x] 1.5 Deeper open question: for which φ is ε-secure approximation even possible? (Bellare–Kohno analogue)
- [x] KEY DISTINCTION: idealize/name φ (ground-truth, maybe uncomputable) vs implement φ (bounded judge E; ε = the gap)

## Stage 2 — The Solution: the AIOracle abstraction  ✅ LOCKED
- [x] 2.1 Definition + pipeline: source→GENERATE_DATA→corpus→LEARN→model→INFER→result, with φ judging the result
- [x] 2.1b LEARN phase (training, pre-deploy) vs INFER phase (runtime) = WHERE IN TIME the attacker struck
- [x] 2.2 "Everything is an AIOracle" → one vocabulary → reduce/reuse theorems across systems
- [x] 2.3 Two numbers: completeness p (benign use, no adversary) vs security ε (adversarial worst case)
- [x] 2.4 A real security claim has THREE legs: ε-secure FOR φ AGAINST ATK (drop one → meaningless)
- [x] 2.4b ATK flavors: observe {white_box, black_box} vs tamper {inject_learn, inject_infer} = which pipeline arrow

## Stage 3 — The Four Results
- [x] 3.1 §4 Utility–privacy tradeoff: GLM + MID game ⇒ p_c ≤ 1/2 + n·ε ; ε ≥ (p_c−1/2)/n. "Useful classifier must leak membership."
- [x] 3.2 §4 GLM = Shoup generic-group analogue; blocks the SEMANTIC SHORTCUT → makes "any useful classifier" a uniform quantifier. Proof = game-hopping reduction. Template: game + generic model + reduction.
      KEY: above-chance accuracy = aggregate membership leakage summed over n points (hybrid). n = # leakage channels; more data HELPS privacy (dilution), not hurts.
- [x] 3.3 §5 Dual construction = search/decision (NP) split: CAIO=Creative=generator(φ₂), BAIO=Boring=filter/classifier(φ₁). Propose-then-check.
- [x] 3.4 §5 Failure probs ADD: complete 1−((1−p₁)+(1−p₂)+e); secure ε₁+ε₂+e (union-bound). e = generator/filter coverage-mismatch (satisfies φ₂ not φ). e SMALL via alignment/RLHF (event rare); e ZERO via no-DoS (∅ acceptable → event costs nothing). e = price of insisting on non-empty answer.
- [x] 3.5 §5 Multi-step agent = repeated `proceed`; union bound → n·ε per trajectory. Two levers: lower per-call ε OR shorten n. Security degrades LINEARLY with run length.
- [x] 3.6 §6 7 sub-predicates / 3 groups: Action{allow,intent} Data{content,correct,useful} Flow{inflow,outflow}. φ=∧ of all 7. Gives ATTRIBUTABILITY (which sub-predicate, which call → 7×k matrix).
      Hardness gradient: clean{outflow,allow,inflow} / classifier-inheriting{content=§4} / open{intent,useful}. NOTE my insight: outflow has a clean recipient-boundary half + a HARD content-laundering (covert-channel) half. "open" = required evaluator complexity unbounded.
- [x] 3.7 §6 4 steps: decompose φ → pick ATK → choose EVALUATOR (co-equal part of spec!) → state falsifiable claim "S is ε-ATK-secure for φ_i under evaluator E by procedure P". Evaluator changes the ε: LLM judge adds its ε to composed bound; human rubric = offline ground-truth, no runtime ε. Template = cure for Stage-1 disease (implicit→explicit/shared/falsifiable; one sentence for defender/red-team/procurement/reviewer).
- [x] 3.8 §7 Ball et al. (Goldwasser et al. 2025) impossibility. Covert channel: CAIO′ hides a signal readable only at φ-complexity; a BAIO below φ-complexity CANNOT COMPUTE the distinguisher → blind. ⇒ filter complexity ≥ predicate complexity (lower bound on BAIO).
      SCOPE LIMITERS: (i) underpowered BAIO; (ii) JOINT CORRUPTION — attacker controls BOTH generator (inject_learn) AND judge (replace φ→φ′). Does NOT cover inject_infer-only (ordinary prompt injection). Does NOT say defenses impossible / dual construction unsound.
      PREDICTION (§7×§6): a cheap reliable φ_intent judge is PROVABLY impossible — φ_intent is open/high-complexity, so any sound judge must be high-complexity too. Complexity reason, not engineering laziness.

## Stage 4 — Why It Matters (broader context & impact)  ✅ LOCKED
- [x] 4.1 Thesis: the contribution is a PARADIGM/VOCABULARY shift, not the 4 theorems. The theorems are DEMONSTRATIONS the vocabulary is productive (prove / compose / specify / re-read).
- [x] 4.2 Methodological import of crypto culture (define-first, reduction, falsifiable claim). Connects to wiki "Chapter 24" = the FOUNDATION layer (eval=U, Kt-complexity); AIOracle = the INTERFACE layer; meet at φ ↔ (task, bounded judge). New frontier: intent-conditioned authorization φ_allow∧φ_intent.
- [x] 4.3 Practice: comparable claims, explicit threat models (ATK), attributable failures (which sub-predicate), named design levers (ε vs n; BAIO≥φ; alignment vs postfilter=e).

## THE SPINE (one principle unifying the whole document)
Capability must be PAID FOR from a metered budget — you cannot be useful, distinguish, or certify beyond the complexity/information you have.
- §4: budget = corpus information absorbed; BILL = membership leakage (GLM forces this; utility==leakage).
- §6: budget = certification cost (clean O(1) → classifier → open/unbounded φ_intent).
- §7: budget = compute (filter can't detect what it can't compute; BAIO ≥ φ).
φ_content SQUEEZE: §4 caps its privacy (useful ⇒ leaks membership) + §7 caps its cheapness (judge ≥ φ_content complexity).

---

## Session result
Mastered: all 4 stages. Self-identified fuzzy corner (§4 membership inheritance) resolved.
Strongest independent move: re-derived "filter complexity must match predicate complexity" (§7) from the φ_outflow content-laundering objection BEFORE reading §7.
