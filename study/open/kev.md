# Kev

- **Category**: open
- **Owner / org**: Jared Palmer (github.com/jaredpalmer)
- **URLs**: repo https://github.com/jaredpalmer/kev ; HF collection https://huggingface.co/collections/jaredpalmer/kev-6aad9d0ea49f2589665e07cd (kev-0.8b/4b/9b/27b, legacy kev-0.5b) ; demo HF Space jaredpalmer/kev ; frozen eval suites HF dataset jaredpalmer/kev-suites ; design reference: archerhume.com/posts/jevs-architecture-unmasked
- **License** (code / weights): Apache-2.0 / Apache-2.0 (HF cards)
- **First release / last update**: repo created 2026-09-17, pushed 2026-10-01; kev-0.5b HF created 2026-09-18, kev-4b 2026-09-19, kev-27b 2026-09-24
- **Popularity signals**: GitHub 8,146 stars; HF downloads: kev-4b 14.1k (94 likes), kev-0.5b 1.7k (62 likes), kev-27b 624 (17 likes)

## Summary
The most thoroughly documented open Jev re-creation: a family of LoRA (0.8B/4B/9B) and full-fine-tuned (27B) Qwen models with a small pointer head, serving a drop-in `/v1/systemone` endpoint. Training is plain cross-entropy plus a fitted temperature; no RL. Author states no Jev outputs were used for training. The repo ships frozen eval suites, a claims-verification CI, and a long PLAN.md lab notebook, which makes it the best source for what works and what does not.

## Approach / architecture
- Bases: Qwen3.5-0.8B/4B/9B-Base (rank-16 LoRA over attention, MLP and DeltaNet projections, frozen base) and Qwen3.8-27B post-trained (all weights trained, 51 GB bf16; final = 0.85/0.15 weight average with the earlier adapter-trained 27B). Legacy Kev-0.5B was on Qwen2.5-0.5B.
- Readout: a "pointer head" scores each option's `</opt>` hidden state against the question's `<decide>` hidden state; softmax over options. Prompt format: `<state> ... <q> instr <opt> o1 </opt> ... <decide>`.
- Parallelism: on attention-only bases (Qwen3) one sequence with a mask lets each question see the state and itself only, with position IDs reset after the state. On hybrid Qwen3.5/3.8 (Gated DeltaNet layers ignore masks) each question is its own row (state + question) sharing a cached state prefix. Isolation is therefore exact; not a single packed pass for current models.
- Calibration: per-checkpoint temperature fitted on held-out data (Kev-4B 2.41, 0.8B 2.35, 9B 2.19, 27B 1.32; later 1.38 noted in PLAN.md). Confidence formulas copied from TypeSafe's reference adapter.

## Interface
`POST /v1/systemone` compatible with the TypeSafe Python SDK (base_url override), plus `/v1/models`, `/v1/systemone/permute`, `/v1/systemone/separate`. Up to 255 options, states up to 65,536 tokens. Backends: PyTorch CUDA/ROCm, MLX on Apple Silicon. Modal deploy script, Next.js playground, `kev-finetune` agent skill.

## Training & data
- Base set `decision-v7`: 10,000 examples from ten public datasets, 896 generated policy examples, 1,680 examples from 60 generated rule structures. 2 epochs, LoRA r16, cross-entropy, lr 1e-4 (0.8B) / 5e-5 (4B, 9B); `--p_none_pair 0.25`. Short follow-up fine-tunes from checkpoints (`--init_from`) on day-count and "evidence removed" cases, real CFPB documents, generated skill data.
- Kev-27B: full FT, 1 epoch on 8x H200, lr 2e-6, 145,840-record corpus (public datasets, licensed task families, generated long-document / tool-routing / agent-log / guardrail records, states up to 32k).
- PLAN.md policy: labels from open-weight teachers only (GLM-5.3, DeepSeek-V4-Pro, Inkling, Qwen) or programmatic solvers; closed frontier model outputs not used; a "sft-v1" corpus keeps a synthetic record only if two blind labelers agree with the generator's intended answer. Contrastive-style "abstention twins" and "unknowable" records (deciding evidence removed) are part of the data.
- Losses: released models use plain cross-entropy; optional `--perm_kl` and `--ord_w` exist but are unused in releases. PLAN.md records soft targets only where open labelers genuinely disagree; label smoothing, focal and Brier terms did not improve ranking (smoothing hurt AURC).
- No RLCD. Data builders and training code are in the repo; the larger synthetic corpora are not fully bundled (evals are).

