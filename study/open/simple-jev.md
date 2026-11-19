# Simple Jev

- **Category**: open
- **Owner / org**: Featherless AI (featherless-ai)
- **URLs**: https://github.com/featherless-ai/simple-jev ; docs/playground https://simple-jev.featherless.ai/ ; public demo API https://simple-jev-demo-api.featherless.ai/v1/ (no auth, 2k-token context, 2 RPS)
- **License** (code / weights): Apache-2.0 / upstream models
- **First release / last update**: created 2026-09-18 / last push 2026-09-30
- **Popularity signals**: ~577 stars; search results describe it as in production at Featherless (vendor claim)

## Summary
Server that takes any compatible Hugging Face model and exposes a classifier/Jev-like endpoint by reading label logits with KV-cache sharing across questions. Includes a versioned shared prompt builder, an evaluation framework (JevBench-native scoring, text and vision) and an optional fine-tuning toolkit (RFDT), so it spans training-free and trained use.

## Approach / architecture
- Prompt builder renders versioned instructions + one scoring branch per question; HF server finds the exact common token prefix across question prompts, prefills it once, and copies the KV cache for batches of suffixes (`--max-batch-size`, `--max-batch-tokens`); reads next-token logits at each row's last real token for allowed answer labels. Cache reuse lives only within a request; requests processed serially.
- Labels must each be a single distinct token (checked). Choice up to 255 options, Score 2-50 levels, Noul = truth/support judgment 0.01-0.99 from the distribution over **nine rating tokens** (not a two-way yes/no).
- Per-architecture "prompt policies" (`baseline`, `examples_binary`, `repeat_state`, `strict_mix_repeat2`) auto-selected by exact backbone configuration (e.g. Qwen3.8-27B -> examples_binary; Gemma-4-26B-A4B -> strict_mix_repeat2); a search tool compares policies on 477 quick cases per format. README warns quick set is a development/selection set, not held-out evidence. Repetition of state in some policies is a prompt-level trick to compensate for causal attention.
- Confidence for choice/score = max probability; "not calibrated probabilities of correctness". No calibration step.
- Also supports Laya via a native encoder backend and vision (image chat inputs).

## Interface
`POST /v1/classifier` with `/v1/systemone` as an alias; request `{model, state|messages, questions}` with `choice/score/noul`, `criteria` objects/arrays; response `answers` + `usage`; `usage.output_tokens` = 0, `usage.input_tokens` counts unique prefixes. Ignores `temperature`, `max_tokens`, `stream`. README says the API "takes inspiration from" TypeSafe's with project-specific behavior (e.g. 9-token Noul), so not strictly identical. Backend: HF Transformers/PyTorch (CPU, CUDA, ROCm).

## Training & data
RFDT scripts: train directly on allowed answer-token logits with the same prompt structure, dataset prep, teacher labelling, LoRA, multi-GPU, export. Hosted fine-tuned model support described as upcoming.

## Reported performance
README retrieved gives no accuracy table; eval tooling only. Demo serves `featherless-ai/gemma-4-26B-A4B-classifier`. Nothing independently verified.

## Self-hosting notes
Python 3.12+, `pip install -e ./hf-server`; runs Qwen3.5-0.8B on CPU; Gemma-4 26B-A4B or Qwen 27B need a bf16 GPU with ample memory; engine is Transformers only (no vLLM/SGLang yet per README).

## Assessment
Most complete "framework" in the batch (server + prompt policy search + eval + training), with the closest thing to a systematic way to choose prompt format per model. No calibration and no published numbers; prompt-policy selection on a quick set risks overfitting (authors flag it).

## Sources
- https://github.com/featherless-ai/simple-jev (README, metadata)
- Web search result summarising the project (search engine snippet)
