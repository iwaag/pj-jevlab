# Q5 evidence: abstention, "none of the above" and missing-information detection

Step2/step3 note for `devdocs/episodes/study/prompt_best_practice/p1`. Access date for every link: **2026-10-03**.
Every row here is an **external source**; the lab's own results are in [../lab-evidence.md](../lab-evidence.md) (Q5-1 to Q5-11) and are only cross-referenced.

## How the sources were read

- **Full text read:** arXiv PDFs were downloaded and searched in full text. The cited section, table or figure was read. Marked `full text`.
- **Fetch summary only:** HTML vendor pages, model cards and GitHub READMEs were read through the fetch tool, which returns a summary written by a small model. Claims from these are paraphrases of that summary. Marked `summary`. Where the text was also downloaded raw (Kev README, Decider README), it says `raw text`.
- "Readout match" is against the lab systems: option-letter logits W12/A27, pointer head K27, encoders J/G, short generative L27.
- Grades: PR = peer-reviewed controlled study; PP = preprint (with code where stated); V = vendor or author evaluation; PR-prac = practitioner report; G = guide or opinion.

## Summary of what the evidence says (for step4)

| Claim | Support | Readout match | Status |
|---|---|---|---|
| Models given a closed option list rarely pick "none"; when the correct answer is "none of the above", accuracy drops sharply (30-50% on MMLU across 28 LLMs; about 2x lower for some phrasings). | S1, S2, S3, S4 (several independent groups) | Partial. S1 (Kadavath) used letter logits on base/RLHF LMs; S2 token-probability confidence only; others generative | Established on generative and letter-logit LMs. Not tested on pointer or encoder scorers |
| An explicit abstain clause raises abstention but costs coverage (answerable accuracy falls). Size of the trade-off depends on the model; small models may not follow it. | S3, S5, S6 | Not matching (generative, zero-shot chat models) | Established for chat LLMs, the cost side is a measured trade-off |
| The wording of the abstain option itself matters (same models, 2x spread by phrasing), and a bare added option can trigger abstention independent of its meaning. | S2 Table 3; S7 | Not matching (generative) | Plausible; two sources, one is a recent preprint |
| Missing-information detection is the weak case: models answer instead of saying "not sure" (0.7-4.6% "not sure" where 41.8% was correct; recall 13% on omitted-context items). | S8, S9, S5 | S9 uses option logprobs (partial match); S8 generative | Established that it is hard; matches the lab's W3 finding |
| Chain-of-thought and reasoning help abstention in some settings (S3, S4) and not in others (S5, S9, S10). | S3, S4, S5, S9, S10 | Not matching (all need generated reasoning) | Open, task- and model-dependent. Not applicable to one-pass readouts |
| Max-softmax probability over option letters predicts correctness (AUROC), so a threshold can abstain; raw probabilities are miscalibrated in chat models, better in base models. | S11, S1 | **Matching** for W12/A27 (letter logits); not tested for pointer heads | Established for letter-logit readout on chat/base LLMs; threshold needs a small labelled set (20 items per dataset in S11) |

## Source records

### S1. Kadavath et al. 2022, "Language Models (Mostly) Know What They Know"
- Link: https://arxiv.org/pdf/2207.05221 (arXiv 2207.05221). Grade: PP (Anthropic; widely cited original). Read: full text, Section 3.1 and Figure 7 (intro bullets).
- Models: Anthropic pretrained LMs up to 52B; RLHF policies discussed separately. **Readout: option-letter probabilities with visible lettered options (matching in kind to W12/A27).**
- Task: MMLU, TruthfulQA, BIG-bench MC; English. n: not extracted (benchmark-level).
- Finding: large models are well calibrated on lettered multiple choice; **replacing the final option with "none of the above" reduces accuracy and calibration significantly** (Fig. 7), whereas True/False self-evaluation stays calibrated. RLHF models look miscalibrated but are fixed by a temperature change (Fig. 9).
- Effect size: not quoted here (figure only). Significance: reported as "significant" qualitatively. Replication: the 30-50% drop in S2 reproduces the direction on 28 other LLMs.
- Readout match: **partial to matching** (letter readout, but pretrained LMs from 2022, not trained decision models).
- Caveat: age (2022); 52B scale; the replacement can make some questions ambiguous (the paper says so).

