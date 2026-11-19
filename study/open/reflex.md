# Reflex

- **Category**: open
- **Owner / org**: kshetrajna12
- **URLs**: repo https://github.com/kshetrajna12/reflex ; browser demo https://kshetrajna12.github.io/reflex/ ; docs/results/ index of experiments
- **License** (code / weights): MIT / no weights released (uses stock Qwen3.5 / Qwen3 / Qwen3.8 weights)
- **First release / last update**: created 2026-09-17, pushed 2026-09-27
- **Popularity signals**: GitHub 160 stars

## Summary
A Jev re-creation whose recommended ("stable") configuration is a FROZEN Qwen3.5-4B read through a lettered-label logit readout with two option orders averaged. The author trained several LoRA adapters and a distillation from a 27B teacher and rejected all of them; the interesting content is this negative result. Included here because the repo contains a full LoRA/Brier training path and a distillation tool, but nothing trained is shipped.

## Approach / architecture
State prefilled once, cached; each question as a branch seeing the state but not other questions; read next-token logits over label letters (A, B, C, and a lettered pair for yes/no), softmax. Each question asked in two option orders inside the same pass and averaged (cheapest accuracy and calibration gain per author). Optional temperature file fitted on user data (`reflex-eval-mmlu --fit-temperature`). Supports Qwen3.5 (with images), Qwen3, Qwen3-VL; PyTorch CUDA, MPS, or SGLang backend; WebGPU demo with a 0.8B model.

## Interface
`POST /v1/systemone` with TypeSafe request/response shapes; choice up to 26 options, score 2-10 levels. `reflex-serve --stable`.

## Training & data
Optional tooling: `reflex-calibrate train` (LoRA, proper scoring rule: log loss or Brier; soft labels supported, e.g. `{"billing":0.7,"sales":0.3}`), `reflex-data mix` from eight public datasets (intents, exam questions, toxicity with soft labels, hallucination checks, passage relevance, helpfulness, code review), `reflex-distill` (stronger model, optionally reasoning, labels the author's own states; student never reasons). README describes this as "the supervised form of the RLCD training Jev uses", which is the author's interpretation, not a verified fact. Trained adapters: one epoch of the mix on Qwen3.5-4B took held-out accuracy 62.7% -> 76.8% and ECE 0.120 -> 0.051 (0.024 with temperature) but lost general judgment on long ambiguous inputs, so were not shipped. GEPA prompt optimization failed similarly.

## Reported performance
Author runs on JevBench public items: frozen 4B two orders easy/standard/hard 1.000/0.917/0.685, hard ECE 0.081, ~200 ms; frozen Qwen3.8-27B 1.000/0.958/0.766, ECE 0.061, ~1 s; Jev 1.13.0 1.000/0.986/0.730, ECE 0.031. The author notes public items were consulted during development. Reported independent: official JevBench v1.2 run by the benchmark's author placed an earlier LoRA 4B configuration #5 of 36 (score 71.7) and reflex-27b #22 with highest Intelligence 90.5 and Calibration 86.2 and hard-tier 75.9% vs Jev 74.1% (details in docs/results/jevbench-official.md, which I did not fetch). Calibration of Qwen3.5-4B on 1,200 MMLU questions: ECE 0.090 -> 0.039 with fitted temperature.

## Self-hosting notes
16 GB CUDA GPU for 4B (8 GB enough for default per README), 60 GB for 27B; `git checkout stable && uv run reflex-serve --stable`.

## Assessment
Key lesson for a lab: prompt/readout design plus order averaging gave gains where fine-tuning on public data did not generalize. Not a trained model; weights are stock Qwen. Good controlled-experiment log (docs/results/). Weakness: development suite overlap with the public benchmark it reports on.

## Sources
- https://github.com/kshetrajna12/reflex (README via gh api)
