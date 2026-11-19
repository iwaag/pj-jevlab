# AutoJev-27B (denis-pplx)

- **Category**: open
- **Owner / org**: denis-pplx (github.com/denis-pplx/autojev; "built with autonomous agents")
- **URLs**: repo https://github.com/denis-pplx/autojev ; weights https://huggingface.co/denis-pplx/autojev-27b (also autojev-sft-27b; mirrors/GGUFs by other users)
- **License** (code / weights): MIT / Apache-2.0
- **First release / last update**: repo created 2026-09-19, pushed 2026-09-22
- **Popularity signals**: GitHub 114 stars; HF 1,136 downloads, 47 likes. Note: a different project, autotrust/JEV-27B, is unrelated.

## Summary
Full-weight SFT of Qwen3.8-27B on 73,000 unique curated decision examples (one H200, 286 updates, released checkpoint at step 200), with cross-entropy and a separately fitted scalar temperature. Multimodal (images accepted), TypeSafe-compatible API. Third-party leaderboards rate it near Jev.

## Approach / architecture
Qwen3.8-27B backbone, all weights trained; one forward pass per question returning probabilities over supplied choices (custom `DecisionModel` loader, `custom-code`); `POST /v1/systemone` with choice/noul/score and optional base64 images; browser playground. About 49 GiB bf16 weights.

## Training & data
Cross-entropy, full-weight SFT, 73k examples, 286 updates on one H200; temperature fitted separately. The curated training corpus is not bundled. Per Kev's PLAN.md the data is "73k broad synthetic decisions" (Kev author's description, not AutoJev's own words). No RLCD; no teacher disclosed in the README.

## Reported performance
Author table (own benchmark, setup not detailed): accuracy 84.60% (Qwen3.8-27B 69.83%, Jev 82.79%), ECE 0.04282 (vs Jev 0.05274), Brier 0.22027 (vs 0.25400). Third-party (from other READMEs, not re-run by us): Decision Index v0.2: AutoJev-27B 50.94 (Jev 51.67) per AutoTrust; Decision Index v0.2.1: 56.40, rank 3, ECE 0.018 per Decider README; Kev PLAN.md measured AutoJev-27B as best at breadth: ahead of Kev-27B on 8 of 9 Kev suites.

## Self-hosting notes
One 80 GB-class GPU (49 GiB weights + overhead); `uv sync`, `autojev-serve`.

## Assessment
Evidence that broad full-weight SFT at 27B, with minimal tricks (CE + temperature), gets close to Jev; useful as the strongest plain-SFT baseline. Training corpus unreleased, so not reproducible.

## Sources
- https://github.com/denis-pplx/autojev ; https://huggingface.co/denis-pplx/autojev-27b
- https://github.com/jaredpalmer/kev (PLAN.md) ; https://github.com/Mapika/decider (README) ; https://huggingface.co/autotrust/JEV-27B
