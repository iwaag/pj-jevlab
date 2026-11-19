# Sources: Cluster D — datasets, validity, generalization, negatives/contrast data, contamination

Verification method. arXiv abstracts were fetched in bulk through the export.arxiv.org API (36 ids). That API returns raw abstract text, not a summary. Where "full-text" is marked, the PDF was downloaded with curl and converted with `pdftotext`, and the cited lines were read in raw text. Dataset facts come from Hugging Face Hub API JSON (`/api/datasets/<id>` cardData), raw README files on GitHub/HF, and the GitHub API. Non-arXiv metadata comes from the Crossref API. Accessed 2026-10-02 for all sources.

> Evidence notes for cluster D of [study/benchmark](../README.md), compiled 2026-10-02 in step2 of benchmark/p1 by a research subagent and reviewed by the lead session. The search log and gaps for this cluster are in [search-log.md](../search-log.md). Verification levels are per entry; claims beyond the stated level must not be attributed to a source.

## Source list

### messick1995validity
- Title: Validity of psychological assessment: Validation of inferences from persons' responses and performances as scientific inquiry into score meaning
- Authors / organization: Samuel Messick
- Date: 1995-09. American Psychologist 50(9):741-749
- URL / DOI: 10.1037/0003-066X.50.9.741 (ERIC EJ517194)
- Type: textbook/tutorial (classic measurement-theory article)
- Verification: abstract (ERIC abstract plus Crossref metadata; APA/psycnet full text not accessible)
- Supports: per the ERIC abstract, the article "presents a comprehensive review of validity that includes an empirical evaluation of the actual and potential consequences of score interpretation and use". Secondary descriptions (search snippets, ETS page) say it frames validity as a single unified construct-validity concept with six aspects: content, substantive, structural, generalizability, external, consequential. I did NOT verify that against primary text. Cite the "six aspects" only as a secondary characterization, or through jacobs2021measurement and wallach2025position, which explicitly adapt Messick.
- Caveats: the full text was not read.

### jacobs2021measurement
- Title: Measurement and Fairness
- Authors: Abigail Z. Jacobs, Hanna Wallach
- Date: arXiv 2019-12-11, v3 2021-03-12 (FAccT 2021)
- URL: arXiv:1912.05511
- Type: method paper / position
- Verification: full-text (§3.1 reliability, §3.2.1-3.2.7 validity)
- Supports: unobservable theoretical constructs are operationalized through a measurement model, and mismatches between construct and operationalization cause harms (abstract). §3.1 covers reliability, e.g. §3.1.1 test-retest reliability. Inter-rater reliability is discussed but deliberately omitted (fn. 4). §3.2 gives a "fairness-oriented conceptualization of construct validity" with seven aspects:
  - face validity (§3.2.1)
  - content validity (§3.2.2), including contestedness of constructs
  - convergent validity (§3.2.3)
  - discriminant validity (§3.2.4)
  - predictive validity (§3.2.5)
  - hypothesis validity (§3.2.6)
  - consequential validity (§3.2.7)
- Caveats: the paper is framed around fairness constructs, so applying it to capability benchmarks is an extrapolation. wallach2025position makes that extrapolation explicitly.

### wallach2025position
- Title: Position: Evaluating Generative AI Systems Is a Social Science Measurement Challenge
- Authors: Hanna Wallach, Meera Desai, A. Feder Cooper, Angelina Wang, et al. (Microsoft Research and others)
- Date: arXiv 2025-02-01, v2 2025-06-06. Proceedings of the 42nd ICML (2025), per the PDF footer
- URL: arXiv:2502.00561
- Type: position/survey
- Verification: full-text (§3 framework, around lines 195-210 of the extracted text; validity lenses list)
- Supports: a four-level framework adapted from Adcock & Collier (2001) with levels background concept → systematized concept → measurement instruments → measurements. The levels are linked by four processes:
  - systematization: narrowing the background concept into the systematized concept
  - operationalization: developing the instruments from the systematized concept
  - application: using the instruments to obtain measurements
  - interrogation: interrogating the validity of the concept, instruments and measurements

  Validity lenses are "adapted from Messick (1987) by Jacobs & Wallach (2021)": face, content, convergent, discriminant, predictive, hypothesis, consequential. Validity is context-dependent and "must be re-interrogated" when the measurement context changes. Face, content and consequential validity are especially useful for conceptual debates.
- Caveats: this is a position paper with no empirical validation of the framework.

### raji2021everything
- Title: AI and the Everything in the Whole Wide World Benchmark
- Authors: Inioluwa Deborah Raji, Emily M. Bender, Amandalynne Paullada, Emily Denton, Alex Hanna
- Date: arXiv 2021-11-26 (NeurIPS 2021 Datasets & Benchmarks)
- URL: arXiv:2111.15366
- Type: position/survey
- Verification: abstract
- Supports: a small set of influential benchmarks is treated as a stand-in for "general" progress. The paper explores "the construct validity issues in their framing as the functionally 'general' broad measures of progress they are set up to be".
- Caveats: abstract only, so no specific recommendations are attributed.

### bowman2021fix
- Title: What Will it Take to Fix Benchmarking in Natural Language Understanding?
- Authors: Samuel R. Bowman, George E. Dahl
- Date: arXiv 2021-04-05, v3 2021-10-15 (NAACL 2021)
- URL: arXiv:2104.02145
- Type: position/survey
- Verification: full-text (§1 criteria list; §3.1 Validity; §3.3 Statistical Power)
- Supports: four criteria.
  1. Good benchmark performance should imply robust in-domain performance on the task (validity).
  2. Examples should be accurately and unambiguously annotated.
  3. Benchmarks should offer adequate statistical power.
  4. Benchmarks should reveal harmful social biases and should not incentivize biased systems.

  The validity section requires that the evaluation set reflect the full range of linguistic variation in the domain, test all expected behaviours, and be "sufficiently free of annotation artifacts". On power (§3.3), a 1-point minimum detectable effect around 80% accuracy needs "a few thousand examples" (citing Card et al. 2020). Detecting 98%→98.1% "requires two orders of magnitude more evaluation data". The paper argues adversarial data collection "does not meaningfully address the causes" of benchmark failures (abstract).
- Caveats: this contradicts the Dynabench position (kiela2021dynabench); see Topic notes.

