# Semantris (Google Research, 2018)

## Overview
A word-association game by Google Research. The player types a word or phrase, and the game "ranks all of the words on-screen, scoring them based on how well they respond to what you typed." Well-matched words are cleared. It has two modes: Arcade (timed, encourages single words) and Blocks (untimed, invites phrases and sentences).

## Relevance level
**Close.** It uses semantic similarity and ranking (a dual-encoder model), not a Jev-style typed decision API. The core game rule is still "player text → rank a runtime-defined set of options".

## Maturity / evidence
- A released, publicly playable web game (research.google.com/semantris, HTTP 200 on 2026-10-02). Announced 2018-04-13.
- **Documented, not played** during this survey. The model description comes from the first-party blog and developer page.

## Game mechanic
The player's free text is the input, and an ML ranking over on-screen targets decides which targets are cleared. Associations, opposites and related concepts are all accepted.

## Decision inputs and outputs
- **Input:** the player's word or phrase.
- **Options:** the words currently on screen (hand-curated lists).
- **Output:** a relevance ranking or score per on-screen word. The game rules turn the ranking into clearing and scoring.

## Implementation / runtime
Google's developer page says the Universal Sentence Encoder is "very similar" to what Semantris uses, but Semantris uses "a dual-encoder approach that maximizes for response relevance". Where inference runs (in the browser or on a server) is not stated in the sources read.

## Availability and licenses
The game is free to play. Its source is not published. A related model is public: Universal Sentence Encoder on TF Hub (the license was not re-verified here).

## Attributed results
None published. Google notes that the word lists are "hand-curated and reviewed" to avoid unwanted associations, so content curation was part of the design.

## Possible jeff adaptation (inference)
- jeff can rank runtime options against a text input: the player's text becomes the state, and the on-screen words become `choice` criteria. Its probabilities would come from GLiFormer's label-versus-text scoring rather than embedding cosine similarity.
- This is the simplest mechanic to test in isolation: short inputs, short options, no long state.
- Differences to test:
  - jeff normalizes probabilities across options (they sum to 1), so it cannot directly say "nothing matches". A threshold or an explicit "none" option is needed.
  - jeff also takes per-request instructions, which can change the game rule (e.g. "pick the opposite").

## Limitations
A ranking game tolerates fuzzy answers, and players adapt to the model. Its success does not show that a model is accurate on rule-critical decisions.

## Sources (accessed 2026-10-02)
- https://research.google/blog/introducing-semantic-experiences-with-talk-to-books-and-semantris/ (2018-04-13)
- https://research.google.com/semanticexperiences/for-developers.html
- https://research.google.com/semantris/ (reachability check only)
- Universal Sentence Encoder, arXiv:1803.11175
