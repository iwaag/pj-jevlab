# Evidence cards: game theory, social choice, stochastic optimisation and learning (areas E and F)

Collected 2026-10-06 for [plan.md](../../../devdocs/episodes/study/statistically_correct/plan.md). Search record: [search-log.md](../search-log.md).

Conventions. **Source claim** = what the paper states or shows. **Lab observation** = anything from local Jev experiments (none are used in this file; no local data were consulted). **Inference** = my reading for transfer, always labelled. "Read in full/partly" says how much I verified from the PDF text (pdftotext); "abstract/search-summary only" means I did not open the full text and do not rely on its numbers. Access date for every URL: 2026-10-06. The 80-90% accuracy range from the brief is a scenario, not a result of any source below.

## 1. Cases at a glance

| ID | Case | Area | Mechanism supported | Verdict for noise/error |
|---|---|---|---|---|
| G-01 | Quantal response equilibrium (McKelvey-Palfrey; Goeree-Holt-Palfrey primer; Haile et al. critique) | E | Descriptive model of noisy choice in equilibrium | Noise is modelled, not shown beneficial; fit alone is uninformative |
| G-02 | Mutations and stochastic stability (Kandori-Mailath-Rob 1993) | E | Constructive variability (selection among equilibria) | Noise selects an equilibrium; selected one is not "best" in general |
| G-03 | Informational cascades (Bikhchandani-Hirshleifer-Welch 1992) | E | Failure case | Correct-on-average private signals still produce wrong collective lock-in |
| G-04 | Cascades in the laboratory (Anderson-Holt) | E | Failure case, empirical | Rational copying produced wrong cascades in human subjects |
| G-05 | Noisy voters as estimators (Conitzer-Sandholm; Caragiannis-Procaccia-Shah) | E | Absorption by aggregation | Positive, under independence and a stated noise model; rule-dependent |
| G-06 | Correlated votes and the jury theorem (Kaniovski 2008) | E | Failure/qualifier for G-05 | Positive correlation lowers group competence |
| G-07 | MusicLab (Salganik-Dodds-Watts 2006) | E | Unpredictability from social influence | Variability shown; benefit not shown |
| G-08 | Simulated annealing (Hajek 1988) | F | Constructive variability, with a schedule | Noise helps only with a cooling condition; guarantee is asymptotic |
| G-09 | Thompson sampling versus greedy and epsilon-greedy (Russo et al. tutorial) | F | Constructive variability (exploration) | Randomisation helps vs. no randomisation; structured beats uniform |
| G-10 | Stochastic resonance (Gammaitoni et al. 1998) | F | Constructive variability (physical) | Optimal noise level exists only with threshold + weak signal |
| G-11 | Gradient noise for very deep nets (Neelakantan et al.) | F | Constructive variability, empirical | Helps under poor init; null with good init |
| G-12 | SGD with noise escapes saddle points (Ge et al. 2015) | F | Constructive variability, theorem | Polynomial-time guarantee only for "strict saddle" functions |
| G-13 | Dropout (Srivastava et al. 2014) | F | Injected noise as regulariser | Better test error; 2-3x training cost; benefit is at training, not at deployment |

## 2. Cross-cutting findings

### 2.1 Positive results

- **Aggregation absorbs independent noise (G-05).** If each voter is a noisy view of a true ranking, with errors conditionally independent, the number of votes needed to recover the truth can grow only logarithmically in the number of alternatives for suitable rules (source claim, theorem under Mallows noise).
- **Noise as selection among equilibria (G-02).** Persistent small mutation can select one equilibrium of a coordination game; the selection is a property of the noise structure.
- **Noise with a schedule can reach global optima (G-08).** Simulated annealing converges in probability to a global minimum under a necessary and sufficient cooling condition (theorem, finite state space).
- **Randomised exploration beats none (G-09, G-11, G-12, G-13).** Compared with greedy action selection or noise-free training, randomisation improved regret or accuracy in the cited settings.
- **Noise can amplify a weak signal (G-10)** in threshold systems.

### 2.2 Negative and qualifying results

