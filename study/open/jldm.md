# JLDM (Jev-like Fast Decision Machine)

- **Category**: open (tooling only; no trained model)
- **Owner / org**: wkzhang81
- **URLs**: https://github.com/wkzhang81/JLDM
- **License** (code / weights): MIT / none (uses third-party Qwen3.8-27B GGUF quantization)
- **First release / last update**: created 2026-09-24, pushed 2026-09-24
- **Popularity signals**: GitHub 0 stars

## Summary
Not a trained model. A Chinese-language CLI + single-file web UI that runs Choice-style decisions on a local KoboldCpp server: a GBNF grammar restricts the single generated token to the option letters, then per-letter logprobs are read from KoboldCpp's `last_logprobs`, merged across same-letter token variants with logsumexp and softmaxed with a user-set temperature (default 1.5). Optional image input via mmproj.

## Approach / architecture
Zero-shot. Default model: a community Qwen3.8-27B GSQ-RCO IQ3_XXS "Uncensored" GGUF with MTP (~13 GB VRAM; RentedNoodle on HF); runs in 16 GB VRAM per README. One request per decision, 300-600 ms stated. Local mode capped at 5 options because KoboldCpp 1.121 returns at most 5 top logprobs; cloud mode via an OpenAI-compatible endpoint. Temperature is manual, not fitted.

## Interface
Own JSON schema (`reference`, `question`, `options`, `images`, `temperature`); no `/v1/systemone`, no Score or Noul types.

## Training & data
None.

## Reported performance
None beyond stated latency; no accuracy or calibration data.

## Self-hosting notes
KoboldCpp >= 1.121 plus the GGUF; Python stdlib only.

## Assessment
Out of scope for trained-model comparison; included as a data point that "letter-logit readout with grammar" is the common zero-shot trick.

## Sources
- https://github.com/wkzhang81/JLDM (README via gh api; Chinese)
