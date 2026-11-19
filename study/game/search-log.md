# Search log — game applications of jeff and typed decision models

Searches run 2026-10-02 (JST) for [game_test/p1](../../devdocs/episodes/game_test/p1/plan.md). Relevance levels are defined in [README.md](README.md#relevance-levels). GitHub star counts are from `gh api` on the same day.

## Tools and sources
- `gh search repos` (GitHub repository search). The search API rate limit (30 queries/min) was hit twice; the affected queries are listed below as "not run".
- `gh api repos/<owner>/<repo>/readme` and `contents/<file>` for READMEs and reports (raw text, not summaries).
- WebSearch and WebFetch for papers, official blogs and documentation.
- Prior repo notes: [study/ecosystem/tooling-and-integrations.md](../ecosystem/tooling-and-integrations.md), [study/ecosystem/evaluations.md](../ecosystem/evaluations.md), [study/ecosystem/aggregators.md](../ecosystem/aggregators.md), [study/open/nanojev.md](../open/nanojev.md), [study/open/jevfire.md](../open/jevfire.md).

## Queries

### GitHub repository search
| Query | Notable hits (stars) | Outcome |
|---|---|---|
| `jeff jev game` | none | No game project built on jeff |
| `jev game` | jev-game-tools (14), jev-gamepilot (5), IAnMove/jev-game-agent (4), aieo-product/jev-gamebenchmark (0), ~10 repos with no description | Mostly scaffolds; agent/benchmark repos not shortlisted (see exclusions) |
| `laya game` | psurge1/LayaGamer (0); otherwise the unrelated LayaAir engine | Name collision with the LayaAir engine |
| `system one game npc` | none | — |
| `jev npc` | dazreil/jev-npc-interaction-prototype (0), Hugo-DDT/JevNPC (0), ispoet/jev-npc, wikigsroom/Jev-Npc-Town (no description) | **Shortlisted:** jev-npc-interaction-prototype |
| `jev godot`, `laya godot` | none | No Godot integration found |
| `jev unity`, `laya unity` | 0x440-1me/laya-unity (1) | Engine SDK, not a game (reference only) |
| `typesafe jev game` | none | — |
| `jev mario` | 4esv/jev-mario (1), SunnyKrS1ngh/JevMario (0) | Covered by the JEVfire Mario demo instead |
| `jev pokemon` | christianmat/jev-pokemon (116) | **Shortlisted** |
| `jev chess` | sliday/jev-chess-algo (2), hemanth/jev-chess (2), pulkitxm/jev-chess-agent (2), eriestra/jev-chess (Stockfish-graded), ~10 more | **Shortlisted:** sliday/jev-chess-algo (best-documented decision boundary) |
| `jev pong` | ably-labs/jev-pong (1), Postman-Devrel/JevPong (1), FlyJevPong, laya-or-jev-pong | Same pattern as T-Rex; not shortlisted |
| `laya-vs-jev` | virajbhartiya/laya-vs-jev (111), PromptEngineer48/laya-vs-jev-arena (29), Mica_4B Pac-Man (2), many benchmarks | **Shortlisted:** laya-vs-jev (local encoder on Mac) |
| `systemone game`, `jev dialogue`, `jev text adventure`, `jev villager`, `laya npc`, `typed decision game`, `decision model npc`, `jev roguelike`, `jev interactive fiction`, `jev card game` | none or unrelated | — |
| `jev rpg` | seventhocean/jev-rpg-world (0, no description) | Not inspected |
| `kev game` | unrelated (name collision) | — |
| `jev minecraft` | Anahadd/jev-minecraft, selmakcby/jev-minecraft-bot (1), NingNing0111/Jev-Minecraft-MineBlind, others (0–1) | Agent bots; not shortlisted |
| `jev werewolf` | NoorElAlfi/jev-werewolf (0) | **Shortlisted** |
| `jev tetris` | trungdq88/jev-tetris (17), thelau/jev-tetris (3), Tsagaanbayr1/jev-tetris (1), MachineLearning-Nerd/jev-tetris | **Shortlisted:** thelau/jev-tetris (has controls and baselines) |
| `jev snake`, `nanojev`, `jev detective`, `jev mystery`, `jev escape room`, `laya npc dialogue`, `system one npc`, `jev text game`, `laya game npc`, `jev godot plugin`, `semantic game input classifier` | — | **Not run** (rate limit). NanoJev was already covered in [open/nanojev.md](../open/nanojev.md) |
| `zero-shot classifier npc`, `godot llm npc local` | none | — |

### Web search
| Query | Notable hits | Outcome |
|---|---|---|
| Semantris, Universal Sentence Encoder | Google Research blog (2018-04-13) | **Shortlisted** (close) |
| Façade NLU, discourse acts (Mateas & Stern) | TIDSE 2004 paper (eis.ucsc.edu PDF) | **Shortlisted** (close) |
| NobodyWho Godot plugin, structured output | docs.nobodywho.ooo, Godot Asset Library | Godot runtime reference, not a game example |
| Inworld goals and actions, intent detection | Inworld docs (redirect to login), LinkedIn, NVIDIA blog | **Excluded:** primary docs not accessible without login; only search snippets |
| Inworld intent "training phrases" | docs.inworld.ai Unity demos (same login redirect), blog index | Same as above |

## Shortlist
| Example | Level | File |
|---|---|---|
| Jev NPC Interaction Prototype (gate guard Arthur) | Direct | [examples/jev-npc-gate-guard.md](examples/jev-npc-gate-guard.md) |
| JEV Tetris (thelau) | Direct | [examples/jev-tetris.md](examples/jev-tetris.md) |
| JEV Chess decision core (jevchess.com) | Direct | [examples/jev-chess.md](examples/jev-chess.md) |
| Jev Plays Pokémon Red | Direct | [examples/jev-pokemon.md](examples/jev-pokemon.md) |
| Jev Werewolf deception judge | Direct | [examples/jev-werewolf.md](examples/jev-werewolf.md) |
| Laya vs Jev T-Rex / Laya-MLX Snake | Direct | [examples/laya-trex-snake.md](examples/laya-trex-snake.md) |
| JEVfire game demos (Last Hearth, Slipstream, World 1-1) | Direct (Jev-style, not Jev wire format) | [examples/jevfire-village.md](examples/jevfire-village.md) |
| Semantris | Close | [examples/semantris.md](examples/semantris.md) |
| Façade natural-language understanding | Close | [examples/facade-nlu.md](examples/facade-nlu.md) |

## Excluded or not shortlisted (with reasons)
- **No jeff game application found.** Searches for `jeff` with game terms returned nothing. In the jeff repo, the README has no game use, and a code search for "game" matches only benchmark data files (`bench/data/*.jsonl`).
- **Hugo-DDT/JevNPC** (Minecraft NPCs, Java/Fabric): Phase 0 engineering only (2026-09-22). The first demo ("villager flees or calls a guard when attacked") is planned and not yet demonstrated. Worth watching; it is a proposal, not an application.
- **0x440-1me/laya-unity**: a Unity client SDK for `/v1/systemone` (MIT, v0.1, "not production-ready"). It is an integration, not a game. Its README example (NPC `attack`/`retreat`/`wait` choice) is illustrative only. Kept as an engine-integration reference in the README.
- **NobodyWho** (Godot GDExtension, llama.cpp, EUPL-1.2): local LLM runtime with grammar-constrained output and embeddings. It is a runtime, not a documented game decision mechanic. Kept as a Godot reference.
- **Inworld Goals and Actions** (intent detection from developer training phrases): mechanically very relevant (close), but the primary documentation redirected to a login page during this survey. Only search-engine snippets were available, so it is not included as an example.
- **NanoJev** (Maze/Snake/ViZDoom): a trained game-control model already covered in [open/nanojev.md](../open/nanojev.md). Not duplicated here. It is control by a trained head, which is far from jeff's zero-shot text classification.
- **Other Jev game bots** (Pong, Mario, Minecraft bots, other Tetris and chess repos, laya-vs-jev-arena, Pac-Man duel, jev-game-agent): same "model picks a game action" pattern as the shortlisted ones, with less documentation or no evaluation. Deduplicated in favor of the best-documented project per pattern.
- **Scaffold repos** with no description or no code calling a model (several `jev-game(s)` repos): excluded per the warning in [tooling-and-integrations.md](../ecosystem/tooling-and-integrations.md).
