# kotoba-lang/typed-decisions (encoders vs. LLaDA-MoE diffusion LM)

- **Category**: open (research repo; weights not committed)
- **Owner / org**: kotoba-lang
- **URLs**: https://github.com/kotoba-lang/typed-decisions
- **License** (code / weights): GitHub reports NOASSERTION / none released (corpus rebuilt from public datasets by `data.py`)
- **First release / last update**: created 2026-09-18, pushed 2026-09-29
- **Popularity signals**: GitHub 8 stars

## Summary
A controlled head-to-head of the Jev shape (state + several Choice/Score/Noul questions, one pass, calibrated distributions) across backbones: encoders (ModernBERT-base/large, DeBERTa-v3-base/large, RoBERTa-large) fully fine-tuned and a diffusion LM (inclusionAI LLaDA-MoE-7B-A1B-Instruct, 7.4B total / ~1B active) with LoRA r16. The only open diffusion-LM trained (not just prompted) Jev-shaped model I found, and it is a measurement study with a Japanese-language summary and an ADR-style log.

## Approach / architecture
- dLLM: `<state>..</state>` plus per-question text with options labelled A), B) ... and an `Ai: [MASK]` slot per question; logits at the [MASK] slots restricted to option-label tokens, softmax; steps=1 (single denoise pass). Steps>1 (LLaDA low-confidence remasking) were measured: steps=2 gave +0.3 points for 2x latency, so one pass is the operating point.
- Encoders: matching head over mean of each option's text tokens vs the question's; the initially designed head on a new `[OPT]` marker token failed to learn at any hyperparameter, while mean-of-option-text pooling worked.
- Calibration: post-hoc temperature on validation, reported as separate "Tfit" row.

## Interface
Research code; wire format helper `wire.py` produces proposal records (memo-key hashed) with admit/escalate thresholds. Not a `/v1/systemone` server.

## Training & data
Public gold labels only (no synthetic data, no teacher for the main runs): banking77 (intent 77-way, product area, card noul), SST-5 (level score, polarity, positive noul), BoolQ; 18,000 train states / 42,000 questions. Loss: CE + Brier for all models. LLaDA: LoRA r16 on q/k/v/o/gate/up/down, 6k states, 1 epoch, $2.29 on H100. Later iterations: augmentation (option shuffle, paraphrase, negation with label flip, distractor dropping) improved OOD-question accuracy 0.622 -> 0.648 and negated-noul by +16 points; a symmetric-KL consistency loss added cost without gains; a Qwen-based teacher was measured on OOD (0.696 vs 0.648 student) but not used for distillation in the shown results. No RLCD.

## Reported performance
Author H100 numbers (test 1,500 states / 3,508 questions): DeBERTa-v3-large 435M 1 epoch acc 0.855, Brier 0.204, ECE 0.014 (T fit), e2e 42 ms for 10 questions, $0.26; LLaDA-MoE LoRA 0.835, Brier 0.231, ECE 0.028, 676 ms, $2.29; ModernBERT-base 0.717, 68 ms, $0.16. Untrained LLaDA zero-shot 0.645. Equal-data control (6k states): LLaDA 0.835 vs DeBERTa-large 0.819 vs ModernBERT-base 0.577. Single seed, no frontier-teacher distillation, in-domain question types; accuracy not comparable to Jev's 67.8% workflow number. OOD questions drop accuracy sharply for all students.

## Self-hosting notes
Modal H100 scripts; LLaDA-MoE needs ~53 GiB peak training memory.

## Assessment
Best controlled evidence that a 7B diffusion LM is competitive in accuracy but 16x slower and 14x more expensive to train than a good encoder on this task shape. Caveat: only three public datasets and mostly short text. Useful as a design-ablation reference (marker-token head failure, OOD-question test, augmentation).

## Sources
- https://github.com/kotoba-lang/typed-decisions (README via gh api)
