# OpenThai-SystemOne

- **Category**: open
- **Owner / org**: iApp Technology / OpenThaiGPT (sponsor: Siam AI for H100 compute)
- **URLs**: https://openthai.ai/en/openthai-systemone ; repo https://github.com/iapp-technology/openthai-systemone ; HF https://huggingface.co/iapp/OpenThai-SystemOne ; Ollama iapp/openthai-systemone ; free preview API https://api.iapp.co.th/v3/store/openthai/systemone
- **License** (code / weights): Apache-2.0 / Apache-2.0
- **First release / last update**: HF created 2026-09-20; repo created 2026-09-20, pushed 2026-09-21 (site says 20-22 Sept; versions v0.2, v0.3 mentioned)
- **Popularity signals**: GitHub 65 stars; HF 9,737 downloads, 29 likes

## Summary
A 0.8B Thai+English System One model: Qwen3.5-0.8B-Base text tower with the 248k LM head replaced by a 256-way "slot" head, continued-pretrained on ~5B Thai tokens, then trained on ~2-3M decision examples and a Brier-loss calibration stage. The only project here with a native (non-letter) slot head and a pretraining stage for a non-English language.

## Approach / architecture
- Qwen3.5-0.8B-Base, vision encoder removed (752M parameters). Options introduced by control tokens `<|ts_opt_0|> ... <|ts_opt_254|>`; the hidden state at each `<|ts_answer|>` token is projected to 256 logits, slots beyond the option count masked, softmax. Slot 255 is "abstain" (none fit). Up to 255 options per Choice; Score 2-10 levels; Noul.
- One forward pass per request via HF remote code; also an Ollama build that does NOT use the slot head: it asks each question as a chat prompt and reads letter A-Z probabilities (2-26 options, no order-invariant mode, no abstain), after fine-tuning v0.3 for Ollama's prompt.
- Calibration: short stage with Brier loss plus per-type temperature.

## Interface
`POST /v1/systemone` mirroring TypeSafe's contract; Python `SystemOneClient` with Choice/Score/Noul; uvicorn server; Ollama >= 0.35 `/v1/systemone`; GGUF (Q8_0, Q4_K_M, bf16).

## Training & data
Pipeline scripts 00-07: model surgery -> Thai-heavy CPT (FineWeb-2 Thai, Thai Wikipedia, OPUS parallel text, machine-state text like accessibility trees and JSON; ~40 H100-hours, ~1 day) -> decision SFT on 1.81M records from 21 public Thai/English datasets (classification, NLI, QA, rating, agent and tool-selection) plus ~100k synthetic Thai/English tasks generated with Qwen3.6-35B (script supports up to 600k; any OpenAI-compatible endpoint) with option-order shuffling and abstain examples (SFT 12k steps, ~0.5 day) -> calibration -> incremental v0.2 (+3k steps) and v0.3 (+5k steps). Configs for 1x H100 are in the repo. Loss: cross-entropy SFT, then Brier + temperature for calibration; no RL.

## Reported performance
From the project page and HF card, author-reported: v0.3 "74.3 public bench" (13-subset suite from Edgar Dyck, PR #2 of the Nimble repo) vs Nimble-9B 74.8, ahead on 8 of 13 subsets; Thai intent 90.0%, news topic 98.1%, XNLI-th 77.1%. Not independently verified here. Latency not stated on the pages I fetched.

## Self-hosting notes
0.8B: CPU, MPS or CUDA; Ollama one-liner. Smallest realistic LLM-based option here.

## Assessment
Strength: complete reproducible pipeline for a small multilingual System One model, native slot head with abstain, permissive license. Weakness: author-only evaluation on a mostly English-sourced 13-subset bench; 0.8B capacity; Ollama variant has different (letter) head and fewer options.

## Sources
- https://openthai.ai/en/openthai-systemone
- https://github.com/iapp-technology/openthai-systemone (README via gh api)
- https://huggingface.co/iapp/OpenThai-SystemOne (model card)
