# Hosted Jev: out-of-scope inputs, "none" options, and the effect of removing the abstain label

- **Sources (accessed 2026-10-02):** https://github.com/priorbench/jev (README; out-of-scope paragraph); https://github.com/jujumilk3/jev-calibration-audit (README; abstention, option-order, calibration paragraphs); https://github.com/ickma2311/jev-baselines-eval (README; CLINC150 OOS paragraph); https://github.com/scienthoon/jev-ood-calibration (README; unknowable-label task and correction note).
- **Evidence type:** independent evaluations (four authors, each stated as unaffiliated or implied so); independence: yes.
- **Model:** TypeSafe Jev 1.13.0 hosted (via OpenRouter, Vercel gateway); size and architecture unknown (vendor does not disclose).
- **Task / rejection mechanism:** priorbench: 30 out-of-scope messages against a closed label set with no "none" option. jujumilk3: unanswerable items with and without an `unknown` option. ickma2311: CLINC150 with an OOS class (n=35 OOS items). scienthoon: unknowable organisation-specific priority score.
- **Data provenance:** author-built; **n:** 30 / ~400-item audit / 35 OOS of 200 / 900 synthetic tickets; **raw cases available:** published per the READMEs (not inspected).
- **Fixed / mitigated?** Offering an explicit unknown option is the mitigation in two of the studies. **fix evaluated?** yes in jujumilk3.
- **Relevant local classes:** L2, L3, L8; Q5, Q6.

## What the sources report
- priorbench: 0 of 30 out-of-scope messages were flagged, at 0.99 confidence overall (cake recipe 0.94, random letters 0.97), because there was no "none" option.
- jujumilk3: with an unknown option accuracy on unanswerable items was 0.950; removing it dropped that to 0.000 with the stereotyped answer rate rising from 0.03 to 0.79 at 0.79 confidence. Option reordering caused zero argmax flips in 400 and a mean shift of 0.005 (contrast with Laya and jeff).
- ickma2311 (pre-registered, verdict AMBIGUOUS): on CLINC150, Jev OOS recall 0.714 vs 0.486 for a nano LLM (exploratory, n=35); Jev accuracy 0.870; error-ranking AUROC 0.734 vs nano 0.816.
- scienthoon: on an unknowable priority score Jev had 44.7% accuracy with mean stated probability 0.74.

## Strength and caveats
- Consistent message: the model returns a valid label for out-of-scope text unless an abstain option is present, and with one present it can use it well (0.950). This matches Q5's concern but shows `none` as a competing label can work for hosted Jev.
- Whether the same holds for small encoders is not tested here (eco-laya-issues-confidence-and-routing shows Laya often not choosing `none`). Per-study n is small; the 0.950 -> 0.000 figure is on a specific unanswerable-item set.
