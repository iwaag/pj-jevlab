# rlcd-lite (and qwen-rlcd)

- **Category**: open (research reimplementation)
- **Owner / org**: arnabgho (rlcd-lite); shamazharikh (qwen-rlcd); also harshatheg/Qwen-2.5-1B-RLCD cited as an inference-only precursor (not fetched)
- **URLs**: https://github.com/arnabgho/rlcd-lite ; https://github.com/shamazharikh/qwen-rlcd
- **License** (code / weights): Apache-2.0 (rlcd-lite) / none declared (qwen-rlcd); no weights released
- **First release / last update**: rlcd-lite 2026-09-18 (single commit); qwen-rlcd 2026-09-16 to 2026-09-25
- **Popularity signals**: rlcd-lite 6 stars; qwen-rlcd 4 stars

## Summary
rlcd-lite is the only explicit attempt I found to reproduce "RL for Calibrated Decisions" with an actual RL algorithm (GRPO with a proper-scoring reward) on a tiny causal LM. Authors state it is a reconstruction, not TypeSafe's (undisclosed) algorithm, and unrelated to the 2023 "RLCD: RL from Contrastive Distillation". qwen-rlcd is an inference-only prototype on Qwen3.5-0.8B-Base with training on hold.

## Approach / architecture
rlcd-lite: parallel constrained decoding on a causal LM: one fused forward over prompt plus per-field suffixes with a block-diagonal attention mask (each field scored as an independent prompt+suffix), logits masked to verified single-token option labels, softmax; each field also has a "stated confidence" token over {1..5}. KV-cache path for new questions on the same context. Qwen2.5-0.5B-Instruct, LoRA r16.
qwen-rlcd: Qwen3.5-0.8B-Base (18 Gated DeltaNet + 6 attention layers); "prefix-fork" (prefill state once, copy cache across branch rows) because tree attention masks cannot isolate branches inside recurrent layers; fork vs sequential max abs diff 2.3e-5; 8-19x faster than one forward per branch on RTX 2080 Ti; scorers: letter-logit, likelihood, PMI, `<|read|>` head (untrained).

## Interface
CLI `rlcd-lite infer/train/eval/data`. No `/v1/systemone`.

## Training & data
rlcd-lite: GRPO (reduces to REINFORCE with group baseline since a decision is one step) with the reward `1[correct] - (conf - 1[correct])^2` (RLCR-style, Damani et al. 2025); ablations `brier` only, `binary` only, decoupled advantages. Data: synthetic 3-field ticket triage with a cross-field rule, banking77, clinc150, boolq, mmlu. 200 steps x 4 examples x G=8 on an M3 Pro, about 7 min per arm.
qwen-rlcd: no training.

## Reported performance
rlcd-lite, synthetic triage, 300 held-out tickets (author, one run): base acc 0.49; GRPO binary 0.76 (stated-confidence ECE 0.352); Brier alone collapsed to 0.21 accuracy (a degenerate "predictably wrong at low confidence" optimum); RLCR 0.78 with stated-conf ECE 0.084 and Brier 0.176; decoupled Brier 0.76 / ECE 0.105. Findings: stated-confidence calibration came without informativeness (resolution 0.000, AURC worse than temperature-scaled softmax); RL collapses raw softmax (mean confidence 0.99-1.00) so raw probabilities are worse calibrated than base unless a temperature is refit; cross-field consistency drifts after RL (violation 0.11-0.28 vs 0 for base).
qwen-rlcd: zero-shot Qwen3.5-0.8B-Base on 100 items: ARC-Challenge 0.60 (letter), BoolQ 0.77-0.79, SST-5 0.23-0.33.

## Self-hosting notes
Laptop-scale (0.5B/0.8B).

## Assessment
Useful cautionary evidence for RLCD-style training: a Brier reward on stated confidence alone is exploitable; correctness must be in the reward; RL sharpens the softmax so post-hoc temperature is still needed; and calibrated is not informative. Tiny scale and single run limit external validity.

## Sources
- https://github.com/arnabgho/rlcd-lite (README via gh api)
- https://github.com/shamazharikh/qwen-rlcd (README via gh api)
