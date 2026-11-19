# Positive reports: Entagl routing study and Arize spam/moderation study

- **Sources:** https://www.entagl.com/blog/typesafe-jev-benchmark-ai-decision-models and https://arize.com/blog/typesafe-jev-llm-judge/ (accessed 2026-10-02; locators: results and limitations sections; read via fetch summaries, not verbatim).
- **Evidence type:** documented deployment / vendor-adjacent evaluation (Entagl evaluates for its own routing product; Arize is an LLM-observability vendor); author independence: yes of TypeSafe, but both have commercial interests.
- **Model:** hosted Jev (Entagl: unspecified version; Arize: unspecified); size unknown.
- **Task:** Entagl: message routing and agent selection for customer service, 1,357 labelled decisions on 283 cases plus 402 real routing decisions from two client workspaces over 21 days; languages English, Turkish, Arabic varieties and others. Arize: spam classification on 18,514 emails and a UK events moderation test.
- **Rejection mechanism:** confidence gating with fallback: Entagl "use Jev only when >=85% sure" handled 88% of decisions at 99.75% accuracy, sending 17 of 20 errors to larger models; at >=97% confidence 986/986 correct. Arize: sending the 4.6% of emails scored 0.3-0.7 to a person left the rest at 99.5% accuracy.
- **Data provenance:** real traffic partly; labels by the vendor or original system; **raw cases available:** no (aggregates).
- **Fixed / mitigated?** Entagl computes missing facts in code and hands them to Jev; **fix evaluated?** n/a.
- **Relevant local classes:** L8 positive counterpart; Q4, Q5.

## What the sources report
- Entagl: Jev 98.5% vs Gemini 99.0% on labelled tests; on real traffic message decisions 91-94% vs 87-91% for the original system, but agent selection 84-91% vs 98% for the original; English 99.1%, Turkish 98.4%, Arabic 96.5%. Listed weaknesses: arithmetic, date comparisons, long irrelevant input, manipulation attempts, missing context.
- Arize: Jev 98.3% vs a TF-IDF classifier trained on ~14,800 examples at 98.4%; Jev 96% vs Gemini Flash-Lite 86% on moderation; no explanations available.

## Strength and caveats
- These are the strongest positive deployments found, with confidence-gated fallback measured. Both are hosted Jev, on in-distribution classification (spam, routing), where the local failure classes are least likely to arise. Neither tests off-topic or override input.
- Real-traffic labels for Entagl were not independently checked.
