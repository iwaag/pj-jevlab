# Sources: Cluster E — statistical comparison, uncertainty, and aggregation across tasks

Accessed for all sources: 2026-10-02. "full-text (pdftotext)" means the PDF was downloaded with curl and converted with `pdftotext`; quoted formulas were read from that raw text, not from a WebFetch summary. "full-text (PMC HTML)" means the PubMed Central HTML page was downloaded with curl and stripped of tags locally.

> Evidence notes for cluster E of [study/benchmark](../README.md), compiled 2026-10-02 in step2 of benchmark/p1 by a research subagent and reviewed by the lead session. The search log and gaps for this cluster are in [search-log.md](../search-log.md). Verification levels are per entry; claims beyond the stated level must not be attributed to a source.

## Source list

### brown2001binomial
- Title: Interval Estimation for a Binomial Proportion
- Authors / organization: Lawrence D. Brown, T. Tony Cai, Anirban DasGupta
- Date: Statistical Science 16(2), May 2001 (with discussion; pp. 101–133 including discussion)
- URL / DOI: https://doi.org/10.1214/ss/1009213286
- Type: method paper (review and comparison of interval methods)
- Verification: abstract (Project Euclid landing page via WebFetch; the author-hosted Wharton PDF now 301-redirects to a 404, the Project Euclid PDF is behind an Incapsula bot wall, and Semantic Scholar lists it as closed-access). The statsmodels `proportion_confint` documentation cites this paper as the basis for its methods (official docs, WebFetch).
- Supports (abstract-level only): the coverage probability of the Wald interval behaves erratically, and this is "persistent" and more severe than commonly thought. Common textbook rules for when the Wald interval is safe are "misleading and defective in several respects and cannot be trusted". The paper recommends the Wilson interval or the equal-tailed Jeffreys interval for small n, and the Agresti–Coull interval for larger n.
- Caveats / disagreements: I could not read the exact n cut-off (often quoted as n ≤ 40) or the "lucky/unlucky n" coverage examples, so do not attribute them here. statsmodels docs (official): "Beta, the Clopper-Pearson exact interval has coverage at least 1-alpha, but is in general conservative"; most of the other methods "have average coverage equal to 1-alpha, but will have smaller coverage in some cases."

### wilson1927
- Title: Probable Inference, the Law of Succession, and Statistical Inference
- Authors: Edwin B. Wilson
- Date: JASA 22(158):209–212, June 1927
- DOI: 10.1080/01621459.1927.10502953
- Type: method paper
- Verification: unverified for content (only the bibliographic record was checked, via Crossref API; the publisher site is paywalled). The formula below comes from bowyer2025clt App. A.2, read in full text.
- Supports: origin of the score interval. Formula (bowyer2025clt Eq. 12), with p̂ = k/N and z = z_{α/2}:
  CI = [ p̂ + z²/(2N) ± (z/(2N))·sqrt(4N p̂(1−p̂) + z²) ] / (1 + z²/N).
  The centre is shrunk toward 1/2, so the interval never has zero width and never leaves [0,1].
- Caveats: none from the source itself.

### agresti1998approx
- Title: Approximate is Better than "Exact" for Interval Estimation of Binomial Proportions
- Authors: Alan Agresti, Brent A. Coull
- Date: The American Statistician 52(2):119–126, 1998
- DOI: 10.1080/00031305.1998.10480550
- Type: method paper
- Verification: unverified (Crossref bibliographic record only; the UFL-hosted PDF returned an HTML block page). It is cited here only because bowyer2025clt §3.1 cites it for the claim that Clopper–Pearson is "overly conservative (too wide) in practice".
- Supports: nothing attributed directly.
- Caveats: the usual "add z²/2 successes and failures" form of the Agresti–Coull interval was not verified from any primary text in this session.

### mcnemar1947
- Title: Note on the Sampling Error of the Difference Between Correlated Proportions or Percentages
- Authors: Quinn McNemar
- Date: Psychometrika 12:153–157, June 1947
- DOI: 10.1007/BF02295996
- Type: method paper
- Verification: unverified for content (Crossref bibliographic record only; paywalled). The test is described below from fagerland2013mcnemar (full text).
- Supports: origin of the matched-pairs test for two correlated proportions.

### fagerland2013mcnemar
- Title: The McNemar test for binary matched-pairs data: mid-p and asymptotic are better than exact conditional
- Authors: Morten W. Fagerland, Stian Lydersen, Petter Laake
- Date: BMC Medical Research Methodology 13:91, 2013
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3716987/
- Type: method paper / simulation study
- Verification: full-text (PMC HTML): Methods (Eqs. 1–6), Results, Table 6, Conclusions.
- Supports:
  - Asymptotic McNemar (Eq. 1): z = (n12 − n21)/sqrt(n12 + n21), approximately N(0,1). Equivalently χ² = (n12 − n21)²/(n12 + n21) with 1 df. Undefined when n12 = n21 = 0.
  - Continuity-corrected version (Eq. 2): z = (|n12 − n21| − 1)/sqrt(n12 + n21).
  - Exact conditional test (Eqs. 3–4): condition on n = n12 + n21. Under H0, n12 ~ Binomial(n, 1/2). The one-sided p is Σ_{x=0}^{min(n12,n21)} C(n,x)(1/2)^n, and the two-sided p is twice that.
  - Mid-p (Eq. 5): mid-p = two-sided exact p − f(n12 | n), where f is the binomial point probability. If n12 = n21, mid-p = 1 − ½ f(n12 | n) (Eq. 6).
  - Evaluation covered 9,595 scenarios (N = 1..100 pairs) at nominal 5%. The mid-p test never violated the nominal level. The asymptotic test without continuity correction was the most powerful but had "small but frequent violations". The exact conditional test and the continuity-corrected test "are highly conservative and have poor power, we do not recommend reporting the results of these two tests in any situation."
  - Table 6 worked example (Bentur et al.; 2/21 vs 8/21): asymptotic p = 0.0339, with CC 0.0771, exact 0.0703, mid-p 0.0391, exact unconditional 0.0353.
- Caveats: mid-p is "quasi-exact" because its type I error is not guaranteed to stay at or below α. The paper's conclusion is for a single test. Under multiplicity correction (e.g. Holm), how conservative the per-test method is affects family-wise power.

### dietterich1998tests
- Title: Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms
- Authors: Thomas G. Dietterich
- Date: Neural Computation 10(7):1895–1923, 1998
- DOI: 10.1162/089976698300017197
- Type: method paper / simulation study
- Verification: abstract (via the Crossref API and Europe PMC record; a mirrored PDF was found but its fonts are unextractable, and MIT Press returns 403).
- Supports (abstract): five tests were compared on type I error. Two tests "should never be used" because of high type I error: the difference-of-two-proportions test, and the paired t-test over several random train/test splits. The 10-fold CV paired t-test has "somewhat elevated" type I error. McNemar's test "is shown to have low type I error". The new 5×2cv test also has acceptable type I error and is slightly more powerful than McNemar. "For algorithms that can be executed only once, McNemar's test is the only test with acceptable type I error. For algorithms that can be executed 10 times, the 5 x 2 cv test is recommended."
- Caveats: this is about comparing learning algorithms, where training-set variability matters. For fixed (pretrained/frozen) systems on a fixed test set, only test-item sampling variability applies, which is the McNemar/paired-bootstrap setting. The 5×2cv statistic was not read from the source.

