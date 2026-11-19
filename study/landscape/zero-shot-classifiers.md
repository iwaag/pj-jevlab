# Zero-shot / encoder classifiers (prior art and clone bases)

Survey date: 2026-10-01. Items marked (verified) were fetched this session; others are from background knowledge (arXiv IDs should be spot-checked before citing).

## Overview
Before "System One" branding, the cheap way to get a typed label plus a probability from natural language input was an encoder (BERT-family) model, not a generative LLM. Three recipes dominate:
1. **NLI-as-classifier**: each candidate label becomes a hypothesis ("This text is about X"); entailment probability is the label score. One forward pass per (text, label) pair, so cost scales with option count (Jev's Choice allows up to 255 options, which would make this approach expensive).
2. **Joint label-text encoders** (GLiNER / GLiClass style): labels are concatenated into the input and scored in a single pass; cost is roughly flat in label count.
3. **Embedding + head** (SetFit, sentence-transformers): few-shot contrastive fine-tune, then a logistic head. Fast, calibrated-ish, but not zero-shot over arbitrary typed schemas.

Modern encoder backbones (ModernBERT, mmBERT) are the usual base for open Jev clones because they give ~10-50 ms latency, which matches or beats Jev's claimed 70-500 ms.

## Key works
- Yin et al. 2019, "Benchmarking Zero-shot Text Classification" - https://arxiv.org/abs/1909.00161 - formalizes NLI entailment as zero-shot classification.
- BART (Lewis et al.) - https://arxiv.org/abs/1910.13461; `facebook/bart-large-mnli` is the default HF `zero-shot-classification` pipeline model.
- DeBERTa / DeBERTaV3 - https://arxiv.org/abs/2006.03654, https://arxiv.org/abs/2111.09543 - strongest classic NLI backbone.
- MoritzLaurer zeroshot-classifier (deberta-v3 NLI + synthetic data) - https://github.com/MoritzLaurer/zeroshot-classifier ; Political DEBATE https://arxiv.org/abs/2409.02078 - shows synthetic-data-trained NLI classifiers rivaling LLMs.
- ModernBERT (Answer.AI/LightOn, 8k context, unpadding, FlashAttention) - https://arxiv.org/abs/2412.13663
- mmBERT (JHU, 1800+ languages, annealed language learning, ModernBERT-style) - https://arxiv.org/abs/2509.06888 ; https://github.com/JHU-CLSP/mmBERT (verified)
- GLiNER (bidirectional span/label encoder for open NER) - https://arxiv.org/abs/2311.08526 ; https://github.com/urchade/GLiNER
- GLiClass (Knowledgator; GLiNER-style sequence classification, labels in the prompt, single forward pass, ~10x faster than cross-encoders) - https://arxiv.org/abs/2508.07662 ; https://github.com/Knowledgator/GLiClass (verified)
- GLiNER Guard (unified encoder family for LLM safety and privacy) - https://arxiv.org/abs/2605.05277 (from search; not read in detail). A "GLiFormer" was not found in this survey; treat as non-existent unless a source appears.
- SetFit (few-shot sentence-transformer fine-tuning, no prompts) - https://arxiv.org/abs/2209.11055 ; https://github.com/huggingface/setfit
- Sentence-BERT / cross-encoders and rerankers (monoBERT, BGE-reranker, etc.) - https://arxiv.org/abs/1908.10084 ; cross-encoder = joint (query, doc) scoring, same shape as NLI scoring.
- BTZSC benchmark (zero-shot text classification across cross-encoders, embedders, rerankers, LLMs) - https://arxiv.org/abs/2603.11991 (from search) - useful eval harness.
- Jev vs GLiNER comparison page (span extraction vs typed decisions) - https://systemonemodels.org/compare/jev-vs-gliner/ (search hit, third-party).

## Which Jev clones use which base (from https://github.com/mturac/awesome-jev-alternatives, verified)
| Clone | Base |
|---|---|
| Laya (NandhaKishorM) | ModernBERT-large (421M, English), mmBERT-base (322M, multilingual); per-(type, option-count) temperature scaling |
| Verdict / OpenJev (Heman10x-NGU) | ModernBERT ~151M + GLiClass-style joint label encoding; CE + Brier loss ("RLCD"), L-BFGS temperature scaling, abstention class |
| open-jev-typed-decision-engine | 150M custom non-AR model |
| Ollaya | runtime that serves Laya, decider, Kev, Von, plain NLI and GLiClass checkpoints |
| decider, Kev, NanoJev, openjev (Gemma) | decoder LLM fine-tunes (Qwen3/3.5, Gemma 3 4B) reading option logits - see llm-as-classifier-logits.md |
| CLM, SemIf, jevlike | frozen encoder (Qwen3-8B or byte encoder) plus small heads |
| OpenJev (razorback16) | DiffusionGemma - see non-autoregressive-and-diffusion.md |

## Observed limits of the encoder route (from clone self-audits, verified)
- Laya README: both checkpoints "over-confident as shipped"; Score is weakest primitive (SST-5 acc 0.372); Noul can follow option labels instead of state; accuracy degrades above ~20 options because a shared token budget is split across labels.
- Verdict audit: 48.07% on TypeSafe's external 337-case eval versus 88.43% for a 26B DiffusionGemma; option reordering flips 4.5% of choices; abstention recall collapses under hard-negative siblings.

## Relevance to Jev-style models
- The encoder route reproduces Jev's *interface* (typed output, probabilities, parallel evaluation of many questions) cheaply, but the clones' accuracy ceiling on complex enterprise state is clearly lower. Jev's undisclosed architecture is likely a larger bidirectional or block-parallel transformer rather than a 150M encoder.
- GLiClass-style "labels in the prompt, one pass" is the closest public analogue to "evaluate every question against the state in parallel".
- Context length matters: ModernBERT (8k) and mmBERT are the practical bases; the 512-token cap used by Laya is a major gap versus long "state" inputs.
- NLI/cross-encoder baselines are the right *lower-bound baselines* for any lab benchmark (BTZSC protocol).
