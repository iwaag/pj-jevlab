# Search log — study/run-002 (2026-10-19)

Question: Jev-style research not yet covered by `study/`. Cut-off: **2026-10-19** (search run that day). Previous cut-off: 2026-10-13 ([../recent_study/search-log-p2.md](../recent_study/search-log-p2.md)).

## arXiv

Source: `arxiv.org/search/` listing pages with curl (the export API answers a redirect on http and was not used). No 429 this time with 3–8 s spacing. Hits were deduplicated by id against `recent_study/catalog.md` and both earlier search logs.

| Query (field) | Result | New 2610.* ids |
|---|---|---|
| `Jev` (all fields), sorted by submitted date, 3 pages | 146 hits, 84 with a 2610 id | 42, all kept |
| `"System One" decision model`, `"typed decision"`, `"decision model" calibrated one forward pass`, `OpenAI Decisions API`, `Jev-style`, `System-1 decision probabilities options single forward pass` (abstract) | 5–75 hits each | 13 more |
| `"System One"`, `"System One" models`, `"typed decision models"`, `"typed decisions"`, `"fallback option"`, `JevBench`, `TypeSafe`, others (all fields, 2 pages each) | up to 1,845 hits (mostly unrelated physics/CS use of "system one") | 28 candidates (13 already counted above) |
| Date-bounded (submitted 2026-10-08 to 10-20) `System One`, `decision models`, `decision model` (title/all) | 20–56 hits each | 9 candidates |

Screening rule (as in the original survey): keep a paper that studies, builds, attacks or applies a typed one-pass decision model, or surveys one. `all:Jev` gave 42 new ids, all kept. The other queries gave 37 further candidates: 25 kept, 1 excluded as off-topic (2610.19345, "decision model" in the decision-theory sense) and 11 false positives (physics, maths, statistics, e.g. 2610.07586, 2610.11462, 2610.20491). Plus 3 September ids. Total 70 kept.

### Finding that changes the method

The earlier surveys relied on `all:Jev`. **28 of the 70 kept papers** (25 October, 3 September) were found only by non-`Jev` queries and would have been missed; their abstracts say "System One", "typed decision model", "decision model" or "System 1" (for example 2610.19856, 2610.18233, 2610.22066, 2610.19811, 2610.18579, 2610.19536, 2610.12292, 2610.18773). Two September papers (2609.30454, 2609.39111) were missed the same way. Future searches should query these phrases as well as `Jev`.

### Window

- 2610.* ids at the earlier boundary and after: the earlier follow-up stopped at 2610.13092 (submitted 10-09) and so missed 10-09 to 10-16.
- The newest id found on 2026-10-19 was 2610.23804 (submitted 2026-10-16). **No paper submitted 10-17 to 10-19 appeared** in any query; either none matched or arXiv had not indexed them (weekend lag is plausible). Run the same queries again later to close this gap.

## Web search (standard mode, 6 queries)

Queries: independent evaluation/blog of Jev (Oct 2026); workshop/tech-report/OpenAI Decisions API evaluation; new Jev-style open model releases after 10-13; Cloudflare Clef; Amazon Strands Decider 2B.

- Results are overwhelmingly vendor pages, launch coverage and explainer blogs relaying TypeSafe's own numbers (self-reported benchmarks; reference labels are an average of two frontier LLMs per one explainer). No independent human-labelled benchmark beyond the arXiv papers was found.
- No workshop proceedings or technical reports on Jev-style models were found by search; the academic follow-up is the arXiv set.
- Open-model releases found: Cloudflare Clef/Clef-flash and Amazon Strands Decider 2B (both 2026-10-01, before the cut-off but absent from `open/`); noted in the catalog as secondary sources. Nothing dated after 10-13.
- Not repeated: Hugging Face model-hub search, GitHub search (outside this run's tools), so open clones created after 10-13 are not covered.

## Depth

- 16 papers read in full text (PDF → pdftotext), cards in [evidence/](evidence/): chosen for the lab's open questions (option order/naming, option set, fallback and missing answer, calibration and thresholds, agent delegation, benchmarks, labelled attack, order-invariant architectures). Cards were drafted by subagents from the PDF text; the lead did not re-verify each number against the PDFs, so spot-check a number before quoting it.
- The other 55 are abstract-level (arXiv abstract page).

## Limits

arXiv-only plus secondary web coverage; keyword search; abstract-level for most rows; vendor-authored papers are flagged in the cards; no code was run.
