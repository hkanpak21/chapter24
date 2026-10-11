# Reviewer findings declined, with the reason

A finding lands here when the review was read, checked against the primary
source, and answered no. A finding answered yes is closed in a commit and does
not appear here.

### 2026-09-03-family-of-preventing-false-discovery
The round-two review asked to recode `preventing-false-discovery-hard` to
`family=none`, on the ground that the paper frames itself as adaptive data
analysis. Declined. The theorem's attack recovers sample elements from query
answers, which the codebook calls `reconstruct`, and the codebook codes the
mechanism the work uses.

### 2026-09-03-tightness-of-undetectable-watermarks
The same review offered `relative` or `measured` for
`undetectable-watermarks-lm`. Ruled `measured`. The pricing is a dollar ratio
observed once at one model size, and a measurement does not become a relation
by being a ratio.
