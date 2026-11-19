# Case catalogue

Step 3 deliverable. Compiled 2026-10-06 from the 55 case cards in [evidence/](evidence) (54 distinct cases: S-04 and M-01 are the same source, Kim et al. 2025, counted once; M-01 is the cross-reference). Cards hold the ten required fields, with source claims, lab observations and inference marked apart. This table is a summary: read the card before relying on a row.

Legend.
- **Mechanism:** *Absorb* (errors dilute or cancel), *Correct* (system-level detection, bounds or repair), *Variab.* (variability used constructively), *Steer* (a bias shifts aggregate behaviour), *Bound* (the source mainly shows where a mechanism fails or what limits it).
- **Evidence:** T theorem; Sim controlled simulation; Emp empirical study; Impl evaluated implementation; Anec anecdote.
- **Jev relevance** (plan field 9): **Direct** directly demonstrated with decision models; **Analog** mechanistically analogous; **Spec** speculative. No card is rated Direct for Jev's own readouts; where a card says "directly demonstrated" it means for generative LLMs, which is a different readout (see the cards).

## A. Statistics and collective judgement

| ID | Case (source, year) | Mechanism | Evidence | Principal limitation / negative result | Jev |
|---|---|---|---|---|---|
| [S-01](evidence/stats-and-reliable-computation.md) | Condorcet jury theorem and its independence assumptions (Dietrich and Spiekermann 2013) | Absorb, Bound | T | If problems are easy or hard for all voters, majority accuracy tends to Pr(easy), not 1; reliability can fall with group size when competence is not homogeneous | Analog (binary factual only) |
| [S-02](evidence/stats-and-reliable-computation.md) | Social influence and wisdom of crowds (Lorenz et al. 2011; Becker et al. 2017) | Bound | Emp (humans) | Showing others' answers shrinks diversity and raises confidence; numeric estimates of obscure quantities; decentralised networks can still help (Becker, abstract only) | Analog |
| [S-03](evidence/stats-and-reliable-computation.md) | Ensemble ambiguity identity (Krogh and Vedelsby 1995) | Absorb | T (identity) | Gain equals disagreement; identical members add nothing; squared error on regression, not argmax choices | Analog if scores averaged |
| [S-04 / M-01](evidence/stats-and-reliable-computation.md) | Correlated errors across 349 LLMs (Kim et al. 2025) | Bound | Emp | Agreement on mutual errors 0.60 (Helm) vs 1/3 chance; more accurate models more correlated; shown for generative LLMs, not label-scoring readouts | Analog (Direct for generative LLMs only) |
| [S-05](evidence/stats-and-reliable-computation.md) | Nine LLM judges, about two effective votes (Kohli 2026, preprint) | Absorb, Bound | Emp | Panel accuracy below the independence ideal; best single judge matches the panel; single author, snapshot | Analog (gives a measurement method) |
| [S-06](evidence/stats-and-reliable-computation.md) | Consensus is not verification (Denisov-Blanch et al. 2026, preprint) | Bound | Emp | Polling-style aggregation shows no consistent gain even at 25x cost; binary questions with verbalised confidence | Analog |
| [S-07](evidence/stats-and-reliable-computation.md) | Self-consistency (Wang et al. 2023) | Variab. + Absorb | Impl | GSM8K +17.9 points; near-null on some tasks; 5–40x cost; needs a unique extractable answer | Analog (factual tasks) |

## B. Reliable computation and communication

| ID | Case | Mechanism | Evidence | Principal limitation | Jev |
|---|---|---|---|---|---|
| [S-08](evidence/stats-and-reliable-computation.md) | von Neumann multiplexing and noisy-gate thresholds (Evans-Schulman; Unger) | Correct | T | Gate-error thresholds (1/6 for 3-input majority formulas; about 0.0886 for 2-input) assume independent faults and a fixed function; not decision-accuracy targets; above threshold redundancy fails | Analog |
| [S-09](evidence/stats-and-reliable-computation.md) | Noisy-channel coding theorem (Shannon 1948) | Correct | T | Needs an explicit code and channel model; a semantic action has no sender-side encoding | Spec |
| [S-10](evidence/stats-and-reliable-computation.md) | Reliable cellular automata (Gács 2001) | Correct | T | Bounded small fault probability; hierarchical repair; abstract and noise model read only | Spec |
| [S-11](evidence/stats-and-reliable-computation.md) | N-version programming with coding agents (Ron, Baudry, Monperrus 2026, preprint) | Absorb, Bound | Impl | 429 coincident failures vs 115.36 expected under independence; 3-version majority cut mean failures from 387.44 to 130.99; failures cluster where the spec is ambiguous | Analog |

