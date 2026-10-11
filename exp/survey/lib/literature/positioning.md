# Positioning

## 1. Setting

A formal claim about the security of machine learning names an attack, a model,
and something the attack achieves against it. Cryptography settles such a claim
with four objects: the adversary class that fixes what the attacker may run, the
budget that fixes how much of it the attacker may spend, the success criterion
with its tolerance, and the baseline that says what public knowledge alone
achieves. The parties are the attacker, the party that trains, the party that
audits a released model, and the mechanism that releases it. Each may be bounded
and usually none is.

## 2. What exists

Papernot, McDaniel, Sinha and Wellman [PMSW18] give the field its standing map,
in three parts: the stage of the pipeline the adversary attacks, what it is able
to do once there, and the goal it pursues. None of the three is a computational
resource. Four later systematizations repair one attack family each and report
the same absence from inside their own subfield: adversarial examples [FK24],
model extraction [SSEP24], data reconstruction [WLBZ25], and membership
inference against language models [MSJFRM25]. Desfontaines and Pejo [DP20]
catalogue the variants of differential privacy along seven dimensions. Arp et
al. [AQPWPWCR22] measure how the field evaluates rather than how it defines.
Brzuska and Couteau [BC22] and LaVigne, Lincoln and Vassilevska Williams [LLW19]
define the ratio between an adversary's work and an honest party's, in
cryptography with no machine learning content.

## 3. The gap

Each repair supplies knowledge, access or a success criterion, and none supplies
a budget. The authors state this themselves: Shafran et al. report that model
extraction has no formal definition of attack success, and Wen et al. report the
same for data reconstruction. Jia et al. [JYCDTCP21] state proof-of-learning's
security requirement as a bare inequality between a forger's cost and an honest
trainer's, and write that they cannot prove it and offer it as a conjecture.
Neither the proof-of-learning line nor the fine-grained line cites the other.
The first limitation is stated by the authors. The second is a count over this
corpus.

## 4. The claim

Formal claims about the security of machine learning cannot be compared with one
another, because almost none of them states what the attacker may spend, and the
vocabulary for stating it already exists in fine-grained cryptography and has
never been carried across.

## 5. Why it is hard

Recording a budget per adversary would lose the cases the field actually
contains, where the bound sits on the party that trains, on the party that
audits, or on the mechanism. Recording it per party admits all of them and makes
the most common answer visible, which is that no party's resources enter the
claim. Establishing that answer needs a coded corpus with a fixed vocabulary and
a deciding quotation per row, because the alternative is an impression. Part of
the field has also considered pricing the attacker and declined [CAPBRTGMK19],
so the paper answers a stated position and not an oversight.

## Status

Written on 2026-08-20. Approved on 2026-09-03.
