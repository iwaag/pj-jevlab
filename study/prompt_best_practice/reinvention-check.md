# Reinvention check: are the lab's prompt, order and second-pass experiments repeating known work?

Written for `devdocs/episodes/study/prompt_best_practice/p1` step5 ([plan](../../devdocs/episodes/study/prompt_best_practice/p1/plan.md)). Drafted 2026-10-03. Reviewed by terra in step6; ten findings applied (see the p1 report).

## How to read this note

Three kinds of statement are kept apart in every section.

- **[Lit]** a source claim. It traces to one of the five evidence notes below, by the source label used inside that note. Nothing is quoted from memory.
- **[Lab]** a lab result, copied from [lab-evidence.md](lab-evidence.md) (row ids Q1-1 and so on), which cites the lab reports.
- **[Inf]** my inference from the two. It is not a finding of either side.

Evidence notes (citation keys used below):

| Key | File | Contents |
|---|---|---|
| q12 | [evidence/q1-q2-instruction-and-options.md](evidence/q1-q2-instruction-and-options.md) | wording and format sensitivity, distractors, keys, descriptions |
| q3 | [evidence/q3-order-and-format.md](evidence/q3-order-and-format.md) | option order, PriDe, permutation averaging, calibration; sources numbered 1-21 |
| q4 | [evidence/q4-second-passes.md](evidence/q4-second-passes.md) | self-correction, verification, voting, elimination; labels A1-G3 |
| q5 | [evidence/q5-abstention.md](evidence/q5-abstention.md) | abstention and none-of-the-above; labels S1-S12 |
| q6 | [evidence/q6-readout-and-vendor.md](evidence/q6-readout-and-vendor.md) | encoder, scorer and vendor evidence; labels A1-A9, C1-C10 |

Lab readouts: W12 and A27 read option-letter logits, K27 a pointer head, J and G are encoders, L27 generates. No source in the evidence notes studies a pointer-head scorer; the closest are GLiNER span scoring (q6 A6) and author statements (q6 C5, C6) ([q6 gaps](evidence/q6-readout-and-vendor.md)).

**Limits of the evidence base (apply to every verdict).** Most sources were read through a fetch tool's summary or at abstract level; each note says which. Many are preprints, several are 2026 preprints without peer review, all are English, and most use 2022-2025 base or chat models, not trained decision models. "The literature does not show X" means "no source in these notes shows X". It is not proof that no such work exists ([search-log.md](search-log.md)). Lab-side limits: one author family wrote all cases, labels were checked by a blind agent and not by humans, F1-F3 wordings were not meaning-reviewed, and set4 and set5 share one fresh set ([lab-evidence.md caveats](lab-evidence.md)).

Verdict scale: **new** (no external answer found for this question on any readout), **confirmation on a new readout** (the phenomenon or its negative is in the literature, the lab measured it on a readout the literature does not cover), **repetition** (the outcome was predictable from the literature on a similar enough readout, and the lab adds no new information beyond its own cases).

## Summary table

