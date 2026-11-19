# NotJev

- **Category**: open
- **Owner / org**: 9pings
- **URLs**: https://github.com/9pings/notjev ; npm `notjev`; docs in `docs/` (question-forms, measurements, servers, internals)
- **License** (code / weights): Apache-2.0 / none
- **First release / last update**: created 2026-09-22 / last push 2026-09-30
- **Popularity signals**: ~20 stars

## Summary
A zero-dependency Node.js client/server that makes any OpenAI-compatible endpoint returning logprobs (vLLM, llama.cpp, Ollama, OpenAI) act as a one-token decider, and exposes a Jev-wire-compatible `/v1/systemone`. Differentiator: explicit abstention (`null` verdict + `theta` margin), engine-portable "bands", and measurement of letter-prior bias across menu sizes.

## Approach / architecture
- Options presented as `A.` `B.` ...; request with `max_tokens: 1` and `logprobs`; keep only the letter mass, renormalise; verdict + margin (p1-p2) + tunable abstention `theta`. `coverage` = option mass before renormalisation (low -> model wanted to say something else), `degraded` flag. Max 26 options. `noul` takes caller-supplied two options (no hard-coded language words); `score` over digit scale gives expectation.
- Raw p1 is not portable across engines; instead `band` (low <0.5, med <0.75, high <0.9, certain) is reported. README: "probabilities are ordered but not calibrated". Optional `harness.letterPrior` estimates and divides out the letter prior.
- Parallelism: one HTTP request per question (leans on server prefix caching); a `packed` arm exists (refused on tokenizers where the `_` placeholder is not a token, e.g. Gemma: `PACKED_MISALIGNED`).
- Escalation design: uncertain cases routed to the same model in chat mode (System 2).

## Interface
`/v1/systemone` (Jev wire contract, "a typesafe-sdk works unchanged"; answers grouped `{nouls, choices, scores}`, `confidence = 1 - H(p)/ln K`, FastAPI-shaped 422s, plus a `notjev` block with margin/band/coverage/degraded), native `/v1/decide`, CLI with exit codes 0/3/4, MCP server and gateway.

## Reported performance
Author-measured, RTX 5090 (bench/throughput.js, raws committed):
- p50: llama-server Qwen3-8B Q4_K_M 23 ms (41.8 q/s c1); Phi-4 Q4_K_M 19 ms; Gemma-3-12B Q4_K_M 61 ms; vLLM Qwen3.8-27B-NVFP4 101 ms (9.6 q/s c1). Hosted Jev quoted at 419 ms median (source not given in README).
- Accuracy on the author's own production-state gold: K=2, rich state: 27B 97.5% (7.5% flips), 8B 92.5%, Phi-4 90.0%, Gemma 87.5%; at K=19 menu: 27B 64.3%, 8B 32.1%, Gemma 53.6%, Phi-4 25.0%; order-flip rates 40-76% at K=19. Letter prior concentrates 50-300x going from K=2 to K=19. Prior correction helps only some models (Phi-4 +14.3 pts, Gemma +7.1, 8B -3.5).
- Notes vLLM `packed` is slower than reading one by one with prefix cache.

## Self-hosting notes
Node >= 20, no dependencies; single-file binaries per release; needs a separately running model server.

## Assessment
Most explicit about abstention semantics and letter-bias failure at large menus; useful practical evidence that K >= 10 is unreliable for small models. Weaknesses: small, author-specific gold sets (unverified externally), no calibration step beyond bands. Good test harness idea (null arms, replay).

## Sources
- https://github.com/9pings/notjev (README, metadata)
