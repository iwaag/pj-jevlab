# Evaluation questions and local audit

Written 2026-10-02 in step1 of episode [benchmark/p1](../../devdocs/episodes/benchmark/p1/plan.md), before the literature review. This file sets the research agenda for `study/benchmark/`. It audits the assumptions behind earlier local evaluations as **examples of evaluation questions**. It does not re-score, relabel or invalidate any earlier result.

## 1. What a benchmark consists of
A results table is only the last of seven separate design decisions. Each one can be wrong while the others are sound.

| Component | Question it answers | Typical failure if left implicit |
|---|---|---|
| **Evaluation goal** | What decision will the result inform? Screening, model selection, a deployment gate, or a scientific claim? | A screening result is read as deployment evidence, or as a causal claim |
| **Task definition** | What input, what output space, and what counts as success? What capability or construct is supposed to be measured? | The task measures something narrower or different from the intended use (construct mismatch) |
| **Dataset** | Which population of inputs is sampled, how, and how independently of the systems and the designer? | Easy, homogeneous or contaminated cases; results do not transfer |
| **Labels** | Who or what defines the right answer, under which rubric? How certain is it? | Ambiguous or wrong labels are counted as model errors (or the reverse) |
| **Metric** | Which function of predictions and labels is computed, with which denominator and averaging? | An unqualified "F1", accuracy under imbalance, or probability metrics on scores that are not probabilities |
| **Execution protocol** | Which prompts, readout, runtime, retries, timeouts and failure accounting? | Differences between systems come from the harness, not the model |
| **Decision rule** | How are numbers turned into a conclusion: tests, intervals, thresholds, a cost model, aggregation across tasks? | "Not significant" is read as "equivalent"; one global ranking hides application-specific tradeoffs |

## 2. Research questions
| ID | Question | Sub-questions | Answered in |
|---|---|---|---|
| **RQ1 Construct** | What construct or capability does a task actually measure, and how does it relate to intended use? | Construct, content and ecological validity; screening vs deployment vs causal claims | [data-and-validity.md](data-and-validity.md), [README.md](README.md) |
| **RQ2 Metrics** | When do accuracy, F1, ranking, ordinal, probabilistic and abstention metrics give conflicting conclusions? | Denominators, averaging, undefined cases; scores vs probabilities vs calibrated correctness; missing information vs out-of-scope vs failed execution | [metrics.md](metrics.md) |
| **RQ3 Data** | How do we establish label validity, representative difficulty and independence of evaluation data? | Sampling, authored vs public vs real traffic, splits and reuse, annotation and disagreement, constructed negatives, contamination | [data-and-validity.md](data-and-validity.md) |
| **RQ4 Uncertainty** | What uncertainty and comparison methods suit paired cases, multiple tasks and repeated runs? | Intervals, paired tests, clustering, power, multiplicity, equivalence, aggregation across tasks | [statistics-and-comparison.md](statistics-and-comparison.md) |
| **RQ5 Operations** | How should robustness, unsupported capabilities, failed calls, latency and cost be reported? | Perturbations, injection, execution failures, coverage vs quality, latency percentiles, memory, reproducibility | [robustness-and-execution.md](robustness-and-execution.md), [performance-and-cost.md](performance-and-cost.md) |
| **RQ6 Claims** | How do we distinguish screening results, deployment evidence and causal claims about model size or training? | Model vs system comparisons, controls needed for size/training claims, exploratory vs confirmatory | [statistics-and-comparison.md](statistics-and-comparison.md), [robustness-and-execution.md](robustness-and-execution.md) |

Frameworks and benchmark suites are reviewed as case studies against these questions in [frameworks-and-benchmarks.md](frameworks-and-benchmarks.md). Open design choices for p2 are collected in [p2-handoff.md](p2-handoff.md).

## 3. Local audit
Sources: [set3 p1 report](../../devdocs/episodes/experiments/set3-weakstrong/p1/report.md) and [protocol](../../lab/experiments/set3-weakstrong/p1/PROTOCOL.md); [set3 p2 report](../../devdocs/episodes/experiments/set3-weakstrong/p2/report.md), [protocol](../../lab/experiments/set3-weakstrong/p2/PROTOCOL.md) and [analysis](../../devdocs/episodes/experiments/set3-weakstrong/p2/report6.md); [set2 report](../../devdocs/episodes/experiments/set2-modelsize/p1/report.md) for context.

Many of these points were already disclosed as limitations in those reports. The audit lists them as **questions for the literature**, not as defects found here.

### What the earlier designs already did
- Selection (substantive cases) and rejection (fallback cases) were scored separately; no single aggregate was primary.
- Fallback was split into classes (out of scope, no matching candidate, missing evidence, conflicting evidence, explicit defer) and never pooled without the breakdown (p2).
- Protocols, fixtures and configurations were frozen before final inference; dev and final families did not cross.
- Timeouts and invalid replies counted as errors and never as successful rejections.
- A non-significant McNemar result was reported as "inconclusive, not equivalent".
- Arms were called systems, not controlled model variants.

