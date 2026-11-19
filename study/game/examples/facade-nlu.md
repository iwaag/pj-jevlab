# Façade natural-language understanding (Mateas & Stern, 2005 game; NLU paper 2004)

## Overview
Façade is a released one-act interactive drama. The player visits a married couple, Grace and Trip, and types free text. Its NLU maps any player utterance onto a small set of **discourse acts** (24 parameterized act types in the paper's Table 1; the authors' other papers say "approximately 30"), and a second phase chooses the characters' reactions given the current dramatic beat. It is the classic precedent for "player text → small runtime label set → authored reaction", built with hand-written rules instead of a model.

## Relevance level
**Close.** It classifies player text into labels that drive game behavior. The classifier is a forward-chaining rule system, not a learned model.

## Maturity / evidence
- A released game (playable distributions are linked from playablstudios.com/facade, HTTP 200 on 2026-10-02) and a peer-reviewed paper.
- **Inspected:** pages 1–6 of the TIDSE 2004 paper (PDF). The game was not played.

## Game mechanic
Conversational drama. The player's utterance (agree, criticize, flirt, praise, refer to an object, etc.) changes the characters' reactions and the drama manager's beat sequencing.

## Decision inputs and outputs
- **Phase 1 (NLU):** surface text → one or more discourse acts. "A strong many-to-few mapping", which "ignor[es] any nuance in the tone" and focuses on pragmatics.
- **Examples of acts:** `DAAgree`, `DADisagree`, `DAPraise`, `DACriticize ?level` (light or harsh), `DAFlirt`, `DAApologize`, `DAReferTo ?obj` (couch, wedding picture, paintings), `DAExplain`, `DAAdvice`, `DAGoodbye`, `DAInappropriate`, `DAMisc ?type` (beat-specific, e.g. "ask for drink").
- **Catch-all:** `DASystemCannotUnderstand`.
- **Phase 2 (reaction):** in context, it determines "what effect this act will have". Collections of phase-1 rules can be turned on or off per context.
- **Rule language:** a custom template language compiled to Jess, using regular expressions, order-free occurrence tests (`tand`, `tor`, `toc`, `tnot`), WordNet expansion and stemming.

## Implementation / runtime
Hand-authored rules ("hundreds" per the authors' related papers), with no learned model. The game runs locally.

## Availability and licenses
The game is a free download. Source and license were not checked.

## Attributed results
The pages read contain no quantitative evaluation of the NLU.

## Possible jeff adaptation (inference)
- jeff could take the role of Phase 1: player text → `choice` over the discourse acts allowed in the current beat, with code-defined options as Façade's rule collections are. This is the same idea as the gate guard's action `choice`, but with the label set placed *before* the reaction rules rather than choosing the reaction directly.
- Façade's explicit `DASystemCannotUnderstand` catch-all points to a design question for jeff. The catch-all could be an explicit option, or the game could apply a confidence threshold. Both need testing.
- Façade parameterizes acts with a character and a level, which jeff can express as extra `choice` questions in the same request (who is addressed, how harsh).

## Limitations
Rules were authored per beat with heavy effort, and its known failure mode is misunderstanding the player. A zero-shot model would remove the per-phrase authoring but bring its own unpredictable errors.

## Sources (accessed 2026-10-02)
- M. Mateas, A. Stern, "Natural Language Understanding in Façade: Surface-text Processing", TIDSE 2004. https://eis.ucsc.edu/papers/MateasSternTIDSE04.pdf ; https://link.springer.com/chapter/10.1007/978-3-540-27797-2_2
- https://www.playablstudios.com/facade (reachability check only)
