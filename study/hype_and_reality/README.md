# Hype and reality: when Jev-style decision models fail, when they work, and whether bigger helps

Investigation run on 2026-10-02 after [game_test/p2](../../devdocs/episodes/game_test/p2/report.md) and [ex1](../../devdocs/episodes/game_test/p2/ex1/report.md). Episode log: [devdocs/episodes/study/hype_and_reality/p1](../../devdocs/episodes/study/hype_and_reality/p1/report.md).

Every statement below is labelled as one of:
- **Source:** with a grade from the [evidence index](evidence/README.md).
- **Local:** our measurements.
- **Inference:** our reading.

## Files
| File | Contents |
|---|---|
| [local-failures.md](local-failures.md) | What must be explained: local failure classes L1–L9, margins, limits, questions Q1–Q8 |
| [search-log.md](search-log.md) | Queries, tools, inclusions, exclusions, unreachable sources |
| [evidence/](evidence/README.md) | 34 graded evidence files (A 5 / B 19 / C 10) and the index |
| [workloads.md](workloads.md) | Which workloads succeed, under which conditions, and where the evidence stops |
| [model-scale.md](model-scale.md) | Scale vs training vs readout; four approaches; confounders |
| [candidates.md](candidates.md) | Verified local candidates and feasibility on this Mac |
| [next-experiment.md](next-experiment.md) | Proposed controlled experiment (not executed) |

## Answers

### 1. Have others seen failures like ours?
**Yes. Failures of the same kinds are widely reported, and they are not specific to jeff.**
- **Off-topic text and requests for missing actions accepted as a listed option (local L2/L3):**
  - Laya issues: chit-chat routed at 0.77–0.91, even with a `none` option (B).
  - Von: an unlisted situation goes to the nearest lexical option (B).
  - Hosted Jev: flags 0/30 out-of-scope messages when no `none` option exists (B).
  - Classic NLU, CLINC150: ~96% in-scope accuracy but 40–59% OOS recall (A).
  - LLM multiple choice: 30–50% drop when "none of the above" is correct, across 1.5B–671B (A).
- **Text inside the input steering the answer (L4):**
  - Appended instructions flip Laya 49–63%, SemIf-4B 27%, Winnow-12B 3%, Jev 0.09% (A).
  - Laya answers "do NOT cancel" with `cancel_account` at 0.9998 (B).
  - **The exact local pattern, an override that names an option key, has no external report. Nobody has published an injection test of jeff/GLiFormer.**
- **Order and context effects (L5–L7):** reproduced for Laya and jeff (B). Hosted Jev showed none (B).
- **Confidence (L8):** wrong answers at high confidence are common. Local error-ranking AUC 0.73 matches hosted Jev's 0.73 on CLINC150 (B).

### 2. What kinds of use tend to succeed?
- **Labels:** bounded, in-distribution label sets where every input is expected to belong to a label.
- **Error cost:** wrong labels are cheap, reviewed, or escalated.
- **Inputs:** cooperative rather than adversarial.

The documented positive cases all add a product-side safeguard:
- Entagl: confidence gate + escalation (C);
- Arize: human review band (C);
- jev-engineering: regex rules first, fail open to a permission prompt (B);
- Banking77 router: LLM escalation (B).

Rejection worked better where the model was **trained** to say "none":
- episodes with the correct option removed (laya-intent-router 0.68 → 0.99, author-reported, C);
- varied negatives (B).

A zero-shot `clarify` label plus a margin threshold did not work as well. See [workloads.md](workloads.md).

### 3. Are small models the problem?
**Partly.** (Source + inference.)
- **Where scale clearly helps:** ~0.5B encoders (jeff, Laya, open-jev-deberta) sit at 35–39% on JevBench's hard tier. 4B LLM readers reach ~61%, and stock 12B instruct models reach ≈ Jev's 73%. On abstain items jeff scores 0/7 and Gemma-12B 13/14 (B). Injection resistance is far better in large or well-trained models (A).
- **Where scale alone does not help:**
  - In the same Kev recipe, 4B → 9B adds little, and injection robustness is not monotonic (A/B).
  - "None of the above" weakness persists at every scale (A).
  - One preprint shows larger models following embedded instructions *more* (B).
  - In Decider, stock models read through the same readout beat trained ones, so base, training and readout all matter (B).
- **No source measures our three costly failure types by model size.**

### 4. Should we try a larger base model locally?
**Yes, as a controlled test, not as an expected fix.** The current encoder family cannot be scaled up: GLiFormer exists only at 264M and 576M. The [proposal](next-experiment.md) compares:
- **Kev 4B vs 9B:** same recipe; MLX and `/v1/systemone` documented;
- **stock Qwen3.5 4B/9B readers:** the same bases, without decision training;
- **Qwen3.8-27B with JSON schema:** already pulled in local Ollama;
- **opaque vs original option keys,** in every arm.

All arms run on fresh non-order-heavy data with a matched false-rejection budget. Confirmation stays in place until an arm meets the automatic-execution criteria on every non-order type.

## Corrections and caveats
- **jeff's model is ~575M parameters, not "400M".** The GLiFormer-large card says 575.6M, and the local weight file is 2.30 GB fp32. jeff's README and [study/open/jeff.md](../open/jeff.md) say ~400M.
- **"Jeff" on sotaaz.com is a different, Qwen3.5-based model.** It was excluded from jeff conclusions.
- **Source quality:**
  - Several paper numbers came through WebFetch summaries (flagged in the files).
  - Reddit, X and HN were not readable.
  - Many reports are single-author or author-run.
- **Local evidence:** agent-written English cases, one machine, no human player.
