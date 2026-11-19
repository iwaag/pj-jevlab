# Handoff to p2: benchmark design decisions

Written 2026-10-02 in step6 of [benchmark/p1](../../devdocs/episodes/benchmark/p1/plan.md) for episode benchmark/p2, which will choose the Jev-style benchmark design.

**This file does not choose.** For each decision it lists:
- the question;
- the defensible alternatives and what each costs;
- the evidence in this study;
- what evidence is still missing.

Nothing here is a settled weight, gate or leaderboard formula, and no model was run in p1.

## Part A. Decision checklist
### A1. Intended use and workload population
- **Question:** which decisions will the benchmark inform?
  - screening which systems to study further;
  - choosing a system for an application class;
  - a deployment gate for one application;
  - a scientific claim, e.g. about size or training.
- **Question:** which population of inputs should the results generalise to?
- **Alternatives:**
  1. **A defined application class with its own population** (e.g. support-ticket routing, claim eligibility with written policy). This gives strong validity for that class, but not beyond it.
  2. **A portfolio of workload classes reported separately.** Broader, but each cell is smaller.
  3. **A capability-oriented diagnostic suite** (selection, each fallback mechanism, rules, ordinal judgment). This shows mechanisms well but has weak predictive validity for any one deployment.
- **Evidence:**
  - [data-and-validity.md §1–2](data-and-validity.md): validity is per interpretation; sampling defines the population.
  - [statistics-and-comparison.md §8](statistics-and-comparison.md): claim types.
- **Missing:**
  - which applications matter to this project;
  - their real class mix, including how often fallbacks occur.

### A2. Task and label ontology
- **Questions:**
  1. What is one task? A question type × domain, or a decision mechanism?
  2. Which outcomes are labels?
- **Options to fix:**
  - **Substantive options.** How many, and how fine-grained? Near-neighbour sets?
  - **Fallback classes:**
    - one generic "none";
    - or separate out-of-scope, no matching candidate, missing evidence, conflicting evidence and explicit defer;
    - plus whether a wrong fallback class counts as partly correct.
  - **The unstated-default rule:** for each task, does an unmentioned fact mean unknown, or conventionally false? Should some cases be scored under both rules?
  - **Value states:** how unknown, false, empty, null and absent are each defined.
  - **Ordinal labels:** levels only, or levels plus a "cannot rate" outcome?
  - **Multi-label and ranking:** do they belong in scope? Native or derived?
- **Evidence:**
  - [metrics.md §7, §11](metrics.md): answerability vs confidence vs shift; outcome accounting.
  - [data-and-validity.md §6](data-and-validity.md): negative types and the unmentioned-fact rule.
- **Missing:**
  - **Agreement data.** Independent human agreement on the boundary definitions, especially missing vs conventionally false, and empty vs missing.

### A3. Data sources and independence
- **Alternatives** (can be combined; each reported as its own slice):
  - **authored by a human or agent:** cheap, controllable, with exact labels, but single-author and of unknown ecological validity;
  - **public benchmark slices:** comparable with other work, licensed, but likely seen in training;
  - **independent human-written data:** writers separate from the task designer, with guidelines and agreement measurement;
  - **operational or realistic traffic:** natural prevalence and wording, but needs labelling and privacy handling.
- **Decisions:**
  - Who writes cases, who labels them, who adjudicates, and how independent each is from the evaluated systems.
  - Whether to hold back a private slice, or add a canary string.
  - How many evaluations each final set may be used for.
- **Evidence:**
  - [data-and-validity.md §3–5, §9](data-and-validity.md): sources, splits, labels, contamination.
- **Missing:**
  - **Availability of human annotators or writers.** This is a human-preparation item for p2/p3.
  - **Any access to non-authored traffic for the target applications.**

### A4. Baselines and reference points
- **Candidates:**
  - **trivial baselines:** majority class, chance, always-fallback, always-answer;
  - **executable code baselines:** keyword lists or rules written *before* seeing data and by someone other than the case author;
  - **partial-input baselines:** options only, or the decisive sentence removed;
  - **oracle solvers over structured facts,** an upper bound that shows when language understanding is not needed;
  - **a general LLM with validated output** (a different system type);
  - **human performance** on a subset.
- **Choice:** which baselines are primary references, and which are upper bounds.
- **Evidence:**
  - [metrics.md §0](metrics.md): reporting rules, including baselines.
  - [data-and-validity.md §7](data-and-validity.md): shortcut diagnostics.
  - [frameworks-and-benchmarks.md](frameworks-and-benchmarks.md): trivial-policy baselines in SQuAD 2.0 and GLUE.