### koehn2004bootstrap
- Title: Statistical Significance Tests for Machine Translation Evaluation
- Authors: Philipp Koehn
- Date: EMNLP 2004 (ACL Anthology W04-3250)
- URL: https://aclanthology.org/W04-3250
- Type: method paper / empirical study
- Verification: full-text (pdftotext): Abstract, §6 "Paired Bootstrap Resampling", Fig. 7–8.
- Supports: bootstrap confidence intervals for corpus-level BLEU, from 1000 resampled test sets. In paired bootstrap resampling, both systems are scored on the same resampled test sets: "If, say, one system outperforms the other system 95% of the time, we draw the conclusion that it is better." The abstract says that "even for small test sizes of only 300 sentences" the methods may give assurance that differences are real.
- Caveats: Berg-Kirkpatrick et al. (2012, fn. 2) note that counting δ(x(i)) < 0 is equivalent to their recentred 2δ(x) version only when the bootstrap distribution of δ is symmetric. Søgaard et al. (2014) warn that bootstrap p-values are anti-conservative for small samples.

### riezler2005pitfalls
- Title: On Some Pitfalls in Automatic Evaluation and Significance Testing for MT
- Authors: Stefan Riezler, John T. Maxwell III
- Date: ACL 2005 Workshop on Intrinsic and Extrinsic Evaluation Measures (W05-0908)
- URL: https://aclanthology.org/W05-0908
- Type: method paper / empirical study
- Verification: full-text (pdftotext): Abstract, Fig. 1 (approximate randomization), Fig. 2 (bootstrap), §4.
- Supports:
  - Approximate randomization (Fig. 1). For R shuffles, swap each sentence's pair of system outputs between X and Y with probability 0.5. Count c = #{|S_X^r − S_Y^r| ≥ |S_X − S_Y|}, then p = (c+1)/(R+1).
  - Bootstrap uses Noreen's "shift" method, centring the bootstrap distribution at the null.
  - Finding: "p-values are estimated more conservatively by approximate randomization than by bootstrap tests, thus increasing the likelihood of type-I error for the latter". For multiple pairwise comparisons they recommend "more stringent rejection levels".
- Caveats / disagreements: Berg-Kirkpatrick et al. (2012, fn. 1) argue that AR is "ill-suited" when the null hypothesis does not condition on the test data, and so prefer the bootstrap. This is a real disagreement about the inferential target: AR answers whether the two systems' outputs on *this* test set are exchangeable, while the bootstrap targets the population of test sets.

### noreen1989 / efron1993bootstrap (books)
- Noreen, E. W. (1989). Computer-Intensive Methods for Testing Hypotheses. Wiley. Efron, B. & Tibshirani, R. (1993). An Introduction to the Bootstrap. Chapman & Hall.
- Type: textbook
- Verification: unverified (books, not accessed). Cited only through the descriptions in riezler2005pitfalls, dror2018hitchhiker and berg2012empirical.

### berg2012empirical
- Title: An Empirical Investigation of Statistical Significance in NLP
- Authors: Taylor Berg-Kirkpatrick, David Burkett, Dan Klein
- Date: EMNLP-CoNLL 2012 (D12-1091)
- URL: https://aclanthology.org/D12-1091
- Type: empirical study
- Verification: full-text (pdftotext): Intro, §2.2, Fig. 1, §5–6.
- Supports:
  - Paired bootstrap p-value procedure (Fig. 1). Draw b bootstrap samples x(i) of size n with replacement. Increment s if δ(x(i)) > 2δ(x). Then p ≈ s/b; they use b = 10^6. The 2δ recentring is used because bootstrap samples are centred on δ(x), not on 0.
  - More similar (correlated) systems reach significance with smaller metric gains.
  - Test set size "plays the largest role" in discrimination ability, with diminishing returns.
  - When new data is i.i.d. from the test distribution, significance levels are "remarkably well-calibrated". As the domain diverges, predictive ability "drops off dramatically".
- Caveats: their analysis covers MT, summarisation and parsing. The calibration finding applies only to same-distribution generalisation.

### sogaard2014pvalue
- Title: What's in a p-value in NLP?
- Authors: Anders Søgaard, Anders Johannsen, Barbara Plank, Dirk Hovy, Héctor Martínez Alonso
- Date: CoNLL 2014 (W14-1601)
- URL: https://aclanthology.org/W14-1601
- Type: empirical study
- Verification: full-text (pdftotext): Abstract, §1–2.
- Supports:
  - Significance results are "very sensitive to sample size, covariates such as sentence length, as well as to the existence of multiple metrics".
  - "Under the assumption of perfect metrics and unbiased data, we need a significance cut-off at ~0.0025 to reduce the risk of false positive results to <5%". This corresponds to Bonferroni for m = 20.
  - Bootstrap at small samples: "with small sample sizes, there is a risk that the calculated p-value will be artificially low — simply because the bootstrap samples are too similar". They use the bootstrap only when n > 200.
- Caveats: the 0.0025 figure is model-based and specific to their simulation.

### dror2018hitchhiker
- Title: The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing
- Authors: Rotem Dror, Gili Baumer, Segev Shlomov, Roi Reichart
- Date: ACL 2018 (P18-1128)
- URL: https://aclanthology.org/P18-1128
- Type: position/survey
- Verification: full-text (pdftotext): §3.2, §3.3 Fig. 1, §4 Table 2.
- Supports:
  - McNemar is for paired binary outcomes. Under H0, with "a sufficiently large number of disagreements", the statistic is χ² with 1 df. Cochran's Q generalises it.
  - Decision tree (Fig. 1): if the test statistic's distribution is known, use a parametric test. Otherwise, if the data are small, use bootstrap or randomization, and if large, use sampling-free non-parametric tests (sign, Wilcoxon).
  - The paired bootstrap "is less effective for small test sets, as it assumes that the test set distribution does not deviate too much from the population distribution". The paper counts "using a Bootstrap test with a small test set size" as an inappropriate test.
  - Survey of ACL 2017: only 63 of 180 experimental long papers reported significance, and 21 of those did not name the test. Of 110 papers with multiple datasets, only 3 corrected for multiplicity, all with Bonferroni.
- Caveats / internal tension: Fig. 1 routes small data to bootstrap/randomization, while §3.2 warns that the bootstrap is less effective on small test sets. AR (exact or approximate permutation) is the safer small-n choice under this guide.