## C. Distributed systems and control

| ID | Case | Mechanism | Evidence | Principal limitation | Jev |
|---|---|---|---|---|---|
| [C-01](evidence/control-and-collective-behaviour.md) | Byzantine Generals (Lamport, Shostak, Pease 1982) | Correct | T | Needs more than 3m of n for m arbitrary faults; reliable links, known m, synchrony; adversarial worst case, not 10–20% errors | Analog (baseline) |
| [C-02](evidence/control-and-collective-behaviour.md) | W-MSR resilient consensus (LeBlanc et al.) | Absorb, Correct | T | Primary paper not opened (secondary restatements); scalar numeric states; bound F on faulty neighbours; leaders do not guarantee the consensus value | Analog |
| [C-03](evidence/control-and-collective-behaviour.md) | Noisy-link average consensus (Kar and Moura 2008) | Absorb | T + numeric | Bias-variance trade-off; additive zero-mean noise, continuous states | Analog |

## D. Collective behaviour and agent-based models

| ID | Case | Mechanism | Evidence | Principal limitation | Jev |
|---|---|---|---|---|---|
| [C-04](evidence/control-and-collective-behaviour.md) | Vicsek model, noise-driven transition (Vicsek 1995; Grégoire and Chaté 2004) | Absorb, Bound | Sim | Order lost above a noise threshold; transition later found discontinuous; noise does not help here | Analog |
| [C-05](evidence/control-and-collective-behaviour.md) | Informed minority steers a group (Couzin et al. 2005) | Steer | Sim | Abstract only; failure modes not seen | Analog |
| [C-06](evidence/control-and-collective-behaviour.md) | Uninformed individuals and democratic consensus (Couzin et al. 2011) | Steer, Bound | Theory + fish experiment | Abstract only; "wide range of conditions", not all | Analog |
| [C-07](evidence/control-and-collective-behaviour.md) | Fish school gradient sensing (Berdahl et al. 2013) | Absorb | Emp + model | Abstract only | Analog / Spec |
| [C-08](evidence/control-and-collective-behaviour.md) | Honeybee nest-site choice (List, Elsholtz, Seeley) | Absorb, Bound | Sim | Needs independent assessment plus interdependent recruitment; without independence cascades | Analog |
| [C-09](evidence/control-and-collective-behaviour.md) | Noise in small groups under correlated cues (Kao and Couzin 2014) | Variab. | T (analytic model) | Benefit only when correlated and independent cues mix; binary choice, majority rule; no experiment | Analog |
| [C-10](evidence/control-and-collective-behaviour.md) | Schelling segregation (Gauvin 2009; Xu, Clark, Pak 2024; Hatna and Benenson 2012) | Steer, Bound | Sim | Mild preferences give sharp thresholds; 5–10% random movers change outcomes (Xu et al.); empirical validity contested | Analog |
| [C-11](evidence/control-and-collective-behaviour.md) | Random neighbour choice and cohesion (Jadhav, Guttal, Raj 2021, preprint) | Variab. | Sim | Benefit tied to cohesion objective, topological neighbourhood | Analog / Spec |
| [C-12](evidence/control-and-collective-behaviour.md) | Predator evasion and criticality (Klamser and Romanczuk 2021) | Absorb, Bound | Sim | The critical state is evolutionarily unstable; prey–predator geometry | Spec |

## E. Game theory and social choice

