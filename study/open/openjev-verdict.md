# OpenJev Verdict / Verdict 2.0 (Heman10x-NGU)

- **Category**: open
- **Owner / org**: Heman10x-NGU (HF: heman10x)
- **URLs**: https://github.com/Heman10x-NGU/Verdict-open-jev ; https://github.com/Heman10x-NGU/openJev-verdict-2.0 ; HF https://huggingface.co/heman10x/rlcd-modernbert-151m ; HF https://huggingface.co/heman10x/openJev-verdict-2.0 ; dashboard https://heman10x-ngu.github.io/openJev-verdict-2.0/
- **License** (code / weights): README badges and text say Apache-2.0; GitHub API reports NOASSERTION for both repos (no recognized LICENSE file detected). HF license metadata: none set on rlcd-modernbert-151m.
- **First release / last update**: Verdict-open-jev created 2026-09-17, last push 2026-09-28; openJev-verdict-2.0 created 2026-09-19, last push 2026-09-20.
- **Popularity signals**: Verdict-open-jev 109 stars; openJev-verdict-2.0 293 stars; HF rlcd-modernbert-151m 27,916 downloads, 37 likes.

## Summary
Two related models from one author. "Verdict" (151M) is ModernBERT-base + GLiClass bi-encoder head with abstention slot, evaluated on JevBench. "Verdict 2.0" (149.6M) is a specialized head trained on the `LocalLLaMA/typed-decisions` benchmark with a separate confidence head. The repos carry self-critical audit experiments (shuffled-context, order sensitivity, contamination) alongside strong headline claims.

## Approach / architecture
- Verdict 1: ModernBERT-base (151,378,177 params) + GLiClass-style bi-encoder head (document and label tokens concatenated with `[TEXT]`/`[LABEL]` delimiters; one pass). Up to 25 candidate slots (24 + an explicit `__insufficient_evidence__` abstention). Loss CE + Brier, post-hoc L-BFGS temperature scaling. README says the weights descend from `knowledgator/gliclass-modern-base-v2.0` (NLI-style pretraining), which is why v1.4 added "It is {description}" hypothesis templating. Context budget cut 1024 -> 512 (trained on states < 71 tokens).
- Optional "topological DAG execution": dependent fields evaluated in a second pass with parent answers appended as state.
- Verdict 2.0: ModernBERT-base, marker-pointer logits (distribution head) plus a dedicated out-of-fold-trained MLP confidence head ("dual-channel calibration"); symmetric permutation-KL penalty for option-order robustness. Weights tracked via Git LFS pointers (`artifacts/verdict2-base/model.pt`) in the repo; HF `heman10x/openJev-verdict-2.0` listed.
- Primitives Choice / Score / Noul via a Python SDK (`rlcd.DecisionEngine`). Not stated to expose `/v1/systemone`; I did not find a Jev-compatible HTTP server in the README. In-browser WebGPU/ONNX playground included.

## Training & data
Verdict 1 fine-tuned largely on Banking77-style data (held-out 1,000 cases with 5 candidates; CLINC150 for OOS). Verdict 2.0 fine-tuned in 8.8 h on a GTX 1660 Ti (6 GB) on typed-decisions training split (author claim). Contamination audit reported: 0 exact matches / 2.3M pairs, 3 near-duplicate pairs.

## Reported performance (all author-measured unless noted)
- Verdict 1 on 231 public JevBench tasks after inference fixes (v1.4): easy 87.5%, standard 69.4%, hard 36.9%, hard-tier ECE 0.298 -> 0.118. Independent: jeff README says JevBench ranks "openJev Verdict 151M at #11" of 18 on v1.2.2; Von card says Verdict 1.4 ties Von on sealed Choice (17.9).
- Verdict 1 in-domain Banking77 (K=5): 95.0% acc, ECE 1.1% raw; falls to 72% at K=25; OOS abstention recall 97.5% but precision 89.45%; abstention does not generalize to hard negatives/synonyms (recall 10% combined).
- Author's own E9: on TypeSafe's public cases (337) Verdict 1 scores 48.07% vs Jev 90.80% - an unusually candid admission of a zero-shot gap.
- Verdict 2.0 on typed-decisions (2,000 decisions): 77.10% acc, Brier 0.0636, correctness-head ECE 0.0144, distribution ECE 0.1513, ~20-25 ms; table compares to Jev 72.70% and Laya 76.60% (Jev/Laya figures taken from Laya's published suite). Verdict 1.0 baseline on that benchmark: 26.10%. A TF-IDF + LogReg baseline scored 66.10% acc - a reminder of how weak the benchmark floor is. The repo description's "beating Jev & Laya" is an author claim; I found no independent replication.
- Note: HF-hosted Laya number 76.60% in this table vs 0.766 in Laya's own README refers to the fine-tuned checkpoint on the same benchmark.

## Self-hosting notes
`git clone`, `pip install -e .`, `python scripts/download_artifacts.py`; ONNX model on HF; runs on CPU, ~35 ms p50 single-thread WASM proxy (author E7). Browser WebGPU demo under 600 MB.

## Assessment
Strengths: smallest (150M) model in the encoder group with abstention and cost-efficient training; extensive self-audit reports. Weaknesses: licensing metadata inconsistent (NOASSERTION); English, <=25 options; heavy dependence on Banking77/typed-decisions; zero-shot generality weak (48% vs Jev 90.8% on TypeSafe cases, author-measured); Verdict 2.0 weights partly LFS pointers. Treat 2.0's headline as in-distribution fine-tune result.

## Sources
- https://github.com/Heman10x-NGU/Verdict-open-jev (README via gh api)
- https://github.com/Heman10x-NGU/openJev-verdict-2.0 (README via gh api)
- https://huggingface.co/api/models/heman10x/rlcd-modernbert-151m
- https://github.com/logan-markewich/jeff (bench/RESULTS.md for JevBench ranks); https://huggingface.co/wfzyx/von
