# Catalog — new arXiv papers on Jev-style decision models, not in recent_study (cut-off 2026-10-19)

71 arXiv rows (70 kept, 1 excluded as off-topic) plus 3 non-arXiv entries (bottom). All arXiv ids were absent from [../recent_study/catalog.md](../recent_study/catalog.md). Most are dated 2026-10-08 to 10-16 (the newest id indexed by arXiv search on 2026-10-19 was 2610.23804, submitted 10-16; see [search-log.md](search-log.md)). Three are September papers that the first survey's `Jev` keyword missed.

- **Finding column:** abstract-level paraphrase unless **Card = yes**. A card means the paper was read in full text and the numbers are checked against the body; cards are in [evidence/](evidence/).
- **All are preprints**, a few days to three weeks old, none peer reviewed. "Hosted Jev" = the closed TypeSafe API (jev-1.13.0 unless stated). Authors who rank a model they built are flagged in the cards.
- Treat the finding column as a pointer, not a verified claim.

Theme counts: Order, option set, fallback 7 · Calibration, abstention, cascades 8 · Robustness, security, bias 13 · Benchmarks and audits 10 (incl. the excluded row) · Open models, training, architectures 17 · Agents and systems 11 · Domain applications 4 · Populations and simulation 1 · Non-arXiv 3. One theme per row. 16 papers have full-text cards.

## Order, option set and fallback (7)

