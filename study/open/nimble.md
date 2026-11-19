# Nimble (Bespoke-Nimble-9B)

- **Category**: open
- **Owner / org**: Bespoke Labs (Maheswaran Sathiamoorthy)
- **URLs**: repo https://github.com/bespokelabsai/nimble ; model https://huggingface.co/bespokelabs/Bespoke-Nimble-9B (also -v2)
- **License** (code / weights): repo has no license file detected by GitHub API (null); HF weights Apache-2.0
- **First release / last update**: repo created 2026-09-18; pushed 2026-09-24 (README update: latest checkpoint, 8,192-token context, up to 255 choices)
- **Popularity signals**: GitHub 2,013 stars; HF 4,028 downloads, 221 likes

## Summary
Open "data, model, recipe" release: Qwen3.5-9B LoRA-fine-tuned on 2,676 synthetic contrastive examples to answer typed questions by reading one answer-token logit per candidate. The notable contribution is "contrastive data curation": near-identical example pairs that differ in one fact so the label flips. Built "in one day" per the authors; no RL, no Jev distillation.

## Approach / architecture
- Base Qwen3.5-9B, LoRA rank 16, CE over the allowed candidate logits only (one-token candidate codes), hard labels. Serving: prefill context+schema once, read logits of candidate code tokens, softmax; no generated JSON.
- Parallelism: MLX `ParallelScorer` processes the shared context once and scores all fields in parallel; the CUDA scorer scores each field with the full prompt (context re-processed per field). Fields cannot see each other. Flat schemas only (enum 1-255 choices, boolean). Rating scale is expressed as an ordered enum; expectation computed by caller. Text only.
- Calibration: single temperature. For original release revision 93ec5d6, T=2.179 fitted on 300 examples, checked on a second 300 (different sources); ECE 0.128->0.066, log loss 0.692->0.555 on that second set. Latest checkpoint ships with T=1.0, no separate fit. Fit was on unmerged adapter; not rechecked on merged weights. On 64 held-out rating questions ECE got worse (0.105->0.177).

## Interface
Python library with `schema` dicts (enum/boolean), MLX and PyTorch CUDA scorers; hosted SGLang deployment guide on Modal; comparison app. Not a drop-in `/v1/systemone` server in the README (Score modelled as ordered enum); a public API was mentioned (docs/TRY_NIMBLE.md).

## Training & data
- 2,676 train + 324 held-out examples (10 subject categories; held-out covers 6). Choice 856 / Noul 888 / Score 932 train. Published later (Sept 20) after being omitted initially.
- Contrastive curation: write schema+policy, derive base facts, build a pair of two evidence sentences (both needed), edit at most eight words in one sentence to flip the focus fact, verify with separate LLM calls (also ablate each sentence: focus fact must become unknown), then labels assigned by code applying the checked rules to checked facts. All LLM requests/responses logged for replay. Labels are fully synthetic and model-checked, no human review. Teacher models not named in the README excerpt reviewed.
- Recipe: LoRA r16, lr 5e-5, effective batch 8, seed 17, 1 epoch (of a 3-epoch schedule), bf16, 2,048-token prompt cap; tuning on L40S, final on H100. Hard labels only; Jev probabilities stored for possible future soft-target distillation but not used.

## Reported performance
Author-measured on 324 held-out contrastive examples (162 pairs, six source families, so narrow): reference-label agreement Nimble-9B 90.12% vs Jev 1.13.0 93.21%, Qwen3.8-27B 84.88%, Qwen3.5-9B 66.36%, 4B 61.42%. Latency (H100): 106 ms median per example (120 examples); M5 Pro 64GB: 444 ms; Jev API 246.7 ms median. Third parties: OpenThai's README claims a 13-subset public bench score of 74.8 for Nimble-9B (vs its own 74.3), per Edgar Dyck's suite (PR #2); AutoTrust's card lists Nimble as a benchmark subset, with Kev-4B at 73.40 on it. Not independently re-run by us.

## Self-hosting notes
Needs ~18 GB for bf16 9B weights; merge step needs extra CPU RAM; Mac Apple Silicon (MLX) or NVIDIA BF16 GPU. Setup is multi-step (merge adapter, write config JSON). Use Python 3.12.

## Assessment
Strengths: clean, reproducible data-curation idea that directly targets sensitivity to evidence; open dataset; honest caveats (narrow test, synthetic labels). Weaknesses: tiny train set; no RL; calibration is T only and the latest checkpoint is uncalibrated (T=1); CUDA path re-encodes context per field. Useful to a lab as a template for contrastive synthetic data, less as a finished model.

## Sources
- https://github.com/bespokelabsai/nimble (README via gh api)
- https://huggingface.co/api/models/bespokelabs/Bespoke-Nimble-9B
