# Tooling and integrations around Jev (brief)

Survey date 2026-10-01. Stars from `gh`; descriptions are repo/awesome-list text (unverified functionality).

## Official / semi-official
- typesafe-ai/skills (2,513 stars, MIT, created 2026-08-24, i.e. before the public launch): official installable agent skills (`npx skills add typesafe-ai/skills`).
- Vercel stack ships Jev as the default eval model: vercel/eve, vercel-labs/ai-cli, vercel-labs/ai-python, vercel-labs/fx (permission reviewer), vercel-labs/json-render; model id `typesafe-ai/jev` via Vercel AI Gateway (`experimental_evaluate`, AI SDK 7). Note: jev-ood-calibration found `typesafe-ai/jev-latest` returns "Model not found" on the Gateway.
- Distribution channels: OpenRouter (beta), Cloudflare AI Gateway, Vercel AI Gateway, Neon AI Gateway (safer-with-jev), Cline plugin collection (jev-browser).
- LangChain: per LangChain's blog "Building a harness with Jev", a `TypeSafeClassifier` provider (state + questions via `.invoke()`) and an `AutoModeMiddleware` that has Jev vet tool calls before execution (repeats vendor claim "up to 200x faster, 400x cheaper"). Mastra: mastra-jev-moderation input processor. LlamaIndex: unofficial llama-index-jev (Score each retrieved passage; nfcorpus nDCG@5 0.340 reported). Smithers, Atomic, opencompany, OpenWork, duet-agent also embed it.

## Agent skills and harness plugins
- jev-ai/jev-agent-skill (4 stars, no license, created 2026-09-21): skill for Claude Code/Codex/Cursor for the *Jev AI* API at thejevai.com (a third-party gateway selling Jev access; default model `typesafe/jev-1.13`, keys `sk_...`, EN and zh-CN onboarding). Not the official TypeSafe skill; do not confuse with typesafe-ai/skills.
- Many "Jev for coding agent X" tools: Claude Code (jev-axi, jev-guard, jev-belay, quicksilver [claims 86% fewer Claude tokens on a 12-task benchmark], fast-jev-compaction, jev-pruner, winnow, jevmem), Codex (jev-codex-router 277 stars, Codex Jev Router), Pi agent (pi-jev, pi-verdict, pi-heed, pi-typesafe-jev, pi-jev-router), DeepSeek Harness (dsh-jev, jevcore, jev-dsh-decision), OpenCode, Cline, Devin (jev-experiments: 22 demos). Dominant patterns: model routers, permission/safety gates, context compaction/pruning, completion checkers, code review.
- MCP servers: jev-mcp (jkudish; blakestone-x), decide-mcp, Jevbridge (ACP+MCP), system-one-connector (340 stars; Jev, D1, CLM, Laya), jev-use.

## SDKs and clients (hosted Jev)
Python jevclient (PyPI), Go jev-go / jevgo, Rust jevkit and jev-rs, Swift (alterhq/typesafe-sdk-swift; peterfriese/system-one-foundation-models bridging Apple Foundation Models), Kotlin Multiplatform kojev, Java (Premo-Cloud/typesafe-sdk-java), Ruby (ruby_decision_model, s1_ruby, jevalyn for Rails, ruby-laya), PHP (laravel-typesafe-jev, laya-php), Elixir (dannote/jev), Scala ZIO (zio-typesafe-ai), TypeScript (huncho, hunch). Data: sqlite-jev, jevql, pg-jev, duckdb-jev (3 variants), advocaat.
Open-model-side tooling: ollaya (Ollama for decision models, 1,070 stars), Arbiter, oh-my-jev gateway, rawwerks/one-system (single API over local and hosted), SystemOneHarness, jevcache (decision cache), Jevstiller/stuntd (distill repeated Jev calls into a local head), jevcal (threshold calibration), should-i-jev (migration pricing CLI).

## Languages and frameworks
- nudge (NekomyaDev/nudge, 3 stars, Apache-2.0, Rust compiler, v1.2.1, created 2026-07-16, i.e. predates Jev): "typed, replayable, budget-aware programming language for LLM agents", compiles to Python and TypeScript. Its README (verified) has a `decide { choose / yes-no / score }` construct for "batched JEV-family decisions with distributions, confidence, deadlines", pointing at a local Laya server or Jev via `NUDGE_DECISION_SERVERS`. Tagged jev-alternative; it is a language that treats decision models as a primitive, not an alternative model.
- Related: Noul discussed as a general "decision primitive" (Ask HN id 49760225); augustus skill maps Choice/Score/Noul to classical methods; s1_ruby makes System One measurement a Ruby primitive.

## Apps built on Jev (sample)
- browser-use/jev-ultrafast: 21,644 stars (MIT, created 2026-09-16): "fastest and cheapest web agent"; per-step Jev action selection; spawned laya-ultrafast, Jev for Chrome, fastbrowse, Sedum, public-browser, BrowserClaw. The single most-starred Jev-using app.
- jeves-desk (dabaicai001, 1 star): generic customer-service platform refactored from OpenAI's ChatKit customer-support sample; ChatKit UI + Jev decisions + Qwen generation + RAG + MCP; industry swap by editing YAML. README text verified; mostly Chinese.
- Jev-trading/Jev-trading (1 star, MIT, 2026-09-24): no-code desktop algo-trading terminal pitched on Jev speed. Other trading: Jevinik, jev_stock, jev-trade (Hyperliquid), warrenduffer (Indian stocks, 15 s ranking of Nifty 50), an on-chain Monad bot deciding every 300 ms block. No performance evidence seen; treat as demos.
- Games/robotics: typesafe-mario, jev-drone (MuJoCo, 2.5 Hz), tsai-sc (StarCraft), jev-plays-pokemon, jev-libero, robo-harness.
- Moderation/feeds: jev-slop-guard, sift, PlotVeil, Jev Moderation Bot, profanity-checker, gg-friggin-ez.
- Consumer/desktop: jev-voice, jev-use (computer use), typesafe-computer-use (1,110 stars; $0.0002/step claim), HA-Jev (Home Assistant), jevgrep (1,961 stars), jgrep, jev-chat-windows (711 stars; WeChat reply assistant).
- Search/RAG: jev-reranker, JevPDF, jevsearch, Jev Search, jev-rag; vendor-neutral evidence: superglue (URL ranking), Willison's BM25-then-Jev reranking demo.
- Warning from awesome-jev-tools: mass-submitted repos with identical AGENTS.md/STATE.md scaffolds; check that code really calls the API.