## Reported performance
Author-measured, with paired-bootstrap tooling (`kev.compare`); dev/test splits, test read once per release. New-source accuracy dev/test: 0.8B 0.648/0.697, 4B 0.817/0.838, 9B 0.820/0.852, 27B 0.851/0.889; Jev (dev only) 0.857. Brier new-source dev: 27B 0.225 vs Jev 0.211. ECE after temperature on 9B: 0.103 -> 0.041; wrong-with-p>=0.9 rate 2.4% vs Jev 3.7% (author-run Jev). At 5% error budget Kev 4B/9B/27B automate 0.52-0.69 vs Jev 0.70 (Jev ranks better). Latency: Kev-4B 18.1 ms model time for six questions on H100, 41.5 ms on L40S, ~101 req/s per H100 container. Weak on MMLU-Pro (27B 0.675 vs Jev 0.840) and date arithmetic. Third-party: Decision Index community (from Decider and AutoTrust READMEs, not re-verified): Kev-4B 74.25 six-group mean in a NeoHorse table. The author's README claims are CI-checked against committed reports but Jev numbers were gathered via Vercel AI Gateway.

## Self-hosting notes
Kev-4B runs on a 32 GB Mac or L40S/H100; 0.8B on a 4 GB GPU for training with batch 1; 27B needs 80 GB card. `uv sync --extra serve` then `python -m kev.serve --run jaredpalmer/kev-4b`. Fine-tune ~$1 on H100 for 4B.

## Assessment
Strengths: transparent lab notebook, honest negative results (e.g., fine-tune from base lost the general skills vs `--init_from`; breadth of data, not replay, was the bottleneck per PLAN.md, which is why AutoJev-style full-weight SFT on 73k broad examples did better at 27B). Weaknesses: calibration quality is temperature-only; no RL; per-question rows on hybrid bases means state is recomputed per question unless the server cache is used. Highly relevant as the reference baseline and eval-suite source for a lab (frozen suites, claims.json CI).

## Independent arXiv evidence (added 2026-10-08)
See [../recent_study/](../recent_study/README.md). No paper tests Kev-27B, the lab's K27; all results below are on Kev 0.8B, 4B or 9B.

**Prompt rendering**
- Kev renders each option as `"{name}: {description}"` (`kev/api.py:58` in the lab's checkout `952ce9d0`). This is the same pattern that makes Laya follow labels over definitions (2610.02586).
- Kev-9B nevertheless resists a yes/no swap against fixed definitions, so trained decoder heads are robust where encoders are not (2610.00346). Kev-9B and Nimble-9B reduce their backbones' swap flips by 34.0 and 30.2 per hundred.

**Second passes and menus**
- For Kev 0.8B/4B/9B (and six other families), the accuracy after a menu-only change is predicted within 4.2 points by renormalising the cached first pass (2610.07716). This is a parallel result to the lab's set5.
- A confidence cascade to a larger sibling beats re-asking at matched cost.

**Other results**
- **Ordinal scales:** Kev 0.8B/4B/9B and Jev use only part of ordinal scales; a BA-LoRA post-training raises utilisation from about 47% to 86% (2609.38827).
- **Coherence:** Kev-4B has the smallest Event-vs-Choice gap (0.063) but a large complement residual (0.51), and changes the act/defer action on 14.9% of cases (2609.37470).
- **SecJev** (2610.03073; abstract) builds 0.8B–9B security specialists on Kev's single-pass candidate scorer; the 0.8B beats general Kev-9B by 20.5 points.

## Sources
- https://github.com/jaredpalmer/kev (README, PLAN.md via gh api)
- https://huggingface.co/api/models/jaredpalmer/kev-4b , kev-27b , kev-0.5b