| Experiment | Already answered? Readout of the answer | Lab vs literature | Missed pitfall or stronger method | Verdict |
|---|---|---|---|---|
| p3 wording family F0-F3 (D1) | Phenomenon: yes, extensively (q12 Sclar, Mizrahi, POSIX, ProSA). Readouts: probability ranking or generation, base/chat models. Not for pointer, encoders or trained decision models | Agrees on existence; the lab's split by readout (encoders 26-36 of 60 change, letter-logit and pointer 6-8) has no published comparator | Spread over variants grows with their number; F1-F3 unreviewed; n = 20 per cell; reporting a distribution was recommended (q12 Mizrahi) | Confirmation on a new readout |
| p3 order diagnostic (D2, reversal, RStd) | Yes (q3 1, 2, 3, 4). Letter-logit readout matches W12/A27. None for pointer or encoder | Compatible: strong models flip little (W12 1, K27 1, A27 3 of 60). J 21 and G 14 have no comparator | Permutation averaging and PriDe (q3 1, 11, 16) not run as a comparison; power at high accuracy (q3 12); letter vs key text not varied | Confirmation on a new readout (letter-logit part near repetition) |
| p3 D3 options-only shortcut check | Idea supported (q12 Chandak, abstract only) | Agrees: 13-31% on options alone | none | Repetition of a standard sanity check |
| set4 WV (wording vote) | Yes (q4 A1 Table 7, E1) | Agrees: little diversity (107 of 120 cases agree), vote no better than base (18 vs 17 false executions) | Plain vote; weak-supervision weighting gains more (q4 E1); permutation or prompt-variant averaging of probabilities (q4 E2, E3) not used | Repetition (outcome predictable) |
| set4 VB (blind verification) | Generative analogue yes (q4 C1 CoVe, B4, C3). None for scorers | Agrees on the weak point: the unknown-fact check said yes on 0 of 17 false executions | Verifier is the same model family as the generator (q4 F1, B7); no sample-size sizing for 2-4 discordant pairs | Confirmation on a new readout; the conflict-check gain (4 rescued) is small and untested beyond p = 0.125 |
| set4 VS (shown verification) | Yes, generative (q4 B1, B8, C1 yes/no agreement bias, B7 blind spot) | Agrees: "supported" on 14 of 17 false executions | Known harmful ingredient is a challenge or attribution framing | Repetition |
| set4 MV (model vote) | Yes (q4 A1 Table 10, E4, E7, E6, C4) | Agrees: three-model majority worse than base (20 vs 17), 12 shared errors | Unweighted vote is the configuration the literature says fails; weighted ensembles beat it (q4 C4) | Repetition |
| set4 abstention rules (unanimity, random-review reference) | Missing-information failure: yes (q5 S8, S9, S11). Unanimity as a gate: indirect (q4 E7, E6) | Agrees: missing evidence is hardest; gates miss high-confidence errors | No risk-coverage curve; the random-review reference is a good control | Confirmation on a new readout |
| set5 D2 (top two, both orders), T3 | Elimination: yes (q4 D1, D2 option-ID elimination, D3). Letter-logit readout matches W12/A27, not K27 | Null on K27 is consistent with the lab's own mechanism check (second-pass probabilities are first pass renormalised). It is not a contradiction of the positive elimination results | Tested only on K27, where a null is expected by construction [Inf]; debiasing step of D2 (q4 D2) absent | Elimination idea: repetition. The K27 null: new but mechanism-predicted |
| set5 Dex (first choice vs best fallback) | No close analogue (nearest: top-3 plus None re-rank, q4 D3) | Null, n = 1 corrected, 0 wrong | Underpowered for any effect below about 5 answers | New design, null |
| set5 F2 (re-ask naming first choice) | Yes, generative (q4 B1, B2, B8, B7) | Near-zero change is in line with the best case of q4 B2 (+0.1 to +1 point with a neutral prompt). The +3 net is untested | Neutral wording avoided the known harmful framing; no oracle stopping, which was the Huang critique | Confirmation on a new readout |
| set5 D2 order-disagreement flag | Idea known under other names (q3 2, 10, 11; q4 E3, q12 ProSA). No precision/recall for a 3-4 option scorer | Direction agrees (disagreement goes with uncertainty). 5 of 6 fired cases wrong has no comparator | Post hoc, 6 cases, p uncorrected; not compared with a first-pass margin baseline | Confirmation on a new readout, unproven as a finding |
| Proposed terse-wording experiment | Terse vs full for scorers: not answered anywhere found. Task-dependence known for generation (q12 Celebi) | The lab's own cells point both ways (K27 W3 up, A27 W2 down, dev pilot over-rejection) | Selected cell, winner's curse; one paraphrase per length | The question is new; the experiment as proposed would repeat a screening result |

## Notes per experiment

### 1. p3 wording family F0-F3 (D1)

**Lab.** [Lab] F1 terse (0.77 of F0 length), F2 formal, F3 restructured on 20 diagnostic cases per class. Cases whose choice changed under at least one of F1-F3, of 60: W12 8, K27 6, A27 8, J 26, D35 7, L27 9, G 36 (Q1-1). Direction depends on system and class (Q1-2, Q1-3). Descriptive only.

**Was it answered, and on what readout?**
- [Lit] Sensitivity to meaning-preserving prompt changes is established. Sclar et al.: median spread 7.5 points across 53 tasks, up to 76 for one task, persisting with size and instruction tuning; the same paper marks the 10-format median as a lower bound (q12, Sclar). Mizrahi et al.: paraphrase rankings differ significantly on 21 of 25 tasks, negatively correlated on 15 (q12, Mizrahi). POSIX and ProSA measure instance-level sensitivity (q12).
- [Lit] Readouts there are probability ranking over options on base or chat models (Sclar) or generation (Mizrahi, ProSA). Format features varied in Sclar are separators and casing, not instruction wording ([q12](evidence/q1-q2-instruction-and-options.md)).
- [Lit] Encoders: NLI cross-encoders shift by about 20 F1 under hypothesis-verb changes (q12, Ghilene; template chosen on evaluation data, so the size is optimistic). Label words move F-score by more than 0.1 on every dataset tested (q12, LOADS). Neither is a label-in-input encoder like J or G.
- [Lit] No source studies instruction wording on pointer-head or trained decision models ([q12 gaps](evidence/q1-q2-instruction-and-options.md), [q6 gaps](evidence/q6-readout-and-vendor.md)).

