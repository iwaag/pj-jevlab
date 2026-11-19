# NeMo Guardrails topical rails: LLM-based intent matching, accuracy on in-scope sets only

- **Sources:** https://arxiv.org/abs/2310.10501 ; PDF https://arxiv.org/pdf/2310.10501 (Rebedea et al., EMNLP 2023 demo), appendix on topical rails evaluation (accessed 2026-10-02; locator: Section 5.1, Appendix G.1, Tables 1-3, Figure 5)
- **Evidence type:** author/vendor evaluation (NVIDIA); toolkit paper
- **Model / base / checkpoint:** text-davinci-003, gpt-3.5-turbo, dolly-v2-3b, falcon-7b-instruct, llama2-13b-chat; user message mapped to a canonical form by retrieving k similar examples from a vector DB then prompting the LLM
- **Task:** match user utterance to a canonical intent: chit-chat (76 intents, 226 test) and banking (77 intents, 231 test); **metrics:** accuracy of user intent, bot intent, bot message; **rejection mechanism:** optional similarity threshold (0.6) matching vs exact match; out-of-scope inputs not part of the reported test sets

## What the source reports
- Banking user-intent accuracy (Table 3) with all examples: text-davinci-003 0.77 (0.82 with similarity), falcon-7b-instruct 0.70 (0.76), llama2-13b-chat 0.76, dolly-v2-3b 0.32 (0.62), gpt-3.5-turbo 0.38 (0.73); k=1 gives 0.50 and k=3 gives 0.65 for davinci.
- On chit-chat (Table 2) llama2-13b-chat 0.87, falcon-7b 0.81, davinci 0.89, with similar large gains from similarity matching for some models.

## Strength and caveats
- Supports: LLM + retrieved examples can classify canonical intents at 0.7-0.9, with a small open model within a few points of the larger ones when many examples are shown; the sensitivity to k and to the matching rule is large.
- Does not report rejection of off-topic input, false acceptance, or margins, so it cannot say "topical rails work" for out-of-scope text. Metric is in-scope only.
- Relevant local classes: L1; Q4.
