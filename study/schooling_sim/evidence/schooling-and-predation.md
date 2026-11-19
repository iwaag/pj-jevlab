# Evidence: classical schooling and predation models

- Searcher areas: (1) classical schooling and predation models (cards SP-xx). The metric definitions these models use are in `metrics-and-protocols.md` (MP-xx).
- Access date: 2026-10-06.
- Read-level legend: **full text** = PDF or HTML of the primary source read, with sections named; **abstract only** = only the abstract read; **fetch summary** = a small-model summary of a web page; **search summary** = a search-engine snippet only. Anything not verified is marked "not verified".
- Already covered elsewhere and not repeated here: Vicsek (C-04), Couzin 2005 (C-05), Couzin 2011 (C-06), Berdahl 2013 (C-07), Kao & Couzin 2014 (C-09), Jadhav et al. 2021 (C-11), Klamser & Romanczuk 2021 (C-12), informational cascades (G-03, G-04), N-version coincident failures (S-11).

## Summary: positive and negative/qualifying results

**Positive (supports the p2 design's ingredients):**
- A discrete left/right/forward choice from a coarse, sector-based egocentric view is enough to evolve swarming under predation. Olson et al. 2013 (SP-01) give each prey a 12-sector retina for prey and a separate one for the predator, and four discrete actions: stay, forward, forward+left 8°, forward+right 8°. This is the closest published analogue of the p2 per-agent decision. It uses 50 clonal prey, 1 predator, 2,000 steps and 180 replicates.
- In SP-01, predator confusion is modelled as P_capture = 1/A_NV, where A_NV is the number of prey visible to the predator within 30 units of the target. Demšar et al. 2015 (MP-03) reuse this rule. p2 can adopt it verbatim.
- Escape cascades in real fish spread through a weighted, directed visual network. Fish do **not** tell a spontaneous (false-alarm) startle from a real-threat startle: a "wrong" individual action propagates exactly like a correct one (SP-04, Rosenthal et al. 2015). This is direct empirical support for p2's temporal outcome (one error propagating via neighbours' previous moves).
- Reynolds 1987 (SP-05) combines urges by strict priority: avoidance first, then the others. This matches the structure of the p2 reference rule (escape the predator first, otherwise follow the neighbours). Reynolds also notes that averaging opposite urges cancels them out, which a binary choice avoids.

**Negative / qualifying:**
- In SP-01, prey evolved under confusion at generation 1,200 **ignored the predator entirely**. They reacted only to conspecifics, and swarming alone gave the protection. A "turn away from the predator" rule is therefore not necessary for group survival in that model. The predator's attack mode and field of view decide whether grouping pays: with a predator FOV of 60° or less, swarming no longer evolved.
- Without predator confusion (SP-01), or without any attacks (SP-02), prey **disperse** rather than school. Uniformly random attack locations select only weakly for grouping (SP-02, Olson et al.). Hamilton's (1971) assumption that attack mode does not matter was not corroborated. Capture rate in p2 will therefore depend heavily on the predator model chosen. That choice is a first-order design decision, not a detail.
- Ioannou et al. 2012 (SP-03): the virtual prey could not detect the predator, and the advantage of coordinated motion depended on boundary/occlusion effects in the arena. Polarised groups were less at risk mostly near the projection boundary.
- Demšar et al. 2015 (MP-03): with "non-confusing" prey (P_success = 1), mean catches per 600-step run were 5.357 against 1.522 for default prey. Most of the collective benefit in these models comes from the confusion term, so p2's capture-rate result will partly reflect that modelling choice.
- None of the sources read injects a **non-random, input-fixed** error. All noise is either Gaussian angular noise, independent across agents (Couzin 2002, MP-01), or stochastic Markov-network outputs. The p2 question (correlated, view-determined errors) is untested in this literature (inference).

---

