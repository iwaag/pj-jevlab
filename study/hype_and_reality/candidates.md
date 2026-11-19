# Candidate models for the next local experiment

Verified 2026-10-02:
- **HF API:** existence, base, licence, parameter counts;
- **GitHub READMEs** (`gh api`): runtime and API;
- **local machine inspection:** installed runtimes.

Nothing was downloaded or run for this survey. "Documented" means stated by the project. "Local" means observed on this Mac. "Expected" means neither.

Machine: Apple M3 Ultra, 512 GiB unified memory, ~1.2 TiB free disk, PyTorch MPS working (jeff), uv available. Found during this survey:
- **Ollama 0.32.15** (`/opt/homebrew/bin/ollama`), with `qwen3.8:27b-mlx-bf16` (55 GB) and `qwen3.8:27b-mxfp8` (31 GB) already pulled;
- **LM Studio** (`lms` CLI), with unrelated models;
- no `mlx`/`mlx-lm` Python package and no `llama-server`.

Fitting in memory does not by itself show that the backend supports a model.

## Shortlist (ranked)
| Rank | Candidate | Role | Exact checkpoints | Base / licence | Backend on this Mac | API | Why |
|---|---|---|---|---|---|---|---|
| **1** | **Kev 4B and 9B** (optionally 0.8B, 27B) | Trained decision model; **within-family scale ladder** | `jaredpalmer/kev-4b`, `jaredpalmer/kev-9b` (LoRA adapters + pointer head, Kev 1.0 `v1.0` tags; 9B rev `b5d8c18e`); optional `kev-0.8b` (rev `9a45d25e`), `kev-27b` (rev `28be62e9`, 25.6B full weights, 51 GB) | Qwen3.5-4B-Base (4.66B) / 9B-Base (9.65B); 27B on Qwen3.8-27B; all Apache-2.0 | **MLX documented** for Apple Silicon (auto in `kev.serve`). 0.8B/4B measured by the author on an M5; **9B and 27B "expected, not measured"**. Needs Python 3.12/3.13 + uv; the first run downloads the adapter + base | **`/v1/systemone` drop-in** (TypeSafe SDK compatible), plus `/v1/systemone/permute` and `/separate` | Same recipe and readout across 0.8/4/9B; trained with removed-evidence and abstention cases; best size evidence (B); injection data exists (A). Weights est. 9.3 GB (4B), 19.3 GB (9B) bf16 |
| **2** | **Stock Qwen3.5-4B and 9B, option reader** | Training-free reader at the **same bases as Kev** (isolates training from size) | `Qwen/Qwen3.5-4B` (4.66B), `Qwen/Qwen3.5-9B` (9.65B); instruct releases, Apache-2.0 | self | SemIf (repo now `TheoLeeCJ/SemIf-OpenJev`, MIT, last push 2026-09-23) documents both PyTorch MPS and MLX, but is pinned to Qwen3.5-4B. Simple Jev (`featherless-ai/simple-jev`, Apache-2.0, last push 2026-10-01) has `/v1/systemone`; its README shows only `--device cpu|cuda|auto`, so MPS/MLX is **not documented**. A minimal reader (option-name log-likelihood via transformers on MPS) is a fallback; it would be new local code | SemIf: library, no server; Simple Jev: `/v1/systemone` | Separates "Kev's decision training" from "Qwen3.5 size". Readout choice is itself a confounder, so fix it |
| **3** | **Qwen3.8-27B with JSON-schema structured output** | General-LLM **system control**; same base as Kev-27B | Ollama `qwen3.8:27b-mlx-bf16` (55 GB) or `qwen3.8:27b-mxfp8` (31 GB), **already present locally**; HF `Qwen/Qwen3.8-27B` (27.8B) | Apache-2.0 | **Ollama present locally.** Its `format` (JSON schema) is documented, but whether it constrains output for the `-mlx` tags is **unknown**. Validate every output in code either way | Own adapter (Ollama `/api/chat`, `format`, thinking off, temperature 0) | Already downloaded, so no extra weights. Tests whether a large general model rejects non-orders and overrides. A system comparison (generation + instructions), not a pure scale test |
| ref | **jeff + GLiFormer-large** (current) and **GLiFormer-base** | Baseline; cheap down-scale point within the encoder family | `knowledgator/gliformer-large-v1` (575.6M; local copy), `knowledgator/gliformer-base-v1` (264.2M) | Apache-2.0 | Local, measured (MPS) | `/v1/systemone` | No larger GLiFormer exists, so the encoder family cannot be scaled up. Base is the only other point |

## Considered, not shortlisted
| Candidate | Reason |
|---|---|
| Decider 0.8B–35B-A3B (`Mapika/decider-*`, Apache-2.0, `/v1/systemone`) | MPS documented only for dense 0.8B/2B; 4B/12B/35B on MPS unknown; per-size training stages differ. **Backup ladder** if Kev fails to run on MLX |
| Decider stock-instruct readouts (Gemma-4-12B/31B) | Strong hard-tier evidence, but MPS support is unknown for large models; overlaps the role of candidate 3 |
| Malkuth 2B/4B | CC-BY-NC-4.0, very new; Kev-derived (redundant) |
| Laya, Von, Verdict, open-jev-deberta | One size each; Laya/Von already show L2/L3/injection failures in issues; no scale ladder |
| GLiClass v3 (≤ 439M), GLiNER2.5-Decide 1B | Not larger in a useful way; the vendor shows 1B ≤ 340M; not `/v1/systemone` |
| Nimble-9B | Adapter + merge step, no `/v1/systemone`, tiny train set, uncalibrated latest checkpoint |
| jevmlx, AnyJev, mini-jev | jevmlx defaults to Qwen2.5 and flags batch drift on Qwen3-8B; AnyJev has no Apple Silicon path; mini-jev is a single model |
| Hosted Jev | Not local; useful only as an optional external reference (needs an API key and sends text out) |

## Ranking rationale
1. **Evidence on local failure types:**
   - Kev has injection, decline (When2Call) and unanswerable subsets by size.
   - Stock readers have hard-tier and abstain evidence.
   - General LLMs have injection evidence, plus NOTA counter-evidence.
2. **Reproducibility:**
   - Kev pins revisions and SHA-256 checksums.
   - Ollama models are already local.
   - The stock reader needs a readout decision.
3. **Setup effort:**
   - Kev: a new uv env plus downloads of about 30 GB for 4B + 9B (bases + adapters, estimate).
   - Qwen3.8-27B via Ollama: no download, needs only an adapter script.
   - Stock reader: a new env plus possibly a small reader script.
4. **Quality/latency:**
   - Author-measured on an M5: Kev-4B 721 ms per 5 questions, 136 ms cached. M3 Ultra numbers for one question are unknown.
   - 27B generation through Ollama is likely above 1 s per decision (not measured).

## Feasibility status (to confirm in the experiment's setup step)
| Item | Status |
|---|---|
| jeff on MPS | **tested locally** (p95 68–94 ms) |
| Kev-4B on MLX | documented (M5, author) — **not yet tested here** |
| Kev-9B on MLX | **expected, not measured** by the author |
| Kev-27B on MLX | expected to fit on a 96–128 GB Mac; not measured (~66 GB resident in bf16 on GPU) |
| Qwen3.5-4B reader on MPS/MLX | documented by SemIf (M5) — not tested here |
| Qwen3.5-9B reader on MPS/MLX | unknown |
| Ollama `qwen3.8:27b` JSON-schema output | runtime present; schema enforcement for MLX tags unknown; latency unknown |