### card2020power
- Title: With Little Power Comes Great Responsibility
- Authors: Dallas Card, Peter Henderson, Urvashi Khandelwal, Robin Jia, Kyle Mahowald, Dan Jurafsky
- Date: EMNLP 2020; arXiv 2010.06595 (v1 2020-10-13)
- URL: https://arxiv.org/abs/2010.06595
- Type: empirical study / method (simulation-based power analysis)
- Verification: full-text (pdftotext): Abstract, §2 Fig. 2, §3.1 Table 1–2, §3 results.
- Supports:
  - Power is "the probability that, given a real effect, an experiment will reject the null hypothesis". Underpowered experiments also exaggerate effects (Type-M error, Gelman & Carlin 2014).
  - For McNemar on classifiers, χ² = (p10 − p01)²/(p10 + p01). Simulation is parametrised by the expected accuracy difference Δacc and the agreement rate Pa (fraction both-right or both-wrong). Power rises with n, Δacc and Pa (Fig. 3).
  - GLUE: only 46% of surveyed SOTA comparisons were predicted to be adequately powered. For WNLI, MRPC and SST-2, most future comparisons will not be adequately powered. MT: test sets of 2,000 sentences have about 75% power to detect a 1 BLEU difference.
  - The paper ships simulation notebooks.
- Caveats: the power estimates rely on regression-based guesses of agreement and of the effect size.

### miller2024errorbars
- Title: Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations
- Authors: Evan Miller (Anthropic)
- Date: arXiv 2411.00640 v1, 2024-11-01
- URL: https://arxiv.org/abs/2411.00640
- Type: method paper (vendor-authored, but a statistical methods note)
- Verification: full-text (pdftotext): §2.1 Eqs. 1–3, §2.2 Eq. 4 and Table 4, §3, §4 Eqs. 5–8 and Table 5, §5 Eqs. 9–10.
- Supports:
  - Super-population framing: questions are drawn from an unseen population, with s_i = x_i + ε_i.
  - SE_CLT = sqrt( (1/(n−1)) Σ (s_i − s̄)² / n ) (Eq. 1). For Bernoulli scores, SE = sqrt(s̄(1−s̄)/n) (Eq. 2). CI95 = s̄ ± 1.96·SE (Eq. 3). The paper regards bootstrapping as "unnecessary unless a complicated sampling scheme or estimator is being used".
  - Clustered SE (Eq. 4): SE_clustered = ( SE²_CLT + (1/n²) Σ_c Σ_i Σ_{j≠i} (s_{i,c} − s̄)(s_{j,c} − s̄) )^{1/2}. Table 4 (real Anthropic data): clustered/naive SE ratio is 3.05 on DROP, 1.10 on RACE-H and 1.88 on MGSM. Report the cluster count alongside the question count.
  - Variance decomposition: Var(μ̂) = (Var(x) + E[σ_i²])/n. Resampling K answers per question reduces the second term to E[σ_i²]/K. Pooling KN answers as if independent is "inconsistent". Use next-token probabilities when possible. "Don't touch the thermostat": lowering temperature can raise Var(x) or bias the estimate.
  - Unpaired difference: SE_{A−B} = sqrt(SE_A² + SE_B²), with z = μ̂_{A−B}/SE_{A−B} (Eqs. 5–6).
  - Paired difference: SE = sqrt(Var(s_A − s_B)/n) (Eq. 7). Var_paired = Var_unpaired − 2Cov(x_A, x_B)/n. Equivalently SE_paired = sqrt(SE_A² + SE_B² − 2 SE_A SE_B Corr). Paired-clustered version is Eq. 8.
  - Recommended reporting: the pairwise difference, its SE, the 95% CI and the score correlation (Table 5).
  - Power (Eq. 9): n = (z_{α/2} + z_β)² (ω² + σ_A²/K_A + σ_B²/K_B)/δ², where ω² = Var(x_A) + Var(x_B) − 2Cov(x_A, x_B). MDE (Eq. 10): δ = (z_{α/2} + z_β) sqrt((ω² + σ_A²/K_A + σ_B²/K_B)/n).
  - Worked example: ω² = 1/9, δ = 0.03, α = .05, power .8 gives n ≈ 969, hence "new evals should contain at least 1,000 questions". With n = 198, raising K from 1 to 10 lowers the MDE from 13.2% to 7.5%.
- Caveats / disagreements: everything is CLT-based. bowyer2025clt argues these intervals under-cover when n is below a few hundred, and that clustered CLT also fails with few clusters (see also cameron2015cluster on few clusters).

### bowyer2025clt
- Title: Position: Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints
- Authors: Sam Bowyer, Laurence Aitchison, Desi R. Ivanova (Bristol / Oxford)
- Date: ICML 2025 (PMLR 267); arXiv 2503.01747 (v1 2025-03-03, v3 2025-05-28)
- URL: https://arxiv.org/abs/2503.01747
- Type: position paper with simulation study
- Verification: full-text (pdftotext): §1, §2, §3.1–3.5 (Figs. 1–6, Snippets 1–2), §5, App. A.2–A.3. The title claim is confirmed.
- Supports:
  - Simulation design: θ ~ Beta(1,1), N ∈ {3, 10, 30, 100}, 100 θ values × 200 datasets, with nominal levels from 0.80 to 0.995.
  - IID setting: CLT and bootstrap intervals under-cover. At N = 100, a nominal 95% CLT interval achieves about 92.5% coverage. Wilson and Bayesian Beta(1+S, 1+N−S) intervals stay near nominal. Clopper–Pearson is valid but conservative. CP is equivalent to the Bayesian interval "with the uniform prior removed" (Thulin 2014).
  - CLT intervals collapse to zero width when θ̂ ∈ {0,1}, and leave [0,1] when θ̂ or 1−θ̂ < 1/(1 + N/z²). Fig. 1 shows this on a real N = 20 tool-use benchmark.
  - Clustered setting (θ_t ~ Beta(dθ, d(1−θ))): neither naive nor clustered CLT achieves coverage at small N. Only the clustered Bayesian (beta-binomial) model does.
  - Independent two-model comparison: the CLT difference interval under-covers. Fisher's exact test is over-conservative. Bayesian intervals for the difference or the odds ratio cover well.
  - Paired comparison: the paired Bayes method (importance sampling) is recommended. Unpaired Bayes is "a reasonable and easier" alternative.
  - Non-average metrics (F1): bootstrap under-covers and Bayesian intervals track nominal.
  - Code: `scipy.stats.binomtest(k,n).proportion_ci("wilson")`. Library: github.com/sambowyer/bayes_evals.
- Caveats: coverage is averaged over a uniform prior on θ, which is the same prior the Bayesian method uses, and this favours it. Conditional (fixed-θ) coverage near 0 or 1 can differ. For the paired setting they did not test McNemar or exact/mid-p tests. In the IID case the paper itself says frequentist Wilson works "as well as" Bayesian.

