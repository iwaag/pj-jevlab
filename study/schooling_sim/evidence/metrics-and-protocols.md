# Evidence: metrics and protocols for schooling-under-predation simulations

- Searcher areas: (5) metrics and protocols (cards MP-xx). The models whose metrics are quoted are carded in `schooling-and-predation.md` (SP-xx).
- Access date: 2026-10-06.
- Read-level legend: **full text** = PDF or HTML of the primary source read, with sections named; **abstract only**; **fetch summary** = a small-model summary of a web page; **search summary** = a search-engine snippet only. "Not verified" = could not be checked against the primary source.

## Summary: positive and negative/qualifying results

**Formulas p2 can adopt verbatim** (2D; u_i = unit heading of agent i; c_i = position; c = centroid; N = agents alive):
- **Polarisation (order parameter):** O_p = | (1/N) Σ_i u_i |. Couzin et al. 2002, eqn 4 (MP-01); Tunstrøm et al. 2013 (MP-02).
- **Rotation / milling order parameter:** O_r = | (1/N) Σ_i u_i × r_i |, with r_i the **unit** vector from the centroid to agent i (Tunstrøm 2013). In 2D the cross product is the scalar u_x r_y − u_y r_x. Couzin 2002 eqn 5 writes r_ic = c_i − c_group without stating normalisation, yet gives the range [0, 1]. Use Tunstrøm's unit-vector form. On a torus the centroid needs care (unwrap, or use a circular mean per axis). That is our note, not from the sources.
- **State classification** (Tunstrøm 2013):
  - polar: O_p > 0.65 and O_r < 0.35;
  - milling: O_p < 0.35 and O_r > 0.65;
  - swarm: O_p < 0.35 and O_r < 0.35;
  - otherwise transitional.

  Robustness was checked with threshold k = 0.25, 0.35 and 0.40, where polar means O_p > 1−k and O_r < k.
- **Cohesion:**
  - swarm density = mean number of other agents within radius R of each agent (R = 30 units in SP-01 and SP-02);
  - dispersion = mean nearest-neighbour distance over living agents (SP-01);
  - fragmentation = connected components of the "within perception" graph (Couzin 2002, equivalence classes);
  - group size = number of interconnected prey (SP-03).
- **Predation:**
  - capture count per run, and survivors at the end of the run;
  - kill rate k = mean prey consumed per step (SP-01 fitness ∝ k);
  - attack efficiency = successful attacks / total attacks (SP-01);
  - confusion: P_capture = 1/A_NV (SP-01, reused in MP-03).

**Protocol numbers reported** (for sizing p2):
| Source | N | Horizon | Replicates |
|---|---|---|---|
| Couzin 2002 | 10–100 (N = 100 in Fig. 3) | ≤ 5,000 steps to a stable state; 2,000 steps per parameter value in the hysteresis runs | 30 per parameter combination; 15 for hysteresis |
| Tunstrøm 2013, simulation | 30 / 70 / 150 / 300 | 2,500 steps (state recorded at the final step) | 500 per speed value |
| Tunstrøm 2013, experiment | 30 / 70 / 150 / 300 fish | 56 min at 30 fps | 7, 7, 7, 3 |
| Olson 2013 | 50 prey, 1 predator | 2,000 steps | 180 |
| Olson et al. 2015 preprint | 250 prey | 1,000 steps | 100 |
| Demšar 2015 | 100 prey | 600 steps | 20 evolutionary replicates; direct competition: 1,000 prey groups × 3 prey settings, 600,000 runs in total |

**Negative / qualifying:**
- No source read defines a **noise-matched baseline**, i.e. a rule plus random error at the same error rate as a model. Noise in Couzin-type models is a Gaussian angular perturbation (σ ≤ 0.2 rad) applied independently per agent. Its effect is reported only qualitatively (more noise → swarm-like states, more fragmentation). The p2 "rule + injected random error at a matched rate" baseline appears to be new. Its matching criterion (matching the per-decision error rate, and perhaps the left/right error asymmetry) must be defined by p2 itself (inference).
- Demšar 2015 shows that a modelling switch (confusion on or off) changes the mean catch about 3.5-fold. Capture-rate comparisons are only meaningful against the same predator and confusion model.
- Tunstrøm 2013 smooths O_p and O_r over 30 frames (1 s) before classifying states. Unsmoothed per-step values on small N fluctuate more. p2 should either smooth or report a time-averaged value.
- Milling (high O_r) is a common attractor in Couzin-type models and real fish. A binary left/right agent biased to one side may produce milling that registers as low polarisation without fragmentation. Report O_r, not only O_p (inference).

---

