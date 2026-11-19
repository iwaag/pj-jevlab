# Synthesis: useful collective behaviour from imperfect decisions

Step 5 deliverable. A reading of the collected literature, written to stand on its own as a survey. Evidence is in the cards ([evidence/](evidence), IDs S-, C-, G-, M-), the table in [catalog.md](catalog.md) and the conditions in [mechanisms.md](mechanisms.md). Compiled 2026-10-06. **[Source]** marks what a source reports; **[Inference]** marks this survey's reading. Numerical tolerances stay with their original settings.

## 1. One question, several literatures

The brief asks whether a decision system that is right 80–90% of the time can still yield a good whole, and whether the remaining 10–20% can help. The literatures that touch this are not asking the same thing. Four different questions are mixed under the heading "imperfect individuals, good collective":

1. **Truth estimation.** Many deciders estimate one fact. Error is departure from the fact; aggregation is the tool (Condorcet and its descendants S-01, G-05; ensembles S-03; LLM panels S-05, M-02, M-04).
2. **Reliable computation.** A system must compute a fixed function from unreliable parts. Redundancy and encoding are the tools (von Neumann, Shannon, Gács: S-08 to S-10; Byzantine agreement C-01).
3. **Emergent pattern.** There is no true answer for an individual move; the pattern (flocking, segregation, cohesion, cascades) is what is assessed (C-04 to C-12, G-03, G-07).
4. **Search and exploration.** Randomness is a tool for finding good options (annealing, bandits, resonance: G-08 to G-10).

A fifth strand asks whether artificial agents resemble people (silicon samples M-05 to M-08, social simulations M-09 to M-12, game bots M-13 to M-15). **[Inference]** The same words, "noise", "error", "diversity", carry different meanings across these, and many apparent conflicts between sources dissolve once the question is identified (mechanisms.md section 3).

## 2. Established results

These are results the sources prove or measure in their stated settings.

**Aggregation reduces independent error and cannot remove shared error.** The ensemble identity (S-03) says ensemble error is mean member error minus disagreement, so a million copies of one network add nothing. The jury theorem family (S-01, G-06) gives growth in accuracy with group size for independent voters better than chance, and the generalisations show that positive correlation lowers competence, that bigger groups can be worse up to some size, and that if a problem is easy or hard for every voter the majority tends to Pr(easy), not to 1. Noisy-voter theory (G-05) shows that the rule matters: plurality needs exponentially many samples under one noise model where pairwise-majority-consistent rules need few.

**Redundancy corrects errors only with an error model and an encoding.** Noisy-gate computation tolerates gate error below stated thresholds (about 1/6 for three-input majority formulas, about 0.0886 for two-input, S-08) for independent faults in a fixed function, and Shannon's theorem (S-09) gives reliability below channel capacity by explicit coding. Byzantine agreement (C-01) needs more than two thirds loyal for oral messages. All of these are worst-case or assumption-bound; none says what accuracy a semantic decider needs.

**Imitation and social information can erase the diversity that aggregation uses.** Showing people each other's estimates narrowed diversity and raised confidence without improving accuracy in one experiment (S-02, with a network qualification from Becker et al.); informational cascades can lock a population in a wrong choice even when every private signal is correct on average (G-03); the laboratory finds them, with heuristics and small groups, in a share of sessions (G-04); in an artificial music market social influence raised inequality and unpredictability (G-07).

**Weak local biases can steer aggregates, with thresholds.** Mild preferences give strong segregation, with sharp transitions (C-10); an informed minority can lead a group (C-05), and uninformed members can return control to the majority (C-06); noise destroys alignment above a threshold in the Vicsek model (C-04).

**Variability helps in structured, narrow settings.** Annealing converges to global minima with a cooling schedule tuned to landscape depth (G-08); Thompson sampling beats greedy and uniform dithering in a bandit with a well-specified prior (G-09); small groups can beat large ones under partly correlated cues (C-09); random neighbour choice increases cohesion in a flocking model (C-11); stochastic resonance needs a threshold, a weak signal and noise (G-10).

**Measured LLM populations show strong dependence.** Different LLMs agree on 0.60 of mutual errors in one dataset against 1/3 chance, and more accurate models are more correlated (S-04/M-01); nine LLM judges carry about two effective votes (S-05); polling-style aggregation shows no consistent gain on binary truthfulness questions (S-06); coding agents show 429 coincident failures against 115.36 expected under independence, yet a three-version majority cuts mean failures from 387.44 to 130.99 (S-11). Panels of different families can match one large judge at lower cost (M-02), and a 12-model ensemble matched a human crowd on 31 forecasting questions (M-04).

## 3. Conditional findings and counterexamples