### bouthillier2021variance
- Title: Accounting for Variance in Machine Learning Benchmarks
- Authors: Xavier Bouthillier, Pierre Delaunay, … Gaël Varoquaux, Pascal Vincent
- Date: MLSys 2021; arXiv 2103.03098 (2021-03-01)
- URL: https://arxiv.org/abs/2103.03098
- Type: empirical study / method
- Verification: full-text (pdftotext): Abstract, §1 recommendations, §4 "Probability of outperforming" (Eq. 9).
- Supports:
  - Data sampling, parameter initialisation and hyperparameter choice all "impact markedly the results". Randomising more sources of variation brings the cheap biased estimator closer to the ideal one, at a "51× reduction in compute cost".
  - Recommendations: (1) randomise as many sources of variation as possible; (2) do not rely on average performance alone, and use P(A > B) = (1/k) Σ_i 1{R_i^A > R_i^B} over paired runs; (3) prefer out-of-bootstrap resampling to a fixed held-out test set.
  - Decision rule: H0 is P(A>B) = 0.5 ("significant") and H1 is P(A>B) = γ ("meaningful"). Use percentile-bootstrap CIs and conclude A is better only if the result is both significant and meaningful. γ = 0.75 is suggested.
- Caveats: the setting is training-pipeline comparison. With frozen systems, only test-set sampling and inference stochasticity apply.

### reimers2017distributions
- Title: Reporting Score Distributions Makes a Difference: Performance Study of LSTM-networks for Sequence Tagging
- Authors: Nils Reimers, Iryna Gurevych
- Date: EMNLP 2017; arXiv 1707.09861
- URL: https://arxiv.org/abs/1707.09861
- Type: empirical study
- Verification: full-text (pdftotext): Abstract.
- Supports: the random seed alone can produce statistically significant (p < 10⁻⁴) differences. For two NER systems, about 1 F1 point separates seeds, "making these systems perceived either as state-of-the-art or mediocre". The paper proposes comparing score distributions over multiple executions rather than single scores.
- Caveats: the experiments are LSTM training seeds, but the argument carries over to any stochastic pipeline (sampling temperature, judge stochasticity).

### dodge2019showyourwork
- Title: Show Your Work: Improved Reporting of Experimental Results
- Authors: Jesse Dodge, Suchin Gururangan, Dallas Card, Roy Schwartz, Noah A. Smith
- Date: EMNLP 2019; arXiv 1909.03004
- URL: https://arxiv.org/abs/1909.03004
- Type: method paper
- Verification: full-text (pdftotext): Abstract, §3 (Eqs. 1–2, §3.1).
- Supports:
  - Expected maximum validation performance as a function of budget n. For n random-search trials, E[V*_n | n] = Σ_v v·(P̂(V ≤ v)^n − P̂(V < v)^n), using the empirical CDF P̂ of the B observed trials.
  - Conclusions can flip with compute budget, so the paper recommends reporting budget curves and validation performance.
- Caveats: this targets hyperparameter tuning effort. For prompt or threshold tuning, the analogue is to report how many configurations were tried on dev.

### madaan2024variance
- Title: Quantifying Variance in Evaluation Benchmarks
- Authors: Lovish Madaan, Aaditya K. Singh, Rylan Schaeffer, Andrew Poulton, Sanmi Koyejo, Pontus Stenetorp, Sharan Narang, Dieuwke Hupkes (Meta et al.)
- Date: arXiv 2406.10229 (2024-06-14)
- URL: https://arxiv.org/abs/2406.10229
- Type: empirical study
- Verification: full-text (pdftotext): Abstract, §2 metric definitions, §3 seed variance, Table 2 discussion.
- Supports:
  - Seed variance is the SD across models trained with different init seeds. The paper also uses a bootstrapped 95% CI and the analytic CI 1.96·sqrt(S(1−S)/N).
  - Benchmarks with few items (COPA, HumanEval) show high variance. 7B seed variance is "generally … well below the 95% CI", with a variable ratio.
  - Continuous metrics (probability mass of the answer, NLL) have "considerably higher" SNR than discrete accuracy.
  - Reframing multiple-choice as completion (cloze) can reduce variance for about 7B models. IRT and item-analysis methods "struggle to meaningfully reduce variance".
- Caveats: this concerns pretraining-checkpoint decisions. The analytic CI used is the Wald form, which bowyer2025clt criticises at small N.

### heineman2025signalnoise
- Title: Signal and Noise: A Framework for Reducing Uncertainty in Language Model Evaluation
- Authors: David Heineman, Valentin Hofmann, Ian Magnusson, Yuling Gu, Noah A. Smith, Hannaneh Hajishirzi, Kyle Lo, Jesse Dodge (AI2)
- Date: arXiv 2508.13144 (2025-08-18)
- URL: https://arxiv.org/abs/2508.13144
- Type: empirical study
- Verification: abstract (arXiv API).
- Supports (abstract): defines *signal* (ability to separate better from worse models) and *noise* (sensitivity to random variability between training steps). A higher SNR makes small-scale decisions more reliable. Switching to perplexity-like metrics, filtering noisy subtasks, and checkpoint averaging all improve SNR. Based on 30 benchmarks and 375 models.
- Caveats: abstract-level only, and the setting is the pretraining decision context.

### agarwal2021precipice
- Title: Deep Reinforcement Learning at the Edge of the Statistical Precipice
- Authors: Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron Courville, Marc G. Bellemare
- Date: NeurIPS 2021 (Outstanding Paper); arXiv 2108.13264 (v4 2022-01-05)
- URL: https://arxiv.org/abs/2108.13264
- Type: method paper
- Verification: full-text (pdftotext): Table 1 (recommendations), §4.1 (stratified bootstrap), §4.2 (performance profiles, Eq. 1), §4.3 (IQM, optimality gap, probability of improvement).
- Supports:
  - Report interval estimates using the stratified bootstrap: resample runs with replacement independently within each task, then recompute the aggregate. Percentile CIs give good coverage with as few as N = 10 runs for median and IQM. A per-task bootstrap with small N is "less useful".
  - Performance profile (score distribution): F̂(τ) = (1/M) Σ_m (1/N) Σ_n 1[x_{m,n} > τ]. It is unbiased, and an outlier run changes it by at most 1/(MN).
  - IQM is the 25% trimmed mean over all runs pooled across tasks. It is more efficient than the median and more robust than the mean.
  - Optimality gap is the amount by which the algorithm falls short of a target γ (default 1.0).
  - Average probability of improvement: P(X>Y) = (1/M) Σ_m P(X_m > Y_m). It "does not account for the size of improvement".
- Caveats: designed for RL runs with normalised scores. IQM and profiles need commensurate (normalised) task scores.