| arXiv | Date | Title | Finding | Card |
|---|---|---|---|---|
| [2610.16655](https://arxiv.org/abs/2610.16655) | 10-12 | Does a Hosted Decision Model Respect Irrelevant Alternatives? Pre-registered test (Jev) | 299,463 hosted-Jev calls: every added option moves gold-vs-rival log-odds (0.20–0.52 nats RMS, 1.2–3× run-to-run), even at ≤0.1% mass; one packed call does not couple questions | yes |
| [2610.19856](https://arxiv.org/abs/2610.19856) | 10-14 | Lost in the Fallback: Do Typed Decision Models Use Fallback Options Reliably? | Paired Fallback Robustness test: fallback recall low (Intern 23.1% on gold-fallback vs 97.9% regular), equivalent wordings change up to 39.8% of decisions, position flips the sign | yes |
| [2610.18233](https://arxiv.org/abs/2610.18233) | 10-13 | Consider, Then Choose: Order-Invariant Decisions (Runoff) | Order flips grow with option count (4.7%→17.0% 2→20); hosted Jev 5.3%; Runoff (pointwise shortlist + all-position compare) ≈0 flips without training | yes |
| [2610.22066](https://arxiv.org/abs/2610.22066) | 10-15 | Prism-1: Position- and Rival-Independent Scoring | Hosted Jev violates Luce's axiom: shuffle flips 4.7% (floor 1.3%), one added option steers 10.9%; option-injection redirects 3–55%; per-option attention blocks fix it | yes |
| [2610.14631](https://arxiv.org/abs/2610.14631) | 10-10 | The Company a Question Keeps: Auditing Open Jev-Style Models for Retrieval | Request-set dependence only in Nimble (9.1%/8.0% flips), traced to serialized schema fields; evidence changes move decisions more; abstention on zero-answer states 7.7–85% | yes |
| [2610.19619](https://arxiv.org/abs/2610.19619) | 10-14 | Are AI Decision Models Biased? A Case Study of Jev | 41,500 hosted-Jev responses: right on classic items, but order and irrelevant numbers move probabilities; edited conjunction item wrong 500/500 at ~95% confidence | yes |
| [2609.30454](https://arxiv.org/abs/2609.30454) | 09-29 | Auditing System-1 Models on Biosecurity-Relevant Benchmarks | (Sept., missed earlier.) Hosted model on 6,020 WMDP/LAB-Bench items: ECE 0.034, AUROC 0.820; 37.4% of WMDP items change answer under four rotations of options |  |

## Calibration, abstention and cascades (8)

| arXiv | Date | Title | Finding | Card |
|---|---|---|---|---|
| [2610.19811](https://arxiv.org/abs/2610.19811) | 10-14 | Calibration and Risk-Budgeted Decisions with System One Models | Naive thresholds exceed the risk budget in ~half of settings; Learn-Then-Test 7.8%; "non-deployment" fallback when no threshold certifies; hosted Jev ECE 0.034–0.29 by task | yes |
| [2610.18579](https://arxiv.org/abs/2610.18579) | 10-13 | Reading Right, Acting Wrong: Decision Failures of System One Models in Agent Loops | 73–85% of errors follow correctly answered fact probes; all competent systems fail on the same 141 states | yes |
| [2610.19536](https://arxiv.org/abs/2610.19536) | 10-14 | Typed Decision Models on Tabular Data | 21 rewrites: Jev/Clef/Kev-27B robust to option rename/reverse (2–8%), nobody robust to table layout; confidence flags fragile (AUROC 0.81–0.93) but not wrong (0.59–0.84) | yes |
| [2610.18529](https://arxiv.org/abs/2610.18529) | 10-13 | How Reliable Are System-One Decisions in Medicine? | 15 medical sets, 8,742 items: stable under relabel/reorder in accuracy but individual reversals 3–13%; models do not recognise a missing correct answer | yes |
| [2610.20907](https://arxiv.org/abs/2610.20907) | 10-14 | From Detection to Decision: Calibration and Deferral for Prompt-Injection Detection | 47,611 examples: LLM judge AUROC 0.897, Jev 0.871, Prompt Guard 2 86M 0.757; Jev native probabilities not consistently better than post-hoc-calibrated classifiers |  |
| [2610.18488](https://arxiv.org/abs/2610.18488) | 10-13 | Recalibrating Many Questions with Few Labels | Theory: pooled isotonic fit with one held-out correction attains minimax rate across questions; per-question tuning loses a factor |  |
| [2610.18389](https://arxiv.org/abs/2610.18389) | 10-13 | PRISM: Calibrating Black-Box Judges with Counterfactual Probes | Attribute-emphasis probes + ridge regression on human labels raise agreement with human rankings for Jev and another judge on SummEval/HANNA |  |
| [2610.17016](https://arxiv.org/abs/2610.17016) | 10-12 | ProbabilityBench: Exact Ground-Truth Uncertainty | Simulated domains with exact class probabilities; most cost-quality Pareto models of 16 are decision models (Jev, Perplexity Decider) |  |

## Robustness, security and bias (13)

| arXiv | Date | Title | Finding | Card |
|---|---|---|---|---|
| [2610.12292](https://arxiv.org/abs/2610.12292) | 10-08 | One Word Opens the Gate: Option-Channel Attack on Typed Decision Models as Guardrails | Renaming only the permissive option label takes fail-open to 93–100% on four label-rendering models; confidence escalation fails (flipped answers equally confident) | yes |
| [2610.17820](https://arxiv.org/abs/2610.17820) | 10-12 | Same Attack, Different Judge: Controlled Adversarial Comparison of Jev, LLM Judges, Safety Classifiers | Jev most robust on input moderation, but structured-input forgeries bypass 19–29% of flagged phishing emails |  |
| [2610.18612](https://arxiv.org/abs/2610.18612) | 10-13 | Nudge the Judge: Program Decision Hijacking in Real-World Jev Applications | JevProbe on 228 real applications, 2,273 cases: 81.5% show decision flips |  |
| [2610.15537](https://arxiv.org/abs/2610.15537) | 10-11 | Poisoned into Action: Context Attacks on Typed Decision Workflows | 1,659 Jev-1.13.0 calls: poisoned evidence reaches execution; source-exclusion gate blocks it but also withholds correct decisions |  |
| [2610.14404](https://arxiv.org/abs/2610.14404) | 10-09 | DICE: Interface Attacks on System One Model | Adapter outputs (state extraction, question generation, output interpretation) can change the decision with the API untouched; binding checks stop them but reject some valid cases |  |
| [2610.19118](https://arxiv.org/abs/2610.19118) | 10-13 | DecisionRobust: Robustness Benchmark for JEV-Style Models, Text and Vision | 30 text / 17 vision configurations; attacks transfer to held-out models |  |
| [2610.19971](https://arxiv.org/abs/2610.19971) | 10-14 | Diagnose Before You Refine: Judge Feedback for Jailbreak Attacks | Jev's probabilistic scores used as attack feedback: 89.8% HarmBench ASR with 10 queries (a misuse of the interface, not an evaluation of it) |  |
| [2610.18122](https://arxiv.org/abs/2610.18122) | 10-13 | Cheap, Consistent, Calibrated, but Biased? Typed Decision Models as Judges | 8 TDMs on CALM: all biased in 3–8 of 12 tests; emotional tone drops a typical TDM from 99% to 42%; all flip verdicts when answers swap |  |
| [2610.22526](https://arxiv.org/abs/2610.22526) | 10-15 | Literal Lock-In: Test Language Shifts Literal Attraction on Bengali Idioms | Adding an idiom's literal gloss to options draws every arm to it (65–96% of residual errors); 1.9–6.4× more in Bengali than English |  |
| [2610.23668](https://arxiv.org/abs/2610.23668) | 10-16 | TUPLE-Bench: Privacy-Utility Trade-offs in Typed Decision Models | Instructions to withhold a cause fail: 91.9–99.9% of responses reveal it through selection or residual probabilities |  |
| [2610.18497](https://arxiv.org/abs/2610.18497) | 10-13 | Judges Follow the Reference: The Derivation Gap in Verifying Tool-Call Arguments | All 7 judges incl. CLM and Jev accept correct values less often when no reference text states them; DeRef reference-writer helps |  |
| [2610.20634](https://arxiv.org/abs/2610.20634) | 09-30 | Jev-as-a-Judge for RAG Claim Verification: Confidence-Gated Cascade | 495 claims: Jev vs frontier LLM tie on the usual metric (−0.56 pt) at 187× cost, but disagree on 15.2% and admit more unsupported claims (23.2% vs 14.1%) |  |
| [2610.16191](https://arxiv.org/abs/2610.16191) | 10-12 | Choice2Seq: Correctness Retention Across Output Interfaces | Jev 97.1%/99.5% on selection but retains 33.0%/2.1% of correct choices under serial construction |  |

## Benchmarks and audits (10, one excluded)

| arXiv | Date | Title | Finding | Card |
|---|---|---|---|---|
| [2610.21244](https://arxiv.org/abs/2610.21244) | 10-15 | System1-Arena: Which Decisions Can Be Left to System 1? | 92k questions/105 tasks + 138 closed-loop environments, 30 models; hosted Jev 72.6% acc on non-agentic tasks vs best LLM 81.1%; step accuracy does not predict loop success | yes |
| [2610.21412](https://arxiv.org/abs/2610.21412) | 10-15 | JevAgentHarness / AgentDecisionBench | Best isolated model solves 69.5% of agent tasks; fixed-threshold delegation −19.0 pt; threshold fitted on shadow trajectories saved 14.2% cost at no loss; failures start at irreversible wrong actions | yes |
| [2610.14112](https://arxiv.org/abs/2610.14112) | 10-09 | Does System One Transfer? Indonesian Regional Languages | Pre-registered: Jev accuracy higher on sentences closer to Indonesian; ECE does not grow but self-error ranking degrades; >500 labels per language to match zero-shot Jev; cascade to IndoBERT |  |
| [2610.18610](https://arxiv.org/abs/2610.18610) | 10-13 | Jev-ToM: Theory of Mind in Typed Decision Models | 11,117 questions, 5 typed models vs 7 generative: Jev 73.2% source-balanced, first or second in all six capability groups |  |
| [2610.20665](https://arxiv.org/abs/2610.20665) | 10-14 | The World Won't Wait: Agents Under a Live Clock (RealtimeBench) | Faster Jev beats a stronger LLM when the game keeps running; teacher-written instructions lift Jev 13.51→24.19 |  |
| [2610.16238](https://arxiv.org/abs/2610.16238) | 10-12 | Embodied Skill Bench | Agent-skill benchmark for LIBERO-Pro robot tasks; decision-model link is peripheral (adjacent) |  |
| [2610.23346](https://arxiv.org/abs/2610.23346) | 10-16 | Jev-as-a-Judge for Brazilian Portuguese IR | Relevance qrels from Jev: kappa 0.52–0.82, system rankings tau 0.90–0.93; reranking BM25 top-1000 nDCG@10 0.333→0.633 |  |
| [2610.14912](https://arxiv.org/abs/2610.14912) | 10-10 | Probable but Not Valid: Psychometric Audit of Decision Models as Synthetic Respondents | 14 decision models vs 47 LLMs on a Lithuanian survey (n=263): 13/14 decision models below gpt-5.4-mini with the rounded readout; probability vectors closer to human item marginals than rounded answers |  |
| [2610.13675](https://arxiv.org/abs/2610.13675) | 10-09 | Can Multimodal Decision Models Classify Breast Ultrasound Images? | Clef/Clef-Flash on 2,818 images: accuracy 51.6–74.9%, prompt-dependent; below majority class on BUS-BRA |  |
| [2610.19345](https://arxiv.org/abs/2610.19345) | 10-14 | When Is Smaller Greener? Right-Sizing LMs for Agentic AI | Excluded as off-topic: "decision model" here means a decision-theory model for choosing LLMs |  |

## Open models, training and architectures (17)

| arXiv | Date | Title | Finding | Card |
|---|---|---|---|---|
| [2610.17205](https://arxiv.org/abs/2610.17205) | 10-12 | Releasing the Inner Jev: A Simple Recipe for Open Decision Models | Training-free letter-logit readout on Gemma 4 31B 79.6 vs Jev 80.1 (after temperature scaling; 72.9 raw); short LoRA 84.4; gain from adapting the LM not the head | yes |
| [2610.20778](https://arxiv.org/abs/2610.20778) | 10-14 | Verdict: Encode Once, Decide Many (Verdict-MQ) | 395M encoder, structured mask: order irrelevant by construction, answers all questions in one read; KL 0.080 vs Laya 0.117; vendor-authored | yes |
| [2610.18773](https://arxiv.org/abs/2610.18773) | 10-13 | Jeva: System One Models from First Principles | Null-aware, permutation-invariant, cacheable design; 0.00% order flips vs hosted Jev 17.00%, Laya 66.83% (600 items); coverage gate AUROC 98.66% on BANKING77 | yes |
| [2610.17175](https://arxiv.org/abs/2610.17175) | 10-12 | FunDM: Cheap, Label-Free Decision Models from Frozen LMs | Label-free head on 24 of Qwen3-8B's 36 layers keeps 99% of MCQ accuracy (75.0 vs 75.7) |  |
| [2610.15501](https://arxiv.org/abs/2610.15501) | 10-10 | Large Decision Models | Run-time-label single-prefill models; +1.5–1.8 pt over matched baseline, 182× faster than reasoning; confidence router recovers ~92% of reasoning gain |  |
| [2610.17309](https://arxiv.org/abs/2610.17309) | 10-12 | StartLux-Decision: AutoThink Decision Models with RL | 0.8B–27B; RLCD² (proper-scoring reward, length penalty) cuts reasoning length up to 65%; vendor-style report with its own benchmark |  |
| [2610.19644](https://arxiv.org/abs/2610.19644) | 10-14 | Selective Reasoning for Typed Decision Models | Frozen Qwen3.5-4B: accuracy 70.96%→84.38% with gated, interruptible reasoning |  |
| [2610.20951](https://arxiv.org/abs/2610.20951) | 10-14 | LEV: Looped Decision Models | Re-running layers: 2.6B goes 63.2%→76.2% on JevBench from depth 1 to 4 |  |
| [2610.22131](https://arxiv.org/abs/2610.22131) | 10-15 | Intern-Decision | 0.8B/2B/4B multimodal models, one decision slot per field; 4B 90.02% avg vs hosted Jev 88.74% over 7 suites (author-built suites) |  |
| [2610.11316](https://arxiv.org/abs/2610.11316) | 10-08 | MetaEncoder: Bi-Encoders for Multimodal System One Decisions | Natural-language interface; bi-encoder scales to millions of candidates |  |
| [2610.18615](https://arxiv.org/abs/2610.18615) | 10-13 | VideoJev | Shared head over temporal intervals/options; cached visual state across queries |  |
| [2610.22276](https://arxiv.org/abs/2610.22276) | 10-15 | MJev-Spatial | Candidates scored by backbone query/key projections, no new parameters |  |
| [2610.21614](https://arxiv.org/abs/2610.21614) | 10-15 | Qwen-Audio-Jev | Audio decision head with CHOICE/NOUL/SCORE: MMAU-mini 78.70%, VoxCeleb1-O EER 6.50% |  |
| [2610.22401](https://arxiv.org/abs/2610.22401) | 10-14 | ASOM: Audio System One Model | 6.2M reader on frozen encoders; beats best of 6 zero-shot audio LMs by 0.072 |  |
| [2610.17113](https://arxiv.org/abs/2610.17113) | 10-12 | Calibrated Typed Decisions for Entity, Relation, Event Extraction (CalOn) | 0.6B encoder, extraction with type definitions |  |
| [2610.15742](https://arxiv.org/abs/2610.15742) | 10-11 | RSAJEV: Abstaining Prototype Memory for Remote Sensing | Letter binding fails out of vocabulary (7.35–96.40%; AUROC 0.38 on open set); training-free abstaining prototype memory |  |
| [2609.39111](https://arxiv.org/abs/2609.39111) | 09-30 | Bongard: Training Machine Intuition | (Sept., missed earlier.) Open 4B-4B encoder-decoder; many judgments from one reading of state; held-out rephrasing 75.7%→85.9% |  |

## Agents and systems (11)

| arXiv | Date | Title | Finding | Card |
|---|---|---|---|---|
| [2610.21411](https://arxiv.org/abs/2610.21411) | 10-15 | Jev-LiteMAS | Routing and review are 31.7–43.5% of generative tokens in three MAS frameworks; Jev replaces them with planning/review gaps bridged by LLM |  |
| [2610.19596](https://arxiv.org/abs/2610.19596) | 10-14 | JevCoder | Which repair decisions to delegate to a cheap judge; 400 SWE tasks, three repair models |  |
| [2610.18326](https://arxiv.org/abs/2610.18326) | 10-13 | Jev-Guard | Guardrail+policy router: 93.72% safety accuracy, 58 ms, 93.10% routing accuracy on 7,033 cases (author-built) |  |
| [2610.23804](https://arxiv.org/abs/2610.23804) | 10-16 | Jarvis: Coordination for Agentic Interactive Models | Typed decision picks operations on live task records; code validates versions |  |
| [2610.20927](https://arxiv.org/abs/2610.20927) | 10-14 | Source-Judged Compaction | Jev scores each summary entry for a source in the environment; removes unsupported entries |  |
| [2610.18780](https://arxiv.org/abs/2610.18780) | 10-13 | BLADE: Auditing Information Use for Failure Attribution | Jev dependency probabilities pick handoffs to audit |  |
| [2610.18272](https://arxiv.org/abs/2610.18272) | 10-13 | JevGPT: Thinking Fast and Slow in Autonomous Research | System One judges sources in parallel under a System Two planner |  |
| [2610.22588](https://arxiv.org/abs/2610.22588) | 10-15 | SAG2: Embedding-Free Multi-Hop Retrieval with BM25 and JEV | Recall@10 86.62/97.43/99.00 on MuSiQue/2Wiki/HotpotQA subsets |  |
| [2610.21046](https://arxiv.org/abs/2610.21046) | 10-14 | PremiseCheck | LLM splits review comments into premises; a decision model checks each: ~GPT-5.5 accuracy at about half cost |  |
| [2610.17727](https://arxiv.org/abs/2610.17727) | 10-13 | SkillScreen | Compact decision model: 20–25% of benign skills flagged at 99% recall on unseen attacks; unfamiliar benign sources raise false positives |  |
| [2610.16967](https://arxiv.org/abs/2610.16967) | 10-12 | Proactive Physical AI (StreamingJev) | Jev-style timing model decides whether/when to intervene from video |  |

## Domain applications (4)

| arXiv | Date | Title | Finding | Card |
|---|---|---|---|---|
| [2610.19478](https://arxiv.org/abs/2610.19478) | 10-13 | AgriJev | Adapted Qwen3.5 0.8–9B; 9B 75.44% mean over 17 views, +5.89 over original generator, narrows gap to hosted Jev |  |
| [2610.15029](https://arxiv.org/abs/2610.15029) | 10-10 | Toward System One Clinical Intelligence | QLoRA on Clef-Flash 9B: 95.42% on Symptom2Disease vs 61.67% remote zero-shot |  |
| [2610.15710](https://arxiv.org/abs/2610.15710) | 10-11 | Suggested Is Not Superseded: Memory-Retirement Gate | Pre-registered: binary gate retires 39.2% of claims whose change is only suggested; three-way cuts to 15.5% at a 15.3-pt detection cost |  |
| [2610.22407](https://arxiv.org/abs/2610.22407) | 10-14 | Adaptive, Survey-Aligned Simulated Urban Mobility (generative agents) | 15 decision models/LLMs compared in a Toulouse mobility simulation (abstract only) |  |

## Populations and simulation (adjacent, 1; see also the survey-respondent paper 2610.14912 and urban mobility 2610.22407 above)

| arXiv | Date | Title | Finding | Card |
|---|---|---|---|---|
| [2610.14449](https://arxiv.org/abs/2610.14449) | 10-09 | Jevolution | Instrumented spatial predator-prey framework (ODD) with asynchronous requests, Jev controlling both species; synthetic fixtures validate software, not intelligence |  |


## Non-arXiv sources (secondary coverage; vendor claims)

| Source | Date | What | Evidence status |
|---|---|---|---|
| Cloudflare Clef (27B) and Clef-flash (9B) | 2026-10-01 | Apache-2.0 open-weight decision models on Qwen3.8-27B / Qwen3.5-9B, Jev-compatible API; sorts options in release code per 2610.19536 | Launch coverage only; the reported Clef-flash CLINC150+OOS macro-F1 66.8 vs Clef 97.4 and 38.8 ms latency are vendor/secondary. Independent use: 2610.19536, 2610.15029, 2610.13675 |
| Amazon Strands Decider 2B | 2026-10-01 | Open Apache-2.0 2B decision model (Qwen3.5-2B pointer head) from Strands Labs | Press and blog coverage; JevBench figures disagree between sources (≈72% vs ≈76% for a rival). An independent order result exists in a populations card of recent_study (0.59→0.38 shuffled) |
| Independent evaluation by Deußer et al. (2609.37647), radiology report study (2609.27607) | Sept. | Already in recent_study / close/jev.md | Not new |
