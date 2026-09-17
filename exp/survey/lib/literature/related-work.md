# Related work, by axis

The corpus itself is the synthesis, coded in
`lab/results/corpus-classification/classification.tsv` and printed in
`paper/tables/04-tables.tex`. This file records what each axis contains and what
the paper says about it, so a reader can find the region before opening a table.

## The systematization this paper builds on

Papernot, McDaniel, Sinha and Wellman [PMSW18], three parts, none of them a
computational resource. The paper adopts its attack families where they fit and
adds one axis, the resource each work bounds and the party it binds.

## Systematizations of one attack family

[FK24] adversarial examples, an oracle abstraction for adversary knowledge.
[SSEP24] model extraction, no formal definition of success. [WLBZ25] data
reconstruction, a definition with a tolerance. [MSJFRM25] membership inference
against language models, the benchmarks carry a distribution shift. [SSZHTE24]
164 black-box attacks in a four-axis grid. [DP20] differential privacy in seven
dimensions. Each supplies knowledge, access or a success criterion. None
supplies a budget.

## Critiques of evaluation practice

[AQPWPWCR22] ten pitfalls across four venues over a decade. [ACW18] obfuscated
gradients. [TCBM20] thirteen defences with adaptive evaluations, all
circumvented. [CAPBRTGMK19] the checklist, and the stated position that attacker
computation should not be a threat-model parameter. These diagnose threat models
as unstated or imprecise. None diagnoses one as unpriced.

## Where the quantity already has a definition

[BC22] fine-grained one-way functions in non-uniform circuit size. [LLW19] the
relative gap, named as an object, in uniform word-RAM time. [BRSV17]
average-case fine-grained hardness, error indexed by the adversary's own
discount. [DVV16] primitives against restricted circuit classes. [BM09] the
query ceiling in the random oracle model, quoted more often than its scope
allows. No machine learning content anywhere in this group.

## Restricted adversary classes as a security tool

[CIM19] a privacy adversary bounded by the function class its attack is drawn
from. [GKVZ22] backdoors undetectable to any polynomial-time distinguisher with
oracle access. [KKOSVZ24] the white-box case under obfuscation. [DNV19] robust
learnability with a hardness profile implies one-way functions. [JCBKP20] model
extraction priced by algorithm class. [CCGJY20] extraction with a query budget
inside its definition. [DKLP22] an extraction adversary charged compute through
a proof-of-work puzzle. These are the closest works to the question this paper
asks.

## The learning-theory exponents

[AGJ21] the information exponent. [ABM23] the leap. [DPLB24, DLB25] the
generative exponent, with a low-degree lower bound and a matching efficient
upper bound. Two boundaries are quoted more often than they hold: the thresholds
were stated for detection rather than recovery, and for single-pass training.
[LOSW24] carries weak recovery through to strong recovery for polynomial links.
[Gla24] reaches vanishing population error on the Boolean parity instance.
[DTAPZK24, TME25, KJWSM26] settle what batch reuse attains. A citation-graph
sweep of this group returned no security or privacy citers.

## Training compute as a measured unit

[KMHBCCGRWA20, HBMBCRCHWCHNMDDGOSERVS22, HBEORGATS24] measure training compute
precisely and bound the trainer. [Sha23] is the one work carrying a
training-compute budget toward a security claim, and it states a hardness
requirement with no construction.
