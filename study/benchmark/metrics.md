# Task metrics and their assumptions

Reference for choosing and reading metrics. Written 2026-10-02 in step3 of [benchmark/p1](../../devdocs/episodes/benchmark/p1/plan.md). Each claim cites a source entry in [evidence/](evidence/), which records how far the source was read (full text, abstract or unverified). **"(derived here)"** marks arithmetic or a synthesis made for this note, not a claim from a source. Uncertainty and significance testing are in [statistics-and-comparison.md](statistics-and-comparison.md).

**This note does not recommend a universal metric.** Section 13 lists the tradeoffs that can only be settled once an intended use and a cost model are fixed.

## 0. Rules that apply to every family
1. **Name the denominator.** "Accuracy" over all cases, over valid replies, over supported cases and over substantive cases are four different numbers. State which cases are in it, and how errors, abstentions and unsupported inputs are counted (section 11).
2. **Name the averaging.** A bare "F1" is ambiguous:
   - per-class F1;
   - macro F1 as the mean of per-class F1;
   - macro F1 as the harmonic mean of macro precision and macro recall;
   - micro F1;
   - support-weighted F1;
   - for multilabel, example-based F1.

   These can differ by up to 0.5 and rank systems differently [opitz2019macrof1](evidence/A-metrics.md#opitz2019macrof1) [sklearn-modeleval](evidence/A-metrics.md#sklearn-modeleval).
3. **Name the zero-division convention.** Precision is undefined when a class is never predicted. Recall is undefined when a class has no gold cases. Conventions:
   - set the value to 0 (the scikit-learn default, with a warning);
   - set it to 1;
   - exclude the class from the average (`zero_division=np.nan`).

   On small test sets this changes macro scores [sklearn-modeleval](evidence/A-metrics.md#sklearn-modeleval) [sakai2021ordinal](evidence/A-metrics.md#sakai2021ordinal).
4. **State the confusion-matrix orientation.** Sources disagree on whether rows are gold or predicted [opitz2024closerlook](evidence/A-metrics.md#opitz2024closerlook) [sklearn-modeleval](evidence/A-metrics.md#sklearn-modeleval) [fawcett2006roc](evidence/A-metrics.md#fawcett2006roc).
5. **Report reference points:**
   - the chance level for the task's option count;
   - the majority-class baseline;
   - where they exist, an executable non-model baseline and an oracle that shows the ceiling of structured information.

   A metric value means little without them.
6. **Report counts, not only rates,** when cells are small. Interval methods are in [statistics-and-comparison.md](statistics-and-comparison.md).

## Comparison table
| Family | Measures | Expected inputs | Typical metrics | Main failure modes | Suitable when | Unsuitable when |
|---|---|---|---|---|---|---|
| Single-label classification | Agreement of one predicted label with one gold label | Predicted label per case | Accuracy, per-class P/R/F1, macro F1, balanced accuracy, κ, MCC | Imbalance hides minority failure; ambiguous "F1"; constant predictors look good | One correct label per case, label costs roughly equal | Several defensible labels; costs very unequal; abstention is a separate outcome |
| Binary scoring / detection | Separation of positives from negatives, and the error mix at a threshold | Score per case (threshold-free) or decision (thresholded) | TPR/FPR, precision, ROC-AUC, PR-AUC/AP, FPR at fixed TPR | Prevalence dependence of precision/PR; ties; optimistic interpolation; threshold tuned on test | A detector feeds a threshold decision; prevalence of deployment is known | Scores are not comparable across systems; only one operating point matters (then report it) |
| Multilabel | Correctness of a label *set* | Set of labels or per-label scores | Subset exact match, Hamming loss, example-/micro-/macro-F1 | Empty sets undefined; threshold drives everything; metrics optimised against each other | Labels are independently applicable | Labels are mutually exclusive (use single-label) |
| Retrieval / ranking | Order quality of candidates | Ranked list or scores per candidate | P@k, R@k, MRR, MAP, nDCG@k | Incomplete judgments; ties; gain/discount variants; candidate-pool construction | Users read a ranked list; graded relevance exists | Only the top choice matters (use classification) |
| Ordinal / regression | Distance between predicted and gold level | Level or number | Exact, within-one, MAE/RMSE, weighted κ, Krippendorff α | Equidistance assumed; κ = 0 for constant predictors; ordinal treated as interval | Ordered levels with a meaningful distance | Levels are categories with no order |
| Probabilistic prediction | Quality of probability statements | Normalised distribution over outcomes | Log loss, Brier, reliability diagram, ECE variants | Binning bias; top-label only; probabilities with different semantics; clipping | Probabilities drive thresholds, routing or expected cost | Outputs are scores, not probabilities; no probabilities exist |
| Abstention / selective prediction | Usefulness of declining to answer | Decision plus confidence, or an explicit abstain label | Risk–coverage, AURC, coverage at target risk, abstention P/R | Mixing answerability with confidence; rewarding always-abstain; threshold tuned on test | Wrong answers cost more than deferrals | No defined cost of deferring; gold "should abstain" not defined |
| Generated / structured outputs | Validity and semantic correctness of free or structured text | Text / JSON | Parse and schema validity, exact match, token F1, acceptable-answer match | Parser decides the score; repair hides failures; equivalent answers missed | A machine consumes the output | — (always report validity separately from correctness) |
| Human or model judging | Quality where no programmatic gold exists | Judgments by people or a model | Agreement (κ, π, α), pairwise preference, Bradley–Terry | Position, verbosity and self-preference bias; tie handling; unvalidated judges | Open-ended outputs; rubric can be stated | A programmatic or evidence-based label is available |
| Utility and cost | Value of decisions under explicit costs | Decisions, costs per outcome, resource measurements | Expected cost, net benefit, cost curves, Pareto fronts | Costs invented post hoc; costs and benefits on different baselines | The deployment decision and its costs are known | Costs unknown (then show the tradeoff curve instead) |

## 1. Single-label classification
**Definitions** [opitz2024closerlook](evidence/A-metrics.md#opitz2024closerlook) [sklearn-modeleval](evidence/A-metrics.md#sklearn-modeleval):

| Quantity | Formula | Notes |
|---|---|---|
| Accuracy | Σ diagonal / N | In single-label multiclass, accuracy = micro-P = micro-R = micro-F1 when every label is included [opitz2024closerlook](evidence/A-metrics.md#opitz2024closerlook) |
| Precision P_i | TP_i / (TP_i + FP_i) | Denominator = cases *predicted* as i |
| Recall R_i | TP_i / (TP_i + FN_i) | Denominator = *gold* cases of i |
| F1_i | 2 P_i R_i / (P_i + R_i) = 2TP / (2TP + FP + FN) | |
| Macro F1 (averaged) | (1/n) Σ_i F1_i | The scikit-learn definition, recommended by Opitz & Burst [opitz2019macrof1](evidence/A-metrics.md#opitz2019macrof1) |
| Macro F1 (F1 of averages) | 2 P̄ R̄ / (P̄ + R̄) | Always ≥ averaged F1; rewards classifiers with skewed error types [opitz2019macrof1](evidence/A-metrics.md#opitz2019macrof1) |
| Weighted F1 | Σ_i support_i F1_i / N | Non-monotonic; can fall outside [P, R]; no clear advantage over accuracy [opitz2024closerlook](evidence/A-metrics.md#opitz2024closerlook) [sklearn-modeleval](evidence/A-metrics.md#sklearn-modeleval) |
| Balanced accuracy | (1/n) Σ_i R_i | Equals macro recall; prevalence-invariant; chance level 1/n [brodersen2010balacc](evidence/A-metrics.md#brodersen2010balacc) [opitz2024closerlook](evidence/A-metrics.md#opitz2024closerlook) |
| Cohen's κ (against gold) | (acc − chance) / (1 − chance), chance = Σ_i p_i b_i | 0 for any constant predictor; scikit-learn notes it is designed for annotator agreement [opitz2024closerlook](evidence/A-metrics.md#opitz2024closerlook) [sklearn-modeleval](evidence/A-metrics.md#sklearn-modeleval) |
| MCC (binary) | (TP·TN − FP·FN) / √((TP+FP)(TP+FN)(TN+FP)(TN+FN)) | Undefined when a row or column of the confusion matrix is empty; 0 for the majority classifier under a limit convention [chicco2020mcc](evidence/A-metrics.md#chicco2020mcc) |

**Averaging conventions:**
- **Micro** pools counts, so frequent classes dominate.
- **Macro** weights every class equally, so rare classes count as much as common ones.
- **Weighted** follows the test-set prevalence.
- **Which is "right" depends on the use.** If every class matters equally to the user (rare intents, fallback classes), use macro. If the population mix is the target, use micro or accuracy, and only on a representatively sampled test set.

**Excluding a label from the average.** Excluding a "none"/fallback label from micro averaging is a legitimate choice, but it changes the meaning of the result [sklearn-modeleval](evidence/A-metrics.md#sklearn-modeleval). Name it.

**Competing views:**
- Chicco & Jurman argue MCC is the most informative binary summary, using six worked confusion matrices. Example: accuracy 0.90, F1 0.95 and MCC −0.03 on the same matrix [chicco2020mcc](evidence/A-metrics.md#chicco2020mcc).
- Opitz finds MCC non-monotonic and harder to interpret than macro recall or κ [opitz2024closerlook](evidence/A-metrics.md#opitz2024closerlook).
- Opitz also shows that metric choice changed the team ranking in SemEval-2017 Task 4 [opitz2024closerlook](evidence/A-metrics.md#opitz2024closerlook).
- There is no consensus multiclass definition of balanced accuracy [sklearn-modeleval](evidence/A-metrics.md#sklearn-modeleval).

**Worked example 1, imbalance** (derived here). 100 cases: 95 negative, 5 positive.

| System | Accuracy | Positive recall | Positive F1 | Macro F1 | Balanced accuracy |
|---|---|---|---|---|---|
| Always "negative" | **0.95** | 0.00 | 0.00 | 0.487 | 0.50 |
| B: catches 4/5 positives, 10 false alarms | 0.89 | **0.80** | 0.42 | **0.68** | **0.85** |

Accuracy prefers the useless constant predictor. Macro F1 and balanced accuracy prefer B. Whether B's 10 false alarms are acceptable is a cost question (section 13), which no metric here settles.

**Worked example 2, micro vs macro** (derived here). Three classes with support 80/15/5. The system is perfect on the large class, gets 10 of 15 of the middle class and none of the small class (all its errors go to the large class).

| Metric | Value |
|---|---|
| Accuracy (= micro F1) | 0.90 |
| Weighted F1 | 0.87 |
| Macro F1 | **0.58** |

The small class's recall of 0 is invisible in the first two numbers.

## 2. Binary scoring and detection
**Rates** [fawcett2006roc](evidence/A-metrics.md#fawcett2006roc):
- TPR (sensitivity, recall) = TP/P.
- FPR = FP/N = 1 − specificity.
- FNR = 1 − TPR.
- Precision (PPV) = TP/(TP + FP).

TPR and FPR are each computed within one gold class, so they do not depend on prevalence. Precision, accuracy and F1 mix the classes, so they change with prevalence even when the classifier does not [fawcett2006roc](evidence/A-metrics.md#fawcett2006roc).

**Worked example 3, prevalence** (derived here). A detector with TPR 0.90 and FPR 0.05 has precision:

| Prevalence | Precision |
|---|---|
| 50% | 0.95 |
| 10% | 0.67 |
| 1% | 0.15 |

A benchmark built with balanced positives and negatives says little about the false-alarm burden at deployment prevalence. Report rates per gold class and, separately, precision at the assumed deployment prevalence.

**ROC-AUC:**
- It is the probability that a random positive outranks a random negative (Mann–Whitney); random = 0.5 [fawcett2006roc](evidence/A-metrics.md#fawcett2006roc).
- Ties must be averaged. Order-dependent tie handling biases it [fawcett2006roc](evidence/A-metrics.md#fawcett2006roc).
- Quantised probabilities create many ties.

**PR-AUC / average precision:**
- The baseline equals the prevalence [saito2015prc](evidence/A-metrics.md#saito2015prc).
- Linear interpolation between PR points is over-optimistic [davis2006prroc](evidence/A-metrics.md#davis2006prroc) [flach2015prg](evidence/A-metrics.md#flach2015prg).
- Software tools compute AUPRC differently and can rank classifiers differently [chen2024auprctools](evidence/A-metrics.md#chen2024auprctools) (abstract only).

**Conflicting conclusions:**
- **Different curves win.** With 20 positives and 2,000 negatives, one curve wins ROC-AUC (0.875 vs 0.813) while the other wins PR-AUC (0.514 vs 0.038) [davis2006prroc](evidence/A-metrics.md#davis2006prroc).
- **Is PR-AUC better under imbalance? Contested.**
  - Saito & Rehmsmeier argue PR plots are more informative under imbalance [saito2015prc](evidence/A-metrics.md#saito2015prc).
  - McDermott et al. show that AUPRC weights false positives by the inverse firing rate, so it prioritises high-score mistakes. They call the general "AUPRC is better under imbalance" claim overgeneralised [mcdermott2024auroc](evidence/A-metrics.md#mcdermott2024auroc).
  - **Both agree** that the choice should follow the deployment cost structure. For example, PR fits top-k screening with expensive false positives.

**Threshold choice:**
- The optimal operating point depends on class priors and misclassification costs [fawcett2006roc](evidence/A-metrics.md#fawcett2006roc) [elkan2001foundations](evidence/B-probability-abstention.md#elkan2001foundations).
- With calibrated probabilities, the F1-optimal threshold is half the optimal F1, and an uninformative classifier maximises F1 by predicting everything positive [lipton2014f1threshold](evidence/A-metrics.md#lipton2014f1threshold) (abstract only). F1 is therefore a poor target for an operational threshold.
- **Freeze the threshold on development data.** A threshold chosen on test data is optimistically biased.

**Operational error budgets:**
- When the use case states limits, report the operating point that satisfies them. Examples: "at most 1% false approvals" or "at least 95% of out-of-scope requests caught".
- Report FPR at a fixed TPR, or TPR at a fixed FPR [liang2018odin](evidence/B-probability-abstention.md#liang2018odin).
- Report the uncertainty of each rate (statistics note).

## 3. Multilabel
- **Example-based metrics** [zhang2014multilabel](evidence/A-metrics.md#zhang2014multilabel) [sklearn-modeleval](evidence/A-metrics.md#sklearn-modeleval):
  - subset accuracy (exact set match), which is strict when there are many labels;
  - Hamming loss (fraction of wrong case–label pairs);
  - example-based precision, recall and F1 (|Y ∩ h|/|h|, /|Y|);
  - Jaccard |Y ∩ h|/|Y ∪ h|.
- **Label-based metrics:** macro (mean of per-label binary metrics) and micro (pooled counts). Micro accuracy + Hamming loss = 1 [zhang2014multilabel](evidence/A-metrics.md#zhang2014multilabel).
- **Optimising one metric hurts another:** a subset-accuracy-optimal classifier and a Hamming-optimal classifier differ [zhang2014multilabel](evidence/A-metrics.md#zhang2014multilabel). Report more than one.
- **Empty sets.** If both the gold and the predicted set are empty, the example-based ratios are 0/0. scikit-learn sets them to 0 by default, and "conventions vary" [sklearn-modeleval](evidence/A-metrics.md#sklearn-modeleval). A system that correctly predicts "no label applies" can therefore score 0 or 1 depending on convention.
  - Count empty-gold cases separately, or treat "none" as an explicit outcome.
  - A system that cannot output an empty set must be reported as such: this is a capability limit, not a low score.
- **Thresholds.** The predicted set is {y : score(y) > t}, so the threshold drives every set-based metric [zhang2014multilabel](evidence/A-metrics.md#zhang2014multilabel). Fix it on dev data and report it.
- **Cardinality.** Report mean gold and mean predicted label-set size. A systematic difference shows over- or under-labelling that F1 alone hides (derived here).

## 4. Retrieval and ranking
| Metric | Definition | Notes |
|---|---|---|
| P@k | relevant in top k / k | Needs no total-relevant count; unstable, averages poorly [manning2008irbook-ch8](evidence/A-metrics.md#manning2008irbook-ch8) |
| R@k | relevant in top k / all relevant | Needs complete relevance judgments |
| MRR | mean over queries of 1/rank of the first correct item, 0 if none within the cut-off | Few distinct values; no credit for several answers; **no credit for correctly saying there is no answer** [voorhees1999trec8qa](evidence/A-metrics.md#voorhees1999trec8qa) |
| AP / MAP | (1/\|Rel\|) Σ over relevant items of precision at that item's rank; unretrieved relevant items count 0; mean over queries | Binary relevance; varies widely across queries [manning2008irbook-ch8](evidence/A-metrics.md#manning2008irbook-ch8) |
| nDCG@k | DCG@k / ideal DCG@k with graded gain and a log discount | Original: linear gain, discount from rank b, ideal from the full recall base [jarvelin2002cg](evidence/A-metrics.md#jarvelin2002cg). Common variants: exponential gain (2^rel − 1)/log₂(1+m) [manning2008irbook-ch8](evidence/A-metrics.md#manning2008irbook-ch8) or linear gain [sklearn-modeleval](evidence/A-metrics.md#sklearn-modeleval). **Values are comparable only with the same gain, discount and ideal** |

- **Ties.** Arbitrary tie-breaking can change system order. Tie-aware expected values over all permutations of the tied items cost no more to compute [mcsherry2008ties](evidence/A-metrics.md#mcsherry2008ties).
- **Candidate pools and incomplete judgments:**
  - Pooled judgments treat unjudged items as non-relevant [manning2008irbook-ch8](evidence/A-metrics.md#manning2008irbook-ch8).
  - MAP, P@10 and R-precision degrade when judgments are incomplete. bpref uses only judged items [buckley2004bpref](evidence/A-metrics.md#buckley2004bpref).
  - In BEIR's TREC-COVID, dense retrievers had 14–32% of their top-10 unjudged, against 3–6% for lexical systems. Judging the holes moved one dense retriever (ANCE, nDCG@10 0.654 → 0.735) from slightly below BM25 to above it [thakur2021beir](evidence/A-metrics.md#thakur2021beir).
  - **The candidate pool is part of the benchmark,** and a new kind of system can be penalised by how the pool was built.
- **Relevance is task-dependent.** Graded relevance encodes a judgment about the user's need. State the rubric and who applied it (section 9).
- **Ranking derived from a classifier's probabilities** is a different system from a native ranker. Name it as derived.

## 5. Ordinal and regression
- **Scale type.**
  - On an ordinal scale only monotone transforms are admissible, so medians and percentiles are invariant but means are not [stevens1946scales](evidence/A-metrics.md#stevens1946scales).
  - MAE and RMSE treat levels as equally spaced integers (interval assumption) [sakai2021ordinal](evidence/A-metrics.md#sakai2021ordinal).
  - Amigó et al. require "ordinal invariance" and count MAE and weighted κ as violating it [amigo2020cem](evidence/A-metrics.md#amigo2020cem).
  - Sakai considers equidistance acceptable in practice [sakai2021ordinal](evidence/A-metrics.md#sakai2021ordinal). **This disagreement is open.**
- **Metrics:**
  - exact accuracy (ignores error size);
  - accuracy within n levels [amigo2020cem](evidence/A-metrics.md#amigo2020cem);
  - MAE^µ (micro) and macro MAE^M averaged over non-empty gold classes [sakai2021ordinal](evidence/A-metrics.md#sakai2021ordinal);
  - linearly or quadratically weighted κ;
  - Krippendorff's α for ordinal data;
  - CEM^ORD [amigo2020cem](evidence/A-metrics.md#amigo2020cem).
- **Rankings disagree.** Sakai found that accuracy and MAE^µ rank systems very differently from κ, macro F1 and MAE^M. He recommends linear weighted κ as primary unless constant-class runs exist (κ = 0 for any constant predictor), and then α [sakai2021ordinal](evidence/A-metrics.md#sakai2021ordinal).
- **An ordinal label is not an interval quantity.** A "score" type returning an expected level Σ_k p_k·k assumes interval spacing. A per-level distribution does not (derived here).

**Worked example 4** (derived here). Gold levels [0,1,2,3,3,2]:

| System | Predictions | Exact | Within one | MAE |
|---|---|---|---|---|
| A | always one level off | 0.00 | 1.00 | 1.00 |
| B | exact on four, three levels off on one and two on another | 0.67 | 0.67 | 0.83 |

B wins on exact accuracy and MAE. A wins on within-one, and never makes a large error. Which matters depends on whether a two-level error is much worse than a one-level error.

**Out-of-scale outcomes.** A "cannot rate" outcome is not a level. Score it as a separate outcome (section 11), not as a level 0 or a missing value.

## 6. Probabilistic prediction
**Proper scoring rules** [gneiting2007proper](evidence/B-probability-abstention.md#gneiting2007proper) [brocker2009decomposition](evidence/B-probability-abstention.md#brocker2009decomposition):
- A rule is *proper* if reporting one's true belief maximises the expected score.
- **Log loss** (−log p_gold) and **Brier score** are strictly proper.
- Accuracy (zero–one) is proper but not strictly proper. It cannot tell honest probabilities from sharpened ones [gneiting2007proper](evidence/B-probability-abstention.md#gneiting2007proper).
- Brier comes in two forms [gneiting2007proper](evidence/B-probability-abstention.md#gneiting2007proper) [brocker2012empirical](evidence/B-probability-abstention.md#brocker2012empirical). State which one is used:
  - multiclass: Σ_j (p_j − δ_{j,gold})², range 0–2;
  - binary: (p − y)², range 0–1.
- **Uniform-forecast reference values** (derived here):

  | Setting | Log loss | Brier |
  |---|---|---|
  | Binary | 0.693 | 0.25 (binary form) |
  | K classes | ln K | 1 − 1/K (multiclass form) |

  Tasks with different option counts need this reference before their scores are compared.
- **Log loss is unbounded.** p = 0 on the gold label gives infinity, so implementations clip. Report the clipping value. One confident error can dominate a small test set.

**Calibration vs discrimination:**
- **Murphy decomposition:** Brier = reliability − resolution + uncertainty [murphy1973partition](evidence/B-probability-abstention.md#murphy1973partition) [brocker2009decomposition](evidence/B-probability-abstention.md#brocker2009decomposition).
- **Calibration alone is useless without discrimination.** Predicting the base rate is perfectly calibrated and has zero resolution [kumar2019verified](evidence/B-probability-abstention.md#kumar2019verified) [tian2023justask](evidence/B-probability-abstention.md#tian2023justask).
- **AUROC is the opposite.** It measures ranking only and is "indifferent to calibration" [kadavath2022know](evidence/B-probability-abstention.md#kadavath2022know).
- **Proper scores reward both.** A proper score is a mixture of threshold-specific decision costs (Schervish representation) [gneiting2007proper](evidence/B-probability-abstention.md#gneiting2007proper). This is why it fits decisions whose threshold is not yet known.

**Calibration notions**, from strongest to weakest [kull2019dirichlet](evidence/B-probability-abstention.md#kull2019dirichlet) [vaicenavicius2019evaluating](evidence/B-probability-abstention.md#vaicenavicius2019evaluating):
1. **Canonical:** the whole vector is calibrated.
2. **Classwise:** each class's probability is calibrated.
3. **Top-label (confidence):** P(correct | max p = c) = c.

The common ECE [guo2017calibration](evidence/B-probability-abstention.md#guo2017calibration) tests only top-label calibration. A temperature-scaled model can be nearly top-label calibrated yet far from classwise calibrated [kull2019dirichlet](evidence/B-probability-abstention.md#kull2019dirichlet).

**ECE caveats:**
- **Settings differ between papers.** Bins: 10 or 15. Binning: equal-width or equal-mass. Norm: L1 or squared. Labels: top-label or classwise [guo2017calibration](evidence/B-probability-abstention.md#guo2017calibration) [naeini2015bbq](evidence/B-probability-abstention.md#naeini2015bbq) [kadavath2022know](evidence/B-probability-abstention.md#kadavath2022know) [tian2023justask](evidence/B-probability-abstention.md#tian2023justask) [nixon2019measuring](evidence/B-probability-abstention.md#nixon2019measuring). Report all four, because method rankings change with them [nixon2019measuring](evidence/B-probability-abstention.md#nixon2019measuring).
- **Two opposite biases:**
  - binning a continuous model *underestimates* its true calibration error [kumar2019verified](evidence/B-probability-abstention.md#kumar2019verified);
  - the finite-sample plug-in estimate *overestimates* it, most for well-calibrated models [roelofs2022mitigating](evidence/B-probability-abstention.md#roelofs2022mitigating) [kumar2019verified](evidence/B-probability-abstention.md#kumar2019verified).
- **Debiased, sweep, smooth and kernel estimators exist** [roelofs2022mitigating](evidence/B-probability-abstention.md#roelofs2022mitigating) [blasiok2023smoothece](evidence/B-probability-abstention.md#blasiok2023smoothece). ECE is also discontinuous at zero [blasiok2023unifying](evidence/B-probability-abstention.md#blasiok2023unifying).
- **With tens to a few hundred cases, a binned ECE is mostly noise** (derived here from the biases above). Prefer:
  - a proper score with an interval;
  - a reliability table that shows counts per bin;
  - a calibration test [vaicenavicius2019evaluating](evidence/B-probability-abstention.md#vaicenavicius2019evaluating).

**Post-hoc recalibration:**
- Temperature or Platt scaling, fitted on held-out data, does not change the argmax [guo2017calibration](evidence/B-probability-abstention.md#guo2017calibration).
- **A temperature fitted on the test set measures calibratability, not deployed calibration.** For example, Tian et al.'s ECE-t is fitted on the evaluation data [tian2023justask](evidence/B-probability-abstention.md#tian2023justask).

## 7. Abstention and selective prediction
**Classical form:**
- A selective classifier answers only when g(x) = 1 [geifman2017selective](evidence/B-probability-abstention.md#geifman2017selective).
- Coverage φ = E[g].
- Selective risk = E[loss · g] / φ.
- The risk–coverage curve traces the tradeoff, with AURC as its area.
- E-AURC subtracts the area of an oracle ranking, because AURC also depends on base accuracy [geifman2019biasreduced](evidence/B-probability-abstention.md#geifman2019biasreduced).
- Chow's rule: with a rejection cost c_r, reject when max p < 1 − c_r [chow1970optimum](evidence/B-probability-abstention.md#chow1970optimum) (abstract; the rule is a standard derivation).

**Ranking vs calibration.** Selective-prediction metrics depend only on the *order* of confidences, while calibration depends on their absolute values [kamath2020selective](evidence/B-probability-abstention.md#kamath2020selective). A system can have a good risk–coverage curve and poor ECE, or the reverse.

**Three different questions** [wen2024knowyourlimits](evidence/B-probability-abstention.md#wen2024knowyourlimits) [yang2024generalizedood](evidence/B-probability-abstention.md#yang2024generalizedood):

| Question | Property of | Ground truth needed | Example data |
|---|---|---|---|
| **Answerability / scope**: can this input be answered from what is given, or is it within the task? | the input | a per-case "answerable/in scope" label | SQuAD 2.0 unanswerables [rajpurkar2018squad2](evidence/B-probability-abstention.md#rajpurkar2018squad2); CLINC150 out-of-scope [larson2019clinc](evidence/B-probability-abstention.md#larson2019clinc) |
| **Correctness confidence**: will this system's answer be right? | the system–input pair | correctness of the system's own answer | misclassification detection [hendrycks2017baseline](evidence/B-probability-abstention.md#hendrycks2017baseline); P(True)/P(IK) [kadavath2022know](evidence/B-probability-abstention.md#kadavath2022know) |
| **Distribution shift**: is this input unlike the training/evaluation population? | the input distribution | in-/out-of-distribution membership | OOD benchmarks [yang2024generalizedood](evidence/B-probability-abstention.md#yang2024generalizedood) |

These are often conflated. Wen et al.'s abstention recall counts wrong answers on answerable questions as "should have abstained", which mixes the first two questions [wen2024knowyourlimits](evidence/B-probability-abstention.md#wen2024knowyourlimits).

**A typed fallback label should be scored against the matching ground truth** (derived here). Examples: out of scope, no matching candidate, missing evidence, conflicting evidence. A low-confidence gate should be scored on correctness.

**Metrics for an explicit abstain outcome** [wen2024knowyourlimits](evidence/B-probability-abstention.md#wen2024knowyourlimits) [feng2024abstain](evidence/B-probability-abstention.md#feng2024abstain):
- coverage;
- abstention precision and recall;
- reliable accuracy (accuracy among answered cases);
- effective reliability: (correct − wrong) / N, which treats a wrong answer as worse than an abstention.

**Always-abstain and always-answer must be reported as baselines:**
- In SQuAD 2.0, abstaining scores 1 on unanswerable items, and always abstaining reaches 48.9 test F1 [rajpurkar2018squad2](evidence/B-probability-abstention.md#rajpurkar2018squad2).
- Conversely, under 0/1 grading with no credit for "I don't know", answering is always optimal [kalai2025why](evidence/B-probability-abstention.md#kalai2025why) (preprint by OpenAI-affiliated authors). Nine of ten popular benchmarks they inspected grade this way. The confidence target t with penalty t/(1−t) makes the intended abstention policy explicit [kalai2025why](evidence/B-probability-abstention.md#kalai2025why) (preprint).
- MRR gives no credit for knowing there is no answer [voorhees1999trec8qa](evidence/A-metrics.md#voorhees1999trec8qa).

**Out-of-scope detection metrics:**
- AUROC, AUPR-In and AUPR-Out [hendrycks2017baseline](evidence/B-probability-abstention.md#hendrycks2017baseline);
- FPR at 95% TPR [liang2018odin](evidence/B-probability-abstention.md#liang2018odin);
- out-of-scope recall plus in-scope accuracy [larson2019clinc](evidence/B-probability-abstention.md#larson2019clinc).

**Tuning on the out-of-scope family being tested is optimistic.** ODIN tuned on an OOD validation set, and CLINC150's threshold baseline was tuned on validation data that contains out-of-scope queries [liang2018odin](evidence/B-probability-abstention.md#liang2018odin) [larson2019clinc](evidence/B-probability-abstention.md#larson2019clinc).

**Conformal prediction** gives distribution-free marginal coverage of prediction sets under exchangeability [angelopoulos2021gentle](evidence/B-probability-abstention.md#angelopoulos2021gentle). It is not conditional coverage, and it is not valid under distribution shift.

## 8. Generated and structured outputs
**Three levels of correctness** (synthesis of [openai_structured_outputs](evidence/C-judging-structured.md#openai_structured_outputs) [geng2025jsonschemabench](evidence/C-judging-structured.md#geng2025jsonschemabench)):
1. The output parses.
2. The output conforms to the schema.
3. The values are semantically right.

Constrained decoding guarantees the first two only for the schema features the engine supports [geng2025jsonschemabench](evidence/C-judging-structured.md#geng2025jsonschemabench). Schema-valid output "can still contain mistakes" [openai_structured_outputs](evidence/C-judging-structured.md#openai_structured_outputs). Truncation and refusals bypass the guarantee, so check `finish_reason` and refusal fields [openai_structured_outputs](evidence/C-judging-structured.md#openai_structured_outputs).

**The parser can decide the score:**
- On GSM8K, a strict regex and an LLM extractor differed by 32–44 points for the same outputs [tam2024speakfreely](evidence/C-judging-structured.md#tam2024speakfreely).
- lm-evaluation-harness reports `strict-match` and `flexible-extract` side by side, and scores an unparseable output as `[invalid]` = wrong [lmeval_harness_filters](evidence/C-judging-structured.md#lmeval_harness_filters).
- Other tools handle failures differently. JUDGE-BENCH replaces invalid outputs with a random label [bavaresco2024judgebench](evidence/C-judging-structured.md#bavaresco2024judgebench). The SQuAD v2 script silently skips missing predictions, so n shrinks [squad_eval_scripts](evidence/C-judging-structured.md#squad_eval_scripts).

**Effect of format constraints on quality is contested:**
- Tam et al. found strict formats hurt reasoning but not classification [tam2024speakfreely](evidence/C-judging-structured.md#tam2024speakfreely).
- A vendor response [kurt2024saywhatyoumean](evidence/C-judging-structured.md#kurt2024saywhatyoumean) and JSONSchemaBench [geng2025jsonschemabench](evidence/C-judging-structured.md#geng2025jsonschemabench) (several authors develop a constrained-decoding library; it reused the vendor's prompts) found parity or small gains once prompts were matched.
- **Agreed confounders:** prompt parity, a schema description in the prompt, field order (reasoning before answer), and the answer parser.

**Acceptable answers:**
- **SQuAD scoring:**
  - normalises (lower-case, strip punctuation and articles);
  - takes the best match over several references;
  - scores token-overlap F1 [rajpurkar2016squad](evidence/C-judging-structured.md#rajpurkar2016squad) [squad_eval_scripts](evidence/C-judging-structured.md#squad_eval_scripts).
- **Lexical matching undercounts long answers.** Human re-judging moved one zero-shot system from 12.6% to 71.4%. More than half of the lexical "failures" were equivalent answers [kamalloo2023odqa](evidence/C-judging-structured.md#kamalloo2023odqa).
- **For closed option sets, the answer key is the label and equivalence is not an issue.** For free text, define an acceptable-answer set before scoring.

**Repair and retries** (no source formally specifies this; synthesis here). Report three quantities:
1. first-pass validity;
2. validity after repair or retry;
3. correctness among valid outputs.

End-to-end success is correct-and-valid over all attempts made. Count the extra calls in latency and cost. A repaired output should never be reported as if it were first-pass.

## 9. Human or model judging
**Agreement coefficients:**
- **Forms.** S, π (Scott), κ (Cohen) and Fleiss's multi-rater coefficient are all (A_o − A_e)/(1 − A_e) and differ only in the chance model [artstein2008agreement](evidence/C-judging-structured.md#artstein2008agreement) [fleiss1971](evidence/C-judging-structured.md#fleiss1971).
- **Krippendorff's α** = 1 − D_o/D_e:
  - handles any number of coders, missing data and ordinal or interval distances [krippendorff2011computing](evidence/C-judging-structured.md#krippendorff2011computing);
  - 0.8 is often cited as a minimum and 0.667 as tentative, with no universal cutoff [artstein2008agreement](evidence/C-judging-structured.md#artstein2008agreement).
- **Prevalence paradox.** With skewed categories, κ can be low even when raw agreement is high [feinstein1990paradox](evidence/C-judging-structured.md#feinstein1990paradox). Artstein & Poesio argue this is correct, because reliability needs agreement on the rare category [artstein2008agreement](evidence/C-judging-structured.md#artstein2008agreement).
- **Report:** number of coders, whether coding was independent, the guideline version, and the agreement table [artstein2008agreement](evidence/C-judging-structured.md#artstein2008agreement).

**Disagreement is not always error:**
- **Disagreement persists:** NLI disagreements remain at 50 raters per item [pavlick2019inherent](evidence/C-judging-structured.md#pavlick2019inherent).
- **Majority labels change:** with 100 annotations, the majority label changed on 10–32% of selected low-agreement items [nie2020chaosnli](evidence/C-judging-structured.md#nie2020chaosnli).
- **Soft evaluation** compares a model's distribution to the human label distribution, using cross-entropy or Jensen–Shannon divergence [uma2021disagreement](evidence/C-judging-structured.md#uma2021disagreement) [plank2022hlv](evidence/C-judging-structured.md#plank2022hlv).
- **Label errors are a separate issue:** at least 3.3% of test labels across ten benchmarks were wrong, enough to flip model rankings [northcutt2021labelerrors](evidence/C-judging-structured.md#northcutt2021labelerrors).

**Model judges:**
- **Biases:**
  - Position: GPT-4 kept its verdict on 65% of position swaps [zheng2023mtbench](evidence/C-judging-structured.md#zheng2023mtbench). Order alone could make one model "win" 66 of 80 queries [wang2023notfair](evidence/C-judging-structured.md#wang2023notfair).
  - Verbosity [zheng2023mtbench](evidence/C-judging-structured.md#zheng2023mtbench).
  - Self-preference, which is linked to self-recognition [panickssery2024selfpref](evidence/C-judging-structured.md#panickssery2024selfpref).
  - Leniency [thakur2024judges](evidence/C-judging-structured.md#thakur2024judges).
- **Agreement depends on tie handling.** GPT-4 agrees with humans 85% without ties and 66% with them. Human–human agreement is 81% and 63% [zheng2023mtbench](evidence/C-judging-structured.md#zheng2023mtbench).
- **High percent agreement can hide 10–20-point score shifts** [thakur2024judges](evidence/C-judging-structured.md#thakur2024judges).
- **Validate against in-domain human labels before use.** Judge quality varies widely by task [bavaresco2024judgebench](evidence/C-judging-structured.md#bavaresco2024judgebench) [thakur2024judges](evidence/C-judging-structured.md#thakur2024judges).
- **Mitigations:**
  - judge in both orders and count a win only if it holds in both;
  - give the rationale before the score;
  - use reference answers [zheng2023mtbench](evidence/C-judging-structured.md#zheng2023mtbench) [wang2023notfair](evidence/C-judging-structured.md#wang2023notfair).
- **Pairwise preferences** are aggregated with Bradley–Terry plus robust or bootstrap intervals [chiang2024arena](evidence/C-judging-structured.md#chiang2024arena).

**Related-model audits.** A model of the same family as the evaluated systems is a correlated annotator. Its agreement shows that the labels are consistent with that family's reading, not that they are valid for people (derived here; see [data-and-validity.md](data-and-validity.md)).

## 10. Utility and cost
- **Bayes decision with a cost matrix** [elkan2001foundations](evidence/B-probability-abstention.md#elkan2001foundations):
  - Minimise Σ_j P(j|x) C(i, j).
  - With two classes, act when p ≥ c_FP / (c_FP + c_FN), taking correct decisions as zero-cost.
  - Costs and benefits must be measured from one baseline.
  - Miscalibration moves the decision boundary.
- **Cost curves** plot normalised expected cost against the probability–cost tradeoff over all priors and cost ratios [drummond2006costcurves](evidence/B-probability-abstention.md#drummond2006costcurves).
- **Decision-curve analysis** plots net benefit NB = TP/n − FP/n · p_t/(1 − p_t) over a range of thresholds, against "act on all" and "act on none" [vickers2006dca](evidence/B-probability-abstention.md#vickers2006dca). It is a template for showing value when the exact cost ratio is uncertain.
- **Review and escalation cost.** A deferral is not free. Its cost (human review time, delay) belongs in the matrix next to false acceptances and false rejections (derived here).
- **Quality and resources together.**
  - Leaderboards that ignore cost (size, energy, latency) do not reflect user utility [ethayarajh2020utility](evidence/E-statistics-aggregation.md#ethayarajh2020utility).
  - When no cost ratio between quality and resources is agreed, report the **Pareto front** (systems not dominated on both quality and cost) rather than a weighted sum (derived here).
  - Measurement details are in [performance-and-cost.md](performance-and-cost.md).

## 11. Outcome accounting: what each case's result *is*
These outcomes need different labels or different accounting:

| Outcome | What happened | Counted as |
|---|---|---|
| Correct substantive answer | gold is substantive, the answer matches | correct |
| Wrong substantive answer | gold is substantive, a different substantive answer | error (a selection error) |
| **False rejection** | gold is substantive, the system declined or chose a fallback | error, reported separately |
| **False acceptance** | gold is a fallback, the system chose a substantive answer | error, reported separately; often the costliest |
| Correct fallback, right class | e.g. gold `missing_evidence`, answer `missing_evidence` | correct |
| Wrong fallback class | e.g. gold `conflicting_evidence`, answer `missing_evidence` | partly right; report separately |
| **Execution failure** | timeout, crash, transport error, invalid output | error in every denominator; **never** a correct rejection |
| **Unsupported** | the system documents that it cannot accept this input type or size | excluded from quality, counted in capability coverage |
| Truncated input | decisive content cut before the model saw it | execution defect; report it |

**Fallback classes** need separate gold labels because they have different causes and different remedies:
- **Out of scope:** the input is not an instance of the task. The remedy is routing.
- **No matching candidate:** the input is on-task, but the correct option was not offered. The remedy is the candidate set.
- **Missing information:** a decisive fact is absent. The remedy is to ask for it.
- **Contradiction:** the sources disagree and no rule resolves them. The remedy is to reconcile them.

Pooling them into one "rejection rate" hides which mechanism fails (derived here; compare the three abstention questions in section 7). Explicitly *unknown*, *false*, *empty* and *absent* values are different facts, and the label definitions must say how each is treated.

**Why execution failures must not count as rejections.** Otherwise a system that fails on hard inputs is rewarded on exactly the cases where a fallback is the gold label. Coverage (the share of inputs handled at all) and quality (correctness on handled inputs) are reported side by side, never multiplied away (derived here; see [robustness-and-execution.md](robustness-and-execution.md)).

## 12. Scores, probabilities and calibrated correctness
| Kind of number | What it supports | What it does not support |
|---|---|---|
| **Arbitrary score** (logit, similarity, verbalised 0–100 value, judge score) | ranking metrics: AUROC, AP, risk–coverage, nDCG | log loss, Brier, ECE (unless mapped to [0, 1] and validated as probabilities) [kadavath2022know](evidence/B-probability-abstention.md#kadavath2022know) [kamath2020selective](evidence/B-probability-abstention.md#kamath2020selective) |
| **Normalised distribution over the offered options** | proper scores and calibration *conditional on that option set* | comparison with another option set: renormalising over candidates changes the numbers, and adding an option changes all of them [jiang2021know](evidence/B-probability-abstention.md#jiang2021know) |
| **Calibrated correctness estimate** (validated on held-out data from the target population) | thresholds, expected cost, routing | transfer to a different population without re-checking [kamath2020selective](evidence/B-probability-abstention.md#kamath2020selective) [angelopoulos2021gentle](evidence/B-probability-abstention.md#angelopoulos2021gentle) |

**Likelihood-based metrics cannot be applied when:**
- the system returns no probabilities: an API without log-probabilities, or a validated JSON choice;
- the output is free text, where the string's likelihood is not the probability of being correct [kalai2025why](evidence/B-probability-abstention.md#kalai2025why);
- the system returns "I don't know";
- confidence is verbalised as exactly 0 or 1, where log loss is infinite unless clipped.

Do not invent a confidence for such systems. Report them on the metrics they support.

**Probabilities from different readouts are not interchangeable**:
- **Readout examples:**
  - softmax over option-letter logits at some temperature;
  - a pointer or readout head with a fitted temperature;
  - an encoder's label softmax;
  - per-label sigmoid scores.
- **A proper score on each system's own probabilities is legitimate per system.**
- **Comparing these scores across systems compares readout and calibration choices as much as decision quality** (derived here).
- **Accuracy and risk–coverage comparisons** need only the decisions and confidence orderings, so they are safer to compare.

## 13. Tradeoffs that need an intended use
No metric resolves these without a stated use and cost model. A benchmark should report the components and the curve, and leave the weighting to the decision it serves:
1. **False acceptance vs false rejection.** Their relative cost decides the threshold, the abstention policy and whether a high-coverage or a high-precision system is better.
2. **Macro vs micro.** Is a rare class as important as a frequent one?
3. **Coverage vs selective risk.** How much deferral is affordable?
4. **Exact vs near-miss on ordinal labels.** How much worse is a two-level error than a one-level error?
5. **Quality vs latency, memory and cost.** What is a point of accuracy worth in milliseconds or gigabytes?
6. **Calibration vs discrimination.** Do probabilities feed thresholds and expected cost, or are they only used to rank?
7. **Per-task results vs an aggregate.** Which tasks are in the workload, in what proportions? Aggregation is discussed in [statistics-and-comparison.md](statistics-and-comparison.md).

## Worked examples where metrics disagree
| # | Situation | Metric A says | Metric B says | Source |
|---|---|---|---|---|
| 1 | 95/5 imbalance, constant predictor | accuracy 0.95 | macro F1 0.49, balanced accuracy 0.50, minority recall 0 | derived here (section 1) |
| 2 | 80/15/5 classes, smallest class never predicted | accuracy 0.90, weighted F1 0.87 | macro F1 0.58 | derived here (section 1) |
| 3 | Same detector at different prevalences | TPR 0.90, FPR 0.05 unchanged | precision 0.95 → 0.15 | derived here (section 2) |
| 4 | Two ROC/PR curves, 20 vs 2,000 | ROC-AUC prefers II (0.875) | PR-AUC prefers I (0.514 vs 0.038) | [davis2006prroc](evidence/A-metrics.md#davis2006prroc) |
| 5 | Same confusion matrix | accuracy 0.90, F1 0.95 | MCC −0.03 | [chicco2020mcc](evidence/A-metrics.md#chicco2020mcc) |
| 6 | Four correct-label probabilities: A = 0.55 each; B = 0.99, 0.99, 0.99, 0.40 | accuracy: A 1.00 > B 0.75 | Brier (binary): B 0.090 < A 0.203; log loss B 0.24 < A 0.60 | derived here |
| 7 | Ordinal: always off by one vs mostly exact with large misses | exact: B 0.67 > A 0 | within-one: A 1.00 > B 0.67 | derived here (section 5) |
| 8 | System that always chooses the fallback on 24 substantive + 16 fallback cases | fallback recall 1.0 | substantive accuracy 0; fallback precision 0.40 | derived here |
| 9 | Calibrated system: p = 0.6 on 80% of cases, 0.95 on 20% | ECE ≈ 0 | full-coverage accuracy 0.67; at threshold 0.9 coverage only 20% (risk 5%) | derived here |
| 10 | Two macro F1 definitions on the same pair of classifiers | F1 of averages ranks one way | averaged F1 ranks the other way | [opitz2019macrof1](evidence/A-metrics.md#opitz2019macrof1) |

Example 8 is the pattern behind a "strong rejection" that is really fallback bias. Example 9 shows that good calibration and useful coverage are different properties. Further worked conflicts (valid JSON with wrong meaning, strong synthetic but weak independent results) are in [frameworks-and-benchmarks.md](frameworks-and-benchmarks.md).