- **Whether aggregation helps depends on the task.** Gains are large where a verifier exists or samples differ (self-consistency S-07: +17.9 points on GSM8K, 5–40x cost) and small where errors are shared (S-05, S-06). **[Inference]** The same technique can look positive or negative depending on how much of the error is shared and on whether the baseline is the average member or the best one (S-05: the best single judge matched the panel).
- **Noise helps only when structured.** G-11 reports no gain from gradient noise with good initialisation; M-17 (ten players, unreviewed) found mean survival of 29.5 s with the optimal guard against 31.1 s with the suboptimal guard, and capture rates of 59.2% against 60.8%, a weak null. G-08 shows constant noise lacks the guarantee that scheduled noise has. **[Inference]** The literature supports "structured variability under a no-noise comparison" and does not support "a fixed error rate is beneficial".
- **Phase-like behaviour.** C-04 (noise threshold), C-10 (segregation thresholds), S-08 (gate-error threshold), M-10 (herding visible at 10,000 agents and not 100): moving a single parameter can flip a collective. This helps steering and also marks the tipping points to avoid.
- **Structure of error matters more than its rate.** Maia (M-14) finds that weakened engines do not reproduce human-style mistakes: depth-limited Stockfish matches human moves 33–41% against Maia's above 52%. BotPrize bots were identified when they got stuck (M-13), and jerky navigation agents were judged non-human (M-15). **[Inference]** These support the framing distinction between random noise and state-dependent error: mistakes that are state-dependent and legible read differently from random-looking ones.

## 4. Superficially similar claims about different phenomena

| Claim | Phenomenon A | Phenomenon B |
|---|---|---|
| "Errors average out" | Truth estimation with independent errors (S-01, S-03, G-05) | Emergent consensus on a pattern with no true answer (C-03 average consensus converges to an average, not a truth) |
| "Noise helps" | Optimisation or exploration with a schedule (G-08, G-09) | Cohesion in a flocking model (C-11), detection by stochastic resonance (G-10); not entertainment |
| "Diversity helps" | Different error patterns improve ensembles (S-03, M-02) | Different preferences or personas produce a realistic population (M-05 to M-08); success is distributional fidelity, not accuracy |
| "Temperature or sampling" | Exploration policy with calibrated uncertainty (G-09) | Diversity of generated opinions (M-06, M-07, M-08); reported confidence can be far sharper than human frequencies |
| "Voting" | Binary or ranked truth with independent voters (G-05, S-01) | Participatory budgeting among conflicting interests (M-08), where no truth exists |
| "Resilient consensus" | Bounded adversarial faults in scalar states (C-01, C-02) | Non-adversarial but correlated semantic errors |

## 5. Direct, transferable and speculative

Judged against Jev-style decision systems (typed finite choices with probabilities, readouts that differ from free-text generation). No source tests a Jev readout in a population.

**Directly demonstrated with decision models (but generative LLMs, not Jev readouts).** Correlated errors across LLMs (S-04/M-01, S-05, S-06, S-11); homogenisation and over-sharp probabilities (M-06, M-07); sensitivity of simulated macro outcomes to prompt wording (M-11); herding and scale dependence in LLM social simulation (M-10); temperature as a diversity-versus-alignment trade-off (M-08).

**Plausible transfers (mechanistically analogous).** The easy/hard structure and effective-vote measurement for aggregating many agents that share one model (S-01, S-05, G-06); cascade risk if agents see each other's decisions (G-03, G-04); structured randomisation against greedy selection (G-09, G-08); steering by weak biases with thresholds (C-10, G-01); independence-plus-interdependence designs (C-08); removing conspicuous faults and keeping state-dependent legible errors (M-13 to M-15).

**Unsupported or speculative analogies.** Reliable-computation thresholds as accuracy targets (S-08 to S-10); Byzantine bounds as accuracy requirements (C-01); stochastic resonance or criticality as a rationale for adding noise (G-10, C-12); dynamic difficulty by lowering NPC accuracy (M-16, no evaluation); designer anecdotes about hit chance and directors (M-18, M-19, no player data); any claim that randomness raises entertainment (only M-17, a weak null).

**What remains unknown (literature gaps, not an experiment programme).** Error dependence for label-scoring or encoder readouts across states and agents; how sampling from option scores behaves in an interactive population compared with argmax; whether scores are calibrated for sampling on the relevant distribution; whether players prefer deliberate mistakes over none in an adequately sized study; independent replications for most of the preprints.

## 6. Do "good enough" individual decisions have general principles?

**[Inference]** The literature supports narrower statements, not one general principle.
- There is no universal tolerable error rate. The numbers that exist (S-08 thresholds, S-05 effective votes, S-11 failure counts) belong to their settings and none concerns a decision with no unique answer.
- There are general principles about *structure*: (i) the effect of errors on the whole depends on dependence and state-dependence more than on their rate (S-01, S-03, S-04, S-05, S-11, M-14); (ii) interaction can amplify as well as absorb (G-03, G-07, C-08); (iii) variability is useful when structured and measured against a no-noise baseline (G-08, G-09, C-09); (iv) aggregate behaviour can show thresholds (C-04, C-10, S-08).
- Where a system's design has a verifier, constraints or feedback, small local errors are tolerated at a cost in extra decisions (S-07, M-12); the survey found no evidence about doing so without them.

## 7. Brief illustrations

- **A school of 300 fish or sardines.** The collective-motion results (C-04, C-05, C-07, C-11, C-12) show alignment holds below a noise level and collective sensing can arise from local interaction. They concern spatial heading rules, not model decisions; whether each decision is 80–90% correct matters less in these models than whether errors are shared and where the noise threshold lies.
- **A village voting.** If the vote is a factual estimate, the aggregation results apply conditional on independence (S-01, G-05, S-05); if it settles conflicting interests, those results do not apply, and the evidence concerns only persona diversity and its limits (M-06, M-08).

Neither example is evaluated in the literature with Jev-style decision models. No design or protocol is proposed here.
