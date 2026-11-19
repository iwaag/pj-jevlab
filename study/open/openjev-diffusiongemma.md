# OpenJev (razorback16) - DiffusionGemma-based System One server

- **Category**: open (code Apache-2.0; also offered as hosted service by Codiv)
- **Owner / org**: razorback16; hosted by Codiv (codiv.ai)
- **URLs**: https://github.com/razorback16/openjev ; Docker `razorback16/openjev`; base model https://huggingface.co/nvidia/diffusiongemma-26B-A4B-it-NVFP4 ; hosted `https://api.codiv.ai/v1/systemone`; upstream vLLM PR vllm-project/vllm#57250 (merged 2026-09-22 per README)
- **License** (code / weights): Apache-2.0 / Apache-2.0 (DiffusionGemma, Laya, Verdict, CLM, JevK5 per README)
- **First release / last update**: created 2026-09-18 / last push 2026-09-29
- **Popularity signals**: ~561 stars. Related: mmastrac/djev (110 stars, Apache-2.0, "example server from vLLM PR 57250"), taeold/djev-run (575), githubnext/localjev (806) - see minor-projects.md

## Summary
Not an autoregressive logit reader: it uses DiffusionGemma 26B-A4B (26B total, 4B active), a discrete-diffusion model, and reads answers out of a masked canvas in a single read-only denoising pass. This is the notable DiffusionGemma base in the batch; several other projects (djev-run, LocalJev, mmastrac/djev) build on the same model. The server also routes to other people's trained models (Laya 421M, Verdict 151M, CLM, JevK5) behind the same API.

## Approach / architecture
- Canvas contains one masked slot per question (question ids hidden; model sees `q1,q2,...`); one read-only pass gives a distribution at each slot over label tokens (`yes/no`, `A/B/C`, `0/1/2`); the distribution is the answer. Confidence = 1 - H(p)/ln K. Not calibrated; "calibrated" in the tagline is a claim of the project, no calibration procedure is described in the parts read.
- Uncertainty-triggered re-reads: if any slot has entropy > 0.1, three more reads with fresh noise are averaged (all questions re-read); `samples` 1-32 overrides; `steps` 1-8 denoise steps; `think` up to 4096 tokens; `sequential` mode for long question lists (chunks of ~12 per read, chunks run in parallel).
- vLLM features required (from PR #57250): seeded canvases (`diffusion_seed_canvas`), read-only steps, step caps, pinned canvas positions; patched cap on requested logprob ids (128 -> 512) for up to 255 choices; image inputs (up to 8) with ~280 tokens each. Prefix caching enabled.
- MLX backend on Apple silicon (mlx-vlm, 4-bit, ~16 GB to load); reads one at a time.

## Interface
Jev wire-compatible `POST /v1/systemone`; the official `typesafe-sdk` works by setting `TYPESAFE_BASE_URL`; accepts `jev-latest`/`jev-preview` aliases; error shapes matched "checked against the live API" (author claim). Extensions (`images`, `steps`, `samples`, `think`, `sequential`) are optional. Also `/v1/chat/completions` for text generation with `diffusiongemma-26b`. Choices up to 255.

## Reported performance
Author-measured on RTX PRO 6000 (38% of GPU), 3 questions/request, cache-busted states: 1 request p50 31 ms (3 questions, `samples:1`); concurrency 16: 43.3 req/s p50 367 ms; concurrency 64: 57.4 req/s. Encoder models: Laya 16 questions 10 ms (short) / 109 ms (full state); Verdict 7/21 ms. CLM on RTX 3090: 99 ms single, 18 req/s at 64. Mac M3 Ultra 0.2-0.4 s per 3-question request. No accuracy numbers in the README for DiffusionGemma itself (djev-run reports JevBench 81.4% for the same base - see minor-projects.md, author-reported).

## Self-hosting notes
NVIDIA GPU >= 24 GB (NVFP4, ~18 GB weights), Docker image pins a specific vLLM commit; or Apple silicon via MLX.

## Assessment
Technically the most distinct approach in the set (diffusion canvas = natively parallel multi-question readout; avoids cross-question KV tricks). Strongest wire fidelity. Dependence on an unmerged/just-merged vLLM feature and a specific checkpoint; calibration and accuracy evidence not provided in README. Known score weakness for CLM (score ignores state).

## Sources
- https://github.com/razorback16/openjev (README, metadata)
- https://github.com/mmastrac/djev (metadata only)
