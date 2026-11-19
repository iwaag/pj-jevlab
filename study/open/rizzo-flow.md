# Rizzo Flow

- **Category**: open
- **Owner / org**: Rizzo AI Academy (Italy)
- **URLs**: https://github.com/Rizzo-AI-Academy/rizzo-flow ; site https://rizzo-ai-academy.github.io/rizzo-flow/ ; HF weights `rizzoaiacademy/rizzo-flow` (4B), `rizzoaiacademy/rizzo-flow-1.7b`
- **License** (code / weights): Apache-2.0 / Apache-2.0 (Spark-X2.5 base + own LoRA)
- **First release / last update**: created 2026-09-21 / last push 2026-09-25
- **Popularity signals**: ~781 stars; community issue reports (Mac M3 Pro, AMD 780M, Intel Iris Xe)

## Summary
Local-first, llama.cpp-based Jev look-alike with a Jev-compatible `/v1/systemone` endpoint and a playground UI. Starts training-free (Spark-X2.5 4B/1.7B, `--weights base`) but ships a LoRA fine-tune as default since 2026-09-25, so it is not purely training-free.

## Approach / architecture
- Every question becomes multiple choice with uppercase letters (max 26 slots, tokenizer checked per request). State prefilled once -> KV cache; each question branches from it sharing cache cells, run in one unpadded micro-batch (`--batch-size` default 4). Only answer-letter logits read at one position per question; Python does softmax, optional temperature, expected values for score, abstention policy.
- Base model: XHToken/Spark-X2.5-4B and 1.7B (Apache-2.0; claimed native 1M-token context). Runtime llama.cpp b11081 (CUDA/Vulkan/Metal/ROCm/SYCL/CPU); optional MLX backend.
- **Fine-tune** (default weights): LoRA (r16, alpha 32, all linear layers; 32.4M params on 4B), soft cross-entropy between target distribution and softmax over answer letters at last prompt position, same prompts as inference; 28,321 questions from tasksource/procedural-typed-decisions, ZefanCai/Open-Jev (redistributable release), Praveenrajus/jev-bench; 1 epoch, AdamW lr 5e-5, 41 min on one RTX PRO 6000. States overlapping evaluation sets removed. Authors say no Jev outputs used.
- Calibration: built-in per-primitive temperature scaling (`rizzo calibrate`), bound to a fingerprint of weights/precision/backend; default is uncalibrated.

## Interface
`POST /v1/systemone` (Jev-compatible, `rizzo-latest` model id, optional Bearer via `RIZZO_API_KEY`), native `POST /v1/decisions`, `rizzo decide`, playground at `/playground`.

## Reported performance
Author-measured on typed-decisions (400 cases, 2,000 decisions), RTX 5060 Ti, Q8_0, llama.cpp:
- 4B base: acc 0.574, KL 2.899, Brier 0.480, ECE 0.349, p50 201 ms. 4B fine-tuned: acc 0.648 (+0.074, CI [+0.050,+0.101]), KL 0.452, Brier 0.205, ECE 0.112, p50 195 ms. 1.7B fine-tuned: acc 0.544 (not significant gain), ECE 0.169. Jev 1.13.0 from dataset card, not re-measured: acc 0.727, KL 1.442, Brier 0.148.
- Observed base model puts 0.9999 on its pick even when wrong; fine-tune spreads mass.
- ~50 ms per single short decision; ~1 s for 21 questions on 2,000-token state; ~150 ms/decision round trip in a Snake demo.
- Known: llama.cpp KV cache ~144 KiB/token on 4B; shared-prefix scoring flips 13/777 near-ties at Q8_0.

## Self-hosting notes
Python >= 3.11, uv; `rizzo download` fetches pinned llama.cpp + 4.4 GB model; runs on 5.6 GiB GPU (Q8_0) or CPU. Tested on Windows 10 + RTX 5060 Ti; other platforms community-reported only.

## Assessment
Most polished product-like packaging and genuinely Jev-wire compatible. The LoRA recipe (soft-label CE on letter logits) is a replicable distillation recipe that visibly improves calibration. Still 8 points below Jev's card accuracy; gold labels from a ~4B teacher.

## Sources
- https://github.com/Rizzo-AI-Academy/rizzo-flow (README, metadata)
