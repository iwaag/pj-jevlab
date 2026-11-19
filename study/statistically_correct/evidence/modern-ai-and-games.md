# Evidence cards: modern AI / multi-agent systems (area G) and games / interactive simulation (area H)

Searcher: areas G and H of Step 2 in [plan.md](../../../devdocs/episodes/study/statistically_correct/plan.md). Search date and cutoff: 2026-10-06 (AI literature searched up to this date; the newest source used here is dated May 2026). Access date for every source below: 2026-10-06. Companion file: [search-log.md](../search-log.md).

Reading convention. "Source:" marks a claim made by the cited paper. "Lab:" marks an observation from this repository's own reports (taken from [framing.md](../framing.md), not re-run). "Inference:" marks my own reasoning, which is not evidence. "Read" states how a source was opened: full PDF text via pdftotext (verified at source), HTML text via curl, or fetch-summary only.

## 0. Top-level reading of the evidence (positive and negative/qualifying)

Positive results that were verified at source

- Aggregating several heterogeneous models can beat single models on factual or binary tasks and can approximate a human crowd (M-02 PoLL judge panel; M-03 majority voting over five samples; M-04 twelve-LLM forecasting ensemble). The measured gains are modest and are conditional on how much the errors differ across members.
- Interactive populations of LLM agents show information diffusion and coordination without scripting (M-09, 25 agents), and can reproduce some aggregate social curves with roughly 30% normalised error (M-10).
- Imperfection that is designed as pacing or as a state-dependent policy is used successfully in shipped or evaluated game systems (M-13 mistake-prone bots are judged by their navigation faults; M-14 Maia models human mistakes by conditioning on state; M-19 the Left 4 Dead director varies frequency, not amplitude). Only M-14 is evaluated quantitatively; M-19 is an anecdote.

Negative or qualifying results that were verified at source

- Errors of different LLMs are correlated (M-01): about 60% agreement when two models are both wrong on one leaderboard (a random choice among wrong options would give 1/3), and more accurate models are more correlated. Using "different models" is not a guarantee of independence.
- Debate between identical agents does not add expected correctness beyond voting in the paper's model and experiments (M-03). Whether voting itself helps depends on the independence of the votes, which is the thing M-01 questions.
- Synthetic populations are homogenised. LLM answers are flatter than human subgroup answers (M-06), a heavily aligned model can place more than 0.99 probability on one option (M-07), and raising temperature to restore diversity either fails to reach human semantic diversity or produces incoherent text (M-06), or lowers human alignment (M-08). The positive "silicon sample" result (M-05) is conditioned on real individual backstories, so real data supplies the heterogeneity.
- Collective outcomes of LLM agent societies can be fragile: wording of a persona changed cooperation by up to 76 percentage points in one model and 1 point in another (M-11); agents herd more than humans after a dislike (M-10).
- Mistakes read as incoherence or non-humanness, not as fun, when they are of the wrong kind: bots that get stuck or move jerkily are identified as bots (M-13, M-15). Weakening a strong engine by limiting depth does not reproduce human errors (M-14). Hidden correction of randomness was used by a major tactical game because displayed odds felt unfair (M-18, anecdote).
- Player-study evidence on "deliberate mistakes improve fun" is thin: the one controlled study found is a ten-participant unreviewed Master's thesis with small, mostly null differences (M-17). Absence of stronger studies in this search is not evidence of absence (see search log).

Which of the plan's distinctions each card most informs

| Distinction | Cards |
|---|---|
| Local correctness vs global utility | M-03, M-14, M-16, M-19 |
| Accuracy vs probability quality | M-04, M-07, M-08 |
| Random noise vs structured error | M-01, M-06, M-11, M-14 |
| Factual voting vs preference aggregation | M-03 (HH-RLHF labelling), M-08 |
| Prediction vs simulation | M-05, M-06, M-07, M-09, M-10 |
| Variability vs benefit | M-06, M-08, M-13, M-17, M-18, M-19 |

---

## Area G: modern AI and multi-agent systems

### M-01 Correlated errors across LLMs

1. Source: Kim, Garg, Peng, Garg, "Correlated Errors in Large Language Models", ICML 2025 (PMLR 267), arXiv 2506.07962. https://arxiv.org/abs/2506.07962 (PDF https://arxiv.org/pdf/2506.07962). Accessed 2026-10-06. Used: Sec. 1, Fig. 1, Table 1, Sec. 4 (Fig. 2), Sec. 5 (Fig. 3). Read: full PDF text.
2. System: pairs and sets of existing LLMs answering fixed questions; no interaction. Decision: pick an answer to a multiple-choice question or rate a resume. Collective objective: none directly; the paper measures what ensembles, judges and hiring markets would inherit.
3. Error = departure from the dataset label (MMLU-based leaderboards) or from human resume-fit labels (Resumes: residual correlation). Natural (observed), not injected. Correlation measured as agreement rate when both models are wrong.
4. Dependence: across models, conditional on wrongness; shared provider, architecture and size raise it. Time and shared information not varied. Source claim: after controlling for these, more accurate model pairs are more correlated.
5. Mechanism: none proposed; it is a failure-boundary result for absorption by aggregation (the independence assumption behind voting and judge panels).
6. Comparison: observed agreement versus the 1/3 random-wrong baseline. Population: 349 models on 12,032 questions (HuggingFace), 71 models on 14,042 questions (Helm), 20 models on 1,800 resume-job pairs. Metric: agreement on errors; in the judge setting, "inflation" of judged accuracy; in the hiring simulation, systemic exclusion rate. Headline: about 60% agreement on Helm; one pair agrees on 0.9987 of commonly wrong questions. Uncertainty: regression coefficients with standard errors in Table 1; I did not extract intervals for the figures.
7. Supported: multiple-choice knowledge questions and one resume task. Failure modes it documents: judges inflate accuracy of weaker same-family models; correlated hiring models raise exclusion. Not tested: decisions in closed loops, readouts other than generated answers, small encoders.
8. Evidence type: empirical study on public leaderboard outputs plus a resume experiment. Replication: not reproduced by me. Code and data stated available (github.com/nikhgarg/llm_correlated_errors_public). Conflicts: none evident (Cornell).
9. Jev relevance: mechanistically analogous (it concerns generative LLMs, not Jev label-scoring readouts). Inference: repeating one model across many agents gives at least this much dependence; the 60% figure should not be transferred to Jev. Missing: error correlation of Jev-style readouts across states and across agents with different local inputs.
10. Cost: none to apply; measuring requires labelled items per model.

