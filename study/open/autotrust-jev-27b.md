# autotrust/JEV-27B (and JEV-9B, JEV-27B-VL)

- **Category**: open (distilled from the closed hosted Jev)
- **Owner / org**: AutoTrust AI (HF autotrust; dataset by SargeDev)
- **URLs**: https://huggingface.co/autotrust/JEV-27B ; JEV-9B ; JEV-27B-VL ; corpus https://huggingface.co/datasets/SargeDev/jev-distill-corpus-v3 ; blog https://huggingface.co/blog/autotrust/autotrustjev-27b-fast-calibrated-decisions-and-ful
- **License** (code / weights): Apache-2.0 (weights, corpus); the corpus labels are outputs of TypeSafe's hosted Jev 1.13, so TypeSafe terms of service may apply (not examined)
- **First release / last update**: HF JEV-27B created 2026-09-25; card updated 2026-10-01
- **Popularity signals**: HF 785 downloads, 21 likes (JEV-27B); corpus 1,271 downloads, 17 likes

## Summary
The one open model here that is explicitly a distillation student of hosted Jev 1.13: a frozen Qwen3.8-27B with a rank-16 LoRA plus a 24-slot decision head (108.9M trainable parameters), trained on Jev's own published output distributions. The same weights also give an untouched System 2 chat path ("Blocks of Experts" recipe). Reports KL to Jev ~0.017 and parity with Jev on six public benchmarks.

## Approach / architecture
Backbone Qwen3.8-27B text tower (bf16) kept bit-identical; System 1 block = LoRA r=16 on decoder projections + fp32 decision head (hidden -> 24 slots: noul 0-1, score 2-7, choice 8-23; choice labels A-P), initialized from `lm_head` rows of verbalizer tokens so step-0 output equals zero-shot restricted next-token distribution (verified |dp| < 1e-5). vLLM serving via LoRA module `jev-decision` and an `lm_head`-expressed head; `/v1/decide` helper. Choice up to 256 options via the vLLM path (first 16 labelled A-P). Score on 0-5 scale. Prompts up to 256K tokens claimed.

## Interface
vLLM engine (System 1 and System 2 from one engine), `serve_decide.py` adds `POST /v1/decide`; a Jev-compatible endpoint is implied but not verified here.

## Training & data
- Distillation with KL to full teacher distributions plus an ordinal RPS term for score; cosine schedule 5,000 steps, ~640k rows (0.98 epoch), ~9.2 B200-hours; 30% option-permutation augmentation. Fitted temperatures 1.014/1.016/1.004, no post-hoc correction needed.
- Corpus `jev-distill-corpus-v3`: rows labelled with TypeSafe Jev 1.13 output distributions (25,376 of 29,955 test targets), Open-Jev programmatic ground-truth rows, plus placeholder rows. Teacher = hosted closed model, so this is distillation of a commercial API (README is upfront about it).
- Not RLCD; "calibration falls out of the objective" because the teacher distribution is already calibrated.

## Reported performance
Author-measured (AutoTrust ran both models; Jev via hosted API on 26-27 Sept): held-out test KL to Jev 0.0186 (Jev-labelled rows ~0.017), noul AUROC 0.996, choice top-1 agreement with Jev 90.3% (95.8% on decisive rows), score MAE 0.098, ECE 0.0009. Six public benchmarks (JevBench public family-macro, Kev, OpenJev text, Nimble, VitaminC, MASSIVE-en): mean 84.07 vs Jev 83.85; JevBench 88.70 vs 87.18; Kev 83.75 vs 85.52; baseline rows (NeoHorse-Jev-4B 77.70, Open-Jev-9B 75.67, Kev-4B 74.25) are copied from NeoHorse's report, not re-run. HumanEval 78.0% unchanged vs base. Latency B200: 137 ms single, 4.2 ms/decision batched of 128; hosted Jev measured 238-301 ms by third parties. Not submitted to Decision Index or JevBench leaderboards at card time.

## Self-hosting notes
27B bf16 (~54 GB) on one B200/H200-class GPU via vLLM with Qwen3.5 support and LoRA on lm_head; JEV-9B cheaper.

## Assessment
Shows the ceiling of distillation: near-zero KL to a black-box teacher with a tiny trainable footprint, which also makes the model a drop-in clone. Caveats: depends on Jev API outputs (legal and reproducibility concerns); fidelity includes the teacher's mistakes; self-run comparison. For a lab: the head-init-from-lm_head trick and RPS term for ordinal Score are the transferable parts.

## Sources
- https://huggingface.co/autotrust/JEV-27B (model card, raw README)
- https://huggingface.co/api/datasets/SargeDev/jev-distill-corpus-v3