### holm1979
- Title: A Simple Sequentially Rejective Multiple Test Procedure
- Authors: Sture Holm
- Date: Scandinavian Journal of Statistics 6(2):65–70, 1979 (JSTOR 4615733)
- Type: method paper
- Verification: unverified for content (JSTOR page failed to load and Semantic Scholar elides the abstract). The procedure is described from demsar2006 §3.2.2 (full text).
- Supports (via Demšar): order the p-values p_(1) ≤ … ≤ p_(m) and compare p_(i) with α/(m − i + 1). Reject sequentially and stop at the first non-rejection; all remaining hypotheses are retained. It controls FWER with no assumptions on dependence and is uniformly more powerful than Bonferroni. Demšar writes this for k−1 comparisons against a control as α/(k − i).

### benjamini1995fdr
- Title: Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing
- Authors: Yoav Benjamini, Yosef Hochberg
- Date: JRSS B 57(1):289–300, 1995
- DOI: 10.1111/j.2517-6161.1995.tb02031.x
- Type: method paper
- Verification: abstract (OUP landing page via WebFetch).
- Supports (abstract): FWER control "has faults". The FDR is the expected proportion of falsely rejected hypotheses. It equals FWER when all nulls are true and is smaller otherwise, which gives a power gain. "A simple sequential Bonferroni-type procedure is proved to control the false discovery rate for independent test statistics."
- Caveats: the step-up rule (reject p_(i) ≤ iα/m for the largest such i) is standard but was not read from the source here. Validity under dependence (proved for PRDS by Benjamini & Yekutieli 2001) is not covered by this abstract. Demšar (2006 §3.2.2) argues FDR methods are "less suitable for the evaluation of machine learning algorithms".

### vanmiltenburg2021prereg
- Title: Preregistering NLP Research
- Authors: Emiel van Miltenburg, Chris van der Lee, Emiel Krahmer
- Date: NAACL 2021 (2021.naacl-main.51)
- URL: https://aclanthology.org/2021.naacl-main.51
- Type: position paper
- Verification: full-text (pdftotext): Abstract, §2, Table 1–3, §4.
- Supports:
  - Preregistration means "specifying what you are going to do, and what you expect to find in your study, before carrying out the study". It separates exploratory from confirmatory research and avoids the "garden of forking paths" (Gelman & Loken).
  - The AsPredicted-based items cover hypothesis, dependent variables, conditions, exact analyses, outliers/exclusions, sample size and stopping rule (to prevent optional stopping).
  - Registered reports allow deviations from plan but "these should be identified in the final report".
- Caveats: the paper offers proposals, with no empirical evaluation.

### lakens2017equivalence
- Title: Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses
- Authors: Daniël Lakens
- Date: Social Psychological and Personality Science 8(4):355–362, 2017
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC5502906/
- Type: textbook/tutorial
- Verification: full-text (PMC HTML): Abstract, "Equivalence tests" section, Figure 1.
- Supports:
  - TOST (Schuirmann 1987): bounds −Δ_L and Δ_U are set from the smallest effect size of interest (SESOI). Two composite nulls are tested, H0₁: Δ ≤ −Δ_L and H0₂: Δ ≥ Δ_U. Rejecting both supports −Δ_L < Δ < Δ_U.
  - Equivalently, the 90% CI lies within the bounds at α = .05.
  - There are four outcomes, from combining NHST with equivalence: equivalent and not different; different and not equivalent; different and equivalent (trivially small); undetermined.
  - "Psychologists often incorrectly conclude there is no effect based on a nonsignificant test result."
- Caveats: the bounds must be pre-specified and justified, and post-hoc bounds invalidate the test.

### walker2011equivalence
- Title: Understanding Equivalence and Noninferiority Testing
- Authors: Esteban Walker, Amy S. Nowacki
- Date: Journal of General Internal Medicine 26(2):192–196, 2011
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC3019319/
- Type: textbook/tutorial
- Verification: full-text (PMC HTML).
- Supports:
  - Equivalence holds at level α if the (1−2α)·100% CI for (new − current) lies within (−δ, δ).
  - "Noninferiority is established, at the α significance level, if the lower limit of a (1–2α) × 100% confidence interval for the difference (new – current) is above −δ" (when higher is better).
  - Sample size is very sensitive to δ. For true proportions .33 vs .28, at power .8 and α .05, n per group is 26,185 for δ = .06, 1,048 for δ = .10 and 535 for δ = .12 (Table 2).
- Caveats: the clinical framing includes margin choice from historical data, assay sensitivity and the constancy assumption.

### fda2016noninferiority
- Title: Non-Inferiority Clinical Trials to Establish Effectiveness — Guidance for Industry
- Authors / organization: U.S. FDA (CDER/CBER)
- Date: November 2016
- URL: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/non-inferiority-clinical-trials
- Type: official docs (regulatory guidance)
- Verification: abstract (landing page via WebFetch; PDF download returned non-PDF content).
- Supports (landing page): the guidance covers when NI designs are interpretable, selection of NI margins, and hypothesis testing.
- Caveats: the M1/M2 margin definitions were not read, so do not attribute them.

### altman1995absence
- Title: Statistics notes: Absence of evidence is not evidence of absence
- Authors: Douglas G. Altman, J. Martin Bland
- Date: BMJ 311(7003):485, 19 August 1995
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC2550545/ (DOI 10.1136/bmj.311.7003.485)
- Type: textbook/tutorial (statistics note)
- Verification: abstract-level (PMC landing page; the full text is a scanned PDF image and BMJ returned 403). Only the title claim and the bibliographic details are verified. Its reference list includes Yusuf et al. 1985 (fibrinolytic therapy meta-analysis) and Sung et al. 1993 (octreotide vs sclerotherapy).
- Supports: the principle in the title, that a non-significant result does not show the absence of an effect. Operationalised by lakens2017equivalence / walker2011equivalence.

### cameron2015cluster
- Title: A Practitioner's Guide to Cluster-Robust Inference
- Authors: A. Colin Cameron, Douglas L. Miller
- Date: Journal of Human Resources 50(2):317–372, 2015 (author-hosted preprint, Feb 2015)
- URL: http://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2015_February.pdf (DOI 10.3368/jhr.50.2.317)
- Type: textbook/tutorial
- Verification: full-text (pdftotext): Abstract, §II.A Eq. 6, §II.F (pairs cluster bootstrap), §VI (few clusters).
- Supports:
  - Default SEs "can greatly overstate estimator precision" under within-cluster correlation.
  - Moulton factor τ ≈ 1 + ρ_x ρ_u (N̄_g − 1). With unequal cluster sizes, replace N̄_g − 1 by V[N_g]/N̄_g + N̄_g − 1. Example: ρ_u = 0.032 with N̄_g = 387 gives τ ≈ 13.3.
  - Pairs cluster bootstrap: resample whole clusters with replacement G times. "It is important that the resampling be done over entire clusters, rather than over individual observations." B = 400 is usually adequate for SEs.
  - Few clusters: "no clear-cut definition of 'few'", which may range from fewer than 20 to fewer than 50 balanced clusters. With CRVE and critical value 1.96, rejection rates were .068/.081/.118/.208 for G = 30/20/10/5. CR2/CR3 bias corrections, T(G−1) critical values and the wild cluster bootstrap (6-point weights when G < 10) help but do not eliminate over-rejection.
