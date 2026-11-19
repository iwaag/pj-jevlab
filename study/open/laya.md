# Laya (ConvAI Innovations)

- **Category**: open
- **Owner / org**: NandhaKishorM / ConvAI Innovations (convaiinnovations on HF)
- **URLs**: repo https://github.com/NandhaKishorM/laya ; HF https://huggingface.co/convaiinnovations/laya (hub for 3 checkpoints), https://huggingface.co/convaiinnovations/laya-multilingual ; docs https://nandhakishorm.github.io/laya/ ; PyPI `laya`; npm `laya-ts`
- **License** (code / weights): Apache-2.0 / Apache-2.0 (HF card metadata)
- **First release / last update**: repo created 2026-09-18, last push 2026-09-29 (HF created 2026-09-18, modified 2026-09-24). Runtime v0.3.20 at time of reading.
- **Popularity signals**: GitHub 29,614 stars (as of 2026-10-01; unusually high for a 2-week-old repo, not independently explained in sources); HF laya 4,750 likes, laya-multilingual 348 likes; HF API download counts show 0 for these repos (unreliable/hub-style repo). 

## Summary
The most prominent open "Jev-like" project: a non-autoregressive "System 1" decision engine (Choice / Score / Noul) built on ModernBERT-large (English) and mmBERT-base (multilingual), with a Router that picks the checkpoint per request by script/language. Ships a Jev-compatible `/v1/systemone` server (`laya-serve`), MCP server, LangChain/LlamaIndex/CrewAI adapters, ONNX and TypeScript runtimes. The authors are unusually candid in the README that the base checkpoints are near chance zero-shot on the typed-decisions benchmark and that the headline accuracy requires fine-tuning.

