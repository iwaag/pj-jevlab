# Q3 evidence: option order, selection bias and answer-symbol format

Access date for every link: 2026-10-03. Scope: study step2+step3 for Q3 ([plan](../../../devdocs/episodes/study/prompt_best_practice/p1/plan.md)). Lab results are in [lab-evidence.md](../lab-evidence.md) (Q3-1 to Q3-7) and are not repeated as evidence here.

## How the sources were read (limits)

- Pages were fetched with WebFetch, which returns a model-written summary of the page, not the raw text. Numbers below are as reported by that summary of the cited section. Table and section numbers marked "(approx.)" came from a summary that was inconsistent about numbering and must be re-checked in the original before being quoted in guidelines.
- Four PDFs could not be parsed (binary stream): the PDF forms of 2309.03882, 2308.11483, 2608.03091 and the SPUQ ACL PDF. 2309.03882 and 2308.11483 were read through ar5iv HTML, SPUQ through its arXiv abstract page. 2608.03091 was not read beyond its title (inaccessible).
- Grades: A = peer-reviewed controlled study; B = preprint with code or released data; C = vendor/author evaluation; D = practitioner report; E = guide/opinion. Where venue is stated in the source it is given. "Code" was only checked where noted.
- Readout match to lab: matching = option-ID/letter token probabilities read in one pass (W12, A27 style); partial = related scorer or readout; not matching = different readout class. Lab systems: W12/A27 option-letter logits, K27 pointer head, J/G encoders, L27 short generative.

## Summary table

| # | Source | Venue / grade | Readout studied | Match to lab | One-line result |
|---|---|---|---|---|---|
| 1 | Zheng et al. 2023/ICLR 2024 | ICLR 2024, A (code repo exists, not opened) | option-ID token probability | matching (W12, A27) | Selection bias is mainly token (ID) prior; PriDe removes it for ~5% extra cost |
| 2 | Pezeshkpour & Hruschka 2023 | arXiv preprint (later NAACL Findings 2024, not verified here), B/C | generation/probability on GPT-4, InstructGPT | partial | Reorder gaps 13-75%; sensitivity linked to top-2/3 uncertainty; voting over orders +2-8 pts |
| 3 | Wei et al. 2024 | arXiv, B | answer from 6 chat LLMs, FR on forward vs reversed | partial | Fluctuation rate higher on harder tasks; gray-box weighting +2-4 pts |
| 4 | Gupta et al. 2024 | arXiv, B | 5-shot MMLU, answer-letter scoring (exact readout not confirmed) | partial | All 10 models degrade on a second shuffle; math worst |
| 5 | Wang et al. 2024 ("My answer is C") | arXiv, B | first-token vs text answer | matching vs not matching (contrast) | first-token readout and text answer disagree 9-66% |
| 6 | Reif & Schwartz 2024 | arXiv, B | class label probability, 279 classification tasks | partial | Contextual calibration can worsen label bias on instruction-tuned models |
| 7 | Zhao et al. 2021 | ICML 2021, A | label probabilities, GPT-2/3 | partial | Contextual calibration up to +30 abs. on few-shot classification |
| 8 | Robinson & Wingate 2022 | arXiv, B | cloze scoring vs letter (MCP) | partial | Letter format wins only for models with symbol binding; PPA measures order invariance |
| 9 | Xue et al. 2024 | arXiv, B | letter selection after LoRA | partial (training) | Fine-tuning symbol binding cuts bias 5 pts at +0.4 to +1.8 acc |
| 10 | Wang et al. 2023 | arXiv, B | pairwise judge generation | not matching (judge) | 46-82% order conflicts; both-order averaging +9.8 to +14.3; entropy flag for human review |
| 11 | Hanna & Feng 2026 | arXiv, B | generation / independent option scoring vs PriDe / cyclic | partial | Removing position influence does not reliably raise accuracy; cyclic permutation helps |
| 12 | Position-bias permutation diagnostic 2607.20864 | arXiv, B | API generation | not matching | Position bias detectable only for 60-95% base accuracy |
| 13 | Alzahrani et al. 2024 / HF MMLU blog | ACL 2024 (A) / practitioner (D) | letter prob vs generation vs sequence likelihood | matching (readout dependence) | Same model 0.637 / 0.637 / 0.488 by implementation |
| 14 | Set-Encoder 2404.06912 | arXiv, B | cross-encoder listwise scorer | partial (encoder) | Listwise rerankers order-sensitive; permutation-invariant cross-encoder is not |
| 15 | GLiClass paper 2025 | arXiv, B/C | joint label-text encoder | partial (J, G family) | Reports attention to labels diminishes with label count; no order analysis |
| 16 | Teacher-student permutation debiasing 2403.13590 | arXiv, B | label token probabilities, FlanT5/Llama2 | matching/partial | Distilling permutation-averaged teacher: RACE++ 61.2 -> 68.1 |
| 17 | Set-Based Prompting 2406.06581 | arXiv, B | attention mask/positions | partial | Order-independent by construction; accuracy within reorder range |
| 18 | PA-GRPO 2603.21016 | arXiv, B | RL-trained 8B-32B, generation | not matching | Consistency 46.2% (PriDe) to 88.0% on MT-Bench |
| 19 | Predictable compression failures 2509.11208 | arXiv, B | evidence-chunk order, 7-9B | not matching | Order effects scale log(n); uniform permutation mixtures near-optimal |
| 20 | CoRA 2511.21860 | arXiv, B | consistency over altered choices | partial | Score drop 0.11 (GPT-4o) to 0.42 (small) when consistency required |
| 21 | SPUQ (2403.02509) | EACL 2024, A (abstract only) | text generation | not matching | perturbation UQ halves ECE on average |

