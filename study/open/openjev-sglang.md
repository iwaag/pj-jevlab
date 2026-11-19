# openjev-sglang

- **Category**: open
- **Owner / org**: ekzhang (Eric Zhang)
- **URLs**: https://github.com/ekzhang/openjev-sglang (Python package `openjev`)
- **License** (code / weights): no license declared on GitHub (gh api returned none; repo has no LICENSE file in root listing) / Qwen3.6-35B-A3B (NVFP4 checkpoint from NVIDIA)
- **First release / last update**: created 2026-09-17 / last push 2026-09-25
- **Popularity signals**: ~335 stars

## Summary
A Jev-wire-compatible server ("TypeSafe/Jev HTTP API") using Qwen3.6-35B-A3B on SGLang with radix caching, deployed on Modal (B200). Prefill-only, first-token readout; emphasises serving engineering and strict API behaviour.

## Approach / architecture
- Render native chat template once (thinking disabled), split into common prefix + per-question suffix. Send prefix to `/generate` with `max_new_tokens=1` to warm SGLang's radix cache; then concurrently send `prefix + suffix + assistant header + "Answer:\n"` for each question with `max_new_tokens=1`, requesting `token_ids_logprob` for each answer label and `logprob_start_len=-1`. N+1 one-token calls for N questions.
- Labels: A-Z then verified single-token letter combinations (AA, AB ...) up to 64 options (Qwen tokenizes `10`, `64` as multiple tokens, so numerals are avoided); all 64 verified at startup.
- Renormalise label logprobs with stable softmax; Noul = P(yes); Choice = argmax + distribution; Score = sum(index * p). Confidence = 1 - H(p)/log K. Temperature setting (default 1.0) applied during label normalisation; no calibration fitted ("not calibrated estimates of correctness").
- Radix reuse is "opportunistic, not a pinned KV session"; hybrid Qwen (mamba) recurrent state and cache pages can reduce hits; `--mamba-radix-cache-strategy extra_buffer`. SGLang 0.5.19 Rust frontend omits cached-token counts.

## Interface
`POST /v1/systemone` with `jev-latest` alias; accepts string/object/array state and chat-message state (rendered with native chat template); `/v1/models`, `/v1/limits`, `/health`, Scalar docs. Limits: 64 questions, 2-64 answers, 2 MiB body, 32,768 tokens per branch; 422/413/529/504 error shapes. Optional Bearer auth. No requests go to TypeSafe.

## Reported performance
README retrieved gives no accuracy or latency tables; a smoke command reports startup wait, inference latency and cache usage; repo has an `evals/` directory (not read). Nothing verified here.

## Self-hosting notes
Targets Modal B200 (`modal deploy modal_app.py`, scale to zero, 5-minute idle); can connect to an existing SGLang (`openjev serve --connect`). Heavy hardware for a 35B MoE.

## Assessment
Cleanest published design for the prefix-cache + one-token-per-question pattern with the Jev wire format; honest about radix-cache uncertainty. Missing calibration and published quality numbers. Missing license is a practical problem for reuse.

## Sources
- https://github.com/ekzhang/openjev-sglang (README, metadata, repo contents listing)
