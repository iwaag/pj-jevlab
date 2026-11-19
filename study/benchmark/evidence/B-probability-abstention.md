# Sources: Cluster B — probabilistic prediction, calibration, abstention / selective prediction, OOD detection, cost-sensitive decisions

Accessed date for all entries: 2026-10-02.
Verification method: every arXiv source was located through the export.arxiv.org API, which confirmed title, authors and version dates. The PDF was then downloaded and converted with `pdftotext -layout`, and the cited sections were read in that raw text, not in a model summary. Non-arXiv sources were checked through Crossref or OpenAlex metadata, author-hosted PDFs, or PMC HTML, as noted per entry. Formulas below are transcribed from the raw extracted text. Where pdftotext mangled symbols, the reading was cross-checked against the rendered page or the surrounding prose (for Elkan 2001 the rendered PDF page image was read).

> Evidence notes for cluster B of [study/benchmark](../README.md), compiled 2026-10-02 in step2 of benchmark/p1 by a research subagent and reviewed by the lead session. The search log and gaps for this cluster are in [search-log.md](../search-log.md). Verification levels are per entry; claims beyond the stated level must not be attributed to a source.

## Source list

### gneiting2007proper
- Title: Strictly Proper Scoring Rules, Prediction, and Estimation
- Authors / organization: Tilmann Gneiting, Adrian E. Raftery (Univ. of Washington)
- Date: JASA 102(477):359–378, March 2007
- URL / DOI: doi:10.1198/016214506000001437; author PDF https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf
- Type: method paper / review (theory)
- Verification: full-text (author-hosted published PDF, 20 pp.; read Abstract, §1, §2.1 Thm 1, §3 Examples 1–4, §3.2 Schervish representation Eq. 14–15)
- Supports:
  - Convention: positively oriented scores, S(P, x) = reward. "A scoring rule is proper if the forecaster maximizes the expected score for an observation drawn from the distribution F if he or she issues the probabilistic forecast F, rather than G ≠ F. It is strictly proper if the maximum is unique." (Abstract)
  - Goal of probabilistic forecasting: "maximize the sharpness of the predictive distributions subject to calibration". Calibration is a joint property of forecasts and observations. Sharpness is a property of the forecasts only. (§1)
  - Thm 1 (Savage/McCarthy-type characterisation): a regular scoring rule is proper iff S(P, ω) = G(P) − ∫G*(P, ω)dP(ω) + G*(P, ω) for a convex G with subtangent G*. Strictly proper iff G is strictly convex. (§2.1, Eq. 5)
  - Example 1, quadratic/Brier score (categorical, m classes): S(p, i) = −Σ_j (δ_ij − p_j)^2 = 2p_i − Σ_j p_j^2 − 1. Its Bregman divergence is the squared Euclidean distance Σ_j (p_j − q_j)^2. Attributed to Brier (1950). (§3)
  - Example 3, logarithmic score: S(p, i) = log p_i, with KL divergence d(p,q) = Σ q_j log(q_j/p_j). The paper notes the log score "has been criticized for its unboundedness" (Selten 1998). (§3)
  - Example 4, zero–one score (reward 1/#modes if the outcome is a mode) is proper but not strictly proper: "the entropy function is neither differentiable nor strictly convex". So accuracy-type scoring does not elicit honest probabilities. (§3)
  - Schervish representation: every left-continuous bounded proper binary scoring rule is a mixture of cost-weighted asymmetric zero–one scores S_c(p,1) = (1−c)1{p>c}, S_c(p,0) = c·1{p≤c}, with a non-negative mixing measure ν(dc) over cost–loss ratios c. The Brier and log scores correspond to particular ν. (§3.2, Eq. 14–15) This links proper scores to expected decision cost averaged over thresholds.
  - Bernardo (1979): every proper local scoring rule is equivalent to the log score. (§4.1, cited)
- Caveats: the paper uses positive orientation (higher is better). Bröcker and most ML papers use loss orientation. The author PDF is the published version.

### brier1950verification
- Title: Verification of Forecasts Expressed in Terms of Probability
- Authors: Glenn W. Brier
- Date: Monthly Weather Review 78(1):1–3, Jan 1950
- DOI: 10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2
- Type: method paper (original)
- Verification: unverified (metadata only via Crossref/OpenAlex. AMS journal site returned HTTP 403 to curl and WebFetch. OpenAlex has no abstract.)
- Supports: bibliographic existence only. For the formula, cite gneiting2007proper Example 1 and brocker2009 Table 1.
- Caveats: Brier's original multi-category form (sum over classes, range 0–2) and the binary form (p − y)^2 (range 0–1) are both called "Brier score". This is visible in gneiting2007proper (§3 Ex. 1, multi-class form) vs brocker2012 (binary S(p,k) = (p_1 − k)^2 plus a K-class generalisation) and kadavath2022 (binary chance level 0.25). Implementations must state which form they use.

### murphy1973partition
- Title: A New Vector Partition of the Probability Score
- Authors: Allan H. Murphy
- Date: Journal of Applied Meteorology 12(4):595–600, June 1973
- DOI: 10.1175/1520-0450(1973)012<0595:ANVPOT>2.0.CO;2
- Type: method paper
- Verification: abstract (via OpenAlex abstract index. The AMS PDF returned 403.)
- Supports (abstract only): the new partition of the probability (Brier) score has three terms: "1) a measure of the uncertainty inherent in the events … (namely, the PS for the sample relative frequencies); 2) a measure of the reliability of the forecasts; and 3) a new measure of the resolution of the forecasts."
- Caveats: the explicit formula below is taken from brocker2009 (full-text) and brocker2012, not from Murphy directly.

### brocker2009decomposition
- Title: Reliability, Sufficiency, and the Decomposition of Proper Scores
- Authors: Jochen Bröcker
- Date: arXiv 0806.0813 (v2, Dec 2008). Published in Q. J. R. Meteorol. Soc. 2009 (journal version not fetched).
- URL: https://arxiv.org/abs/0806.0813
- Type: method paper (theory)
- Verification: full-text (§2 Eq. 2–13, Table 1)
- Supports:
  - Loss orientation. Scoring function s(p,q) = Σ_k S(p,k) q_k. Divergence d(p,q) = s(p,q) − s(q,q) ≥ 0 (proper), with equality only at p = q (strictly proper). Entropy e(p) = s(p,p). (Eq. 2–4)
  - Table 1: Brier S(p,y) = |y − p|^2, d = |p − q|^2, e(p) = p(1−p) (binary). Ignorance (log) S = −log p_y, d = KL, e = Shannon entropy.
  - General decomposition for any strictly proper score, with γ the forecast, π^γ = P(Y | γ) and π̄ = E π^γ (climatology): E[S(γ,Y)] = e(π̄) − E d(π̄, π^γ) + E d(γ, π^γ), i.e. UNCERTAINTY − RESOLUTION + RELIABILITY. (Eq. 13) For the Brier score this reduces to Murphy's decomposition.
  - Both better reliability and better resolution lower (improve) the expected score.
- Caveats: this is the population (expectation) decomposition. For the empirical version see brocker2012.

### brocker2012empirical
- Title: Estimating reliability and resolution of probability forecasts through decomposition of the empirical score
- Authors: Jochen Bröcker
- Date: Climate Dynamics 2012 (author's corrected version dated 8 Dec 2011)
- URL: http://www.personal.reading.ac.uk/~pt904209/publications/decomp_interp_clim_dyn_2011.pdf
- Type: method paper
- Verification: full-text (author-hosted corrected version. Read Abstract, §1, §2.3 Eq. 9–14, §3.2 Eq. 23–25)
- Supports:
  - The empirical score over an archive decomposes exactly as (1/N)Σ_n S = Σ_d e(o^(d)) r_d + Σ_d d(γ^(d), o^(d)) r_d, and Σ_d e(o^(d)) r_d = e(ō) − Σ_d d(ō, o^(d)) r_d. Here d indexes the distinct forecast values γ^(d), o^(d) is the observed frequency among cases with that forecast, and r_d = N_•d/N. (Eq. 13–14)
  - Abstract: the empirical decomposition "provides a too optimistic estimate of the potential score … a forecast assessment based solely on the empirical resolution and reliability terms will be misleading". §1: "in truth the forecast tends to be more reliable than what the empirical reliability term suggests".
  - Brier bias terms: E of the empirical reliability term = true reliability + (1/N)Σ_d ν_d e(π^(d)), with ν_d = 1 − (1 − ρ_d)^N. (Eq. 25)
  - The author's correction (§3.2) says the earlier claim that empirical resolution always overestimates true resolution "is wrong in general" for Brier, although it holds for many configurations.
- Caveats: the decomposition is exact only when forecasts are grouped by identical values. Binning continuous forecasts adds within-bin terms (not covered here).

### guo2017calibration
- Title: On Calibration of Modern Neural Networks
- Authors: Chuan Guo, Geoff Pleiss, Yu Sun, Kilian Q. Weinberger
- Date: ICML 2017. arXiv 1706.04599 (v2 Aug 2017)
- URL: https://arxiv.org/abs/1706.04599
- Type: empirical study + method paper
- Verification: full-text (§2 Eq. 1–5, §4.2 temperature scaling, Table 1, §S2)
- Supports:
  - Perfect (top-label) calibration: P(Ŷ = Y | P̂ = p) = p, ∀p ∈ [0,1]. (Eq. 1)
  - Reliability diagram: M equal-width bins I_m = ((m−1)/M, m/M]. acc(B_m) and conf(B_m) are per-bin accuracy and mean confidence.
  - ECE = Σ_{m=1}^M (|B_m|/n) |acc(B_m) − conf(B_m)|. (Eq. 3) MCE = max_m |acc(B_m) − conf(B_m)|. (Eq. 5) NLL = −Σ_i log π̂(y_i | x_i).
  - "Reliability diagrams do not display the proportion of samples in a given bin." (§2)
  - Experiments report ECE with M = 15 bins (Table 1).
  - NLL can overfit while 0/1 error keeps improving, which yields miscalibration. "NLL can be used to indirectly measure model calibration." (§3)
  - Platt scaling: q̂_i = σ(a z_i + b), with a and b fit by NLL on a validation set. Temperature scaling: q̂_i = max_k σ_SM(z_i/T)^(k), a single T > 0 fit by NLL on validation. It "does not change the maximum of the softmax function", so accuracy is unchanged. (§4.1–4.2) Temperature scaling was best on most of their datasets.
- Caveats: ECE as defined is top-label only and uses equal-width bins (see nixon2019, kull2019, kumar2019, roelofs2022). Calibration maps must be fit on held-out data, not the test set.

### naeini2015bbq
- Title: Obtaining Well Calibrated Probabilities Using Bayesian Binning
- Authors: Mahdi Pakdaman Naeini, Gregory F. Cooper, Milos Hauskrecht
- Date: AAAI 2015
- DOI / URL: 10.1609/aaai.v29i1.9602; PMC4410090 https://pmc.ncbi.nlm.nih.gov/articles/PMC4410090/
- Type: method paper
- Verification: full-text (PMC HTML. Read the "calibration measures" paragraph and the abstract.)
- Supports: binary ECE = Σ_{i=1}^K P(i)|o_i − e_i| and MCE = max_i |o_i − e_i|. o_i is the true fraction of positives in bin i, e_i the mean calibrated probability in bin i, and P(i) the fraction of instances in bin i. "The predictions are sorted and partitioned into K fixed number of bins (K = 10 in our experiments)." Proposes BBQ.
- Caveats: the PMC text ("sorted and partitioned into K fixed number of bins") reads like equal-frequency binning, while guo2017 describes Naeini's ECE as using equally spaced bins. This is an example of how "ECE" bin conventions drift between papers.

### nixon2019measuring
- Title: Measuring Calibration in Deep Learning
- Authors: Jeremy Nixon, Mike Dusenberry, Ghassen Jerfel, Timothy Nguyen, Jeremiah Liu, Linchuan Zhang, Dustin Tran (Google)
- Date: arXiv 1904.01685 (v1 Apr 2019, v2 Aug 2020). CVPR 2019 Workshops.
- Type: empirical study
- Verification: full-text (§3.1–3.4, §4.1–4.5, Tables)
- Supports:
  - ECE pathologies: (§3.1) it uses only the predicted-class probability. (§3.2) fixed bins plus sharp predictions mean "only a few bins contribute the most to ECE". (§3.3) the number of bins is a bias–variance tradeoff. (§3.4) "you can get near 0 calibration error due to overconfident and underconfident predictions overlapping in the same bin".
  - SCE = (1/K) Σ_k Σ_b (n_bk/N)|acc(b,k) − conf(b,k)|, i.e. classwise and all probabilities. ACE = (1/(KR)) Σ_k Σ_r |acc(r,k) − conf(r,k)|, with adaptive (equal-count) ranges. Thresholding of tiny probabilities is also discussed. (§4)
  - Abstract: rank ordering of recalibration methods is "drastically impacted by the choice of calibration measure". Recommends class conditioning, adaptive binning and the L2 norm.
  - Fig. 1: the temperature that minimizes calibration error is not the same one that minimizes cross-entropy.
- Caveats: empirical scope is image classification (MNIST to ImageNet).

### kumar2019verified
- Title: Verified Uncertainty Calibration
- Authors: Ananya Kumar, Percy Liang, Tengyu Ma (Stanford)
- Date: NeurIPS 2019. arXiv 1909.10155 (v2 Jan 2020)
- Type: method paper (theory + experiments)
- Verification: full-text (§2 Def. 2.1–2.4, §3 Def. 3.1, Ex. 3.2, Prop. 3.3, §5 Def. 5.1–5.2, Thm 5.3–5.4)
- Supports:
  - Calibration alone is not sufficient: a constant 0.5 predictor on a 50/50 dataset is calibrated but useless. MSE (Brier) = squared calibration error + "sharpness" term. (§2.1)
  - Top-label calibration error TCE(f) = (E[(P(Y = argmax f(X) | max f(X)) − max f(X))^2])^{1/2}. Marginal (classwise) calibration error = (Σ_k w_k E[(f(X)_k − P(Y=k | f(X)_k))^2])^{1/2}. (Eq. 2–3) Temperature scaling can have better top-label calibration but worse marginal calibration than vector scaling.
  - For continuous-output models, binned evaluation underestimates calibration error. CE(f_B) ≤ CE(f) (Prop. 3.3, by Jensen). There exists a distribution with CE(f_B) = 0 but CE(f) ≥ 0.49 (Ex. 3.2). Measured binned CE increases with more bins (Fig. 2). So Platt and temperature scaling are "less calibrated than reported".
  - For a model that outputs B discrete values, the plug-in estimator Ê²_pl = Σ_s p̂_s(s − ŷ_s)² is biased upward (each term has bias about 1/n, total about B/n). The debiased estimator Ê²_db = Σ_s p̂_s[(s − ŷ_s)² − ŷ_s(1−ŷ_s)/(p̂_s n − 1)] needs O(√B/ε²) samples, against O(B/ε²) for plug-in. (Def. 5.1–5.2, Thm 5.3–5.4)
  - Proposes the scaling-binning calibrator, whose calibration can be verified.
- Caveats: there are two opposite biases. Binning a continuous model underestimates its true CE. The finite-sample plug-in estimate of a binned CE overestimates it, most of all for well-calibrated models (see roelofs2022).

### kull2019dirichlet
- Title: Beyond temperature scaling: Obtaining well-calibrated multiclass probabilities with Dirichlet calibration
- Authors: Meelis Kull, Miquel Perello-Nieto, Markus Kängsepp, Telmo Silva Filho, Hao Song, Peter Flach
- Date: NeurIPS 2019. arXiv 1910.12656
- Type: method paper
- Verification: full-text (§2 Def. 1–3, classwise-ECE definition, Fig. 1)
- Supports:
  - Def. 1 (multiclass / canonical): P(Y = i | p̂(X) = q) = q_i for all i.
  - Def. 2 (classwise): P(Y = i | p̂_i(X) = q_i) = q_i.
  - Def. 3 (confidence): P(Y = argmax p̂(X) | max p̂(X) = c) = c. Defs. 2 and 3 are weaker, necessary conditions for Def. 1.
  - classwise-ECE = (1/k) Σ_j Σ_i (|B_{i,j}|/n) |y_j(B_{i,j}) − p̂_j(B_{i,j})|.
  - Example (CIFAR-10 wide ResNet): after temperature scaling, conf-ECE is 0.0078 (nearly confidence-calibrated), yet it is "far from being classwise-calibrated" (class-2 reliability diagram).
- Caveats: none beyond the binning issues.

### vaicenavicius2019evaluating
- Title: Evaluating model calibration in classification
- Authors: Juozas Vaicenavicius, David Widmann, Carl Andersson, Fredrik Lindsten, Jacob Roll, Thomas B. Schön
- Date: AISTATS 2019. arXiv 1902.06977
- Type: method paper
- Verification: full-text (§1–2 Eq. 1–2. Consistency resampling and hypothesis testing paragraphs.)
- Supports:
  - Full reliability: P[Y ∈ · | g(X)] = g(X) (Eq. 1). The ML community often calls a model "perfectly calibrated" under the much weaker condition P[Y = argmax g(X) | max g(X)] = max g(X) (Eq. 2), "possibly giving rise to some confusion".
  - Example: two outputs (0.9, 0.1, 0) and (0.9, 0, 0.1) look identical to top-label evaluation.
  - Proposes consistency resampling (Bröcker & Smith 2007) to obtain p-values for a test of perfect calibration. The ECE estimator is biased, so the estimate alone cannot be read as evidence of miscalibration.
- Caveats: none noted.

### roelofs2022mitigating
- Title: Mitigating Bias in Calibration Error Estimation
- Authors: Rebecca Roelofs, Nicholas Cain, Jonathon Shlens, Michael C. Mozer (Google)
- Date: AISTATS 2022. arXiv 2012.08668 (v3 Feb 2022)
- Type: method paper / empirical study
- Verification: full-text (Abstract, §1, Fig. 1)
- Supports:
  - ECE_bin with 15 equal-width bins is the standard estimator (Guo/Naeini). Its statistical bias (expected ECE_bin − true calibration error) "is most severe for perfectly calibrated models". The Fig. 1 simulation from a perfectly calibrated model gives non-zero ECE_bin.
  - Equal-mass binning has lower bias than equal-width.
  - Recommended estimators: ECE_debias (Bröcker 2012; Ferro & Fricker 2012) and ECE_sweep (equal-mass bins, with the number of bins chosen as large as possible while the bin-accuracy curve stays monotone). ECE_debias does better for perfectly calibrated models, ECE_sweep for miscalibrated ones.
- Caveats: the analysis is about bias, not variance (stated §1/§4).

### blasiok2023unifying
- Title: A Unifying Theory of Distance from Calibration
- Authors: Jarosław Błasiok, Parikshit Gopalan, Lunjia Hu, Preetum Nakkiran
- Date: STOC 2023. arXiv 2211.16886 (v2 Mar 2023)
- Type: method paper (theory)
- Verification: full-text (Abstract, §4.3 Lemma 4.7–4.8)
- Supports: population ECE(f) = E[|E[y|f] − f|]. ECE "does not satisfy robust completeness, and is discontinuous at 0". Example (Lemma 4.8): X = {0,1} uniform, true f*(0) = 0, f*(1) = 1. The predictor f_ε = 1/2 ∓ ε is within ε of the calibrated constant 1/2, yet ECE(f_ε) = 1/2 − ε, while ECE(1/2) = 0. Smooth calibration, interval calibration and Laplace-kernel calibration are "consistent" calibration measures (polynomially related to the ℓ1 distance to the nearest perfectly calibrated predictor).
- Caveats: theoretical, binary setting.

### blasiok2023smoothece
- Title: Smooth ECE: Principled Reliability Diagrams via Kernel Smoothing
- Authors: Jarosław Błasiok, Preetum Nakkiran (Apple)
- Date: arXiv 2309.12236 (Sep 2023). ICLR 2024.
- Type: method paper
- Verification: full-text (abstract, Fig. 1)
- Supports: smooth the observations with a kernel, then compute ECE of the smoothed function (SmoothECE). With a suitable bandwidth this is a consistent calibration measure. The reliability diagram visually encodes smECE. Hyperparameter-free package `relplot`. Fig. 1 example: ECE_15 = 0.161 vs smECE = 0.138 on the same predictions.
- Caveats: newer and less established in practice than binned ECE.

### platt1999probabilistic
- Title: Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods
- Authors: John C. Platt
- Date: in Advances in Large Margin Classifiers, MIT Press, 1999, pp. 61–74
- Type: method paper
- Verification: unverified (book chapter. Only the ResearchGate and bibsonomy listings were found and not accessed.) The method description used here comes from guo2017calibration §4.1 (full text).
- Supports (via guo2017): sigmoid recalibration σ(a z + b) fit by NLL on held-out data.

### kadavath2022know
- Title: Language Models (Mostly) Know What They Know
- Authors: Saurav Kadavath et al. (Anthropic)
- Date: arXiv 2207.05221 (v4 Nov 2022)
- Type: empirical study
- Verification: full-text (Abstract, §1.1 Contributions, Glossary "Observables and Metrics", §3.3, Fig. 9 caption)
- Supports:
  - Large models are well calibrated on multiple-choice questions "when they are provided in the right format" (visible lettered options). Calibration improves with model size and with few-shot prompting.
  - Replacing an option with "none of the above" "reduces accuracy and calibration significantly".
  - RLHF policies "naively seem miscalibrated, but with a simple temperature adjustment" (same T = 2.5 for all evaluations) "they become fairly well-calibrated" (§3.3, Fig. 9).
  - P(True) is the model's probability that its own sampled answer is correct. P(IK) is the probability that it "knows" the answer, trained with a classifier head, and it "struggle[s] with calibration of P(IK) on new tasks".
  - Metric conventions (Glossary): ECE uses 10 equal-count bins over the top prediction. RMS calibration error is also reported as "better motivated theoretically". AUROC "captures discriminative power but is indifferent to calibration". Brier chance level on binary tasks is 0.25, and Brier "combine[s] the discriminative power … with calibration".
  - Few-shot self-evaluation mainly improves calibration rather than AUROC.
- Caveats: results come from the authors' own models (vendor claim). The ECE convention (equal-count, 10 bins) differs from Guo (equal-width, 15).

### tian2023justask
- Title: Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback
- Authors: Katherine Tian, Eric Mitchell, Allan Zhou, Archit Sharma, Rafael Rafailov, Huaxiu Yao, Chelsea Finn, Christopher D. Manning
- Date: EMNLP 2023. arXiv 2305.14975 (v2 Oct 2023)
- Type: empirical study
- Verification: full-text (Abstract, §2–3 metrics paragraph, footnote 5, Tables 1–4)
- Supports:
  - For RLHF LMs (gpt-3.5-turbo, gpt-4, claude-1/2, Llama-2-70B-chat), "verbalized confidences emitted as output tokens are typically better-calibrated than the model's conditional probabilities" on TriviaQA, SciQ and TruthfulQA, "often reducing the expected calibration error by a relative 50%".
  - Metrics: ECE, ECE-t (after temperature scaling p̃_i ∝ p_i^β fit by NLL), BS-t (Brier on temperature-scaled confidences), and AUC of selective accuracy vs coverage (Geifman & El-Yaniv).
  - Footnote 5: "For binary classification, a system that guesses randomly and outputs 50% confidence each time has perfect ECE." ECE "completely fails to capture the confidences' discriminative power."
  - Correctness of free-form answers was judged by GPT-4 or GPT-3.5 for semantic equivalence, to avoid exact-match false negatives.
- Caveats: their ECE is described as the "average (squared) error" per bin, which differs from Guo's absolute-error ECE. Temperature-scaled metrics (ECE-t, BS-t) are fit on the evaluation data ("to minimize NLL on the data"), so they measure post-hoc calibratability rather than out-of-the-box calibration. Correctness labels depend on an LLM judge.

### openai2023gpt4
- Title: GPT-4 Technical Report
- Authors: OpenAI
- Date: arXiv 2303.08774 (v1 Mar 2023, v6 Mar 2024)
- Type: vendor/benchmark-author claim
- Verification: full-text (§5 Limitations, Figure 8 and caption)
- Supports (verified): "the pre-trained model is highly calibrated (its predicted confidence in an answer generally matches the probability of being correct). However, after the post-training process, the calibration is reduced (Figure 8)." Figure 8: calibration on "a subset of the MMLU dataset". The x-axis bins are the model's logprob confidence in each A/B/C/D choice. Panel ECE is 0.007 (pre-train) vs 0.074 (ppo). "The post-training hurts calibration significantly."
- Caveats: the MMLU subset, binning and ECE details are not given, and the result cannot be reproduced externally. kadavath2022 (§3.3) reports that RLHF miscalibration was largely fixed by a single temperature. kalai2025why reproduces this figure.

### jiang2021know
- Title: How Can We Know When Language Models Know? On the Calibration of Language Models for Question Answering
- Authors: Zhengbao Jiang, Jun Araki, Haibo Ding, Graham Neubig
- Date: TACL 2021. arXiv 2012.00955 (v2 May 2021)
- Type: empirical study + method paper
- Verification: full-text (Abstract, §2 Eq. 1, §3 ECE)
- Supports:
  - T5, BART and GPT-2 on QA: are their probabilities well calibrated? "the answer is a relatively emphatic no". Calibration is improved by fine-tuning, post-hoc probability modification (e.g. temperature), or adjusting outputs/inputs (paraphrasing).
  - Candidate-normalized probability for multiple choice: P_N(Ŷ|X) = P_LM(Ŷ|X) / Σ_{Y'∈I(X)} P_LM(Y'|X). (Eq. 1) For extractive QA, a manageable candidate set is enumerated. Free-form abstractive QA was considered (footnote 2) but the study focuses on candidate-constrained formats.
- Caveats: calibration of a generative LM is defined relative to a chosen candidate set. Renormalizing over candidates changes the probabilities.

### chow1970optimum
- Title: On optimum recognition error and reject tradeoff
- Authors: C. K. Chow
- Date: IEEE Trans. Information Theory 16(1):41–46, Jan 1970
- DOI: 10.1109/TIT.1970.1054406
- Type: method paper
- Verification: abstract (OpenAlex abstract index. IEEE page not retrievable.)
- Supports (abstract): describes "an optimum rejection rule" and "a general relation between the error and reject probabilities". "The error rate can be directly evaluated from the reject function."
- Caveats: the familiar form (reject iff max_k P(k|x) < 1 − c_r for rejection cost c_r relative to unit error cost) is a standard derivation (see Topic notes), not verified from Chow's text.

### elyaniv2010foundations
- Title: On the Foundations of Noise-free Selective Classification
- Authors: Ran El-Yaniv, Yair Wiener
- Date: JMLR 11:1605–1641, 2010
- URL: https://www.jmlr.org/papers/volume11/el-yaniv10a/el-yaniv10a.pdf
- Type: method paper (theory)
- Verification: abstract + §1 intro (full text downloaded. Only the abstract and introduction were read.)
- Supports: "selective classification … 'classification with a reject option.' The essence … is to trade-off classifier coverage for higher accuracy. We term this trade-off the risk-coverage (RC) trade-off." Traces the idea to Chow (1957, 1970).
- Caveats: the noise-free (realizable) setting is a theoretical idealization.

### geifman2017selective
- Title: Selective Classification for Deep Neural Networks
- Authors: Yonatan Geifman, Ran El-Yaniv
- Date: NeurIPS 2017. arXiv 1705.08500
- Type: method paper
- Verification: full-text (§2 Eq. 1–2, §3 Eq. 3, §4 SR/MC-dropout)
- Supports:
  - Selective classifier (f, g): output f(x) if g(x) = 1, "don't know" if g(x) = 0. Coverage φ(f,g) = E_P[g(x)]. Selective risk R(f,g) = E_P[ℓ(f(x),y) g(x)] / φ(f,g). (Eq. 1) The risk–coverage curve plots risk as a function of coverage.
  - Threshold rule g_θ(x) = 1[κ_f(x) ≥ θ], where κ is a confidence-rate function used only for ranking. (Eq. 3)
  - SGR algorithm: for a target risk r* and confidence δ, pick θ so that Pr{R(f,g) > r*} < δ, maximizing coverage (binomial tail bound on held-out data).
  - Softmax response (SR) κ = max_j f(x|j) and MC-dropout as confidence functions. On ImageNet, a "2% top-5 error … with probability 99.9%, and almost 60% test coverage" (abstract).
- Caveats: the guarantee is i.i.d.-based and does not hold under shift (see kamath2020).

### geifman2019biasreduced
- Title: Bias-Reduced Uncertainty Estimation for Deep Neural Classifiers
- Authors: Yonatan Geifman, Guy Uziel, Ran El-Yaniv
- Date: ICLR 2019. arXiv 1805.08206
- Type: method paper
- Verification: full-text (§2 AURC, Eq. 3, E-AURC definition, Fig. 1)
- Supports:
  - AURC(κ, f | V_n) = (1/n) Σ_{θ∈Θ} r̂(f, g_θ | V_n): the area under the empirical RC curve over all thresholds at observed κ values.
  - The optimal-in-hindsight κ* ranks all errors below all correct predictions. AURC(κ*) = (1/n) Σ_{i=1}^{r̂n} i/(n(1 − r̂) + i) ≈ r̂ + (1 − r̂) ln(1 − r̂).
  - E-AURC = AURC(κ) − AURC(κ*). Example: CIFAR-100 with r̂ ≈ 0.29 at full coverage, about 0.06 at coverage 0.5, and AURC(κ*) = 0.04802.
- Caveats: AURC depends on the base error rate r̂, so E-AURC subtracts the oracle value. The text says "normalize by AURC(κ*)" but the formula is a difference. AURC mixes classifier accuracy with ranking quality.

### kamath2020selective
- Title: Selective Question Answering under Domain Shift
- Authors: Amita Kamath, Robin Jia, Percy Liang
- Date: ACL 2020. arXiv 2006.09462
- Type: method paper / empirical study
- Verification: full-text (Abstract, §1, §2.3, §3.1)
- Supports:
  - Setting: test on a mixture of in-domain (SQuAD) and unknown OOD data. Abstain when confidence c < γ.
  - Metrics: the risk–coverage curve, its AUC, and the "maximum possible coverage for a desired risk level" (e.g. coverage at 80% accuracy).
  - Selective prediction metrics "depend only on relative confidences", whereas calibration error "depends on the absolute confidence scores". (§2.3)
  - MaxProb (softmax) abstention fares poorly because models are overconfident on OOD inputs. A trained calibrator (on a mixture of in-domain and known-OOD data) reaches 56.1% coverage at 80% accuracy, against 48.2% for MaxProb.
- Caveats: the calibrator needs some known-OOD data, and results are QA-specific.

### rajpurkar2018squad2
- Title: Know What You Don't Know: Unanswerable Questions for SQuAD
- Authors: Pranav Rajpurkar, Robin Jia, Percy Liang
- Date: ACL 2018. arXiv 1806.03822
- Type: benchmark/dataset paper
- Verification: full-text (Abstract, §1, §5.1–5.2, footnote 3)
- Supports: SQuAD 2.0 adds 53,775 adversarially written unanswerable questions. Models abstain when P(unanswerable) exceeds a threshold tuned on the dev set to maximize F1. Scoring: "For negative examples, abstaining receives a score of 1, and any other response gets 0, for both exact match and F1" (fn. 3). The best model scored 66.3 F1 against human 89.5. "a baseline that always abstains gets 48.9 test F1".
- Caveats: this is answerability (a property of the question and context), not model-knowledge abstention. The always-abstain baseline score depends on the share of unanswerable items.

### wen2024knowyourlimits
- Title: Know Your Limits: A Survey of Abstention in Large Language Models
- Authors: Bingbing Wen, Jihan Yao, Shangbin Feng, Chenjun Xu, Yulia Tsvetkov, Bill Howe, Lucy Lu Wang
- Date: arXiv 2407.18418 (v1 Jul 2024, v3 Feb 2025). TACL 2025 (journal version not fetched)
- Type: position/survey
- Verification: full-text (Fig. 1 framework, §4.2 metrics, Table 1)
- Supports:
  - Three perspectives: query answerability a(x), model confidence c(x,y), and human values h(x), h(x,y). Abstain if any falls below threshold.
  - Abstention confusion matrix (Table 1). Ground truth "no abstention" gives N1 correct, N2 incorrect, N3 abstained. Ground truth "abstention" gives N4 answered, N5 abstained.
  - Formulas: Coverage = (N1+N2+N4)/N. Abstention rate = (N3+N5)/N. Abstention accuracy = (N1+N5)/N. Precision_abs = N5/(N3+N5). Recall_abs = N5/(N2+N4+N5). Reliable accuracy = N1/(N1+N2+N4). Effective reliability = (N1 − N2 − N4)/N. Also Coverage@Acc, AURCC, AUACC and AUROC.
  - Recommendation: "No single metric captures all aspects". Report task performance, abstention P/R/F1, coverage and accuracy–coverage trade-off together.
- Caveats: survey. Recall_abs counts N2 (wrong answers on answerable questions) as "should have abstained", which conflates model-knowledge abstention with query answerability.

### kirichenko2025abstentionbench
- Title: AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions
- Authors: Polina Kirichenko, Mark Ibrahim, Kamalika Chaudhuri, Samuel J. Bell (Meta)
- Date: arXiv 2506.09038 (Jun 2025)
- Type: benchmark/dataset paper (contains benchmark-author claims)
- Verification: full-text (Abstract, §1, §3.4)
- Supports: 20 datasets covering unknown answers, underspecification, false premises, subjective and outdated questions. 20 frontier LLMs evaluated. "scaling models is of little use". "reasoning fine-tuning degrades abstention (by 24% on average)". A crafted system prompt helps but does not resolve the problem. Abstention is detected by an LLM judge (Llama 3.1 8B Instruct), with 88% accuracy on a manually annotated sample. The headline metric is abstention recall, because precision was generally high.
- Caveats: the judge error rate (12% disagreement) is comparable to some reported effects. These are benchmark-author claims.

### feng2024abstain
- Title: Don't Hallucinate, Abstain: Identifying LLM Knowledge Gaps via Multi-LLM Collaboration
- Authors: Shangbin Feng, Weijia Shi, Yike Wang, Wenxuan Ding, Vidhisha Balachandran, Yulia Tsvetkov
- Date: ACL 2024. arXiv 2402.00367 (v2 Jul 2024)
- Type: method paper
- Verification: full-text (Abstract, §2.1 calibration-based baselines)
- Supports: baselines include token-probability thresholding, temperature scaling (τ fit on a held-out set H by cross-entropy, then a threshold), verbalized-confidence thresholds and self-consistency thresholds. They note "over-reliance on held-out sets" as a weakness. Proposed cooperative and competitive multi-LLM probing gives "up to 19.3% improvements on abstain accuracy". Defines abstain accuracy / precision / recall / F1, reliable accuracy, effective reliability and abstain ECE (formulas transcribed in wen2024).
- Caveats: method paper reporting its own gains.

### angelopoulos2021gentle
- Title: A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification
- Authors: Anastasios N. Angelopoulos, Stephen Bates
- Date: arXiv 2107.07511 (v1 Jul 2021, v6 Dec 2022). Foundations and Trends in ML 2023.
- Type: textbook/tutorial
- Verification: full-text (§1 Eq. 1, §1 general recipe Eq. 2, Thm 1, §3 conditional coverage)
- Supports:
  - Split conformal classification: calibration scores s_i = 1 − f̂(X_i)_{Y_i}. q̂ = the ⌈(n+1)(1−α)⌉/n empirical quantile. C(x) = {y : f̂(x)_y ≥ 1 − q̂}.
  - Marginal coverage: 1 − α ≤ P(Y_test ∈ C(X_test)) ≤ 1 − α + 1/(n+1). The upper bound needs tie-breaking. Thm 1 assumes i.i.d. (exchangeable) calibration and test data.
  - "although the guarantee always holds, the usefulness of the prediction sets is primarily determined by the score function". Random scores give valid but useless sets.
  - Marginal ≠ conditional coverage, and conditional coverage is "impossible to achieve" in the most general case (§3).
  - Covers selective classification (§5.5) and Learn-then-Test risk control.
- Caveats: the guarantees break under distribution shift (§5.3 treats time-series shift separately). Coverage is averaged over the calibration draw.

### kalai2025why
- Title: Why Language Models Hallucinate
- Authors: Adam Tauman Kalai, Ofir Nachum, Santosh S. Vempala, Edwin Zhang (OpenAI / Georgia Tech)
- Date: arXiv 2509.04664 (Sep 2025)
- Type: position paper with theory (by vendor-affiliated authors)
- Verification: full-text (§1, §3 Corollary/Eq. on err ≥ 2·err_iiv, §4.1 Observation 1, §4.2, Table 2)
- Supports:
  - Under binary grading (1 for correct, 0 for wrong and for IDK), "abstaining is strictly sub-optimal": for any belief ρ_c over binary graders, the optimal responses are not abstentions (Observation 1).
  - A meta-evaluation of 10 popular benchmarks (GPQA, MMLU-Pro, IFEval, Omni-MATH, WildBench, BBH, MATH L5, MuSR, SWE-bench, HLE) found 9 use binary grading with no IDK credit. WildBench gives partial credit, but its rubric may score IDK below hallucinated "fair" answers.
  - Proposal: explicit confidence targets in the prompt: "Answer only if you are > t confident, since mistakes are penalized t/(1 − t) points, while correct answers receive 1 point, and an answer of 'I don't know' receives 0 points". Answering beats IDK iff P(correct) > t. Examples: t = 0.5 (penalty 1), 0.75 (penalty 2), 0.9 (penalty 9).
  - "Behavioral calibration": audit accuracy and error rates across stated thresholds instead of requiring verbalized probabilities. This avoids "exponentially many ways to phrase correct responses".
  - Theory: generative error rate ≳ 2 × the Is-It-Valid misclassification rate. Calibration of pretrained models is argued to imply errors.
- Caveats: recent preprint (not peer-reviewed as of access). One sentence in §4.2 says the optimal behavior is "outputting IDK among examples where its correctness probability is greater than the target", which looks like a typo for "less than", given the preceding derivation.

### hendrycks2017baseline
- Title: A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks
- Authors: Dan Hendrycks, Kevin Gimpel
- Date: ICLR 2017. arXiv 1610.02136 (v3 Oct 2018)
- Type: method paper / benchmark
- Verification: full-text (§2 metrics, §3 baseline)
- Supports: the maximum softmax probability (MSP) is the baseline score for both misclassification detection and OOD detection. AUROC is "threshold-independent" and equals the probability that a positive example scores higher than a negative one (random = 50%). AUPR is reported because AUROC "is not ideal when the positive class and negative class have greatly differing base rates". AUPR depends on which class is called positive, so they report AUPR-In and AUPR-Out (Succ/Err).
- Caveats: this paper does not define FPR@95%TPR. That metric comes from liang2018odin.

### liang2018odin
- Title: Enhancing The Reliability of Out-of-distribution Image Detection in Neural Networks (ODIN)
- Authors: Shiyu Liang, Yixuan Li, R. Srikant
- Date: ICLR 2018. arXiv 1706.02690
- Type: method paper
- Verification: full-text (§4 metrics, §4.2 hyperparameter selection)
- Supports: "FPR at 95% TPR can be interpreted as the probability that a negative (out-of-distribution) example is misclassified as positive (in-distribution) when the true positive rate (TPR) is as high as 95%." Detection error P_e = 0.5(1 − TPR) + 0.5·FPR at TPR 95%. ODIN uses temperature T = 1000 and input perturbation.
- Caveats: ODIN's hyperparameters were "chosen to minimize the FPR at TPR 95% on the validation OOD dataset" (iSUN). This uses OOD data for tuning, which is a known optimistic bias in OOD benchmarking. Note that in-distribution is the positive class here.

### larson2019clinc
- Title: An Evaluation Dataset for Intent Classification and Out-of-Scope Prediction (CLINC150)
- Authors: Stefan Larson, Anish Mahendran, Joseph J. Peper, Christopher Clarke, Andrew Lee, Parker Hill, Jonathan K. Kummerfeld, Kevin Leach, Michael A. Laurenzano, Lingjia Tang, Jason Mars
- Date: EMNLP-IJCNLP 2019. arXiv 1909.02027
- Type: benchmark/dataset paper
- Verification: full-text (§2, §3.2–3.3, Table 2)
- Supports: 150 intents in 10 domains, with 100 train, 20 validation and 30 test queries per intent. 1,200 out-of-scope (OOS) queries: 100 for training, 100 for validation, 1,000 for testing. Variants: Small, Imbalanced, OOS+. Three OOS strategies: oos-train (a 151st class), oos-threshold (threshold on predicted probability, chosen to maximize validation score treating OOS as its own intent), oos-binary. Metrics: in-scope accuracy and OOS recall. The best system reached about 66% OOS recall. The threshold approach "provided erratic results" for several models. Only about 69% of prompts targeting OOS actually yielded OOS queries.
- Caveats: OOS recall alone ignores false OOS on in-scope queries (partly visible in in-scope accuracy). The threshold is tuned on validation data that contains OOS examples.

### yang2024generalizedood
- Title: Generalized Out-of-Distribution Detection: A Survey
- Authors: Jingkang Yang, Kaiyang Zhou, Yixuan Li, Ziwei Liu
- Date: IJCV 2024. arXiv 2110.11334 (v1 Oct 2021, v3 Jan 2024)
- Type: position/survey
- Verification: full-text (§1, Fig. 1–2, §3.1 post-hoc methods, §6.1 challenges)
- Supports: a unified "generalized OOD detection" framework covering anomaly detection, novelty detection, open-set recognition, OOD detection and outlier detection. They differ in covariate vs semantic shift and in whether ID classification is also required. ODIN-style temperature for OOD "is different from confidence calibration". Pitfalls: OOD test sets must have ID classes removed (§6.1). Outlier-exposure training data needs de-duplication against ID data. Points to the OpenOOD benchmark.
- Caveats: vision-centric.

### elkan2001foundations
- Title: The Foundations of Cost-Sensitive Learning
- Authors: Charles Elkan
- Date: IJCAI 2001
- URL: https://cseweb.ucsd.edu/~elkan/rescale.pdf (author preprint, "To appear, IJCAI'01")
- Type: method paper
- Verification: full-text (rendered pp. 1–2: §1 Eq. 1, §1.1–1.3 Eq. 2)
- Supports:
  - Optimal prediction minimizes L(x,i) = Σ_j P(j|x) C(i,j), where C(i,j) is the cost of predicting i when the truth is j. (Eq. 1)
  - Two classes: predict 1 iff p ≥ p* = (c10 − c00) / (c10 − c00 + c01 − c11). (Eq. 2) With zero cost for correct predictions this is p* = c10/(c10 + c01).
  - "Reasonableness" conditions: c10 > c00 and c01 > c11. A 2×2 cost matrix has effectively one degree of freedom for decisions.
  - Costs vs benefits: all entries must be measured from the same baseline. The German credit cost matrix is shown to be economically incoherent.
  - Recommendation: learn a classifier from the training set as given, then compute optimal decisions explicitly from its probability estimates. Rebalancing has little effect on Bayesian and decision-tree learners.
- Caveats: needs calibrated P(j|x). Miscalibration directly moves the decision boundary.

### drummond2006costcurves
- Title: Cost curves: An improved method for visualizing classifier performance
- Authors: Chris Drummond, Robert C. Holte
- Date: Machine Learning 65(1):95–130, 2006 (author preprint dated 23 Nov 2005)
- DOI: 10.1007/s10994-006-8199-5; preprint https://www.site.uottawa.ca/~cdrummon/pubs/ML_2006.pdf
- Type: method paper
- Verification: full-text (author preprint. Abstract, §3 Eq. 2–6)
- Supports: E[Cost] = FN·p(+)·C(−|+) + FP·p(−)·C(+|−). (Eq. 4) Normalized expected cost Norm(E[Cost]) = E[Cost] / (p(+)C(−|+) + p(−)C(+|−)). (Eq. 5) Probability cost PC(+) = p(+)C(−|+) / (p(+)C(−|+) + p(−)C(+|−)). Then Norm(E[Cost]) = FN·PC(+) + FP·(1 − PC(+)), which is a straight line from (0, FP) to (1, FN) (Eq. 6). Here FN and FP are rates. Cost curves show performance over all class priors and cost ratios, plus confidence intervals and significance, which they argue is easier than with ROC.
- Caveats: two-class only. The preprint may differ slightly from the journal version.

### vickers2006dca
- Title: Decision Curve Analysis: A Novel Method for Evaluating Prediction Models
- Authors: Andrew J. Vickers, Elena B. Elkin
- Date: Medical Decision Making 26(6):565–574, 2006
- DOI / URL: 10.1177/0272989X06295361; PMC2577036
- Type: method paper
- Verification: full-text (PMC HTML. Read the Theory section and the worked example.)
- Supports: the threshold probability p_t, at which treat/no-treat expected benefits are equal, encodes the harm ratio: (a − c)/(d − b) = (1 − p_t)/p_t (Eq. 1). Net Benefit = TP/n − (FP/n)·(p_t/(1 − p_t)), "first attributed to Peirce". Worked example at p_t = 10%: TP = 65, FP = 225, n = 902 gives NB = 65/902 − (225/902)(0.1/0.9) = 0.0443. Compare against "treat all" and "treat none" (NB = 0). The decision curve plots NB against p_t. The theoretical range is from −∞ to the prevalence.
- Caveats: medical domain. Requires the model's probabilities to be used at threshold p_t, so miscalibration lowers net benefit.

## Topic notes

### 1. Proper scoring rules, log loss, Brier score, decomposition
- **Definitions** (gneiting2007proper §3. brocker2009 Table 1):
  - Log loss / NLL / ignorance: −log p_y, averaged over items. Its divergence is KL. It is local: it depends only on the probability given to the realized outcome (Bernardo's result, cited by gneiting2007proper §4.1).
  - Multiclass Brier: Σ_j (p_j − δ_{jy})², range [0, 2]. Binary Brier: (p − y)², range [0, 1]. These differ by a factor of 2 in the binary case. Always state the form used.
  - Both are strictly proper. Accuracy (zero–one score) is proper but not strictly proper, so it cannot distinguish honest from sharpened probabilities (gneiting2007proper Ex. 4).
- **Murphy/Bröcker decomposition** (murphy1973partition abstract. brocker2009 Eq. 13 general. Brier instantiation derived from brocker2009 Table 1 and brocker2012 Eq. 13–14):
  - BS = REL − RES + UNC.
  - With forecasts grouped into K distinct values f_k (n_k cases, observed frequency ō_k, overall base rate ō): REL = (1/N)Σ_k n_k (f_k − ō_k)², RES = (1/N)Σ_k n_k (ō_k − ō)², UNC = ō(1 − ō).
  - REL measures calibration (lower is better). RES measures discrimination / refinement (higher is better). UNC depends only on the data.
  - Exact only if forecasts within a group are identical. With binned continuous forecasts, extra within-bin terms appear.
  - The empirical REL is biased upward (true forecasts are more reliable than the empirical term suggests) by about (1/N)Σ_d ν_d e(π^(d)) (brocker2012 Eq. 25).
- **Calibration vs discrimination**:
  - Calibration alone is insufficient: the constant base-rate forecast is perfectly calibrated with zero resolution (kumar2019 §2.1. tian2023 fn. 5).
  - AUROC measures ranking only and is "indifferent to calibration" (kadavath2022 Glossary).
  - A proper score rewards both. Gneiting's paradigm is "maximize sharpness subject to calibration".
  - Schervish: proper scores are mixtures of threshold-specific cost-weighted losses (gneiting2007proper Eq. 14–15). This explains why a proper score is an average of decision utilities over unknown cost ratios.
- **Pitfalls**:
  - Log loss is unbounded. p = 0 on the true class gives +∞, so implementations clip (e.g. ε = 1e-15). Clipping changes the score, so report ε. A single confident error can dominate small-n results.
  - Small worked numbers (computed here, not from a source): p = 0.9 on the true class gives log loss 0.105 and binary Brier 0.01. p = 0.1 on the true class gives log loss 2.303 and Brier 0.81. The uniform p = 0.5 gives log loss 0.693 and Brier 0.25, which is the chance level cited in kadavath2022.
  - For K classes the uniform forecast gives log loss ln K and multiclass Brier 1 − 1/K. Normalize or compare against this baseline across tasks with different K.

### 2. Calibration measurement
- **Notions** (kull2019 Def. 1–3. vaicenavicius2019 Eq. 1–2. kumar2019 Eq. 2–3):
  - Canonical / multiclass: P(Y | p̂(X)) = p̂(X).
  - Classwise / marginal: each p̂_k is calibrated for its one-vs-rest event.
  - Top-label / confidence: P(correct | max p̂) = max p̂.
  - Each is strictly weaker than the one before. ECE in Guo's form tests only top-label calibration. Temperature-scaled models can be confidence-calibrated (conf-ECE 0.0078) yet classwise-miscalibrated (kull2019 Fig. 1).
- **ECE estimator conventions differ across papers**. Report bins, binning scheme, norm and label set.

  | Source | Bins | Binning | Norm | Label set |
  |---|---|---|---|---|
  | guo2017 | 15 | equal-width | L1 | top-label |
  | naeini2015 | 10 | sorted (likely equal-mass) | L1 | binary |
  | kadavath2022 | 10 | equal-count | L1 | top prediction, plus RMS |
  | tian2023 | not stated | — | squared | top-label |
  | nixon2019 | — | SCE/ACE variants | L1/L2 | classwise, thresholded |

  nixon2019 shows that rankings of methods change with these choices.
- **Bias**:
  - Binning a continuous model underestimates the true calibration error (kumar2019 Prop. 3.3, Ex. 3.2 with CE(f_B) = 0 but CE(f) ≥ 0.49).
  - The finite-sample plug-in estimate is biased upward, worst for well-calibrated models (roelofs2022 Fig. 1. kumar2019 Thm 5.3: bias about B/n for squared CE). With small n per cell (e.g. 3–24), a binned ECE is dominated by this noise.
  - Remedies: the debiased estimator (kumar2019 Def. 5.2. brocker2012), ECE_sweep (roelofs2022), equal-mass bins (roelofs2022, nixon2019), smooth / kernel ECE (blasiok2023smoothece), and consistency-resampling hypothesis tests (vaicenavicius2019).
  - ECE is discontinuous at 0 (blasiok2023unifying Lemma 4.8).
- **Post-hoc recalibration** (guo2017 §4):
  - Platt scaling σ(az + b). Temperature scaling softmax(z/T), with T fit by NLL on held-out validation data. It does not change argmax accuracy.
  - Alternatives: histogram binning, isotonic regression, BBQ (naeini2015), vector/matrix scaling and Dirichlet calibration (kull2019).
  - Pitfall: fitting T on the test set (cf. tian2023 ECE-t) reports calibratability, not deployed calibration.

### 3. LLM calibration and verbalized confidence
- **Sources of confidence**:
  - Token / label probability over a fixed option set: P(A), P(B), … (kadavath2022. openai2023 Fig. 8).
  - Candidate-renormalized probability P_N = P_LM(Ŷ)/Σ_{Y'∈I(X)} P_LM(Y') (jiang2021 Eq. 1).
  - P(True) self-evaluation of a sampled answer, and a P(IK) head (kadavath2022).
  - Verbalized numeric or linguistic confidence (tian2023).
  - Sampling consistency (feng2024 baseline).
- **Findings**:
  - Pretrained LMs are well calibrated on formatted multiple-choice questions (kadavath2022). The format matters: "none of the above" hurts.
  - Post-training / RLHF reduces calibration: GPT-4 MMLU-subset ECE went from 0.007 to 0.074 (openai2023 Fig. 8, vendor claim). This is largely fixable by a single temperature, T = 2.5 (kadavath2022 §3.3, on Anthropic models).
  - For RLHF chat models, verbalized confidence is often better calibrated than token probabilities (about 50% relative ECE reduction. tian2023).
  - The generative T5, BART and GPT-2 models were poorly calibrated in QA (jiang2021).
- **Where likelihood-based metrics do not apply**:
  - (a) Closed APIs that return no logprobs. Only verbalized or behavioral confidence is available.
  - (b) Free-form generated text. Correctness must be judged (exact match, alias sets or an LLM judge as in tian2023 and kirichenko2025), so labels are noisy. A "probability of the answer string" is not a probability of being correct, given the "exponentially many ways to phrase correct responses" (kalai2025 §4.2).
  - (c) Renormalized vs unnormalized scores. Probabilities renormalized over a candidate set (jiang2021) are conditional on that set and change if candidates are added. Raw sequence likelihoods are not comparable across lengths. Unnormalized confidence scores (MSP from logits after arbitrary transforms, verbalized 0–100 values, judge scores) support ranking metrics (AUROC, AURC, risk–coverage) but not log loss, Brier or ECE unless they are mapped to [0,1] and interpreted as probabilities.
  - (d) A verbalized "0%" or "100%" makes log loss infinite. Clip and report.
  - (e) Abstention outputs ("I don't know") have no probability of correctness. Score them separately (see §4).

### 4. Selective prediction and abstention
- **Classical**: Chow's reject option (chow1970 abstract).
  - Derivation (standard, not verified from Chow): with unit error cost and rejection cost c_r < 1, the expected cost of predicting the argmax is 1 − max_k p_k. Reject iff 1 − max_k p_k > c_r, i.e. iff max_k p_k < 1 − c_r.
  - This is the same form as kalai2025's target t, with penalty t/(1−t) for errors and 0 for IDK: answer iff p > t.
- **Risk–coverage** (geifman2017 Eq. 1–3. elyaniv2010):
  - Coverage φ = E[g]. Selective risk = E[ℓ g]/φ.
  - Summary metrics: the RC curve, AURC (geifman2019) and E-AURC = AURC − AURC(κ*) with AURC(κ*) ≈ r̂ + (1−r̂)ln(1−r̂). Also coverage at a target risk or accuracy (kamath2020, "Coverage@Acc" in wen2024) and the AUC of accuracy–coverage (tian2023).
  - The SGR algorithm sets a threshold with a high-probability risk guarantee on i.i.d. held-out data.
- **Ranking vs calibration**: selective metrics depend only on the ordering of confidences, calibration on their absolute values (kamath2020 §2.3). A model can have good AURC and terrible ECE, or the reverse.
- **AURC caveat**: AURC confounds base accuracy with ranking quality (geifman2019's motivation for E-AURC). Compare systems with different accuracies via E-AURC or full RC curves.
- **Under shift**: MaxProb abstention degrades on mixed ID/OOD inputs, and a trained calibrator helps (kamath2020: 56.1% vs 48.2% coverage at 80% accuracy).
- **Answerability benchmarks**:
  - SQuAD 2.0 gives abstention full credit on unanswerable items. The always-abstain baseline gets 48.9 F1, so a large share of the score is available to a trivial policy (rajpurkar2018).
  - The threshold is tuned on dev to maximize F1, which is itself a decision-threshold choice that must be frozen before test.
- **LLM abstention metrics**: the confusion matrix and formulas (wen2024 Table 1, §4.2. feng2024). Report coverage, abstention P/R/F1, reliable accuracy and effective reliability together.
  - AbstentionBench reports recall-focused results and finds reasoning fine-tuning lowers abstention by 24% on average (kirichenko2025, benchmark-author claim). It depends on an LLM judge with 88% accuracy.
- **Incentives**:
  - Binary-graded benchmarks make guessing optimal. Observation 1 in kalai2025: abstention is never optimal under 0/1 grading with IDK scored 0.
  - Fix: state the confidence target t and penalty t/(1−t) explicitly, then audit "behavioral calibration" (accuracy and error vs t).
  - This is a utility-based evaluation and links to §6.
- **Conformal prediction** (angelopoulos2021): distribution-free marginal coverage 1−α ≤ P(Y ∈ C) ≤ 1−α + 1/(n+1) under exchangeability, from split calibration with the ⌈(n+1)(1−α)⌉/n quantile.
  - Pitfalls: marginal, not conditional, coverage. Invalid under distribution shift. Set size (efficiency) depends on score quality. With small calibration n, the realized coverage of a fixed set fluctuates around the target.

### 5. OOD detection, and how it differs from answerability and confidence
- **Metrics** (hendrycks2017 §2. liang2018odin §4):
  - AUROC is threshold-free and equals P(score_pos > score_neg).
  - AUPR-In and AUPR-Out depend on the base rate and on which class is positive.
  - FPR@95%TPR, with ID treated as positive in ODIN.
  - Detection error = 0.5(1−TPR) + 0.5·FPR.
  - Report which class is positive.
  - CLINC150 uses in-scope accuracy plus OOS recall, with the OOS threshold tuned on validation data containing OOS (larson2019).
- **Pitfalls**:
  - Tuning detector hyperparameters on OOD validation data from the test OOD family (ODIN tuned on iSUN) is optimistic.
  - ID/OOD class overlap in test sets and de-duplication of outlier-exposure data (yang2024 §6.1).
  - Threshold methods "provided erratic results" on CLINC150 (larson2019).
  - OOD AUROC says nothing about calibration.
- **Distinguish three questions**:
  - (i) Answerability or scope: is the question answerable from the given context or within the system's scope? This is a property of the input. Examples: SQuAD 2.0 (rajpurkar2018), CLINC OOS (larson2019), and the query perspective in wen2024.
  - (ii) Confidence or correctness prediction: will this model's answer be right? This is a property of the model–input pair. Examples: misclassification detection (hendrycks2017), P(IK)/P(True) (kadavath2022), and selective prediction (geifman2017).
  - (iii) Distribution shift detection: is x drawn from a different distribution? Semantic vs covariate shift (yang2024).
  - These overlap but are not identical. An OOD input may be answered correctly, and an in-distribution input may be unanswerable. Benchmarks often label only (i), while abstention metrics such as wen2024 Recall_abs mix (i) and (ii) by counting wrong answers on answerable items as "should have abstained".
  - A typed fallback label (e.g. out_of_scope vs missing_evidence vs low confidence) should be evaluated against the matching ground truth.

### 6. Cost-sensitive decisions and utility
- **Bayes decision**: minimize Σ_j P(j|x)C(i,j). The two-class threshold is p* = (c10 − c00)/(c10 − c00 + c01 − c11) (elkan2001 Eq. 1–2).
  - Learn on the natural distribution and apply the threshold to calibrated probabilities. Rebalancing is not needed.
  - Costs and benefits must share one baseline (elkan2001 §1.2).
- **Cost curves** (drummond2006 Eq. 4–6): normalized expected cost as a function of PC(+) visualizes performance over all priors and cost ratios. A classifier is a line from (0, FP) to (1, FN), and the lower envelope gives the best choice per operating point.
- **Decision curve analysis** (vickers2006):
  - NB(p_t) = TP/n − FP/n · p_t/(1−p_t), compared against treat-all and treat-none across a plausible p_t range.
  - Example: NB = 0.0443 at p_t = 0.1.
  - This is a template for utility-based evaluation of a decision system: choose the range of thresholds that stakeholders find plausible, then report net benefit relative to the default policies.
- **Connections**:
  - Proper scores are averages of such threshold utilities (gneiting2007proper Schervish representation).
  - The kalai2025 confidence target t is a decision threshold with penalty t/(1−t), the same algebra as DCA's p_t/(1−p_t) weight.
  - Chow's reject rule is the abstain-option version.
  - If probabilities are miscalibrated, the cost-optimal threshold computed from the cost matrix is wrong. A threshold tuned empirically on dev data partially compensates, but must be frozen before test.

### Methodological evidence vs benchmark-author claims
- **Methodological / theoretical**: gneiting2007proper, brocker2009, brocker2012, kumar2019, roelofs2022, blasiok2023unifying, blasiok2023smoothece, vaicenavicius2019, kull2019 (definitions), geifman2017, geifman2019, angelopoulos2021, elkan2001, drummond2006, vickers2006, kalai2025 Observation 1 (trivial theorem).
- **Empirical studies with vendor or benchmark-author claims**: openai2023 Fig. 8 (not reproducible), kadavath2022 (own models), tian2023, kirichenko2025 (24% degradation, judge-based), feng2024 (19.3% gain), larson2019 and rajpurkar2018 baseline numbers.
