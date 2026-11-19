# Laya issue cluster: routing with a "none" option, long text, confidence gates, federal IT eval

- **Sources (all accessed 2026-10-02):** https://github.com/NandhaKishorM/laya/issues/35 (Romanian routing; Skystar9999, 2026-09-20); /issues/124 (Chinese routing; lzero07, 2026-09-22); /issues/99 (nikolai-vysotskyi, 2026-09-21); /issues/394 (PerryLink, 2026-09-24); /issues/450 (bhushankinge, 2026-09-24, with comments); /issues/635 (Charanraj-24, 2026-09-27); /issues/781 (rpriven, 2026-09-30). Locators: issue bodies' tables.
- **Evidence type:** reproducible bug reports / independent evaluations (several authors); independence: yes for all; each is a small or domain-specific set.
- **Model / base / checkpoint:** laya, laya-multilingual, laya-typed-decisions, versions 0.3.3 to 0.3.22; **size:** English 421M (stated in #450); others unknown/not stated per issue; **architecture/training:** not re-verified.
- **Task / options / rejection:** #35 and #124: pick 1 of 13 skills including an explicit `none`, 20 hand-labelled requests each (Romanian; Chinese). #450: 19-question bundle on 12,000 US federal IT solicitations, 741 quote-graded rows. #781: `guard` preset yes/no heads on 53 synthetic cases.
- **Data provenance:** authors' own sets (#450 is graded against later quote outcomes); **n:** 20 / 20 / 741 / 53; **raw cases available:** yes for #35, #124, #781; partial for #450 (aggregates, ids private).
- **Fixed / mitigated?** README gating advice changed (PR #378); per-language evaluation harness added (#210); abstention via `min_confidence` shipped (#456); others open. **fix evaluated?** only #635 proposes a reorder-stability signal (AUROC reported by the proposer, not independently verified).
- **Relevant local classes:** L2, L3 (chit-chat and unlisted requests forced into a skill), L5, L8, L9-like; Q1, Q3, Q5.

## What the sources report
- #35: with a `none` option present, "What time is it in Tokyo?" went to a skill at 0.78 and "Translate this sentence to French" to another skill at 0.77; 50-55% accuracy overall; confidence did not separate right from wrong.
- #124: three chit-chat or off-topic Chinese inputs expected `none` were routed to `email` at 0.91 and 0.82; the English checkpoint conversely returned `none` at 0.98 for hard Chinese input (confident refusal). Accuracy 0.60-0.70 across checkpoints.
- #99: on long noisy multilingual posts the multilingual checkpoint collapsed to two options, an empty message returned the dominant option at 0.85, and bare option names without descriptions still drove >80% of answers, which is a prior-dominated readout.
- #394: a fixed 0.85 threshold selected below model accuracy at 20 options; the shipped `choice:11+` temperature (0.1006) forced confidence 1.0 including wrong answers; maintainer removed the 0.85 recommendation.
- #450: Laya English 0.780 vs Jev 0.919 on primary class (741 rows), ECE 0.322 vs 0.049, rare presence flags over-fire (e.g. `has_warranty` 0.451 vs 0.030); the 1,024-token checkpoints were worse; accuracy fell to 0.655 on 600-1,200-character states.
- #635: on MASSIVE (20 options) 37 of 65 wrong answers had confidence >= 0.90.
- #781: the guard's `prompt_injection` head scored 0.00-0.30 on three document-embedded instructions aimed at the AI, while a benign text merely quoting "ignore previous instructions" scored 0.619; the head tracks vocabulary, not addressee (53 synthetic cases, author-labelled).

## Strength and caveats
- Independent and inspectable, but each is small or narrow. #35/#124 are the most relevant to L2/L3 because a `none` option existed and was often not chosen; they do not show how often. #781 contradicts the single-case "injection immunity" of eco-laya-adversarial-hf-discussion3 for a different mechanism (guard preset).
- Laya is a trained Jev-style model, not a zero-shot NLI wrapper, so this is evidence for Q3: training did not remove L2/L3-type behaviour at ~300-420M.