### liao2021learning
- Title: Are We Learning Yet? A Meta Review of Evaluation Failures Across Machine Learning
- Authors: Thomas I. Liao, Rohan Taori, Inioluwa Deborah Raji, Ludwig Schmidt
- Date: NeurIPS 2021 Datasets & Benchmarks (round 2)
- URL: https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/file/757b505cfd34c64c85ca5b5690ee5293-Paper-round2.pdf
- Type: position/survey (meta-review of 107 survey papers)
- Verification: full-text (abstract; §3 Internal validity: §3.1-3.4; §4 External validity headings)
- Supports: a taxonomy of evaluation failures.
  - Internal validity (within one benchmark), §3:
    - implementation variations (§3.1). Example: BLEU parameter choices change scores by up to 1.8 BLEU, versus a 0.14 BLEU gap between #1 and #2 on one leaderboard.
    - errors in test-set construction (§3.2): label errors, label leakage, test-set size, contaminated data. Example: 10% of CIFAR-100 test images have train duplicates, and deduplication lowers performance by up to 14% relative.
    - overfitting from test-set reuse (§3.3)
    - inadequate baselines (§3.4)
  - External validity (transfer across problems), §4: types of transfer, metric misalignment, comparisons to human performance.
- Caveats: the paper gives examples, not effect-size estimates.

### devries2020ecological
- Title: Towards Ecologically Valid Research on Language User Interfaces
- Authors: Harm de Vries, Dzmitry Bahdanau, Christopher Manning
- Date: arXiv 2020-07-28
- URL: arXiv:2007.14435
- Type: position/survey
- Verification: abstract
- Supports: language user interface (LUI) benchmarks "emphasize the quantity of collected data at the cost of its naturalness and relevance to real-world LUI use cases". The authors call this "low ecological validity". They describe an ideal methodology, categorize "five common ways" benchmarks deviate from it, and give recommendations.
- Caveats: the five deviations are not enumerated here because only the abstract was read.

### bean2025measuring
- Title: Measuring what Matters: Construct Validity in Large Language Model Benchmarks
- Authors: Andrew M. Bean, Ryan Othniel Kearns, Angelika Romanou, et al. (42 authors; Oxford Internet Institute and others)
- Date: arXiv 2025-11-03 (NeurIPS 2025 Datasets & Benchmarks track, per search results and HF paper page)
- URL: arXiv:2511.04703
- Type: position/survey (systematic review)
- Verification: full-text (§5 Recommendations 5.1-5.8). Existence confirmed.
- Supports: 29 expert reviewers examined 445 LLM benchmarks (abstract). The eight recommendations, each with a checklist:
  1. Define the phenomenon (§5.1). 78.2% of benchmarks provide definitions, 47.8% target phenomena without consensus definitions, and 61.2% have sub-components.
  2. Measure the phenomenon and only the phenomenon (§5.2). Control confounds such as output format: 21.1% of benchmarks require specific formats. Validate LLM-based answer parsers.
  3. Construct a representative dataset (§5.3). 27.0% use convenience sampling, only 17.1% use random or stratified sampling, and 47.5% use synthetic items.
  4. Acknowledge limitations of reusing datasets (§5.4). 38.2% reuse data from earlier benchmarks or exams.
  5. Prepare for contamination (§5.5). Vet items at creation time; consider dynamic or procedurally generated tasks.
  6. Use statistical methods to compare models (§5.6). Report sample size, justify power, and report uncertainty. Only 16.0% of benchmarks run any statistical test.
  7. Conduct error analysis (§5.7). Check whether failures correlate with non-targeted confounders.
  8. Justify construct validity (§5.8). Only 53.4% justify why the benchmark is a valid measure.
- Caveats: the percentages come from reviewer coding of papers, which the authors note involves judgment.

### gururangan2018annotation
- Title: Annotation Artifacts in Natural Language Inference Data
- Authors: Suchin Gururangan, Swabha Swayamdipta, Omer Levy, Roy Schwartz, Samuel R. Bowman, Noah A. Smith
- Date: arXiv 2018-03-06 (NAACL 2018)
- URL: arXiv:1803.02324
- Type: empirical study
- Verification: abstract
- Supports: a hypothesis-only text classifier labels about 67% of SNLI and 53% of MultiNLI correctly without seeing the premise. Negation and vagueness correlate with specific classes, so NLI success "has been overestimated".
- Caveats: none noted. Chance level is about 33% for 3 classes.

### mccoy2019hans
- Title: Right for the Wrong Reasons: Diagnosing Syntactic Heuristics in Natural Language Inference
- Authors: R. Thomas McCoy, Ellie Pavlick, Tal Linzen
- Date: arXiv 2019-02-04 (ACL 2019)
- URL: arXiv:1902.01007
- Type: benchmark/dataset paper (controlled diagnostic set)
- Verification: abstract
- Supports: HANS targets three fallible heuristics: lexical overlap, subsequence, and constituent. MNLI-trained models, BERT included, "perform very poorly on HANS", which suggests they adopted those heuristics.
- Caveats: exact accuracy numbers were not read.

### geirhos2020shortcut
- Title: Shortcut Learning in Deep Neural Networks
- Authors: Robert Geirhos, Jörn-Henrik Jacobsen, Claudio Michaelis, Richard Zemel, Wieland Brendel, Matthias Bethge, Felix A. Wichmann
- Date: arXiv 2020-04-16, v5 2023-11-21 (Nature Machine Intelligence 2020)
- URL: arXiv:2004.07780
- Type: position/survey (perspective)
- Verification: abstract
- Supports: definition: "Shortcuts are decision rules that perform well on standard benchmarks but fail to transfer to more challenging testing conditions, such as real-world scenarios." The paper gives recommendations for interpretation and benchmarking.
- Caveats: the specific recommendations were not read.