- Caveats: written for regression. A cluster-mean estimate is the intercept-only special case.

### field2007clustered
- Title: Bootstrapping Clustered Data
- Authors: C. A. Field, A. H. Welsh
- Date: JRSS B 69(3):369–390, 2007
- DOI: 10.1111/j.1467-9868.2007.00593.x
- Type: method paper
- Verification: abstract (OUP landing page via WebFetch).
- Supports (abstract): the consistency of bootstrap variance estimates depends on the model. "The cluster bootstrap gives consistent estimates under both the transformation and the random-effect model", while the residual bootstrap is consistent only under the transformation model.
- Caveats: abstract-level only, and covers one-way arrays.

### demsar2006
- Title: Statistical Comparisons of Classifiers over Multiple Data Sets
- Authors: Janez Demšar
- Date: JMLR 7:1–30, 2006
- URL: https://www.jmlr.org/papers/v7/demsar06a.html
- Type: method paper / tutorial
- Verification: full-text (pdftotext): Abstract, §3.1.3 (Wilcoxon), §3.2.2 (Friedman, Iman–Davenport, Nemenyi CD, Holm/Hochberg/Hommel), §5 conclusions.
- Supports:
  - Recommends Wilcoxon signed-rank for two classifiers and Friedman with post-hoc tests for more, over multiple datasets, with critical-difference (CD) diagrams.
  - Wilcoxon: R⁺ = Σ_{d_i>0} rank(d_i) + ½ Σ_{d_i=0} rank(d_i), with R⁻ defined analogously and T = min(R⁺, R⁻).
  - Friedman: χ²_F = (12N/(k(k+1))) [Σ_j R_j² − k(k+1)²/4], with k−1 df (rule of thumb N > 10, k > 5). Iman–Davenport: F_F = (N−1)χ²_F/(N(k−1) − χ²_F), distributed F with (k−1, (k−1)(N−1)) df.
  - Nemenyi: CD = q_α sqrt(k(k+1)/(6N)).
  - Comparing against a control only, with Holm, is more powerful than all-pairs comparison.
  - Averaging across datasets is problematic because of commensurability. Parametric tests are also problematic: normality is questionable and they are outlier-sensitive.
- Caveats: the datasets are the sampling units, so N = number of datasets (often small), which differs from per-item tests. Benavoli et al. (2016) criticise the mean-rank post-hoc test.

### benavoli2016meanranks
- Title: Should We Really Use Post-Hoc Tests Based on Mean-Ranks?
- Authors: Alessio Benavoli, Giorgio Corani, Francesca Mangili
- Date: JMLR 17(5):1–10, 2016
- URL: https://www.jmlr.org/papers/v17/benavoli16a.html
- Type: method paper
- Verification: full-text (pdftotext): Abstract, §1.
- Supports: the outcome of the mean-ranks (Nemenyi-type) post-hoc test for A vs B "depends on the pool of algorithms originally included in the experiment", which can produce paradoxes. The paper recommends pairwise Wilcoxon signed-rank or sign tests, whose decisions do not depend on the pool, with multiplicity correction. For m = 2, Friedman reduces to the sign test.

### benavoli2017bayesian
- Title: Time for a Change: a Tutorial for Comparing Multiple Classifiers Through Bayesian Analysis
- Authors: Alessio Benavoli, Giorgio Corani, Janez Demšar, Marco Zaffalon
- Date: JMLR 18(77), 2017; arXiv 1606.04316 (v3 2017-07-15)
- URL: https://arxiv.org/abs/1606.04316
- Type: textbook/tutorial (position)
- Verification: full-text (pdftotext): Abstract, §3 (correlated t-test Eq. 1–2), §4 (Bayesian correlated t-test, ROPE).
- Supports:
  - Argues for abandoning NHST in favour of Bayesian tests (correlated t-test, hierarchical correlated t-test, signed-rank).
  - Nadeau–Bengio correlated t: t = x̄/sqrt(σ̂²(1/n + ρ/(1−ρ))) with ρ = n_te/n_tot.
  - ROPE: for classifiers, the region of practical equivalence is [−0.01, 0.01] in accuracy. Report P(A ≪ B), P(A = B) and P(A ≫ B) as posterior mass below, inside and above the ROPE.
- Caveats: the ROPE width is a user choice, analogous to the TOST bounds.

### ethayarajh2020utility
- Title: Utility is in the Eye of the User: A Critique of NLP Leaderboards
- Authors: Kawin Ethayarajh, Dan Jurafsky
- Date: EMNLP 2020; arXiv 2009.13888 (v4 2021-03-03)
- URL: https://arxiv.org/abs/2009.13888
- Type: position paper
- Verification: full-text (pdftotext): Abstract, §1.
- Supports: identifies three limitations of leaderboards. (1) Non-smooth utility: a gain counts only if it raises rank. (2) Prediction cost (size, energy, latency) is treated as zero. (3) Robustness and fairness are ignored. "There is no way to rank models so that everyone is satisfied", so the paper recommends leaderboards require reporting of practical statistics (size, energy, latency).

### dehghani2021lottery
- Title: The Benchmark Lottery
- Authors: Mostafa Dehghani, Yi Tay, Alexey A. Gritsenko, Zhe Zhao, Neil Houlsby, Fernando Diaz, Donald Metzler, Oriol Vinyals
- Date: arXiv 2107.07002 (2021-07-14)
- URL: https://arxiv.org/abs/2107.07002
- Type: empirical study / position
- Verification: full-text (pdftotext): Abstract, §3.1.1 (SuperGLUE task-subset experiment), section index (§7 "What can we do?").
- Supports: relative rankings change with the choice of benchmark tasks ("task selection bias"). Across 55 models, mean-aggregating every 4-of-8 SuperGLUE subset (70 subsets) gives 6 distinct Top-1 models, and about 60 of 70 Top-3/Top-5 rankings disagree. The paper also discusses community bias and "rigging the lottery".
- Caveats: the §7 recommendations were not read in detail.

### colombo2022bestsystems
- Title: What are the best systems? New perspectives on NLP Benchmarking
- Authors: Pierre Colombo, Nathan Noiry, Ekhine Irurozki, Stephan Clémençon
- Date: NeurIPS 2022; arXiv 2202.03799 (v4 2022-10-07)
- URL: https://arxiv.org/abs/2202.03799
- Type: method paper
- Verification: full-text (pdftotext): Abstract, §2–3 (instance-level vs task-level aggregation, Kemeny consensus, Borda approximation).
- Supports: mean aggregation is problematic when metrics have different scales. The paper proposes rank aggregation via Kemeny consensus, d(η,τ) = Σ_{i<j} 1[(η_i − η_j)(τ_i − τ_j) < 0], approximated by Borda count. It works at the task level and the instance level, and gives different SOTA conclusions than the mean on over 270k scores.