### SP-01 Predator confusion is sufficient to evolve swarming (Olson et al. 2013)
1. **Source.** Olson RS, Hintze A, Dyer FC, Knoester DB, Adami C (2013). "Predator confusion is sufficient to evolve swarming behaviour." J. R. Soc. Interface 10(85): 20130305. arXiv:1209.3330v3. https://arxiv.org/abs/1209.3330. Accessed 2026-10-06. Read level: **full text** of arXiv v3 (Introduction, Methods 2.1–2.4, Results 3.1–3.4, start of Discussion); SI not read.
2. **Local view and representation.** Discrete, sector-based ("pixelated retina") and limited-distance. Prey: 180° frontal FOV split into 12 sectors of 15°, range 100 units, with two layers (conspecific layer and predator layer). Each sector reports only **presence** of a type, not count. Predator: one layer, 12×15° (180° frontal), range 200. The view is neither metric k-neighbour nor topological: it is a binary occupancy per sector within a range.
3. **Per-agent decision and dimensionality.** Discrete, 4 options: (1) stay still; (2) move forward 1 unit; (3) turn left 8° and move forward 1; (4) turn right 8° and move forward 1. Encoded by two binary outputs L and R. The controller is a Markov Network (a stochastic state machine with memory), evolved by a GA. The predator turns 6° per step and moves 3× faster than prey.
4. **Predator model and interaction.** One embodied, coevolving predator. When it is within 5 units of a visible prey it attacks automatically, with a handling time of 10 steps between attempts. Confusion: **P_capture = 1 / A_NV**, where A_NV = number of prey visible to the predator (anywhere in its visual field) within 30 units of the target. The authors call this functionally equivalent to models based on total swarm size. Arena: closed 512×512.
5. **Noise or error.** Stochasticity is internal to the Markov Network (probabilistic logic gates). It is not an injected error, and it is not described as independent across agents. Prey are **clonal** (50 copies of one genome), "to eliminate any possible effects of selection on the individual level." The spread of errors between agents was not measured.
6. **Collective metrics, baselines, N, horizon, replicates, effect sizes.** N = 50 prey, 1 predator; 2,000 steps per evaluation; 1,200 generations; 180 replicates. Fitness: W_predator = Σ_t (S − A_t), W_prey = Σ_t A_t (S = 50, A_t = prey alive at t). Metrics:
   - swarm density = mean number of prey within 30 units of each prey over the lifespan;
   - swarm dispersion = mean distance to the nearest prey, over living prey and over the lifespan;
   - survivorship = surviving prey at the end.

   Results at generation 1,200 (mean ± SE):
   | Metric | With confusion | Without confusion |
   |---|---|---|
   | Swarm density | 12.48 ± 0.8 | 0.69 ± 0.02 |
   | Dispersion (nearest-prey distance) | 22.54 ± 1.32 | 46.69 ± 0.44 |
   | Survivors | 34.7 ± 0.6 | 25.54 ± 0.49 |

   Cohesive swarms formed in 70% of replicates with confusion and in none without it. With a predator FOV ≤ 60° the density was 0.68 ± 0.02; at FOV ≥ 120° it was 6.13 ± 0.76. Evolved prey **ignored the predator** and reacted only to conspecifics.
7. **Evidence type.** Simulation (evolutionary). Code https://github.com/adamilab/eos, data https://github.com/adamilab/eos-data (as stated in the paper; repositories not opened).
8. **Relevance to p2 (inference).** This is the closest published match to p2's discrete sector view plus a binary-ish turn decision.
   - **Can copy:** the sector encoding; the P_capture = 1/A_NV confusion rule; the density and dispersion metrics; the use of clonal agents. p2's decision models are effectively clonal, which is exactly why their errors are input-fixed.
   - **Contradicts:** the assumption that turning away from the predator is what protects the group. Here, following conspecifics alone sufficed.
   - **Leaves untested:** the effect of deterministic, input-fixed decision errors; a fixed (non-evolved) reference rule; capture outcomes on a torus with a non-evolving predator.

### SP-02 Selfish herd: attack mode decides whether grouping evolves (Olson, Knoester, Adami; with Hamilton 1971)
1. **Source.** Olson RS, Knoester DB, Adami C. "Evolution of swarming behavior is shaped by how predators attack." arXiv:1310.6012v2 (24 Nov 2015). https://arxiv.org/abs/1310.6012. The journal version (reportedly Artificial Life, 2016) is **not verified**. Read level: **full text** of arXiv v2 (Abstract, Methods §3–3.1, Table 1, §4 Artificial Predation including 4.1–4.4). Coevolution sections were skimmed only.
   Secondary original: Hamilton WD (1971). "Geometry for the selfish herd." J. Theor. Biol. 31: 295–311. PDF http://www.csun.edu/~dgray/BE528/Hamilton1971Selfish_herd.pdf. Read level: **full text, first pages only** (abstract and §1, the one-dimensional "frogs on a pond rim" model).