**Agreement.** [Inf] The existence of wording sensitivity is a repetition. The split by readout is the new part: letter-logit and pointer systems moved little (6-8 of 60), encoders moved 26 and 36. The literature on size says effects shrink for stronger models (ProSA) or not (Sclar), so it does not predict which. The encoder result is consistent with the q6 A1 and A3 pattern that older encoder classifiers are driven by surface features, but that is a different model class.

**Pitfalls.**
- [Inf] "Changed under at least one of three variants" is a maximum-over-variants statistic. It grows with the number of variants and with noise, a point the lab's own caution makes and that q12 Mizrahi handles by reporting quantiles over many paraphrases. Three variants, one per type, cannot give a distribution.
- [Lab] F1-F3 were authored after the freeze and not meaning-reviewed. [Lit] Mizrahi's human check found about 15% of machine paraphrases invalid before filtering (q12). So some of the encoder changes may be meaning changes, not wording noise.
- [Inf] n = 20 per cell: three discordant cases move all-correct by 15 points, inside Sclar's cross-task spread.

**Verdict: confirmation on a new readout.** Descriptive and unreviewed; do not cite as a measured wording effect for any single system.

### 2. p3 order diagnostic (D2 reversal, RStd) and D3

**Lab.** [Lab] Option dict reversed; changed choices of 60: W12 1, K27 1, A27 3, J 21, D35 3, L27 6, G 14 (Q3-1). RStd per cell (Q3-2). Options-only check gives about 13-31% (Q1-11, Q2-7). Lab decision: no permutation averaging because of cost x4-16 (Q3-7).

**Was it answered?**
- [Lit] Yes. Option-ID and position bias are established on letter-probability readouts: gold in D costs GPT-3.5 6.3 points, gold in A gains LLaMA-30B 15.2 (q3 1); reorder gaps of 13-75% are best-minus-worst and an adversarial upper bound (q3 2); fluctuation is higher on harder tasks (q3 3); a second shuffle of MMLU options lowers all ten models, by 6-27 depending on metric, using only 2 of 24 permutations (q3 4).
- [Lit] Known countermeasures: PriDe estimates the ID prior on about 5% of items at about 1.2x cost against 4-5x for full permutation, +2.6 to +4.0 accuracy in 2023 models (q3 1). Permutation averaging helped in 5 of 6 pairs (q3 11). Simple instructions and chain-of-thought did not help (q3 1, 2).
- [Lit] Encoders: pointwise cross-encoders are order independent by construction, joint listwise ones are not (q3 14). No label-order test of GLiNER or GLiClass was found (q3 15). No pointer-head test (q3 14).

**Agreement.** [Inf] W12, A27, K27 flipping 1-3 of 60 is, tentatively, in line with what the literature suggests for strong letter-logit models (W12/A27 only; K27 is an untested pointer-head result with no external comparison): effects shrink with strength and with accuracy (q3 synthesis item 2). Position-bias diagnostics also lose power at ceiling accuracy and tiny n (q3 12: bias detectable mainly between 60% and 95% base accuracy, single author), so a flat 60-case result does not prove absence. J (21 of 60) and G (14 of 60) have no published comparator; the joint-encoding listwise result (q3 14) and the GLiClass attention-dilution remark (q3 15) are the only partial leads.

**Pitfalls.**
- [Lab] RStd gives 0.25 for K27 on W3 in both orders with zero changed choices (Q3-2). [Inf] This shows RStd confounds position with gold position when gold position differs between orders. Zheng's RStd assumes balanced gold positions; the lab already notes this.
- [Inf] The cost argument for skipping permutation averaging ignores PriDe's roughly 5% estimation cost, though PriDe addresses ID-token prior, which does not exist for K27 (pointer) or the encoders.
- [Inf] Letter vs key text was not varied. [Lit] Changing symbols barely moves bias; scoring option text without IDs lowers it (q3 1). That applies to W12 and A27 only.
- [Lit] Readout artifacts matter: first-token letter logits and generated text differ by 9-66% on chat models, and part of the apparent bias is a readout artifact (q3 5, 5b). Fine-tuned decision models like W12 are not the chat models studied, so this may not apply [Inf].

