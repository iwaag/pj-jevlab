# Guidelines: instruction, option and second-pass design for Jev-style decision models

Written for `devdocs/episodes/study/prompt_best_practice/p1` step4 ([plan](../../devdocs/episodes/study/prompt_best_practice/p1/plan.md)). Evidence access date: 2026-10-03 (every source was accessed on that date). Every claim below is traceable to one of these notes. Nothing here comes from outside them.

- Lab results: [lab-evidence.md](lab-evidence.md) (rows Q1-1 ... Q6-7, R-1 ... R-6). These are measured on the lab's own authored cases (one agent family, no human-written inputs). Many are descriptive or inconclusive.
- External sources, by topic: [Q1/Q2 note](evidence/q1-q2-instruction-and-options.md), [Q3 note](evidence/q3-order-and-format.md), [Q4 note](evidence/q4-second-passes.md) (source labels A1 ... G3), [Q5 note](evidence/q5-abstention.md) (source labels S1 ... S12), [Q6 note](evidence/q6-readout-and-vendor.md) (labels A1 ... A9, C1 ... C10; these overlap with the Q4 labels, so every citation below names the file or the author).

## How to read this guide

**Readouts.** The lab's systems read the answer in different ways, and most of the published work uses a different one.

| Lab system | Readout | External evidence that matches |
|---|---|---|
| W12, A27 | option-letter logits, one forward pass | letter or option-ID probability studies (Zheng, Plaut, Sanz-Guerrero, PoE_ID, Guda) |
| K27 | pointer head: each option span scored | none found. Closest is GLiNER span scoring (partial) |
| J, G | encoders (label-in-input) | none controlled. Older NLI and zero-shot encoder work is partial |
| L27 | short generative JSON | most chat-LLM studies, but those usually let the model write reasoning, which L27 does not |

**Classification used for every recommendation.**
- **established**: several independent sources agree and at least some of them used a matching readout. Where the agreement exists only for generative models, the label says "established for generative models" and the lab-readout status is given separately.
- **plausible**: one source, or several sources on a different readout, or sources that disagree on size but agree on direction.
- **open**: conflicting or missing evidence.

**Grades** follow the plan: peer-reviewed controlled study (PR), preprint with code or data (PP), vendor or author evaluation (V), practitioner report (P), guide or opinion (G). The notes give the venue or "venue not checked" per source; where the notes mark a source as read at abstract or fetch-summary level only, that is stated here as "abstract only" or "summary".

**Lab match.** Each recommendation ends with the lab row(s) that match it. A lab result is a local observation on one set of cases, not a confirmation of the literature. Where lab and literature disagree or cover different readouts, the text says so.

**Effect sizes are as reported.** They are averages, maxima or single-cell values as stated, and they come from older or smaller models than the lab's trained decision models unless the source says otherwise.

**Chat-LLM findings.** A finding obtained on generative chat LLMs is labelled "(generative)". It is not carried to W12, A27, K27, J or G without saying so.

## Summary: what is established, plausible and open

| # | Recommendation (short) | Class | Where |
|---|---|---|---|
| R1.1 | Never judge a wording or format change from one prompt; report a distribution over many variants and instance-level inconsistency | established | Q1 |
| R1.2 | Expect wording effects to be model-specific and of either sign; test the wording on the target model | established as a phenomenon; size open for lab readouts | Q1 |
| R1.3 | Give definitions or fuller instructions where the category is not self-explanatory; do not expect them to help where it is | plausible | Q1 |
| R1.4 | Terse versus full instruction on option-logit, pointer or encoder scorers | open | Q1 |
| R1.5 | Keep irrelevant text out of the input; test before adding context | established for generative models; open for lab readouts | Q1 |
| R1.6 | Data-boundary sentence and delimiters | open | Q1 |
| R1.7 | Rules written into the question for a small letter-logit decision model | open (single author probe) | Q1 |
| R1.8 | Do not expect a "do not be biased" instruction or chain-of-thought to fix option bias | plausible | Q1, Q3 |
| R2.1 | Choose label words and option keys deliberately; they matter more than template wording | plausible | Q2 |
| R2.2 | Write option descriptions that separate options from each other; concrete and contrastive | plausible | Q2 |
| R2.3 | Give confusable options `what` / `not_for` fields | open (vendor guidance only) | Q2 |
| R2.4 | Keep option lists short; for very large lists shortlist or score one by one | plausible | Q2 |
| R2.5 | Do not use option keys that name an action if the input can contain text naming that key | open (lab result only) | Q2 |
| R2.6 | Letters versus option text as the answer symbol | open | Q2 |
| R2.7 | Make generic or fallback options look like buckets | plausible (author statement) | Q2, Q5 |
| R3.1 | Expect option-ID and order effects on letter-logit readers; measure them, do not assume zero | established | Q3 |
| R3.2 | Order effects shrink with model strength and are task-dependent; a small diagnostic can hide them | plausible | Q3 |
| R3.3 | Permutation averaging reduces bias at a cost proportional to the number of permutations | established | Q3 |
| R3.4 | PriDe-style prior estimation on a small subset | plausible | Q3 |
| R3.5 | Lower order sensitivity is not the same as higher accuracy | plausible | Q3 |
| R3.6 | Calibrate-before-use: do not apply blindly to instruction-tuned models | plausible (negative result) | Q3 |
| R3.7 | The readout implementation changes the number; fix and report it | established | Q3, Q6 |
| R3.8 | Encoders and pointer scorers: order sensitivity is architecture-dependent | open | Q3 |
| R4.1 | Do not expect a free-text second pass without outside information to help | established for generative models; open for lab readouts | Q4 |
| R4.2 | Verification that is blind to the first answer is better than verification shown the answer | plausible | Q4 |
| R4.3 | Same-family verifiers and voters share the generator's errors | established for generative/MCQ; plausible for lab readouts | Q4 |
| R4.4 | Voting over wordings gains little; voting over mixed-strength models can lose | plausible | Q4 |
| R4.5 | If a second pass is used, weight it by estimated accuracy, or let an independent signal enter | plausible | Q4 |
| R4.6 | Narrowing the options and re-asking (elimination) helps letter-logit readers with many options | plausible | Q4 |
| R4.7 | Top-k re-ranking helps only on samples where the first stage is uncertain | plausible | Q4 |
| R4.8 | Order disagreement as an error flag | open | Q4 |
| R4.9 | Confidence gates catch low-confidence errors only | plausible | Q4, Q5 |
| R5.1 | A closed option list with no fallback option pushes models to pick an answer; include fallback options | established for generative and older letter-logit LMs; untested for pointer/encoder/trained decision scorers | Q5 |
| R5.2 | Replacing a correct answer with "none of the above" costs accuracy; size depends on model and phrasing | established | Q5 |
| R5.3 | An abstain clause raises abstention and costs coverage; size is model-specific | established for generative models; open for lab readouts | Q5 |
| R5.4 | The wording of the abstain option matters, and a bare added option may trigger abstention | plausible | Q5 |
| R5.5 | Missing-information detection is the weak case; do not rely on the model to notice | established | Q5 |
| R5.6 | Threshold on max letter probability gives an abstention route for letter-logit readers | established for letter-logit LMs; open for trained decision models and K27 | Q5 |
| R5.7 | For encoder and span scorers, abstention is set at training time | plausible | Q5, Q6 |
| R5.8 | Explicit "not stated" markers in the input | plausible (lab result plus vendor statement) | Q5 |
| R6.1 | Do not carry a chat-LLM prompting result to a scorer without a test | established | Q6 |
| R6.2 | Encoders: label wording and templates matter; no controlled evidence for label-in-input encoders | open | Q6 |

## Q1. Instruction wording, structure and length

