# Audit findings, 2026-08-20 to 2026-08-22

What the full verification pass over the wiki found. Written to survive context loss. Companion to
[[2026-08-22-plan-survey-tasks]] (the work) and [[2026-08-22-plan-survey-scope-and-structure]] (the reasoning).

**Outcome: 181 of 181 source pages verified, 186 papers on disk, zero broken links.** The quote rule
that blocked drafting is cleared.

---

## 1. Why the audit happened

The wiki's documented failure mode was restating an existential result about a constructed object as a
universal claim about deployed systems. A quote check found something worse: passages in quotation
marks that no paper contains. The audit then widened from quotes to content, which is where the
serious errors were.

Method, reusable: extract every PDF with `pdftotext`, strip all non-alphanumerics from both the quote
and the paper text, match 45-character windows. **Always `grep -a`** — without it BSD grep silently
prints nothing on these files and every quote looks absent.

**The method has two false-positive modes, both encountered.** A quote fails if a spelling variant
differs (`overparameterization` against the paper's `overparametrization`), and it fails if an
editorial gloss was welded inside the quotation marks. Both produced false accusations of fabrication
against correct pages. A false fabrication charge is worse than a missed one.

---

## 2. Corrections to the repository's own standing record

Seven entries in the root `CLAUDE.md` were wrong. All are corrected there; recorded here because each
changes what a section of the survey may claim.

| Claim as recorded | Verdict | What is true |
| --- | --- | --- |
| Dinur–Nissim: §3 vs §4, the separation is the main theorem, the OLS example is theirs | **wrong on three counts** | Headings are §3.1 and §3.2, siblings inside §3. The abstract says the main result is "a polynomial reconstruction algorithm of data from noisy (perturbed) subset sums"; §3.1 is a warm-up on very small databases. **"OLS", "least squares" and "regression" occur zero times as words** — the attack is a linear program over subset sums plus rounding at 1/2. Bounds are right: `o(n)` fatal against exp(n), `o(√n)` against poly(n), `Õ(√T(n))` suffices against time-`T(n)` |
| Bogdanov et al.: low-degree-bounded adversaries carry real crypto security | **too broad** | Propositions 4.1 and 4.3 quantify over `(s,ε)`-indistinguishability, i.e. **size-bounded circuits**; Prop 4.1's proof builds an explicit circuit from a hypothesised distinguisher. Conjectures 1.3 and 1.4 are stated in **polynomial time**, with low-degree offered as "evidence for these conjectures". BJRZ does exactly what ABIKN does. **No security definition in either paper quantifies over a low-degree adversary** |
| Cohen et al.: Def C.1 is equivalent to one-wayness | **holds, antecedent dropped** | The equivalence is **Theorem C.5**, and requires `f` efficiently computable **and well-spread** (Def C.4). Narcissus resiliency also does not compose in general (Appendix D) |
| Xiao–Suh–Devadas: no learnable transformation gets worst-case crypto security for free | **narrower** | Theorem 1 is an **IND-CPA impossibility about the encoding `T`**, not about a training map. "One-way function" appears nowhere. The adversary picks the challenge distributions and its own concept class. Two escapes are named by the authors. Correct title is *Learnable Obfuscation* |
| Song: §1.3.3 proves black-box impossibility; §1.3.2 names bounded discriminators | **section numbers wrong; one claim not his** | No subsections 1.3.1–1.3.3 exist; §1.3 is a three-item list titled *Future directions*. Item 2 holds verbatim. Item 3's black-box statement is **Bruna–Regev–Song–Tang's, restated, conditional on lattice hardness** — not proved here. Item 2 also says a sampler fooling only bounded testers "could simply generate standard Gaussian samples", so the lattice gate is on `L²`-accurate score estimation, not sampling |
| Suliman et al.: conjectures fiber-navigation infeasibility and stops | **framing wrong** | Title is *Towards a Re-evaluation of Data Forging Attacks in Practice*; the actual result is **empirical** — published forging attacks miss the reproduction-error threshold by orders of magnitude and are detectable. The conjecture is real but incidental, names no adversary class or hardness assumption, and the paper says nothing about the evaluation-versus-training map distinction attributed to it |
| Haghifam–Smith–Ullman: `m ≳ n²ρ²+n`, unbounded adversary | **holds** | Verified in full. Three additions: antecedent `d > c₁(n + n²ρ²)`; success tolerance only 0.02 (TPR ≥ 0.51, FPR ≤ 0.49); and **the separation vanishes when the attacker knows the covariance** (Thm 1.2: `min{n, 1/ρ²} ≤ n`), so it prices ignorance of `Σ` rather than attack difficulty |

### Four errors that were mine, not the wiki's

- **Bubeck–Sellke**: I reported "overparameterization is necessary" as fabricated. It is verbatim in the abstract, spelled *overparametrization*. The real and narrower issue is that the theorem concerns **smooth interpolation**, a bounded Lipschitz constant, not resistance to an adversary.
- **Merkle ceiling**: recorded as "quadratic is provably optimal in the ROM". It is a **query** bound — Eve makes `(16n/δ)²` oracle queries, and the authors note she "can be implemented efficiently in a relativized world where P = NP". It forbids a super-quadratic *query* gap, not a *time* gap.
- **Detection ⟺ generation**: recorded as "§5, both directions, poly-time, bounded distinguisher class". Both directions in §5 is right; poly-time is refuted by the paper itself ("would lead to a general exponential-time algorithm"); the polynomial-time result is §6, one direction only; and no distinguisher carries a runtime bound at all. Both directions are empirical on a fixed sample.
- **Yeom**: the membership no-op is **Definition 4 / Experiment 1**, not Def 6. Def 6 is *Alternative attribute advantage*, whose baseline is the Bayes optimal simulator and is therefore not degenerate.

---

## 3. Content errors found in the wiki

Worse than the quote errors, because no quote check would catch them.

**Inverted or reversed:**
- `adversarial-vulnerability-any-classifier` had the paper saying the human visual system is "inherently **vulnerable**"; Fawzi et al. wrote **robust**. The conditional does not follow with the word reversed.
- `adversarial-examples-computational-constraints` claimed hardness "under standard cryptographic assumptions" with a PRF construction. **Bubeck–Price–Razenshteyn use no cryptographic assumption at all** — "cryptograph" occurs once in the paper, "statistical query" eleven times; the bound is unconditional in the SQ model.
- The BPR/BLPR relation was **inverted**: the page had BPR relying on trapdoor PRGs and BLPR weakening to one-way functions. It is the reverse, and the assumption is **quadratic residuosity** via Blum-Blum-Shub.
- `io-undetectable-backdoors-nn` claimed to close the white-box gap. Kalavasis et al. say GKVZ22 "leave open the question" — which is why they assume obfuscation.
- `jailbreak-paradox` had Theorems 3.1 and 4.1 with their contents swapped.
- Two Gamarnik quotes were swapped between sibling pages.

**Invented:**
- `seven-challenges-cross-domain-mas`: the seven challenges listed were **fabricated**, overlapping the paper's actual seven on at most two.
- **"IMTM" occurs zero times in the paper it was attributed to, zero times across all 186 PDFs, and twice in the compass artifact.** The wiki built a source page, a **concept page**, and the raw filename around it. Concept page now marked.
- `melon-indirect-prompt-injection`: the "provable detection theorem" does not exist.
- `camel-defeating-prompt-injections`: "Theorem", "Lemma", "we prove" occur zero times.
- `covert-learning`: an LWE assumption, halfspace results, and a theorem — none in the paper.
- `low-degree-polynomials-survey` cited "arXiv 2603.02594, 2026" as a known counterexample. The phrase does not occur in the survey, which is itself from June 2025. **A 2026 identifier cited by a 2025 document.**

**Misdescribed:**
- `holmgren-counterexamples-low-degree`: described as a learning-parities/3-XOR construction. "Parity" occurs zero times; both counterexamples use efficiently decodable error-correcting codes.
- `hirahara-planted-clique-conjectures-equivalent`: put refutation inside the equivalence class. It is a separate equivalence, with average-case k-clique on Erdős–Rényi graphs.
- `pkc-from-different-assumptions`: listed three assumptions where the paper states two, and gave the planted set `|S|/3` neighbours, a string absent from the paper.
- `cryptography-from-planted-graphs`: garbled the main result and confused **share** size with **message** size.
- `robust-generalization-more-data`: quoted the abstract while deleting "already in a simple natural data model", turning an existential into a universal. The paper also contains a counterexample to its own title — the gap holds "whenever one employs **linear** classifiers", and a slightly non-linear thresholding classifier recovers the smaller sample complexity.

**Two contamination paths, both traced.** Sixteen quotes on thirteen pages were the compass artifact's own editorial prose in quotation marks; strings like "the cleanest current theoretical extension" occur there and in none of the papers. Fourteen more were paraphrase. Around 5% of the wiki's 1100+ quotations were wrong.

---

## 4. Structural findings that shape the survey

These are results, not repairs. They belong in the paper.

- **The geometry cluster does not price anyone.** Of 18 papers in the concentration and robust-PAC region, eleven constrain no party at all or constrain only the learner in samples. Three price an adversary. Diakonikolas et al. inverts the usual picture — the **defender** is the polynomial-time party while the adversary is unbounded on a counting budget.
- **The agentic and certified-defence cluster has no resource-bounded adversary anywhere.** Across 16 papers, every "bound" is a geometric radius, a poisoned-sample count, or an interface restriction. Two state outright that the adversary is computationally unbounded. Five have no theorem at all.
- **The prior systematization has no computational-resource axis.** Papernot et al. use pipeline stage, attacker write-power, access level, and goals. A resource-like quantity appears three times inside the survey — a poisoning fraction, "unbounded" meaning unbounded poisoning power, and an ACRE query-complexity result — but never as an axis. **The survey's novelty claim is safe, and can be stated precisely.**
- **Reconstruction robustness — the closest published relative of `R` — carries no computational bound.** Definition 2 quantifies over *any* `R : Θ → Z`. `η` is the tolerance, `γ` the success bound, and the baseline `κ_{π,ℓ}(η)` is the best **oblivious** attack that ignores the model. The baseline field already exists in the literature; the compute axis does not.
- **The gradient-inversion literature defines no success criterion.** LAMP reports ROUGE scores with no threshold, so "reconstructed" is unadjudicable from the paper, and there is no gradient-free control. Cost is reported in GPU-hours.
- **Fine-grained cryptography has three incompatible conventions, not two.** Ball–Rosen–Sabin–Vasudevan is uniform Word-RAM time with `ε` indexed by **the adversary's own discount** as well as by `n`, so success may degrade as the adversary is given more budget. Quoting "BRSV17 Definition 2" as a single number quotes something the paper does not define. Part III.4 must present three conventions and their conversions.
- **The computational-DP impossibility has one more clause than anyone recorded.** Meisingseth–Rechberger show the Groce–Katz–Yerukhimovich utility barrier needs `ε ∈ O(log κ)`, a condition that, verbatim, "was not identified in" the original.
- **`κ` takes "unstated" constantly.** Confirmed across every cluster. The count is a result of the survey, not a gap in the mapping.

---

## 5. What this means for drafting

- Part I's material is verified and can be written now.
- Part III.1 has its empirical claim ready: the geometry cluster prices nobody.
- Part III.3 must carry the corrected Bogdanov reading — restricted-class analysis as *evidence*, security over circuits.
- Part III.4 grows: three δ conventions, and the Merkle ceiling is a query bound, which widens what a compute-priced claim may promise.
- Part VI's "considered rejection" section is unchanged and complete.
- The fiber framing's refutation rests partly on a false claim about Dinur–Nissim. **The refutation may need re-examining** — the size-versus-navigability split is still in that paper, but it is not the main theorem and the OLS example is not theirs.
