# Jev (TypeSafe AI)

- **Category**: close
- **Owner / org**: TypeSafe AI (San Francisco)
- **URLs**: blog https://typesafe.ai/blog/introducing-system-one-models-and-jev ; docs https://docs.typesafe.ai/introduction/quickstart (full docs index: https://docs.typesafe.ai/llms.txt); console https://console.typesafe.ai/playground ; Wikipedia https://en.wikipedia.org/wiki/Jev_(AI_model)
- **License** (code / weights): proprietary, hosted only; no weights, no technical paper (Wikipedia, TrueFoundry)
- **First release / last update** (as seen 2026-10-01): early access 2026-09-15; stable per Wikipedia `jev-1.13.0`; waitlist-gated
- **Popularity signals**: coverage by TechCrunch (2026-09-18, Tim Fernholz), Forbes, The Register, SiliconANGLE (per Wikipedia); available via Vercel AI Gateway (`typesafe-ai/jev`, announced 2026-09-16), OpenRouter, LiteLLM pass-through, Respan gateway; dozens of open clones appeared within days

## Summary
Jev is the first "System One model": a non-autoregressive model that takes unstructured state plus typed questions and returns typed answers with calibrated probabilities in one parallel pass, with no text generation. TypeSafe markets it as a "frontier-intelligence function call". All headline numbers (70-500 ms, up to 193.6x faster / 444.6x cheaper) are vendor-claimed; the few independent tests found are small and narrow.

## Company, founders, timeline
- Founded 2024 by Diogo Almeida (CEO, ex-OpenAI, credited with instruction-following research behind ChatGPT), Erik Gafni, Sasha Sheng (Wikipedia; TechCrunch headline lists the three). Wikipedia: $40M seed from DCVC, ~$200M valuation (single-source; not confirmed on the vendor blog I read).
- Roughly two years in stealth (vendor blog). Launch/early access 2026-09-15 (Wikipedia, DataCamp, others). The blog page shows a publication date of Sep 28 alongside the Sep 15 date; unclear which is canonical.
- 2026-09-16: Vercel AI Gateway adds it. Within ~2 weeks: Upstage, Liquid, Respan, Together, OpenAI (Decisions API, 2026-09-29) and many open clones followed.

## Approach / architecture (all vendor-claimed / speculative)
- Transformer-based (Wikipedia), "new model architecture designed for decision-making", "parallel sampler" that produces all outputs in one query instead of token-by-token (vendor blog). Questions in a request are evaluated in parallel; adding questions barely changes latency (LangChain blog, Papercompute).
- Training: trained exclusively on synthetic data (Wikipedia; vendor blog says training data source is not disclosed) with "Reinforcement Learning for Calibrated Decisions (RLCD)", contrasted with RLHF/RLVR; goal is "epistemically honest probabilities".
- Parameter count, base model, weights: undisclosed. Layer3Labs: "Calibration is a training objective. It is not an operational guarantee."
- Speculation about internals (third-party, not verified): shared state encoding followed by per-question heads / constrained single-step readout over allowed options. I found no authoritative source; treat as conjecture. Open clones (Kev, Decider, Tev1, Laya) imply plausible reimplementations via logit reading or encoder heads.
- Choice cardinality up to 255 options; larger sets need "two-stage scoring" (blog). Schema conformance is by construction, but the model can pick a wrong valid answer.

## Interface (API)
- Endpoint: `POST https://api.typesafe.ai/v1/systemone`, `Authorization: Bearer <API_KEY>`, `Content-Type: application/json`. Models: `jev-latest` (default), `jev-1.13.0` (docs). Via OpenRouter: `typesafe/jev-1.13` or `jev-1.13` at `https://openrouter.ai/api/v1/systemone`; via Respan: `POST https://api.respan.ai/api/typesafe/v1/systemone`, model `typesafe/jev-1.13.0`. SDKs: `typesafe-sdk` (Python >= 3.10, TypeScript), `langchain_typesafe`.
- Request: `model`, `state` (string, JSON object, or array), `questions` (object keyed by your own names). OpenRouter additionally lists optional `provider`, `session_id`, `trace`, `user`.
- Question types:
  - `noul`: `{"type":"noul","instructions":"..."}` (OpenRouter schema also lists `criteria` with true/false keys) -> `{"type":"noul","noul":0.0-1.0}`
  - `choice`: `{"type":"choice","instructions":"...","criteria":{"key":"description",...}}` -> `choice` (selected key), `confidence`, `probabilities` per key
  - `score`: `{"type":"score","instructions":"...","criteria":["level_0","level_1",...]}` -> `score` (probability-weighted float), `confidence`, `probabilities` by index, `legend`. Score scale 2-10 points (baobab-tech repo summary).
