# Phase 4 — Conditional Validation and Implementation Plan

Updated: 2026-11-05. Status: offline technical baseline completed; customer and Hermes work pending. No jobs scheduled, outreach sent, integrations connected or agent deployed.

## Commit in stages

The initial contract-review SaaS winner and fixed build sequence are withdrawn. Begin with a two-week validation stage. The remaining 90-day outline is conditional on buyer, data, quality and economic evidence. The earlier $3,000/month budget and solo-founder assumptions are not confirmed operating constraints.

Before spending or provisioning, establish available operator hours, budget, customer access, reviewer availability, jurisdiction, data restrictions and target time to revenue. Do not assume access to legal expertise, customer records or enterprise procurement.

## Days 1–14: select a testable offer

| Window | Work and owner role | Deliverable | Gate |
| --- | --- | --- | --- |
| Days 1–2 | Operator defines constraints and evidence gaps | Constraint sheet and comparison of N01/N02/N03 | No invented buyer access or budget |
| Days 3–5 | Operator conducts authorized buyer discovery; reviewer assesses sample scope | Proposed target: 5–8 relevant conversations, if reachable; objections and sample permissions recorded | Evidence of a recurring problem and a purchasing path |
| Days 6–9 | Builder and reviewer prepare representative tasks and simple baseline | Proposed 30–50-case starter set, labeled development/held-out split, baseline costs | Reliable labels and affordable review |
| Days 10–12 | Builder compares A and B from Phase 2 | Accepted sample deliverables, failures, costs and time including review | Hermes adds value or a simpler alternative is selected |
| Days 13–14 | Operator evaluates a scoped paid pilot offer | Buyer response, price hypothesis, deliverable limits and go/no-go record | Concrete demand, manageable scope and plausible economics |

These quantities and dates are planning targets, not observed results or statistical guarantees. Obtain permission before outreach or handling nonpublic data. If buyer access takes longer, extend discovery or stop; do not treat the calendar as evidence.

Do not build multi-platform gateways, a marketplace, generic memory infrastructure or broad SaaS billing before proving the workflow needs them.

## Conditional days 15–90

| Stage | Deliverables | Dependencies | Pass evidence | Stop or narrow when |
| --- | --- | --- | --- | --- |
| Days 15–30: assisted pilot | Pinned runtime/model, minimum integrations, reviewed skills, logs, scoped output | Data permission, buyer agreement, reviewer and budget | Buyer accepts useful work; major costs measured | Critical errors cannot be reviewed affordably or access fails |
| Days 31–60: repeatability | Multiple batches, exception handling, cost accounting, optional C experiment | Continued demand and stable baseline | Repeated accepted delivery and improvement beyond B if C is pursued | Rework grows, margins remain negative, or learning regresses |
| Days 61–90: productization decision | Standard onboarding, support limits, release/rollback process and acquisition results | Repeatable positive contribution and buyer continuation | Evidence supports scaling, a bounded managed service, or a narrow software product | Sales or delivery depends on unsustainable bespoke effort |

Estimate effort and spend after the first sample: operator hours, reviewer hours, annotation effort, inference/API usage, integration work and fixed costs. Attach downside/base/upside estimates using Phase 3. Do not fill this plan with arbitrary costs before those inputs exist.

## Minimum implementation specification

This remains the proposed runtime specification. A subset now exists as an offline baseline: normalized-input validation, immutable run directories, provenance hashes, reviewer packets and deterministic scoring. No verified Hermes configuration or production release exists.

- One tenant-scoped agent profile and a pinned model/provider.
- Versioned input schema, permitted source corpus and deterministic output validation.
- Minimal authorized read tools; draft outputs by default.
- Durable job IDs, idempotency controls, bounded retries and status records.
- Source-linked outputs and reviewer decisions.
- Evaluation harness with baseline conditions A/B/C and protected expected answers.
- Release manifest: runtime commit/tag, model version, skill versions, data versions, evaluation results and reviewer approval.
- Operational logs, per-job spend limits, kill switch and rollback to the previous approved skill release.

Revalidate the selected Hermes release's features and tool permissions before implementing. No invented configuration keys or commands are provided here.

## Initial skill seeding

Seed the three narrow skills for the selected candidate from Phase 2 with reviewer-approved procedures and representative examples. Keep facts with sources and effective dates; keep personal preferences separate. Do not use a random document count as a proxy for coverage.

Each skill should specify trigger, input schema, scope, procedure, approved tools, output schema, evidence requirements, validators, failure modes and escalation. The first release remains fixed while the baseline is evaluated.

## Proposed jobs, not activated schedules

