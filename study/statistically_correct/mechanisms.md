# Mechanisms, conditions and failure boundaries

Step 4 deliverable. Built from [catalog.md](catalog.md) and the cards in [evidence/](evidence); card IDs (S-, C-, G-, M-) point there. Compiled 2026-10-06. Labels: **[Source]** what a source reports, **[Inference]** this survey's reading, **[Local]** a lab note, used as a lead only. No universal acceptable error rate is inferred; numbers stay with their settings.

## 1. Mechanism by error-structure matrix

Rows are the mechanisms from the plan. Columns are the error structures of the framing. Cells say what the cited work supports; "no evidence" means no card, not proof of absence.

| Mechanism | Independent noise | Shared (same-model, same-input) errors | State-dependent errors | Persistent or temporally correlated errors | Adversarial or arbitrary faults |
|---|---|---|---|---|---|
| **Averaging or voting (absorb)** | Works: S-01, S-03, G-05, C-03. Gain depends on the independence assumption | Fails or stalls: S-01 (easy/hard), G-06, S-04/M-01, S-05, S-06, S-11. Measured on LLMs | Same as shared when the hard states coincide: S-01 Theorem 3 gives Pr(easy), not 1; S-11 clusters at ambiguous spec parts | Not covered by the cards | Tolerated only with a bound on the faulty share: C-01, C-02 |
| **Redundancy with explicit structure (correct)** | Works below a stated threshold: S-08, S-09, S-10 | Not addressed; the theorems assume independent faults | Not addressed | S-10 allows bounded-probability faults with repair | C-01 (more than two thirds loyal for oral messages), C-02 |
| **Constraints, environmental feedback, recovery (correct)** | M-12: expected-versus-observed comparison, vendor report | M-09, M-12: failures such as norm errors persist | M-13, M-15: removing conspicuous faults (stuck, jerky) changed human-likeness judgements | M-12 argues a small hallucination rate can compound; argued, not measured | No evidence |
| **Interaction among agents (absorb or amplify)** | C-08: independence plus interdependence finds the best site | G-03, G-04, S-02, G-07: imitation can lock in or amplify early noise | C-08: without independence, consensus not robustly on the best site | G-07: histories diverge from the same start | C-06: strongly opinionated minority captured by uninformed majority |
| **Variability on purpose (variab.)** | G-08 (needs a cooling schedule), G-09 (structured beats uniform), C-09, C-11 (models); G-11 and M-17 are nulls | Benefit conditional: C-09 benefit appears when cues are correlated and independent mixed | C-09 only | No evidence | No evidence |
| **Statistical bias as steering (steer)** | C-10 (weak preferences give sharp thresholds), G-01 (noisy response to payoffs) | C-05, C-06 (minority steering), M-16 and M-18 (designers adjust accuracy or displayed odds; no evaluation) | G-02: rare errors choose among equilibria | G-02 | C-06 |
| **Escalation or override** | Local leads only ([Local] [hype_and_reality](../hype_and_reality/README.md): confidence gates, review bands, regex rules first; graded B and C there) | Not tested: confidence is not an error rate (M-07: more than 0.99 probability on one option) | Not tested | Not tested | Not tested |

## 2. Mechanism sections

Each section lists prerequisites, evidence, a counterexample or unresolved limit, and how the sources define and evaluate success.

### 2.1 Averaging, voting and population scale

- **When justified [Source].** Aggregation reduces error when members err independently or when their errors differ (ambiguity): S-03 gives ensemble error equal to mean member error minus disagreement, so identical members add nothing. For binary factual questions with independent voters better than chance, the jury theorem and its noisy-voter descendants give growth in group accuracy with size (S-01, G-05). Under Mallows-type noise, the choice of rule matters: plurality needs exponentially many samples where pairwise-majority-consistent rules need logarithmically many (G-05).
- **What must be measured first [Inference].** The dependence of the deciders' errors. S-05 supplies a usable measure (effective votes from error correlation, nine judges giving about two) and S-04/M-01 shows agreement on mutual errors of 0.60 against 1/3 chance in one dataset. Population size is not the quantity that matters; effective sample size is.
- **Counterexamples.** Easy/hard structure (S-01 Theorem 3); positive correlation can make bigger juries worse up to a size (G-06); polling-style aggregation shows no consistent gain at 25x cost on binary truthfulness questions (S-06); a panel of nine does not beat its best member (S-05); M-04 is a positive counterpart (12 different LLMs matching 925 humans on 31 forecasting questions), but with few questions and different models.
- **Success definition.** Group accuracy or Brier score against a truth, or against labelled items. None of these sources defines success for preference aggregation. G-05 explicitly applies only where an objective truth exists; M-08 is the only card on model agents voting over interests, and it reports a diversity-versus-human-alignment trade-off set by temperature rather than an accuracy.
- **Factual versus preference voting [Inference].** The theorems above license aggregation of factual judgements. A village voting over conflicting interests has no true answer, and none of these results transfers; social choice offers axioms, not accuracy bounds.

