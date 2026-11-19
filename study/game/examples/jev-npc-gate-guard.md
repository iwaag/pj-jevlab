# Jev NPC Interaction Prototype (gate guard "Arthur")

## Overview
A small browser text game. The player talks over an intercom to Arthur, a gate guard, and tries to get into a warehouse car park. Arthur's lines are all hand-authored. A decision model chooses only Arthur's next structured action, and the game then picks a matching authored line. Purpose stated in the README: test "whether a decision model can make hand-authored NPC dialogue feel reactive and autonomous."

## Relevance level
**Direct.** Hosted Jev (`jev-1.13.0`) through the System One API; jeff uses the same request shape.

## Maturity / evidence
- Playable prototype with an offline Mock mode, hosted at jev-npc-interaction-prototype.vercel.app (HTTP 200 on 2026-10-02; Mock only, since Jev mode needs a server-side key).
- **Inspected:** README and `PLAYTEST_REPORT.md` (automated scenario run generated 2026-09-22). **Not inspected:** the game itself was not played, and the code was not run.
- Repo created 2026-09-19, last push 2026-09-30; 0 stars.

## Game mechanic
Natural-language persuasion. The player builds a credible case through free text (work claim, emergency, delivery, apology). Arthur can ask for a reason or proof, become suspicious, repair the conversation, warn, de-escalate, refuse, or allow entry. Four terminal outcomes: entry, refusal, expulsion, lockout.

## Decision inputs and outputs
- **State:** the player's message, Arthur's fixed character profile (one of four), the latest 6 exchanges, up to 8 tagged memories, emotional state values, and a cognitive note ("estimated IQ of 95").
- **Questions** (one request, evaluated in parallel):
  - `choice` over the **currently available** actions. There are 12 in total: ANSWER_QUESTION, REFUSE_ENTRY, ASK_FOR_REASON, ASK_FOR_PROOF, ALLOW_ENTRY, WARN_PLAYER, DEESCALATE_THREAT, THREATEN_PLAYER, SHOW_SYMPATHY, BECOME_SUSPICIOUS, REPAIR_CONVERSATION and END_CONVERSATION.
  - `noul`: "is the player's spoken case credible?"
- **Consumption:**
  - The game validates the action and selects an authored line (templates with slots, deterministic variant choice).
  - It applies deterministic state and memory effects.
  - `ALLOW_ENTRY` is accepted only with action confidence ≥ 0.50 **and** credibility ≥ 0.55. Otherwise Arthur asks for a better explanation.
- **Rules around the model:**
  - Code removes actions from the option set based on state. Unrepaired serious memories remove `ALLOW_ENTRY`, and `BECOME_SUSPICIOUS` is unavailable until a repair.
  - An invalid action falls back to `REFUSE_ENTRY`.
  - If the provider fails, the turn is not consumed: the text is kept and the selector returns to Mock.

## Implementation / runtime
- JavaScript in the browser, no build step.
- `server.mjs` (Node) keeps the TypeSafe API key on the server and forwards the decision requests.
- Speech uses Piper (WASM neural TTS) with eSpeak NG and Web Speech fallbacks.
- Hosted Jev; no local decision model.
- A rule-based Mock provider (keyword intent matching) is the offline baseline.

## Availability and licenses
- Source is public on GitHub. **No license file** is reported by the GitHub API, so reuse rights are unclear.
- Third-party assets: VT323 font (OFL); Piper and eSpeak NG data under CC-BY-SA/GPL per `THIRD_PARTY_NOTICES.md`.
- No model weights; Jev is closed.

## Attributed results (author's automated playtest, `PLAYTEST_REPORT.md`, 2026-09-22)
- Core scenarios: Jev 12/15 PASS vs Mock 11/15.
- Generalization probes (familiar intents without the Mock's keywords: implied bribe, veiled threat, unusual phrasing): **Jev 5/5 vs Mock 0/5**.
- Action coverage: Jev 11/12 (never chose SHOW_SYMPATHY), Mock 12/12.
- Confidence: Jev averaged 0.82 over 41 turns; 5 turns fell below 0.50, the lowest at 0.24.
- Mistakes the author flags include REFUSE_ENTRY for "Why is the warehouse closed?" (expected ANSWER_QUESTION), and ASK_FOR_REASON instead of SHOW_SYMPATHY for an emotional appeal.
- Failure checks: an invalid action and offline recovery both passed.
- The author recommends keeping Jev as the optional provider and Mock as the offline fallback.
- No latency figures are published. Blind human playtesting is planned (`MANUAL_PLAYTEST.md`), and no results were found.

## Possible jeff adaptation (inference, not observed)
- jeff could serve the same `choice` request through its `/v1/systemone` endpoint locally, with no API key.
- The surrounding code would remain: state assembly, action filtering, the dialogue library, the confidence gates, and the fallbacks.
- Risks:
  - jeff's `noul` is reportedly brittle, so the credibility gate might need a two-option `choice` instead.
  - jeff's shared encoder pass lets choice and score questions influence each other.
  - The state here is long (history, memories, profile), and GLiFormer's long-input behavior has not been tested.
  - The 0.50 / 0.55 thresholds were set for Jev and would need re-tuning for jeff's temperature-3.2 probabilities.

## Limitations
The test scenarios were written by the author and include the probes; there is no held-out set. The game is in English only. The "intelligence" is measured as agreement with the author's expectations, not as player experience.

## Sources (accessed 2026-10-02)
- https://github.com/dazreil/jev-npc-interaction-prototype (README, `PLAYTEST_REPORT.md`, metadata via `gh api`)
- https://jev-npc-interaction-prototype.vercel.app (reachability check only)
