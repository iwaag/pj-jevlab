# Out-of-scope / out-of-domain intent detection with and without LLMs (L2, L3, Q1, Q3, Q4, Q5)

- **Sources:** https://arxiv.org/abs/1909.02027 (Larson et al., EMNLP-IJCNLP 2019, CLINC150, abstract); https://arxiv.org/abs/2402.17256 (Wang et al., LREC-COLING 2024, "Beyond the Known", findings/experiments); https://arxiv.org/abs/2410.01627 (Arora et al., "Intent Detection in the Age of LLMs", results); https://arxiv.org/abs/2608.20371 (decision framework, search-hit only, not read beyond a snippet: treat as lead) (accessed 2026-10-02; via WebFetch summaries)
- **Evidence type:** peer-reviewed/preprint paper; author independence: yes (Arora et al. are from Amazon using Claude and Mistral)
- **Model / base / checkpoint:** Wang: gpt-3.5-turbo, GPT-4, text-davinci-002/003, Claude, Llama2-70B-Chat; Arora: Claude v1 Instant, v2, v3 Haiku, v3 Sonnet, Mistral 7B, Mixtral 8x7B, Mistral Large vs SetFit (MPNet); **size:** as named (verified from fetched text; closed models unknown); **training:** instruction-tuned
- **Task:** intent classification with an out-of-scope (OOS/OOD) class on CLINC150 and Banking77 (Wang), HINT3 and internal AID3 (Arora); **language:** English; **rejection mechanism:** OOS as a binary label or an explicit class
- **Data provenance:** public intent datasets; **metrics:** accuracy, F1, OOS recall; **configuration:** zero-shot and few-shot ICL; **raw cases available:** no
- **Fixed / mitigated?** Arora: hybrid SetFit-to-LLM routing within 2% of LLM accuracy at about 50% lower latency; **fix evaluated?** yes
- **Relevant local classes:** L2, L3, Q1, Q3, Q4, Q5

## What the source reports
- Larson et al.: classifiers with strong in-scope accuracy "struggle to identify" OOS queries (CLINC150, 150 intents, 10 domains). Establishes OOS as a known hard failure of intent classifiers since 2019.
- Wang et al.: LLMs are strong zero-/few-shot OOD detectors but underperform fully fine-tuned discriminative models; zero-shot ChatGPT trails the fine-tuned UniNL baseline (13.36 points on Banking IND accuracy at 50% intent split); long prompts with many intents degrade results and cause output failures (about 8.5% on large-scale tests).
- Arora et al.: LLM OOS detection depends on how broad the intent labels are and how many labels there are; average F1 0.736 (Claude 3 Haiku), 0.735 (Mistral Large), 0.658 (SetFit with negative augmentation).
- Arora et al. report that a trained small SetFit model was competitive when given negative augmentation, i.e. training data for the none class matters as much as model size.

## Strength and caveats
- Independent, peer-reviewed evidence that OOS rejection is a general weakness, that LLMs do it better than naive classifiers, and that trained small models can compete when trained with OOS data (relevant to Q3). Not a size sweep within one family, so Q1 stays unanswered by these papers.
- Task shape differs: full-sentence customer intents with trained/ICL none class, not 2-6 verb-described options with an in-list `clarify`.
- Numbers come from WebFetch summaries; row-level tables not checked.