### 2.2 Constraints, environment feedback and reversible choices

- **Evidence is thin.** M-09 and M-12 show failure modes persisting in interactive populations (erratic location choices, norm misclassification, over-cooperation) and M-12 reports a feedback module comparing expected and observed outcomes as helpful, as a vendor report with preliminary results. M-13 and M-15 show that removing conspicuous faults (stuck states, jerky motion) changed how humans judged agents.
- **Prerequisites [Inference].** The invalid-action category of the framing is removable by constraints (code filters legal actions). Wrong-but-legal actions are not: [Local] the JEVfire demo author states "a legal choice can still get a villager killed" ([jevfire-village](../game/examples/jevfire-village.md)).
- **Limit.** No card compares a constrained system with an unconstrained one at a defined error rate; a design with reversible choices is not evaluated in any case.

### 2.3 Role diversity, different information and decentralised control

- **Diversity.** Different models help only to the extent that their errors differ (S-03, M-02). M-02 reports three small models from different families matching or beating a single large judge at roughly 7–8x lower cost, with the vendor's own model on the panel. S-04/M-01, S-05 and S-11 show the correlation among different models is substantial.
- **Different information.** C-08 and C-09 show that independence of information, not only of decision rules, is the active ingredient: bees assess independently and then recruit; small groups benefit when cues are partly independent.
- **Decentralised steering.** A small informed minority can steer (C-05) or be diluted by uninformed members (C-06); a strongly opinionated minority can also capture a group.
- **Heterogeneity in LLM populations.** Persona prompts do not reliably create it: M-06 (flattening), M-07 (aligned model near-deterministic), M-11 (persona wording sensitivity from 1 to 76 points across models). Real conditioning data supplied the heterogeneity in M-05.

### 2.4 Sample, bias, add noise, or stay deterministic

- **Sampling or noise as a design variable [Source].** G-08: convergence guarantees for annealing need a cooling schedule matched to the landscape; constant noise carries none. G-09: structured randomisation (Thompson) beats greedy and uniform dithering in a bandit when the prior is well specified. C-09 and C-11 give a no-noise comparison inside models. G-10 requires a threshold, a weak signal and noise.
- **Nulls [Source].** G-11 reports no gain with good initialisation; M-17 (n = 10, unreviewed) finds mean survival 29.5 s (optimal guard) versus 31.1 s (suboptimal guard) and capture 59.2% versus 60.8%, a weak null that supports neither direction; G-13 removes the noise at deployment.
- **Probability quality [Source].** M-07: an aligned model assigned more than 0.99 probability to one option, unlike human response frequencies. M-06: raising temperature reaches human diversity at 1.4 where the text is incoherent. M-08: temperature trades diversity against human alignment. All three are generative LLMs; none tests label-scoring readouts.
- **Steering by bias [Source].** C-10: mild local preferences produce strong aggregate segregation with sharp thresholds, and 5–10% random movers change the outcome in one study; G-01 casts noisy choice as a response to payoffs, with the caveat that without restrictions a QRE can fit any behaviour.
- **Reading [Inference].** The cards support a general point: variability helps when it is *structured* (scheduled, uncertainty-driven, or matched to a threshold) and when the system has something to explore or a lock-in to escape. They do not support the claim that a fixed 10–20% error rate produces benefit; the closest cases (G-08 constant noise, G-11) are the ones without guarantee or with null results. They do not show that a real model's errors have the structure of injected noise.

### 2.5 Escalation to an LLM or a rule-based override

