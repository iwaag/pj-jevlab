# Reinvention check: the lab's experiments against arXiv, 2026-09-15 to 2026-10-07

For each lab experiment this file says:

- whether a recent paper already did it, did it in parallel, or extends it;
- what the lab has that the papers lack.

Paper claims come from the evidence cards in [evidence/](evidence/). Lab numbers come from the episode reports under `devdocs/episodes/` and from `lab/experiments/set4-advanced_method/p1/out/fresh_analysis.md`.

**Verdicts:**

| Verdict | Meaning |
|---|---|
| prior | A paper posted before the lab's report shows the same thing |
| parallel | The same result, posted within days of the lab's report |
| extends | A paper adds conditions, models or a mechanism |
| lab-only | No paper found |
| contradicts | A paper's result disagrees with the lab's |

**Scope warning:** almost every paper tests hosted Jev or small open models: Kev 0.8–9B, Laya, Open-Jev and Qwen 4–8B readouts. None tests Kev-27B (K27), Winnow-12B (W12) as a decision model, AutoJev-27B (A27) or jeff (J). LLM-as-Jev reports W12 only as a JevBench baseline score. So "already shown" means shown on other systems.

## Summary table

| Lab experiment (date) | Closest papers | Verdict | What the lab adds |
|---|---|---|---|
| set5: narrowed second pass on K27 = renormalised first pass (report 10-03) | 2610.07716 Readout Stability (10-06): menu-only changes are predicted within 4.2 pt by restricting and renormalising the cached first pass, over 7 families | **parallel** | K27 pointer head at 27B (the paper's Kev models are 0.8–9B); policy workload W3 with fallback classes; preregistered primary tests |
| set6 p1: one-model populations ≈ 1 effective vote; mixed-model panel 3.4–5.6 of 7 (10-06) | 2609.29769 (09-24): LLM judges repeat 96% of Jev's confident errors, juries never beat the best single judge; 2610.09188 (10-06): a second answer from the same judge is no substitute; 2609.36399: ICC 0.997 over repeated calls; 2609.27535 KITE: persona count 10→200 buys nothing | **prior / parallel** for the one-model half; **tension** for the mixed panel | n* measured against ground truth for persona, presentation and sampling populations; the only measurement of a mixed decision-model panel. The tension is likely a selection effect: 2609.29769 counts only Jev's most confident errors. Recompute the lab's n* on p ≥ 0.8 errors before claiming either |
| set4: three-model majority made things worse; unanimity no better than random review | 2609.29769; 2610.07177 (a cascade over a near-chance judge escalates 92–100%, no better than random); 2610.09683 (deferral gain ∝ actor AUROC, ρ 0.87; the most accurate actors gain nothing) | **prior** (mechanism) | Measured on W3 policy cases with fallback classes |
| set4 C1: answer-free "does the outcome depend on an unknown fact?" check on K27 | 2610.01006 (10-01): an answer-free sufficiency noul separates complete from incomplete evidence at AUROC 0.95 against 0.85 for confidence (hosted Jev) | **extends**, in both directions | On W2 the lab's C1 said yes for **14/16** missing-evidence vs 6/36 substantive cases, the same signal on K27. On W3 (policy with priorities) it caught **6/20** missing-evidence cases and **0/17** false executions. The paper has no priority-rule workload, so the lab shows where the method stops working. The lab applied C1 as a hard yes/no rule; P(yes) was never thresholded |
| set3 / benchmark p3: when a decisive fact is unstated, every system decides anyway at p ≥ 0.8 | 2610.01006 (up to 0.80 on a salient option with no information); 2609.34024 (Jev picks "I don't know" on 10.5% of unanswerable items); 2609.39496 (7% correct rejection with an explicit NONE option); 2610.03935 (89% on the mode vs 35% true); 2610.07730 SanSi (hard answer on 17.5% of key-evidence-removed items) | **prior / parallel** | Fresh blind-audited cases with fallback classes; the failure shown across 7 systems and 4 readouts. Not yet tried by the lab: fallback-probability threshold, counterfactual fact probing (see [ideas.md](ideas.md)) |
| set1 / set2 / game_test: a key-naming sentence in the state is followed by every decision model (59/60); opaque keys do not fix it | 2609.31142 JevAdvBench: on hosted Jev, commands naming the target key flip 8–10%, an observer opinion without a command flips 12.1%; 2609.26758 and 2610.02586: the option *label* overrides its *definition*, caused by the rendering `"{label}: {definition}"`; 2610.00346: trained decoder heads (Kev-9B etc.) resist the yes/no label swap (≤6.5 flips/100) | **extends** (different attack) | The lab's attack is a state sentence naming a key, not a label/definition conflict. No paper tests it on Kev-class models. The lab's rate (59/60) is far above hosted Jev's 8–10% for key-naming commands, but the attack template differs. **Checked here:** Kev renders options as `"{name}: {description}"` (`kev/api.py:58` in the local checkout), so the key string is in the model input and an opaque key is still an exact lexical match. This is a hypothesis for why opaque keys failed; it is not tested |
| set3 p2: supplied priority swaps separate systems (K27, A27 4/4; W12, L27 1/4) | 2609.33689: a fine-tuned typed encoder returned its training answer for 98–99.5% of changed questions while its calibrated gate kept acting; paraphrase tests cannot detect this | **extends** | Confirms that swap pairs are the right test; the lab already uses them |
| benchmark p3: option reversal flips J 21/60, G 14/60 | 2610.02267: Laya flips 30.3% under reversal vs 1.8% for hosted Jev; 2610.00831 AnyJev: rotation averaging cuts flips 0.33→0.14/0.18; 2610.01601 and 2610.06744: order-invariant heads reach ≈0 flips | **prior** | Countermeasures are now published and cheap; the lab has not applied one to J or G |
| set6 p2: a 21%-wrong decision model leaves the school's collective behaviour unchanged; random view-fixed or per-agent-biased errors of the same size do not | 2609.27535 KITE (once-per-unique-state tables, shared discrepancy does not shrink with N); 2610.03935 JEVal (election simulation: right state calls, vote shares twice as wrong, systematic lean); 2610.01834 (code simulates, model evaluates) | **lab-only** for the main result | No paper tests whether the *form* of a decision model's errors decides whether a collective tolerates them. KITE is the closest machinery; the view cache is a coarse version of it |
| game_test p2/ex1: confirm-before-execute protects state | 2609.26532 REFLEX (reliability depends on action-set size and near-valid alternatives near authorisation boundaries); 2609.33401 (strict miss limits automate few inputs) | **extends** | Game setting, live protection logs |
| game_test p2: Japanese text with Japanese options collapses (jeff 5/18) | 2609.36965 Chinese-Jev; 2610.02293 HakemBench (Turkish); 2609.36399 (less confident in Arabic); 2609.37647 (all models degrade on low-resource languages) | **extends** | The only Japanese measurement in the set |
| prompt_best_practice: recommends permutation averaging / PriDe, margin gates, weighted ensembles | 2610.00831 AnyJev (prior division + cyclic rotations on stock LLM readouts); 2610.09188 (soft average of two models' probabilities beats one model, +9.6 Elo) | **prior** (now on decision-model readouts) | — |
| benchmark p1/p2 design | 2609.32160 (14-item checklist); 2610.02267 (self-audit: omitted pre-screen cost, gate accuracy as end-to-end, in-sample thresholds); 2609.31142 (score attacks against a re-run floor) | **extends** | The lab's design already meets most items; see the checklist table in [evidence/evaluation-methodology.md](evidence/evaluation-methodology.md). The lab-status column there was judged from a summary and not audited item by item |

## Should the lab stop or change anything?

- **Stop:**
  - **Narrowed re-asks on one-pass scorers.** set5 and 2610.07716 agree. Any menu-only variant can be computed offline from the cached first pass.
  - **Second voters with the same weights** (personas, wordings, repeats) as a way to fix errors. set4, set6 p1, 2609.29769, 2610.09188 and 2609.36399 agree.
- **Do not claim as new:**
  - that decision models decide anyway on missing evidence;
  - that confidence gates fail when errors are confident;
  - that option order matters for encoders;
  - that type safety is not correctness.

  All of these are now published. Cite the papers and describe the lab's contribution as the readout, the size, the workload class or the fallback-class design.
- **Can still be claimed:**
  - the error-form result in the school (set6 p2);
  - mixed decision-model panels as the only source of independent votes, once checked on confident errors;
  - the W2-vs-W3 split of the sufficiency check;
  - the key-naming-in-state attack on Kev-class models;
  - Japanese.

## Contradictions

None outright.

- **Mixed panel vs "wrong in the same places".** The mixed-panel result (set6 p1) and 2609.29769 seem to disagree. The likely cause is that they count different error sets: confident errors only in the paper, all errors in the lab. Settle it by computing the lab's n* on confident errors.
- **Stronger key-naming effect in the lab.** The lab sees a much larger key-naming effect than hosted Jev shows in JevAdvBench. The attacks and models differ, so this is not a contradiction.

## Follow-up (study/run-001, 2026-10-08 to 2026-10-13)

9 new papers, 2 read more closely (abstract-level; see [evidence/labels-and-injection.md](evidence/labels-and-injection.md) and [evidence/evaluation-methodology.md](evidence/evaluation-methodology.md)). Neither changes a verdict above; both add to rows already on record:

- **Row 31 (key-naming/label override, set1/set2/game_test)**: 2610.11436 adds a fourth attack surface — hosted Jev's judge false-acceptance rate moves from 1.0% to 26-26.5% from a one-character edit to a judged candidate, depending on output-label presentation. Different mechanism (judge-grading presentation, not a label/key match) from the lab's state-embedded key-naming attack, so this is a sibling finding, not a test of the lab's own claim. Still **lab-only** for the key-naming-in-state attack on Kev-class models — no paper, including this one, tests it.
- **Row 38 (benchmark p1/p2 design)**: 2610.11392 (TypedBench) adds a benchmark purpose-built for the calibration-reference gap 2609.32160 already flagged, plus a cost-matrix methodology (probabilities can give a worse decision than the top answer under asymmetric cost) the lab's own gate work has not separately measured. **Extends**, same as the row's existing verdict.
- None of the other 7 new papers (agent-workflow cost/reliability, multilingual/knowledge benchmarking, stance detection, RL priors, compact inference, knowledge tracing, budgeted feature acquisition) land on a row above; they are domain/engineering extensions of the surrounding catalog themes, not matches to a specific lab experiment.
- The "still unpublished" list in the main summary (mixed decision-model panels, error-form tolerance, W2-vs-W3 sufficiency split, key-naming-in-state on Kev-class models, Japanese) is unchanged by this follow-up: none of the 9 new papers addresses any of them.
