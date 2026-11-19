# jeff: reversing question order flips a choice answer (conformance-suite finding)

- **Sources:** https://github.com/logan-markewich/jeff/issues/4 (mandu5, 2026-09-24; accessed 2026-10-02); report https://github.com/mandu5/jevcompat/blob/main/results/jeff/report.md (accessed 2026-10-02; locator: order-sensitivity section). Also jeff issue #3 (maintainer comment 2026-09-21) for the maintainer's description of jeff.
- **Evidence type:** reproducible bug report; author independence: yes (conformance-suite author).
- **Model / base / checkpoint:** jeff at commit 34b32f9, server reports `gliformer-large-v1`; **size:** ~400M (listed on JevBench as GLiFormer 400M; not stated in issue #4); **architecture:** zero-shot GLiFormer wrapper with a shared encoder pass; **training:** none beyond the base model.
- **Task:** one support ticket with three questions (noul refund, choice team, score anger) sent in two orders; **options / readout:** Billing/Technical/Sales probabilities, temperature 3.2; **rejection mechanism:** none tested.
- **Data provenance:** author-written conformance case; **n:** 1 ticket x 2 orders x 3 repeats (the suite reports a mean shift of 0.417 on the Billing option, tolerance 0.050); **configuration:** M1 Pro; **raw cases available:** yes.
- **Fixed / mitigated?** Open as of access. The local project found `JEFF_ISOLATE=all` removes the effect; the issue does not mention it. **fix evaluated?** not in the issue.
- **Relevant local classes:** L7 (multi-question interference; this is the same shared-pass mechanism), L5 partly; Q8.

## What the source reports
- Same three questions, order refund/team/anger vs reversed: `team` Billing 0.768 vs 0.351 and Technical 0.142 vs 0.426; all repeats in each order identical, so not noise.
- `score` is computed before temperature scaling, so it disagrees with the returned probabilities (0.9973 vs 0.864).
- Suite result: 30/32 MUST and 11/14 SHOULD requirements met; label limit is 64 vs 255 promised; error body shape differs from the official server.
- The report does not test abstention or injection.

## Strength and caveats
- Independent confirmation of L7 on a second machine and a different case, but with n=1 ticket.
- Question order across a batch, not option order within a question, so it does not cover L5.
