# Cua-S1 (cua-s1-forms, nano, 4b-0.1, 4b-0.2)

- **Category**: open
- **Owner / org**: Cua (trycua; HF cua-ai)
- **URLs**: https://github.com/trycua/cua (`libs/cua-s1`, `libs/cua-bench-s1`, jev-use driver examples) ; HF cua-ai/cua-s1-forms, cua-s1-nano-0.1, cua-s1-4b-0.1, cua-s1-4b-0.2 ; HN thread https://news.ycombinator.com/item?id=49767564
- **License** (code / weights): MIT (code); forms MIT; nano and 4B LoRA adapters Apache-2.0 (adapter only; Qwen3.5-4B keeps its own license)
- **First release / last update**: cua-s1-forms HF created 2026-09-18, updated 2026-09-26; libs/cua-s1 last commit 2026-09-29
- **Popularity signals**: whole cua repo 27,651 stars (not representative of Cua-S1 itself); cua-s1-forms 114 likes, 0 downloads listed

## Summary
A set of small computer-use "System One" decision models: from-scratch tiny option-attention classifiers (cua-s1-forms 706k parameters, 2.8 MB; cua-s1-nano 855k parameters) and LoRA adapters on Qwen3.5-4B (4b-0.1 and 4b-0.2; the latter has text and multimodal adapters each with an SFT stage and an RL stage on live GUI environments). Built from ideas and code in jevlike. Authors say it is not a reproduction of Jev and not calibrated with TypeSafe's RLCD.

## Approach / architecture
- forms/nano: byte-level embedding + 2-layer transformer (width 128, 4 heads); each option is a query attending to context tokens (option-attention head); cross-entropy over the live option count; single parallel forward pass over all (element, action) options. nano has an optional frozen SmolVLM-256M or SigLIP backbone for screenshot crops.
- 4B: Qwen3.5-4B LoRA rank 16; one-letter-per-option readout (max 26 options), final-position logits softmaxed. Closed-option contract: cannot propose actions outside the caller's set.

## Interface
Python `cua_s1` package (inference only for 4B; the training/RL recipes are in the repo but the README says the training extras do not yet run on Qwen3.5 due to a Transformers 4 pin). Integrates as the "jev-use" closed-candidate chooser in cua-driver (`suggest_action`). Not a `/v1/systemone` server as far as I saw.

## Training & data
- forms: 10,000 synthetic episodes from `cua_s1/synth.py` (forms with 2-16 fields from a 55-concept catalog with synonyms; fictional personas, reserved phone numbers); trained in under 30 minutes. Cross-entropy.
- nano: from scratch on synthetic GUI task families plus AndroidControl, GUI-360 derived data; chess and ViZDoom control as OOD checks.
- 4b-0.2: supervised stage on held-out-by-dataset real GUI data, then RL "against live GUI environments" (cua-bench-basic, 13 usable single-widget environments, 6 excluded as not reliably rewardable). Reward details are in libs/cua-bench-s1 and were not read here. Not RLCD.

## Reported performance
Author claims (HN post, model card): forms 99.7% vs hosted Jev 83.6% on the same form task (Jev 96% on judgment-type steps, 74% on skip-filled-fields); local latency 7-9 ms vs 260-280 ms for hosted Jev. Synthetic form-disjoint test 99.95%; shuffled-context control 37%. 4b-0.2 text held-out cross-dataset 0.875 task accuracy, ECE 0.121; multimodal 0.929, ECE 0.069; live cua-bench-basic episode success 0.944 text / 0.722 multimodal. Model card is candid: chess and game_control task accuracy 0.0; pagination row is mislabeled mid-episode steps; toggle-switch 0/3. Author-run, not independently verified.

## Self-hosting notes
forms/nano run on CPU in milliseconds; 4B needs Qwen3.5-4B (9.3 GB) + 187 MB adapter.

## Assessment
Narrow-domain specialists show how far a sub-1M-parameter model can go when the data is synthetic and in-distribution (it will not generalize: authors note held-out accuracy collapses outside). The 4b-0.2 RL stage is another partial RLCD analogue (outcome reward on live GUIs) but with no published calibration objective. Useful to a lab for synthetic UI-decision data generation code and the option-attention design.

## Sources
- https://github.com/trycua/cua (libs/cua-s1/README.md, MODEL_CARD.md via gh api)
- https://huggingface.co/cua-ai/cua-s1-forms (fetched summary)
- https://news.ycombinator.com/item?id=49767564 (fetched summary)
