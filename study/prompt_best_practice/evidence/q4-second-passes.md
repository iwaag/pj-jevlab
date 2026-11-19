# Q4 evidence: second passes (self-consistency, verification, self-correction, elimination, re-ranking, voting, judge self-agreement)

Access date for every link: 2026-10-03. Scope: study step2 + step3 for Q4 ([plan](../../../devdocs/episodes/study/prompt_best_practice/p1/plan.md)). The lab's own second-pass results are in [lab-evidence.md](../lab-evidence.md) (Q4-1 to Q4-12, Q6-2) and are not repeated as evidence here; they are only referenced as "lab item".

## How the sources were read (limits)

- Papers were downloaded as PDF from arXiv (`https://arxiv.org/pdf/<id>`) and read as extracted text (`pdftotext -layout`). Numbers are copied from the cited table, figure caption or paragraph. Two PDFs (CAPE at OpenReview, the ACL Anthology copy of POE) could not be opened as text; see "Not opened" below. For CAPE an earlier workshop version of the same idea was opened instead.
- Section and table numbers are those printed in the opened version (arXiv version given in each entry). Where an entry says "n not extracted", the paper's n was not found in the passage read.
- Grades: A = peer-reviewed controlled study (venue visible in the opened text or in a listing I saw; stated per entry); B = preprint with code or released data; C = vendor or single-organisation evaluation; D = practitioner report; E = guide or opinion. "Code" was only counted when a repository link appears in the opened text.
- Readout match to the lab systems: **matching** = option-letter/ID token probabilities read in one pass (W12, A27) or a comparable scorer; **partial** = related scorer (option log-likelihood, encoder score, letter probability under another model class) or generative with a short label; **not matching** = free-text/CoT generation or sampling, which the lab's logit, pointer and encoder systems do not do. K27 (pointer head), J and G (encoders) and L27 (short generative) are named where relevant.
- Statements marked **(inference)** are mine, not the sources'. Everything else is a paraphrase of the cited passage.

## Summary table

| # | Source | Venue / grade | Readout studied | Match to lab | One-line result |
|---|---|---|---|---|---|
| A1 | Wang et al., Self-Consistency | ICLR 2023, A | sampled CoT text, majority vote | not matching | +7.6 to +17.9 on arithmetic with PaLM-540B; prompt-set and prompt-order ensembles gain much less; mixing a weaker model hurts |
| A2 | Xiong et al., confidence elicitation | ICLR 2024, A | verbalised confidence + sampling consistency | not matching | verbalised confidence overconfident; consistency helps but no method wins everywhere |
| A3 | Chen et al., "Are more LM calls all you need" | arXiv, B (code not checked) | majority vote over GPT-3.5 samples | not matching | vote can get worse with more calls: better on easy queries, worse on hard ones |
| A4 | Li et al., "More agents" | TMLR 2024, A | sampling and voting | not matching | accuracy rises with ensemble size, gain larger on harder tasks and weaker models |
| B1 | Huang et al., LLMs cannot self-correct reasoning yet | ICLR 2024, A | generative re-ask, 2 rounds | partial (MC task, generative) | intrinsic self-correction lowers accuracy; CSQA GPT-3.5 75.8 -> 38.1 |
| B2 | Liu et al., LLMs have intrinsic self-correction ability | arXiv v2, B (code not checked) | generative re-ask, zero temperature | partial | with a "fair" prompt gains of 0.1-1 point; the Huang prompt lowers accuracy |
| B3 | Kamoi et al., critical survey of self-correction | arXiv v3 (venue not verified in text), B | survey | not applicable | no reliable prompted self-correction in general tasks; works with reliable external feedback |
| B4 | Stechly et al., self-verification limitations | arXiv v2 (2 workshop precursors), B | GPT-4 generative critique | not matching | self-critique lowers accuracy; sound verifier raises it; plain re-sampling keeps most of the gain |
| B5 | Tyen et al., LLMs cannot find errors | arXiv v3, B (code not checked) | step-level mistake finding | not matching | mistake finding weak; correction given the location works |
| B6 | Zhang et al., small LMs need strong verifiers | arXiv v2, B | ≤13B generative | partial (small models) | weak self-verifier brings little; GPT-4 verifier adds +8.3 on average |
| B7 | Tsui, Self-Correction Bench | COLM 2026, A | injected vs own errors, 14 open models | not matching | 64.5% blind spot: same error fixed when external, missed when own |
| B8 | Laban et al., FlipFlop | arXiv v2, B | "Are you sure?" re-ask on classification | partial (classification, generative) | models flip 46% of answers; mean accuracy drop 17 points |
| C1 | Dhuliawala et al., CoVe | arXiv, B (no code link in text) | Llama 65B generative | not matching | factored verification cuts hallucinated list items; yes/no verification questions agree with the claim |
| C2 | Gou et al., CRITIC | ICLR 2024, A | LLM + search/code tools | not matching | critique without tool is about as good as CoT/self-consistency; tools carry the gain |
| C3 | Zhou et al., Variation in Verification | ICLR 2026, A | generative verifiers, 14 models 2B-72B + GPT-4o | not matching | verifier true-negative rate drops 0.68 -> 0.17 as the generator gets stronger |
| C4 | Saad-Falcon et al., Weaver | arXiv v3 (NeurIPS 2025 per a search listing), B | weak judges/reward models, distilled 400M cross-encoder | partial (cross-encoder distillation) | weighted verifier ensemble +15.5 over majority vote; unweighted ensembles and self-verification do not beat majority vote |
| C5 | Brown et al., Large Language Monkeys | arXiv v3, B | repeated sampling | not matching | without an automatic verifier, majority vote and reward models plateau |
| D1 | Ma and Du, POE | EMNLP 2023 (per anthology listing seen in search; not opened), A | option log-likelihood scoring, FLAN-T5-XL 3B | partial | elimination beats multiple-choice prompting on 5 of 8 tasks, helps logical tasks, hurts others |
| D2 | Zhu et al., PoE_ID (option-ID elimination) | arXiv v3, B (code link) | option-ID logprobs, 6 open LLMs 9B-32B | matching | +0.8 to +6.3 points over debiased baseline, larger with more options; asking the model to name the wrong option is much worse |
| D3 | Ma et al., filter-then-rerank | arXiv v2 (venue not verified), B (code not checked) | SLM filter + LLM multiple-choice rerank of top-3 | partial | +2.4 F1 average; LLM reranking hurts easy samples, helps hard ones |
| E1 | Arora et al., Ask Me Anything | arXiv v3 (ICLR 2023 per its reference style, not stated in text), B (code) | prompt-chain votes, GPT-J-6B etc. | partial (T0-3B option scoring) | majority vote over prompts gains little and can hurt; prompt errors are correlated |
| E2 | Hua et al., calibrating with prompt variations | workshop paper (venue not stated in the text), C | letter-token probability averaged over paraphrases | matching (letter probabilities, one model) | ECE cut >70% with temperature scaling; accuracy about unchanged |
| E3 | Guda et al., permutation voting with KV caching | arXiv v1, B | option-ID scoring, 3B models | matching | permutation majority vote +0.8 to +21 points; bias metric becomes 0 |
| E4 | Trad and Chehab, ensembles for phishing detection | arXiv v1, B | LLM label text | partial (classification, generative) | ensemble helps only when members are of similar strength; best single model not beaten |
| E5 | Kamen and Kamen, "Majority Rules" | arXiv v1, C (company authors) | ten LLMs, IAB taxonomy | partial (generative classification) | headline "up to 65% F1 over the strongest single model"; design and significance not verified |
| E6 | Kohli, "Nine judges, two effective votes" | arXiv v1 (May 2026), B | 9 frontier LLMs as NLI judges | partial (3-way NLI, generative) | panel behaves like about 2 independent votes; best single judge matches or beats the panel |
| E7 | Kim et al., correlated errors in LLMs | ICML 2025 (PMLR 267 per text), A | 349 + 71 LLMs on MCQ leaderboards | partial (MCQ) | models agree on 42-60% of items when both wrong (random: 13% / 33%); more accurate models more correlated |
| F1 | Panickssery et al., self-preference | arXiv v1, B (code link) | GPT-4, GPT-3.5, Llama-2-7B judges | not matching | self-preference correlates linearly with self-recognition; fine-tuning shows dose-response |
| F2 | Wataoka et al., self-preference bias | arXiv v2, B | GPT-4 etc. as judges vs human labels | not matching | GPT-4 shows the largest bias; all judges favour low-perplexity text |
| F3 | Zheng et al., MT-Bench | NeurIPS 2023 D&B, A | GPT-4 judge | not matching | self-enhancement suggestive but the authors say data cannot determine it |
| F4 | Haldar and Hockenmaier, Rating Roulette | EMNLP Findings 2025, A | Llama-3.1-70B, R1-Distill-Qwen, Qwen3-32B judges | not matching | same-prompt re-runs agree poorly (alpha 0.27-0.79 depending on benchmark and model) |
| F5 | Ding, "When LLMs agree, are they right?" | arXiv v2 (Jul 2026), B (released data) | gpt-4.1 family K=50 samples; 3 Claude tiers | not matching | agreement is a weak positive predictor of correctness; worst for the most consistent model; partly positional |
| G1 | Wang et al., "My answer is C" | ACL Findings 2024, A (per the anthology listing seen in search; opened as arXiv v2) | first-token probability vs text | contrast | the two readouts disagree on 10-51% of MMLU items depending on model |
| G2 | Leviathan et al., prompt repetition | arXiv v1, C (Google Research, no code) | non-reasoning generative, 7 models | partial (re-reading in context) | repeating the prompt wins 47 of 70 tests, 0 losses (McNemar p<0.1) |
| G3 | Taubenfeld et al., CISC | arXiv v2, B | confidence-weighted vote, 9 models | not matching | confidence-weighted vote needs 40% fewer samples; the best-calibrated confidence was worst within-question |

