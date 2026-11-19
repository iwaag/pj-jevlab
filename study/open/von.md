# Von

- **Category**: open
- **Owner / org**: wfzyx (Victor Hugo Panisa per citation)
- **URLs**: repo https://github.com/wfzyx/von ; HF https://huggingface.co/wfzyx/von ; PyPI/npm `von-sdk`; Docker `ghcr.io/wfzyx/von:cpu`
- **License** (code / weights): Apache-2.0 / Apache-2.0
- **First release / last update**: repo created 2026-09-18, last push 2026-10-01; HF created 2026-09-19, modified 2026-09-30. Current: Von 1.3 (`von-1.3.0`, weights unchanged from 1.2).
- **Popularity signals**: GitHub 801 stars; HF 78,075 downloads (API field "downloads", likely 30-day), 52 likes.

## Summary
Open-source System One model on ModernBERT-large (395M) with an Option-Marker scoring head, English only, drop-in server/client for the TypeSafe `/v1/systemone` wire protocol. Of the open projects, it is the one with the most rigorous evaluation discipline (paired McNemar tests, JevBench sealed/open, Decision Index, jabr v2, out-of-sample suites) and an honest limitations list. Other projects (poorjev) benchmark against it and report it as the best open option on Banking77.

## Approach / architecture
- State, question and all candidate options packed into ONE sequence; each option gets a `[MASK]` marker whose final hidden state is scored by a small head; softmax over markers = answer distribution. One encoder pass regardless of option count. Noul = two-option Choice (holds / is false, or caller's `criteria`); Score = Choice over level descriptions with expectation over distribution.
- Order-invariant scoring (since 1.2): custom attention so each option's tokens attend only to the shared premise and itself, position ids restart per option. Author-measured on JevBench hard (111 items x 4 orderings): v1.1 flipped 49.5% of answers, v1.2 flips 0.
- "Chain-of-options" engine in 1.3 (sub-decisions, max 16 encoder calls) improves public hard 0.378 -> 0.441 locally (McNemar p = 0.065, not significant by author's own rule).
- Context 8192 tokens; middle-truncation or HTTP 422 on overflow.
- Calibration: input-conditioned temperature `T = bias + w_H*H_norm + w_len*log10(tokens)/4 + w_K*(K/8)`, clamped [0.3, 12]; Noul passes a "band" rule mapping p to 0.8+0.1(p-0.5) so answers commit outside the 0.2-0.8 abstention band. `von calibrate labels.jsonl` refits on user labels in minutes on CPU.

## Interface
`/v1/systemone` byte-compatible with TypeSafe spec (change base URL; `VON_API_KEY` for bearer auth). Python and TypeScript SDKs (`decide`, `judge`, `rate`, `system_one`). CLI `von serve`, `von calibrate`. Runs on CPU (OpenVINO), CUDA, ROCm, Apple MPS.

## Training & data
Fine-tuned ModernBERT-large with listwise softmax CE + Brier on a ~290k-item balanced decision corpus (ops/enterprise workflows ~25%, security/devops ~20%, safety/policy ~15%, linguistic ~15%, triage ~10%, ANLI/WANLI anchor ~15%), then continued on synthetic two-hop/numeric sets. Corpus builders released under `training/`. Author states no JevBench item (public or sealed) used for gradient training; calibration map fitted on the 231 public JevBench items (so in-sample there).

## Reported performance
- JevBench v1.4 table (author-reproduced; JevBench is run by Benchmark Heaven): Von 1.2 Intelligence 34.5, composite 27.5, sealed 0.279, sealed ECE 0.107 vs Jev 1.13 Intelligence 53.1, composite 63.3, sealed 0.367; jeff 36.8 / 30.6 / 0.331; Laya 36.1 / 30.3 / 0.308 / ECE 0.172. v1.5.1 board: Calibration 83.5, Cost 82.7; Noul sealed competence negative under the v1.5 abstention rule until the band fix (re-measurement pending).
- Latency: 0.096 s raw p50 on 4 vCPU (OpenVINO), 0.023 s on A10G (JevBench protocol); 32.8 ms p50 on A10G in Decision Index.
- Out of sample: Decision Index v0.2.1 score 13.74 (raw 34.11); jabr v2 72.0% macro (Choice 83.0%); ViZDoom Defend-the-Center 9.0 kills/episode vs Jev 1.13 5.6 (author-run).
- Third-party: poorjev crossbench (author of a competing project) measured Von Banking77 acc 0.838 (> Jev 0.812) ECE 0.135; multi-primitive set acc 0.775 ECE 0.108 vs Jev 0.906 / 0.045.
- Calibration caveat (author): map is JevBench-shaped and "does not carry to other distributions"; on a 38-label probe a refit scalar T=2.15 moved ECE 0.21 -> 0.11.

## Self-hosting notes
~3 GB fp32 weights (1.5 GB per card) fetched on first use; Docker CPU image provided; auto device selection. English only; `judge` without `criteria` is weakest path; known training gap on auth failures/rate limits (issue #22).

## Assessment
Strengths: best-documented evaluation among encoder-based open projects, wire-compatible, order-invariant design, calibration refit CLI, permissive license, active (pushes through 2026-10-01). Weaknesses: English only; behind Jev on JevBench composite and hard-tier reasoning; shipped calibration is in-sample on JevBench. Good reference implementation for a lab; worth reading the training scripts and the order-invariant attention trick.

## Sources
- https://github.com/wfzyx/von (README)
- https://huggingface.co/wfzyx/von (card, HF API)
- https://github.com/rupeshpoojary9/poorjev (crossbench numbers)
