# Winnow-12B

- **Category**: open
- **Owner / org**: EldanRing (HF EldanRing; inference code github.com/EldanRing/winnow-inference)
- **URLs**: https://huggingface.co/EldanRing/Winnow-12B (GGUF only: BF16 23.8 GB, Q8_0 12.7 GB, mmproj 175 MB) ; https://github.com/EldanRing/winnow-inference
- **License** (code / weights): Apache-2.0 per HF metadata (base Gemma 4 12B IT has its own terms)
- **First release / last update**: HF created 2026-09-20
- **Popularity signals**: HF 21,482 downloads, 32 likes; the unrelated repo GhalebDweikat/winnow (100 stars) is a Claude Code context filter that uses a System One model

## Summary
Gemma 4 12B IT fine-tuned with LoRA (r32/alpha64, merged) for typed decisions, plus chat and vision from the same GGUF in a llama.cpp-based server. Winnow-12B Q8 ties Jev on the JevBench public subset in the author's runs, and JevBench lists a "Winnow-12B Q8" at #2 (score 73.2) per Decider's README.

## Approach / architecture
llama.cpp-based server exposing `/v1/systemone` and `/v1/chat/completions` from one loaded model: prefill state once, fork question branches, read answer-token logits (no answer text generated). No separate head; no adapter at load time.

## Interface
`/v1/systemone` (noul/choice/score), OpenAI chat; image input with mmproj; 64K context tested on a 16 GB RTX 5070 Ti with Q8 KV cache.

## Training & data
LoRA on all attention and MLP projections; training data private: synthetic scenarios, teacher-supervised examples, labeled semantic tasks (routing, policy/rule application, evidence selection, workflow decisions, ordinal judgments, entailment, paraphrase, answerability), with contrastive examples varying decision-changing facts (similar in spirit to Nimble). Initial decision fine-tune, then a 26,000-example refinement mixture with replay (19,200 presentations at the selected checkpoint), BF16, effective batch 8, 8,192-token cap. Objective: gold-label cross-entropy plus teacher-distribution cross-entropy only when the teacher agrees with gold. Teacher not named. No RLCD.

## Reported performance
Author-run, same frozen inputs, Jev via OpenRouter: JevBench public subset (231 items) Winnow BF16 85.28% / Q8 85.71% vs Jev 1.13 85.71%; Kev-v9 clean (1,046 items) 81.45% / 81.55% vs Jev 87.00%. Hardware: RTX PRO 5000 Blackwell for evals; Q8 on RTX 5070 Ti: 143 ms for a cached four-question request, 25 s cold at near-full 64K context. Third party (Decider README, not re-run): JevBench leaderboard #2, score 73.2, intelligence 74.4, calibration 84.1.

## Self-hosting notes
16 GB GPU for Q8; llama.cpp build; weights as GGUF only (no safetensors), so not directly fine-tunable from the release.

## Assessment
Strong open result at 12B with a small private LoRA corpus; dataset closed, which limits reproduction. Teacher-agreement-gated mixed loss is a useful recipe detail.

## Sources
- https://huggingface.co/EldanRing/Winnow-12B (raw README)
- https://github.com/Mapika/decider (leaderboard excerpt)
