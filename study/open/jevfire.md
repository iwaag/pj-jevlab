# JEVfire

- **Category**: open
- **Owner / org**: kikoncuo
- **URLs**: https://github.com/kikoncuo/jevfire ; visual guide https://kikoncuo.github.io/jevfire/learn.html ; docs `docs/api.md`, `docs/deployment.md`, `benchmarks/`
- **License** (code / weights): MIT / none
- **First release / last update**: created 2026-09-16 / last push 2026-09-18
- **Popularity signals**: ~71 stars

## Summary
A FastAPI sidecar over an existing vLLM CUDA server that assigns typed variables from finite choices by scoring verified single-token labels, then assembles JSON in code. Focus is latency vs grammar-constrained JSON and game-agent demos (browser Mario, racing cars, villagers with WebLLM/WebGPU).

## Approach / architecture
- Maps each field's options to verified single-token labels; asks vLLM for their scores (logprobs) with prefix reuse; picks the best label per field. Boolean or 2-255 string choices per field; fields are independent (values do not condition on siblings). 129-255 choices require an optional version-checked vLLM patch raising the requested-score cap 128 -> 256.
- Parallelism: independent fields batched through vLLM; shared prefix reused "when the engine cache permits"; "cache the right boundary" (aligned prefill for hybrid-attention model) cut long-context 12-field median 2,167 -> 255 ms warm.
- Calibration: none; README says relative label probabilities are "not calibrated confidence". Recommends an explicit `unknown` choice.
- README clarifies other projects that actually train (AlexWortega/openjev NLI fine-tune of Qwen3.5-4B, Verdict 151M ModernBERT, RLCR).

## Interface
Own API `POST /v1/decisions` (Swagger at /docs, `/health`); not the Jev wire format (no `/v1/systemone` mention). Backend: vLLM 0.29.0 only (tested with Qwen3.8-27B-FP8). Browser SDK uses WebLLM.

## Reported performance
Author-measured, Qwen3.8-27B-FP8 on RTX PRO 6000 Blackwell, 5 trials per cell (synthetic fixtures; authors stress initial estimate):
- Fresh prefix vs constrained JSON generation: 4 fields 877.5 -> 109.9 ms (7.98x); 12 fields 2239.4 -> 330.1 (6.78x); 28 fields 5113.1 -> 496.9 (10.29x); 28 fields warm prefix 346.3 ms (14.77x); long context 12 fields 2951.1 -> 1060.8 (2.78x).
- Mario in browser with Qwen3.5 0.8B: 71.26 ms mean worker inference per action, 511 accepted choices (hybrid with a physics guard; one level). Racing: faster scoring did not make drivers better.
- No accuracy benchmark; "representative task accuracy and other models still need evaluation".

## Self-hosting notes
Python 3.11+, existing vLLM CUDA server; tokenizer must match served revision.

## Assessment
Good evidence for the speed side (parallel logit scoring vs JSON) and cache-boundary engineering; no accuracy or calibration evidence, no Jev API. Mostly relevant for latency engineering ideas.

## Sources
- https://github.com/kikoncuo/jevfire (README, metadata)
