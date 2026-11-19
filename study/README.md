# Study: Jev and Jev-like ("System One" / decision) models

Literature survey as of **2026-10-01** (Jev launched 2026-09-15). Everything here was compiled from web sources (vendor pages, READMEs, HF cards, blogs, third-party evals). Nothing has been re-run locally yet. Each file distinguishes author/vendor claims from independent measurements; treat unlabelled numbers as claims.

## Directory layout

| Path | Contents |
|---|---|
| [close/](close/) | Hosted-only / closed-weight models (Jev itself and commercial rivals) |
| [open/](open/) | Open-weight or open-source, self-hostable models, frameworks and servers (one file per project; thin ones in [open/minor-projects.md](open/minor-projects.md)) |
| [landscape/](landscape/) | Prior art and adjacent technology that Jev-likes build on |
| [hype_and_reality/](hype_and_reality/README.md) | 2026-10-02 follow-up: failures like game_test/p2's, successful workload conditions, scale evidence, verified local candidates, proposed experiment |
| [statistically_correct/](statistically_correct/README.md) | 2026-10-06: cross-disciplinary literature survey on useful collective outcomes from imperfect decisions (54 cases, mechanisms, failure boundaries, Jev relevance) |
| [schooling_sim/](schooling_sim/README.md) | 2026-10-06 (episode set6 p2/pre1): targeted survey for a decision-model school with a predator (22 cases: schooling and predation models, metrics, perception, contagion, LLM swarms, spatial language) and the supported/contradicted/open list of p2 design choices |
| [benchmark/](benchmark/README.md) | 2026-10-02 (episode benchmark/p1): foundations of AI task evaluation (metrics, data validity, statistics, robustness, performance) and the decision checklist for the Jev-style benchmark design |
| [prompt_best_practice/](prompt_best_practice/README.md) | 2026-10-03 (episode study/prompt_best_practice/p1): prompt, option, order and second-pass knowledge for decision models, graded by readout, and a reinvention check of the lab's experiments |
| [recent_study/](recent_study/README.md) | 2026-10-08 (episode study/recent_study/p1): 111 arXiv papers on Jev-style decision models posted 2026-09-15 to 10-07 (42 read in full), a reinvention check of every lab experiment, and offline-first ideas for missing evidence, option rendering, order and populations |
| [recent_study_p3/](recent_study_p3/README.md) | 2026-10-19 (study/run-002): 70 further arXiv papers 10-08 to 10-16 (16 read in full), incl. 28 found only by non-`Jev` queries; order/option-set/fallback evidence, a reinvention-check addendum and ideas P1–P10 |
| [ecosystem/](ecosystem/) | Aggregators + master catalog (~600 rows), independent evaluations, tooling, reception |

Per-project files follow a common template: summary, approach, interface, training & data, reported performance, self-hosting notes, assessment, sources.

## What Jev is (one paragraph)

TypeSafe AI's Jev takes unstructured `state` plus a set of typed `questions` and returns typed answers with probabilities in one parallel pass, never generating free text. Three primitives: **noul** (yes/no → probability), **choice** (pick a key among ≤255 options → choice, confidence, per-option probs), **score** (ordered levels → expected score, per-level probs). Wire format `POST /v1/systemone` has become the de facto standard copied by competitors and clones. Claimed: transformer, "parallel sampler", trained on synthetic data with RLCD (RL for Calibrated Decisions), 70–500 ms, $0.042/MTok input, outputs free. No weights, paper, or parameter count. Details: [close/jev.md](close/jev.md).

## Taxonomy of Jev-likes

