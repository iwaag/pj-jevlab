# Sources: Cluster C — generated/structured outputs, annotation agreement, human/model judging, annotation practice

Accessed date for all sources: 2026-10-02. "Raw text" means the PDF was downloaded with curl and converted with `pdftotext`, then the passages were read directly (not through a WebFetch summary). Section, table and equation numbers refer to the version noted.

> Evidence notes for cluster C of [study/benchmark](../README.md), compiled 2026-10-02 in step2 of benchmark/p1 by a research subagent and reviewed by the lead session. The search log and gaps for this cluster are in [search-log.md](../search-log.md). Verification levels are per entry; claims beyond the stated level must not be attributed to a source.

## Source list

### cohen1960kappa
- Title: A Coefficient of Agreement for Nominal Scales
- Authors / organization: Jacob Cohen
- Date: 1960 (Educational and Psychological Measurement 20(1):37–46)
- URL / DOI: doi:10.1177/001316446002000104
- Type: method paper
- Verification: abstract-level only. The Crossref metadata (title, venue, volume and pages) was fetched; the paper itself is paywalled and was not read. The formula below is taken from artstein2008agreement §2.4.3, which presents Cohen's definition.
- Accessed: 2026-10-02
- Supports: kappa = (A_o − A_e)/(1 − A_e), where A_e = Σ_k P̂(k|c1)·P̂(k|c2). Each coder's marginal distribution is estimated separately (per artstein2008agreement §2.4).
- Caveats: All details beyond the bibliographic metadata come from artstein2008agreement.

### fleiss1971
- Title: Measuring nominal scale agreement among many raters
- Authors: Joseph L. Fleiss
- Date: 1971 (Psychological Bulletin 76(5):378–382)
- DOI: 10.1037/h0031619
- Type: method paper
- Verification: abstract-level only (Crossref metadata). The formulas come from artstein2008agreement §2.5.1.
- Supports: Fleiss's multi-rater coefficient uses pairwise agreement within each item, agr_i = (1/(c(c−1))) Σ_k n_ik(n_ik − 1), and A_o = mean_i agr_i. Expected agreement uses one pooled distribution: P̂(k) = n_k/(i·c) and A_e = Σ_k P̂(k)².
- Caveats: Fleiss called the coefficient "kappa", but it generalizes Scott's pi, not Cohen's kappa. The CL community's "K" (Siegel & Castellan) is in fact Fleiss's coefficient (artstein2008agreement fn. 5).

### artstein2008agreement
- Title: Inter-Coder Agreement for Computational Linguistics (survey article)
- Authors: Ron Artstein, Massimo Poesio
- Date: 2008 (Computational Linguistics 34(4):555–596)
- URL / DOI: https://aclanthology.org/J08-4004 ; doi:10.1162/coli.07-034-R2
- Type: position/survey (tutorial-level treatment of the mathematics)
- Verification: full text (raw text of the ACL Anthology PDF). Read §2.4–2.7, §3.2, §4.1 and §5.1–5.3.
- Supports:
  - §2.4: S, π and κ all take the form (A_o − A_e)/(1 − A_e) and differ only in the chance model. S assumes uniform categories (A_e = 1/k). π assumes one shared distribution (P̂(k) = n_k/2i). κ assumes a separate distribution for each coder. All three assume the coders are independent. Table 2 works an example with A_o = 0.7: S = 0.4, π ≈ 0.341, κ ≈ 0.348.
  - §2.4.1: S can be inflated by adding categories that are never used.
  - §2.5.1: Fleiss's multi-π formulas (see fleiss1971 above).
  - §2.6.1: Krippendorff's α = 1 − D_o/D_e. It derives from the variance ratio α = 1 − s²_within/s²_total. It works with multiple coders, missing values and any distance d with d_kk = 0. For nominal data, α ≈ π, and the two converge as the number of items or coders grows. α corrects for small samples by using an unbiased estimator of expected agreement.
  - §2.6.1/§4.4: different distance metrics give different α values for the same data, which makes the values hard to interpret.
  - §2.6.2: Cohen's (1968) weighted κ_w is the two-coder counterpart.
  - §3.2 (prevalence "paradox", citing Feinstein & Cicchetti 1990): with skewed data, A_e is high, so κ/π can be low even when A_o is high. With 2 coders, a Common and a Rare category, and identical marginals, π = κ = δ/(δ+ε) − ε/(1−(δ+ε)) ≈ δ/(δ+ε). In words, reliability is driven by agreement on the rare category. Numerical example: if 95% of items fall in one category, random coding produces 90.25% joint assignment and accuracy of at least 85.7%, yet the coefficient stays low.
  - §3.1/§5.2: the "bias problem" (κ vs π) matters less as the number of annotators grows. The authors recommend α when categories are not equally distinct, such as hierarchical tagsets or set-valued labels.
  - §4.1/§5.3: on thresholds, Krippendorff treats 0.8 as the minimum and 0.67 as only "highly tentative". The Landis & Koch (1977) scale is reproduced but criticized. The authors' own experience is that only values above 0.8 gave reasonable quality, but they doubt one cutoff fits every purpose. They recommend reporting the methodology (number of coders, whether coding was independent, whether coders relied only on the manual), significance, and a confusion matrix or agreement table.
  - §5.1: the authors favour chance-corrected coefficients over percent agreement. They recommend an independent evaluation of the downstream task in addition to agreement.
- Caveats: once weights are used, standard rule-of-thumb thresholds no longer apply (§4.4).

