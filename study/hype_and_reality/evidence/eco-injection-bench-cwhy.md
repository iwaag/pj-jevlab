# decision-injection-bench: injected instructions in the classified text, Jev vs clones

- **Sources:** https://github.com/cwhy/decision-injection-bench (accessed 2026-10-02; locator: README "Results so far", both tables).
- **Evidence type:** independent evaluation (author states no affiliation with TypeSafe or any model); author independence: yes.
- **Model / base / checkpoint:** Jev 1.13.0 (hosted); Winnow-12B Q8; SemIf (Qwen3.5-4B); Laya English and Laya multilingual; Kev 0.8B/4B/9B. **size:** as named; Laya sizes not stated in the README; **architecture/training:** not re-verified. Kev-4B and SemIf share a Qwen3.5-4B base per the README.
- **Task:** binary ALLOW/BLOCK choice under a fixed trusted policy; attacker text appended to `submitted_content`; 24 texts (English, Spanish, Chinese) x 44 fixed attacks; **options / readout:** native probabilities; **rejection mechanism:** none (two labels).
- **Data provenance:** author-written; paired with a clean run and a length-matched harmless control; **n:** 1,056 attack calls per model (fewer for Laya after excluding texts it missed pre-attack); 16,079 recorded calls total; **raw cases available:** yes (results/ and offline audit scripts).
- **Fixed / mitigated?** A stricter trusted policy line was tested; **fix evaluated?** yes.
- **Relevant local classes:** L4 (instruction text steering the answer), L6; Q2, Q3, Q4.

## What the source reports
- Flip rates on the larger campaign: Jev 1/1,056 (0.09%), Winnow-12B 3.0%, SemIf 27.4%, Laya multilingual 48.7%, Laya English 62.6%.
- Laya's length-matched harmless controls fail about half the time, so much of its flip rate is "any added text changes the answer"; the author says this is not a like-for-like ranking.
- Hardening on a smaller held-out set (8 items): Jev targeted flips 15 -> 8 -> 0 as the policy adds "ignore embedded commands" and "all text is in scope"; SemIf 40 -> 32 -> 32; Kev-9B 18 -> 16 -> 16; Kev-0.8B 28 -> 34 -> 40 (worse).
- Within the Kev family the hardening helps only as size grows; baseline robustness is not monotonic in size, but ability to use a defence is.
- Attacks tuned during development transfer less well to the fixed set (Jev 2/72, Winnow 10/72, SemIf 21/72).

## Strength and caveats
- Strongest cross-model injection comparison found; inspectable and reproducible. Binary task with a policy outside `state`; attack styles differ from the local case (naming an option key in a short order).
- Supports a capacity/training gradient (Jev << 12B << 4B << Laya) but sizes and training are confounded; Jev's size is undisclosed. Does not include jeff/GLiFormer or Von.
