# Implications for the p2 design

Step 4 deliverable, 2026-10-06. Organised by p2 design choice ([framing.md §1](framing.md#1-the-p2-design-in-one-page)). Each choice gets one of three verdicts:
- **Supported:** a source uses it and it works.
- **Contradicted / qualified:** a source shows a problem with it.
- **Open:** no source tests it.

Card IDs link to [catalog.md](catalog.md). "Lab" marks a local lead from [framing.md](framing.md), not a literature result. "Inference" marks my own reading. This page lists choices and evidence only. It is not a p2 protocol.

## 1. Space and perception

| Choice | Verdict | Evidence |
|---|---|---|
| 2D torus | Supported, with two notes | SP-02 (736 × 736 torus) and LA-04 (40 × 40 torus) use one. **Notes:** (a) No metric source defines the centroid on a torus, so O_r needs an unwrapped or circular-mean centroid (MP-02 note). (b) The predator needs a start rule. MP-03 starts it 200 body lengths behind the group; a torus has no "outside". |
| 8 angular sectors | Supported in kind; resolution open | SP-01 uses 12 × 15° frontal sectors and SP-02 24 × 15° over 360°, both presence-only, and swarming evolves. PN-04: binary angular occupancy is enough for cohesion. **Open:** no source compares a sector view with continuous perception, or 8 sectors with finer ones. SP-01's prey have a rear blind zone; p2's 8 sectors cover 360°. Biological models use 270–300° (MP-01, MP-02, MP-03) and the choice is not neutral (log entries for Tian 2009 and Nguyen 2014 disagree on the best view angle). |
| 3 distance bands for the predator | Open | No source uses distance bands. SP-01 uses presence within a range; MP-03's escape drive scales linearly with distance inside a radius. Bands are a coarse version of the latter (inference). |
| k = 3 topological neighbours | Supported for cohesion; qualified for independence | PN-01's 2D predator-pass simulation uses nc = 3 topological neighbours: stragglers 5% against 43% for the metric model. C-11 also uses topological K. **Qualified:** for fish, visual networks fit better than k-nearest (PN-02). k-nearest networks have high transitivity, so neighbours see overlapping neighbours. In p2 that gives correlated inputs, and with input-fixed errors, correlated errors that are not contagion (inference from PN-02 and lab p1). |
| Neighbours described by sector and previous move only (no distance, no heading) | **Contradicted / open** | See §2: the rule never uses the neighbours' sectors, and no carded model aligns on neighbours' previous *turns*. |
| Fixed field order | Supported by lab evidence | Lab p1: shuffling fields changed 2–8 of 68–69 K27 answers. SL-04: the text encoding of the same space changed accuracy 2–5×. Freeze one order, and test one alternative encoding on the same views so that errors can be attributed to the view, not the format (SL-04). |

## 2. Decision and reference rule

| Choice | Verdict | Evidence |
|---|---|---|
| A discrete per-agent decision | Supported | SP-01 and SP-02: 4 actions from two binary outputs. PN-03: binary heading (±1) gives a real flocking phase. LA-04: 5 discrete turns. EC-01 and PN-02: real fish act on a binary "responded or not" state of neighbours. |
| **Exactly two options, a turn every step (no "straight")** | **Contradicted / open** | No source uses a pure left/right forced turn at every step. SP-01/SP-02 include forward and stay. LA-04 includes 0°. PN-03's binary variable is the heading, not a turn. **Risk:** an agent that must turn every step can only go straight by alternating (SP-02 card note). The rule can produce long same-direction runs: a neighbour majority that turned left yields left again, which gives circling (milling) rather than translation (inference). Milling is a common attractor even in continuous models (MP-01, MP-02). |
| **Alignment by copying the neighbours' majority previous move** | **Contradicted / open** | Every schooling model carded aligns on neighbours' **headings** (MP-01 orientation zone, PN-04, C-04, PN-01) or is attracted to their **positions** (MP-01, SP-05, MP-03). None copies neighbours' turns. Copying turns synchronises turning but does not pull headings together or keep agents together. The rule has no cohesion term, although the view contains neighbour sectors that could supply one (inference). PN-04 warns that cohesion needs an explicit mechanism. **Implication:** the rule-only baseline must be shown to school (polarised, cohesive) before any model is compared with it. The literature suggests it may not. |
| Strict priority: predator first, else neighbours | Supported | SP-05: Boids arbitrates by priority because averaging cancels opposite urges. Binary choice avoids that cancellation. MP-01: repulsion has absolute priority. |
| "Turn away from the predator" as the predator response | Supported for survival; qualified for schooling | LA-04: a TurnAway rule beat a learned flock and Boids on survival. MP-03's prey use an escape drive away from the predator. **Qualified:** in SP-01 evolved prey ignored the predator and survived through confusion alone. SP-03: grouping protected prey that could not sense the predator. Fleeing and schooling are separate effects, so p2 needs a baseline for each (§3). |
| Rule cases when the predator is ahead, behind or unseen | Open; audit needed | No source defines such a tie case. SL-01 found 14 of 214 benchmark templates mislabelled. Audit the rule's labels at sector boundaries (what "ahead" and "behind" mean) before counting model errors. |
| Argmax against sampling | Lab | Lab p1: sampled individuals are worse than argmax by the calibration gap (0.05 for K27) and add no votes. |

## 3. Baselines

| Baseline | Verdict | Evidence |
|---|---|---|
| Rule-only | Supported, but must be validated first (§2) | All carded studies have a rule or a no-model condition. |
| Rule + random error at a matched rate | **New; must be defined by p2** | No source defines a noise-matched baseline (MP summary). All published noise is independent Gaussian angular noise (MP-01, MP-02, C-04). "Matched" can mean the overall error rate, or the rate per view class (per predator sector, left/right asymmetry). The two give different tests. |
| **Rule + view-fixed random error** (a random lookup table that flips the rule's answer on a fixed set of views, at the model's rate) | Suggested by the literature; untested | This is the input-space analogue of quenched disorder (EC-04). It separates "errors fixed to views" (shared by all agents in that view, lab p1) from "this model's particular errors". EC-04 predicts flocks tolerate quenched disorder better than one might expect, and an optimal annealed noise may exist on top of it. Untested for input-space disorder. |
| Fixed per-agent bias (each agent has its own constant left/right bias) | Suggested | MP-01 fixes individual traits per agent, which sorts agents spatially. A third error structure between independent noise and view-fixed error. |
| TurnAway-only (ignore neighbours) | Suggested | LA-04: the best survival strategy there. Separates fleeing from schooling. |
| Neighbour-only (ignore predator) | Suggested | SP-01 and SP-03: protection without reacting to the predator. |
| Continuous Boids or Couzin model with a predator | Suggested | LA-04 (Boids with avoidance), LA-02 (NetLogo Flocking), MP-03. Gives the "normal" schooling reference that p2's binary rule is a coarse version of. |
| No-predator control | Suggested | Separates collective structure from predation effects; Tunstrøm states are defined without a predator (MP-02). |
| Null predator (random target at the same attack times) | Suggested | SP-03: separates targeting from vulnerability. |
| Confusion on/off | Suggested if the predator has confusion | MP-03: confusion changes mean catches 3.5-fold. SP-01: no grouping without it. The predator model is a first-order factor (SP-02), so fix it, report it, and ideally vary it. |
| Hybrid (k model agents among rule agents) | Suggested | LA-02's design. Shows where model agents end up (periphery) and whether a minority with shared errors steers the group (C-05, C-06). |

## 4. Metrics and replicates

**Adopt verbatim:**
- **Polarisation** O_p = |(1/N) Σ u_i|.
- **Milling** O_r = |(1/N) Σ u_i × r_i|, with r_i the unit vector from the centroid (MP-02).
- **States** from Tunstrøm's thresholds: polar when O_p > 0.65 and O_r < 0.35; milling when O_p < 0.35 and O_r > 0.65; swarm when both < 0.35.
  - Time fractions in each state, and transitions counted only between P, M and S.
  - Values smoothed over a window, with the k = 0.25 / 0.40 threshold check (MP-02).
- **Cohesion:**
  - connected components and straggler fraction (PN-01);
  - density within radius R and mean nearest-neighbour distance (SP-01).
- **Predation:**
  - captures per run with bootstrap CIs;
  - the same set of initial configurations for every condition, i.e. common random numbers (MP-03);
  - survivors and time to first capture (SP-01).
- **Initial condition.** Fix it and report it. Couzin-type models show hysteresis (MP-01).
- **Report O_r, not only O_p.** A binary turner biased to one side will mill (§2).

**Replicates reported in the literature:**

| Source | Replicates |
|---|---|
| Couzin 2002 (MP-01) | 30 per setting |
| Demšar 2015 (MP-03) | 20 |
| Olson 2015 preprint (SP-02) | 100 |
| Olson 2013 (SP-01) | 180 |
| Tunstrøm 2013 (MP-02) | 500 |

Typical sizes are N = 50–300 and 600–2,500 steps. Milling depends on N (MP-02), so fix N, report it, and preferably use two values.

**Cost (lab + inference).** At K27's 1.66 s per request, N = 50 × T = 1,000 × 30 replicates is 1.5 M requests (about 29 days sequentially). That is infeasible per condition. But the p2 view space is finite:
- predator: 8 sectors × 3 bands + unseen = 25 states;
- each neighbour: 8 sectors × 2 previous moves = 16 states;
- three ordered neighbours: 16³ = 4,096.

That gives 102,400 views in total, fewer after mirror symmetry. The lab's deciders are deterministic at argmax (lab: bit-identical repeats for jeff). So the model can be queried **once per view** and stored as a table: about 47 h for K27, 22 h for W12, or about 3 h for jeff, after which replicates are free. The table is also the complete per-view error map that the view-fixed baseline (§3) and the mirror check (§6) need. A lazy cache over views actually visited costs less.

## 5. Error propagation

The literature measures spread in these ways, and p2 can report the same quantities:

| Quantity | Source |
|---|---|
| Cascade size after a single initiator (distribution and mean) | EC-01, EC-02 |
| Spatial extent of the responders against time; propagation speed | EC-01, EC-03 |
| Attenuation of the response with rank in the cascade | EC-03 |
| Simple vs fractional-threshold contagion fit | EC-01 (fractional fits fish best; PN-02 uses the same form) |
| A structural predictor: the initiator's local clustering in the interaction network | EC-01 |
| Factorial separation: vary structure with the decision rule fixed, and the reverse | EC-02 (cascade size followed spacing, not responsiveness) |

Expectations and cautions:

- **A single wrong neighbour is a 1/3 fraction under the majority-of-3 rule, so it is usually outvoted** (EC-01 card, inference). Large cascades need errors that co-occur among neighbours, which is what view-fixed errors on overlapping neighbourhoods produce (PN-02, lab p1). p2's neighbourhood co-error measure must therefore separate shared input from contagion:
  - compare co-error among agents with identical views against co-error among neighbours;
  - and/or run EC-02's factorial design.
- **Contagion and correlation need different measures.** Error correlation among neighbours (observed co-error against chance) has no direct precedent in the collective-motion cards. The closest measures are mutual-error agreement in the LLM literature (S-04, Kim et al.) and coincident failures (S-11).
- **Do not generalise p2's spread results to animal schools.** p2's rule is first-order (no inertia). Models of that class damp the spread of a turn, whereas starling flocks show linear, undamped spread (EC-03).
- **Measuring one error's effect directly.** Run a twin of the same simulation with one forced error and the same random numbers, and measure how the two runs diverge. Physics calls this "damage spreading", but no source for it was carded. Treat it as a gap, not as established practice.
- **Do not transfer cascade theory to p2 without checking.** Cascades lock in early errors under sequential observation (G-03, G-04). p2's previous-move channel has the same structure in space, but no source tests that.

## 6. Rendering space to the model

| Choice | Verdict | Evidence |
|---|---|---|
| Simulator precomputes an egocentric view; model only decides | Supported | LA-01: raw coordinates gave sign errors and collapse. SL-03: the frame update is where models fail. SL-01: precomputed geometry plus a solver gives 2 errors in 1,000. study/game: code computes, model chooses (lab). |
| Labels for sectors | Open; risk identified | SL-02: Llama3-70B systematically reverses left and right when converting perspective. SL-03: models fall back to a default frame. LA-02: turn-direction errors on small counterclockwise turns. Use labels that need no frame conversion (e.g. "front-left" relative to the agent, never compass words), and test 2–3 wordings (lab R2.1). |
| Mirror check | Recommended | Errors are systematic (SL-02, SL-03), not noise. Every view has a mirror image whose correct answer is the opposite turn. Scoring both detects a left/right bias directly (inference; cheap given the view table of §4). |
| Option order and keys | Lab | Fix the option order or average both orders; jeff changed 21/60 answers under reversal (R3.8). Keys must not appear in the state text (R2.5): the state contains "left"/"right" as neighbours' previous moves, which is exactly that case for a left/right question. |
| Missing predator | Lab | Write `unseen` explicitly (R5.8). |
| Neighbour list length | Supported as short | SL-01: accuracy falls with hops and distractors. Three neighbours plus the predator is small, but the majority over three moves is an aggregation step that no benchmark tests. |
| One question per request | Lab | Several agents in one jeff request need `JEFF_ISOLATE=all`. Otherwise, one agent per request. |
| Which decider | Open | No text benchmark of a binary left/right choice from a structured egocentric state exists (SL gap). Small models are weak on egocentric frames zero-shot (SL-03), and fine-tuning closes much of the gap. The lab's only state-rendering test hurt jeff (lab, game_test/p2). |

## 7. Novelty

As far as this search found, p2 would be the first to measure five things:
1. **Per-decision agreement with the rule** for a learned or language-model decider inside a moving collective. LA-02 compared only at the collective level, LA-01 had no rule baseline, and LA-03/SP-01 had no reference rule.
2. **Spatial and temporal correlation of agent errors** in a school, separated into shared input and contagion.
3. **View-fixed against independent random error** at a matched rate in a collective-motion model. Quenched disorder has been studied only in physical space (EC-04).
4. **A Jev-style or LLM decider in a swarm with a predator.** No 2024–2026 example was found.
5. **A pure binary left/right turn every step from a sector view**, with a topological k = 3 under a fixed reference rule.

Items 1–3 are p2's scientific contribution. Item 5 is a design choice whose risks (§2) may be larger than its novelty.

## 8. Gaps of this study

- **Sources not opened:**
  - the confusion-effect originals (Ioannou et al. 2008, Tosh 2011);
  - escape-wave and fountain-effect models;
  - damage spreading;
  - classifier imitation of Boids;
  - the Ginelli and Chaté (2010) Voronoi result (lead only).
- **Single reads.** EC-04 was read partially and SL-04 only to the end of its introduction.
- **Supplements unread.** No supplement was read (SP-01, SP-03, PN-01, PN-04, EC-01).
- **Unchecked numbers.** Spot-checks covered seven claims. Other numbers are as the searchers extracted them.
