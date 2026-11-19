# Framing — schooling_sim (prior work for a decision-model school with a predator)

Date: 2026-10-06. Step 1 of the study plan ([devdocs/episodes/experiments/set6-statistically_correct/p2/pre1/plan.md](../../devdocs/episodes/experiments/set6-statistically_correct/p2/pre1/plan.md)). Serves idea F1 of [set6 idea.md](../../devdocs/episodes/experiments/set6-statistically_correct/idea.md). This page fixes the design being checked, the definitions used in the cards, and what the lab's own material already settles. Everything under "Local leads" is a lead, not a finding of this study.

## 1. The p2 design in one page

- **World.** A 2D torus. N prey agents and one predator. Discrete time steps. Constant speed; each prey changes heading only by a fixed turn.
- **View (computed by the simulator, not by the model).** Egocentric and discretised:
  - predator: one of 8 angular sectors relative to the agent's heading, and one of 3 distance bands, or `unseen`;
  - the k = 3 nearest neighbours (topological, not metric): each neighbour's sector and its previous move (left, right).
  - The view is written as structured text with a fixed field order.
- **Decision.** One binary question per agent per step: turn left or turn right. A Jev-style model returns a probability over the two options; the argmax (or a draw) is the action.
- **Reference rule (defines the "correct" turn from the same view).** Turn away from the predator. When the predator is ahead, behind or unseen (no side to turn away from), follow the majority of the neighbours' previous moves.
- **Conditions.** Rule-only; rule plus injected random error at the model's measured error rate (noise-matched); model-driven.
- **Outcomes.**
  - Individual: agreement with the reference rule.
  - Neighbourhood: whether neighbours err in the same step more often than independent errors would.
  - Temporal: whether one error propagates through neighbours' previous moves into later errors.
  - Collective: capture rate, polarisation, cohesion.

## 2. Definitions used in this study

| Term | Meaning here |
|---|---|
| View | The input the decider sees for one agent at one step (above). Perception is exact; only the decision can be wrong. |
| Rule | The reference rule above. It is a definition of correctness, not a claim of optimality; a source's rule is compared to it by what it uses (predator side, neighbours' headings, neighbours' moves). |
| Error | A decision that differs from the rule's decision on the same view. *Injected noise*: an error drawn independently of the view. *Model error*: an error that is a function of the view (p1: fixed to cases). |
| Neighbourhood | *Metric*: all agents within a radius. *Topological*: a fixed number k of nearest agents. *Visual*: agents not occluded in the field of view. Each card records which. |
| Cascade / contagion | A change in one agent's action that causes changes in others' actions through the interaction rule. Reported as a quantity per source (e.g. cascade size, fraction of the group reached, speed of the turning wave). |
| Polarisation | Magnitude of the mean unit heading vector (0 disordered, 1 aligned). Exact definitions per source in [evidence/metrics-and-protocols.md](evidence/metrics-and-protocols.md). |
| Cohesion | A group-integrity measure: largest-cluster fraction, mean nearest-neighbour distance or group extent. Varies by source; recorded per card. |
| Capture / survival | Fraction of prey caught per attack or per unit time; time to first capture. |
| Demonstration vs evaluation | A demonstration shows that a system runs; an evaluation compares it with a baseline on a stated metric. |

## 3. Local leads: the broad survey

Cards in [study/statistically_correct](../statistically_correct/README.md), reopened. "Settles" is what the card already answers for this study's questions (Q1–Q5); "open" is what it leaves.

| Card | Settles | Leaves open |
|---|---|---|
| C-04 Vicsek (with Grégoire–Chaté correction) | Q1/Q4: metric neighbourhood, continuous heading, independent angular noise; order is lost above a critical noise, and the transition is discontinuous, so a noise knob near threshold is bistable. Q5: polarisation \|v_a\| as the order metric; N 4,000–16,000 in the original. | No predator, no binary choice, no structured (view-dependent) noise. |
| C-05 Couzin 2005 (abstract only) | Q1: zone-type models in which a few informed agents steer a group; larger groups need a smaller informed fraction. | Rules and numbers not seen; no predator. |
| C-06 Couzin 2011 (abstract only) | Q4: a strongly opinionated minority can capture a group; uninformed agents restore majority control. | Relevant as a risk: a cluster of agents with the same wrong bias is an "opinionated minority". No predator. |
| C-07 Berdahl 2013 (abstract only) | Q1: group-level sensing from individually poor local measurements. | No numbers; not predator escape. |
| C-08 Honeybee nest choice | Q4: interdependence without independence gives consensus on the wrong option (cascade). | Not spatial; not motion. |
| C-09 Kao and Couzin 2014 | Q4: correlated information sources make large groups worse than small ones; binary majority model. | Analytic, not spatial; shared cue ≈ the shared blind spots of one model (inference). |
| C-11 Jadhav, Guttal, Raj 2021 | Q2: topological K nearest with random choice of 1 of K gives better cohesion than nearest-only; blind zone; asynchronous updates. Code public. | No predator; noise is choice of partner, not decision error. |
| C-12 Klamser and Romanczuk 2021 | Q1/Q5: predator-prey agent model with capture rate, polarisation, criticality; capture rate anti-correlated with inter-individual distance (R = −0.69). Code public. | Population and attack counts only from a fetch summary; no decision error. |
| G-03 / G-04 cascades | Q4: sequential observation of others' actions locks in early errors; lab rate of reverse cascades 13/41 and 18/46. | Not spatial; p2's previous-move channel is the same structure in space (inference). |
| S-11 N-version coding agents | Q4: nominally diverse AI agents fail together (429 coincident failures vs 115 expected). | Not motion. |
| M-13 to M-15 game-agent legibility | Q4 (side): human judges read stuck, jerky, abrupt behaviour as non-human; human-like mistakes are state-dependent (Maia). | Not collectives. |

