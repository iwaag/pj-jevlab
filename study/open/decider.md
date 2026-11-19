# Decider

- **Category**: open
- **Owner / org**: Mark Marosi (github.com/Mapika)
- **URLs**: repo https://github.com/Mapika/decider ; HF Mapika/decider-2b, -4b, -35b-a3b, -12b, -0.8b, -2b-vision, GGUFs, decider-chat-gemma4-31b, decider-chat-qwen3.6-27b ; pip `decider-ai` 1.8.1 ; docs/RL.md, RESULTS.md, HISTORY.md
- **License** (code / weights): Apache-2.0 / Apache-2.0
- **First release / last update**: repo created 2026-09-16, pushed 2026-09-30 (decider-ai 1.8.1)
- **Popularity signals**: GitHub 1,024 stars; HF downloads: decider-2b 265.7k (96 likes), decider-4b 22.3k (13), decider-35b-a3b 1.3k (9)

## Summary
A family of single-pass typed-decision models: full/partial fine-tunes of Qwen3.5 Base models (0.8B, 2B, 4B, 35B-A3B MoE), Gemma-4-12B with a state-tracking LoRA, plus two "decider-chat" entries that are stock instruct models read through the package's layout with fitted temperatures. It is the only open project here that describes an RL stage with a proper-scoring "belief" loss, though that stage's code is not released.

## Approach / architecture
- Prompt renders state plus one answer slot per question; hidden state at each slot is projected to one label token per option (A-J, then K-Z and two-letter tokens, up to 255 options); softmax over valid ones at a fitted temperature. Letters are never generated, so all slots come from one forward pass.
- Parallelism: two prompt layouts trained 50/50: state-first (default) and schema-first (question/option block as a state-independent prefix, cached per schema; costs accuracy but faster). Questions can also be scored in separate rows for exact isolation; Score levels judged alone.
- CUDA graphs, torch.compile, optional FP8, MPS, GGUF (llama.cpp) and vLLM server variants.
- Calibration: temperature per question type (e.g., decider-12b v2 Choice 1.5, Noul 0.05, Score 1.0); `temperature_by_options` T(n)=max(min, a+b ln n) for option-count dependence (decider-chat-gemma4-31b: 10.124 - 1.633 ln n). `calibrate.py` fits from labeled answers.

## Interface
`POST /v1/systemone` via `decider.serve` (continuous batching) and vLLM server; Python `Decider.system_one()` and simpler `decide()`. TypeSafe SDK shapes (Choice 2-255, Score 2-10, Noul). confidence follows TypeSafe's definition since 1.3.0.

## Training & data
- Supervised: one epoch over a mixture of 1.47M examples / 455M tokens (5.3 h on a GH200) built from about 95 public datasets plus data labelled by a local Qwen3.5-27B teacher (`teacher_data/`, `mixture.py`); input-shape augmentations. Cross-entropy fine-tune. Mixture v2 (decider-4b) adds 26 more public datasets and ten programmatic families with verifiable gold. 35B-A3B: frozen-expert Muon training with FP32 master weights (author flags this as possibly harmful and plans a retrain). `scripts/train.sh full` reproduces the public 60% of the 4B data; reproduction not byte-identical. Author states nothing was distilled from Jev.
- RL stage (v8 -> v10 on the 2B; docs/RL.md; code not released because it needs a separate research repo, live Chrome/MiniWoB++ and four GPUs): 384 optimizer steps at peak lr 1e-6 (576 scheduled), AdamW with FP32 master weights, 96 sampled transitions/iteration. Environments: 16 live MiniWoB++ click tasks, exact 4x4 minesweeper, 5x5 slippery grid, bag-draw games. Rewards from outcomes only (no gold labels). Loss terms: PPO actor (coef 0.1) with leave-one-replicate-out baseline; "belief" term (coef 0.2), a log score of the model's one-pass answer to "what happens next" against the exact known probability law (proper scoring rule, option orders averaged); rendering-consistency KL (coef 1.0) across four renderings; retention KL to v8 (coef 0.7) with a hard fallback (94 of 576 steps). Six gates for checkpoint eligibility. This is the closest open analogue to "RL for calibrated decisions", but it trains calibration on game/outcome laws, not on generic text decisions.

## Reported performance
Author-measured (v10 vs v8, 2B): live browser sampled play 83.0% -> 93.2%, belief excess over exact laws 0.473 -> 0.219 nats, click-outcome log score -0.349 -> -0.034; general accuracy -0.4 pts (within noise); OpenJev -0.8 pts. Held-out accuracy (regression set): 2B v11 0.752, 4B v2.1 0.784, 35B 0.810. Third-party leaderboards (author read them 2026-09-29, did not run): JevBench v1.5.2 decider-4b v2 #7 score 71.3 (intelligence 55.8, calibration 85.6) vs Jev 1.13.0 72.1; decider-2b #28 45.1; 35B-A3B #41 27.5 (cost-penalized). Decision Index v0.2.1: decider-chat-gemma4-31b 57.33 (#2, ECE 0.047) vs Jev 57.91; 35B NVFP4 47.11; 4B 40.70 (ECE 0.084); 2B 28.97. Author notes stock instruct models read with its readout outrank its trained 35B/4B/2B on the index (base model dominates), and that calibration on JevBench hard items is the weak axis (ECE 0.10-0.31). Latency: 2B GGUF Q4_K_M on 8 CPU threads 0.12-0.31 s per request; MPS M1 Pro 133 ms median.

## Self-hosting notes
2B ~4 GB, 4B 8.4 GB, 35B 65 GB bf16 or 19.6 GB NVFP4 in vLLM; GGUF on CPU/laptop; pip install and one-line loader. Windows ARM64 build notes provided.

## Assessment
Strongest breadth of model sizes and runtimes, extensive self-critical limits section (teacher bias, one-pass arithmetic ceiling, knowledge gap vs Jev). The honest finding that base model sets most of the score is useful. RL stage is the only partial analogue of RLCD (belief loss against exact laws + PPO + retention KL), but unreleased and narrow. Relevant as a recipe for combining supervised CE with proper-scoring objectives and for the T(n) option-count temperature trick.

## Sources
- https://github.com/Mapika/decider (README; docs/RL.md via gh api)
- https://huggingface.co/api/models/Mapika/decider-2b , -4b , -35b-a3b