## A. Self-consistency and voting over samples

### A1. Wang et al., "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
- Links: [arXiv 2203.11171](https://arxiv.org/abs/2203.11171), [PDF](https://arxiv.org/pdf/2203.11171). Footer of the opened PDF: "Published as a conference paper at ICLR 2023". Grade A.
- Models and readout: UL2-20B, LaMDA-137B, GPT-3 code-davinci-001/002 (175B), PaLM-540B; sampled chain-of-thought text, final answers majority-voted (40 samples, 10 runs averaged). Not matching to W12/A27/K27/J/G; L27 only if sampling with a rationale.
- Tasks: arithmetic (GSM8K, SVAMP, AQuA, MultiArith, AddSub, ASDiv), commonsense (CSQA, StrategyQA, ARC), NLI/QA (ANLI, e-SNLI, RTE, BoolQ, HotpotQA). English. n per task not extracted.
- Result, Table 2: PaLM-540B CoT -> self-consistency GSM8K 56.5 -> 74.4, AQuA 35.8 -> 48.3, SVAMP 79.0 -> 86.6; UL2-20B gains only +3.2 to +6.8. Gains grow with model size (text under Table 2).
- Table 5 (PaLM-540B, NLI and QA; section 3.3): chain-of-thought alone lowers ANLI-R1, e-SNLI and RTE below standard prompting (e.g. RTE standard 84.8, CoT 79.1) and self-consistency recovers and passes it (RTE 86.3, ANLI-R1 78.5 vs 69.1 standard).
- Table 7 (section 3.4, LaMDA-137B): GSM8K CoT 17.1, ensemble over 3 hand-written prompt sets 18.6, ensemble over 40 prompt-order permutations 19.2, self-consistency 27.7. So voting over prompt wording or order gave a fraction of the sampling gain.
- Table 10 (appendix A.1.3): ensembling different models (LaMDA + PaLM = 36.9, PaLM + GPT-3 = 36.6) is far below PaLM-540B alone (56.5 greedy); the text says lower-capacity members drag the ensemble down and a much weaker member can hurt.
- Replication/significance: standard errors over 10 runs given; many later papers re-use it. Limitation stated (cost; section 6): more computation, performance saturates quickly.
- Relevance (inference): a vote over sampled outputs needs a stochastic generator. W12, A27, K27, J, G are deterministic scorers (the lab found repeat noise zero), so only L27 could be sampled; the logit-side analogue is a vote over prompt variants or option permutations (E2, E3).

### A2. Xiong et al., "Can LLMs Express Their Uncertainty?"
- Links: [arXiv 2306.13063](https://arxiv.org/abs/2306.13063), [PDF](https://arxiv.org/pdf/2306.13063). Footer: ICLR 2024. Grade A (code link in abstract).
- Models: five LLMs including GPT-4, GPT-3.5, Vicuna and LLaMA-2-70B Chat; verbalised confidence, sampling-consistency aggregation, white-box comparison. Five dataset types (commonsense, arithmetic, professional knowledge and others). English. Metrics ECE and AUROC (section 5, Table in 5.1).
- Result: verbalised confidence is overconfident (average ECE above 0.377 for GPT-3.5 and Vicuna, section 5.1); better prompts and consistency help but "none of these techniques consistently outperform others"; white-box methods are better but the gap is narrow (AUROC "0.522 to 0.605" as printed in the abstract); all methods struggle on professional-knowledge tasks.
- Relevance (inference): supports not trusting a generative model's stated confidence as a gate for a second pass; the lab's own result is that K27 errors are high-confidence (lab item Q4-10), which is a pointer-head observation, not this paper's.

### A3. Chen et al., "Are More LM Calls All You Need?"
- Links: [arXiv 2403.02419](https://arxiv.org/abs/2403.02419), [PDF](https://arxiv.org/pdf/2403.02419). arXiv v2, June 2024; venue not visible in text. Grade B.
- Model: GPT-3.5-turbo-0125, 1,000 runs averaged. Tasks (section on real data): MMLU Physics, TruthfulQA, GPQA, AVeriTeC. Readout: sampled answers, majority vote ("Vote") and LM-filtered vote ("Filter-Vote").
- Result (abstract and Figure 2): accuracy can first rise and then fall as the number of calls grows. Decomposition on MMLU Physics: easy queries (53% of the set) improve with more calls, difficult queries (47%) get worse. Theory ties this to the spread of query difficulty: if the modal answer is wrong, more votes make it more certain.
- Relevance (inference): the lab's W3 missing-evidence cases are ones where the base model's modal answer is wrong (lab items Q4-1 to Q4-4); this paper predicts voting does not rescue them. It does not test classification with a label set.

### A4. Li et al., "More Agents Is All You Need"
- Links: [arXiv 2402.05120](https://arxiv.org/abs/2402.05120), [PDF](https://arxiv.org/pdf/2402.05120). Published in Transactions on Machine Learning Research, Oct 2024 (header of the PDF). Grade A (code link).
- Models: Llama2-13B-Chat, Llama2-70B-Chat, GPT-3.5-Turbo, GPT-4 (comparison only). Tasks: GSM8K, MATH, Chess, MMLU, HumanEval; sampling-and-voting up to 40 samples (Table 2).
- Result: accuracy rises with ensemble size; Llama2-13B at 40 agents scores 0.59 on GSM8K versus 0.54 for Llama2-70B single (section on Table 2); gain larger on harder tasks and weaker models (abstract and section 1).
- Relevance (inference): same-model sampling vote, not matching; shows the favourable regime (partial-competence model, diverse samples).

## B. Intrinsic self-correction and re-asking

### B1. Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet"
- Links: [arXiv 2310.01798](https://arxiv.org/abs/2310.01798), [PDF](https://arxiv.org/pdf/2310.01798). Footer: ICLR 2024. Grade A.
- Models: GPT-3.5-Turbo, GPT-4, GPT-4-Turbo, Llama-2-70b-chat. Tasks: GSM8K (n = 1,319), CommonSenseQA dev (n = 1,221, five-option multiple choice), HotpotQA (100 questions). English. Readout: generated text, two self-correction rounds, with and without oracle stop.
- Table 2 (oracle labels decide when to stop): GPT-3.5 CSQA 75.8 -> 89.7; this is the "improvement" earlier work reported and the paper argues it is oracle-driven (section 3.2).
- Table 3 (intrinsic, no oracle): GPT-3.5 GSM8K 75.9 -> 75.1 -> 74.7; CSQA 75.8 -> 38.1 -> 41.8; HotpotQA 26.0 -> 25.0 -> 25.0. GPT-4: GSM8K 95.5 -> 91.5 -> 89.0; CSQA 82.0 -> 79.5 -> 80.0; HotpotQA 49.0 -> 49.0 -> 43.0. Table 4: GPT-4-Turbo CSQA 84.0 -> 81.5 -> 83.0; Llama-2-70b-chat GSM8K 62.0 -> 36.5, CSQA 64.0 -> 36.5. Table 5 and 6: the drop appears under three different feedback prompts.
- Mechanism (section 4.2, Figure 1): for GSM8K the model keeps its answer in most cases (GPT-3.5: 74.7% unchanged) and when it changes it is more often right-to-wrong; on CommonSenseQA GPT-3.5 changes the answer often because candidate options look plausible and the "find problems" prompt biases it to switch (text of 4.2).
- Table 7 (section 5): multi-agent debate does not beat self-consistency at equal numbers of responses (GSM8K, GPT-3.5, 3/6/9 responses: self-consistency 82.5 / 85.3 / 88.2; debate 83.2 at 6, 83.0 at 9).
- Readout match: partial. The task is multiple choice but answered by generation; no letter-logit or pointer system was tested.
- Relevance (inference): a re-ask that names the first answer and invites revision (lab item Q4-7, F2) is the same kind of prompt; the lab's neutral wording ("may be the same option or a different one") differs from the "find problems" wording that this paper and B2 show to be the harmful ingredient.
- Replication: partly contradicted by B2 (prompt dependence); consistent with B3, B4, B5, B7.

### B2. Liu et al., "Large Language Models Have Intrinsic Self-Correction Ability"
- Links: [arXiv 2406.15673](https://arxiv.org/abs/2406.15673), [PDF](https://arxiv.org/pdf/2406.15673). arXiv v2, Dec 2024; the opened text does not state a venue. Grade B (code link not checked).
- Models: GPT-3.5, GPT-4, Mistral, Llama-3.1-8B-Instruct (Table 2); Qwen 2.5 family for size ablation (Table 3). Tasks: CommonSenseQA, HotpotQA, MMLU subsets, BIG-bench Sports, GSM8K, SVAMP. Readout: generation at temperature 0.
- Claim (section 5.2, Table 2): two factors decide the result, zero temperature and a "fair" prompt without words like "problem", "correct", "incorrect". With the Huang et al. prompt (Set 1) accuracy falls, e.g. GPT-3.5 CSQA 75.92 -> 66.34, Sports 83.25 -> 50.76; with the fair prompt (Set 3) it rises slightly: CSQA 75.92 -> 76.00, GPT-4 CSQA 84.11 -> 84.60, average across datasets GPT-3.5 74.84 -> 75.93 (p < 0.003), GPT-4 89.09 -> 89.65 (p < 0.05).
- Effect size: about +0.1 to +1 point on average; the best single cell is Sports GPT-3.5 +5.6. This is a small effect that depends on a prompt designed to avoid inducing a change.
- Readout match: partial (generative). Task-dependent: GSM8K GPT-3.5 77.63 -> 77.94 (flat).
- Relevance (inference): consistent with the lab's finding that re-asks with neutral wording leave answers almost unchanged (lab item Q4-8 shows probabilities near the first pass), but the cause in the lab is a different readout.

### B3. Kamoi et al., "When Can LLMs Actually Correct Their Own Mistakes?"
- Links: [arXiv 2406.01297](https://arxiv.org/abs/2406.01297), [PDF](https://arxiv.org/pdf/2406.01297). Survey, arXiv v3 Dec 2024; venue not visible in the extracted text. Grade B (survey of published work).
- Passage (abstract, section 1, RQ1 and RQ2 bullets, section 4, section 5.1): no prior work shows reliable self-correction by in-context prompting in general tasks; it works with reliable external feedback (code interpreters, search), with large-scale fine-tuning, and on tasks with decomposable responses; "feedback from prompted LLMs" is the bottleneck (section 7). Prior positive results often use oracle stopping, weak initial prompts or tasks well suited to correction. Section 12 briefly discusses work after May 2024.
- Readout match: not applicable (survey, generative).

### B4. Stechly, Valmeekam, Kambhampati, "On the Self-Verification Limitations of LLMs on Reasoning and Planning Tasks"
- Links: [arXiv 2402.08115](https://arxiv.org/abs/2402.08115), [PDF](https://arxiv.org/pdf/2402.08115). arXiv v2; the text says preliminary results appeared in two NeurIPS 2023 workshop papers (the precursors [2310.12397](https://arxiv.org/abs/2310.12397) and [2310.08118](https://arxiv.org/abs/2310.08118) were opened at abstract/table level only). Grade B.
- Model: GPT-4 as generator and verifier. Tasks: Game of 24, graph colouring, Blocksworld, Mystery Blocksworld; n = 100 instances per domain (section 5). Readout: generated solution and critique.
- Table 1: standard prompting versus LLM+LLM self-critique: Game of 24 5% -> 3%, graph colouring 16% -> 2%, Mystery Blocksworld 4% -> 0%; Blocksworld 40% -> 55% (the only gain). With a sound external verifier (binary feedback): 36%, 38%, 60%, 10%. Table 2: LLM verifier false-negative rate 95.8% (graph colouring) and 97.1% (Mystery Blocksworld); false-positive rate 18.6% (Blocksworld).
- Ablation (section 5.2): re-sampling with the same prompt until the sound verifier accepts ("Sampling k=15": 28%, 40%, 68%, 9%) keeps most of the gain of critique-informed re-prompting; self-consistency over 15 samples gives 6%, 14%, 42%, 4% (no improvement over standard prompting in the hard domains). The text concludes the verifier's soundness, not the critique content, carries the gain.
- Precursor 2310.08118 (Blocksworld, GPT-4, n = 100): the LLM verifier accepted 38 of 45 invalid plans (false-positive rate 84.45%, Table 2).
- Readout match: not matching. Task-dependent: a modest gain in Blocksworld where the LLM verifier is comparatively accurate.
- Relevance (inference): where the generator rarely produces a correct answer, an unsound verifier and voting both fail; this resembles the lab's W3 missing-evidence cases, but those are classification, not planning.

### B5. Tyen et al., "LLMs Cannot Find Reasoning Errors, but Can Correct Them Given the Error Location"
- Links: [arXiv 2311.08516](https://arxiv.org/abs/2311.08516), [PDF](https://arxiv.org/pdf/2311.08516). arXiv v3, June 2024; venue not stated in the extracted text. Grade B.
- Models: GPT-4, GPT-4-Turbo, GPT-3.5-Turbo, Gemini Pro, PaLM 2 Unicorn. Data: BIG-Bench Mistake, 2,186 chain-of-thought traces over 5 tasks with human-labelled first-error step (Tables 2-3, inter-rater agreement). Readout: step-level generated judgement.
- Result (Table 4): mistake-finding accuracy is low even for the best model, GPT-4 52.87% overall with direct step-level prompting; GPT-3.5-Turbo 14.78%. Given the true mistake location, backtracking improves downstream accuracy (Table 6), so the bottleneck is finding the error, not fixing it.
- Readout match: not matching; supports "detection is the weak step" for generative models.

### B6. Zhang et al., "Small Language Models Need Strong Verifiers to Self-Correct Reasoning"
- Links: [arXiv 2404.17140](https://arxiv.org/abs/2404.17140), [PDF](https://arxiv.org/pdf/2404.17140). arXiv v2, June 2024; venue not stated in the extracted text. Grade B.
- Models: LLaMA-2-13B-chat and Gemma-7B-it (both fine-tuned with the authors' SCORE procedure). Tasks: five datasets of math and commonsense reasoning, including CommonSenseQA and GSM8K. Readout: generated solution plus a verifier decision.
- Result (section 4, Figure 3, Table 2): refinement with an oracle verifier shows the upper bound; "a weak self-verifier can only bring minor improvements, if not misguiding the refiner"; with a GPT-4 verifier the refiner gains +8.3 on average across five datasets for Gemma-7B-it. The confusion matrices (Figure 3, GSM8K, LLaMA-2-13B) show the self-verifier misses many errors.
- Readout match: partial (small models, but fine-tuned and generative).

### B7. Tsui, "Self-Correction Bench"
- Links: [arXiv 2507.02778](https://arxiv.org/abs/2507.02778), [PDF](https://arxiv.org/pdf/2507.02778). Header: "Published as a conference paper at COLM 2026" (arXiv v3, Aug 2026). Grade A (single author).
- Setup (abstract): the same injected error is presented as user-attributed or model-attributed; 14 open-source non-reasoning models. Result: 64.5% blind spot (errors fixed when attributed to the user are missed when attributed to the model); appending "Wait" reduces the blind spot by 89.3%; 5,306 error-correction fine-tuning traces reduce it by 76.0%. Cause traced to post-training data composition.
- Readout match: not matching (generative, chat-format). Model sizes and task mix not extracted.
- Relevance (inference): suggests a re-ask that frames the first answer as the model's own is the weaker arrangement; a separate "blind" pass (lab VB) removes the attribution. Not tested on classification.

### B8. Laban et al., "Are You Sure? Challenging LLMs Leads to Performance Drops in the FlipFlop Experiment"
- Links: [arXiv 2311.08596](https://arxiv.org/abs/2311.08596), [PDF](https://arxiv.org/pdf/2311.08596). arXiv v2, Feb 2024; venue not stated in the extracted text. Grade B.
- Models: ten LLMs (open: Llama2-7b, 13b, Mistral-7b; proprietary: GPT-3.5-Turbo, GPT-4, Claude V2, PaLM Bison and others). Seven classification tasks (Table 1; includes logical fallacy, TruthfulQA, ARC, SciQ and others); zero-shot; English. Readout: generated answer in round 1, then a challenger such as "Are you sure?".
- Result (abstract, Figure 1, section 4): models flip their answer 46% of the time on average; accuracy falls on average by 17 points between first and final answer (Claude V2 -33.6, PaLM Bison -18.0, GPT-4 -7.0 on a 100-sample illustration). Fine-tuning on synthetic data reduces the drop by 60% for Mistral-7B but does not remove it.
- Readout match: partial (classification, but generated and sycophancy-driven).
- Relevance (inference): the lab's F2 wording names the first reading but is neutral, which is not a challenge. This paper is about challenge phrasing and does not test neutral phrasing.

## C. Verification chains and verifiers

### C1. Dhuliawala et al., "Chain-of-Verification Reduces Hallucination in LLMs"
- Links: [arXiv 2309.11495](https://arxiv.org/abs/2309.11495), [PDF](https://arxiv.org/pdf/2309.11495). arXiv preprint (Meta AI; the opened text carries no venue line, no code link). Grade B/C.
- Model: Llama 65B (few-shot, greedy; base model, not instruction-tuned), also compared with Llama 2 70B Chat, ChatGPT and PerplexityAI on longform. Tasks: Wikidata and Wiki-Category list questions, MultiSpanQA (closed-book), longform biographies (FactScore). English.
- Table 1: Wikidata precision 0.17 (few-shot) -> 0.29 (joint) / 0.36 (two-step) / 0.32 (factored); hallucinated entities 2.95 -> 0.68-0.98; Wiki-Category 0.12 -> 0.15 / 0.21 / 0.22. Table 2: MultiSpanQA F1 0.39 -> 0.48 (factored). Table 3: FactScore 55.9 -> 71.4 with factor-and-revise.
- Table 4 and text: verification questions generated by the model beat templated ones (0.16 versus 0.22 precision, factored); open verification questions beat yes/no ones, and the text says the model "tends to agree with facts in a yes/no question format whether they are right or wrong" (appendix 9, anecdotal). Limitations (section 6): does not remove hallucinations, only directly stated factual errors were addressed, bounded by the model's own knowledge.
- Readout match: not matching (open-ended generation with list outputs). The factored design (verify without seeing the first answer) is the generative counterpart of the lab's blind verification VB.
- Relevance (inference): the yes/no agreement bias fits the lab's VS result (a shown-answer check said "supported" for 14 of 17 false executions, lab item Q4-3), but the source evidence is anecdotal and generative.

### C2. Gou et al., CRITIC
- Links: [arXiv 2305.11738](https://arxiv.org/abs/2305.11738), [PDF](https://arxiv.org/pdf/2305.11738). Footer: ICLR 2024. Grade A.
- Models: text-davinci-003, ChatGPT (gpt-3.5-turbo), LLaMA-2 7B/13B/70B. Tasks: AmbigNQ, TriviaQA, HotpotQA (500 validation examples each), math program synthesis (GSM8K, SVAMP, TabMWP), toxicity reduction. Tools: web search, code interpreter, toxicity API.
- Table 1 (ChatGPT, AmbigNQ EM): CoT 51.8, self-consistency 52.6, CRITIC 62.0, CRITIC without tool 55.2, CRITIC with oracle-triggered correction 69.6. TriviaQA F1: CoT 79.2, CRITIC 81.7, CRITIC w/o tool 79.9. Table 2 (GSM8K, ChatGPT): PoT 72.5, CRITIC 78.2, w/o tool 77.0; text-davinci-003 GSM8K w/o tool 68.3 versus PoT 70.1 (-1.8). Section "Results": "CRITIC works better with more powerful LLMs".
- Readout match: not matching. External tools matter; verification without a tool is roughly equal to CoT or self-consistency.

### C3. Zhou et al., "Variation in Verification: Understanding Verification Dynamics in Large Language Models"
- Links: [arXiv 2509.17995](https://arxiv.org/abs/2509.17995), [PDF](https://arxiv.org/pdf/2509.17995). Header: "Published as a conference paper at ICLR 2026". Grade A (controlled, many models).
- Models: 14 open models from Qwen2.5 (3B, 7B, 72B), Qwen3 (4B, 8B, 32B), Llama (3B-70B), Gemma-2 (2B, 9B, 27B), Mistral, plus GPT-4o; generative verifiers (CoT then binary verdict). Tasks: 2,347 math, 1,196 knowledge-QA, 901 natural-language-reasoning problems (12 benchmarks); English.
- Findings (section 1 bullets, section 4.2 Figure 4): verifiers recognise correct answers on easy problems; true-positive rate is above 0.7 almost everywhere; true-negative rate falls as generator strength rises, e.g. Qwen2.5-72B verifier TNR 0.68 on Llama-3.1-8B solutions versus 0.17 on Qwen3-32B solutions (mathematics). The paper's explanation: strong generators produce coherent but wrong chains that the verifier accepts; weak generators make surface errors (supported by an LLM-judge analysis, Figure 33).
- Strong verifiers add little when the generator is strong (GPT-4o no better than Qwen2.5-7B in those regimes); Gemma2-9B plus a verifier closes 75.7% of the gap to Gemma2-27B (section 5.1).
- Readout match: not matching (generative verifier). Relevance (inference): errors that look internally consistent are the hardest to catch; the lab's blind-verification C1 check answered "yes" on none of K27's 17 false executions (lab item Q4-2), which is the same pattern in a different model class.

### C4. Saad-Falcon et al., "Shrinking the Generation-Verification Gap with Weak Verifiers" (Weaver)
- Links: [arXiv 2506.18203](https://arxiv.org/abs/2506.18203), [PDF](https://arxiv.org/pdf/2506.18203). arXiv v3 (Aug 2026). A NeurIPS 2025 proceedings listing and an ICML 2025 virtual-site listing appeared in search results; neither page was opened. Grade B.
- Models: Llama 3.3 70B Instruct (and 8B) as generator, K = 100 samples; verifiers are LM judges and reward models up to 70B; a distilled 400M cross-encoder. Tasks: MATH500, GPQA Diamond, MMLU College, MMLU Pro (and others in appendices). English.
- Table 1: first sample 68.4% average, majority vote at 100 samples 72.2%, best reward model 72.7%, naive ensemble of top-10 reward models 69.1%, self-verification 66.9% (below the first sample), Weaver 87.7% (+15.5 over majority vote), Pass@100 oracle 91.9%. Section 4.1: verifier accuracies spread by up to 37.5 points, so unweighted averaging lets weak verifiers dominate; weighted ensembles learned with labels beat naive ones by 3.6-7.8 points (Figure 2) but with only 0.01n labelled samples learned weights drop by 20.1% on average (Table 17; baseline of that drop not extracted), so label-free weights (weak supervision) are used.
- Section 5 and Figure 4: gains diminish as verifiers are added because of "correlated biases on hard examples". Section 6: a 400M cross-encoder trained on Weaver's pseudo-labels retains 98.7% of Weaver's accuracy gains at 0.03% of the verification compute.
- Readout match: partial. The distillation target is a cross-encoder scoring (query, response) pairs, the family of J/G, but it scores long generated responses for correctness, not option choice.
- Relevance (inference): evidence for "weak verifiers only help when weighted by estimated accuracy and when errors are not shared"; the lab's unweighted three-model vote (lab item Q4-4) is the naive configuration.

### C5. Brown et al., "Large Language Monkeys"
- Links: [arXiv 2407.21787](https://arxiv.org/abs/2407.21787), [PDF](https://arxiv.org/pdf/2407.21787). arXiv v3, Dec 2024; venue not stated in the extracted text. Grade B.
- Result (abstract and section 5): coverage (any sample correct) scales log-linearly with samples; where answers are automatically checkable (coding, formal proofs) this converts to accuracy, e.g. SWE-bench Lite 15.9% with one sample to 56% with 250. Where no automatic verifier exists, majority voting and reward models "plateau beyond several hundred samples" (about 100 per section 1).
- Readout match: not matching. It frames the limit of any second pass: the gain is bounded by the verifier.

## D. Elimination and top-k re-ranking

### D1. Ma and Du, "POE: Process of Elimination for Multiple Choice Reasoning"
- Links: [arXiv 2310.15575](https://arxiv.org/abs/2310.15575), [PDF](https://arxiv.org/pdf/2310.15575). The ACL Anthology listing (EMNLP 2023) appeared in search results but was not opened; the arXiv text has a code link. Grade A (per the listing).
- Model: FLAN-T5-XL (3B) in both steps; ChatGPT in an extension (section 5, not read in detail). Readout: option log-likelihood scoring with "multiple choice prompting" (MCP); step 1 masks options scoring below the average, step 2 chooses among the remaining options. Zero-shot, 100 sampled instances per task, 5 seeds (section 3).
- Table 1 (8 tasks): POE beats MCP on 5 (CQA 87.2 -> 89.2; SIQA 79.0 -> 82.0; LD 39.8 -> 53.6; CC 60.2 -> 72.2; SS 74.0 -> 76.6) and is slightly lower on the other three (ANLI 57.8 -> 55.0, DQA 67.8 -> 67.4, SIT 25.4 -> 25.2), which the text calls comparable. Table 2 (8 further tasks): POE gains on four logical-reasoning tasks (LA +18.8, IMT +13.2, CLD +8.7, RACO +6.8) and loses on four commonsense/social tasks (CAI -2.3, EIE -5.9, RS -6.1, IOM -6.2). Figure 3: three-shot results mixed (CC 79.6 -> 66.8, RACO 4.8 -> 50.4).
- Section 5.2: the best masking configuration keeps the correct option in 91.9% of cases; higher mask accuracy gives higher final accuracy.
- Readout match: partial. The scorer is an option scoring model (3B encoder-decoder), not a one-pass letter-logit read; it is closer to W12/A27 than anything generative.
- Replication/significance: seed standard deviations only; n = 100 per task. Task-dependent in both signs.

### D2. Zhu et al., "Option-ID Based Elimination For Multiple Choice Questions" (PoE_ID)
- Links: [arXiv 2501.15175](https://arxiv.org/abs/2501.15175), [PDF](https://arxiv.org/pdf/2501.15175). arXiv v3, May 2025; code link in the text; venue not stated. Grade B.
- Models: Qwen2.5-7B/14B/32B and Gemma-2-9B (pt and it), Gemma-3-12B/27B; readout: probabilities of option IDs (letters), the same class of readout as W12/A27 (matching). Tasks: MMLU-Pro (10 options), BIG-bench Abstract_Narrative_Understanding (10), Arithmetic (7) and Timedial (3). English.
- Method: one pass with a debiasing step (PriDe) on option-ID probabilities; options below the mean log-probability are removed from the list and the question is asked again (PoE_ID^log), or the lowest option is removed iteratively (PoE_ID^seq).
- Table 2 (average over six models): debiased MCP (D-MCP) -> PoE_ID^log: Timedial 84.4 -> 85.2 (+0.8), Arithmetic 69.6 -> 75.9 (+6.3), Abstract_Narrative 70.0 -> 72.1 (+2.1), MMLU-Pro 46.3 -> 48.9 (+2.6). The text attributes the small Timedial gain to fewer options.
- Table 1: without the debiasing step the method degrades when answer labels are randomised instead of all "A" (Qwen2.5-14B Arithmetic 74.2 MCP vs 65.1 elimination), so option-ID priors matter.
- Section 5.4 ("causes of EE failure") and appendix table: asking the model to name the incorrect option explicitly is much worse than elimination by ID probability, e.g. Gemma-3-12B Arithmetic D-MCP 64.4 versus 46.5 and 30.9 for the explicit-elimination variants. Section on error propagation: if the correct option is eliminated the later step cannot recover; elimination applied on top of D-MCP does not remove options that D-MCP answered correctly, as stated in 5.2.
- Readout match: matching for W12 and A27 (decoder, option-letter probabilities, restricted option set). Not matching for K27, J, G.
- Relevance (inference): this is the closest published analogue of the lab's top-k narrowing (D2, T3). It shows a narrowed re-ask changes letter-logit outputs and helps on questions with many options, using a debiased prior. The lab tested narrowing only on K27, where the first pass already scores each option independently (lab item Q4-8), so the K27 null does not transfer to W12/A27 either way.

### D3. Ma et al., "Large Language Model Is Not a Good Few-shot Information Extractor, but a Good Reranker for Hard Samples!"
- Links: [arXiv 2303.08559](https://arxiv.org/abs/2303.08559), [PDF](https://arxiv.org/pdf/2303.08559). arXiv v2, Oct 2023; venue not stated in the extracted text. Grade B (code not checked).
- Models: fine-tuned small models (RoBERTa-large based) as filter; Vicuna-13B, InstructGPT, GPT-4 as rerankers (Codex also in the direct-ICL baselines). Tasks: FewNERD (NER), TACREV (relation extraction), ACE05 (event detection), 5- to 100-shot. English. Readout: the LLM reads the top-3 labels plus "None" as a multiple-choice question and generates an answer with an explanation (section 5.1).
- Result (sections 4.2, 5.3-5.5): the LLM alone is worse than the fine-tuned small model with enough training data (Table 3); LLM reranking improves the hard (low-confidence) samples and degrades easy ones (Figure 5; "particularly for very easy samples"); a confidence threshold tuned on the validation set decides which samples are reranked (0.5%-10% of samples, Table 4, F1 change on the reranked subset: GPT-4 +8.8, +17.7, +26.8 and InstructGPT -3.1, +9.6, +20.1 for FewNERD, TACREV, ACE05). Average +2.4 F1 with InstructGPT (Table 3), cost down 80%-90% against direct ICL (Figure 7). Ablation (Table 5): chain-of-thought explanations, demonstrations and label filtering to the top-N each add a little; the last row (no CoT, no demos, all labels, all samples sent to the LLM) gives 12.5, 59.9 and 5.4 F1 on the three datasets, which the paper reads as the need for a difficulty filter.
- Readout match: partial. A confidence-gated top-k second stage with a generative reader; the first stage is a supervised scorer (closer to J, G, K27).
- Relevance (inference): the gain depends on the first stage being uncertain on its errors. The lab found K27's missing-evidence errors to be high-confidence (lab item Q4-10), the regime where this design would not trigger.

## E. Prompt and model ensembles, and error correlation

### E1. Arora et al., "Ask Me Anything"
- Links: [arXiv 2210.02441](https://arxiv.org/abs/2210.02441), [PDF](https://arxiv.org/pdf/2210.02441). arXiv v3, Nov 2022 (code link in the text); venue not stated in the extracted text. Grade B.
- Models: GPT-J-6B, BLOOM, OPT, EleutherAI models 125M-175B, T0 (3B); 20 benchmarks (SuperGLUE tasks CB, RTE, WIC, WSC and others). Readout: generated or scored answers to several rewritten prompts (QA format), aggregated.
- Section 3 intro and 3.1: majority vote over prompts has a "minor effect" (introduction: +4% for CB and -2% for RTE against the average prompt; section 3.1 baseline: vote 39.3% for CB, +2.2 over the average prompt, and 54.5% for RTE, -2). Section 4 (observations on prompt sets): best-to-worst prompt gap 9.6-12.1 points; error-set Jaccard index 39.9-42.2 against 0.25 expected for independent 60%-accuracy prompts; prompts are therefore correlated and unequal. Section 5.3: weak-supervision aggregation beats majority vote by up to 8.7 points and is no worse on 16 of 20 tasks. Table 2 (T0-3B, ten PromptSource formats): vote average +3.6, weak supervision +6.1.
- Readout match: partial (T0-3B scores options; the main method is generative).
- Replication: the point that a plain vote over wordings gains little is consistent with A1 Table 7 and the lab's wording vote (lab item Q4-1).

### E2. Hua et al., "Calibrating Black Box LLMs with Prompt Variations"
- Links: [PDF (workshop paper)](https://static1.squarespace.com/static/6266e3c48fb0751e74f60eb6/t/6671d62520d991084c200225/1718736422125/HSTSRrelm23.pdf). Venue not stated in the opened text; the file name suggests a 2023 workshop. Preliminary experiments. Grade C. The fuller "Calibrating Language Models via Augmented Prompt Ensembles" (OpenReview) was not accessible.
- Model: text-davinci-003 (RLHF-trained), token probabilities over the option answers. 900 questions: 100 from each of nine datasets (OpenbookQA, TruthfulQA, LogiQA, MMLU subjects). English.
- Method: the model writes paraphrases of the question and options; the option-token probability distributions are averaged; optionally temperature scaling.
- Result (Table 1, Figures 3-4): variations plus temperature scaling cut expected calibration error by over 70% and the Brier score by over 34% across datasets, with accuracy "roughly the same". Raw RLHF probabilities concentrate at 0 and 1; averaging over variants spreads them.
- Readout match: matching in kind (option-token probabilities averaged over prompts), but a different model class (a 2022 RLHF model) and tiny scale.
- Relevance (inference): an unsupervised way to make letter-logit confidences usable as a gate; the paper reports calibration, not error detection.

### E3. Guda et al., "Quantifying and Mitigating Selection Bias in LLMs: A Transferable LoRA Fine-Tuning and Efficient Majority Voting Approach"
- Links: [arXiv 2511.21709](https://arxiv.org/abs/2511.21709), [PDF](https://arxiv.org/pdf/2511.21709). arXiv v1, Nov 2025; venue not stated. Grade B (code availability not checked).
- Models: Qwen2.5-3B-Instruct, Phi-2, Llama-3.2-3B. Tasks: TeleQnA, MedMCQA, QASC, ARC. Readout: option-ID scoring over permutations (matching). English.
- Result (section 4.2, Table 2): a label-free permutation bias metric (PBM, answer changes over permutations) is highest on the hardest dataset (MedMCQA); majority voting over permutations drives PBM to 0.000 (by construction) and raises accuracy: Qwen2.5-3B TeleQnA 0.546 -> 0.571, ARC 0.804 -> 0.839, QASC 0.737 -> 0.947; Phi-2 QASC 0.630 -> 0.933; Llama-3.2-3B QASC 0.489 -> 0.837; MedMCQA gains only +0.01. The KV-cache variant saves time (up to 84%-89%) and over 90% of tokens.
- Limitation for Q4: the paper reports bias and accuracy, not whether permutation disagreement flags the errors; the lab's D2 order-disagreement flag (lab item Q4-9) has no direct published counterpart in the opened sources. Q3 evidence for permutation averaging is in [q3-order-and-format.md](q3-order-and-format.md).
- Readout match: matching (3B decoders reading option IDs).

### E4. Trad and Chehab, "To Ensemble or Not: Assessing Majority Voting Strategies for Phishing Detection with LLMs"
- Links: [arXiv 2412.00166](https://arxiv.org/abs/2412.00166), [PDF](https://arxiv.org/pdf/2412.00166). arXiv v1, Nov 2024. Grade B (single small study; no code link found).
- Models: GPT-3.5-Turbo, GPT-4, Gemini 1.0 Pro, PaLM 2, LLaMA 2 70B. Task: phishing URL versus legitimate, 1,000 balanced URLs from PhishStorm (500/500), batches of 50, three prompts (zero-, one-, two-shot). Readout: label text. English-script URLs.
- Result (sections 5.3-5.5, Figures 4-7): a prompt ensemble matches or beats the best single prompt for every model except GPT-3.5-Turbo, whose prompts differed in quality (0.85 vs 0.88 accuracy); the five-model ensemble failed to beat the best single model, GPT-4 (accuracy up to 0.946); removing the best and worst model gave an ensemble that improved. Abstract: ensembles suit members of equivalent strength; with a large spread, "opting for ensemble techniques is not recommended".
- Readout match: partial (classification with generated labels). Single task, n = 1,000, no significance test.

### E5. Kamen and Kamen, "Majority Rules: LLM Ensemble is a Winning Approach for Content Categorization"
- Links: [arXiv 2511.15714](https://arxiv.org/abs/2511.15714), [PDF](https://arxiv.org/pdf/2511.15714). arXiv v1, Nov 2025; authors from two companies (RingCentral, Relevad). Grade C.
- Setup (abstract, section 1): ten LLMs, zero-shot, IAB hierarchical taxonomy, 8,660 human-annotated samples; a consensus threshold fitted on human annotations (section on CDM). Headline: up to 65% F1 improvement over the strongest single model.
- What was not verified: significance, how much of the gain is category-inflation correction versus voting, and the base F1 values. Hierarchical multi-label output, not a closed option list.
- Readout match: partial. Use only as a statement that a multi-model consortium has been reported to help in label-set categorisation; it does not control for error correlation.

### E6. Kohli, "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels"
- Links: [arXiv 2605.29800](https://arxiv.org/abs/2605.29800), [PDF](https://arxiv.org/pdf/2605.29800). arXiv v1, May 2026, single author (Apple). Grade B.
- Models: nine frontier LLMs from seven families (including Qwen3-32B and Claude Sonnet 4.5) as judges. Tasks: three-way NLI on MNLI, SNLI and AlphaNLI with 100 human annotations per item (ChaosNLI-style). Readout: generated verdict. English.
- Result (abstract and section 1): the panel carries about 2 independent votes' worth of information (Kish effective sample size); panel accuracy is 8-22 points below the independent-voting ideal; on MNLI the panel (72.0%) equals the best judge (71.8%), on SNLI the best judge (84.2%) beats the panel (77.7%), on AlphaNLI 91.2% vs 88.7%. Smarter aggregation closes at most 11% of the gap, even with correct answers; the deficit holds across prompt variants, temperatures and chain-of-thought.
- Readout match: partial (classification-like NLI, but generative frontier models).

### E7. Kim et al., "Correlated Errors in Large Language Models"
- Links: [arXiv 2506.07962](https://arxiv.org/abs/2506.07962), [PDF](https://arxiv.org/pdf/2506.07962). The text states PMLR 267 (ICML 2025). Grade A (code link in the text).
- Data: responses of 349 LLMs on 12,032 multiple-choice questions (HuggingFace leaderboard), 71 LLMs on 14,042 questions (HELM), 20 LLMs on 1,800 resume-job pairs. The readout used by those leaderboards is not stated in the passages read.
- Result (section 3, Figure 1, Table 1): when both models are wrong they pick the same wrong option 42.3% (HuggingFace; random 12.7%) and 60% (HELM; random 33%) of the time on average; the share is higher for models from the same developer or architecture or of similar size, and higher for more accurate models. A regression with those features explains 34%-62% of the variation. Section 4: as a judge, a model inflates the accuracy of weaker models (and of same-provider models) because it accepts their shared wrong answers.
- Readout match: partial (multiple-choice tasks, readout unknown). Condition it documents: independence assumptions behind voting fail for the models most likely to be used.

## F. Self-agreement and self-preference in judging

### F1. Panickssery, Bowman, Feng, "LLM Evaluators Recognize and Favor Their Own Generations"
- Links: [arXiv 2404.13076](https://arxiv.org/abs/2404.13076), [PDF](https://arxiv.org/pdf/2404.13076). arXiv v1, Apr 2024 (code link in the text; venue not stated in the extracted text). Grade B.
- Models: Llama-2-7b-chat, GPT-3.5, GPT-4 (judges and sources); fine-tuning of Llama 2 and GPT-3.5. Tasks: summarisation on XSUM and CNN/DailyMail. Readout: pairwise choice with normalised token probabilities of the two options, and individual scoring.
- Results (section 1 findings, Figures 1-3, section 3): all three show self-preference; GPT-4 distinguishes its own summaries from two other models and humans with 73.5% accuracy; fine-tuning on 500 examples gives over 90% self-recognition; self-preference strength is linearly correlated with self-recognition across fine-tuned variants (Figure 1); section 3.4 controls for confounders by fine-tuning on other properties; the authors state the causal claim is suggestive.
- Readout match: not matching (summary judging). Note that the judge readout here is an option-token probability, but the item being judged is free text.
- Relevance (inference): a verifier of the same family as the generator is expected to favour the generator's answer; consistent with the lab's observation that blind terra checks and K27 shared the same error (lab item Q4-12), but that observation is in a different task.

### F2. Wataoka, Takahashi, Ri, "Self-Preference Bias in LLM-as-a-Judge"
- Links: [arXiv 2410.21819](https://arxiv.org/abs/2410.21819), [PDF](https://arxiv.org/pdf/2410.21819). arXiv v2, June 2025; venue not stated. Grade B.
- Models: GPT-4, GPT-3.5-Turbo, Vicuna-7b/13b, Koala, Llama 3.1 and others as judges of dialogue responses against human preferences. Metric (Definition 4.1, section 4.3): the difference between the judge's recall on responses humans rated favourably and on those humans rated unfavourably; GPT-4 0.520 (recall 0.945 versus 0.425, Figure 2 confusion matrix; Figure 1b).
- Result (sections 4-5, Figures 3-4): GPT-4 shows the largest self-preference; for the open models with obtainable perplexity, every model favours lower-perplexity responses more than humans do, whether or not the response is its own; the authors read this as bias towards familiar text, not self-recognition. Perplexity was not available for GPT-4 and GPT-3.5, so the explanation is not tested for the strongest case.
- Readout match: not matching. Contradicts F1's causal story in emphasis (familiarity versus self-recognition).

### F3. Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
- Links: [arXiv 2306.05685](https://arxiv.org/abs/2306.05685), [PDF](https://arxiv.org/pdf/2306.05685). NeurIPS 2023 Datasets and Benchmarks track (first-page footer). Grade A.
- Passage (section 3.3, "Self-enhancement bias", Figure 3b): GPT-4 favours itself with a 10% higher win rate than humans give it and Claude-v1 with 25%, but GPT-3.5 does not favour itself; the authors say limited data and small differences mean the study cannot determine whether self-enhancement exists.
- Readout match: not matching. Relevance: the original self-preference signal was inconclusive and became clearer only in later, more controlled work (F1, F2).

### F4. Haldar and Hockenmaier, "Rating Roulette: Self-Inconsistency in LLM-As-A-Judge Frameworks"
- Links: [ACL Anthology PDF](https://aclanthology.org/2025.findings-emnlp.1361.pdf) (Findings of EMNLP 2025, per the URL and the page numbers 24989-24990 in the opened PDF). Grade A.
- Models: Llama-3.1-70B-Instruct, DeepSeek-R1-Distill-Qwen, Qwen3-32B as judges, three independent runs with the same prompt. Benchmarks: SummaC (binary), SummEval (ordinal), MT-Bench; metric Krippendorff's alpha (section 3.3).
- Result: self-reliability on SummaC 0.33 (Llama), 0.63 (R1), 0.79 (Qwen3); MT-Bench 0.27, 0.51, 0.56; per-criterion variation (SummEval Fluency very low). Test-retest agreement under sampling is far from perfect for generative judges.
- Readout match: not matching. It concerns sampled generation; the lab's local systems have zero repeat noise (lab common caveat), so it does not apply to them, and it does not say that a stable answer is a correct one.

### F5. Ding, "When LLMs Agree, Are They Right? Auditing Self-Consistency and Cross-Model Agreement as Confidence Signals"
- Links: [arXiv 2607.08065](https://arxiv.org/abs/2607.08065), [PDF](https://arxiv.org/pdf/2607.08065). arXiv v2, Jul 2026, single author; de-identified data and pipeline released. Grade B with a provenance caveat: runs were produced by 53 students in a graduate course cohort, so they are independently submitted but not guaranteed independent (section 2).
- Models: gpt-4.1-nano, gpt-4.1-mini, gpt-4.1 at temperature 1.0, K = 50 samples; exploratory check on claude-haiku-4.5, claude-sonnet-4.6, claude-opus-4.7. Tasks: GPQA Diamond (four options) and AIME; 265,000 samples.
- Result (Table 1, sections 6-8): the rank correlation of self-consistency with majority-correctness is positive but weak (0.20-0.59, all positive and surviving Holm correction); it is highest for the mid tier, and worst for the most consistent frontier model: gpt-4.1 has consistency 0.89 yet majority accuracy 0.48 on GPQA, consistency at or above 0.8 on 77% of GPQA entries, 48% of which are wrong. Chain-of-thought improves accuracy but barely the agreement signal; a confidence-routed cascade is dominated by always using the mid-tier model (Table 9). Option-shuffle control (section 7, Figure 4, 48 cases): gpt-4.1-mini majority accuracy 0.50 -> 0.29 under shuffling (CIs overlap at n = 48), and "D" is under-selected (about 16%) in both orders, so part of the confidence is positional. Confident errors are partly shared across providers (48%-63% agreement on majority answers between gpt-4.1 and the Claude tiers).
- Readout match: not matching (sampled generation, temperature 1). The positional-prior result bears on any agreement-based gate over option letters.

## G. Readout and re-reading effects

### G1. Wang et al., "'My Answer is C': First-Token Probabilities Do Not Match Text Answers in Instruction-Tuned Language Models"
- Links: [arXiv 2402.14499](https://arxiv.org/abs/2402.14499), [PDF](https://arxiv.org/pdf/2402.14499); the ACL Anthology listing (Findings of ACL 2024) appeared in search results and was not opened. Grade A (code and classifier released per footnote 1).
- Models: Llama2-Chat 7b/13b/70b, Mistral-Instruct v0.1/v0.2 and others (six instruction-tuned models). Tasks: MMLU and OpinionQA. Measure: how often the first-token argmax differs from the answer in the generated text.
- Result (section 4, Table 3 on MMLU): mismatch 51.4% (Llama2-7b), 35.3% (13b), 13.2% (70b), 15.1% and 10.2% (Mistral v0.1, v0.2); accuracy by text versus first token 41.0 vs 34.9 (Llama2-7b), 47.6 vs 40.2 (13b), 55.6 vs 53.9 (70b); the abstract reports mismatch rates above 60% (the introduction names Llama2-7b-Chat), and that constraining the prompt (forcing an option letter or an example template) lowers but does not remove it.
- Readout match: contrast study. It supports saying that a second pass written in free text and a letter-logit read are different readouts (Q6-2 in lab-evidence). The lab's W12 and A27 are the first-token class.

### G2. Leviathan, Kalman, Matias, "Prompt Repetition Improves Non-Reasoning LLMs"
- Links: [arXiv 2512.14982](https://arxiv.org/abs/2512.14982), [PDF](https://arxiv.org/pdf/2512.14982). arXiv v1, Dec 2025, Google Research, marked "Preprint"; no code. Grade C.
- Models: seven models from Gemini, GPT, Claude and DeepSeek families (sizes undisclosed). Tasks: ARC Challenge, OpenBookQA, GSM8K, MMLU-Pro and three synthetic tasks; multiple-choice both with the question first and with options first. Readout: generation with reasoning disabled.
- Result (Figure 1 and section 2): repeating the whole prompt ("<QUERY><QUERY>") wins 47 of 70 model-benchmark pairs and loses none (McNemar p < 0.1 counted as a win); gains are small for question-first multiple choice and larger for options-first; with reasoning enabled it is neutral to slightly positive (5 wins, 1 loss in 28). Explanation given: in a causal model the second copy lets every prompt token attend to every other token.
- Readout match: partial. It is a prefill-only re-reading trick and applies in principle to decoder scorers (W12, A27), but no letter-logit measurement is reported, and the pointer head already conditions on the whole instruction (K27 note in lab-evidence).
- Relevance (inference): a cheaper "second look" than a second call. Untested on the lab's systems and not independently replicated in the sources read.

### G3. Taubenfeld et al., "Confidence Improves Self-Consistency in LLMs"
- Links: [arXiv 2502.06233](https://arxiv.org/abs/2502.06233), [PDF](https://arxiv.org/pdf/2502.06233). arXiv v2, Sep 2025; venue not stated in the extracted text. Grade B.
- Models: nine models, four datasets (MATH among them); confidence-weighted vote over sampled reasoning paths (CISC) with P(True)-style confidence.
- Result (abstract, Figure 1): reduces the number of samples needed by more than 40% on average; at 8 samples CISC surpasses 30-sample self-consistency for Gemma2-9B on MATH. They introduce within-question confidence evaluation, because standard calibration measures (ECE-style) do not predict which of several answers to the same question is right; "the most calibrated confidence method proved to be the least effective" within question.
- Readout match: not matching (sampled reasoning). Relevance (inference): calibration of the overall confidence distribution is not the property that makes a vote or a gate work; ranking within a question is.

## Cross-source observations by condition (inference unless a source is named)

1. **Generator-only second pass (self-correction, "are you sure", shown-answer verification).** Sources B1, B3, B4, B7, B8 and C3 agree that without external information the effect is zero to negative on average, with a strong dependence on prompt wording (B2: the same task goes from -9 points to +0.1 point depending on wording and temperature). The one controlled positive (B2) is below one point on average. Not tested on letter-logit, pointer-head or encoder systems.
2. **What produced gains.** An external check (C2 tools, B4 sound verifier, B6 GPT-4 verifier), re-sampling until an external verifier accepts (B4), a verifier set weighted by estimated accuracy (C4), answer narrowing by option-ID probability with a debiased prior (D2, mainly for 7-10 options), and confidence-gated reranking when the first stage is uncertain (D3). A common thread is that an independent signal enters the second pass.
3. **Voting.** Gains come from variance reduction on items where the modal answer is right (A1, A3, A4); items where it is wrong get worse (A3). Voting over wordings or prompt order gains much less than voting over samples (A1 Table 7, E1) and can lose (E1 RTE -2). Mixed-strength members drag the ensemble toward the weaker ones (A1 Table 10, E4); same-family and high-accuracy models share errors (E7, E6, E1 error Jaccard), so effective independent votes are far fewer than members. Weighted aggregation helps where unweighted does not (C4, E1).
4. **Calibration and gates.** Verbalised confidence is overconfident (A2); RLHF letter probabilities are extreme and prompt-variant averaging flattens them (E2, small and old); within-question ranking matters more than ECE (G3); agreement is a weak and regime-dependent proxy, worst for the most consistent frontier model, and partly positional (F5). Confidence gates only help if the errors are low-confidence (D3, with the lab's counter-observation for K27 in lab item Q4-10).
5. **Readout dependence.** Most evidence is sampled or chain-of-thought generation (not matching). Letter/ID-logit evidence exists for elimination (D2), permutation voting (E3) and prompt-variant averaging (E2). No opened source studies pointer-head or encoder second passes. The first-token versus text mismatch (G1) means free-text second-pass results should not be assumed to describe letter-logit readers.
6. **Judges.** Self-preference is reported with a family-level pattern (F1, F2, E7) but its cause is contested (self-recognition versus perplexity) and the original MT-Bench signal was inconclusive (F3). Self-agreement across runs is a measure of stability, not of validity (F4, F5).

## Contradictions, task dependence and non-replication

- Intrinsic self-correction: B1 (large drops) versus B2 (small gain with a fair prompt at temperature 0). The disagreement is about the prompt and temperature, not the data; both agree that the "find problems" wording lowers accuracy.
- POE: gains on logical tasks, losses on commonsense and social tasks, and mixed few-shot results (D1 Table 2, Figure 3); the 2025 option-ID follow-up (D2) reports gains on all four datasets with debiasing and larger models, so the sign may depend on the scorer and the debiasing step.
- Self-preference: F3 could not determine it; F1 finds it and argues causality; F2 finds it and attributes it to perplexity.
- Cross-context review ([arXiv 2603.12123](https://arxiv.org/abs/2603.12123), opened, not used as evidence in the table): its first version reported advantages over same-session review that did not hold up in the three-run average (the updated abstract says CCR is no longer significantly ahead of context-aware subagent review, p = 0.057, or a single same-session review, p = 0.26). One model (Claude Opus 4.6), 30 artifacts with 150 injected errors, code and documents; left out of the table as a weak non-replicated example of "fresh-session review".
- "Majority Rules" (E5) reports large gains from a multi-model panel, while E4, E6 and A1 Table 10 report no gain over the best member when members differ in strength or share errors. E5 did not control for either.

## Not opened or inaccessible

- Calibrating Language Models via Augmented Prompt Ensembles (OpenReview `L0dc4wqbNs`): page returned only a browser check. The earlier workshop version (E2) was read instead.
- ACL Anthology pages for POE (2023.emnlp-main.273) and "My Answer is C" (2024.findings-acl.441): listed in search results; the arXiv versions were read; venue statements for these two rest on those listings.
- NeurIPS 2025 and ICML 2025 pages for Weaver: listed in search results, not opened.
- Venue lines were not visible in the extracted text for A3, B2, B3, B5, B6, B8, C1, C5, D2, D3, E1, E3, E4, F1, F2, G3; they are graded B unless a peer-reviewed venue is shown in the opened text.
- Search results also listed Variation-in-Verification-adjacent and 2026 preprints (for example 2607.17384 on weighted ensemble lift, 2512.17630 on confidence-credibility weighted small-model ensembles) that were downloaded but not read to the passage level; they are not cited.

## Gaps for Q4 (as found, not proof of absence)

- No opened source tests a second pass on a pointer-head scorer (K27 class) or an encoder scorer (J, G class). The Weaver cross-encoder is a distillation target for long responses, not an option scorer.
- No opened source tests whether disagreement between an option order and its reverse predicts errors (the lab's D2 flag). PBM (E3) measures inconsistency but is reported against bias and accuracy.
- No opened source studies verification or re-asking for abstention classes (missing-evidence, conflicting-evidence) in classification with option lists; the closest are the NLI panel (E6) and verifier TNR results (C3), both generative.
- Prompt-variant votes on option-logit readers are covered only by E2 (a 2022 RLHF model, 900 questions) and by the permutation-vote work (E3).
- No opened source is in Japanese; all tasks are English.
- Several sources use GPT-3.5/GPT-4 or other closed models (A3, B1, B4, C1 comparison, D3, E4); model sizes are undisclosed there.
