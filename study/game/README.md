# Study: game applications of jeff and typed decision models

Survey as of **2026-10-02** for episode [game_test/p1](../../devdocs/episodes/game_test/p1/plan.md). It looks for existing games, or close examples, in which a runtime classifier or typed decision model (Jev-style `choice` / `noul` / `score`) drives game rules or interaction. Search coverage and exclusions are in [search-log.md](search-log.md), and per-example notes are in [examples/](examples/). General model surveys stay in [open/](../open/) and [close/](../close/); start with [open/jeff.md](../open/jeff.md) and [open/laya.md](../open/laya.md).

**Headline: no game application of jeff itself was found.** Games built on hosted Jev, the open Laya encoder and the Jev-style JEVfire are plentiful, and they use the same request shape as jeff. These are the evidence base below. Nothing here was run or played locally. All results are attributed to their authors.

## Relevance levels
- **Direct:** a documented game application of jeff or of a Jev-compatible / Jev-style typed decision model whose output drives game behavior.
- **Close:** classification, intent detection, semantic matching or scoring (not Jev-style) that drives actual game behavior.
- **Adjacent:** broader game AI with an identifiable decision component. None was retained: the direct and close examples covered the mechanics better.

## Comparison
| Example | Mechanic | Level | Demonstrated status | Model role | Local execution | Fit for a small isolated jeff test |
|---|---|---|---|---|---|---|
| [Jev NPC gate guard](examples/jev-npc-gate-guard.md) | Player free text → NPC action + credibility gate; authored lines | Direct | Playable prototype; author's scripted playtest | `choice` over state-filtered actions + `noul` | No (hosted Jev; Mock offline) | **High**: short options, clear expected labels, existing scenario style to copy |
| [JEV Tetris](examples/jev-tetris.md) | Code-described placements ranked by model | Direct | Playable; 3-seed eval with controls | `choice` ×5, weighted blend | No (hosted) | Medium: good harness, but a keyword baseline already wins |
| [JEV Chess core](examples/jev-chess.md) | Legal moves as options; code computes facts | Direct | Live web game; anecdotal analysis | `choice` over all legal moves | No (hosted) | Low–medium: many near-identical options |
| [Jev Plays Pokémon](examples/jev-pokemon.md) | Long-horizon RPG agent over legal options | Direct | Completed 37 h run (author-reported) | `choice` per menu / battle / navigation step | No (hosted) | Low: too large; reuse the loop-protection idea |
| [Jev Werewolf](examples/jev-werewolf.md) | Deception judge; drives village vote | Direct | Research prototype with CIs | per-player probability (several designs) | No (hosted; local LLM baseline) | Medium: a "suspicion meter" with known hidden truth; long text is a risk |
| [Laya T-Rex / Snake](examples/laya-trex-snake.md) | Real-time control; planner proposes, model picks, shield corrects | Direct | Runnable demos; latency benchmark | `choice` among planner-labelled moves | **Yes** (MLX, Apple Silicon) | Medium: architecture reference; jeff too slow per frame |
| [JEVfire demos](examples/jevfire-village.md) | Player-written NPC policies → finite jobs | Direct (Jev-style) | Public web demos; no policy-following eval | finite-label scoring by Qwen 0.8B | **Yes** (WebGPU in the browser) | **High**: few options, low decision rate, policy-as-text |
| [Semantris](examples/semantris.md) | Player word ranks on-screen words | Close | Released game (2018) | similarity ranking (dual encoder) | Not stated | **High**: simplest input/option shape |
| [Façade NLU](examples/facade-nlu.md) | Player text → discourse acts → reactions | Close | Released game (2005) + paper | rule-based classification (24 act types) | Yes (rules, not a model) | **High** as a design template: label set before reaction rules |

"Fit" is our inference about how easily the mechanic can be tested in isolation with jeff. It is not a property reported by the source.

## Synthesis
1. **The model chooses and the code does everything else.** In every Direct example, the game code:
   - builds the option set and filters it by state;
   - writes the facts the model needs (exchange outcomes, placements, distances);
   - validates or executes the choice;
   - owns fallbacks: a Mock provider, a default action, safety shields, loop tagging, checkpoint reload.

   An illegal action cannot be represented, but a legal and *bad* action still can.
2. **The model only adds value where the input is open-ended.**
   - When code-written descriptions already encode the answer, a regex beats Jev (Tetris).
   - When the player phrases things freely, Jev beat a keyword Mock 5/5 vs 0/5 on paraphrased intents (gate guard).

   The best fit for jeff is interpreting player language, not reading data that code has already structured.
3. **Question design and option wording dominate results.**
   - Werewolf: narrow multi-dimension questions reached AUC 0.71, while one broad `noul` was below chance.
   - Chess: identical move descriptions made the model guess.
   - Werewolf: naming a tactic in the criteria backfired.
4. **Confidence is used as a gate, but thresholds are set by hand.**
   - The gate guard requires confidence ≥ 0.50 and credibility ≥ 0.55 before granting entry.
   - Werewolf found abstention thresholds *hurt* win rate.
   - No example calibrates probabilities for game use.
5. **Latency shapes the mechanic.**
   - Hosted Jev (~0.2–0.4 s per decision) appears only in turn-based or event-driven games.
   - The real-time games use in-process local models (Laya-MLX ~13 ms; Qwen 0.8B ~71 ms) together with planners or shields.
   - jeff on this Mac was observed at ~50–180 ms through HTTP after warm-up (single observations, [start/p2](../../devdocs/episodes/start/p2/report.md)). That is suitable for turn-based or event-driven play, not shown to be suitable for per-frame play.
6. **Evaluation is thin.**
   - Results are run by the authors, on few seeds or on scenarios they wrote themselves.
   - No human playtest results were found for any example.
   - The gate guard plans blind playtests but has none published.

