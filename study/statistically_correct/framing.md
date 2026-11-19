# Framing: concepts, local leads and unresolved assumptions

Step 1 of [plan.md](../../devdocs/episodes/study/statistically_correct/plan.md). Written 2026-10-06. Local reports below are used as leads and background for the literature questions, not as verified external facts, and no new measurement was made. An exhaustive audit of local experiments was not attempted (see "Scope of the inventory").

## 1. What the local material says

| Local source | What was measured | Model / readout | Isolated or closed loop | Untested |
|---|---|---|---|---|
| [Werewolf voting](../game/examples/jev-werewolf.md) (author results, repo not re-run) | Per-player deception probability; villagers win 50% [36, 64] with Jev-batched deciding the vote vs 24% random votes and 12% local llama judge (50 games per condition). Human games: no judge clearly useful; Jev ECE 0.41–0.56 on spoken Werewolf | Hosted Jev `jev-1.13.0`; llama3.1:8b baseline | Isolated per-view judgements plus a live game in which the top suspect is voted out (a closed loop, but one decider, not a population) | Population of many deciders; error dependence between deciders; transfer from LLM-written to human games (the signal largely did not) |
| [JEVfire village](../game/examples/jevfire-village.md) (author claims, demos not played) | Latency (71 ms per action in one demo). Author statements: "a legal choice can still get a villager killed"; prompts express intended strategy, not guaranteed behaviour | Qwen3.5 0.8B, label scoring | Closed loop (six villagers, round-robin) | No quantitative result on village outcomes or on how well player policy is followed |
| [Hype and reality](../hype_and_reality/README.md) | Literature plus local failure classes: off-topic input accepted as an option, injected text, order and context effects, confident wrong answers (local error-ranking AUC 0.73) | Encoders (jeff, Laya) and logit readers | Isolated questions | Failures by model size; behaviour when decisions feed back into the next state |
| [game_test/p2 report](../../devdocs/episodes/game_test/p2/report.md) (local) | One decision per written order: 86% vs 53% keyword baseline on clear-intent orders, 83.3% on the formal held-out set (gate 85%); non-orders handled without cost 75% (gate 80%); never turned a real order into a different job | jeff (GLiFormer, about 575M) | Isolated, single decision per order | Repeated play; many agents; Japanese (13/18 → 5/18 with Japanese options) |
| [Prompt best practice](../prompt_best_practice/README.md) | Source study: order bias is largely an option-ID prior; voting over orders gives a few points; correlated errors limit unweighted votes; models answer rather than abstain | Mostly generative LLMs; lab readouts differ (W12, A27 letter logits; K27 pointer head) | Isolated questions | Nothing on pointer or encoder readouts |
| [Benchmark foundations](../benchmark/README.md) | Evaluation concepts (metrics, data validity, statistics, robustness) | — | — | — |

Observations that matter for this survey:

1. **No local result measures error structure across agents.** Every number above is a per-question accuracy, a calibration figure or a single-decider game outcome. None says whether errors are independent across states, agents or time.
2. **The only closed-loop evidence is weak or anecdotal.** The Werewolf win rates concern one decider; JEVfire has no outcome measurement.
3. **Local reports stress structured failures** (injected text, order prior, off-topic input, confident wrong answers, language shift). These are state-dependent errors, which is the case where simple "independent 10–20% noise" results fail. This is a lead for Q6, not a finding.
4. **Benchmark accuracy is not carried into any simulator** in this survey. Where the 80–90% figure appears it is only the design scenario of the [brief](../../devdocs/episodes/study/statistically_correct/braindump.md).

## 2. Operational definitions

These are the definitions used to compare sources. Each source's own definition is recorded on its case card; where it differs, the card says so.

