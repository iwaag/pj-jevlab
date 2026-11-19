# JEV Chess decision core (sliday/jev-chess-algo, jevchess.com)

## Overview
[jevchess.com](https://jevchess.com) is a shared online board: Jev plays one side and visitors play the other. The repo extracts its decision core. Every legal move becomes an option of one typed `choice` question, and the move description is computed by code (including a hanging-piece check), so the model never does arithmetic.

## Relevance level
**Direct.** Hosted Jev via OpenRouter's Decisions endpoint (`~typesafe/jev-latest`).

## Maturity / evidence
- A live web game (HTTP 200 on 2026-10-02) plus an extracted, tested decision core (`npm test`: 19 tests; `npm run demo` prints the request without a key). Created 2026-09-21; 2 stars.
- **Inspected:** README. **Not inspected:** the live site's decision logs; no game was played.

## Game mechanic
Opponent AI for a turn-based board game. Illegal moves are **unrepresentable**: the option list is the legal move list, so there is no parse, validate or retry loop.

## Decision inputs and outputs
- **State:** a prose position summary written for the side to move ("YOU ARE PLAYING WHITE…"), FEN, an ASCII board, material, check status, counts of safe moves, and an explicit "CHECKMATE IS AVAILABLE" line when there is one.
- **Options:** every legal move keyed by SAN, each with a plain-language description from the exchange analysis, for example "…leaving you 3 points down overall, a serious blunder". Blunders are never pruned from the list.
- **Questions:** `best_move` (`choice`), plus king safety, plan, sharpness and a second move question used as a tiebreak, all in the same request.
- **Consumption:** the chosen SAN is played directly. The live site shows the probability distribution over moves and keeps a calibration record.

## Implementation / runtime
TypeScript with chess.js. The live game runs on Cloudflare Durable Objects. Moving from building a new board per lookahead level to `move`/`undo` on one board cut the analysis from 1,029 ms to 365 ms.

## Availability and licenses
MIT (code). Jev is hosted and closed.

## Attributed results (author)
- In six lost games (190 Jev moves), Jev played a move described as losing 3+ points only once while a safe move was available.
- In quiet positions, about 51% of legal moves had identical descriptions. The author concludes the model "was being outplayed slowly" because the descriptions did not tell the options apart. The live game now adds threat and king-pressure facts.
- The author describes a bug: an exchange check that stopped after one recapture made the state misleading, and Jev lost a piece. The lesson: the model is only as good as the facts the code writes.
- No playing strength (Elo) is published.

## Possible jeff adaptation (inference)
The pattern carries over directly: legal options computed by code, described by code, and chosen by the model. Two points need testing with jeff: whether it can choose well among dozens of near-identical descriptions (GLiFormer scores labels against text, which suits short, distinct labels), and how its accuracy drops as the number of options grows.

## Limitations
The evidence is anecdotal, from the author's game analysis. There is no strength benchmark, and calibration is claimed but not published in the repo.

## Sources (accessed 2026-10-02)
- https://github.com/sliday/jev-chess-algo (README)
- https://jevchess.com (reachability check only)