2. **Local view and representation.** Olson et al.: 360° retina, range 200, split into 24 sectors of 15°. Each sector reports the presence of a conspecific and of a predator, not the count. Toroidal 736×736 arena. Hamilton: no perception model. Each animal has a "domain of danger", the region of points closer to it than to any other animal.
3. **Per-agent decision and dimensionality.** Olson et al.: two binary outputs encode 4 actions: 00 forward, 01 turn right, 10 turn left, 11 stay still (Table 1). Markov Network controller. Hamilton: movement to reduce one's own domain of danger (a jump to the gap between neighbours in 1D).
4. **Predator model and interaction.** Olson et al. compared artificial (disembodied) attack modes: random location → nearest prey; random walk; attack from outside the group → nearest prey; high-density-area attacks. Also density-dependent capture, P_capture = 1/A_density, and an embodied coevolving predator. One attack every 4 steps after a 250-step predation-free period; artificial attacks always succeed. Hamilton: the predator appears at a random point and takes the nearest prey.
5. **Noise or error.** Stochastic MN outputs only. Prey are selected individually (fitness = survival time T), not clonally. No inter-agent error spread was measured.
6. **Collective metrics, baselines, N, horizon, replicates, effect sizes.** N = 250 prey; 1,000 steps; 40,000 generations; 100 replicates. Metric: swarm density = mean number of prey within 30 units, averaged over the lifespan. Thresholds as stated: ≥ 15 "cohesive swarming", 5–15 "loosely grouping", ≤ 5 "random, non-grouping". Findings:
   - No attacks → completely dispersive behaviour.
   - Random attacks → swarming took "upwards of 5,000 generations", compared with under 1,000 for the other modes.
   - Outside attacks → fastest selfish-herd evolution.
   - The authors state that Hamilton's assumption that attack mode has no impact on the evolution of swarming "is not corroborated by this model".
7. **Evidence type.** Simulation (evolutionary); Hamilton is theory. Code https://github.com/adamilab/eos-selfish-herd, data on figshare (as stated; not opened).
8. **Relevance to p2 (inference).** p2's capture rate and cohesion will depend strongly on the predator's attack rule (nearest prey, edge prey, random). The predator rule should be fixed and reported, and ideally varied as a robustness factor. The 4-action encoding via two binary outputs shows that published work does use binary per-agent outputs. p2 drops "forward" and "stay" and keeps only left/right. Nothing published here tests an always-turning agent: an agent forced to turn every step mills by construction unless the turns alternate. Check that the p2 rule-only baseline can produce straight motion at all.

### SP-03 Real predators attacking virtual prey (Ioannou, Guttal & Couzin 2012)
1. **Source.** Ioannou CC, Guttal V, Couzin ID (2012). "Predatory fish select for coordinated collective motion in virtual prey." Science 337(6099): 1212–1215. doi:10.1126/science.1218919. Author copy at https://d-nb.info/1130587576/34 (KOPS). Accessed 2026-10-06. Read level: **full text of the main paper** (all 4 pages). The supplementary materials (model details, null-predator method) were **not read**.
2. **Local view and representation.** Couzin-type zonal model (attraction, orientation and "ignore" weights). Neighbour range details are in the SM, not read. Periodic (torus) projection boundaries.
3. **Per-agent decision and dimensionality.** Continuous heading. Each of 16 prey has three trait weights w_a, w_o, w_p (attraction, orientation, ignore), summing to 1.
4. **Predator model and interaction.** A **real** bluegill sunfish attacking prey projected on a screen. Prey **cannot detect or respond** to the predator. Only the first attack per fish was analysed. A "null predator" chose prey at random at the same time steps as the real attacks, to give the expected targeting baseline.
5. **Noise or error.** Behavioural heterogeneity is set by traits. Noise details are in the SM (not read).
6. **Collective metrics, baselines, N, horizon, replicates, effect sizes.** N = 16 prey; 70 attacks in experiment 1 (the largest count on one prey type was 14). Metrics:
   - group size by interconnected prey, every 250 steps;
   - tortuosity, every 100 steps;
   - polarisation, with "group tortuosity = 1 – group polarization" (Fig. 3 legend).

   Attraction × orientation interaction on attack risk: GLM LRT(1,12) = 11.43, P = 0.00072. The predator's decision time increased with target group size (LRT(1,67) = 11.32, P = 0.00077), consistent with confusion. Risk depended on vertical position in the projection, i.e. on boundary effects.
7. **Evidence type.** Empirical with simulated prey (hybrid). The paper states "Data and code are freely available at http://icouzin.princeton.edu" (not opened).
8. **Relevance to p2 (inference).** The **null-predator baseline**, a random target at the same attack times, is a clean way to separate "who gets caught" from predator targeting, and p2 could copy it for its capture outcome. The paper also shows that group protection can arise with prey that do not react to the predator. p2 should report capture rate for an "ignore-the-predator" (neighbour-only) baseline as well as for the full rule.

### SP-04 Hidden visual networks predict escape cascades (Rosenthal et al. 2015)