Details follow. Each entry lists models, readout, task, language, n, metric, effect, significance and the passage read.

## 1. Zheng et al., "Large Language Models Are Not Robust Multiple Choice Selectors"
- Links: [arXiv abs](https://arxiv.org/abs/2309.03882), [ar5iv HTML (read)](https://ar5iv.labs.arxiv.org/html/2309.03882), PDF not parsable. Published ICLR 2024 (per arXiv listing and search result "Published as a conference paper at ICLR 2024"). Grade A.
- Models: 20 LLMs, LLaMA 7B-65B, LLaMA-2, Vicuna, Falcon, GPT-3.5-turbo. English. MMLU (4 options), ARC-Challenge, CommonsenseQA (5 options).
- Readout: probabilities of option ID tokens (A/B/C/D) for open models; matches W12/A27.
- Effects (sec. 1, Table 1 as summarised): moving the gold answer to D cost GPT-3.5-turbo 6.3 points (67.2 to 60.9); moving to A gained LLaMA-30B 15.2 points; LLaMA-30B picked A/B/C/D 34.6/27.3/22.3/15.8% with balanced gold. Recall standard deviation (RStd) used as bias measure.
- Cause analysis (sec. 2.4, approx.): removing IDs reduces RStd for most models; changing the symbol set (letters, lowercase, digits) barely changes bias; so token prior dominates, position effect is model- and task-dependent and less regular. Chain-of-thought and an explicit "do not be biased" instruction did not fix GPT-3.5-turbo (RStd 4.5-6.1 range, sec. 2.6, approx.).
- PriDe (sec. 3, Eq. 3 approx.): estimate the ID prior by cyclic permutations on about 5% of test samples, divide it out on the rest. Reported cost about 1.2x versus 4-5x for full permutation (sec. 4.1, Fig. 4). Gains with 5% budget: MMLU RStd -8.9 and +2.6 accuracy, ARC RStd -7.3 and +2.9, CSQA RStd -8.9 and +4.0 (Table 3). Prior transfers across domains with slight loss when domain gap is large (sec. 4.2, Fig. 5).
- Limits: models are 2023-era; the benchmarks are knowledge QA; no significance tests beyond averages in the summary; no test of letter vs key text beyond ID symbols; no encoder or pointer scorer.

## 2. Pezeshkpour and Hruschka, "Large Language Models Sensitivity to the Order of Options in MCQ"
- Links: [arXiv abs 2308.11483](https://arxiv.org/abs/2308.11483), [ar5iv (read)](https://ar5iv.labs.arxiv.org/html/2308.11483). Grade B (arXiv; I did not verify the later venue). 
- Models: GPT-4, InstructGPT (text-davinci-003). Tasks: CSQA (5), Big-Bench Logical Deduction (3), MMLU subsets abstract algebra, high-school chemistry, professional law (4). English.
- Zero-shot sensitivity gap (best vs worst of tested orders, Table 1): GPT-4 13.1 to 30%; InstructGPT up to 39.4% on abstract algebra and 75% maximum. Adversarial best/worst is an upper bound, not a random-reorder effect.
- Mechanism (analysis, Table 3): sensitivity is larger when the model is uncertain among top 2-3 options; placing the top two options first and last amplifies it, adjacent mitigates. The summary reports that most sensitive cases were ones where several answers were plausible.
- Mitigation (Table 5): majority vote over 10 random reorderings +2 to +8 points; "Multiple Evidence Calibration" inconsistent, sometimes lower. Few-shot gave only marginal gains (sec. 3.2).
- Relevance: supports order disagreement as a sign of an uncertain item, but evidence is correlational on 2023 API models; detection performance (AUROC etc.) was not read.

## 3. Wei et al., "Unveiling Selection Biases: Exploring Order and Token Sensitivity"
- Link: [arXiv HTML 2406.03009](https://arxiv.org/html/2406.03009). Grade B.
- Models: PaLM 2, Gemini Pro, GPT-3.5-turbo, LLaMA 2 7B/13B/70B (instruction-tuned). Six benchmarks (ARC-C, HellaSwag, MMLU 14,042, Winogrande, MathQA, OpenBookQA).
- Fluctuation rate (answers differing between forward and reversed option order): higher on harder (lower-accuracy) tasks (Table 1, Fig. 1). Commercial models more order- than token-sensitive in 17 of 18 cases; no consistent pattern across LLaMA 2 sizes.
- Mitigation: gray-box probability weighting (+2-4% on GPT-3.5), probability calibration (up to +14.29 on elementary math); a black-box two-hop strategy worked on 5 of 6 tasks but not Winogrande (negative, task-dependent).
- Readout: mixed (probabilities where available, otherwise answers). Partial match.

## 4. Gupta et al., "Changing Answer Order Can Decrease MMLU Accuracy"
- Link: [arXiv HTML 2406.19470](https://arxiv.org/html/2406.19470). Grade B.
- Ten models 7B-70B (Llama 2/3, Yi-34B, Mixtral, Falcon-40B, Mistral-7B, Gemma-7B); MMLU, two random shuffles, 5-shot. The proposed metric is "answered correctly in both orderings". Reported drop: Llama-3-70B 6.2%, Gemma-7B-it 26.5%, Falcon-40B-it 27.2%; math categories 40-42% for small models; history and law more resilient. Caveat: the summary does not make clear whether "drop" is in accuracy or in this stricter both-correct metric, so do not quote as an accuracy drop. Only 2 of 24 permutations per question.

## 5. Wang et al., "My Answer is C: First-Token Probabilities Do Not Match Text Answers"
- Link: [arXiv HTML 2402.14499](https://arxiv.org/html/2402.14499). Grade B (ACL Findings 2024 per memory, not verified here).
- Llama-2-Chat 7/13/70B, Mistral-Instruct v0.1/v0.2, Mixtral-8x7B. OpinionQA 414 questions and MMLU. First-token log-prob ranking vs classifier-extracted text answer. Mismatch 13.3-66.2% (OpinionQA), 9.0-51.4% (MMLU). Llama-2-7b MMLU accuracy 41.0 (first-token) vs 34.9 (text). Refusals explain much of the gap; larger models align better; example templates increased mismatch.
- Readout lesson: first-token logits (W12/A27 style) and generated text (L27 style) can disagree on the same prompt. Matching for the first-token side, not matching for text-side conclusions on logits.

## 5b. Companion: Instruction-tuned models are more robust than they seem
- Link: [arXiv HTML 2404.08382v1](https://arxiv.org/html/2404.08382v1). Grade B.
- Llama2-7b/13b-Chat, Mistral-7b-Instruct-v0.2, Gemma-7b-it; MMLU (and OpinionQA validation). Text answers show lower RStd than first-token probabilities, especially when text/token mismatch is high (Gemma 56.8%, Llama2-7b 51.4%, Mistral 10.2%; Table 4, Fig. 2). PriDe-debiased first-token still worse than text when mismatch above 50% (secs. 3.3, 3.5).
- Implication: part of the "selection bias" measured on instruction-tuned models via first-token logits is a readout artifact. This partially undercuts the size of the effects in source 1 for chat models read by logits, and is directly relevant to W12 (chat-tuned, letter logits).

## 6. Reif and Schwartz, "Beyond Performance: Quantifying and Mitigating Label Bias in LLMs"
- Link: [arXiv HTML 2405.02743](https://arxiv.org/html/2405.02743). Grade B.
- Ten LLMs 7B-40B (Llama-2 7B/13B base and chat, Mistral 7B base/instruct, Falcon 7B/40B), 279 Super-NaturalInstructions tasks (264,176 examples), English. Metrics BiasScore (probability) and RSD (class-wise accuracy). Contextual calibration (CC) "substantially worsens" label bias for instruction-tuned models; domain-context calibration mixed; proposed leave-one-out calibration beats both (Fig. 3). Negative result for calibrate-before-use on instruction-tuned models. Label bias here is class-label prior, not option position; partial match.

## 7. Zhao et al., "Calibrate Before Use"
- Link: [arXiv abs 2102.09690](https://arxiv.org/abs/2102.09690). ICML 2021, grade A. GPT-2 and GPT-3. Contextual calibration with content-free inputs (for example "N/A") estimates answer prior; up to 30.0 absolute accuracy, reduced variance across prompt format and example order. Read abstract only. Models are pre-instruction-tuning; see source 6 for the negative result on tuned models.

## 8. Robinson and Wingate, "Leveraging LLMs for Multiple Choice Question Answering"
- Link: [ar5iv 2210.12353](https://ar5iv.labs.arxiv.org/html/2210.12353). Grade B (published at ICLR 2023 per my background knowledge; not verified here).
- GPT-3 175B, Codex, InstructGPT (Curie, Davinci), GPT-2 1.5B, Jurassic-1 Jumbo, CodeParrot; 20 datasets. Defines multiple-choice symbol binding (MCSB) and PPA (proportion of plurality agreement over option permutations; chance 1/n). MCP (letters) beats cloze (score each answer text independently) by about 8.3 (zero-shot) to 12.2 (one-shot) points with Codex, max 44.3 on Cosmos QA, but only for models with high PPA: code/instruction training is needed.
- Format lesson: the letter format is not free; small or base models bind symbols poorly and cloze scoring (independent per option, no order dependence by construction) can be better. Partial match to encoders that score each label independently.

## 9. Xue et al., "Strengthened Symbol Binding Makes LLMs Reliable MC Selectors"
- Link: [arXiv HTML 2406.01026](https://arxiv.org/html/2406.01026). Grade B. LLaMA2-7B/13B with LoRA; MMLU and CSQA. Point-wise negative samples reduce selection bias 5.0 points (MMLU, 7B), accuracy +0.4 to +1.8, worst-order accuracy +3.9 to +4.9. Training-time only; English; two sizes.

## 10. Wang et al., "Large Language Models are Not Fair Evaluators"
- Link: [arXiv HTML 2305.17926](https://arxiv.org/html/2305.17926). Grade B. Pairwise judging on 80 Vicuna-benchmark questions; GPT-4 and ChatGPT as judges. Swap conflict: GPT-4 46.3% (Vicuna vs ChatGPT) and 5.0% (vs Alpaca); ChatGPT 82.5% and 52.5%. Win rate of a model swung 2.5% to 82.5% by position. Both-order averaging plus multiple evidence: +9.8 (GPT-4), +14.3 (ChatGPT) accuracy (Table 4). Entropy of the both-order outcome flags cases for human review: ChatGPT with 20% human cost 71.3% accuracy.
- Relevance: the nearest published analogue of the lab's D2 order-disagreement flag, but on pairwise judging with generative judges. Partial/not matching.

## 11. Hanna and Feng, "Accuracy and Order Sensitivity Diverge Under Label-Free Strategies"
- Link: [arXiv HTML 2608.11947](https://arxiv.org/html/2608.11947). Grade B (single run per condition, no variance estimate; stated).
- GPT-4.1 mini, Gemini 2.5 Flash, Llama 3.1 8B, Qwen 2.5 7B (API and local); MMLU 1,000 and ARC-C 1,000, four options, temperature 0. Two-stage (generate then match) lowers end-to-end accuracy in 11 of 12 model-benchmark pairs; independent per-option scoring lowers it in 8 of 11; GPT-4.1 mini MMLU flip rate 21.6 to 11.8 while accuracy 81.8 to 80.1 (sec. 4.4). Visible options plus a matcher is within noise of baseline (sec. 4.6, Table 11). Cyclic permutation improves 5 of 6 pairs on each benchmark. Takeaway: lower position sensitivity is not the same as higher accuracy; permutation averaging helped, option-hiding did not. Includes a PriDe baseline (numbers not extracted).

## 12. Position bias is hidden behind ceiling effects (2607.20864)
- Link: [arXiv HTML](https://arxiv.org/html/2607.20864v1). Grade B (single author, small n). gpt-4o-mini, claude-haiku-4-5, gemini-2.5-flash, grok-3; five MMLU subjects x 50 questions x 24 permutations = 24,000 calls; chi-squared and Cramér's V. Position bias only statistically detectable in roughly 60-95% base accuracy; frontier models showed "no signal", which is not proof of no bias. Generation readout; not matching. It is a power warning for diagnostics: tiny n and ceiling accuracy hide bias (relevant to the lab's 60-case order diagnostics).

## 13. Readout dependence: Alzahrani et al. and the Hugging Face MMLU write-up
- Links: [Alzahrani et al. abs 2402.01781](https://arxiv.org/abs/2402.01781) (ACL 2024, grade A; abstract only: reordering choices or changing the selection method shifted rankings by up to 8 places); [Hugging Face blog](https://huggingface.co/blog/open-llm-leaderboard-mmlu) (grade D, read). LLaMA-65B MMLU: 0.637 (original, letter probabilities) and 0.637 (HELM, generated text) vs 0.488 (EleutherAI harness, full answer-sequence likelihood, Jan 2023). Falcon-40B and GPT-NeoX-20B rankings also change. 2023 base models. Matching for the letter-probability readout.

## 14. Order effects in cross-encoders / rerankers
- Set-Encoder, [arXiv HTML 2404.06912](https://arxiv.org/html/2404.06912). Grade B. Listwise rerankers (RankGPT-4o, RankZephyr 7B, LiT5-Distill 220M) show order-dependent effectiveness (rank-change heatmaps, Fig. 2; reverse-ideal input hurts LiT5; windowing creates step patterns). A 110M/330M ELECTRA cross-encoder with inter-passage attention and per-passage position ids restarting at zero is permutation invariant by construction and matches listwise effectiveness (TREC DL19/20 nDCG@10 about 0.73-0.79, Fig. 3). Pointwise monoELECTRA is order independent by construction but slightly lower (0.720-0.733 BM25 setting). Retrieval task, not choice among labels. Partial match for encoders: a pointwise cross-encoder cannot show order bias, a joint listwise one can.
- A 2026 paper on listwise reranker position bias ([2608.03091](https://arxiv.org/pdf/2608.03091)) was found but is inaccessible (PDF not parsable); not used.
- No source on order effects in span-pointer scorers (K27 style) was found.

## 15. Label order in joint label-text encoders (GLiClass family)
- [GLiClass, arXiv HTML 2508.07662v1](https://arxiv.org/html/2508.07662v1). Grade B/C (authors' own model). Sizes 32.7M-439M (Table 2), DeBERTa v3 and ModernBERT backbones. The paper does not analyse label order. Sec. 2.3.3 notes attention between label tokens and the text diminishes as number of labels grows. A search-snippet claim that "performance on one label can be influenced by order and number of other labels" could not be traced to a passage in the paper and is not used. No published label-order test of GLiNER or GLiClass was found.

## 16. Permutation-averaged teacher distillation
- [arXiv HTML 2403.13590](https://arxiv.org/html/2403.13590). Grade B. FlanT5 3B/11B, Llama2-chat 7B/13B teachers; DeBERTa/RoBERTa 110M-330M students; label token probabilities. RACE++, CosmosQA, ARC-C, SummEval comparative assessment. Error-correction student: RACE++ 68.1 vs 61.2 for biased baseline (Table 2). Shows that an encoder student can absorb a debiased target. Partial.

## 17. Set-Based Prompting
- [arXiv HTML 2406.06581](https://arxiv.org/html/2406.06581). Grade B. GPT-2 1.5B, Llama 2 7B/13B, Llama 3 8B, Mistral 7B. Modifies attention mask and positions so options are order independent by construction (Theorem 1, sec. 3.3); accuracy typically within the best/worst reorder range (Figs. 3-4), out-of-distribution risk for instruction-tuned models (sec. 4.3, Fig. 5). Requires model internals; not applicable to a hosted API.

## 18-21. Other items read
- PA-GRPO, [arXiv HTML 2603.21016](https://arxiv.org/html/2603.21016v1): Llama-3.1-8B, Qwen3-8B, Qwen3-32B trained with permutation-consistency RL; MT-Bench consistency 46.2% (PriDe) to 88.0%; English, open weights only. Training-time, generation. Not matching.
- Order sensitivity of evidence chunks, [arXiv HTML 2509.11208](https://arxiv.org/html/2509.11208): Qwen2-7B and Llama-3.1-8B, 3,059 items; order effect grows with log n; uniform mixtures over 16 permutations capture the gain; abstention gate. Task is binary evidence adjudication. Not matching.
- CoRA, [arXiv HTML 2511.21860](https://arxiv.org/html/2511.21860): eight models 7-8B plus GPT-4o; MedQA 1,273, MMLU 14,042, ARC-C 1,172, TruthfulQA 817; requiring consistency over shuffled/altered choices cuts MedLlama3 0.74 to 0.32 and GPT-4o by 0.11. Evaluation-metric proposal.
- SPUQ, [abs 2403.02509](https://arxiv.org/abs/2403.02509), EACL 2024 (abstract only): input perturbation (paraphrase, dummy tokens) aggregated to cut ECE by 50% on average; generation tasks, not option order.
- CalibraEval, [abs 2410.15393](https://arxiv.org/abs/2410.15393) (ACL 2025 per search listing): pairwise judge debiasing by order-preserving distribution alignment; abstract only; numbers in search snippet (ChatGPT RewardBench 65.27 to 67.13, RStd 16.79 to 5.51) not verified in the paper. Judge task.

## Cross-source synthesis for Q3 (with grades; not guidelines)

1. Option-position and ID-token biases are real and large on 2023-era open and API models read via letter probabilities (sources 1, 2, 3, 4). Effect sizes in the tens of points are best-case-minus-worst-case or small/base models; typical random-reorder effects are a few points (source 1 Table 1: 6 to 15 points for one answer move; source 4: 6-27 depending on metric). Not generalisable to modern instruction-tuned models by default.
2. Effects shrink with model strength and are task-dependent: bigger gaps on harder, lower-accuracy tasks (3), uncertainty-driven (2), and small diagnostics lose power at high accuracy (12). A negative or flat result on a strong model is expected, not a contradiction. The lab's finding that W12, A27, K27 flip 1-3 of 60 is compatible; J flipping 21 of 60 is the outlier and no matching published encoder result was found.
3. Countermeasures with evidence: permutation averaging (1, 2, 10, 11, 19; cost x n); PriDe prior estimation on about 5% of items (1; one source with an ICLR venue, replicated mainly as a baseline in others; 18 uses it as a weaker baseline); both-order averaging for pairwise (10); distillation (16) and training (9, 18) when weights are available; Set-Based Prompting and permutation-invariant cross-encoders (14, 17) when architecture is controllable. Simple prompt fixes (CoT, "avoid bias" instruction, few-shot) did not help (1, 2).
4. Calibration: contextual calibration helped GPT-3 era models (7) but worsened label bias on instruction-tuned models (6). PriDe is permutation-based, not content-free-input-based, and was shown for ID-prior removal only. No evidence for calibrating pointer or encoder scorers was found.
5. Symbol and format: swapping letters for lowercase or digits changed bias little (1); the letter format needs symbol binding that base models lack, so cloze scoring can win for them (8); first-token letter readout can disagree with generated text by 9-66% on chat models and inflate apparent selection bias (5, 5b); implementation of the readout changed LLaMA-65B MMLU by 0.15 (13). Letters versus key text (as in the lab's key naming) was not directly tested by any source read.
6. Order disagreement as an uncertainty flag: supported indirectly. Sensitivity associates with top-choice uncertainty (2); both-order disagreement entropy sent ambiguous judge cases to humans at 20% cost with accuracy parity to humans (10); Hanna and Feng warn that fewer flips need not mean more correct (11). No source tested order disagreement as an error detector on a 3-4 option pointer or letter-logit classifier with a precision/recall number. The lab's 5 of 6 fired cases wrong has no published comparator.
7. Lower sensitivity does not imply accuracy gain (11), and flip-rate metrics grow with the number of permutations tried (2, upper bound).

## Negative and task-dependent results recorded
- Calibrate-before-use worsens label bias on instruction-tuned models (6).
- Two-hop black-box mitigation ineffective on Winogrande (3).
- Multiple Evidence Calibration inconsistent (2).
- Hiding options and scoring independently lowered accuracy in most pairs (11).
- Bias undetectable for accuracy above about 95% or below 60% in small samples (12).
- PriDe-debiased first-token logits remain worse than text answers when mismatch is above 50% (5b).
- Letter format harms models without symbol binding (8).
