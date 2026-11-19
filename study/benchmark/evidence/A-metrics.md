# Sources: Cluster A — classification, detection, multilabel, retrieval/ranking, ordinal/regression metrics

Accessed 2026-10-02 for all sources. "full-text" means that I read the cited passages in raw text from the PDF/HTML (via `curl` + `pdftotext` or page images). It does not mean a WebFetch summary. Numbers marked "(derived)" are my own arithmetic on a source's numbers or definitions. They are not claims from the source.

> Evidence notes for cluster A of [study/benchmark](../README.md), compiled 2026-10-02 in step2 of benchmark/p1 by a research subagent and reviewed by the lead session. The search log and gaps for this cluster are in [search-log.md](../search-log.md). Verification levels are per entry; claims beyond the stated level must not be attributed to a source.

## Source list

### opitz2019macrof1
- Title: Macro F1 and Macro F1 (a note)
- Authors / organization: Juri Opitz, Sebastian Burst (Heidelberg University)
- Date: arXiv v1 2019-11-08; v3 2021-02-08
- URL / DOI / arXiv id: arXiv:1911.03347 (https://arxiv.org/abs/1911.03347)
- Type: method paper (short analytical note)
- Verification: full-text (PDF v3; §1 Eqs. 1-3, §2 Theorem + Lemma Eq. 4, §3 Tables 1-2, Fig. 1)
- Supports:
  - Confusion matrix convention: m_ij = |{s : f(s1)=i ∧ s2=j}| (rows = predicted, columns = gold). P_i = m_ii / Σ_x m_ix, R_i = m_ii / Σ_x m_xi, F1_i = 2P_iR_i/(P_i+R_i). **P_i, R_i, F1_i are set to 0 when the denominator is zero** (Eq. 1).
  - Two definitions are both called "macro F1". (a) "Averaged F1" = (1/n) Σ_x F1_x (Eq. 2). (b) "F1 of averages" = H(P̄, R̄) = 2P̄R̄/(P̄+R̄), where P̄ and R̄ are the arithmetic means (Eq. 3).
  - Theorem: F1-of-averages ≥ averaged-F1, with equality iff P_i = R_i for every class. The supremum of the difference is 0.5 for even n and 0.5 − 1/(2n²) for odd n (§2).
  - The difference is large for classifiers with skewed error types (some classes with P≫R and others with R≫P). The F1 of averages "rewards" such classifiers (§2).
  - The two definitions can rank classifiers differently. Table 1 (2×2, rows predicted [a: 5,10; b: 5,10]) and Table 2 ([a: 1,1; b: 9,19]) show it. Adding bias toward class b raises F1-of-averages (0.50 → 0.55) and lowers averaged-F1 (0.49 → 0.48). I re-computed these values (derived): Table 1 F1_a=0.400, F1_b=0.571, mean 0.486, P̄=R̄=0.5. Table 2 F1_a=0.167, F1_b=0.792, mean 0.479, P̄=0.589, R̄=0.525, H=0.555.
  - Simulation with random classifiers on 95/5 binary data: F1-of-averages reaches ≈0.56 and averaged-F1 ≈0.41. Pearson ρ = 0.72 between the two (§3, Fig. 1a).
- Caveats / disagreements: Recommends averaged-F1, the arithmetic mean of per-class F1 (§4). scikit-learn implements this definition (see sklearn-modeleval).

### opitz2024closerlook
- Title: A Closer Look at Classification Evaluation Metrics and a Critical Reflection of Common Evaluation Practice
- Authors / organization: Juri Opitz (University of Zurich)
- Date: arXiv 2024-04-25 (v2 2024-07-02); published in TACL 2024
- URL / DOI / arXiv id: arXiv:2404.16958; DOI 10.1162/tacl_a_00675
- Type: method paper + survey of shared-task practice
- Verification: full-text (arXiv v2 PDF; §2 Preliminaries, §3 properties PI–PV, §4.1–4.7, Eqs. 1–16, Table 5, §7.1 Table 6 / Fig. 1)
- Supports:
  - Definitions: bias(i) = Σ_x m_{i,x} (number predicted as i), prevalence(i) = Σ_x m_{x,i}, correct(i) = m_{i,i}. P_i = correct/bias ≈ P(c=i | f→i), R_i = correct/prevalence ≈ P(f→i | c=i) (Eqs. 1–2).
  - Five properties: PI monotonicity, PII class sensitivity, PIII class decomposability (macro-average form, Eq. 4), PIV prevalence invariance (metric(mλ) = metric(mλ') for diagonal column scalings λ), and PV chance correction (§3).
  - Accuracy = Σ_i m_ii / |S|. In multi-class single-label evaluation, accuracy = micro-P = micro-R = micro-F1 (§4.1). Accuracy has only PI.
  - Macro recall, macR = (1/n) Σ R_i (Eq. 7), has all five properties and is strictly chance-corrected with baseline 1/n. It equals accuracy after "prevalence calibration" (λ_ii = |S|/(n·prevalence(i)), Eq. 6) (§4.2). This is the same quantity as balanced accuracy.
  - Macro precision lacks prevalence invariance (§4.3). Macro F1 (mean of per-class F1, Eq. 10) lacks PIV. Its chance baseline upper bound 1/n is reached only when P(f→i) = P(c=i) (§4.4).
  - macF1' (harmonic mean of macP and macR, Eq. 11) is not class-decomposable (§4.5). Opitz attributes an early mention of this variant to Sokolova & Lapalme (2009).
  - Weighted F1 = (1/|S|) Σ prevalence(i)·F1_i. It is **non-monotonic** and has only PII. Opitz "could not determine clear reasons for favoring weighted F1 over Accuracy" (§4.6, §6.1).
  - Multi-class MCC = (accuracy − chance)/√((1 − bᵀb)(1 − pᵀp)), and Cohen's κ = (accuracy − chance)/(1 − chance), where chance = pᵀb on a normalized matrix (Eqs. 13–15). Both are non-monotonic and fully chance-corrected (baseline 0). Their signs agree and |MCC| ≥ |κ| (§4.7).
  - Empirical result: in SemEval-2017 Task 4 (sentiment), different metrics give different team rankings, and Fig. 1 shows the ranking correlation matrix. Most shared tasks gave no convincing argument for their metric choice (§7).
- Caveats / disagreements: Conflicts with Chicco & Jurman's "MCC is the most informative" position. Opitz finds MCC non-monotonic and less interpretable than κ or macro recall.

### sklearn-modeleval
- Title: scikit-learn User Guide §3.4 "Metrics and scoring: quantifying the quality of predictions" (plus API pages for precision_recall_fscore_support, ndcg_score, cohen_kappa_score)
- Authors / organization: scikit-learn developers
- Date: documentation version 1.9.1 (stable, as served on 2026-10-02)
- URL: https://scikit-learn.org/stable/modules/model_evaluation.html ; https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html ; .../sklearn.metrics.ndcg_score.html ; .../sklearn.metrics.cohen_kappa_score.html
- Type: official docs
- Verification: full-text (raw HTML stripped; §3.4.4.1, 3.4.4.2, 3.4.4.4, 3.4.4.8, 3.4.4.9.1–2, 3.4.4.13, 3.4.4.15, 3.4.5.4, plus the API parameter text)
- Supports:
  - Averaging (§3.4.4.1, §3.4.4.9.2). With y the set of true (sample, label) pairs, ŷ the predicted pairs, P(A,B) = |A∩B|/|B| and R(A,B) = |A∩B|/|A|:
    - "micro": P(y, ŷ), computed from pooled TP/FP/FN.
    - "macro": (1/|L|) Σ_l P(y_l, ŷ_l).
    - "weighted": Σ_l |y_l| P(y_l, ŷ_l) / Σ_l |y_l|, i.e. weighted by support.
    - "samples": (1/|S|) Σ_s P(y_s, ŷ_s), multilabel only.
    - The docs note that in multiclass micro-P = micro-R = micro-F = accuracy when all labels are included. "Weighted" F can fall outside the range [P, R]. Macro F is "the arithmetic mean over per-label F … not the harmonic mean over the arithmetic precision and recall means … see [OB2019]".
  - Zero/undefined cases. "Conventions vary on handling A = ∅; this implementation uses R(A,B) := 0, and similar for P." The parameter `zero_division ∈ {"warn", 0.0, 1.0, np.nan}` defaults to "warn", which acts as 0. With np.nan (added in v1.3) such values "will be excluded from the average". Recall is undefined with no positive labels, precision with no positive predictions. F_β is computed as (1+β²)tp / ((1+β²)tp + fp + β²fn) and is "still undefined when there are no true positives, false positives, or false negatives". It defaults to 0 for an all-true-negative set.
  - Labels. The `labels` argument can exclude a "negative class" from micro/macro averaging, or include labels absent from the data, which then count as 0 in macro averages.
  - Accuracy (§3.4.4.2) = (1/n) Σ 1(ŷ_i = y_i). In multilabel it is **subset accuracy**.
  - Balanced accuracy (§3.4.4.4) is the macro-average of per-class recall, i.e. accuracy with each sample weighted by the inverse prevalence of its true class. In binary it is ½(TP/(TP+FN) + TN/(TN+FP)). `adjusted=True` rescales so that chance = 0 (binary: Youden's J / informedness). The docs say "there is no certain consensus in the literature" on the multiclass definition and list the alternatives of Mosley 2013 (mean over classes of min(P,R)) and Urbanowicz 2015 (per-class mean of sensitivity and specificity).
  - Hamming loss (§3.4.4.8) = (1/(n_samples·n_labels)) ΣΣ 1(ŷ_ij ≠ y_ij). It is upper-bounded by the zero-one loss.
  - Average precision: AP = Σ_n (R_n − R_{n−1}) P_n, not interpolated. "With random predictions, the AP is the fraction of positive samples". The docs cite Davis & Goadrich and Flach & Kull on why linear interpolation of PR points with the trapezoid rule is "overly-optimistic", and Chen et al. 2024 on interpolation strategies.
  - MCC (§3.4.4.13): binary (tp·tn − fp·fn)/√((tp+fp)(tp+fn)(tn+fp)(tn+fn)). Multiclass (c·s − Σ p_k t_k)/√((s² − Σ p_k²)(s² − Σ t_k²)). For more than two classes the minimum lies between −1 and 0.
  - ROC (§3.4.4.15): multiclass AUC options are OvR (macro/weighted/micro) and OvO (Hand & Till 2001, macro/weighted). `max_fpr` gives a partial AUC.
  - NDCG (§3.4.5.4, API): DCG@K = Σ_{r=1}^{min(K,M)} y_{f(r)}/log(1+r). This uses **linear gain**, and NDCG divides by the ideal DCG. `ignore_ties=False` by default, with ties handled per McSherry & Najork 2008. Negative y_true may give values outside [0,1].
  - cohen_kappa_score: κ = (p_o − p_e)/(1 − p_e), with `weights ∈ {None, 'linear', 'quadratic'}`. `replace_undefined_by` (default nan) was added in 1.9 for undefined cases. The guide says the function is "intended to compare labelings by different human annotators, not a classifier versus a ground truth".
- Caveats: Documentation describes the library's conventions, not universal ones. The defaults (zero_division→0, linear NDCG gain) differ from other toolkits, e.g. Manning's exponential NDCG gain.

### brodersen2010balacc
- Title: The balanced accuracy and its posterior distribution
- Authors: Kay H. Brodersen, Cheng Soon Ong, Klaas E. Stephan, Joachim M. Buhmann (ETH Zurich / Univ. Zurich)
- Date: 2010 (ICPR 2010, pp. 3121–3124)
- URL / DOI: DOI 10.1109/ICPR.2010.764; PDF https://ong-home.my/papers/brodersen10post-balacc.pdf
- Type: method paper
- Verification: full-text (§I–III)
- Supports:
  - Balanced accuracy = ½(TP/P + TN/N). "If the classifier performs equally well on either class, this term reduces to the conventional accuracy … if the conventional accuracy is high only because the classifier takes advantage of an imbalanced test set, then the balanced accuracy … will drop to chance" (§III).
  - A cost-weighted variant c·TP/P + (1−c)·TN/N is also given (§III).
  - Averaging fold accuracies has two problems: it supports no meaningful CI (SEM-based intervals can exceed 100%), and it is optimistic for a biased classifier on imbalanced data (§I). As an alternative, the posterior of accuracy is Beta(C+1, I+1) under a flat prior (§II, Eqs. 1–2). The paper extends this to the posterior of balanced accuracy (§III).
- Caveats: Binary only. The multiclass extension is not in this paper (sklearn notes that there is no consensus).

### chicco2020mcc
- Title: The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation
- Authors: Davide Chicco, Giuseppe Jurman
- Date: 2020; BMC Genomics 21:6
- URL / DOI: DOI 10.1186/s12864-019-6413-7 (full text via Europe PMC PMC6941312)
- Type: position / method paper with worked examples
- Verification: full-text (Europe PMC full-text XML; the "undefined MCC" passage, Eq. 3, use cases A1–C2, Table 4)
- Supports:
  - MCC ∈ [−1, +1], and 0 is the expected value for coin tossing. MCC is **undefined when a whole row or column of the confusion matrix is zero**, e.g. the trivial majority classifier. Their convention: if only one entry is nonzero, MCC = +1 when that entry is TP or TN and −1 when it is FP or FN. In the four cases with one zero row or column, a limit with ε→0 gives MCC = 0. Hence "MCC=0 for the trivial majority classifier" (Eq. 3).
  - Use cases (Table 4), listed as (TP, FN, TN, FP) → accuracy / F1 / MCC:
    - A1, positively imbalanced (91 pos / 9 neg): (90, 1, 0, 9) → 0.90 / 0.95 / −0.03.
    - A2: (5, 70, 19, 6) → 0.24 / 0.12 / −0.24.
    - B1, balanced: (47, 3, 5, 45) → 0.52 / 0.66 / +0.07.
    - B2: (10, 40, 46, 4) → 0.56 / 0.31 / +0.17.
    - C1, negatively imbalanced: (9, 1, 1, 89) → 0.10 / 0.17 / −0.19.
    - C2: (2, 9, 88, 1) → 0.90 / 0.29 / +0.31.
  - The authors conclude that MCC was the only one of the three rates that flagged the problem in all six cases.
- Caveats / disagreements: This is an advocacy paper. Opitz 2024 shows that MCC is non-monotonic and depends on classifier bias (bᵀb). The use cases are selected illustrations, not a systematic study.

### sokolova2009systematic
- Title: A systematic analysis of performance measures for classification tasks
- Authors: Marina Sokolova, Guy Lapalme
- Date: 2009-07; Information Processing & Management 45(4):427–437
- DOI: 10.1016/j.ipm.2009.03.002
- Type: survey / method paper
- Verification: **unverified** for content. Metadata was verified via Crossref and Semantic Scholar, but ScienceDirect returned 403, the author-site PDF URL returned HTML, and Semantic Scholar marks it CLOSED with the abstract elided.
- Supports: No claims attributed from direct reading. Secondhand only: Opitz 2024 §4.5 says this paper is an early mention of macro-F1 as the harmonic mean of macro-P and macro-R.
- Caveats: Do not cite for specific formulas without obtaining the text.

### fawcett2006roc
- Title: An introduction to ROC analysis
- Authors: Tom Fawcett
- Date: 2006; Pattern Recognition Letters 27:861–874
- DOI: 10.1016/j.patrec.2005.10.010 (PDF via a university mirror)
- Type: textbook/tutorial
- Verification: full-text (§2, §4.2, §5 incl. Fig. 6, §6 Eq. 1, §7)
- Supports:
  - tp rate = positives correctly classified / total positives (= recall). fp rate = negatives incorrectly classified / total negatives (§2).
  - "ROC curves … are insensitive to changes in class distribution". TPR and FPR are each "a strict columnar ratio". Accuracy, precision, lift and F use both columns and therefore change with class skew "even if the fundamental classifier performance does not" (§4.2). Fig. 5 shows the same two classifiers at 1:1 and 1:10 class ratios. The ROC curves are identical while the PR curves "differ substantially", and "the conclusion of which classifier has superior performance can change".
  - AUC equals the probability that a random positive is ranked above a random negative (equivalent to the Wilcoxon rank test), and Gini + 1 = 2·AUC (§7). Random guessing gives AUC 0.5.
  - **Ties:** equally scored instances should be handled by emitting the ROC point only after all ties are processed (the diagonal "expected" segment). Without this, results depend on test-set order, and the AUC error can reach nm/(2PN) for a tied leaf with n positives and m negatives (§5, Fig. 6).
  - Iso-performance lines have slope m = c(Y,n)p(n) / (c(N,p)p(p)). The optimal operating point therefore depends on class priors and costs (§6, Eq. 1).
- Caveats: Fawcett treats ROC's prevalence-invariance as an advantage. Saito & Rehmsmeier and Davis & Goadrich argue that this invariance hides poor precision under skew.

### davis2006prroc
- Title: The Relationship Between Precision-Recall and ROC Curves
- Authors: Jesse Davis, Mark Goadrich
- Date: ICML 2006
- URL: https://ftp.cs.wisc.edu/machine-learning/shavlik-group/davis.icml06.pdf
- Type: method paper
- Verification: full-text (Abstract, §3 Theorems 3.1–3.2, §4 Table 1, §5)
- Supports:
  - Theorem 3.1: for a fixed dataset there is a one-to-one correspondence between ROC and PR curves (same confusion matrices) when recall ≠ 0.
  - Theorem 3.2: a curve dominates in ROC space iff it dominates in PR space.
  - **Linear interpolation in PR space is incorrect and over-optimistic.** Interpolate in counts instead: TP_A + x, with FP increasing by the local skew (FP_B − FP_A)/(TP_B − TP_A). Worked example (§4, Table 1): 20 positives, 2000 negatives, A = (TP 5, FP 5), B = (TP 10, FP 30).
  - **Conflicting-conclusions example (§5, Fig. 7):** with 20 positives and 2000 negatives, curve I has AUC-ROC 0.813 vs 0.875 for curve II, but AUC-PR 0.514 vs 0.038. "Algorithms that optimize the area under the ROC curve are not guaranteed to optimize the area under the PR curve."
- Caveats: none.

### saito2015prc
- Title: The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets
- Authors: Takaya Saito, Marc Rehmsmeier
- Date: 2015-03-04; PLOS ONE 10(3):e0118432
- DOI: 10.1371/journal.pone.0118432
- Type: empirical study (simulation + literature analysis)
- Verification: full-text (Abstract, Methods/baselines, simulation section, Fig. 5)
- Supports:
  - The ROC baseline is fixed (the diagonal). The PRC baseline is y = P/(P+N), and the AUC(PRC) of a random classifier equals P/(P+N).
  - Simulation: 1,000 positives vs 1,000 or 10,000 negatives. ROC and CROC curves and AUCs are unchanged by imbalance while PRC changes. For the ER− classifier, the same ROC point is 160 FP / 500 TP when balanced and 1,600 FP / 500 TP when imbalanced. Derived: precision 0.758 vs 0.238 at the same (TPR 0.5, FPR 0.16).
  - ER+ and ER− have the same AUC(ROC) of 0.8 but differ in early retrieval. "AUC (ROC) is inadequate to evaluate the early retrieval performance in this case."
  - Analysis of 58 articles from a literature search (categories in S1 File).
- Caveats / disagreements: Contested by McDermott et al. 2024, who argue that AUPRC is not generally superior under imbalance.

### flach2015prg
- Title: Precision-Recall-Gain Curves: PR Analysis Done Right
- Authors: Peter A. Flach, Meelis Kull
- Date: NIPS 2015
- URL: https://papers.nips.cc/paper_files/paper/2015/file/33e8075e9970de0cfea955afd4644bb2-Paper.pdf
- Type: method paper
- Verification: full-text (Abstract, §1 ROC properties, §2 PR problems, §3 Definition 1 Eq. 4, Theorems 1–2)
- Supports:
  - ROC has universal baselines and linear interpolation, and E[acc] = π(1−π)(2·AUROC − 1) + ½ (§1).
  - PR has non-universal baselines (random precision = π, and "the always-negative classifier has undefined precision"), non-linear interpolation, and "it isn't meaningful to take the arithmetic average of precision values". The area under PR takes an arithmetic mean while F_β uses a harmonic mean, which are incoherent scales (§2, Abstract).
  - A random classifier predicting positive with probability p has F_β = (1+β²)pπ/(p + β²π). The relevant baseline is the always-positive classifier (prec = π, rec = 1) (§3).
  - Definition 1: precG = (prec − π)/((1−π)·prec) = 1 − (π/(1−π))·FP/TP, and recG = (rec − π)/((1−π)·rec) = 1 − (π/(1−π))·FN/TP (Eq. 4).
  - In PRG space interpolation is linear (Theorem 1) and F_β isometrics are straight lines with slope −β² (Theorem 2). AUPRG relates to expected F1. The abstract says that "the area under traditional PR curves can easily favour models with lower expected F1 score".
- Caveats: AUPRG is not widely adopted. McDermott 2024 lists it as future work.

### mcdermott2024auroc
- Title: A Closer Look at AUROC and AUPRC under Class Imbalance
- Authors: Matthew B. A. McDermott, Haoran Zhang, Lasse Hyldig Hansen, Giovanni Angelotti, Jack Gallifant
- Date: arXiv 2024-01-11 (v4 2025-01-13); NeurIPS 2024
- URL: arXiv:2401.06091; OpenReview S3HvA808gk
- Type: method paper + literature review (contrarian)
- Verification: full-text (Abstract, §2 Theorems 1–3, §6–7)
- Supports:
  - Theorem 1: AUROC(f) = 1 − E_{t∼f(x)|y=1}[FPR(f,t)], while AUPRC(f) = 1 − P(y=0)·E_{t∼f(x)|y=1}[FPR(f,t)/P_x(f(x)>t)]. AUPRC therefore weights FPR by the inverse "firing rate".
  - Theorem 2: AUROC improves by the same amount whichever mis-ordered pair is fixed. AUPRC "prioritizes high-score mistakes".
  - Theorem 3, which assumes perfect calibration: AUPRC can favor improvements in higher-prevalence subpopulations, which can increase disparities.
  - From the review of more than 1.5M papers, the authors say the claim "AUPRC is superior under class imbalance" is "often made without citation, misattributed … and aggressively overgeneralized".
  - Recommendation: choose the metric by deployment context. For example, AUPRC-like emphasis suits settings where false positives are expensive and top-k screening is used (Fig. 1).
- Caveats / disagreements: Directly disputes the general recommendation in Saito & Rehmsmeier. Theorem 3 needs a perfect-calibration assumption, which the authors themselves call a major limitation (§6). Both sides agree that AUPRC depends on prevalence. They disagree on whether that makes it better for model comparison.

### chen2024auprctools
- Title: Commonly used software tools produce conflicting and overly-optimistic AUPRC values
- Authors: Wenyu Chen, Chen Miao, Zhenghao Zhang, … Qin Cao
- Date: 2024-05; Genome Biology 25:118
- DOI: 10.1186/s13059-024-03266-y
- Type: empirical study
- Verification: abstract (Europe PMC)
- Supports (abstract only): The authors tested 10 popular PRC/AUPRC tools, used in more than 3,000 studies. The tools "rank classifiers differently and some tools produce overly-optimistic results."
- Caveats: Details of which tools and interpolation rules were not read.

### lipton2014f1threshold
- Title: Thresholding Classifiers to Maximize F1 Score
- Authors: Zachary C. Lipton, Charles Elkan, Balakrishnan Narayanaswamy
- Date: arXiv 2014-02-08
- URL: arXiv:1402.1892
- Type: method paper
- Verification: abstract (arXiv API)
- Supports (abstract only): For calibrated conditional probabilities, the F1-optimal threshold is half the optimal F1. For a completely uninformative classifier, the F1-optimal behavior is to predict all examples positive. The paper discusses micro, macro and per-instance F1 in multilabel settings.
- Caveats: The PRG paper (§2) also cites this result.

### zhang2014multilabel
- Title: A Review on Multi-Label Learning Algorithms
- Authors: Min-Ling Zhang, Zhi-Hua Zhou
- Date: IEEE TKDE 26(8), 2014 (author preprint)
- URL: http://palm.seu.edu.cn/zhangml/files/TKDE'13.pdf; DOI 10.1109/TKDE.2013.39
- Type: position/survey
- Verification: full-text (preprint §II-A3 threshold calibration, §II-B1–4, Fig. 1, Eq. 2)
- Supports:
  - Prediction is h(x) = {y | f(x,y) > t(x)}, where t is a thresholding function. Calibration options are a constant t (e.g. 0) or a learned, stacking-style t(x) (§II-A3).
  - Example-based metrics (§II-B2):
    - subsetacc = (1/p) Σ [[h(x_i) = Y_i]], which "tends to be overly strict especially when … q is large".
    - Hamming loss = fraction of misclassified instance-label pairs, (1/p) Σ |h(x_i) Δ Y_i| normalized by q. Text extraction lost the 1/q factor, but the paper's remark that "hloss … will be 2/q times of the traditional misclassification rate" for single-label data implies it.
    - Accuracy_exam = (1/p) Σ |Y∩h|/|Y∪h|, Precision_exam = |Y∩h|/|h|, Recall_exam = |Y∩h|/|Y|, and F^β_exam computed from these.
  - Ranking metrics: one-error, coverage, ranking loss and average precision.
  - Label-based metrics (§II-B3): B_macro = (1/q) Σ_j B(TP_j, FP_j, TN_j, FN_j), and B_micro = B(Σ TP_j, Σ FP_j, Σ TN_j, Σ FN_j). Macro "assume[s] equal weights for labels", micro for examples. Accuracy_macro = Accuracy_micro, and Accuracy_micro + hloss = 1.
  - Macro-AUC is the mean per-label Wilcoxon–Mann–Whitney statistic. Micro-AUC is computed over all relevant vs irrelevant instance-label pairs (Eq. 2).
  - §II-B4: classifiers that maximize subset accuracy "would perform rather poor if evaluated in terms of hamming loss, and vice versa". Evaluate on a broad range of metrics, not only the one being optimized.
- Caveats: Does not specify conventions for empty Y_i or empty h(x_i), where the example-based ratios are 0/0. See sklearn-modeleval for one implementation's choice (P or R := 0, configurable).

### manning2008irbook-ch8
- Title: Introduction to Information Retrieval, Chapter 8 "Evaluation in information retrieval"
- Authors: Christopher D. Manning, Prabhakar Raghavan, Hinrich Schütze
- Date: Cambridge UP 2008 (online edition 2009)
- URL: https://nlp.stanford.edu/IR-book/pdf/08eval.pdf
- Type: textbook/tutorial
- Verification: full-text (§8.3, §8.4 Eqs. 8.8–8.9, §8.5 pooling)
- Supports:
  - MAP(Q) = (1/|Q|) Σ_j (1/m_j) Σ_k Precision(R_jk), where m_j is the number of relevant documents. **A relevant document that is not retrieved contributes precision 0** (Eq. 8.8). MAP weights each information need equally. MAP varies widely across queries (e.g. 0.1–0.7), so test sets must be "large and diverse enough".
  - Precision at k does not need the size of the relevant set, but it is "the least stable" commonly used measure and "does not average well".
  - R-precision is precision at rank |Rel|, which equals the break-even point. It is "highly correlated with MAP empirically".
  - ROC/specificity is of little use for unranked retrieval because the true-negative set is huge.
  - NDCG(Q,k) = (1/|Q|) Σ_j Z_kj Σ_{m=1}^{k} (2^{R(j,m)} − 1)/log₂(1+m). This form uses **exponential gain** and a log₂(1+m) discount. Z normalizes a perfect ranking to 1, and if fewer than k documents are retrieved the sum runs up to k′ (Eq. 8.9).
  - Pooling: relevance is judged on the union of top-k results from several systems (§8.5). R-precision notes that Rel "may be incomplete" under pooling.
- Caveats: The gain function differs from Järvelin & Kekäläinen (linear gain, discount from rank b) and from sklearn (linear gain, log(1+r)). NDCG values are not comparable across implementations unless the gain and discount match.

### jarvelin2002cg
- Title: Cumulated Gain-Based Evaluation of IR Techniques
- Authors: Kalervo Järvelin, Jaana Kekäläinen
- Date: 2002; ACM TOIS 20(4):422–446
- DOI: 10.1145/582415.582418
- Type: method paper
- Verification: full-text (§2.1–2.3 Eqs. 1–4)
- Supports:
  - CG[i] = CG[i−1] + G[i] (Eq. 1). DCG[i] = CG[i] if i < b, else DCG[i−1] + G[i]/log_b(i) (Eq. 2). The discount is not applied below rank b, and the base b models user persistence.
  - Worked example with b = 2 and G = ⟨3,2,3,0,0,1,2,2,3,0,…⟩: CG = ⟨3,5,8,8,8,9,11,13,16,16,…⟩ and DCG = ⟨3,5,6.89,6.89,6.89,7.28,7.99,8.66,9.61,9.61,…⟩.
  - The ideal vector BV is built from the **recall base** of the topic: all judged relevant documents sorted by grade, not just the retrieved ones (Eq. 4). Normalized (D)CG divides the actual vector by the ideal vector position by position.
  - Uses graded relevance on a four-point scale (0–3). For statistical testing the authors note that 0–3 "is on an ordinal scale" and suggest nonparametric tests (Friedman) (§3.6).
- Caveats: The original nDCG is a vector over ranks. The scalar nDCG@k used today is a later convention.

### mcsherry2008ties
- Title: Computing Information Retrieval Performance Measures Efficiently in the Presence of Tied Scores
- Authors: Frank McSherry, Marc Najork (Microsoft Research)
- Date: ECIR 2008, LNCS 4956, pp. 414–421
- DOI: 10.1007/978-3-540-78646-7_38; PDF https://marc.najork.org/papers/ecir2008.pdf
- Type: method paper
- Verification: full-text (Abstract, §1, §2–2.1)
- Supports:
  - Tied scores define only a partial order. TREC's approach was "to arbitrarily pick one of the valid … orderings". The authors found that different well-sorted permutations "can have appreciably different performance values, large enough to affect the relative ordering of several of the scoring functions" (§1).
  - The paper gives tie-aware P, R, F1, AP, RR and NDCG equal to the average over all permutations of tied groups, at the cost of the tie-oblivious computation.
  - Tie-aware P@k: for the tied group V_c that straddles the cut-off, with n_c items of which r_c are relevant, the expected number of relevant items in the window is (k − t_c)·r_c/n_c (§2.1).
  - Macro-averaging over queries is the standard (§2).
- Caveats: Most relevant when scores are discrete, e.g. LLM outputs with coarse confidence levels or rounded probabilities.

### buckley2004bpref
- Title: Retrieval Evaluation with Incomplete Information
- Authors: Chris Buckley, Ellen M. Voorhees
- Date: SIGIR 2004
- URL: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=150469
- Type: method paper
- Verification: full-text (Abstract, §1, bpref and bpref-10 definitions)
- Supports:
  - The Cranfield paradigm assumes complete judgments. Pooled TREC collections approximate completeness, and comparisons are robust to small violations (§1).
  - Existing measures (MAP, P@10, R-prec) "are not robust to substantially incomplete relevance judgments" and decrease monotonically as qrels are reduced.
  - bpref = (1/R) Σ_r (1 − |n ranked higher than r| / R), where n ranges over the first R judged non-relevant documents. It uses only judged documents, so unjudged documents are ignored.
  - bpref-10 = (1/R) Σ_r (1 − |n ranked higher than r| / (10 + R)), with n among the top 10+R judged non-relevant documents. This fixes coarseness when R is very small.
  - bpref is highly correlated with MAP when judgments are complete.
- Caveats: Later work (e.g. Sakai 2007 "Alternatives to bpref"; Büttcher et al. 2007) critiqued bpref. These appeared in search results but were not read, so they are unverified.

### voorhees1999trec8qa
- Title: The TREC-8 Question Answering Track Report
- Authors: Ellen M. Voorhees (NIST)
- Date: TREC-8 proceedings, 1999
- URL: https://trec.nist.gov/pubs/trec8/papers/qa_report.pdf
- Type: benchmark/dataset paper (track overview)
- Verification: full-text (scanned PDF read as page images; §1, §2, Table 1)
- Supports:
  - Mean reciprocal rank: each question scores the reciprocal of the rank of the first correct response, or 0 if none of the 5 responses is correct. MRR is the mean over questions (§1).
  - Stated properties: MRR is "closely related to the average precision measure", "bounded between 0 and 1, inclusive, and averages well". It penalizes failing to retrieve an answer "but not unduly so".
  - Drawbacks: a question's score takes only six values (0, .2, .25, .33, .5, 1). There is no credit for multiple correct answers. Because at least one response was required, **"a system could receive no credit for realizing it did not know the answer"** (§1). This is relevant to abstention and fallback labels.
- Caveats: The set of score values depends on the cut-off (here 5).

### thakur2021beir
- Title: BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models
- Authors: Nandan Thakur, Nils Reimers, Andreas Rücklé, Abhishek Srivastava, Iryna Gurevych
- Date: arXiv 2021-04-17 (v4 2021-10-21); NeurIPS 2021 Datasets & Benchmarks track
- URL: arXiv:2104.08663
- Type: benchmark/dataset paper (benchmark-author claims)
- Verification: full-text (§3.3 Evaluation Metric, §6 Annotation Selection Bias, Table 4)
- Supports:
  - Metric choice (§3.3). P and R are rank-unaware, and MRR and MAP "fail to evaluate tasks with graded relevance". The authors chose nDCG@10 for all datasets, computed with pytrec_eval, the Python interface to trec_eval. Recall@100 is reported in an appendix. These are benchmark-author justifications, not methodological evidence.
  - Annotation selection bias (§6). Unjudged documents are "assumed to be irrelevant", so pools built from lexical systems disadvantage dense retrievers. On TREC-COVID, Hole@10 (the share of top-10 hits never judged) was 6.4% for BM25 and 2.8% for docT5query, against 14.4% for ANCE and 31.8% for TAS-B.
  - After annotating 980 missing pairs, ANCE nDCG@10 rose from 0.654 (slightly below BM25) to 0.735, while docT5query moved only from 0.713 to 0.714. **The system ranking changed** (Table 4).
- Caveats: This is a single-dataset hole study. The authors did the annotation blind to which system retrieved each document.

### sakai2021ordinal
- Title: Evaluating Evaluation Measures for Ordinal Classification and Ordinal Quantification
- Authors: Tetsuya Sakai (Waseda University)
- Date: ACL 2021 (2021.acl-long.214)
- URL: https://aclanthology.org/2021.acl-long.214.pdf
- Type: empirical study (meta-evaluation)
- Verification: full-text (§3.1 Eqs. 1–6, §5, Conclusions)
- Supports:
  - With c_ij = number of items of true class j predicted as i, and C⁺ = gold classes that are not empty:
    - MAE^M = (1/|C⁺|) Σ_{j∈C⁺} Σ_i |i−j| c_ij / c_•j (macro, Eq. 1).
    - MAE^µ = Σ_j Σ_i |i−j| c_ij / N (Eq. 2).
    - Sakai's version handles **empty gold classes** explicitly, unlike Baccianella et al. 2009. Both MAEs "assume equidistance".
  - CEM^ORD (Amigó et al. 2020) is restated with prox_ij = −log₂(max{0.5, K_ij}/N). The max keeps it finite (Eqs. 3–4).
  - Weighted κ (Cohen 1968): e_ij = c_i• c_•j / N and κ = 1 − Σ w_ij c_ij / Σ w_ij e_ij (Eq. 5). Linear weights are w_ij = |i−j|. **κ is 0 for every constant-class baseline system.**
  - Krippendorff's α for ordinal data (α-ORD) is also covered (Eq. 6).
  - Results: α, the two macro-F1 variants, MAE^M and κ give similar system rankings (Group A). MAE^µ and accuracy are similar to each other but drastically different from Group A (§5).
  - Recommendation for ordinal classification: use linear weighted κ as primary unless the task includes constant-class runs. Otherwise use α-ORD, and report both. For ordinal quantification use RNOD as primary and NMD as secondary. Sakai does "not see relying on equidistance as a practical problem" (Conclusions).
- Caveats / disagreements: Disagrees in emphasis with Amigó et al. 2020, who make ordinal invariance (no equidistance) a requirement. Sakai treats equidistance as acceptable.

### amigo2020cem
- Title: An Effectiveness Metric for Ordinal Classification: Formal Properties and Experimental Results
- Authors: Enrique Amigó, Julio Gonzalo, Stefano Mizzaro, Jorge Carrillo-de-Albornoz
- Date: ACL 2020, pp. 3938–3949
- URL: https://aclanthology.org/2020.acl-main.363.pdf
- Type: method paper
- Verification: full-text (Abstract, Table 1, §4.1 Properties 1–3, §4.2 metric analysis)
- Supports:
  - Popular ordinal-classification metrics either ignore order (P/R per class) or assume intervals (MAE). Shared tasks used MSE, MAE^M, Pearson, AvgRec, F1 and accuracy (Table 1).
  - Property 1, ordinal invariance: the metric is unchanged under strictly increasing transforms of both system output and gold. Property 2, ordinal monotonicity: moving predictions closer to the truth increases the score. Property 3, imbalance: errors on a small class should cost more than errors on a large class.
  - Classification metrics are ordinal-invariant but not monotonic. "Accuracy at n (Gaudette and Japkowicz, 2009)" relaxes accuracy with an ordinal margin.
  - MAE and MSE violate ordinal invariance. Their macro versions satisfy imbalance.
  - Weighted κ can be monotonic depending on the weights but is not ordinal-invariant.
  - Kendall τ-b and Spearman satisfy imbalance, while Pearson does not (§4.2).
  - The paper proposes CEM (Closeness Evaluation Measure), based on measurement and information theory.
- Caveats: CEM is newer and less adopted. Sakai 2021 found CEM^ORD rankings to be somewhat distinct from other measures.

### stevens1946scales
- Title: On the Theory of Scales of Measurement
- Authors: S. S. Stevens
- Date: Science 103(2684):677–680, 1946-06-07
- URL: JSTOR stable 1671815 (PDF via a course mirror)
- Type: position/survey (foundational)
- Verification: full-text (scanned pages 677–678 read as images; Table 1)
- Supports:
  - Table 1 gives four scales:
    - nominal: permutation group; number of cases, mode, contingency correlation.
    - ordinal: isotonic group (any monotonic increasing f); median, percentiles.
    - interval: general linear group x′ = ax + b; mean, SD, rank-order correlation, product-moment correlation.
    - ratio: similarity group x′ = ax; coefficient of variation.
  - "The criterion for the appropriateness of a statistic is invariance under the transformations." The mean of an ordinal variable is not invariant. Stevens notes that rank-order correlation, "usually deemed appropriate to an ordinal scale", in fact assumes equal intervals.
- Caveats: Stevens' admissibility doctrine is debated in statistics. This basis underlies Amigó's ordinal invariance and Sakai's equidistance discussion.

### gaudette2009ordinal
- Title: Evaluation Methods for Ordinal Classification
- Authors: Lisa Gaudette, Nathalie Japkowicz
- Date: 2009; Canadian AI 2009, LNCS 5549, pp. 207–210
- DOI: 10.1007/978-3-642-01818-3_25
- Type: empirical study (short paper)
- Verification: **unverified**. The Springer page redirects to an auth wall, Crossref has no abstract, and no open PDF was found on the author's publication list. Only a WebSearch snippet summary was seen, and it is not relied on.
- Supports: none directly. Secondhand via Amigó 2020: it introduced "accuracy at n" (within-n accuracy) for ordinal classification.
- Caveats: A search-engine summary claimed the paper finds MSE best when larger errors should be penalized and MAE good otherwise. This is **not verified** and should not be cited without reading the paper.

### cohen1968weightedkappa
- Title: Weighted kappa: Nominal scale agreement with provision for scaled disagreement or partial credit
- Authors: Jacob Cohen
- Date: Psychological Bulletin 70(4):213–220, 1968
- Type: method paper
- Verification: **unverified** (paywalled; not fetched). The formula is used as restated by Sakai 2021 Eq. 5, which is full-text verified.
- Supports: none directly.

## Topic notes

### 1. Single-label classification
- **Confusion matrix and orientation.** Conventions differ. Opitz uses rows = predicted and columns = gold. sklearn's `confusion_matrix` uses rows = true. Fawcett's Fig. 1 uses rows = hypothesized and columns = true. Always state the orientation.
- **Core per-class quantities:**
  - P_i = TP_i/(TP_i+FP_i), where the denominator is the number predicted as i ("bias").
  - R_i = TP_i/(TP_i+FN_i), where the denominator is gold support ("prevalence").
  - F1_i = 2P_iR_i/(P_i+R_i) = 2TP/(2TP+FP+FN).
  - Sources: opitz2019macrof1, opitz2024closerlook, sklearn-modeleval.
- **Accuracy** = Σ diag / N. In single-label multiclass it equals micro-P = micro-R = micro-F1 (opitz2024 §4.1, sklearn §3.4.4.9.2). "Micro-F1" therefore adds nothing beyond accuracy unless some labels are excluded, e.g. a "none"/fallback class removed via `labels` (sklearn).
- **Macro averaging:**
  - Macro-F1 has two definitions: averaged F1 (sklearn, recommended by Opitz & Burst) and the harmonic mean of macro-P and macro-R. They can differ by up to 0.5 and can rank systems differently (opitz2019). Always state which one is used.
  - Weighted-F1 weights classes by support. It is non-monotonic (opitz2024 §4.6) and can fall outside [P, R] (sklearn).
  - Macro-recall equals balanced accuracy (sklearn §3.4.4.4; opitz2024 §4.2). It is prevalence-invariant with a strict chance baseline of 1/n.
- **Zero and undefined cases:**
  - A class never predicted makes P undefined. A class absent from gold makes R undefined. A class with TP+FP+FN = 0 makes F undefined.
  - sklearn defaults to 0 with a warning. `zero_division=np.nan` excludes those classes from the macro mean (sklearn API).
  - Opitz sets them to 0.
  - Sakai's MAE^M drops empty gold classes (C⁺).
  - These choices change macro scores on small test sets, so report them.
- **Chance and majority baselines:**
  - Majority-class prediction gives accuracy equal to the majority prevalence, balanced accuracy 1/n (adjusted: 0), κ = 0, and MCC = 0 by the Chicco & Jurman limit convention (chicco2020; sklearn; sakai2021 for κ = 0 on constant baselines).
  - Uniform random prediction gives macro-recall = 1/n.
  - Macro-F1's chance level depends on whether the prediction distribution matches the prevalence (opitz2024 §4.4).
- **Small numerical example of conflicting conclusions** (derived, consistent with the definitions above):
  - Setup: binary data with 95 negatives and 5 positives, and an always-negative classifier.
  - Accuracy 0.95. Balanced accuracy 0.50.
  - Macro-F1 (averaged, zero_division=0) = (0.974 + 0)/2 = 0.487.
  - MCC = 0 under the Chicco convention, otherwise undefined.
- **Worked examples from Chicco & Jurman (Table 4):**
  - Use case A1 gives accuracy 0.90 and F1 0.95 but MCC −0.03.
  - Use case C2 gives accuracy 0.90 but F1 0.29 and MCC +0.31.
- **Competing views.** Chicco & Jurman advocate MCC as the binary summary. Opitz (2024) prefers macro-recall/κ for interpretability, notes MCC's non-monotonicity, and shows that metric choice changes SemEval rankings. sklearn notes that κ is designed for annotator agreement, not classifier-vs-truth.
- **Uncertainty.** Brodersen 2010 argues for posterior intervals (Beta) on accuracy and balanced accuracy rather than the SEM across folds, which can exceed 100%.

### 2. Binary detection (threshold-free and threshold choice)
- **Rates:**
  - TPR (sensitivity, recall) = TP/P.
  - FPR = FP/N = 1 − specificity.
  - FNR = 1 − TPR.
  - Precision (PPV) = TP/(TP+FP).
  - Sources: fawcett2006roc, manning ch8.
- **Prevalence dependence:**
  - TPR and FPR are column ratios, so ROC is invariant to class ratio.
  - Precision, accuracy and F mix columns, so they shift with prevalence (fawcett §4.2).
  - The PR baseline equals the prevalence π, and a random classifier's AUPRC ≈ π (saito2015; sklearn AP note; flach2015).
- **ROC-AUC:**
  - It equals P(score⁺ > score⁻), the Wilcoxon/Mann-Whitney statistic, and Gini = 2·AUC − 1 (fawcett §7).
  - Ties must be averaged. Order-dependent tie handling can bias AUC by up to nm/(2PN) (fawcett §5).
  - Hand & Till's OvO is the multiclass extension, and partial AUC is available via `max_fpr` (sklearn).
- **PR-AUC / AP:**
  - Linear interpolation of PR points is wrong and optimistic (davis2006 §4; flach2015 §2; sklearn).
  - AP as a step sum Σ(R_n − R_{n−1})P_n avoids interpolation (sklearn).
  - Different tools compute AUPRC differently and rank classifiers differently (chen2024, abstract).
- **Conflicting conclusions:**
  - Davis & Goadrich Fig. 7: AUC-ROC favors curve II (0.875 vs 0.813) while AUC-PR favors curve I (0.514 vs 0.038), with 20 positives and 2,000 negatives.
  - Saito & Rehmsmeier: the same ROC point (TPR 0.5, FPR 0.16) gives precision ≈0.76 at 1:1 but ≈0.24 at 1:10 (derived from their counts). Two classifiers with equal AUROC of 0.8 differ in early retrieval.
- **Contrarian evidence.** McDermott et al. 2024 (NeurIPS) prove that AUPRC is AUROC-like but weights FPR by the inverse firing rate, so it favors fixing high-score mistakes. They argue that it is "not generally superior" under imbalance and can amplify subgroup disparities (assuming calibration). Reconciliation: PR is informative when positive predictive value at the top matters (screening, retrieval). ROC suits context-free ranking comparison. Choose by deployment cost structure (mcdermott2024 Fig. 1; fawcett §6 iso-performance slope depends on priors and costs).
- **PRG.** Flach & Kull rescale PR by the always-positive baseline. precG = (prec − π)/((1−π)prec) and recG likewise. This restores linear interpolation and gives AUPRG an expected-F1 meaning.
- **Threshold choice:**
  - The optimal operating point depends on priors and costs via the iso-performance slope c(Y,n)p(n)/(c(N,p)p(p)) (fawcett §6).
  - For calibrated probabilities the F1-optimal threshold equals F1*/2, and an uninformative classifier maximizes F1 by predicting everything positive (lipton2014, abstract).
  - A threshold tuned on test data is optimistically biased. Thresholds should be frozen on dev data. This is general practice, not tied to a single source here.

### 3. Multilabel
- **Example-based metrics** (zhang2014 §II-B2):
  - Subset accuracy (exact set match) is strict for large q.
  - Hamming loss is the fraction of wrong instance-label pairs (sklearn: 1/(n·L) ΣΣ).
  - Example-based accuracy, precision, recall and F use |Y∩h|/|Y∪h|, /|h| and /|Y|.
- **Label-based metrics:** macro means per-label binary metrics, micro pools counts (zhang2014 §II-B3; sklearn "macro"/"micro"; sklearn "samples" = example-based). Accuracy_micro + Hamming loss = 1.
- **Ranking-based metrics:** one-error, coverage, ranking loss, average precision, and macro/micro AUC (zhang2014).
- **Optimizing one metric hurts another:** subset-accuracy-optimal and Hamming-optimal classifiers differ, so report several metrics (zhang2014 §II-B4).
- **Empty label sets.** If both Y_i and h(x_i) are empty, the example-based ratios are 0/0. sklearn sets P or R := 0 (configurable via zero_division) and notes that "conventions vary". Zhang & Zhou do not specify. A system that correctly predicts "no label" can therefore be scored 0 or 1 depending on convention. Report the convention, or treat "none" as an explicit label.
- **Thresholds:** h(x) = {y : f(x,y) > t(x)}, where t is constant or learned (stacking). Threshold choice drives all set-based metrics, while ranking metrics avoid it (zhang2014 §II-A3; sklearn ROC note).

### 4. Retrieval/ranking
- **P@k** = (#relevant in top k)/k. It needs no |Rel| but is unstable and averages poorly (manning). **R@k** = (#relevant in top k)/|Rel| and needs the full relevant set. **R-precision** = P@|Rel|.
- **AP and MAP:** AP = (1/|Rel|) Σ_{relevant d} Precision@rank(d). Unretrieved relevant documents contribute 0. MAP is the mean over queries, with equal weight per query (manning Eq. 8.8). MAP uses binary relevance.
- **MRR:** the mean over queries of 1/rank of the first correct answer, or 0 if none appears within the cut-off (voorhees1999). It takes only discrete values. It gives no credit for multiple answers or for abstaining when no answer exists.
- **nDCG:**
  - Original: graded gain, DCG with a log_b(i) discount from rank b, and an ideal vector from the full recall base (jarvelin2002).
  - Common variants: exponential gain (2^rel − 1)/log₂(1+m) (manning Eq. 8.9) or linear gain rel/log(1+r) (sklearn).
  - Values are comparable only with an identical gain/discount and an identical ideal (all judged relevant documents vs retrieved only).
  - BEIR uses nDCG@10 via trec_eval (thakur2021).
- **Ties:** discrete scores produce ties. Arbitrary tie-breaking (TREC's historical practice) can change system order. Tie-aware expectations over permutations are computable at no extra cost (mcsherry2008). sklearn ndcg_score averages ties by default, and Fawcett gives the ROC analog.
- **Pooling and incomplete judgments:**
  - Pooling judges the union of top-k results from participating systems. Unjudged documents are treated as non-relevant (manning §8.5; beir §6).
  - MAP, P@10 and R-prec degrade under incomplete judgments. bpref uses only judged documents and stays correlated with MAP (buckley2004).
  - BEIR case: dense retrievers had 14–32% unjudged top-10 hits vs 3–6% for lexical ones. Filling the holes raised ANCE from below BM25 to 6.7 points above it, a **ranking reversal caused by judgment incompleteness**.

### 5. Ordinal and regression metrics
- **Measurement scale:** for an ordinal scale, only monotone transforms are admissible, so median and percentiles are fine but the mean is not invariant (stevens1946 Table 1). This motivates Amigó's ordinal invariance (Property 1).
- **Exact and within-n accuracy:**
  - Exact accuracy ignores error magnitude.
  - "Accuracy at n" (Gaudette & Japkowicz 2009, per Amigó; primary unverified) relaxes accuracy by a margin.
  - Both are ordinal-invariant but not ordinal-monotonic (amigo2020 §4.2).
- **MAE and RMSE** treat classes as equidistant integers. MAE^µ ignores imbalance. Macro MAE^M averages per-gold-class MAE over non-empty classes (sakai2021 Eqs. 1–2). Sakai cites Chai & Draxler 2014 on RMSE vs MAE (not read).
- **Weighted κ:**
  - κ_w = 1 − Σ w_ij c_ij / Σ w_ij e_ij, with e_ij = c_i• c_•j / N (sakai2021 Eq. 5, following Cohen 1968).
  - Linear weights: w = |i−j|. Quadratic weights (QWK): w = (i−j)². sklearn's `weights='quadratic'` names this, but the formula was not printed on the page read.
  - κ is chance-corrected and equals 0 for any constant-class system. This makes it blind to differences among constant baselines (sakai2021).
  - Weighted κ is not ordinal-invariant (amigo2020).
  - sklearn notes that κ is an annotator-agreement measure.
- **Alternatives:** Krippendorff's α-ORD (Sakai) and CEM^ORD (Amigó), which avoid equidistance. Sakai recommends linear weighted κ as primary unless constant-class runs exist (then α-ORD), and reporting both. MAE^µ and accuracy produce rankings that diverge strongly from κ, MAE^M and macro-F1 (sakai2021 §5).
- **Conflict:** Amigó requires ordinal invariance and treats MAE and κ as violating it. Sakai considers equidistance a non-problem in practice.

### Cross-cutting pitfalls
1. Two "macro-F1"s exist.
2. Zero-division conventions differ.
3. Weighted-F1 is near-micro and non-monotonic.
4. ROC vs PR conclusions can reverse under skew. Which to prefer is contested (Saito vs McDermott).
5. AUPRC values depend on the tool and interpolation.
6. NDCG gain and discount variants differ.
7. Tie handling can reorder systems.
8. Incomplete pooled judgments penalize novel systems.
9. MRR gives no credit for correct abstention.
10. κ is 0 for constant predictors.
11. Equidistance assumptions are implicit in MAE and linear/quadratic κ.
