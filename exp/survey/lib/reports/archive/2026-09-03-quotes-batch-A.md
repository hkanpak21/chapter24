# Quote supply, batch A, 2026-09-03

Twelve `cls_evidence` rows filled from the primary PDFs. No coded value changed. Full
detail (page, section, extraction artifacts) is in each page's `cls_evidence_src`.

| slug | party, unit, tightness as coded | quotation | source | agree or DISPUTE |
| --- | --- | --- | --- | --- |
| active-learning-model-extraction | attacker, queries, budget | "Let A be an adversary interacting with S with a maximum budget of q queries." | Experiment 1, §3.1, p. 10 | agree |
| adaptive-attacks-defenses | attacker, perturbation, budget | "Projected Gradient Descent (Madry et al., 2017) is a strategy for finding an adversarial example x0 for an input x that satisfies a given norm-bound." | §2.1, PGD paragraph, p. 5 | agree |
| adversarial-spheres | attacker, perturbation, budget | "we prove that any model which misclassifies a small constant fraction of the data manifold will be vulnerable to adversarial perturbations of size O(1/√n)." | Introduction, bulleted results, p. 2 | agree |
| beyond-labeling-oracles | none, none, unstated | "We are not aware of any ME literature that formally defines what makes model extraction attacks successful." | §3.2, "Primer on ML costing", p. 3 | agree |
| blind-baselines-beat-mia | none, none, unstated | "we show that blind attacks—that distinguish the member and non-member distributions without looking at any trained model—outperform state-of-the-art MI attacks." | Abstract, p. 1 | agree |
| calibrated-proof-of-work-extraction | attacker, time, measured | "This deters attackers by greatly increasing (even up to 100x) the computational effort needed to leverage query access for model extraction." | Abstract, p. 1 | agree |
| computational-differential-privacy | attacker, time, poly | "This adaptation is obtained by considering a ppt adversary A, and requiring that f "looks differentially private" to every such A." | §2, paragraph before Definition 3 (IND-CDP), p. 5 | agree |
| cryptanalytic-extraction-nn | attacker, queries, measured | "For example, we extract a 100,000 parameter neural network trained on the MNIST digit recognition task with 2^21.5 queries in under an hour, such that the extracted model agrees with the oracle on all inputs up to a worst-case error of 2^-25." | Abstract, p. 1 | agree |
| curse-of-concentration | attacker, perturbation, budget | "In this special case, our attacks only need to perturb the test instance by at most O(√n) to make it misclassified, where n is the data dimension." | Abstract, p. 1 | agree |
| do-mias-work-on-llms | none, none, unstated | "We find that MIAs barely outperform random guessing for most settings across varying LLM sizes and domains." | Abstract, p. 1 | agree |
| empirically-measuring-concentration | attacker, perturbation, budget | "We use it to empirically estimate the intrinsic robustness to ℓ∞ and ℓ2 perturbations of several image classification benchmarks." | Abstract, p. 1 | agree |
| fine-grained-one-way-functions | attacker, circuit size, exponent | "At a high level, f is an (ε, δ)-FG-OWF if all circuits of (slightly higher) size o(\|fm\|^1+δ) have probability at most ε to find a preimage of fm(x) for a random input x." | §2.2, informal definition before Definition 6, p. 8 | agree |

Notes on extraction artifacts, kept out of the table above and recorded in full in each
page's `cls_evidence_src`: `adaptive-attacks-defenses`'s epsilon after "≤" extracts as an
unreadable control byte (0x0F) with `pdftotext` and the quotation stops before it rather
than reproduce a non-character; `adversarial-spheres` and `curse-of-concentration` both
drop the square-root glyph before `n`, rendering `O(1/√n)` and `O(√n)` as `O(1/ n)` and
`O( n)`; `empirically-measuring-concentration` renders `ℓ∞`/`ℓ2` with a backtick in place
of the ℓ; `cryptanalytic-extraction-nn` drops superscripting so `2^21.5` and `2^-25`
appear as `221.5` and `2−25`. All four are known `pdftotext` font/glyph failures, not
absent text, and the surrounding sentence was verified readable and verbatim in every
case with `grep -a`.

No disputes: all twelve quotations support the `cls_party`/`cls_unit`/`cls_tightness`
values already on the page.
