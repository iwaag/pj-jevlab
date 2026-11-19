# Evaluation data, labels, validity and generalization

Guidance for building evaluation data that supports the claims made from it. Written 2026-10-02 in step4 of [benchmark/p1](../../devdocs/episodes/benchmark/p1/plan.md).
- Citations link to [evidence/](evidence/) entries; many cluster-D sources were read only at abstract level, and only their abstract claims are used.
- **"(derived here)"** marks synthesis made for this note.
- Metric definitions are in [metrics.md](metrics.md); uncertainty is in [statistics-and-comparison.md](statistics-and-comparison.md).

## 1. Validity: what a score is evidence of
**A score measures a construct.**
- A benchmark score operationalises an unobservable construct such as "routing ability" or "knows when information is missing". Harms and wrong conclusions come from mismatches between the construct and its operationalisation [jacobs2021measurement](evidence/D-data-validity.md#jacobs2021measurement).
- Wallach et al. structure evaluation in four levels [wallach2025position](evidence/D-data-validity.md#wallach2025position):
  1. **background concept** → (systematisation)
  2. **systematised concept**, a precise definition → (operationalisation)
  3. **instrument**: tasks, data, metric → (application)
  4. **measurements**.

  The validity of all levels is then interrogated.
- **Validity belongs to an interpretation in a context, not to a dataset.** It must be re-examined when a dataset is reused for a new purpose [wallach2025position](evidence/D-data-validity.md#wallach2025position).

**Validity lenses** used in ML measurement, from Jacobs & Wallach and adapted from Messick [jacobs2021measurement](evidence/D-data-validity.md#jacobs2021measurement) [messick1995validity](evidence/D-data-validity.md#messick1995validity) (Messick's own framing is verified at abstract level only):

| Lens | Question for a decision-model benchmark (derived here) |
|---|---|
| Face | Does the task look like the intended decision to a domain user? |
| Content | Does the case set cover the situations the construct includes (selection, each fallback class, rules with exceptions, long inputs, languages)? Is the construct itself contested? |
| Convergent | Do scores agree with other measures of the same capability (independent data, real traffic, human review)? |
| Discriminant | Is the score *not* explained by something else (formatting, option order, lexical overlap, prompt wording)? |
| Predictive | Does a better benchmark score predict better outcomes in the intended deployment? |
| Hypothesis | Do scores behave as theory predicts (harder variants are harder; removing the decisive fact moves the answer to the fallback)? |
| Consequential | What happens when the score is used for a decision (choice of system, a gate threshold)? Who bears the errors? |

**Internal vs external validity** [liao2021learning](evidence/D-data-validity.md#liao2021learning):
- **Internal validity** asks whether the measurement is right within this benchmark. Threats:
  - implementation variation (BLEU settings moved scores by up to 1.8 against a 0.14 leaderboard gap);
  - label errors and leakage;
  - small test sets;
  - contamination;
  - test-set reuse;
  - weak baselines.
- **External validity** asks whether the conclusion transfers to other data, metrics or settings.

**Ecological validity.**
- Benchmarks built for data quantity lose naturalness and relevance to real use [devries2020ecological](evidence/D-data-validity.md#devries2020ecological).
- Crowd-written queries (e.g. CLINC150) and authored cases are instances of this concern. They are not automatically invalid, but they need convergent evidence from natural data (derived here).

**Construct validity in current LLM benchmarks** [bean2025measuring](evidence/D-data-validity.md#bean2025measuring):
- **Scope:** a systematic review of 445 benchmarks.
- **Findings:**
  - 47.8% target phenomena without a consensus definition;
  - 27.0% use convenience sampling, only 17.1% random or stratified sampling, and 47.5% synthetic items;
  - 38.2% reuse earlier data;
  - only 16.0% run any statistical test;
  - only 53.4% justify why the benchmark is a valid measure.
- **The eight recommendations,** used here as a checklist:
  1. Define the phenomenon, including its sub-components and what it excludes.
  2. Measure only that phenomenon. Control confounds such as output format, and validate answer parsers.
  3. Construct a representative dataset.
  4. Acknowledge the limits of reused data.
  5. Prepare for contamination.
  6. Use statistics to compare models.
  7. Analyse errors against confounders.
  8. Justify construct validity.
- Raji et al. criticise treating a few benchmarks as measures of "general" capability [raji2021everything](evidence/D-data-validity.md#raji2021everything).

**Four criteria for a benchmark** (Bowman & Dahl) [bowman2021fix](evidence/D-data-validity.md#bowman2021fix):
1. good scores imply robust in-domain performance;
2. accurate, unambiguous labels;
3. adequate statistical power;
4. exposure of harmful bias.

On power, they estimate that a 1-point difference near 80% accuracy needs a few thousand examples.

## 2. Representative sampling, difficulty, ceiling and floor
- **Sampling defines the population the result generalises to.**
  - A random or stratified sample of a defined population supports a population estimate.
  - A convenience or authored sample supports only claims about the cases in it, plus whatever convergent evidence links it to the population [bean2025measuring](evidence/D-data-validity.md#bean2025measuring).
  - Stratification can over-sample rare but important cases (fallback classes, exceptions). The report must then **re-weight or report strata separately**, because the pooled rate is not a population rate (derived here).
- **Difficulty.**
  - **Ceiling:** when all strong systems are near 100%, the benchmark no longer separates them. Remaining differences are mostly noise; at n = 24, the 95% Wilson interval is [0.80, 0.99] for 23/24 and [0.86, 1.00] for 24/24 (derived here).
  - **Floor:** when all systems are near chance, the benchmark cannot separate them either.
  - **Benchmarks saturate quickly.** A study of 3,765 benchmarks found that many trended to near-saturation [ott2022mapping](evidence/D-data-validity.md#ott2022mapping).
- **Raising difficulty without biasing the comparison** (derived here, building on [kiela2021dynabench](evidence/D-data-validity.md#kiela2021dynabench) [bowman2021fix](evidence/D-data-validity.md#bowman2021fix)):
  - **Define difficulty by design features fixed before any model is run.** Examples: exceptions, negation, unstated defaults, long distractor text, near-neighbour options.
  - **Avoid selection by a candidate model's failures.** Keeping only the cases that one evaluated system fails makes the set adversarial to *that* system, which biases comparisons with it.
  - **Adversarial collection is disputed.** Dynabench uses model-in-the-loop collection to keep benchmarks hard [kiela2021dynabench](evidence/D-data-validity.md#kiela2021dynabench). Bowman & Dahl argue that it does not fix validity [bowman2021fix](evidence/D-data-validity.md#bowman2021fix). If it is used, the target model must be excluded from the comparison or reported separately.

## 3. Data sources compared
| Source | Strengths | Limitations | Provenance to record | Contamination risk |
|---|---|---|---|---|
| **Authored synthetic cases** (written by a person or an agent) | Full control of design features; exact labels by construction; paired variants are easy; no licence issues | One author's style and assumptions; artefacts and shortcuts; ecological validity unknown; designer's baselines are optimistic | Author identity (human, which model), guidelines version, generation prompts, date, any filtering | Low before publication; but the *patterns* may be familiar to models trained on similar text |
| **Public benchmark data** | Established labels; comparability with literature; known difficulty | Probably in training corpora; labels have errors (≥3.3% average across ten test sets [northcutt2021labelerrors](evidence/C-judging-structured.md#northcutt2021labelerrors)); written for another purpose; licence terms | Dataset, version or revision, split, row IDs, licence, original label, transformation applied | High; must be disclosed, not assumed absent |
| **Independent human-written data** (writers who did not design the task or the system) | Breaks the single-author link; natural variation; can test the definitions | Costly; needs guidelines and agreement measurement; still not real traffic | Writer pool, instructions, payment, independence from the designer, agreement | Low if new and unpublished |
| **Real operational traffic** | Ecological validity; natural prevalence of classes and fallbacks | Privacy and consent; labels must be created; prevalence of rare classes may be tiny; distribution drifts | Source system, time window, sampling rule, filtering, de-identification, label procedure | Low for private data; may contain public text |

**Fresh wording is not independence.**
- A new paraphrase of a known task, written by the same author or with the same model family, can share the task's semantics, its label rules and its shortcuts (derived here).
- Contamination concerns semantic as well as verbatim overlap. Rephrased benchmark data inflates scores while evading detection [dekoninck2024evading](evidence/D-data-validity.md#dekoninck2024evading). In open-domain QA, about 30% of test questions had a near-duplicate paraphrase in training [lewis2021overlap](evidence/D-data-validity.md#lewis2021overlap).
- **Independence is a property of the process:**
  - who designed the task;
  - who wrote the inputs;
  - who labelled them;
  - whether any evaluated system or its relatives took part.

**Reproducing a collection process still shifts results.** Re-creating ImageNet and CIFAR-10 test sets by the original process lowered accuracy by 11–14% and 3–15%, attributed to slightly harder examples rather than adaptive overfitting [recht2019imagenet](evidence/D-data-validity.md#recht2019imagenet). Expect a gap between a benchmark and its nominal population even under careful replication.

## 4. Splits, reuse and adaptive tuning
- **Leakage taxonomy** [kapoor2023leakage](evidence/D-data-validity.md#kapoor2023leakage):
  - **(L1) no clean train/test separation:** no test set, preprocessing or feature selection on all data, duplicates;
  - **(L2) illegitimate features;**
  - **(L3) a test set not drawn from the target distribution:** temporal leakage, non-independence, sampling bias.

  The authors found leakage in 329 papers across 17 fields.
- **Development / test separation for frozen systems.** Any choice made after looking at data belongs to development. Examples: prompt wording, thresholds, temperature, parsing, repair rules. The test set is used once, with frozen choices (derived here, consistent with [larson2019clinc](evidence/B-probability-abstention.md#larson2019clinc) and [rajpurkar2018squad2](evidence/B-probability-abstention.md#rajpurkar2018squad2), which tune thresholds on validation data).
- **Group and scenario splits.**
  - Variants of one base case share information: paraphrases, reorderings, complete/incomplete pairs, removed-candidate pairs and translations. They must stay on the same side of every split, which addresses duplicate leakage and non-independence [kapoor2023leakage](evidence/D-data-validity.md#kapoor2023leakage).
  - The same grouping matters for statistics: variants are clustered observations ([statistics-and-comparison.md](statistics-and-comparison.md)).
- **Random vs standard splits.**
  - Gorman & Bedrick recommend random splits plus paired testing over one standard split [gorman2019standard](evidence/D-data-validity.md#gorman2019standard).
  - Søgaard et al. find that random and even biased splits underestimate error on new samples, and recommend multiple independent test sets [sogaard2021random](evidence/D-data-validity.md#sogaard2021random).
  - Both reject reliance on a single fixed split.
- **Duplicate detection.** Check exact and near duplicates within the evaluation set, against development data, and (where possible) against known public sources. Report overlap-stratified results when overlap exists [lewis2021overlap](evidence/D-data-validity.md#lewis2021overlap).
- **Final-set reuse.**
  - Reusing a holdout adaptively can overfit it [dwork2015reusable](evidence/D-data-validity.md#dwork2015reusable) (abstract).
  - Kaggle leaderboards showed little substantial overfitting in practice [roelofs2019metaanalysis](evidence/D-data-validity.md#roelofs2019metaanalysis) (abstract), where submission limits bound adaptivity.
  - **Small authored sets with many design iterations are the risky case** (derived here).
- **New confirmation data after observing test failures.**
  - Once test failures have been inspected and the design, prompts or labels changed in response, that test set is development data for the changed design.
  - A claim about the changed design needs a new, frozen set. Results on the old set may be reported only as historical or seen data (derived here; this is the logic of preregistration [vanmiltenburg2021prereg](evidence/E-statistics-aggregation.md#vanmiltenburg2021prereg)).
  - Log how many evaluations each set has been through.

## 5. Labels and annotation
**Label sources, roughly in order of how directly they can be checked:**

| Label source | Strengths | Risks |
|---|---|---|
| **Programmatic** (solver over structured facts, rule over flags) | Exact and reproducible given the facts | Tests the rule, not language understanding. A model with the facts in structured form can be replaced by the solver. The label is only as valid as the rule's fit to the construct |
| **Evidence-based** (gold tied to a recorded deciding sentence or source) | Checkable; explains disagreements | The deciding evidence may be ambiguous; distractor evidence may support other labels |
| **Expert or annotator judgment with a rubric** | Covers open constructs | Needs guidelines, agreement measurement and adjudication |
| **Dataset label reused** | Comparable with literature | Original guideline and error rate inherited; e.g. MMLU estimated at 6.49% erroneous questions [gema2025mmlu](evidence/F-robustness-frameworks-perf.md#gema2025mmlu) |

**Annotation process** (MATTER cycle, via a handbook chapter) [pustejovsky2012matter](evidence/C-judging-structured.md#pustejovsky2012matter-and-finlayson2016overview):
1. Model the phenomenon and write a specification.
2. Annotate with written guidelines.
3. Train annotators until agreement is acceptable.
4. Track agreement and guideline versions.
5. Adjudicate disagreements into the gold.
6. Revise the scheme.

Datasheets add documentation of who labelled, how they were paid, the labelling process, and known errors [gebru2021datasheets](evidence/C-judging-structured.md#gebru2021datasheets).

**Practical elements** (derived here, building on [artstein2008agreement](evidence/C-judging-structured.md#artstein2008agreement) [squad_eval_scripts](evidence/C-judging-structured.md#squad_eval_scripts)):
- **Explicit rubric in the label definitions.** Include definitions of the boundary cases.
- **Acceptable-answer sets** where two answers are defensible, rather than forcing one gold.
- **Blind adjudication.** The adjudicator sees the case and the competing labels, not which system produced which.
- **A recorded reason per adjudicated case.**

**Agreement.**
- Report a chance-corrected coefficient (κ, π or α) with the agreement table, the number of coders and whether coding was independent [artstein2008agreement](evidence/C-judging-structured.md#artstein2008agreement) [krippendorff2011computing](evidence/C-judging-structured.md#krippendorff2011computing).
- With skewed labels, raw agreement is misleading [feinstein1990paradox](evidence/C-judging-structured.md#feinstein1990paradox).

**Disagreement is information** [aroyo2015truth](evidence/C-judging-structured.md#aroyo2015truth) [pavlick2019inherent](evidence/C-judging-structured.md#pavlick2019inherent) [nie2020chaosnli](evidence/C-judging-structured.md#nie2020chaosnli) [plank2022hlv](evidence/C-judging-structured.md#plank2022hlv):
- **It is not always error.** Some items have more than one defensible reading. Disagreement on NLI persists with 50 raters per item [pavlick2019inherent](evidence/C-judging-structured.md#pavlick2019inherent). Majority labels changed on 10–32% of selected low-agreement items with 100 raters [nie2020chaosnli](evidence/C-judging-structured.md#nie2020chaosnli).
- **Options for representing this:**
  - an acceptable set;
  - a soft label (distribution of judgments), scored with cross-entropy or Jensen–Shannon divergence [uma2021disagreement](evidence/C-judging-structured.md#uma2021disagreement);
  - moving the item to an unscored exploratory slice.

**Ambiguity vs model error.**
- When all strong systems agree on a non-gold answer, check the label before calling it a shared model failure.
- Conversely, a defensible alternative reading must be shown by the label definitions, not inferred from model behaviour (derived here).

**Related-model audits are not independent human validation.**
- A second annotator from the same model family as the author or the evaluated systems shares training data, conventions and blind spots.
- High agreement then shows internal consistency, not validity for human users of the task. It can miss exactly the defaults that models share (derived here).
- LLM judges vary widely by task and must be validated against human labels before use [bavaresco2024judgebench](evidence/C-judging-structured.md#bavaresco2024judgebench) [thakur2024judges](evidence/C-judging-structured.md#thakur2024judges). Their biases include self-preference [panickssery2024selfpref](evidence/C-judging-structured.md#panickssery2024selfpref).

## 6. Positives, negatives and minimal pairs
- **Minimal pairs and contrast sets.**
  - A contrast set perturbs an input minimally near a "pivot", usually changing the gold label.
  - **Contrast consistency** (all members correct, including the original) is stricter than accuracy and exposes local decision-boundary errors [gardner2020contrast](evidence/D-data-validity.md#gardner2020contrast).
  - Counterfactually revised data uses the same idea with human minimal edits [kaushik2020cad](evidence/D-data-validity.md#kaushik2020cad).
- **Behavioural tests** [ribeiro2020checklist](evidence/D-data-validity.md#ribeiro2020checklist):
  - **MFT** (minimum functionality): targeted unit tests.
  - **INV** (invariance): label-preserving perturbations; the prediction must not change.
  - **DIR** (directional): the prediction must move in a known direction.

  Results are failure rates per capability, not population accuracies.
- **Kinds of negatives:**

  | Negative | Construction | What it tests | Caveat |
  |---|---|---|---|
  | Out-of-scope input | Inputs that are not instances of the task; CLINC150's 1,000 OOS test queries [larson2019clinc](evidence/D-data-validity.md#larson2019clinc) | Scope detection | Crowd-written OOS prompts were OOS only about 69% of the time [larson2019clinc](evidence/B-probability-abstention.md#larson2019clinc) |
  | Near-neighbour candidates | Confusable options from the same domain; Banking77's fine-grained intents [casanueva2020banking77](evidence/D-data-validity.md#casanueva2020banking77) | Fine discrimination | Banking77 has no OOS class and no validation split |
  | Removed candidate / removed evidence | The gold option or the decisive evidence is deleted from an otherwise valid case | "No matching candidate" / "missing evidence" | Must be adjudicated: another remaining option may become defensible |
  | Adversarial unanswerable | Written to resemble answerable questions, with a plausible distractor span; SQuAD 2.0 [rajpurkar2018squad2](evidence/D-data-validity.md#rajpurkar2018squad2) | Answerability | Adversarial by construction, not a natural sample of user queries |
  | Contrastive evidence | Nearly identical evidence that does or does not support a claim; VitaminC [schuster2021vitaminc](evidence/D-data-validity.md#schuster2021vitaminc) | Evidence sensitivity | Synthetic pairs may carry artefacts; report real and synthetic separately |
  | Negation, quotation, reported speech | A minimal edit that flips or neutralises meaning | Meaning-sensitivity (DIR) | Gold must be derived explicitly |
  | Unmentioned fact | A decisive fact is simply not stated | Missing-information detection | See below: depends on what the task says about defaults |
  | Explicitly unknown / null / empty | A field states that the value is unknown, or is blank | Reading of explicit markers | Unknown ≠ false ≠ empty must be defined |
  | Contradiction | Two sources disagree and no rule resolves them | Conflict detection | If the input gives a resolution rule (recency, authority), the case is substantive |

- **Unmentioned facts need a task-level rule** (derived here).
  - Whether "not mentioned" means "unknown" or "conventionally false" is a property of the task, not of language. Examples: "final sale" not stated, a receipt not mentioned.
  - A benchmark must state the rule in the task definition before asking a model to apply it. Otherwise the label measures agreement with the author's default.
  - Some cases should be scored under each rule and reported apart.
- **Artificial negatives can misrepresent traffic** (derived here, following the ecological-validity concern [devries2020ecological](evidence/D-data-validity.md#devries2020ecological)).
  - Constructed negatives often differ from natural negatives in prevalence (balanced instead of rare) and in surface form (cleaner or more obvious).
  - Strong results on them do not establish false-acceptance rates on real traffic.
  - Report fallback results per construction type, and confirm on natural negatives before a deployment claim.

## 7. Shortcuts and artefacts
- **Annotators leave label-predictive cues.** A hypothesis-only classifier gets about 67% on SNLI and 53% on MultiNLI [gururangan2018annotation](evidence/D-data-validity.md#gururangan2018annotation).
- **Models adopt heuristics that fail on targeted cases.** An example is lexical overlap in HANS [mccoy2019hans](evidence/D-data-validity.md#mccoy2019hans).
- **This is "shortcut learning"** [geirhos2020shortcut](evidence/D-data-validity.md#geirhos2020shortcut): decision rules that work on standard benchmarks but fail to transfer.
- **Diagnostics** (derived here, from the cited pattern):
  - **Partial-input baselines:** answer from the options only, or from the input with the decisive sentence removed.
  - **Option-text-only and keyword baselines.**
  - **Controlled challenge sets** that break a suspected heuristic.

  If a partial-input baseline does well, the benchmark measures the shortcut as much as the construct.

## 8. Distribution shift and generalisation
- **Dataset shift** is a change in the joint distribution of inputs and outputs. **Covariate shift** is the special case where only the inputs change [quinonero2009shift](evidence/D-data-validity.md#quinonero2009shift).
- **Natural shifts produce large in-distribution vs out-of-distribution gaps** [koh2021wilds](evidence/D-data-validity.md#koh2021wilds). WILDS reports worst-group or worst-domain performance next to the average [koh2021wilds](evidence/F-robustness-frameworks-perf.md#koh2021wilds), and documents that model selection on OOD validation data is a protocol choice.
- **Shift axes relevant to decision tasks** (derived here):
  - domain and topic;
  - writing source (author, crowd, real users);
  - language and script;
  - input length and noise;
  - option count;
  - label prevalence, especially the share of fallback cases;
  - time.

  Report each axis as a separate slice rather than folding it into one score.

## 9. Contamination
- **Definitions** [sainz2023trouble](evidence/D-data-validity.md#sainz2023trouble):
  - **guideline contamination:** the annotation guidelines were seen;
  - **raw-text contamination:** the source text was seen;
  - **annotation contamination:** the labelled examples were seen.

  Exposure of the *test* split invalidates the experiment. Exposure of train/dev invalidates zero- or few-shot claims.
- **Memorisation is not exploitation:** models can memorise labels without using them [magar2022contamination](evidence/D-data-validity.md#magar2022contamination).
- **Detection methods and their limits:**

  | Method | Evidence it gives | Limit |
  |---|---|---|
  | n-gram overlap with the training corpus [brown2020gpt3](evidence/D-data-validity.md#brown2020gpt3) | Overlap flags and clean-vs-full comparison | Needs corpus access. False positives with shared passages (DROP was 94% "dirty"). Misses paraphrases. GPT-3 §4 says 13-grams; App. C uses N in [8, 13] |
  | Corpus documentation [dodge2021c4](evidence/D-data-validity.md#dodge2021c4) | Benchmarks found in a public crawl | Only for documented corpora |
  | Guided-completion probes [golchin2024timetravel](evidence/D-data-validity.md#golchin2024timetravel) | Near-verbatim memorisation of instances | Relies on an LLM judge; verbatim only |
  | Exchangeability (order) test [oren2024proving](evidence/D-data-validity.md#oren2024proving) | Provable false-positive bound under exchangeability | Detects verbatim, order-memorised data only; cannot rule out partial contamination |
  | Fresh parallel test set (vendor-produced) [zhang2024gsm1k](evidence/D-data-validity.md#zhang2024gsm1k) | Gap between old and matched new data (up to 8% for some families) | Costly; matching difficulty is imperfect |
  | Time-split live benchmarks [white2025livebench](evidence/D-data-validity.md#white2025livebench) [jain2024livecodebench](evidence/D-data-validity.md#jain2024livecodebench) | Items newer than the model's cutoff | Trusts the stated cutoff; time windows change difficulty |

- **Every detector can be evaded** by deliberately rephrased contamination [dekoninck2024evading](evidence/D-data-validity.md#dekoninck2024evading). **Detection is evidence, not proof of a clean dataset.** Never claim a dataset is clean without saying which checks were run and what they cannot detect.
- **Leakage through labels and options.** Option wording, option order and answer formats can reveal the label without the input. Partial-input baselines (section 7) and selection-bias measures ([robustness-and-execution.md](robustness-and-execution.md)) test for this (derived here).
- **Benchmark overfitting.** A public leaderboard becomes an optimisation target. Biderman et al. note that the Open LLM Leaderboard became one, with fine-tuning aimed at its formatting [biderman2024lessons](evidence/F-robustness-frameworks-perf.md#biderman2024lessons).
- **Protecting a private set:**
  - hold back a slice;
  - publish with a precommitted later release, as GSM1k (a vendor-produced set, Scale AI) did [zhang2024gsm1k](evidence/D-data-validity.md#zhang2024gsm1k);
  - embed a canary string so it can be filtered from training corpora, as BIG-bench did [srivastava2023bigbench](evidence/F-robustness-frameworks-perf.md#srivastava2023bigbench).

## 10. Licensing and documentation (only where it affects use)
- **Licences decide what can be redistributed in a derived evaluation set.** ShareAlike terms carry over to derivatives:

  | Dataset | Licence |
  |---|---|
  | CLINC150 | CC BY 3.0 |
  | Banking77 | CC BY 4.0 |
  | SQuAD 2.0 | CC BY-SA 4.0 |
  | VitaminC data | CC BY-SA 3.0 (code MIT) |

  Sources: [larson2019clinc](evidence/D-data-validity.md#larson2019clinc) [casanueva2020banking77](evidence/D-data-validity.md#casanueva2020banking77) [rajpurkar2018squad2](evidence/D-data-validity.md#rajpurkar2018squad2) [schuster2021vitaminc](evidence/D-data-validity.md#schuster2021vitaminc).
- **Licence metadata on hosting sites is often missing or wrong.** An audit found omission above 70% and errors above 50% [longpre2024provenance](evidence/D-data-validity.md#longpre2024provenance). Check the original LICENSE.
- **Real traffic needs privacy handling** (consent, de-identification). This limits what can be published and therefore how others can reproduce a result.
- **A datasheet-style record** (motivation, composition, collection, labelling, uses) makes these limits visible [gebru2021datasheets](evidence/D-data-validity.md#gebru2021datasheets).

## 11. Checklist for trustworthy evaluation data
1. **Construct:**
   - State the systematised construct and what it excludes.
   - State the decision the result will inform.
2. **Population:** Define the population. Sample from it, or say why the sample is a convenience sample and what convergent evidence will link it.
3. **Provenance per item:**
   - author or source;
   - date and version;
   - licence;
   - transformation;
   - label source.
4. **Difficulty:** Design features are fixed before running systems. There is no selection by evaluated systems' failures.
5. **Splits and freeze:**
   - Group variants and keep each group on one side of every split.
   - Run duplicate checks.
   - Freeze the dev and test sets; log test uses; add new confirmation data after design changes.
6. **Labels:**
   - Labels are tied to a rubric, evidence or a rule.
   - Use acceptable sets where needed.
   - Measure agreement with an independent annotator, including at least one human pass for validity claims.
   - Use blind adjudication with reasons.
7. **Negatives:**
   - one class per mechanism (out of scope, no candidate, missing, conflicting);
   - construction type recorded;
   - explicit rules for unstated defaults and for unknown, false and empty values.
8. **Shortcut checks:** partial-input and keyword baselines.
9. **Contamination:** checks run and their limits stated; public items flagged as likely seen.
10. **Shift slices:** each shift axis reported separately; natural data used before deployment claims.
