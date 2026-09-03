# Review, round 2. IEEE S&P 2027 SoK track

Submission: "How Hard Is the Attack? A Complexity-Theoretic Systematization of Machine Learning Security". Reviewed from `exp/survey/main.pdf` (built 2026-09-03), `exp/survey/supplementary.pdf`, `exp/survey/sections/*.tex`, `exp/survey/results.tex`, `exp/survey/notes/classification.tsv`, `exp/survey/notes/2026-08-22-note-classification-codebook.md`, the `cls_*` front matter of the wiki pages named below, and the primary PDFs named below, extracted with `pdftotext` and searched with `grep -a`. Every count below was recomputed from the TSV with a script rather than read off the paper.

## 1. Summary in my own words

The paper reads 200 formal works on the security and privacy of learning and codes each on thirteen fields, of which three carry the argument: which party a work's main claim bounds (attacker, learner, auditor, mechanism, nobody), in what unit, and how tightly. Its claim is that the machine learning security literature describes its adversaries by access and phase but does not price them in any resource, that the one form of bound that would let two results be compared, a relation between two parties' work, exists in fine-grained cryptography and is almost absent from attack papers, and that a small set of works already hold such a quantity without naming it. The evidence is the coded table, the per-cell counts derived from it, and a deciding quotation per row, with the counts stated as directions rather than sizes where the corpus cannot support a size. The main idea can be stated in one sentence: threat models in machine learning security are unpriced, and the vocabulary to price them already exists in cryptography. What the paper proves is nothing, what it measures is the distribution of its own coded corpus, and what it asserts is that this distribution reflects the field.

## 2. Verdict

Weak reject.

The paper attempts the third SoK criterion, a new taxonomy of an established area, and the axis it adds (constrained party, unit, tightness) is genuinely absent from Papernot et al. and from the single-family systematizations it lists. That is a real viewpoint and a hostile reviewer could not call the paper a survey without insight. It fails at present because the classification is the paper and the classification does not yet agree with itself. The headline numbers in the abstract (11 relative bounds, 3 in attack works) are contradicted by the paper's own evidence layer, where at least seven rows coded `exponent` carry a recorded reason that states a relation to the honest party's work, which is the paper's own definition of `relative` (F1). The literature section illustrates two of its five regions with works the table places in other regions (M1). Twenty-four rows, including most of the works the prose leans on, carry no deciding quotation at all, against an abstract that says every row does (M2). One reported count in Section 5.2 is wrong in its subject (M4), and the argument of Sections 5.1 and 5.2 rests on a statistic that measures the opposite of what it is used for (M5). None of these needs new research. All of them need a recount and a rewrite of the numbers and the illustrations, and after that the paper would be a weak accept. The paper stands without the planned formalization section. A SoK does not need a ledger of its own. It needs the table to be right.

## 3. Findings

### FATAL

F1. The headline `relative` count is contradicted by the paper's own evidence layer.

Sentence: abstract, "Only 11 works state a bound relative to another party's work, the form that lets two results share a scale, and 3 of those study an attack." Repeated in Section 5.3 and the conclusion.

What is wrong. Codebook revision 6 (`notes/2026-08-22-note-classification-codebook.md`) defines `relative` as "two parties" and `exponent` as "a stated exponent in one party's own resource". The TSV has 11 rows coded `relative` and 27 coded `exponent`. I read the `cls_reason` field of every `exponent` row and found seven whose recorded reason states a two-party relation, which under revision 6 is `relative`:

- `filter-impossibility-ai-alignment` (BGGKRR25): reason says "bounded in Thm 7 by o(t^ε) against the model's time t, a stated relation to the honest party's work, hence tightness=exponent". Section 5.5 of the paper itself calls this "a ratio between two parties' compute".
- `sequential-functions-fine-grained`: reason says "A2 is bounded by parallel running time (depth) relative to the honest party's k·tC(λ), a stated relation to the honest party's work, so tightness=exponent".
- `undetectable-watermarks-lm`: reason says "tightness=exponent from the paper's own stated ~2000x-honest-cost pricing".
- `unlearning-verification-fragile`: evidence is "Assume the time complexity of naive retraining is T(n). The time complexity of Algorithm 1 is T(n)", a relation between the forger and honest retraining.
- `certificates-statistical-algorithms`: reason says "the verifier's O(log k) cost is stated directly against the honest prover's Θ~(sqrt k) cost".
- `fine-grained-one-way-functions` (BC22) and `pkc-fine-grained-setting` (LLW19): hand-coded, no reason on file. Section 2.2 and Section 3.5 of the paper describe both as relations between adversary and honest cost, BC22 Definition 6 as "no circuit of size below |f|^{1+δ}" and LLW19 Definition 5 as "the (relative) gap". Section 6.6 cites both as members of "the one region that states a bound as a relation between two parties' work". I verified the definitions: `raw/BC22_FineGrainedOWF.pdf` Definition 6 reads "if |C_m| < |f_m|^{1+δ}, then we have Pr[...] ≤ ε(m)", and `raw/LLV19_PKCFineGrained.pdf` Definition 5 reads "The (relative) gap of an T(n) fine-grained one-way function f is the".

