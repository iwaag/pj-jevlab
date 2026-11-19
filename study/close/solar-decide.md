# Solar Decide (Upstage)

- **Category**: close
- **Owner / org**: Upstage (Korea)
- **URLs**: https://openrouter.ai/upstage/solar-decide ; https://llm24.net/model/solar-decide
- **License** (code / weights): proprietary, hosted
- **First release / last update** (as seen 2026-10-01): beta 2026-09-22 on Upstage console (modelsystem.one registry); LLM24/OpenRouter page lists 2026-09-28 (OpenRouter route date)
- **Popularity signals**: OpenRouter listing (1 provider); referenced in community repos and benches

## Summary
Hosted System One endpoint built on Solar Mini 4, using the same /v1/systemone schema as Jev. Differentiators are a 512K context and strong Korean/multilingual coverage.

## Approach / architecture
Per OpenRouter listing: runs on Solar Mini 4 (35B MoE, ~3B active, ~524K context); single forward pass, no prose, probabilities read from the model. Exact head/decoding method not disclosed.

## Interface
`/v1/systemone` with choice / score / noul, Jev-compatible; available through OpenRouter. A zero-data-retention Upstage endpoint exists (per community bench PR).

## Training & data
Not disclosed.

## Reported performance
Third-party community bench (umstek/zero-shot-ie-bench PR, unverified, small n): mixed pool of 48 questions 95.8% vs cloud Jev 93.8%; multilingual suite (54 texts, 9 languages) 100%; latency 0.308 s/question mixed, 0.885 s/text multilingual; about $1.8e-5/question. Vendor performance claims: none seen.

## Self-hosting notes
None; hosted only.

## Assessment
Pricing is inconsistent across sources: $0.05/MTok input on OpenRouter (output free); registry lists $0.10 with 50% off. Strong choice for multilingual/long-state comparisons against Jev. Benchmarks are tiny and community-run.

## Sources
- https://openrouter.ai/upstage/solar-decide (via search summary)
- https://llm24.net/model/solar-decide
- https://github.com/umstek/zero-shot-ie-bench/pull/17
- https://systemonemodels.tech/system-one-models