- Response: `{"model","answers":{...},"usage":{"input_tokens","output_tokens"}}`; OpenRouter adds optional `id`, `provider`. Errors listed by OpenRouter: 400, 401, 402, 403, 404, 413, 429, 5xx. Streaming is unsupported (Respan: `stream:true` returns 400).
- Exact example (from OpenRouter-hosted docs excerpt, via search summary):
```
curl https://openrouter.ai/api/v1/systemone \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" -H "Content-Type: application/json" \
  -d '{"model":"jev-1.13","state":"I was charged twice for my subscription.",
       "questions":{"refund":{"type":"noul","instructions":"Is the customer asking for money back?"}}}'
```
  response: `{"refund":{"type":"noul","noul":0.98}}` inside `answers`. LangChain blog shows `{"model":"jev-latest","state":"Hi, I've been trying to connect my Stripe account for 3 days...","questions":{"is_urgent":{"type":"noul","instructions":"The message conveys urgency or time-sensitivity"}}}` returning `noul: 0.999`. Respan docs example response: `usage: {"input_tokens":279,"output_tokens":22}` (note nonzero output_tokens there, differing from clones that report 0).
- Context: 32K tokens (Digital Applied listing via OpenRouter; vendor figure not seen). Rate limits unpublished.
- Pricing (vendor): $0.042 / MTok input, output free. No prefix caching (Navya AI), so repeated state is billed in full.

## Reported performance
Vendor-claimed:
- 70-500 ms end-to-end; "40-200x faster, 40-400x cheaper" than frontier LLMs; peaks 193.6x faster / 444.6x cheaper on TypeSafe-built "workflow evals". Caveats the vendor admits: workflows built by its own team, reference answers averaged OpenAI/Anthropic models, headline figures are high-end, "0% hallucination" is theoretical not empirical.
- Workflow eval table (DataCamp, attributed to TypeSafe): Jev 67.8% acc, $0.0004/case, 0.4 s; GPT-5.6 Terra 67.9%, $0.0304, 10.1 s; GPT-5.6 Sol 74.1%; Claude Opus 5 73.1%. Structured-output error rate: Jev 0%, GPT-5.6 Sol 17%, Claude Haiku 4.5 45.5%.
- JevBench v1.5.4: Jev 72.1 (as cited in baobab-tech repo; scorer is a community benchmark, not verified by me).

Third-party / semi-independent:
- Navya AI (self-run, 2026-09-21, AG News 4-class, 200 test + 200 holdout): accuracy 87.5-88%, raw ECE 0.080 (0.037 after temperature scaling T=5.17), p50 latency 357.7 ms, cost $18.57/1M cases. Beat gpt-4.1-nano/gpt-4o-mini JSON on calibration; real cost advantage vs small models was small; measured ~2.9x faster and ~12x cheaper than comparable alternatives, far below 193.6x. Per-type ECE: noul 0.012, score 0.254. Zero invalid JSON in 600 strict calls. Caveats: one easy task, +-6 pt intervals.
- eesel review: 284 chats, triage accuracy 93%, spam 100% with no false positives (self-reported). Quotes Vercel CEO: "up to 18x faster (p95) and more accurate" (vendor-adjacent).
- Respan (competitor, vendor-run behavior benchmark): Jev 1.13.0 F1 0.716/71.5 vs Span-01 0.806; separately a Respan-run 11-model table put Jev top on accuracy 0.932 and ECE 0.045.
- Liquid (competitor): Decision Index 0.2.1 (Hugging Face): d1 58.9 vs Jev 1.13 57.9.
- meraGPT (competitor): typed-decisions accuracy 0.768 vs Jev 0.727, KL 0.096 vs 1.442.
- Upstage-related community bench (umstek/zero-shot-ie-bench PR): Jev cloud 93.8% on 48-question mixed pool.
- Layer3Labs / BenchLM: "No independent benchmark of Jev exists as of September 2026" (earlier than some tests above).

## Limitations / criticism
- Can't emit malformed output but can be confidently wrong; "can't hallucinate" is overstated (Hacker News consensus per eesel/Firecrawl; reportedly CEO agreed in thread; HN thread not directly read).
- No explanations/rationales, no text generation, no streaming; max 255 choices; early access; unproven at scale; closed, no self-hosting.
- Weakly validated calibration: no published reliability diagram or ECE from TypeSafe; score-type questions poorly calibrated in Navya test.
- Benchmarks built by vendor, comparisons to frontier models not used for classification in practice; pricing sustainability unknown (DataCamp). Demos (Minecraft, drone, driving sim) are simulator-only (MindStudio).
- Possible English-first bias (a dev.to author measured decision models in Japanese; not read in detail).