### MP-01 Canonical polarisation, angular momentum and zonal model (Couzin et al. 2002)
1. **Source.** Couzin ID, Krause J, James R, Ruxton GD, Franks NR (2002). "Collective memory and spatial sorting in animal groups." J. Theor. Biol. 218: 1–11. doi:10.1006/jtbi.2002.3065. PDF copy at https://jmvidal.cse.sc.edu/library/couzin02a.pdf. Accessed 2026-10-06. Read level: **full text** of "Behavioural rules: description", "Analysis of the model" (eqns 1–6, Table 1), the collective-states description and "Hysteresis and behavioural transitions" (Figs 3–4 legends).
2. **Local view and representation.** Continuous, **metric**, 3D. Three non-overlapping zones: repulsion radius r_r, orientation r_o (width Δr_o = r_o − r_r), attraction r_a (width Δr_a = r_a − r_o). A **blind volume** behind the agent is a cone of interior angle (360 − α)°, where α is the field of perception (200–360° explored; 270° in Fig. 3).
3. **Per-agent decision and dimensionality.** Continuous desired direction d_i. Steps:
   - If n_r > 0: d_r = −Σ_{j≠i} r_ij/|r_ij|, with absolute priority.
   - Otherwise: d_o = Σ v_j/|v_j| over the orientation zone; d_a = Σ r_ij/|r_ij| over the attraction zone. Use d_o or d_a if only one zone is occupied, and ½(d_o + d_a) if both are.
   - If the social terms give a zero vector or nothing is detected, keep v_i.

   The agent then turns towards d_i, limited to a maximum turn of θτ per step (turning rate θ = 10–100°/s, τ = 0.1 s). Speed is constant, s = 1–5 units/s.
4. **Predator model and interaction.** None.
5. **Noise or error.** d_i is rotated by an angle drawn from a spherically wrapped Gaussian with SD σ (0–0.2 rad). It is drawn independently per agent per step. Individual differences (speed, turning rate, error, zone sizes) are drawn once per agent and fixed. In MP-01 this sorts agents spatially: e.g. faster agents end up at the front. That is a precedent for **fixed per-agent idiosyncrasy** as distinct from per-step noise. Spread of errors between agents was not measured.
6. **Collective metrics, baselines, N, horizon, replicates, effect sizes.** Formulas, verbatim from the paper:
   - eqn 4: p_group(t) = (1/N) | Σ_{i=1}^{N} v_i(t) |;
   - eqn 5: m_group(t) = (1/N) | Σ_{i=1}^{N} r_ic(t) × v_i(t) |;
   - eqn 6: r_ic = c_i − c_group and c_group(t) = (1/N) Σ c_i(t). Both measures are stated to lie in [0, 1].

   Fragmentation is computed via equivalence classes (connected components) under the criterion "within field of perception". There are four states: swarm (low p, low m); torus (low p, high m); dynamic parallel (high p, low m); highly parallel (very high p). There is **hysteresis**: the state depends on the path through Δr_o. Settings: N = 100 (Fig. 3; range 10–100); stable state within 5,000 steps; Fig. 3 uses 30 replicates per parameter combination; the hysteresis runs use 2,000 steps per r_o value and 15 replicates. Initial condition: random orientations, positions within a sphere in which each agent detects at least one other. Rank correlations (Spearman ρ) link individual traits to position.
7. **Evidence type.** Simulation. No code link in the paper.
8. **Relevance to p2 (inference).** The source of p_group and m_group. p2 should use the normalised unit-vector form for m (see MP-02). Hysteresis means the initial condition, e.g. starting polarised vs random, must be fixed and reported. The "fixed per-agent trait" protocol is close to p2's input-fixed errors and could serve as a third baseline: a fixed random per-agent bias, as opposed to a fixed per-input error.

### MP-02 Order parameters O_p, O_r and state thresholds (Tunstrøm et al. 2013)
1. **Source.** Tunstrøm K, Katz Y, Ioannou CC, Huepe C, Lutz MJ, Couzin ID (2013). "Collective states, multistability and transitional behavior in schooling fish." PLoS Comput. Biol. 9(2): e1002915. doi:10.1371/journal.pcbi.1002915. Accessed 2026-10-06. Read level: **full text** of Results/Discussion (order-parameter definitions, group-size results, state transitions), Methods (order parameters, density plots, defining states, simulations) and the Fig. S3 legend.
2. **Local view and representation.** Experiment: tracked golden shiners. Simulation: Couzin et al. 2002 model in 3D, zones 1 / 3 / 15, field of perception 270°.
3. **Per-agent decision and dimensionality.** Simulation: continuous heading (Couzin 2002), with turning rate 60° and error 0.2 rad.
4. **Predator model and interaction.** None.
5. **Noise or error.** Simulation error 0.2 rad (independent Gaussian, per Couzin 2002). Experimental tracking error: frames with tracking accuracy above 80% made up 88% / 91% / 80% / 71% of frames for 30 / 70 / 150 / 300 fish.
6. **Collective metrics, baselines, N, horizon, replicates, effect sizes.**
   - O_p = | (1/N) Σ u_i |, with u_i the unit direction of fish i.
   - O_r = | (1/N) Σ u_i × r_i |, with r_i the **unit vector** from the shoal's centre of mass to fish i. Both lie in [0, 1].
   - Both are smoothed with a 30-frame (1 s) moving average.
   - States: P if O_p > 0.65 and O_r < 0.35; M if O_p < 0.35 and O_r > 0.65; S if O_p < 0.35 and O_r < 0.35; otherwise transitional (T). Qualitative results held for k = 0.25 / 0.35 / 0.40 (Fig. S3).
   - A transition counts only on moving from one of P/M/S to a different one. Going P → T → P is not a transition.
   - Fraction of time polarised fell with group size: 0.57, 0.26, 0.18, 0.05 for N = 30 → 300. Milling rose: 0.03, 0.18, 0.36, 0.45. Transition rates were 2.0, 1.4, 1.2, 0.8 per min.
   - Experiment: 7 replicates for N = 30, 70, 150 and 3 for N = 300, each 56 min at 30 fps.
   - Simulation: speed 0.1–4.1 in steps of 0.1, 500 replicates per speed, 2,500 steps, order parameters recorded at the last step.
   - Packing fraction via alpha-shape area.