Recoding these seven gives 18 `relative` rows, of which 7 carry an attack family (the existing 3 plus filter-impossibility, watermarks, unlearning-verification, certificates). Going the other way, of the existing 3 attack-family `relative` rows, `authentication-bounded-storage` is a MAC in the bounded storage model whose `cls_reason` says "family=forge is the generic cryptographic sense (MAC/signature unforgeability), not the ML-specific 'forge a training artifact' sense used elsewhere in this codebook", and Section 5.2 of the paper itself says of this work that it "is bounded-storage cryptography rather than an attack on a learned model". The codebook's own definition of `forge` is "proof-of-learning spoofing and unlearning forgery". So the paper counts that row as an attack in the abstract and disowns it in Section 5.2. `preventing-false-discovery-hard` is coded `reconstruct` on the stated ground that "family tracks the mechanism used, not the paper's chosen frame", which is the opposite of Rule 1.

Also: `proof-of-learning` is coded `tightness=unstated`. Its Property 2 (Definition 2 in the paper, `raw/JYC+21_ProofOfLearning.pdf` line "E[CT] ≤ E[CA]") is a relation between two parties' work with exponent one. Under the codebook's definition of `relative` it is `relative`. If the authors want it to be `unstated` because the relation carries no exponent, class or security parameter, the codebook must say that `relative` requires one, and then the seven rows above must be re-examined under that rule too. The paper cannot have PoL as a "near miss that states no tightness" (Section 5.5) and BGGKRR25 as an `exponent` row at the same time under one definition.

Why fatal. The abstract, Section 5.3, Section 6.6 and the conclusion all rest on 11 and 3. The paper's own data supports something between 5 and 7 attack works and 16 to 18 works overall. The direction of the finding survives (a small minority of attack works state a two-party bound), and Section 5.3's "roughly threefold" inflation becomes roughly twofold. Every sentence that carries these numbers has to change, and the codebook must state the rule that produced the new count.

Smallest fix. Add one sentence to the `relative` definition in the codebook that decides PoL and the seven rows one way or the other. Re-read all 38 rows coded `exponent` or `relative` under it. Recount. Rewrite the abstract, 5.3, 6.6 and the conclusion. Report the recount in Section 4.5.

### MAJOR

M1. Section 6 illustrates two regions with works the table places elsewhere.

Section 6.4, "Nobody bounded", opens with "Thirty-three works constrain no party at all" and names Mahloujifar, Diochnos and Mahmoody [143] and Gilmer et al. [109] as its first line, saying "These conclude inevitability precisely because no resource enters them". The TSV codes `curse-of-concentration` and `adversarial-spheres` as `party=attacker, unit=perturbation, tightness=budget`, and `empirically-measuring-concentration` likewise. The second line names Athalye et al. [6] and Tramèr et al. [182] as works that "bound nobody because their claims are about practice"; `obfuscated-gradients` and `adaptive-attacks-defenses` are coded `attacker, perturbation, budget`. Four of the six works named as examples of the 33 are inside the 28 of Section 6.2. Codebook Rule 6 ("A perturbation budget is a bound") and Section 4.2's own sentence about the revision that added the value exist precisely to keep these apart. The prose applies the reading the codebook rejected.

Section 6.1, "The attacker bounded in time", 35 works, names Bun, Chen and Vadhan [27] (coded `mechanism, time`), Goldwasser et al. [106] and Kalavasis et al. [131] (coded `auditor, time`, and the paragraph says so), and Degwekar, Nakkiran and Vaikuntanathan [81] (`win-win-robust-learning`, coded `learner, time`). Four of the six examples are outside the region.

Fix. Either re-pick the examples from rows the table places in each region, or, if the authors believe MDM19 and Gilmer bound nobody, recode them and every sibling and recount 28 and 33. The first is smaller. The GKVZ paragraph can stay if it is moved to 6.5.

M2. The evidence layer is not complete, against the abstract's claim that it is.

Sentence: abstract, "with the deciding sentence of each source quoted and checked against it"; Section 1 contribution 2, "Every classification records the verbatim sentence that decided it and where in the paper it appears".

Checked: 24 rows in the TSV carry `prov=hand`, and each of their wiki pages carries `cls_evidence: absent` with `cls_evidence_src: "classified by hand in the first batch, before the evidence requirement was added to the brief"`. They include `proof-of-learning`, `mia-cannot-prove-training`, `calibrated-proof-of-work-extraction`, `mia-from-first-principles`, `obfuscated-gradients`, `adaptive-attacks-defenses`, `adversarial-spheres`, `curse-of-concentration`, `empirically-measuring-concentration`, `planting-undetectable-backdoors`, `fine-grained-one-way-functions`, `pkc-fine-grained-setting`, `raz-parity-time-space`, `universal-law-of-robustness`, `win-win-robust-learning`, `computational-differential-privacy`, `jagielski-model-extraction`, `reconstructing-informed-adversaries`. That is most of the works the prose in Sections 2, 5.5, 6 and 7 leans on. A further 27 rows carry `cls_evidence: absent` as an evidenced claim of absence, which is legitimate and which the paper describes. Section 4.4 separately says that of the second verification pass "57 verify" and "85 could not be bound by title", and 57 + 85 + 25 is 167, not 200. A reader who disputes the PoL cell cannot "go to the line it came from" because there is no line.

