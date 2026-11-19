# Search log — hype_and_reality/p1

All searches were run on 2026-10-02 (JST). Three research subagents ran them in parallel, plus a fourth for model scale and candidates (step5; see its section). The lead session spot-checked key sources: the decision-injection-bench README table and the laya-intent-router README OOS figures were re-read via `gh api` and matched the evidence notes.

## Tools and coverage
- `gh api` (READMEs, issues, contents) and `gh search`. Repo-scoped issue search worked; global `gh search issues` returned nothing usable.
- WebSearch and WebFetch for papers, blogs and HF pages. **Caveat:** WebFetch returns a model-written summary, not raw text. Numbers taken only from such summaries are marked in the evidence files. Where the PDF text was extracted (CLINC150, HINT3, InjecGuard, NeMo Guardrails, 41-model study), the numbers come from that text.
- **Not reachable:** Reddit and X posts could not be fetched. Hacker News comments appeared only as search snippets and were not used.
- An unsuccessful search is not evidence that no such experience exists.

## Inclusion rule
A source was included when it gave something concrete and inspectable: a model, a task, cases or numbers, and a link. It also had to bear on one of the local failure classes L1–L9 or questions Q1–Q8 ([local-failures.md](local-failures.md)). Positive and negative results were both sought. Prior `study/` notes were used as leads only.

## Ecosystem: Jev, clones, GitHub issues, independent benches (`eco-` evidence)
| Query / action | Tool | Notable hits | Outcome |
|---|---|---|---|
| read study/ecosystem/evaluations.md, reception.md, local-failures.md | Read | leads | used as leads only |
| gh api issues for jeff, von, OpenDecision, poorjev, kev, SemIf, Verdict(x2), laya, laya-jev-lab, jev-ood-calibration, typed-decision-bench, jevbench, jev-benchmarks | gh | jeff #4; von #3,#21,#22; laya many; OpenDecision #1; SemIf #40,#52 | included as eco-jeff-order-sensitivity-issue4, eco-von-issues-out-of-domain, eco-laya-*; OpenDecision #1 only auth/timeouts, excluded; SemIf #40/#52 are image-only/one-line complaints (screenshots not readable), excluded; poorjev, kev, typed-decision-bench had no relevant issues (kev issues are maintainer progress logs) |
| gh search issues (injection, abstain, none of the above, order sensitivity) | gh search | empty output | no usable result (repo-scoped API search used instead) |
| gh api search/issues repo:NandhaKishorM/laya (adversarial, abstain, out-of-domain, wrong answer, negation, order) | gh | #377,#781,#450,#124,#35,#99,#394,#635 | included as eco-laya-negation-377, eco-laya-issues-confidence-and-routing |
| arXiv 2609.30216 | WebFetch | exists: "Jev in the Wild", Ling, Xue, Ye, submitted 2026-09-24, 2,170 GitHub projects | verified; abstract has no adversarial/abstention content; no evidence file |
| HF convaiinnovations/laya discussions/3 (x2) | WebFetch | 40.3% verified, 305 decisions, multilingual 321.9M | included as eco-laya-adversarial-hf-discussion3 |
| mandu5/jevcompat jeff report | WebFetch | order shift 0.417 | included in eco-jeff-order-sensitivity-issue4 |
| scienthoon/jev-ood-calibration, jev-baselines-eval, priorbench/jev, jujumilk3/jev-calibration-audit | WebFetch | none-option, OOS numbers | included as eco-jev-none-option-and-oos-studies, eco-jev-calibration-audits |
| Shogo-nfrealmusic/jev-eval README | WebFetch | numbers not in README (in RESULTS.md); only limitations | not run further: RESULTS.md not fetched; excluded |
| yibie/laya-jev-lab README | WebFetch | boundary tier Jev 40% / Laya 20%, n=10, no none option stated | excluded: boundary labels may have no correct answer, low value; mention only |
| Sophos blog | WebSearch | snippet only | used second-hand in eco-jev-calibration-audits; not fetched |
| awesome-jev-robustness | WebFetch | list of injection/abstention studies | lead; cwhy, jagged, system1-system2, jev-engineering opened; JevOut, jev-bias-audit, jev-evaluation, jev-abstentionbench not opened |
| cwhy/decision-injection-bench (fetch + readme) | WebFetch, gh | cross-model injection table | included as eco-injection-bench-cwhy |
| zkousama/jagged, Iskandeur/system1-system2, eugeniughelbur/jev-engineering | WebFetch | injection numbers | included as eco-jev-injection-other-studies |
| primeline.cc pre-registered test | WebFetch | 4 confirmed / 8 refuted failure modes | not written up (no OOD/abstention content); mention only |
| JevBench README | WebFetch | hard tier 220 items; jeff 63.5, Laya 64.3 | included as eco-jevbench-hard-tier (top-5 table not re-verified) |
| sotaaz jeff-vs-jev, decision-confidence | WebFetch | Jeff Qwen3.5-based; 26-option limit | included as eco-sotaaz-jeff-vs-jev (name collision flagged) |
| entagl, arize blogs | WebFetch | gated fallback measured | included as eco-positive-deployments-entagl-arize |
| WebSearch: Jev production results/fallback | WebSearch | entagl, arize, towardsai, dev.to | entagl/arize included; others not opened |
| WebSearch: HN Jev none of the above / OOD | WebSearch | search-snippet summaries of HN comments (jacobgold wrong valid value; early-access user on OOD behaviour) | not fetched (HN thread item=49717558 not opened); excluded as second-hand |
| typed-decision-bench results page, kyr0 | gh | repo has 0 stars, no issues | not run further: results unextractable earlier; excluded |
| Reddit/X posts | - | - | not run: tools cannot fetch |

