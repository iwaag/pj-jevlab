# recent_study_p3: Jev-style decision-model papers not yet covered (2026-10-08 to 10-19)

Study run `study/run-002`, 2026-10-19. Builds on [../recent_study/](../recent_study/README.md) (111 papers to 10-07, 9 more to 10-13). Everything here is a preprint or secondary coverage; vendor claims are kept apart from independent measurements in the cards.

## What is new

1. **70 arXiv papers were missing from the earlier catalog** (71 listed, 1 excluded). 42 matched `Jev` but fell between 10-09 and 10-16, after the earlier follow-up's stop; 28 (25 October, 3 September) were found only by non-`Jev` queries (their abstracts say "System One", "typed decision model", "decision model") and were invisible to the earlier `all:Jev` search. See [search-log.md](search-log.md); this is a method correction, not only new papers.
2. **16 papers read in full** ([evidence/](evidence/)). The findings that matter for the lab:
   - **Option order and option set.** Hosted Jev flips 4.7–5.3% of answers under shuffling (re-ask floor 1.3%), up to 17% with 20 options in other measurements; adding one irrelevant option moves the odds between gold and its rival (0.20–0.52 nats, pre-registered). Sorting options does not fix it; Runoff does (≈0 flips, two passes, no training).
   - **Fallback options are a separate failure.** Recall of the fallback class 23.1% against 97.9% for regular classes, equivalent wordings change up to 39.8% of decisions, and thresholds do not transfer across wordings (2610.19856).
   - **Missing answers.** Models lose 11–15 points when the gold option is removed, an optional abstain option adds under 1 point for hosted Jev (2610.18529); zero-answer abstention ranges 7.7–85% (2610.14631).
   - **Confidence tracks fragility, not correctness** (flip AUROC 0.81–0.93, error AUROC 0.59–0.84, 2610.19536); finite-sample threshold selection (Learn Then Test) holds a risk budget where naive thresholds fail in about half the settings (2610.19811).
   - **Agents.** Isolated accuracy misranks decision models; a fixed 0.5 threshold lowers task success by 19.0 points while a threshold fitted on the agent's own trajectories saved 14.2% cost at no loss (2610.21412, whose authors also rank their own models).
   - **Label channel.** Renaming only the permissive option takes fail-open to 93–100% on models that feed the key to the network (2610.12292).
3. **Two non-arXiv model releases** (Cloudflare Clef, Amazon Strands Decider 2B) are noted in [catalog.md](catalog.md) from launch coverage only; no independent source beyond arXiv evaluations was found.

## Files

| File | Contents |
|---|---|
| [catalog.md](catalog.md) | One line per paper (71 arXiv + 3 non-arXiv), by theme |
| [search-log.md](search-log.md) | Queries, cut-off, exclusions, gaps |
| [evidence/option-set-order-and-fallback.md](evidence/option-set-order-and-fallback.md) | Six cards |
| [evidence/calibration-abstention-and-benchmarks.md](evidence/calibration-abstention-and-benchmarks.md) | Eight cards |
| [evidence/labels-and-architectures.md](evidence/labels-and-architectures.md) | Two cards |
| [reinvention-check.md](reinvention-check.md) | Addendum against the lab's experiments |
| [ideas.md](ideas.md) | Ten proposals, P1–P10 |

## Uncertain

- Nothing submitted 2026-10-17 to 10-19 was found; re-run the searches later.
- Most rows are abstract-level; card numbers were drafted from the PDF text and not each re-verified.
- Authors of Runoff, Prism-1, Jeva, Verdict-MQ, StartLux-Decision and JevAgentHarness rank models they built.
- Hugging Face and GitHub were not searched; open clones after 10-13 are not covered.
