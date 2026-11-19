# OpenAI Decisions API

- **Category**: close
- **Owner / org**: OpenAI
- **URLs**: https://the-decoder.com/openai-expands-codex-and-its-api-at-devday-with-security-scans-a-decisions-api-and-ultrafast/ ; https://modelsystem.one/runtimes/openai-decisions-api/
- **License** (code / weights): proprietary, hosted
- **First release / last update** (as seen 2026-10-01): announced at DevDay 2026-09-29; limited preview, broader rollout "in the coming days"
- **Popularity signals**: TechCrunch headline "OpenAI's Jev clone could help the frontier lab stop its swarming agents"; widespread press

## Summary
OpenAI's entry into System One-style models: define a question and a bounded list of answers, supply context (text, reportedly images), get a selected option with a confidence score in one call. Press says it is powered by a specialized GPT-6 Luna.

## Approach / architecture
Reported (press, not official detail): specialized version of GPT-6 Luna; ~150 ms per decision vs 1.6 s via the regular Luna API ("ten times faster"). Mechanism unpublished.

## Interface
No endpoint or schema published as of 2026-09-29 (modelsystem.one). Only choice confirmed; unclear if noul/score exist. Not /v1/systemone-compatible. Pricing, limits, rate limits unpublished. Image input is a preview capability per one practical guide (secondary source, flagged speculative).

## Training & data
Not disclosed.

## Reported performance
Only the vendor latency figure above; no accuracy or calibration data; calibration of the confidence score unverified.

## Self-hosting notes
None.

## Assessment
Worth tracking: the first frontier-lab competitor, but there is nothing testable yet. Details in secondary blogs (Hugging Face-hosted posts, Medium) are partly speculative.

## Sources
- https://the-decoder.com/openai-expands-codex-and-its-api-at-devday-with-security-scans-a-decisions-api-and-ultrafast/
- https://modelsystem.one/runtimes/openai-decisions-api/
- https://huggingface.co/blog/sora-2/what-is-openai-decisions-api-a-practical-guide
- https://techcrunch.com/?s=Jev+TypeSafe (headline only)
