# Search log

Literature search for `study/benchmark/`, run 2026-10-02 (JST) in step2 of [benchmark/p1](../../devdocs/episodes/benchmark/p1/plan.md). Sources are indexed in [sources.md](sources.md) and annotated in [evidence/](evidence/).

## Questions and clusters
The research questions come from [questions-and-audit.md](questions-and-audit.md). The search was split into six clusters, each run by one research subagent with the same written instructions:

| Cluster | Research questions | Topics |
|---|---|---|
| A | RQ2 | single-label, binary detection, multilabel, retrieval/ranking, ordinal/regression metrics |
| B | RQ2, RQ5 | proper scores, calibration measurement, LLM confidence, selective prediction and abstention, OOD detection, cost-sensitive decisions |
| C | RQ2, RQ3 | inter-annotator agreement, label variation, LLM-as-judge, generation metrics and acceptable answers, structured outputs, annotation practice |
| D | RQ1, RQ3 | construct/content/ecological validity, shortcuts, contrast sets and negatives, distribution shift, splits and holdout reuse, contamination, documentation and licensing |
| E | RQ4, RQ6 | binomial intervals, paired tests, power, repeated runs, multiplicity, equivalence/non-inferiority, clustered data, multi-task aggregation |
| F | RQ5, RQ6, case studies | prompt/format/option sensitivity, prompt injection, model vs system evaluation and harness effects, benchmark suites, performance and cost measurement |

## Method
- **Preference order:**
  1. original papers, textbooks or tutorials;
  2. official dataset, benchmark or framework documentation and code;
  3. vendor or blog material, only as primary documentation of the vendor's own artefact or event.
- **A small set of foundational sources per subtopic,** plus recent work (2023–2026) where practice has changed.
- **Every source was fetched and its verification level recorded** (see [sources.md](sources.md)).
  - Formulas and numbers were read from raw text: `curl` + `pdftotext`, arXiv HTML, PMC HTML, raw README or code files.
  - Model-written WebFetch summaries were used only to locate pages.
  - **One WebFetch summary misreported a table** (the dottxt blog). The numbers were corrected from the raw HTML.
- **Metadata** (title, authors, dates, versions) was checked through the arXiv export API, Crossref, OpenAlex, ACL Anthology, PMC, the Hugging Face Hub API and the GitHub API.
- **Dataset licences** were read from the original LICENSE file or dataset card. Hosting-site metadata was not trusted alone; for example, the GitHub API reports CLINC150 as NOASSERTION while its LICENSE file is CC BY 3.0.
- **The lead session reviewed every cluster file.** It then spot-checked the derived worked examples in [metrics.md](metrics.md) by recomputing them.
- **No source was run or reproduced locally.** Numbers from papers are the authors' results.

## Unavailable or partly available sources (summary)
Full per-cluster lists are below. The most important gaps:
- **Classic originals behind paywalls.** Their formulas are attributed through full-text secondary sources named in the evidence entries:
  - Brier 1950, Murphy 1973 (abstract), Chow 1970 (abstract), Platt 1999;
  - Cohen 1960/1968, Fleiss 1971, Feinstein & Cicchetti 1990 (abstract), Krippendorff 2004 (book);
  - Wilson 1927, McNemar 1947, Holm 1979, Agresti & Coull 1998, Brown–Cai–DasGupta 2001 (abstract);
  - Sokolova & Lapalme 2009, Gaudette & Japkowicz 2009;
  - Messick 1995 (abstract), Dwork et al. 2015 Science (abstract).
- **Not fetched:**
  - the Pustejovsky & Stubbs annotation book (MATTER is cited through a handbook chapter read in full);
  - Dietterich 1998 full text (PDF text garbled; abstract only);
  - the FDA non-inferiority margin definitions;
  - FEVER's data licence.
- **Abstract level only:** many cluster-D papers (WILDS, Dynabench, HANS, annotation artifacts, shortcut learning, Lewis et al., Søgaard et al. 2021, Golchin & Surdeanu, Dodge et al., Ott et al.). Only their abstract claims are used.
- **Not searched or not covered:**
  - independent replication of the constrained-decoding quality dispute;
  - 2025–2026 LLM-judge work beyond revised versions of two papers;
  - a formal missing-data treatment for multi-task aggregation;
  - small-n paired-difference confidence intervals (Newcombe, Tango);
  - canary strings beyond BIG-bench;
  - LLMPerf/AIPerf;
  - Open LLM Leaderboard v2 and MTEB v2;
  - independent quantization studies.
- **A methodological gap rather than a search gap:** no source found here separates prompt-induced score spread from finite-sample binomial noise.

An unsuccessful search is not evidence that no such work exists.

