# Evaluation frameworks and benchmarks: case studies

A bounded comparison of established suites and tools, and what transfers to evaluating decision models (typed `choice` / `noul` / `score` questions over free-text state). Written 2026-10-02 in step6 of [benchmark/p1](../../devdocs/episodes/benchmark/p1/plan.md).
- Citations link to [evidence/](evidence/).
- Statements about each artefact's scope, version and licence come from its paper or official repository, as recorded in the evidence entry.
- **Performance claims inside these papers are benchmark-author claims.**
- **"Lesson" columns are inference made for this note (derived here).**

## 1. Four different things called "a benchmark"
| Role | What it is | Examples here | What its existence does *not* establish |
|---|---|---|---|
| **Dataset / benchmark** | Fixed items, labels and a metric | MMLU, CLINC150, SQuAD 2.0, FEVER, BEIR, WILDS | That its construct matches your use; that its labels are right; that it is unseen by the models |
| **Execution harness** | Software that runs systems on tasks and scores them | lm-evaluation-harness, HELM, Inspect, simple-evals, MTEB's package, MLPerf LoadGen | That its default prompt, readout or parser is neutral; supporting a metric does not validate that metric for every task |
| **Analysis or test tool** | Generates tests or quantifies sensitivity and uncertainty | CheckList, FormatSpread, Inspect's stderr/Wilson metrics, rliable-style summaries | That the tests sample a population; failure rates are not accuracies |
| **Methodology / protocol** | Rules for how to measure | HELM's multi-metric design, MLPerf scenarios and early stopping, CheckList's test types, preregistration | That a given implementation follows it |

A framework that computes a metric does not make that metric appropriate. Appropriateness is a validity question ([data-and-validity.md](data-and-validity.md)).