### S2. Tam et al. 2025, "None of the Above, Less of the Right"
- Link: https://arxiv.org/abs/2503.01550 (HTML https://arxiv.org/html/2503.01550v1). Grade: PP. Read: full text, abstract, Section 5.1 to 5.5, Table 3, Table 4.
- Models: 28 LLMs, 1.5B to 671B (Claude 3 Haiku, Gemini 1.5/2.0, GPT-4o mini, DeepSeek-V3, Llama 3/3.1/3.2, Qwen 2.5, Gemma-2, Mistral, Mixtral, Yi-1.5, SOLAR). **Readout: 0-shot chain-of-thought generation, temperature 0**; token probability of the selected letter used only as a confidence proxy (one model).
- Task: MMLU, 14,042 questions in 57 subjects; NA variants built for applicable questions; English.
- Result: NA as the correct answer causes a **30-50% performance drop regardless of scale** (abstract; example DeepSeek-V3 65.7% vs 90.8% baseline). NA as a distractor leaves accuracy near baseline. Domain dependence: mathematics 14.6% drop, business ethics 48.1%.
- **Wording of the NA option (Table 3, three models):** "Answer not found" 0.134 / 0.224 / 0.376 (LLaMA-8B / Gemini-1.5-flash / gpt-4o-mini), "No valid options" 0.216 / 0.339 / 0.411, "None options are correct" 0.256 / 0.358 / 0.494, "None of the above" 0.323 / 0.317 / 0.476. The paper calls the models "moderately sensitive" and says rankings are preserved; for LLaMA-8B the spread is 2.4x.
- Fine-tuning (Table 4, LLaMA-3-8B): NA-as-answer 28.5% baseline to 49.5% (SFT) and 57.7% (DPO) on MMLU, but NA-as-distractor falls from 64.1% to 55.0% / 54.7%: gaining abstention cost standard accuracy.
- Significance: ANOVA used for the test-reliability analysis only; the 30-50% drop is descriptive across models.
- Readout match: **not matching** (CoT generation). Task-dependence recorded above.

### S3. Madhusudhan et al. 2025, "Do LLMs Know When to NOT Answer?" (Abstain-QA)
- Link: https://arxiv.org/abs/2407.16221. Grade: peer-reviewed (COLING 2025, per the citation in S5's reference list; the arXiv copy read is v2). Read: full text, Section 4.1, Section 5, Tables 1-3.
- Models: GPT-3.5 Turbo, GPT-4 Turbo, GPT-4 32k, Mixtral 8x7b, Mixtral 8x22b, Mistral 7b (Instruct). **Readout: generation in a zero-shot MCQ with an explicit "IDK/NOTA" option** (positions randomised).
- Task: MMLU (1000 MCQ pairs, 100 questions in each of 10 subjects), Pop-QA (100 questions in each of 10 relations), CQA (Carnatic-music, n not read). English. Answerable and unanswerable halves (unanswerable gold = IDK/NOTA).
- Design: three clauses on the same question. Standard (option shown, no instruction), Abstain Clause (mentions consequences of a wrong answer), Extreme Abstain Clause (emotional pressure).
- Effect on CQA, Base task prompt (answerable accuracy AAC, unanswerable accuracy UAC, Table 1): GPT-4 Turbo UAC 32.8, 50.8, 62.2 and AAC 48.0, 42.6, 38.4 for Standard, AC, EAC. Mixtral 8x22b UAC 27.3, 65.1, 54.2; AAC 32.8, 24.0, 26.6. GPT-3.5 Turbo UAC only 0.6, 10.2, 7.1. Mistral 7b UAC 3.5, 35.5, 45.1; AAC 25.7, 20, 15.5.
- Reading: the clause raises abstention of unanswerable items but **answerable accuracy falls** (coverage cost). EAC helps larger models, hurts or does not help smaller ones ("EAC's increased complexity can hinder these models' adherence").
- Option position (Table 2, GPT-4 Turbo and Mistral 7b, MMLU): moving the correct answer between middle and edge positions changes answerable accuracy slightly; UAC and abstention rate change negligibly.
- CoT raised UAC and abstention rate in most cells (for example MMLU GPT-4 Turbo Base-Standard UAC 21.6 vs CoT 42.6 in the shown rows). Verbal confidence did not consistently beat the base setting. Few-shot (Table 3) helped GPT-4 Turbo, hurt Mistral 7b.
- Significance/replication: single runs, no intervals reported in the passages read.
- Readout match: **not matching** (generative). The qualitative trade-off (abstain instruction trades coverage for abstention) is the same structure as the lab's terse/abstain wording question (lab Q5-10).