## Assessment
Relevance to the lab: Jev defines the de facto wire protocol (/v1/systemone, noul/choice/score) that every competitor copies, so it is the baseline for compatibility tests. Treat vendor numbers as unverified; the Navya calibration numbers (ECE 0.08 raw) are the best independent anchor but are narrow. Priority experiments: calibration per question type (especially score), multilingual, long state, and prompt-injection robustness.

## Independent arXiv evidence (added 2026-10-08)
Most of the 111 arXiv papers posted between 09-19 and 10-07 use or evaluate hosted Jev (mostly jev-1.13.0); see [../recent_study/](../recent_study/README.md). Highlights, each from a full-text card unless marked "abstract":

**Accuracy and calibration**
- **Broad zero-shot sweep** (2609.37647): 37 datasets, 346,009 requests for under USD 10.
  - Beats the Qwen3.8-27B next-token readout on 27 of 37 datasets; none of Qwen's leads is outside the bootstrap intervals.
  - Rotating the options leaves accuracy unchanged.
  - Binary probabilities rank well, but a fixed 0.5 threshold is poorly placed. (abstract)
- **Against the best LLMs:** trails the per-task best LLM on 14 of 15 social-science annotation tasks, by a median of 11.6 macro-F1, at 44x lower cost (2609.24574). Close to GPT-6 Sol on PubMedQA but far behind on diagnosis cases (2609.34024; abstract).
- **Calibration** varies by task: good on familiar closed-choice tasks (2610.01006); three frontier LLMs are better calibrated on social-science tasks (2609.24574). It overstates the probability of the mode, 89% against a true 35% (2610.03935).

**Missing information**
- With no answer-relevant information, Jev still puts up to 0.80 on a salient option (2610.01006).
- An answer-free "is the evidence sufficient?" noul separates complete from incomplete evidence at AUROC 0.95, against 0.85 for answer confidence (2610.01006).
- With an explicit NONE option, correct rejection on arithmetic is only 7% (99% when the answer is present). A threshold on p(NONE) chosen on dev data raises it to 79% (2609.39496).
- Picks "I don't know" on 10.5% of unanswerable medical items (2609.34024).

**Option names and injection**
- **Label swaps:** swapping yes/no against fixed definitions flips 50.5 answers per hundred (2610.00346); AUC .81→.58 under a 0/1→no/yes rename (2609.26758).
- **Appended text:** one appended unverified opinion flips 12.1% of decisions, the same as the strongest injected command (10.1%), and pushes 38% of confident answers below 0.8 (2609.31142).
- **Optimised text:** fluent optimised context flips 61.4% of correct decisions (2609.30243).
- **Injected tool requests:** InjecAgent-style attacks select the attacker's target only 1.8% of the time (3.5% adaptive) (2609.28613).

**Coherence**
- P(X) + P(not X) misses 1 by 0.064, and single-label probabilities sum to 1.14 (2609.33209).
- Asking the same binary event through Event vs Choice changes the act/defer action on 32.8% of cases (2609.37470).
- Hierarchy reconstruction costs 22.9 points on CLINC150 (2609.33971).

**Shared errors**
- LLM judges repeat 96% of Jev's most confident errors, so Jev→LLM cascades add at most 2.7 points (2609.29769).
- **Ordinal scales:** decisions use only 67–76% of the gold level support (2609.38827).

## Sources
- https://typesafe.ai/blog/introducing-system-one-models-and-jev
- https://en.wikipedia.org/wiki/Jev_(AI_model)
- https://docs.typesafe.ai/introduction/quickstart
- https://openrouter.ai/docs/api/api-reference/systemone/submit-a-system-one-request
- https://www.respan.ai/docs/apis/type-safe-gateway/typesafe-systemone
- https://www.langchain.com/blog/building-a-harness-with-jev
- https://www.mindstudio.ai/blog/jev-system-one-model-launch
- https://papercompute.com/concepts/jev/
- https://www.datacamp.com/blog/system-one-models-jev
- https://www.truefoundry.com/blog/typesafe-ai-jev
- https://www.eesel.ai/blog/typesafe-jev-review
- https://www.navyaai.com/blog/jev-typesafe-limitations-production
- https://www.layer3labs.io/guides/jev-benchmarks
- https://github.com/baobab-tech/decision-models-experiments
- https://modelsystem.one/news/span-01-hyper-parallel-classifier/
- https://github.com/umstek/zero-shot-ie-bench/pull/17
- TechCrunch search listing (headlines only)
