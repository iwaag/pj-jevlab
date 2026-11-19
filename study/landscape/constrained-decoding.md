# Constrained decoding and structured output

Items marked (verified) came from search results this session; the rest are background knowledge.

## Overview
"Typed output" was previously solved by making an autoregressive LLM emit valid JSON/enum. Two families:
1. **Grammar/logit masking at decode time**: compile a JSON Schema, regex or CFG into an automaton; at each step set invalid-token logits to -inf. Structural validity is guaranteed; semantic correctness is not.
2. **Prompt + validate + retry** libraries wrapping the above or vendor APIs (Instructor, DSPy signatures, Pydantic AI, BAML).
Vendor "JSON mode / Structured Outputs" (OpenAI, Anthropic, Gemini, etc.) are server-side constrained decoding behind an API.

Common to all: the model is still **autoregressive** (latency scales with output length, typically 0.5-several seconds for a short JSON), output is **sampled text**, and any probability is at best a token logprob that you must extract and calibrate yourself. Constraints can also hurt quality ("Let Me Speak Freely?" finds format restrictions degrade reasoning) and introduce distribution distortion (masking renormalizes mid-sequence).

## Key works
- Outlines, "Efficient Guided Generation for LLMs" - https://arxiv.org/abs/2307.09702 ; https://github.com/dottxt-ai/outlines - FSM/regex index over the vocabulary.
- XGrammar (MLSys 2025) - https://arxiv.org/abs/2411.15100 ; https://github.com/mlc-ai/xgrammar - persistent-stack PDA, precomputed context-independent token masks, <40 us/token (verified); default in vLLM/SGLang/TensorRT-LLM. XGrammar-2 for agentic dynamic structures: https://arxiv.org/abs/2601.04426 (verified).
- llguidance (Microsoft, Rust, lazy lexer, Earley parser) - https://github.com/guidance-ai/llguidance ; Guidance https://github.com/guidance-ai/guidance. Used by OpenAI structured outputs per vendor blog (not verified here).
- Geng et al., "Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning" - https://arxiv.org/abs/2305.13971
- JSONSchemaBench, "Generating Structured Outputs from LMs: Benchmark and Studies" - https://arxiv.org/abs/2501.10868 (verified)
- Tam et al., "Let Me Speak Freely?" - https://arxiv.org/abs/2408.02442
- Constrained decoding in small LLMs: structural failures vanish, "scale-dependent semantic gap" remains - https://arxiv.org/abs/2609.23742 (verified, search hit)
- Instructor (Pydantic + retries) - https://github.com/567-labs/instructor
- DSPy (declarative signatures, prompt/weight optimization) - https://arxiv.org/abs/2310.03714 ; https://github.com/stanfordnlp/dspy
- Vendor docs: OpenAI Structured Outputs, Anthropic structured outputs / tool use, Gemini responseSchema (consult current docs).
- Speculative / parallel-aware constrained decoding for diffusion LMs is emerging; see non-autoregressive-and-diffusion.md.

## How they differ from Jev
| Axis | Constrained AR LLM | Jev (as described) |
|---|---|---|
| Decoding | Sequential tokens, grammar mask | Parallel sampler, single pass, all questions at once |
| Latency | ~0.5-5 s, grows with output | 70-500 ms, flat |
| Type safety | Syntactic validity guaranteed | Output is a typed head by construction (no text to parse) |
| Probabilities | Token logprobs, uncalibrated, post-RLHF overconfident | Trained for calibration (RLCD) |
| Hallucination claim | Possible in free fields | Claimed impossible because output space is closed (a closed-set error is still an error) |
| Open/closed | Open tools | Hosted only, architecture undisclosed |

Note: with constrained decoding to a closed enum, the *semantic* failure mode is identical (wrong choice); "cannot hallucinate" means "cannot produce an out-of-schema answer", not "cannot be wrong".

## Relevance to Jev-style models
- The real baseline for "typed decisions" in production is: constrained-decoding enum output from a small LLM (XGrammar via vLLM) with logprobs on. Compare latency, accuracy, and calibration against it.
- Constrained decoding with `logprobs=true` over a single-token enum is effectively the letter-logprob method in llm-as-classifier-logits.md: the two literatures merge for Choice/Noul.
- A clone should avoid reimplementing grammar machinery; its output heads are fixed-arity softmaxes. Open-vocabulary extensions (>255 options, free-form fields) would need constrained decoding or retrieval over options.
- DSPy-style optimization is a relevant orthogonal tool for prompt design of the decoder-based clones.
