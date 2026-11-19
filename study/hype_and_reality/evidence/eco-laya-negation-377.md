# Laya: negated instructions answered with the action they negate (issue #377)

- **Sources:** https://github.com/NandhaKishorM/laya/issues/377 (accessed 2026-10-02; locator: reproduction table; comments by NandhaKishorM 2026-09-24, syncword 2026-09-25, paulocarinhena 2026-09-26). README change via PR #385 (title only seen).
- **Evidence type:** reproducible bug report; author independence: yes (PerryLink, syncword, paulocarinhena are third parties; maintainer replies).
- **Model / base / checkpoint:** `laya` (English, 421M per issue #450) and `laya-multilingual`, laya 0.3.20; **size:** 421M English (stated in issue #450), multilingual 321.9M (HF discussion #3); **architecture/training:** unknown here.
- **Task:** forced choice between two semantic keys (`no_action` / `cancel_account`) and operation-style keys (refund/delete/lock); **input language:** English; **readout:** native choice probability; **rejection mechanism:** none beyond the keys written.
- **Data provenance:** hand-written minimal pairs; **n:** 5 states (PerryLink) + 4 verb rows (syncword) + domain minimal pairs (paulocarinhena, not read in full); **raw cases available:** yes (in the issue body).
- **Fixed / mitigated?** Documented as a limit in the README ("review step for irreversible actions"); maintainer says it is a model limitation. **fix evaluated?** no.
- **Relevant local classes:** L3-like (lexical match to the action named in the text), L4; Q2, Q3.

## What the source reports
- "do NOT cancel" style states: English checkpoint wrong on 4 of 5, multilingual on 2 of 5; the multilingual worst case is cancel_account at 0.9998, so a confidence gate would not catch it.
- Using semantic rather than boolean keys (the README workaround) did not avoid it.
- syncword reproduced with operation-style keys: "Please do NOT refund my charge" answered refund_charge at 0.9675; "do NOT lock" passed, so it depends on key/verb.
- Maintainer's advice: validate negated wording yourself and put irreversible actions behind review.

## Strength and caveats
- Very small hand-written sets, but they are inspectable minimal pairs and reproduced by two independent authors.
- Closest external analogue to local L4: the text names an action and the model picks that action. Here the cause is negation, not an override instruction, and key text was semantic; it does not show key-string leakage.
