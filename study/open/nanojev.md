# NanoJev

- **Category**: open
- **Owner / org**: Tianyu Chen (github.com/TianyuCodings)
- **URLs**: repo https://github.com/TianyuCodings/NanoJev ; model https://huggingface.co/C-Tianyu/NanoJev ; data https://huggingface.co/datasets/C-Tianyu/NanoJev-Data ; follow-up project JevHarness (github.com/TianyuCodings/JevHarness)
- **License** (code / weights): MIT (repo); weights license not stated in HF metadata I fetched
- **First release / last update**: repo created 2026-09-17, last push 2026-09-21; HF tag `unified-games-v1`
- **Popularity signals**: GitHub 2,463 stars; HF 8,094 downloads, 84 likes

## Summary
A 0.6B "nano replica" of Jev built on Qwen3-0.6B with trained decision heads, aimed at game-playing decisions (Maze, Snake, ViZDoom Basic and Predict Position). It is the only project in this set with a written-up RLCD-inspired objective experiment, but the released model is trained with supervised cross-entropy; RLCD post-training is still a roadmap item.

## Approach / architecture
- Backbone Qwen3-0.6B (release checkpoint about 4.8 GB incl. initialization files) with shared scoring heads: Choice uses set attention over 2-255 candidates then softmax; Boolean uses a sigmoid; Score is a distribution over 2-10 ordered levels with expectation. Candidate paths encoded by the backbone; batching of independent states/questions/candidates in one backbone forward; no answer-token decoding.
- A persistent inference service at `POST /api/evaluate` (custom API, not the TypeSafe wire format as far as the README shows; docs/TYPESAFE_CONTRACT.md describes the input contract).

## Interface
Custom `DecisionPredictor` API and `scripts/serve_decisions.py` (CUDA). Browser replays/playground for ViZDoom, Maze, Snake. No evidence of `/v1/systemone` compatibility.

## Training & data
- Released checkpoint: step 400 of a 600-update run `hard_lr1e5` (backbone lr 1e-5, head lr 1e-4), mixed-task supervised cross-entropy, 24 questions/update (8 Maze, 8 Snake, 4 Basic, 4 Predict Position), BF16, 8,192-token cap. Hard (one-hot) vs soft Predict-Position targets compared; hard won on development.
- Data: 18,760 decision questions per target variant (10,898 train; 16,333 are ViZDoom), 896 expert Predict-Position episodes (17,498 decisions). Data is game/simulator-generated (expert and programmatic), not LLM-synthetic text; the dataset is released.
- RLCD experiment (docs/RLCD_EXPERIMENT.md): states explicitly that TypeSafe's reward and optimizer are undisclosed and the formula is an "independent research candidate". Objective: draw M>=2 predictions from the candidate softmax, reward = pairwise agreement with the observed outcome minus a same-sample agreement penalty, which has expectation 2 p.q - ||p||^2 (equivalent to minimizing squared L2 to the true outcome distribution), optimized with a policy gradient and a conditional baseline. Verified by exact enumeration (gradient error 1.4e-16). On a CPU MLP and on a Qwen3-0.6B event task the paired policy-gradient was no better than direct controls: Qwen test NLL/Brier/known-q L2 0.428/0.278/0.118 (paired PG) vs 0.450/0.303/0.124 (CE) vs 0.451/0.303/0.138 (direct Brier); OOD NLL was best for direct Brier. Authors conclude evidence does not show sampled RL beats direct proper-scoring losses. One seed on the Qwen run.

## Reported performance
Author-run held-out gameplay (274-case test; same controller across systems): Basic 128/128 vs Jev 56/128; Predict Position 27/128 vs Jev 11/128 (untuned Qwen 11/128); Snake 8/8 for NanoJev and Jev; Maze 4/10 vs Jev 7/10. Maze exit in 225 attempts vs Jev 2,738. Jev runs by the author (via API); not independently reproduced. These are game-control results, not text-decision accuracy or calibration comparisons.

## Self-hosting notes
CUDA environment; checkpoint/dataset via `snapshot_download(revision="unified-games-v1")`; `requirements-toy.txt`, ViZDoom extras.

## Assessment
Strengths: only open attempt that writes down and gradient-checks an RLCD-like proper-scoring RL estimator and reports it honestly as not superior; also shows that a very small model with a task-specific head can win on narrow control tasks. Weaknesses: domain is games, not text decisions; no calibration comparison to Jev on standard benchmarks; RLCD not applied in the released weights. Relevance: reference for what an RLCD reproduction experiment looks like and how little it buys over CE/Brier in a small test.

## Sources
- https://github.com/TianyuCodings/NanoJev (README; docs/UNIFIED_DEVELOPMENT_RELEASE.md; docs/RLCD_EXPERIMENT.md via gh api)
- https://huggingface.co/api/models/C-Tianyu/NanoJev
