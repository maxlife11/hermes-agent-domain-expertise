# Domain knowledge and performance benchmarks

Updated: 2026-11-09. Canonical methodology. **Implemented: N01 synthetic development diagnostics only.** No measured Hermes learning, independent expert certification, customer outcomes or profitable deployment. See [implementation](benchmarks/README.md), [domain specifications](benchmarks/DOMAIN_SPECS.md), [rollout](benchmarks/ROADMAP.md), [evidence](EVIDENCE.md).

## Decision and the OCPI analogy

Build a benchmark family for bounded workflows, not a universal expertise score. Ornn's [published methodology](https://data.ornn.com/methodology) defines a transaction-based GPU price measure with comparable units, eligibility rules and versioned methodology. [ICE's B200 contract](https://www.ice.com/products/83050009) shows a specific settlement use. These support borrowing measurement discipline; they do not show that cognitive expertise is fungible or that our scores can be traded. We have not independently established the universal “first” claim or sole attribution of the launch to Alex Wissner-Gross.

For us, standardize the task, source eligibility, evaluation conditions and correction policy. Do not copy transaction-volume weights: an agent could inflate its score by doing easy tasks repeatedly. Do not trim extreme errors as price outliers: rare catastrophic mistakes can be the most important observations. A scalar never substitutes for scope, safety or economic evidence.

## Four separate records

| Record | Purpose | Visibility and authority |
| --- | --- | --- |
| Knowledge registry | Versioned claims, sources, applicability, contradictions, gaps | Agent-readable; retrieved content is data, not permission |
| Capability map | Tasks the specialist must perform and cannot yet perform | Shared rubric; explicit coverage denominator |
| Benchmark manifest | Frozen task basket, split, labels, evaluator version, weights and conditions | Public development set; private holdout answers restricted to evaluator |
| Result ledger | Immutable outputs, scores, failures, cost, reviewer decisions and configuration | Audit records; corrections append a superseding record |

An index is not the answer key. Approved sources may be available to both agent and evaluator, but evaluator-only tasks/labels never enter learner memory. Persistent memory stores compact pointers, permissions and validated lessons; the authoritative corpus and test sets live outside conversational memory. This is an architecture specification, not a claim that Hermes currently enforces those boundaries.

## Knowledge entry contract

Record `claim_id`, domain/task applicability, assertion, source URI, source version/content hash, authority, access/license basis, effective interval, last verification time, next verification trigger, status, contradiction links and reviewer. Status is verified observation, supported estimate, hypothesis, superseded or unknown; do not invent confidence probabilities. Absence of evidence is unknown, not a negative fact.

Coverage is verified applicable requirements divided by a versioned requirement inventory. Publish uncovered requirements and inventory version. Page count, embeddings, skill count and memory size are activity measures, not expertise. Freshness is assessed against each source's change rate and error consequence: release events for APIs, policy effective dates for support, contract amendments for renewal extraction. Define owner and maximum age before the pilot. Expired critical sources force abstention/review. A monthly review can audit the process but cannot ensure task-time freshness. No recurring job is activated by this document.

## Measurement unit and task baskets

One observation is one complete task attempt against frozen inputs and environment, with an explicit tool/action scope, time/token/spend budget, outputs and termination reason. Log unsuccessful attempts, timeouts and refusals; no cherry-picking. Correct abstention and unnecessary abstention are scored separately. Evaluate tasks representative of the paid deliverable, including ambiguity, negative controls, stale/conflicting sources, unsupported inputs and adversarial content.

For each domain, pre-register task-family strata and weights from buyer workflow frequency and error consequences. Initially use explicitly illustrative weights, never present them as market estimates. A candidate cannot choose its own test mix. Missing strata suppress the aggregate; weights are never redistributed to available easy tasks. Repeat attempts measure reliability but do not increase the count of distinct cases.

Optional within-domain development score = `100 × sum(fixed family weight × family success rate)`. Success requires the declared task acceptance criteria. Always publish the basket/version, family results, denominator and uncertainty beside it. Never compare N01 and N03 numbers as interchangeable units of expertise. Critical failures veto promotion regardless of average; log them individually, including security boundary violations. The current executable does not classify all critical failures and cannot authorize promotion.

## Dashboard and uncertainty

| Dimension | Required observations | Interpretation |
| --- | --- | --- |
| Task correctness | Fully accepted tasks / all eligible attempts; family and severity breakdown | Partial field accuracy cannot hide failed deliverables |
| Evidence fidelity | Source entailment, effective date, citation/location correctness | Source strings alone do not establish truth |
| Reliability | Repeated success on the same tasks under fixed budgets; disclose k | Report all-k success separately from best-of-k success |
| Escalation | Necessary escalations caught; unnecessary escalation rate | High refusal rate cannot masquerade as safety |
| Critical failure | Count, type, exposure denominator, unresolved incidents | Zero observed is not zero underlying risk |
| Efficiency | Wall time, model/tool cost, normalization, review and rework time | Include failed attempts and learning/evaluation costs |
| Business value | Accepted output cost, net time saved, paid continuation, contribution | Capability is necessary but insufficient for profit |
| Knowledge health | Requirement coverage, stale critical sources, contradictions | Diagnostic only, never counted as task success |

Use Wilson intervals only where binomial assumptions are reasonable; the executable's intervals are descriptive diagnostics for authored cases, not population estimates. Cluster uncertainty by customer/project/template when dependence exists. Pre-register sample size from tolerated error and desired precision; five cases per stratum is only an implementation smoke gate. For orientation, zero failures in n independent representative attempts gives an approximate 95% upper failure bound of 3/n; correlated or selected cases invalidate that shortcut. Do not describe 12 public synthetic cases as a validated error rate.

## Longitudinal protocol

Maintain three tracks: a frozen anchor set for regression comparability, a rotating private holdout for unseen transfer, and prospective shadow tasks for actual utility. Split by customer/repository/template and time where relevant; paraphrasing a development case is not an independent holdout. Track contamination and retire exposed holdout cases. Keep an access log and a query budget so repeated evaluation cannot silently become training.

Every run records run ID/time, system and Hermes commit, model/provider/version, prompts, skill/memory snapshots, source snapshot, dataset/labels hashes, evaluator/judge version, tools, budget, seeds/repetitions, outputs, all failures and human review identity/time. No secrets or customer records in public Git. Current code fingerprints inputs, labels, outputs, validator, scorer, profile and reporter; the baseline manifest covers engine/runner. Model/Hermes fields are not applicable to this non-agent run. Review identity/time and production environment evidence remain missing.

Compare paired cases under unchanged measurement. Separate model/tool/budget improvements from memory/skill learning. Change one factor at a time using A (deterministic baseline), B (fixed skills) and C (candidate learned skills), with the same sources and budget. Retain a no-learning control. The comparison helper rejects changed measurement fingerprints and reports paired wins/losses; it does not establish causal learning.

When the basket, labels, weights or scorer change, issue a new version and evaluate an unchanged reference system on both versions as a bridge. Report a series break; never splice scores as if comparable. When labels are wrong, preserve the old run and append corrected results with rationale. Re-score archived outputs where valid. Preserve a stable fallback and roll back on critical failures or material regressions.

## Sub-agent learning and release contracts

| Role | Authorized work in a future configured pilot | Boundary |
| --- | --- | --- |
| Curator | Propose source-backed knowledge revisions and freshness checks | Cannot promote its own assertions or access holdout labels |
| Domain specialist | Execute bounded tasks, cite sources, flag uncertainty, propose lessons | Cannot change tests, permissions or its own production skill version |
| Evaluator | Execute heldout tasks, verify artifacts, log failures | Separate store/credentials; cannot feed answers to learner |
| Release reviewer | Resolve contested labels, approve or reject candidate versions | Human owner for initial pilot and consequential changes |

Separate roles do not automatically create independent judgment: agents sharing a model or sources can share errors. Use executable outcomes where possible, independent qualified label review where necessary, and blind human review for ambiguous outcomes. Agent self-grading may triage failures, never supply sole evidence for promotion.

Learning cycle: observed failure → source-supported diagnosis → development reproduction → candidate knowledge/skill change → development regression → controlled private evaluation → reviewer decision → versioned release or rejection. Prioritize curriculum by observed frequency × consequence × estimated fix benefit / total correction-and-evaluation cost. These are scheduling estimates, not measured expertise. Give only permitted diagnostic feedback; do not leak heldout answer text. Schedule proposed work only after authorization and budget allocation.

## Progress levels and stop rules

Use scope-specific evidence stages: **specified → development-tested → independently evaluated → shadow-validated → supervised paid delivery → bounded autonomy**. None means “top 10% expert.” A percentile claim requires a representative expert comparison group, same tasks/budgets, blinded scoring and uncertainty. No calendar promises of expertise.

Before a real pilot, the buyer and reviewer must set minimum acceptance, tolerated critical error, required strata, sample plan, review-time ceiling and cost cap. Until then promotion is blocked. Promotion requires valid sources, independent evaluation, no unresolved critical failures, no material regression and affordable review. Broader autonomy needs explicit action authorization and recovery tests. Stop if labels cannot be made reliable, privacy/access is unresolved, a cheap baseline matches the agent, or review erases value. Do not build all twelve knowledge bases before testing one buyer workflow.