## Approach / architecture
- Backbone: ModernBERT-large (395M, fully fine-tuned) + decision head trained from scratch (2 transformer layers, option-marker scorer, act/escalate head) = 421M total. Multilingual: mmBERT-base (22 layers, 256k vocab), 322M total. Third checkpoint `laya-typed-decisions` (ModernBERT-large, 421M, 1024 ctx), fine-tuned on the typed-decisions benchmark's training split.
- Each option is scored at its own `[MASK]` marker, softmax over that question's options; schema is defined at request time (no retraining for new option sets). All questions in a call answered in one forward pass.
- Context: 512 tokens (English, head_max_len 192), 1024 (multilingual, head_max_len 256; up to 8192 via `max_len=8192`, accuracy on long docs variable beyond ~4k tokens per author's test).
- Training: "RLCD" (Reinforcement Learning for Calibrated Decisions): REINFORCE with group-mean baseline (GRPO-style), Gaussian noise on logits for exploration, strictly proper scoring rule reward (log + spherical, RPS for ordinal). Calibration by fitted temperature per (question type, option count); temperatures are fitted post-hoc and the shipped model is over-confident without refit (author: mean ECE 0.466 -> 0.081 after refit for `laya`; 0.314 -> 0.106 multilingual).

## Interface
- Python `Router().predict(state, questions)`; CLI `laya`; `laya-serve` exposes `POST /v1/systemone` with the same request/response shape as TypeSafe Jev (accepts `criteria` as list; optional bearer auth via `LAYA_API_KEY`, binds 0.0.0.0 with no auth by default).
- Extras: `laya[mcp]`, `laya[langchain]`, `laya[llamaindex]`, `laya[crewai]`, `laya[onnx]`, `laya[fast]` (TileLang GPU path), Docker, fine-tuning notebook (Kaggle 2xT4), `laya.evals` gating.
- Ecosystem noted in README: omp-laya-judge (oh-my-pi MCP plugin), laya-apple (MLX + ANE runtime, tc3oliver, 16 stars).

## Training & data
Author states typed-decisions fine-tune is distilled against a "teacher" (teacher self-agreement ceiling 0.735). Full pretraining data for the base checkpoints is not described in the HF card text I read (not verified in the README sections consulted). Training code and fine-tuning notebook released; synthetic multilingual tickets used for some benchmarks.

## Reported performance
All Laya numbers below are author-measured (T4 GPU); Jev numbers are third-party published (AbdelStark/jev-benchmarks, nibzard/decision-model-benchmark), "never measured here" per the README (no TypeSafe API access).
- Latency (T4): 1 question 39.5 ms (EN) / 32.8 ms (multilingual); 10 questions 158.6 / 72.3 ms; 103-332 q/s batched. Author claims 6-8x faster than Jev (236-276 ms p50, third-party).
- typed-decisions (2,000 decisions, 4 workflows): `laya-typed-decisions` 0.766 acc vs Jev 0.727 (published) and teacher ceiling 0.735; ECE 0.213 raw vs Jev 0.144; Brier 0.062 vs 0.148; soft acc 0.471 vs Jev 0.580. Base `laya` 0.362, `laya-multilingual` 0.342 on the same set (below majority-class 0.461).
- Public sets: AG News 0.950 vs 0.910; DAIR Emotion 0.595 vs 0.480; Banking77 0.425 (77 labels) vs Jev 0.870 (72 labels) - Jev leads at >20 options; ECE 0.081 (post-temperature) vs 0.246.
- Multilingual: 45/51 languages usable (>3x random); English checkpoint collapses on non-Latin scripts (Khmer 0.000 acc at 0.952 confidence).
- Known issues (author-listed): `noul` can follow option labels over state ([#156]), `action.act_probability` carries no usable signal (AUROC 0.30; [#185]), score is the weakest primitive (SST-5 0.372).
- Independent measurements: JevBench v1.4 table (cited in the Von model card) lists Laya (421M) Intelligence 36.1, composite 30.3, sealed 0.308, sealed ECE 0.172. jeff's README places Laya #5 of 18 on JevBench v1.2.2 (Intelligence 63.2). poorjev's crossbench (see poorjev.md) measured Laya Banking77 acc 0.519 / ECE 0.388 and multi-primitive set acc 0.775 / ECE 0.215. fastino's GLiNER2.5-Decide card lists "Laya Router" at 46.6% on fast-decisions (vs 60.2% for GLiNER2.5-Decide). Foq's README (competitor) claims Laya fails on critical triage and negation; unverified.

## Self-hosting notes
`pip install laya`; checkpoints ~808 MB (EN) and ~647 MB (multilingual) on disk. GPU recommended for 30-40 ms; CPU works (slower). Preloading all three checkpoints needs roughly 8.6 GB (3.35 GB RAM + 5.31 GB VRAM per Foq's measurement, competitor claim). Python >=3.10.

## Assessment
Strengths: Apache-2.0, widest tooling and multilingual coverage, Jev-wire-compatible server, honest "limits" section, fine-tuning path, huge ecosystem of ports. Weaknesses: zero-shot base checkpoints weak (author admits); ships over-confident, requires per-domain temperature refit; weak on many-option choice due to shared head token budget; noul brittleness. Best treated as a base to fine-tune, not a drop-in Jev replacement. The star count (29.6k) should be treated as a popularity signal only; note it far exceeds all other projects and I did not verify its origin.

## Derivatives
- **laya-mlx** (https://github.com/mizorewww/laya-mlx; Apache-2.0; 6,675 stars; created 2026-09-19): native MLX runtime, no PyTorch. Author-measured on M3 Max FP16: 13.42 ms P50 (421M) / 7.39 ms (322M) for a short question; 146.8 / 395.0 q/s on 50-question batches; peak 944 / 688 MiB. Weights at HF `aac6fef/laya-mlx`. Includes Snake-game demo. Same author (mizorewww) also shipped laya-coreml.
- **laya-coreml** (https://github.com/mizorewww/laya-coreml; Apache-2.0; 1,531 stars): Core ML / Apple Neural Engine port; 4.98 ms P50 / 5.31 ms P95 on M3 Max for one short multilingual decision, 2.78x better whole-system energy per decision than compiled MLX FP16 (W8 variant 3.19x); author notes the requested 10x was not achieved. ANE bundle has a 96-token total limit. Conversion fidelity checked on fixtures (not general accuracy). Clamps fitted calibration temperatures to [0.5, 5.0] because a shipped bucket (choice:11+) had T=0.1006 (would sharpen logits ~10x). Weights `aac6fef/laya-multilingual-coreml-ane`.
- **oh-my-laya** (https://github.com/leo1394/oh-my-laya; MIT; 2 stars): installer that registers a `laya_tell_me` tool in Codex, Claude Code, DeepSeek Harness, pi-agent on top of laya-mlx; ~678 MB multilingual FP16 checkpoint.
- **laya-apple** (https://github.com/tc3oliver/laya-apple; Apache-2.0; 16 stars): MLX GPU + ANE concurrent serving, language routing, prebuilt ANE artifacts validated only for Apple M4 Max / macOS 26; first Core ML load compiles on-device (~4.5 min cold per README).
- **laya-bangla** (https://github.com/shamspias/laya-bangla; Apache-2.0; 40 stars): Bangla-focused adaptation; as of README, only local baseline tooling and a 36-message synthetic smoke set exist; fine-tuning and a released checkpoint are "planned". No model yet.
- **laya-windows** (https://github.com/Zuhair-01/laya-windows; Apache-2.0; 2 stars): ONNX Runtime + DirectML port with Arabic eval suite; per its status checklist the encoder runs on DirectML but the decision head is NOT yet ported to ONNX (runs on CPU from the transformers checkpoint). Other forks with the same name exist (astrodevit-creator, mateusgl8) with 0 stars.
- Other Laya-derived repos seen: laya-mlx-zh (ZLHAOOO, Chinese fine-tune, 5 stars), laya-as-judge (rbrus, 9), omp-laya-judge (F0Rextasy, 6), FluidInference/FluidUse (215 stars; uses laya + CUA-S1-FORMS on Core ML; claims 3.6 ms per laya question on ANE), zhengbangbo/structured-decision-bench (Jev vs Laya CoreML vs Qwen3 8B), sallout/laya-coreml-vs-jev-benchmark (Banking77/ArBanking77/CLINC150; contents not read).

## Independent arXiv evidence (added 2026-10-08)
See [../recent_study/](../recent_study/README.md).

**Calibration**
- A preregistered reproduction (2609.33843) found the shipped checkpoint uniformly *under*-confident: signed gap −0.214.
- One temperature T = 0.469 cuts held-out ECE from 0.204 to 0.037.
- The frozen confidence gate misses its 10% error target out of sample (0.140).
- No zero-shot out-of-distribution transfer (0.617).

**Option labels decide the answer**
- Deleting all definitions leaves accuracy unchanged (0.8559 vs 0.8487). A label that contradicts its definition drops accuracy to 0.1357 (2610.02586).
- The cause is the rendering `"{label}: {definition}"` in `laya/common.py`: removing the label makes Laya exactly invariant to label conflicts.
- A yes/no swap flips 91.3 answers per hundred (2610.00346) and 76.9% in 2609.26758.

**Order and changed questions**
- Reversing the option order changes 30.3% of answers, against 1.8% for hosted Jev (2610.02267).
- A fine-tuned Laya returned its training answer for 98.2–99.5% of changed questions while its calibrated gate kept acting (2609.33689).

**Coherence**
- Category-level total variation between direct and reconstructed probabilities is 0.42–0.69 (2609.33971).

**Extensions**
- LAVOIR adds missing-information slots with value-of-information targets (2609.30706).
- COGNIT-Guard uses Laya-322M as the escalation tier of a safety cascade (2609.33671; abstract).

## Sources
- https://github.com/NandhaKishorM/laya (README via gh api)
- https://huggingface.co/convaiinnovations/laya (card + HF API)
- https://huggingface.co/api/models/convaiinnovations/laya-multilingual
- https://github.com/mizorewww/laya-mlx ; https://github.com/mizorewww/laya-coreml ; https://github.com/leo1394/oh-my-laya ; https://github.com/tc3oliver/laya-apple ; https://github.com/shamspias/laya-bangla (+ docs/baseline-smoke-results.md) ; https://github.com/Zuhair-01/laya-windows
- https://huggingface.co/wfzyx/von ; https://github.com/logan-markewich/jeff (bench/RESULTS.md) ; https://github.com/rupeshpoojary9/poorjev ; https://huggingface.co/fastino/GLiNER2.5-Decide ; https://github.com/yohanargentina-oss/Foq (cross-references)