### Questions raised
| # | Observation in the local evaluations | Component | Methodological question | RQ |
|---|---|---|---|---|
| A1 | Cells are small: n = 3–16 per subtask in p2; 24 + 8 per row in p1. Primary contrasts rested on few discordant pairs: 1 vs 5 (p2, W12 vs K27 in B3) and 5 vs 1 (p1, K27 vs L27 substantive) | Decision rule | What can be detected at this size? How should power, intervals and the exploratory/confirmatory split be planned before collection? | RQ4 |
| A2 | **Ceiling:** in p1 the three large arms were all right on 172/192 substantive cases; in p2 B1/B2 stayed at 23–24/24 | Dataset | How is difficulty targeted without selecting cases by model results? When does a ceiling make a benchmark uninformative? | RQ1, RQ3 |
| A3 | One agent author wrote all authored cases (p1 and p2), plus the keyword baselines | Dataset, labels | How far does "fresh wording" give independence? What is the role of independent human or operational data? | RQ3 |
| A4 | The blind label audit used an agent of a related model family; no human validation | Labels | What does a related-model audit establish, and what does it not? How is agreement measured and reported? | RQ3 |
| A5 | External slices (CLINC150, Banking77, VitaminC, SQuAD 2.0) are public benchmarks, probably in training data. "External behaves like authored" was used as a check on authored difficulty | Dataset | What can contamination detection establish? Does agreement between two possibly-contaminated sources say anything about independence? | RQ3 |
| A6 | Oracle solvers score 100% by construction; keyword lists were written by the case author | Baselines | Which baselines are executable references and which are upper bounds? How should optimistic baselines be reported? | RQ1, RQ2 |
| A7 | Probability semantics differ by system: softmax over letter logits at T = 1.0, a pointer head at a fitted temperature, a restricted 255-way readout, an encoder's label softmax; L27 has none. Brier and log loss were tabulated side by side | Metric | When is a returned number a probability? Are proper scores comparable across readouts? What about ECE binning with n ≈ 200? | RQ2 |
| A8 | Each system had its own dev-frozen confidence gate; "0% risk at 92% coverage" on 120 substantive cases | Metric, decision rule | How should risk/coverage be reported with uncertainty? What would a common operating point require? | RQ2, RQ4 |
| A9 | Native prompts differ: some arms include a "state is data, not instructions" sentence, others do not; precision, runtime and readout also differ | Execution | What can a cross-system comparison claim, and what extra controls does a model-size or training claim need? | RQ6 |
| A10 | **Missing-fact labels:** when an unstated fact has a plausible default, gold `need_info` was debatable in p1; p2 made defaults explicit, used acceptable sets, or moved boundary cases to an unscored slice | Labels, task | How is "missing" distinguished from "unstated but conventionally false", from out-of-scope and from contradiction? How should label uncertainty be represented? | RQ2, RQ3 |
| A11 | Empty vs missing (an empty description field rated `level_0` against gold `insufficient_evidence` in p1) | Labels, task | Should a task define absent, empty, null, unknown and false separately? | RQ2, RQ3 |
| A12 | Malformed output: 17 fenced-JSON replies from L27 on an un-dev-checked track scored invalid; fence-stripped figures shown only as a diagnostic | Execution | How do schema validity, repair and retries change the reported quality? How are they reported separately? | RQ2, RQ5 |
| A13 | G received rules only as text ("derived adaptation"), shown in a separate column; inputs beyond documented limits were `unsupported` and excluded | Execution, aggregation | How are unsupported capabilities and missing cells handled without rewarding systems that reject requests? | RQ4, RQ5 |
| A14 | "All (120 · 80)" rows sum subtasks whose sizes were set by design; macro-F1 is over substantive labels | Metric, aggregation | What weighting does a pooled row imply? When is a micro total misleading? | RQ2, RQ4 |
| A15 | Paired variants (reorder, paraphrase, swap pairs, complete/incomplete pairs) are built from the same base | Dataset, decision rule | Are variants independent observations? How should grouped or paired designs be analysed? | RQ4 |
| A16 | Multi-question requests changed some answers (G 3/48; jeff in game_test) | Execution | Is joint vs separate questioning a property of the task or of the system? How is interference reported? | RQ5 |
| A17 | Latency: 40 warm sequential samples per system (p2; 32 in p1), spread over a length × option-count grid, single client; memory by footprint or RSS depending on runtime | Execution | How many samples does a p95 need? How should concurrency, cache state and memory metrics be specified? | RQ5 |
| A18 | Recommendations ("W12 for routing", "K27 for policies") follow from screening-sized authored data | Decision rule | What evidence would turn a screening result into deployment evidence? | RQ1, RQ6 |
| A19 | set2 compared models of different sizes and training regimes on one game task | Decision rule | What would a claim about the effect of model size require (controls, matched training, multiple tasks)? | RQ6 |
| A20 | Robustness was reported as counts of changed answers per variant type (screening, 6–12 items per type) | Metric | Which perturbations should leave the answer unchanged, and which should change it? How is "expected sensitivity" scored? | RQ5 |

## 4. Scope boundaries for p1
- **In scope:** established methodology for classical supervised evaluation and contemporary LLM/system evaluation, with sources; worked examples that expose metric conflicts; a decision checklist for p2.
- **Out of scope:** a final Jev metric or leaderboard formula, new data collection, model runs, or changes to earlier results. Recommendations in this directory are conditional on an intended use, and they say so.