7. **Evidence type.** Empirical plus simulation. Data availability not checked.
8. **Relevance to p2 (inference).** p2 can adopt these definitions **verbatim**: O_p, O_r with unit r_i, the 0.65/0.35 state thresholds, and the transition definition. The time-in-state fractions give a richer collective outcome than mean polarisation alone. Smoothing and the k-sensitivity check are ready-made robustness steps. The strong dependence of milling on N means p2 must fix N and report it, and should ideally run two N values.

### MP-03 Predator-attack simulation protocol, capture counts and confusion ablation (Demšar et al. 2015)
1. **Source.** Demšar J, Hemelrijk CK, Hildenbrandt H, Lebar Bajec I (2015). "Simulating predator attacks on schools: Evolving composite tactics." Ecological Modelling 304: 22–33. Preprint PDF: http://itzsimpl.info/papers/Dem%C5%A1ar.etal.2015.Simulating%20predator%20attacks%20on%20schools-%20evolving%20composite%20tactics.Preprint.pdf. Accessed 2026-10-06. Read level: **full text of the preprint**: §2 model (prey drives, eqns 1–9), §2.3 experiments (Tables 1–2, catch rule eqn 12), §2.4 tactics, §3.3 direct competition. Not compared against the published version.
2. **Local view and representation.** Continuous, metric, 2D. Prey field of view 300° (60° blind angle behind). Zones: separation 5 BL, alignment 25 BL, cohesion 100 BL, escape 100 BL (BL = body lengths). The predator has a 360° view.
3. **Per-agent decision and dimensionality.** Continuous acceleration a = w_s a_s + w_a a_a + w_c a_c + w_e a_e, with weights 5, 0.3, 0.01 and 5. Escape drive: a_e = −d̂_p (1 − |d_p|/r_e) if the predator is visible and within r_e, else 0. Prey behaviour is fixed (not evolved). The predator's tactic parameters evolve: probabilities of attacking the nearest, the most peripheral or the most central prey, or a "dispersing" tactic.
4. **Predator model and interaction.** One predator, 1.5× faster than prey and less manoeuvrable. Its first attack comes from behind, starting 200 BL south of the group centre. It makes a catch attempt within the catch distance with **P_success = 1/|N_co|**, the number of prey within its confusability radius r_co (after Olson 2013). Handling time applies after a catch and refocus time after a confused failure. Pursuit stops if the target leaves the hunting zone. Ablations:
   - "prey with delayed response": escape zone 50 BL, escape weight 12;
   - "non-confusing prey": P_success = 1.

   Controls: always random, always peripheral, always nearest, always central.
5. **Noise or error.** Randomised initial positions (100 prey in 100 BL²) and headings (north ± 0.05 rad) per group. No per-decision noise is described in the sections read. Spread of errors between agents was not measured.
6. **Collective metrics, baselines, N, horizon, replicates, effect sizes.** N = 100 prey; 600 steps (Δt = 1 s); predator population 100; 500 generations; 20 replicates. Direct competition: each evolved predator was run against the same 1,000 prey groups in each of 3 prey settings, 600,000 simulations in total. Outcome: number of caught prey per 600-step run, which ranged 0–9. Mean catches (95% CI):
   | Prey setting | Mean catches |
   |---|---|
   | Default prey | 1.522 (1.517–1.527) |
   | Delayed response | 1.327 (1.322–1.332) |
   | Non-confusing prey | 5.357 (5.35–5.363) |

   The best predator against default prey was the dispersing tactic, with 2.773 (2.757–2.787). CIs are bootstrapped.
7. **Evidence type.** Simulation. Code availability not stated in the sections read.
8. **Relevance to p2 (inference).** A template for p2's capture outcome:
   - run each condition against the **same set of initial prey configurations** (common random numbers);
   - report the catch-count distribution with bootstrap CIs;
   - include fixed-tactic predator controls;
   - include a confusion on/off ablation, since confusion alone changed mean catches about 3.5-fold.

   The 2D, finite-horizon, single-predator setup with an attack from behind is directly transferable to p2. p2 uses a torus, so it needs a rule for where the predator starts.
