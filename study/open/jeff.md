# jeff

- **Category**: open
- **Owner / org**: logan-markewich (individual)
- **URLs**: https://github.com/logan-markewich/jeff ; base model https://huggingface.co/knowledgator/gliformer-large-v1
- **License** (code / weights): MIT (code) / GLiFormer base is Apache-2.0 per HF metadata; jeff ships no new weights, it downloads `knowledgator/gliformer-large-v1`.
- **First release / last update**: created 2026-09-19, last push 2026-09-20.
- **Popularity signals**: 276 GitHub stars. GLiFormer-large-v1: 1,800 HF downloads, 163 likes.

## Summary
> **Correction (2026-10-02, [hype_and_reality](../hype_and_reality/README.md)):** GLiFormer-large-v1 is 575.6M parameters per its HF card, and the locally downloaded `pytorch_model.bin` is 2.30 GB fp32, which is consistent with that figure. The "~400M" below repeats jeff's README.

A self-hosted implementation of TypeSafe's System One HTTP API powered by an off-the-shelf zero-shot classifier (GLiFormer, ~400M, DeBERTa-based per the token-count note). It is a server/adaptor, not a newly trained model: no Jev-specific training. Its README is unusually frank ("Cheaper to self-host, but less accurate than jev").

## Approach / architecture
Knowledgator GLiFormer-large-v1 (~400M); the code runs the DeBERTa encoder (optionally ONNX int8) then RNN + classification head in PyTorch. Probabilities are normalized sigmoids, temperature-scaled at 3.2 (`JEFF_TEMPERATURE`; set 1 to disable); confidence = (p_max - 1/n)/(1 - 1/n). Noul questions get separate encoder passes (`JEFF_ISOLATE=nouls`); choice and score questions share a pass and can influence each other (`JEFF_ISOLATE=all` for independence at extra cost). So not strictly one pass for all questions. Noul modes `yes_no` (default) / `single`; the author's issue note says Noul returns the negative label regardless of state for some label-pair formulations.

## Interface
Drop-in for the official `typesafe-sdk` via `TYPESAFE_BASE_URL`; endpoints `POST /v1/systemone`, `GET /v1/models`, `/healthz`, `/stats`; model aliases `jev-latest`, `jev`. Bearer keys, rate limiting, request batching (default batch 16, wait 5 ms), queue limit with 529. Modal deployment scripts (L4 GPU), ONNX CPU path.

## Training & data
None by jeff itself; relies on GLiFormer pretraining.

## Reported performance (author-measured; JevBench item run by the benchmark's author)
- Own bench, 1,600 items / 8 datasets: AG News 75.5% (jev 90.5%); sequential p50 from a laptop 151 ms via Modal L4 HTTP vs jev 129 ms; ~$2.6 vs ~$15.6 per 1M single-question requests.
- JevBench v1.2.2 (run by Benchmark Heaven, official): score 66.9 (#9 of 18) vs Jev 75.3 (#2); Intelligence 63.9 (#14), Calibration 64.6, Speed 63.5, Cost 76.6; easy/standard/judge/hard accuracy 100/76/61.6/37.7%; hard-tier ECE 0.185 vs Jev 0.061; CPU p50 0.94 s (4 threads Ryzen 5 3600).
- Von's card (JevBench v1.4) lists jeff (GLiFormer-large ~400M): Intelligence 36.8, composite 30.6, sealed 0.331 - the best sealed score of the encoder group it lists.
- fastino's GLiNER2.5-Decide card: "GLiFormer large-v1" 49.0% on fast-decisions (vs 60.2% for GLiNER2.5-Decide) (vendor benchmark).
- CPU/ONNX deployment is slower and more expensive than hosted jev per the README.

## Self-hosting notes
`uv sync`, download model (~1.6 GB fp32 est.), `uv run jeff`. Device: CUDA, then MPS, then CPU. Python 3.12. HTTP throughput ~50 req/s per container on L4.

## Assessment
Strengths: easiest way to get a Jev-API-compatible endpoint backed by a stock open model; strong ops features (batching, rate limit, auth); honest benchmarks including JevBench. Weaknesses: no training for Jev-style tasks, weak on reasoning/judge/hard tiers, Noul brittleness, calibration needs tuning. Useful as a baseline/harness and wire-protocol reference rather than a quality model.

## Sources
- https://github.com/logan-markewich/jeff (README; bench/RESULTS.md)
- https://huggingface.co/api/models/knowledgator/gliformer-large-v1
- https://huggingface.co/wfzyx/von ; https://huggingface.co/fastino/GLiNER2.5-Decide
