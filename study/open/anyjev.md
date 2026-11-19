# AnyJev

- **Category**: open
- **Owner / org**: nokia-applied-research (authors: Jiamu Zhang, Tianze Yang, Yucheng Shi, Liang Wu; Nokia Sunnyvale / Tencent Hunyuan)
- **URLs**: https://github.com/nokia-applied-research/AnyJev ; PyPI `anyjev`; docs in repo (`docs/levels.md`, `docs/method_v3.md`, `docs/rotation_budget.md`, `docs/research_log.md`)
- **License** (code / weights): Apache-2.0 / heads for 5 Qwen3 models shipped in repo (`anyjev-heads/`); base models keep own licenses
- **First release / last update**: created 2026-09-21 / last push 2026-09-28
- **Popularity signals**: ~997 GitHub stars (gh api, 2026-10-01); PyPI package exists

## Summary
A Python library that turns any open LLM into a Jev-style decision model with a ladder of "levels" (raw, L0, L1, L2) that trade labels for quality. The distinguishing point: it is the only project in this batch that treats position bias and calibration as first-class, measurable things, and it adds a label-fitted linear head on a mid-depth hidden state (L2). Strictly, L0/L1 are training-free; L2 needs 100-300 labels per question (closed-form fit, no gradients, weights untouched).

## Approach / architecture
- Typed question (choice / noul / score) rendered as a lettered multiple-choice prompt; one prefill; probabilities read from the next-token distribution restricted to option-letter tokens ("raw" level). Max 26 options in the letter readout (README limitation).
- **L0 (zero labels)**: averages position bias out by reading the question over every cyclic shift of the options (K prefills for K options) and divides out a label prior estimated without labels from the batch. Optional "rotation budget" (`adaptive_shifts=True`): read rotations one at a time and stop when the leader is far enough ahead; threshold calibrated against its own full-cycle readout with no labels (7.2 rotations instead of 18 at a certified 1% disagreement rate; 2.2x decisions/s on vLLM, 2.3-2.7x on transformers; author-measured).
- **L1**: temperature scaling on top of L0 (100-500 labels per question). Ranking unchanged.
- **L2**: closed-form (ridge-style, "one solve") head per question on the hidden state at an intermediate block (e.g. block 24/36 of Qwen3-8B; model truncated, so cost is ~0.7x of a full forward). Heads ship as 1.8-4.4 MB files with 23 heads per model. Heads are self-maintaining: feature mean/scale re-estimated from unlabelled traffic (30 unlabelled requests recover a reworded-question drop from 0.65-0.70 to 0.74-0.75, author claim). `d.observe(q, state, label)` auto-solves at 30 labels, re-solves at 60, 120...
- Every `Decision` carries its `level`; `require="L1"` lets downstream code refuse weaker decisions.
- Parallelism: HF/transformers and vLLM backends; L2 on vLLM works via an embed server's pooler (`--task embed`, LAST pooling, no normalise) on a layer-truncated checkpoint (`anyjev.truncate`), so a decision endpoint is "a pooling server plus a few kilobytes of head". SGLang not yet. Prefix/KV sharing is left to the engine; the library's own contribution is the rotation scheme.

## Interface
Python library (`Decider`, `Question.choice/noul/score`, `decide`, `decide_batch`, `fit_head`, `calibrate_adaptive`). Backends: transformers, vLLM. The README does not describe an HTTP server or `/v1/systemone` wire compatibility (grep found no mention); there is a "Jev mode" demo doc and game demos (2048, Minesweeper, maze). Not a drop-in for the Jev SDK.

## Training & data
No gradient training. L1/L2 use labels (100-500 / 100-300 per question). Benchmarks: BANKING77 (20-way), LocalLLaMA/typed-decisions (20 questions x 300 labels, 2,000 held-out decisions, gold = mean of three samples of a teacher LLM; teacher self-agreement 0.735 per README). Heads for Qwen3 1.7B/4B/8B/30B-A3B/32B released in repo.

## Reported performance
All author-measured unless noted; numbers claimed regenerated from committed JSON and "a second run from a clean checkout reproduced every zero-label number bit for bit" (author claim).
- Qwen3-8B, BANKING77-20, 300 items: order-flip rate raw 0.230 -> L0 0.073; accuracy 0.747 -> 0.803; ECE raw 0.240 / L0 0.184 / L1 0.095; share auto-decidable at <=5% error 7.7% -> 46.3% (L0) -> 52.0% (L1).
- typed-decisions, L0 vs L2: Qwen3-1.7B 0.494 -> 0.730; 4B 0.564 -> 0.786; 8B 0.647 -> 0.771; 30B-A3B 0.630 -> 0.799; 32B 0.700 -> 0.798. Pooled ECE 0.03-0.05 for L2. Compared with "Jev 0.727 and fine-tuned Laya 0.768 on the same set, as published by their authors" (not rerun).
- Caveat: accuracy on typed-decisions is agreement with a teacher LLM. Limitations section also says L0's batch prior costs accuracy when one label dominates.

## Self-hosting notes
`pip install "anyjev[hf]"`; three commands to truncate, serve with vLLM, and fit a head. `python -m anyjev.pipeline <model>` converts/serves/measures in one go. `--backend fake` demo runs on CPU in seconds. Needs a GPU for 7B-class models; vLLM >= version supporting pooler config override.

## Assessment
Strongest methodological content in the batch for a lab: explicit order-flip metric, label-prior correction, risk-coverage framing ("auto-decidable at 5% risk"), and the finding that a mid-depth linear head beats the last-layer readout. Weaknesses: L2 is per-question and per-model (not training-free in the strict sense, does not transfer), no Jev wire format, headline L2 numbers rely on a teacher-LLM gold. Conformal abstention is only a roadmap item ("conformal abstention" listed under future work). Relevant as a reference harness for calibration/bias experiments.

## Technical report (added 2026-10-08)
arXiv 2610.00831 (see [../recent_study/evidence/methods-and-training.md](../recent_study/evidence/methods-and-training.md)) documents two training-free corrections:

- **Label prior:** divides out a label prior estimated from unlabelled inputs.
- **Rotation averaging:** averages log-probabilities over the K cyclic rotations of the option list.
  - Lowers the order-flip rate from 0.328 to 0.138 (banking20) and from 0.334 to 0.183 (newsgroups).
  - Raises accuracy on 11 of 11 models on both tasks.
  - Gains on already-trained 9B and 32B decision models are tiny (+0.16 and +0.56 points).
  - The prior step (alpha 0.75) lowered accuracy on a skewed-label set (65.0–65.6% vs about 68%).
- **Stopping rule:** reads 7.3 of 18 rotations, for 2.2x throughput on vLLM. Its error bound holds only when threshold selection and verification use disjoint states.

A 5G testbed study (2609.33689; abstract) found AnyJev acted wrongly on at most 0.137 of changed questions, against up to 80% for a fine-tuned Laya.

## Sources
- https://github.com/nokia-applied-research/AnyJev (README via gh api, repo metadata, docs listing)
