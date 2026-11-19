# Search log — statistically_correct (2026-10-06)

Search cutoff for recent AI work: 2026-10-06 (newest source opened: arXiv 2605.18890, May 2026). Four parallel searchers each covered two areas, opened sources at full-text or abstract level (marked per card), and wrote a fragment that is merged below unchanged. Failed or empty searches are not evidence that no work exists. Case cards are in [evidence/](.) (see [catalog.md](catalog.md)).

## Coverage summary

| Area (plan step 2) | Searcher fragment | Cards |
|---|---|---|
| Statistics and collective judgement; reliable computation and communication | [stats-and-reliable-computation](#fragment-1-statistics-and-reliable-computation) | S-01 to S-11 (11) |
| Distributed systems and control; collective behaviour and agent-based models | [control-and-collective-behaviour](#fragment-2-control-and-collective-behaviour) | C-01 to C-12 (12) |
| Game theory and social choice; stochastic optimisation and learning | [game-theory-and-stochastic-optimisation](#fragment-3-game-theory-and-stochastic-optimisation) | G-01 to G-13 (13) |
| Modern AI and multi-agent systems; games and interactive simulation | [modern-ai-and-games](#fragment-4-modern-ai-and-games) | M-01 to M-19 (19) |

55 cards, all eight areas covered, pre-LLM work in every area. S-04 and M-01 are the same source (Kim et al. 2025); the catalogue counts it once, so 54 distinct cases. Main gaps (details in fragments): correlated-voter theorems (Ladha, Boland) not opened; Boids, self-stabilisation, gossip and stochastic-control stability not retrieved; no adequately sized player study of deliberate NPC mistakes; no measured sampling-versus-argmax comparison in an interactive agent population; no Japanese-language source was used (searches were run only by the games searcher and yielded nothing usable); few independent replications opened.


---

## Fragment 1: statistics and reliable computation

## Search log: statistics, collective judgement and reliable computation (areas A and B)

Date: 2026-10-06 (search cutoff: the same day; recent AI work searched through that date). Cards: [stats-and-reliable-computation.md](evidence/stats-and-reliable-computation.md). Failed or incomplete searches are not evidence of absence.

### Queries run

Searches used the WebSearch tool, which returns summaries and links. Fetches used WebFetch (summary by a small model) or curl plus pdftotext (full text). Only full-text reads count as "read" in the cards.

| # | Query or fetch | Candidate URLs | Decision and reason |
|---|---|---|---|
| 1 | arXiv PDFs fetched directly: 2506.07962, 2203.11171, 2605.29800, 2603.06612, 2606.20158, 0711.0351, math/0003117 | arxiv.org/pdf/&lt;id&gt; | Included; full text read for the cited parts |
| 2 | NIPS 1994 PDF (Krogh and Vedelsby) | papers.nips.cc/paper_files/paper/1994/file/b8c37e33defde51cf91e1e03e51657da-Paper.pdf | Included (S-03); Sections 1-3 read |
| 3 | "Lorenz Rauhut Schweitzer Helbing 2011 How social influence can undermine the wisdom of crowd effect PNAS" | pnas.org/doi/10.1073/pnas.1008636108 (HTTP 403 on WebFetch and on curl); pnas.org/doi/10.1073/pnas.1109947108 (Farrell comment); pnas.org/doi/10.1073/pnas.1615978114 (Becker et al.); arxiv.org/pdf/2007.15508 (analytic approach); arxiv.org/pdf/1406.7578 | Lorenz included (S-02) via PMC full text (PMC3107299). Becker abstract read via Europe PMC and used as qualification. Farrell comment: title only (Europe PMC returned no abstract), not used for claims. arXiv 2007.15508 and 1406.7578 not opened: out of scope for the cap on cases |
| 4 | "Evans Pippenger maximum tolerable noise for reliable computation by formulas threshold" | users.cms.caltech.edu/~schulman/Papers/vnthresh.pdf; arxiv.org/pdf/0711.0351; cs.ubc.ca/~will/papers/thesis.pdf (Evans thesis); arxiv.org/pdf/1206.4851; dl.acm.org/doi/10.1109/TIT.2024.3486278 | Included (S-08): Evans-Schulman PDF and Unger PDF read. The Evans thesis PDF was downloaded (72 pages) but not read. Result summary of Pippenger's depth result not verified at source. Large-alphabet paper (TIT 2024) and 1206.4851 not opened |
| 5 | "Dietrich Spiekermann Independent Opinions? ... jury theorems conditional independence common causes" | personal.lse.ac.uk/spiekerk/papers/DietrichSpiekermann-IndependentOpinions.pdf; mpra.ub.uni-muenchen.de/40137/ | Included (S-01); LSE PDF read |
| 6 | WebFetch plato.stanford.edu/entries/jury-theorems/ | SEP "Jury Theorems" | Used in S-01 as **fetch-summary only**; its quotations were returned by a summarising model and not checked against the page text |
| 7 | "Ladha 1992 The Condorcet Jury Theorem, Free Speech, and Correlated Votes AJPS" | link.springer.com/content/pdf/10.1007/s11238-009-9170-2.pdf (Optimal jury design for homogeneous juries with correlated votes); personal.lse.ac.uk/kanazawa/pdfs/MSS1998.pdf; link.springer.com/article/10.1007/s11238-014-9426-3; cambridge.org APSR Austen-Smith and Banks 1996 | **Excluded as a card.** Ladha (1992, AJPS 36(3): 617-634) is only known from a search summary stating that a low average correlation between votes suffices for the theorem's main results and that diversity may lower the average correlation. The original is behind a journal paywall and was not opened; curl of the Springer jury-design PDF returned an HTML page, not a PDF. Boland (1989) and Boland-Proschan-Tong (1989) likewise not opened. Austen-Smith and Banks (1996) is cited by Kohli (S-05) as showing that correlated voters can perform worse than individuals; not verified at source |
| 8 | "LLM ensemble majority vote correlated errors limitation wisdom of the silicon crowd OR multi-agent debate fails to beat self-consistency" | science.org/doi/10.1126/sciadv.adp1528; PMC11800985 (Schoenegger et al. 2024); arxiv.org/html/2605.29800; arxiv.org/html/2603.06612; arxiv.org/pdf/2511.07784 (Can LLM agents really debate?); arxiv.org/pdf/2310.01798 (LLMs cannot self-correct reasoning yet); arxiv.org/html/2604.02460v1 (single-agent vs multi-agent under equal token budget); arxiv.org/html/2607.18269v2 (Wisdom of LLM Crowds); arxiv.org/pdf/2603.06197; alexanderakm.github.io wisdom-of-llm-crowd.pdf | S-05 and S-06 included. Schoenegger et al. 2024 (Science Advances): WebFetch summary only (12 LLMs, 31 Metaculus questions, 925 human forecasters; LLM ensemble Brier 0.20, human crowd 0.19, no significant difference): **not included as a card** because only a summary was seen and the numbers were not checked; the summary's wording about ensembles vs individual models was ambiguous. The multi-agent-debate claims in the search summary ("most MAD frameworks fail to surpass self-consistency") come from search-result text only and were not verified; the underlying papers 2511.07784, 2604.02460, 2310.01798 were **not opened**. 2607.18269v2, 2603.06197, alexanderakm PDF not opened |
| 9 | "Knight Leveson 1986 An experimental evaluation of the assumption of independence in multiversion programming 27 programs coincident failures" | csc.kth.se/.../KnightLeveson.pdf (course summary, 125 lines); arxiv.org/html/2606.20158 (Ron et al.); github.com/ASSERT-KTH/Knight-Leveson-Redux; arxiv.org/html/2607.02808 (failure independence in LLM-generated code); en.wikipedia.org/wiki/N-version_programming; arxiv.org/pdf/1610.00049 | S-11 included on the Ron et al. paper (read). Knight-Leveson original **not opened** (IEEE paywall); course summary read for the abstract only. 2607.02808 and the GitHub repository not opened; Wikipedia not used |
| 10 | "Gács Reliable cellular automata with self-organization arXiv noise independent hierarchical" | arxiv.org/html/math/0003117v2; cs-web.bu.edu/faculty/gacs/papers/long-ca-ms-24.pdf; researchgate reader's guide; arxiv.org/pdf/2105.00725 (reversible CA forget everything) | S-10 included; the arXiv PDF was read at the abstract and noise-model level only |
| 11 | "von Neumann Probabilistic logics and the synthesis of reliable organisms from unreliable components pdf multiplexing bundle" | static.ias.edu/pitp/archive/2012files/Probabilistic_Logics.pdf; archive.org/download/von_Neumann_Probabilistic_Logics_Caltech_Lecture_1952/...pdf; mit.edu/~6.454/Slides/JohnSun_vonNeumann.pdf | S-08 included; IAS PDF read in extracted text (the PDF is the 1952 Caltech lectures text as printed in Automata Studies 1956; the pagination of the 1956 print was not checked against it) |
| 12 | Shannon 1948 PDF (curl from people.math.harvard.edu) | people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf | S-09 included; text of Sections on the noisy-channel theorem read |
| 13 | Europe PMC REST search by DOI for Lorenz (PMC3107299) abstract; full-text XML endpoint | ebi.ac.uk/europepmc/webservices/rest/... | Abstract retrieved; the fullTextXML endpoint returned HTTP 500; full text taken from pmc.ncbi.nlm.nih.gov instead |

### Searches not run, or not completed

- **Kuncheva and Whitaker (2003)**, "Measures of diversity in classifier ensembles and their relationship with the ensemble accuracy", *Machine Learning* 51: 181-207: no query was run for it and no copy was opened. Gap: diversity-measure results for classifier majority voting.
- **Majority-vote bounds** (for example Dietterich 2000 on ensembles, PAC-Bayes or C-bound analyses of majority vote, Lacasse et al. 2007): not searched. Gap.
- **Effective sample size beyond Kish**: only Kohli (S-05) was read, which cites Kish (1965, *Survey Sampling*), not opened. Design-effect literature on correlated clusters was not searched. Gap.
- **Wisdom of crowds, further literature**: Galton (1907), Surowiecki (2004), Hong and Page diversity theorem, Prelec's Surprisingly Popular algorithm (cited in S-06) were not searched. Gap.
- **Social influence replication and boundary**: Becker et al. 2017 abstract only; Farrell 2011 comment unread; follow-ups on confidence-weighting or adaptive networks (the search returned pnas.org/doi/pdf/10.1073/pnas.1917687117, "Adaptive social networks promote the wisdom of crowds") were not opened.
- **Boland / Ladha / Berg / Kanazawa / Austen-Smith and Banks 1996**: not opened (see query 7). The negative result "correlated voters can perform worse than individuals" is carried only as Kohli's attribution.
- **Self-consistency negative or limiting results**: Wang et al. read; beyond S-06 no study of its failure on tasks without unique answers was searched (for example universal self-consistency, Chen et al. 2023). Gap.
- **Correlated LLM errors, other studies**: Goel et al. 2025 and Wenger and Kenett 2025 are cited in S-04's related work (not opened). Jiang et al. 2025 ("artificial hivemind") and Lefort et al. 2024 are cited in S-05 (not opened).
- **Pippenger 1985 "On networks of noisy gates"**, **Dobrushin and Ortyukov 1977**, **Feder 1989**, **Hajek and Weller 1991**, **Evans and Pippenger 1998**: not opened; claims on them come from Evans-Schulman and Unger introductions.
- **Error-correcting codes in practice**: Hamming, Reed-Solomon, LDPC, turbo codes: not searched beyond Shannon's theorem.
- **N-modular redundancy in hardware** (Lyons and Vanderkulk 1962, triple modular redundancy, voter failure): not searched. Gap; the only redundancy case with hardware framing is von Neumann.
- **Japanese-language searches**: not run (no Japanese sources were identified as relevant to these two areas).

### Access and verification problems

- pnas.org returned HTTP 403 to both WebFetch and curl (full text via PMC instead).
- Europe PMC full-text XML endpoint returned HTTP 500.
- The Springer PDF for "Optimal jury design for homogeneous juries with correlated votes" was not retrievable by curl (an HTML page was returned).
- The SEP quotations (S-01) and the Schoenegger numbers (not used in a card) came from WebFetch summaries.
- Several 2026 preprints (S-05, S-06, S-11) have not been peer reviewed, and their arXiv identifiers and dates were taken from the downloaded files and search results. None was cross-checked against a second index.

### Coverage against the plan

- Area A (statistics and collective judgement): S-01 to S-07 (seven cards; theorem, human experiment, identity, three LLM correlation or aggregation studies, one LLM aggregation gain).
- Area B (reliable computation and communication): S-08 to S-11 (four cards; two theorem cards for gates and channels, one for cellular automata, one empirical software N-version case).
- Total 11 cards: 6 pre-LLM (S-01, a 2013 paper on a 1785 theorem; S-02, S-03, S-08, S-09, S-10) and 5 LLM-era (S-04 to S-07, S-11). S-01, S-02, S-08 and S-11 contain secondary or summary-only material, marked in the cards.
- Known gaps against the plan's questions: majority-vote bounds and diversity measures (Kuncheva-Whitaker), correlated-voter theorems at source (Ladha, Boland), hardware N-modular redundancy, error-correcting code practice, semantic-error-correcting ideas (for example redundancy with verification) outside LLM aggregation.

---

## Fragment 2: control and collective behaviour

## Search log: control and collective behaviour (areas C and D)

Date: 2026-10-06. Tools: WebSearch, WebFetch, curl to a private scratchpad, pdftotext, Europe PMC REST API (abstract lookup by DOI). Failed or blocked searches are not evidence of absence. Cards: [control-and-collective-behaviour.md](evidence/control-and-collective-behaviour.md).

Note: WebSearch returns a model-written summary plus links; those summaries were not treated as evidence. A few result links carried arXiv identifiers dated 2026 (for example 2606.11259, 2610.04415, 2606.28025); they were not opened and are not used.

### Queries run

| # | Query (abridged) | Candidates | Outcome |
|---|---|---|---|
| 1 | LeBlanc Zhang Koutsoukos Sundaram resilient asymptotic consensus robust networks W-MSR arXiv | JSAC 2013 paper (Semantic Scholar link), arXiv:1802.09654, 1802.08457, 2002.00040, 1901.11000 | Primary not openable. Used 1802.09654 (full text) and 1802.08457 (intro) as secondary restatements. |
| 2 | LeBlanc ... pdf IEEE JSAC (2F+1)-robust F-local malicious | same set | No new primary link. |
| 3 | Vicsek novel type of phase transition arXiv cond-mat/0611743 | arXiv:cond-mat/0611743, comment cond-mat/0703532, Wikipedia, Kuramoto relation 1005.2140 | Included 0611743 (full), 0703532 (first page). 1005.2140 not opened. Wikipedia excluded (tertiary). |
| 4 | Chate Ginelli Gregoire Raynaud collective motion without cohesion first-order | PRE 2008 (Semantic Scholar, ResearchGate), arXiv:2103.07444, 1301.7701, 2211.03879 | PRE 2008 not opened (no direct PDF found in results). Not used as a source; mentioned only as a lead. |
| 5 | Gregoire Chate onset of collective and cohesive motion vectorial noise | arXiv:cond-mat/0401208, PRL link, Physica D 2003 PDF, arXiv:2404.18675, 1212.2060 | Included cond-mat/0401208. 1212.2060 (Meschede, Hallatschek, local disalignment promotes order) downloaded and read in abstract and intro; excluded from cards because the manipulation is a collision-angle rule, not noise; recorded as a lead for a dense-regime "disalignment helps" result. |
| 6 | Couzin Uninformed individuals promote democratic consensus Science 2011 | Science abstract, Bristol, PubMed, ScienceDaily, arXiv:2606.11259 | Abstract via Bristol page and Europe PMC; Science page 403; PubMed returned a cookie notice. C-06 abstract only. |
| 7 | Berdahl Torney Ioannou Faria Couzin emergent sensing Science 2013 | Science, Bristol, PubMed, PLoS CB 1003762, arXiv:1904.02895, 2610.04415 | C-07 abstract only (Bristol). PLoS CB 1003762 (Kao et al. collective learning) abstract retrieved via Europe PMC, not carded. |
| 8 | Couzin Krause Franks Levin 2005 Effective leadership Nature | Nature, Princeton, Bristol | Nature page redirect to login; Bristol page had metadata only; abstract retrieved from Europe PMC. C-05 abstract only. |
| 9 | Berdahl 2013 ... "many wrongs" light gradient group size accuracy | same | Nothing new. Berdahl's quorum/"many eyes" claim (from the assignment) not located in a readable source. Gap. |
| 10 | Handegard Boswell Ioannou ... group hunting and collective information transfer Current Biology 2012 | ResearchGate, SpringerLink citing works, MPI page, PLoS CB criticality paper | Not opened (no accessible full text). Gap for sardine/herring and "starling" evasion field studies. |
| 11 | Ioannou Guttal Couzin predatory fish virtual prey Science 2012 | Science, Bristol, Semantic Scholar, ADS, arXiv:2112.02974, PNAS 2406293121 | Science not opened; only a search-summary of the abstract exists; cited as a lead in C-12. arXiv:2112.02974 included (C-11). |
| 12 | Schelling 1971 mild preference strong segregation limitations Clark Fossett | arXiv:1402.1229, 2602.09795, 0907.1777, JASSS 15/1/6, PNAS 2313752121 (PMC10873625) | Included PMC10873625 (text read), JASSS 15/1/6 (fetch summary only). Clark and Fossett 2008 PNAS and Schelling 1971 not opened. |
| 13 | Gauvin Vannimenus Nadal phase diagram Schelling arXiv | arXiv:0903.4694 | Included (full text sections). A first attempt used a wrong arXiv ID (0811.3105, an unrelated astrophysics paper); it was discarded. |
| 14 | Seeley Visscher ... stop signals cross inhibition Science 2012 | Bristol, Science, arXiv:2407.20927, 2310.15592 | Abstract via Europe PMC only; not carded separately, cited inside C-08. |
| 15 | List Elsholtz Seeley independence and interdependence honeybee | LSE preprint PDF, Graz PDF, arXiv:0909.1582, PhilPapers | LSE preprint read (C-08). arXiv:0909.1582 (pattern formation / analytical approaches follow-up) not opened; lead. |
| 16 | Hein Rosenthal Hagstrom Berdahl Couzin evolution of distributed sensing eLife 2015 | eLife, arXiv:1602.06737, PubMed | eLife page failed to load; abstract via Europe PMC (OA, PMC4755780). Not carded; lead for phase-transition-like sensing and noise. |
| 17 | Kao Couzin decision accuracy small group sizes Proc B 2014 | Proc B, Princeton news, arXiv:1509.08157 | Full text from PMC4043084 (partially read). Included (C-09). Europe PMC fullTextXML endpoint returned HTTP 500; the PMC HTML page worked. |
| 18 | Direct fetches | Lamport byz.pdf (OK), Kar and Moura arXiv:0711.3915 (OK), Dijkstra EWD391 (utexas PDF) | Lamport and Kar included. EWD391 is a scanned image PDF; pdftotext returned only the copyright notice, so self-stabilisation is not carded. |
| 19 | Europe PMC lookups by DOI | 10.1038/nature03236, 10.1126/science.1225883, .1210280, .1210361, 10.1098/rspb.2013.3305, 10.7554/eLife.10955, 10.1371/journal.pcbi.1003762 | Abstracts retrieved; no body text for the Science and Nature papers. |
| 20 | Klamser and Romanczuk PLoS CB 1008832 | PLoS printable PDF (curl OK) | Abstract and introduction read (C-12). Fetch summary also gave N = 400 and 76 attacks; not re-verified. |

### Queries not run (time or scope)

Gossip with noise (Boyd et al. 2006, randomized gossip), stochastic control stability under noise (no specific source chosen), random versus adversarial fault comparison beyond C-01 to C-03, Boids (Reynolds 1987), Sumpter and Pratt quorum paper, Marshall et al. on optimal decision-making in brains and insect colonies, Condorcet jury theorem with correlated errors (likely covered by area A or B searchers), Ballerini et al. 2008 starling topological interactions, Herbert-Read 2017 predation and interaction rules, and negative-result searches specific to Boids ("limitations", "replication"). Only a limited set of negative terms was used (first-order correction, limitations of Schelling, criticality failure, correlated information).

### Inclusion and exclusion reasons

- Included: primary or author-hosted full text read, or an abstract from a trusted record, and a stated collective objective with an error, noise or variability element.
- Excluded: Wikipedia and news pages (tertiary); papers with 2026 arXiv identifiers (not examined); Meschede and Hallatschek (not about noise as such); Kar and Moura is included although it concerns sensor networks, because it states the bias-variance trade-off for noisy averaging.

### Inaccessible material

- Science (Couzin 2011, Berdahl 2013, Seeley 2012, Ioannou 2012): HTTP 403 or abstract only.
- Nature (Couzin 2005): login redirect.
- IEEE JSAC (LeBlanc et al. 2013): no PDF found.
- Phys. Rev. E (Chate et al. 2008), Schelling 1971 (J. Math. Sociol.), Clark and Fossett 2008, Current Biology (Handegard 2012), Dijkstra 1974.
- PubMed pages: cookie notice only.
- eLife (Hein 2015): page did not load.

### Gaps

1. No source found that tests noise or random choice as a benefit with a real LLM agent or a human decision maker; all variability-helps results are models or simulations (C-09, C-11).
2. No quantitative evidence on predator evasion from field data (sardine, herring, starling) was retrieved in readable form.
3. Self-stabilisation, gossip and stochastic control stability: not covered.
4. The Berdahl 2013 "many eyes" quorum material and Sumpter's work: not retrieved.
5. Replication status is unknown for most cards; only the Vicsek continuity claim has a documented correction (C-04).
6. Numeric effect sizes for C-05, C-06, C-07 are unavailable because only abstracts were read.

---

## Fragment 3: game theory and stochastic optimisation

## Search log: game theory, social choice, stochastic optimisation (areas E and F)

Date: 2026-10-06. Tools: WebSearch (US index), WebFetch, curl plus pdftotext into the session scratchpad (E/). Failed or empty searches are not evidence of absence. Companion file: [game-theory-and-stochastic-optimisation.md](evidence/game-theory-and-stochastic-optimisation.md).

### Queries run (11 batches, 17 queries) and outcomes

| # | Query (abbreviated) | Candidates | Decision |
|---|---|---|---|
| 1 | Caragiannis Procaccia Shah "When Do Noisy Votes Reveal the Truth" pdf | dl.acm.org/doi/10.1145/2892565; procaccia.info/.../samples.pdf; cs.toronto.edu nisarg pdf | Included G-05; read procaccia.info PDF |
| 2 | Hajek 1988 Cooling schedules for optimal annealing | pubsonline.informs.org (403 on fetch); web.mit.edu/6.435/www/Hajek88.pdf (via later search) | Included G-08 |
| 3 | McKelvey Palfrey 1995 QRE pdf | sciencedirect abstract; ideas.repec; focal QRE arXiv 2304.00438 | Original paper not opened (paywalled); used abstract only; included G-01 via primer and critique |
| 4 | Salganik Dodds Watts 2006 | princeton.edu PDF; science.org; SOM PDF; arXiv 0912.5240; arXiv 1408.1542 | Included G-07; SOM and follow-ups not opened |
| 5 | Bikhchandani Hirshleifer Welch 1992 pdf | snap.stanford.edu PDF; ETH and Montclair copies | Included G-03 (Stanford copy) |
| 6 | Anderson Holt 1997 cascades in the laboratory | econweb.ucsd.edu PDF; NBER w12767; Goeree-type follow-ups; Kariv papers | Included G-04 (ucsd PDF). Search summary quoted 20 sessions and 78 percent Bayesian; the PDF I read had six-session designs; I used only PDF numbers |
| 7 | Gammaitoni Hanggi Jung Marchesoni stochastic resonance RMP | augsburg opus PDF (curl failed); physik.uni-augsburg.de/.../195.pdf (worked) | Included G-10; read partially |
| 8 | Blume 1993 / Young 1993 log-linear, stochastic stability | ideas.repec Blume abstract; arXiv 1804.02693 (downloaded, not read) | Blume and Young not opened; no separate card; mentioned in G-02 as search-only |
| 9 | Russo et al. tutorial on Thompson sampling | arXiv 1707.02038 | Included G-09 |
| 10 | Hajek-Sasaki "to cool or not" | experts.illinois; Springer chapter | Not opened; noted as gap |
| 11 | Ladha 1992 correlated votes | Kaniovski draft PDF; researchgate; Springer pdf "optimal jury design" | Included G-06 (Kaniovski); Ladha not opened |
| 12 | Srivastava Hinton dropout | jmlr.org PDF | Included G-13 |
| 13 | Kandori Mailath Rob 1993 | dklevine.com/archive/refs4500.pdf | Included G-02 |
| 14 | Haile Hortacsu Kosenok QRE empirical content | aeaweb; cowles d1432.pdf | Included in G-01 (abstract read only, text not extracted beyond abstract) |
| 15 | Ellison 1993 local interaction | econometricsociety page; ideas.repec | Not opened; gap |
| 16 | Goeree Holt Palfrey QRE traveler's dilemma | caltech primer PDF; Cowles | Included primer in G-01 |
| 17 | evolutionary algorithm mutation rate runtime | arXiv 1811.12824 (Doerr); 2602.23573; 1704.02191 | Snippet only, no card; gap |

Direct fetches via curl: arXiv 1511.06807 (Neelakantan, G-11), 1503.02101 (Ge, G-12), 1207.1368 (Conitzer-Sandholm, G-05), cps.pdf, sdw.pdf, bhw.pdf, ah.pdf, h88.pdf, kmr.pdf, ts.pdf, kan.pdf, drop.pdf, hhk.pdf, qre.pdf, gam.pdf. Neelakantan and Ge were identified from background knowledge, then confirmed on arXiv; they were not surfaced by a search query.

### Inaccessible or unverified

- INFORMS page for Hajek 1988: HTTP 403 via WebFetch. The MIT copy was used; its OCR is noisy, so only abstract and Section 1 were relied on.
- McKelvey-Palfrey 1995 (ScienceDirect): not fetched (paywall); only search-summary description used for citation details.
- Augsburg opus link for Gammaitoni: curl produced no file; the other Augsburg URL worked.
- Young 1993, Blume 1993, Banerjee 1992, Kirkpatrick 1983, Ladha 1992, Hajek-Sasaki 1989, Ellison 1993, Bishop 1995: not opened; not used for numbers.
- Anderson-Holt PDF may differ from the AER print version (see above).
- Fetch-summary-only reads: none from WebFetch; all content-bearing reads were pdftotext of the PDFs (full or partial as stated in each card).
- Partial reads: Gammaitoni (abstract, Section I, greps), Caragiannis et al. (first pages only), Kaniovski (abstract and corollary text), Ge et al. (statements, not proofs), HHK (abstract), KMR (abstract and introduction).

### Gaps and weaknesses

1. No local Jev data used; Jev relevance statements are inferences.
2. Trembling-hand perfection, Banerjee herding, Arrow's theorem, epsilon-greedy/Boltzmann exploration primary texts, evolutionary-algorithm mutation rate, Bishop (1995) noise regularisation: not carded.
3. Stochastic-resonance criticisms and failure cases not systematically extracted.
4. No source here directly tests error dependence among LLM agents; negative-term searches (failure, correlated errors, bias, limitations, replication) were run only partially: correlated votes (query 11), QRE fit (query 14), cascade lab results (query 6). A dedicated replication search for MusicLab and for gradient-noise results was not run.
5. Numerical effect sizes in G-06, G-08, G-09, G-10 were not extracted.

---

## Fragment 4: modern AI and games

## Search log: modern AI / multi-agent (G) and games / interactive simulation (H)

Date of searches: 2026-10-06. Cutoff: AI literature searched up to 2026-10-06 (newest item opened: arXiv 2605.18890, 17 May 2026; items dated June-September 2026 appeared in result lists and were not opened unless noted). Tools: WebSearch (US-only results) and WebFetch; arXiv PDFs fetched with curl into the scratchpad and converted with pdftotext. Cards: [modern-ai-and-games.md](evidence/modern-ai-and-games.md). A failed or empty search is not evidence of absence.

Reading status labels: FULL = PDF or page text opened and searched; PARTIAL = opened, only parts read; SNIPPET = seen only in search-result text; SUMMARY = WebFetch summary only; NONE = could not open.

### 1. Queries run

| # | Query (abridged) | Main candidates returned |
|---|---|---|
| 1 | Correlated errors in large language models Kim Garg Peng Garg | arXiv 2506.07962 (used, M-01); 2609.11428 "Wavering Oracles" (not opened); 2603.04408 (not opened) |
| 2 | Replacing judges with juries PoLL | arXiv 2404.18796 (used, M-02); 2512.01786 jury-on-demand, 2505.21972, 2501.10970 (SNIPPET, not opened) |
| 3 | Should we be going MAD multi-agent debate benchmark | arXiv 2311.17371 (PARTIAL, supporting in M-03); 2510.20963 "When and why does MAD fail" (downloaded, not read); 2502.08788 "Stop overvaluing MAD" (SNIPPET) |
| 4 | Out of One, Many Argyle algorithmic fidelity | arXiv 2209.06899 (used, M-05); 2602.15785 validating LLM simulations (SNIPPET) |
| 5 | LLMs cannot replace human participants misportray flatten | arXiv 2402.01908 (used, M-06); 2504.11673 (SNIPPET) |
| 6 | Generative agents social simulation homogeneity limitations replication failure | 2506.19806, 2507.19364, 2507.06310, 2605.18890 (used, M-11), 2605.30258, 2607.28347, 2511.15573 |
| 7 | BotPrize Turing test game bots Hingston | Hingston 2009 (NONE for full text), Wikipedia page, UT Austin news (SNIPPET), arXiv 2105.09637 NTT (PARTIAL) |
| 8 | Player study perceived fairness hit chance randomness XCOM | forum threads and blogs (SNIPPET, not used); "Interplay Between Fairness and Randomness in a Spatial Computer Game" ResearchGate (SNIPPET, not opened) |
| 9 | Maia chess human-like engine | arXiv 2006.01855 (used, M-14); other Maia follow-ups (SNIPPET) |
| 10 | Dynamic difficulty adjustment player study enjoyment Hunicke L4D | Hunicke 2005 (SNIPPET); Hunicke and Chapman (used, M-16); MCTS-DDA enjoyment paper (ResearchGate, SNIPPET); MDPI DDA methods (403) |
| 11 | Deliberately imperfect game AI mistakes player experience user study | YSU thesis (used, M-17); 2606.27689 "When AI deceives" (SNIPPET); ACM CHI 2024 deception paper (SNIPPET) |
| 12 | ゲームAI 人間らしさ 意図的なミス プレイヤー 評価 実験 | Fujii thesis (core.ac.uk, NONE: server returned HTML), alphaxiv 2209.00459 (SNIPPET), kochi-tech page (SNIPPET), Morikatron Hanabi article (SNIPPET) |
| 13 | LLM agents voting collective decision diversity homogeneity ... same model independence | 2402.01766 (used, M-08); 2508.17536 (used, M-03); 2604.03809 (see exclusions); 2608.02827, 2603.20324, 2604.18005, 2602.09341 (SNIPPET / not read) |
| 14 | Wisdom of the silicon crowd | Science Advances / PMC11800985 (used, M-04, PARTIAL); 2607.18269, 2512.22625, 2506.00723, 2507.04562 (SNIPPET) |
| 15 | OASIS one million agents herd effect | arXiv 2411.11581 (used, M-10); 2509.18052 PIMMUR (downloaded, not read); 2503.10248 (SNIPPET) |
| 16 | AgentSociety large-scale simulation | arXiv 2502.08691 (SNIPPET only, not opened); GATSim, others |
| 17 | RimWorld storyteller AI director player study | wiki, Steam threads, Medium and Substack essays (practitioner, SNIPPET, not used) |
| 18 | Hingston "A Turing Test for Computer Game Bots" TCIAIG | ro.ecu.edu.au abstract page (SUMMARY); full text not accessible |
| 19 | Karpov Schrum Miikkulainen BotPrize UT^2 | nn.cs.utexas.edu PDF (used, M-13) |
| 20 | Navigation Turing Test Devlin Georgescu | arXiv 2105.09637 and Microsoft PDF (PARTIAL); related CHI papers listed |
| 21 | "Navigates Like Me" CHI 2023 | arXiv 2303.02160 (used, M-15); ACM page blocked by Cloudflare, used arXiv instead |
| 22 | Fujii 藤井叙人 人間らしい ゲームAI 揺らぎ 遅れ 疲れ | IPSJ page, researchmap, CEDEC 2014 session, JAIST repository (SNIPPET; thesis NONE) |
| 23 | Jake Solomon XCOM hidden aim assist | Game Developer interview page (SUMMARY, M-18); Game Rant, 80.lv, PCGamesN, wikis (SNIPPET, not used) |
| 24 | LLMエージェント 社会シミュレーション 住民 多様性 偏り | alphaxiv Japanese views of 2506.19806, 2605.18890, 2507.19364, 2607.02464; Zenn articles (SNIPPET, not used) |
| 25 | LLM agent sampling versus greedy argmax multi-agent diversity | RL and reasoning papers (2604.00344, 2607.11250, 2405.15054 etc., SNIPPET); none used |
| 26 | Booth "The AI Systems of Left 4 Dead" | Valve PDF (used, M-19) |

Direct fetches of known works (not search queries): arXiv PDFs 2506.07962, 2404.18796, 2311.17371, 2209.06899, 2402.01908, 2303.17548, 2304.03442, 2411.00114, 2510.20963, 2402.01766, 2508.17536, 2604.03809, 2608.02827, 2603.20324, 2105.09637, 2303.02160, 2006.01855, 2605.18890, 2411.11581, 2506.19806, 2509.18052, 2507.19364; Karpov PDF; Hunicke and Chapman PDF; YSU thesis PDF; Valve L4D PDF; PMC11800985 HTML.

### 2. Inclusion and exclusion

| Item | Decision | Reason |
|---|---|---|
| Kim et al. 2025 (M-01) | include | Large measurement of error correlation across 350+ models; data and code stated available |
| Verga et al. 2024 (M-02) | include | Ensemble of different families versus single judge; vendor conflict noted |
| Choi et al. 2025 and Smit et al. 2024 (M-03) | include | Separates voting from debate, with theorem and tables; Smit read at abstract level only |
| Schoenegger et al. 2024 (M-04) | include | Probabilistic ensemble against human crowd, with a proper scoring rule |
| Argyle et al. (M-05) | include | Foundational positive claim of silicon samples; arXiv v1 only, journal version not opened |
| Wang et al. 2025 (M-06) | include | Human-participant evidence on flattening and a temperature test |
| Santurkar et al. 2023 (M-07) | include | Distribution-level misalignment; sharpness of aligned models |
| Yang et al. 2024 (M-08) | include | Preference aggregation by model agents against human votes; temperature trade-off |
| Park et al. 2023 (M-09) | include | Measured interactive population, with failure modes |
| Yang et al. OASIS 2024 (M-10) | include | Large population, scale and herd effects; authors evaluate own system |
| Ye et al. 2026 (M-11) | include | Controlled demonstration of macro sensitivity; preprint |
| Altera Project Sid 2024 (M-12) | include with caution | Vendor technical report, "preliminary"; useful for architecture-level correction and role heterogeneity |
| Karpov et al. (BotPrize 2010) (M-13) | include | Open source with results table; Hingston 2009 not accessible |
| McIlroy-Young et al. 2020 (M-14) | include | Structured versus weakened error with large data |
| Milani et al. 2023 (M-15) | include | Human judgements on why agents look non-human |
| Hunicke and Chapman 2004 (M-16) | include | Pre-2023 design of deliberate adjustment; no evaluation, flagged |
| Khan 2026 thesis (M-17) | include as weak | Only controlled player study on suboptimal opponents found; n = 10, unreviewed |
| Solomon interview (M-18) | include as anecdote | SUMMARY read only |
| Booth 2009 (M-19) | include as anecdote | Primary design talk, no player data |
| Patel 2026 "Representational collapse" 2604.03809 | exclude | Single author, 100 questions, three agents of one model; claims modest (cosine 0.888 among role-prompted agents); read abstract and introduction only; run-to-run variance reported as 1 to 3 points, comparable to the 3-point accuracy gain |
| Emergence of Biased Consensus 2608.02827; When Agents Disagree 2603.20324 | not used | Downloaded, not read |
| 2510.20963 "When and why does MAD fail" | not used | Downloaded, not read; a possible additional source for M-03 |
| 2506.19806, 2507.19364, 2509.18052 (social-simulation critiques) | not used | Downloaded, not read in depth; the lines on homogeneity come only from search snippets and are not cited |
| AgentSociety 2502.08691 | not used | SNIPPET only; the validity claims I saw are the authors' own summary |
| Hunicke 2005 "The case for DDA"; MCTS-DDA enjoyment study; MDPI DDA methods | not used | Not opened (paywall, ResearchGate listing, HTTP 403); the claim in search snippets that DDA techniques show no clear superiority in enjoyment is not verified |
| Hingston 2009 | not used for numbers | Full text not accessible; abstract only |
| 2012 BotPrize 52% versus 40% result | mentioned as unverified | Seen only in news snippets (UT Austin news, Singularity Hub, Wikipedia) |
| RimWorld storyteller pages, Dwarf Fortress | exclude | Practitioner or fan pages; no evaluation |
| XCOM forum and blog posts | exclude | Anecdote beyond the one interview; not opened |
| Fujii 2016 thesis, CEDEC 2014 session | not used | Thesis PDF not accessible (HTML returned); content seen only in snippets |
| Maia follow-up papers (individual models, Matilda) | not used | SNIPPET only |

### 3. Inaccessible material

- Hingston 2009 IEEE TCIAIG paper: publisher full text not opened; ECU repository page gave only the abstract.
- Fujii Nobuto doctoral thesis (core.ac.uk PDF returned an HTML page, not a PDF); IPSJ page and CEDEC session seen as snippets only.
- ACM Digital Library pages (Cloudflare challenge): used arXiv versions instead.
- MDPI "Exploring Dynamic Difficulty Adjustment Methods for Video Games": HTTP 403.
- Argyle et al., Political Analysis 2023 version: not opened; arXiv v1 read instead.
- Game Developer interview page: WebFetch summary only, not a verbatim read.
- Park et al. and others: a source's code or data repositories were not opened or tested.

### 4. Gaps

- Player studies. Only one study of deliberate suboptimal NPCs (M-17, weak). No opened source compares mistakes versus no mistakes on enjoyment with adequate sample size. DDA player studies were found only in snippets.
- Randomness and fairness in games with human participants: not opened (one candidate paper listed on ResearchGate).
- Left 4 Dead director: only the developer's talk; no independent evaluation.
- Simulation storytellers (Dwarf Fortress, RimWorld): practitioner material only.
- Costikyan "Uncertainty in Games" and Lantz essays: not searched for, not opened.
- Sampling versus argmax for agent actions: one query, no direct measured comparison in an interactive population; M-06 and M-08 only show temperature effects on generated outputs.
- Interactive populations of LLM agents with measured error dependence over time (as opposed to isolated question errors) are few: M-09, M-10, M-11, M-12 are the only measured interactive cases here, and none measures error independence directly.
- LLM voting and collective decision beyond M-08 (for example deliberation among agents with differing preferences): not covered.
- Replication: no card has an independent replication opened in this search.
- Japanese: three queries; no Japanese-language player study located; Fujii's work is a lead only.
- Several results in the AI area are from 2026 preprints (M-11, M-17 thesis); their review status was not checked.
