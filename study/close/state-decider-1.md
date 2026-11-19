# Decider 1 / state-decider-1 (meraGPT)

- **Category**: close (hosted per registry; weights status not stated on vendor page)
- **Owner / org**: meraGPT
- **URLs**: https://meragpt.com/
- **License** (code / weights): not stated; listed as Proprietary in the systemonemodels.tech registry
- **First release / last update** (as seen 2026-10-01): ~2026-09-22 (registry)
- **Popularity signals**: low; not independently covered in what I found

## Summary
Small hosted System One model speaking `/v1/systemone`; compatible with typesafe-sdk by changing the base URL.

## Approach / architecture
Undisclosed parameter count. 4,096-token context. Up to 20 questions per state in one pass.

## Interface
`/v1/systemone`; yes/no, choice, score. $0.03/MTok input, output free (e.g., five decisions over 1,000-token state ~ $0.00003).

## Training & data
Not disclosed.

## Reported performance
Vendor-claimed: accuracy 0.768 vs Jev 0.727 on a typed-decisions benchmark; KL divergence 0.096 vs 1.442; Brier 0.052. Benchmark not identified; unverified.

## Self-hosting notes
No info on weights.

## Assessment
Cheaper than Jev, short context. The comparison is self-reported and the benchmark is unnamed, so treat skeptically.

## Sources
- https://meragpt.com/
- https://systemonemodels.tech/system-one-models
