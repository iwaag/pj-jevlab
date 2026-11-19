# Does a larger model help? Scale, training and readout for Jev-style decisions

Written 2026-10-02. The evidence files are in [evidence/](evidence/README.md) and the local failure classes in [local-failures.md](local-failures.md). Every number is a source claim with its grade, unless it is marked **local** or **inference**.

## Short answer
- **Worth testing, as a bounded controlled experiment, not as an expected fix.**
- **What the evidence supports:**
  - Moving from a ~0.5B zero-shot encoder to a 4B+ decoder decision model improves hard, abstain-type and injection-type decisions substantially.
  - Within one trained family, most of the gain comes from 0.8B → 4B; 4B → 9B adds little.
- **What it does not support:**
  - That size alone fixes "none of the above" behaviour.
  - That size alone fixes rejection of adjacent requests, or text that names a label.
  - Training for abstention, the readout, and the interface each matter about as much as size.
  - No source measures the three local failures (L2 greetings, L3 unavailable jobs, L4 key-naming overrides) as a function of size. That gap is the reason to run the test locally.

## 1. Within-family size comparisons (same recipe and readout)
| Family | Sizes | Metric(s) closest to local failures | Result | Confounders | Grade |
|---|---|---|---|---|---|
| **Kev** ([scale-kev-size-ladder](evidence/scale-kev-size-ladder.md)) | 0.8B / 4B / 9B (same recipe on Qwen3.5-Base); 27B different base and corpus | New-source acc. dev/test 0.65/0.70 → 0.82/0.84 → 0.82/0.85 → 0.85/0.89 (Jev 0.857 dev). Prompt-injection source 0.55 → 0.75 (0.8B→4B; Jev 0.89). When2Call incl. decline 0.17 → 0.66. Unanswerable answered at p ≥ 0.9: 0.00 at all sizes (Jev 0.09) | Author-run; abstention twins in training (partly in-distribution); 27B confounded | B |
| **Kev** in the cwhy injection bench ([eco-injection-bench-cwhy](evidence/eco-injection-bench-cwhy.md)) | 0.8B / 4B / 9B | Targeted flips under appended instructions; effect of a defensive policy line | Baseline robustness **not monotonic** (4B ≈ 9B). The defence improves 9B slightly, leaves 4B unchanged, and makes **0.8B 43% worse** | Independent; binary task | A |
| **Decider** ([scale-decider-…](evidence/scale-decider-size-ladder-and-stock-readout.md)) | 2B / 4B / 35B-A3B | JevBench public hard tier | 0.577 / 0.649 / 0.676; stock Gemma-4-12B-it with the same readout 0.730 (= Jev) | Different bases and stages per size; MoE training flagged | B |
| **Malkuth** (Kev-derived) ([scale-jevbench-…](evidence/scale-jevbench-cross-model-and-jeff-hard-tier.md)) | 2B / 4B | JevBench ambiguous (abstain) items | 4/14 → 8/14 | n = 14 | B |
| **SemIf reader ladder** ([scale-semif-…](evidence/scale-semif-minijev-jevmlx-llm-readers.md)) | Qwen3-0.6B / MiniCPM5-2B / Qwen3.5-4B / 27B | Authored balanced accuracy | 0.44 / 0.69 / 0.81 / 0.96 | Different families and quantization; authored fixtures | C |
| **AnyJev** ([scale-anyjev-…](evidence/scale-anyjev-qwen3-label-heads.md)) | Qwen3 1.7B → 32B | Zero-label typed decisions | 0.49 → 0.70; a fitted label head gives 0.73–0.80 at small sizes | Teacher-LLM gold labels | C |
| **GLiFormer** ([scale-gliformer-…](evidence/scale-gliformer-base-vs-large.md)) | base 264M / large 576M only | Generic macro-F1 | 72.4 → 75.0; base cannot answer noul questions (jeff probe) | No rejection data; **no larger GLiFormer exists** | B |
| **GLiNER2.5-Decide** ([scale-trained-encoders-…](evidence/scale-trained-encoders-zero-shot-gap.md)) | 340M (card) / 1B | Vendor fast-decisions | 60.2% vs 59.6%: the larger model is not better | Vendor benchmark | C |
| **LLM selection bias** ([lit-selection-bias-zheng](evidence/lit-selection-bias-zheng.md)) | Llama-2 7/13/70B; Vicuna 7/13/33B | Option-position bias (RStd) | Llama-2 23.0 → 7.5 → 4.1; Vicuna 5.3 → 10.5 → 8.2 (non-monotonic) | MMLU, not decisions | A |