## 2. Case studies
| Artefact | Role | Purpose and coverage | Metric and protocol | Reproducibility | Known gaps | Lesson for decision-model evaluation (derived here) |
|---|---|---|---|---|---|---|
| **GLUE / SuperGLUE** [wang2019glue](evidence/F-robustness-frameworks-perf.md#wang2019glue) [wang2019superglue](evidence/F-robustness-frameworks-perf.md#wang2019superglue) | Dataset suites + leaderboard + diagnostic set | General English NLU; GLUE has 9 tasks; SuperGLUE added harder tasks, with a licence criterion, after GLUE was surpassed | Macro average of task scores; multi-metric tasks averaged first; hidden test labels; server submission | Fixed data; hidden test limits overfitting | Saturated; one number averages different metrics; many WNLI submissions predicted the majority class | Hidden test labels protect a final set. A single average invites gaming. Report the trivial baselines |
| **BIG-bench** [srivastava2023bigbench](evidence/F-robustness-frameworks-perf.md#srivastava2023bigbench) | Dataset suite | 204 tasks; Lite = 24-task subset | Per-task preferred metric normalised to 0–100; canary GUID string to keep it out of training data | Repository archived | Heterogeneous tasks; some "breakthroughs" come from brittle metrics | A canary string and a fixed canonical subset are cheap and useful. Normalisation hides metric differences |
| **MMLU** [hendrycks2021mmlu](evidence/F-robustness-frameworks-perf.md#hendrycks2021mmlu) and **MMLU-Redux** [gema2025mmlu](evidence/F-robustness-frameworks-perf.md#gema2025mmlu) | Dataset; dataset audit | 57 subjects, 14,079 test questions, 4 options | Accuracy; official score is a micro average over items [biderman2024lessons](evidence/F-robustness-frameworks-perf.md#biderman2024lessons) | Three implementations gave LLaMA-65B 0.637 / 0.488 / 0.636 [fourrier2023hfmmlu](evidence/F-robustness-frameworks-perf.md#fourrier2023hfmmlu) | ~6.49% erroneous questions, 57% in Virology; rankings change on corrected labels [gema2025mmlu](evidence/F-robustness-frameworks-perf.md#gema2025mmlu) | Readout (letter probability, generated letter, full-answer likelihood) is part of the system. Audit labels. State micro vs macro |
| **HELM** [liang2023helm](evidence/F-robustness-frameworks-perf.md#liang2023helm) | Harness + suite + methodology | 16 core scenarios, 30 models; 7 metric families | Accuracy, calibration (ECE-10, selective accuracy), robustness (worst case over invariance and equivariance perturbations), fairness, bias, toxicity, efficiency (denoised and idealised runtime) | Raw prompts and completions released; versioned ("living") | Its MMLU implementation was one of the divergent three; numbers depend on version | The template for reporting more than accuracy. Separate invariance from equivariance. Report efficiency with its hardware context |
| **lm-evaluation-harness** [biderman2024lessons](evidence/F-robustness-frameworks-perf.md#biderman2024lessons) [lmeval_harness_filters](evidence/C-judging-structured.md#lmeval_harness_filters) | Harness | Many tasks via configuration files | Task metrics with bootstrap SE; filters (strict vs flexible extraction); unparseable → `[invalid]` (wrong) | Configs, `--log_samples`, release versions | Defaults reflect base-model log-likelihood evaluation | Log every sample. Name the extraction pipeline. Count invalid as wrong |
| **Inspect** [inspect-docs](evidence/F-robustness-frameworks-perf.md#inspect-docs) | Harness | Dataset → solver → scorer; agents and tools | stderr with clustering, bootstrap, Wilson interval, Krippendorff α, epochs (repeats) | Open source; fast-moving docs (cite the version) | — | Clustered SE, Wilson intervals and repeats as first-class metrics are exactly what small decision benchmarks need |
| **simple-evals** [openai-simple-evals](evidence/F-robustness-frameworks-perf.md#openai-simple-evals) | Reference harness (vendor) | Zero-shot chain-of-thought prompts | "Evals are sensitive to prompting" | No longer updated for new models (July 2025) | Vendor framing | Prompt protocol is a choice of construct, not a neutral default |
| **BEIR** [thakur2021beir](evidence/A-metrics.md#thakur2021beir) | Dataset suite + framework | 18 zero-shot retrieval datasets | nDCG@10 via trec_eval | Code and data public | Pooled judgments favour lexical systems; filling holes reversed a ranking | The candidate pool and judgment completeness are part of the benchmark |
| **MTEB** [muennighoff2023mteb](evidence/F-robustness-frameworks-perf.md#muennighoff2023mteb) | Suite + harness + leaderboard | 8 task types, 58 datasets (paper version) | One main metric per task type, averaged | Live package and leaderboard have grown since the paper | Averages heterogeneous metrics; paper ≠ current leaderboard | No method dominated across tasks. Per-task reporting matters more than the average |
| **WILDS** [koh2021wilds](evidence/F-robustness-frameworks-perf.md#koh2021wilds) | Dataset suite + package | 10 natural distribution shifts | In-distribution average vs out-of-distribution worst-group or worst-domain | Package and splits fixed | Using OOD validation data for model selection is a protocol choice | Report the worst slice next to the average. State whether shift data was used for tuning |
| **CheckList** [ribeiro2020checklist](evidence/D-data-validity.md#ribeiro2020checklist) | Methodology + test generator | Capability × test-type matrix | MFT / INV / DIR failure rates | Templates shareable | Failure rates are not population accuracies; templates reflect tester assumptions | Behaviour tests per capability, with explicit invariance and direction expectations |
| **FEVER** [thorne2018fever](evidence/F-robustness-frameworks-perf.md#thorne2018fever) | Dataset + scoring protocol | 185,445 claims; Supported / Refuted / NotEnoughInfo | A verdict counts only with the correct evidence set; best pipeline 31.87% with evidence vs 50.91% without | Public data and scorer | Data licence not confirmed here; synthetic claim mutations | Requiring the *reason* (evidence) changes scores a lot. "Not enough info" is a first-class label |
| **CLINC150** [larson2019clinc](evidence/F-robustness-frameworks-perf.md#larson2019clinc) | Dataset | 150 intents + out-of-scope queries | In-scope accuracy + out-of-scope recall, reported separately | Public (CC BY 3.0) | Only ~69% of OOS-prompted queries were actually OOS; threshold tuned on validation data that contains OOS | Report selection and rejection separately. Out-of-scope data must be verified, not assumed |
| **SQuAD 2.0** [rajpurkar2018squad2](evidence/B-probability-abstention.md#rajpurkar2018squad2) | Dataset | Adversarially written unanswerable questions | EM/F1; abstaining scores 1 on unanswerable items; always-abstain baseline 48.9 F1 | Official script; hidden test set | The script skips missing predictions [squad_eval_scripts](evidence/C-judging-structured.md#squad_eval_scripts) | Always report the trivial abstention baseline. Check how missing outputs are handled |
| **Chatbot Arena** [chiang2024arena](evidence/C-judging-structured.md#chiang2024arena) | Platform + methodology | Crowd pairwise preferences | Bradley–Terry with robust intervals (moved from Elo) | Votes partly released | Self-selected users and prompts; no absolute quality | Pairwise preference needs a statistical model and intervals. It measures preference, not correctness |
| **MLPerf Inference** [reddi2020mlperf](evidence/F-robustness-frameworks-perf.md#reddi2020mlperf) [mlperf-rules](evidence/F-robustness-frameworks-perf.md#mlperf-rules) | Methodology + benchmark + LoadGen | Scenario-based latency and throughput | Single-stream p90, server tail bound, offline throughput; quality ≥ fixed share of the reference; early stopping | Submissions must list all software and hardware | Data-centre and edge oriented | Define the load scenario first. Percentiles need enough samples. Quality floor plus performance, not a blended score |

## 3. What transfers, and what does not
- **Transfers well** (derived here):
  - separate selection and rejection metrics (CLINC150);
  - hidden or frozen final sets (GLUE);
  - canary strings (BIG-bench);
  - invariance vs directional tests (CheckList, HELM);
  - worst-slice reporting (WILDS);
  - requiring evidence for verdicts (FEVER);
  - trivial-policy baselines (SQuAD 2.0);
  - per-sample logs and named extraction (lm-eval);
  - clustered intervals and repeats (Inspect);
  - scenario-first performance measurement (MLPerf).
- **Does not transfer directly:**
  - **Generation-oriented parsing rules.** A typed decision interface returns a key, so parsing matters only for systems that answer in free text or JSON.
  - **Leaderboard averaging.** Decision workloads differ by application.
  - **Preference arenas.** Decision tasks usually have a checkable gold.
- **Typed decision interfaces need things none of these suites provide** (derived here):
  - scoring of per-option probabilities whose semantics differ by readout;
  - typed fallback classes (out of scope, no matching candidate, missing evidence, conflicting evidence);
  - joint vs separate multi-question requests;
  - a rule for unstated defaults.

  These are design decisions for p2 ([p2-handoff.md](p2-handoff.md)).

## 4. Worked conflicts
Each example shows two defensible readings of the same results. The numbers marked "local" come from earlier episodes in this repository and are quoted as illustrations, not re-analysed.

**1. High accuracy with poor minority recall.**
- On 95 negatives and 5 positives, a constant "negative" predictor has accuracy 0.95, macro F1 0.49 and minority recall 0.
- In a three-class 80/15/5 example, accuracy is 0.90 and macro F1 0.58 (derived; [metrics.md §1](metrics.md)).
- **Reading:** a pooled accuracy over a test set dominated by one class says little about rare but important classes. Rare classes include the fallback classes.

**2. High rejection caused by fallback bias.**
- A system that always picks the fallback option has fallback recall 1.0 and substantive accuracy 0 (derived; metrics.md, worked example 8).
- **Local:** in set3/p1, jeff looked strong at rejection on two rows, but it falsely rejected 18/24 and 16/24 substantive cases there ([set3 p1 report](../../devdocs/episodes/experiments/set3-weakstrong/p1/report.md)).
- **Reading:** rejection metrics need their counterpart, the false-rejection rate on substantive cases, from the same system.

**3. Calibrated probabilities with low useful coverage.**
- A system that outputs 0.6 on 80% of cases and 0.95 on 20% can be perfectly calibrated. At a 0.9 confidence threshold it covers only 20% of cases, at 5% risk (derived; metrics.md, worked example 9).
- **Reading:** calibration (absolute values) and selective usefulness (ordering, sharpness) are different properties [kamath2020selective](evidence/B-probability-abstention.md#kamath2020selective) [kumar2019verified](evidence/B-probability-abstention.md#kumar2019verified). A "well-calibrated" verdict does not show that a confidence gate is useful.

**4. Valid JSON with incorrect meaning.**
- `{"choice": "approve"}` passes a strict schema whose enum contains `approve`, whatever the gold is.
- Structured-output guarantees cover syntax and schema only, and schema-valid output "can still contain mistakes" [openai_structured_outputs](evidence/C-judging-structured.md#openai_structured_outputs).
- A constrained decoder fixes the format, while the content can still change with the constraint [tam2024speakfreely](evidence/C-judging-structured.md#tam2024speakfreely) [geng2025jsonschemabench](evidence/C-judging-structured.md#geng2025jsonschemabench).
- **Reading:** report validity and correctness separately, and never treat "100% valid" as a quality result.

**5. Strong synthetic results with weak independent validation.**
- **Independent replications show drops:**
  - re-creating ImageNet by the original process lowered accuracy by 11–14% [recht2019imagenet](evidence/D-data-validity.md#recht2019imagenet);
  - a matched fresh GSM8K-style set (vendor-produced, Scale AI) showed drops of up to 8% for some model families [zhang2024gsm1k](evidence/D-data-validity.md#zhang2024gsm1k).
- **Local:** in set3/p2, the large systems scored similarly on authored and on public external slices ([set3 p2 report](../../devdocs/episodes/experiments/set3-weakstrong/p2/report.md)).
  - The comparison is confounded by subtask mix and ceiling. The 65 external items sat only in the classification, matching and passage-answering bundles, where the large systems scored 36–38/38. The bundles where systems separated (rules and policies, rubrics) had no external items. So it shows only that the external items were no harder in those bundles.
  - It does not show independence, because both sources may be familiar to the models, and the authored cases share one author ([data-and-validity.md §3](data-and-validity.md)).
- **Reading:** independent human or operational data is the missing evidence, not more authored cases.
