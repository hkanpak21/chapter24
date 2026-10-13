# Sweep brief, 2026-10-13

Shared by the three lane sweeps. Each sweep agent reads this file first.

## What the survey is becoming

An SoK on machine learning security seen through the theory of computation and
the theory of information. The organizing notion, a working proposal: a security
property of a learned artifact is a complexity gap between two tasks on the same
data, the honest task (train, learn, verify) and the adversary's task (infer
membership, reconstruct, extract, evade, poison, plant or remove a backdoor or
watermark, forge a proof of training). A result is placed by

- the resource model the gap lives in:
  - information: samples, queries, bits, memory, against an adversary unbounded in time;
  - algorithmic class: SQ, CSQ, low-degree, gradient methods, bounded memory;
  - computation: time or circuit size, under a named assumption or reduction;
- the sign of the gap: adversary strictly dearer than the honest party, equal,
  cheaper, existence only, or not a gap result.

Out of scope as foundation: geometric existence results (concentration of
measure, isoperimetry, certified radii) and purely empirical attacks or
defences. List one only when a prominent theory result needs it as a limit.

## What prominent means

Published at STOC, FOCS, SODA, ITCS, COLT, ALT, CRYPTO, EUROCRYPT, TCC, S&P,
CCS, USENIX Security, NeurIPS, ICML, ICLR, JMLR, IEEE Trans. Inf. Theory, J. ACM,
SIAM J. Comput., or highly cited (OpenAlex cited_by_count), or the origin of a
definition the field uses. Include the foundations and the 2023 to 2026 frontier.

## Method

Seeds, then backward (reference lists) and forward (citers, newest first and
by citation count) on the OpenAlex API, e.g.
`curl -s 'https://api.openalex.org/works?filter=cites:W...&sort=cited_by_count:desc&select=id,title,publication_year,cited_by_count,doi&per-page=50'`.
Also WebSearch and WebFetch. Around 60 web calls at most.

## Verification rules, no exceptions

- Open every paper's arXiv, DOI, dblp or publisher page before listing it.
  A paper you did not open is not listed.
- Title and authors as printed on that page. Venue with an evidence URL, dblp preferred.
  A preprint is "arXiv preprint", never a guessed venue.
- Never give a theorem number, constant or quotation you did not see. If the
  statement comes from the abstract only, write "(abstract)".
- Corpus check: the existing corpus is
  `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/*.md`, each with
  a `title:` front-matter line. Grep with `grep -il` on a distinctive title
  fragment and record the slug, or "no".
- Known corrections, do not repeat the old errors: Bogdanov-Jones-Rosen-Zadik
  TCC'24 and Abram-Beimel-Ishai-Kushilevitz-Narayanan TCC'23 quantify security
  over size-bounded circuits, with low-degree analysis as supporting evidence
  only. Ngo-Kim arXiv:2607.15528 bounds the verifier's queries, its prover is
  unrestricted. Groce-Katz-Yerukhimovich TCC'11 covers black-box constructions
  and outputs in R^n for constant n, and excludes queries that return classifiers.
  Damian et al.'s generative-exponent bound is a detection threshold.

## Constraints

- Do not spawn sub-agents. Do not use the Agent or Workflow tools.
- Never use mcp__claude-in-chrome tools.
- Write only your one output file. Do not touch wiki/, raw/, paper/ or any other file.

## Output

`lib/literature/sweeps/2026-10-13-<lane>.md`, in this order:

1. What the field has in this lane: one paragraph naming the 3 to 6 results
   that define it, plainly, each with its key.
2. One sheet per paper, at most 20 papers, these fields one per line:
   key (IACR style, author initials plus two-digit year, e.g. HSU25),
   title, authors, venue, venue_evidence, year, link,
   lane (I information / A algorithmic class / C computation / D definition),
   honest task, adversary task, bounded party, resource, adversary class,
   assumption (named, or none), statement (in words, with where seen),
   technique, gap sign, prominence (venue tier; cited_by_count with date),
   in_corpus (slug or no), prerequisite (what a reader must know first),
   tier (deep / read / skim / cite).
3. A triage table: key, title, venue, year, lane, gap sign, in_corpus, tier.
4. Searches that returned nothing, with the vocabulary used.

Return to the caller a summary of at most 200 words: the defining results,
the papers not yet in the corpus, and anything that contradicts the
organizing notion above.