## Literature: papers on small-model and zero-shot classification failures (`lit-` evidence)

| Query / action | Tool | Notable hits | Outcome |
|---|---|---|---|
| Read study/landscape/*.md ID grep | Bash | IDs for Zheng 2309.03882, Holtzman 2104.08315, Zhao 2102.09690, Shi 2302.00093 | Verified by fetch: 2309.03882, 2104.08315, 2102.09690, 2302.00093 (all match titles). Not verified: 2210.03057 (is MGSM, not relevant), Kadavath 2207.05221, GLiNER Guard 2605.05277, 2609.02292 |
| arXiv abs 2309.03882 + html | WebFetch | Table 3 RStd | lit-selection-bias-zheng |
| arXiv abs 2308.11483 | WebFetch | 13%-75% gap | lit-selection-bias-zheng |
| arXiv 2406.03009 | WebFetch | Wei et al. | lit-selection-bias-zheng |
| arXiv 1909.02027 | WebFetch | CLINC150 | lit-oos-intent-detection |
| arXiv 2402.17256 abs/html | WebFetch | LLM OOD intent | lit-oos-intent-detection |
| arXiv 2410.01627 | WebFetch | Arora et al. | lit-oos-intent-detection |
| LLM OOS intent search | WebSearch | 2608.20371 etc. | 2608.20371 lead only, not read |
| ACL 2021 short.99 | WebFetch | Ma et al. | lit-nli-zeroshot-lexical-overlap |
| Holtzman, Zhao abs | WebFetch | | lit-nli-zeroshot-lexical-overlap |
| NOTA search; arXiv 2503.01550, 2409.00113 | WebSearch/Fetch | 30-50% drop | lit-nota-abstention-mcq |
| prompt injection judge searches; 2504.18333, 2505.13348, 2511.21752 | WebSearch/Fetch | ASR table | lit-prompt-injection-classifiers-judges (2511.21752 size trend unverified) |
| inverse scaling searches; 2306.09479, 2605.29491 | WebSearch/Fetch | DistractionIF | lit-prompt-injection..., lit-scaling-and-distractors |
| arXiv 2302.00093 | WebFetch | GSM-IC | lit-scaling-and-distractors |
| arXiv 2508.07662 GLiClass | WebFetch | abstract only, no OOS/multilingual info | excluded: no relevant failure data |
| arXiv 2603.11991 BTZSC | WebFetch | size helps, English | lit-scaling-and-distractors |
| Japanese zero-shot NLI searches; 2402.03223 | WebSearch/Fetch | no Japanese | lit-multilingual-zeroshot-nli |
| arXiv 2210.03057 | WebFetch | MGSM only | excluded: not relevant |
| Pezeshkpour full PDF, Zheng PDF | WebFetch | binary undecodable | used HTML instead |
| GitHub issues searches | gh | | not run (out of scope) |

## Positive and mixed usage: routers, moderation, intent detection (`use-` evidence)

| Query / action | Tool | Notable hits | Outcome |
|---|---|---|---|
| Read common.md, local-failures.md, study/game README + facade-nlu | Read/Bash | local taxonomy; Facade lead | context; Facade not re-verified, not included |
| arxiv 2209.11055 (SetFit) abs + html | WebFetch | RAFT table summary | included as use-setfit-fewshot (numbers relayed by fetch tool; flagged) |
| arxiv 1909.02027 + PDF text | WebFetch/pdftotext | Table 2/3 | included as use-clinc150-oos |
| github aurelio-labs/semantic-router | WebFetch | returns None on no match; threshold optimisation notebook; no accuracy numbers | excluded: no measured metrics |
| HF Llama-Prompt-Guard-2-86M | WebFetch | AUC .998, recall 97.5% @1% FPR (vendor card) | excluded as standalone; contrasted via InjecGuard (card figures not independently checked) |
| arxiv 2009.13833 (HINT3) | WebFetch/pdf | Tables 2,3,5 | included as use-hint3-real-chatbot-oos |
| arxiv 2106.08616 html | WebFetch | K+1 classifier numbers | excluded: method paper, out of time |
| arxiv 2509.21138 AutoIntent | WebFetch | PDF unparsable via tool | not read; excluded |
| WebSearch prompt injection over-defense | WebSearch | InjecGuard, PIDS-Bench 2609.15017, AWS blog 98.97% -> half FP, HiddenLayer | InjecGuard included; AWS blog inaccessible (fetch returned header only); PIDS-Bench not fetched |
| arxiv 2410.22770 PDF | curl/pdftotext | Tables 1, 7 | included as use-injecguard-overdefense |
| WebSearch Llama Guard/ShieldGemma independent eval | WebSearch | arxiv 2609.36477 (guard overconfidence), 2609.19072, 2605.28830, 2502.15427 | 2609.36477 fetched: adversarial calibration, not OOS; excluded. Search snippet claim "ShieldGemma-2B beats 9B" unverified, not used |
| WebSearch LLM vs encoder OOS CLINC | WebSearch | smallestbusiness/intent-router, vrajnotviraj/laya-intent-router, 2607.27421, 2106.04564 | first three included; 2106.04564 not fetched |
| gh api readme smallestbusiness/intent-router | gh | negative class experiments | included as use-intent-router-banking77 |
| gh api readme vrajnotviraj/laya-intent-router | gh | 98.6% OOS recall author claim | included as use-laya-intent-router |
| arxiv 2607.27421 pdf | curl/pdftotext | 41 models | included as use-zeroshot-llm-41-models |
| WebSearch NeMo Guardrails topical rails eval; arxiv 2310.10501 pdf | WebSearch/pdftotext | Tables 2,3 | included as use-nemo-guardrails-topical |
| Rasa fallback/OOS docs, Inworld, AI Dungeon, parser IF, voice-command games | - | - | not run (time); gap |
| Production structured-output LLM classification blogs with numbers | - | - | not run; gap |
| SetFit/ticket classification vs GPT-4 real-data reports | - | - | not run beyond SetFit; gap |

## Model scale and local candidates (`scale-` evidence, step5 input)

# Search log (scale- agent, 2026-10-02)

| Query / action | Tool | Notable hits | Outcome |
|---|---|---|---|
| Read study/open notes (kev, semif, simple-jev, laya, von, verdict, deberta, jevmlx, mini-jev, anyjev, nimble, decider, gliner2-5-decide, modernbert-ja, nanojev) | Read/Bash | leads only | used as leads; re-verified against sources |
| HF API model metadata for 25 candidate ids | curl (HF API) | sizes, bases, licences, dates | included in candidates-raw.md; `knowledgator/gliformer-small-v1` and `heman10x/openJev-verdict-2.0` returned auth error (not found / inaccessible) |
| HF API list author=knowledgator search=gliformer / gliclass | curl | only base-v1 and large-v1 for gliformer; GLiClass up to large-v3.0 | included as scale-gliformer-base-vs-large |
| gliformer base/large model cards | curl raw README | 264.2M vs 575.6M; classification macro-F1 72.36 vs 75.03 | included as scale-gliformer-base-vs-large |
| jeff README and bench/RESULTS.md | gh api | JevBench tiers, families, base noul failure | included as scale-gliformer-base-vs-large, scale-jevbench-cross-model-and-jeff-hard-tier |
| Kev README + 4 model cards | gh api | size ladder, injection, When2Call, unknowable | included as scale-kev-size-ladder |
| Decider README | gh api | size ladder, stock readout, MPS | included as scale-decider-size-ladder-and-stock-readout; RESULTS.md path 404 |
| JevBench repo: RESULTS.md, family-supplement JSON, METHOD-v1.4 | gh api | hard_by_family for 9 systems | included as scale-jevbench-cross-model-and-jeff-hard-tier |
| SemIf docs RESULTS/APPLE_SILICON/MLX/README | gh api | ladder 0.6B/2B/4B/27B; MPS+MLX | included as scale-semif-minijev-jevmlx-llm-readers |
| mini-jev, jevmlx, simple-jev, AnyJev, Nimble, Von, Laya READMEs | gh api | backend/Apple notes | candidates-raw.md; mini-jev/jevmlx included in scale-semif-...; AnyJev as scale-anyjev-qwen3-label-heads |
| GitHub repo metadata for 13 repos | gh api | pushed dates, licences, stars | candidates-raw.md |
| HF API Qwen3.5 / Qwen3.6 / Qwen3.8 / Gemma-4 sizes | curl | params for all sizes | candidates-raw.md |
| HF search mlx-community/Qwen3.5, unsloth Qwen3.5, ollama.com library tags | curl | MLX 4/6/8-bit/bf16, GGUF, Ollama tags | candidates-raw.md |
| llama.cpp grammars README, Ollama structured-outputs doc, mlx-lm SERVER.md/sample_utils, xgrammar and outlines READMEs | gh api | json_schema->GBNF; Ollama format; mlx-lm no schema; xgrammar[metal] | candidates-raw.md (class d) |
| dhtocks/malkuth-4b card, kev-suites dataset, LocalLLaMA/typed-decisions dataset | curl | Kev-derived 2B/4B (CC-BY-NC) | candidates-raw.md |
| Cygnet / Winnow-12B / typecastlm / clm-8b details | HF search | only unrelated hits for "cygnet" | not run in depth; only numbers from jevbench artifact used |
| arXiv / independent scale papers (NLI size vs shortcuts) | not run | out of scope (lit- agent) | not run |
| WebSearch/WebFetch | not used | gh/curl sufficed | n/a |
| GitHub issues for per-size rejection failures (Kev/Decider/Laya) | not run | time; eco- agents cover issues | not run |