| ID | Case | Mechanism | Evidence | Principal limitation | Jev |
|---|---|---|---|---|---|
| [G-01](evidence/game-theory-and-stochastic-optimisation.md) | Quantal response equilibrium (McKelvey and Palfrey; Goeree, Holt, Palfrey; Haile et al.) | Steer | T + experimental fit | Without distributional restrictions a QRE fits any behaviour; McKelvey–Palfrey 1995 itself not opened | Analog (softmax over scores) |
| [G-02](evidence/game-theory-and-stochastic-optimisation.md) | Mutations and stochastic stability (Kandori, Mailath, Rob 1993) | Variab. (equilibrium selection) | T | 2×2 symmetric games; selects risk-dominant equilibrium, not necessarily welfare-best | Analog |
| [G-03](evidence/game-theory-and-stochastic-optimisation.md) | Informational cascades (Bikhchandani, Hirshleifer, Welch 1992) | Bound | T + anecdote | Correct-on-average private signals still lock into wrong cascades; cascades fragile to new public information | Analog |
| [G-04](evidence/game-theory-and-stochastic-optimisation.md) | Cascades in the laboratory (Anderson and Holt) | Bound | Emp (humans) | Reverse cascades 13/41 and 18/46 in two designs (PDF version read; a search summary quoted other totals); small groups | Analog |
| [G-05](evidence/game-theory-and-stochastic-optimisation.md) | Noisy voters as estimators (Conitzer and Sandholm; Caragiannis, Procaccia, Shah) | Absorb | T | Factual voting only; independent votes; rule choice matters (plurality exponentially worse under Mallows noise) | Analog |
| [G-06](evidence/game-theory-and-stochastic-optimisation.md) | Correlated votes and the jury theorem (Kaniovski) | Bound | T | Positive correlation lowers group competence; draft, partial read | Analog |
| [G-07](evidence/game-theory-and-stochastic-optimisation.md) | MusicLab (Salganik, Dodds, Watts 2006) | Bound (variability from dependence) | Emp (online) | Influence raised inequality and unpredictability; no benefit measured | Analog |

## F. Stochastic optimisation and learning

| ID | Case | Mechanism | Evidence | Principal limitation | Jev |
|---|---|---|---|---|---|
| [G-08](evidence/game-theory-and-stochastic-optimisation.md) | Simulated annealing (Hajek 1988) | Variab. | T | Needs a cooling schedule tuned to landscape depth; constant noise has no guarantee | Analog (temperature) |
| [G-09](evidence/game-theory-and-stochastic-optimisation.md) | Thompson sampling vs greedy and epsilon-greedy (Russo et al.) | Variab. | Sim + tutorial | Structured randomisation beats uniform dithering; needs reward feedback and calibrated uncertainty | Analog |
| [G-10](evidence/game-theory-and-stochastic-optimisation.md) | Stochastic resonance (Gammaitoni et al. 1998) | Variab. | Review | Requires a threshold, a weak signal and noise; partial read | Spec |
| [G-11](evidence/game-theory-and-stochastic-optimisation.md) | Gradient noise for deep networks (Neelakantan et al.) | Variab. | Emp | Null result with good initialisation; training-time only | Analog at most |
| [G-12](evidence/game-theory-and-stochastic-optimisation.md) | Noisy SGD escapes saddles (Ge et al. 2015) | Variab. | T | Strict-saddle functions; local minimum only | Spec |
| [G-13](evidence/game-theory-and-stochastic-optimisation.md) | Dropout (Srivastava et al. 2014) | Variab. | Emp | Noise removed at deployment; 2–3× training time | Weak |

## G. Modern AI and multi-agent systems

| ID | Case | Mechanism | Evidence | Principal limitation | Jev |
|---|---|---|---|---|---|
| [M-02](evidence/modern-ai-and-games.md) | Panel of LLM evaluators, PoLL (Cohere 2024) | Absorb | Emp (vendor) | Three settings; vendor's own model on the panel; independence assumed by design | Analog |
| [M-03](evidence/modern-ai-and-games.md) | Debate or Vote (2025; Smit et al.) | Absorb | Emp + T | Voting accounts for most of the gain attributed to debate; says nothing about shared bias | Analog |
| [M-04](evidence/modern-ai-and-games.md) | 12-LLM forecasting ensemble vs 925 humans (Science Advances 2024) | Absorb | Emp | 31 questions; Brier score; ensemble statistically indistinguishable from human crowd | Analog |
| [M-05](evidence/modern-ai-and-games.md) | Silicon samples (Argyle et al.) | Bound (validity) | Emp | Needs real respondent conditioning; later work fails to reproduce the fidelity | Spec |
| [M-06](evidence/modern-ai-and-games.md) | LLMs flatten and misportray identity groups (Wang et al.) | Bound | Emp (3,200 humans) | Temperature reaches human diversity only at 1.4, where text is incoherent | Analog |
| [M-07](evidence/modern-ai-and-games.md) | Whose opinions do LMs reflect (Santurkar et al.) | Bound | Emp | An aligned model puts more than 0.99 probability on one option; bears on calibration for sampling | Analog |
| [M-08](evidence/modern-ai-and-games.md) | LLM agents voting in participatory budgeting (Yang et al.) | Variab., Bound | Emp vs human experiment | Temperature trades diversity against human alignment; order and ID effects; preference aggregation | Analog |
| [M-09](evidence/modern-ai-and-games.md) | Generative Agents (Park et al. 2023) | Correct (architecture) | Impl | 25 agents, two days; over-cooperation, norm errors | Analog |
| [M-10](evidence/modern-ai-and-games.md) | OASIS (large social simulation) | Bound | Impl (self-evaluated) | About 30% normalised error; herding stronger than humans; effect only at 10,000 agents not 100 | Analog |
| [M-11](evidence/modern-ai-and-games.md) | Robustness of LLM social simulations (Ye et al. 2026, preprint) | Bound | Sim | Persona wording shifted cooperation by up to 76 points in one model and 1 in another | Analog |
| [M-12](evidence/modern-ai-and-games.md) | Project Sid (Altera) | Correct (feedback modules) | Impl (vendor report) | Preliminary; vendor's own product | Analog |