### krippendorff2011computing
- Title: Computing Krippendorff's Alpha-Reliability
- Authors: Klaus Krippendorff (Annenberg School for Communication, UPenn; ScholarlyCommons asc_papers/43)
- Date: 2011-01-25; literature list updated 2013-09-13
- URL: https://www.asc.upenn.edu/sites/default/files/2021-03/Computing%20Krippendorff's%20Alpha-Reliability.pdf
- Type: textbook/tutorial (author's computational note)
- Verification: full text (raw text, 8 pp.). Greek letters were garbled by pdftotext but are clear from context. Read pp. 1–5.
- Supports:
  - α = 1 − D_o/D_e, with D_o = (1/n) Σ_c Σ_k o_ck · metricδ²_ck and D_e = (1/(n(n−1))) Σ_c n_c Σ_k n_k · metricδ²_ck. Both are computed from a coincidence matrix in which each unit's pairable values are counted in both orders.
  - α works for any number of observers, any number of categories, any metric (nominal, ordinal, interval, ratio, circular and others), missing data, and small or large samples.
  - The range is 1 ≥ α ≥ 0, with values below 0 arising from systematic disagreement or sampling error.
  - Binary 2-coder example (p. 2): α = 1 − (n−1)·o_01/(n_0·n_1). With 10 units, n = 20, o_01 = 4, n_0 = 14 and n_1 = 6, α = 1 − 19·4/84 ≈ 0.095.
  - The ordinal metric depends on the marginal frequencies of the ranks in between. The interval metric is (c−k)².
- Caveats: this note does not state the 0.800/0.667 thresholds; those are quoted via artstein2008agreement. Coincidence matrices differ from contingency tables.

### feinstein1990paradox
- Title: High agreement but low kappa: I. The problems of two paradoxes
- Authors: Alvan R. Feinstein, Domenic V. Cicchetti
- Date: 1990 (J Clin Epidemiol 43(6):543–549)
- DOI: 10.1016/0895-4356(90)90158-L ; PMID 2348207
- Type: method paper (critique)
- Verification: abstract (PubMed efetch)
- Supports (abstract): In a 2×2 table, a high p_o can be "drastically lowered" by a large imbalance in the marginal totals (paradox 1). Kappa is higher when the imbalance is asymmetric rather than symmetric (paradox 2). Substituting kappa_max does not fix either paradox and seems to make the second one worse.
- Caveats: artstein2008agreement §3.2 argues the prevalence effect is justified, because reliability requires agreement on rare categories.

### aroyo2015truth
- Title: Truth Is a Lie: Crowd Truth and the Seven Myths of Human Annotation
- Authors: Lora Aroyo, Chris Welty
- Date: 2015 (AI Magazine 36(1):15–24)
- DOI: 10.1609/aimag.v36i1.2564
- Type: position/survey
- Verification: full text (raw text of the AAAI OJS PDF). The two-column layout made close reading harder, but the myth list and abstract are clear.
- Supports: The paper names seven myths: (1) One Truth, (2) Disagreement Is Bad, (3) Detailed Guidelines Help, (4) One Is Enough, (5) Experts Are Better, (6) All Examples Are Created Equal, (7) Once Done, Forever Valid. It argues that disagreement is signal and proposes "crowd truth" metrics, including sentence/item-level ambiguity and worker–worker disagreement. Its examples come from medical relation extraction with crowds of 10, 20 or 30 workers per sentence. On myth 3, the authors argue that overly specific guidelines suppress disagreement without improving quality.
- Caveats: The empirical evidence comes from the authors' own projects, so the paper is a position piece.

### pavlick2019inherent
- Title: Inherent Disagreements in Human Textual Inferences
- Authors: Ellie Pavlick, Tom Kwiatkowski
- Date: 2019 (TACL 7:677–694)
- URL: https://aclanthology.org/Q19-1043
- Type: empirical study
- Verification: full text (raw text). Read the abstract, §1, the data collection section (50 raters per pair on a −50..50 slider), the GMM analysis and §5.3 / Table 4.
- Supports: Disagreements on NLI often persist as more ratings are collected and as context varies, so they are not simple noise. A Gaussian mixture model fits held-out ratings better than a single Gaussian. About 20% of sentence pairs have a nontrivial second component (weight > 0.2). Model softmax outputs approximate the human distribution poorly (Table 4: cross-entropy expected 0.03 vs observed 0.37). The authors argue that NLI evaluation should reward predicting the distribution of human judgments.
- Caveats: The task is NLI only, and the rating scale is graded rather than categorical.

### nie2020chaosnli
- Title: What Can We Learn from Collective Human Opinions on Natural Language Inference Data?
- Authors: Yixin Nie, Xiang Zhou, Mohit Bansal
- Date: 2020 (EMNLP 2020; arXiv 2010.03532v2)
- URL: https://arxiv.org/abs/2010.03532
- Type: benchmark/dataset paper + empirical study
- Verification: full text (raw text). Read the abstract, §4 Table 2 and the JSD/KL section.
- Supports:
  - ChaosNLI collects 100 annotations per example (464,500 in total) for 3,113 SNLI/MNLI examples and 1,532 αNLI examples.
  - Table 2: the new majority label differs from the old one for 10.64% (α), 24.97% (S) and 31.77% (M) of the selected subsets. On the full SNLI/MNLI-m dev sets the corresponding rates are 3.78% and 5.08%.
  - Models are near-perfect on high-agreement items but "barely beat a random guess" on low-agreement items.
  - Evaluation uses Jensen–Shannon distance (a bounded, symmetric metric) and KL between the model softmax and the human label distribution.
- Caveats: The SNLI/MNLI subsets were deliberately chosen as low-agreement items (the original 5-label majority was weak), so the change rates do not hold for the full datasets.

### uma2021disagreement
- Title: Learning from Disagreement: A Survey
- Authors: Alexandra N. Uma, Tommaso Fornaciari, Dirk Hovy, Silviu Paun, Barbara Plank, Massimo Poesio
- Date: 2021 (JAIR 72:1385–1470)
- DOI: 10.1613/jair.1.12752
- Type: position/survey (with a systematic empirical comparison)
- Verification: full text (raw text of the JAIR PDF). Read the abstract, §2.8 section list, §4.1–4.2 and §4.3.2.
- Supports:
  - Sources of disagreement (§2.8): errors and interface problems, the annotation scheme, ambiguity, item difficulty, and subjectivity.
  - Hard evaluation (§4.1): accuracy and F1 against gold labels. Crowd-truth weighted F1 (Eq. 7–8) down-weights high-disagreement items through irs(i) = cos(V_i, r̂).
  - Soft evaluation (§4.2): cross-entropy against the human distribution (Eq. 9; the minus sign is dropped in the printed equation) and JSD(p_hum‖p_θ) = ½KL(p_hum‖M) + ½KL(p_θ‖M) with M = (p_hum + p_θ)/2 (Eq. 10–12). Normalized-entropy similarity and correlation are also used.
  - §4.3.2: KL and JSD have a lower bound of 0. Cross-entropy is bounded below by H(P) rather than 0. JSD is bounded above (ln 2, or 1 in base 2), which makes it comparable across datasets.
  - Abstract: which training method looks best depends heavily on the evaluation form chosen. With large datasets annotated by many high-quality coders, training on soft labels beats gold labels.
- Caveats: Many papers that propose "learning from disagreement" still evaluate against hard gold labels (§4.1).

### plank2022hlv
- Title: The "Problem" of Human Label Variation: On Ground Truth in Data, Modeling and Evaluation
- Authors: Barbara Plank
- Date: 2022 (EMNLP 2022; arXiv 2211.02570v1)
- URL: https://arxiv.org/abs/2211.02570
- Type: position/survey
- Verification: full text (raw text). Read the abstract and §4 (Evaluation).
- Supports: The paper introduces the term "human label variation" (HLV), covering disagreement, subjectivity and multiple plausible answers. HLV affects data, modeling and evaluation. Accuracy against a single gold label is "severely flawed" for many tasks. The listed soft metrics are cross-entropy, entropy correlation, and KL/JSD. Other approaches evaluate against individual annotators or split data by agreement level, annotator cluster, item difficulty or uncertainty flags. Which evaluation suits which task is left open.
- Caveats: This is a position paper and gives no new experiments.

### northcutt2021labelerrors
- Title: Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks
- Authors: Curtis G. Northcutt, Anish Athalye, Jonas Mueller
- Date: 2021 (NeurIPS Datasets & Benchmarks; arXiv 2103.14749)
- URL: https://arxiv.org/abs/2103.14749
- Type: empirical study
- Verification: full text (raw text). Read the abstract and the introduction.
- Supports: Across 10 test sets (vision, text and audio), label errors average at least 3.3%. At least 6% of the ImageNet validation set is mislabeled (2,916 errors). Candidates come from confident learning and are then validated by crowd workers; on average 51% of flagged candidates are real errors. On corrected labels, model rankings can flip: ResNet-18 beats ResNet-50 on ImageNet if the share of originally mislabeled test examples rises by 6%, and VGG-11 beats VGG-19 on CIFAR-10 at 5%.
- Caveats: The error rates are lower bounds, since only algorithmically flagged items were reviewed.

### zheng2023mtbench
- Title: Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
- Authors: Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, et al.
- Date: 2023 (NeurIPS 2023 Datasets & Benchmarks; arXiv 2306.05685)
- URL: https://arxiv.org/abs/2306.05685
- Type: empirical study + benchmark paper
- Verification: full text (raw text). Read §3.1–3.4, §4.2, Tables 2–5.
- Supports:
  - Judge formats (§3.1): pairwise comparison, single-answer grading and reference-guided grading. Pairwise comparison does not scale (pairs grow quadratically). Single-answer grading may miss subtle differences.
  - Position bias (Table 2, swapping two similar answers): consistency was 65.0% for GPT-4 (default prompt), 46.2% for GPT-3.5 and 23.8% for Claude-v1. Claude-v1 favoured the first position 75.0% of the time.
  - Verbosity bias (Table 3, "repetitive list" attack on 23 answers): failure rates were 91.3% for Claude-v1 and GPT-3.5 and 8.7% for GPT-4.
  - Self-enhancement: GPT-4 shows about a 10% higher win rate for itself and Claude-v1 about 25%, but the authors say the study "cannot determine" whether self-enhancement bias exists.
  - Mitigations (§3.4): judge twice with positions swapped and count a win only if the answer wins in both orders (otherwise call a tie). Few-shot examples raised GPT-4 consistency from 65.0% to 77.5%. Chain-of-thought and reference-guided judging are also proposed for math.
  - Agreement (§4.2, Table 5, MT-bench): defined as the probability that randomly selected individuals of each judge type agree. Setup S2 (non-tie votes only, random = 50%): GPT-4 pairwise vs humans 85%, human vs human 81%. Setup S1 (ties and inconsistent votes counted as ties, random = 33%): GPT-4 pairwise vs humans 66%, human vs human 63%.
- Caveats: The headline "over 80% agreement" depends on dropping ties (S2). The judges evaluated are 2023 models.

### wang2023notfair
- Title: Large Language Models are not Fair Evaluators
- Authors: Peiyi Wang, Lei Li, Liang Chen, et al.
- Date: 2023 (arXiv 2305.17926v2, 30 Aug 2023; ACL 2024)
- URL: https://arxiv.org/abs/2305.17926
- Type: empirical study + method paper
- Verification: full text (raw text). Read the abstract and §2–3.
- Supports: Reordering the two responses can flip the ranking. With ChatGPT as judge, Vicuna-13B beat ChatGPT on 66 of 80 queries (82.5%). Conflict Rate = (1/N) Σ I(ER_i^{r12} ≠ ER_i^{r21}) (Eq. 1). For GPT-4, the win rate for Vicuna-13B was 51.3% in position 1 and 23.8% in position 2. Conflict rates are lower when the two responses differ more in quality. Proposed fixes: Multiple Evidence Calibration (rationale before score), Balanced Position Calibration (average over both orders), and Human-in-the-Loop calibration using balanced position diversity entropy to route hard items to humans.
- Caveats: Small question set (80 Vicuna questions).

### chiang2023alternative
- Title: Can Large Language Models Be an Alternative to Human Evaluation?
- Authors: Cheng-Han Chiang, Hung-yi Lee
- Date: 2023 (ACL 2023; arXiv 2305.01937v1)
- URL: https://arxiv.org/abs/2305.01937
- Type: empirical study
- Verification: full text (raw text). Read the abstract and the Kendall τ section (Table 2).
- Supports: LLMs were given the same instructions as human raters. For story generation, text-davinci-003 ratings correlate positively ("weak to strong") with English teachers' ratings, measured by Kendall τ over 200 stories. The authors use correlation rather than inter-annotator agreement because IAA asks for exact rating matches whereas correlation asks about relative ordering. Human IAA is reported with Krippendorff's α. Results were stable across instruction wording and sampling.
- Caveats: Only two tasks were studied, with 2023 models.

### liu2023geval
- Title: G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment
- Authors: Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang, Ruochen Xu, Chenguang Zhu
- Date: 2023 (EMNLP 2023; arXiv 2303.16634)
- URL: https://arxiv.org/abs/2303.16634
- Type: method paper
- Verification: full text (raw text). Read the abstract and §2 (scoring function and setup).
- Supports: The method combines auto-generated chain-of-thought evaluation steps with form filling. The score is probability-weighted: score = Σ_i p(s_i)·s_i over the predefined scores s_i. With GPT-4, which did not expose token probabilities, p(s_i) was estimated from 20 samples (n=20, T=1). It reached a summary-level Spearman correlation of 0.514 with human judgments on SummEval. The authors flag a possible bias of LLM evaluators toward LLM-generated text.
- Caveats: Expected-score aggregation needs access to logprobs or repeated sampling.

### panickssery2024selfpref
- Title: LLM Evaluators Recognize and Favor Their Own Generations
- Authors: Arjun Panickssery, Samuel R. Bowman, Shi Feng
- Date: 2024 (arXiv 2404.13076v1; NeurIPS 2024)
- URL: https://arxiv.org/abs/2404.13076
- Type: empirical study
- Verification: abstract plus the Fig. 1 caption (raw text). The experimental sections were not read in detail.
- Supports (abstract/Fig. 1): Self-preference means an LLM scores its own outputs higher even when humans rate them as equal. Out of the box, GPT-4 and Llama 2 can tell their own outputs apart from those of other LLMs and humans with non-trivial accuracy. After fine-tuning, self-recognition strength correlates linearly with self-preference strength (CNN/DailyMail, XSUM).
- Caveats: The tasks are summarization only.

### thakur2024judges
- Title: Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges
- Authors: Aman Singh Thakur, Kartik Choudhary, Venkat Srinik Ramayapally, Sankaran Vaidyanathan, Dieuwke Hupkes
- Date: 2024 (arXiv 2406.12624; v6 dated 18 Aug 2025, which is the version read)
- URL: https://arxiv.org/abs/2406.12624
- Type: empirical study
- Verification: full text (raw text, v6). Read the abstract, §1 findings list and the alignment-metric section with fn. 2.
- Supports: 13 judge models graded answers from 9 exam-taker models on TriviaQA, a deliberately clean setup with high human alignment. Only the best and largest judges (GPT-4 Turbo, Llama-3/3.1 70B) aligned well, and they still differed from human-assigned scores by up to 5 points. A judge with high percent agreement can still be 10–20 points off. Scott's π separates judges better than percent agreement. Judges showed leniency, sensitivity to prompt length and quality, and failures on under-specified answers. The cheap lexical "contains" metric and small judges ranked exam-takers reasonably well.
- Caveats: Earlier versions used Cohen's κ. v6 switched to Scott's π, citing documented theoretical problems with κ (fn. 2), so numbers differ across versions. Always cite a version.

### bavaresco2024judgebench
- Title: LLMs instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks (JUDGE-BENCH)
- Authors: Anna Bavaresco, Raffaella Bernardi, Leonardo Bertolazzi, et al.
- Date: 2024 (arXiv 2406.18403; v3 dated 2 Jun 2025, which is the version read; ACL 2025)
- URL: https://arxiv.org/abs/2406.18403
- Type: benchmark/dataset paper + empirical study
- Verification: full text (raw text, v3). Read the abstract, the evaluation protocol and the valid-response appendix.
- Supports: 20 datasets with human annotations and 11 LLMs. Metrics are Cohen's κ for categorical judgments and Spearman ρ for graded judgments. Performance varies widely by property, by the expertise of the human judges, and by whether the text was written by humans or models. The paper concludes that LLMs must be validated against human judgments before being used as evaluators. Protocol detail relevant to parse failures: invalid LLM responses are replaced with judgments sampled at random from the label set so every model has the same n. Table 1 shows only models with ≥98% valid response rate, and the valid-response rates are reported in an appendix.
- Caveats: Random imputation of invalid outputs pulls scores toward chance. This is a deliberate choice that should be reported.

### chiang2024arena
- Title: Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference
- Authors: Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios N. Angelopoulos, et al.
- Date: 2024 (ICML 2024; arXiv 2403.04132)
- URL: https://arxiv.org/abs/2403.04132
- Type: benchmark/dataset paper + method paper
- Verification: full text (raw text). Read §4 (Eq. 1–3), §5 (CIs) and §7.1 (Table 3 discussion).
- Supports:
  - Bradley–Terry model: P(H_t = 1) = 1/(1 + e^{ξ_{m′} − ξ_m}). The coefficients ξ minimize binary cross-entropy, with ξ_1 = 0 fixed for identifiability.
  - Rank_m = 1 + Σ_{m′} 1{s_{m′} > s_m}.
  - Sandwich (robust) covariance keeps the MLE asymptotically normal even when the BT model is misspecified. Pivot bootstrap and sandwich intervals were compared, and sandwich intervals were deployed.
  - Earlier leaderboard versions used Elo. The switch to BT was made because BT coefficients are better suited to statistical estimation.
  - About 240K votes from about 90K users. Agreement between crowd users and experts was 72–83%, and between two experts 79.4% and 89.8%. The authors attribute expert disagreement to prompts with no ground truth.
- Caveats: Preferences come from self-selected users. Absolute quality is not measured.

### rajpurkar2016squad
- Title: SQuAD: 100,000+ Questions for Machine Comprehension of Text
- Authors: Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, Percy Liang
- Date: 2016 (EMNLP 2016; arXiv 1606.05250)
- Type: benchmark/dataset paper
- Verification: full text (raw text). Read §6.1 and §6.2.
- Supports: Both metrics ignore punctuation and articles (a, an, the). EM is the percentage of predictions that exactly match any ground-truth answer. F1 treats prediction and truth as bags of tokens, takes the maximum over all ground-truth answers, and averages over questions. Human performance on test, treating the second answer as the human prediction against at least 3 answers, is 77.0% EM and 86.8% F1. The authors say mismatches come mostly from non-essential phrase inclusion rather than real disagreement.

### rajpurkar2018squad2
- Title: Know What You Don't Know: Unanswerable Questions for SQuAD
- Authors: Pranav Rajpurkar, Robin Jia, Percy Liang
- Date: 2018 (ACL 2018; arXiv 1806.03822)
- Type: benchmark/dataset paper
- Verification: full text (raw text). Read §5 (results text and footnote 3).
- Supports: For unanswerable questions, abstaining scores 1 and any other answer scores 0, for both EM and F1. Human F1 is 89.5. An always-abstain baseline gets 48.9 test F1.

### squad_eval_scripts
- Title: Official evaluation scripts for SQuAD v1.1 and v2.0 (copies vendored in Hugging Face `evaluate`: metrics/squad/compute_score.py and metrics/squad_v2/compute_score.py)
- Authors / organization: SQuAD authors, redistributed by Hugging Face
- Date: script headers say "Official evaluation script for v1.1" and "for SQuAD version 2.0". Fetched from the main branch on 2026-10-02.
- URL: https://github.com/huggingface/evaluate/tree/main/metrics/squad_v2
- Type: official docs/code (redistributed copy of the official script)
- Verification: full text (code read)
- Supports:
  - `normalize_answer` = lowercase → remove punctuation → remove articles (\b(a|an|the)\b) → collapse whitespace.
  - `compute_exact` checks equality after normalization.
  - `compute_f1` uses token-multiset overlap (Counter intersection). If either side is empty it returns int(gold == pred).
  - The score is the maximum over gold answers. Gold answers that normalize to empty are dropped, and if none remain the gold is [""] (unanswerable).
  - An optional na_prob threshold converts the prediction to "no answer".
  - A missing prediction is skipped with a printed warning rather than scored 0 in get_raw_scores.
- Caveats: This is a copy and not the CodaLab original. The skip-on-missing behaviour is a reporting hazard: n silently shrinks.

### kamalloo2023odqa
- Title: Evaluating Open-Domain Question Answering in the Era of Large Language Models
- Authors: Ehsan Kamalloo, Nouha Dziri, Charles L. A. Clarke, Davood Rafiei
- Date: 2023 (ACL 2023; arXiv 2305.06984v3)
- URL: https://arxiv.org/abs/2305.06984
- Type: empirical study
- Verification: full text (raw text). Read the abstract, §1 and the setup section.
- Supports: Lexical matching fails when a correct answer is missing from the gold list, and this gets worse with long LLM answers. Human re-evaluation covered 301 randomly sampled NQ-open questions. InstructGPT zero-shot moved from 12.6% (EM) to 71.4% under human judgment, a gain of nearly 60 points. More than 50% of lexical-matching failures were semantically equivalent answers. Regex matching ranks models consistently with humans but is still unnecessarily strict. BEM and InstructGPT-eval are reasonable surrogates in some cases but fail on long-form LLM answers and on hallucinations. The authors conclude there is "no substitute for human evaluation" at the time.

### tam2024speakfreely
- Title: Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models
- Authors: Zhi Rui Tam, Cheng-Kuang Wu, Yi-Lin Tsai, Chieh-Yen Lin, Hung-yi Lee, Yun-Nung Chen
- Date: 2024 (arXiv 2408.02442v3, 14 Oct 2024; EMNLP 2024 Industry)
- URL: https://arxiv.org/abs/2408.02442
- Type: empirical study
- Verification: full text (raw text). Read §3, §4, §5.2–5.3 and the Conclusion.
- Supports:
  - Four conditions: constrained decoding (JSON-mode), format-restricting instructions (FRI), NL-to-Format (answer in natural language, then convert), and free natural language.
  - On reasoning tasks (GSM8K, Last Letter, Shuffled Objects), stricter formats generally hurt. JSON-mode was worst in most cases.
  - On classification tasks (e.g. DDXPlus), JSON-mode was competitive or better, which the authors attribute to the constrained answer space.
  - Answers were extracted by an LLM "Perfect Text Parser" (claude-3-haiku) to separate format errors from content.
  - §5.3: parse errors are not the main cause of the gaps. Llama-3-8B had a 0.148% JSON parse error rate but a 38.15-point gap on Last Letter.
  - A corrective reformatting step (prompting an LLM to fix unparseable outputs) improved JSON/YAML scores.
  - Appendix: on GSM8K, a strict regex scored 43.7% versus 75.5% overall accuracy for GPT-3.5-Turbo (31.8 points); Gemini-1.5-Flash differed by 43.5 points.
  - §5.2: in JSON-mode the model sometimes did not put reasoning before the answer, which lowered reasoning accuracy.
- Caveats: Contested by kurt2024saywhatyoumean and geng2025jsonschemabench (see Topic notes).

### kurt2024saywhatyoumean
- Title: Say What You Mean: A Response to 'Let Me Speak Freely'
- Authors / organization: Will Kurt, .txt (dottxt, the Outlines maintainers)
- Date: 2024 (no exact date visible on the page)
- URL: https://blog.dottxt.ai/say-what-you-mean.html
- Type: vendor/benchmark-author claim (blog by the constrained-decoding vendor)
- Verification: full text. A WebFetch summary misreported the table, so the raw HTML was read with curl.
- Supports (vendor claim): Re-running with Llama-3-8B-instruct, unstructured vs structured scored GSM8K 0.77 vs 0.78, Last Letter 0.73 vs 0.77, and Shuffle Object 0.41 vs 0.44. The post attributes the original drop to different prompts for the structured and unstructured conditions, JSON prompts that did not describe the schema, and the choice of answer parser.
- Caveats: The author is the vendor. geng2025jsonschemabench cites it as "Kurt [2024b]".

### geng2025jsonschemabench
- Title: JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models (also titled "Generating Structured Outputs from Language Models: Benchmark and Studies")
- Authors: Saibo Geng, Hudson Cooper, Michał Moskal, Samuel Jenkins, Julian Berman, Nathan Ranchin, Robert West, Eric Horvitz, Harsha Nori
- Date: 2025 (arXiv 2501.10868v3, 27 Feb 2025)
- URL: https://arxiv.org/abs/2501.10868
- Type: benchmark/dataset paper + empirical study. Several authors are Guidance/Microsoft developers, so there is a possible author-interest conflict.
- Verification: full text (raw text). Read the abstract, §1, Definitions 5.1–5.3, §5.1 setup and §6.
- Supports:
  - Three axes: efficiency, coverage and quality. The benchmark has 10K real-world JSON schemas plus the official JSON Schema Test Suite. Six frameworks were tested: Guidance, Outlines, llama.cpp, XGrammar, OpenAI and Gemini.
  - Declared coverage: the schema is accepted without error. Empirical coverage: the outputs validate. True coverage: the framework's constraints exactly equal the schema, which is not measurable in practice. Compliance Rate = C_empirical/C_declared.
  - Efficiency averaged over covered instances only is biased in favour of low-coverage engines, which tend to accept only simpler schemas.
  - Setup: Llama-3.2-1B, greedy decoding, validation with the Python `jsonschema` library (Draft 2020-12, format checks on), 40 s timeouts. Exceeding a timeout counts as a failure.
  - §6 quality: on Last Letter, Shuffle Objects and GSM8K, using Kurt's prompts with Llama-3.1-8B, constrained decoding beat unconstrained in every framework. Guidance was about 3 points above LM-only. The abstract mentions gains of up to 4%.
  - The authors explain how quality could degrade in principle: tokenization ambiguity and distribution shift (toy example of '89,000' being forced into '890000').
- Caveats: These results contradict tam2024speakfreely. Prompt design is the confounder both sides acknowledge.

### willard2023outlines
- Title: Efficient Guided Generation for Large Language Models
- Authors: Brandon T. Willard, Rémi Louf
- Date: 2023 (arXiv 2307.09702v4, 19 Aug 2023)
- URL: https://arxiv.org/abs/2307.09702
- Type: method paper
- Verification: full text (raw text). Read the abstract, §1 and §2 setup.
- Supports: Guided generation is reformulated as transitions of a finite-state machine (for regular expressions) or a parser (for CFGs), with an index precomputed over the vocabulary. The next-token boolean mask m: P(V) → {0,1}^N costs O(1) on average rather than O(N) per step. Structure is guaranteed. Implemented in Outlines.
- Caveats: The method guarantees syntax, not semantic correctness.

### openai_structured_outputs
- Title: Structured Outputs (API guide)
- Authors / organization: OpenAI (platform docs)
- Date: living document, fetched 2026-10-02. The page text now mentions current model names, so content may change.
- URL: https://platform.openai.com/docs/guides/structured-outputs
- Type: official docs
- Verification: full text (HTML fetched with curl and stripped to text)
- Supports:
  - Structured Outputs is "the evolution of JSON mode". Both produce valid JSON, but "only Structured Outputs ensure schema adherence".
  - Enabled via `response_format: {type: "json_schema", json_schema: {..., strict: true}}` or `strict: true` on function definitions.
  - Supports only a subset of JSON Schema (string, number, boolean, integer, object, array, enum, anyOf). All fields must be `required`, and `additionalProperties: false` must be set. Limits: up to 5000 properties, 10 nesting levels, 1000 enum values, 120,000 characters of total string length.
  - Safety refusals are returned in a separate, programmatically detectable `refusal` field.
  - Edge cases still have to be handled: check `finish_reason` (e.g. truncation leaves the output incomplete) and refusals.
  - For JSON mode, a validation library and possibly retries are recommended.
  - "Structured Outputs can still contain mistakes", i.e. schema-valid values can still be wrong.
  - The first request with a new schema has extra latency for fine-tuned models.
- Caveats: This is vendor documentation describing guarantees, not an independent measurement.

### lmeval_harness_filters
- Title: lm-evaluation-harness task guide (Filters) + `lm_eval/filters/extraction.py` + `lm_eval/tasks/gsm8k/gsm8k.yaml`
- Authors / organization: EleutherAI
- Date: main branch at commit d6de816 (committed 2026-09-14)
- URL: https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/task_guide.md
- Type: official docs/code
- Verification: full text (raw files read)
- Supports:
  - Filters post-process model outputs before scoring, in chains such as regex → take_first, or regex → majority_vote → take_first for maj@k. One task can run several filter pipelines on the same generations.
  - `RegexFilter` returns `fallback="[invalid]"` when nothing matches, so an unparseable output is scored as wrong rather than dropped.
  - gsm8k.yaml reports two pipelines: "strict-match" (`#### (number)`) and "flexible-extract" (the last number-like string). Exact match is configured with ignore_case, regexes_to_ignore (",", "$", etc.) and ignore_punctuation: false.
- Caveats: Strict and flexible scores can differ a lot, so the filter must be named when reporting a number.

### liang2022helm
- Title: Holistic Evaluation of Language Models (HELM)
- Authors: Percy Liang, Rishi Bommasani, Tony Lee, et al. (Stanford CRFM)
- Date: 2022 (arXiv 2211.09110v2, 1 Oct 2023; TMLR)
- URL: https://arxiv.org/abs/2211.09110
- Type: benchmark/dataset paper
- Verification: full text for the findings list only (§1.1 findings 22–23, raw text). HELM's per-instance parsing rules were not read.
- Supports: Finding 22: all models are significantly sensitive to prompt formatting and to the choice and number of in-context examples. Finding 23: the multiple-choice adaptation method matters a great deal. OPT-175B scored 79.1% on HellaSwag with separate 0-shot prompts per choice and 30.2% with joint 5-shot multiple-choice formatting. The best adaptation differs across models.
- Caveats: Does not directly document how HELM counts parse failures (gap).

### gebru2021datasheets
- Title: Datasheets for Datasets
- Authors: Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III, Kate Crawford
- Date: arXiv 1803.09010 (v8 read); CACM 64(12):86–92, 2021 (doi:10.1145/3458723)
- Type: position/survey (documentation framework)
- Verification: full text (raw text, v8). Read the Composition, Collection process and §3.4 Preprocessing/cleaning/labeling sections only.
- Supports (annotation-relevant questions only):
  - Composition: "Is there a label or target associated with each instance?" and "Are there any errors, sources of noise, or redundancies?"
  - Collection: "Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated?"
  - §3.4: was any preprocessing, cleaning or labeling done; was the raw data saved; is the labeling software available. These questions are meant to be read before labeling and answered afterwards.
  - Maintenance: will the dataset be updated, e.g. to correct labeling errors?
- Caveats: Does not ask for agreement statistics explicitly. That has to be added from artstein2008agreement.

### pustejovsky2012matter (and finlayson2016overview)
- Title: Natural Language Annotation for Machine Learning (O'Reilly, 2012, 342 pp., ISBN 9781449306663). Secondary source: Finlayson & Erjavec, "Overview of Annotation Creation: Processes & Tools", in Ide & Pustejovsky (eds.) Handbook of Linguistic Annotation, Springer 2016/2017; arXiv 1602.05753.
- Authors: James Pustejovsky, Amber Stubbs; Mark A. Finlayson, Tomaž Erjavec
- Type: textbook/tutorial (book); position/survey (handbook chapter)
- Verification: the book is unverified (O'Reilly and Semantic Scholar returned 403/429; only search-result catalog listings were seen). The Finlayson & Erjavec chapter is full text (raw text, §2.1).
- Supports (via Finlayson & Erjavec §2.1):
  - MATTER = Model, Annotate, Train, Test, Evaluate, Revise.
  - Model: theory, annotation scheme and specification, with versioning.
  - Annotate: write guidelines, recruit and train annotators until IAA is acceptable, track IAA and guideline versions, schedule adjudication meetings, adjudicate multiple annotations into a gold standard, and capture process metadata such as time and annotator identity.
  - The MAMA sub-cycle (Model–Annotate–Model–Annotate) uses pilot annotation to revise the scheme before full annotation. A smaller loop rewrites guidelines inside the Annotate stage.
  - Finlayson & Erjavec replace Train/Test with "Leverage" for non-ML uses.
- Caveats: The chapter cites "Pustejovsky & Stubbs (2013)" while catalog listings give Oct 2012. The MATTER claims are attributed via the secondary source.

## Topic notes

### 1. Inter-annotator agreement (IAA)
- **General form.** S, π and κ are all (A_o − A_e)/(1 − A_e). They differ only in the chance model (artstein2008agreement §2.4):
  - S: uniform chance, A_e = 1/k. It can be gamed by adding unused categories.
  - π (Scott) and Fleiss's multi-rater coefficient: one pooled distribution, A_e = Σ_k P̂(k)².
  - κ (Cohen): a separate marginal for each coder, A_e = Σ_k P̂(k|c1)P̂(k|c2).
- **Multi-rater (Fleiss).** agr_i = Σ_k n_ik(n_ik−1)/(c(c−1)), A_o = mean_i agr_i, and P̂(k) = n_k/(ic) (fleiss1971 via artstein2008agreement §2.5.1). Fleiss's "kappa" is actually a multi-π.
- **Krippendorff's α.** α = 1 − D_o/D_e, built from a coincidence matrix and a distance δ² (nominal, ordinal, interval, ratio). It handles missing data and any number of coders (krippendorff2011computing). For nominal data, α ≈ π with a small-sample correction.
  - Worked example: 2 coders, 10 binary units, o_01 = 4, n_0 = 14, n_1 = 6 gives α = 1 − 19·4/(14·6) ≈ 0.095.
  - For ordinal "score" labels, an ordinal or interval δ is the principled choice. Different δ give different α (artstein2008agreement §2.6.1, §4.4).
- **Paradoxes.** With skewed prevalence, κ can be low while A_o is high (feinstein1990paradox). Asymmetric marginal imbalance gives higher κ than symmetric imbalance. Artstein & Poesio show κ ≈ δ/(δ+ε), driven by agreement on the rare class, and argue this is the correct behaviour for a reliability measure.
- **Interpretation.** Krippendorff's α ≥ 0.8, with 0.667 "highly tentative". Landis–Koch bands are widely used but criticized. No universal cutoff exists.
- **Reporting.** Report the number of coders, whether coding was independent, the guidelines used, and a confusion matrix or agreement table (artstein2008agreement §5.3).
- **LLM-judge practice.** thakur2024judges v6 replaced Cohen's κ with Scott's π. bavaresco2024judgebench uses Cohen's κ for categorical and Spearman for graded judgments. chiang2023alternative uses Kendall τ, arguing IAA penalizes exact-rating mismatch while correlation measures ordering.

### 2. Label variation and disagreement
- **Disagreement can be signal.** aroyo2015truth lists seven myths, notably "one truth", "disagreement is bad" and "detailed guidelines help". pavlick2019inherent found disagreement persists at 50 raters/item and ~20% of NLI pairs are bimodal. nie2020chaosnli found the old majority label changes on 10–32% of selected low-agreement items with 100 labels, and models are near chance on low-agreement items.
- **Evaluation options** (uma2021disagreement §4, plank2022hlv §4):
  - Hard: accuracy or F1 against gold, or crowd-truth-weighted F1.
  - Soft: cross-entropy H(p_hum, p_θ), which is bounded below by H(p_hum) and not 0.
  - Soft: JSD, which is bounded and symmetric. ChaosNLI uses JS *distance* (the square root of JSD) in [0,1].
  - Soft: entropy correlation.
  - Splits by agreement level.
- **Test-set label errors** are a separate issue from inherent variation. At least 3.3% of test labels are wrong on average, and they can reverse model rankings (northcutt2021labelerrors).
- **Practical implication.** When items are ambiguous, a probabilistic "choice" output can be scored against a human label distribution (CE/JSD) rather than only against an argmax gold label. This needs more than one label per item.

### 3. LLM-as-judge
- **Protocols.** Pairwise preference, single-answer (absolute) grading, and reference-guided grading (zheng2023mtbench §3.1). Pairwise grows quadratically and is more sensitive to position. Single grading scales but gives more ties and may miss subtle differences. G-Eval computes an expected score Σ p(s_i)s_i to get continuous output (liu2023geval).
- **Known biases with measured magnitudes:**
  - Position: GPT-4 swap-consistency 65% (zheng2023mtbench). ChatGPT conflict rate up to 82.5%, and order alone could make Vicuna "win" 66/80 queries (wang2023notfair).
  - Verbosity: repetitive-list attack fails 91.3% of the time for weaker judges and 8.7% for GPT-4.
  - Self-preference: inconclusive in zheng2023mtbench. Linked causally to self-recognition in panickssery2024selfpref.
  - Leniency and prompt sensitivity (thakur2024judges).
  - Bias toward LLM-generated text (liu2023geval, a stated concern).
- **Mitigations.** Swap positions and count a win only if it holds in both orders. Average over orders (Balanced Position Calibration). Use a rationale before the score. Use few-shot examples. Use reference answers for math. Route high-entropy items to humans.
- **Agreement numbers depend on tie handling.** GPT-4 vs humans is 85% without ties but 66% with ties; human–human is 81% vs 63% (zheng2023mtbench Table 5). Report the chance baseline (50% or 33%) and the tie policy.
- **Validation requirement.** Judges vary widely by task and property, so validate on in-domain human labels before use (bavaresco2024judgebench, thakur2024judges). High percent agreement can hide 10–20 point score shifts, so use chance-corrected agreement and score-level deviations as well.
- **Aggregating pairwise preferences.** Use Bradley–Terry MLE with sandwich or bootstrap CIs (chiang2024arena). Arena moved from Elo to BT for statistical estimation.

### 4. Generation metrics and acceptable answers
- **SQuAD EM/F1.** Normalize (lowercase, strip punctuation, drop a/an/the, collapse whitespace). EM is equality. F1 is token-multiset overlap. Take the max over multiple references, then the macro mean (rajpurkar2016squad §6.1, squad_eval_scripts).
- **SQuAD 2.0.** Unanswerable gold = [""]. An abstention scores 1 only on unanswerable items. An na_prob threshold converts predictions to abstentions.
- **Human ceiling.** On SQuAD v1.1 this is 77.0 EM / 86.8 F1, and is mostly boundary disagreement. Multiple references are what keep F1 meaningful.
- **Lexical matching underestimates generative and LLM answers.** InstructGPT zero-shot went from 12.6% to 71.4% under human judgment, and more than 50% of failures were semantically equivalent answers. Regex/alias matching preserved rankings. Automated semantic judges (BEM, LLM-eval) fail on long answers and hallucinations (kamalloo2023odqa).
- **Parser choice can dominate.** Strict regex vs LLM extraction differs by 30–43 points on GSM8K (tam2024speakfreely appendix). lm-eval reports strict-match and flexible-extract side by side (lmeval_harness_filters).

### 5. Structured outputs
- **Three levels of correctness.**
  1. Syntactic validity (parses).
  2. Schema compliance (validates against the JSON Schema).
  3. Semantic correctness (the values are right).
  Constrained decoding guarantees (1) and (2) only for the subset of schema features the engine supports. OpenAI's own docs state that structured outputs "can still contain mistakes" (openai_structured_outputs). JSON mode guarantees (1) only.
- **Engine coverage is partial.** geng2025jsonschemabench distinguishes declared, empirical and true coverage and defines compliance rate = empirical/declared. It also warns that efficiency averaged over covered schemas favours engines that accept fewer, simpler schemas.
- **Effect on task quality is contested:**
  - tam2024speakfreely: strict format, especially JSON-mode, hurts reasoning but helps classification. Parse errors were not the cause (0.148% parse error with a 38-point gap).
  - kurt2024saywhatyoumean (vendor) and geng2025jsonschemabench: with matched prompts, a schema description in the prompt, and reasoning fields placed before the answer, constrained decoding equals or beats unconstrained by about 1–4 points.
  - Agreed confounders: prompt parity, schema description in the prompt, field order (reasoning before answer), and the answer parser.
- **Retries and repair.** A corrective reformatting pass raised JSON/YAML scores (tam2024speakfreely §5.3). OpenAI recommends validation plus retries for JSON mode (openai_structured_outputs). End-to-end success = P(valid on attempt 1) + P(invalid then repaired and correct). Report first-pass validity, post-repair validity, and correctness conditional on validity separately, and count the extra calls in cost and latency. This decomposition is the synthesis in this file, not a quoted source.
- **Accounting for parse failures differs across harnesses:**
  - lm-eval maps no-match to "[invalid]", which is scored wrong.
  - bavaresco2024judgebench imputes a random label for invalid outputs and reports valid-response rates.
  - The SQuAD v2 script skips missing predictions with a warning, so n silently shrinks.
  - HELM documents strong sensitivity to prompt format and adaptation method (liang2022helm findings 22–23).
  - Practice point: always state the policy (count as wrong / impute / exclude) and report the invalid rate.
- **Implementation.** Constrained decoding via an FSM or CFG index with O(1)-average mask lookup (willard2023outlines). OpenAI strict mode requires all fields `required` and `additionalProperties: false`. Check finish_reason and refusals, because truncation and refusals bypass the schema guarantee.

### 6. Annotation guidelines practice
- **MATTER cycle** (Model → Annotate → Train → Test → Evaluate → Revise), with the MAMA pilot sub-cycle and a guideline-revision loop inside Annotate (pustejovsky2012matter via finlayson2016overview). The Annotate stage includes:
  - writing guidelines;
  - training annotators until IAA is acceptable;
  - tracking IAA and guideline versions;
  - adjudicating into a gold standard;
  - recording process metadata.
- **Datasheets** (gebru2021datasheets): document labels and targets, known errors and noise, who annotated and how they were paid, the labeling process and software, whether raw data was kept, and whether label errors will be corrected.
- **Tension with the disagreement literature.** aroyo2015truth argues detailed guidelines can suppress informative disagreement. artstein2008agreement notes the trade-off between replicability (naive coders following the manual) and usefulness (experts or intensive training), and recommends evaluating the downstream task independently.
