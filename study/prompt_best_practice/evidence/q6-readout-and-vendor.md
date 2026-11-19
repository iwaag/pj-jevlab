# Q6 evidence: readout dependence, encoder and scorer evidence, and vendor or practitioner sources

Step2/step3 note for `devdocs/episodes/study/prompt_best_practice/p1`. Access date for every link: **2026-10-03**.
All rows are **external sources**. Lab results are in [../lab-evidence.md](../lab-evidence.md) (Q6-1 to Q6-6) and are only cross-referenced. Q5 sources are in [q5-abstention.md](q5-abstention.md) (S1 to S12) and are cited here by those labels.

Reading conventions are the same as in the Q5 note. `full text` means the PDF was downloaded and the passage read. `summary` means the page was read through the fetch tool's small-model summary. `raw text` means the raw README was downloaded and searched. Grades: PR peer-reviewed controlled; PP preprint (code stated when so); V vendor or author evaluation; PR-prac practitioner; G guide or opinion. Readout match is against W12/A27 (option-letter logits), K27 (pointer head), J/G (encoders), L27 (short generative).

## Short answers (for step4)

1. **No source found that tests prompt or label wording on pointer-head scorers or on trained decision models in a controlled way.** The only evidence on those readouts is vendor and author documentation (Section C). This is a gap, not evidence of no effect.
2. **Letter-logit readout has external evidence** (S1, S11, BTZSC): max probability over letters predicts correctness; first-token probability can disagree with what a chat model would write (Wang 2024, below). The lab's W12 and A27 are trained decision models, so this evidence is only partial.
3. **Encoder and NLI zero-shot classifiers are sensitive to label wording and hypothesis template in the older literature** (Ma 2021, Bareiß 2024), but the newer benchmark (BTZSC) did not vary templates, and no GLiClass or GLiNER2 paper reports a label-description ablation (full-text search of both papers).
4. **Findings known to need generated text** and therefore not carried to one-pass readouts without a test: chain-of-thought gains for abstention (S3, S4), reasoning-budget effects (S5, S10), verbalised confidence (S3), self-reflection second passes.
5. **Training-time levers for abstention on span or label scorers have direct evidence:** GLiNER negative-type sampling trades precision for recall (Table 5); Kev uses "none pairs" and "abstention twins" in training (author README and plan).

## A. Encoder, cross-encoder, NLI and zero-shot classifier evidence

### A1. Ma, Yao, Lin, Zhao 2021, "Issues with Entailment-based Zero-shot Text Classification"
- Link: https://aclanthology.org/2021.acl-short.99.pdf (ACL-IJCNLP 2021 short paper; the paper calls itself an opinion piece with experiments). Grade: PR (short). Read: full text, Sections 1-3, Tables 1-5.
- Models: bert-base-uncased fine-tuned on RTE, MNLI, FEVER (Yin et al. 2019), raw BERT with next-sentence prediction (NSP). **Readout: sentence-pair entailment score per label hypothesis (cross-encoder).** Languages: English.
- Tasks: Yahoo topic (10 classes), emotion (9 + a "none" label), situation (11 + "none"), AG News, SST-2, Snips. Metric: accuracy or weighted F1.
- Findings: huge variance across datasets; raw NSP BERT matched or beat NLI-fine-tuned BERT on topic, intent and sentiment (Table 1: Yahoo NSP-reverse 53.1 vs MNLI 37.9, 49.1 best run); five MNLI runs with equal in-domain accuracy differ widely out of domain (Table 2: Yahoo mean 39.0, std 10.5, range 26.9-50.2; AG News 63.7, std 11.0). **Emotion and situation tasks, which include a "none" label, stayed at 12-25 F1 for all systems** (Table 1). Shuffling the tokens of the input barely changes predictions (Table 4), which the authors read as reliance on shallow lexical patterns. Three debiasing methods raised HANS accuracy and gave no real gain on the classification sets (Table 5), a negative result.
- Significance: seed variance reported (five runs); no formal tests. Readout match: **partial for J and G** (encoder scoring of label text; J and G are uni-encoder label-token models, not pair classifiers). Dated (BERT-base).

