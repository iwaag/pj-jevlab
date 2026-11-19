# jevmlx

- **Category**: open
- **Owner / org**: bnsd55
- **URLs**: https://github.com/bnsd55/jevmlx ; JS client `@jevmlx/client` (in `js/`); BENCHMARKING.md
- **License** (code / weights): MIT / none (MLX community 4-bit Qwen quantisations)
- **First release / last update**: created 2026-09-17 / last push 2026-09-25
- **Popularity signals**: ~69 stars

## Summary
Apple Silicon (MLX) engine and CLI/HTTP server turning a schema of fields (booleans, enums, multi-selects, Pydantic models) plus a context into one batched forward pass; JSON assembled from winners with per-field probabilities. Includes a `/v1/systemone` route mapped onto its schema engine, and a community leaderboard against TypeSafe's public eval cases.

## Approach / architecture
- Schema compiled per tokenizer (codebook search for neutral alias codes whose candidate rows tokenize cleanly); context fenced with a per-context nonce; one prefill with shared KV cache; one scoring row per field (extra trie rows for multi-token options); restricted softmax. Two scorers: `labels` (default, scores option text, measured better on 7B) and `slots` (single-token letter codes, cheaper for long lists).
- Per-field telemetry: `probability`, top-3 `alternatives`, `probability_margin` (top1-top2, with `abstain_below_margin`), `legal_mass` (leak signal), ordinal stats (`expected_index`, `argmax_level`) for ordered enums, `prior_correction=True` (subtract neutral-context prior), multi-select with `calibration=<path>`, constrained MAP (implies/excludes).
- `jevmlx calibrate` fits a temperature + multi calibrator on labelled JSONL.
- Alternative backend: any OpenAI-compatible server with logprobs (one request per field, top-k only; missing options get a floor and `truncated: true`).

## Interface
`POST /decide`, `POST /v1/systemone` (`{state, questions}` -> `{model, answers, usage}`; same queue), `/v1/models`, `/health`, `/ready`; backpressure 429/413. One Metal GPU, serial worker. Presets (fraud 28 fields, support triage 30, 255-choice tariff router, etc.).

## Reported performance
Measured by contributors on 45 public TypeSafe example cases (indicative only; TypeSafe's official numbers are on a private set): agreement with consensus label (GPT-6 Astra + Claude Fable 5.1): Qwen3-8B-4bit `labels` 84.6% [71.2, 92.3] at 0.6 s/case vs `naive` generate+parse 69.3% at 1.6 s; `slots` 34.7% for Qwen3-8B (63.2% for Qwen2.5-7B). Qwen2.5-7B-4bit `labels` 82.1% vs naive 67.7%. Cited official Jev 67.8%, 0.4 s/case. Parity check flagged DRIFT (0.078 / 0.750) between batched and single-call scores. Hardware: M5 Max 128 GB. Comparison to Jev's accuracy is not like-for-like (different case sets).

## Self-hosting notes
Apple Silicon M1+, Python 3.12+, ~2 GB (3B) to ~4.5 GB (7B) weights.

## Assessment
Scoring option text beat letter slots strongly on Qwen3-8B (opposite of mini-jev's finding that letters help; different models, tasks and quantisation, so not directly comparable). Good observability fields (legal_mass, margin, parity gate). Small eval, parity drift warnings.

## Sources
- https://github.com/bnsd55/jevmlx (README, metadata)