### S4. Góral et al. 2024-25, "Wait, that's not an option"
- Link: https://arxiv.org/abs/2409.00113 (PDF https://arxiv.org/pdf/2409.00113, v3 June 2025). Grade: PP (code released; venue not confirmed in the copy read). Read: full text, Tables 1-4, Sections 3-4, Appendix B.
- Models: GPT-4o, o1-mini, GPT-4o mini, Claude 3 family and 3.5 Sonnet, Gemini 1.5, Llama 3.1 8B/70B/405B, Qwen2/2.5 (7B to 32B, base and instruct), DeepSeekMath-7B (base, instruct, RLHF). **Readout: "Respond solely with A or B" generation; options all wrong, no NOTA option.**
- Task: Basic Addition Dataset (n not read), MMLU 400 questions, MedMCQA 200; English. Metric: reflective-judgment score (refuse or give the unlisted correct answer).
- Instruction conditions (Table 3): Easy ("The answer may not be in the options."), Standard (nothing), Hard (must pick one). Table 1, arithmetic: GPT-4o Easy 0.9% / Standard 0% / Hard 0%; Claude 3.5 Sonnet 99.0 / 0.1 / 0; Gemini 1.5 Pro 97.3 / 64.5 / 57.3; Llama 3.1-405B 100 / 42.5 / 91.5; Llama 3.1-8B 0 in all three; Qwen2.5-7B base 49 / 40.9 / 33.6 vs Qwen2.5-7B-Instruct 1.8 / 0 / 0.
- Findings: **the same one-sentence warning gives 0% for some models and about 100% for others**; aligned/instruct versions are often worse than base; ability grows with size inside a family (Llama 8B to 405B, Fig. 4); high-stakes framing did not help (Fig. 3). Prompt variants (Table 4, level 2): GPT-4o-mini 0.07% with the original prompt vs 14.89% averaged over six paraphrases; Llama 3.1-405B 42.5 vs 80.16; Qwen2-Math-7B 98.0 vs 82.25. Removing the instruction raised reflective judgment (Fig. 6). CoT raised it by more than 85 points for the models tested (Fig. 6) but "is not a universal solution".
- Significance: correlation between arithmetic accuracy and reflective judgment r about 0.7, p<0.05; other results descriptive.
- Readout match: **not matching** (generation). Useful as a negative result: instruction wording effects are model-specific and prompt-paraphrase-sensitive.

### S5. Kirichenko et al. 2025, "AbstentionBench"
- Link: https://arxiv.org/abs/2506.09038 (https://arxiv.org/html/2506.09038v1). Grade: PP with code (https://github.com/facebookresearch/AbstentionBench); search results list it as a NeurIPS 2025 poster (that page not opened). Read: full text, abstract, Sections 3-4.4, Figures 3, 7, 8.
- Models: 20 LLMs (GPT-4o, o1, Gemini 1.5 Pro, Llama 3.1 8B/70B/405B, Llama 3.3 70B, Qwen 2.5 32B, Mistral 7B, OLMo 7B/Tulu checkpoints, s1.1 32B, DeepSeek R1 Distill Llama 70B). **Readout: free generation, 4k tokens, temperature 0.8; LLM judge (Llama 3.1 8B, 88% agreement with humans).**
- Task: 20 datasets, about 35,000 unanswerable questions (unknown answer, false premise, stale, subjective, underspecified context, underspecified intent); English. Metric: abstention recall (precision and F1 in the appendix).
- Findings: scale has almost no effect (Fig. 3b, Llama 8B/70B/405B). Reasoning fine-tuning degrades abstention **by 24% on average** (abstract). Larger reasoning budget (512 to 4096 tokens, s1.1) improves accuracy and leaves abstention flat or worse (Fig. 7). Underspecified-context is the weakest scenario and SFT lowers it (Fig. 5). A crafted system prompt that lists abstention scenarios raises abstention for both standard and reasoning models without a significant precision loss (Section 4.4, Fig. 8b); the authors say it "is unlikely to fundamentally address a lack of reasoning about uncertainty".
- Significance: no formal tests quoted in the passages read.
- Readout match: **not matching** (long generation). The system-prompt gain is the closest external support for an abstain-scenario list in the instruction.

