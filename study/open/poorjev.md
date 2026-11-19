# poorjev

- **Category**: open
- **Owner / org**: rupeshpoojary9 (individual)
- **URLs**: https://github.com/rupeshpoojary9/poorjev (crossbench/ directory holds comparison harness)
- **License** (code / weights): MIT / uses a third-party zero-shot NLI model (name not stated in README; ~400 MB download)
- **First release / last update**: created 2026-09-19, last push 2026-09-21.
- **Popularity signals**: 10 GitHub stars.

## Summary
"The poor man's Jev": Choice/Score/Noul API over a small local zero-shot NLI model, with the project's emphasis on post-hoc calibration (temperature scaling, conformal abstention) and an MCP server for Claude Code. Its main contribution is a reproducible cross-system benchmark (Jev API vs Von vs Laya vs poorjev) with candid reporting that it loses to Jev and to Von on key axes.

## Approach / architecture
One batched forward pass of a local zero-shot NLI model scoring each option as an entailment hypothesis, then temperature scaling (5-fold CV) and conformal thresholding for "I don't know, escalate" signals. Outputs are constrained to declared options by construction (tested against NaN/inf/negatives). Optional LLM backend is on the roadmap. Lesson noted by the author: the local model is strong on concrete questions and weak on abstract ones.

## Interface
Python `Client().ask(state, questions)` with `Choice`, `Score`, `Noul`; MCP server (`poorjev serve`) exposing `gate`, `judge`, `classify`, `rate`, `decide`; `poorjev eval` / `poorjev calibrate` CLIs. Not stated to expose a `/v1/systemone` HTTP endpoint.

## Training & data
No training; calibration fit on a 55-item / 160-decision hand-labelled eval set (one labeller, English, support-flavoured; author flags it as small).

## Reported performance (author-run; crossbench harness released)
- Own eval: accuracy 0.781; ECE 0.170 raw -> 0.071 calibrated (T=2.71, cross-validated).
- Crossbench (Jev called via API, Von, Laya, poorjev on identical inputs): Banking77 (n=154): acc Jev 0.812 / Von 0.838 / Laya 0.519 / poorjev 0.656; ECE 0.084 / 0.135 / 0.388 / 0.414. Multi-primitive set (n=160): acc 0.906 / 0.775 / 0.775 / 0.781; ECE 0.045 / 0.108 / 0.215 / 0.071. At 10% error budget, answers 55% of decisions and escalates the rest.
- This is a competitor-run benchmark, but it reports results unfavorable to the author and publishes raw results; I did not re-run it. The Laya figures reflect the base checkpoint (not the fine-tuned one).

## Self-hosting notes
`pip install "poorjev[local]"`; CPU only needed; ~400 MB model download; no API key.

## Assessment
Strengths: honest calibration-centred framing, reproducible cross-system comparison (useful independent data on Laya/Von/Jev), simple MCP integration. Weaknesses: small and weak backend, poor high-cardinality calibration (Banking77 ECE 0.414 unchanged by recalibration), tiny eval set, no HTTP Jev-compat endpoint. The crossbench harness is the reusable part.

## Sources
- https://github.com/rupeshpoojary9/poorjev (README via gh api)
