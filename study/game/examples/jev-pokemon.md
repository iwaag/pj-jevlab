# Jev Plays Pokémon Red (christianmat)

## Overview
A harness reads Pokémon Red's RAM in a Game Boy emulator and lists the legal options, each with facts (type matchups, damage estimates, distance to the objective). Jev picks one, and the harness turns it into button presses. The author reports that Jev finished the game in a live stream (2026-09-25 to 09-26).

## Relevance level
**Direct.** Hosted Jev via Vercel AI Gateway.

## Maturity / evidence
- A completed long run with a landing page (jev-pokemon.vercel.app, HTTP 200 on 2026-10-02). 116 stars; created 2026-09-25.
- **Documented, not inspected:** the numbers come from the README. The stream recording and the logs were not reviewed. Running it needs a user-supplied ROM.

## Game mechanic
A long-horizon agent playing a commercial RPG. The model makes the high-level and menu decisions, and the harness does pathfinding (A*) and the menu mechanics.

## Decision inputs and outputs
- **State:** map, party, battle state and on-screen text read from RAM, plus the current story milestone. Hidden items are not shown.
- **Options:** the legal choices in the current context, each with facts:
  - menu answers;
  - what to focus on (progress, heal, train, catch, shop, explore, team);
  - which Pokémon to catch or swap;
  - where to go and whom to talk to;
  - battle actions (move, switch, item, ball, run);
  - nicknames, spelled one letter at a time (A–Z or DONE).
- **Consumption:** the harness executes the choice. Loop protection tags options already tried without effect, samples an alternative if the same failing choice keeps returning, and as a last resort reloads the latest milestone checkpoint.

## Implementation / runtime
TypeScript and Node, with a Game Boy emulator, RAM addresses from the pret/pokered disassembly, and a local viewer. `JEV_MODE=mock` gives a free stand-in. Requests are throttled (300 ms minimum interval, 90 per minute).

## Availability and licenses
GPL-2.0 (code). No ROM is included. Jev is hosted and closed.

## Attributed results (author, README)
37 h 40 min total; 16,150 decisions; about 39.2 M input tokens; about $1.65 Jev cost; median decision time about 0.4 s; 16 team wipes (14 at the Elite Four); 15 Elite Four attempts.

## Possible jeff adaptation (inference)
This shows that a decision model can run a long game when the harness keeps each decision small and supplies the facts. A zero-shot encoder like jeff would probably need more harness help: Jev scores well above jeff on JevBench (75.3 vs 66.9 overall in v1.2.2; jeff reaches 37.7% on the hard tier, see [open/jeff.md](../../open/jeff.md)), and this game depends on many judgment calls. It is not a good first experiment for jeff, but the loop-protection design (tagging options already tried, sampling an alternative, reloading a checkpoint) is a reusable fallback pattern.

## Limitations
A single run, with no baseline comparison (for example, a scripted or random agent with the same harness). It is unclear how much of the success comes from the harness, the milestone knowledge and the loop protection rather than from the model.

## Sources (accessed 2026-10-02)
- https://github.com/christianmat/jev-pokemon (README, metadata)
- https://jev-pokemon.vercel.app (reachability check only)
