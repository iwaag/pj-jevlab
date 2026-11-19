# JEVfire game demos: Last Hearth, Slipstream, World 1-1

## Overview
[JEVfire](../../open/jevfire.md) assigns typed variables by scoring finite single-token labels with an LLM, instead of generating JSON. It ships three browser games in which a local Qwen3.5 0.8B (WebLLM/WebGPU) picks finite actions:
- **Last Hearth:** a 3D survival village where six villagers have personality prompts and role policies **written by the player**. Collectors choose safe or bold foraging, fighters train or defend, and builders repair, build or heal. Every role can also relax.
- **Slipstream:** four racing cars, each with an editable strategy prompt. They choose speed changes, overtakes, boost and pit stops.
- **World 1-1:** a Mario-style level where the model selects collision-checked maneuvers, with a physics guard.

## Relevance level
**Direct (Jev-style).** It is a typed finite-choice decision layer, but not the Jev wire format (`/v1/decisions`, not `/v1/systemone`), and the model is a decoder LLM, not an encoder.

## Maturity / evidence
- Playable public web demos (kikoncuo.github.io/jevfire, HTTP 200 on 2026-10-02). MIT; 71 stars; created 2026-09-16.
- **Inspected:** README sections on the games. **Not played** (it needs a WebGPU browser and a ~450 MB model download).

## Game mechanic
**Player-authored natural-language policy → NPC action selection.** The player writes orders and role policies. The model reads them together with an observation and picks one of a finite set of jobs. This differs from the gate guard: the player's text is a standing policy, not a conversational turn.

## Decision inputs and outputs
- **Last Hearth state:** nearby orcs and their targets, food routes, travel estimates, hunger, wounded allies, damaged buildings, plus the villager's personality and role prompt.
- **Last Hearth options:** the jobs for the villager's role, "filtered to useful jobs" by code.
- **Rules outside the model:** automatic needs (eating, rest triggered by stamina) and supply consumption are game rules and "do not count as AI decisions".
- **Scheduling:** one living NPC is scored at a time, in a fair round-robin.
- **Slipstream state:** position, gaps, lane traffic, closing speeds, time to contact, corner distance and safe speed, tyres, damage, boost, pit distance.
- **Inspectability:** every decision is shown in the UI with its option scores and the exact observation used.

## Implementation / runtime
Browser, WebLLM and WebGPU. Qwen3.5 0.8B runs entirely locally, with no API key. A separately labelled scripted baseline needs no model download. The CUDA/vLLM server path is separate.

## Availability and licenses
MIT (code). Qwen weights are downloaded separately (license not re-verified here). Art credits are in `web/ASSETS.md`.

## Attributed results (author)
- World 1-1 on Apple M4 Max: 71.26 ms mean worker inference per action; 511 accepted choices; level cleared in 40.12 s.
- Slipstream: "Prompts express intended strategies, not guaranteed behavior." The earlier survey notes that faster scoring did not make the drivers better.
- Last Hearth: no quantitative results. The author notes that structure is guaranteed but "a legal choice can still get a villager killed".

## Possible jeff adaptation (inference)
The Last Hearth loop is close to jeff's strengths: short observations, a few role-specific options, a low decision rate (round-robin, not per frame), and visible probabilities. jeff could take the place of the Qwen scorer behind a local HTTP call. What has to be tested is whether a zero-shot NLI-style classifier actually **follows a player-written policy** (e.g. "Mira never leaves the walls at night"), which is entailment between the policy, the situation and the option.

## Limitations
There is no evaluation of how well the player's policy is followed. The demos use a tiny decoder LLM, not an encoder, so the results do not transfer directly to jeff.

## Sources (accessed 2026-10-02)
- https://github.com/kikoncuo/jevfire (README; `docs/` listing)
- https://kikoncuo.github.io/jevfire/ (reachability check only)
