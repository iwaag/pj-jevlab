# Open Alternative to Jev ("so1")

- **Category**: open
- **Owner / org**: ikermoel
- **URLs**: https://github.com/ikermoel/open-alternative-jev ; PyPI `open-alternative-jev` (import `so1`); HF Space https://huggingface.co/spaces/IkerMoel/open-alternative-jev (Qwen3.5-4B demo)
- **License** (code / weights): Apache-2.0 / none (stock Qwen)
- **First release / last update**: created 2026-09-18 / last push 2026-09-25
- **Popularity signals**: ~58 stars (but its benchmark methodology is cited by notjev)

## Summary
In-process Python library ("System One" = `so1`) that packs several typed questions about one state into a single sequence and reads option letters at per-question positions in one forward pass. Notable for unusually candid benchmarking (self-corrected README, interference and option-order studies) and a claim that stock Qwen3.6-27B zero-shot edges Jev on LocalLLaMA/typed-decisions.

## Approach / architecture
- ChatML prompt: each question is a user turn; turns concatenated with a fixed placeholder answer (`_`) between them; one forward pass; logits read only at the readout positions (`logits_to_keep` on HF, `prompt_logprobs` top-20 on vLLM); softmax over option letters A-Z (max 26 options; letters must be single tokens, checked at decide time).
- Modes: `packed` (state written once, all questions in one sequence) and `separate` (one sequence per question; on vLLM uses `allowed_token_ids` + prefix cache). Finding: on vLLM, `separate` with prefix cache is fastest; packing helps on engines without prefix caching.
- `permutations=2` averages the original and reversed option order (cyclic shifts for k>2) to cancel position bias; off by default.
- Calibration: `TemperatureScaler` (single scalar fitted on held-out labels).

## Interface
Python package only (`Decider.from_pretrained`, `Choice`, `yes_no`). README states explicitly: "there is no HTTP server or drop-in API for the official Jev SDK". Backends: HF Transformers (incl. bitsandbytes 8/4-bit), vLLM.

## Training & data
None. Benchmarks: RACE-H (250 passages x 4), MMLU (1,200), LocalLLaMA/typed-decisions (400 cases, 2,000 decisions), scored with the code of third-party `Luni/laya-jev-benchmark` (author says it reproduces Laya's published numbers exactly).

## Reported performance
All author-measured (one H200 MIG slice, 35 GB) except the Jev row:
- typed-decisions, Qwen3.6-27B 8-bit zero-shot packed: accuracy 73.7%, ECE 0.020, Brier 0.113, KL-to-gold 0.27, 582 ms/case. Jev 1.13.0 row (72.7%, ECE 0.144, KL 1.44, 710 ms) "measured by the benchmark's authors via TypeSafe's API on 2026-09-18" - not by this repo. Teacher self-agreement ceiling 73.5%. Lower models: Qwen3.5-4B 59.3% (ECE 0.118), 2B 47.3%, 1.7B 45.9% (ECE 0.509), 0.6B 29.1% (ECE 0.534).
- `permutations=2`: 27B 75.5%, ECE 0.0075, KL 0.23 at 1.7x latency; 4B ECE halved.
- Temperature scaling on MMLU: ECE 5.4% -> 2.1%; on RACE-H 2.8% -> 1.1%. Fitted to teacher soft labels it improved Brier/KL but raised hard-label ECE (0.020 -> 0.135).
- RACE-H: packing 2.5x fewer tokens, 2.3x batch throughput at equal accuracy (92.9% vs 92.6%) on 27B. Interference: share of answers changed by packing 37/20/14/7.6/3.9% for 0.6B->27B; below ~4B it costs accuracy. Noise floor from padding alone is 2.7%.
- vLLM vs HF agreement in `separate` mode 99.8%, mean |dp| 0.003.
- Self-reported correction: initial "1.4x faster than batching" on MMLU was shown to be padding waste.
- Author could not reproduce an external leaderboard's claim of a 72% -> 21% yes/no collapse under option reversal (found -13.5 points on 4B, none on 27B).

## Self-hosting notes
`pip install open-alternative-jev` (+`[vllm]`, `[quant]`); works on CPU for 0.5B tests; 27B at 8-bit needs ~35 GB.

## Assessment
Most careful measurement of cross-question interference and position bias in the batch; supports the idea that bias averaging plus temperature scaling gives good calibration with no training. Caveats: gold is teacher-LLM-derived, Jev numbers come from a third party, "beats Jev" is within noise (1 point on 2,000 decisions, authors say so), and the 27B baseline is far larger/slower than Jev's reported footprint. Not wire-compatible.

## Sources
- https://github.com/ikermoel/open-alternative-jev (README, metadata)