### M-02 Panel of LLM evaluators (PoLL)

1. Source: Verga et al. (Cohere), "Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models", arXiv 2404.18796 (2024). https://arxiv.org/abs/2404.18796. Accessed 2026-10-06. Used: Sec. 3.1, Tables 1-2, Sec. 4.5, Sec. 5. Read: full PDF text.
2. System: three judge models (Command R, Haiku, GPT-3.5) scoring other models' answers. Decision: correct/incorrect (QA) or 1-5 score (Chatbot Arena Hard). Objective: agreement with human judgements or with a human-derived ranking.
3. Error = disagreement with human labels (Cohen's kappa) or with Arena ranking (Pearson, Kendall tau). Natural.
4. Dependence: judges drawn from three disjoint model families on purpose, to reduce shared bias; independence not tested. Judge outputs compared per item.
5. Mechanism: absorption by aggregation (max vote for binary, average for scores) over deliberately different members.
6. Comparison: PoLL versus single GPT-4 and versus each member. Examples from the tables: single-hop QA kappa on one dataset GPT-4 0.627, Command R 0.734, Haiku 0.749, GPT-3.5 0.726, PoLL 0.763 (Table 1); Arena Pearson 0.917 for PoLL versus 0.817 for GPT-4 and 0.883 for Haiku/GPT-3.5 (Table 2). Population: three judges. Cost: PoLL is stated as seven to eight times cheaper than a GPT-4 Turbo judge. Uncertainty: unreported in the tables I read; differences between PoLL and the best single member are small.
7. Supported: QA correctness and pairwise chat judging with three families. Limits stated by the authors: only three settings and a limited set of judges; not tested in math or other domains; no explicit latency measurement. Failure mode shown: GPT-4 judge ranks another GPT-4 variant higher (intra-model bias).
8. Evidence type: empirical study. Replication: not located. Code: not checked. Conflict: author is a model vendor, and one panel member is the vendor's own model; the cost comparison favours the vendor's cheaper models.
9. Jev relevance: mechanistically analogous (factual-style judgement by an ensemble of different small models; the panel beating one large model is the closest published parallel to many small deciders). Missing: independence across members is assumed by design, and M-01 indicates that it is only partial.
10. Cost: three calls per item instead of one; latency lower in parallel than one large model per the authors (unmeasured).

### M-03 Debate versus voting among identical agents

1. Source: Choi, Zhu, Li, "Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?", arXiv 2508.17536 v2 (Oct 2025). https://arxiv.org/abs/2508.17536. Accessed 2026-10-06. Used: Table 1, Sec. 3.2, Sec. 4 (martingale theorem). Read: full PDF text. Supporting source with fetch of abstract only: Smit et al., "Should we be going MAD?", ICML 2024, arXiv 2311.17371 (abstract and Figure 1/Table 2 text lines opened; not examined in depth).
2. System: five agents (same model) answering benchmark questions, with or without debate rounds. Decision: choose an answer. Objective: accuracy.
3. Error = wrong benchmark answer; includes an alignment-labelling task (HH-RLHF) where the label is an annotator preference. Natural (sampling randomness).
4. Dependence: agents are samples of one model. In debate, agents condition on each other's answers (state and shared information). The theorem assumes homogeneous, fully connected agents.
5. Mechanism: absorption by majority voting; claimed non-contribution of debate as correction. Source claim: debate induces a martingale over agents' belief in the correct answer, so expected correctness does not change; a targeted bias toward correction helps.
6. Comparison: single agent, three MAD variants (T = 2, 3, 5 rounds), majority voting without debate. N = 5 agents, seven benchmarks, Qwen2.5-7B-Instruct and Llama3.1-8B-Instruct (a 32B model in Sec. 6). Qwen average accuracy over the seven benchmarks (Table 1): single 0.7205, best MAD (decentralised, T = 2) 0.7377, majority voting 0.7691. Llama average: single 0.6203, best MAD 0.6990, majority voting 0.7242. On Arithmetic with Qwen, single 0.814 versus voting 0.990. Centralised MAD is below the single-agent baseline in several cells (average 0.6551 Qwen at T = 2; 0.5670 Llama at T = 5). On the HH-RLHF preference-labelling task the gain from voting is small (Qwen 0.4773 to 0.4867). Single-agent baseline averaged over five runs with reported spread; multi-agent rows show no spread.
7. Supported: closed-form and multiple-choice style tasks with small open models. Failure modes: debate can lower accuracy; gains on the preference-like task are near zero. Theorem holds only under its homogeneity and full connectivity assumptions.
8. Evidence type: empirical study plus theorem in a stylised model. Replication: Smit et al. reach a compatible conclusion (debate does not reliably beat self-consistency), which I read only at abstract level. Code stated available (github deeplearning-wisc/debate-or-vote). Conflicts: none evident.
9. Jev relevance: mechanistically analogous. Inference: voting over repeated samples helps when sample errors are partly independent (sampling variance), and this says nothing about shared bias, which M-01 shows exists across models. Missing: sampling-based variation exists for generative models; Jev label-scoring readouts are near deterministic unless noise is injected, so the "independent samples" premise itself needs checking.
10. Cost: N times the inference cost for voting; debate adds T rounds of context.

### M-04 Twelve-LLM forecasting ensemble versus a human crowd

1. Source: Schoenegger, Tuminauskaite, Park, Bastos, Tetlock, "Wisdom of the silicon crowd: LLM ensemble prediction capabilities rival human crowd accuracy", Science Advances 2024 (PMC11800985). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11800985/. Accessed 2026-10-06. Used: Abstract, Study 1 methods and results, Limitations. Read: HTML full text through curl, searched by key terms and read in part (not every paragraph).
2. System: twelve LLMs forecasting the same questions; crowd formed by median aggregation. Decision: a probability for a binary event. Objective: low Brier score against realised outcomes.
3. Error = Brier score (strictly proper), which scores probabilities, not only the top choice. Natural.
4. Dependence: models differ in training and fine-tuning; no independence test. Shared information: all saw the same question text; human forecasters saw a community prediction on some questions (15 of 31 collected before it was revealed).
5. Mechanism: absorption by averaging heterogeneous probabilistic forecasts.
6. Comparison: the LLM ensemble versus a no-information benchmark (always 50%) and versus 925 human forecasters in a three-month Metaculus tournament; 31 binary questions. Source claim: the ensemble beats the no-information benchmark and is statistically indistinguishable from the human crowd; the aggregate had a numerically lower Brier score than 9 of the 12 models, but not significantly after multiple-comparison adjustment. Also observed: positive bias (acquiescence-like) with just over 45% of questions resolving positive. Effect sizes beyond these: unreported in what I extracted.
7. Supported: real-time geopolitical and economic forecasting with a small question set. The authors list the low number of questions as a substantial limitation. Single models did not clearly beat the 50% baseline in the earlier study they cite.
8. Evidence type: empirical study with null and alternative hypotheses stated in the text (the text mentions a non-preregistered robustness analysis; I did not verify which analyses were preregistered). Replication: the paper cites related replications for single-model weakness; none located for the ensemble result. Conflicts: one author wrote some questions (disclosed).
9. Jev relevance: mechanistically analogous (probability-quality evaluated by a proper scoring rule, aggregation across different models). Inference: it separates accuracy from probability quality, which the plan requires. Missing: forecasting of external events, not decisions inside a simulation.
10. Cost: twelve model calls per question.

### M-05 Silicon samples: positive case for distributional fidelity

1. Source: Argyle, Busby, Fulda, Gubler, Rytting, Wingate, "Out of One, Many: Using Language Models to Simulate Human Samples", arXiv 2209.06899 v1 (Sept 2022; later Political Analysis 2023, not opened). https://arxiv.org/abs/2209.06899. Accessed 2026-10-06. Used: Sec. 3 (four criteria), Sec. on ANES vote choice, Table 1, Cramer's V analysis. Read: arXiv v1 full PDF text.
2. System: GPT-3 conditioned on first-person backstories built from real survey respondents (ANES 2012/2016/2020, Pigeonholing Partisans). Decision: vote choice or word lists. Objective: distributional and correlational fidelity to the human sample.
3. Error = departure of simulated response distribution or association pattern from the human survey. Inferred through comparison with survey data.
4. Dependence: each silicon respondent is conditioned on one real person's covariates; independence across respondents is supplied by the real covariate distribution (inference). Model sampling per prompt.
5. Mechanism: none for error absorption; this is a validity argument for use as a simulator or predictor ("algorithmic fidelity").
6. Comparison: GPT-3 versus ANES. Source figures: mean predicted probability of voting for the Republican candidate 0.391 versus 0.404 in 2012; 0.432 predicted in 2016; tetrachoric correlation with reported vote 0.90 (2012) and 0.92 (2016) across all respondents. Population: thousands of conditioned backstories; I did not extract the exact N. Uncertainty: not extracted.
7. Supported: US survey items with rich demographic conditioning, one model (GPT-3), one time period. Known failure modes appear in later work: M-06 (flattening, misportrayal), M-07 (alignment-tuned models are far less representative), M-11 (prompt fragility). Argyle's own limitations were not extracted.
8. Evidence type: empirical study. Replication: later studies (M-06, M-07) fail to find the same fidelity for other models and settings. Code and data: not checked. Conflicts: none evident.
9. Jev relevance: speculative for a village simulation. Inference: good fidelity on aggregate vote shares with real covariates does not show that a model can generate heterogeneous preferences from invented personalities. Missing: real conditioning data, which a game village does not have.
10. Cost: one call per simulated person; requires a survey with covariates.

### M-06 LLMs misportray and flatten identity groups

1. Source: Wang, Morgenstern, Dickerson, "Large language models that replace human participants can harmfully misportray and flatten identity groups", Nature Machine Intelligence 2025; arXiv 2402.01908 v3 (Feb 2025). https://arxiv.org/abs/2402.01908. Accessed 2026-10-06. Used: Abstract, Fig. 4, Fig. 5 and surrounding text. Read: arXiv v3 full PDF text.
2. System: four LLMs (Llama-2-Chat 7B, Wizard Vicuna Uncensored 7B, GPT-3.5-Turbo, GPT-4) prompted with demographic identities; free-response questions discretised into categories. Objective: whether LLM responses match human in-group responses and human diversity.
3. Error: misportrayal (closer to out-group views of the group than to in-group views) and flattening (less diverse than humans). Measured by human studies and several diversity measures. Natural.
4. Dependence: 100 samples per question and identity from one model; the diversity shortfall is the dependence.
5. Mechanism: none; this is a failure boundary for variability as a source of population diversity. Source claim: next-word-prediction training pushes toward likely answers.
6. Comparison: LLM versus human in-group responses, 3,200 human participants over 16 identities; 100 LLM responses per question. Source result: nearly all models and identities are less diverse than humans across the measures; GPT-4 and GPT-3.5 cover about 3 of 5 multiple-choice options in 100 samples. Temperature test on GPT-4 at 1.0, 1.2, 1.4: diversity measured by unique n-grams reaches human level only at 1.4, where the text is incoherent, and no semantic measure reaches human diversity. Intervals: shown as 95% intervals in figures; not extracted.
7. Supported: English survey-like questions, identity prompting, four models. Failure mode central to the paper. Inference-time techniques "reduce, but do not remove" harms.
8. Evidence type: empirical study with human participants. Replication: not located. Code/data: not checked. Conflicts: none evident.
9. Jev relevance: mechanistically analogous to persona-conditioned residents; directly demonstrates the failure of temperature as a diversity fix for generated text. Inference: Jev label scoring differs from free text generation, so temperature or sampling over option scores might behave differently; this card does not test it.
10. Cost: human studies needed to check fidelity; none to run the prompts.

### M-07 Whose opinions do language models reflect

1. Source: Santurkar, Durmus, Ladhak, Lee, Liang, Hashimoto, "Whose Opinions Do Language Models Reflect?", arXiv 2303.17548 (ICML 2023). https://arxiv.org/abs/2303.17548. Accessed 2026-10-06. Used: Abstract, Sec. 4.1 (representativeness), modal-representativeness paragraph. Read: arXiv v1 full PDF text.
2. System: nine LMs (350M to 178B parameters, OpenAI and AI21) compared with Pew American Trends Panel answers (OpenQA with 60 demographic groups). Decision: option probabilities for opinion questions.
3. Error = divergence between the model's option distribution and the group's distribution (a distribution-level criterion, not per-item accuracy). Inferred by comparison with survey data.
4. Dependence: not applicable; measured per question.
5. Mechanism: none; failure-boundary result for sampling from scores. Source observation: a human-feedback-tuned model assigned more than 0.99 probability to one option on most questions, unlike human respondents, and its answers resembled the modal opinions of some groups.
6. Comparison: base versus feedback-tuned models; default versus demographic steering. Source claims: substantial misalignment with US groups, "on par with the Democrat-Republican divide on climate change"; steering does not remove it. Effect sizes beyond these: unreported in my extraction.
7. Supported: US-centric English multiple-choice opinions; models from 2022-2023.
8. Evidence type: empirical study. Replication: not reproduced; later models not covered. Code and data stated available (github tatsu-lab/opinions_qa). Conflicts: none evident.
9. Jev relevance: mechanistically analogous to probability quality. It shows that a model's confidence can be far sharper than human response frequencies. This is the one card that bears directly on the framing item A3 (calibration for sampling). Missing: models used here are generative LLMs of 2022-2023; Jev readouts are different.
10. Cost: none.

### M-08 LLM agents voting in participatory budgeting

1. Source: Yang, Dailisan, Korecki, Hausladen, Helbing, "LLM Voting: Human Choices and AI Collective Decision-Making", arXiv 2402.01766 v3 (Aug 2024). https://arxiv.org/abs/2402.01766. Accessed 2026-10-06. Used: Abstract, Sec. on temperature (Fig. 7), order-effects text, Limitations. Read: arXiv v3 full PDF text.
2. System: GPT-4 Turbo and LLaMA-2 70B agents voting on 24 participatory-budgeting projects, compared with data from a human voting experiment. Decision: approval, cumulative, ranked or other voting inputs. Objective: aggregate preference and individual-vote agreement with humans, and preference diversity.
3. Error: not a task error; the criteria are alignment with the human preference ranking (Kendall's tau), individual overlap (Jaccard), and diversity (Jaccard distance). Preference differences are treated as legitimate, so this is a preference-aggregation case. Inferred against human data.
4. Dependence: agents share a model; persona text from respondents' self-reported preferences creates between-agent variation; order and ID labelling are shared state.
5. Mechanism: none for correction; this studies variability (temperature) and structure (personas) as determinants of collective preference outcomes.
6. Comparison: LLM versus human aggregate rankings; temperature sweep; persona on/off; order and ID reversal. Source numbers: GPT-4 with persona gives the highest tau reported for any condition, 0.54; LLaMA-2 tau is near 0 at all temperatures; for GPT-4, tau is highest at temperature 1 and moving to 1.5 lowers tau from 0.39 to 0.37 while diversity (Jaccard distance) rises from 0.44 to 0.67; reversing order and IDs changes LLaMA-2 outputs substantially (tau -0.2 in one comparison). Source conclusion: no temperature setting maintained both human-like preferences and human-level diversity; LLMs "may lead to less diverse collective outcomes". Human N: unreported in my extraction.
7. Supported: one participatory-budgeting setting; limits stated by authors (context specificity, order effects not measurable in the human data). Failure modes: strong order and ID effects; persona raised self-interest relative to humans.
8. Evidence type: empirical study against a human experiment. Replication: not located. Code and data: stated available. Conflicts: none evident.
9. Jev relevance: mechanistically analogous to the "village votes" idea and the only card here about preference aggregation by model agents. Source claim versus inference: the paper shows temperature trades diversity against alignment for generated votes; whether sampling from Jev option scores shows the same trade-off is not tested.
10. Cost: human experiment for the baseline; multiple runs per voter.

### M-09 Generative agents (25-agent village)

1. Source: Park, O'Brien, Cai, Morris, Liang, Bernstein, "Generative Agents: Interactive Simulacra of Human Behavior", UIST 2023, arXiv 2304.03442. https://arxiv.org/abs/2304.03442. Accessed 2026-10-06. Used: Sec. 6 (believability evaluation), Sec. 7.1 (emergent outcomes), Sec. 7.2-8.2 (failure modes, limitations). Read: full PDF text.
2. System: 25 LLM agents with memory, reflection and planning in a sandbox town over two simulated days. Decision: next action and dialogue. Objective: believable individual behaviour and emergent social outcomes (information spread, coordination).
3. Error: lack of believability (ranked by 100 human evaluators), hallucinated knowledge (checked against memory streams), misclassified location norms. Natural.
4. Dependence: agents influence each other through conversation; shared base model; shared world state.
5. Mechanism: none for error correction in the paper; the architecture (memory, reflection, planning) is the intervention. Constructive variability is not isolated.
6. Comparison: full architecture versus ablations and a crowdworker-authored condition, ranked by 100 evaluators, TrueSkill: full 29.89 (sigma 0.72), no-reflection 26.88, no-reflection-no-planning 25.64, crowdworker 22.95, none of memory-planning-reflection 21.21; Kruskal-Wallis H(4) = 150.29, p < 0.001; the paper reports d = 8.16 between prior-work condition and the full architecture. Emergence: agents knowing a party invitation rose from 1 (4%) to 13 (52%) and knowing a candidacy from 1 (4%) to 8 (32%) in two days; network density rose from 0.167 to 0.74; 6 of 453 agent responses (1.3%) about other agents were hallucinated. Single run; no population variation or seeds reported.
7. Supported: a small town, two days, one base model of 2023. Failure modes recorded by the authors: retrieval errors, erratic location choices as memory grows, norm misclassification (agents entering a closed shop or an occupied one-person bathroom), over-politeness and over-cooperation attributed to instruction tuning, and cost of "thousands of dollars" for two days.
8. Evidence type: evaluated implementation with a human-rated study and a descriptive deployment measure. Replication: later work (M-10, M-11, M-12) concerns larger systems; no direct replication opened. Code: released per the paper (not checked). Conflicts: none assessed.
9. Jev relevance: mechanistically analogous; shows a measured interactive population but with a generative LLM and 25 agents. Source versus inference: over-cooperation is attributed by the authors to instruction tuning (their hypothesis); homogeneous politeness would reduce the variability a Jev village might need.
10. Cost: high inference cost per agent-day; more modules (memory, reflection) required.

### M-10 OASIS: large LLM-agent social media simulation

1. Source: Yang et al. (CAMEL-AI), "OASIS: Open Agent Social Interaction Simulations with One Million Agents", arXiv 2411.11581. https://arxiv.org/abs/2411.11581. Accessed 2026-10-06. Used: Sec. 3 (information propagation, herd effect, scale experiment), Fig. 6-7, limitations heading. Read: full PDF text, most of the results sections.
2. System: LLM agents with a 21-action space on simulated X and Reddit platforms with recommendation systems, up to 10,000 or more agents in the experiments reported. Decision: like, comment, follow, post. Objective: reproduce information spread, polarisation and herd effects seen in human data.
3. Error: discrepancy from real-world curves (normalised RMSE) and from human behaviour in a herd-effect experiment; not per-agent correctness. Inferred by comparison.
4. Dependence: strongly interactive (recommender plus social exposure); agents share a model family.
5. Mechanism: none for correction; scale is the manipulated variable.
6. Comparison: simulation versus real information-propagation curves; Source claim: propagation trends matched with normalised RMSE around 30%. Herd effect on Reddit (40 time steps): for initially disliked comments, agents score significantly lower than humans, which the authors read as agents being "more inclined" to herd. Scale: with 100 agents no herd effect appeared in the counterfactual-post experiment; at 10,000 agents the effect appeared and the authors describe growing self-correction among agents. Seeds, intervals: unreported in my extraction.
7. Supported: social-media interaction types, a handful of phenomena. Failure/qualifier: herding stronger than humans; results depend on the base LLM (Fig. 13, per the paper).
8. Evidence type: evaluated implementation with a human-data comparison. Replication: none located. Code available (github camel-ai/oasis). Conflicts: system authors evaluate their own simulator.
9. Jev relevance: mechanistically analogous; shows a population-size dependence that a 300-resident village would be sensitive to. Inference: effects that appear only at 10,000 agents may not exist at 300.
10. Cost: LLM call per agent step; scaling infrastructure.

### M-11 Robustness of LLM social simulations to small specification changes

1. Source: Ye, Cao, Chen, Ferrara, "Stop Drawing Scientific Claims from LLM Social Simulations Without Robustness Audits", arXiv 2605.18890 (17 May 2026), a position paper with two case studies. https://arxiv.org/abs/2605.18890. Accessed 2026-10-06. Used: Abstract, Sec. 4.1-4.2, Appendix C. Read: full PDF text, key sections. Preprint; peer review status not known to me.
2. System: (a) two LLM agents playing a 10-round repeated Prisoner's Dilemma; (b) 100 persona-conditioned agents in a 15-round echo-chamber simulation. Decision: cooperate or defect; choose a post or action from neighbours' feed. Objective: cooperation rate, polarisation metrics.
3. Error: not task error; the measured quantity is how much outcomes move under minor, nominally irrelevant changes to persona format, instruction framing, network homophily or hub assignment. Injected perturbations of the specification.
4. Dependence: repeated interaction among agents lets small differences cascade (the "butterfly effect" argument); model-family-specific.
5. Mechanism: none; failure-boundary result for global outcomes of closed-loop agent systems.
6. Comparison: perturbed versus plain persona formats, N = 30 seeds per condition, four LLMs. Source numbers: cooperation shifted by up to 76 percentage points (descriptive persona versus plain persona in the two-agent setting, one frontier model); the same perturbation shifted another model by 1 point; hub assignment in the echo chamber changed polarisation metrics with confidence intervals reported (example mean 0.759 [0.739, 0.779] versus 0.690 for anti-regulation hubs).
7. Supported: two toy settings. The authors state robustness is model- and claim-specific.
8. Evidence type: controlled simulation (small, two case studies). Replication: none located. Code: not checked. Conflicts: none evident.
9. Jev relevance: mechanistically analogous; it is the clearest measured warning that macro outcomes of an LLM-driven population can depend on prompt wording. Inference: a Jev village might show smaller or larger sensitivity; untested.
10. Cost: robustness audits multiply the number of simulation runs (authors acknowledge the burden).

### M-12 Project Sid: many-agent Minecraft simulations

1. Source: Altera.AL, "Project Sid: Many-agent simulations toward AI civilization", arXiv 2411.00114 (Oct 2024). https://arxiv.org/abs/2411.00114. Accessed 2026-10-06. Used: Sec. 1 (Reasons 1-2, Fig. 2), Sec. 3 (Fig. 5), Sec. 5.1 (specialisation, Fig. 8), Sec. 7 (limitations). Read: full PDF text, selected sections.
2. System: 10 to 1,000+ agents in Minecraft with a modular architecture (PIANO). Decision: action selection with social goals. Objective: individual item progression, role specialisation, adherence to collective rules, cultural transmission.
3. Error: hallucination and action loops that propagate through conversation (author claim, conceptual figure); measured outcomes are item counts and role distributions. Natural.
4. Dependence: agents share information through chat; a hallucination can spread, per the authors (Fig. 2 is a schematic, not a measurement).
5. Mechanism: correction by architecture: an "action awareness" module compares expected and observed outcomes; a social-awareness module supports role persistence.
6. Comparison: full architecture versus baseline and ablations. Source figures: average 17 unique items per agent after 30 minutes (25 agents, 5 repeated simulations); best agents 30 to 40; with action awareness ablated, item progression is lower (Fig. 5A; numbers not extracted). Specialisation (30 agents, 20 minutes): without social modules, roles did not persist and were homogeneous (lower role entropy). 49 agents over 4 hours saturated at about one third of all items. Intervals and seeds: mostly unreported.
7. Supported: a Minecraft setting with GPT-4o; authors state older base models could not do it, and list lack of spatial reasoning and lack of innate drives as limitations. "Preliminary results" in their own words.
8. Evidence type: evaluated implementation, vendor technical report. Replication: none. Code: not checked. Conflicts: company reporting on its own product.
9. Jev relevance: mechanistically analogous for local error correction through environment feedback (expected versus observed outcomes). Source claim versus inference: that a small hallucination rate "poisons" downstream behaviour is argued, not measured here.
10. Cost: extra modules and many parallel LLM calls per agent.

---

## Area H: games and interactive simulation

### M-13 BotPrize: Turing-style test of game bots (pre-2023)

1. Source: Karpov, Schrum, Miikkulainen, "Believable Bot Navigation via Playback of Human Traces", in Believable Bots (Springer, 2012), PDF https://nn.cs.utexas.edu/downloads/papers/karpov.believablebots12.pdf. Accessed 2026-10-06. Used: Sec. 3.2 (BotPrize 2010 rules), Sec. 5.1 (Table 2 and observations). Read: full PDF text. Background (not opened at source): Hingston, "A Turing Test for Computer Game Bots", IEEE TCIAIG 1(3), 2009, https://ro.ecu.edu.au/ecuworks/594/ (abstract only).
2. System: Unreal Tournament 2004 deathmatch with a "judging gun"; bots, native game bots and humans in each game. Decision: bot movement and combat. Objective: be judged human by human judges.
3. Error: any behaviour that reveals a bot, for example getting stuck on geometry; measured by the percentage of judgements calling the bot human. Natural.
4. Dependence: judges' decisions per opponent; no population effects.
5. Mechanism: not variability itself; the authors correct the faults that reveal bots (stuck states) by replaying human traces. This is correction of conspicuous failures, not use of mistakes.
6. Comparison: 2010 humanness ratings (percent of judgements calling the bot human, Table 2): native UT2004 bot 35.4, Conscious-Robots 31.8, UT^2 27.3, ICE-2010 23.3, Discordia 17.8, w00t 9.3. Five teams, three one-hour rounds of three 20-minute games. The human baseline value is not in the table I read. Later result (secondary, not verified at source): search snippets of news coverage report that two bots passed the 50% mark in 2012 (UT^2 and MirrorBot at 52%) versus 40% for humans; treat as unverified.
7. Supported: first-person shooter, 2010 competition. Failure mode shown: bots stuck in narrow areas not covered by the navigation graph; the authors note that the human-trace database is needed in each problem area. Observations rely on reading demo recordings (qualitative).
8. Evidence type: empirical competition results plus qualitative author analysis. Replication: yearly competition; not re-run. Data: judgement records on botprize.org (per the paper; not opened). Conflicts: authors are a competing team.
9. Jev relevance: mechanistically analogous. Inference: errors that look like faults (stuck, jerky) read as non-human; random-looking variation is not what judges rewarded. Missing: BotPrize judges are looking for humanness, not enjoyment.
10. Cost: recording human traces; engineering effort.

### M-14 Maia: mistakes modelled by state, not by weakening (pre-2023)

1. Source: McIlroy-Young, Sen, Kleinberg, Anderson, "Aligning Superhuman AI with Human Behavior: Chess as a Model System", KDD 2020, arXiv 2006.01855. https://arxiv.org/abs/2006.01855. Accessed 2026-10-06. Used: Introduction, Sec. on depth-limited Stockfish and Leela, Maia results, blunder prediction. Read: full PDF text.
2. System: chess engines predicting the move a human of a given rating plays. Decision: a move. Objective: match human moves (and predict human blunders), not win.
3. Error: a human blunder is a move that worsens the position by a threshold (defined from Stockfish evaluations); the target is the actual human move. Inferred from game records.
4. Dependence: moves conditioned on board state and rating band; no agent interaction.
5. Mechanism: not variability for effect; the claim concerns structure of error: human mistakes are state-dependent and predictable, and degraded strong engines do not reproduce them.
6. Comparison: 15 depth-limited Stockfish versions match human moves 33 to 41% of the time with accuracy that rises with the strength of the humans being predicted (so they do not target weak players); Leela versions reach at most 46% and are nearly flat across rating; Maia reaches above 52%, with Maia 1100 at about 46%. Test data: Lichess human games (scale per the paper; I did not record the exact number of games for the move-matching test; the blunder-prediction training set is stated as 182M blunders and 272M non-blunders). Intervals: unreported in my extraction.
7. Supported: chess on Lichess data. Not a player study of enjoyment; the paper argues for human-AI alignment and teaching. A weakened engine's errors are "orthogonal" to human strength, in the authors' words.
8. Evidence type: empirical study with evaluated implementation. Replication: Maia has public models and later work (a personalised version is cited in search results, not opened). Code: github CSSLab/maia-chess (listed in search; not opened). Conflicts: co-authors from Microsoft Research (the paper concerns its own system).
9. Jev relevance: mechanistically analogous and the strongest pre-2023 games-side card on structured versus random error. Inference: adding random noise to a strong policy is not expected to produce human-like mistakes. Missing: whether human-like mistakes make a game more enjoyable (not evaluated).
10. Cost: large human game datasets and training per rating band.

### M-15 Human-likeness judgements of navigation agents

1. Source: Milani et al. (Microsoft Research, Ninja Theory, CMU), "Navigates Like Me: Understanding How People Evaluate Human-Like AI in Video Games", CHI 2023, arXiv 2303.02160. https://arxiv.org/abs/2303.02160. Accessed 2026-10-06. Also read as background: Devlin et al., "Navigation Turing Test (NTT)", ICML 2021, arXiv 2105.09637 (opened; only the study design lines read). Used: Sec. 3.3-3.4 (agents), Sec. 5 (HNTT), Sec. 7 (results). Read: full PDF text, main sections.
2. System: a 3D game navigation task; judges watch paired videos, one human and one agent. Decision: which video navigated more like a human. Objective: agents that humans judge human-like.
3. Error: behaviours that judges cite as non-human: lack of smoothness, abrupt turns, collisions, low responsiveness. Coded from free-text justifications by the authors. Natural (agent behaviour).
4. Dependence: none across agents; each judge sees several trials.
5. Mechanism: correction of conspicuous faults by reward shaping (penalties for abrupt camera changes and wall collisions) and finer action space (14 actions instead of 8).
6. Comparison: hybrid and symbolic baseline agents versus a reward-shaping agent versus human videos, crowd judges on MTurk. Source claims: only the reward-shaping agent passes the human-likeness test; judges characterise human-like behaviour as smoother, more responsive and goal-directed; game familiarity did not predict accuracy. Numbers from Table 5: not extracted. Population: judge count not extracted.
7. Supported: simple navigation, short videos (15 seconds); the authors state that familiarity may matter in full games.
8. Evidence type: empirical human study. Replication: builds on the earlier study, which also found the baselines detected above chance. Code and data: not checked. Conflicts: the authors work for the studio and lab that built the agents.
9. Jev relevance: mechanistically analogous. Inference: people used smoothness and goal-directedness as markers of humanness; a stream of random-looking mistakes would be expected to break both, but this study does not test noise injection. Missing: enjoyment.
10. Cost: human judging; reward engineering.

### M-16 Hamlet: dynamic difficulty adjustment by inventory control (pre-2023)

1. Source: Hunicke and Chapman, "AI for Dynamic Difficulty Adjustment in Games", Northwestern University (AAAI workshop paper, 2004). PDF https://users.cs.northwestern.edu/~hunicke/pubs/Hamlet.pdf. Accessed 2026-10-06. Used: whole short paper, in particular "Policies", "Preliminary Conclusions" and "Evaluation". Read: full PDF text. (A related paper, "The case for dynamic difficulty adjustment in games", Hunicke 2005, was found but not opened.)
2. System: Hamlet, a system in the Half-Life engine that monitors player statistics and adjusts supply and demand of items such as health and ammunition. Decision: intervene or not, and how. Objective: keep the player in a "flow channel".
3. Error: not defined for the player. The system itself reduces the accuracy of enemy attacks or donates a health pack when the player is "flailing"; so deliberate suboptimality of NPCs is a control action. Inferred state estimate of the player.
4. Dependence: interventions are conditioned on the player's recent history, past interventions and location.
5. Mechanism: steering through deliberate adjustments of NPC accuracy and resources.
6. Comparison: none. The paper describes the system and says that evaluation (heart-rate monitoring of players on two settings) is planned. Population, effect size, uncertainty: unreported.
7. Supported: described for a first-person shooter. Authors state that DDA takes control away from designers and that commercial DDA has often failed (citing a GDC talk, not opened).
8. Evidence type: design description of an implemented system; no evaluation in this paper. Replication: none. Code: none stated. Conflicts: none.
9. Jev relevance: speculative for effect, but it documents the idea that NPC imperfection can be a deliberate, state-conditioned steering variable. No evidence of benefit here.
10. Cost: monitoring, estimators and designer-defined policies.

### M-17 Do suboptimal AI opponents improve player experience (weak evidence)

1. Source: Khan, "Do Suboptimal AI Opponents Improve Player Experience? An Experimental Study in Game AI", Master's thesis, Youngstown State University, August 2026. https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=ysu1786448341566405&disposition=inline. Accessed 2026-10-06. Used: Abstract, Tables 2-3, Sec. 5.4. Read: full PDF text (selected sections). Unreviewed student thesis.
2. System: a 2D stealth game with a finite-state-machine guard (patrol, chase, search, return) using vision cones and A*. Decision: guard actions. Objective: player experience measured by questionnaire plus survival and capture.
3. Error (suboptimality) is designed and injected: reduced vision range, delayed reactions, less frequent replanning, slightly inefficient paths, randomised patrol pauses. Injected.
4. Dependence: none across agents; one guard.
5. Mechanism: constructive variability or deliberate handicap, tested against an optimal-AI condition.
6. Comparison: within-subject, optimal versus suboptimal AI, ten participants, 49 and 51 trials. Mean survival 29.49 s (SD 27.19) optimal versus 31.12 s (SD 25.22) suboptimal; capture rate 59.18% versus 60.78%. The author reports participants noticed the difference and gave positive ratings of fairness, challenge, believability and enjoyment, with no strong measurable difference. No significance tests were extracted.
7. Supported: one small game and ten players. Author states small sample, one environment, rule-based AI, differences between conditions may be too small, subjective measures.
8. Evidence type: empirical study, very small. Replication: none. Code and data: not checked. Conflicts: none evident.
9. Jev relevance: speculative; included mainly as a null or weak result on the question "do deliberate mistakes raise enjoyment". Inference: it cannot support either direction.
10. Cost: building both AI conditions; running a human study.

### M-18 XCOM hit chance (anecdote: displayed odds versus experienced fairness)

1. Source: Game Developer staff report of an interview with Jake Solomon (Firaxis), "Jake Solomon explains the careful use of randomness in XCOM 2", 1 March 2016. https://www.gamedeveloper.com/design/jake-solomon-explains-the-careful-use-of-randomness-in-i-xcom-2-i-. Accessed 2026-10-06. Read: fetch-summary only (quotes returned by the fetch tool; not independently checked against the full page).
2. System: a tactical game where displayed hit chances drive combat. Decision: attack resolution. Objective: player experience.
3. Error: not defined; the issue is player perception of probability as "close to a hundred" at high displayed odds.
4. Dependence: outcomes in sequence (miss streaks); hidden adjustments at lower difficulties.
5. Mechanism: steering of experienced randomness. Per the fetch summary, Solomon says several things tweak the number in the player's favour at lower difficulties ("That 85 percent isn't actually 85 percent"), that it may be closer to 95 percent, and that unpredictability implies an uneven experience.
6. Comparison, population, effect size: unreported. No data.
7. Supported: statements by one designer about one franchise. Other web items (forum posts, blog posts) gave claims about hidden aim assist and miss-streak boosts; I did not open or verify them and do not use them.
8. Evidence type: anecdote (practitioner interview). Replication: not applicable. Conflicts: developer describing its own design.
9. Jev relevance: speculative. Inference: shows that designers have chosen to correct randomness toward the perceived rather than the mathematical expectation; it says nothing about a measured benefit.
10. Cost: hidden correction logic; reduces transparency of displayed numbers.

### M-19 Left 4 Dead AI Director (anecdote with design documentation)

1. Source: Booth (Valve), "The AI Systems of Left 4 Dead", GDC 2009 slides. https://steamcdn-a.akamaihd.net/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf. Accessed 2026-10-06. Used: slides on "Structured Unpredictability" and "Adaptive Dramatic Pacing". Read: full PDF text.
2. System: a director that populates the level and modulates threat intensity for four human players. Decision: when to create or remove infected, items and so on. Objective: replayability and dramatic pacing.
3. Error: not applicable; variability is designed. The estimator of "survivor intensity" is admitted to be crude.
4. Dependence: intensity estimate per survivor from injuries, incapacitation and nearby kills; the director's actions feed back into player state.
5. Mechanism: constructive variability under a designer-defined envelope, plus steering through a feedback estimator. Source claims: population functions are "not purely random, nor deterministically uniform"; spawn timings are randomised between 90 and 180 seconds; the algorithm adjusts frequency (pacing), not amplitude (difficulty), and "simple algorithms can generate compelling pacing"; timing and location of peaks differ each play.
6. Comparison, population, effect size, uncertainty: unreported. The slides give no player-study data.
7. Supported: one cooperative shooter design. Failure modes not discussed in the slides.
8. Evidence type: practitioner presentation (anecdote), evaluated only by commercial release. Replication: none. Conflicts: developer describing its own product.
9. Jev relevance: speculative to mechanistically analogous (variability bounded by a state-conditioned controller). Inference: separating pacing from difficulty is a design idea for controlling variability's cost; no evidence in this card that it increases enjoyment.
10. Cost: designer effort to define population functions and intensity thresholds.

---

## Gaps in this file (details in the search log)

- No controlled player study was found that compares deliberate NPC mistakes with a no-mistake condition at adequate sample size (only M-17, which is weak).
- No source opened that studies randomness fairness in games with human participants (M-18 is an interview; an academic paper was listed but not opened).
- Dwarf Fortress / RimWorld storytellers: only practitioner pages seen, none used.
- Frank Lantz and Costikyan essays were not searched for or opened.
- Japanese search found a lead on human-like game AI using fluctuation, delay and fatigue (Fujii thesis, 2016) but the PDF could not be opened, so no numbers are used.
- Sampling versus argmax in LLM agents was searched once and returned mostly reinforcement-learning and reasoning papers; only M-06 and M-08 give measured temperature effects for generated outputs.