> **Cross-reference.** Same source as [EC-01](error-and-contagion.md#ec-01-rosenthal-et-al-2015-startle-cascades-in-golden-shiners-fractional-contagion-on-visual-networks), the primary card (fuller read); counted once in the catalogue.

1. **Source.** Rosenthal SB, Twomey CR, Hartnett AT, Wu HS, Couzin ID (2015). "Revealing the hidden networks of interaction in mobile animal groups allows prediction of complex behavioral contagion." PNAS 112(15): 4690–4695. doi:10.1073/pnas.1420068112; PMC4403201 (https://pmc.ncbi.nlm.nih.gov/articles/PMC4403201/). Accessed 2026-10-06. Read level: **full text** of the Abstract, Introduction and Results up to the network-reconstruction section (Figs 1–3 legends). Later results, methods and SI were not read.
2. **Local view and representation.** Empirical visual field per fish, reconstructed by ray casting from body posture and eye position. Candidate features: metric distance, topological distance, angular position, angular area, ranked angular area. The best two predictors were **log metric distance** and **ranked angular area**. Visual occlusion strongly prevents response.
3. **Per-agent decision and dimensionality.** Binary: respond (fast-start startle) or not. Response probability P(i|j) = 1 / (1 + exp(−β1 − β2·LMD − β3·AR)), with β1 = 0.302, β2 = −1.421, β3 = −0.126 (fit to first responders).
4. **Predator model and interaction.** No predator. Spontaneous startles serve as the stimulus. A mechanosensory alarm stimulus was used for comparison.
5. **Noise or error.** The key finding for p2: fish showed **no difference** in response to spontaneous (no-threat) startles and to threat-induced startles. Spontaneous startles occur about once per 3.3 h per individual. A false alarm by one individual propagates like a true one. Spread was measured: cascade size had a broad distribution, and waves travelled at about twice the maximum swim speed.
6. **Collective metrics, baselines, N, horizon, replicates, effect sizes.** About 150 fish per school (150 ± 4); 138 spontaneous evasion events. Network edge weight w_ij = P(i|j), directed and weighted. The initiator's weighted directed local clustering coefficient predicted cascade magnitude (Fig. 3C). Three contagion models (fractional, numerical, simple) were compared in simulation (Fig. 3D).
7. **Evidence type.** Empirical plus model fitting. Code and data availability not checked.
8. **Relevance to p2 (inference).**
   - Supports p2's temporal outcome: errors can spread through neighbours who cannot tell an erroneous move from a correct one.
   - Offers a measurable propagation quantity: cascade size from a single initiator, i.e. how many agents changed decision because of one agent's error.
   - Suggests a structural predictor: local clustering of the initiator in the interaction network.

   Caveat: p2 uses k = 3 topological neighbours, whereas here metric distance plus visual ranking beat pure topological distance.

### SP-05 Boids: three prioritised local rules (Reynolds 1987)
1. **Source.** Reynolds CW (1987). "Flocks, herds, and schools: A distributed behavioral model." Computer Graphics 21(4) (SIGGRAPH '87), 25–34. HTML version at https://www.cs.toronto.edu/~dt/siggraph97-course/cwr87/ (the author's page red3d.com returned 403 to curl; a fetch summary confirmed the citation). Accessed 2026-10-06. Read level: **full text** (HTML) sections "Simulated Flocks", "Arbitrating Independent Behaviors", the perception/neighbourhood discussion and "Algorithmic Considerations".
2. **Local view and representation.** Continuous and metric. "A spherical zone of sensitivity centered at the boid's local origin", with sensitivity "an inverse exponential of distance", so two parameters: radius and exponent. A forward-weighted zone is suggested but not implemented. Reynolds stresses that flocking "depends upon a limited, localized view of the world". With a central force (global) model, scattered flocks converge unnaturally.
3. **Per-agent decision and dimensionality.** Continuous acceleration. Three urges, "in order of decreasing precedence": Collision Avoidance, Velocity Matching, Flock Centering. They are combined by **prioritized acceleration allocation**: requests are accumulated in priority order until a maximum acceleration budget is used up. Reynolds rejected simple weighted averaging because opposite urges "largely cancel out", causing indecision.
4. **Predator model and interaction.** None in the model. Predators are mentioned only as an evolutionary motive for flocking.
5. **Noise or error.** No noise model described in the sections read.
6. **Collective metrics, baselines, N, horizon, replicates, effect sizes.** None. "The success and validity of these simulations is difficult to measure objectively." Validation was visual. The algorithm is O(N²).
7. **Evidence type.** Demonstration (computer animation).
8. **Relevance to p2 (inference).** The p2 reference rule (predator escape first, otherwise neighbour majority) is a strict-priority arbiter in Reynolds' sense, so p2 can cite it as the precedent for priority rules over averaging. Reynolds' cancellation argument also supports a binary forced choice: a classifier answering left/right cannot "average" to straight ahead. Reynolds offers no metrics, so take quantitative definitions from MP-01 and MP-02.
