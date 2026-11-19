# jevlab: literature surveys on Jev-style decision models

Jev (TypeSafe AI, launched 2026-09-15) takes unstructured text plus typed questions (yes/no, choice, score) and returns typed answers with probabilities in one pass. Many open clones followed within days. This repository holds the literature surveys one lab compiled about Jev and Jev-like models, benchmarking, prompting and collective decision making.

## Start here

[`study/README.md`](study/README.md) is the index: a taxonomy of Jev-likes (classes A–G), per-project notes, and the key findings. Each subfolder (`hype_and_reality`, `benchmark`, `prompt_best_practice`, `statistically_correct`, `schooling_sim`, `recent_study`, `recent_study_p3`, `ecosystem`, `landscape`, `open`, `close`, `game`) has its own README or file list.

## How to read the evidence

- The surveys were compiled from web sources (vendor pages, READMEs, model cards, blogs, third-party evaluations, arXiv papers), with the survey date stated in each README. Sources move; links and numbers may have changed since.
- Each file separates what a source *claims* from what was independently *measured*. Treat unlabelled numbers as claims.
- Statements labelled **Local** report the lab's own measurements; those experiments and their data are **not** in this repository.
- Some classic paper IDs in `study/landscape/` were written from memory and are marked as such: verify before citing.

## What is not here

The lab's experiments, benchmark harness, replay viewer and run/episode records are not published (yet). Many surveys link to them with relative paths such as `../../devdocs/…` or `../../lab/…`; those links do not resolve in this repository. They are provenance pointers, not required reading.

## Licence

[CC0 1.0](LICENSE): the surveys are dedicated to the public domain. Third-party works they cite keep their own licences; the surveys summarise and link to them rather than reproduce them.
