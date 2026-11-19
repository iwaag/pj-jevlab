# Study: schooling_sim — prior work for a decision-model school with a predator

Targeted literature survey as of **2026-10-06**. It serves the set6 p2 design (idea F1 in [set6 idea.md](../../devdocs/episodes/experiments/set6-statistically_correct/idea.md)):
- a 2D school of N agents and one predator;
- each agent sees a simulator-computed, egocentric, discretised view (predator sector and distance band, 3 nearest neighbours' sectors and previous moves);
- a Jev-style decision model answers "turn left or right" once per agent per step;
- outcomes are scored against a reference rule and at the collective level.

This study builds on the broad survey [statistically_correct](../statistically_correct/README.md). No model was run and no simulator was built. Plan and step reports: [devdocs/episodes/experiments/set6-statistically_correct/p2/pre1/](../../devdocs/episodes/experiments/set6-statistically_correct/p2/pre1/report.md).

## Files

| File | Contents |
|---|---|
| [framing.md](framing.md) | The p2 design in one page; definitions; what local leads (broad-survey cards, p1, lab rendering evidence) settle and leave open |
| [search-log.md](search-log.md) | Queries, URLs, inclusion decisions, access levels, gaps; three searcher fragments; cutoff 2026-10-06 |
| [evidence/](evidence) | 24 cards (22 distinct cases) in six areas: schooling and predation (SP), metrics and protocols (MP), perception (PN), error and contagion (EC), learned and language agents (LA), spatial language (SL) |
| [catalog.md](catalog.md) | One row per case (view, decision, predator, noise, metrics, evidence type, p2 relevance); spot-check record |
| [implications.md](implications.md) | p2 design choices marked supported, contradicted or open, with card links; baselines, metrics, replicates, spread measures, rendering, novelty |

## Answers

**Q1. Standard predator-avoidance schooling models and their baselines.**
- **The models:**
  - Boids: prioritised rules, no metrics (SP-05).
  - Couzin zones: repulsion, orientation, attraction; blind volume; Gaussian heading noise (MP-01).
  - Vicsek: metric alignment plus noise (C-04).
  - Hamilton's selfish herd, with an evolutionary test showing that the attack mode decides whether grouping evolves (SP-02).
  - The confusion effect, modelled as P_capture = 1/(prey near the target) (SP-01, MP-03).
  - Predator-prey agent models with capture rate (C-12, MP-03).
- **Low-dimensional per-agent choices** appear only in evolved Markov-network prey (4 actions from two binary outputs; SP-01, SP-02), RL agents (5 discrete turns; LA-04), the active Ising model (binary heading; PN-03) and binary startle responses (EC-01).
- **Baselines used:**
  - confusion on/off (no grouping evolves without it; catches 3.5× higher);
  - fixed-tactic predators;
  - a null predator that picks random targets;
  - TurnAway and Boids against learned agents (TurnAway won on survival).

**Q2. Local perception and discretisation.**
- **Topological interaction** is empirically grounded: starlings use 6.5 ± 0.9 neighbours. In 2D, a topological model with nc = 3 resisted a predator pass far better than a metric one (stragglers 5% vs 43%) (PN-01).
- **Coarse perception still gives schooling and escape:**
  - 12 × 15° presence-only sectors (SP-01);
  - binary dark/light projection plus 4 neighbours (PN-04);
  - binary headings, which give a flocking phase with bands, not Vicsek's transition (PN-03).
- **Qualifications:**
  - For fish, visual networks fit better than k-nearest. k-nearest neighbourhoods overlap, which correlates neighbours' inputs (PN-02).
  - Studies disagree on the effect of view angle.
  - No source compares sector × band views with continuous perception.

**Q3. Learned or language policies replacing the local rule.**
- **LLM swarms so far are small and mostly fail or need repair:**
  - GPT-3.5 given raw coordinates collapsed in about 60% of 5-agent runs and showed sign errors; there was no rule baseline (LA-01).
  - GPT-4o birds in a 30-bird NetLogo flock matched the rule flock only after prompt repair. Turn-direction errors on small counterclockwise turns remained, and the comparison was at flock level only (LA-02).
- **Evolved and RL policies:** they use egocentric discrete views (SP-01, LA-04), and in LA-04 a trivial TurnAway rule beat the RL flock on survival.
- **The gap:** no source scores agent-level decisions against the rule, measures how agent errors correlate, or uses a predator with an LLM swarm.

**Q4. Errors and noise in these populations.**
- **Published noise is independent** Gaussian or thermal noise (MP-01, C-04, PN-03). There are noise thresholds, and they are bistable (C-04).
- **Wrong actions spread like correct ones:**
  - Fish false-alarm startles spread exactly like real alarms. Spread fits a fractional threshold (a share of neighbours) (EC-01).
  - Cascade size follows group spacing rather than individual responsiveness (EC-02).
- **Spread speed:** turning waves in starlings spread linearly and undamped, whereas first-order alignment models (p2's class) damp them (EC-03).
- **Quenched disorder:** flocks tolerate disorder that is frozen in space, and an optimal added noise can exist (EC-04).
- **Gap:** no source has errors fixed to the agent's input, which is p2's case (lab p1).

**Q5. Metrics and comparison conditions.**
- **Metrics to adopt verbatim:**
  - O_p and O_r with unit r_i;
  - Tunstrøm state thresholds (0.65/0.35) and time-in-state fractions, with smoothing (MP-02);
  - connected components and stragglers (PN-01);
  - density and nearest-neighbour distance (SP-01);
  - captures per run with bootstrap CIs over common initial configurations (MP-03).
- **Typical study sizes:** N 50–300; 600–2,500 steps; 20–500 replicates.
- **No source defines a noise-matched baseline.** p2 must define one, and implications §3 adds a view-fixed random-error baseline.

**Q6. Language or decision models reading spatial relations from text.**
- **One-hop relations with precomputed geometry are easy;** accuracy falls with hops and distractors (SL-01).
- **Egocentric frames are harder, and the errors are systematic:**
  - systematic left/right reversal under perspective change (SL-02);
  - fallback to a default frame (SL-03);
  - turn-direction errors (LA-02).
- **Text format alone changes accuracy 2–5×** (SL-04).
- **Small models** are weak zero-shot on egocentric tasks, and fine-tuning closes much of the gap (SL-03).
- **Gap:** there is no benchmark of a single binary left/right choice from a structured egocentric state.

**Q7. Implications for p2.** See [implications.md](implications.md). The main points:
- **Supported:** a discrete egocentric sector view; topological k = 3; strict-priority rule; turning away from the predator for survival; simulator-computed geometry.
- **Contradicted or open:**
  - A forced left/right turn every step, with "copy the neighbours' majority previous turn", has no alignment-to-heading or cohesion term in any carded model. Show that the rule-only baseline schools before comparing models.
  - The predator model (confusion, attack mode) dominates capture rate.
  - k-nearest neighbourhoods correlate inputs, which mimics contagion.
- **Cost:** the view space is finite (about 102k views), so a deterministic decider can be tabulated once (about 3 h for jeff, 22–47 h for W12/K27). Replicates then cost nothing, and the table gives the full per-view error map and a mirror (left/right) check.
- **New:** per-decision agreement scoring in a collective; error correlation split into shared input and contagion; view-fixed against random error at a matched rate; a Jev-style decider in a school with a predator.

## Caveats

- **Who read what.** Subagents read the sources. Read levels are on each card, and most are full text of the main sections. Supplements were not read. Seven claims were spot-checked against the source text and all matched.
- **Gaps.** The confusion-effect originals, escape-wave models, damage spreading and classifier imitation of Boids were not carded. Japanese searches added nothing usable.
- **Verdicts are inferences.** The "Relevance to p2" fields and the verdicts in implications.md are inferences. Lab facts come from local reports, not from this search.
