# Proposed next local experiment: scale, training, readout and interface on Blackout Dispatch decisions

**Status: proposal, not executed** (written 2026-10-02).
- Inputs: [local-failures.md](local-failures.md), [model-scale.md](model-scale.md), [candidates.md](candidates.md), [workloads.md](workloads.md).
- Suggested home: a new `game_test` sub-episode, with code under `lab/` next to `lab/game_test/p2/ex1/`, whose harness, fixtures and confirmation session it reuses.

## Questions this experiment must separate
| Q | Question | Arms that answer it |
|---|---|---|
| E1 | Does a larger model of the **same recipe and readout** reduce non-order false acceptance (L2/L3/L4)? | Kev-4B vs Kev-9B (and 0.8B if run). jeff-large vs jeff-base is a down-scale point only |
| E2 | Does **decision training** help at a fixed base? | Kev-4B vs stock Qwen3.5-4B reader; Kev-9B vs stock Qwen3.5-9B reader (and optionally Kev-27B vs Qwen3.8-27B) |
| E3 | Is the key-naming override (L4) an **interface** effect? | Every arm × {original snake_case keys, opaque keys `job_a…job_e` with unchanged descriptions} |
| E4 | Does a **general LLM with validated structured output** reject non-orders better, and at what latency? | Qwen3.8-27B via Ollama JSON schema (system comparison) |
| E5 | Does any arm meet the bar for automatic execution, or only for the confirmation/advisory role? | All, against the criteria below |

## Arms
| ID | Arm | Checkpoint / runtime | Request path | Role |
|---|---|---|---|---|
| A0 | jeff + GLiFormer-large (current) | `knowledgator/gliformer-large-v1` (local), MPS, temperature 3.2, `JEFF_ISOLATE=nouls`, one question | `/v1/systemone` (existing adapter) | Baseline, unchanged |
| A1 | jeff + GLiFormer-base | `knowledgator/gliformer-base-v1` (264M), same server flags | same | Encoder down-scale point (no larger GLiFormer exists) |
| K4 / K9 | Kev-4B / Kev-9B (Kev 1.0) | `jaredpalmer/kev-4b@v1.0`, `jaredpalmer/kev-9b@v1.0` on `kev.serve` with MLX; shipped temperatures | `/v1/systemone` (same adapter, new base URL). Diagnostics via `/v1/systemone/permute` | Trained decision model, scale ladder |
| K0.8 (optional) | Kev-0.8B | `jaredpalmer/kev-0.8b@v1.0` | same | Lower ladder point; cheap |
| Q4 / Q9 | Stock Qwen3.5-4B / 9B option reader | `Qwen/Qwen3.5-4B`, `Qwen/Qwen3.5-9B`; SemIf-OpenJev (MLX/MPS, 4B documented) or Simple Jev (`--device auto`, MPS undocumented). **One reader for both sizes**, chosen in setup | `/v1/systemone` (Simple Jev) or a thin local wrapper | Training-free control at Kev's bases |
| L27 | Qwen3.8-27B, general LLM | Ollama `qwen3.8:27b-mlx-bf16` (already local; fallback `-mxfp8`), thinking off, temperature 0, `format` = JSON schema `{job: enum(legal keys + clarify)}`; output re-validated in code | new adapter mapping to the existing proposal path | General-LLM system control |
| K27 (optional) | Kev-27B | `jaredpalmer/kev-27b@v1.0` (51 GB) on MLX — "expected, not measured" by its author | `/v1/systemone` | Training effect at the same base as L27; run only if K9 shows a gain and setup succeeds |

Fixed for all arms:
- wording v3 descriptions;
- the same legal-option filter;
- order-only `state`;
- one question per request;
- fixed option order for the primary run;
- the same 200-character input limit and 3 s timeout (L27 may use a separately reported 10 s timeout, see latency).

## Setup prerequisites (step 1 of the experiment)
1. **Kev:** new uv env (Python 3.13) in a git-ignored `.work/` directory, `uv sync --extra serve`, first-run download of adapters + Qwen3.5 bases (~30 GB estimated for 4B + 9B). Record revisions and SHA-256.
2. **Stock reader:** install SemIf-OpenJev or Simple Jev in its own env. Confirm that 4B **and** 9B load on MPS/MLX with the same readout. If only one size works, Q9 is dropped and the drop is reported.
3. **Ollama:** check that `format` constrains output for the MLX tag. Otherwise use the mxfp8 tag or code-side validation only, and report which.
4. **Smoke test** each arm on 5 p2 dev cases. Record load time, resident memory, warm latency.
5. **Setup failure budget:** at most ~2 hours per arm. A failed arm is reported as "setup failed" with the error. It is never silently dropped.
6. Update `.local/localenv.md` with everything installed.

## Data
| Set | Content | Use |
|---|---|---|
| **Regression** | p2 dev/heldout/heldout2 (91), ex1 dev (34), final (72), final2 (72), the 39 p2 misread texts | Diagnostic and regression only; already seen, **never counted as fresh evidence** |
| **dev3** (new) | ~40 cases, agent-written, all categories | The only data used for any per-arm adaptation |
| **final3** (new) | ≥ 60 clear-intent (clear / paraphrase / state-dependent) and ≥ 60 non-orders: ≥ 20 unavailable, ≥ 20 off-topic (incl. greetings), ≥ 20 overrides (≥ 10 naming a key, ≥ 10 not), plus ~8 ambiguous. All five jobs and all states S0–S7; grouped by scenario | Formal comparison; run **once per frozen arm** |