- **Missing:**
  - **Independently written baseline rules.**
  - **Human baseline data.**

### A5. Primary metrics
- **Questions:**
  1. Which quantity is primary for each task family?
  2. Which quantities are secondary?
  3. Which are diagnostic only?
- **Defensible alternatives:**
  - **Selection:** accuracy on substantive cases, or macro recall (balanced accuracy) or macro F1 when classes are uneven. The macro-F1 definition must be named.
  - **Rejection, per fallback class:**
    - recall of each class;
    - false-acceptance rate (fallback gold → substantive answer);
    - false-rejection rate (substantive gold → fallback);
    - a wrong-class rate.
  - **Joint view:** effective reliability or a cost-weighted score, *only if* a cost model (A8) exists. Otherwise show the separate rates side by side.
  - **Probabilities, per system:**
    - log loss or Brier on the offered options;
    - a reliability table with counts;
    - risk–coverage at a dev-frozen threshold, or the full curve.

    Cross-system comparison of proper scores is caveated by readout semantics ([metrics.md §12](metrics.md)).
  - **Ordinal:** exact, within-one, MAE, linear weighted κ. Choose according to the equidistance view.
  - **Multi-label and ranking:** subset exact match, example F1 and cardinality; nDCG with named gain and discount, tie-aware.
- **Evidence:** [metrics.md](metrics.md), especially §13 on tradeoffs that need a use.
- **Missing:** the relative costs of false acceptance, false rejection and deferral in the target applications.

### A6. Execution protocol and failure accounting
- **Decisions:**
  - **System path:** each system's native path (system comparison), or a common prompt and readout family (closer to a model comparison).
  - **Data-boundary sentence:** for every system or none, or reported as a variable.
  - **Option order:** fixed, or permuted with averaging.
  - **Prompts:** a single prompt, or a prompt family with a reported range.
  - **Repeats:** none (deterministic) or K per item.
  - **Failure policy:** deadline; validity rule; repair policy (none, or frozen on dev); how unsupported inputs and truncation are recorded.
  - **Multi-question:** in or out of the primary score; joint vs separate.
- **Evidence:** [robustness-and-execution.md §2, §6–7](robustness-and-execution.md).
- **Missing:**
  - **Determinism:** a check on each local runtime.
  - **Prompt-family sensitivity:** for the decision interface, as distinct from MCQ benchmarks.

### A7. Uncertainty and decision rules
- **Decisions:**
  - Unit of analysis (case, base case or cluster) and the interval method.
  - **The confirmatory family,** fixed before data collection: which comparisons, which test (mid-p McNemar, permutation, Bayesian paired), and which correction (Holm).
  - **Target minimum detectable effect,** and therefore the cell sizes.
  - **Pre-specified margins,** if any equivalence or non-inferiority claim is wanted.
  - **Aggregation:** none, or per-task results plus a named-weight aggregate on a common supported subset, with coverage reported beside it.
- **Evidence:** [statistics-and-comparison.md](statistics-and-comparison.md). With about 10% discordance:

  | Cases per comparison | Minimum detectable difference |
  |---|---|
  | 24 | ~16 points |
  | 200 | ~6 points |

- **Missing:** realistic discordance rates between the candidate systems on the new tasks. Earlier data can serve as a prior, but it is seen data.

### A8. Cost and operational targets
- **Decisions:**
  - **Load scenario:** single-stream sequential, fixed concurrency, or a Poisson rate.
  - **Input grid:** length × option count × question count.
  - **Percentiles and sample sizes:** a distribution-free p95 interval needs n ≥ 59 ([min, max], almost one-sided) or n ≥ 72 (equal-tailed); p99 needs 299 or 368.
  - **Memory counter and sampling.**
  - **Cost units:** latency, memory, energy, cost per decision.
  - **Comparison:** a Pareto front or explicit target thresholds, e.g. "p95 under X ms at concurrency Y".
- **Evidence:** [performance-and-cost.md](performance-and-cost.md).
- **Missing:** target latency and memory budgets for the intended applications.

### A9. Optional diagnostic axes
Each is reported as its own slice, never folded into the primary score unless A1 makes it part of the construct:
- robustness: invariance and directional variants, option permutation, paraphrase;
- injected instruction inside content vs direct request, with a stated policy;
- input length and evidence position;
- language (input, instruction and option language);
- option count;
- multi-question interference;
- calibration under shift.

- **Evidence:**
  - [robustness-and-execution.md §1–5](robustness-and-execution.md);
  - [data-and-validity.md §8](data-and-validity.md).
- **Missing:** a decision on which axes matter for the intended use (A1).