### rofin2023votenrank
- Title: Vote'n'Rank: Revision of Benchmarking with Social Choice Theory
- Authors: Mark Rofin, Vladislav Mikhailov, Mikhail Florinskiy, Andrey Kravchenko, Elena Tutubalina, Tatiana Shavrina, Daniel Karabekyan, Ekaterina Artemova
- Date: EACL 2023; arXiv 2210.05769 (v3 2023-02-12)
- URL: https://arxiv.org/abs/2210.05769
- Type: method paper
- Verification: full-text (pdftotext): Abstract, §2 (rules: Plurality, Borda, Dowdall, Threshold, Baldwin, Condorcet, Copeland, Minimax), §3.3 "Robustness to Missing Scores" (Eq. 3).
- Supports:
  - Mean aggregation is "utilitarian". Social-choice rules can pick different winners on GLUE, SuperGLUE and VALUE.
  - Missing cells: majority-relation rules (Copeland, Minimax) use m1 µ m2 ⇔ Σ_i w_i R(m1, m2, i) > 0 and ignore task pairs where either score is missing, "without losing any information whilst accounting for the available criteria". On VALUE, where HUMAN has 6 of 11 tasks, HUMAN becomes the Condorcet winner.
  - Kemeny is excluded because it is NP-hard.
- Caveats: dropping missing pairs assumes the cells are missing at random with respect to performance.