## Engine integration references (not games)
- [0x440-1me/laya-unity](https://github.com/0x440-1me/laya-unity): a Unity client for `/v1/systemone` (MIT, v0.1, "not production-ready"). Transport-only: no embedded model. It would work against jeff's endpoint unchanged, as far as the README shows (not tested).
- [NobodyWho](https://docs.nobodywho.ooo/): a Godot 4 GDExtension for local llama.cpp LLMs with structured output and embeddings (EUPL-1.2). It is an alternative local runtime, not a classifier API.
- **No Godot game or plugin using a Jev-style model was found.** A Godot client for jeff would be a plain `HTTPRequest` to `/v1/systemone`. This is an inference: it has not been built or tested.

## Guidance for p2 and p3
Everything in this section is proposal and inference, derived from the examples above. None of it has been tested with jeff yet.

### Promising mechanism patterns
| Pattern | Grounded in | Why it fits a small original game | jeff's responsibility | Deterministic rules around it |
|---|---|---|---|---|
| **A. Player utterance → NPC reaction** | [gate guard](examples/jev-npc-gate-guard.md), [Façade](examples/facade-nlu.md) | Open-ended input is where a classifier beats keywords. A handful of actions plus authored lines fits a single scene. | One `choice` over the actions (or discourse acts) currently allowed. Optionally a second `choice` (e.g. credible / not credible) instead of `noul`. | State-based action filtering, authored dialogue per action, confidence gate on rule-critical actions (e.g. "open the door"), default action when invalid, low-confidence or slow |
| **B. Player-written order → NPC job** | [JEVfire Last Hearth](examples/jevfire-village.md) | The player's text acts as a standing policy, so a decision rate of seconds per NPC is fine. Each role has few options. | One `choice` per NPC tick: state = policy text + short observation; options = that role's useful jobs | Code filters useless jobs, automatic needs (eat, rest) override, a round-robin schedule, and visible probabilities so players can debug their orders |
| **C. Semantic matching of a player word against runtime targets** | [Semantris](examples/semantris.md) | The simplest input and option shape (one word or phrase vs ~5–20 short labels). Clearing rules are easy to make deterministic. | One `choice` over on-screen targets, with instructions setting the relation (associated / opposite) | Score threshold or explicit "none" option (probabilities always sum to 1), clearing and scoring rules, curated word lists |

The judging pattern ([werewolf](examples/jev-werewolf.md)) and the enumerated-legal-moves pattern ([Tetris](examples/jev-tetris.md), [chess](examples/jev-chess.md)) are secondary. The judging pattern depends on long transcripts. In the legal-moves pattern, code already encodes the answer.

### Isolated tests for each pattern (p2)
For each chosen pattern, test jeff alone through `/v1/systemone`, with no game:
- **Valid outputs:** the answer is always one of the offered keys. Probabilities lie in [0, 1] and sum to 1, including with options removed by state.
- **Obvious cases:** at least one clear input per option (e.g. a polite request → ASK_FOR_REASON; a threat → WARN_PLAYER).
- **Ambiguous and paraphrased inputs:** keyword-free paraphrases (the gate guard's probe style), mixed intents, and off-topic text. Record the top-1 choice and the top-two margin, and compare them with a keyword baseline.
- **Repeatability:** the same request twice gives identical probabilities (seen once in start/p2), and changing option order or wording changes the result.
- **Latency:** cold start, first request and warm requests. Vary the number of options, the state length, and `JEFF_ISOLATE` settings. Report observed distributions, not guarantees.

### Uncertainties p2 must resolve
- **Japanese input:** GLiFormer-large-v1 has not been tested on Japanese here. If the game is in Japanese, test it early. [modernbert-ja-310m-jev](../open/modernbert-ja-310m-jev.md) and Laya multilingual are fallback candidates.
- **Thresholds:** jeff's probabilities are temperature-scaled sigmoids (T = 3.2), not calibrated. Any gate value (like the gate guard's 0.50 / 0.55) must be chosen from p2 data for jeff specifically.
- **Option wording:** label keys vs descriptions, and how many options can be offered before accuracy drops.
- **`noul` and `score`:** untested in this repo, and `noul` is reportedly brittle. Prefer two-option `choice` until they are tested.
- **Disagreement handling:** decide in advance what the game does when jeff's choice is legal but contradicts the expected behavior, e.g. low-margin fallback to a default action, a re-ask line, or accepting it as character.
- **Long state:** history and memories make the state long. Encoder behavior with longer inputs needs testing.

### Implications for p3 (Godot)
- **Asynchronous calls:** use Godot `HTTPRequest` (or a thread) so the game never blocks while waiting for a decision. Show a "thinking" state, as the gate guard's performance lifecycle does.
- **Startup and warm-up:** start jeff before the game, or from a launcher. Poll `/healthz` (~11 s observed to healthy), then send a throwaway warm-up request during a loading screen (the first request took up to 1.35 s).
- **Timeouts and fallback:** set a per-request timeout. On a timeout, error or invalid answer, apply a deterministic fallback, e.g. a rule-based Mock as in the gate guard, or a safe default action. Never consume the player's turn on a failure.
- **Logging:** record the state, options, probabilities, choice and latency for every decision, so playtest sessions can be analysed (as the Tetris and gate-guard projects do).
- **Needs human playtesting:**
  - whether reactions feel fair and intelligible;
  - how often misclassification frustrates players;
  - whether waits are noticeable;
  - whether showing probabilities helps;
  - whether players game the classifier with keywords.

  No example in this survey has published human results, so p3 cannot borrow them.
- The smoke-test timings from start/p2 (three requests, single observations) do **not** guarantee interactive performance. Measure latency inside the p3 game.