### S6. Tomani et al. 2024, "Uncertainty-Based Abstention in LLMs"
- Link: https://arxiv.org/abs/2404.10960. Grade: PP (abstract read only; body not searched). Models: LLMs with and without RLHF; **statistical uncertainty metrics (softmax-based) and a verbalised measure**; QA, unanswerable QA, safety.
- Abstract claims: abstaining on a few highly uncertain samples improves correctness by 2-8%, avoids 50% of hallucinations on unanswerable questions, and raises safety by 70-99%. Readout match: **partial** (softmax-uncertainty abstention matches the idea of thresholding W12/A27 probabilities, but the models are generative QA). Only the abstract was verified.

### S7. "LLM Abstention Can Be a Prompt Artifact, in Addition to Genuine Uncertainty" (2026 preprint, v9)
- Link: https://arxiv.org/abs/2507.16199 (read via https://arxiv.org/html/2507.16199v9, summary only). Grade: PP (single-group, recent, heavily revised: v9). Not independently replicated.
- Models: DeepSeek-V4-Flash, GPT-5.4-nano, Gemini-3.1-Flash-Lite (main), Olmo-3-7B (representation analysis), Gemma family (scale). **Readout: generation, plus logit-lens on hidden states.**
- Task: FLD and FOLIO (500 answerable + 300 Unknown-labelled each), ARC, MedQA, MMLU, LogiQA (500 each).
- Reported: adding an "Unknown" option to a true/false task drops accuracy by 19.8 points on average with 34.5% abstention; in MCQ the drop is 1.2 points. Replacing "Unknown" with an unrelated word ("Triangular", "Cerulean") gives similar abstention (about 30%), so the **extra option itself, not its meaning, triggers abstention**. Removing the option recovers about 66% accuracy on items that were abstained. Larger models (26B+) show less inflation.
- Readout match: **not matching**. Treat as a hypothesis to test on the lab's readouts: it conflicts with the assumption that abstention wording drives behaviour (lab Q5-10, Q5-11).
- Caveat: summary only; numbers not checked against the full text.

### S8. Li, Kim, Wang 2025, "QuestBench" (underspecification, Google DeepMind)
- Link: https://arxiv.org/abs/2503.22674. Grade: PP with benchmark (v2 Oct 2025). Read: full text, Section 5.4 and Table 5-7 region.
- Models: GPT-4o, GPT-4-o1 preview, Claude 3.5 Sonnet, Gemini 1.5 Pro/Flash, Gemini 2.0 Flash Thinking, Gemma 2 2B/9B/27B. **Readout: generation; multiple-choice question to ask.**
- Task: logic, planning, GSM-type problems with one missing variable; English. Result: models are good on GSM-Q (above 80%) and weak on Logic-Q and Planning-Q (40-50%).
- Detection of underspecification (Section 5.4): asked to answer or say "not sure", models said "not sure" on **1.4% (Gemini Flash Thinking), 4.6% (Claude 3.5) and 0.7% (GPT-4o) of Planning-Q cases while the true share was 41.8%**; F1 for "not sure" was at most 5 points above a random baseline on Planning-Q.
- Readout match: **not matching**, but the behaviour (assume the missing fact and answer) is the lab's Q5-3/Q5-6 failure.

### S9. Machcha et al. 2026, "Knowing When to Abstain: Medical LLMs Under Clinical Uncertainty" (MedAbstain)
- Link: https://arxiv.org/abs/2601.12471 (v2, Jan 2026). Grade: PP. Read: full text, Section 3 (variants), Sections 5.1-5.7, Conclusion.
- Models: open and closed LLM families (list not extracted), zero-shot vs few-shot, CoT vs none, Qwen thinking vs not. **Readout: single answer token with logits/logprobs, conformal prediction sets (LAC, APS) over options; MCQA with an explicit abstention option at a random position.**
- Task: MedQA and AMBOSS (private), English. Variants: no abstention (NA), abstention option added (A), key information removed by gpt-4.1-mini (NAP), both (AP).
- Findings: adding the abstention option moves uncertainty and abstention **far more than removing context does**; few-shot gives negligible abstention gains; CoT negligible; thinking mode lowers abstention; scale or "advanced prompting" brings little. Human check on the perturbed items: abstention was appropriate in 77.55% of labelled cases (over 90% when the removed information was rated moderately or highly important); **model abstention precision 71.43%, recall 13.16%** on those items.
- Significance: medians with IQR; no formal tests quoted. Readout match: **partial to matching** (logprob readout of option tokens, same missing-evidence failure as lab Q5-3, Q5-4). Strongest external analogue of the lab's W3 failure, but a preprint on generic chat LLMs.

