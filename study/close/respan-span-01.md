# Span-01 (Respan)

- **Category**: close
- **Owner / org**: Respan (formerly Keywords AI)
- **URLs**: https://openrouter.ai/respan/span-01 ; https://modelsystem.one/news/span-01-hyper-parallel-classifier/ ; benchmark dataset https://huggingface.co/datasets/respanai/behavior-benchmark
- **License** (code / weights): proprietary, hosted; early access via waitlist
- **First release / last update** (as seen 2026-10-01): 2026-09-24 (with free Span-01 Lite); listed on OpenRouter after claiming 4.5B tokens processed (RuntimeWire)
- **Popularity signals**: OpenRouter listing; used in a community project as free default judge

## Summary
A behavior-scoring classifier: given a conversation/trace span and plain-language behavior definitions, returns for each the probability the behavior is present / absent / not observable. A specialized, non-generic cousin of Jev for LLM/agent evaluation, guardrails and monitoring.

## Approach / architecture
Non-autoregressive single forward pass, trained with RLAIF (modelsystem.one summary of Respan's material). Size undisclosed.

## Interface
Behavior-definition questions over a trace; per-question probabilities in parallel. Available on OpenRouter. Respan also operates a Jev gateway (`https://api.respan.ai/api/typesafe/v1/systemone`), separate from Span-01. Span-01 Lite is free; Span-01 is $0.02/MTok input.

## Training & data
Not disclosed. Respan's benchmark: 1,990 traces, 34,885 trace-behavior pairs, 19 languages; labels derive from model agreement, not human ground truth.

## Reported performance
Vendor-run (Respan): overall F1 0.806 vs Jev 0.716, Claude Sonnet 5 0.719, GPT-6 Sol 0.885 (Digital Applied: GPT-6 Sol beats all small models in 6 of 7 domains). Another cut: Span-01 84.3, Jev 1.13.0 71.5, GPT-6 Luna 81.5, GPT-5.6-terra 83.7. Respan's 11-model comparison (vendor judging competitors, no third-party audit): Jev 1.13.0 had best accuracy 0.932 and ECE 0.045. Not independently verified.

## Self-hosting notes
None.

## Assessment
Cheapest hosted option (cost illustration: 1M x 2K-token conversations ~ $40/month). Domain-narrow; useful for LLM-judge-style evaluation. Treat F1 claims cautiously given label provenance.

## Sources
- https://openrouter.ai/respan/span-01 (search summary)
- https://modelsystem.one/news/span-01-hyper-parallel-classifier/
- https://www.digitalapplied.com/blog/decision-models-probabilities-not-text-api
- https://www.respan.ai/docs/apis/type-safe-gateway/typesafe-systemone
