# Surogate Rune 26B-A4B

- **Category**: open (some artifacts gated)
- **Owner / org**: Invergent (invergent-ai; engine "surogate"; HF surogate/, michaelfeil/rune-26b-a4b mirror)
- **URLs**: https://github.com/invergent-ai/surogate ; https://huggingface.co/michaelfeil/rune-26b-a4b ; https://huggingface.co/surogate/rune-26b-a4b-GGUF (restricted access, 2,780 downloads, 46 likes) ; blog https://invergent.ai/blog/rune/
- **License** (code / weights): Apache-2.0 (model card)
- **First release / last update**: model card dated about 2026-09-26 (v3)
- **Popularity signals**: GGUF repo 2,780 downloads / 46 likes; mirror 41 downloads in the last month

## Summary
Full fine-tune of Google's Gemma 4 26B-A4B (MoE, 26.5B total, 8 of 128 experts active) for text+image typed decisions. Listed #1 on Decision Index v0.2.1 with 57.44 (Jev 57.91 listed separately), per the model card and Decider's README. Information available to me is thin: training data and loss were not specified on the pages I could reach.

## Approach / architecture
Fine-tune of Gemma4ForConditionalGeneration; served by the surogate engine, whose decisions endpoint "implements the protocol Rune was trained with" (search-result summary). Probabilities are overconfident at T=1.

## Interface
Surogate server `--decision-temperature` flag; details of the API not verified.

## Training & data
Not disclosed on the card I fetched ("full fine-tune"). Blog may contain details; not read.

## Reported performance
Model card: Decision Index 0.2.1 (151,034 requests, 44 benchmarks) score 57.44, thinking-on est. 59.2; images 83.4% with 1,120 image tokens (1,196 items), 77.1% at 280 tokens. Calibration at default T=1: mean confidence 86.4% vs accuracy 73.9%, ECE 12.5%; at T=2 ECE 2.2% (Decision Index lists ECE 0.120 at default). Author-reported on a third-party index; I did not re-run.

## Self-hosting notes
Gated GGUF; Gemma 4 26B-A4B MoE; NVFP4 serving PR exists in the surogate repo (PR #245).

## Assessment
Probably the highest-scoring open model on the Decision Index, but under-documented; calibration needs a temperature of about 2. Worth reading the Invergent blog for the training protocol before using as a reference.

## Sources
- https://huggingface.co/michaelfeil/rune-26b-a4b (fetched summary)
- https://github.com/Mapika/decider (README leaderboard table)
- web search results (huggingface.co/surogate/rune-26b-a4b-GGUF, access gated)