- **Ordering:** final3 and dev3 are written and committed before any candidate is run on them, and before any per-arm tuning.
- **Authorship:** human-written orders are preferred. If a human provides them (see Human preparation), they form a separate `final3-human` slice, scored and reported separately, with authorship recorded per case. Agent-written cases are labelled as such.
- **Opaque-key variant:** the same final3 cases are rendered with opaque keys. Override texts that name original keys stay unchanged, so they now name no option. Override texts that name opaque keys are added as a small extra slice (≥ 10).

## Procedure
1. Freeze this protocol and the data (commit).
2. Setup and smoke tests (above).
3. **Bounded dev-only adaptation per arm.** At most two wording revisions of the `clarify` description and instruction, plus the margin/confidence gate. Options:
   - choose the gate that keeps clear-intent misses ≤ 10% on dev3 (the matched false-rejection budget);
   - or keep the arm's argmax if it has no usable score (L27).

   Commit the frozen per-arm configuration before final3.
4. Run final3 (original keys and opaque keys) once per arm. Log raw requests and responses, invalid outputs, timeouts and setup failures.
5. **Diagnostics (not used for the decision):**
   - 3 option-order permutations (or Kev `/permute`);
   - 2 paraphrase sets of 20 clear orders;
   - the regression sets.
6. Replay every arm's final3 proposals through the ex1 confirmation session. Confirm 0 state changes before confirmation (protection must be model-independent).
7. Latency: warm p50/p95 over n ≥ 40 single-question requests at 20 and 200 characters; startup to first answer; peak resident memory.

## Metrics (all reported per arm and key condition, with counts)
**Raw interpretation** (scored on the model's answer after the frozen gate, before any confirmation):
- clear-intent accuracy (expected job proposed, or refused as unaffordable);
- wrong-job rate on real orders;
- clarification rate on real orders (coverage);
- **non-order false acceptance**, overall and by type: off-topic, unavailable, override-with-key, override-without-key;
- false acceptance at the matched false-rejection budget from dev3. A secondary curve is computed from logged scores where the arm has one;
- invalid or unparseable outputs and timeouts. These are counted as a miss on a real order and reported as a separate error count on a non-order; they are never dropped from the denominators. Setup failures are reported per arm.

**With confirmation** (product-level):
- state changes before confirmation (must be 0);
- wrong proposals shown to the player per 100 non-orders.

**Cost:** warm p95 latency, startup, memory, download size.

**Statistics:**
- Comparisons between arms are paired on the same cases: report the discordant counts and an exact McNemar test.
- With ~60 cases per group, a single-arm 95% CI is about ±12 points. A difference is called a finding only if McNemar p < 0.05 **and** the gap is ≥ 10 points.
- Everything else is reported as "no detectable difference at this n".

## Acceptance criteria (pre-registered)
| Role | Criteria on fresh final3 (original keys unless stated) |
|---|---|
| **Automatic execution** (no confirmation) | clear-intent ≥ 90%, wrong-job ≤ 2% on real orders, non-order false acceptance ≤ 10% overall **and** ≤ 10% in every non-order type including override-with-key, warm p95 ≤ 1 s. On `final3-human`, if it exists, the same thresholds hold within 1 case. Benchmark rank or clear-intent accuracy alone never qualifies an arm |
| **Confirmation / advisory** (current design) | clear-intent ≥ 85%, non-order false acceptance ≤ 20% (vs 38–44% today), warm p95 ≤ 1 s, 0 pre-confirmation state changes |
| **Interface fix sufficient** | Opaque keys bring override-with-key false acceptance to within 10 points of override-without-key for A0, without a clear-intent loss ≥ 5 points |

## Decisions supported by possible outcomes
| Outcome | Decision |
|---|---|
| K9 (or K4) passes automatic-execution criteria; A0 does not; K4→K9 gain is significant | **Larger trained model:** adopt for automatic execution (still behind legality checks), re-run with human wording before the game build |
| K4 ≈ K9, both much better than A0 and Q4/Q9 | **Training/readout, not size:** use the smaller Kev (4B), consider a short game-specific fine-tune with removed-gold episodes rather than a larger model |
| Q4/Q9 ≈ K4/K9 | Base capacity dominates; choose by latency; decision training not needed for this task |
| L27 best but p95 > 1 s | Large general LLM is only a quality ceiling or offline labeller (e.g. to generate fine-tune data); not the runtime model |
| Opaque keys fix most L4 on A0, and L2/L3 stay similar across arms | **Interface/design fix:** keep jeff + confirmation, change keys; handle unavailable jobs in code ("not yet") |
| No arm meets the confirmation-role bar on non-orders | **Redesign interaction:** keep confirmation, add explicit job controls (advisory mode), postpone automation |
| Setup failures block the ladder (K9 does not run) | Report as a feasibility result; fall back to the Decider 2B/4B ladder or to the 4B comparison only |

## Human preparation (optional, improves the result)
- **Human-written orders (most valuable):** 40–80 orders written by people who did not author the options. They should see only the game description and state, and include their own small talk and "tricks". This is the only way to address Q7.
- **No API keys** are needed. Hosted Jev would be an optional external reference, but it sends text off the machine; skip it unless explicitly approved.

## Out of scope
Godot integration, any training or fine-tuning, Japanese input (a separate model decision), multi-question requests.
