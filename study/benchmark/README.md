# Study: foundations of AI task evaluation

Literature review as of **2026-10-02**, written in episode [benchmark/p1](../../devdocs/episodes/benchmark/p1/plan.md). It revisits what an evaluation can establish, how metrics relate to tasks, and how data, uncertainty and implementation shape conclusions. It prepares p2, which will design a benchmark for Jev-style decision models: typed `choice` / `noul` / `score` questions over free-text state.

- **Sources:** about 200 sources, indexed in [sources.md](sources.md), with how far each was read in [evidence/](evidence/) and the search in [search-log.md](search-log.md).
- **No models were run** for this study, and no numbers were reproduced locally.
- **Claims are labelled.** A claim is either attributed to a source at its verification level, labelled as a benchmark-author or vendor claim, or marked "(derived here)".

## Files
| File | Contents |
|---|---|
| [questions-and-audit.md](questions-and-audit.md) | What a benchmark consists of (seven components), research questions RQ1–RQ6, audit of earlier local evaluations (A1–A20) |
| [metrics.md](metrics.md) | Metric reference for ten families; reporting rules; outcome accounting; scores vs probabilities; tradeoffs that need an intended use; worked conflicts |
| [data-and-validity.md](data-and-validity.md) | Validity, sampling and difficulty; data sources; splits and reuse; labels and annotation; negatives and minimal pairs; shortcuts; shift; contamination; licensing |
| [statistics-and-comparison.md](statistics-and-comparison.md) | Sources of variance; intervals; paired tests; clustering; power; multiplicity; equivalence; claim types; aggregation across tasks |
| [robustness-and-execution.md](robustness-and-execution.md) | Invariance vs directional tests; prompt, format and option effects; injection; multi-question; model vs system; failure accounting |
| [performance-and-cost.md](performance-and-cost.md) | Load scenarios; LLM latency metrics; cold/warm and caches; percentile sample sizes; throughput; memory; reproducible configuration; cost |
| [frameworks-and-benchmarks.md](frameworks-and-benchmarks.md) | Dataset vs harness vs analysis tool vs methodology; 16 case studies; what transfers; five worked conflicts |
| [p2-handoff.md](p2-handoff.md) | Decision checklist for p2 (A1–A9), lessons from earlier local evaluations, evidence still missing |
| [sources.md](sources.md), [search-log.md](search-log.md), [evidence/](evidence/) | Source index, search record, annotated evidence |
| [tools/](tools/) | Scripts that built the evidence files and resolve citations |

## Synthesis by question
### RQ1. What does a task measure, and how does it relate to intended use?
- **A benchmark is seven decisions, not a table:** goal, task, data, labels, metric, execution protocol and decision rule ([questions-and-audit.md](questions-and-audit.md)).
- **A score operationalises a construct.**
  - Validity belongs to an interpretation in a context, and has to be re-examined when a dataset is reused ([data-and-validity.md §1](data-and-validity.md)).
  - In a review of 445 LLM benchmarks, only 53% justified their validity and only 16% used any statistical test.
- **Ecological validity needs natural data.** Authored and crowd-written cases need convergent evidence from natural data before deployment claims.

### RQ2. When do metrics disagree?
They disagree routinely; [metrics.md](metrics.md) has worked examples. Common cases:
- accuracy vs macro metrics under imbalance;
- two definitions of macro F1;
- ROC vs PR under low prevalence, where the preferred choice is contested;
- accuracy vs proper scores;
- exact vs within-one on ordinal labels;
- calibration vs useful coverage.

**Name every denominator, averaging and zero-division convention.**

**Rejection is not one thing.**
- Out-of-scope input, no matching candidate, missing evidence, conflicting evidence and execution failure are different outcomes.
- **Answerability, correctness confidence and distribution shift** are three different questions.
- **Execution errors never count as rejections.**

**Probabilities from different readouts are not interchangeable.** A proper score is valid per system; risk–coverage curves compare more safely across systems.

**No universal aggregate exists.** False-acceptance vs false-rejection cost, macro vs micro, coverage vs risk and quality vs resources all need an intended use ([metrics.md §13](metrics.md)).