## Contradictions and open disagreements found
| Topic | Position 1 | Position 2 | Where discussed |
|---|---|---|---|
| ROC-AUC vs PR-AUC under imbalance | PR is more informative (Saito & Rehmsmeier 2015) | The general claim is overgeneralised; choose by deployment cost (McDermott et al. 2024) | [metrics.md §2](metrics.md#2-binary-scoring-and-detection) |
| MCC as the binary summary | MCC is most informative (Chicco & Jurman 2020) | MCC is non-monotonic and less interpretable (Opitz 2024) | metrics.md §1 |
| Equidistance in ordinal metrics | Required ordinal invariance (Amigó et al. 2020) | Acceptable in practice (Sakai 2021) | metrics.md §5 |
| Format restriction and quality | Strict formats hurt reasoning (Tam et al. 2024) | Parity or gains with matched prompts (Kurt 2024, vendor; Geng et al. 2025) | metrics.md §8 |
| GPT-4 calibration after post-training | Post-training hurts calibration (OpenAI 2023, vendor) | RLHF miscalibration is largely fixed by one temperature (Kadavath et al. 2022, other models) | evidence B |
| ECE estimation | Binning underestimates (Kumar et al. 2019) | Plug-in overestimates, most for calibrated models (Roelofs et al. 2022). Both hold; they are different biases | metrics.md §6 |
| Bootstrap vs approximate randomization | Bootstrap targets the population (Berg-Kirkpatrick et al. 2012) | Randomization has more accurate type-I error (Riezler & Maxwell 2005); bootstrap is anti-conservative at small n (Søgaard et al. 2014) | [statistics-and-comparison.md](statistics-and-comparison.md) |
| CLT intervals for evals | CLT and clustered SE (Miller 2024) | Not below a few hundred items (Bowyer et al. 2025) | statistics-and-comparison.md |
| Mean-rank post-hoc tests | Friedman + Nemenyi (Demšar 2006) | Outcome depends on the pool of algorithms (Benavoli et al. 2016) | statistics-and-comparison.md |
| Adversarial data collection | Dynamic adversarial collection (Kiela et al. 2021) | Does not fix validity (Bowman & Dahl 2021) | [data-and-validity.md](data-and-validity.md) |
| Random splits | Random splits over a single standard split (Gorman & Bedrick 2019) | Random splits are still optimistic; use independent test sets (Søgaard et al. 2021) | data-and-validity.md |
| Holdout reuse | Adaptive reuse can overfit (Dwork et al. 2015) | Little overfitting observed on Kaggle (Roelofs et al. 2019) | data-and-validity.md |
| GPT-3 contamination n-grams | 13-gram (§4) | Variable N in [8, 13] (App. C) of the same paper | data-and-validity.md |
| Prompt-sensitivity magnitude | Large spreads from format and paraphrase (Sclar et al. 2024; Mizrahi et al. 2024) | Few-shot and minor prompt changes have little *rank* effect (Alzahrani et al. 2024) | [robustness-and-execution.md](robustness-and-execution.md) |
| LLM-judge self-preference | Inconclusive (Zheng et al. 2023) | Linked to self-recognition (Panickssery et al. 2024) | metrics.md §9 |

## Per-cluster query logs
Queries, tools and outcomes as recorded by each research subagent. "Included" means that an evidence entry exists; exclusions give a reason.

### Cluster A: Classification, detection, multilabel, ranking and ordinal metrics

#### Queries
| Query / URL | Tool | Outcome |
|---|---|---|
| export.arxiv.org API id_list=1911.03347, 2104.08663, 2401.06091, 2404.16958, 1402.1892 | Bash curl | metadata/abstract verified; comments give venues |
| arXiv title search "Macro F1 and Macro F1", "Precision-Recall-Gain", "ordinal classification and ordinal quantification" | Bash curl | first found (1911.03347); others not on arXiv (fetched from NeurIPS/ACL) |
| arxiv.org/pdf/1911.03347v3 | curl+pdftotext | included (opitz2019macrof1) |
| arxiv.org/pdf/2404.16958 | curl+pdftotext | included (opitz2024closerlook) |
| arxiv.org/pdf/2401.06091 | curl+pdftotext | included (mcdermott2024auroc) |
| arxiv.org/pdf/2104.08663 | curl+pdftotext | included (thakur2021beir) |
| aclanthology.org/2021.acl-long.214.pdf | curl+pdftotext | included (sakai2021ordinal) |
| aclanthology.org/2020.acl-main.363.pdf | curl+pdftotext | included (amigo2020cem) |
| journals.plos.org … pone.0118432 printable | curl+pdftotext | included (saito2015prc) |
| papers.nips.cc … 33e8075e…-Paper.pdf | curl+pdftotext | included (flach2015prg) |
| www.biostat.wisc.edu/~page/rocpr.pdf | curl | empty, then used ftp.cs.wisc.edu davis.icml06.pdf: included (davis2006prroc) |
| people.inf.elte.hu/kiss/11dwhdm/roc.pdf | curl+pdftotext | included (fawcett2006roc) |
| palm.seu.edu.cn/zhangml/files/TKDE'13.pdf | curl+pdftotext | included (zhang2014multilabel) |
| bmcgenomics / springer PDF for Chicco & Jurman | curl | HTML/blocked; Europe PMC fullTextXML PMC6941312: included (chicco2020mcc) |
| WebFetch bmcgenomics article | WebFetch | redirect, not used |
| microsoft.com ecir2008.pdf | curl | HTML; WebSearch found marc.najork.org/papers/ecir2008.pdf: included (mcsherry2008ties) |
| nlp.stanford.edu/IR-book/pdf/08eval.pdf | curl+pdftotext | included (manning2008irbook-ch8) |
| faculty.cc.gatech.edu/~zha/CS8803WST/dcg.pdf | curl+pdftotext | included (jarvelin2002cg) |
| ong-home.my/papers/brodersen10post-balacc.pdf | curl+pdftotext | included (brodersen2010balacc) |
| cs.cornell.edu lec09.pdf (guessed bpref URL) | curl | wrong document, excluded |
| WebSearch "Buckley Voorhees 2004 Retrieval evaluation with incomplete information bpref pdf" | WebSearch | found NIST PDF; tsapps.nist.gov pub_id=150469: included (buckley2004bpref) |
| WebSearch "McSherry Najork … tied scores pdf" | WebSearch | found author PDF (included) |
| WebSearch "Sokolova Lapalme 2009 … pdf" (2 queries) | WebSearch | no open full text; found Opitz 2024 TACL |
| rali.iro.umontreal.ca SokolovaLapalme-JIPM09.pdf (http/https) | curl | HTML not PDF, unavailable |
| ir.webis.de anthology page | WebFetch | 404 |
| sciencedirect S0306457309000259 | WebFetch | 403 |
| api.crossref.org works 10.1016/j.ipm.2009.03.002 and 10.1007/978-3-642-01818-3_25 | curl | metadata only, no abstract |
| api.semanticscholar.org DOI:10.1016/j.ipm.2009.03.002 | curl | CLOSED, abstract elided |
| api.semanticscholar.org search Gaudette | curl | 429 rate limit |
| scikit-learn.org model_evaluation.html (v1.9.1) | curl, HTML stripped | included (sklearn-modeleval) |
| scikit-learn precision_recall_fscore_support, ndcg_score, cohen_kappa_score API pages | curl | included (same source) |
| WebSearch "Gaudette Japkowicz 2009 Evaluation methods for ordinal classification" | WebSearch | Springer only; snippet summary not relied on |
| link.springer.com chapter 978-3-642-01818-3_25 | curl / WebFetch | auth redirect, unavailable |
| site.uottawa.ca/~nat/Papers/papers-old.html | curl | listing only, no PDF |
| WebSearch "Stevens 1946 On the theory of scales of measurement pdf" | WebSearch | found course mirror PDF |
| faculty.ucmerced.edu … Stevens 1946.pdf | curl + Read (page images) | included (stevens1946scales) |
| WebSearch "Cohen 1968 Weighted kappa …" | WebSearch | only secondary pages; primary paywalled, unverified |
| trec.nist.gov/pubs/trec8/papers/qa_report.pdf | curl + Read (page images) | included (voorhees1999trec8qa) |
| WebSearch "Chen 2024 Genome Biology … AUPRC values" | WebSearch | found; Europe PMC REST abstract: included (chen2024auprctools) |
| local sklearn check of majority-classifier example | Bash python | sklearn not installed; example computed by hand (marked derived) |

#### Gaps and unavailable sources
- **Sokolova & Lapalme 2009**: full text not accessible (403/closed), so it cannot be cited for specific claims. Opitz 2024 and sklearn cover the same ground.
- **Gaudette & Japkowicz 2009**: not accessible. "Accuracy at n" is attested only via Amigó 2020. Claims about MSE vs MAE recommendations are unverified.
- **Cohen 1968**: not accessed. The weighted κ formula comes from Sakai 2021 (verified). No primary source was read that prints the quadratic weights (i−j)² explicitly. The sklearn docs only name 'quadratic'.
- **Tsoumakas & Katakis** multilabel overview was not fetched. Zhang & Zhou 2014 is used instead.
- **Hand 2009** ("a coherent alternative to AUC", H-measure) and **Hand & Till 2001** were not read. Hand & Till appears only as cited by sklearn.
- **Critiques of bpref** (Sakai 2007 "Alternatives to bpref"; Büttcher et al. 2007) were seen in search results only.
- **Voorhees' TREC pooling-bias studies** (e.g. Zobel 1998; Voorhees & Harman) were not fetched. BEIR §6 and Manning §8.5 cover pooling.
- **Chai & Draxler 2014** (RMSE vs MAE) was cited by Sakai but not read.
- Chen et al. 2024 (AUPRC tools) and Lipton et al. 2014 are abstract-level only.

### Cluster B: Probabilities, calibration, abstention, OOD and cost-sensitive decisions

#### Queries
| Query / URL | Tool | Outcome |
|---|---|---|
| export.arxiv.org API id_list (24 ids: 1706.04599, 1904.01685, 1909.10155, 1910.12656, 1902.06977, 2012.08668, 2211.16886, 2309.12236, 2207.05221, 2305.14975, 2303.08774, 2012.00955, 1705.08500, 2006.09462, 1806.03822, 2407.18418, 2506.09038, 2402.00367, 2107.07511, 2509.04664, 1610.02136, 1909.02027, 2110.11334, 0806.0813) | curl | First http call returned empty. Retried via https: all 24 metadata confirmed |
| arxiv.org/pdf/<id> for the 24 ids + pdftotext | curl | all downloaded. Included |
| sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf | curl+pdftotext | full text (20 pp.). Included |
| journals.ametsoc.org downloadpdf Murphy 1973, Brier 1950 | curl | empty (blocked) |
| journals.ametsoc.org view pages Murphy 1973, Brier 1950 | WebFetch | HTTP 403 |
| api.crossref.org works for Murphy, Brier, Gneiting, Drummond, Vickers, Chow DOIs | curl | metadata confirmed |
| WebSearch "Brier 1950 Verification of forecasts … pdf" | WebSearch | only S2/ResearchGate links. Brier left unverified |
| WebSearch "Murphy 1973 A new vector partition … pdf" | WebSearch | found Bröcker 2012 Reading PDF. Included as brocker2012 |
| api.semanticscholar.org paper lookups | curl | HTTP 429 rate-limited. Not used |
| api.openalex.org works/doi: Chow 1970, Murphy 1973, Brier 1950, Drummond, Vickers, Naeini | curl | abstracts for Chow, Murphy, Vickers, Naeini. Brier and Drummond had none |
| ieeexplore.ieee.org/document/1054406 (Chow) | WebFetch | empty page. Used OpenAlex abstract |
| personal.reading.ac.uk/~pt904209/…/decomp_interp_clim_dyn_2011.pdf | curl+pdftotext | full text. Included |
| link.springer.com PDF / article for Drummond & Holte | curl | HTML (paywall) |
| WebSearch "Drummond Holte Cost curves … pdf" | WebSearch | found author preprint |
| site.uottawa.ca/~cdrummon/pubs/ML_2006.pdf | curl+pdftotext | full text. Included |
| ijcai.org/Proceedings/01/IJCAI-2001-e.pdf | curl | 100-page proceedings bundle. Not used |
| cseweb.ucsd.edu/~elkan/rescale.pdf | curl, WebFetch, Read (rendered pages) | pdftotext garbled the formulas. WebFetch failed. Read the rendered pages 1–2. Included |
| pmc.ncbi.nlm.nih.gov/articles/PMC2577036 (Vickers) | curl | full text. Included |
| pmc.ncbi.nlm.nih.gov/articles/PMC4410090 (Naeini) | curl | full text of the ECE/MCE paragraph. Included |
| arxiv.org/pdf/1805.08206 (Geifman 2019 AURC) | curl+pdftotext | full text. Included |
| jmlr.org/papers/volume11/el-yaniv10a/el-yaniv10a.pdf | curl+pdftotext | read abstract and intro. Included |
| arxiv.org/pdf/1706.02690 (ODIN, to source FPR@95TPR) | curl+pdftotext | full text. Included (Hendrycks & Gimpel do not define FPR95) |
| WebSearch "Platt 1999 Probabilistic outputs … pdf" | WebSearch | only ResearchGate/bibsonomy. Platt left unverified, cited via Guo |

#### Gaps and unavailable sources
- **Brier 1950**: unverified, because AMS returned 403 and no abstract was available. Formulas are sourced from gneiting2007proper and brocker2009.
- **Murphy 1973**: abstract only. The explicit REL/RES/UNC formula is derived from brocker2009 and brocker2012.
- **Chow 1970**: abstract only. The reject-rule formula in the notes is a standard derivation, not a quote.
- **Platt 1999**: unverified. The method is cited via guo2017.
- **El-Yaniv & Wiener 2010**: only the abstract and introduction were read.
- **Not fetched**: Stephenson et al. 2008 ("two extra components" of the binned Brier decomposition), Ferro & Fricker 2012 (debiased reliability), the OpenOOD benchmark paper, Ovadia et al. 2019 (calibration under shift), Lin et al. 2022 (verbalized calibration), and Xiong et al. 2024 (LLM confidence elicitation). These are candidates if more depth on shift or verbalized confidence is needed.
- **Version notes**: journal versions of Bröcker 2009, Wen 2024 (TACL) and Yang 2024 (IJCV) were not checked against the arXiv versions read.
- **Still unpublished as of access**: kalai2025 (arXiv only) and kirichenko2025 (arXiv v1).

### Cluster C: Annotation agreement, human/model judging, generated and structured outputs

#### Queries
| Query / URL | Tool | Outcome |
|---|---|---|
| arxiv.org/pdf/{2306.05685, 2305.17926, 2305.01937, 2404.13076, 2406.12624, 2406.18403, 2403.04132, 2303.16634, 2305.06984, 1606.05250, 1806.03822, 2408.02442, 2501.10868, 2307.09702, 2211.02570, 2010.03532, 2103.14749, 1803.09010} | curl + pdftotext | all included (full text) |
| aclanthology.org/J08-4004.pdf, Q19-1043.pdf | curl + pdftotext | included |
| aclanthology.org/2022.naacl-main.183.pdf | curl | excluded: wrong paper (Plank 2022 is EMNLP; the arXiv version was used instead) |
| repository.upenn.edu bitstream guess | curl | failed (HTML) |
| "Computing Krippendorff's Alpha-Reliability" pdf | WebSearch | found asc.upenn.edu PDF; included |
| Uma et al. 2021 JAIR | WebSearch; jair.org article/download/12752/26751 | Bocconi mirror returned HTML; JAIR PDF included |
| api.crossref.org for Cohen 1960, Fleiss 1971, Feinstein 1990, Aroyo 2015, Artstein 2008, Gebru CACM | curl | metadata verified |
| PubMed esearch/efetch PMID 2348207 | curl | Feinstein & Cicchetti abstract included |
| ojs.aaai.org aimagazine article 2564 PDF | curl | Aroyo & Welty full text included |
| platform.openai.com/docs/guides/structured-outputs | curl + HTML strip | included |
| huggingface/evaluate metrics/squad{,_v2}/compute_score.py | curl | included (copies of official scripts) |
| white0dew/squad evaluate-v2.0.py | curl | 404, excluded |
| EleutherAI lm-evaluation-harness docs/task_guide.md, filters/extraction.py, tasks/gsm8k/gsm8k.yaml; GitHub API commit | curl | included (commit d6de816) |
| blog.dottxt.co → blog.dottxt.ai/say-what-you-mean.html | WebFetch + curl | included as vendor claim. The WebFetch summary misstated the GSM8K numbers; corrected from raw HTML |
| arxiv.org/pdf/2211.09110 (HELM) | curl + pdftotext | included (findings 22–23 only) |
| Pustejovsky Stubbs MATTER | WebSearch | catalog listings only |
| oreilly.com library page; semanticscholar.org page | WebFetch | 403, unavailable |
| api.semanticscholar.org; googleapis books | curl | 429 / no items, unavailable |
| arxiv.org/pdf/1602.05753 (Finlayson & Erjavec) | curl + pdftotext | included as secondary source for MATTER |

#### Gaps and unavailable sources
- Cohen 1960 and Fleiss 1971 originals (paywalled) and Feinstein & Cicchetti 1990 (abstract only). Formulas are attributed via artstein2008agreement. Landis & Koch 1977 and Krippendorff's 2004 book were not fetched; the thresholds are quoted via Artstein & Poesio.
- The Pustejovsky & Stubbs book was not accessible. MATTER content comes from the Finlayson & Erjavec chapter.
- HELM's per-scenario output parsing and invalid-output policy was not checked, and neither was the HELM docs site. Only the paper's prompt-sensitivity findings are cited.
- No independent (non-vendor, non-author) replication settling Tam 2024 vs Kurt/Geng 2025 was found. A search for 2025–2026 follow-ups was not run.
- Panickssery 2024: only the abstract and Fig. 1 were read, so no effect sizes are quoted.
- 2025–2026 LLM-judge work (e.g. reward-model/judge benchmarks, judge calibration studies) was not surveyed beyond the v6/v3 revisions of Thakur and Bavaresco.
- No source found that formally specifies "retry/repair" accounting in an evaluation harness. The decomposition in Topic notes §5 is synthesis.

### Cluster D: Validity, datasets, negatives, splits and contamination

#### Queries
| Query / URL | Tool | Outcome |
|---|---|---|
| export.arxiv.org API id_list=36 ids (1912.05511 … 2310.16787) | curl | included (all 36 returned and abstracts read) |
| huggingface.co/api/datasets/{clinc/clinc_oos, PolyAI/banking77, tals/vitaminc, rajpurkar/squad_v2, legacy-datasets/banking77} | curl | included (licenses, split sizes) |
| huggingface.co/datasets/tals/vitaminc/raw/main/README.md | curl | included (license) |
| raw.githubusercontent.com/clinc/oos-eval/master/README.md and LICENSE; api.github.com/repos/clinc/oos-eval | curl | included (split sizes, CC BY 3.0, NOASSERTION) |
| raw.githubusercontent.com/PolyAI-LDN/task-specific-datasets README; GitHub API | curl | included (10,003/3,080/77, CC-BY-4.0) |
| raw.githubusercontent.com/TalSchuster/VitaminC README; GitHub API | curl | included (real/synthetic tests; MIT code) |
| arxiv.org/pdf/{2005.14165, 2005.04118, 2004.02709, 2310.17623, 2308.08493, 2207.07048, 2104.02145, 2310.18018, 2402.02823, 2203.08242, 1806.03822, 1909.02027, 2012.07421, 2005.00636, 2008.02637, 2405.00332} + pdftotext | curl | full-text used for the ones marked; others downloaded but abstract-level only |
| "Bean Measuring what matters construct validity" | WebSearch | included (arXiv:2511.04703, existence verified) |
| arxiv.org/pdf/2511.04703 | curl+pdftotext | included (§5) |
| "Liao Taori Raji Schmidt Are We Learning Yet" | WebSearch | included |
| datasets-benchmarks-proceedings.neurips.cc …757b505…-Paper-round2.pdf | curl+pdftotext | included (full-text) |
| "Roelofs A Meta-Analysis of Overfitting" | WebSearch | included |
| proceedings.neurips.cc …ee39e503…-Paper.pdf | curl+pdftotext | included (abstract) |
| aclanthology.org/P19-1267.pdf | curl+pdftotext | included (full-text abstract/§1.1) |
| doi.org/10.1037/0003-066X.50.9.741 → psycnet | WebFetch | redirect chain; psycnet not fetched |
| "Messick 1995 Validity of psychological assessment abstract" | WebSearch | ERIC page found |
| eric.ed.gov/?id=EJ517194 | WebFetch | included (abstract) |
| science.org/doi/10.1126/science.aaa9375 | WebFetch | 403; used Crossref summary + arXiv companion |
| "Dwork ... reusable holdout Science 2015" | WebSearch | metadata confirmed |
| doi.org/10.1016/j.patter.2023.100804; cell.com fulltext | WebFetch | redirect / 403; Crossref metadata used, arXiv v1 read |
| mitpress.mit.edu Dataset Shift in ML | WebFetch | 403; Crossref book abstract used |
| api.crossref.org/works/{Kapoor, Messick, Dwork, Quiñonero-Candela, Longpre NMI} | curl | included (metadata/abstracts) |
| arxiv.org/pdf/2502.00561 and 1912.05511 | curl+pdftotext | included (full-text sections) |
| livebench.ai | WebFetch | no content (JS); excluded |
| raw.githubusercontent.com/LiveBench/LiveBench/main/README.md | curl | included |
| livecodebench.github.io | WebFetch | included (summary) |
| raw.githubusercontent.com/LiveCodeBench/LiveCodeBench/main/README.md | curl | included (release versions) |

#### Gaps and unavailable sources
- Messick 1995: full text was not accessible (APA paywall). Only the ERIC abstract was verified, so the six aspects were not verified against primary text.
- Dwork et al. 2015 (Science): full text returned 403. Only the editor's summary and the companion arXiv abstract were read. Thresholdout's exact parameters and bounds are not recorded.
- Quiñonero-Candela et al.: book description only. Formal taxonomies of shift (prior/label shift, concept shift) are not sourced here.
- WILDS, Dynabench, Ott et al., Raji et al., de Vries et al., HANS, Gururangan, Geirhos, Lewis, Søgaard, Golchin, Xu, Dodge, Gebru, Kaushik: abstract-level only. Specific numbers beyond the abstracts should not be attributed.
- Banking77 paper: abstract only. Dataset facts come from the official README and HF.
- LiveBench website content could not be rendered. GitHub README used instead; its "current release 2025-04-25" may be stale as of 2026-10.
- Not covered: canary strings (e.g. BIG-bench canary), Min-K% Prob (Shi et al. 2023) as a primary source, and grouped-split tooling (e.g. scikit-learn GroupKFold docs). Add these if the study needs them.

### Cluster E: Intervals, paired tests, power, multiplicity and aggregation

#### Queries
| Query / URL | Tool | Outcome |
|---|---|---|
| export.arxiv.org API id_list=2411.00640,2503.01747,2010.06595,2103.03098,1707.09861,1909.03004,2406.10229,2108.13264,2107.07002,2202.03799,2210.05769,2405.01719,2009.13888,1606.04316 | curl | all 14 metadata confirmed (titles, authors, dates) |
| arxiv.org/pdf/<each id above> | curl + pdftotext | full text obtained for all 14; included |
| aclanthology.org/{P18-1128,D12-1091,W14-1601,W04-3250,W05-0908,2021.naacl-main.51,2021.acl-long.179}.pdf | curl + pdftotext | full text; included |
| jmlr.org demsar06a.pdf, benavoli16a.pdf | curl + pdftotext | full text; included |
| BMC Fagerland 2013 PDF (biomedcentral) | curl | returned HTML; switched to PMC |
| pmc.ncbi.nlm.nih.gov/articles/PMC3716987 | curl | full text; included (fagerland2013mcnemar) |
| projecteuclid.org BCD 2001 .full | curl | Incapsula bot wall |
| www-stat.wharton.upenn.edu ~tcai and ~lbrown BCD PDFs | curl / WebFetch | HTML / 301→404; unavailable |
| WebSearch "Brown Cai DasGupta 2001 Interval Estimation for a Binomial Proportion pdf" | WebSearch | found links; only the Euclid landing page was usable |
| projecteuclid.org BCD landing | WebFetch | abstract; included at abstract level |
| api.semanticscholar.org DOI:10.1214/ss/1009213286, 10.1080/00031305.1998.10480550 | curl | both CLOSED access |
| users.stat.ufl.edu/~aa/articles/agresti_coull_{1998,2001}.pdf | curl | HTML block; unavailable |
| statsmodels proportion_confint docs | WebFetch | official docs notes on CP conservatism; included in brown2001 entry |
| sci2s.ugr.es dietterich1998.pdf | curl + pdftotext | PDF fonts unextractable (garbled); excluded as text source |
| oregonstate nc-stats.pdf | curl | HTML; unavailable |
| direct.mit.edu Dietterich | WebFetch | 403 |
| Europe PMC / Crossref API Dietterich DOI | curl | abstract obtained; included (abstract) |
| Semantic Scholar API for McNemar1947, Holm1979, BH1995, Lakens2017, Altman1995, Cameron2015 | curl | metadata and OA links; abstracts elided for most |
| academic.oup.com BH 1995 | WebFetch | abstract; included |
| jstor.org/stable/4615733 (Holm) | WebFetch | page failed to load; bibliographic only |
| Crossref API Holm query | curl | returned Hochberg/Rom-type records, not Holm; Holm bibliographic details from S2/JSTOR id |
| Crossref API Wilson 1927, McNemar 1947, Field & Welsh 2007, Agresti–Coull 1998 | curl | bibliographic confirmed |
| academic.oup.com Field & Welsh 2007 | WebFetch | abstract; included |
| pmc.ncbi.nlm.nih.gov/articles/PMC5502906 (Lakens) | curl | full text; included |
| bmj.com Altman & Bland PDF and article page | curl / WebFetch | HTML / 403 |
| Europe PMC search → PMC2550545 | curl | PMC landing (scanned PDF only); included at title level |
| cameron.econ.ucdavis.edu Cameron_Miller_JHR_2015_February.pdf | curl + pdftotext | full text; included |
| Europe PMC search "Understanding equivalence and noninferiority testing" → PMC3019319 | curl | full text; included |
| fda.gov NI guidance landing page | WebFetch | summary only; included (abstract) |
| fda.gov/media/78504/download | curl | non-PDF response; unavailable |
| export.arxiv.org search "Signal and Noise" LM evaluation | curl | 2508.13144 abstract; included (abstract) |

#### Gaps and unavailable sources
- **Brown, Cai & DasGupta 2001**: abstract only. The exact n thresholds, coverage plots, and the Agresti–Coull and Jeffreys formulas were not read from primary text. For the formula-level claim, use bowyer2025clt App. A for Wilson/CP, or obtain the paper via library access.
- **Wilson 1927, McNemar 1947, Holm 1979, Agresti & Coull 1998**: bibliographic verification only. Their procedures are described through secondary full-text sources (bowyer2025clt, fagerland2013mcnemar, demsar2006).
- **Dietterich 1998**: abstract only. The 5×2cv t statistic and the simulation details were not read.
- **Efron & Tibshirani 1993 and Noreen 1989** (books): not accessed.
- **Altman & Bland 1995**: the scanned full text could not be read, so only the title claim is verified.
- **FDA 2016 NI guidance and ICH E9/E10**: landing page only. The M1/M2 margin definitions are not verified.
- **Benjamini–Hochberg under dependence** (Benjamini & Yekutieli 2001) and Hochberg 1988 were not fetched.
- **Missing-cell handling** in multi-task aggregation has no formal statistical treatment among the verified sources beyond Vote'n'Rank's pairwise-deletion approach.
- **Not covered**: exact unconditional tests for paired proportions (e.g. Suissa–Shuster), Newcombe's paired-difference CI (Newcombe 1998), and Tango's score interval for paired differences. These would give a CI, not just a p-value, for the McNemar setting and would be worth adding if the study needs paired-difference CIs at small n.

### Cluster F: Robustness, harnesses, benchmark suites, performance and cost

#### Queries
| Query / URL | Tool | Outcome |
|---|---|---|
| export.arxiv.org API id_list (30 ids: 2310.11324, 2401.00595, 2309.03882, 2308.11483, 2307.03172, 2302.00093, 2402.01781, 2302.12173, 2312.14197, 2403.06833, 2404.13208, 2405.14782, 2211.09110, 1804.07461, 1905.00537, 2206.04615, 2009.03300, 2406.04127, 2104.08663, 2210.07316, 2012.07421, 2005.04118, 1803.05355, 1909.02027, 1911.02549, 2309.06180, 2002.05651, 1906.02243, 2211.05102, 2411.02355) | curl (http failed empty; https OK) | all 30 metadata/abstracts/comments retrieved — included |
| arxiv.org/html/{16 ids} → text | curl + local HTML-to-text | full text for subtopics 1–3, PagedAttention, quantization — included |
| arxiv.org/pdf/{14 ids} → pdftotext | curl + pdftotext | full text for suites, MLPerf, energy, Pope — included |
| https://huggingface.co/blog/open-llm-leaderboard-mmlu | curl | included (fourrier2023hfmmlu) |
| https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ | curl | included; author/date verified |
| https://inspect.aisi.org.uk/ , /scoring.html, /metrics.html (scorer-metrics.html, scoring-metrics.html → 404) | curl | index + metrics included |
| raw.githubusercontent.com/openai/simple-evals/main/README.md | curl | included |
| raw.githubusercontent.com/triton-inference-server/perf_analyzer/main/genai-perf/README.md | curl | included |
| raw.githubusercontent.com/vllm-project/vllm/main/vllm/benchmarks/serve.py + gh api commits | curl/gh | included |
| raw.githubusercontent.com/mlcommons/inference_policies/master/inference_rules.adoc + gh api commits | curl/gh | included |
| research.google/pubs/the-tail-at-scale/ ; barroso.org TheTailAtScale.pdf | curl | included (venue from Google page; text from PDF) |
| leboudec.github.io/perfeval/ + book/perf.pdf | curl + pdftotext | included (order-statistic CI) |
| api.semanticscholar.org paper/batch (venues) | curl | unavailable (HTTP 429) |
| dblp.org search API (venues) | curl | unavailable (empty/non-JSON responses; stopped) |
| aclanthology.org/{2024.tacl-1.52, 2024.tacl-1.9, 2024.acl-long.744, 2020.acl-main.442, N18-1074, D19-1131, 2023.eacl-main.148, 2024.findings-naacl.130, 2025.naacl-long.262} | curl | titles verified — venues confirmed |
| doi.org/10.1145/3605764.3623985 | curl -I | redirects to ACM DL (Greshake AISec'23); ACM page 403 |
| proceedings.mlr.press/v139/koh21a.html | curl | WILDS ICML 2021 confirmed |
| gh api repos/{clinc/oos-eval, beir-cellar/beir, embeddings-benchmark/mteb, google/BIG-bench, hendrycks/test, p-lambda/wilds, marcotcr/checklist, EleutherAI/lm-evaluation-harness, stanford-crfm/helm, UKGovernmentBEIS/inspect_ai, mlcommons/inference, sheffieldnlp/fever-scorer} | gh | code licenses, last push, latest release — included in table |
| clinc/oos-eval LICENSE; HF api datasets/clinc/clinc_oos, cais/mmlu | curl | CLINC CC BY 3.0; MMLU MIT tag — included |
| fever.ai/dataset/fever.html | curl | page fetched but license text not extracted — FEVER data license left unverified |
| Considered, not fetched: Dettmers LLM.int8 (2208.07339) | — | excluded (kurtic2025quant more recent/comprehensive for accuracy effects) |
| Local computation (python, binomial CDF) | Bash | order-statistic sample sizes; MLPerf Eq. 2 arithmetic check — reported as derived |

#### Gaps and unavailable sources
- **FEVER data license**: not confirmed from official page text (commonly cited as CC BY-SA 3.0 with Wikipedia-derived content; unverified).
- **Pope et al. venue** (MLSys 2023) and **Biderman et al. venue** not verified (arXiv metadata gives none; Semantic Scholar/DBLP lookups failed).
- **Greshake et al. AISec '23**: confirmed only via DOI redirect; ACM landing page blocked (403).
- **Wallace et al.** evaluation numbers beyond abstract/intro not checked (treat numerically as abstract-level).
- **LLMPerf (Anyscale)** and **AIPerf (NVIDIA successor to GenAI-Perf)** docs not fetched; GenAI-Perf + vLLM code were used instead for TTFT/ITL/TPOT definitions.
- **Open LLM Leaderboard v2 changes (2024)** and **MTEB v2 / MMTEB (2025)** not covered; paper-era descriptions may not match the live artefacts.
- No source found here that statistically separates *prompt-induced* spread from *finite-sample binomial noise* (a methodological gap worth noting in the study; sclar2024formatspread App. B.2 adds stdev but not a noise model).
- Quantization: only one (vendor-affiliated) comprehensive study included; independent replications not searched.
- Standard textbook for quantile CIs other than Le Boudec (e.g., David & Nagaraja "Order Statistics", Hahn & Meeker "Statistical Intervals") not accessed.