### zhang2024tradeoffs
- Title: Inherent Trade-Offs between Diversity and Stability in Multi-Task Benchmarks
- Authors: Guanhua Zhang, Moritz Hardt
- Date: ICML 2024; arXiv 2405.01719 (v2 2024-05-06)
- URL: https://arxiv.org/abs/2405.01719
- Type: method paper / empirical study
- Verification: full-text (pdftotext): Abstract, §1 (Fig. 1–2).
- Supports:
  - Cardinal benchmarks average scores, while ordinal benchmarks aggregate per-task rankings (e.g. HELM's win rate). Arrow's theorem applies to ordinal systems, and the failing property is independence of irrelevant alternatives: adding irrelevant models can reorder the top contenders.
  - Diversity is measured as 1 − Kendall's W across tasks. Sensitivity is the maximum rank change under irrelevant task transformations.
  - Across 7 cardinal and 11 ordinal benchmarks, "the more diverse a multi-task benchmark, the more sensitive to trivial changes it is".

### peyrard2021paired
- Title: Better than Average: Paired Evaluation of NLP Systems
- Authors: Maxime Peyrard, Wei Zhao, Steffen Eger, Robert West
- Date: ACL-IJCNLP 2021 (2021.acl-long.179)
- URL: https://aclanthology.org/2021.acl-long.179
- Type: method paper / empirical study
- Verification: full-text (pdftotext): Abstract, Fig. 1, §2 (Eq. 1), §6 limitations.
- Supports:
  - Mean and median ignore instance-level pairing. Bradley–Terry uses P(A > B) = λ_A/(λ_A + λ_B), fitted from per-instance wins. For two systems, λ̂_A is the number of instances A wins.
  - Re-evaluating 296 setups, the choice of aggregation changes the SOTA conclusion in about 30% of them.
  - Limitations: adding or removing a baseline can change other systems' BT scores, which links to Arrow. BT assumes constant relative strengths across instances. IRT, Elo and TrueSkill are possible refinements.
- Caveats: BT discards the magnitude of differences (like the sign test), which agarwal2021precipice also notes for probability of improvement.

## Topic notes

### 1. Binomial confidence intervals
- **Wald interval**: p̂ ± z·sqrt(p̂(1−p̂)/n). Its coverage is erratic and non-monotone in n and p. It collapses to width 0 at p̂ ∈ {0,1} and can leave [0,1] (brown2001binomial abstract; bowyer2025clt §3.1 with the explicit boundary condition and Fig. 1).
- **Wilson score interval** (wilson1927, formula from bowyer2025clt Eq. 12): obtained by inverting the score test. Its centre is (p̂ + z²/2n)/(1 + z²/n). It is recommended for small n (brown2001binomial abstract) and keeps near-nominal coverage down to N = 3–10 when averaged over θ ~ U(0,1) (bowyer2025clt Fig. 2).
- **Clopper–Pearson** (bowyer2025clt App. A.3): it inverts two one-sided binomial tests at α/2, so coverage is ≥ 1−α everywhere but conservative (statsmodels docs; bowyer2025clt). Equivalent quantile form: Beta(α/2; k, n−k+1) to Beta(1−α/2; k+1, n−k). This identity is standard but was not read from a source here.
- **Agresti–Coull and Jeffreys**: recommended for larger n (AC) and small n (Jeffreys) per the brown2001binomial abstract. Formulas were not verified from primary text.
- **Bayesian Beta(1+S, 1+N−S)** credible interval: bowyer2025clt Eq. 7. It is close to Wilson in practice.
- **Pitfalls**: the bootstrap percentile interval also under-covers at small N (bowyer2025clt Fig. 2). For fractional (non-Bernoulli) scores use SE_CLT, not the Bernoulli formula (miller2024errorbars §2.1).

### 2. Paired comparisons of two systems on the same items
- **Why pair**: Var_paired = Var_unpaired − 2Cov/n (miller2024errorbars §4.2). Correlated systems reach significance with smaller gains (berg2012empirical). Power depends on the agreement rate Pa (card2020power §3.1).
- **McNemar family** (fagerland2013mcnemar): all versions use only the discordant counts n12 and n21. Recommended: the mid-p test (never exceeded the nominal level in 9,595 scenarios) or the asymptotic test without CC. Not recommended: exact conditional and CC versions, which are over-conservative. Dietterich (1998, abstract) found McNemar has low type I error and is the only acceptable test when an algorithm can be run once.
- **Paired bootstrap** (koehn2004bootstrap; berg2012empirical Fig. 1): resample items, recompute any metric (works for corpus-level and non-decomposable metrics), and use the 2δ recentring for the p-value. Caveat: anti-conservative for small n (sogaard2014pvalue: use only for n > 200; dror2018hitchhiker §3.2).
- **Approximate randomization / permutation** (riezler2005pitfalls Fig. 1): swap each item's pair with probability ½, then p = (c+1)/(R+1). More conservative than the bootstrap. Its inference conditions on the test set.
- **Disagreement**: berg2012empirical prefers the bootstrap because its null does not condition on the test set, while riezler2005pitfalls prefers AR for type I error accuracy. dror2018hitchhiker's Fig. 1 allows either for small data, but its text warns against bootstrap at small n.
- **Bayesian alternatives**: paired Bayes (bowyer2025clt §3.4), Bayesian correlated t-test with ROPE (benavoli2017bayesian).
- **Two systems over many runs/seeds**: P(A>B) with a "meaningful" threshold γ = 0.75 (bouthillier2021variance). Report score distributions (reimers2017distributions).

### 3. Power and sample size
- **Closed form** (miller2024errorbars Eq. 9): n = (z_{α/2}+z_β)²(ω² + σ_A²/K_A + σ_B²/K_B)/δ². The MDE follows from Eq. 10. Example: n ≈ 969 for δ = 3 pts under the stated assumptions.
- **Simulation-based power for McNemar** (card2020power), parametrised by (n, Δacc, Pa). Underpowered comparisons are common (GLUE: 46% adequately powered), and significant results from underpowered tests exaggerate effects (Type M).
- **Small-n caveat** (bowyer2025clt): power formulas built on the CLT inherit its under-coverage below a few hundred items. Simulate with exact/mid-p tests instead.
- **Equivalence/NI** needs much larger n than superiority for tight margins (walker2011equivalence Table 2: 1,048 per group at δ = .10 vs 26,185 at δ = .06).

### 4. Repeated runs and variance
- **Sources of variance**: question sampling, generation stochasticity, seeds/initialisation, data order, hyperparameters (bouthillier2021variance; miller2024errorbars §3; madaan2024variance).
- **Resampling answers K times per item**: average within the item, then compute the SE across items. Never pool K·N answers as independent (miller2024errorbars §3.1). Do not lower temperature only to reduce variance (§3.3).
- **Continuous metrics** (probabilities, NLL) have higher SNR than discrete accuracy (madaan2024variance Table 2; heineman2025signalnoise abstract; miller2024errorbars §3.2 next-token probabilities).
- **Reporting**: score distributions and seeds (reimers2017distributions), expected max performance vs budget (dodge2019showyourwork), stratified bootstrap CIs, IQM and performance profiles (agarwal2021precipice).

### 5. Multiplicity
- **FWER**: Bonferroni (α/m). Holm step-down (p_(i) vs α/(m−i+1)) is uniformly more powerful with no dependence assumptions (holm1979 via demsar2006 §3.2.2). Hochberg and Hommel are more powerful but rely on Simes-type conditions.
- **FDR**: Benjamini–Hochberg controls the expected false-discovery proportion. It is proven for independent statistics (abstract) and gains power when many nulls are false. Demšar considers FDR less suitable for algorithm comparison.
- **Practice evidence**: only 3 of 110 ACL 2017 multi-dataset papers corrected for multiplicity (dror2018hitchhiker). Søgaard et al. suggest p < 0.0025 as an effective threshold. Multiple metrics are a hidden multiplicity source (sogaard2014pvalue).
- **Preregistration** (vanmiltenburg2021prereg): pre-specify hypotheses, dependent variables, analyses, exclusions, sample size and stopping rule, and report deviations. The family over which Holm is applied should itself be preregistered.

### 6. Equivalence / non-inferiority; absence of evidence
- A non-significant difference is not evidence of no difference (altman1995absence title claim; lakens2017equivalence).
- **TOST**: pre-specify the SESOI bounds (−Δ_L, Δ_U). Equivalence holds at α if the (1−2α) CI, i.e. the 90% CI for α = .05, lies inside the bounds (lakens2017equivalence; walker2011equivalence).
- **Non-inferiority**: the lower limit of the (1−2α) CI for (new − reference) lies above −δ (walker2011equivalence). Regulatory guidance on margins exists (fda2016noninferiority, landing page only).
- **Bayesian analogue**: ROPE posterior mass (benavoli2017bayesian), e.g. ±1% accuracy.
- **Pitfall**: margins chosen after seeing data. With small n, CIs are wide, so most comparisons are "undetermined" (Lakens' fourth outcome).

### 7. Grouped / dependent data
- Items drawn in clusters (passages, translated variants, templates, the same source item) violate independence. Naive SEs can be about 3× too small (miller2024errorbars Table 4; Moulton factor in cameron2015cluster).
- **Clustered SE** (miller2024errorbars Eqs. 4 and 8). The cluster bootstrap resamples whole clusters (cameron2015cluster §II.F) and is consistent under both transformation and random-effect models (field2007clustered abstract).
- **Few clusters** (< 20–50): CRVE over-rejects (e.g. .208 at G = 5). Use CR2, T(G−1) critical values, or the wild cluster bootstrap (cameron2015cluster §VI). For very small G, bowyer2025clt finds only a hierarchical Bayesian (beta-binomial) model covers.
- **Multi-task aggregates**: stratify the bootstrap by task (agarwal2021precipice). Treat sub-tasks separately rather than pooling N across non-IID sub-tasks (bowyer2025clt §1).

### 8. Multiple datasets / aggregation across tasks
- **Frequentist over datasets** (demsar2006): Wilcoxon signed-rank for two systems, Friedman (or Iman–Davenport F_F) for k systems, then post-hoc tests. Nemenyi CD for all pairs, or Holm against a control. Benavoli2016 warns that mean-rank post-hoc results depend on the pool of algorithms, so use pairwise Wilcoxon or sign tests plus a correction. The sampling unit is the dataset, so N is small and power is low.
- **Bayesian** (benavoli2017bayesian): hierarchical correlated t-test and Bayesian signed-rank with a ROPE.
- **What the mean hides**:
  - Commensurability and scale (demsar2006; colombo2022bestsystems).
  - Task-selection sensitivity (dehghani2021lottery: 6 Top-1 winners across 70 four-task subsets).
  - The diversity vs stability trade-off and IIA failure for ordinal aggregates (zhang2024tradeoffs).
  - Leaderboard utility differs from user utility, since cost is ignored (ethayarajh2020utility).
- **Alternatives**: Kemeny/Borda rank aggregation (colombo2022bestsystems); social-choice rules including Copeland and Minimax (rofin2023votenrank); Bradley–Terry paired aggregation (peyrard2021paired, which changes SOTA in about 30% of setups but discards magnitude); IQM, optimality gap, average probability of improvement and performance profiles (agarwal2021precipice).
- **Missing cells**:
  - rofin2023votenrank: majority-relation rules ignore pairs with a missing score.
  - colombo2022bestsystems: ranking-based aggregation needs only per-task rankings.
  - The mean over available tasks silently changes the task mix per system, the same mechanism as task-selection bias in dehghani2021lottery. This is an inference, not a claim from that paper.
  - All of these assume missingness is unrelated to performance. None of the sources verified here gives a formal missing-data treatment such as MAR modelling or imputation.

### Methodological evidence vs vendor/benchmark-author claims
- miller2024errorbars is an Anthropic-authored methods note. Its formulas are standard survey-sampling and econometrics results (clustered SE as in Abadie et al. 2023, and Cameron & Miller). Its "≥1,000 questions" figure depends on assumed ω² = 1/9 and δ = 3 pts, and is not a general law.
- bowyer2025clt is a position paper whose simulations use the same uniform prior as the method it advocates.
- madaan2024variance (Meta) and heineman2025signalnoise (AI2) are developer studies on their own model families.
