# Search log — study/recent_study (2026-10-08)

Goal: list every arXiv paper on Jev-style typed decision models ("System One" models) posted since Jev's launch (2026-09-15). Use them as sources of ideas and as a check against reinventing results the lab has already produced or is about to produce.

## Method

- **Source:** the arXiv API (`export.arxiv.org/api/query`), sorted by submission date, 100 results per query, keeping entries published on or after 2026-09-01. Run from the shell with curl on 2026-10-08 between about 14:10 and 14:40 JST. The cutoff is therefore arXiv's listing as of the morning of 2026-10-08 (newest kept paper: submitted 2026-10-07).
- **Completeness check for the main query:** `all:Jev` returns 93 results in total, of which 91 are dated September 2026 or later. The other two are from 2024 and unrelated. Paging to `start=100` returns nothing, so this query is complete.
- **Web search:** two general web searches ("arxiv Jev System One decision model paper", "arxiv typed decisions calibrated decision model Jev clone benchmark") returned only blogs and vendor pages and no arXiv papers. They contributed nothing to the candidate set.
- **Full text:** 42 papers were downloaded as PDFs from arxiv.org and converted with `pdftotext -layout`. The rest were read at abstract level.

## Queries

| # | Query | Hits ≥ 2026-09-01 | New |
|---|---|---|---|
| 1 | `all:Jev` | 91 | 91 |
| 2 | `abs:"system one" AND abs:decision` | 25 | 5 |
| 3 | `abs:"System-One"` | 41 | 12 |
| 4 | `abs:"typed decision"` | 27 | 8 |
| 5 | `abs:"typed decisions"` | 27 | 0 |
| 6 | `abs:TypeSafe` | 16 | 0 |
| 7 | `abs:RLCD` | 5 | 0 |
| 8 | `abs:"decision model" AND abs:calibrated` | 25 | 6 |
| 9 | `abs:"decision models" AND abs:LLM` | 18 | 2 |
| 10 | `abs:"noul"` | 5 | 0 |
| 11 | `abs:"/v1/systemone"` | 0 | 0 |
| 12 | `abs:"Solar Decide"` | 0 | 0 |
| 13 | `abs:"Liquid d1"` | 0 | 0 |
| 14 | `abs:"Span-01"` | 0 | 0 |
| 15 | `abs:"Decisions API"` | 0 | 0 |
| 16 | `abs:JevBench` | 1 | 0 |
| 17 | `abs:"parallel sampler"` | 2 | 2 |
| 18 | `abs:"one forward pass" AND abs:classification AND abs:calibrat*` | 0 | 0 |
| 19 | `abs:"zero-shot classifier" AND abs:LLM AND abs:calibrat*` | 0 | 0 |
| 20 | `abs:Laya AND abs:decision` | 12 | 0 |
| 21 | `abs:"prefill-only"` | 2 | 1 |
| 22 | `abs:"decision head" AND abs:LLM` | 0 | 0 |
| 23 | `abs:"System 1" AND abs:typed` | 4 | 1 |
| 24 | `abs:"System 1" AND abs:"decision model"` | 4 | 1 |
| 25 | `abs:"single-pass" AND abs:decision AND abs:calibrat*` | 0 | 0 |
| 26 | `abs:"single pass" AND abs:"typed"` | 8 | 6 |
| 27 | `abs:systemone` | 0 | 0 |
| 28 | `abs:"structured decision" AND abs:calibrat*` | 0 | 0 |
| 29 | `abs:"decision models" AND abs:agent` | 10 | 0 |
| 30 | `abs:"direct-decision"` | 7 | 5 |
| 31 | `abs:"System One" AND abs:LLM` | 13 | 0 |
| 32 | `abs:SemIf OR abs:jeff AND abs:GLiClass` | 1 | 0 |
| 33 | `abs:"option logits" AND abs:calibrat*` | 0 | 0 |
| 34 | `abs:"zero-shot" AND abs:"typed"` | 65 | 55 |

Queries 1–19 yielded 126 unique candidates and queries 20–34 added 69 more, 195 in all. Almost every hit from queries 3, 26 and 34 is off topic: physics ("system one" as in "system 1"), unrelated zero-shot work, NER datasets.

## Screening

- **Rule:** keep a paper if it studies, builds, attacks or applies a model that returns typed option probabilities without generating text (Jev, a Jev clone, or a self-described decision / System One model), or if it is a survey of such models.
- **Kept:** 111 papers, listed in [catalog.md](catalog.md).
  - 107 are in scope.
  - 4 are adjacent, kept for context and marked as such. One more adjacent paper, an LLM persona crowd-evacuation simulation, is kept because the owner's set6 line asks the same kind of question.
- **Excluded:**
  - 82 off-topic hits, almost all from queries 3, 26 and 34 (physics, astronomy, robotics, NER, vision and so on);
  - one grid-safety certification paper (2609.28182);
  - one observability foundation model paper (2610.05577).
- **Already cited in `study/`:** 2609.30216 (Jev in the Wild) and 2609.02292 (SCX router) appeared in earlier study files. Every other kept paper is new to `study/`.

## Selection for full-text reading

The 42 papers read in full were picked because they bear on a lab experiment or a lab design choice. The themes are:

- option labels and injection (lab: key-naming override, opaque keys);
- missing information and abstention (lab: the W2/W3 missing-evidence failure);
- second passes, voting and cascades (lab: set4, set5, set6 p1);
- populations and simulations (lab: set6 p1/p2);
- open-model methods (lab: order sensitivity of J and G, readout choice, RLCD);
- evaluation methodology (lab: benchmark design).

Domain evaluations of hosted Jev (crash narratives, medicine, networks and so on) were left at abstract level unless they report a mechanism.

## Limits

- arXiv only. Workshop papers, blogs, GitHub reports and non-arXiv venues are not covered. `study/ecosystem/` covers some of them.
- Keyword search can miss papers that never use "Jev", "System One", "typed decision" or "decision model". Query 34 shows the cost of widening the search: 55 new hits, none relevant.
- These papers are 1–3 weeks old preprints. None is peer reviewed, and several are by vendors of competing models; the cards mark which.
- PDF-to-text conversion loses table layout in places. The readers checked numbers against the surrounding text, and cards say when a number could only be found in the abstract.