**D3 options-only.** [Lit] Chandak et al. (abstract only) report that many MC items are answerable without the question (q12). [Inf] The lab's check is a routine shortcut test, a repetition with a useful local result (cases need the input).

**Verdict: confirmation on a new readout**, with the letter-logit rows close to repetition. The encoder result is the part with no published counterpart; it is descriptive.

### 3. set4 WV (wording vote)

**Lab.** [Lab] Majority over wordings O, L, S on K27, 120 fresh W3 cases: false executions 18 vs 17 for the base, test P1 Holm p 1.00 (Q4-1). Wordings agreed on 107 of 120 (Q1-5).

**Answered?** [Lit] Yes. Voting over prompt sets or prompt order gives a fraction of sampling gains: GSM8K LaMDA 17.1 to 18.6 (three prompt sets) and 19.2 (40 orders) vs 27.7 for sampling (q4 A1 Table 7). Ask Me Anything: plain vote over prompts has a minor effect, +4 on CB and -2 on RTE; prompts' errors are correlated (Jaccard 39.9-42.2 against 0.25 expected); weak-supervision aggregation beats the vote by up to 8.7 points (q4 E1). Readout of these is generation or T0-3B scoring (partial).

**Agreement.** [Inf] The lab result is exactly the predicted outcome: little wording diversity from K27, so little to vote on.

**Missed.** [Lit] Weighted aggregation (q4 E1, C4) and averaging probabilities over paraphrases or permutations (q4 E2 for one RLHF model, E3 for 3B models). [Inf] Both would be the natural stronger comparators for a scorer that exposes probabilities. The lab voted on labels, not probabilities.

**Verdict: repetition.** Cost: 3 calls per decision for no measured benefit.

### 4. set4 VB, VS (verification)

**Lab.** [Lab] VB: three separate yes/no checks without options or B's answer; false executions 13 of 60 (B 17), 4 rescued, 0 newly wrong, Holm 0.50; the conflict check C2 caught the 4 conflicting-evidence cases; C1 (unknown decisive fact) said yes on 0 of 17 false executions (Q4-2). VS: shown the answer; "supported" on 14 of 17 false executions (Q4-3). Blind terra annotator and adjudicator reproduced K27's error on 6 of 7 disputed cases (Q4-12).

**Answered?**
- [Lit] Self-correction without external information is flat to negative: CSQA GPT-3.5 75.8 to 38.1 under a "find problems" prompt (q4 B1); +0.1 to +1 with a neutral prompt at zero temperature (q4 B2); survey conclusion (q4 B3). Self-critique falls and a sound verifier raises accuracy (q4 B4). Models flip 46% of answers when challenged (q4 B8). Own errors are missed 64.5% of the time vs injected ones (q4 B7).
- [Lit] Factored verification (CoVe, q4 C1) is the generative counterpart of VB. It also reports yes/no questions agree with the claim whatever its truth (anecdotal), which fits VS.
- [Lit] Verifier true-negative rate falls 0.68 to 0.17 as the generator gets stronger (q4 C3): errors that look coherent are hardest to catch. Same-family judges favour their own outputs (q4 F1; cause contested by F2).
- All generative. [Lit] No source tests verification of a scorer ([q4 gaps](evidence/q4-second-passes.md)).