| Trigger/cadence | Purpose | Output and gate | Cost control |
| --- | --- | --- | --- |
| Authorized new input | Execute the approved workflow | Validated draft or explicit escalation | Per-job tool, token, time and retry limits |
| Daily during an active pilot | Summarize failures and review load | Metrics only; no automatic production skill changes | Aggregate existing logs rather than rereading all sources |
| Weekly, if enough new evidence exists | Review error clusters and candidate changes | Development experiment; independent evaluation before promotion | Batch evaluations and stop low-value experiments |
| Source version change | Detect potentially stale references | Revalidation task and affected-skill list | Monitor defined sources, not unrestricted browsing |
| Approved release | Promote evaluated skills | Version manifest and rollback checkpoint | Bounded rollout and review |
| Critical incident or budget breach | Suspend affected action | Incident record and human decision | Kill switch and limited diagnostics |

A cadence does not create useful feedback. Skip jobs whose expected value is below their cost or that have no new evidence.

## Sample operating charter

- Objective: produce the selected workflow's accepted deliverable within buyer-defined quality, cost and time limits.
- Inputs: only authorized sources and the minimum customer data needed.
- Permitted actions: retrieve, analyze, validate and create drafts in designated locations.
- Approval required: publication, merges, customer messages, reminders, contractual notices, production changes and any expanded access.
- Excluded actions: autonomous professional determinations, payments and unsupported customer commitments.
- Learning: propose changes in an isolated candidate version; do not modify production skills or approval rules.
- Budget: enforce operator-approved per-job and period caps before execution. Values remain unset until approved.
- Escalation: missing/conflicting evidence, critical ambiguity, permission failure, unfamiliar action or exceeded limits.
- Completion: return evidence, validation status, unresolved issues and actual usage.
- Recovery: stop, preserve permitted audit evidence, and restore the last approved release when directed.

For N03, require reviewer approval of dates, notice conditions, amendment precedence and any proposed reminders. Initial scope excludes sending notices or deciding legal risk.

## First three experiments

| Experiment | Procedure | Proposed pass/fail rule |
| --- | --- | --- |
| Demand | Present a bounded sample and scoped offer to reachable relevant buyers | Pass with a paid pilot or concrete purchasing commitment and permitted task access; interest alone is inconclusive |
| Delivery | Compare A and B on representative held-out tasks with independent review | Pass chosen workflow only if quality fits agreed limits and fully costed delivery supports the offered price; target net time saving set in advance |
| Learning | Compare candidate C with frozen B, including annotation/evaluation costs | Promote only for predeclared held-out gains without critical regressions and with credible cost recovery over expected reuse |

Experiments may fail. Preserve negative results and change the offer or method accordingly. Do not tune thresholds after seeing results to manufacture a pass.

## Decision dashboard

Track sampled cases and time period; accepted/rejected outputs; critical and noncritical errors; review and rework minutes; escalation precision/recall where labeled; tool failures; cost per accepted unit; contribution per customer; pilot conversion and continuation.

Separate leading indicators from realized revenue and retention. Include a reason for every stage transition. Readiness is a documented evidence decision, not a date.

## Domain Knowledge Index Creation and Monitoring Step

### Added Step for Implementation Plan
After initial skill seeding and before the first controlled learning loop run, create and monitor a domain knowledge index per candidate:

1. **Create per-domain index**: For N01–N12, build an index entry cataloging key facts, sources, effective dates, confidence levels, covered subtopics, and gaps.
2. **Monitor per-domain index**: Schedule recurring checks to track source freshness, coverage completeness, gap emergence, and accuracy decay.
3. **Integrate into controlled improvement loop**: Index updates feed smallest-relevant-skill changes; index health metrics feed evaluation dimensions.
4. **Approval boundary**: Index additions are operator-approved for production; candidate/experimental indexes remain uninstalled skills.

### Days 1–14: select testable offer
| Window | Work and owner role | Deliverable | Gate |
| --- | --- | --- | --- |
| Days 1–2 | Operator defines constraints and evidence gaps | Constraint sheet and comparison of N01/N02/N03 | No invented buyer access or budget |
| Days 3–5 | Operator conducts authorized buyer discovery; reviewer assesses sample scope | Proposed target: 5–8 relevant conversations, if reachable; objections and sample permissions recorded | Evidence of a recurring problem and a purchasing path |
| Days 6–9 | Builder and reviewer prepare representative tasks and simple baseline | Proposed 30–50-case starter set, labeled development/held-out split, baseline costs | Reliable labels and affordable review |
| Days 10–12 | Builder compares A and B from Phase 2 | Accepted sample deliverables, failures, costs and time including review | Hermes adds value or a simpler alternative is selected |
| Days 13–14 | Operator evaluates a scoped paid pilot offer | Buyer response, price hypothesis, deliverable limits and go/no-go record | Concrete demand, manageable scope and plausible economics |

### Days 15–90 (conditional)

| Stage | Deliverables | Dependencies | Pass evidence | Stop or narrow when |
| --- | --- | --- | --- | --- |
| Days 15–30: assisted pilot | Pinned runtime/model, minimum integrations, reviewed skills, logs, scoped output | Data permission, buyer agreement, reviewer and budget | Buyer accepts useful work; major costs measured | Critical errors cannot be reviewed affordably or access fails |
| Days 31–60: repeatability | Multiple batches, exception handling, cost accounting, optional C experiment | Continued demand and stable baseline | Repeated accepted delivery and improvement beyond B if C is pursued | Rework grows, margins remain negative, or learning regresses |
| Days 61–90: productization decision | Standard onboarding, support limits, release/rollback process and acquisition results | Repeatable positive contribution and buyer continuation | Evidence supports scaling, bounded managed service, or narrow software product | Sales or delivery depends on unsustainable bespoke effort |