## Part B. Earlier local evaluations: lessons and gaps
These map the audit points in [questions-and-audit.md](questions-and-audit.md) to what the literature says. The earlier results stand as recorded. This is about what p2 should do differently or keep, not a re-judgement.

| Audit | Observation | Lesson from the review | What p2 must decide | Evidence still missing |
|---|---|---|---|---|
| A1 | n = 3–24 per cell; primary contrasts with 6 discordant pairs (1 vs 5, 5 vs 1) | Such cells support screening, not confirmatory differences. With a Holm family of ten tests, an exact McNemar test needs at least 9 discordant pairs all in one direction (mid-p: 8) | Cell sizes from a target minimum detectable effect; which comparisons are confirmatory | Expected discordance on new tasks |
| A2 | Ceiling on authored selection cases | Ceiling cells carry little comparative information; difficulty should come from predefined design features, not selection by model failure | Difficulty features per task; how to avoid adversarial selection against an evaluated system | Pilot difficulty on dev data |
| A3, A4 | One agent author; label audit by a related model | Fresh wording ≠ independence; related-model agreement shows consistency, not validity | Role of independent human writers and annotators; agreement statistic | Human annotation availability |
| A5 | Public slices likely seen; "external looks like authored" | Agreement between two possibly familiar sources does not establish independence; contamination checks have known blind spots | Whether public slices are kept, and how they are labelled in reports | Non-public or time-split data |
| A6 | Oracle solvers 100% by construction; keyword lists by the case author | Oracles bound what structured facts give; author-written baselines are optimistic | Baselines written independently and before data | — |
| A7 | Different probability readouts; Brier compared side by side | Proper scores are valid per system; cross-system comparison mixes readout and calibration | Whether probability metrics are per-system diagnostics or compared, and under what normalisation | — |
| A8 | Dev-frozen gates; "0% risk at 92% coverage" | On ~110 accepted cases, 0 errors still allows ~3% risk (95% upper bound); per-system thresholds are not a common operating point | Report risk with upper bounds; a common target risk, or curves | — |
| A9 | Prompts differ between arms (data-boundary sentence) | Injection and robustness results then compare prompts as well as models | Treat the boundary sentence as a controlled variable or a disclosed system difference | Effect size of the sentence |
| A10, A11 | Missing-fact defaults; empty vs missing | "Not mentioned" has no universal meaning; tasks must state it, and boundary cases need acceptable sets or exploratory status | The default rule per task; value-state definitions | Human agreement on these boundaries |
| A12 | Fenced JSON scored invalid on an un-dev-checked track | Validity and correctness are separate; repair policy must be frozen on dev | Validity rule and repair policy for non-typed systems | — |
| A13 | Rules given as text to an instruction-free classifier; unsupported cells | Unsupported ≠ wrong ≠ rejected; aggregate only over common supported subsets with coverage beside it | Coverage table; common subset | — |
| A14 | "All" rows pool subtasks with design-chosen sizes | A pooled row weights subtasks by how many cases were written | Per-subtask primary results; named weights if any aggregate | — |
| A15 | Paired variants from one base | Variants are clustered; analyse per base | Unit of analysis; clustered or stratified resampling | — |
| A16 | Multi-question interference | Interference is a system and deployment parameter | Whether joint requests are in scope; isolation setting | — |
| A17 | 40 warm sequential samples over a length × option grid; RSS vs footprint | p95 from 40 samples has no distribution-free interval, and pooling grid cells gives a mixture quantile that also breaks the iid assumption; memory counters differ by runtime | Load scenario, sample sizes, one memory counter | Concurrency behaviour |
| A18 | Recommendations from screening-sized authored data | Deployment evidence needs representative data and an operating point from the application | Which claim type p3 will make | Application data |
| A19 | Cross-system size comparison (set2) | Size claims need variants that differ only in size, and several tasks | Whether any size or training claim is in scope | Controlled model families |
| A20 | Robustness as counts of changed answers | Pair invariance with directional tests; report per base; small spreads are partly noise | Which perturbations; expected direction per variant | — |

## Part C. Evidence p1 could not provide
1. **Independent human validation** of the label boundaries that matter most: missing vs conventionally false, empty vs missing, conflict vs resolvable.
2. **Natural or operational inputs** for the target workloads, including the real share of fallback cases.
3. **Costs** of false acceptance, false rejection and deferral for the target applications.
4. **Prompt-family sensitivity of typed decision interfaces.** The literature measures MCQ and generation; the review found no study of this interface.
5. **Discordance rates and determinism** of candidate systems on new, harder tasks, for power planning.
6. **Latency and memory targets** from an intended deployment.