## 2. Cross-model comparisons (different families; system comparisons)
- **JevBench hard tier (B):**
  - Zero-shot and trained ~150–575M encoders cluster at 35–39%: jeff 38.7, Laya 35.1, open-jev-deberta 37.8.
  - A frozen Qwen3.5-4B reader (SemIf) scores 61.3, and Jev 73.0.
  - On abstain items jeff scores 0/7 and stock Gemma-4-12B 13/14.
  - clm-8b reaches only 4/12 on adversarial items: **size does not guarantee success.**
- **Injection (A):** Jev 0.09% < Winnow-12B 3.0% < SemIf-4B 27.4% < Laya 49–63%. Size and training are confounded, and Jev's size is undisclosed.
- **"None of the above" (A):** 28 LLMs from 1.5B to 671B drop 30–50% when NOTA is the correct answer, "regardless of scale". SFT/DPO helps but does not close the gap.
- **Instruction-like noise (B, preprint):** DistractionIF reports inverse scaling. The Qwen3 pass rate falls from 66% at 0.6B to 37.6% at 235B, because larger models follow embedded instructions more.
- **Judge injection (B):** small open judges are more injectable (Gemma-4B 66.7%) than GPT-4 (32.4%). The Gemma 4B → 27B gap is small for adaptive attacks.

## 3. Four approaches compared
| Approach | Example | Evidence for local failure types | Strength | Weakness |
|---|---|---|---|---|
| **(a) Zero-shot encoder wrapper** (current) | jeff + GLiFormer-large 576M | Local: L2–L8 as measured. Hard-tier 38.7%, abstain 0/7 | Fast (p95 ≤ 94 ms local), already integrated | No larger checkpoint; no abstention training; order- and key-sensitive |
| **(b) Trained decision model** | Kev 0.8–27B, Decider, Laya, Von | Trained abstention lowers confident wrong answers (Kev 0.00 at p ≥ 0.9). Trained encoders (Laya/Von) still show L2/L3 errors and injection flips | Same API, calibrated temperature, abstention episodes in training; Kev has `/permute` and `/separate` endpoints | Encoder-class training did not fix L2/L3; small LLM sizes (0.8B) unreliable |
| **(c) Training-free LLM option-logit reader** | SemIf, Simple Jev, stock Gemma via Decider readout | Stock 12B ≈ Jev on hard tier; SemIf-4B 27.4% injection flips | No training; any base | Letter vs name readout swings 10–50 points; order bias; quantization flips near-ties |
| **(d) General LLM with validated structured output** | Qwen3.5/3.8 via Ollama JSON schema | Frontier LLMs resist injection better than small ones; NOTA weakness persists | Can be instructed, and can be asked for a separate "not an order" field | Latency (seconds on large models); generation is a system difference, not a pure scale change; DistractionIF inverse scaling |

## 4. Confounders a local test must control
1. **Base vs training:** Decider's stock-instruct readouts beat its trained models, so training and scale must be varied separately. Kev 4B vs stock Qwen3.5-4B with an option reader isolates training at a fixed base.
2. **Readout:** letter vs option-name readout (mini-jev vs jevmlx disagree). Key text inside label text (local L4). Temperature (does not change argmax, but changes the margin gate).
3. **Option order:** fix and also permute (Kev `/v1/systemone/permute` exists).
4. **Precision/backend:** bf16 vs fp32 flips ~1/300 Kev answers; MLX vs CUDA differ by ≤ 0.05 probability per the Kev README.
5. **Prompt/wording:** each approach gets the same bounded dev-only adaptation budget.
6. **Question isolation:** one question per request, or explicit separation (`JEFF_ISOLATE=all`, Kev `/separate`).

## 5. Inference: what to expect
- **L4 (key-naming overrides):** expected to improve with Kev-4B+ or large LLMs (injection evidence), but the cheapest test is interface-side (opaque keys). Test both, so that scale is not credited with an interface fix.
- **L3 (unavailable job):** the most likely to benefit from a model *trained* with removed-gold episodes (Kev trains "deciding evidence removed"; laya-intent-router 0.68 → 0.99). It is least likely to be fixed by size alone (NOTA evidence).
- **L2 (greetings):** likely improves with trained abstention and with LLM readers. Small menus (2 options at S0) remain a stated risk even for trained routers.
- **L1 (missed paraphrases):** may improve with capacity, but is already cost-free.
- **Latency:** Kev-4B is measured at 721 ms per 5 questions on an M5 (author). M3 Ultra latency for one question is unknown. A ≤ 1 s budget is plausible for 4B and must be measured for 9B/27B.
- **Counter-risk:** larger instruction-tuned models may *follow* override text more (DistractionIF). The fresh set must include overrides.