### RQ3. How are label validity, difficulty and independence established?
- **Independence is a property of the process,** not of fresh wording ([data-and-validity.md §3](data-and-validity.md)). It depends on who designed, wrote and labelled the data, and whether evaluated systems or their relatives took part.
- **Labels:**
  - tie them to a rubric, evidence or a rule;
  - measure chance-corrected agreement with independent annotators;
  - treat disagreement as information (acceptable sets, soft labels, exploratory slices).
- **A related-model audit is not human validation.**
- **Difficulty should come from design features fixed before running systems,** not from selecting cases that a candidate fails.
- **Contamination checks have known blind spots,** and rephrased contamination evades all of them. Never call a dataset clean without stating the checks.

### RQ4. What uncertainty methods fit paired cases, multiple tasks and repeated runs?
- **Small cells:** use Wilson or Clopper–Pearson intervals, not Wald or CLT.
- **Paired comparisons:** mid-p McNemar or permutation tests. Use the bootstrap only with enough items. Report the difference with its interval ([statistics-and-comparison.md](statistics-and-comparison.md)).
- **Variants of one base are clustered:** analyse per base, or with clustered or cluster-bootstrap methods.
- **Plan power before collecting.** With about 10% discordance, 24 paired cases detect only about 16-point differences.
- **"Not significant" is inconclusive** unless a prespecified equivalence margin is met.
- **Aggregates across tasks are unstable** and hide tradeoffs. Use per-task results first, a common supported subset, and coverage reported beside quality.

### RQ5. How should robustness, unsupported capabilities, failures, latency and cost be reported?
- **Robustness tests:**
  - pair invariance tests with directional (meaning-changing) tests;
  - control option order and prompt family;
  - separate injected instructions inside content from direct requests ([robustness-and-execution.md](robustness-and-execution.md)).
- **Failures:** keep unsupported, setup failure, timeout, invalid, truncation and repair as separate categories. Report coverage beside quality.
- **Performance:**
  - define the load scenario before the latency metric ([performance-and-cost.md](performance-and-cost.md));
  - a distribution-free p95 interval needs at least 59 samples (one-sided-like [min, max]) or 72 (equal-tailed), and p99 at least 299 or 368;
  - use one memory counter for all systems;
  - record the full configuration.

### RQ6. Screening vs deployment evidence vs causal claims
- **A comparison of systems that differ in base model, training, precision, runtime, readout and prompt is a system comparison.** It does not support claims about model size or training.
- **Deployment evidence** needs representative data, the application's operating point and costs, and upper bounds on error rates ([statistics-and-comparison.md §8](statistics-and-comparison.md), [robustness-and-execution.md §6](robustness-and-execution.md)).

## Corrections to earlier working assumptions
These revise how earlier local evaluations were *framed*, not their recorded results. Details are in [p2-handoff.md Part B](p2-handoff.md).
1. **Cell sizes.** Cells of 3–24 cases are screening evidence. A 5-to-0 discordant split gives exact p = 0.06 and mid-p = 0.03; neither survives a Holm correction over ten comparisons.
2. **"0% risk at ~90% coverage" on about a hundred cases** has a 95% upper bound near 3%. It should be reported with that bound.
3. **"External slices behave like authored ones"** is confounded: the external items sat only in the classification, matching and passage bundles, at or near ceiling, while the bundles where systems separated (rules, rubrics) had none. It shows the external items were no harder there; it says nothing about the difficulty of the other bundles, and it does not show independence.
4. **A blind label audit by a related model** shows consistency, not validity for people.
5. **Pooled "All" rows** weight subtasks by how many cases were written. Per-subtask results are primary.
6. **A missing fact with a plausible default** is a task-definition question before it is a model failure. The rule has to be stated per task.

## Open problems this review did not resolve
- Prompt-family sensitivity specific to typed decision interfaces (no study found).
- Separating prompt-induced spread from finite-sample noise (no source found).
- Formal handling of missing cells in multi-task aggregation, beyond pairwise deletion.
- Independent replication of the constrained-decoding quality dispute.