**Agreement.** [Inf] VS and the C1 result match the literature (a shown or same-family check accepts the generator's reasoning; unknown-fact errors look coherent). The C2 result is a different kind: a structured check with a rule-like criterion (two records disagree, no precedence) works because the evidence is detectable in the input; [Lit] gains elsewhere came when an independent signal entered the second pass (q4 cross-source item 2). [Inf] The lab's VB therefore shows a genuine but tiny gain (4 cases, exact p 0.125, no multiplicity-surviving effect).

**Missed.** [Inf] The verifier used was K27 itself, so same-family inheritance was built in; the terra check (Q4-12) supports that the error is shared by a different family on 6 of 7 cases, which weakens that worry. No sizing was done for 2-4 discordant pairs (set5 did one for F2).

**Verdict.** VS: repetition. VB: confirmation on a new readout for the negative result on missing evidence (the lab's real finding); the C2 gain is new and unproven.

### 5. set4 MV (model vote) and abstention rules

**Lab.** [Lab] Three-model majority (W12, K27, A27): 20 false executions of 60 vs 17 for B; W12 alone 25. MV-u (unanimity) sent 30 of 120 to review and left 12 false executions, which is the random-review count (12.8) (Q4-4). WV-u sent 13 and left 15 (random 15.2). VB sent 5 and caught 4. The random-review reference is part of the design.

**Answered?**
- [Lit] Ensembles of unequal members drag toward the weaker one: LaMDA+PaLM 36.9 vs PaLM alone 56.5 (q4 A1 Table 10); five-model ensemble did not beat the best single model (q4 E4); nine judges behave as about two votes and the best judge matches or beats the panel (q4 E6). Models agree on 42-60% of items when both are wrong, more for accurate models (q4 E7). Unweighted ensembles and self-verification do not beat majority vote, weighted do (+15.5, q4 C4). One company-authored paper reports large consortium gains but controlled neither error correlation nor strength (q4 E5).
- [Lit] Missing-information detection is the weak case on every readout checked: "not sure" on 0.7-4.6% of cases where 41.8% were underspecified (q5 S8); abstention recall 13.16% with logit readout on medical items (q5 S9); abstention instructions raise abstention at a coverage cost (q5 S3, S6); the Unknown option itself triggers abstention in a recent unreplicated preprint (q5 S7).
- [Lit] Letter-logit max-probability predicts correctness (AUROC) and a threshold can abstain with about 20 labelled items to choose it (q5 S11); the same probabilities are overconfident on errors in chat models. Confidence-gated re-ranking works when the first stage is uncertain on its errors (q4 D3).

**Agreement.** [Inf] All of the lab's MV and abstention results are what these sources predict, including the hardest case: 12 shared errors under MV-u and missing evidence as the failure that no check reaches. The lab's high-confidence K27 errors (Q4-10, K27 0.99) fit the condition under which confidence gates fail (q4 D3), but the lab and q5 S11 differ in readout, so S11's AUROC claim is not tested on K27.

**Missed.** [Inf] No risk-coverage curve or AURC for the flags (the Kev card reports AURC, q6 C5); the random-review reference partly covers this. No weighted ensemble.

**Verdict: MV repetition. Abstention: confirmation on a new readout.** The lab's contribution is evidence for pointer-head and letter-logit models on missing-fact classification, where only one preprint (q5 S9) exists.

### 6. set5 D2, Dex, T3, F2 (narrowed and named re-asks)

**Lab.** [Lab] B correct 96/120. D2 95 (1 corrected, 2 newly wrong, Holm 1.00); Dex 97 (1 and 0, Holm 1.00); T3 2 and 3; F2 4 and 1 (99/120, untested, about 520 pairs to confirm) (Q4-6, Q4-7). Second-pass probabilities differ from the renormalised first pass by a median of 0.001-0.015 (Q4-8). The gold was the second choice in 23 of 24 fresh errors.

**Answered?**
- [Lit] Elimination: POE with option log-likelihood scoring beat multiple-choice prompting on 5 of 8 tasks, helped logical tasks and hurt others (q4 D1). Option-ID elimination with a debiasing step on letter logits (matching W12/A27) gained +0.8 to +6.3 over a debiased baseline, with the smallest gain on the 3-option task and more with more options (q4 D2). Asking a model to name the wrong option was much worse. Without the debiasing step it degraded when labels were randomised (q4 D2 Table 1). Top-3 re-ranking helped hard samples and hurt easy ones, gated by first-stage confidence (q4 D3).
- [Lit] Re-ask naming the first answer: the same family as intrinsic self-correction (q4 B1, B2, B8), generative.
- [Lit] No source tests a narrowed or named re-ask on a pointer-head scorer (q4 gaps).

**Agreement.**
- [Inf] The K27 null does not contradict the positive PoE_ID result. The two readouts differ: a letter-logit decoder reads all options in one context, so removing options changes its distribution. A pointer head scores each option span against the question state, so removing options largely renormalises on this set (median absolute differences 0.007-0.015, with non-trivial 90th-percentile differences). The lab's mechanism check (median change 0.011 for D2a) shows this directly. So the experiment was close to a foregone conclusion for K27 once the readout is known, and the lab's own report says so.
- [Inf] F2 near zero fits the neutral-prompt end of the self-correction literature (+0.1 to +1 point, q4 B2). The lab's +3 of 120 (2.5 points) is inside its own noise: 4 corrected and 1 newly wrong is a 5-case difference. No effect should be claimed.
- [Inf] Dex has no close external analogue. With 1 and 0 discordant pairs it cannot detect anything below about 5 answers.

**Missed.**
- [Inf] The literature points to letter-logit decision models (W12, A27) as the readout where narrowing could matter, and those were not tested. Expected size from q4 D2 on few-option tasks is small (+0.8 on 3 options), so the null probably holds there too, but the matching-readout test was not run.
- [Lit] The positive PoE results use a debiasing step first (q4 D2). Not relevant for K27 (no position bias: first-listed option chosen in 116 of 240, Q3-6).
- [Lit] Huang et al. attribute reported self-correction gains to oracle stopping (q4 B1). [Lab] The lab used no gold-based stopping; this pitfall was avoided.

**Verdict.** Elimination (D2, T3): repetition of the idea (q4 D1, D2), with a K27 null that was predictable by the pointer-head mechanism. Dex: new design, null. F2: confirmation on a new readout.

### 7. set5 D2 order-disagreement flag

**Lab.** [Lab] Fired on 6 of 120 fresh W3 cases; B wrong on 5; recall 5 of 24 errors; exact tail P(X >= 5) = 0.0012, descriptive and uncorrected. Same-pass comparators: VB 5 sent, 4 errors; VS 9, 4; WV-u 13, 5. Dev: fired twice, 1 error (Q4-9). Both orders agreed in 114 of 120 pairs; no position bias (Q3-6).

**Answered?**
- [Lit] The idea exists under several names. Sensitivity to order is larger when the model is uncertain between its top 2-3 options (q3 2, correlational, 2023 API models). Both-order disagreement entropy sent ambiguous pairwise-judge cases to human review at 20% cost with accuracy parity (q3 10, generative judges). Permutation-disagreement metrics (PBM, q4 E3) are reported against bias and accuracy, not as an error detector. ProSA defines instance-level inconsistency (q12). Perturbation-based uncertainty halves ECE on average for generation (q3 21, SPUQ, abstract only). Hanna and Feng warn that lower flip rates need not mean higher accuracy (q3 11).
- [Lit] No source reports precision and recall of an order-disagreement flag on a 3-4 option scorer (q3 synthesis item 6; [q4 gaps](evidence/q4-second-passes.md)).

**Agreement.** [Inf] Directionally consistent. The lab's flag fires when top-2 is near a tie and the two orders differ, and Pezeshkpour's association between sensitivity and top-2/3 uncertainty predicts this.

**Pitfalls.**
- [Inf] **Redundancy with first-pass confidence.** If the flag fires only when the first-pass margin is small, it adds nothing to a margin gate. [Lab] Q4-10 says margin gates cannot catch K27's high-confidence missing-fact errors, and 2 of the 17 false executions were caught by the flag; the notes do not show how the six flagged cases relate to first-pass margin. The comparison to a margin baseline at the same review budget (6 of 120) is missing.
- [Inf] **Forking paths.** The 0.0012 tail was computed for one flag chosen after seeing several (VB, VS, WV-u, D2-rev). Against VB (4 of 5) the difference is within noise. Development gave 1 of 2.
- [Inf] **Small numbers.** Recall 5 of 24 and 6 fired cases is not a stable estimate.
- Permutation averaging as a debiaser (PriDe, q3 1) would not apply: K27 has no measured position bias.

**Verdict: confirmation on a new readout** of a known idea (consistency under permutation as uncertainty). It is unproven as a finding.

### 8. The proposed terse-wording experiment

**Lab basis.** [Lab] On K27, W3, F1 terse: all-correct 15/20 to 18/20, E-fb 4/9 to 7/9, three wrong-to-right and none right-to-wrong (Q1-2). Opposite signs elsewhere: A27 on W2 19/20 to 16/20; L27 on W3 12 to 15; W12 on W3 with the formal wording 12 to 15 (Q1-3). The dev pilot saw terse push A27 and K27 towards over-rejection (Q1-4, Q5-10).

**Answered?**
- [Lit] Terse vs full instructions for option-logit, pointer or encoder readouts: no source found (q12 gaps). The nearest controlled work is generative and task-dependent: detailed category definitions add 17-37 points where the category is not self-explanatory and nothing where it is (q12, Celebi and Penczynski, fetch summary only).
- [Lit] Author probe on a letter-logit decision model: rules in the question hurt (0.67 for one sentence vs 0.24 for a paragraph of rules on a form-filling probe; n not read), "a fixed convention has to be in the training data" (q6 C6). Directional support for shorter instructions on that system, vendor-grade.
- [Lit] Template meaning matters less than target words in NLI with older models (q12, Webson and Pavlick; q6 A3).
- [Lit] An abstain clause trades coverage for abstention and the same sentence yields 0% to about 100% across models (q5 S3, S4). If the terse wording dropped a hedge, the dev-pilot over-rejection direction would fit S3; if it dropped decisiveness text, the opposite.

**Agreement.** [Inf] Sign flips across systems and classes are what one expects from paraphrase sensitivity (q12 Mizrahi: negatively correlated rankings on 15 of 25 tasks).

**Pitfalls.**
- [Inf] The K27 W3 cell is one favourable cell among about 21 (7 systems times 3 classes) on 20 cases each, found after looking, with one terse paraphrase. Winner's-curse risk is high; three discordant cases is below any test threshold.
- [Lab] F1 is 0.77 of F0 length (design asked 40-60%) and was not meaning-reviewed, so length and content are confounded.
- [Lit] The recommended practice is a distribution over many paraphrases (q12 Mizrahi, PromptEval), not one rewrite.

**Verdict: the question is new, but the experiment as proposed would repeat a screening observation on the same single cell.** A useful design needs several terse and several full paraphrases per system (see C4 below).

## Candidate next experiments

Proposals, not plans. Each is only listed where the literature leaves a gap that matters for the lab. Expected effect sizes are ranges from the cited sources on other readouts plus my reading; none was measured on these systems.

**C1. Permutation averaging on the encoders (J and G).**
- Hypothesis [Inf]: the order flips of J (17-32% of top-1 in the game, 21 of 60 on p3) and G (14 of 60) shrink to near zero under cyclic permutation averaging, and part of the lost accuracy comes back.
- Readout: encoder scores, per-option sigmoid or softmax averaged over cyclic orders; endpoints are flip rate and E-sub/E-fb (p3) or clear-intent and no-cost accuracy (game, [Q3-3](lab-evidence.md)).
- Evidence: permutation averaging gains +2 to +8 on 2023 API models ([q3 2](evidence/q3-order-and-format.md)), +0.8 to +21 on 3B decoders with flip metric forced to 0 ([q4 E3](evidence/q4-second-passes.md)), 5 of 6 model-benchmark pairs improved ([q3 11](evidence/q3-order-and-format.md)); a teacher-student form lets an encoder absorb the average ([q3 16](evidence/q3-order-and-format.md)).
- Expected effect: flip rate to 0 by construction; accuracy change from 0 to a few points, because lower sensitivity does not by itself raise accuracy ([q3 11](evidence/q3-order-and-format.md)) and most game flips swap between an action and `clarify`. Gap: no published test for label-in-input encoders ([q3 15](evidence/q3-order-and-format.md)). Cost is small for 0.4B encoders.

**C2. Is the order-disagreement flag more than a low-margin flag? (re-analysis first)**
- Hypothesis [Inf]: the six flagged cases are the low first-pass-margin cases, so a margin gate with the same review budget finds as many errors.
- Readout: K27 pointer probabilities already stored for the fresh run; endpoints are precision and recall at a fixed budget (6 of 120) against the first-pass margin and against VB. Then the same on W12 and A27 reversed-order tracks, since Q6-3 lists only K27.
- Evidence: order sensitivity tracks top-2/3 uncertainty ([q3 2](evidence/q3-order-and-format.md)); both-order entropy as a review flag ([q3 10](evidence/q3-order-and-format.md)); max-probability AUROC for letter logits ([q5 S11](evidence/q5-abstention.md)).
- Expected effect: if the flag is redundant, precision of the margin gate approaches 5 of 6; if not, the flag adds a few of the 17 false executions that a margin gate misses (the lab found 2 of 17). Needs no new inference for the first part. Treat 5 of 6 as unconfirmed until a second set.

**C3. Terse vs full instruction as a distribution, with length varied apart from content.**
- Hypothesis [Inf]: once many paraphrases per length level are used, the K27 terse effect on W3 is inside the paraphrase spread, and any systematic length effect differs by readout.
- Readout: all-correct and E-fb on W3 for K27, A27, W12, with at least 8 reviewed paraphrases at each of two lengths, paired McNemar and a quantile report ([q12 Mizrahi](evidence/q1-q2-instruction-and-options.md)).
- Evidence: Sclar median spread 7.5 points ([q12](evidence/q1-q2-instruction-and-options.md)); task dependence of instruction detail ([q12 Celebi](evidence/q1-q2-instruction-and-options.md)); Decider probe on rules in the question ([q6 C6](evidence/q6-readout-and-vendor.md)); abstain clause trade-off ([q5 S3](evidence/q5-abstention.md)).
- Expected effect: unknown. Under Sclar-like spread the paraphrase SD would be a few points on 20-case cells; a length effect of the size seen (3 of 20) would not stand out. Run only if the owner wants the wording question answered rather than the K27 cell confirmed.

**C4. Wording of the fallback option and the effect of its mere presence.**
- Hypothesis [Inf]: E-fb and false execution on W3 depend on how the fallback options are worded (bucket-like vs descriptive), and a fallback option's presence partly drives abstention independent of its meaning.
- Readout: E-fb and false executions on W3 and W2 for W12, A27, K27, with the fallback description rewritten (3 phrasings) and a content-free label control, as in [q5 S7](evidence/q5-abstention.md).
- Evidence: NOTA wording gives up to 2.4x spread for one 8B model ([q5 S2](evidence/q5-abstention.md)); an unrelated word as the extra option gives similar abstention in one preprint ([q5 S7](evidence/q5-abstention.md), summary only, unreplicated); a clone's audit reports abstention recall falling from 75.5% to 23.5% under a synonym of the abstention prompt ([q6 C9](evidence/q6-readout-and-vendor.md)); Decider: generic options must look like buckets ([q6 C6](evidence/q6-readout-and-vendor.md)).
- Expected effect: for the encoders, tens of points are plausible (clone audit, author evidence). For K27, A27 and W12 the lab's fallback accuracy is already 16-24 of 24 on W3 and W1, so detectable differences are probably 1-4 cases per cell. The experiment matters because fallback accuracy on W3 is the lab's main failure.

**Not proposed.**
- A second pass for L27 or a hosted reasoning model (the set5 report's own suggestion). [Lit] The generative self-correction evidence predicts near zero with neutral wording and loss with challenge wording (q4 B1, B2, B7), so the literature makes a large gain unlikely without an independent signal (a tool or independent check); a test on the target model (L27's constrained JSON setup) remains necessary.
- Another unweighted multi-model vote or another vote over wordings (q4 A1, E4, E6, E7).
- A letter vs key-text test on W12 and A27 as a stand-alone study: [Lit] expected effect on large instruct models is small (q12 Sanz-Guerrero: Llama-3.1-70B-Instruct +0.3, Gemma 3 12B not significant).
- A narrowed re-ask on W12 and A27 only if W3 cases have many options. [Lit] The gain on 3-option tasks was +0.8 and +2 to +6 on 7-10 options (q4 D2); the W3 option counts are not in the notes read.

## Overall answer to the reinvention question

**Mostly not reinvention, but not mostly new either.** [Inf]

1. **The phenomena are settled; the readouts are not.** Prompt sensitivity, order bias, vote failures, self-correction failure and the missing-information failure are all in the literature. None of that literature, as found, covers pointer-head scorers, label-in-input encoders or fine-tuned letter-logit decision models. Most of the lab's experiments therefore add a new readout; D3 and the W12/A27 order rows are repetitions or near-repetitions. That has value because the literature's readout warnings (first-token logits vs text, q3 5, 5b, q4 G1) say that transfer cannot be assumed.
2. **Four set4/set5 arms were predictable and cost real compute:** wording vote, shown verification, three-model vote, and the K27 narrowed re-asks. The first three repeat results that were in print before the experiments (q4 A1, E1, E4, E6, E7, B1, B8, C1). The K27 narrowed re-ask was predictable from the lab's own scoring mechanism, and the one readout where the literature shows gains (letter logits, q4 D2) was not tested.
3. **What is new and worth keeping:** the readout-split diagnostics (encoders vs letter-logit and pointer), the 0-of-17 result for a blind unknown-fact check on missing-fact errors, the shared-error finding across K27 and a blind terra annotator, and the absence of any second-pass effect on K27. The order-disagreement flag is the one promising by-product, with the caveats in section 7.
4. **Missed methods and pitfalls, in order of weight:** no multi-paraphrase distribution or quantile reporting (q12 Mizrahi), so wording results cannot be separated from paraphrase noise; no first-pass-margin baseline for the order flag; no permutation-averaging or PriDe comparison for the sensitive readouts (J, G) despite its low cost (q3 1, 11); unweighted votes; underpowered primary tests with 2-4 discordant pairs.
5. **Nothing found contradicts the literature.** The only apparent conflict, a null for narrowing against positive results for option-ID elimination, is a readout difference (q4 D2 vs lab Q4-8), not a disagreement.
6. **Reliability of this answer.** It rests on evidence notes that are partly summary- and abstract-level, with 2026 preprints. Terra review (plan step6) is done; a check of the abstract-only sources would raise confidence in the "no published comparator" statements, which are claims of absence in a finite search.
