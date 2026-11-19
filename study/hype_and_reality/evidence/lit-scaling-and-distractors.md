# Scaling evidence and irrelevant-context sensitivity (L6, Q1, Q8)

- **Sources:** https://arxiv.org/abs/2302.00093 (Shi et al., ICML 2023, GSM-IC); https://arxiv.org/abs/2306.09479 (McKenzie et al., Inverse Scaling Prize, TMLR 2023); https://arxiv.org/abs/2211.02011 (Wei et al., "Inverse scaling can become U-shaped", from search listing only); https://arxiv.org/abs/2603.11991 (BTZSC benchmark, Aarab) (accessed 2026-10-02; abstract-level or WebFetch summary)
- **Evidence type:** peer-reviewed/preprint paper; author independence: yes
- **Model / base / checkpoint:** GSM-IC: code-davinci/GPT-3.5-class models (exact list not extracted; unknown); Inverse Scaling Prize: multiple LM families (unknown from fetch); BTZSC: DeBERTaV3, ModernBERT cross-encoders, E5/GTE/BGE embedders, rerankers, LLMs (Gemma, Llama, Mistral, Qwen, Phi); **size:** unknown (not extracted)
- **Task:** arithmetic with irrelevant sentences; 11 inverse-scaling tasks; zero-shot text classification benchmark; **language:** English (BTZSC mainly English); **rejection mechanism:** none
- **Metrics:** accuracy; **raw cases available:** public benchmarks
- **Fixed / mitigated?** GSM-IC: self-consistency and an instruction to ignore irrelevant information; **fix evaluated?** yes
- **Relevant local classes:** L6, L2, Q1, Q8

## What the source reports
- Shi et al.: model performance drops dramatically when irrelevant information is added to problems; self-consistency and explicit "ignore irrelevant info" instructions help. Establishes distractor sensitivity in prompted LMs; sizes not extracted.
- McKenzie et al.: 11 tasks show worse performance with scale, attributed to memorized-sequence preference, imitation of undesirable patterns, easy distractor tasks, and misleading demonstrations; some trends are U-shaped. The "easy distractor task" cause is the nearest analogue to a neighbour-option substitution but is a hypothesis, not proof for L3.
- Wei et al. (search listing): two of four tasks become U-shaped with larger models, and chain-of-thought flips the rest; scaling trends are therefore prompt dependent.
- BTZSC: reports that larger models generally do better in zero-shot classification and that cross-encoders beat embedding models; it is an accuracy benchmark with no OOS/none test (per fetched summary).

## Strength and caveats
- Gives a prior that both "bigger helps" (BTZSC accuracy) and "bigger does not help or reverses" (inverse scaling) occur, so Q1 must be tested directly.
- GSM-IC concerns math word problems and large LMs, not 400M encoders with extra state lines; it supports L6 only as a general phenomenon.
- I did not find a within-family size sweep of a GLiClass/GLiFormer-style encoder; this is a gap.
