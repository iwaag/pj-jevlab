# Tev1 (tev1-4B-experimental, Together AI)

- **Category**: open (weights on HF; endpoint on Together)
- **Owner / org**: Together AI (togethercomputer)
- **URLs**: repo https://github.com/togethercomputer/tev1 ; weights https://huggingface.co/togethercomputer/Tev1-4B-experimental ; blog https://www.together.ai/blog/how-to-train-your-own-jev
- **License** (code / weights): MIT (code, original docs); HF card lists base_model Qwen/Qwen3.5-4B, no license field in metadata I fetched; repo says training data and weights are not bundled and third-party datasets/weights have their own terms
- **First release / last update**: created 2026-09-23, pushed 2026-09-24
- **Popularity signals**: GitHub 193 stars; HF 2,805 downloads, 25 likes

## Summary
Ordinary LoRA SFT of Qwen3.5-4B on a mixture of 37,840 decision examples to output a single answer letter (2-24 options). Explicitly Jev-inspired but openly next-token: not non-autoregressive and not a probability model; logprobs "are model preferences, not calibrated confidence". Marketed as a ~$17, ~25-minute fine-tune recipe.

## Approach / architecture
Qwen3.5-4B with Qwen's existing LM head; prompt = state, question, lettered options; answer = one letter; example client constrains output to option letters and returns token logprobs. No slot head, no shared-prefix parallelism, no temperature fit in the repo.

## Interface
Together endpoint (OpenAI-style) with logprobs; `examples/decide.py`; no `/v1/systemone`. Ollama `tev1` library entry and a vllm.cpp PR (#3312) exist per search results (not fetched).

## Training & data
"new v1" dataset: 37,840 unique training + 4,568 validation examples across language classification, policy decisions, routing and synthetic research classification (builders in `build_all.py`, `fetch_sources.py`). LoRA SFT: rank 8, 1 epoch, lr 5e-5, 2,048-token limit (training example's saved starting recipe; the repo says exact job settings still need verification). No Jev outputs used. No RL, no calibration step.

## Reported performance
Author dev evals only: 880/1,000 main decisions and 300/300 policy-transfer decisions (reused development benchmarks, not untouched tests). No ECE/Brier reported in the README.

## Self-hosting notes
Weights open on HF but the intended path is Together fine-tuning/hosting; any Qwen3.5-4B stack can run it as a text-generation model.

## Assessment
The weakest Jev analogue in the sense of calibration (no probabilities by design), but the cheapest and simplest baseline. Useful to a lab as a lower-bound baseline: what plain letter-SFT achieves without readout calibration.

## Sources
- https://github.com/togethercomputer/tev1 (README via gh api)
- https://huggingface.co/api/models/togethercomputer/Tev1-4B-experimental
- web search summary (alphasignal.ai, ollama.com/library/tev1) for the $17 / 25 min claim
