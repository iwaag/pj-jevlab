# Case catalogue — schooling_sim

Step 3 deliverable. Compiled 2026-10-06 from the 24 cards in [evidence/](evidence). These are 22 distinct cases: SP-01 = LA-03 (Olson et al. 2013) and EC-01 = SP-04 (Rosenthal et al. 2015), each counted once below. The table is a summary; read the card before relying on a row. Cards reused from the broad survey ([statistically_correct](../statistically_correct/catalog.md)) are listed at the end and were not re-read.

## Legend

- **View:**
  - *cont/metric*: continuous positions within a radius;
  - *topo k*: the k nearest neighbours;
  - *visual*: occlusion-based;
  - *sector*: discrete angular sectors;
  - *text*: rendered as text to a language model.
- **Decision:** *cont*: continuous heading or acceleration; *disc n*: n discrete actions; *bin*: binary.
- **Noise:**
  - *ind*: independent across agents and steps;
  - *quenched*: frozen in space;
  - *model*: errors made by a learned or language model;
  - *none*: no error model.
  - "spread meas." means the spread of an action or error between agents was measured.
- **Evidence:** Sim simulation; Emp empirical; T theory; Demo demonstration without a comparison; Bench benchmark.
- **p2 relevance** (inference): **Copy** something to adopt; **Contra** contradicts or qualifies a p2 choice; **Open** leaves a p2 question untested.
- **Read:** F full text of the main sections; P partial; A abstract and introduction only.

## Schooling and predation (SP)

| ID | Case | View | Decision | Predator | Noise | Metrics | Evidence | Read | p2 relevance |
|---|---|---|---|---|---|---|---|---|---|
| [SP-01](evidence/schooling-and-predation.md) (= LA-03) | Olson et al. 2013, predator confusion evolves swarming | sector: 12 × 15°, presence bits, prey and predator layers | disc 4 (stay, forward, ±8° turn) | coevolving; P_capture = 1/A_NV | Markov-network stochasticity; clonal prey | density, nearest-prey distance, survivors; N 50, 2,000 steps, 180 replicates | Sim | F | **Copy** sector view, confusion rule, clonal agents. **Contra** evolved prey ignored the predator, and nothing grouped without confusion (70% of replicates with it, 0% without) |
| [SP-02](evidence/schooling-and-predation.md) | Olson, Knoester, Adami (preprint), with Hamilton 1971: attack mode shapes swarming | sector: 24 × 15°, 360°, torus | disc 4 from 2 binary outputs | artificial attack modes; density-dependent capture | stochastic | density thresholds 5/15; N 250, 100 replicates | Sim (T for Hamilton) | F | **Contra** with no attacks prey disperse, and the attack rule decides the outcome. **Open** an always-turning agent mills by construction |
| [SP-03](evidence/schooling-and-predation.md) | Ioannou, Guttal, Couzin 2012: real fish attack virtual prey | Couzin zones (details in the supplement, not read) | cont | real bluegill; prey cannot detect it | trait heterogeneity | attack risk, polarisation, group size; 70 attacks | Emp + Sim | F (supplement not read) | **Copy** null-predator baseline (random target at the same attack times). **Contra** protection without any reaction to the predator |
| [SP-05](evidence/schooling-and-predation.md) | Reynolds 1987, Boids | cont/metric, spherical zone | cont, prioritised acceleration | none | none | none (visual validation only) | Demo | F | **Copy** strict priority among rules, which is the precedent for p2's rule; averaging opposite urges cancels them |

## Metrics and protocols (MP)

| ID | Case | View | Decision | Predator | Noise | Metrics | Evidence | Read | p2 relevance |
|---|---|---|---|---|---|---|---|---|---|
| [MP-01](evidence/metrics-and-protocols.md) | Couzin et al. 2002, zonal model, collective memory | cont/metric zones, blind volume | cont, max turn per step | none | ind Gaussian (σ ≤ 0.2 rad), plus fixed per-agent traits | p_group, m_group, fragmentation; N 100, 30 replicates, hysteresis | Sim | F | **Copy** polarisation formula; fix the initial condition (hysteresis). A fixed per-agent trait is a possible third baseline |
| [MP-02](evidence/metrics-and-protocols.md) | Tunstrøm et al. 2013, collective states of schooling fish | Couzin model, 270° view (simulation) | cont | none | ind 0.2 rad | O_p, O_r (unit r_i), state thresholds 0.65/0.35, 1 s smoothing; N 30–300 | Emp + Sim | F | **Copy** O_p, O_r, state classes and the transition definition verbatim. **Contra** milling grows with N, so fix and report N |
| [MP-03](evidence/metrics-and-protocols.md) | Demšar et al. 2015, simulated predator attacks | cont/metric, 300° view | cont, weighted drives | evolved tactics; confusion 1/\|N_co\| | none per decision | catches per run with bootstrap CI; common prey sets; N 100, 600 steps | Sim | F (preprint) | **Copy** common-random-number protocol and fixed-tactic predator controls. **Contra** confusion on/off changes catches 3.5-fold (1.52 vs 5.36) |

