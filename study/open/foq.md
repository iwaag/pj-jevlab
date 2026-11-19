# Foq

- **Category**: open
- **Owner / org**: yohanargentina-oss (site foq.fr)
- **URLs**: https://github.com/yohanargentina-oss/Foq ; PyPI `foq` ; weights based on https://huggingface.co/prism-ml/Ternary-Bonsai-8B-gguf
- **License** (code / weights): MIT (code) / Apache-2.0 (Ternary Bonsai 8B, by PrismML; Foq re-hosts a SHA-256-pinned copy per README, though also says "never redistributes model weights")
- **First release / last update**: created 2026-09-19, last push 2026-09-20.
- **Popularity signals**: 9 GitHub stars.

## Summary
NOT encoder-based. Foq wraps a 1.58-bit ternary 8B decoder LLM (Qwen3-8B architecture) and reads probabilities from a single prefill pass, adding a calibration layer, Pydantic extraction and a security guard. Included here because its README is explicitly positioned against Laya and Jev.

## Approach / architecture
Reference model `foq-reflex-8b-pq2_0.gguf` (2.2 GB) = PrismML Ternary Bonsai 8B in PQ2_0 format, which requires PrismML's llama.cpp fork (not stock llama.cpp). "One feed-forward pass over your context returns calibrated probabilities" - i.e., logit reading from an autoregressive-architecture LLM, no generation for decisions; `extract()` uses grammar-constrained multi-token generation (100-300 ms). Calibration via "RLCD temperature scaling" (ECE "published" in BENCHMARKS.md, not read).

## Interface
Python `FoqEngine().system_one(state, questions)` with `Boolean` / `Choice` types, local server on port 8089 (`foq serve`), CLI (`setup`, `demo`, `inspect`, `benchmark`). Wire compatibility with `/v1/systemone` was not verified from the README. `needs_review` flag below a confidence threshold.

## Training & data
No training described; builds on Ternary Bonsai 8B plus calibration layer.

## Reported performance (author claims only, unverified)
- ~20-25 ms per decision; ~4.8 GB total memory; 4,096 context; "100% on operational suite (8B depth)".
- Claims Laya (3-model router) uses ~8.6 GB, mis-triages an emergency database-down message as non-urgent at 100% confidence, and collapses to 7-14% confidence on negation. These are competitor claims from a single-author README; the replay script is `examples/benchmark_foq_vs_laya.py` but I did not run it. Table also asserts Laya "77.8% (fails on critical triage)", a figure which matches WaterSheep's in-distribution accuracy rather than anything in Laya's docs (unclear provenance; treat as unreliable).
- No JevBench or independent results found.

## Self-hosting notes
Needs the Foq/PrismML llama-server build from GitHub Releases (Windows/Linux/macOS, plus an Apple xcframework); 2.2 GB weights.

## Assessment
Different design point (decoder LLM at ternary quantization) from the encoder group; could be useful as a contrast, but marketing-heavy README, aggressive unverified comparisons, 9 stars, and a non-standard runtime dependency limit its evidential weight.

## Sources
- https://github.com/yohanargentina-oss/Foq (README via gh api)
