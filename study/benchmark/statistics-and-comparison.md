# Uncertainty, comparison and aggregation

How to attach uncertainty to evaluation results, compare systems on the same cases, and combine results across tasks. Written 2026-10-02 in step5 of [benchmark/p1](../../devdocs/episodes/benchmark/p1/plan.md). Citations link to [evidence/](evidence/). **"(derived here)"** marks arithmetic or synthesis made for this note.

## 1. What varies, and what the interval is about
An evaluation score varies for several separate reasons:

| Source of variation | Applies when | How to capture it |
|---|---|---|
| **Item sampling**: which cases ended up in the test set | Always, if the claim is about a population of cases | Interval over items (binomial, bootstrap over items) [miller2024errorbars](evidence/E-statistics-aggregation.md#miller2024errorbars) |
| **Within-item stochasticity**: sampling temperature, judge randomness, nondeterministic serving | Generation at T > 0; LLM judges; shared servers [he2025nondeterminism](evidence/F-robustness-frameworks-perf.md#he2025nondeterminism) | Repeat each item K times, average within the item, then compute the interval across items [miller2024errorbars](evidence/E-statistics-aggregation.md#miller2024errorbars) |
| **Training or configuration randomness**: seeds, hyperparameters, prompt choice | When the claim is about a training method or a design, not one frozen artefact | Several runs or configurations; score distributions [bouthillier2021variance](evidence/E-statistics-aggregation.md#bouthillier2021variance) [reimers2017distributions](evidence/E-statistics-aggregation.md#reimers2017distributions) |
| **Clustering**: several items derived from one source | Variants, translations, passages with several questions | Clustered standard errors or cluster bootstrap (section 4) |

- **Different intervals answer different questions.** A bootstrap over items answers "how much would the score change if the questions were resampled", not run-to-run variation [biderman2024lessons](evidence/F-robustness-frameworks-perf.md#biderman2024lessons).
- **For a frozen system on a frozen test set,** only item sampling and within-item stochasticity apply. Training-variance methods such as 5×2cv address another question [dietterich1998tests](evidence/E-statistics-aggregation.md#dietterich1998tests).
- **Pooling K·N repeated answers as if independent is wrong** [miller2024errorbars](evidence/E-statistics-aggregation.md#miller2024errorbars).
- **Lowering temperature only to reduce variance** can bias the estimate. Miller's advice is "don't touch the thermostat" [miller2024errorbars](evidence/E-statistics-aggregation.md#miller2024errorbars).
- **Prefer continuous per-item scores where they exist.** The probability of the gold answer and NLL have higher signal-to-noise than 0/1 accuracy [madaan2024variance](evidence/E-statistics-aggregation.md#madaan2024variance) [heineman2025signalnoise](evidence/E-statistics-aggregation.md#heineman2025signalnoise) (the second at abstract level).

## 2. Intervals for one proportion
- **Wald** (p̂ ± z√(p̂(1−p̂)/n)):
  - coverage is erratic [brown2001binomial](evidence/E-statistics-aggregation.md#brown2001binomial) (abstract);
  - width collapses to 0 at 0/n or n/n, and the interval can leave [0, 1] [bowyer2025clt](evidence/E-statistics-aggregation.md#bowyer2025clt);
  - **do not use it for small cells.**
- **Wilson score interval:** [p̂ + z²/2n ± (z/2n)√(4np̂(1−p̂) + z²)] / (1 + z²/n) [wilson1927](evidence/E-statistics-aggregation.md#wilson1927) (formula via [bowyer2025clt](evidence/E-statistics-aggregation.md#bowyer2025clt)).
  - Recommended for small n [brown2001binomial](evidence/E-statistics-aggregation.md#brown2001binomial).
  - Near-nominal coverage down to N = 3–10 in simulation [bowyer2025clt](evidence/E-statistics-aggregation.md#bowyer2025clt).
  - Built into Inspect's metrics [inspect-docs](evidence/F-robustness-frameworks-perf.md#inspect-docs).
- **Clopper–Pearson ("exact"):**
  - coverage is at least nominal, but the interval is conservative [bowyer2025clt](evidence/E-statistics-aggregation.md#bowyer2025clt);
  - for 0 successes in n, the upper limit is 1 − (α/2)^(1/n). The rule of three, 3/n, approximates the one-sided 95% bound (derived here).
- **Bayesian Beta(1 + k, 1 + n − k)** behaves like Wilson in practice [bowyer2025clt](evidence/E-statistics-aggregation.md#bowyer2025clt).
- **The CLT and percentile bootstrap under-cover below a few hundred items.** A nominal 95% CLT interval covered about 92.5% at N = 100 [bowyer2025clt](evidence/E-statistics-aggregation.md#bowyer2025clt). Their simulation averages over a uniform prior, which favours the Bayesian method they recommend, so treat the exact numbers with care.

**Worked numbers** (derived here):

| Observation | 95% interval |
|---|---|
| 24/24 | Wilson [0.86, 1.00] |
| 23/24 | Wilson [0.80, 0.99] |
| 0 errors among 110 accepted answers | Clopper–Pearson upper bound 3.3%, Wilson upper bound 3.4% |
| 0 errors in 24 | Clopper–Pearson upper bound 14% |

"0% risk" on about a hundred cases is compatible with a true risk of about 3%.

**For metrics that are not a single proportion** (macro F1, nDCG, Brier):
- use a bootstrap over items, or a Bayesian model, and report the method;
- the bootstrap under-covers at small n for F1 too [bowyer2025clt](evidence/E-statistics-aggregation.md#bowyer2025clt).

## 3. Comparing two systems on the same cases
**Pair the comparison.**
- When both systems answer the same cases, the variance of the difference shrinks by the covariance: Var_paired = Var_unpaired − 2Cov/n [miller2024errorbars](evidence/E-statistics-aggregation.md#miller2024errorbars).
- Correlated systems reach significance with smaller gains [berg2012empirical](evidence/E-statistics-aggregation.md#berg2012empirical).
- Power depends on how often the systems agree [card2020power](evidence/E-statistics-aggregation.md#card2020power).
- **An unpaired test on paired data wastes this power and is the wrong model.**

**Methods:**

| Method | Statistic | Use | Caveats |
|---|---|---|---|
| **McNemar** (paired binary outcomes) | Uses only discordant counts b (A right, B wrong) and c. Asymptotic z = (b − c)/√(b + c). Exact conditional: b ~ Bin(b + c, ½) under H0 [fagerland2013mcnemar](evidence/E-statistics-aggregation.md#fagerland2013mcnemar) | Two systems, one correct/incorrect outcome per case | Exact conditional and continuity-corrected versions are very conservative. The **mid-p** version never exceeded the nominal level in 9,595 scenarios and is recommended [fagerland2013mcnemar](evidence/E-statistics-aggregation.md#fagerland2013mcnemar). Dietterich found McNemar to have low type-I error for single-run comparisons [dietterich1998tests](evidence/E-statistics-aggregation.md#dietterich1998tests) (abstract) |
| **Paired bootstrap** | Resample items with replacement, recompute the metric for both systems, recentre at the null [koehn2004bootstrap](evidence/E-statistics-aggregation.md#koehn2004bootstrap) [berg2012empirical](evidence/E-statistics-aggregation.md#berg2012empirical) | Any metric, including non-decomposable ones | Anti-conservative at small n; one study uses it only above n = 200 [sogaard2014pvalue](evidence/E-statistics-aggregation.md#sogaard2014pvalue) [dror2018hitchhiker](evidence/E-statistics-aggregation.md#dror2018hitchhiker) |
| **Approximate randomization (permutation)** | Swap the two systems' outputs per item with probability ½; p = (c + 1)/(R + 1) [riezler2005pitfalls](evidence/E-statistics-aggregation.md#riezler2005pitfalls) | Any metric; conditions on the test set | More conservative than the bootstrap. Its inference is about *this* test set, while the bootstrap targets a population. Berg-Kirkpatrick et al. prefer the bootstrap for that reason [berg2012empirical](evidence/E-statistics-aggregation.md#berg2012empirical) |
| **Paired difference with SE** | Mean per-item difference, SE = √(Var(s_A − s_B)/n), 95% CI [miller2024errorbars](evidence/E-statistics-aggregation.md#miller2024errorbars) | Large n, continuous or binary scores | CLT-based; under-covers at small n [bowyer2025clt](evidence/E-statistics-aggregation.md#bowyer2025clt) |
| **Bayesian paired model** | Posterior of the difference [bowyer2025clt](evidence/E-statistics-aggregation.md#bowyer2025clt), or a correlated t-test with a region of practical equivalence [benavoli2017bayesian](evidence/E-statistics-aggregation.md#benavoli2017bayesian) | Small n; direct probability statements | Prior and ROPE are choices to report |

**Report the effect size, not only the p-value.**
- Miller recommends reporting four things [miller2024errorbars](evidence/E-statistics-aggregation.md#miller2024errorbars):
  1. the difference;
  2. its standard error;
  3. its 95% interval;
  4. the correlation between the two systems' scores.
- For McNemar, report b and c themselves.

**What tiny discordant counts can show** (derived here; exact two-sided McNemar):

| Discordant split (b vs c) | Exact p | Mid-p |
|---|---|---|
| 5 vs 1 | 0.22 | 0.13 |
| 5 vs 0 | 0.06 | 0.03 |
| 6 vs 0 | 0.03 | 0.02 |
| 9 vs 0 | 0.004 | 0.002 |

Under a Holm correction over ten such tests, the smallest p must be below 0.005. With exact tests, that needs at least nine discordant cases all in one direction. In that family, a comparison with five or fewer discordant pairs cannot reach significance at that level, whatever the true difference.

## 4. Dependent cases and grouped resampling
- **Clustered items are not independent.** Several cases derived from one base share information and errors. Examples: paraphrases, option reorderings, translations, complete/incomplete pairs, several questions on one passage.
- **Naive standard errors can be several times too small.** The clustered/naive SE ratio was 3.05 on DROP and 1.88 on MGSM [miller2024errorbars](evidence/E-statistics-aggregation.md#miller2024errorbars). The Moulton factor 1 + ρ(N̄_g − 1) gives the inflation for a mean, where the regressor correlation is 1 (the general form is 1 + ρ_x ρ_u (N̄_g − 1)) [cameron2015cluster](evidence/E-statistics-aggregation.md#cameron2015cluster).
- **Methods:**
  - **clustered SE** [miller2024errorbars](evidence/E-statistics-aggregation.md#miller2024errorbars);
  - **cluster bootstrap**, which resamples whole clusters, never individual items [cameron2015cluster](evidence/E-statistics-aggregation.md#cameron2015cluster) [field2007clustered](evidence/E-statistics-aggregation.md#field2007clustered);
  - **stratified bootstrap across tasks** [agarwal2021precipice](evidence/E-statistics-aggregation.md#agarwal2021precipice).
- **Few clusters** (fewer than about 20–50) make cluster-robust tests over-reject. The rejection rate at a nominal 5% was 0.208 with five clusters [cameron2015cluster](evidence/E-statistics-aggregation.md#cameron2015cluster). Small-sample corrections help but do not remove this. For very few clusters, a hierarchical (beta-binomial) model was the only method that covered in simulation [bowyer2025clt](evidence/E-statistics-aggregation.md#bowyer2025clt).
- **Paired variants are better analysed as pairs** (derived here):
  - report the per-pair outcome ("both right", "changed answer"), as GSM-IC's macro accuracy counts a base problem as solved only when all its variants are [shi2023gsmic](evidence/F-robustness-frameworks-perf.md#shi2023gsmic);
  - or count the base case as the unit and the variants as repeated measures.
- **Count the pairs, not the variants.** Three variants of 12 base cases are 12 independent units, not 36.

## 5. Power and sample size
- **Definition.** Power is the probability of detecting an effect that exists.
- **Underpowered studies are common and exaggerate significant effects** (type-M error) [card2020power](evidence/E-statistics-aggregation.md#card2020power):
  - only 46% of surveyed GLUE state-of-the-art comparisons were predicted to be adequately powered;
  - in machine translation, 2,000 sentences give about 75% power for a 1-BLEU difference.
- **Closed-form sample size** [miller2024errorbars](evidence/E-statistics-aggregation.md#miller2024errorbars):
  - n = (z_{α/2} + z_β)² (ω² + σ_A²/K_A + σ_B²/K_B) / δ², where ω² = Var(x_A) + Var(x_B) − 2Cov(x_A, x_B).
  - Miller's example (ω² = 1/9, δ = 3 points) gives about 1,000 questions. That figure depends on its assumptions and is not a general law.
- **For paired binary outcomes,** ω² ≈ d − δ², where d is the discordance rate (derived here). With 80% power at α = 0.05:

  | Discordance d | Accuracy difference δ | Paired cases needed |
  |---|---|---|
  | 8% | 5 points | ~240 |
  | 8% | 3 points | ~690 |

  With 10% discordance, the minimum detectable difference is roughly:

  | n | Minimum detectable difference |
  |---|---|
  | 24 | 16 points |
  | 120 | 8 points |
  | 200 | 6 points |

  These are CLT approximations, optimistic at small n [bowyer2025clt](evidence/E-statistics-aggregation.md#bowyer2025clt). Simulate with the planned exact or mid-p test when cells are small [card2020power](evidence/E-statistics-aggregation.md#card2020power).
- **Equivalence and non-inferiority sample sizes grow sharply as the margin tightens.** Example: 1,048 vs 26,185 per group for margins of 10 vs 6 points [walker2011equivalence](evidence/E-statistics-aggregation.md#walker2011equivalence).

## 6. Multiplicity and preregistration
- **Many tests, metrics or slices inflate false positives.**
- **Family-wise error control:**
  - Holm's step-down procedure: compare the i-th smallest p with α/(m − i + 1). It is uniformly more powerful than Bonferroni and needs no dependence assumption [holm1979](evidence/E-statistics-aggregation.md#holm1979) (via [demsar2006](evidence/E-statistics-aggregation.md#demsar2006)).
  - FDR control (Benjamini–Hochberg) is less strict and is proved for independent statistics [benjamini1995fdr](evidence/E-statistics-aggregation.md#benjamini1995fdr) (abstract).
- **Practice evidence:**
  - Only 3 of 110 multi-dataset ACL 2017 papers corrected for multiplicity [dror2018hitchhiker](evidence/E-statistics-aggregation.md#dror2018hitchhiker).
  - Søgaard et al. argue that a cut-off near 0.0025 is needed to keep false positives below 5% [sogaard2014pvalue](evidence/E-statistics-aggregation.md#sogaard2014pvalue).
  - Multiple metrics are a hidden source of multiplicity [sogaard2014pvalue](evidence/E-statistics-aggregation.md#sogaard2014pvalue).
- **Preregistration** [vanmiltenburg2021prereg](evidence/E-statistics-aggregation.md#vanmiltenburg2021prereg):
  - **What to fix before collecting data:** hypotheses, dependent variables, conditions, exact analyses, exclusions, sample size and stopping rule.
  - **Report deviations.**
  - **Fix the family of tests to be corrected in advance.** Only those are confirmatory; everything else is exploratory.

## 7. Absence of evidence, equivalence and non-inferiority
- **"Not significant" does not mean "no difference"** [altman1995absence](evidence/E-statistics-aggregation.md#altman1995absence) [lakens2017equivalence](evidence/E-statistics-aggregation.md#lakens2017equivalence).
- **Equivalence (TOST)** [lakens2017equivalence](evidence/E-statistics-aggregation.md#lakens2017equivalence) [walker2011equivalence](evidence/E-statistics-aggregation.md#walker2011equivalence):
  - **Fix the bounds in advance.** Set a smallest effect size of interest ±Δ before seeing the data.
  - **Conclude equivalence** only when the 90% CI of the difference (for α = .05) lies inside the bounds.
  - **Four outcomes are possible:** different; equivalent; different but trivially small; undetermined.
- **Non-inferiority:** the lower limit of the (1 − 2α) CI of (new − reference) must lie above −δ [walker2011equivalence](evidence/E-statistics-aggregation.md#walker2011equivalence). Margin choice has regulatory guidance in medicine [fda2016noninferiority](evidence/E-statistics-aggregation.md#fda2016noninferiority) (landing page only).
- **Bayesian analogue:** the posterior mass inside a region of practical equivalence, e.g. ±1 accuracy point [benavoli2017bayesian](evidence/E-statistics-aggregation.md#benavoli2017bayesian).
- **Bounds chosen after seeing the data invalidate the test.**
- **With small n, most comparisons end "undetermined"** (derived here). This is the honest result.

## 8. Exploratory vs confirmatory, screening vs deployment vs causal claims
| Claim type | What it needs (derived here, from sections 1–7 and [data-and-validity.md](data-and-validity.md)) |
|---|---|
| **Exploratory / screening:** "this system looks weak at X" | Any frozen data; descriptive counts with intervals; no multiplicity guarantee; hypotheses for later tests |
| **Confirmatory comparison:** "A beats B on population P" | Preregistered hypothesis, metric, test and family; a fresh test set sampled from P; adequate power; paired test; correction |
| **Deployment evidence:** "A is fit for use U" | Confirmatory evidence on data representative of U (ideally real traffic); operating point and costs from U; error budget with upper confidence bounds; robustness and operational measurements in the deployment configuration |
| **Causal claim about a factor** (model size, training method, readout) | Controlled variants that differ only in that factor. Several tasks. Repeated runs or seeds where training varies. Other factors held fixed: data, prompt, precision, runtime, readout. A comparison of systems that differ in many factors supports none of these claims ([robustness-and-execution.md](robustness-and-execution.md)) |

## 9. Aggregation across tasks
- **Averaging scores** treats task metrics as commensurable and weights tasks by inclusion.
  - GLUE's leaderboard is a macro average of task scores, and multi-metric tasks are averaged first [wang2019glue](evidence/F-robustness-frameworks-perf.md#wang2019glue).
  - BIG-bench normalises each task's preferred metric to 0–100 [srivastava2023bigbench](evidence/F-robustness-frameworks-perf.md#srivastava2023bigbench).
  - Averages across heterogeneous metrics have no unit, and the weights are a choice [demsar2006](evidence/E-statistics-aggregation.md#demsar2006) [colombo2022bestsystems](evidence/E-statistics-aggregation.md#colombo2022bestsystems).
- **Rankings are unstable.** Mean-aggregating every 4-of-8 subset of SuperGLUE gave six different top-1 models [dehghani2021lottery](evidence/E-statistics-aggregation.md#dehghani2021lottery).
- **Diversity vs stability.** The more diverse a multi-task benchmark, the more sensitive its ranking is to irrelevant changes. Ordinal aggregates can be reordered by adding irrelevant models (Arrow's independence of irrelevant alternatives) [zhang2024tradeoffs](evidence/E-statistics-aggregation.md#zhang2024tradeoffs).
- **Alternatives to the mean:**
  - **Rank aggregation:** Kemeny consensus approximated by Borda [colombo2022bestsystems](evidence/E-statistics-aggregation.md#colombo2022bestsystems), or social-choice rules [rofin2023votenrank](evidence/E-statistics-aggregation.md#rofin2023votenrank).
  - **Paired Bradley–Terry** from per-instance wins. This changed the state-of-the-art conclusion in about 30% of 296 setups, but discards the size of differences [peyrard2021paired](evidence/E-statistics-aggregation.md#peyrard2021paired).
  - **Robust summaries:** IQM, performance profiles and probability of improvement [agarwal2021precipice](evidence/E-statistics-aggregation.md#agarwal2021precipice).
- **Statistics over datasets** treat the dataset as the sampling unit, so N is small:
  - Wilcoxon signed-rank for two systems, Friedman for several [demsar2006](evidence/E-statistics-aggregation.md#demsar2006);
  - mean-rank post-hoc tests depend on which other systems are in the pool, so prefer pairwise tests with correction [benavoli2016meanranks](evidence/E-statistics-aggregation.md#benavoli2016meanranks).
- **Missing and unsupported cells.**
  - A mean over each system's available tasks silently gives each system a different task mix (derived here).
  - Options:
    1. Report each system on the **common supported subset**, and name it.
    2. Report coverage (supported tasks) separately from quality on supported tasks.
    3. Use pairwise rules that skip missing pairs, which Vote'n'Rank does [rofin2023votenrank](evidence/E-statistics-aggregation.md#rofin2023votenrank).
  - All of these assume that missingness is unrelated to performance. No verified source gives a formal missing-data treatment.
  - Imputing an unsupported cell as 0 conflates "cannot do" with "did badly". Imputing it as the mean rewards unsupported systems (derived here).
- **Why a global ranking hides tradeoffs.**
  - Users weight tasks and costs differently, and leaderboard utility ignores cost [ethayarajh2020utility](evidence/E-statistics-aggregation.md#ethayarajh2020utility).
  - A system best on average can be worst on the task a given application depends on.
  - Report per-task results with intervals first. Any aggregate should name its weights, its common subset and its intended use (derived here).

## 10. Reporting checklist
1. Unit of analysis: items, base cases, clusters, tasks.
2. Counts and n per cell; interval method (Wilson or Clopper–Pearson for small proportions).
3. Paired comparisons: discordant counts, the difference and its interval, the test (mid-p McNemar, permutation or bootstrap with n > ~200), and the correlation.
4. Clustered or stratified resampling where cases share a base or a task.
5. Power or minimum detectable effect, computed before collection.
6. Preregistered confirmatory family and correction; everything else labelled exploratory.
7. Non-significant results reported as inconclusive unless an equivalence or non-inferiority test with prespecified margins passes.
8. Aggregates only with named weights, a common subset and coverage reported beside them.
