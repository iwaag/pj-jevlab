# JevK5

- **Category**: open
- **Owner / org**: Alibi Serikbay (github.com/allebee, HF alibiserikbay)
- **URLs**: repo https://github.com/allebee/jevk5 ; HF alibiserikbay/JevK5 (4B), JevK5-9B, JevK5-2B, JevK5-GGUF, JevK5-Lite (DeBERTa-v3-large CPU model)
- **License** (code / weights): Apache-2.0 / Apache-2.0 (note: some teacher outputs "subject to OpenAI's terms")
- **First release / last update**: repo created 2026-09-22 (README mentions v0.1/v0.2 earlier on HF), pushed 2026-09-28 (v0.3.x)
- **Popularity signals**: GitHub 128 stars; HF JevK5 8,885 downloads, 17 likes

## Summary
Qwen3.5-4B (and 9B, 2B) with a merged rank-16 LoRA distilled from teacher-written hard decisions, read via the SemIf-style answer-letter logit readout with one temperature. Cleanest "teacher-distill + public replay + temperature" recipe in the set, with a pre-registered-style epoch sweep and frequent self-corrections (e.g., a test-set leak in v0.2 replay was disclosed and fixed in v0.3).

## Approach / architecture
Softmax over next-token logits of option letters (up to 16 options per pass; more via a knockout tournament: groups of 16, then a final of 16, ceil(n/16)+1 passes, with a second `knockout_temperature`). Each question evaluated separately; server serializes requests on one GPU. CUDA graphs per padded input length (13 ms vs ~70 ms eager on H100). Calibration: single global temperature fitted on held-out teacher questions from three domains unseen in training (4B 1.22, 9B v0.3 1.049, v0.3.3 1.316); per-question-type temperature and two-order averaging were measured and rejected.

## Interface
`POST /v1/systemone` (TypeSafe-style) via `jevk5-serve`; Python `JevK5.decide()`; GGUF via llama-server (`JevK5GGUF`); English only; 16,384-token input limit.

## Training & data
- Teacher data: Qwen3.6-27B (thinking) writes realistic documents with 3 hard typed questions each across 17 business domains and 11 decision families (policy exceptions, date/number traps, multi-step lookups, judging answers, ambiguity, misleading notes, injected instructions, rule precedence, routing, extraction, rubrics); answers each question twice independently, keeps only if both match the intended answer. v0.3 adds 14,138 questions from "GPT-6 Luna" via the OpenAI API (total 17,408 teacher questions).
- Replay: 30,052 human-labelled items from train splits of 26 public datasets; every row decontaminated against Decision Index test/validation text and JevBench public items (exact or 8-word overlap).
- LoRA rank 16 on attention projections, cross-entropy on option-letter logits, lr 3e-5, 1 epoch over 47,460 rows (v0.2: 2 epochs over 6,544; 9B v0.3.3 1.5 epochs). Items carrying an exact distribution train against that distribution. No Jev outputs, no RLCD.

## Reported performance
Author-run JevBench public items (231), 4B: v0.3 easy 1.000 / standard 0.944 / hard 0.784, hard ECE 0.054 (v0.2 0.739 / 0.066; untrained Qwen3.5-4B 0.613 / 0.117). 9B v0.3 hard 0.730, ECE 0.126 (worse than the 4B); v0.3.3 9B hard 0.775, ECE 0.071. Independent: JevBench v1.4 ranked JevK5 v0.2 second of 76 (62.04 vs Jev 63.29); on 308 fresh sealed decisions 33.1% vs Jev 36.7% (evaluator calls this set unusually difficult). Decision Index: v0.2.2 36.31, 15th of 49, 4th-best calibration (v0.3 not yet run). Latency H100 p50 13.2 ms (4B, short), 32 ms (9B). Many-option (BANKING77 77 options) accuracy 0.65-0.69, ECE ~0.04.

## Self-hosting notes
4B ~9 GB bf16; 9B ~19 GB; GGUF Q4/Q5/Q8 for CPU (0.6 s/decision on M1 Pro, 4B). `pip install "jevk5[fast] @ git+..."` plus flash-linear-attention for Qwen3.5.

## Assessment
Good evidence that a few-thousand-question teacher set + replay LoRA reaches near-Jev hard-tier scores on small models. Weaknesses: knowledge/hard-case gap; Judging-answers family regressed; OpenAI-derived data adds license friction; tournament for >16 options is an approximation. Strong external validation (JevBench #2) makes it a key baseline.

## Sources
- https://github.com/allebee/jevk5 (README via gh api)
- https://huggingface.co/alibiserikbay/JevK5 (model card; API metadata)
