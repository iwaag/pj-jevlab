# Search log — prompt_best_practice p1 (2026-10-03)

Failed or empty searches are not evidence that no work exists. Sections come from four parallel searchers, one per topic group.

---

# Search log fragment: Q1/Q2 (instruction wording, distractors, compression, option keys, descriptions, option count, near-neighbours, "none of these")

Date of all searches and fetches: 2026-10-03. Evidence note: [../evidence/q1-q2-instruction-and-options.md](../evidence/q1-q2-instruction-and-options.md). To be merged into `search-log.md`.

## Method notes
- WebSearch returns summaries, not evidence. Every candidate that was used was opened. The PDF route through WebFetch returned binary for arXiv PDFs, so papers were downloaded with `curl` from `https://arxiv.org/pdf/<id>` and converted with `pdftotext -layout` into a scratchpad folder; passages were then read with grep and sed. Web pages (vendor docs, PLOS ONE, Hugging Face, GitHub) were read through WebFetch, which condenses the page with a small model; these are marked "fetch summary" in the evidence note and their numbers were not independently checked.
- Two-column PDFs make `pdftotext` interleave text, so some numbers were read from tables only when the row was unambiguous.
- Another agent writes to the same scratchpad folder and files I had downloaded disappeared once; I moved to a private subfolder and re-downloaded what I needed.

## Queries run (WebSearch)
1. prompt compression effect on classification tasks negative results short prompts LLMLingua evaluation 2025
2. label descriptions vs label names zero-shot classification LLM effect on accuracy arXiv 2024
3. "none of the above" option LLM multiple choice accuracy drop NOTA arXiv
4. number of answer options multiple choice LLM accuracy more options distractors effect arXiv 2024 2025
5. GLiClass label descriptions prompt prefix labels improve zero-shot classification encoder
6. spotlighting delimiting datamarking indirect prompt injection defense evaluation arXiv Hines 2024
7. zero-shot NLI classification hypothesis template wording label names sensitivity cross-encoder evaluation Laurer 2024
8. LLM classification with "other" or "none of the above" category confusable similar labels hard negatives abstention recall drop arXiv
9. Anthropic prompt engineering classification guidance clear instructions XML tags data delimiters docs.claude.com
10. OpenAI cookbook classification logprobs multiple choice single token labels tips prompt
11. instruction length verbose vs concise prompt classification accuracy LLM controlled study task description length effect 2024 2025 arXiv
12. POSIX prompt sensitivity index LLM multiple choice paraphrase option order template arXiv 2024
13. multiple-choice answer options semantic key names versus letters A B C D vs descriptive labels LLM accuracy comparison arXiv
14. LLM text classification label name wording paraphrase synonyms sensitivity "label" "verbalizer" instruction-tuned LLM 2025 study
15. entity type descriptions definitions improve zero-shot NER GLiNER ablation label descriptions vs label names arXiv
16. zero-shot text classification cross-encoder label description vs label name effect accuracy encoder classifier joint label encoding limitations many labels

Known-source lookups (opened directly by arXiv ID or URL, from the plan, from [../lab-evidence.md](../lab-evidence.md) leads, or by following citations): Sclar 2310.11324; Mizrahi 2401.00595; He 2411.10541; Zheng 2309.03882; Wang "My Answer is C" 2402.14499; Wang "Look at the Text" 2404.08382; Voronov 2401.06766; ProSA 2410.12405; PromptEval 2405.17202; POSIX 2410.02185; Shi 2302.00093; Levy 2402.14848; Yoran 2310.01558; Cuconasu 2401.14887; Liu "Lost in the Middle" 2307.03172; LLMLingua 2310.05736; LLMLingua-2 2403.12968; compression survey 2410.12388; MMLU-Pro 2406.01574; Alzahrani 2402.01781; Robinson and Wingate 2210.12353; Holtzman 2104.08315; Webson and Pavlick 2109.01247; Wei 2303.03846; Label Words are Anchors 2305.14160; LongICLBench 2404.02060; GLiNER 2311.08526; GLiNER multitask 2406.12925; GLiNER2 2507.18546; GLiClass 2508.07662; Principled Instructions 2312.16171; Prompt Report 2406.06608; Changing Answer Order 2406.19470; Jev docs and blog; Laya README; Laurer 2312.17543 and model card.

## Candidates and inclusion reasons