**Gaps already known from the broad survey:** Boids not retrieved; no source tests a decision model in a moving collective; no card on predator confusion, selfish herd, topological interaction (Ballerini) or startle contagion. These are search targets for step 2.

## 4. Local leads: p1 results that constrain p2

From [set6 p1 report](../../devdocs/episodes/experiments/set6-statistically_correct/p1/report.md):

- **Errors are fixed to cases.** In one-model populations, 0–6% of cases are "middle" (wrong for some copies); the rest are easy or hard for every copy. Prediction for p2 (inference): agents with the same view will make the same error, so neighbourhood error correlation will be driven by view similarity, and in a polarised school neighbours have similar views. A noise-matched random-error baseline will not reproduce this.
- **Field order matters a little.** Shuffling state fields changed 2–8 of 68–69 K27 answers. p2 fixes the field order; this is the size of effect to expect if it is changed.
- **Sampling is worse than argmax by the calibration gap** (0.05 for K27 on W2/W3). Sampled individuals would have a lower rule agreement than argmax ones, with no aggregation benefit.
- **Cost.** p50 latency per request: K27 1.66 s, W12 0.76 s (W3, sequential). N agents × T steps decisions are needed per run; e.g. N = 50, T = 200 is 10,000 requests, about 4.6 h for K27 sequentially. Replicate counts from the literature (Q5) must be set against this.
- **Who the decider is.** K27 and W12 are decoder fine-tunes; J (jeff, encoder) is about 0.1 s per request but has different failure modes (below).

## 5. Local leads: how state has been rendered to decision models in this lab

- **game_test/p2 (jeff, Blackout Dispatch).** No spatial state was ever rendered. Adding a 7-field visible game state (robot location, battery "N of MAX", flags) changed top-1 on 26 of 59 cases, 23 newly wrong; the state was dropped ([report5](../../devdocs/episodes/game_test/p2/report5.md)). Option order changed 17–32% of top-1 answers. Keys that name an action attract overrides containing that word.
- **Within-request interference (`JEFF_ISOLATE`).** Two `choice` questions in one jeff request under the default (`nouls`) changed the job answer on 40 of 197 cases; `JEFF_ISOLATE=all` made combined requests identical to separate ones ([ex1 report5](../../devdocs/episodes/game_test/p2/ex1/report5.md)). For p2: one question per request, or isolation, if several agents are batched in one request.
- **study/game.** The working pattern is "code computes, model chooses" (code writes distances and placements). In the chess example the model received prose plus FEN plus ASCII board and was outplayed; where code-written descriptions already encode the answer, a rule beats the model ([study/game/README.md](../game/README.md)). Inference: p2's reference rule is computable from the view, so the model cannot beat the rule on agreement; the study is about the structure of its errors, not about performance.
- **study/prompt_best_practice.** R1.5 send only what the decision needs and A/B any added context; R1.1 judge wording by spread over variants; R2.1/R2.2 test 2–3 label wordings and use contrastive descriptions; R2.5 keys should not name actions that appear in the state; R3.1–R3.3 expect order effects, permutation averaging reduces them; R3.8 jeff changed 21/60 answers under option reversal; R5.8 write missing values as explicit `unknown` ([guidelines.md](../prompt_best_practice/guidelines.md)). A two-option `choice` and `noul` were equivalent within n = 6.

**Not settled locally (open for Q6 and for p2 itself):** whether any lab decider can read an egocentric sector view at all; sector and distance wording; how to list three neighbours; left/right symmetry and position bias for a mirror pair of options; whether a mirrored view gives the mirrored answer (an obvious check, cheap to run).

## 6. Distinctions applied when reading sources

From the plan: rule agreement vs survival; injected noise vs model error; perception vs decision (here perception is exact); metric vs topological neighbourhood; claim vs measurement (demonstrations of LLM swarms establish feasibility only).