- **Cascades defeat "correct on average" signals (G-03, G-04).** Each private signal is right with probability p > 1/2, yet once actions coincide, later agents rationally ignore their own signal. The probability of the wrong cascade is "remarkably high" even for informative signals (BHW, Section II.A and Fig. 1). In the laboratory, 13 of 41 and 18 of 46 cascades in two designs were reverse (wrong) cascades (G-04, version-specific, see card).
- **The jury-theorem benefit is conditional on independence (G-06).** With positive correlation, group competence falls, and enlarging the jury can hurt up to a threshold size.
- **Stochastic-stability results can be slow and fine-print dependent (G-02).** The theorem concerns the limit of vanishing mutation; time to reach the selected state is a separate question (not verified here; see gaps).
- **Annealing noise needs a schedule (G-08).** Constant temperature does not yield the guarantee; a fixed noise level converges to a Gibbs distribution that only concentrates on minima as T goes to 0. The logarithmic-schedule constant must be at least the depth of the deepest non-global local minimum, which is generally unknown.
- **Gradient noise is not universally helpful (G-11).** With analytically derived good initialisation, noise gave no gain (97.4 vs 97.5 and 97.4 vs 97.2 best test accuracy), and a 5-layer net showed no improvement.
- **QRE fit is uninformative without restrictions (G-01).** Without distributional assumptions a QRE can match any behaviour distribution in any normal form game.
- **Variability is not benefit (G-07).** MusicLab shows more unpredictability and inequality under social influence; it does not show that outcomes were better or more enjoyable.
- **Training-time noise costs (G-13).** Dropout nets take 2-3 times longer to train.

### 2.3 Distinctions required by the plan

- **Factual voting versus preference aggregation.** Conitzer-Sandholm state both views in their introduction: view 1, idiosyncratic preferences with a compromise or welfare goal; view 2, a "correct" outcome of which votes are noisy estimates. Their results, and G-05/G-06, apply only to view 2. Arrow's impossibility concerns view 1 (axioms for aggregating genuine preferences); Caragiannis et al. note that axiom combinations are impossible [Arrow 1951] and use estimation as a competing approach. Nothing in this file justifies majority voting over conflicting interests.
- **Random noise versus structured error.** G-05 assumes conditional independence; G-06 shows what correlation does; G-03 is dependence through observed actions (sequential, shared information).
- **Local correctness versus global utility.** Cascades: each local decision is Bayes-rational yet the aggregate is wrong. QRE and stochastic stability: individual choice noise changes which collective state is selected.
- **Accuracy versus probability quality.** Softmax/logit choice (QRE, log-linear learning, Boltzmann exploration) presumes the scores are payoffs on a scale where the temperature has meaning. None of the sources shows that an LLM confidence is such a quantity. Argmax and sampling are different policies in G-09 (greedy versus Thompson).
- **Prediction versus simulation.** G-07 and G-04 are empirical studies of humans; G-03 and G-08 are mathematical models. None validates an artificial agent society as a predictor of a real one.

## 3. Case cards

### G-01 Quantal response equilibrium

