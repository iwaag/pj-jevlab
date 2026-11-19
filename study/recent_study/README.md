# Recent arXiv work on Jev-style decision models (2026-09-15 to 2026-10-07)

Compiled 2026-10-08 (episode `study/recent_study/p1`; brief in [braindump.md](../../devdocs/episodes/study/recent_study/p1/braindump.md)).

- **What this is:** a literature survey. No model was run.
- **Purpose:** collect the ideas in the recent arXiv papers on Jev-style typed decision models ("System One" models), and check whether the lab's experiments repeat published work.

## Scope at a glance

- **Search:** the arXiv API on 2026-10-08, 34 queries, 195 hits, **111 papers kept** ([search-log.md](search-log.md)).
- **Depth:** 42 papers read in full by five parallel readers, each covering one theme. I spot-checked six key numbers against the PDFs: 2610.07716, 2609.29769, 2610.01006, 2609.39496, 2610.00831 and 2610.00346. All matched.
- **Status of the papers:** all are preprints 1–3 weeks old, none peer reviewed, and several are by vendors of competing models.

## Files

| File | Contents |
|---|---|
| [catalog.md](catalog.md) | All 111 papers by theme, one line each, plus a 9-paper follow-up section |
| [search-log-p2.md](search-log-p2.md) | Follow-up search (2026-10-08 to 2026-10-13): method, rate-limit workaround, per-query yield |
| [reinvention-check.md](reinvention-check.md) | Each lab experiment against the papers: prior, parallel, extends or lab-only; what to stop; what can still be claimed |
| [ideas.md](ideas.md) | Reusable methods, controls and designs, with source, applicable lab system and cost; offline-first |
| [evidence/labels-and-injection.md](evidence/labels-and-injection.md) | 7 cards: label vs definition, yes/no swap, context flips, JevAdvBench, injection, security |
| [evidence/missing-information-and-abstention.md](evidence/missing-information-and-abstention.md) | 7 cards: sufficiency questions, rejection bottleneck, threshold transfer, value-of-information slots, "I don't know", Laya calibration |
| [evidence/second-pass-and-cascades.md](evidence/second-pass-and-cascades.md) | 8 cards: readout stability, "wrong in the same places", coherence checks, judge cascades |
| [evidence/populations-simulation-agents.md](evidence/populations-simulation-agents.md) | 8 cards: KITE, JEVal social simulation, persona effects, evaluation vs simulation, Doom deferral, chess distillation |
| [evidence/methods-and-training.md](evidence/methods-and-training.md) | 10 cards: AnyJev, PACT, order-invariant heads, RLCD vs cross-entropy, LLM-as-Jev, looped models, ordinal bias |
| [evidence/evaluation-methodology.md](evidence/evaluation-methodology.md) | The early evidence audit with its 14-item checklist (lab status judged from a summary), and a self-audit's pitfalls |

## Main findings

1. **The field has caught up with the lab's main results.**
   - set5's finding, that a second pass on a one-pass scorer is the renormalised first pass, was published three days later on seven other model families (2610.07716).
   - "Decision models decide anyway when a fact is missing" is reported for hosted Jev in several papers: 2610.01006, 2609.34024, 2609.39496, 2610.03935.
   - "Copies of one model are one voter" matches 2609.29769, 2610.09188 and 2609.36399.
2. **Some of the lab's results are still unpublished.** No paper found does any of the following:
   - shows that the *form* of a decision model's errors decides whether a collective tolerates them (set6 p2);
   - measures a mixed decision-model panel as several independent voters (set6 p1; this needs a check on confident errors first);
   - shows a sufficiency check working on W2 but failing on priority-rule W3 (set4 C1);
   - tests the key-naming-in-state attack on Kev-class models;
   - measures Japanese.
3. **The most useful new tools for the lab's open failure, missing evidence:**
   - a threshold on the fallback option's probability, with thresholds fitted per workload (2609.39496, 2610.03387, 2609.33843);
   - a thresholded answer-free sufficiency score (2610.01006). The lab already logs this as set4's C1 for K27.

   Both can first be tested offline on stored records.
4. **Option labels in the input matter more than definitions** on encoder-style models (2609.26758, 2610.02586), but trained decoder heads resist this (2610.00346). The cause is the rendering `"{label}: {definition}"`, which Kev also uses, so a description-only rendering test on the key-naming cases is cheap and diagnostic.
5. **Cascades work only when the first stage's errors sit at low confidence and the fallback errs elsewhere** (2609.29769, 2610.07177, 2610.09683, 2609.26550). This explains set4's null results.
6. **RLCD-style training has not beaten cross-entropy** for one-pass scorers in three independent papers (2610.02486, 2610.06744, 2609.38850).
7. **Order sensitivity has cheap fixes:** rotation averaging (2610.00831) and order-blind heads (2610.01601, 2610.06744). The lab has not applied them to J or G.

## Limits

- arXiv only, keyword search; workshop papers, blogs and GitHub reports are not covered here (see [../ecosystem/](../ecosystem/)).
- 69 of the 111 papers were read at abstract level only.
- The paper evidence is almost all on hosted Jev or small open models; transfer to K27, W12, A27 or J is untested in every case.
- The lab-status column of the 14-item checklist was judged from a summary of the lab's work, not item by item.

## What's new since 2026-10-07 (`study/run-001`, 2026-10-13)

A follow-up search for papers submitted 2026-10-08 through 2026-10-13, same method and query list, found **9 new papers** (1 more candidate excluded as a false-positive keyword match) — a small amount of new material, as expected for a 6-day window. Full method and per-query yield: [search-log-p2.md](search-log-p2.md); rows added to [catalog.md](catalog.md) under "Follow-up"; two papers prompted additions to existing evidence files rather than new ones.

- **Nothing in the "still unpublished" list (main findings §2 above) got published.** None of the 9 new papers measures a mixed decision-model panel, the error-form/collective-tolerance result, the W2-vs-W3 sufficiency split, the key-naming-in-state attack on Kev-class models, or Japanese. All five open questions from §2 and the "Open questions worth experiments" list stand as before.
- **Two papers add to findings already on record, without changing a verdict:**
  - 2610.11436 extends the label/injection theme (`evidence/labels-and-injection.md`) with a new attack surface: a one-character edit to a judged candidate moves hosted Jev's judge false-acceptance rate from 1.0% to 26-26.5%, depending on output-label presentation. Different mechanism from the lab's own key-naming attack (judge-grading presentation vs a state text matching a key), so it neither confirms nor contradicts the lab's finding.
  - 2610.11392 (TypedBench) extends the evaluation-methodology theme (`evidence/evaluation-methodology.md`) with a benchmark built around calibration, wording/framing sensitivity and realised cost under asymmetric cost matrices — relevant to the "per-type calibration" open question and to any future cost-weighted gate design.
- **The other 7 new papers** (agent-workflow cost/reliability on Jev, multilingual/knowledge/stance benchmarking, Jev as a frozen RL component, compact multimodal JEV inference, knowledge tracing, budgeted feature acquisition) are domain or engineering extensions of existing catalog themes; none bears closely enough on a specific lab experiment to warrant a card, so they are abstract-level catalog rows only.
- **Method note:** arXiv's export API (used by the original search) was unreachable this session (HTTP 429 throughout); the follow-up used arXiv's HTML search pages instead, paced manually to avoid the same rate limit. See `search-log-p2.md` for what this changes about how "new" was determined (by arXiv id prefix, not the page's shown submission date, since the HTML page shows the latest revision's date).