Fix. Supply the 24 quotations (one session's work, since the PDFs are on disk) and rerun both passes. Then restate Section 4.4 with numbers that sum to 200. If the 85 unbound works remain unbound, the contribution must say that 85 rows were checked against the corpus and not against their own document.

M3. Sibling works of one kind are coded to three different parties.

Lower bounds against a restricted algorithm class on planted or statistical problems are coded `learner` (`feldman-statistical-algorithms-planted-clique`, `low-degree-polynomials-survey`, `ding-low-degree-community-detection`, `holmgren-counterexamples-low-degree`, `low-degree-estimation-schramm-wein`, `low-degree-almost-orthonormal`), `auditor` (`barak-sos-lower-bound-planted-clique`, `rigorous-implications-low-degree`) and `attacker` (`brennan-sq-lowdegree-equivalence`). The `cls_reason` fields show the classifiers inventing the rule each time: barak-sos cites "rule 6's auditor convention for a verification/refutation role", brennan says "party=attacker is the generic label for the bounded distinguisher", feldman says "matching this programme's established 'restricted-class learner' framing". The codebook's `party` entry has no rule for a distinguisher with no security role. Feldman's detection bound and rigorous-implications' Result 2 are the same shape of claim (a restricted class cannot distinguish a planted distribution from null) and land in two parties. These rows feed the 62, 12 and 35 of Section 6. The right value is `learner` for all of them, or a new value `solver`, and the codebook must say which. Either way the counts move by up to three.

M4. A count in Section 5.2 has the wrong subject.

Sentence: "Among the 101 works studying an attack, the adversary itself is bounded in time in 17 of them, by a perturbation radius in 23, in queries in 10, in samples in 9, and by a corruption fraction in 5."

Recomputed from the TSV over attack-family rows with `party=attacker`: time 17, perturbation 23, queries 9, samples 1, corruption 5. The figures 10 and 9 are `unit` counts over any party. Eight of the nine sample-bounded attack works bound the learner or the auditor, not the adversary. Only `haghifam-sample-complexity-mia` bounds the adversary in samples. Fix: "in queries in 9, in samples in 1".

M5. Sections 5.1 and 5.2 draw opposite conclusions from the same statistic.

Section 5.1 says the phase-by-access table "comes out full. 19 of its 32 cells are populated" and concludes the field agrees on access and phase. Section 5.2 says the party-by-unit table "fills 25 of 75 cells, and the occupied cells do not concentrate" and concludes the field does not agree on resources. Populated-cell fraction measures spread, not agreement. A field that agrees concentrates into few cells. Recomputed: over the 101 attack works, phase-by-access occupies 18 cells and its five largest hold 61 per cent of the works, while party-by-unit occupies 15 cells and its five largest hold 78 per cent. By concentration, the resource table is the more agreed one. Over all 200 works the numbers are 74 per cent against 62 per cent, and the first is driven by the 88 works in (n/a, none). The paper's substantive point survives, that the vocabulary of access is shared while the resource column is mostly `none` or a perturbation radius, but the argument as written proves the reverse. Fix: replace "19 of 32 cells are populated" with a statement about shared vocabulary (71 of 101 attack works name an access level from a list of six values), and replace "do not concentrate" with what the table shows, that the two largest cells among attack works are `none` (23) and `perturbation` (23).

M6. Section 7 misstates the method of Suya et al.

Sentence: "Suya et al. re-run 164 surveyed attacks under a fixed time budget". `raw/SSK+24_SoKBlackBoxPitfalls.pdf`, Section on transfer attacks: "This leaves us with 164 attacks, of which 102 are published in major security and machine learning conferences" (the survey), then "we selected transfer attacks that augment the baseline I-FGSM attack ... this leaves us with 20 attacks ... Of these 20 attacks, we picked 11 that span a wide range of local runtimes", and "we re-run all the attacks but instead of running them for a fixed number of iterations as in prior work, we run them for the same time duration (30 minutes per batch)". They re-ran 11. The quotation the paper gives is verbatim. Fix: "Suya et al. survey 164 black-box attacks, re-run 11 transfer attacks under a fixed 30-minute budget, and recommend that ...".

M7. The 18 near-miss works are read as one phenomenon and are not.

Section 5.5 closes with "These 18 works are where the quantity this survey is about already exists in the literature without a name." The 18 is computed mechanically in `tools/check-numbers.py` as rows where `tightness` and `assessed` disagree with the modal pairing. The six "run the other way" rows (`tightness=measured, assessed=explicit`) are `calibrated-proof-of-work-extraction`, `polo-proof-of-learning-ownership`, `universal-jailbreak-rlhf-backdoors`, `data-pruning-beats-power-laws`, `feature-learning-improves-scaling` and `hidden-progress-sgd-parities`. The last three are scaling and learning-dynamics papers with no adversary, whose measured quantity is training cost, which has a name and a literature (Section 6.7 says so). They are not places where an unnamed adversary price sits. Similarly `adversary-aware-dp-bounds` and `robustly-reliable-learners-poison` in the first group are not obviously about an unpriced adversary. Fix: list the 18 in a table with the quantity each holds, and restrict the closing sentence to the rows it is true of.

M8. The `party` coding of `sok-differential-privacies` violates Rule 9 and is inconsistent with its sibling.

Coded `attacker, time, poly` on the evidence "Distinguisher modelled explicitly as a non-uniform ppt Turing machine" from Definition 21, which is the paper's restatement of Mironov et al.'s definition in a catalogue. Codebook Rule 9: "Classify what the work claims, not what it discusses ... The bound must be one the work asserts, not one it examines." `sok-security-privacy-machine-learning` (Papernot et al.) is coded `none` on the same rule. Desfontaines and Pejó assert no bound. This row is one of the 35 in Section 6.1 and one of the 167 priced works. Fix: recode to `none` and recount, or delete Rule 9.

M9. Format and anonymity do not meet the call.

The title lacks the prefix "SoK:". The author block "Halil İbrahim Kanpak, Koç University, Istanbul, Türkiye" appears on page 1 of `main.pdf` and on page 1 of `supplementary.pdf`. The call requires anonymous submission. Both are trivial to fix and both are desk-reject conditions. IEEEtran with `conference,compsoc` and US letter are met (`pdfinfo`: 612 x 792). Text runs 9 pages, within 13. The supplement is 19 pages. I did not check the call's rule on supplementary length.

### MINOR

m1. Section 2.2, "they add two pages later that 'given that we are not aware of a mechanism ...'". In `raw/JYC+21_ProofOfLearning.pdf` the sentence "would be at least as computationally expensive as what it took T" and the conjecture sentence are on the same page (both fall after the fifteenth form feed in the extraction, about thirty lines apart, in §VII-B3a). Both quotations are verbatim. Fix: "they add, in the same subsection, that ...".

m2. Section 2.2 and 3.5, BC22 Definition 6. The paper says "inverts with non-negligible probability". Definition 6 bounds the inversion probability by ε(m), where ε is a parameter of the definition, and the paper uses constant ε (0.99 appears in a bound on page 711 of the extraction). Fix: "inverts with probability above ε".

m3. Section 6.3, Montasser, Hanneke and Srebro, "sometimes at a sample cost exponential in the dimension". `raw/MHS19_VCClassesRobust.pdf`: "sample complexity that is sometimes exponential in the VC dimension". Fix: "in the VC dimension".

m4. Section 7, "it is restated from earlier work by an overlapping set of authors [6]". `raw/ACW18_ObfuscatedGradients.pdf` contains the practice ("We use between 100 and 10,000 iterations of gradient descent, as needed to obtain convergance") and no stated position on attacker compute as a threat-model parameter. Fix: "and it is consistent with the practice in [6]". Section 7's paraphrase "conclude that an evaluation should assume an adversary who spends whatever time is needed" is a fair reading of "it is worth evaluating against a strong attack with many iterations of gradient descent". The sentence that carries the principle, and that the paper should quote, is the one before it: "Because the threat model must not constrain the approach an attacker takes".

m5. Section 5.1, "they split evenly between attacking a model at test time and attacking one already released". Among the 71 attack works naming an access level: post hoc 33, test time 25, train time 12. Not even, and the third phase is omitted.

m6. Section 5.6 title, "Half the attack literature states no baseline". The numbers are 22 of 49 that define success (45 per cent), or 74 of 101 attack works that state no baseline (73 per cent, counting the 52 with no success criterion). Say which.

m7. Section 5, title "Four findings from the classification", has six subsections.

m8. Section 4.2, "The vocabulary was revised four times". The codebook carries revisions 2 through 6, five after the first. Section 4.2 also says "Eight of the fourteen gaps"; the codebook's own counts are 7 then 6 then further post-freeze gaps, and fourteen cannot be reconstructed from it.

m9. Section 4.4, "The first, over the 200 works then in the corpus". The codebook's verification table is over 181 pages ("129 verified, 25 absence, 27 symbol-heavy"), and the 17 scaling-law works were added later. Also the numbers 57, 85, 25 do not sum to 200 (see M2).

m10. Figure 1. All twenty labels match the TSV (recomputed: family groups 24, 56, 6, 13, 2, 99; parties 86, 62, 12, 7, 33; tightness 11, 27, 24, 31, 4, 8, 46, 14, 35). Two defects. The caption says works with no attack family "and works generic over several attacks share the leftmost band", but the figure draws "Several attacks (2)" as its own band. The first stage is labelled "What is attacked" but is built from `family`, not `target`, in `figures/src/sankey.py`, so backdoor works whose `target` is `parameters` appear under "Model behaviour" and the bounded-storage MAC appears under "Record of training".

m11. Section 1, "it appears in 21 of the 200 works surveyed here" (membership inference). The TSV has 12 rows with `family=membership`. The 21 is a tag count from wiki front matter (`results.tex` comment). Say "is discussed in 21" or use 12.

m12. `feldman-statistical-algorithms-planted-clique` has `baseline=stated` with reason "Thm 2.9 fixes the success criterion at probability at least 2/3". The codebook and Section 5.6 both exclude a success tolerance from `stated`. Sixteen non-attack rows carry `stated`; at least this one is the error Section 5.6 says the re-pass removed. It does not touch the reported 27 and 22, which are over attack works only.

m13. The `cls_reason` text of rows recoded to `relative` under revision 6 still says "tightness=exponent" (`authentication-bounded-storage`, `preventing-false-discovery-hard`, `bounded-storage-simple-schemes`, `fine-grained-nike-lower-bounds`, `permissionless-consensus-fine-grained`). `haghifam-sample-complexity-mia` has `cls_frame: statistical` and a reason that says "frame=compute stretches the codebook". `authentication-bounded-storage` has `cls_baseline: absent` and a reason ending "baseline=stated because ...". The evidence layer's reasoning is stale relative to its values in at least seven rows.

m14. `raz-parity-time-space` is coded `tightness=budget`. Raz's theorem is a threshold in the learner's own resource (memory below n²/25 forces 2^Ω(n) samples), which the codebook calls `exponent`. It also carries `phase=train time` where every sibling with `family=none` carries `n/a`; nine such rows exist (`bandeira-franz-parisi-criterion`, `fine-grained-erm`, `low-degree-polynomials-survey`, `quasi-poly-low-degree-conjecture-false`, `universal-law-of-robustness`, `covert-learning`, `what-can-we-learn-privately`, `deep-learning-differential-privacy`, `raz-parity-time-space`), and they add cells to the "19 of 32".

m15. `frame=compute` is assigned to 14 rows with `unit=samples`, 4 with `flops` and 3 with `parameters`. The codebook defines `compute` as "time, circuit size, memory, queries or an algorithm class". `universal-law-of-robustness` is `compute` while Section 6.3 calls it "an information-theoretic law". `frame` is not used in any reported number, so this is a codebook hygiene point.

m16. Typography. Page 3, two sentences begin in lower case because the macros hold words: "seven of them rely", "six are circumvented". Section 8 paragraph headings render with a double period ("builds on..") because the `\paragraph` titles end in a period. "Mądry" renders as "M˛ adry" in the body and the bibliography. Reference [1] reads "in IACR ePrint/, 2023" and [48] "in IACR ePrint/335"; four of the five bibliography entries I opened in `refs.bib` are `@misc` with an `annote` "venue-unconfirmed", including [49] Carlini et al. and [197] Zhang et al. The paper calls FK24, SSEP24 and WLBZ25 "preprints at the time of writing" on the strength of unconfirmed venues.

m17. Process language remains in the prose despite the paper's own rule: Section 5.3 "we lost it once ... which is what an earlier version of this classification did", Section 5.6 "This column was the least reliable in the classification and was re-checked in full", supplement page 1 "Of the 200 works classified so far", "This is a partial pass. 200 of the corpus's works are classified. The remainder are not yet placed." The last two sentences are false as printed.

m18. "24 of 27" inter-reader agreement appears in Section 4.5 and again in Section 5.6. Once is enough.

### Unverified (no evidence checked by me)

u1. "Seventeen works on neural scaling laws were added to this corpus late" (Section 6.7). The TSV has no field that marks them.
u2. "24 of 27" agreement between two readers (Sections 4.5, 5.6).
u3. Meeus et al.'s "0.988 to 0.994 AUC on WikiMIA" (Section 2.1). I verified "at least 10 new MIA methods" in `raw/MSJ+25_SoKMIALLMsRushing.pdf` and did not check the AUC figures.
u4. The venue status of FK24, SSEP24, WLBZ25 (m16).
u5. Whether the S&P 2027 call limits supplementary material to a page count.

## 4. Numbers I recomputed

From `notes/classification.tsv` (200 rows). All agree with the paper unless marked.

| Where | Paper | Recomputed | Note |
| --- | --- | --- | --- |
| Abstract, 5.4, conclusion | 33 unbounded | 33 | |
| 5.1 | 19 of 32 cells | 19 | includes 4 cells with `access=none` and 1 with `phase=n/a` |
| 5.1 | 71 of 101 name access | 71 | |
| 5.2 | 25 of 75 cells | 25 | includes (none, none) |
| 5.2 | attacker time 17, perturbation 23, queries 10, samples 9, corruption 5 | 17, 23, 9, 1, 5 | M4 |
| 5.2 | four attacker-memory works, one with attack family | 4, 1 | |
| 5.3 | 11 relative, 3 with attack family | 11, 3 as coded | F1 |
| 5.3 | 27 exponent | 27 | |
| 5.3 | 38 budget, 25 unstated, 17 poly, 10 measured, 4 class | 38, 25, 17, 10, 4 | |
| 5.4 | 23 of 101 vs 10 of 99, CI 2.6 to 22.8 | Wald 2.6 to 22.8 | |
| 5.4 | 10 of 71 vs 5 of 87, CI −1.1 to 17.8 | 10/71, 5/87 from `claim_quantifier` ≠ empirical joined to family; Wald −1.1 to 17.8 | quantifier lives in wiki front matter, not the TSV, and `check-numbers.py` does not check these four |
| 5.5 | 91 per cent, 18 = 10 + 6 + 2 | 91, 10, 6, 2 | M7 on interpretation |
| 5.6 | 132 n/a, 49 = 27 + 22 | 132, 27, 22 | `check-numbers.py` does not check these |
| 6.1 | 35 attacker in time or circuit size | 35 | M8 would make it 34 |
| 6.2 | 28 = 23 + 5 | 28 | |
| 6.3 | 62 = 21 time, 18 samples, 13 class, 4 flops | 62, 21, 18, 13, 4 | remainder 3 parameters, 1 each circuit size, memory, queries |
| 6.4 | 33 | 33 | |
| 6.5 | 19 = 12 + 7 | 12, 7 | |
| 6.7 | 4 flops | 4 | |
| Figure 1 | all labels | all match | m10 |
| 4.4 | 57 + 85 + 25 | 167 ≠ 200 | M2 |

`python3 tools/check-numbers.py` prints "all 28 macros match the corpus". It does not cover the Baseline, Thm, NumMIApages or scaling-law macros.

## 5. Quotations checked against primary PDFs

| Where | Quotation | Source | Result |
| --- | --- | --- | --- |
| 2.2, 5.5 | "would be at least as computationally expensive as what it took" | JYC+21, §VII-B3a | verbatim; "two pages later" is false (m1) |
| 2.2 | "given that we are not aware of a mechanism to prove this formally, we present the following as a conjecture" | JYC+21, same page | verbatim |
| 2.2 | E[C_A] ≥ E[C_T] "three times" | JYC+21 | three occurrences found (Property 2, and two in §VII-A) |
| 2.2 | "the (relative) gap of an T(n) fine-grained one-way function f" | LLV19 Def 5 | verbatim |
| 2.2, 3.5 | BC22 Def 6, size below |f|^{1+δ} | BC22 Def 6 | correct; "non-negligible" is not the paper's condition (m2) |
| 1, 8 | Papernot Figure 3, both fragments | PMSW18 Fig. 3 caption | verbatim |
| 2.1 | "would still be prohibitively expensive as it would require training new large models" | ZDKT25 | verbatim |
| 2.3 | "the technical tools to evaluate defenses properly already exist"; "is methodological rather than technical" | TCBM20 abstract | verbatim |
| 2.4 | Arp et al. P10 definition | AQP+22 | verbatim |
| 7 | Carlini et al., "few reasonable threat models ..." | CAP+19 §4.8 | verbatim |
| 7 | Suya et al., "execution cost such as the local attack runtime ..." | SSK+24 | verbatim; the "164 re-run" claim around it is wrong (M6) |
| 3.5 | Barak and Mahmoody O((n/δ)²) | BM09 | theorem gives (16n/δ)², consistent |
| 1 | Das et al. "eight published benchmarks" | DZT24 | "For 8 published" found |
| 1 | Duan et al. "none exceeds 0.6 AUC outside one domain" | DSM+24 | "No single MIA or target model demonstrates attack AUC above 0.6" found, GitHub outlier noted |
| 1 | Meeus et al. "at least ten new methods" | MSJ+25 | "at least 10 new MIA methods" found |

## 6. Classification rows checked

Agree means the coded value follows from the codebook and the evidence on file. Rows are named by wiki slug.

| Slug | Field | Coded | My value | Deciding quotation or reason |
| --- | --- | --- | --- | --- |
| authentication-bounded-storage | tightness | relative | relative | "Then m = O(n²)" (Thm 7.11), honest n bits |
| authentication-bounded-storage | family | forge | none, vocabulary gap | cls_reason: "family=forge is the generic cryptographic sense ... not the ML-specific ... sense used elsewhere in this codebook"; codebook: forge "covers proof-of-learning spoofing and unlearning forgery" |
| haghifam-sample-complexity-mia | tightness, party, unit | relative, attacker, samples | agree | "every sample-based MIA ... requires m ≳ n²ρ² + n samples" (Thm 1.1) |
| preventing-false-discovery-hard | tightness | relative | relative | "no computationally efficient oracle that given n samples is accurate on n^{3+o(1)} adaptively chosen queries" |
| preventing-false-discovery-hard | family | reconstruct | none | cls_reason: "family tracks the mechanism used, not the paper's chosen frame", against Rule 1 |
| bounded-storage-simple-schemes | tightness | relative | agree | S(n) = Cn² against honest O(n) |
| speak-much-remember-little | tightness | relative | agree | "arbitrarily large gaps between m and n, up to exponential m = 2^{O(n)}" |
| merkle-puzzles-are-optimal | tightness, unit | relative, queries | agree | "honest users make at most n queries ... adversary making O(n²) queries" |
| fine-grained-nike-lower-bounds | tightness | relative | agree | "honest parties ask n queries each, while the adversary needs n^{K/(K−1)} queries" |
| permissionless-consensus-fine-grained | tightness | relative | agree | "adversarial power A = T^{1−ε} ... where T denotes the honest computational power" |
| fine-grained-one-way-functions (BC22) | tightness | exponent | relative | BC22 Def 6: "if |C_m| < |f_m|^{1+δ}"; no evidence on file |
| pkc-fine-grained-setting (LLW19) | tightness | exponent | relative | LLV19 Def 5: "The (relative) gap"; no evidence on file |
| filter-impossibility-ai-alignment | tightness | exponent | relative | "for every prompt filter running in time o(t^ε)"; cls_reason: "a stated relation to the honest party's work" |
| filter-impossibility-ai-alignment | party, assessed | auditor, implicit | agree | the filter is the bounded party |
| sequential-functions-fine-grained | tightness | exponent | relative | "A2 runs in time strictly less than k · tA(λ)" |
| undetectable-watermarks-lm | tightness | exponent | relative or measured | cls_reason: "~2000x-honest-cost pricing ($960.36 vs $0.48)"; a dollar ratio is a measurement |
| unlearning-verification-fragile | tightness | exponent | relative | "Assume the time complexity of naive retraining is T(n). The time complexity of Algorithm 1 is T(n)" |
| certificates-statistical-algorithms | tightness | exponent | relative | verifier O(log k) against honest prover Θ̃(√k) |
| proof-of-learning | tightness | unstated | relative, or codebook must exclude it | Property 2: "E[CT] ≤ E[CA]"; no evidence on file |
| pol-incentive-security | tightness, assessed | budget, implicit | agree | "we assume it to be 0" (§3.3) |
| mia-cannot-prove-training | party, tightness | auditor, unstated | agree with reservation | no evidence on file; the paper's own Section 2.1 quotation would serve |
| calibrated-proof-of-work-extraction | tightness, assessed | measured, explicit | agree | no evidence on file |
| on-evaluating-adversarial-robustness | unit, tightness, assessed | perturbation, budget, implicit | agree | "worst-case loss L for a given perturbation budget" (§2.2.2); §4.8 declines compute |
| kaplan-bayesian-memorization-reconstruction | party | none | agree | "for all attackers A" (Def 3.1); "computational" means extraction-based |
| privacy-risk-overfitting | party | none | agree | A is "an arbitrary function of (z, A_S, n, D)" |
| reconstructing-informed-adversaries | party | none | agree | Def 2 quantifies over any R with no bound; no evidence on file |
| suliman-data-forging-attacks | party | none | agree | 0 hits for "polynomial-time", "running time", "adversary class" |
| forgeability-and-unlearning | party | none | agree | "computationally feasible" used descriptively in Def 4 |
| jailbreak-paradox | party | none | agree | Pareto dominance is a performance ordering, not a resource |
| difficulty-of-mia | party, baseline | none, stated | agree | ZeroR and naive attack are the paper's argument |
| beyond-labeling-oracles | party | none | agree with reservation | no evidence on file; `raw/SOURCES.md` says it "proposes an unformalized cost inequality", which is the PoL case and should be checked for `assessed=implicit` under Rule 8 |
| sok-differential-privacies | party | attacker | none | Def 21 catalogues Mironov et al.; Rule 9; sibling `sok-security-privacy-machine-learning` is `none` |
| feldman-statistical-algorithms-planted-clique | party | learner | learner | "any SQ algorithm requires n^{Ω(log n)} queries" |
| feldman-statistical-algorithms-planted-clique | baseline | stated | n/a | cls_reason: "fixes the success criterion at probability at least 2/3"; codebook excludes a tolerance |
| brennan-sq-lowdegree-equivalence | party | attacker | learner | cls_reason: "party=attacker is the generic label for the bounded distinguisher"; no such rule in the codebook |
| barak-sos-lower-bound-planted-clique | party | auditor | learner | cls_reason cites "rule 6's auditor convention", which the codebook does not contain |
| rigorous-implications-low-degree | party | auditor | learner | Result 2 is a distinguishing lower bound, the same shape as feldman |
| adversarial-spheres, curse-of-concentration, empirically-measuring-concentration | party, unit | attacker, perturbation | agree | Rule 6; Section 6.4 prose disagrees with the table (M1) |
| obfuscated-gradients, adaptive-attacks-defenses | party, unit | attacker, perturbation | agree | Rule 6; Section 6.4 prose disagrees (M1); no evidence on file |
| separating-cdp-client-server | party | mechanism | agree | "there exists a polynomial-time εk-PURE-SIM-CDP mechanism" (Thm 11); Section 6.1 prose disagrees (M1) |
| win-win-robust-learning (DNV19) | party | learner | agree | Section 6.1 prose disagrees (M1); no evidence on file |
| computational-hardness-robust-learning | party, unit | attacker, circuit size | agree | "the size of circuit used by the adversary controls its computational power" |
| raz-parity-time-space | tightness, phase | budget, train time | exponent, n/a | threshold in the learner's own resource; siblings use n/a |
| universal-law-of-robustness | frame | compute | statistical | Section 6.3: "an information-theoretic law with no adversary in it" |
| hidden-progress-sgd-parities, data-pruning-beats-power-laws | tightness, assessed | measured, explicit | agree | membership in the near-miss set is mechanical; the prose reading is not (M7) |
| membership-inference-shokri | unit | queries | queries with the flagged gap | "Increasing the number of shadow models would increase the accuracy of the attack but also its cost"; the unit is training runs |
| capacity-bounded-dp | party, unit, tightness | attacker, algo class, class | agree | "bounded not in computational power, but in terms of the function class" |
| certified-defenses-data-poisoning, certified-robustness-randomized-smoothing | party, unit | attacker, corruption / perturbation | agree | not re-read; consistent with Section 6.2 |

Where the data supported the paper against my first impression: `kaplan-bayesian-memorization-reconstruction` (I expected a computational bound from the title; the page shows the paper's "computational" is the proof-of-knowledge sense), `haghifam`, all five bounded-storage and fine-grained rows coded `relative`, and Section 5.4's two confidence intervals, which I recomputed and which hold.

## 7. Explanation findings

1. The thirteen fields are never listed in the body. Section 4.2 says "thirteen fields ... Six ... and seven" and names none. A reader meets `party`, `unit`, `tightness`, `assessed`, `baseline`, `frame` and `second party` only through the supplement's column headings. Repair: a half-page table in Section 4.2 with field, values, and a one-line definition, taken from the codebook.
2. `party` is used in the contribution list ("a bound on an auditor") before any sentence says what an auditor or a mechanism is. Repair: one sentence each at first use in Section 1 or in the field table.
3. `tightness` and its nine values are introduced in pieces. Section 5.3 defines `relative`, `exponent` and `budget` by contrast; `conditional`, `quasi-poly` and `class` are named only in Figure 1's labels; `measured` is glossed as "a measurement with no definitional standing" once. Repair: the field table.
4. `assessed` (explicit or implicit) is defined by paraphrase in Section 5.5 without its name. The contribution bullet mentions it. Repair: name it where Section 5.5 defines it and give the Rule 8 test (a number exists but is not a parameter).
5. No row is ever shown in full. Repair: one worked row, thirteen fields and the deciding quotation, for a work the prose already uses, Haghifam et al. or the filter impossibility. This also demonstrates the evidence layer that contribution 2 claims.
6. `frame` is introduced through the revision story in Section 4.2 and never used in a finding. Either use it (it is what separates 6.2 from 6.4) or drop it from the body.
7. "Comparable" is the load-bearing word of Section 5.3 and is defined only by the clause "relates one party's work to another's". State the definition once, first, as the codebook does: two parties, one statement, both units named.
8. Section 3.3 (worst and average case), 3.4 (reductions) and 3.6 (terminology collision) are not used by Sections 5 or 6. A reader arriving from machine learning security spends a column on material the paper never calls. Cut 3.3, 3.4 and 3.6, keep 3.1, 3.2 and 3.5.
9. Section 6.6's four paragraphs on generative exponents, batch reuse and Kovačević et al. are a specialist digression inside a survey whose reader is a security researcher. They support no count and no finding. Cut to two sentences in 6.3, or move to the supplement.
10. Section 7 is one paragraph standing between the literature and related work. It is the counterposition to the whole paper and belongs either as the last part of Section 2 (the field's own answer to Problem 3) or as a subsection of Section 5 next to the near-miss row for the same work.
11. Section 5.1's argument should state the statistic it uses (see M5). A reader who checks the two fractions will conclude the opposite of the text.
12. The Sankey's first stage is labelled "What is attacked" and is built from `family`. Label it "Attack family, grouped" or build it from `target`.
13. The ordering is right for a complexity reader and wrong for the stated audience. Section 2 works. Section 3 should be a page, not two. Section 4 should carry the field table. Section 5 should open with one worked row. Section 6 can then be read as the tour it is meant to be.

## 8. What the four spare pages should carry, in order of value

1. The field table and one fully worked row (about one page). Without it a reviewer cannot audit a single cell from the paper alone.
2. The `relative` rows as a table: work, both parties, both units, and the relation as stated in the source (m ≳ n²ρ² + n; |C| < |f|^{1+δ}; m = O(n²); A = T^{1−ε}; filter time o(t^ε) against model time t). This is the paper's payload and is currently visible only as a count (about half a page). Recount first (F1).
3. The eighteen near-miss rows as a table with the quantity each holds and where it appears, marking which hold an adversary price and which hold a training cost (about half a page). This turns M7 into the paper's best section.
4. A compact party-by-unit table for the 101 attack works in the body, since Section 5.2 argues from it and the supplement's Table 2 is landscape and unreadable at column width (about half a page).
5. One page of instruction: what a priced threat model states, using the four objects Section 1 names (class, budget, criterion with tolerance, baseline), with two restatements of existing results in that form, Carlini et al.'s LiRA and Jia et al.'s PoL Property 2 with δ left symbolic. This is what the field would do differently after reading the paper, and the paper does not say it anywhere. It does not need the planned formalization section. It needs a template and two instances.

Cut to make room: Sections 3.3, 3.4, 3.6, the batch-reuse paragraphs of 6.6, the duplicated agreement sentence, and the revision narrative in 4.2 (keep the two sentences that state what the revisions added).

## 9. SoK criteria, strongest claim, fairness

Criteria. The paper meets the third criterion (a new taxonomy of an established area) in intent and will meet it in fact once the table is consistent. It touches the second (challenging a long-held belief) only in Section 7, where the belief that attacker compute is not a threat-model parameter is stated and answered in one paragraph. It does not attempt the first.

Strongest claim and its support. The strongest claim is that a two-party bound is almost absent from the attack literature (Section 5.3). It is supported in direction at any reading of the codebook (between 3 and 7 of 101 attack works). It is not supported at the stated size (3 of 11) because the count depends on an unstated rule (F1). The second claim, that attack works bound nobody more often than theory works, is stated at exactly the strength the data supports and is the best-argued passage in the paper. The third, that eighteen works hold an unnamed quantity, is supported for about a dozen of the eighteen (M7).

What the field would do differently. As written, nothing specific. The paper diagnoses and does not prescribe. Item 5 of Section 8 above is the missing half page.

Fairness. Section 7 is fair to Carlini et al.: the quotation is verbatim, it is called "a considered position rather than an oversight", and the paper distinguishes the use it rejects (compute as a restriction inside a threat model) from the use it proposes (compute as a unit of comparison). The attribution to Athalye et al. is loose (m4). Related work describes rather than judges, is grouped, and is generous. The one sentence that judges rather than describes is in Section 6.5, "it has repeatedly been restated as a universal claim about deployed ones", said of Ball et al. with no citation to any such restatement. Either cite one or cut the clause.

## 10. What I did not check

The 85 rows Section 4.4 says could not be bound to their document, beyond the rows listed in Section 6 of this review. Supplement Tables 5 and 6 row by row. The remaining roughly 150 rows of the TSV. The inter-reader agreement figure. The membership of the 17 scaling-law works. The AUC figures from Meeus et al. The venue status of the works called preprints. The S&P 2027 call's rule on supplementary length. The sparse-parity experiment in `results.tex` and `experiments/`, which no section of the paper uses. The bibliography beyond the five entries named above.