1. **Source.** McKelvey and Palfrey (1995), "Quantal Response Equilibria for Normal Form Games", Games and Economic Behavior 10(1):6-38. https://www.sciencedirect.com/science/article/abs/pii/S0899825685710238 (abstract via search summary only; paper not opened). Read in part: Goeree, Holt, Palfrey (2018), "Stochastic Game Theory for Social Science: A Primer on Quantal Response Equilibrium", https://www.its.caltech.edu/~trp/QRE%20Primer.pdf (intro, Sections on matching pennies, minimum-effort game, summary). Critique read in part (abstract): Haile, Hortacsu, Kosenok (2003 Cowles DP 1432; AER 2008, 98(1):180-200), https://cowles.yale.edu/sites/default/files/2022-08/d1432.pdf.
2. **System / decision / objective.** Players in a matrix game. Each chooses an action with probability increasing in its expected payoff (smoothed best response); equilibrium requires beliefs to match the induced choice frequencies. The objective is descriptive: explain experimental play that departs from Nash.
3. **Error meaning and measurement.** Error is payoff-disturbance noise, i.i.d. in the standard form, with a precision parameter (logit lambda) estimated from data. Natural (human) noise, inferred by maximum likelihood. Source claim (primer): "standard (i.i.d.) error assumptions provide sharp, falsifiable predictions, even without specific distributional assumptions".
4. **Dependence.** Independent disturbances across decisions given payoffs; beliefs are equilibrium-consistent (shared through the fixed point). No temporal dependence in the static model.
5. **Mechanism.** Neither absorption nor correction. It is a model of how noisy individual choice shifts the equilibrium (steering of equilibrium by responses to payoff scale); some games are "pulled to the center", the minimum-effort game "to the extremes" (primer, Summary).
6. **Comparison and metrics.** Compared with Nash. Primer states the relative measure of QRE-consistent behaviour in a matching-pennies-type game is bounded above by 1/K! for K actions (as cited from Goeree et al. 2018). Effect sizes and uncertainty: unreported in what I read.
7. **Conditions and failure modes.** Source claim (HHK abstract): without a priori distributional assumptions a QRE can match any distribution of behaviour by each player in any normal form game, so fit alone is uninformative; empirical content comes from restricting the disturbance distribution and from reusing one precision across treatments (primer). Adding parameters for heterogeneity weakens content (primer).
8. **Evidence type.** Theory plus experimental fit; the primer is a review. Code/data: not checked. Conflict: the primer argues content exists, HHK show it is absent without restrictions; these are compatible (different assumption sets).
9. **Jev relevance.** Mechanistically analogous (inference). It is the closest game-theory formalisation of "sample an action from scores, with temperature". Missing for transfer: that a model's scores play the role of expected payoffs on a scale; that the precision parameter can be estimated for a model rather than for human subjects; no benefit claim.
10. **Cost.** Estimation requires choice data per game or treatment; no runtime cost.

### G-02 Mutations and stochastic stability

1. **Source.** Kandori, Mailath, Rob (1993), "Learning, Mutation, and Long Run Equilibria in Games", Econometrica 61(1):29-56. http://www.dklevine.com/archive/refs4500.pdf (read abstract and introduction; proofs not verified). Related, search-summary only, not opened: Young (1993) Econometrica 61(1):57-84; Blume (1993) Games and Economic Behavior 5(3):387-424 (log-linear/logit response, https://ideas.repec.org/a/eee/gamebe/v5y1993i3p387-424.html).
2. **System.** Finite population repeatedly playing a symmetric 2x2 coordination game; strategies grow with their current relative success, with ongoing random mutations. Collective objective: which equilibrium persists in the long run.
3. **Noise.** Mutations "can occur in every period"; injected in the model (exogenous probability); interpreted as experimentation or error.
4. **Dependence.** Mutations independent across agents and time; adjustment depends on the population state (state-dependent, shared through aggregate payoffs).
5. **Mechanism.** Constructive variability in the sense of equilibrium selection: noise "drastically reduce[s] the set of equilibria to ... long-run equilibria". For large populations the selected equilibrium satisfies Harsanyi-Selten risk dominance, and Pareto dominance when security levels are equal (abstract).
6. **Comparison.** Compared with the deterministic dynamic, which keeps all strict equilibria. Population size: large-population limit. Horizon: long-run (stationary distribution as mutation goes to 0). Effect sizes: not applicable (theorem).
7. **Conditions and failures.** Result is for 2x2 symmetric games with the stated dynamics. Selected state is risk dominant, which need not maximise welfare except in the equal-security case. How long convergence takes is a separate matter: I did not open a source on it. Ellison (1993) in the search results discusses finite horizons and local interaction; only its abstract-level search summary was seen.
8. **Evidence type.** Theorem. No data. No code. Replication: later literature (not checked).
9. **Jev relevance.** Mechanistically analogous only. It shows rare errors can decide among stable collective states, so "the error does not average away" can be a feature of the model. Missing: coordination-game structure; mutation as independent noise (LLM errors are likely not); the horizon.
10. **Cost.** None to run; the result concerns long horizons, which may be impractical (unverified).

### G-03 Informational cascades

