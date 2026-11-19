# Search log — schooling_sim (2026-10-06)

Step 2 of the study plan. Search cutoff: 2026-10-06 (newest source opened: arXiv 2604.10690, April 2026). Three parallel searchers each covered two of the plan's six areas, using one brief. They opened primary sources where possible (arXiv or PMC full text via curl and pdftotext) and recorded the read level on every card. Their fragments are merged below unchanged. A failed or empty search is not evidence that no work exists. The cards are in [evidence/](evidence) (see [catalog.md](catalog.md)).

## Coverage summary

| Area (plan step 2) | Fragment | Cards | Pre-2010 source |
|---|---|---|---|
| Classical schooling and predation models | [A](#fragment-a-schooling-and-predation-metrics-and-protocols) | SP-01 to SP-05 | Reynolds 1987 (SP-05); Hamilton 1971 (in SP-02) |
| Metrics and protocols | [A](#fragment-a-schooling-and-predation-metrics-and-protocols) | MP-01 to MP-03 | Couzin et al. 2002 (MP-01) |
| Perception and neighbourhood | [B](#fragment-b-perception-and-neighbourhood-error-and-contagion) | PN-01 to PN-04 | Ballerini et al. 2008 (PN-01); Tian et al. 2009 (log only) |
| Error and contagion | [B](#fragment-b-perception-and-neighbourhood-error-and-contagion) | EC-01 to EC-04 | None opened. Radakov 1973 and Treherne and Foster 1981 are cited inside EC-01 but were not opened |
| Learned and language-based agents | [C](#fragment-c-learned-and-language-agents-spatial-language) | LA-01 to LA-04 | Ward et al. 2001 (search summary only) |
| Spatial language for models | [C](#fragment-c-learned-and-language-agents-spatial-language) | SL-01 to SL-04 | Levinson 2003 and Hill 1982 (cited in SL-02, not opened) |

**Totals.** There are 24 cards. Two sources were carded twice by different searchers, and the duplicates are kept as cross-references, so there are **22 distinct cases**:

| Source | Primary card | Cross-reference |
|---|---|---|
| Olson et al. 2013 | SP-01 | LA-03 |
| Rosenthal et al. 2015 | EC-01 | SP-04 |

This is slightly above the plan's 12–20 target. All six areas are covered. 23 of the 24 cards rest on full text of at least the main sections. The exceptions are:
- EC-04, a partial read;
- SL-04, abstract and introduction only;
- the C-xx, G-xx, S-xx and M-xx cards of the broad survey, which are reused as they are and not re-read.

**Main gaps (details in the fragments):**
- **The p2 design itself.** No source scores a learned or language model's per-agent decisions against the rule it replaces in a moving collective. None measures the spatial or temporal correlation of agent errors.
- **Views and choices.** No source tests a discretised sector × distance-band view against continuous perception. None uses a pure binary left/right turn at every step.
- **Errors and baselines.** No source has errors that are a deterministic function of the input. None defines a noise-matched random-error baseline.
- **LLMs and predators.** No LLM-driven swarm with a predator was found.
- **Not carded:** the confusion-effect originals (Ioannou et al. 2008, Tosh 2011), escape-wave and fountain-effect models, and Boids imitation by a classifier.
- **Japanese sources.** Japanese searches gave only review-level or translated material, none of it carded.

---

## Fragment A: schooling and predation; metrics and protocols


| # | Query or fetch | Candidate URLs | Decision and reason (incl. access level) |
|---|---|---|---|
| 1 | WebSearch: Olson Hintze Dyer Knoester Adami 2013 predator confusion swarming arXiv | arxiv.org/abs/1209.3330; arxiv.org/pdf/1310.6012; arxiv.org/pdf/2009.02079 (Klamser, already C-12) | Kept 1209.3330 → SP-01 (full text via curl+pdftotext). Followed lead 1310.6012 → SP-02. Skipped 2009.02079 (already C-12). |
| 2 | WebSearch: Couzin Krause James Ruxton Franks 2002 collective memory pdf | jmvidal.cse.sc.edu/library/couzin02a.pdf; arxiv 2507.16102 (noise-induced collective memory) | Kept couzin02a.pdf → MP-01 (full text). 2507.16102 not opened (budget). |
| 3 | WebSearch: Tunstrøm 2013 collective states PLoS Comput Biol | journals.plos.org/.../pcbi.1002915; arxiv 1409.6430 (Calovi data-driven model) | Kept PLoS (printable PDF, full text) → MP-02. 1409.6430 not opened (budget). |
| 4 | WebSearch: Ioannou Guttal Couzin 2012 virtual prey Science pdf | science.org/doi/10.1126/science.1218919; d-nb.info/1130587576/34 | Kept the KOPS author copy (full text of the main paper; SM not read) → SP-03. |
| 5 | WebSearch: Ioannou Tosh Neville Krause 2008 confusion effect neural networks | Behav Ecol 19:126 (no OA link found); rsos.260483 (target occlusion) | Not carded: no open full text found in one try. Its existence is confirmed via the SP-03 reference list (ref 26). Gap. |
| 6 | WebSearch + curl: Rosenthal et al. 2015 PNAS hidden networks | pmc.ncbi.nlm.nih.gov/articles/PMC4403201 | Europe PMC fullTextXML returned HTTP 500; the PMC HTML worked. Full text read up to network reconstruction → SP-04. |
| 7 | WebSearch: Demšar Hemelrijk Hildenbrandt Bajec 2015 composite tactics | research.rug.nl; lrss.fri.uni-lj.si/cb/publications.html; itzsimpl.info/papers/ | WebFetch (fetch summary) of the lab page gave a preprint URL. The first URL had the wrong letter case (404); a directory listing gave the correct one. Preprint full text → MP-03. Also downloaded Demšar & Lebar Bajec 2014 "Simulated predator attacks on flocks: a comparison of tactics" (Artificial Life) but did not card it (budget). |
| 8 | Fetch: red3d.com Reynolds 1987 boids | red3d.com/cwr/papers/1987/boids.html (curl 403; WebFetch = abstract/citation only); cs.toronto.edu/~dt/siggraph97-course/cwr87/ | Full HTML text from the Toronto mirror → SP-05. |
| 9 | WebSearch: Hamilton 1971 geometry for the selfish herd | csun.edu/~dgray/BE528/Hamilton1971Selfish_herd.pdf | Full text available; read only the abstract and §1. Folded into SP-02 as the original model whose assumption Olson et al. test. |
| 10 | WebSearch: fountain effect / flash expansion simulation Hemelrijk Hildenbrandt | nature.com/articles/s42003-024-07267-2 (collective anti-predator escape manoeuvres, optimal attack and avoidance); arxiv 2210.03989 (SDE predator-avoidance) | Not carded (budget). Lead for the fountain effect: s42003-024-07267-2 reports that fountain manoeuvres emerge from an optimal escape angle plus social interactions (search summary only). |
| 11 | WebSearch (Japanese): 魚群 シミュレーション 捕食者 回避 エージェントモデル 群れ 秩序変数 | kurims kokyuroku 1900-15 (阪上・寺山・炭谷, 魚群のダイナミクスと情報伝達); agriknowledge 三宮 水産工学 30(1) | Not opened. Search summary only. The Kyoto RIMS note on information transfer in fish schools may be relevant to propagation; not verified. |
| 12 | WebSearch: schooling does not reduce predation / limitations, agent-based | elifesciences.org/articles/76344 (both prey and predator features predict predation risk); rsbl 2023 "paradox of predation studies"; arxiv 2508.00953 (school fragmentation under predation) | Not opened (budget). eLife 76344 is the best lead for empirical individual risk in schooling prey (search summary only). The negative and qualifying evidence used in this fragment comes instead from SP-01, SP-02 and MP-03 (no-confusion, no-attack and non-confusing ablations). |

### Gaps and inaccessible sources
- **Confusion effect, original:** neither Ioannou, Tosh, Neville & Krause 2008 (Behav Ecol 19:126, an artificial neural-network predator) nor Tosh 2011 (J Theor Biol 281:24) was read. No open copy was found in one attempt.
- **Escape waves / fountain effect models:** not carded. Hemelrijk & Hildenbrandt models and the 2024 Commun. Biol. paper (s42003-024-07267-2) are leads only. Herbert-Read et al. 2015 "Initiation and spread of escape waves" was not searched.
- **Noise-matched baselines:** no source read defines a baseline that matches the error rate of a learned or decision model with random error. All published noise is independent Gaussian angular noise. This looks like a genuine gap that p2 must design itself.
- **Binary per-agent choice:** the only binary or low-dimensional choices found are Olson et al. 2013/2015 (4 actions from two binary outputs; Markov networks) and Rosenthal 2015 (binary startle response). No source has a pure two-option left/right forced choice at every step.
- **Torus + predator:** Olson 2015 used a torus, and SP-03 used periodic projection boundaries. A centroid on a torus is not addressed in any metric source.
- **Not opened (budget):** SI of Olson 2013 and Ioannou 2012; the code repositories adamilab/eos and eos-selfish-herd; Couzin lab data.
- Olson et al. 1310.6012 journal venue (reportedly Artificial Life 2016): not verified.

---

## Fragment B: perception and neighbourhood; error and contagion


| # | Query or fetch | Candidate URLs | Decision and reason (incl. access level) |
|---|---|---|---|
| 1 | WebSearch: Ballerini 2008 topological rather than metric distance arXiv | pnas.org/doi/10.1073/pnas.0711437105; arxiv 0709.1916 | Kept → PN-01. Full text of the arXiv PDF via curl+pdftotext (Results, Discussion, Fig. 4 caption, Methods). |
| 2 | WebSearch: Solon Tailleur active Ising model | arxiv 1303.4427; arxiv 1506.05749; 2306.10791 | Kept → PN-03 (1506.05749 full text, model and off-lattice sections; 1303.4427 abstract). Field-theory follow-up 2306.10791 not opened. |
| 3 | WebSearch: Rosenthal et al. 2015 hidden networks startle cascade | PNAS 10.1073/pnas.1420068112; PMC4403201 | Kept → EC-01. PNAS returned 403 to WebFetch; full main text read from the PMC HTML. |
| 4 | WebSearch: Attanasi 2014 information transfer starling | Nature Physics 10:691; arXiv 1303.7097 | Kept → EC-03. Full text of the arXiv version (main text, Table I, Fig. 3). |
| 5 | curl arXiv 1705.01213 (Crosato et al., informative and misinformative interactions in a fish school, transfer entropy) | arxiv 1705.01213 | Downloaded; title and abstract only. Not carded (budget). Lead for an information-theoretic spread measure. |
| 6 | WebSearch: Pearce et al. 2014 role of projection | arxiv 1407.2414 | Kept → PN-04. Full text of the arXiv main text; SI not read. |
| 7 | WebSearch: Strandburg-Peshkin 2013 visual sensory networks | PMC4780851 | Kept → PN-02. Full text of the PMC author manuscript. |
| 8 | WebSearch: Sosna 2019 encoding of risk false alarms | PNAS 10.1073/pnas.1905585116; PMC6789631; Dryad 10.5061/dryad.sn02v6x5x | Kept → EC-02. Full text via Europe PMC XML. Dryad not opened. |
| 9 | WebSearch: flocking blind angle field of view Vicsek limited vision | arxiv 1405.7149; 2607.27819; 2602.21338 | 1405.7149 (Nguyen, Lee, Ngoc): full text skimmed. Phase transition only for half-angle ≥ 0.5π, N = 40–500; low weight, not carded. 2026 papers (2607.27819, 2602.21338) seen in search summary only. |
| 10 | WebSearch + curl: Tian et al. 2009 optimal view angle PRE 79, 052102 | arxiv 0806.3594 | Read (main text and figure captions): optimal view angle for fastest consensus (3π/2 in the example; N = 400, L = 10, R = 0.6, v0 = 0.04, 500 realisations). Used in the PN summary as a pre-2010 source; not carded (budget). |
| 11 | WebSearch: Vicsek correlated vs independent noise | arxiv 2607.05870 (spatially heterogeneous noise); 2102.02633 | No direct correlated-vs-independent comparison found. Not opened. Gap. |
| 12 | WebSearch + curl: Toner, Guttenberg, Tu 2018 quenched disorder | arxiv 1805.10324 | Kept → EC-04 (partial: abstract, intro, conclusions). |
| 13 | WebSearch + curl: Chepizhko, Altmann, Peruani 2013 optimal noise heterogeneous media | arxiv 1305.5707 | Folded into EC-04 (abstract, intro, model, Fig. 1–2 captions). |
| 14 | WebSearch (JA): 魚群 シミュレーション 位相的相互作用 近傍 個体数 逃避 伝播 | kurims 1900-15 (Sakagami et al. 2014, 数理解析研究所講究録); jps.or.jp 22-06-4; Tohoku press release 2024 | Kurims PDF opened with pdftotext (intro only): sardine torus school of about 3000 fish, fast propagation of escape after a cutlassfish attack. Review-level, not carded. The JPS snippet says giant rotating schools form only when each fish interacts with few individuals (search summary; not verified). |
| 15 | WebSearch: topological vs metric limitations, Katz 2011, Herbert-Read 2011 | arxiv 1007.1783 (Ginelli & Chaté 2010, metric-free Voronoi); PNAS 10.1073/pnas.1107583108 (Katz et al. 2011) | Search summary only. Noted in the PN summary as leads; not verified. |
| 16 | WebFetch pnas.org Rosenthal | — | 403; used PMC instead. |

### Gaps and inaccessible sources
- No study found that tests a **discretised egocentric view** (angular sectors × distance bands) against continuous perception in a predator–prey school, or that uses a binary *turn* (rather than a binary heading, as in the active Ising model) with topological k = 3.
- No study found where agents' **errors are a deterministic function of their perceptual input** (quenched in input space). The closest are quenched-disorder flocking in physical space (EC-04) and N-version coincident failures (S-11, already covered).
- No direct simulation comparing **correlated vs independent heading noise** in Vicsek-type models was found in this budget.
- Not read: the SI of Rosenthal 2015 (contagion-model details, randomised baselines), the SI of Pearce 2014 (blind-angle variants), the SI of Ballerini 2008, the journal versions of the active Ising model papers (journal citations not verified), Crosato et al. 2017 beyond its abstract, Katz et al. 2011 and Herbert-Read et al. 2011 (fish interaction rules; may bear on how many neighbours fish attend to, reported as about 1 in some analyses — not verified).
- Pre-2010 coverage: Ballerini 2008 (PN-01) and Tian et al. 2009 (log #10). For contagion, the classic Radakov (1973) and Treherne & Foster (1981) "Trafalgar effect" studies are cited inside EC-01 but were not opened.

---

## Fragment C: learned and language agents; spatial language


Accessed 2026-10-06. Downloads in scratchpad/C/.

| # | Query or fetch | Candidate URLs | Decision and reason (incl. access level) |
|---|---|---|---|
| 1 | WebSearch "LLM flocking Boids large language model agents arXiv" | arxiv 2404.04752; 2505.06513 (LLM-Flock); 2503.03800; 2506.14496 | Leads. 2404.04752 -> LA-01 (full text). 2503.03800 -> LA-02 (full text). 2506.14496 full text read, not carded (3 boids x 5 iterations; noted in summary). 2505.06513 downloaded, not read (robot formation with consensus layer; lower priority than rule-comparison papers) |
| 2 | WebSearch "LLM2Swarm OR SwarmGPT ... swarm robotics" | 2410.11387 (LLM2Swarm); 2312.01059 (Swarm-GPT); 2502.03814 (survey); 2605.01461 (LLM-Foraging); 2605.07764 (CommandSwarm) | LLM2Swarm full text skimmed: "showcases" only, no quantitative comparison -> demonstration, not carded. Swarm-GPT is choreography (waypoints from LLM + safe planner), not local decisions -> rejected (search summary). Others not opened (budget) |
| 3 | curl+pdftotext arXiv 2404.04752, 2506.14496, 2503.03800, 2410.11387 | as above | Full text for LA-01, LA-02; full text for 2506.14496; skim 2410.11387 |
| 4 | WebSearch "Olson Hintze ... predator confusion ... Markov network retina" | arXiv 1209.3330; rsif.2013.0305; 2209.06338; 1602.08802 | 1209.3330 -> LA-03 (full text Methods/Results 3.1). Follow-ups (2209.06338 "How predator confusion shapes swarm-like behaviors"; Olson et al. 2016 "Evolution of swarming behavior is shaped by how predators attack", Artificial Life) not read |
| 5 | WebSearch "LLM agents predator prey simulation emergent collective behavior grid neighbours 2025" | 2509.21862 (Shachi); 2602.10140 (LLMs implementing ABMs, PPHPC); Sci Rep 2025 pursuit-evasion MARL; 2508.15047 (LLM crowds) | No LLM-as-prey schooling paper found. Not opened; 2508.15047 is crowd dynamics, possible later lead |
| 6 | WebSearch "deep reinforcement learning fish schooling predator avoidance ... egocentric" | 1905.04077 (SELFish); ScienceDirect MARL fish schooling 2022; PubMed 36322983 (dense schooling); DeepFoids | 1905.04077 -> LA-04 (full text). Others abstract-level in search only; not carded |
| 7 | WebSearch "Ward Gobet Kendall 2001 Evolving collective behavior..." | Artificial Life 7(2); chrest.info preprint | Pre-2010 evolved-schooling precursor; search summary only, noted in LA file |
| 8 | WebSearch "LLM agents ... correlated errors homogeneous" | 2506.07962 (Correlated Errors in LLMs); 2503.13657 (Why multi-agent LLM systems fail) | 2506.07962 noted (search summary; authors not verified), belongs near S-11 |
| 9 | WebSearch Japanese "LLM エージェント 群制御 群れ 大規模言語モデル ボイド" | alphaxiv JA pages of 2404.04752, 2508.15047 | No new Japanese-language primary source; only translations of English papers |
| 10 | WebFetch pettingzoo.farama.org simple_tag | 404 | Moved |
| 11 | WebFetch mpe2.farama.org/environments/simple_tag/ | — | Fetch summary: continuous allocentric obs, 5 world-frame moves, 1 good + 3 adversaries, 25 cycles. Noted, not carded (not a schooling model) |
| 12 | WebSearch "StepGame benchmark spatial reasoning multi-hop" | 2204.08292; 2401.03991; 2405.15064; 2310.12557 | 2204.08292 + 2401.03991 -> SL-01 (full text). 2405.15064 not read |
| 13 | WebSearch "LLM egocentric allocentric ... left right confusion benchmark" | REM; 2511.21471; 2606.03890; 2602.05789; 2509.18200; Snorkel blog | Mostly multimodal/VLM benchmarks -> out of scope for text-only decision model; not read |
| 14 | WebSearch "Yamada ... Evaluating Spatial Understanding of LLMs" | 2310.14540; 2502.17775 (FoREST); 2407.01892 (GRASP); 2502.16690 | 2310.14540 full text partly read, noted in SL file. 2502.17775 -> SL-02 (full text). GRASP, 2502.16690 not read |
| 15 | WebSearch "text-only LLM perspective taking egocentric left right ... small models" | 2603.17333 (GSU); 2602.15892; LRR-Bench; SpinBench | 2603.17333 -> SL-03 (full text). Others VLM; not read |
| 16 | WebSearch "LLM grid world representation ASCII map vs coordinate list" | 2604.14641; 2604.10690; mihai.page blog; 2505.20874 | 2604.10690 -> SL-04 (abstract + intro). 2604.14641 search summary only. Blog not used |

### Gaps and inaccessible sources
- No study found that scores an LLM or classifier's per-agent decisions against the flocking/escape rule it replaces, or measures spatial/temporal correlation of agent errors in a swarm. LA-02 compares only collective heading differences; LA-01 has no rule baseline. This is the main novelty gap p2 would fill.
- No LLM-driven swarm with a predator found (2024-2026). Predator studies with learned agents are evolutionary (LA-03) or RL (LA-04).
- No paper found on "imitation of Boids by a classifier" (behaviour cloning of Boids rules with agreement rates); searches folded into #1/#6 returned nothing specific. Not searched with dedicated queries due to budget.
- No text benchmark found for a single binary left/right decision from a structured egocentric sector state, nor for small classifiers on such inputs.
- Numbers in figures (2506.14496 Boids metrics; 2503.03800 heading differences; 1209.3330 density/dispersion; 1905.04077 survival) were not extracted; cards say so.
- Tables in 2502.17775 and 2603.17333 were garbled by pdftotext; only prose numbers quoted.
- 2604.10690 read only to the end of the introduction.
- Pre-2010: area 3 -> Ward et al. 2001 (search summary only); area 6 -> Levinson 2003 and Hill 1982 cited inside SL-02, not read.