- **No card tests it.** The plan asks when the latency and cost are worth it; the only material is [Local]: [hype_and_reality](../hype_and_reality/README.md) reports documented successes with a safeguard (confidence gate plus escalation, human review band, rules first, LLM escalation), graded B and C and not re-verified here. [Local] [Werewolf](../game/examples/jev-werewolf.md): an abstention threshold lowered the win rate (28% versus 50%, 50 games per condition, author results).
- **Reason for caution [Source, Inference].** Escalation depends on a usable error signal. M-07 shows confidence can be far sharper than human frequencies; S-05/S-06 show unweighted aggregation of correlated judges does not improve. A confidence gate is valuable only to the extent that confidence ranks errors on the relevant distribution.
- **Gap.** Costs of escalation (latency, supervision) were not measured in any card.

### 2.6 Where none of these mechanisms helps

- **Common bias.** If all deciders share the same wrong tendency, voting converges to it (S-01 Theorem 3; S-04/M-01; S-05; S-11 failure clusters at ambiguous specification).
- **Unstable feedback.** Imitation amplifies early noise: G-03 (cascade probability tends to one as the number of individuals grows under the model), G-04 (reverse cascades 13/41 and 18/46 in two designs, from the PDF version read), G-07 (inequality and unpredictability rise with influence), M-10 (herding stronger than humans, appearing at 10,000 agents and not at 100).
- **Phase-like thresholds.** C-04: order lost above a noise threshold; C-10: sharp thresholds in segregation; S-08: above the gate-error threshold redundancy no longer helps. The thresholds belong to their settings.
- **Irreversible mistakes.** No card measures rare irreversible failures or distribution shift; [Local] Japanese options degraded jeff (13/18 to 5/18) in game_test/p2 ([report](../../devdocs/episodes/game_test/p2/report.md)).
- **Small-population sensitivity.** M-11: small prompt changes shift macro outcomes between models.

## 3. Where findings agree, differ or rely on incompatible assumptions

**Agree.** Aggregation benefits depend on error diversity (S-01, S-03, S-05, S-11, G-06, C-09). Imitation or social information can reduce that diversity (S-02, G-03, G-07, C-08). Weak local biases can steer aggregates (C-05, C-10). Nobody reports a free benefit of constant noise.

**Differ.**
- *Does noise help?* Annealing (G-08) and bandits (G-09) say yes with structure; gradient noise (G-11) says no when initialisation is good; C-09 says it helps with correlated cues; C-04 says noise destroys order. These ask different questions: optimisation, exploration, cohesion, order.
- *Do ensembles of LLMs help?* M-02, M-04 and S-07 report gains; S-05, S-06 and M-03 report that gains are small or absent when errors are shared. The sources differ in task (verifiable tasks versus judging), in whether members are from different families, and in whether gains are measured against a single model or the best model.
- *Do cascades matter?* G-03 predicts them in idealised Bayesian settings; G-04 finds them in the laboratory but with heuristics and small groups.

**Incompatible assumptions.**
- Theorems (S-01, S-08, S-09, G-05) assume independent faults or explicit encodings; the empirical LLM work (S-04, S-05, S-06, S-11) measures dependence; the two meet only in the conclusion that dependence must be measured.
- Factual truth-estimation results (G-05, S-05) and preference studies (M-08, G-01 fits) use different success definitions and cannot be pooled.
- Simulation papers (C-04 to C-12, M-09 to M-12) use their own objective (cohesion, similarity to human data); a benefit in one is not a benefit in another.
- Calibration: M-07 and M-06 concern generative LLMs; readouts differ. This is a transfer gap, not a contradiction.

## 4. What this step does not establish

- No universal error rate is supported. S-08's thresholds (about 1/6 for 3-input majority formulas, about 0.0886 for 2-input) are gate error rates for independent faults in fixed functions, not accuracy requirements for decisions.
- "Works despite errors" has more support (absorption and redundancy under independence; steering under bias) than "works better because of variability", which has support only in structured, narrow settings and one weak null in a player study.
- Gaps are not evidence of absence: correlated-voter theorems (Ladha, Boland) were not opened; self-stabilisation, gossip and stochastic-control stability were not retrieved; no adequately sized player study of deliberate NPC mistakes or randomness was found.