### S10. Fan et al. 2025, "Missing Premise exacerbates Overthinking" (MiP-Overthinking)
- Link: https://arxiv.org/abs/2504.06514 (full text read: Sections 1-3, Table 2). Grade: PP with code (GitHub repo title in search results indicates COLM 2025; page not opened).
- Models: reasoning LLMs (DeepSeek-R1, QwQ-32B, o1 and others) vs non-reasoning (GPT-4o and others). **Readout: generation; GPT-4o judge.**
- Task: MiP-Formula (50), MiP-SVAMP, MiP-GSM8K, MiP-MATH. Example: GPT-4o abstain rate 70.0 (MiP-Formula), 96.3 (SVAMP), 46.9 (GSM8K), 15.4 (MATH).
- Finding: reasoning models produce 2-4x more tokens on missing-premise questions and do not abstain more; non-reasoning models quickly flag them. Readout match: **not matching** (applies only to long-reasoning generators). Evidence that a generative-only mechanism can reduce abstention.

### S11. Plaut, Nguyen, Trinh 2025, "Probabilities of Chat LLMs Are Miscalibrated but Still Predict Correctness on Multiple-Choice Q&A"
- Link: https://arxiv.org/abs/2402.13213 (TMLR 08/2025 header read). Grade: **PR** (TMLR). Read: full text, abstract, Section 1 and the abstention paragraph.
- Models: 15 chat LLMs (Falcon 7B, Llama 2/3/3.1 7-8B and 70B, Mistral 7B, Yi 34B, SOLAR 10.7B, GPT-3.5 Turbo and others) plus base models. **Readout: probability of each answer-letter token, renormalised; MSP = maximum; also max logit. Matching W12/A27.**
- Task: ARC-Challenge, HellaSwag, MMLU, TruthfulQA, WinoGrande; 21,407 questions, 642,210 prompts, two phrasings; English. Metric: AUROC of MSP for correctness, calibration error.
- Findings: MSPs are miscalibrated but predict correctness (Mann-Whitney tests, 280 AUROC points); correctness prediction rises with accuracy (R squared 0.94 for MSP AUROC vs accuracy), calibration does not improve with capability. In a version of the task with abstention (+1 correct, 0 abstain, -c wrong, c = 1 or 2), thresholding the MSP or max logit gave substantial gains over never abstaining, with **about 20 labelled questions per dataset** to pick the threshold. Base models are better calibrated than chat models.
- Readout match: **matching for W12/A27** (letter logits). Supports a threshold-on-probability abstain route; does not address the missing-fact failure (lab Q5-5 found that gates fail on high-confidence missing-fact errors).

### S12. Wen et al. 2025, "Know Your Limits: A Survey of Abstention in LLMs"
- Link: https://aclanthology.org/2025.tacl-1.26/ (TACL 13:529-556). Grade: PR (survey). Abstract page only (abstract read; the body was not searched for prompting claims). It frames abstention by query, model and human values and organises methods by pretraining, alignment and inference. Used as a map; no effect sizes taken from it.

## Negative, task-dependent and non-replicating results (kept next to the positives)

- NA wording: S2 says sensitivity is moderate while Table 3 shows a 2.4x spread for one model; read the table, not the sentence.
- Abstain clause effects are model-dependent (S3: small models do not follow EAC; S4: 0% to 100% for the same sentence).
- CoT helps abstention in S3 and S4 and does not in S5, S9, S10. All need generated reasoning, so none transfers to one-pass readouts.
- S7 (option triggers abstention regardless of meaning) conflicts with the idea that the abstain label's wording is the lever; it is a single preprint and unreplicated.
- Fine-tuning for NA raises NA-keyed accuracy and lowers ordinary accuracy (S2 Table 4).
- Model size: abstention improves with size inside families in S4, not in S5 (scale "almost no effect"). The scenarios and readouts differ.

## Excluded or not used

- Ravikumar 2026, "The Missing 'I Don't Know'" (https://arxiv.org/abs/2609.17686): opened; a position paper that combines three earlier results and reports no new measurements, so no evidence taken.
- Out-of-scope intent detection items found by search (https://arxiv.org/abs/2608.20371, https://arxiv.org/abs/2507.01541) are recorded in q6-readout-and-vendor.md.

## Gaps for Q5

- No controlled study found of "none of the above" or abstention on **pointer-head, encoder or trained decision-model readouts** apart from the vendors' own audits (see q6 file).
- No external study isolates an abstain instruction clause on a logit-readout model; S3 and S4 are generative.
- No external replication of the missing-decisive-fact failure on logit readouts apart from S9 (preprint).