### gardner2020contrast
- Title: Evaluating Models' Local Decision Boundaries via Contrast Sets
- Authors: Matt Gardner, Yoav Artzi, et al.
- Date: arXiv 2020-04-06, v2 2020-10-01 (Findings of EMNLP 2020)
- URL: arXiv:2004.02709
- Type: method paper / benchmark paper
- Verification: full-text (§2.2 Definitions; Table 2 caption; §1)
- Supports (§2.2):
  - Local decision boundary around pivot x: {(x', y') | d(x, x') < ε}.
  - A contrast set C(x) is any sample of points from that local boundary. Typically y' ≠ y.
  - Contrast consistency is all({ŷ = y' ∀(x', y') ∈ C(x)}). Table 2 reports it as "the percentage of the contrast sets for which a model's predictions are correct for all examples in the set (including the original example)".
  - About one person-week of work yields roughly 1,000 perturbed instances (§1).
  - Models drop up to 25% on contrast sets (abstract) and do worse still on consistency.
- Caveats: the authors note that numbers are not comparable across datasets because sizes, models and designs differ (§4).

### kaushik2020cad
- Title: Learning the Difference that Makes a Difference with Counterfactually-Augmented Data
- Authors: Divyansh Kaushik, Eduard Hovy, Zachary C. Lipton
- Date: arXiv 2019-09-26, v2 2020-02-14 (ICLR 2020)
- URL: arXiv:1909.12434
- Type: method paper / dataset paper
- Verification: abstract
- Supports: humans revise documents so that each one (i) accords with a counterfactual target label, (ii) stays internally coherent, and (iii) avoids unnecessary changes. Classifiers trained on original data fail on the revised data and vice versa. Training on the combined data reduces sensitivity to spurious features. Datasets are public.
- Caveats: none noted.

### ribeiro2020checklist
- Title: Beyond Accuracy: Behavioral Testing of NLP models with CheckList
- Authors: Marco Tulio Ribeiro, Tongshuang Wu, Carlos Guestrin, Sameer Singh
- Date: arXiv 2020-05-08 (ACL 2020)
- URL: arXiv:2005.04118
- Type: method paper
- Verification: full-text (§2.2 Test Types)
- Supports: a capability × test-type matrix with three test types, reported as failure rate per test.
  - MFT (Minimum Functionality test): "a collection of simple examples (and labels) to check a behavior within a capability", inspired by unit tests and "particularly useful for detecting when models use shortcuts".
  - INV (Invariance test): "label-preserving perturbations to inputs" where the prediction is expected to stay the same, e.g. changing location names, adding typos.
  - DIR (Directional Expectation test): "the label is expected to change in a certain way". Example: adding "You are lame." should not make sentiment more positive.
  - INV and DIR are inspired by software metamorphic testing.
- Caveats: the authors do not frame failure rates as estimates of a population quantity, because test cases are generated from templates.

### rajpurkar2018squad2
- Title: Know What You Don't Know: Unanswerable Questions for SQuAD
- Authors: Pranav Rajpurkar, Robin Jia, Percy Liang
- Date: arXiv 2018-06-11 (ACL 2018)
- URL: arXiv:1806.03822. HF dataset rajpurkar/squad_v2
- Type: benchmark/dataset paper
- Verification: full-text (Table 2, §4.1-4.3, Table 1). The HF card was read through the API.
- Supports:
  - Over 50,000 unanswerable questions (53,775 in the text) were "written adversarially by crowdworkers to look similar to answerable ones".
  - Each unanswerable question comes with a plausible-answer span as a distractor.
  - Table 2 split sizes:

    | Split | Total | Negatives | Notes |
    |---|---|---|---|
    | Train | 130,319 | 43,498 | about 2:1 answerable to unanswerable |
    | Dev | 11,873 | 5,945 | about 1:1 |
    | Test | 8,862 | 4,332 | hidden |

  - Table 1 gives a typology of negative-example phenomena from 100 inspected dev negatives.
  - A strong system scores 86% F1 on SQuAD 1.1 but 66% on 2.0 (abstract).
  - HF license: cc-by-sa-4.0. HF splits: train 130,319 and validation 11,873. HF "validation" is the official dev set; the official test set is hidden.
- Caveats: unanswerables are adversarial by construction, so they are not a natural sample of user queries.

### larson2019clinc
- Title: An Evaluation Dataset for Intent Classification and Out-of-Scope Prediction
- Authors: Stefan Larson et al. (Clinc / University of Michigan)
- Date: arXiv 2019-09-04 (EMNLP-IJCNLP 2019)
- URL: arXiv:1909.02027. GitHub clinc/oos-eval. HF clinc/clinc_oos
- Type: benchmark/dataset paper
- Verification: full-text (§3.2 OOS prediction, §3.3 Metrics). Repo README, LICENSE and HF API card were all read.
- Supports:
  - Size: 150 intents in 10 domains. The Full variant has 100 train / 20 val / 30 test per intent, plus out-of-scope (OOS) 100 train / 100 val / 1,000 test (README).
  - Variants: Small, Imbalanced, and OOS+ (250 OOS train) (§3).
  - Three OOS baselines (§3.2):
    - oos-train: a 151st class
    - oos-threshold: a threshold on the classifier probability, chosen to maximize validation score with OOS treated as its own intent
    - oos-binary: two-stage
  - Metrics (§3.3): in-scope accuracy over 150 intents and OOS recall.
  - License: LICENSE file is CC BY 3.0 Unported. HF card says cc-by-3.0. The GitHub API reports "NOASSERTION".
  - HF split sizes: plus has train 15,250 / val 3,100 / test 5,500.
- Caveats: OOS queries were crowdsourced, so they are not real traffic. The README notes that others named the dataset "CLINC150". Recall-only OOS evaluation ignores false OOS rejections of in-scope queries; in-scope accuracy partially captures those.

### casanueva2020banking77
- Title: Efficient Intent Detection with Dual Sentence Encoders
- Authors: Iñigo Casanueva, Tadas Temčinas, Daniela Gerz, Matthew Henderson, Ivan Vulić (PolyAI)
- Date: arXiv 2020-03-10 (NLP4ConvAI workshop 2020)
- URL: arXiv:2003.04807. GitHub PolyAI-LDN/task-specific-datasets. HF PolyAI/banking77
- Type: method paper + dataset
- Verification: abstract. Dataset facts come from the official README, GitHub API and HF API.
- Supports: a single-domain (online banking) intent dataset with 13,083 examples and 77 intents (abstract). The README lists train 10,003 and test 3,080. License is CC BY 4.0 (GitHub API spdx and HF card).
- Caveats: no official validation split and no out-of-scope class. Fine-grained, overlapping intents make it a near-miss confusion benchmark, not an abstention benchmark. Anyone using it for OOS must hold out intents themselves; that is common practice, but not part of the dataset definition.

### schuster2021vitaminc
- Title: Get Your Vitamin C! Robust Fact Verification with Contrastive Evidence
- Authors: Tal Schuster, Adam Fisch, Regina Barzilay
- Date: arXiv 2021-03-15 (NAACL 2021)
- URL: arXiv:2103.08541. HF tals/vitaminc. GitHub TalSchuster/VitaminC
- Type: benchmark/dataset paper
- Verification: abstract. The HF README (license) and GitHub README (test sets real/synthetic) were also read.
- Supports: over 100,000 Wikipedia revisions plus synthetic ones give more than 400,000 claim-evidence pairs. Examples are contrastive: "evidence pairs that are nearly identical in language and content, with the exception that one supports a given claim while the other does not". Training on it improves adversarial fact verification by 10% and adversarial NLI by 6%. HF data license is cc-by-sa-3.0. The GitHub code repository is MIT. Test sets are split into "real" (revision-based) and "synthetic".
- Caveats: data and code licenses differ. Synthetic pairs may carry generation artifacts, so real and synthetic should be reported separately.

### koh2021wilds
- Title: WILDS: A Benchmark of in-the-Wild Distribution Shifts
- Authors: Pang Wei Koh, Shiori Sagawa, et al.
- Date: arXiv 2020-12-14, v3 2021-07-16 (ICML 2021)
- URL: arXiv:2012.07421, https://wilds.stanford.edu
- Type: benchmark/dataset paper
- Verification: abstract (the PDF was downloaded but not read in detail)
- Supports: 10 datasets with naturally arising shifts (across hospitals, camera traps, time and location). Standard training yields "substantially lower out-of-distribution than in-distribution performance", and existing robustness methods do not close the gap.
- Caveats: the paper's own definitions of domain generalization versus subpopulation shift were not read.

### recht2019imagenet
- Title: Do ImageNet Classifiers Generalize to ImageNet?
- Authors: Benjamin Recht, Rebecca Roelofs, Ludwig Schmidt, Vaishaal Shankar
- Date: arXiv 2019-02-13, v2 2019-06-12 (ICML 2019)
- URL: arXiv:1902.10811
- Type: empirical study
- Verification: abstract
- Supports: new test sets were built by following the original collection processes. Accuracy drops 3-15% on CIFAR-10 and 11-14% on ImageNet. Gains on the original test sets translate to larger gains on the new ones. The drops are "not caused by adaptivity" but by inability to generalize to slightly "harder" images.
- Caveats: none noted.

### quinonero2009shift
- Title: Dataset Shift in Machine Learning
- Authors (eds.): Joaquin Quiñonero-Candela, Masashi Sugiyama, Anton Schwaighofer, Neil D. Lawrence
- Date: MIT Press. Crossref issued date 2008-12-12; commonly cited as 2009
- URL / DOI: 10.7551/mitpress/9780262170055.001.0001
- Type: textbook/tutorial (edited volume)
- Verification: abstract (book description from Crossref)
- Supports: "Dataset shift ... occurs when the joint distribution of inputs and outputs differs between training and test stages. Covariate shift, a particular case of dataset shift, occurs when only the input distribution changes."
- Caveats: chapter-level content was not read.

### kiela2021dynabench
- Title: Dynabench: Rethinking Benchmarking in NLP
- Authors: Douwe Kiela, Max Bartolo, Yixin Nie, et al.
- Date: arXiv 2021-04-07 (NAACL 2021)
- URL: arXiv:2104.14337
- Type: benchmark/dataset paper (platform) / position
- Verification: abstract
- Supports: human-and-model-in-the-loop collection in which annotators write examples that a target model misclassifies but a person would not. Motivation: models "quickly achieve outstanding performance on benchmark tasks but nonetheless fail on simple challenge examples".
- Caveats: bowman2021fix disputes that adversarial collection fixes validity.

### ott2022mapping
- Title: Mapping global dynamics of benchmark creation and saturation in artificial intelligence
- Authors: Simon Ott, Adriano Barbosa-Silva, Kathrin Blagec, Jan Brauner, Matthias Samwald
- Date: arXiv 2022-03-09, v4 2022-10-07 (Nature Communications 2022)
- URL: arXiv:2203.04592
- Type: empirical study
- Verification: abstract
- Supports: covers 3,765 CV and NLP benchmarks. "A large fraction of benchmarks quickly trended towards near-saturation", many benchmarks are rarely used, and performance gains come in "unforeseen bursts".
- Caveats: the operational definition of saturation was not read.

### dwork2015reusable
- Title: The reusable holdout: Preserving validity in adaptive data analysis (Science), plus the companion paper "Generalization in Adaptive Data Analysis and Holdout Reuse" (arXiv:1506.02629, NeurIPS 2015)
- Authors: Cynthia Dwork, Vitaly Feldman, Moritz Hardt, Toniann Pitassi, Omer Reingold, Aaron Roth
- Date: Science 349(6248):636-638, 2015-08-07. arXiv 2015-06-08
- URL / DOI: 10.1126/science.aaa9375. arXiv:1506.02629
- Type: method paper
- Verification: abstract (Science editor's summary via Crossref; arXiv abstract of the companion). Science full text returned 403.
- Supports: "Reusing a holdout set adaptively multiple times can easily lead to overfitting to the holdout set itself". The paper gives an algorithm (Thresholdout in the companion) that validates many adaptively chosen hypotheses "while provably avoiding overfitting", based on differential privacy. A description-length approach and "approximate max-information" are also given (arXiv abstract).
- Caveats: the Thresholdout parameters and guarantees were not read. roelofs2019metaanalysis finds that adaptive overfitting is small in practice on Kaggle.

### roelofs2019metaanalysis
- Title: A Meta-Analysis of Overfitting in Machine Learning
- Authors: Rebecca Roelofs, Vaishaal Shankar, Benjamin Recht, Sara Fridovich-Keil, Moritz Hardt, John Miller, Ludwig Schmidt
- Date: NeurIPS 2019
- URL: https://proceedings.neurips.cc/paper/2019/file/ee39e503b6bedf0c98c388b7e8589aca-Paper.pdf
- Type: empirical study
- Verification: abstract (from the PDF text)
- Supports: in more than 100 Kaggle competitions, comparing the public leaderboard (a reused holdout) with the private test set (used once) shows "little evidence of substantial overfitting". Search snippets say 112 competitions; the abstract text read says "over one hundred".
- Caveats: Kaggle practice bounds adaptivity (submission limits). This does not cover contamination or model selection on tiny dev sets.

### kapoor2023leakage
- Title: Leakage and the reproducibility crisis in machine-learning-based science
- Authors: Sayash Kapoor, Arvind Narayanan
- Date: arXiv 2022-07-14. Patterns 4(9):100804, 2023-09 (Crossref)
- URL / DOI: 10.1016/j.patter.2023.100804. arXiv:2207.07048
- Type: empirical study / survey
- Verification: full-text (arXiv v1 §2.4 taxonomy)
- Supports: leakage errors were found in 17 fields, affecting 329 papers (abstract). Taxonomy (§2.4):
  - [L1] Lack of clean train/test separation:
    - L1.1 no test set
    - L1.2 pre-processing on train and test together
    - L1.3 feature selection on train and test together
    - L1.4 duplicates
  - [L2] Illegitimate features
  - [L3] Test set not drawn from the distribution of scientific interest:
    - L3.1 temporal leakage
    - L3.2 non-independence between train and test samples
    - L3.3 sampling bias in the test distribution

  The paper proposes "model info sheets". In the civil-war prediction case study, the claimed superiority of complex models over logistic regression fails to reproduce.
- Caveats: the arXiv v1 was read, not the Patterns version of record.

### lewis2021overlap
- Title: Question and Answer Test-Train Overlap in Open-Domain Question Answering Datasets
- Authors: Patrick Lewis, Pontus Stenetorp, Sebastian Riedel
- Date: arXiv 2020-08-06 (EACL 2021)
- URL: arXiv:2008.02637
- Type: empirical study
- Verification: abstract
- Supports: in WebQuestions, TriviaQA and Open Natural Questions:
  - 60-70% of test answers appear somewhere in training.
  - 30% of test questions have a near-duplicate paraphrase in training.
  - Models do much worse on non-memorizable questions: a mean absolute gap of 63% between repeated and non-repeated data.
  - Nearest-neighbour baselines beat a BART closed-book model.
- Caveats: none noted.

### gorman2019standard
- Title: We need to talk about standard splits
- Authors: Kyle Gorman, Steven Bedrick
- Date: ACL 2019
- URL: https://aclanthology.org/P19-1267
- Type: empirical study
- Verification: full-text (abstract, §1.1)
- Supports: reproduction of nine POS taggers fails to reproduce some rankings under random splits, so the paper recommends randomly generated splits for system comparison. §1.1 describes McNemar for paired comparison: under δ=0, n_{1>2} ~ Bin(n, 0.5) with n = n_{1>2} + n_{2>1}. A Bonferroni correction is used across splits.
- Caveats: søgaard2021random argues that random splits are also overly optimistic.

### sogaard2021random
- Title: We Need to Talk About Random Splits
- Authors: Anders Søgaard, Sebastian Ebert, Jasmijn Bastings, Katja Filippova
- Date: arXiv 2020-05-01, v3 2021-04-26 (EACL 2021)
- URL: arXiv:2005.00636
- Type: empirical study / position
- Verification: abstract
- Supports: random splits, like standard splits, give "overly optimistic performance estimates". Even worst-case biased splits often under-estimate error on new in-domain samples, which "invalidates the covariate shift assumption". Recommendation: use multiple independent test sets, or failing that, multiple biased splits instead of multiple random splits.
- Caveats: none noted.

### dodge2021c4
- Title: Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus
- Authors: Jesse Dodge, Maarten Sap, Ana Marasović, et al.
- Date: arXiv 2021-04-18, v2 2021-09-30 (EMNLP 2021)
- URL: arXiv:2104.08758
- Type: empirical study
- Verification: abstract
- Supports: C4 contains "evaluation examples from other benchmark NLP datasets" and machine-generated text, and blocklist filtering disproportionately removes text from and about minority individuals. sainz2023trouble also cites Dodge et al. Table 2 for benchmarks found in C4; Table 2 itself was not read here.
- Caveats: none noted.

### brown2020gpt3
- Title: Language Models are Few-Shot Learners
- Authors: Tom B. Brown et al. (OpenAI)
- Date: arXiv 2020-05-28, v4 2020-07-22 (NeurIPS 2020)
- URL: arXiv:2005.14165
- Type: method paper (includes a contamination analysis)
- Verification: full-text (§4 "Measuring and Preventing Memorization of Benchmarks"; Appendix C; Table C.1)
- Supports:
  - A bug meant detected overlaps were only partially removed from training data (§4).
  - Clean subsets drop examples with 13-gram overlap with the pretraining set, or whole-example overlap when shorter than 13 grams (§4).
  - Appendix C actually uses a variable N: the 5th-percentile example length in words, with minimum 8 (non-synthetic tasks) and maximum 13. An example is dirty if it has "any N-gram overlap with any training document". 13-grams matching more than 10 training documents were ignored when filtering training data.
  - Reporting compares the relative change between the clean-only and full score. A clean score more than 1-2% worse suggests overfitting; a significantly better clean score suggests the filter flagged easier examples.
  - False positives are common for datasets with web-sourced background passages. DROP was 94% dirty because passages, not Q/A pairs, matched.
  - A quarter of benchmarks were over 50% potentially contaminated, yet performance changes were mostly negligible. The paper says it "cannot be sure that the clean subset is drawn from the same distribution".
- Caveats: §4 and Appendix C give different N (13 versus variable 8-13), so cite both. n-gram overlap misses paraphrase contamination (see dekoninck2024evading).

### magar2022contamination
- Title: Data Contamination: From Memorization to Exploitation
- Authors: Inbal Magar, Roy Schwartz
- Date: arXiv 2022-03-15 (ACL 2022)
- URL: arXiv:2203.08242
- Type: empirical study (controlled)
- Verification: full-text (§2 definitions)
- Supports: BERT is pretrained on Wikipedia plus labelled downstream data, and test sets are split into seen and unseen. Two measures:
  - mem: the MLM accuracy difference, seen minus unseen, for predicting the gold label before fine-tuning. It is a lower bound on label memorization.
  - expl: the task-performance difference, seen minus unseen, after fine-tuning.

  Memorization "does not guarantee exploitation". Both measures grow with the number of duplicates and with model size.
- Caveats: small BERT models and classification tasks only.

### sainz2023trouble
- Title: NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark
- Authors: Oscar Sainz, Jon Ander Campos, Iker García-Ferrero, Julen Etxaniz, Oier Lopez de Lacalle, Eneko Agirre
- Date: arXiv 2023-10-27 (Findings of EMNLP 2023)
- URL: arXiv:2310.18018
- Type: position/survey
- Verification: full-text (§4.1-4.3)
- Supports: data contamination is defined as "any breach in the strict control of datasets required by the experimental protocol". Types of contamination:
  - guideline contamination: annotation guidelines were seen
  - raw-text contamination: source text was seen, e.g. Wikipedia-based datasets
  - annotation contamination:
    - test split exposed: "the experiment is completely invalidated"
    - train or dev exposed: this invalidates zero/few-shot claims but not comparisons among models trained on those splits

  Contamination can also enter at supervised fine-tuning, including through distillation from contaminated teachers.
- Caveats: none noted.

### golchin2024timetravel
- Title: Time Travel in LLMs: Tracing Data Contamination in Large Language Models
- Authors: Shahriar Golchin, Mihai Surdeanu
- Date: arXiv 2023-08-16, v3 2024-02-21 (ICLR 2024)
- URL: arXiv:2308.08493
- Type: method paper
- Verification: abstract
- Supports: "guided instruction" prompts the model with the dataset name, the partition, and a random-length prefix of an instance. An instance is flagged if the completion exactly or nearly matches the rest. A partition is flagged if (a) overlap (ROUGE-L/BLEURT) under guided prompts is significantly higher than under general prompts, or (b) a GPT-4 few-shot classifier flags multiple exact or near-exact matches. Reported accuracy against human judgment is 92-100%. The paper reports GPT-4 contamination for AG News, WNLI and XSum.
- Caveats: this only detects verbatim or near-verbatim memorization, and it relies on GPT-4 as a judge.

### oren2024proving
- Title: Proving Test Set Contamination in Black Box Language Models
- Authors: Yonatan Oren, Nicole Meister, Niladri Chatterji, Faisal Ladhak, Tatsunori B. Hashimoto
- Date: arXiv 2023-10-26, v2 2023-11-24 (ICLR 2024)
- URL: arXiv:2310.17623
- Type: method paper
- Verification: full-text (§2 Proposition 1; §3.1 permutation test; §3.2 sharded test; Limitations)
- Supports:
  - Under H0 (the model is independent of the dataset) with an exchangeable dataset, log p_θ(seq(X)) has the same distribution as log p_θ(seq(X_π)) for a uniformly random permutation π (Prop. 1).
  - Permutation test: p̂ = (Σ_{i=1}^m 1{log p_θ(seq(X)) < log p_θ(seq(X_{π_i}))} + 1)/(m+1). It has an O(m|X|) cost and a p-value floor of 1/(m+1). The sharded rank-comparison test fixes this.
  - The false-positive guarantee holds under exchangeability.
  - Limitations: no multiple-testing correction; exchangeability of off-the-shelf datasets cannot be proven, so the authors urge dataset creators to shuffle and say so; the test targets verbatim contamination only and "cannot rule out ... partial contamination".
  - An audit of five models found "little evidence for pervasive contamination" (abstract).
- Caveats: power depends on memorization of example order.

### zhang2024gsm1k
- Title: A Careful Examination of Large Language Model Performance on Grade School Arithmetic
- Authors: Hugh Zhang, Jeff Da, et al. (Scale AI)
- Date: arXiv 2024-05-01, v4 2024-11-22 (NeurIPS 2024 Datasets & Benchmarks)
- URL: arXiv:2405.00332
- Type: benchmark/dataset paper / empirical study
- Verification: abstract plus full-text spot check (§1, §3 release policy)
- Supports: GSM1k is 1,205 newly written problems matched to GSM8k on human solve rate, number of steps and answer magnitude. Some model families drop up to 8% relative to GSM8k. Spearman r² = 0.36 between a model's probability of generating GSM8k examples and its GSM8k−GSM1k gap. Frontier models show minimal overfitting. Policy: GSM1k is withheld from public release, with a precommitted later release (conditional, or by June 2025), and the authors recommend this pattern.
- Caveats: this is a vendor-produced held-out set. Whether the conditional release happened was not checked.

### xu2024survey
- Title: Benchmark Data Contamination of Large Language Models: A Survey
- Authors: Cheng Xu, Shuhao Guan, Derek Greene, M-Tahar Kechadi
- Date: arXiv 2024-06-06
- URL: arXiv:2406.04244
- Type: position/survey
- Verification: abstract
- Supports: reviews benchmark data contamination (BDC) and alternative assessment methods.
- Caveats: its specific taxonomy was not read.

### dekoninck2024evading
- Title: Evading Data Contamination Detection for Language Models is (too) Easy
- Authors: Jasper Dekoninck, Mark Niklas Müller, Maximilian Baader, Marc Fischer, Martin Vechev
- Date: arXiv 2024-02-05, v2 2024-02-12
- URL: arXiv:2402.02823
- Type: empirical study / method (attack)
- Verification: full-text (abstract, §5 EAL)
- Supports: detection methods assume benign providers. EAL (Evasive Augmentation Learning) rephrases benchmark samples with GPT-4, iterating until they are "unrecognizably rephrased", and fine-tunes on them mixed with background data. This "significantly inflates benchmark performance while completely evading current detection methods" (abstract). n-gram and likelihood-based detectors such as Shi et al. 2023 Min-K are within scope.
- Caveats: none noted.

### white2025livebench
- Title: LiveBench: A Challenging, Contamination-Limited LLM Benchmark (plus the official GitHub README)
- Authors: Colin White, Samuel Dooley, et al. (Abacus.AI, NYU, NVIDIA, et al.)
- Date: arXiv 2024-06-27, v2 2025-04-18 (ICLR 2025 spotlight per README)
- URL: arXiv:2406.19314. https://github.com/LiveBench/LiveBench
- Type: benchmark/dataset paper + official docs (benchmark-author claims)
- Verification: abstract + README. livebench.ai is JS-rendered and WebFetch got no content.
- Supports: questions come from recent math competitions, arXiv papers, news and datasets, with objective ground-truth scoring. They are updated monthly. The README says the current release is 2025-04-25 but "not all questions for this release are public on Huggingface", and the latest public set is 2024-11-25. Releases are selectable with `--livebench-release-option`.
- Caveats: "contamination-limited" (paper title v2) versus "Contamination-Free" (README bibtex) is an author claim. Partial non-public release is a deliberate mitigation.

### jain2024livecodebench
- Title: LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code (plus official README/site)
- Authors: Naman Jain, King Han, Alex Gu, et al. (UC Berkeley, MIT, Cornell)
- Date: arXiv 2024-03-12, v2 2024-06-06
- URL: arXiv:2403.07974. https://livecodebench.github.io. https://github.com/LiveCodeBench/LiveCodeBench
- Type: benchmark/dataset paper + official docs
- Verification: abstract + README + site (WebFetch summary)
- Supports: problems from LeetCode, AtCoder and CodeForces are annotated with release dates, so a model with cutoff D can be evaluated on problems released after D. The `--start_date`/`--end_date` window flags support this. Versions run from release_v1 (400 problems, May 2023-Mar 2024) to release_v6 (1,055 problems, May 2023-Apr 2025). The paper restricts DeepSeek results to problems after Aug/Sep 2023 because of a contamination signal.
- Caveats: a time split only guards against contamination if the model's training cutoff is truthful. Time windows also change difficulty and distribution.

### gebru2021datasheets
- Title: Datasheets for Datasets
- Authors: Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III, Kate Crawford
- Date: arXiv 2018-03-23, v8 2021-12-01 (CACM 2021)
- URL: arXiv:1803.09010
- Type: method paper (documentation practice)
- Verification: abstract
- Supports: every dataset should have a datasheet documenting "its motivation, composition, collection process, recommended uses, and so on".
- Caveats: none noted.

### longpre2024provenance
- Title: A large-scale audit of dataset licensing and attribution in AI (arXiv title: The Data Provenance Initiative: ...)
- Authors: Shayne Longpre, Robert Mahari, et al.
- Date: arXiv 2023-10-25, v3 2023-11-04. Nature Machine Intelligence 6(8):975-987, 2024-08-30
- URL / DOI: 10.1038/s42256-024-00878-8. arXiv:2310.16787
- Type: empirical study
- Verification: abstract (NMI abstract via Crossref, and arXiv abstract)
- Supports: an audit of more than 1,800 text datasets. Hosting sites show "licence omission rates of more than 70% and error rates of more than 50%". The Data Provenance Explorer is released.
- Caveats: the audit covers fine-tuning collections, not evaluation sets specifically.

## Topic notes

### 1. Validity of evaluation (construct, content, ecological, internal/external)
- Measurement framing: a benchmark score is an operationalization of an unobservable construct (jacobs2021measurement). Wallach et al. structure it as background concept → systematized concept → instrument → measurements, linked by systematization, operationalization, application and interrogation (wallach2025position). Validity is interrogated through lenses (face, content, convergent, discriminant, predictive, hypothesis, consequential) that descend from Messick's unified view (messick1995validity; the abstract only was verified). In this tradition validity is a property of an interpretation in a context, not of a dataset. It has to be re-examined when the dataset is reused for a new purpose (wallach2025position).
- Internal versus external validity in ML (liao2021learning). Internal: implementation variation, label errors and leakage, test size, contamination, test reuse, weak baselines. External: transfer to related problems, metric misalignment, human comparisons.
- Ecological validity (devries2020ecological): data collected for quantity loses naturalness and relevance to real use. Crowd-paraphrased intents, such as those in CLINC150, are an instance of this kind of collection.
- Practical checklist (bean2025measuring §5). Define the phenomenon, including sub-components and negative definitions. Control confounds such as output format and parsers. Sample items representatively rather than by convenience. Document reuse. Check contamination. Report sample size, power and uncertainty: only 16% of reviewed benchmarks used any statistical test. Do error analysis against confounders. Justify validity.
- Power (bowman2021fix §3.3): about a few thousand examples are needed to detect a 1-point difference near 80% accuracy. Detecting 98%→98.1% takes about 100× more. Small authored sets (n of 3-24 per cell) therefore support only very large effects or qualitative failure detection. This connects to the statistics cluster (Wilson CIs, McNemar).

### 2. Annotation artifacts and shortcuts
- Annotators leave label-predictive cues: hypothesis-only models reach about 67% on SNLI and 53% on MNLI (gururangan2018annotation). Models learn heuristics that work on frequent cases and fail on targeted ones (mccoy2019hans). The general phenomenon is "shortcut learning" (geirhos2020shortcut).
- Standard diagnostics are partial-input baselines (hypothesis-only, question-only, evidence-only) and controlled challenge sets built to break specific heuristics. For typed-question evaluation, the analogue is a state-only baseline or an option-text-only baseline that checks whether answers are recoverable without the intended evidence.

### 3. Contrast sets, counterfactuals, behavioral tests and negatives
- Contrast sets (gardner2020contrast) are minimal perturbations near a pivot, usually label-changing. Contrast consistency means every member of the set, including the original, is correct. Consistency is stricter than accuracy and exposes local decision-boundary errors.
- Counterfactually-augmented data (kaushik2020cad) uses the same human-minimal-edit idea for training and evaluation.
- CheckList (ribeiro2020checklist) gives three test types. MFT is the targeted unit test. INV is label-preserving and the prediction must not change. DIR expects a directional change. Results are reported as failure rates per capability and test type. For probabilistic outputs, INV and DIR can be checked on probabilities as well as on labels. That extension is ours, not CheckList's; CheckList itself mentions expectations on confidence for DIR, but that wording was not verified in detail.
- Negatives and abstention data:
  - SQuAD 2.0 has adversarially written unanswerables with plausible-answer distractors, a 1:1 answerable/unanswerable ratio in dev, and a hidden test set (rajpurkar2018squad2).
  - CLINC150 has an explicit OOS class: 1,000 OOS test queries against 4,500 in-scope test queries in the Full variant. Its baselines are oos-train, oos-threshold and oos-binary. It reports OOS recall alongside in-scope accuracy, and the threshold is chosen on validation (larson2019clinc).
  - Banking77 has no OOS class and no validation split. It is useful for fine-grained near-miss confusion (casanueva2020banking77).
  - VitaminC provides contrastive evidence pairs where nearly identical evidence supports or does not support the same claim. It is a natural source of "missing/conflicting evidence" style negatives (schuster2021vitaminc).
- Licenses:

  | Dataset | License |
  |---|---|
  | CLINC150 | CC BY 3.0 |
  | Banking77 | CC BY 4.0 |
  | SQuAD 2.0 | CC BY-SA 4.0 |
  | VitaminC data | CC BY-SA 3.0 (code MIT) |

  ShareAlike terms matter if derived evaluation slices are redistributed.
- Pitfall: thresholds or gates for abstention must be tuned on validation data, not on test data (larson2019clinc §3.2). Constructed negatives (adversarial, crowdsourced) differ from natural traffic negatives, which limits ecological validity.

### 4. Distribution shift and saturation
- Dataset shift is a change in the joint distribution between train and test. Covariate shift is the special case where only p(x) changes (quinonero2009shift).
- WILDS (koh2021wilds) shows large in-distribution to out-of-distribution gaps on natural shifts.
- Recht et al. built a carefully reproduced new test set and still saw 3-15% (CIFAR-10) and 11-14% (ImageNet) drops, attributed to harder examples rather than adaptivity. Rankings were largely preserved: gains transfer, with slope > 1 (recht2019imagenet).
- Søgaard et al. find that random and even biased splits underestimate error on new in-domain samples. They recommend multiple independent test sets (sogaard2021random). Gorman & Bedrick recommend random splits over a single standard split, with paired testing (gorman2019standard). These are not contradictory: both reject reliance on a single fixed split, but they disagree on whether random resplitting is enough.
- Saturation: benchmarks quickly approach ceiling (ott2022mapping). Dynabench answers with adversarial human-in-the-loop collection (kiela2021dynabench). Bowman & Dahl argue that adversarial collection does not fix validity and that the remedies are better design, annotation reliability, size, and bias handling (bowman2021fix). This disagreement is open.

### 5. Splits, leakage and holdout reuse
- Leakage taxonomy (kapoor2023leakage): L1 is train/test separation (no test set, preprocessing or feature selection on all data, duplicates). L2 is illegitimate features. L3 is a test distribution that is not the target (temporal leakage, non-independence, sampling bias). Grouped splits, where all items derived from the same source document, template or state are kept on one side, address L1.4 and L3.2.
- Train-test overlap in QA (lewis2021overlap): about 30% of test questions are paraphrases of training questions, and performance on non-overlapping items is much lower. Report overlap-stratified results.
- Adaptive reuse. Theory says reusing a holdout adaptively can overfit it, and differential-privacy-style mechanisms such as Thresholdout allow safe reuse (dwork2015reusable). Empirically, Kaggle shows little substantial overfitting from leaderboard reuse (roelofs2019metaanalysis), consistent with Recht et al.'s finding that drops were not due to adaptivity. The practical consequence is to freeze configurations on dev, touch test once, and log how many test evaluations were run.

### 6. Contamination
- Definitions. Sainz et al. distinguish guideline, raw-text and annotation contamination. Test-split exposure invalidates the experiment. Train/dev exposure invalidates zero/few-shot claims only (sainz2023trouble). Magar & Schwartz separate memorization (mem) from exploitation (expl) and find that one does not imply the other (magar2022contamination).
- Detection families and their limits:
  - n-gram overlap with the training corpus. This needs corpus access; GPT-3 used N between 8 and 13 and compared clean versus all. It has false positives when a benchmark reuses web passages (DROP was 94% "dirty") and misses paraphrases (brown2020gpt3).
  - Corpus documentation and audits (dodge2021c4).
  - Black-box completion probes using guided versus general instruction (golchin2024timetravel).
  - Exchangeability or ordering tests. These give a provable false-positive bound but detect verbatim, order-memorized contamination only (oren2024proving).
  - Fresh parallel test sets: GSM1k against GSM8k (zhang2024gsm1k).
  - Time-split live benchmarks, filtered by release date versus model cutoff (white2025livebench, jain2024livecodebench).
  - All of these can be evaded by deliberate rephrased contamination, EAL (dekoninck2024evading). Detection is therefore evidence, not proof of cleanliness.
- Evidence about magnitude is mixed. GPT-3 found mostly negligible clean-versus-all differences. Oren et al. found little pervasive verbatim contamination. GSM1k found drops of up to 8% for some families and none for frontier models. Lewis et al. found large overlap effects in open-domain QA. The effect depends on the benchmark and the model.
- For freshly authored private sets, contamination risk is low before publication. After publishing, a held-back slice or a precommitted release (the GSM1k pattern), plus canary or time-stamping, preserves future validity. Canaries are not covered by the sources verified here.

### 7. Documentation and licensing
- Datasheets document motivation, composition, collection, uses and so on (gebru2021datasheets).
- Licence metadata on hosting sites is often missing (more than 70%) or wrong (more than 50%) (longpre2024provenance). Verify licenses at the original source. Example: for CLINC, the HF card and LICENSE say CC BY 3.0 while the GitHub API reports NOASSERTION. For VitaminC, the code is MIT but the data is CC BY-SA 3.0.

### Contradictions and caveats summary
- Adversarial data collection is disputed: Dynabench argues for it, Bowman & Dahl argue it does not fix validity.
- Splits are disputed: Gorman & Bedrick recommend random splits, while Søgaard et al. find random splits still optimistic and recommend independent test sets.
- Holdout reuse: theory (Dwork) predicts a risk that is small in observed practice (Roelofs; Recht). Kaggle-type limits may explain the gap.
- GPT-3 contamination procedure: §4 says 13-gram, Appendix C uses variable N in [8, 13].
- Contamination detectors give false positives (DROP, passage overlap) and false negatives (paraphrase, EAL).
- Messick's "six aspects" is a secondary characterization in this file. Jacobs & Wallach's seven lenses were read in full text.