## H. Games and interactive simulation

| ID | Case | Mechanism | Evidence | Principal limitation | Jev |
|---|---|---|---|---|---|
| [M-13](evidence/modern-ai-and-games.md) | BotPrize 2010 (Karpov et al.) | Correct (fault removal) | Emp | Stuck bots identified as bots; qualitative; competing team | Analog |
| [M-14](evidence/modern-ai-and-games.md) | Maia chess (McIlroy-Young et al. 2020) | Bound | Emp | Weakened engines do not reproduce human-style mistakes (depth-limited Stockfish matches 33–41% of human moves vs Maia above 52%); no enjoyment study | Analog |
| [M-15](evidence/modern-ai-and-games.md) | Human-likeness of navigation agents (CHI 2023) | Correct (fault removal) | Emp (humans) | Jerky agents judged non-human; authors built the agents | Analog |
| [M-16](evidence/modern-ai-and-games.md) | Hamlet dynamic difficulty (Hunicke and Chapman 2004) | Steer | Design description | No evaluation | Spec |
| [M-17](evidence/modern-ai-and-games.md) | Suboptimal guard AI thesis (2026, unreviewed) | Variab. (test) | Emp, n=10 | Mean survival 29.5 s (optimal) vs 31.1 s (suboptimal); capture 59.2% vs 60.8%: a weak null; no significance tests extracted | Spec |
| [M-18](evidence/modern-ai-and-games.md) | XCOM hit chance (Solomon 2016 interview) | Steer | Anec | One designer; fetch summary only | Spec |
| [M-19](evidence/modern-ai-and-games.md) | Left 4 Dead AI Director (Booth 2009) | Variab. + Steer | Anec | No player data | Spec / Analog |

## Counts

| Mechanism (primary tag) | Cases |
|---|---|
| Absorb | S-01, S-03, S-05, S-07, S-11, C-02, C-03, C-04, C-07, C-08, C-12, G-05, M-02, M-03, M-04 (15) |
| Correct | S-08, S-09, S-10, C-01, M-09, M-12, M-13, M-15 (8) |
| Variab. | C-09, C-11, G-02, G-08 to G-13, M-17 (and M-08, M-19 in part) (9–11) |
| Steer | C-05, C-06, C-10, G-01, M-16, M-18 (6) |
| Bound (mainly a failure or limit) | S-02, S-04, S-06, G-03, G-04, G-06, G-07, M-05, M-06, M-07, M-10, M-11, M-14 (13) |

Takeaways for step 4 (inferences, to be tested against the cards there):
- Cases supporting *variability helps* with a no-noise comparison inside the source are few: C-09, C-11 (models), G-08 to G-10 (physical or optimisation settings, narrow conditions), G-11 (null with good initialisation). Only M-17 tests it with players, and it is a weak null.
- The measured LLM populations (S-04 to S-06, S-11, M-01, M-06, M-07, M-10, M-11) mostly document correlation and homogenisation, not independence.
- Absorption results hold under stated independence or diversity; steering and cascade results show how a weak bias or imitation changes aggregates.
- No card measures a Jev-style readout in a population, and none measures a sampling-versus-argmax comparison in an interactive agent population.