| Candidate | Link | Included? | Reason |
|---|---|---|---|
| Sclar et al. | https://arxiv.org/abs/2310.11324 | yes (full text) | Original format-spread study; ICLR; defines how to report spread; probability-ranking readout |
| Mizrahi et al. | https://arxiv.org/abs/2401.00595 | yes (full text) | Paraphrase ranking instability, TACL; the "15 of 25" lead verified |
| Voronov et al. | https://arxiv.org/abs/2401.06766 | yes (partial) | Template sensitivity for classification across 21 models; template ensembles |
| PromptEval, POSIX, ProSA | arXiv 2405.17202, 2410.02185, 2410.12405 | yes (abstract plus tables) | Reporting methods and instance-level inconsistency; scale and instruction-tuning claims conflict between studies |
| MMLU-Pro | https://arxiv.org/abs/2406.01574 | yes, with confounding caveat | Only source with 24-prompt spread and an option-count change; confounded |
| Alzahrani et al. | https://arxiv.org/abs/2402.01781 | yes (sections 1, 5) | Symbol change and scoring method; section 5.4 is a negative result on prompt changes |
| He et al. | https://arxiv.org/abs/2411.10541 | yes (abstract only) | Format effects on GPT models |
| Webson and Pavlick | https://arxiv.org/abs/2109.01247 | yes (full text) | Instruction semantics versus target words; encoder (ALBERT) included |
| Celebi and Penczynski (PLOS ONE) | https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0354757 | yes (fetch summary) | Only controlled instruction-length/definition-detail study found; task-dependent; summary only |
| Shi et al.; Levy et al.; Cuconasu et al.; Yoran et al. | arXiv 2302.00093, 2402.14848, 2401.14887, 2310.01558 | yes | Distractor/irrelevant-context literature, including one contradicting result (random documents help) |
| Spotlighting; Critical evaluation | arXiv 2403.14720, 2505.18333 | yes | Data-boundary wording; pro and (second-hand) con |
| Principled Instructions | https://arxiv.org/abs/2312.16171 | yes, low weight | Often cited instruction guide; author benchmark, averages |
| LLMLingua; empirical study; RCT; in the wild | arXiv 2310.05736, 2505.00019, 2603.23525, 2604.02985 | yes | Compression evidence; none for short classification prompts |
| Zheng et al. | https://arxiv.org/abs/2309.03882 | yes (full text) | Option-ID logit readout, symbol swaps |
| Sanz-Guerrero et al. | https://arxiv.org/abs/2509.15020 | yes (full text) | Letter-logit readout, tokenisation of the space, matching the lab readout |
| Robinson and Wingate | https://arxiv.org/abs/2210.12353 | yes | Symbol binding as a prerequisite for letter interfaces |
| Wang (two papers) | arXiv 2402.14499, 2404.08382 | yes (abstract only) | First-token readout versus text answer; warning for tuned models |
| ABCD | https://arxiv.org/abs/2602.17445 | yes (read) | Uniform labels and text matching; generation readout |
| LOADS | https://arxiv.org/abs/2410.19195 | yes (read) | Label-word choice and elaboration effects, with numbers |
| Gao et al. label-description training | https://arxiv.org/abs/2305.02239 | yes (read) | Verbaliser/pattern sensitivity and descriptions for an encoder |
| Walshe et al. | https://arxiv.org/abs/2501.12332 | yes (read) | Label names versus descriptions; 77-label collapse |
| JPT; SLIMER | arXiv 2604.05158, 2407.01272 | yes | Definition ablations for NER; JPT's bilinear scorer is the closest published relative of a pointer head |
| GLiNER, GLiNER2, GLiClass, GLiNER multitask | arXiv 2311.08526, 2507.18546, 2508.07662, 2406.12925 | yes (GLiNER, GLiNER2, GLiClass read; multitask downloaded only) | Authors' own guidance; GLiNER negative-type ablation; no description ablation |
| BTZSC | https://arxiv.org/abs/2603.11991 | yes (read) | Cross-model zero-shot comparison with fixed verbalisation; LLMs scored by option next-token probability |
| Ghilene et al. SUD | https://arxiv.org/abs/2409.13735 | yes (read) | NLI hypothesis wording effect size, with the selection-on-test caveat |
| Laurer et al. and model card | arXiv 2312.17543 | yes (guide) | NLI verbalisation practice; no ablation |
| Wait, that's not an option | https://arxiv.org/abs/2409.00113 | yes (read) | Invalid-option handling; alert prompt; base versus RLHF |
| NOTA / least incorrect; UA-Bench; Answer matching; option psychometrics | arXiv 2402.01349, 2604.17293, 2507.02856, 2608.02966 | yes (abstract only) | Hand-off and distractor background; weaker |
| Confusion-aware classification | https://arxiv.org/abs/2609.01564 | yes (abstract only) | Near-neighbour labels |
| LongICLBench | https://arxiv.org/abs/2404.02060 | yes (low weight) | Many classes, but via demonstrations |
| Jev docs, Laya README, OpenAI cookbook, Anthropic guide | see evidence note | yes (fetch summaries) | Vendor/author guidance; no measured evidence |
| Wei et al. (semantically unrelated labels) | https://arxiv.org/abs/2303.03846 | yes (abstract) | Semantic label names versus arbitrary |
| Holtzman et al. | https://arxiv.org/abs/2104.08315 | yes (abstract, introduction) | Option-text scoring and surface-form competition |
| Yousefiramandi and Cooney | https://arxiv.org/abs/2512.12677 | yes, low weight | Verbaliser ablation, one seed |