| Class | How it produces typed probs | Typical base | Representative projects |
|---|---|---|---|
| **A. Encoder + decision head** | Fine-tuned bidirectional encoder scores each option (option markers / GLiClass-style head) in one forward pass | ModernBERT, mmBERT, DeBERTa-v3, GLiNER2 (140–430M) | [Laya](open/laya.md), [Von](open/von.md), [Verdict](open/openjev-verdict.md), [Julia 1](open/julia-1.md), [WaterSheep](open/watersheep.md), [GLiNER2.5-Decide](open/gliner2-5-decide.md), [open-jev-deberta](open/open-jev-deberta-v3-large.md), [modernbert-ja-310m-jev](open/modernbert-ja-310m-jev.md) (Japanese) |
| **B. Zero-shot classifier wrappers** | Stock NLI / GLiClass zero-shot model behind a Jev API, no training | ModernBERT-NLI, GLiFormer | [jeff](open/jeff.md), [OpenDecision](open/opendecision.md), [poorjev](open/poorjev.md) |
| **C. Decoder LLM fine-tune** | LoRA/SFT so the next-token distribution over option letters/slots is the answer; temperature refit | Qwen3.5 0.8B–9B, Qwen3.8-27B, Gemma 4 | [Kev](open/kev.md), [Nimble](open/nimble.md), [Decider](open/decider.md), [JevK5](open/jevk5.md), [Tev1](open/tev1.md), [OpenThai-SystemOne](open/openthai-systemone.md), [NanoJev](open/nanojev.md), [AutoJev-27B](open/autojev-27b.md), [autotrust JEV-27B](open/autotrust-jev-27b.md), [Winnow-12B](open/winnow-12b.md), [Surogate Rune](open/surogate-rune.md), [Rizzo Flow](open/rizzo-flow.md), [CLM](open/clm.md) (frozen LLM + contrastive head) |
| **D. Training-free logit readers** | Read first-token logits of option letters (or option-text likelihood) from a stock LLM; share the state prefix KV cache across questions | Any Qwen/Gemma; vLLM / SGLang / MLX / HF | [SemIf](open/semif.md), [AnyJev](open/anyjev.md), [Simple Jev](open/simple-jev.md), [LitJev](open/litjev.md), [open-alternative-jev](open/open-alternative-jev.md), [openjev-sglang](open/openjev-sglang.md), [jevmlx](open/jevmlx.md), [jevfire](open/jevfire.md), [NotJev](open/notjev.md), [mini-jev](open/mini-jev.md), [Reflex](open/reflex.md), [jev-on-a-laptop](open/jev-on-a-laptop.md), [go-system-one](open/go-system-one.md), [JLDM](open/jldm.md), [Foq](open/foq.md) |
| **E. Diffusion-LM canvas read** | One masked slot per question in a discrete-diffusion canvas; one read-only denoise pass gives all distributions | DiffusionGemma 26B-A4B, LLaDA-MoE | [OpenJev (razorback16)](open/openjev-diffusiongemma.md), [dlm-jev family](open/dlm-jev-diffusiongemma.md), [kotoba typed-decisions](open/typed-decisions-kotoba.md) |
| **F. Tiny task specialists** | From-scratch option-attention models for one domain | <1M params | [CUA-S1-FORMS](open/cua-s1-forms.md), [Cua-S1 family](open/cua-s1.md), [jevlike](open/jevlike.md) |
| **G. RLCD reproductions** | RL with proper-scoring rewards on decisions | Qwen2.5-0.5B | [rlcd-lite](open/rlcd-lite.md) (no working full repro exists; see also NanoJev and Decider) |

Closed rivals: [Solar Decide](close/solar-decide.md) (Upstage), [Liquid d1](close/liquid-d1.md), [Span-01](close/respan-span-01.md) (Respan), [OpenAI Decisions API](close/openai-decisions-api.md) (preview 2026-09-29), [Decider 1](close/state-decider-1.md) (meraGPT, unrelated to open Decider), [Trio-Spark](close/trio-spark.md).

Note on overlapping files: `cua-s1.md` (family) vs `cua-s1-forms.md` (the forms model in depth); `openjev-diffusiongemma.md` (the razorback16 server) vs `dlm-jev-diffusiongemma.md` (the broader DiffusionGemma family + the one trained LoRA).

## Key findings

1. **The interface is the product; the mechanism is reproducible.** Replicas appeared within 1–4 days. Any LLM's option logits, an encoder head, or a diffusion canvas can serve `/v1/systemone`. TypeSafe's founder reportedly agreed it is "basically a zero-shot classifier". The real novelty is a runtime-defined, schema-safe classification primitive. ([ecosystem/reception.md](ecosystem/reception.md), [landscape/](landscape/))
2. **Vendor numbers are not confirmed independently.**
   - Speed: third-party tests find Jev ~3–9x faster than LLMs, against the claimed 193.6x.
   - Cost: the saving ranges from 4x to 580x depending on which model it is compared with.
   - Accuracy: Jev roughly matches cheap LLMs, not frontier ones. ([ecosystem/evaluations.md](ecosystem/evaluations.md))