### Minimum implementation specification
- One tenant-scoped agent profile and pinned model/provider
- Versioned input schema, permitted source corpus, deterministic output validation
- Minimal authorized read tools; draft outputs by default
- Durable job IDs, idempotency controls, bounded retries, status records
- Source-linked outputs and reviewer decisions
- Evaluation harness with baseline conditions A/B/C and protected expected answers
- Release manifest: runtime commit/tag, model version, skill versions, data versions, evaluation results, reviewer approval
- Operational logs, per-job spend limits, kill switch and rollback to previous approved skill release

### Initial skill seeding
Seed the three narrow skills for the selected candidate from Phase 2 with reviewer-approved procedures and representative examples. Keep facts with sources and effective dates; keep personal preferences separate. Do not use a random document count as a proxy for coverage.

### Proposed jobs, not activated schedules
| Trigger/cadence | Purpose | Output and gate | Cost control |
| --- | --- | --- | --- |
| Authorized new input | Execute the approved workflow | Validated draft or explicit escalation | Per-job tool, token, time and retry limits |
| Daily during active pilot | Summarize failures and review load | Metrics only; no automatic production skill changes | Aggregate existing logs rather than rereading all sources |
| Weekly, if enough new evidence | Review error clusters and candidate changes | Development experiment; independent evaluation before promotion | Batch evaluations and stop low-value experiments |
| Source version change | Detect potentially stale references | Revalidation task and affected-skill list | Monitor defined sources, not unrestricted browsing |
| Approved release | Promote evaluated skills | Version manifest and rollback checkpoint | Bounded rollout and review |
| Critical incident or budget breach | Suspend affected action | Incident record and human decision | Kill switch and limited diagnostics |

### Sample operating charter
- Objective: produce the selected workflow's accepted deliverable within buyer-defined quality, cost and time limits
- Inputs: only authorized sources and minimum customer data needed
- Permitted actions: retrieve, analyze, validate and create drafts in designated locations
- Approval required: publication, merges, customer messages, reminders, contractual notices, production changes, expanded access
- Excluded actions: autonomous professional determinations, payments, unsupported customer commitments
- Learning: propose changes in isolated candidate version; do not modify production skills or approval rules
- Budget: enforce operator-approved per-job and period caps before execution
- Escalation: missing/conflicting evidence, critical ambiguity, permission failure, unfamiliar action or exceeded limits
- Completion: return evidence, validation status, unresolved issues and actual usage
- Recovery: stop, preserve permitted audit evidence, and restore the last approved release when directed.

### First three experiments
| Experiment | Procedure | Proposed pass/fail rule |
| --- | --- | --- |
| Demand | Present bounded sample and scoped offer to reachable relevant buyers | Pass with a paid pilot or concrete purchasing commitment and permitted task access; interest alone is inconclusive |
| Delivery | Compare A and B on representative held-out tasks with independent review | Pass only if quality fits agreed limits and fully costed delivery supports the offered price; target net time saving set in advance |
| Learning | Compare candidate C with frozen B, including annotation/evaluation costs | Promote only for predeclared held-out gains without critical regressions and with credible cost recovery over expected reuse |

Experiments may fail. Preserve negative results and change the offer or method accordingly. Do not tune thresholds after seeing results to manufacture a pass.

### Decision dashboard
Track sampled cases and time period; accepted/rejected outputs; critical and noncritical errors; review and rework minutes; escalation precision/recall where labeled; tool failures; cost per accepted unit; contribution per customer; pilot conversion and continuation.

Separate leading indicators from realized revenue and retention. Include a reason for every stage transition. Readiness is a documented evidence decision, not a date.

## What completion would mean

A credible milestone is one paying customer receiving a repeatable scoped deliverable with measured positive contribution and an affordable review process. A later milestone is controlled autonomy for specific actions supported by prospective evidence. Neither commercial or autonomous milestone currently exists in this repository. An offline development baseline is now available.

## Completed technical increment

See [pilot brief](pilot/brief.md), [evaluation protocol](evals/README.md), [development run](results/development-baseline-v1/summary.md) and [decision log](pilot/decision_log.md). The five regression tests and 12 synthetic cases check plumbing and supported-rule behavior. They do not certify expert performance. CI is configured to repeat these checks; the [release checklist](pilot/release_checklist.md) distinguishes CI from promotion authority.

Next dependencies: operator constraints, buyer access, permitted representative inputs and an independent reviewer. Then pin a Hermes version and add a B adapter only if the baseline comparison warrants it. The candidate procedure has not been installed into a running agent.
