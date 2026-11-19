# jev-on-a-laptop

- **Category**: open
- **Owner / org**: rorshopping (unofficial; sibling repo `rorshopping/parallel-decisions` for GPU/Torch backend)
- **URLs**: https://github.com/rorshopping/jev-on-a-laptop ; HF Space https://huggingface.co/spaces/rorshopping/parallel-constrained-decisions (static)
- **License** (code / weights): code MIT per README (GitHub reports NOASSERTION/Other) / engine harshatheg/Qwen-2.5-1B-RLCD Apache-2.0 (cloned at setup)
- **First release / last update**: created 2026-09-16 / last push 2026-09-17
- **Popularity signals**: ~24 stars

## Summary
A study (not a product) of "parallel constrained decoding" on stock small Qwen models on an Apple Silicon laptop: prefill context once, broadcast KV across one batch row per field, evaluate all fields in one forward pass, assemble JSON in code. Its value is the candid evaluation, including a head-to-head vs Jev on TypeSafe's public eval cases.

## Approach / architecture
- Uses the community `harshatheg/Qwen-2.5-1B-RLCD` engine code (parallel decisions) with mlx-lm; logits sliced, softmax over candidate options. Fields whose choices share a first token hit a slower fallback. Raw softmax confidence: repo itself says "'Calibrated' confidence: no".
- Torch/CUDA backend with shared-prefix reuse and optional CUDA graphs (separate repo).

## Interface
Scripts only (benchmark, demo); no API; no Jev wire format.

## Reported performance
Author-measured, M5 MacBook Air 16 GB, 4-bit, 28-field fraud preset: naive JSON vs parallel decisions 1.5B 3.3 s vs 0.41 s (7.9x), 7B 11.9 vs 1.52 s, Qwen3-8B 14.3 vs 2.03 s; naive JSON never schema-valid, parallel always valid. Quality (24 labelled cases x 3 fields): 1.5B primary-field accuracy 58% (equals majority baseline 54%), 7B 96%, 8B 92%. Confidence unreliable: 7B >0.90 confident on 13 of its 20 wrong fields. Head-to-head on 20 rebuilt public cases / 373 reference question-pairs from TypeSafe's evals (343 answered by all): Opus (published) 89.8%, Sol 89.2%, Jev (published) 86.6%, local Qwen2.5-7B 73.8%, Qwen3-8B 71.2% (partial). The author concludes the local model is about 13 points behind Jev on Jev's own public benchmark and withdraws an earlier tie claim as a small-sample artifact. The dataset was rebuilt by the author, so not an official test.

## Self-hosting notes
Apple Silicon Mac, `./setup.sh && ./run_benchmark.sh`.

## Assessment
One of the more honest comparisons against Jev (Jev ahead by ~13 points vs a 7B 4-bit local model on TypeSafe's public questions). Small-sample, rebuilt data; confidence-error observation is a useful warning for calibration research.

## Sources
- https://github.com/rorshopping/jev-on-a-laptop (README, metadata)