## Candidates seen but not used
- Label Words are Anchors (https://arxiv.org/abs/2305.14160): mechanism in GPT2-XL and GPT-J for in-context learning; abstract read; no wording guidance, not used.
- Changing Answer Order Can Decrease MMLU Accuracy (https://arxiv.org/abs/2406.19470): order topic (Q3); abstract only.
- Lost in the Middle, LLMLingua-2, the compression survey, The Prompt Report, GLiNER multitask, GLiNER bi-encoder (https://arxiv.org/abs/2602.18487), and the body of "Every Wrong Answer Counts": downloaded or seen, not read for this note.
- Search hits: Climate-NLI (https://aclanthology.org/2024.paclic-1.57.pdf) was opened, and the "+/-20 F1" claim that a search summary attributed to it is **not** in it (the claim is in Ghilene et al. 2409.13735). Not opened: MaVEN verbaliser enrichment (https://arxiv.org/abs/2410.06173, abstract only, few-shot MLM verbalisers); Gen-Z label descriptions (https://arxiv.org/pdf/2311.07115, seen in results, not opened).

## Inaccessible or failed
- WebFetch of arXiv PDFs returned binary (3 papers); worked around with curl and pdftotext.
- https://docs.claude.com/en/docs/about-claude/use-case-guides/classification redirected to https://platform.claude.com/docs/en/about-claude/use-case-guides/classification, which returned 404. The XML-tags page redirected to the general prompting best-practices page, which was read for structure and long-context statements only.
- Climate-NLI PDF (https://aclanthology.org/2024.paclic-1.57.pdf): opened via curl, but the sought claim was not there (see above).
- No paywalled source was needed. Vendor docs for GLiNER2 and GLiClass contain no effect sizes.

## Coverage
Covered with at least one opened source: format and paraphrase sensitivity and reporting; instruction semantics; instruction detail for classification; data-boundary sentences; irrelevant-context effects (generation); compression; answer symbols and option-ID readers; label-word choice; label and option descriptions (LLM, MLM encoder, NER scorers); NLI hypothesis wording; GLiNER/GLiClass documentation; option count; near-neighbours; none-of-these and hand-off for chat LLMs; Jev and clone documentation on option writing.

## Gaps (a failed search is not evidence that no work exists)
1. Terse versus full instruction for letter-logit, pointer-head or encoder readouts: nothing found. Searches 11, 14 and 15 returned generative or training-time results only.
2. Distractor and irrelevant-context effects on encoders and option scorers: nothing found; the lab's J result (23 new failures after adding state) has no published comparator here.
3. Label-description ablations for GLiNER2 or GLiClass: not found; only feature statements.
4. Option count from 2 to about 50 at fixed difficulty for logit readers: not found; evidence is confounded (MMLU-Pro) or from generative or vendor sources.
5. Compression of short classification prompts: not found.
6. Near-neighbour options with an abstain option, for scorers: only an abstract-level preprint and vendor advice.
7. Decisiveness and "if none, clarify" clauses: not found outside the abstention literature (see q5).
8. Several items rest on abstracts or fetch summaries (listed in the evidence note); upgrading them needs the full text.

---

# Search log fragment: Q3 (order and format), access date 2026-10-03

## Queries (WebSearch)
1. option order selection bias multiple choice LLM debiasing permutation 2025 arXiv
2. PriDe prior estimation selection bias "Large Language Models Are Not Robust Multiple Choice Selectors"
3. position bias cross-encoder reranker candidate order sensitivity pointwise vs listwise
4. permutation consistency as uncertainty confidence multiple-choice LLM order sensitivity calibration error detection
5. zero-shot classification label order sensitivity GLiNER GLiClass label permutation encoder NLI candidate label order bias
6. arXiv sensitivity gap order permutation correlates with error rate ... "Mitigating Order Sensitivity"
7. UniBias OR CalibraEval OR PINE selection bias ... comparison PriDe results
8. modern LLMs option position bias small or negligible frontier models MMLU option shuffle 2025 replication
9. perturbation consistency uncertainty quantification prompt paraphrase option shuffling confidence estimate LLM classification calibration

## Opened and used (see evidence note for details)
Zheng 2309.03882 (ar5iv); Pezeshkpour 2308.11483 (ar5iv); Wei 2406.03009; Gupta 2406.19470; Wang 2402.14499; 2404.08382; Reif 2405.02743; Zhao 2102.09690 (abstract); Robinson 2210.12353 (ar5iv); Xue 2406.01026; Wang 2305.17926; Hanna 2608.11947; 2607.20864; Alzahrani 2402.01781 (abstract) and HF MMLU blog; Set-Encoder 2404.06912; GLiClass 2508.07662; 2403.13590; 2406.06581; 2603.21016; 2509.11208; 2511.21860; SPUQ 2403.02509 (abstract); CalibraEval 2410.15393 (abstract).
Inclusion reasons: direct evidence on option-order/ID bias, PriDe or permutation countermeasures, readout dependence, calibration, encoder/reranker order effects, order disagreement as uncertainty.

## Opened but excluded
- 2604.26206 (option-order randomisation in prompted sandbagging): Llama-3-8B, MMLU-Pro 10 options; about deliberate underperformance, not bias estimation.
- Search hits not opened: UniBias 2405.20612, PINE 2407.01100 (not searched directly), Set-LLM 2505.15433, Dual Group Advantage 2605.11974, 2604.27599, 2607.24869, 2411.04602, 2407.06716, Mapping from Meaning 2510.17028, 2410.19195, Megagon blog, Medmarks.

## Inaccessible
- PDF forms of 2309.03882v4, 2308.11483, 2604.26206 (first try), 2608.03091, SPUQ ACL PDF returned binary; the first two read via ar5iv, SPUQ and 2410.15393 only via abstract, 2608.03091 not read (title only).
- Note: WebFetch returns a model summary, not raw text. Section/table numbers from the Zheng ar5iv summary were inconsistent ("Table 2.4") and need checking against the PDF before quotation. Venues for Pezeshkpour (NAACL Findings 2024), Robinson (ICLR 2023) and Wang 2402.14499 were not verified in the fetched pages.

## Coverage
Covered: ID/position bias size, PriDe, permutation averaging, distillation/training, calibrate-before-use and its negative result, readout dependence (first-token vs text vs sequence), symbol effects (ID symbol swap, symbol binding), listwise cross-encoder order effects, order disagreement for judges.

## Gaps
- No source on order effects in span-pointer scorers (K27) or in joint label-text encoders (GLiNER/GLiClass J, G); only the by-construction argument for pointwise cross-encoders and listwise reranker results.
- No test of letters versus key text or description text as symbols; only ID-symbol swaps (letters, lowercase, digits).
- No published error-detection score (precision/recall) for order disagreement on small-option classifiers; only judge-entropy human-review result and correlational links.
- PriDe replication by independent groups seen only as a baseline (11, 18); no independent re-estimation of its 5% budget claim; no 2025-2026 test on modern instruction-tuned chat models read by logits except 5b (2024).
- No test on abstention / "none of these" option position.
- Many hits are 2026 preprints I read by summary only; their reliability is unvetted.

---

# Search log fragment: Q4 second passes

Date of all searches and fetches: 2026-10-03. Tools: WebSearch for discovery; arXiv PDFs downloaded with curl and read as extracted text (pdftotext) for the passages cited in [evidence/q4-second-passes.md](../evidence/q4-second-passes.md). WebFetch on PDFs returned unusable summaries (binary), so it was abandoned for papers. A search is not evidence that no work exists.

## Queries run

WebSearch (each returned ranked links; the ones used are listed under candidates):
1. first token probability does not match text answer multiple choice "My Answer is C" mismatch
2. permutation disagreement uncertainty multiple-choice LLM option order inconsistency predicts errors abstention
3. weak verifiers ensemble Weaver shrinking the generation-verification gap 2025
4. self-correction blind spot LLM Self-Correction Bench 2025 correct others' errors but not own
5. ensemble of small LLMs majority vote text classification outperforms single larger model diversity error correlation 2024 2025
6. paraphrase prompt ensemble multiple-choice logit averaging across prompt variants improves accuracy calibration LLM
7. process of elimination prompting large language models multiple choice option elimination LLM zero-shot 2024 2025 evaluation
8. LLM-as-a-judge self-consistency repeated judgments agreement not correctness verification noise reliability 2025
9. LLM rerank top-k candidates from small classifier few-shot text classification intent detection candidate labels second-stage LLM improves
10. zero-shot NLI classification hypothesis template ensemble multiple templates averaging effect cross-encoder entailment
11. LLM judge same model verifier shares errors with generator correlated verification weak generator strong verifier same family self-verification multiple choice 2025
12. Prompt Repetition Improves Non-Reasoning LLMs repeat the prompt twice
13. Condorcet jury theorem LLM ensemble majority voting correlated errors diversity limits empirical 2025 multiple-choice

Direct fetches (known originals, followed from citations in the lab notes and in the sources): arXiv 2203.11171, 2310.01798, 2406.01297, 2309.11495, 2310.15575, 2303.08559, 2310.12397, 2402.08115, 2310.08118, 2311.08516, 2406.15673, 2404.17140, 2404.13076, 2410.21819, 2306.05685, 2502.00674, 2506.07962, 2403.02419, 2402.05120, 2406.04692, 2306.13063, 2407.21787, 2402.14499, 2506.18203, 2507.02778, 2603.21016, 2511.21709, 2607.20864, 2603.12123, 2604.18547, 2311.08596, 2310.13548, 2305.11738, 1612.01474, 2210.02441, 2401.02994, 2306.02561, 2412.06593, 2502.06233, 2607.08065, 2511.15714, 2412.00166, 2501.15175, 2609.13824, 2606.19544, 2311.09649, 2509.17995, 2512.14982, 2605.29800, 2512.17630, 2607.17384; ACL Anthology PDF of Rating Roulette; workshop PDF of "Calibrating Black Box LLMs with Prompt Variations".

## Candidates and decisions

Included in the evidence note (read at the cited passage): 2203.11171, 2306.13063, 2403.02419, 2402.05120 (voting and confidence); 2310.01798, 2406.15673, 2406.01297, 2402.08115 (with precursor 2310.08118 at table level), 2311.08516, 2404.17140, 2507.02778, 2311.08596 (self-correction and re-asking); 2309.11495, 2305.11738, 2509.17995, 2506.18203, 2407.21787 (verification); 2310.15575, 2501.15175, 2303.08559 (elimination and reranking; D2 matches the lab's letter-logit readout); 2210.02441, workshop calibration paper, 2511.21709, 2412.00166, 2511.15714, 2605.29800, 2506.07962 (prompt and model ensembles, error correlation); 2404.13076, 2410.21819, 2306.05685, Rating Roulette, 2607.08065 (judges and self-agreement); 2402.14499, 2512.14982, 2502.06233 (readout and re-reading effects). Inclusion reason in each case: it measures a second-pass or aggregation method with numbers, or documents the condition (error correlation, calibration, verifier strength, readout) under which one works or fails; recency preferred, originals followed for self-consistency, CoVe, self-correction and POE.

Opened but not used as evidence: 2603.12123 (cross-context review; mentioned in the non-replication section only because its first version's advantages did not hold in the revised averages; single model, injected errors in code and documents); 2604.18547 (FUSE, verifier ensembling; read abstract only, same family as Weaver); 2603.21016 and 2607.20864 (Q3 topics, covered by q3 note); 2412.06593 (anchoring; not read to the passage level); 2310.13548 (sycophancy; not read to the passage level, FlipFlop used instead); 2306.02561 (LLM-Blender) and 2401.02994 (Blending); 2406.04692 (Mixture-of-Agents); 1612.01474 (Deep Ensembles, image and regression, not language); 2609.13824 and 2606.19544 (judge consistency, abstract level only); 2311.09649 (ICXML, extreme multi-label with huge label sets, different regime); 2512.17630 and 2607.17384 (weighted small-model ensembles, downloaded, not read to passage level). Reasons: not directly on a second pass for closed option lists, generative-only with weak controls, or not read deeply enough to cite.

## Inaccessible or partly accessible

- OpenReview PDF of "Calibrating Language Models via Augmented Prompt Ensembles" (id L0dc4wqbNs): browser verification page only, no text. Replaced by the earlier workshop PDF (static squarespace link), which was readable.
- ACL Anthology pages for POE (2023.emnlp-main.273) and "My Answer is C" (2024.findings-acl.441): appeared in search results, not opened; arXiv versions read, venue statements rest on the listings.
- NeurIPS 2025 and ICML 2025 pages for Weaver: appeared in search results only.
- WebFetch of arXiv PDFs: binary or size-limit failures (2203.11171 over 10 MB; POE, filter-then-rerank unreadable). Direct download plus pdftotext was used instead.
- Venue lines not visible in extracted text for many arXiv papers; grades follow what the opened text shows, otherwise B.

## Coverage against the assignment

- Self-consistency: covered (A1, A3, A4, F5, G3). Verification chains and CoVe: covered (C1, C3, C4). Intrinsic self-correction and failure without external feedback: covered (B1-B8). Process-of-elimination: covered (D1, D2). Top-k re-ranking: covered with one source (D3) plus elimination on option IDs (D2). Generate-then-verify with external tools: CRITIC (C2), sound-verifier results (B4), survey (B3). Prompt ensembles and wording votes: A1 Table 7, E1, E2, E3, E4. Multi-model voting and weak-model ensembles: A1 Table 10, E4, E5, E6, E7, C4. Judge self-agreement and self-preference: F1-F5.
- Model kinds and conditions: readout match recorded per source; error correlation (E1, E6, E7, C4), calibration (A2, E2, G3, F5), verifier strength versus generator strength (C3, B6), task dependence (D1, A3, B2).

## Gaps

- No opened source on second passes for pointer-head or encoder scorers; no source on whether order-reversal disagreement predicts errors; no source on verification for abstention classes in option-list classification; no Japanese-language evidence; prompt-variant voting on letter-logit readers rests on one small, old study (E2) and the permutation-vote paper (E3).
- A top-k reranking source on closed label sets with a modern small classifier as first stage was not found beyond D3 (information extraction); the ICXML result is for extreme label spaces.
- Several 2026 preprints surfaced (weighted ensemble lift, committee voting thresholds, verifier ensembling) and were not read to passage level; they may add evidence on weighted voting and error correlation.
- Venue verification and replication checks were limited to what the opened text showed; no citation-count or follow-up replication search was done per paper beyond the contradictions listed in the evidence note.

---

# Search-log fragment: Q5 and Q6 (step2/step3)

Date of all searches and fetches: 2026-10-03. Tools: WebSearch (US-only), WebFetch (returns a small-model summary of the page), plus `curl` and `pdftotext` on arXiv, ACL Anthology and raw GitHub files for full-text reading. Evidence notes: [../evidence/q5-abstention.md](../evidence/q5-abstention.md) and [../evidence/q6-readout-and-vendor.md](../evidence/q6-readout-and-vendor.md). A failed search is not evidence that no work exists.

## Queries run
1. "none of the above" option multiple-choice LLM abstention benchmark arXiv 2024 2025
2. abstention LLM survey "Know Your Limits"
3. AbstentionBench reasoning LLMs fail on unanswerable questions
4. GLiClass label descriptions zero-shot classification encoder GLiNER labels prompt
5. missing premise detection LLM "MiP" overthinking missing premises reasoning models
6. zero-shot text classification NLI hypothesis template sensitivity label wording cross-encoder
7. out-of-scope intent detection LLM classifier abstain threshold "none of the above" CLINC OOS 2025
8. Anthropic docs classification prompt "other" category unknown allow Claude to say "I don't know"
9. OpenAI structured outputs classification guide enum "other" or "unknown" option prompt best practices
Direct fetches (no search): Jev docs pages, Liquid docs, Hugging Face and GitHub model pages of the lab systems and clones, Gemini prompting guide, arXiv IDs followed from citations (Kadavath, Plaut, Wang first-token, Webson, QuestBench, MedAbstain, Madhusudhan, Tomani, GLiNER, GLiNER2).

## Candidates and decisions
| Candidate | Decision | Reason |
|---|---|---|
| Tam 2025 NOTA (2503.01550) | included, full text | 28 LLMs, phrasing table, SFT/DPO trade-off |
| Góral 2024-25 (2409.00113) | included, full text | instruction conditions per model, prompt paraphrase table |
| Madhusudhan 2025 Abstain-QA (2407.16221) | included, full text | option IDK/NOTA plus abstain clause, coverage trade-off |
| AbstentionBench (2506.09038) | included, full text | scale, reasoning, system prompt effects |
| Kadavath 2022 (2207.05221) | included, full text (Sec. 3.1) | original NOTA calibration result, letter readout |
| Plaut 2025 TMLR (2402.13213) | included, full text | matching letter-logit readout, MSP abstention |
| MedAbstain (2601.12471) | included, full text | logprob readout, missing-context recall 13% |
| QuestBench (2503.22674) | included, full text | "not sure" rate on underspecified problems |
| MiP-Overthinking (2504.06514) | included, full text | generative-only mechanism, negative for reasoning |
| Prompt-artifact abstention (2507.16199 v9) | included, summary only | conflicting claim; flagged unreplicated |
| Tomani 2024 (2404.10960) | included, abstract only | softmax-based abstention |
| Wen 2025 survey (TACL) | included as map, abstract only | no effect sizes taken |
| Premise critique PCBench (2505.23715) | opened (full text searched), not used in notes | only qualitative: models rely on explicit prompts to flag errors; no readout match; no numbers extracted |
| "Beyond Solving Math Quiz" (2508.11252) | opened (downloaded), not used | not read beyond download; generative reasoning models |
| Ravikumar 2026 (2609.17686) | excluded | position paper, no measurements |
| Ma 2021, Bareiß 2024, Webson 2022, BTZSC | included, full text | encoder and NLI evidence |
| GLiClass, GLiNER, GLiNER2 papers | included, full text | label descriptions, negative sampling |
| Wang 2024 first-token (2402.14499) | included, full text | readout mismatch |
| 2608.20371, 2507.01541 | included, summary only | encoder versus LLM OOS |
| Jev docs, Liquid docs, model cards, Kev, Decider, Verdict, Laya, Tev1, Navya, allanrbo | included, summaries (Kev and Decider also raw text) | vendor and practitioner sources |
| Anthropic reduce-hallucinations, OpenAI structured outputs, Gemini prompting | included as guides | classification and uncertainty statements only |

## Inaccessible or unusable
- Anthropic classification use-case guide: 404 at both docs.anthropic.com redirect and platform.claude.com path.
- Kev PLAN via the GitHub HTML page returned only navigation; the raw file was fetched with curl instead.
- Hacker News thread on Jev (listed in study/close/jev.md) was not opened. Jev blog page returned only a short summary without writing guidance. NeurIPS poster page and COLM page were not opened (venue statements marked as taken from search results).
- All HTML pages read through WebFetch carry the summariser's possible omissions; numbers from them (Verdict, Laya, Navya, cards) were not checked against full text except Kev and Decider READMEs.

## Coverage and gaps
- Q5: good coverage of generative LLMs and some letter-logit evidence (Kadavath, Plaut, MedAbstain). Gaps: no external study on abstention with pointer-head or encoder readouts; no study isolating an abstain clause on a logit-readout model; nothing on a "hand-off" or "need more information" option compared with "none of the above" as separate options.
- Q6: good coverage of NLI cross-encoder zero-shot literature (older) and the lab systems' own documentation. Gaps: no label-description ablation for GLiClass or GLiNER2; no template study for current cross-encoders; no external order-permutation study for encoders (only Laya's own logit spreads); nothing peer-reviewed on Jev-style decision models.
- Not searched: Japanese or other non-English abstention evidence beyond Bareiß 2024; calibration under distribution shift beyond the vendors' own reports; process-of-elimination and second-pass literature (Q4, other agents).