### A2. Bareiß, Klinger, Barnes 2024, "English Prompts are Better for NLI-based Zero-Shot Emotion Classification than Target-Language Prompts"
- Link: https://arxiv.org/abs/2402.03223 (WWW '24 Companion). Grade: PR (companion track). Read: full text, RQ1/RQ2 sections.
- Models: six multilingual NLI models (cross-encoders), seven prompt types from Plaza-del Arco et al., Google-Translate prompts. **Readout: NLI entailment score per label.** Data: Universal Joy (18 languages), EmoEvent, de/enISEAR.
- Result: English prompts beat target-language prompts on every Universal Joy language (average macro-F1 difference 0.025), equal on EmoEvent, a small difference for de/enISEAR English-German (0.013). The paper states that small prompt changes can change classification a lot; prompt-type stability across languages is analysed in RQ2.
- Readout match: **partial** (NLI cross-encoder; same family as the older zero-shot classifiers, not the lab's label-token encoders). Language: relevant to any non-English test of J and G (G card says English only, see C3).

### A3. Webson and Pavlick 2022, "Do Prompt-Based Models Really Understand the Meaning of Their Prompts?"
- Link: https://arxiv.org/abs/2109.01247 (v2 Apr 2022). Grade: PP (controlled, widely cited). Read: full text, abstract, Sections 1, 3, 5.
- Models: fine-tuned and prompt-tuned BERT, DistilBERT, RoBERTa, ALBERT and T5; T0 3B and 11B; GPT-3 175B. **Readout: rank classification over target words (verbalisers).** Task: NLI (RTE validation is shown in the figures read; other NLI sets not verified), 30+ manual templates, English.
- Result: models learn as fast with intentionally irrelevant or misleading templates as with instructive ones in few-shot, and instruction-tuned models produce good predictions with irrelevant and misleading prompts even at zero shot; **the choice of target words (yes/no versus arbitrary or reversed words) matters much more than the template meaning** (Section 5; the neutral class used "unclear").
- Readout match: **partial** (rank classification over label words resembles letter or key readout). It is evidence against assuming that more instructive wording helps, and for key or verbaliser naming mattering. Different task (NLI) and older models.

### A4. Aarab 2026, "BTZSC: A Benchmark for Zero-Shot Text Classification Across Cross-Encoders, Embedding Models, Rerankers and LLMs"
- Link: https://arxiv.org/abs/2603.11991 (ICLR 2026 header in the PDF). Grade: PR (ICLR 2026). Read: full text, Section 4-5, Appendix A.2.
- Models: 38 models in four families, all strictly zero-shot: 11 NLI cross-encoders (about 300M), 11 embedding models (22M to 8B), 6 rerankers (22M to 8B), 8 instruction-tuned LLMs (270M to 12B). **LLM readout: multiple-choice prompt with enumerated verbalised labels; the answer is the option with the highest next-token probability (matching W12/A27 in kind, untrained for decisions).**
- Tasks: 22 English datasets (sentiment, topic, intent, emotion), 2 to 77 classes; macro-F1.
- Results: Qwen3-Reranker-8B F1 0.72; best LLM Mistral-Nemo-12B 0.67; best embedding gte-large-en-v1.5 0.62; best NLI cross-encoder 0.60. LLMs jump between 3B and 8B (Qwen3-4B 0.65 vs Llama-3.2-3B and Phi-4-mini mid-0.40s), so "instruction-tuning quality and base model design matter more than parameter count" at moderate scale; embeddings plateau near 0.60-0.62.
- Prompts: one fixed verbaliser per dataset shared across all families; no per-model tuning (Appendix A.2). **So the paper gives no evidence on wording sensitivity.** No abstention or none class (single-label sets).
- Readout match: **partial** (letter-style readout for LLMs; cross-encoders compare to J and G only loosely).

### A5. GLiClass (Stepanov et al. 2025) paper, model card and README
- Links: https://arxiv.org/abs/2508.07662 (PDF downloaded and searched for label-wording experiments; table numbers below are as given in the fetch summary), https://huggingface.co/knowledgator/gliclass-modern-base-v3.0 (summary), https://github.com/knowledgator/gliclass (summary). Grade: paper PP; card and README V.
- Models: uni-encoder DeBERTa-v3 (large, base, edge variants; modern-base 151M). **Readout: one pass, label tokens prefixed with `<<LABEL>>` and scored jointly with the text.** This is the architecture family of J (GLiFormer) and G (GLiNER2.5).
- Results (Table 3, 13 datasets, F1): gliclass-large-v3.0 0.7193 vs DeBERTa-v3-large cross-encoder 0.6821; edge 0.49. Throughput does not collapse with label count (Table 6) while cross-encoders drop about 50x from 1 to 128 labels. Limits stated: large label sets (positional encoding), extreme label-to-text ratios, residual calibration differences across datasets (Sections 4-5, Table 7).
- **Label wording:** full-text search of the paper found no experiment on label phrasing or label descriptions. The card says zero-shot F1 ranges 0.22-0.94 by dataset, strongest on sentiment and weaker on complex multi-class problems like banking intent; it recommends a single hypothesis input; thresholds 0.5 (multi-label) and 0.0 (NLI). The README documents an optional task `prompt`, few-shot `examples` and per-text prompts, with no stated effect sizes.
- Readout match: **matching in architecture for J/G**, no wording or abstention evidence.

### A6. GLiNER (Zaratiana et al. 2023) and GLiNER2 (Zaratiana et al. 2025)
- Links: https://arxiv.org/abs/2311.08526 and https://arxiv.org/abs/2507.18546 (both full text read). Grade: PP (code released).
- GLiNER: bidirectional encoder scores spans against entity-type prompts (pointer-style span scoring; **closest published readout to K27's pointer head**). Table 5, effect of negative entity-type sampling during training: 0% negatives P 49.3 / R 58.1 / F1 53.3; 50% negatives 62.3 / 59.7 / 60.9; 75% negatives 61.1 / 56.5 / 58.6. More negatives make the model "more cautious" (precision up, recall down). Randomly dropping entity types helps too (Figure 6: 59.5 without dropping vs 60.9 full).
- GLiNER2: feature table lists label descriptions (Table 1) and Section 2 says entity-type descriptions are supported "alongside labels"; zero-shot classification Table 2 (7 datasets): GLiNER2 205M average 0.72, GLiClass 0.63, DeBERTa-v3 NLI 0.69, GPT-4o 0.84; Banking77 (77 labels) GLiNER2 0.70, GLiClass 0.21, DeBERTa 0.42, GPT-4o 0.78. **Full-text search found no ablation of label descriptions.**
- Readout match: GLiNER **partial for K27** (span scoring), both **matching for J/G architecture**. The negative-sampling table is evidence that abstention behaviour on span or label scorers is set at training time, not by prompt wording.

### A7. Out-of-scope detection with classifiers versus LLMs
- 2608.20371, "When Do LLMs Replace Fine-Tuned NLU?" https://arxiv.org/abs/2608.20371 (summary of the HTML, Sept 2026 preprint). Models: roberta-base fine-tuned, claude-haiku-4-5 zero-shot, TF-IDF, MiniLM kNN. CLINC150 (150 intents + 1,000 OOS items): Claude OOS recall 85.6, F1 85.0; RoBERTa 58.1 / 73.0; TF-IDF 36.4 / 51.7. The prompt gave the label set and a JSON schema; no wording analysis. **Readout: generation.** Grade: PP. Readout match: not matching; indicates that a trained closed-set encoder abstains poorly while a zero-shot LLM abstains better, consistent in direction with lab Q5-1 (J and G fail on fallback options).
- 2507.01541, "Efficient Out-of-Scope Detection in Dialogue Systems via Uncertainty-Driven LLM Routing", https://arxiv.org/abs/2507.01541 (summary only; ACL industry track per the search result). DistilBERT in-scope classifier with an uncertainty score routes uncertain utterances to fine-tuned Llama 3.1-8B to choose among top-3 intents or OOS. F1 0.853 (BookData), 0.761 (HINT3 average, high routing). Readout: encoder score plus generative second stage. Grade: PP/industry. Not checked at full text.

### A8. First-token readout versus text answer (Wang et al. 2024)
- Link: https://arxiv.org/abs/2402.14499, "'My Answer is C': First-Token Probabilities Do Not Match Text Answers in Instruction-Tuned Language Models". Grade: PP with code (venue not verified in the copy read). Read: full text, abstract, Sections 3-4.
- Models: Llama2-Chat 7B/13B/70B, Mistral v0.1/v0.2, Mixtral 8x7B. **Readout: first-token log-probability over option letters versus the model's actual text answer.** Data: MMLU and a 414-question OpinionQA subset; each question ten times with shuffled options.
- Result: mismatch rate above 60% in some models; more constrained instructions reduce it but it persists; models heavily fine-tuned on conversation or safety data are worst; **text output is more robust to prompt perturbation and shows less selection bias than the first-token readout** for all models except Mixtral 8x7B.
- Readout match: **partial for W12/A27** (same letter-logit readout, but on chat models never trained to emit a letter first; the lab's models are trained to read the letter slot, so the mismatch need not apply). Warns against carrying prompt-robustness findings from text answers to logit readouts or back.

### A9. Readout-dependence summary cross-references
- Letter-logit readout, correctness from max probability: S11 (matching). Calibration of base versus chat models: S11, S1.
- Letter-logit readout, abstention option in the options: S1 (replacing an option with NOTA hurts), S9 (logprob readout, abstention option moves uncertainty more than missing context).
- Generation-only mechanisms (do not carry to one-pass readouts without a test): CoT and thinking gains or losses (S3, S4, S5, S9, S10), verbalised confidence (S3), few-shot gains that depend on model size (S3).

## B. Which prompting findings are known to hold only for generative models

| Finding | Evidence | Why it is generative-only |
|---|---|---|
| Chain-of-thought raises abstention and reflective judgment | S3 (UAC roughly doubles on MMLU for GPT-4 Turbo), S4 (more than 85 points) | needs generated reasoning; S9 finds no gain with logit readout on options |
| More reasoning budget hurts or does not help abstention | S5 Fig. 7, S10 | long generation |
| Verbalised confidence thresholds | S3 (not consistently better than base) | needs generated numbers |
| Abstain-scenario system prompt raises abstention | S5 Sec. 4.4 | tested only on chat and reasoning generators |
| Emotional "extreme abstain" pressure | S3 (helps GPT-4 Turbo, hurts small models) | instruction following by chat models |
| First-token probability tracks text answer | A8 (does not, in chat models) | depends on response style |
| Second-pass narrowed re-ask changes answers | lab only (K27: Q6-2); no external source found | untested externally |

## C. Vendor, author and practitioner sources

Everything below is grade V or PR-prac unless marked G. Most were read as fetch summaries; the Kev and Decider READMEs were also downloaded raw and searched.

### C1. TypeSafe Jev documentation (the reference system)
- Pages read (summary): https://docs.typesafe.ai/llms.txt (index), https://docs.typesafe.ai/primitives.md, https://docs.typesafe.ai/primitives/choice.md, https://docs.typesafe.ai/primitives/advanced.md, https://docs.typesafe.ai/confidence.md, https://docs.typesafe.ai/patterns/confidence-routing.md, blog https://typesafe.ai/blog/introducing-system-one-models-and-jev.
- Guidance paraphrased: write the complete question in `instructions` even when the question id is self-explanatory; target "snap judgments" a knowledgeable person makes in a second; reference state fields by path; split multi-factor judgments into separate questions and combine in code; use structured instructions (JSON with labelled keys) for multi-part questions; for confusable choices give each option `what`, `not_for` and `examples` ("each option says what it is not for"); give the full option list (up to 255) rather than a shortlist; **"add an `other` or `none of the above` option when the list might not cover every input"**; for yes/no questions define the condition precisely.
- Abstention: confidence (concentration of the probability distribution) is the main lever. Three tiers (act, confirm or review, do not act); thresholds should depend on the consequence of the action (0.5 floor, 0.85-0.9+ for high stakes; confidence-routing page example 0.6 floor and 0.85). The docs give no guidance on option order and say nothing on how instructions change confidence.
- Evidence status: guidance without published measurements; the blog states calibration as a goal. Readout: undisclosed. Match: unknown (reference system, not a lab readout).

### C2. Liquid decision-model guide
- Links (summary): https://docs.liquid.ai/guides/decision-model-guide, https://docs.liquid.ai/lfm/models/decision-models.
- Guidance: state the decision as a direct question; pair each option with a descriptive explanation ("billing: charges, invoices, refunds, or payment methods"); examples use 3-5 options; no ordering guidance; no abstention mechanism documented, uncertainty is expressed by confidence below 0.5, noul near 0.5, and runner-up probabilities; the model page lists no benchmarks or failure modes. Readout: zero generated tokens (probabilities). Match: unknown.

### C3. GLiNER2.5-Decide card (lab system G)
- Link (summary): https://huggingface.co/fastino/GLiNER2.5-Decide. Grade V. 340M DeBERTa-v3-large encoder, English only (a multilingual sibling exists), Apache-2.0, 60.2% exact-match accuracy on `fastino/fast-decisions` (17 domains, 300 held-out examples each).
- Label guidance: labels are passed as strings at call time; **"when the name of a label is not enough, pass a short description with it. The description is part of the decision."** No prompt template; for question-style tasks a `prompt` key is used; multi-label tasks need an explicit `cls_threshold`. The card states it "does not reason, explain, or answer open questions". No guidance on abstention or none labels. **Readout: encoder label logits. Matching G.**

### C4. Jeff (lab system J) README
- Link (summary): https://github.com/logan-markewich/jeff. GLiFormer ~400M; probabilities are normalised sigmoids temperature-scaled at 3.2 (`JEFF_TEMPERATURE`); `noul` has three modes. The README states it is "substantially behind on irony, reading comprehension, and JevBench's judge and hard tiers" and "less accurate than jev on reasoning-heavy tasks" (AG News 75.5% vs Jev 90.5%; JevBench 66.9 vs 75.3). No wording or abstention guidance found. **Readout: encoder. Matching J.**

### C5. Kev (lab system K27) README and PLAN
- Links (raw text downloaded): https://github.com/jaredpalmer/kev (README) and https://github.com/jaredpalmer/kev/blob/main/PLAN.md (raw file from raw.githubusercontent.com). Grade V (author evaluation).
- Readout: pointer head over option states. **Matching K27.**
- Abstention: the `transfer-v9` suite includes "unknowable" records whose deciding evidence was removed; the README reports the share answered at 0.9 or higher confidence: **Kev-9B 0%, Jev 9%**. The plan lists the unknowable share as a guard (at most 0.05; 0.000 for the candidates shown). Training uses "none pairs" (taught "none of the above", probability 0.25, only on states of at most 8,192 tokens) and "abstention twins". The lab found K27 missing decisive-fact cases at high confidence (lab Q5-3, Q4-10): the author's suite and the lab's W3 missing-fact cases are different tests, and the lab result is not a replication or a contradiction of a number.
- Limitations stated: calibration is a single temperature; automatable share at a 5% error budget 0.52-0.69 vs Jev 0.70; **"changing option order can change an answer"**; fine-tuning degraded date arithmetic. The README advises testing a probability threshold on your own data.

### C6. Decider (D35 family) README
- Link (raw text downloaded): https://github.com/Mapika/decider. Grade V. Readout: hidden state at each slot projected onto one label token per option (letters), softmax over valid options, "letters are never generated". **Matching W12/A27 in readout kind.**
- Statements under "Limits, stated plainly": calibration on hard items is the weak axis (decider-2b v10 top-label ECE 0.31 on JevBench public hard items, 0.18 for v11 and decider-4b v2.1, 0.15 for the 35B, 0.10 for decider-4b v2; release limit 0.08 not met on held-out families); **"Generic options need to look like buckets... A plain `support` next to `other` sends an in-scope complaint to `other`"**; **"Rules written into the question are not followed at this size": a one-sentence question scores 0.67 and a paragraph of rules 0.24 on the form-filling probe, "a fixed convention has to be in the training data, not in the question"**; picking a record out of a long JSON array by position is the least accurate input shape (0.51 with 64 records, 0.70 with one); known regressions between versions. English only.
- Use: the closest author statement on instruction length and rules in the question for a letter-logit decision model. It is an author probe with n not read here.

### C7. Winnow-12B (lab system W12) card
- Link (summary): https://huggingface.co/EldanRing/Winnow-12B. Readout: option-letter logits normalised over the supplied options, entropy-based confidence ("not a guaranteed probability of correctness"); no guidance on abstention or a none option ("implement through prompt engineering or branching"); JevBench public subset 231 items 85.71%, Kev-v9 clean 1,046 items 81.55% (Q8). **Matching W12.**

### C8. AutoJev-27B (lab system A27)
- Link (summary): https://github.com/denis-pplx/autojev. Qwen3.8-27B base, one forward pass per question, probabilities over supplied choices; cross-entropy training with a separately fitted scalar temperature; overall accuracy 84.60% (baseline 69.83%), ECE 0.04282 (0.06483), Brier 0.22027 (0.40834). No abstention or wording guidance found. **Matching A27.**

### C9. Clone audits and practitioner reports
- OpenJev Verdict (summary): https://github.com/Heman10x-NGU/Verdict-open-jev. Abstention is an explicit `__insufficient_evidence__` candidate. Author audit: abstention recall 75.5% (precision 89.45%) in-domain, collapsing to **18.0% with nine hard-negative sibling options**; a paraphrased synonym of the abstention prompt drops recall to 23.5%; combined 10.0% ("abstention does not generalize across synonyms"); option reversal flips 3.0% and random permutations 4.5% of predictions, concentrated in low-confidence items (mean confidence 58.9% flipped vs 93.7% unchanged); 48.07% on TypeSafe's 337-case external set vs 88.43% for a 26B baseline. Option writing: v1.4 changed bare noun-phrase candidates to hypothesis framing (`It is {description}`) "and lifts accuracy" (author claim, no number in the summary). Readout: encoder (ModernBERT with joint label encoding). Match: J/G family.
- Laya (summary): https://github.com/NandhaKishorM/laya. Accuracy degrades above about 20 options (shared token budget), position bias shown by logit spreads across slots (+1.68 to -1.91 for one example) which motivates `option_order` permutation, both checkpoints over-confident as shipped, `noul` can follow option labels rather than the state, score is the weakest primitive. Encoder. Match: J/G family.
- Tev1 blog (summary): https://www.together.ai/blog/how-to-train-your-own-jev. Prompt: "Select exactly one listed option. Return only its letter", temperature 0, 8 tokens; an explicit "none of the listed intents matches" option D inside the option list; 37,840 training examples; no calibration, order or abstention evaluation reported. Generative short output (like L27 in kind, not the same model).
- Navya AI (summary): https://www.navyaai.com/blog/jev-typesafe-limitations-production. 200 AG News articles, four classes; ECE per question type noul 0.012, choice 0.086, score 0.254; "never gate on raw confidence"; keeping each model's most confident 80% did not change the ranking (Jev 98.6%, Haiku 98.9%). Practitioner report; one easy task.
- allanrbo blog (summary): https://allanrbo.blogspot.com/2026/09/a-jev-like-wrapper-for-llms-including.html. A wrapper that renders lettered options, asks for the best letter and reads first-token logprobs, 2 to 20 criteria per question; reports no accuracy study. Practitioner; readout letter logits (matching in kind).

### C10. General vendor prompt guides (classification and multiple choice only)
- Anthropic, "Reduce hallucinations": https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations (summary of the fetched page). Grade G. First listed strategy: explicitly allow the model to say "I don't know", with an example clause "If you're unsure about any aspect or if the report lacks necessary information, say..."; claims it "can drastically reduce false information" with no measurement in the page. Generative; not a classification guide.
- OpenAI, structured outputs: https://developers.openai.com/api/docs/guides/structured-outputs (summary). Grade G. Enum classification is shown; the guide says to include instructions on how to handle input that cannot yield a valid response; it does not discuss an "other" option. Refusals appear in a separate field.
- Google Gemini prompting strategies: https://ai.google.dev/gemini-api/docs/prompting-strategies (summary). Grade G. Says nothing on option wording, order, none options or "if unsure" instructions; mentions reformulating a task as multiple choice.
- **Inaccessible:** Anthropic classification use-case guide (https://docs.anthropic.com/en/docs/about-claude/use-case-guides/classification and its platform.claude.com redirect target) returned 404; no content read.

## Gaps for Q6

- No external controlled study on pointer-head scorers (K27 type) or trained decision models (W12, A27) for wording, order or abstention. Closest: GLiNER span scoring (A6), Decider and Kev author statements (C5, C6).
- No label-description ablation found for GLiClass or GLiNER2 despite the feature (A5, A6).
- BTZSC, the newest benchmark, did not vary templates, so template sensitivity of current cross-encoders rests on the older work (A1, A2, A3).
- Vendor guidance (Jev, Liquid) conflicts in no direct way with the lab, but all of it is unmeasured guidance. The Decider statement that rules in the question hurt a small letter-logit model is the only direct evidence on instruction length for that readout.
- Jev's own documentation and blog give no measured effect of instruction wording on abstention.
