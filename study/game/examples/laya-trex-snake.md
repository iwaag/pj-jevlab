# Laya vs Jev T-Rex and Laya-MLX Snake (local encoder)

## Overview
Two related demos built on [laya-mlx](https://github.com/mizorewww/laya-mlx), the MLX port of the open Laya encoder:
- **laya-vs-jev** (virajbhartiya): Chrome's T-Rex game played side by side by local Laya (MLX on Apple Silicon) and hosted Jev.
- **laya-snake**: a terminal Snake game in laya-mlx, where every move calls Laya.

In both, a deterministic planner or safety layer proposes or corrects moves, and the model chooses among them.

## Relevance level
**Direct.** Laya is a Jev-style typed decision model (`choice`/`score`/`noul`; ModernBERT-large 421M or mmBERT-base 322M with decision heads). It is the closest local analogue to jeff: an encoder of similar size running on a Mac, trained rather than zero-shot. See [study/open/laya.md](../../open/laya.md).

## Maturity / evidence
- Runnable demos with recording and replay export. laya-vs-jev: 111 stars, created 2026-09-21. laya-mlx is a released PyPI package.
- **Inspected:** the laya-vs-jev README, which embeds the laya-mlx README. **Not run.**

## Game mechanic
Real-time control: jump or duck timing in T-Rex, direction choices in Snake. The model selects among moves that a planner has labelled.

## Decision inputs and outputs
- **T-Rex:** "A deterministic physics planner labels the moves, and the models choose between them. Safety checks can override unsafe or stale choices."
- **Snake:** a three-question loop per move, with a visible "cycle safety layer" that can correct unsafe proposals.
- **Consumption:** the chosen move is executed unless a safety check overrides it. A "best move" statistic measures agreement with the planner, and `--unassisted` disables the safety checks.

## Implementation / runtime
Python and MLX, with no PyTorch, Transformers or cloud API at inference time. T-Rex uses adapted Chromium game code. Jev requires network access and an API key; Laya runs fully local after download.

## Availability and licenses
Apache-2.0 (laya-vs-jev and laya-mlx code). Weights `aac6fef/laya-mlx` and `aac6fef/laya-multilingual-mlx` are Apache-2.0 according to the HF metadata. Chromium assets are BSD-3-Clause.

## Attributed results (laya-mlx author, M3 Max)
- One short question, end to end: P50 13.42 ms (421M) / 7.39 ms (322M multilingual). 50-question throughput: 146.8 / 395.0 q/s. The author notes these are API benchmarks, **not** gameplay frame times.
- Snake with `--optimize --max-speed`: 75.40 moves/s over 2,400 moves, zero deaths and 2 visible safety interventions.
- T-Rex: the README states that assisted scores "measure the combined system, not independent model skill". No model-only score is given.

## Possible jeff adaptation (inference)
- The architecture (a planner proposes, the model chooses, a shield corrects) is the safest way to put a classifier in a real-time loop.
- jeff was observed at about 50–180 ms per request on this Mac (PyTorch MPS, through HTTP) vs Laya-MLX's reported ~13 ms in-process. That is too slow for per-frame control, but jeff could make decisions at a lower rate (e.g. per obstacle or per turn) while the game keeps running.
- Laya itself is a natural comparison baseline for any jeff game test.

## Limitations
The safety shields and the planner do most of the work in assisted mode. The latency figures come from a different machine (M3 Max) and from a benchmark, not from gameplay.

## Sources (accessed 2026-10-02)
- https://github.com/virajbhartiya/laya-vs-jev (README incl. the embedded laya-mlx docs; metadata)
- https://github.com/mizorewww/laya-mlx (license via `gh api`)
- https://huggingface.co/api/models/aac6fef/laya-mlx ; https://huggingface.co/api/models/aac6fef/laya-multilingual-mlx (license metadata)
