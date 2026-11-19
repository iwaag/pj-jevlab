# Laya intent router (150M): trained "none" option, author-reported OOS recall and its stated limits

- **Sources:** https://github.com/vrajnotviraj/laya-intent-router README (created 2026-09-28; author vrajnotviraj) (accessed 2026-10-02; locators: top example block, "Results: 94.9% routing accuracy, 98.6% out-of-scope recall", "How it was made", "Where it slips"); original Laya referenced at https://huggingface.co/convaiinnovations/laya (not re-checked)
- **Evidence type:** author evaluation (single developer, a Jev-like/Laya derivative); author independence: not independent of the model; independent of TypeSafe
- **Model / base / checkpoint:** Ettin-encoder-150M distilled from a ModernBERT-large "Laya-large" teacher with a decision head; **size:** 150M (README); **architecture:** encoder + 2 extra transformer layers + per-intent [MASK] scorer, temperature per menu size; **training:** about 122k routing episodes from 7 public intent datasets plus 76 synthetic workflows; about 40% of episodes had the right intent removed, to teach "none"
- **Task:** zero-shot routing of short English customer messages over user-supplied intent lists, or none; **options / readout:** intent score, threshold 0.625; **rejection mechanism:** explicit `__none__` option trained with removed-gold episodes plus threshold
- **Data provenance:** 1,636 hand-written messages across 10 setups incl. adversarial near-duplicates/typos; insurance and telecom unseen in training; **caveat stated by author:** test messages written by the same process as synthetic training data; **metrics:** routing accuracy, OOS recall, wrongly-accepts-OOS; **raw cases available:** unknown (training/ scripts in repo, not inspected)

## What the source reports
- Original zero-shot Laya: routing 0.728, catches OOS 0.682 (wrongly accepts 31.8%); the author's concrete example is nonsense `qwewqeqw` routed to `order_not_received` at 0.73.
- Distilled 150M model: routing 0.949, catches OOS 0.986 (wrongly accepts 1.4%); teacher 0.950 / 0.959. New domains 0.920 (original 0.777). Big menus (20-45) 0.943.
- Weak spots stated: filler words ("ok", "nice") landing on a bye intent when the menu has only 2 intents; indirect requests and heavy typos (~0.83-0.86); intents match only the phrasings given.

## Strength and caveats
- Suggests: training with explicit episodes where the right option is absent is associated with a large OOS-rejection gain at the same model family (the conditions that made rejection work), and small menus remain risky.
- Not verified independently; same-process test data; one week old; unknown whether OOS test includes small talk or instruction-override text; the repo does not report option-order or key-name sensitivity.
- Relevant local classes: L2, L3 (removed-gold episodes are exactly the unavailable-job case), L5 unknown; Q3, Q5, Q6.
