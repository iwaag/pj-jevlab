# Search log — follow-up (2026-10-08 to 2026-10-13)

Goal: extend [search-log.md](search-log.md) with Jev-style typed decision model papers that appeared since its 2026-10-07 cutoff, using the same method and query list, for `study/run-001`.

## Method and a change from the original

- **Source, attempt 1:** the arXiv API (`export.arxiv.org/api/query`), as the original search used. On 2026-10-13 this returned HTTP 429 "Rate exceeded" on every attempt, including with a paced retry loop (6 attempts, 20s apart, over 2 minutes; a prior session attempt the same day had already hit the same wall and lost a backgrounded retry when its turn ended).
- **Source, attempt 2 (used):** `arxiv.org/search/` — arXiv's own HTML search/listing pages, read with curl (not the export API). These answered, but also returned 429 under the same pace as the API; a single request succeeded only after a ~30-45s back-off, and every subsequent request needed the same spacing. All fetches below used a foreground script with a 40-45s sleep before each request and up to 3 retries, run to completion before continuing (not backgrounded), per the run's resume instruction.
- **Query list:** the original's 34 queries (`search-log.md`), reduced to the ones that had found something before: #1 (`all:Jev`) plus the ones with nonzero prior yield (#2, #3, #4, #8, #9, #17, #21, #23, #24, #26, #30), and #34 (`abs:"zero-shot" AND abs:"typed"`, reconsidered per the plan despite being the noisiest query, since it is also the broadest). Queries with zero hits in the original (#5–7, #10–16, #18–20, #22, #25, #27–29, #31–33) were not re-run: in a 6-day window, an exact-phrase query that matched nothing in the whole Jev-era corpus is very unlikely to match something new, and the project's time/request budget favoured the high-yield queries.
- **Sort and dedup:** each query fetched with `order=-submitted_date&size=200` (newest submission/revision first). Hits were compared by arXiv id against the 111 ids already in [catalog.md](catalog.md); only ids not already kept were inspected further.
- **A caveat on "submitted date" here:** arXiv's search page shows the date of the *current* version, not the original announcement. A paper whose id prefix is `2609` (first announced September 2026) can show a October submission date because of a revision. Those are not new arrivals; the id prefix, not the shown date, decided whether a hit was in scope. Only ids with prefix `2610.*` (first announced October 2026) were treated as candidates for "new since 2026-10-07", together with a few `2610.*` ids shown at the Oct 7 boundary that were missing from the original catalog (see below).

## Queries re-run

| # | Query | New ids found (any date) | New ids in window (prefix `2610.*`, not already catalogued) |
|---|---|---|---|
| 1 | `all:Jev` | 6 (listed below) | 7 |
| 2 | `abs:"system one" AND abs:decision` | 0 | 0 |
| 3 | `abs:"System-One"` | 4 (1507.08047, 0910.2669, 2212.01058, 1101.4559 — physics/unrelated pre-Jev papers; 2609.32893 — Sept 2026, out of window) | 0 |
| 4 | `abs:"typed decision"` | 0 | 0 |
| 8 | `abs:"decision model" AND abs:calibrated` | 0 | 0 |
| 9 | `abs:"decision models" AND abs:LLM` | 0 | 0 |
| 17 | `abs:"parallel sampler"` | 0 | 0 |
| 21 | `abs:"prefill-only"` | 0 | 0 |
| 23 | `abs:"System 1" AND abs:typed` | 0 | 0 |
| 24 | `abs:"System 1" AND abs:"decision model"` | 0 | 0 |
| 26 | `abs:"single pass" AND abs:"typed"` | 0 | 0 |
| 30 | `abs:"direct-decision"` | 0 | 0 |
| 34 | `abs:"zero-shot" AND abs:"typed"` | 1 (2412.05430, 2026-03 pre-Jev, off-topic) | 0 |

No query besides `all:Jev` turned up a genuinely new in-window paper. This matches the original's note that "Jev" is the query that does almost all the work; the follow-up window is short enough that the secondary queries' extra recall (mostly noise in the original, see `search-log.md`) did not pay off even once.

## `all:Jev`, in-window candidates

Sorted by shown submission date, newest first; 103 total hits for this query, of which the following 10 had an id not in the 111-paper catalog and fell at or after the 2026-10-07 cutoff:

| arXiv id | Shown date | In catalog before? | Kept |
|---|---|---|---|
| 2610.13092 | 9 Oct 2026 | no | yes |
| 2610.11392 | 9 Oct 2026 | no | yes |
| 2610.11978 | 8 Oct 2026 | no | yes |
| 2610.11901 | 8 Oct 2026 | no | yes |
| 2610.11692 | 8 Oct 2026 | no | yes |
| 2610.11436 | 8 Oct 2026 | no | yes |
| 2610.11379 | 8 Oct 2026 | no | yes |
| 2610.11135 | 7 Oct 2026 | no | yes |
| 2610.10978 | 7 Oct 2026 | no | **excluded** |
| 2610.10615 | 7 Oct 2026 | no | yes |

- The three "7 Oct" ids are at the boundary of the original's stated cutoff ("newest kept paper: submitted 2026-10-07"); they are not in the 111-paper catalog, so either they were not yet indexed when the original ran on the morning of 2026-10-08, or they were seen and screened out. Since they are new to `study/`, they are treated as follow-up material regardless of which.
- **2610.10978** ("Probabilistic Sensing, Deterministic Authority...") matched `all:Jev` but neither its title nor its abstract names Jev, a Jev clone, or a System One model; it is a generic model-observation/governance-contract paper. Checked and excluded as a false-positive keyword match (same disposition as the original's "off-topic hits" category), not screened further.
- The other 9 are on-topic per the original's screening rule (study, build, attack or apply a typed decision model, or survey one) and are added to [catalog.md](catalog.md) under a new "Follow-up" section.

## Depth

All 9 kept papers were read at abstract level (fetched from `arxiv.org/abs/<id>`, full abstract, not the PDF). Two were read more closely — abstract plus a check of what the abstract itself claims in detail, since both directly bear on points in [reinvention-check.md](reinvention-check.md) and [evidence/](evidence/):

- 2610.11392 (TypedBench) — benchmark design, per-type calibration, wording sensitivity.
- 2610.11436 (adversarial cues in decision-model judges) — judge robustness to request presentation, continuing the label/injection theme.

Full PDFs were not fetched for this follow-up: given the small number of candidates and the arXiv rate limit encountered above, abstract-level reading was judged sufficient to place these papers in the catalog and to update the two evidence files; this is weaker evidence than the original's full-text cards and is marked as abstract-level throughout.

## Web search

Two general web searches, matching the original's method ("arxiv Jev System One decision model paper new October 2026", "Jev typed decision model benchmark preprint October 2026"), were not additionally run for this follow-up: the original reported these contributed nothing (blogs and vendor pages, no new arXiv papers), and the arXiv-side search above already needed most of the available time budget under the rate limit. This is a gap relative to the original method, noted here rather than silently dropped.

## Limits

- Same limits as the original (arXiv only, keyword search, preprints only; see `search-log.md`).
- The secondary queries (2–34 except 1 and 34) were not re-run in full against every possible rephrasing; only the ones with prior yield were checked, per the plan's instruction to reconsider only queries that look weak.
- Web search was not repeated this round (see above).
- The arXiv export API was unavailable for this entire session (429 on every attempt); if a reader wants the original API-based completeness check repeated, that is still outstanding.