**Individual decision quality.** A property of a decision rule on a defined input distribution, with a defined reference. Four reference types are kept apart:
- *Ground truth* (a fact with a unique answer: is the defendant guilty, is the predator on the left).
- *Reference policy* (what an expert, optimal controller or a larger model would do). Agreement with it is not correctness unless the reference is itself validated.
- *Preference* (a choice that is right for that agent's interests; no shared truth).
- *Distributional* (the population of choices matches a population of humans or a target mixture; accuracy per item is not the criterion).

**Error** (Q1). The survey uses five categories and records which a source means:
1. *Task error*: departure from ground truth or a validated reference.
2. *Preference difference*: disagreement caused by different interests; not an error in the aggregate sense.
3. *Uncertainty*: the decider cannot tell; an honest probability near 0.5 is not an error.
4. *Deliberate randomisation*: a designed policy that samples actions (mixed strategies, epsilon-greedy, softmax). Not a fault.
5. *Invalid action*: outside the legal set or format. Usually removable by constraints and distinct from a wrong legal action.

**Noise versus structured error.** *Independent noise*: errors independent across agents and time given the true state. *Structured error*: shared across agents (same model, same prompt, same observation), state-dependent (fails in particular situations), subgroup-specific, or temporally persistent (the same agent repeats it). The same error rate has very different aggregate effects in the two cases.

**Collective outcome.** A quantity defined at system level: group accuracy, survival or escape, resource allocation, welfare, diversity of behaviour, player-experienced quality. Local accuracy and collective outcome are different variables; the relation between them is what the survey examines.

**Statistical bias (as a steering tool).** A systematic shift in the probability of an action that is applied on purpose (a score, a temperature, a prior) and that changes aggregate behaviour without fixing any single choice. Distinguish *argmax selection* (deterministic) from *sampling from scores* (stochastic policy); a model's reported confidence is not an empirical error rate unless calibrated on the relevant distribution.

**Error correction.** Any mechanism that lowers the effect of local errors on the outcome without improving the local decider: redundancy and aggregation, constraints on the action set, environmental feedback, recovery or rollback, selective escalation. Each has a cost (extra decisions, communication, latency, supervision). The survey groups these as *absorb* (errors dilute or cancel) and *correct at system level* (errors are detected or bounded).

**Constructive variability.** Variability that improves an outcome measured against a no-variability comparison: exploration, escape from lock-in, behavioural diversity, unpredictability, perceived entertainment. Entropy, surprise or diversity alone is not benefit. "Works despite errors" and "works better because of variability" are recorded as separate claims.

## 3. How disciplines define correctness and usefulness

Initial map, to be checked against sources in steps 2–3 (this is expectation, not a finding):

| Field | Typical meaning of "correct" | Typical meaning of "useful" | Cases without unique correct action |
|---|---|---|---|
| Statistics, collective judgement | Match to a true value or binary truth | Error of the aggregate, calibration | Preferences treated separately (social choice) |
| Reliable computation | Output equals the fault-free output | Failure probability bounded under a fault model | Not applicable; function specified in advance |
| Distributed systems, control | Agreement or convergence; stability | Bounded deviation, recovery time | Consensus on any value within bounds |
| Collective behaviour, ABMs | Often no ground truth; match to observed pattern | Emergent pattern (polarisation, escape, segregation) | Central: the pattern, not the individual move, is evaluated |
| Game theory, social choice | Best response, equilibrium | Equilibrium or welfare under noise | Central: no unique action, mixed strategies |
| Stochastic optimisation | Reaches a good optimum | Final objective value versus compute | Randomness is part of the method |
| Modern AI, multi-agent | Benchmark label; human-likeness | Task score; distributional fidelity | Synthetic populations: fidelity is the criterion |
| Games, simulation | Rarely defined | Player experience, believability | Central: usefulness is perceived, not computed |

## 4. Unresolved assumptions

These are not assumed anywhere in the survey and are carried as open items to be resolved or labelled in later steps.

| ID | Assumption | Where it matters | Status |
|---|---|---|---|
| A1 | The "80–90% accuracy" scenario corresponds to some defined error type | Q1, Q2 | Unspecified in the brief; treated as a scenario, not a threshold |
| A2 | Errors of one model repeated across many agents are independent | Q2, Q6 | Not assumed; the survey asks what is known about dependence |
| A3 | Model probabilities are calibrated and usable for sampling | Q5 | Local evidence points the other way (confident wrong answers; ECE 0.41–0.56 in one case) |
| A4 | Model choices resemble human choices | Q7 | Local Werewolf evidence shows transfer failure from LLM-written to human games |
| A5 | Randomness is desirable for entertainment | Q4 | Needs player studies; not assumed |
| A6 | A convergent result (theorem or simulation) applies to semantic decisions | Q2, Q3 | Many theorems assume binary, independent or explicit encodings; check per case |
| A7 | Benchmark accuracy on isolated questions predicts behaviour in a closed loop | Q6 | No local evidence; keep separate |
| A8 | A reference policy is the correct action | Q1 | Agreement with a reference is recorded as agreement only |

## 5. Scope of the inventory

Read for this step: the five study notes in the table above and the game_test/p2 final report. Not re-read: the experiment sets (`devdocs/episodes/experiments/`), benchmark episodes and game_test/p1, because the plan only asks for background; their relevance to error structure will be checked if a source in steps 2–4 points to a specific local question.