3. **"Calibrated" means something only within the training distribution.**
   - Jev: ECE is ~0.02–0.03 on public QA sets. It reaches 0.08–0.33 on organisation-specific rules, ranking, and the `score` type.
   - Output is quantised to 0.01, and many answers are exactly 0 or 1.
   - Most open clones ship uncalibrated or overconfident and rely on post-hoc temperature scaling.
   - Nobody ships conformal abstention yet. ([landscape/calibration.md](landscape/calibration.md))
4. **"RLCD" has not been reproduced.** Clones use cross-entropy (sometimes plus Brier loss) and one fitted temperature. The few RL attempts (NanoJev, Decider v10, rlcd-lite) found no clear gain over cross-entropy, and found a Brier-only reward exploitable. The closest published analogue is RLCR (arXiv 2507.16806).
5. **Scale and the base model dominate quality.**
   - On JevBench, small encoders (Laya/Von/jeff, ~400M) score Intelligence ~34–37 vs Jev 53.
   - Fine-tuned 4B LLMs (Imajev-4B, Plumb-4B, decider-4b) rank above Jev 1.13 overall. Treat with caution: that board's author is also a vendor.
   - DiffusionGemma 26B reaches ~81–88% on Jev-style evals, against ~48% for a 151M encoder.
   - Encoders win on latency (10–35 ms) but fail zero-shot out of distribution: Laya scored 40.3% on an adversarial set.
6. **Standard engineering levers:**
   - Shared-prefix KV caching (one state, many questions).
   - Option-order permutation averaging against position bias.
   - Per-question-type temperature.
   - A local-first cascade: a small model answers and escalates to Jev below a confidence threshold. One study matched Jev's accuracy at 1.8x speed this way.
7. **Hype lifecycle.**
   - New repo creation peaked on 09-22 (~127/day) and is now ~25–35/day.
   - There are 36+ awesome lists and many AI-generated, scaffold-only repos.
   - Discussion has moved on to benchmarks: JevBench, typed-decision-bench, jev-benchmarks, and the "Jev in the Wild" survey (arXiv 2609.30216). ([ecosystem/aggregators.md](ecosystem/aggregators.md))
8. **Academic follow-up (to 2026-10-07).**
   - 111 arXiv papers appeared in three weeks, most of them using or evaluating hosted Jev.
   - Several independently reproduce lab findings:
     - a second pass on a one-pass scorer is the renormalised first pass;
     - models decide anyway on missing evidence;
     - copies of one model share their errors.
   - Option labels rendered as `"{label}: {definition}"` can override the definitions.
   - RLCD has not beaten cross-entropy for one-pass scorers.
   - Details: [recent_study/](recent_study/README.md) and [recent_study/reinvention-check.md](recent_study/reinvention-check.md).

## Suggested starting points for lab/

- **Baselines to stand up locally:**
  - Class D: SemIf or Simple Jev on Qwen3.5-4B. Cheapest, and the strongest "is training even needed?" baseline.
  - Class A: Laya or Von. Fast encoder reference.
  - Class C: Kev-4B or JevK5. Fine-tuned LLM reference.
  - Class E (optional, needs a large GPU): OpenJev / DiffusionGemma.
- **Eval harnesses to reuse:**
  - typed-decision-bench (kyr0): 27.6k cases with calibrate/train/test splits.
  - JevBench (Benchmark Heaven).
  - The gate-style calibration checks in jev-orderby-bench and jev-ood-calibration.
- **Open questions worth experiments:**
  - Per-type calibration, especially `score`.
  - Japanese/multilingual performance (see [modernbert-ja-310m-jev](open/modernbert-ja-310m-jev.md)).
  - Letter-logit vs option-text-likelihood readout: mini-jev and jevmlx reach conflicting results.
  - RLCD-style training vs cross-entropy plus temperature.
  - Cascade thresholds.
- **Caveats when citing:**
  - Most numbers are self-reported on the author's home-turf tasks.
  - Some classic paper IDs in `landscape/` were written from memory and are marked as such; verify them before citing.
  - A few sources conflict (dates, context sizes, Tev1's open/closed status); see the individual files.