1. **Source.** Bikhchandani, Hirshleifer, Welch (1992), "A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades", J. Political Economy 100(5):992-1026. https://snap.stanford.edu/class/cs224w-readings/bikhchandani92fads.pdf. Read: Section II.A, Fig. 1, Proposition 1 and footnote 16, parts of the fragility discussion.
2. **System.** Agents decide in sequence (adopt or reject), each with a private binary signal of accuracy p and observing all earlier decisions. Objective: collective choice of the correct action.
3. **Noise.** Private signal noise (probability 1-p of being wrong), natural/assumed. Signals are correct on average and informative.
4. **Dependence.** Signals conditionally independent given the true state; decisions depend on all earlier decisions (sequential shared information).
5. **Mechanism.** Failure mechanism. Once earlier actions create an imbalance, it is optimal to ignore one's own signal; the cascade stops information aggregation. Source claim: with more individuals the probability that a cascade starts approaches one (Prop. 1), and "even for very informative signals ... the probability of the wrong cascade is remarkably high"; footnote 16: it "can be close to .5 if the signal is noisy enough".
6. **Comparison.** The implicit comparison is aggregation of all private signals, which would converge to the truth. Metric: probability of a correct vs incorrect cascade as a function of p (graph; specific values unreported in text except the approximately 0.5 statement). Uncertainty: not applicable.
7. **Conditions and failures.** Cascades are fragile: new public information can break them (Section III); signal types and payoff structure matter; the paper presents hybrid-corn adoption and similar examples as illustrations only (anecdote-level in my read).
8. **Evidence type.** Theorem/model, plus anecdotal illustrations. No code. Experimental test: G-04.
9. **Jev relevance.** Directly analogous in structure if agents see each other's decisions in sequence: 300 agents, each 80-90% accurate (inference), could lock in. Mechanistically analogous; missing: whether Jev agents condition on peers' actions, whether they update as Bayesian agents, whether signals are independent given the state.
10. **Cost.** Mitigation cost (e.g., hiding others' choices, disclosing public information) not quantified in the source.

### G-04 Cascades in the laboratory

1. **Source.** Anderson and Holt (1997), "Information Cascades in the Laboratory", American Economic Review 87(5):847-862. PDF fetched: https://econweb.ucsd.edu/~jandreon/Econ264/papers/Holt%20Anderson%20AER%201997.pdf. Read: abstract, results on cascade formation and error counts. Caution: the file may be a working-paper or reprint layout (six sessions in the designs I read); numbers below are from that text only. A search summary quoted different totals (20 sessions); I did not verify those and do not use them.
2. **System.** Sequential prediction of which of two urns generated draws; each subject sees a private draw and earlier public predictions; paid for a correct guess.
3. **Noise.** Private draws are noisy evidence; decision errors also occur (source: about 4 percent of decisions inconsistent with both Bayes' rule and the private signal; 26 percent of cases where Bayes required ignoring the private signal, the subject followed it instead). Natural.
4. **Dependence.** Sequential, with public predictions; signals independent given the urn.
5. **Mechanism.** Failure mechanism, empirical, plus one correction mechanism: public draws can break a reverse cascade (the paper describes a reverse cascade broken by a subject acting on a private draw against the public pattern).
6. **Comparison.** Compared with Bayes prediction and a "follow your own signal" benchmark. Reported: cascades formed in 41 of 56 periods where they were possible (symmetric design) and 46 of 66 (asymmetric design); reverse cascades in 13 of 41 and 18 of 46 respectively; average actual efficiency 91.4 percent versus 72.1 percent for private-information-only (36 subjects). Uncertainty: unreported in what I read.
7. **Conditions and failures.** Subjects also used counting heuristics; the paper reports Bayes' rule and counting disagree in the asymmetric design and people were Bayesian half the time (41 of 82). Student subjects, small groups (six rounds).
8. **Evidence type.** Controlled laboratory experiment. Replication: later cascade experiments exist (not opened). Code/data: not checked.
9. **Jev relevance.** Mechanistically analogous; shows the failure appears with real, not only idealised, agents, including a share of reverse cascades. Missing: LLM agents' update rules; scale (300, not 6).
10. **Cost.** Not applicable.

### G-05 Noisy voters as estimators of a true ranking

1. **Source.** Conitzer and Sandholm (2005), "Common Voting Rules as Maximum Likelihood Estimators", UAI 2005. https://arxiv.org/pdf/1207.1368 (read abstract, introduction). Caragiannis, Procaccia, Shah (2016), "When Do Noisy Votes Reveal the Truth?", ACM TEAC 4(3):15 (EC 2013 preliminary). https://procaccia.info/wp-content/uploads/2016/03/samples.pdf (read abstract, Sections 1 to 1.2; theorems not verified).
2. **System.** A set of voters each submits a ranking that is a noisy estimate of a true outcome. Collective objective: recover the true winner or ranking.
3. **Noise.** The Mallows/Condorcet model: each pair ranked correctly with probability p > 1/2, independently; more general noise families tied to distance functions. Assumed (model-based).
4. **Dependence.** Votes independent given the true outcome (explicit condition in Conitzer-Sandholm: "we require that the votes are drawn independently given the correct outcome"; they also show that without this restriction all voting rules are MLEs).
5. **Mechanism.** Absorption by aggregation. Source claim: for pairwise-majority-consistent rules the sample count under Mallows noise is logarithmic in the number of alternatives (and in 1/epsilon), no rule can do asymptotically better, and plurality needs exponentially many samples.
6. **Comparison.** Across rules (Kemeny, PM-c rules vs plurality). Metric: samples needed for probability 1-epsilon. Population size: asymptotic. No experimental effect sizes. Uncertainty: not applicable.
7. **Conditions and failures.** Conitzer-Sandholm: only some common voting rules are MLEs of any independent noise model, and the sets differ for winner versus ranking outcomes. Rule choice matters enormously (plurality exponentially worse). Valid only where an objective truth exists ("especially sensible in contexts such as document selection").
8. **Evidence type.** Theorems. No code/data. Conflict: none found; the paper itself contrasts with the axiomatic (Arrow) route.
9. **Jev relevance.** Mechanistically analogous to factual voting only (village question with a true answer, not interest conflicts). Missing: independence of LLM-generated votes; a defined true ranking; pairwise-error model p > 1/2 for the actual errors.
10. **Cost.** Number of voters/queries scales as stated; each vote is a model call.

### G-06 Correlated votes and the Condorcet jury theorem

1. **Source.** Kaniovski (2008 draft), "Aggregation of Correlated Votes and Condorcet's Jury Theorem". https://serguei.kaniovski.wifo.ac.at/fileadmin/pdf/condorcet.pdf (read abstract and corollary statements; proofs not checked). Ladha (1992) AJPS 36:617-634 appeared in search results only (not opened).
2. **System.** Homogeneous jury of n voters with individual competence p, binary choice; objective: probability the majority is correct.
3. **Noise.** Individual error 1-p with a correlation structure between votes; parameterised, assumed.
4. **Dependence.** Explicit: correlation coefficient between votes.
5. **Mechanism.** Failure/qualifier of absorption. Source claim (abstract): negative correlation raises jury competence and positive correlation lowers it; with positive correlation an enlargement can be detrimental up to a certain size, beyond which it becomes beneficial; a second theorem identifies a family of distributions for which correlation has no effect.
6. **Comparison.** Independent votes. Metric: probability majority correct, with bounds (maximum and minimum for given competence and dependence). Values: unreported here (not extracted).
7. **Conditions and failures.** Results depend on the chosen dependence model (two different solutions to the aggregation problem are used); not all correlation structures give the same effect.
8. **Evidence type.** Theorem; draft, not peer-reviewed in the version read.
9. **Jev relevance.** Mechanistically analogous and directly relevant to plan question Q2/Q6 (same model repeated in many agents). Missing: an estimate of the actual correlation between model errors (inference: shared prompts or observations likely give positive correlation, unverified).
10. **Cost.** Not applicable.

### G-07 MusicLab: social influence and unpredictability

1. **Source.** Salganik, Dodds, Watts (2006), "Experimental Study of Inequality and Unpredictability in an Artificial Cultural Market", Science 311(5762):854-856. https://www.princeton.edu/~mjs3/salganik_dodds_watts06_full.pdf (read main text including Figs. 1 and 2 captions, no supplementary).
2. **System.** 14,341 participants downloading songs from 48 unknown bands, in an independent condition or in one of eight parallel "worlds" with visible download counts. Objective: understand how success in a cultural market arises.
3. **Noise.** Not injected; inherent unpredictability measured as the average pairwise difference in market share of a song across social-influence worlds, versus across random halves of the independent condition. Natural.
4. **Dependence.** Social influence worlds: later choices depend on earlier download counts (sequential shared information); independent condition: no sharing.
5. **Mechanism.** Variability generated by dependence (not by individual error). Source claim: social influence increased both inequality (Gini) and unpredictability; stronger influence (experiment 2) increased both further; quality (independent-condition share) was only partly predictive: "the best songs rarely did poorly, and the worst rarely did well, but any other result was possible".
6. **Comparison.** Independent versus social influence, experiment 1 versus 2. All differences reported significant (P < 0.01). Numerical Gini and unpredictability values are in figures, unreported in text.
7. **Conditions and failures.** The authors note the artificial market likely understates real-world influence; teen-oriented website sample; effect depends on how salient the social signal is.
8. **Evidence type.** Large controlled online experiment. Follow-up works (search hits: Salganik and Watts, arXiv 0912.5240; arXiv 1408.1542) not opened. Code/data: not checked.
9. **Jev relevance.** Mechanistically analogous: a population of agents that see others' choices produces different histories from the same start. That is variability, not benefit; whether it is entertaining or useful is not tested. Missing: any player-experience measure.
10. **Cost.** Large participant pool; multiple worlds required to observe unpredictability (a design cost, as one history shows none).

### G-08 Simulated annealing and the cooling condition

1. **Source.** Hajek (1988), "Cooling Schedules for Optimal Annealing", Mathematics of Operations Research 13(2):311-329. https://web.mit.edu/6.435/www/Hajek88.pdf (OCR text noisy; read abstract and Section 1; proofs not verified). Publisher page not accessible (HTTP 403). Hajek and Sasaki (1989) "Simulated annealing - to cool or not" was found in search only.
2. **System.** Minimise a function V on a finite state set with neighbour moves; a descent algorithm with random uphill moves accepted with probability exp(-delta/T). Objective: reach a global minimum.
3. **Noise.** Injected through the temperature T (controlled randomness), with T decreasing toward 0.
4. **Dependence.** Markov chain: next state depends on current state and temperature.
5. **Mechanism.** Constructive variability with an annealed amount. Source claim: a "simple necessary and sufficient condition on the cooling schedule" for convergence in probability to the set of global minima; for T(t) = c/log(1+t) the condition is that c be at least the depth of the deepest local minimum that is not a global minimum.
6. **Comparison.** Against pure descent (no uphill moves) and constant temperature. Section 1 shows that for constant T the chain converges to a Gibbs distribution that concentrates on minima only as T goes to 0. Metric: convergence in probability; no effect size.
7. **Conditions and failures.** Finite state space and a reachability ("weak reversibility"-type) assumption on the neighbour structure; the depth constant is problem specific and generally unknown to the user; the logarithmic schedule is slow (my inference from the form c/log t; the paper's abstract does not state runtime). Missing from my reading: finite-time performance.
8. **Evidence type.** Theorem. Practical performance evidence (Kirkpatrick et al. 1983) not opened in this search.
9. **Jev relevance.** Mechanistically analogous to temperature-controlled sampling. Key transferable point (inference): the benefit needs noise that is reduced over time and tuned to the landscape; a fixed 10-20 percent error rate corresponds to constant T, which has no such guarantee. Missing: a search landscape and an ability to lower the noise.
10. **Cost.** Many iterations; schedule tuning.

### G-09 Thompson sampling versus greedy and epsilon-greedy

1. **Source.** Russo, Van Roy, Kazerouni, Osband, Wen (2018/2020 v3), "A Tutorial on Thompson Sampling", Foundations and Trends in Machine Learning. https://arxiv.org/pdf/1707.02038 (read the greedy-decisions chapter, Figs. 3.1 and 3.2 description).
2. **System.** Online decision problem (three-armed Bernoulli bandit, theta = (0.9, 0.8, 0.7)); each period choose an action; objective: minimise regret versus the best action.
3. **Noise.** Randomised action selection injected by the algorithm (posterior sampling) or by epsilon dithering; reward noise is natural.
4. **Dependence.** Choices depend on the history through the posterior.
5. **Mechanism.** Constructive variability (exploration). Source claims: a greedy algorithm can fail to explore and lock onto a suboptimal action; epsilon-greedy "can improve behavior relative to a purely greedy approach" but "wastes resources" by giving equal trials to actions with no chance of being optimal; Thompson sampling's per-period regret vanishes over time while greedy's does not (Fig. 3.2, 10,000 simulations averaged).
6. **Comparison.** Greedy, epsilon-greedy, Thompson sampling; per-period regret; horizon about 1000 periods; 10,000 simulations. Numerical values appear only in plots; unreported in text. Uncertainty bands: unreported in what I read.
7. **Conditions and failures.** Result for a simple Bernoulli bandit with a well-specified prior; the tutorial states the comparison depends on theta (Fig. 3.2a vs 3.2b). The distinction between uniform random dithering and posterior-driven randomisation is the point: noise helps more when it is structured by uncertainty.
8. **Evidence type.** Controlled simulation and tutorial exposition; theory exists but was not read. Code: not checked.
9. **Jev relevance.** Mechanistically analogous to sampling from scores versus argmax; speculative for entertainment. Missing: reward signal and feedback loop; calibrated uncertainty (a model's reported confidence is not a posterior).
10. **Cost.** Needs a model of uncertainty and repeated trials.

### G-10 Stochastic resonance

1. **Source.** Gammaitoni, Hanggi, Jung, Marchesoni (1998), "Stochastic resonance", Reviews of Modern Physics 70(1):223-287. https://www.physik.uni-augsburg.de/theo1/hanggi/Papers/195.pdf (read abstract, Section I, grep of the rest; not read in full). The Augsburg opus link failed to download.
2. **System.** Nonlinear threshold or bistable systems (double well, neurons, lasers) driven by a weak periodic signal plus noise. Objective: signal transmission quality.
3. **Noise.** Inherent or added; thermal or external; measured through signal-to-noise ratio of the output as a function of noise strength.
4. **Dependence.** Noise is typically independent in time (white or coloured, per section); the signal is coherent and periodic.
5. **Mechanism.** Constructive variability in a physical sense: noise-induced hopping synchronises with the weak forcing when the mean waiting time is comparable to half the period; response peaks at an intermediate noise level.
6. **Comparison.** Zero-noise case, where a subthreshold signal is not transmitted; effect size depends on system (not summarised here).
7. **Conditions and failures.** Source claim: the effect "requires three basic ingredients": a threshold/barrier, a weak coherent input, and a noise source. The review also says the statistical synchronisation holds "only in the statistical average". Criticisms of the term and of information-theory measures (the review asks whether the effect can be characterised "by means of information theory concepts alone") were seen as questions in text; I did not extract a full list of controversies.
8. **Evidence type.** Review of theory, experiments and applications across fields. Replication: broad across physical systems.
9. **Jev relevance.** Speculative. The conditions are narrow (threshold plus subthreshold signal). Missing: any threshold element in a Jev decision whose subthreshold signal would be amplified by noise.
10. **Cost.** Noise must be tuned: too little or too much reduces performance (peak at an intermediate level).

### G-11 Gradient noise for very deep networks

1. **Source.** Neelakantan et al. (2015/ICLR 2016 submission), "Adding Gradient Noise Improves Learning for Very Deep Networks". https://arxiv.org/pdf/1511.06807 (read abstract, Sections 3-5, Tables 1 and 6).
2. **System.** Training of 20-layer MNIST networks, memory networks, Neural Programmer, Neural RAM, Neural GPU. Objective: lower training loss/error.
3. **Noise.** Injected annealed Gaussian noise on gradients, variance eta/(1+t)^0.55 with eta in {0.01, 0.3, 1.0}. The paper reports annealed noise works better than fixed variance (no table seen for this claim in the text read).
4. **Dependence.** Independent per step; schedule depends on time.
5. **Mechanism.** Constructive variability (escape from poor optimisation regions).
6. **Comparison.** Same runs without noise. MNIST 20-layer, 40 runs per row: Simple Init best/average 89.9/43.1 (no noise) vs 96.7/52.7 (noise); zero init 11.4/10.1 vs 94.5/49.7. Neural GPU, 7290 random trials, error below 1 percent: 28 successes without noise, 58 with noise. Abstract headline: 72 percent relative error reduction on a question-answering task (not verified at table level by me). Uncertainty intervals: unreported.
7. **Conditions and failures.** Source-reported nulls: with two analytically derived good initialisations noise gave 97.5 vs 97.4 and 97.2 vs 97.4 best accuracy (no gain); a 5-layer network showed no improvement; tuned gradient-clipping gave comparable accuracy without noise; authors conclude careful initialisation makes noise unnecessary for that problem. Dropout with the same setup gave 11.3 percent best accuracy (the table row labelled "No Noise + Dropout").
8. **Evidence type.** Empirical study with multiple seeds; preprint. Code: not checked. No independent replication read.
9. **Jev relevance.** Mechanistically analogous at most; the noise is on training, not on decisions in deployment. Missing: any analogue of optimisation landscape; the benefit depends on poor starting conditions.
10. **Cost.** Almost none; schedule and eta selection.

### G-12 SGD with noise escapes saddle points

1. **Source.** Ge, Huang, Jin, Yuan (2015), "Escaping From Saddle Points - Online Stochastic Gradient for Tensor Decomposition", COLT 2015. https://arxiv.org/pdf/1503.02101 (read abstract, intro, Section 3 statements; proofs not verified).
2. **System.** Non-convex optimisation (orthogonal tensor decomposition). Objective: reach a local minimum in polynomial time.
3. **Noise.** Added noise sampled uniformly from the unit sphere in the update; the authors state that if the stochastic gradient already has non-negligible variance in every direction, added noise is unnecessary.
4. **Dependence.** Independent per step.
5. **Mechanism.** Constructive variability (escape from saddles).
6. **Comparison.** Without noise, gradient descent can stall at saddles (stated; the analysis shows with high probability it cannot escape in the next polynomial number of iterations from a saddle start, Lemma 8 per the text). Result: with noise, a polynomial number of iterations, Otilde(eta^-2 log 1/zeta) as stated for small enough eta.
7. **Conditions and failures.** Applies to functions with the "strict saddle" property (a negative Hessian eigenvalue at every saddle, positive definiteness at local minima); the guarantee reaches a local minimum, not a global one, in general; the formulation of the tensor problem was redesigned to satisfy the property.
8. **Evidence type.** Theorem. No data replications.
9. **Jev relevance.** Speculative; included as the "noise helps escape saddles" case requested. Missing: optimisation objective.
10. **Cost.** Polynomial iterations; polynomial dependence on dimension.

### G-13 Dropout

1. **Source.** Srivastava, Hinton, Krizhevsky, Sutskever, Salakhutdinov (2014), JMLR 15:1929-1958. http://www.jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf (read abstract, MNIST results paragraph, discussion of training time).
2. **System.** Neural network training with random unit removal. Objective: reduce overfitting.
3. **Noise.** Injected unit-wise Bernoulli masking at training only; at test time the full network with scaled weights is used.
4. **Dependence.** Independent per unit and per training case.
5. **Mechanism.** Constructive variability, as regularisation (averaging over thinned networks).
6. **Comparison.** Same architecture without dropout. MNIST: a standard 2-layer net reaches 1.60 percent error, 1.35 percent with dropout, 1.25 with logistic units replaced, 1.06 with max-norm, down to 0.95 percent for a larger net (as read). Other datasets in the paper (CIFAR, TIMIT, ImageNet) not extracted. Uncertainty: unreported in the text read.
7. **Conditions and failures.** Source claim: 2-3 times longer to train; very noisy updates; a trade-off between overfitting and training time; benefits depend on dropout rate.
8. **Evidence type.** Empirical study across tasks; widely reused technique. Code: not checked.
9. **Jev relevance.** Weak: noise is used during training and removed at deployment, the opposite of a decision-time 10-20 percent error. Inference.
10. **Cost.** 2-3 times training time.

## 4. Gaps (areas without verified source in this file)

- Trembling-hand perfection (Selten) and noisy best response in evolutionary games beyond G-02: not searched at source level.
- Banerjee (1992) herding and Arrow's theorem primary text: not opened; the Arrow link is made only through Caragiannis et al. and Conitzer-Sandholm.
- Epsilon-greedy and Boltzmann exploration primary sources (Sutton-Barto; Auer et al.) and Bishop (1995) noise as regularisation: not retrieved. Evolutionary-algorithm mutation rate: only a search snippet (Doerr; "too-high mutation rate can lead to exponential runtime on OneMax"); not opened, no card.
- Kirkpatrick et al. (1983) and Hajek-Sasaki (1989): not opened. Stochastic resonance criticisms: not extracted from the review.
- Time to reach stochastically stable states (Ellison 1993): only a search-summary level; no number to use.
- Nothing here measures LLM-agent error dependence; all dependence statements are about the models in each paper.
