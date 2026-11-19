# SemIf (formerly OpenJev, TheoLeeCJ/openjev)

- **Category**: open
- **Owner / org**: TheoLeeCJ (independent; "not affiliated with Jev or TypeSafe")
- **URLs**: https://github.com/TheoLeeCJ/SemIf (github.com/TheoLeeCJ/openjev redirects to the same repo, renamed); browser WebGPU demo in `webgpu-demo/`; docs in `docs/` (RESULTS, METHOD, CALIBRATION, REPRODUCE, MLX, APPLE_SILICON)
- **License** (code / weights): MIT / no weights bundled (upstream model licenses)
- **First release / last update**: created 2026-09-16 / last push 2026-09-23
- **Popularity signals**: ~4,641 GitHub stars (highest of this batch); several external PRs (MPS, EXL3, temperature calibration)

## Summary
The most popular and most evidence-oriented of the training-free reproductions. A frozen 4B model (Qwen3.5-4B) reads option-token logits directly, with committed fixtures, row-level outputs and prompt hashes. Other projects here (Rizzo Flow, Deqio) cite it as inspiration or bundle it as a model option.

## Approach / architecture
- One forward pass per decision; "native option logits" of declared options -> probabilities; no sampling, no decode loop. Prompts frozen and hashed (`prompt_sha256`).
- Modes: `direct` (fresh scoring), `serial` prefix reuse, `shared` (prefill state once, evaluate criteria in parallel as suffixes). Backends: PyTorch/CUDA, PyTorch/MPS, MLX, llama.cpp (GGUF, CPU), EXL3 bridge (Qwen3.8-27B 5 bpw), and an in-browser WebGPU build with quantised GGUF.
- Calibration: per-workload **temperature scaling** fitted on labelled decisions, out-of-fold evaluation; does not change the selected option.
- Also compared against a native reranker (Qwen3-Reranker-4B) as a baseline; direct logits were the better general-decision baseline.

## Interface
Input is JSONL (`state`, `question`, `options[{id,description}]`) via the `semif-score` CLI; a state can be a JSON object/array. The README documents no HTTP `/v1/systemone` server (no match for "systemone" in README); wire-format fidelity is not a goal, interface *pattern* is. Deqio wraps it as a model option behind its own API.

## Training & data
None. Authored fixtures (144 decisions), a 37-state x 21-criterion shared-state workload (777 decisions), WANLI (256 rows), a 102-row subset aligned to TypeSafe's public evaluation cases, and "Every" judgment grids. Fixtures, runners and raw results committed.

## Reported performance
Author-measured on one RTX 3090 unless noted:
- Latency: 21 binary criteria on one state with Qwen3.5-4B: direct typed logits 1.023 s (0 output tokens) vs autoregressive compact JSON array 5.332 s (111 tokens, 5.21x). Reuse on 777 decisions: fresh 2.33 dec/s, serial prefix reuse 10.75 dec/s, parallel suffixes 20.03 dec/s, native reranker 1.86 dec/s.
- Quality (balanced accuracy, BF16 4B): authored 0.813; WANLI 0.637; TypeSafe 102-row subset modal agreement 0.845 vs published Jev 0.883 (read from TypeSafe's published records; no live Jev run; only 102 aligned rows of TypeSafe's reported 711). 27B EXL3 on authored rows 0.958 (system-level comparison, not a controlled ablation). Browser ladder: Qwen3-0.6B 0.440, MiniCPM5-2B 0.686, Qwen3.5-4B 0.813 authored.
- Calibration ECE raw -> out-of-fold calibrated: authored 0.068 -> 0.038 (T=1.23); WANLI 0.208 -> 0.069 (T=2.50); Every 0.050 -> 0.047 (T=1.71). Authors note intervals overlap on two of the three.
- Quantisation/prefix reuse can change near-ties (documented by downstream Rizzo Flow: 13 of 777 decisions flip at Q8_0).

## Self-hosting notes
Python 3.10+, GPU that fits a 4B BF16 model (~8 GB+), or CPU via GGUF, Apple Silicon via MLX/MPS, or just the browser. Easiest to reproduce in the batch.

## Assessment
Best-documented baseline: pinned revisions, hashes, out-of-fold calibration, honest Jev comparison limits. Weak spots: no wire-compatible server, small public eval subset, comparison to Jev rests on TypeSafe's published data. Clear reference implementation for first-token option-logit reading with shared-prefix suffix batching.

## Sources
- https://github.com/TheoLeeCJ/SemIf (README, metadata; /openjev redirects)