## Perception and neighbourhood (PN)

| ID | Case | View | Decision | Predator | Noise | Metrics | Evidence | Read | p2 relevance |
|---|---|---|---|---|---|---|---|---|---|
| [PN-01](evidence/perception-and-neighbourhood.md) | Ballerini et al. 2008, topological interaction | topo 6.5 ± 0.9 (empirical); simulation topo nc = 3 vs metric | cont | passing predator, 1/r repulsion | not stated | connected components and stragglers after the attack: 5% (topological) vs 43% (metric); N 200 | Emp + Sim | F | **Copy** k = 3 topological (the authors' own 2D predator simulation) and the components/stragglers metric |
| [PN-02](evidence/perception-and-neighbourhood.md) | Strandburg-Peshkin et al. 2013, visual networks | metric vs topo vs Voronoi vs visual | bin (respond or not) | none | logistic response | model likelihood; transitivity; N 70 | Emp | F | **Contra** k-nearest is not the best fit for fish, and its neighbours overlap, which correlates their inputs |
| [PN-03](evidence/perception-and-neighbourhood.md) | Solon and Tailleur, active Ising model | on-site (zero range) | bin (heading ±1) | none | ind thermal | magnetisation, phase diagram; bands | T + Sim | F (2015 paper) | **Copy** binary choice gives flocking. **Contra** discrete symmetry changes the transition (bands), so Vicsek results do not carry over |
| [PN-04](evidence/perception-and-neighbourhood.md) | Pearce et al. 2014, projection model | binary dark/light projection + topo 4 visible | cont | none | ind | cohesion, opacity | Sim + Emp | F (supplement not read) | **Copy** coarse binary perception plus a few neighbours gives cohesion. **Open** p2 has no attraction term |

## Error and contagion (EC)

| ID | Case | View | Decision | Predator | Noise | Metrics | Evidence | Read | p2 relevance |
|---|---|---|---|---|---|---|---|---|---|
| [EC-01](evidence/error-and-contagion.md) (= SP-04) | Rosenthal et al. 2015, startle cascades on visual networks | visual (ray-cast) | bin (startle) | none (spontaneous false alarms) | false alarms; spread meas. | cascade size distribution, spread against time, clustering of the initiator; fractional contagion fits best; N about 150, 138 events | Emp + Sim | F | **Copy** single-initiator cascade size and simple vs fractional contagion fits. A false alarm spreads exactly like a real alarm |
| [EC-02](evidence/error-and-contagion.md) | Sosna et al. 2019, risk encoded by structure | visual | bin | alarm cue | false alarms; spread meas. | cascade count and size; dose-threshold model; N 40 | Emp + model | F | **Copy** factorial design: hold the model and vary structure, then the reverse. Cascade size follows spacing, not responsiveness |
| [EC-03](evidence/error-and-contagion.md) | Attanasi et al. 2014, turning waves in starlings | — | cont | (motivation only) | spread meas. | rank against time, speed 10–20 m/s, negligible attenuation; N 50–595 | Emp + T | F | **Contra** first-order alignment models (p2's class) predict damped spread; real flocks do not damp. **Copy** spread metrics |
| [EC-04](evidence/error-and-contagion.md) | Toner et al. 2018; Chepizhko et al. 2013, quenched disorder | cont/metric | cont | none (obstacles) | quenched + ind | order parameter; an optimal noise level exists | T + Sim | P | **Open** closest analogue to input-fixed error, but frozen in physical space, not in input space |

## Learned and language-based agents (LA)

| ID | Case | View | Decision | Predator | Noise | Metrics | Evidence | Read | p2 relevance |
|---|---|---|---|---|---|---|---|---|---|
| [LA-01](evidence/learned-and-language-agents.md) | Li et al. 2024, LLMs fail at flocking | text: global coordinate list (allocentric) | cont target position (free text) | none | model; sign errors | nearest-neighbour distance error; about 60% of 5-agent runs collapse; N ≤ 5 | Sim (negative demo, no rule baseline) | F | **Copy** precompute an egocentric view. **Open** no rule baseline and no per-decision error rate |
| [LA-02](evidence/learned-and-language-agents.md) | Jimenez-Romero et al. 2025, GPT-4o birds in NetLogo | text: relative x, y, heading of neighbours in the vision radius | cont heading (JSON) | none | model; turn-direction errors on small counterclockwise turns | heading difference against the rule-only flock; 5 LLM among 30, 800 steps, 5 seeds | Sim with rule baseline (collective only) | F | **Copy** hybrid condition; check where model agents end up in the school. **Open** never scored per decision |
| [LA-03](evidence/learned-and-language-agents.md) | see SP-01 | | | | | | | | |
| [LA-04](evidence/learned-and-language-agents.md) | Hahn et al. 2019, SELFish RL escape flocking | egocentric topo n: distance, bearing, orientation | disc 5 turns (DQN) / cont | scripted, chases nearest, random among ties | none; one shared policy | clusters, alignment, captures; Boids and TurnAway baselines | Sim | F | **Contra** a TurnAway rule beat the learned flock and Boids on survival. **Copy** TurnAway-only and Boids baselines |

## Spatial language for models (SL)

| ID | Case | Encoding | Question | Error types | Numbers | Evidence | Read | p2 relevance |
|---|---|---|---|---|---|---|---|---|
| [SL-01](evidence/spatial-language.md) | StepGame (2022) and its LLM re-evaluation (2024) | allocentric story, 8 directions | relation of A to B, k = 1–10 hops | accuracy falls with hops; 14 of 214 templates were mislabelled | GPT-4 100% at k = 1, 25% at k = 10 | Bench | F | **Copy** one-hop questions with precomputed geometry are the easy end; audit the reference rule's labels |
| [SL-02](evidence/spatial-language.md) | FoREST 2025, frame of reference | short scene sentences with or without perspective | relation after a perspective change | systematic left/right reversal (Llama3-70B); default frame bias | best camera-to-relatum 55.5% | Bench | F | **Contra** left/right errors are systematic, not noise. **Copy** frame-free labels; test mirror images |
| [SL-03](evidence/spatial-language.md) | GSU 2026, grids and egocentric frames | grid coordinates with heading | localisation and navigation | fall back to the default "+Y forward" frame; front/back flips | 7–8B models below 50 on egocentric localisation; LoRA gives large gains | Bench | F | **Copy** precompute egocentric relations; fine-tuned small models close the gap. Expect errors fixed to headings or sectors |
| [SL-04](evidence/spatial-language.md) | Zhu et al. 2026, maze format | adjacency list vs character grid | path, proximity | representation dependence | 86% vs 34% on the same 5×5 maze | Bench | A | **Contra** encoding changes accuracy 2–5×; freeze one encoding and test a second |

## Broad-survey cards reused (not re-read)

| ID | Case | Use here |
|---|---|---|
| [C-04](../statistically_correct/evidence/control-and-collective-behaviour.md) | Vicsek model and its first-order correction | noise threshold; polarisation; bistability near the threshold |
| [C-05](../statistically_correct/evidence/control-and-collective-behaviour.md), [C-06](../statistically_correct/evidence/control-and-collective-behaviour.md) | Informed and opinionated minorities (abstracts only) | a cluster of agents sharing one wrong bias can steer a group |
| [C-09](../statistically_correct/evidence/control-and-collective-behaviour.md) | Kao and Couzin 2014 | correlated cues make large groups worse |
| [C-11](../statistically_correct/evidence/control-and-collective-behaviour.md) | Jadhav et al. 2021 | topological K, blind zone; random partner choice aids cohesion |
| [C-12](../statistically_correct/evidence/control-and-collective-behaviour.md) | Klamser and Romanczuk 2021 | predator-prey model with capture rate; code public |
| [G-03](../statistically_correct/evidence/game-theory-and-stochastic-optimisation.md), [G-04](../statistically_correct/evidence/game-theory-and-stochastic-optimisation.md) | Informational cascades, theory and lab | observing others' actions locks in early errors |
| [S-11](../statistically_correct/evidence/stats-and-reliable-computation.md) | N-version coding agents | nominally diverse AI agents fail together |

## Spot-check (step 3)

Seven quoted claims were checked against the source text, re-downloaded independently of the searchers:

| Card | Claim checked | Result |
|---|---|---|
| PN-01 | nc = 3 in the topological simulation; stragglers 43% vs 5% | match |
| SP-01 | 70% of replicates; 180 replicates | match |
| LA-01 | "nearly 60% of the tests fail and gather to the same point" | match |
| LA-04 | "the best strategy to survive is to simply turn away" | match |
| LA-02 | opposite directions; errors on counterclockwise turns | match |
| SL-02 | left/right reversal; 55.5% | match |
| MP-03 | 1.522, 5.357, 2.773 | match, from the searcher's downloaded preprint |

No errors were found. The remaining numbers are as the searchers report them.