### R1.1 Report prompt sensitivity as a distribution, with instance-level inconsistency
- **What to do:** When comparing wordings, formats or option orders, evaluate many plausible variants (not one), report max, average, median and a quantile or an interval, and report per-item inconsistency (how many answers change), not only accuracy. Do not compare two models or two wordings on a single prompt.
- **Evidence and grade:** Sclar et al. (ICLR 2024, PR): spread up to 76 accuracy points on one LLaMA-2-13B task, median spread 7.5 points over 10 sampled formats (a lower bound), and model comparisons reverse under another format with probability 0.141 for LLaMA-2-13B vs 70B. Mizrahi et al. (TACL, PR): significant ranking differences across paraphrases on 21 of 25 tasks; 15 of 25 with negative average Kendall's tau. Voronov et al. (PP): template standard deviation up to 35% of the mean. POSIX (EMNLP Findings 2024, PR) and ProSA (PP, instance-level PromptSensiScore) agree. PromptEval (PP, abstract and introduction only) proposes estimating the distribution over about 100 templates cheaply. See [Q1/Q2 note](evidence/q1-q2-instruction-and-options.md), "Sensitivity and reporting sources".
- **Readouts:** Sclar: probability ranking over valid options on base and early chat models (partial for letter logits). Mizrahi: generation (not matching). POSIX: log-likelihood (partial). Mostly 2022-2024 base and chat models up to 70B.
- **Effect size:** "up to 76" is the maximum over 53 tasks. The median is 7.5 points.
- **Exceptions and cautions:** Spread statistics grow with the number of variants and with sampling noise. The notes found no source that separates prompt-induced spread from finite-sample noise. Sensitivity shrinks with scale in some studies (ProSA, He et al.) and persists in others (Sclar).
- **Class:** established (as a phenomenon and as a reporting practice). Effect size for the lab's trained decision models: open.
- **Lab match:** [Q1-1](lab-evidence.md#q1-instruction-wording-structure-and-length) (F1-F3 changed 6-9 of 60 choices for W12, K27, A27, D35, L27; 26 for J; 36 for G). The lab's F1-F3 wordings are unreviewed and the cells are 20 cases, so the lab number is a screening figure. The lab results agree in direction with the literature (wording matters, size differs by system), but the lab does not report an interval over many wordings.

### R1.2 Expect wording effects to be model-specific and to differ in sign
- **What to do:** Test any wording change on the model that will be deployed. Do not transfer "terse is better" or "formal is better" from another model or readout. Keep alternative wordings as a regression set.
- **Evidence and grade:** Mizrahi et al.: one word edit ("excludes" to "lacks") changed Flan-T5-large by -28% and Flan-T5-XL by +46% (section 4.2, generation, PR). Voronov et al.: the best templates do not transfer between models of the same family (PP). Gao et al. (EMNLP 2023, PR) and Webson and Pavlick (below) show template sensitivity on encoders and verbaliser readers. Goral et al. (PP): the same one-sentence warning gave about 0% for some models and about 100% for others (generative, arithmetic; see R5.3).
- **Exceptions:** None of these sources used a trained decision model.
- **Class:** established as a phenomenon; the size for W12, A27, K27, J and G is open.
- **Lab match:** [Q1-2, Q1-3](lab-evidence.md#q1-instruction-wording-structure-and-length): terse F1 helped K27 on W3 (15/20 to 18/20) and L27 on W3 (12/20 to 15/20) but hurt A27 on W2 (19/20 to 16/20). [Q1-4](lab-evidence.md#q1-instruction-wording-structure-and-length): in the dev pilot terse wording pushed A27 and K27 towards over-rejection. Signs differ by system and class, which matches the literature. All descriptive on 20 cases per cell.

### R1.3 Add definitions where the category is not self-explanatory
- **What to do:** Give a codebook-style definition or a short description of each category where the label alone does not say what is meant; do not spend length where labels are self-explanatory.
- **Evidence and grade:** Celebi and Penczynski 2026 (PLOS ONE, PR; fetch summary only, numbers not checked against the PDF): minimal to verbatim codebook raised accuracy by about +17 to +37 points on two theory-dependent tasks (for example GPT 5.4 47.4 to 81.3) and by about 0 to +3 points (not significant for GPT 5.4) on a task with self-explanatory categories. Walshe et al. (PP): label plus a generated 50-word description raised Mistral-7B zero-shot macro accuracy, for example Banking77 81.6 to 88.8 and AG News 76.2 to 83.4 (descriptions were generated from training examples on public datasets, so leakage is possible). Gao et al. (PR): label-description fine-tuning of RoBERTa raised zero-shot accuracy by about 17-19 points. Li et al. (LOADS, PP): elaborating a label word had limited average impact, with changes above 0.2 on certain dataset-model pairs in both directions.
- **Readouts:** Celebi and Walshe: generation (not matching). Gao: masked-LM encoder with verbalisers and training on the descriptions (partial). LOADS: first generated token (partial).
- **Exceptions:** Smaller models did best with instructions but little context; extra context can hurt them (Celebi). No ablation was found for GLiNER2 or GLiClass descriptions; their documentation only says descriptions are supported. The GLiNER2.5-Decide card says: pass a short description when the label name is not enough ([Q6 note](evidence/q6-readout-and-vendor.md), C3, vendor).
- **Class:** plausible.
- **Lab match:** [Q1-6, Q1-7, Q2-1](lab-evidence.md#q2-option-keys-and-descriptions): in the game task, concrete verb-rich option descriptions v3 beat generic v1 (v1 made 11 more cases fail), on J. This is direction-consistent, on one author's n = 59 (descriptive).

### R1.4 Terse versus full instruction on lab-type readouts is open
- **What to do:** Treat the question as unresolved. If a terse variant is tried, test it per system and per case class and report the sign for each.
- **Evidence and grade:** No source isolates terse versus full instruction wording for option-logit, pointer or encoder scorers ([Q1/Q2 note](evidence/q1-q2-instruction-and-options.md), "Coverage and gaps"). The only controlled instruction-length result is Celebi and Penczynski (generative, task-dependent, see R1.3). Prompt compression work targets long contexts and demonstrations; for short contexts all methods lose performance as the ratio rises (Zhang et al. 2025, workshop paper). A pre-registered trial found that retaining about 20% of a production instruction raised cost by 1.8% because outputs grew (preprint, abstract only, quality by embedding similarity).
- **Class:** open.
- **Lab match:** [Q1-1 to Q1-4, Q5-10](lab-evidence.md#q1-instruction-wording-structure-and-length). The two lab results on terse wording point in different directions (K27 on W3 improved; the dev pilot and A27 on W2 got worse). No published counterpart exists to say which to expect. The proposed terse-wording experiment would therefore be new, not a repetition (to be assessed in step 5).

### R1.5 Keep irrelevant text out of the input; test before adding context
- **What to do:** Send only what the decision needs. Before adding more context to the request (for example robot state, history, long preambles), test the effect on the target model.
- **Evidence and grade:** Shi et al. (PP): accuracy drops sharply when an irrelevant sentence is added (GSM-IC); an instruction "feel free to ignore irrelevant information" gave +5.4 points (72.4 to 77.8, code-davinci-002) and +2.9 (68.4 to 71.3, text-davinci-003), not significance-tested. Levy et al. (PP): average accuracy over models fell from 0.92 to 0.68 as padding grew to 3,000 tokens. Cuconasu et al. (SIGIR 2024, PR): one related distractor document lowers accuracy by up to 0.24; more distractors by up to 0.38. **Contradicting result in the same paper:** random unrelated documents raised accuracy by up to 0.07 (+35%) in some settings. Alzahrani et al. section 5.4 (PP): off-subject few-shot examples changed performance only slightly.
- **Readouts:** all generation on 2022-2024 models (not matching). No source on encoders, cross-encoders, option-logit or pointer scorers.
- **Exceptions:** "Irrelevant text hurts" is not a rule (Cuconasu, Alzahrani). Levy's padding range (250-3,000 tokens) is larger than the lab's roughly 2,800-character long-context axis.
- **Class:** established for generative models; open for the lab's readouts.
- **Lab match:** [Q1-8](lab-evidence.md#q1-instruction-wording-structure-and-length): adding 7 lines of visible state to J changed top-1 on 26 of 59 cases (23 newly failing), with no published counterpart found. [Q2-3](lab-evidence.md#q2-option-keys-and-descriptions): large systems were 6/6 at all positions of a decisive sentence among about 2,800 characters of irrelevant paragraphs (n = 6 per cell, screening size).

### R1.6 Data-boundary sentences and delimiters: evidence conflicts, effect on scorers unknown
- **What to do:** If the input can contain instruction-like text, do not rely on a sentence alone. Delimiters or datamarking have measured effects on generative models; test whatever is used on the actual scorer.
- **Evidence and grade:** Hines et al. 2024 (Microsoft preprint, PP): a defensive instruction alone had negligible effect on attack success on GPT-3.5-Turbo; delimiters about halved it; datamarking cut it from about 50% to below 3%. Jia et al. 2025 (PP; introduction and related work only): states, second-hand, that delimiter and tag wrapping "are largely ineffective". The two papers use different models and attack sets.
- **Readouts:** generation, older models (not matching). Effect on logit-readout, pointer or encoder scorers: not found.
- **Class:** open.
- **Lab match:** [Q1-9, Q1-10, Q6-4](lab-evidence.md#q1-instruction-wording-structure-and-length): K27 had no boundary sentence and was not steered by appended instructions; W12 had one and was steered by a direct request; L27 had one and followed key-naming overrides 3/20. The sentence was confounded with base model, readout and training, so the lab data cannot say whether it works. Descriptive, screening size.

### R1.7 Rules written into the question may not be followed by small letter-logit decision models
- **What to do:** For a small trained letter-logit decision model, do not assume that a paragraph of rules in the question will be applied. Put a stable convention into training data (supported by the Decider author probe) and check the model with a probe. Moving it into structured input fields is an untested implementation hypothesis.
- **Evidence and grade:** One author statement, the Decider README ([Q6 note](evidence/q6-readout-and-vendor.md), C6; V; raw text read): rules written into the question "are not followed at this size", a one-sentence question scores 0.67 and a paragraph of rules 0.24 on the form-filling probe; n not read.
- **Readout:** letter logits via slot readout (matching in kind for W12/A27, but this is one model family, D35).
- **Class:** open (single author probe, not replicated).
- **Lab match:** [R-3](lab-evidence.md#reference-observations-that-frame-the-wording-and-abstention-evidence): supplied priority orders separated systems (K27 and A27 4/4 swap pairs, W12 and L27 1/4, D35 and J 0/4). This agrees in direction that rules in the input are not equally followed, but the lab test is a different design.

### R1.8 Do not expect "do not be biased" instructions or chain-of-thought to fix option bias
- **What to do:** Do not use an added instruction as the main remedy for option-order or option-ID bias.
- **Evidence and grade:** Zheng et al. (ICLR 2024, PR): simple debiasing instructions and chain-of-thought gave little (RStd 6.1 and 4.5 for gpt-3.5-turbo on MMLU). Pezeshkpour and Hruschka (PP): few-shot gave only marginal gains. Both on generative-or-letter readouts with 2023 models.
- **Class:** plausible (two sources, partial match).
- **Lab match:** none (the lab did not test a debiasing instruction).

## Q2. Option keys and descriptions

### R2.1 Choose label words and option keys deliberately
- **What to do:** Treat the key or label word as a design choice that is tested, not a free name. Prefer semantically meaningful, plain label words and check two or three alternatives on the target model.
- **Evidence and grade:** Webson and Pavlick (PP): models learned about as fast with irrelevant or misleading templates as with instructive ones, but the choice of target words (yes/no, then yes-no-like, then arbitrary, then reversed targets) mattered much more (Figure 8; ALBERT, T5, T0, GPT-3; rank classification). LOADS (PP): changing only the label words moved F-score by more than 0.1 on every dataset and model and by more than 0.2 on more than half of the datasets (stance, 8B models, generation); some label sets caused degenerate outputs. Ghilene et al. (NLI cross-encoders): changing the verb in the hypothesis template changed average F1 by about +/-20; the best template was chosen on the evaluation data, so this is not a clean held-out estimate. Wei et al. (PP, abstract only): with semantically unrelated labels small models fail and instruction tuning strengthens reliance on semantic priors.
- **Readouts:** rank classification of label words (partial); first generated token (partial); NLI entailment (partial, nearest published family to J and G).
- **Exceptions:** Webson and Pavlick used pre-2023 models and one task family. It shows these models do not use template semantics, not that wording never matters for current instruction-tuned models.
- **Class:** plausible.
- **Lab match:** none directly. The lab did not vary key naming for accuracy; see R2.5 for key names that invite override.

### R2.2 Write option descriptions that separate options from each other
- **What to do:** Make each description concrete and contrastive (what separates this option from its neighbours), not generic.
- **Evidence and grade:** vendor and author guidance only: Jev choice docs ("Write descriptions that separate the options from each other"), how-to-build guide (contrastive criteria, consistent field names), Liquid guide (pair each option with a descriptive explanation), OpenJev Verdict author claim that hypothesis framing "It is {description}" lifted accuracy (no number in the summary) ([Q1/Q2 note](evidence/q1-q2-instruction-and-options.md) and [Q6 note](evidence/q6-readout-and-vendor.md), C1, C2, C9; V, summaries). Controlled support for descriptions generally is in R1.3.
- **Class:** plausible (guidance plus indirect evidence from R1.3).
- **Lab match:** [Q2-1, Q1-7](lab-evidence.md#q2-option-keys-and-descriptions): J, game task, descriptions v3 (concrete) beat v1 (generic); v4 and v5 did not beat v3. Descriptive, one author.

### R2.3 For confusable options, add `what` / `not_for` fields
- **What to do:** Where options are easily confused, state in each description what it is for and what it is not for, optionally with examples.
- **Evidence and grade:** Jev documentation recommends it (V, summary; no measurement). A 2026 preprint (abstract only): top-K retrieval does not help the model separate similar labels; adding known confusable partners plus pairwise rules raised macro F1 by up to 10.0 points (generative LLM, three benchmarks).
- **Class:** open (vendor guidance and one abstract-only preprint on a different readout).
- **Lab match:** none.

### R2.4 Keep the option list short; use a shortlist or one-by-one scoring for very long lists
- **What to do:** Prefer a small candidate list. For lists of tens of options, narrow with a shortlist or score options independently, and test. Scope: the controlled support is generative (Mistral-7B, 77 labels) plus vendor statements; the lab's own 4/8/16-option screening found no effect on the large systems, so run a system-specific test before adding a shortlist stage.
- **Evidence and grade:** Walshe et al. (PP): putting 77 Banking77 labels with descriptions into one prompt collapsed Mistral-7B macro F1 to 4.0 (generation). GLiClass paper (PP): performance gets harder with very large label sets, attributed to positional encoding and attention limits; no ablation. Laya README (V, summary): degrades above about 20 options (shared token budget); Jev docs: up to 255 options, two-stage scoring for larger sets. MMLU-Pro's 4-to-10 option drop is confounded with harder questions and is not an option-count effect. Zheng et al. covered 2 to 5 options only.
- **Exceptions:** no controlled study varies 2 to about 50 options at fixed difficulty for option-logit, pointer or encoder scorers.
- **Class:** plausible.
- **Lab match:** [Q2-3](lab-evidence.md#q2-option-keys-and-descriptions): 4, 8, 16 candidates gave no effect on large systems (6/6); J was 1/6 on routing at every count. The lab sizes are far below the 77-label failures, so no conflict. Screening size.

### R2.5 Avoid option keys that name an action when the input may name that key
- **What to do:** Where the input can contain instruction-like text (for example free-chat orders), do not choose keys that read as commands such as `reset_breaker`, because input text naming a key was followed by most systems. Use neutral keys or map keys to descriptions.
- **Evidence and grade:** lab result only. No external source tests key naming as an override channel. External context: Wei et al. (PP, abstract only) say semantic labels carry prior weight; Hines (R1.6) on injection in generative models.
- **Class:** open (lab-only, descriptive).
- **Lab match:** [Q2-2, Q1-9](lab-evidence.md#q2-option-keys-and-descriptions): key-naming overrides followed by D35 20/20, K27 19/20, J 20/20 and L27 3/20; key-free overrides D35 5/20, K27 1/20, L27 0/20, J 0/20. Confounded with the data-boundary sentence (L27's native prompt has one).

### R2.6 Letters versus option text as the answer symbol is not settled
- **What to do:** Keep the symbol convention fixed and part of the interface contract. If bias is a concern, test option-text scoring or hybrid scoring against letters on the target model.
- **Evidence and grade:** Zheng et al. (PR): replacing A/B/C/D by a/b/c/d, 1/2/3/4 or (A)(B)(C)(D) did not remarkably reduce RStd; removing IDs and scoring option text lowered RStd (MMLU 5.5 to 1.0) with accuracy about unchanged (67.2 to 66.7). Alzahrani et al. (PP): rare or shuffled symbols did not remove bias, hybrid scoring recommended. Sanz-Guerrero et al. (PP, letter logits): tokenising the space with the letter changes accuracy by up to 11% on small base models and by 0.3-1.5 points on large instruct models (significant for Llama-3.1-8B, not for Gemma 3 12B). Robinson and Wingate (ICLR 2023, PR): the letter format beats cloze only for models with high symbol binding (Codex OpenBookQA 83.0 vs 65.6), and loses for GPT-3 (41.4 vs 57.4). Hanna and Feng 2026 (PP, single run): hiding options and scoring independently lowered accuracy in most model-benchmark pairs (see R3.5). ABCD 2026 (PP): uniform unordered labels with full-text answers cut accuracy variance about 3x, but Llama-3.1-8B did not improve.
- **Readouts:** letter logits (matching) on base and chat models; ABCD is generation plus embedding matching.
- **Exceptions:** whether a letter interface works depends on symbol binding, which fine-tuned W12 and A27 were presumably trained for (the Q1/Q2 note marks this as inference, not tested).
- **Class:** open for trained decision models; the facts on untrained models are established by several sources.
- **Lab match:** [Q3-7](lab-evidence.md#q3-option-order-and-format): the lab did not vary the symbol.

### R2.7 Make generic and fallback options look like buckets
- **What to do:** Write the "other" or fallback option as a described bucket (what it catches), not a bare word, and avoid a generic option next to a near-synonym of an in-scope class.
- **Evidence and grade:** Decider README (V, raw text): "Generic options need to look like buckets... A plain `support` next to `other` sends an in-scope complaint to `other`" ([Q6 note](evidence/q6-readout-and-vendor.md), C6). Jev docs recommend an `other` or `none of the above` option when the list may not cover every input (V, summary). Tev1 blog used an explicit "none of the listed intents matches" option inside the list.
- **Class:** plausible (author statements only, no measured effect).
- **Lab match:** [Q2-6, Q5-1](lab-evidence.md#q5-abstention-none-of-the-above-and-missing-information-detection): the lab used five separately named fallback classes and a `none_of_these`; the lab did not vary the fallback description.

## Q3. Option order and format

### R3.1 Expect option-ID and order effects on letter-logit readers
- **What to do:** For W12/A27-type readouts, assume some selection bias exists and measure it (reverse order and permute) on the target model before trusting a single ordering.
- **Evidence and grade:** several independent sources. Zheng et al. (ICLR 2024, PR, letter-ID probabilities, 20 models): moving the gold to position D lowered gpt-3.5-turbo from 67.2 to 60.9; moving it to A raised LLaMA-30B by 15.2; the authors attribute most of the bias to the ID token prior, with position effects smaller and irregular. Pezeshkpour and Hruschka (PP): best-versus-worst order gap 13.1 to 30% for GPT-4 and up to 75% for InstructGPT (adversarial upper bound, not a random-reorder effect). Wei et al. (PP): fluctuation rate higher on harder tasks. Gupta et al. (PP): all 10 models degrade under a second shuffle (the note flags that "drop" may be a stricter both-correct metric). Alzahrani et al. (PP).
- **Readouts:** matching for Zheng, Sanz-Guerrero; others generation or mixed. 2023-2024 base and chat models.
- **Exceptions:** "tens of points" figures are best-minus-worst or small-or-base-model effects. Typical random-reorder effects are a few points (Q3 note, synthesis 1). Not generalisable to modern instruction-tuned models by default.
- **Class:** established.
- **Lab match:** [Q3-1](lab-evidence.md#q3-option-order-and-format): reversal changed 1 (W12), 1 (K27), 3 (A27), 3 (D35), 6 (L27), 14 (G) and 21 (J) of 60. The trained letter-logit and pointer systems showed little order effect, which the notes judge compatible with the literature; J and G changing many has no published encoder counterpart.

### R3.2 Order effects shrink with model strength and are task-dependent; small diagnostics lose power
- **What to do:** Do not read a flat order diagnostic on a strong model as proof of no bias; do not read a large effect on a weak model as general. State the n and the accuracy ceiling when reporting.
- **Evidence and grade:** Wei et al. (PP): fluctuation higher on lower-accuracy tasks. Pezeshkpour and Hruschka (PP): sensitivity is larger when the model is uncertain among its top 2-3 options. The position-bias power study (2607.20864, PP, single author, small n, generation): bias is only statistically detectable for base accuracy of roughly 60-95%, and "no signal" is not proof of no bias.
- **Class:** plausible.
- **Lab match:** [Q3-2, R-4](lab-evidence.md#q3-option-order-and-format): n = 20 per class; W1 substantive is at ceiling for five of seven systems. Per-position recall (RStd) splits by gold position, which differs between orders, so it is not a bias measure on its own. K27 on W3 had RStd 0.25 in both orders and zero changed choices.

### R3.3 Permutation averaging reduces bias at a cost proportional to the number of permutations
- **What to do:** Where order or ID bias matters and cost allows, average the option probabilities over cyclic or random permutations; for pairwise judging, average both orders.
- **Evidence and grade:** Zheng et al.: full permutation costs about 4-5x for 4-5 options. Pezeshkpour and Hruschka (PP): majority vote over 10 random reorderings gave +2 to +8 points. Hanna and Feng 2026 (PP, single run per condition): cyclic permutation improved 5 of 6 model-benchmark pairs on each benchmark. Guda et al. (PP, 3B decoders, option-ID scoring): permutation majority vote raised accuracy, for example QASC 0.737 to 0.947 (Qwen2.5-3B), with only +0.01 on MedMCQA; the bias metric becomes 0 by construction; the KV-cache variant saves up to 84-89% of time. Wang et al. (PP, pairwise judges): both-order averaging plus multiple evidence +9.8 (GPT-4) and +14.3 (ChatGPT). Teacher-student distillation of permutation-averaged targets: RACE++ 61.2 to 68.1 (PP, label token probabilities).
- **Readouts:** matching for Zheng, Guda (option-ID scoring); partial or generation for others. Small and 2023-2025 models.
- **Exceptions:** accuracy gains are task-dependent (Guda: +0.01 on MedMCQA). The lab's strong systems already change 1-3 of 60 under reversal, so the headroom may be small.
- **Class:** established.
- **Lab match:** [Q3-7](lab-evidence.md#q3-option-order-and-format): no permutation averaging in the benchmark (cost x4-16), and the lab did not compare it with a single pass. The set5 D2 pair was used as a re-ask, not as a debiaser ([Q4-6, Q3-6](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag)).

### R3.4 PriDe-style prior estimation on a small subset is a cheaper alternative (one primary source)
- **What to do:** If permutation averaging is too costly, estimate the option-ID prior on a small subset of items by cyclic permutations and divide it out on the rest.
- **Evidence and grade:** Zheng et al. (PR, ICLR 2024): about 5% of samples, cost about 1.2x versus 4-5x; gains MMLU RStd -8.9 and +2.6 accuracy, ARC -7.3 and +2.9, CSQA -8.9 and +4.0 (5% budget); the prior transfers across domains with slight loss when the domain gap is large. Elsewhere PriDe was used mainly as a baseline (the Q3 note); PoE_ID (PP) uses it as the debiasing step and shows that without it elimination degrades under randomised labels. "My answer is C" companion (PP, abstract-level): PriDe-debiased first-token logits remained worse than text answers when mismatch exceeded 50% on chat models.
- **Class:** plausible (one primary source; used as a component elsewhere).
- **Lab match:** none (not run; the plan names PriDe as a possible stronger method for step 5).

### R3.5 Lower order sensitivity does not mean higher accuracy
- **What to do:** Evaluate a debiasing change on accuracy as well as on flip rate; never accept it on flips alone.
- **Evidence and grade:** Hanna and Feng 2026 (PP, single run per condition, no variance): GPT-4.1 mini MMLU flip rate 21.6 to 11.8 while accuracy 81.8 to 80.1; two-stage (generate then match) lowered accuracy in 11 of 12 pairs; independent per-option scoring lowered it in 8 of 11. Gupta et al. and Zheng et al. concur that flips grow with the number of permutations tried (upper bound, Q3 note synthesis 7).
- **Class:** plausible (one recent single-run source plus the metric argument).
- **Lab match:** [Q3-1, Q3-3](lab-evidence.md#q3-option-order-and-format): J flips 17-32% of top-1 under reordering; most flips swap between an action and `clarify`.

### R3.6 Do not apply calibrate-before-use blindly to instruction-tuned models
- **What to do:** If using content-free-input calibration, test it on the target model first.
- **Evidence and grade:** Zhao et al. (ICML 2021, PR, abstract only): contextual calibration gave up to +30.0 absolute accuracy on GPT-2/GPT-3 few-shot classification. Reif and Schwartz (PP, 10 LLMs, 279 tasks): contextual calibration "substantially worsens" label bias for instruction-tuned models; their leave-one-out calibration beat it. Label bias there is class-label prior, not option position.
- **Class:** plausible (negative result for tuned models; positive for older base models). No evidence for calibrating pointer or encoder scorers.
- **Lab match:** none.

### R3.7 The readout implementation changes the number; fix it and report it
- **What to do:** State exactly how the answer is read (letter probability, generated letter, answer-sequence likelihood, first token) and keep it constant across comparisons.
- **Evidence and grade:** Hugging Face MMLU write-up (P) with Alzahrani et al.: LLaMA-65B 0.637 (letter probabilities), 0.637 (generated text) and 0.488 (full answer-sequence likelihood); rankings change. Wang et al. ("My Answer is C", ACL Findings 2024, PR per listing; companion preprint): first-token argmax and text answer disagree on 10-51% of MMLU items for chat models (Llama2-7b 51.4%), and constraining the prompt lowers but does not remove it; text answers show lower selection bias than first-token logits, so part of the measured bias on chat models is a readout artifact. Sanz-Guerrero (R2.6) shows a tokenisation convention changes accuracy.
- **Class:** established.
- **Lab match:** [Q6-7](lab-evidence.md#q6-readout-dependence): two L27 records failed because output hit the token limit; 11 of 12 fenced replies in L27's JSON permutation prompt were scored invalid. These are output-format failures, a different effect, but the same lesson. The warning from Wang et al. may not apply to W12 and A27, which are trained for the letter slot (the Q6 note, A8).

### R3.8 For encoders and pointer scorers, order sensitivity is architecture-dependent and untested
- **What to do:** Measure it per system. A pointwise scorer that sees one option at a time is order-independent by construction; a joint scorer is not.
- **Evidence and grade:** Set-Encoder (PP): listwise rerankers (RankGPT-4o, RankZephyr, LiT5) are order-dependent; a cross-encoder with permutation-invariant position ids is invariant; pointwise monoELECTRA is order independent by construction and slightly lower in effectiveness (retrieval, not label choice). GLiClass (PP): attention to labels diminishes as the label count grows; it does not analyse label order, and a snippet claiming label-order influence could not be traced. Kev README (V): "changing option order can change an answer". Laya README (V, summary): per-slot logits show a position spread (+1.68 to -1.91 across five slots). No source on span-pointer order effects was found.
- **Class:** open.
- **Lab match:** [Q3-1, Q3-3, Q3-6](lab-evidence.md#q3-option-order-and-format): K27 chose the first-listed option in 116 of 240 requests (no position bias on the W3 pairs); J changes 21 of 60 and G 14 of 60. These are consistent with encoder joint scoring being order sensitive, but no external source tests that.

## Q4. Second passes

All second-pass experiments in the lab used K27 as base model (except the reference three-model vote), so no lab result tests a second pass on a letter-logit, encoder or generative scorer.

### R4.1 Do not expect a free-text second pass without outside information to help
- **What to do:** Do not add a self-reflection or "are you sure?" step to a generative decision model as a general improvement. If a re-ask is used, word it neutrally and measure it; give the second pass something new (a tool, a sound verifier, a fresh independent check).
- **Evidence and grade:** several independent sources. Huang et al. (ICLR 2024, PR): intrinsic self-correction lowered accuracy, for example GPT-3.5 CSQA (five-option multiple choice) 75.8 to 38.1 and GSM8K 75.9 to 74.7; oracle-stopped results look good but need labels. Kamoi et al. (PP survey): no reliable prompted self-correction in general tasks; it works with reliable external feedback. Stechly et al. (PP): GPT-4 self-critique lowered accuracy in three of four domains, and a sound verifier raised it; plain re-sampling kept most of the gain. Tsui (COLM 2026, PR): 64.5% blind spot, errors fixed when attributed to the user are missed when attributed to the model. Laban et al. (PP): models flip 46% of answers on "Are you sure?", mean accuracy drop 17 points. Zhou et al. (ICLR 2026, PR): verifier true-negative rate drops from 0.68 to 0.17 as the generator gets stronger. **Counter-evidence:** Liu et al. (PP): with a "fair" prompt at temperature 0, gains of 0.1 to 1 point on average (best cell +5.6 on Sports), while the Huang-style prompt lowers accuracy.
- **Readouts:** generation (partial or not matching). None tested letter-logit, pointer or encoder systems.
- **Class:** established for generative models; open for the lab's readouts.
- **Lab match:** [Q4-7, Q4-8](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag): F2 (re-ask naming the first choice, neutral wording "may be the same option or a different one") on K27 corrected 4 and broke 1 of 120 (net +3, untested arm). Narrowed passes moved at most 3 answers because K27's second-pass probabilities approximate the first pass renormalised (median absolute difference 0.001-0.015). The lab cause is the readout; the literature cause is the lack of new information. Both give a null, for different reasons.

### R4.2 Blind verification is better than verification shown the first answer
- **What to do:** If a verification step is added, ask a specific question about the input without showing the first answer, rather than asking whether the shown answer is right. Prefer open or specific questions to yes/no agreement questions.
- **Evidence and grade:** CoVe (Dhuliawala et al., PP): factored verification (verify without seeing the first answer) beat joint verification; open verification questions beat yes/no ones; the paper states, anecdotally, that the model "tends to agree with facts in a yes/no question format whether they are right or wrong". Tsui (R4.1): attribution to the model's own output weakens correction. Generative Llama 65B, list outputs; the evidence is partly anecdotal.
- **Class:** plausible (generative, partly anecdotal; supported in direction by the lab).
- **Lab match:** [Q4-2, Q4-3](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag): VB (blind) rescued 4, newly wrong 0 (exact p 0.125, Holm 0.50, inconclusive); VS (shown) answered "supported" on 14 of 17 false executions. Neither primary test was conclusive, and VB's gain came only from conflicting-evidence cases (check C2); on missing-evidence false executions nothing helped.

### R4.3 Same-family verifiers and voters share the generator's errors
- **What to do:** Do not treat a second model or a second call from the same family as independent evidence. Count effective independent votes, and use a verifier of a different kind (tool, rule, human) for the errors that matter.
- **Evidence and grade:** several sources. Kim et al. (ICML 2025, PR): when two models are both wrong they choose the same wrong option 42.3% (HuggingFace leaderboard; random 12.7%) and 60% (HELM; random 33%) of the time; higher for same developer and for more accurate models. Kohli (PP): a nine-judge panel carries about two independent votes' worth of information, and the best single judge matched or beat the panel on MNLI and SNLI. Panickssery et al. (PP) and Wataoka et al. (PP): self-preference, with the cause contested (self-recognition versus familiar low-perplexity text); Zheng et al. (MT-Bench, NeurIPS D&B) found the original signal inconclusive. Weaver (PP): gains from weak verifiers diminish because of "correlated biases on hard examples". Ding (PP): confident errors are partly shared across providers (48-63% agreement on majority answers).
- **Readouts:** generative judges and MCQ leaderboards (partial or not matching).
- **Class:** established for generative models and MCQ leaderboards; plausible for the lab's readouts.
- **Lab match:** [Q4-12, Q4-4](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag): K27, the blind terra annotator and the terra adjudicator applied the same lower-priority rule on 6 of 7 disputed cases; MV-u left 12 false executions that all three models share. Descriptive.

### R4.4 Voting over wordings gains little; voting over mixed-strength models can lose
- **What to do:** Do not use a vote over paraphrases as the main second pass. Vote over models only when members are of similar strength, and test the vote against the best single member.
- **Evidence and grade:** Wang et al. (self-consistency, ICLR 2023, PR, Table 7, LaMDA-137B): CoT 17.1, ensemble over 3 prompt sets 18.6, over 40 prompt-order permutations 19.2, self-consistency over sampled outputs 27.7; ensembling LaMDA with PaLM (36.9) is far below PaLM-540B alone (56.5). Arora et al. (AMA, PP): a majority vote over prompts has a "minor effect" (CB +2.2, RTE -2 against the average prompt); error-set Jaccard about 40-42% against 0.25 expected for independent prompts. Trad and Chehab (PP, one task, n = 1,000, no significance test): a five-model ensemble did not beat the best single model. Chen et al. (PP): voting can get worse with more calls because easy queries improve and hard queries get worse. Li et al. (TMLR 2024, PR): sampling-and-voting gains grow with ensemble size, larger on harder tasks and weaker models. **Conflicting:** Kamen and Kamen (company authors, PP): a ten-model panel reported "up to 65% F1" over the best single model, with design and significance not verified and no control for error correlation.
- **Readouts:** generation, option scoring in T0-3B (AMA, partial).
- **Class:** plausible (single-readout agreement across several sources; one conflicting company report).
- **Lab match:** [Q1-5, Q4-1, Q4-4](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag): the three wordings agreed on 107 of 120 W3 cases; WV 18 false executions vs B 17; MV 20 vs B 17 (W12 alone made 25). WV vs B test inconclusive (Holm 1.00). Direction agrees with the literature.

### R4.5 If a second pass is used, weight it by estimated accuracy or let an independent signal enter
- **What to do:** Prefer a verifier or ensemble whose members are weighted by their measured accuracy on a labelled sample; for external checks (tools, rules) give the second pass something the first pass did not have.
- **Evidence and grade:** Weaver (Saad-Falcon et al., PP, Llama 3.3 70B generator, K = 100): majority vote 72.2%, naive ensemble of top reward models 69.1%, self-verification 66.9% (below the first sample at 68.4%), weighted ensemble 87.7% (+15.5 over majority vote); learned weights drop by 20.1% on average with only 0.01n labelled samples; a distilled 400M cross-encoder kept 98.7% of the gains. AMA (PP): weak supervision beat majority vote by up to 8.7 points. CRITIC (ICLR 2024, PR): critique without tools was about as good as CoT or self-consistency (AmbigNQ EM CoT 51.8, CRITIC without tool 55.2, with tool 62.0). Large Language Monkeys (PP): without an automatic verifier, majority voting and reward models plateau.
- **Readouts:** generation; the Weaver distilled verifier is a cross-encoder scoring long responses (partial), not an option scorer.
- **Class:** plausible.
- **Lab match:** [Q4-4](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag): the lab's three-model vote is the unweighted configuration.

### R4.6 Narrowing the options and re-asking helps letter-logit readers with many options
- **What to do:** For a letter-logit reader with many options (7-10), consider eliminating low-probability options and re-asking, using a debiased option prior. Do not use it for a scorer that already scores each option independently.
- **Evidence and grade:** Zhu et al. PoE_ID (PP, code link, six open LLMs 9B-32B, option-ID probabilities; matching for W12/A27): +0.8 (Timedial, 3 options), +2.1 (Abstract_Narrative, 10), +2.6 (MMLU-Pro, 10) and +6.3 (Arithmetic, 7) over a debiased baseline (average of six models); gains larger with more options; without the debiasing step elimination degrades under randomised labels; asking the model to name the incorrect option was much worse (Gemma-3-12B Arithmetic 64.4 vs 46.5 and 30.9). Ma and Du POE (EMNLP 2023, PR per listing; FLAN-T5-XL 3B, option log-likelihood): elimination beat multiple-choice prompting on 5 of 8 tasks and lost slightly on 3; across a further 8 tasks it gained on four logical tasks (+6.8 to +18.8) and lost on four commonsense and social tasks (-2.3 to -6.2); few-shot results mixed.
- **Exceptions:** if the correct option is eliminated, the later step cannot recover (PoE_ID). Task-dependent in both signs (POE).
- **Class:** plausible (one matching source; one partial source with mixed sign).
- **Lab match:** [Q4-6 to Q4-8](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag): D2, Dex, T3 on K27 (4-option-ish W3 sets) moved at most 3 answers; the lab explains it by K27's pointer scoring, where dropping options leaves the remaining scores almost unchanged. The null on K27 does not say anything about W12 and A27, where the literature reports gains (Q4 note, D2 relevance).

### R4.7 Top-k re-ranking helps only on samples where the first stage is uncertain
- **What to do:** Gate a stronger second stage to the low-confidence samples; do not send every sample.
- **Evidence and grade:** Ma et al. (PP, filter-then-rerank; fine-tuned small-model first stage, top-3 labels plus "None", generative LLM reader): reranking improved hard samples (GPT-4 F1 change on the reranked subset +8.8, +17.7, +26.8) and degraded easy ones; average +2.4 F1 with InstructGPT; sending all samples to the LLM gave 12.5, 59.9 and 5.4 F1 on the three datasets; cost down 80-90%. Out-of-scope work (summaries): a DistilBERT classifier routing uncertain utterances to a fine-tuned Llama 3.1-8B (F1 0.853 BookData, not checked at full text).
- **Exceptions:** the gain needs the first stage to be uncertain on its errors.
- **Class:** plausible.
- **Lab match:** [Q4-10](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag): K27's missing-evidence errors are high-confidence, the regime where this design would not trigger; every changed answer in the gated variants already had first-pass probability below 0.9.

### R4.8 Order disagreement as an error flag is unsettled
- **What to do:** Treat "answers differ between an order and its reverse" as a cheap inconsistency signal, but do not rely on it as a measured error detector until it is tested on the target readout.
- **Evidence and grade:** indirect only. Pezeshkpour and Hruschka (PP): sensitivity is larger when the model is uncertain among its top 2-3 options (correlational, 2023 API models). Wang et al. (PP, pairwise judges): the entropy of the both-order outcome flagged cases for human review (ChatGPT with 20% human cost reached 71.3% accuracy). ProSA (PP): instance-level inconsistency between prompts. Guda et al. (PP): label-free permutation bias metric highest on the hardest dataset, but it does not report error detection. Hanna and Feng warn that fewer flips need not mean higher accuracy (R3.5). Ding (PP): agreement signals are weak and regime-dependent, and partly positional. No source tests order disagreement as an error detector on a 3-4 option pointer or letter-logit classifier with precision and recall.
- **Class:** open (no matching source; supported only by indirect evidence).
- **Lab match:** [Q4-9](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag): the flag fired on 6 of 120 fresh W3 cases, 5 were B errors (random expectation 1.20; descriptive, uncorrected, post-hoc); recall 5 of 24 errors. It has no published comparator in the notes.

### R4.9 Confidence gates catch low-confidence errors only
- **What to do:** Do not use a confidence threshold to catch errors that the model makes with high confidence (for example an unstated decisive fact with a plausible default).
- **Evidence and grade:** Xiong et al. (ICLR 2024, PR): verbalised confidence is overconfident and no method wins everywhere. Taubenfeld et al. (PP): within-question ranking of confidence matters more than overall calibration. Ding (PP): gpt-4.1 had consistency 0.89 yet majority accuracy 0.48 on GPQA. Ma et al. (R4.7): reranking helps where the first stage is uncertain. Plaut et al. (TMLR, PR; letter-logit): the probability threshold does help for letter-logit readers on average (see R5.6).
- **Class:** plausible (generative sources; the lab observation is on K27).
- **Lab match:** [Q4-10, Q5-5](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag): margin gates cannot fix K27 and D35 high-confidence missing-fact errors (K27 0.99 on one T5 case); dev-frozen gates still gave K27 0% risk at 92% coverage on the fresh core.

## Q5. Abstention, "none of the above" and missing information

### R5.1 Include fallback options; a closed list with none pushes the model to pick an answer
- **What to do:** Where the input may not fit any option, include explicit fallback options (out of scope, no match, need more information, defer) rather than relying on the model to refuse.
- **Evidence and grade:** several sources. Goral et al. (PP, 'Wait, that's not an option'): when the correct answer was not offered and no NOTA option existed, aligned models often picked an invalid option; GPT-4o reflective-judgment score 0.9 / 0.0 / 0.0 (Easy / Standard / Hard), while Llama 3.1-405B scored 100 / 42.5 / 91.5 (generation, arithmetic, two options). Madhusudhan et al. (COLING 2025, PR; generative, explicit IDK/NOTA option): unanswerable accuracy was low without an abstain clause (GPT-3.5 Turbo 0.6 on CQA). Jev docs, Tev1 and Decider advise an `other`/NOTA option (V). Vendor prompt guides (Anthropic hallucination guide, OpenAI structured outputs) advise allowing "I don't know" or handling invalid input (G, generative, summaries).
- **Class:** established for generative models. For the lab's readouts the supporting evidence is the lab's own: encoders J and G without a gate choose an answer on every missing-evidence case.
- **Lab match:** [Q5-1, Q5-8](lab-evidence.md#q5-abstention-none-of-the-above-and-missing-information-detection): J and G selected the fallback on 0/14 W2 missing-evidence cases (both chose a non-fallback answer on all 14); J falsely rejects 18/24 substantive T3 cases (the opposite error, fallback attraction).

### R5.2 A "none of the above" answer costs accuracy; size depends on model and phrasing
- **What to do:** Expect lower accuracy on items whose correct answer is the NOTA option than on items with a listed answer; measure the NOTA-correct slice separately and test the NOTA wording.
- **Evidence and grade:** Kadavath et al. (PP, Anthropic; letter probabilities on pretrained LMs up to 52B): replacing the final option with NOTA reduced accuracy and calibration significantly (figure only). Tam et al. 2025 (PP; 28 LLMs, 0-shot CoT generation, MMLU 14,042 questions): NA as the correct answer causes a 30-50% performance drop regardless of scale (DeepSeek-V3 65.7% vs 90.8%); NA as a distractor leaves accuracy near baseline; the wording spread in Table 3 for LLaMA-8B is 2.4x ("Answer not found" 0.134 vs "None options are correct" 0.256). A 2024 preprint (abstract only) reports drops when NOTA substitutes for the correct answer.
- **Exceptions:** a replacement can make some questions ambiguous (Kadavath). Domain dependence: mathematics 14.6% drop, business ethics 48.1% (Tam).
- **Class:** established (several groups, one letter-readout source).
- **Lab match:** [Q5-1](lab-evidence.md#q5-abstention-none-of-the-above-and-missing-information-detection): K27, A27, W12, L27 and D35 are near ceiling on W1 fallback cases (E-fb 23-24 of 24), but W3 fallback accuracy is 9-16 of 24, with W12, K27, A27 and L27 all missing missing-decisive cases 3/8.

### R5.3 An abstain clause raises abstention and costs coverage; size is model-specific
- **What to do:** Do not add an abstain instruction without measuring both sides: abstention on unanswerable items and accuracy on answerable ones, per model. A scenario list in the system prompt is the better-supported form for chat models.
- **Evidence and grade:** Madhusudhan et al. (COLING 2025, PR): on CQA, GPT-4 Turbo unanswerable accuracy 32.8 (standard), 50.8 (abstain clause), 62.2 (extreme clause) with answerable accuracy 48.0, 42.6, 38.4; the extreme clause helped larger models and not smaller ones (Mistral 7b UAC 3.5, 35.5, 45.1 with AAC 25.7, 20, 15.5); GPT-3.5 Turbo UAC only 0.6 to 10.2. Tam et al. Table 4 (PP): fine-tuning LLaMA-3-8B for NOTA raised NA-correct accuracy 28.5% to 49.5% (SFT) / 57.7% (DPO) but NA-distractor accuracy fell 64.1% to 55.0% / 54.7%. Goral et al.: the same one-sentence warning gives 0% to about 100% across models, and paraphrases changed GPT-4o-mini from 0.07% to 14.89% (Table 4). AbstentionBench (PP, 20 LLMs, free generation): a system prompt listing abstention scenarios raised abstention without a significant precision loss, but the authors say it is unlikely to fix the lack of reasoning about uncertainty.
- **Readouts:** generation (not matching). No external study isolates an abstain clause on a logit-readout model.
- **Class:** established for generative models; open for the lab's readouts.
- **Lab match:** [Q5-10, Q5-11, Q1-12](lab-evidence.md#q5-abstention-none-of-the-above-and-missing-information-detection): the lab's decisiveness clause became mandatory after a second annotator found v1 open-world wording ambiguous (annotator agreement, not a model result); terse wording and K27 over-rejection point in different directions; the D35 card warning on abstention wording was not tested.

### R5.4 The wording of the abstain option matters, and a bare added option may trigger abstention
- **What to do:** Test two or three phrasings of the NOTA or "unknown" option. Control for the effect of adding any extra option.
- **Evidence and grade:** Tam et al. (PP): wording spread described above. "LLM Abstention Can Be a Prompt Artifact" (PP, v9, single group, summary only): adding an "Unknown" option to a true/false task dropped accuracy by 19.8 points on average with 34.5% abstention (MCQ: 1.2 points); replacing "Unknown" by an unrelated word ("Triangular", "Cerulean") gave similar abstention (about 30%), so the extra option itself, not its meaning, triggered abstention; larger models (26B+) showed less inflation. MedAbstain (Machcha et al., PP, logprob readout, MedQA): adding the abstention option moved abstention far more than removing context did.
- **Readouts:** generation (not matching); MedAbstain is logprob over option tokens (partial to matching), preprint.
- **Class:** plausible (two or three sources, preprints, mutual tension: wording matters in Tam, meaning does not in the artifact paper).
- **Lab match:** [Q5-11](lab-evidence.md#q5-abstention-none-of-the-above-and-missing-information-detection): not tested. The artifact paper's claim conflicts with the assumption that the wording of the abstain label is the lever, and it is a hypothesis to test on the lab's readouts.

### R5.5 Missing-information detection is the weak case; do not rely on the model to notice
- **What to do:** Do not rely on an instruction or an option to catch a decisive fact that is simply absent. Make missing fields explicit in the input (R5.8) and add a rule or schema check where facts are structured.
- **Evidence and grade:** several sources. QuestBench (PP; generation): when asked to answer or say "not sure", models said "not sure" on 0.7-4.6% of Planning-Q cases where 41.8% were underspecified; F1 for "not sure" at most 5 points above a random baseline. MedAbstain (PP; logprob readout over options): model abstention precision 71.43% and recall 13.16% on items where key information had been removed. AbstentionBench (PP): underspecified-context is the weakest scenario and reasoning fine-tuning lowers abstention by 24% on average. MiP-Overthinking (PP): reasoning models do not abstain more on missing premises and produce 2-4x more tokens. UA-Bench (2026, abstract only): even strong models struggle to separate "under-specified" from "beyond my capability".
- **Class:** established for generative models; partial evidence for option-logprob LMs (MedAbstain); open for pointer and encoder scorers.
- **Lab match:** [Q5-2 to Q5-6](lab-evidence.md#q5-abstention-none-of-the-above-and-missing-information-detection): missing evidence /47: A27 43, W12 40, L27 38, K27 36, D35 27, J 23, G 21; K27 false executions 17 of 60 (11 missing evidence); no tested second pass reached the missing-fact failure; a blind check of whether a decisive fact is unknown said yes on 0 of 17 false executions. Agreement with the literature in direction (assume a default and decide), descriptive on authored cases.

### R5.6 Thresholding the maximum letter probability is a supported abstention route for letter-logit readers
- **What to do:** For a letter-logit reader, set a threshold on the maximum option probability (or max logit) using a small labelled sample, and route below-threshold items to review. Check the high-confidence error slice separately.
- **Evidence and grade:** Plaut et al. (TMLR 2025, PR; 15 chat LLMs plus base, 21,407 questions, letter-token probabilities; matching): probabilities are miscalibrated but predict correctness (AUROC), and in an abstention game thresholding gave substantial gains with about 20 labelled questions per dataset to pick the threshold; base models are better calibrated than chat models. Kadavath et al. (PP): large models are well calibrated on lettered multiple choice, and RLHF miscalibration is fixed by a temperature change (Fig. 9). Tomani et al. (PP, abstract only): abstaining on a few highly uncertain samples improved correctness by 2-8%. Jev docs (V): thresholds 0.3-0.5 for review and confidence tiers; Navya (P): never gate on raw confidence; ECE per type noul 0.012, choice 0.086, score 0.254 (one easy task). Hua et al. (workshop paper, text-davinci-003): averaging letter probabilities over paraphrases with temperature scaling cut ECE by over 70% with accuracy about unchanged.
- **Exceptions:** does not address the missing-fact failure with high confidence (R4.9). Not tested on pointer heads or encoders.
- **Class:** established for letter-logit LMs; open for trained decision models and K27.
- **Lab match:** [Q5-5, Q4-10](lab-evidence.md#q5-abstention-none-of-the-above-and-missing-information-detection): dev-frozen gate K27 0% risk at 92% coverage, A27 0% at 85%, W12 3.7% at 90% (descriptive); A27 best calibrated on fallbacks (Brier 0.09).

### R5.7 For encoder and span scorers, abstention depends strongly on training (and can be added post hoc)
- **What to do:** Do not expect prompt wording alone to give an encoder or span scorer an abstention ability it was not trained for; training with negatives or none-pairs can materially change it (GLiNER negative sampling, below). If absent, add a post-hoc gate (confidence threshold or selective-prediction reject option calibrated on held-out data; classic references such as Geifman & El-Yaniv, NeurIPS 2017, and Conformal Risk Control, ICLR 2024, are NOT in the evidence notes and were added by terra review, unverified here) or a separate model, and evaluate on a risk-coverage curve.
- **Evidence and grade:** GLiNER (PP, span scoring, closest published readout to K27): negative entity-type sampling during training: 0% negatives P 49.3 / R 58.1 / F1 53.3; 50% negatives 62.3 / 59.7 / 60.9; 75% negatives 61.1 / 56.5 / 58.6, so more negatives make the model more cautious. Ma et al. 2021 (ACL-IJCNLP short, PR): in entailment-based zero-shot classification, emotion and situation tasks with a "none" label stayed at 12-25 F1 for all systems (BERT-base, dated). 2608.20371 (PP, summary): fine-tuned RoBERTa OOS recall 58.1 vs Claude haiku 85.6 on CLINC150 (generation for Claude). Kev README (V): training with "none pairs" and "abstention twins", unknowable records answered at 0.9+ confidence 0% (Kev-9B) vs 9% (Jev) in the author's suite.
- **Class:** plausible (one controlled source on span scorers; author statements for Kev).
- **Lab match:** [Q5-1, Q5-8, Q6-6](lab-evidence.md#q5-abstention-none-of-the-above-and-missing-information-detection): J and G are near zero on W2 missing evidence and choose an answer on every missing-evidence case; K27 was 36/47. These agree in direction with the training-time reading. The lab did not run a training-time experiment, and the Kev suite and the lab's W3 cases are different tests (not a replication or contradiction of a number).

### R5.8 Mark missing values explicitly in the input
- **What to do:** Where records have fields, write absent facts as an explicit `unknown`, blank or `null` rather than omitting the field.
- **Evidence and grade:** the lab result and the Kev "unknowable records" design ([Q6 note](evidence/q6-readout-and-vendor.md), C5, V). The Jev docs say to give full instructions and structured instructions (V). The external notes contain no controlled study of explicit-marker effects.
- **Class:** plausible (lab result plus author statements).
- **Lab match:** [Q5-4](lab-evidence.md#q5-abstention-none-of-the-above-and-missing-information-detection): explicit `unknown`, blank, `null` and absent fields were handled well (b4-rec fallbacks: A27, W12, L27 8/8; K27 7/8; D35 5/8), while an unstated workaround became "no workaround" (0/2 each). Descriptive, authored cases.

## Q6. Readout dependence

### R6.1 Do not carry a chat-LLM prompting result to a scorer without a test
- **What to do:** For every published prompting trick, check which readout it was shown on. For W12 and A27 (letter logits), K27 (pointer), J and G (encoders), run a small test on the target system before adopting it. The following findings need generated text and are not known to hold for one-pass readouts.

| Finding | Evidence | Why generative-only |
|---|---|---|
| Chain-of-thought raises abstention | Madhusudhan (UAC roughly doubles on MMLU for GPT-4 Turbo), Goral (more than 85 points) | needs generated reasoning; MedAbstain (logprob readout) found negligible CoT gain |
| More reasoning budget does not help abstention | AbstentionBench Fig. 7, MiP-Overthinking | long generation |
| Verbalised confidence | Xiong (overconfident), Madhusudhan (not consistently better than base) | needs generated numbers |
| Abstain-scenario system prompt | AbstentionBench Sec. 4.4 | tested on chat and reasoning generators only |
| Emotional "extreme abstain" pressure | Madhusudhan (helps GPT-4 Turbo, hurts small models) | instruction following by chat models |
| Self-correction, self-consistency over samples | Huang, Kamoi, Wang et al. | needs a stochastic or reflecting generator |
| Prompt repetition improves non-reasoning LLMs | Leviathan et al. (Google, PP, no code; 47 of 70 wins, 0 losses, McNemar p < 0.1) | generation; no letter-logit measurement, a pointer head already conditions on the whole instruction |

- **Evidence and grade:** these rows are from [Q6 note](evidence/q6-readout-and-vendor.md), section B, [Q4 note](evidence/q4-second-passes.md), and [Q5 note](evidence/q5-abstention.md). The first-token versus text mismatch of chat models (Wang et al., R3.7) is the direct evidence that readouts differ.
- **Class:** established that the readouts differ; whether each finding transfers is open.
- **Lab match:** [Q6-1, Q6-2](lab-evidence.md#q6-readout-dependence): the lab sees wording and order sensitivity differ by readout (encoders J and G change many choices; letter-logit and pointer systems change few), and K27's second pass is the first pass renormalised. These are between-system contrasts, not controlled readout experiments.

### R6.2 Encoders: label wording and hypothesis templates matter; label-in-input encoders are untested
- **What to do:** For J and G, treat label wording and descriptions as tuned parameters and test them. Write labels in English if the model is English-only. Use fixed templates and report the spread.
- **Evidence and grade:** NLI cross-encoders (partial for J and G): template or verb changes changed F1 by about +/-20 (Ghilene et al., workshop-level, best template chosen on evaluation data); English prompts beat target-language prompts on all Universal Joy languages (average macro-F1 difference 0.025; Bareiß et al., WWW'24 Companion, PR); Ma et al. 2021: huge dataset variance and shallow lexical reliance. BTZSC (ICLR 2026, PR): Qwen3-Reranker-8B macro F1 0.72, best letter-readout LLM 0.67, NLI cross-encoders 0.60 best; it used one fixed verbaliser per dataset, so it gives no wording evidence. GLiClass and GLiNER2 papers (PP): no label-description ablation found by full-text search; GLiNER2.5-Decide card: pass a description when the label name is not enough (V). Laurer et al.: documentation says to test different hypothesis templates, with no numbers.
- **Exceptions:** the older NLI work uses pair classifiers (BERT-base), not uni-encoder label-token models like J and G.
- **Class:** open for J and G; plausible for the general statement that label wording matters to NLI-style encoders.
- **Lab match:** [Q6-1, Q6-5, Q6-6, R-5](lab-evidence.md#q6-readout-dependence): J and G change many choices under rewording and reordering; J on the game task with Japanese options 5/18 vs English options 13/18. J is "substantially behind" on JevBench hard tiers per its README (V). Descriptive. The lab's Japanese observation agrees in direction with the English-prompt result for NLI cross-encoders, but the models differ.

## Practices to avoid (when there is evidence against)

| Practice | Evidence against | Scope | Lab match |
|---|---|---|---|
| Judging a wording, format or model on a single prompt | Sclar, Mizrahi (rankings reverse; 15 of 25 tasks negatively correlated) | established | [Q1-1](lab-evidence.md#q1-instruction-wording-structure-and-length) |
| An intrinsic "find the problem with your answer" second pass for a generative model, without outside information | Huang (CSQA 75.8 to 38.1), Liu (the "problem/incorrect" prompt lowers accuracy), Laban (46% flips), Tsui | established for generative models | none on the lab's readouts |
| Shown-answer yes/no verification as the only check | CoVe (yes/no agreement bias, anecdotal); lab: VS said "supported" on 14 of 17 false executions | plausible | [Q4-3](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag) |
| A same-family verifier or a same-style annotator as the only control | Kim (42-60% shared wrong choices), Kohli, Panickssery/Wataoka (contested), lab Q4-12 | established for generative models | [Q4-12](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag) |
| A free-form vote over wordings as the main second pass | Wang (Table 7), Arora; lab WV | plausible | [Q4-1](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag) |
| An unweighted vote over models of different strength | Wang (Table 10), Trad and Chehab, Weaver (naive ensemble 69.1 vs first sample 68.4) | plausible | [Q4-4](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag) |
| A wording that raises abstention without measuring the coverage cost | Madhusudhan (answerable accuracy 48.0 to 38.4), Tam (NA-distractor 64.1 to 54.7) | established for generative models | [Q5-10](lab-evidence.md#q5-abstention-none-of-the-above-and-missing-information-detection) |
| Relying on an abstain sentence alone when the model is small or untested | Goral (0% to about 100% for the same sentence), Madhusudhan (small models do not follow the extreme clause) | established for generative models | none |
| Using a confidence gate to catch high-confidence errors | Ding (confidence 0.89, accuracy 0.48); lab: K27 0.99 on a missing-fact error | plausible | [Q4-10](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag) |
| Applying contextual calibration to an instruction-tuned model without a test | Reif and Schwartz ("substantially worsens") | plausible | none |
| Adding an "are you sure" or reflection pass to a non-generating scorer, expecting a new answer | lab: K27 second-pass probabilities equal the first pass renormalised; no external source tests it | lab only | [Q4-8](lab-evidence.md#q4-second-passes-verification-voting-narrowed-re-ask-order-disagreement-flag) |
| Parsing generated output without verifying format (L27) | no external source in the evidence notes; lab: 64-token cutoff and fenced JSON scored invalid | lab only | [Q6-7](lab-evidence.md#q6-readout-dependence) |
| Treating lower flip rate as a gain | Hanna and Feng (flip 21.6 to 11.8, accuracy 81.8 to 80.1) | plausible | [Q3-3](lab-evidence.md#q3-option-order-and-format) |
| Reading "no position bias" from a small, near-ceiling diagnostic | 2607.20864 (power), lab R-4 | plausible | [Q3-2](lab-evidence.md#q3-option-order-and-format) |
| Compressing a short classification instruction to save tokens | no evidence either way for short classification instructions; compression papers lose quality in short contexts (Zhang 2025) | open | [Q1-1](lab-evidence.md#q1-instruction-wording-structure-and-length) |

## Templates (derived from cited sources, not lab-tested)

Each template is a design pattern assembled from the cited sources. None has been tested in the lab, and none is validated for W12, A27, K27, J or G. Test before use.

**Template 1: option with `what` / `not_for` fields for confusable options** (derived from Jev documentation, V, summary; no measurement).
```
option: <short key>
description:
  what: <what this option is for, in concrete terms>
  not_for: <the neighbouring option and the cases that belong there instead>
  examples: <one or two>
```
Supported by: [Q1/Q2 note](evidence/q1-q2-instruction-and-options.md), "Vendor guidance for Jev-type interfaces"; direction supported by R1.3 evidence (generative).

**Template 2: fallback option written as a bucket** (derived from the Decider README, V, and Jev docs; no measurement).
```
other: <what it catches, for example "any request that none of the options above covers", not the bare word "other">
need_info: <a decisive fact required by the rules is not stated in the input>
```
Supported by: [Q6 note](evidence/q6-readout-and-vendor.md), C1 and C6; R2.7 and R5.1.

**Template 3: abstain-scenario instruction for a generative chat model** (derived from AbstentionBench Sec. 4.4, PP, generative only).
```
If the input does not contain a fact that the rules depend on, or two records conflict and no rule says which prevails,
or the request does not match any option, choose the fallback option that names that case. Do not assume a default value.
```
This wording is ours, assembled from the scenario-list idea in AbstentionBench and the "do not assume" failure in QuestBench and the lab; the sources do not give this text. Only the principle (list the abstention scenarios) has external support, and not for the lab's readouts. The lab's v1 wording had no decisiveness clause and annotators disagreed, which is why a decisiveness clause became mandatory ([Q1-12](lab-evidence.md#q1-instruction-wording-structure-and-length)). Test coverage cost per R5.3.

**Template 4: sensitivity report** (derived from Mizrahi, Sclar, PromptEval, ProSA).
```
For each candidate wording or format: run k plausible variants (k >= 10 where the budget allows) on the same cases;
report max, mean, median and a quantile of accuracy, the count of items whose answer changes across variants,
and the number of items; compare systems on the same variants, not on one prompt.
```
**Template 5: letter-logit gate** (derived from Plaut et al., PR).
```
Read the maximum probability over the offered letters. Pick the threshold on about 20 labelled items per task or dataset (the source's figure),
check coverage and risk on a held-out sample, and review the high-confidence errors separately.
```
**Template 6: order protocol for letter-logit readers** (derived from Zheng et al. and Guda et al.).
```
Measure the answer under the original and reversed order and, if cost allows, cyclic permutations.
If flips are material, average option probabilities over the permutations (cost multiplies by the number of permutations),
or estimate the ID prior on about 5% of items and divide it out (PriDe).
```
No templates are given for terse wording, data-boundary sentences, narrowed re-ask, order-disagreement flags or encoder label wording, because the evidence does not support one (R1.4, R1.6, R4.6, R4.8, R6.2).

## Where the evidence is missing

- No controlled external study on pointer-head scorers (K27) or on trained decision models (W12, A27) for wording, order or abstention ([Q6 note](evidence/q6-readout-and-vendor.md), "Gaps for Q6").
- No source isolates terse versus full instruction, irrelevant context, or an abstain clause on option-logit, pointer or encoder readouts.
- No external test of order disagreement as an error detector, and no second-pass study on pointer or encoder scorers ([Q4 note](evidence/q4-second-passes.md), "Gaps for Q4").
- No label-description ablation for GLiNER2 or GLiClass; no controlled study of option count from 2 to about 50 for logit-readout scorers.
- Evidence is English and mostly 2022-2025 base or chat models up to 70B, and no source is in Japanese. Several 2026 preprints had no peer review at the time of access, and the notes mark the ones read at abstract or summary level only.
- The lab cases were all written by one agent family and labels were checked by blind agents, not humans. Many lab tests are descriptive or inconclusive (primary tests with 2-4 discordant pairs); "inconclusive" is not "no effect".
