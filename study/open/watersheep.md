# WaterSheep

- **Category**: open
- **Owner / org**: SamratDuttaOfficial (HF: samratduttaofficial)
- **URLs**: https://github.com/SamratDuttaOfficial/WaterSheep ; HF https://huggingface.co/samratduttaofficial/WaterSheep ; demo Space samratduttaofficial/WaterSheep ; site https://samratduttaofficial.github.io/WaterSheep/
- **License** (code / weights): Apache-2.0 / Apache-2.0
- **First release / last update**: repo created 2026-09-29, last push 2026-09-29 (HF created 2026-09-29).
- **Popularity signals**: 1 GitHub star, 18 HF downloads, 1 like (very new).

## Summary
Encoder-based (ModernBERT-base, 154M) calibrated decision model with Noul, Choice, Score and an added multi-label type, trained on a large mix of public datasets plus Qwen3.5-4B-generated synthetic decisions. Runs in Python, as ONNX, and in the browser via a JS file. Newest of the projects (appeared 2 days before today).

## Approach / architecture
`answerdotai/ModernBERT-base` with a decision head (154.3M params in safetensors), `trust_remote_code` HF pipeline. Types: `noul` (P(yes)), `choice`, `score` (expected level), `multi` (labels above threshold); a probability per option. Calibration: temperature per question type fitted on a validation split.

## Interface
`transformers.pipeline(model=..., trust_remote_code=True)`, Python package (`WaterSheep.decide`, `.ask` with Jev-like `state`/`questions` schema and `criteria`), CLI with `--serve` (local HTTP on port 8766), HF Inference Endpoint payload, `watersheep.js` (browser) and `onnx/model_quantized.onnx`. Not stated to be wire-compatible with `/v1/systemone`.

## Training & data
Dozens of openly licensed public datasets (listed on HF card: e.g., hh-rlhf, banking77, clinc_oos, go_emotions, MMLU-Pro, BoolQ, nli sets, reward-bench, Aegis safety, jailbreak sets, legal sets), plus synthetic decisions from Qwen3.5-4B with verification filtering. Training recipe and scripts released (`scripts/run.sh`).

## Reported performance (author-measured; not compared to Jev)
- In-distribution test split 77.8% acc, ECE 0.026; held-out datasets 61.2% acc, ECE 0.043.
- Per-benchmark examples: prompt_injection 91.4%, HateCheck 75.1%, XSTest 73.6%, GoEmotions 22.4%, legalbench tasks from 21% to 86%. Note HateCheck/XSTest/legalbench listed as "not in training".
- No Jev, JevBench, or Laya/Von comparison in the sources consulted. English only; long inputs truncated; scores weakest.

## Self-hosting notes
Small model; runs on CPU or in-browser; Git LFS needed for git clone.

## Assessment
Strengths: Apache-2.0, small, multi-label support, browser/ONNX packaging, broad data with transparent provenance (NOTICE), reasonable held-out calibration. Weaknesses: brand-new, nearly zero adoption, no Jev-compat API, no competitive benchmarking, trust_remote_code requirement. Worth watching for the data-recipe, not yet for quality claims.

## Sources
- https://github.com/SamratDuttaOfficial/WaterSheep (README via gh api)
- https://huggingface.co/samratduttaofficial/WaterSheep (card + HF API)
