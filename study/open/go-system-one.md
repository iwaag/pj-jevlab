# go-system-one

- **Category**: open (runtime; model is a stock Gemma, not trained by the author)
- **Owner / org**: Rui Carmo (github.com/rcarmo)
- **URLs**: https://github.com/rcarmo/go-system-one
- **License** (code / weights): MIT / Gemma license for the downloaded Gemma 4 12B IT GGUF (unsloth UD-Q4_K_XL, 7.4 GB)
- **First release / last update**: created 2026-09-22, pushed 2026-09-29
- **Popularity signals**: GitHub 5 stars

## Summary
A native Go inference runtime (hand-tuned PTX kernels loaded through the NVIDIA Driver API, no CGo, llama.cpp or CUDA toolkit at run time) that scores finite-choice, ordered-score and yes/no decisions on an UNTRAINED, pinned Gemma 4 12B instruction model. The docs state it does not load Jev weights or use a pointer head and does not claim parity; Kev's learned pointer head is described as a separate checkpoint contract.

## Approach / architecture
Compiled schema -> candidate trie of bounded token paths; prefix (state) KV reuse; independent suffix scoring per field; constrained probabilities over admitted candidates only. Probabilities are explicitly "not calibrated estimates of real-world correctness"; TypeSafe confidence parity is unverified.

## Interface
`POST /v1/decision` (boolean and string-enum fields, 1-256 contexts) and `POST /v1/systemone` (noul/choice/score adapter). Playground at `/go-system-one`.

## Training & data
None.

## Reported performance
Author: JevBench v1.4.0 public subset 196/231 = 84.85% (easy 48/48, original 71/72, hard 77/111), no failed requests; not the official sealed-set composite. Latency: pinned RTX 3060 request 72.80 ms median (from 521 ms in the first native version); automatic two-field batches 12.01 entries/s at 100 entries. Unverified by third parties.

## Self-hosting notes
Go 1.26.2, NVIDIA GPU (RTX 3060 tested), accept the Gemma license; `make setup`, `make artifacts-download`, `make run`.

## Assessment
Interesting as a systems baseline: shows a zero-shot instruct model plus trie scoring reaches ~85% on JevBench public items. No training, so no RLCD or calibration method beyond what the model gives.

## Sources
- https://github.com/rcarmo/go-system-one (README; docs/jev-like.md; docs/artifacts.md via gh api)
