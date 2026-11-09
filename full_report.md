# Hermes Agent Domain Expertise Combined Report

> Generated from phase1.md through phase4.md. Do not edit directly.

> Status: hypotheses and proposed validation; no validated business winner.

> See [README](README.md), [evidence register](EVIDENCE.md) and [revision record](CHANGELOG.md).

# Phase 1 — Workflow Hypotheses and Evidence Requirements

Updated: 2026-11-05. Status: discovery candidates; commercial demand unverified.

## Scope and correction

The initial report asserted 61+ niches but described ten and left the remaining categories as a placeholder. This revision deliberately replaces that breadth target with 12 specific workflow hypotheses. It does not claim exhaustive market coverage or newly validated TAM estimates.

Define an opportunity as **buyer + recurring problem + bounded workflow + measurable deliverable + payment hypothesis**. A parent industry's size is not the service's accessible market. Large budgets do not establish access to buyers, data or procurement approval.

The original 2025–2027 outlook is not a verified forecast. Future research must distinguish historical observations, current offers, and forecasts, retaining source dates and uncertainty.

## Domain Knowledge Index Requirement

For each of the 12 workflow hypotheses (N01–N12), the opportunity definition now includes an explicit domain knowledge index requirement: a bounded, source-linked index of domain facts, sources, and gaps must be created before any commercial or autonomy claim can be advanced. The index serves as the knowledge substrate for the agent's learning loop and must be monitored for staleness and coverage.

### Index Requirements per Candidate
1. Key facts — extracted propositions, sources, effective dates, confidence levels
2. Covered subtopics — mapping current vs. missing domain aspects
3. Source registry — authorized data feeds, document repositories, API endpoints with last-verified dates
4. Refresh schedule — monthly monitoring of staleness, gap detection, accuracy decay metrics
5. Version history — indexed revisions with changelog and reviewer approval dates

### Monthly Index Health Check
- Coverage %: proportion of known domain subtopics present
- Staleness score: average age of indexed source entries vs. freshness target
- Gap report: newly identified missing domains or outdated entries
- Accuracy decay: proportion of index entries contradicted by newer authoritative sources

### Index Maintenance Actions
- Add: new sources discovered during task execution or buyer feedback
- Update: revise facts when fresh authoritative data exceeds defined confidence threshold
- Prune: remove entries with no fresh source support beyond X days
- Escalate: index coverage below Y% or staleness beyond Z days to operator for review

Index entries are scoped to the candidate's bounded workflow and do not expand autonomously. Metadata lives in Hermes memory with source provenance tags.

## Candidate inventory

All commercial propositions below have **unverified** confidence. Mechanistic reasons to test a workflow are design judgments, not proof of demand. IDs remain stable across phases.

| ID | Buyer and problem | Narrow deliverable and value hypothesis | Required access and evaluation | Principal obstacle |
| --- | --- | --- | --- | --- |
| N01 | Developer-tools company; docs drift after API releases | Source-linked drift report, tested examples and draft documentation PR | Authorized repository/specification, docs, test environment; maintainer acceptance and example execution | Existing tooling may solve enough of the problem; reviewer burden may erase savings |
| N02 | SaaS support lead; resolved issues fail to reach the knowledge base | Draft article updates linked to resolved tickets and approved product facts | Authorized, minimized tickets and KB; blinded editor review and measured editing time | Privacy, conflicting answers, weak incremental willingness to pay |
| N03 | Operations/procurement lead; renewal and notice dates are scattered | Reviewed register of dates, conditions, notice methods and source passages | Authorized contracts and qualified reviewer; exact field correctness and critical-miss analysis | Amendments, ambiguous dates and missed obligations |
| N04 | B2B sales engineering lead; repetitive questionnaires | Draft responses supported only by approved evidence, with unresolved gaps flagged | Current approved answer library; evidence validity and reviewer acceptance | Confidentiality and unsupported commitments |
| N05 | E-commerce operations lead; inconsistent product catalogs | Detect attribute, variant and policy mismatches; propose a correction queue | Authorized catalog exports and platform rules; item-level correctness | Integration variability and low value per correction |
| N06 | Agency analytics lead; tracking failures undermine reporting | Read-only event/schema checks and a prioritized issue report | Test events, authorized analytics access and expected event specification | Establishing ground truth and attributing business value |
| N07 | Customer-success operations lead; account records are incomplete | Source-backed reconciliation suggestions and duplicate review queue | CRM exports and approved matching rules; false-merge and correction rates | Incorrect merges, stale data and permissions |
| N08 | Finance operations lead; invoices conflict with approved orders | Exception packets with matched fields, discrepancies and evidence | Authorized invoice/order data; exact reconciliation and reviewer time | Sensitive data and costly matching errors; no autonomous payments |
| N09 | Real-estate brokerage operations lead; listing data is inconsistent | Listing QA against supplied source documents and brokerage rules | Licensed data and reviewer; field accuracy and compliance with supplied rules | Data rights and local variation; excludes autonomous valuation |
| N10 | Compliance operations lead; relevant source changes are missed | Dated source-change digest with citations and reviewer routing | Defined official sources and reviewer-owned relevance rules | Coverage gaps and interpretation burden; excludes compliance determinations |
| N11 | B2B product-marketing lead; competitive changes are hard to track | Evidence-linked pricing/feature changes and draft sales-enablement updates | Permitted public sources and dated snapshots; factual change verification | Public information may be easy to replicate and hard to monetize |
| N12 | SaaS support operations lead; escalations lack reproducible context | Structured reproduction/evidence packets for engineering triage | Authorized tickets, logs and isolated repro environment; engineer acceptance | Secrets in logs, unreliable reproduction and environment drift |

## Initial discovery set

Investigate N01, N02 and N03 first because their deliverables can be inspected and kept under review. This is a proposed test order, not a claim that they are the three most profitable niches.

| Candidate | First proof to obtain | Initial boundary | What would disqualify it |
| --- | --- | --- | --- |
| N01 | A maintainer provides actual drift examples and evaluates a sample | Draft PR only; no merge or release authority | Existing checks deliver comparable results at lower total cost |
| N02 | A support lead provides authorized sample tickets and measures editing effort | Draft articles; no publishing or customer replies | Review effort equals or exceeds manual authoring |
| N03 | A buyer and qualified reviewer provide representative contracts | Extract and cite; reviewer approves register and reminders | Critical omissions remain hard to detect affordably |

Buyer access can change this order. No access advantage has been established in this repository.

## Treatment of the original broad opportunities

Retain the original ideas as historical leads, not recommendations. General contract review, autonomous property valuation, insurance underwriting, clinical trial matching and diagnosis support require evidence and controls beyond the initial pilot scope. Procurement response work is narrowed to N04, regulatory monitoring to N10, real-estate operations to N09, and contract operations to N03.

Financial modeling, cybersecurity threat hunting, ESG reporting, meeting intelligence, advertising optimization, churn prediction, logistics, smart-home energy, recruitment, moderation, agricultural detection and legal document generation are deferred rather than declared unprofitable. Their source access, buyer economics and error exposure have not been adequately investigated. Historical descriptions are preserved in the initial commit linked from README.md.

## Evidence required before selection

For each finalist record:

- Named buyer role, purchasing trigger, existing workaround, frequency and actual time/cost burden.
- Reachable acquisition channel and observed purchasing process, not an assumed enterprise sales motion.
- Permitted representative data, independent reviewers and labels, including difficult cases.
- Specific competing offers and dated prices; advertised pricing is not evidence of realized sales.
- A testable scoped offer and a concrete buying signal. Distinguish interview interest, trial use, payment, renewal and retention.
- Delivery costs including onboarding, review, exceptions, support and acquisition.
- Two independent evidence sources where available, including direct buyer evidence; multiple summaries of one study count as one source.
- Contradictory evidence, freshness requirements and the next cheapest uncertainty-reducing test.

Use [EVIDENCE.md](EVIDENCE.md) for provenance. Do not populate unknown fields with invented numbers. Collect no customer-sensitive data without explicit permission and an appropriate handling agreement.

## Execution update

N01 is now the first offline technical experiment, with 12 authored synthetic cases and a deterministic normalized-input baseline. This does not change its unverified commercial confidence or the comparative status of N02/N03. See [pilot scope](pilot/brief.md) and [buyer discovery](pilot/buyer_evidence.md). Buyer access remains unconfirmed.

---

# Phase 2 — Controlled Learning and Bounded Autonomy

Updated: 2026-11-05. Status: offline condition A implemented; Hermes integration and independent expertise evaluation pending.

## Verified capability versus business claim

Official documentation checked during the review describes the capabilities below. The project has not pinned and tested an upstream release. Verify each dependency against the selected release before implementation; documentation support does not prove production reliability.

| Capability | Documentation support | What remains to build or verify |
| --- | --- | --- |
| Agent-managed skills | [Skills system](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/) describes reusable procedures and create/update operations | Domain procedures, test cases and an independent promotion decision |
| Skill-write staging | The same reference describes approval-gated skill writes | Version-specific configuration and enforcement; approval alone is not an evaluation harness |
| Persistent facts | [Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) describes bounded MEMORY.md/USER.md-style memory | Retrieval quality, freshness rules and tenant isolation |
| Scheduling, tools and delegation | [Official overview](https://hermes-agent.nousresearch.com/docs) describes cron, tools, MCP and isolated subagents | Authenticated integrations, permissions, failure recovery and measured costs |
| Model flexibility | Official overview describes provider flexibility | Benchmark every model/version change; portability does not imply equal quality |
| Learning from outcomes | Skills can retain procedures and corrections | Reliable outcome labels and proof of improvement on unseen tasks |
| Model-weight training | Not established by the ordinary memory/skill loop | Any separate training pipeline needs its own data, permissions, compute and evaluation |

Reading documents, retrieving context, changing a procedure, and training model weights are different operations. More memory does not automatically mean more expertise.

## Operational stages

Replace calendar-based expert labels with evidence-based stages. No top-decile claim or fixed time-to-expertise estimate is justified.

| Stage | Required evidence | Permitted operation |
| --- | --- | --- |
| Assisted operator | Useful outputs on representative tasks with errors identified by a reviewer | Read-only work and drafts |
| Reliable specialist | Repeated held-out performance within buyer-approved error and cost limits | Continued reviewed delivery; limited low-consequence actions may be considered |
| Bounded autonomous operator | Stable prospective results, tested exception handling, audit logs and rollback | Only specifically approved actions within explicit limits |

Elapsed time depends on sample availability, feedback delay, integration complexity and failure severity. Passing a small pilot is not evidence of broad autonomy or expertise in an entire profession.

## Minimal architecture

Start with one Hermes profile, a pinned model/provider, narrow tools, deterministic validators and a reviewer. Add subagents only if a controlled comparison shows a net quality, latency or cost advantage.

| Layer | Responsibility | Boundary |
| --- | --- | --- |
| Notion | Approved decisions, evidence summaries, project state and source links | Curated shared knowledge; not the runtime queue or credential store |
| GitHub | Versioned skills, schemas, evaluation code and release manifests | No credentials or customer-confidential artifacts |
| Operational storage | Job state, permitted source artifacts, outputs and audit events | Tenant-scoped access, retention and deletion rules |
| Hermes memory | Compact contextual facts and pointers | Curated and scoped; not an ever-growing domain corpus |
| Retrieval corpus | Versioned permitted references with source and effective dates | Untrusted content cannot grant permissions or override operating rules |
| Evaluation/promotion service | Evaluate candidate skill changes and release approved versions | Separate authority from the agent proposing the change |

The official memory reference warns against multiple agent processes sharing a Hermes home. Use separate profiles and explicit shared-memory access. Do not assume this alone provides a complete multi-tenant security boundary.

## Controlled improvement loop

1. Record the task, source versions, output, model/tool versions, elapsed time, costs and reviewer corrections.
2. Classify the error: retrieval, source quality, reasoning, tool execution, formatting or scope.
3. Propose the smallest relevant skill change. An unsolved task does not automatically require another agent or more memory.
4. Test the candidate in isolation on development cases.
5. Compare with the incumbent on held-out cases and regressions.
6. Promote only when predeclared quality, cost and safety criteria pass and authorized review approves.
7. Version the release; record its evidence and rollout boundary.
8. Monitor prospective tasks. Revert or suspend actions when critical errors, unauthorized actions, cost overruns or drift exceed agreed limits.

Production skills remain fixed between releases. Outcome collection may run regularly; self-modification of production is not the default. Separate source facts from experimental lessons and approved operating procedures.

## Baselines and attribution

Compare three conditions on the same representative task distribution:

- A: simplest viable script or general assistant.
- B: Hermes with fixed, reviewed skills.
- C: the same Hermes setup with candidate skill updates.

Hold model version, tools, source access and spending limits comparable. Record any unavoidable differences. Count the cost of proposing and evaluating changes in C. A stronger replacement model is not evidence that the memory loop learned.

Choose the simplest condition meeting buyer requirements at the lowest total cost. A profitable B can be worth deploying even if C adds no value.

## Evaluation protocol

Create evaluation cases before iterative skill development. For the first workflow, a proposed starter set is 30–50 varied cases; actual size must follow variation, failure severity and affordable independent review. This is not enough by itself to establish rare-event reliability.

- Separate development and held-out sets; keep expected held-out answers out of agent-accessible memory and skill references.
- Split by customer, template family, product version or time when near-duplicates could leak answers.
- Include missing, conflicting, ambiguous, malformed and out-of-scope inputs.
- Record sample sizes, denominators, reviewer disagreements and uncertainty; do not report percentage accuracy without its basis.
- Keep a final untouched set or refresh it when repeated testing overfits the development process.
- Use independent reviewers where feasible. The agent's confidence and self-grade are not ground truth.
- Verify citations actually support the extracted claim, not merely that a URL exists.
- Distinguish retrospective evaluation from prospective production monitoring.

| Dimension | Measure |
| --- | --- |
| Quality | Field-level correctness; accepted deliverables; unsupported assertions; critical omissions |
| Efficiency | End-to-end completion time including reviewer and rework time |
| Economics | Fully costed delivery and contribution profit per accepted unit |
| Reliability | Tool failures, duplicate actions, retries, timeout recovery and deterministic replay where feasible |
| Escalation | Correct abstentions, missed escalations and unnecessary escalations |
| Learning | Held-out improvement versus B, with regression and evaluation costs included |

Memory-entry counts, skill counts and iteration counts are diagnostic activity measures, not expertise metrics.

## Domain Knowledge Index

For each candidate workflow (N01–N12), maintain a domain knowledge index that catalogs:

1. Key facts — extracted propositions, sources, effective dates, confidence levels
2. Covered subtopics — mapping current vs. missing domain aspects
3. Source registry — authorized data feeds, repository docs, API endpoints with last-verified dates
4. Refresh schedule — monthly monitoring of staleness, gap detection, accuracy decay
5. Version history — indexed revisions with changelog and reviewer approval dates

### Monthly Index Health Check
- Coverage %: proportion of known domain subtopics present
- Staleness score: average age of indexed source entries vs. freshness target
- Gap report: newly identified missing domains or outdated entries
- Accuracy decay: proportion of index entries contradicted by newer authoritative sources

### Index Maintenance Actions
- Add: new sources discovered during task execution or buyer feedback
- Update: revise facts when fresh authoritative data exceeds defined confidence threshold
- Prune: remove entries with no fresh source support beyond X days
- Escalate: index coverage below Y% or staleness beyond Z days to operator for review

Index entries are scoped to the candidate's bounded workflow and do not expand autonomously. Metadata lives in Hermes memory with source provenance tags.

## Concrete skill candidates

These are proposed domain procedures, not installed skills. A repository-local N01 candidate and a limited condition A baseline now exist; neither demonstrates Hermes skill performance.

| Workflow | Skill | Inputs and output | Check and escalation |
| --- | --- | --- | --- |
| N01 | Detect API documentation drift | Versioned API/spec diff plus docs → cited mismatch queue | Verify referenced symbols; escalate undocumented intended behavior |
| N01 | Test documented example | Example plus isolated environment → reproducibility result | Pin dependencies; report setup failures separately from product bugs |
| N01 | Draft minimal documentation change | Validated mismatch → draft PR with evidence | Human review; no merge authority |
| N02 | Extract reusable support resolution | Authorized resolved ticket → de-identified resolution candidate | Confirm resolution evidence; escalate incomplete tickets |
| N02 | Reconcile KB contradiction | Candidate plus approved sources → update or conflict report | Prefer current approved facts; reviewer resolves disagreement |
| N02 | Draft article update | Approved resolution → cited draft and change rationale | Check confidentiality and editing time; no publication |
| N03 | Extract renewal and notice terms | Contract and amendments → structured fields with exact passages | Verify date/condition linkage; preserve uncertainty |
| N03 | Resolve document precedence | Supplied agreement hierarchy → proposed effective terms | Escalate unclear amendments or conflicting provisions |
| N03 | Prepare reviewed obligation register | Approved extractions → register and proposed reminder dates | Reviewer approves every critical field; no notice sending |

## Operational controls

Use least-privilege tools, sandbox document/code execution, minimize sensitive data, and keep credentials in a dedicated secret mechanism. Treat retrieved documents and tickets as data, not instructions. Use idempotency keys and verified postconditions for writes, bounded retries, budget limits, logs and a tested kill switch.

For the initial candidates, retain human approval for publishing, merging, customer communication, changing deadlines and production configuration. No autonomous legal determinations, payments, contract notices or customer commitments.

Schedules in Phase 4 are proposals only. Configure them only within explicit authorization after the workflow is validated.

## Implemented baseline and evaluation limits

[Evaluation instructions](evals/README.md) define an executable condition A for removed operations and newly required parameters absent from structured examples. The runner rejects labels in task inputs, hashes provenance and creates review records. The public 12-case development set is not a private holdout. [Results](results/development-baseline-v1/summary.md) measure field matching only. B/C adapters, independent reviewer labels, real customer examples and runtime promotion remain pending.

Use the [review protocol](pilot/review_protocol.md) to define critical errors, reviewer qualifications and adjudication. Hide condition identity during comparisons when feasible. Change one component at a time; improvements from model, retrieval, prompt and validator changes must not be conflated.

---

# Phase 3 — Feasibility, Prioritization and Economics

Updated: 2026-11-05. Status: decision framework; no validated winner or populated commercial ranking.

## Withdraw the initial ranking

The original weights summed to 105%, its overall scores did not reproduce, risk-score direction was unclear, and the top-five narrative differed from the ranking. The complete historical arithmetic audit is in [CHANGELOG.md](CHANGELOG.md).

Normalizing the old numbers does not repair unsupported inputs. Do not reuse the corrected historical scores to choose a business.

## Pre-pilot selection: do not require future outcomes

Compare reachable buyer access, repeated problem evidence, permitted sample availability, independent evaluability, implementation effort and error consequences. Record pass/fail/unknown and a next experiment; do not assign speculative commercial totals. Prioritize the cheapest decisive uncertainty reduction. Unknown economics permits an offline measurement experiment, not an unchecked paid production launch.

The technical baseline selects N01 for evaluability without credentials. Commercial selection remains open. The [operator brief](pilot/operator_brief.md) and [buyer evidence protocol](pilot/buyer_evidence.md) collect the missing inputs. Do not use retention, realized margins or measured learning gains as prerequisites to starting discovery.

## Feasibility gates before scoring

Record pass, fail or unknown with a source and date. Unknown is not a pass; fatal gaps cannot be offset by an attractive market score.

| Gate | Evidence needed |
| --- | --- |
| Buyer access | Reachable budget owner and a credible purchasing path |
| Data access | Permission and representative inputs sufficient for a pilot |
| Evaluability | Independent reviewer or reliable ground truth; explicit failure classes |
| Scope | Bounded outcome with manageable error consequences and action permissions |
| Economics | Plausible positive contribution profit after review and rework |
| Delivery | Minimal integrations, security and operational support within actual resources |

A paid pilot requires adequate gates for its limited scope. Production autonomy requires stronger evidence and separate authorization.

## Post-pilot scoring after gates

This model is for post-pilot comparison, when outcomes can be observed. It must not block initial experiments by requiring future renewal or learning evidence. Weights sum to 100%. Higher scores always mean more attractive. Scores compare opportunities, not probabilities of success.

| Criterion | Weight | Score 1 | Score 3 | Score 5 |
| --- | --- | --- | --- | --- |
| Buyer pain and payment evidence | 20% | No concrete buyer evidence | Repeated buyer reports and defined budget owner | Paid use with repeated value and renewal evidence |
| Contribution economics | 15% | Negative or unmeasured | Plausible margin with measured major costs | Positive observed margin across varied cases |
| Validated learning benefit | 15% | No correction signal or measured gain | Reliable labels and a feasible improvement test | Repeated held-out gains net of learning cost |
| Acquisition feasibility | 15% | Buyers inaccessible | Reachable channel with observed responses | Repeatable paying acquisition at measured acceptable cost |
| Time to paid value | 10% | Long unknown dependency chain | Scoped pilot with manageable dependencies | Demonstrated short path from access to paid value |
| Data and evaluation quality | 10% | Unavailable or unreliable | Permitted representative samples and reviewers | Stable access, high-quality labels and prospective feedback |
| Repeatability/productization | 5% | Bespoke delivery each time | Shared core with some onboarding variation | Repeated delivery with low incremental customization |
| Defensibility | 5% | Easily substituted with no advantage shown | Some integration or specialized evaluation advantage | Demonstrated retention tied to hard-to-replicate delivery assets |
| Manageable operational risk | 5% | Errors hard to detect or reverse | Reviewable workflow with explicit controls | Low-consequence scope and tested recovery |

Formula: score out of 100 = sum(weight_percent × rating / 5). Use whole-number totals when presenting rankings. Unknown ratings remain null, not zero or an invented midpoint. Do not compare partially scored totals as if complete.

Record evidence confidence separately: verified observation, supported estimate, hypothesis or unknown. Distinguish customer-reported numbers from measured costs. After real inputs exist, test rankings under greater emphasis on near-term cash flow, low supervision and restricted budgets.

## Domain Knowledge Index Feasibility Gate

Prior to scoring any candidate (N01–N12), the following index readiness conditions must be documented:

1. Index exists — a bounded domain knowledge index has been created for the candidate covering key facts, source registry, and initial gaps
2. Index health measured — coverage %, staleness score, and gap report from the Monthly Index Health Check are on file
3. Monitoring scheduled — recurring task is defined with responsible reviewer

The index readiness assessment is a gate *before* post-pilot scoring; it does not replace the feasibility gates (buyer access, data access, evaluability, scope, economics, delivery) but operates in parallel. A candidate with strong market signals but no viable index receives "Unknown" on all scored dimensions until index readiness is established.

Index metadata (creation date, reviewer, version, coverage %, staleness score) must be recorded in the same evidence register as other feasibility gate outcomes.

## Domain Knowledge Index Feasibility Gate

Prior to scoring any candidate (N01–N12), the following index readiness conditions must be documented:

1. Index exists — a bounded domain knowledge index has been created for the candidate covering key facts, source registry, and initial gaps
2. Index health measured — coverage %, staleness score, and gap report from the Monthly Index Health Check are on file
3. Monitoring scheduled — recurring task is defined with responsible reviewer

The index readiness assessment is a gate *before* post-pilot scoring; it does not replace the feasibility gates (buyer access, data access, evaluability, scope, economics, delivery) but operates in parallel. A candidate with strong market signals but no viable index receives "Unknown" on all scored dimensions until index readiness is established.

Index metadata (creation date, reviewer, version, coverage %, staleness score) must be recorded in the same evidence register as other feasibility gate outcomes.

## Current candidate decision table

| Candidate | Discovery priority | Gates | Commercial score | Next decisive test |
| --- | --- | --- | --- | --- |
| N01 API documentation maintenance | Offline baseline implemented | Buyer/data/economics unknown | Not scored | Maintainer reviews real-input sample and scoped paid offer |
| N02 Support KB maintenance | Initial set | Unknown | Not scored | Support lead measures time saved on authorized ticket-to-article tasks |
| N03 Renewal/notice extraction | Initial set | Unknown | Not scored | Buyer and qualified reviewer test critical-field extraction and cost |
| N04–N12 | Reserve set | Unknown | Not scored | Revisit if access or evidence is stronger than the initial set |

N01 may be a useful first technical demonstration because code/spec references permit explicit checks. That is not a conclusion about willingness to pay. Existing buyer access can make N02 or N03 the better first commercial test. No first-choice niche has been approved.

## Initial offer hypotheses

| ID | Scoped offer | Proposed delivery model | Distribution experiment | Primary failure reason |
| --- | --- | --- | --- | --- |
| N01 | One release's drift audit and reviewed draft fixes | Paid diagnostic, then capped managed maintenance | Discuss recent docs failures with reachable developer-tools maintainers | Existing tools plus staff are cheaper |
| N02 | One approved ticket category's KB update batch | Capped managed service with human editorial approval | Work with reachable support leads or support-service partners | Editing and privacy overhead erase value |
| N03 | One contract type's reviewed renewal register | Paid setup plus capped reviewed maintenance | Work with operations/procurement leads and an appropriate reviewer | Missing critical terms makes review uneconomic |

These channels have not been exercised. Writing an outreach plan is not permission to send messages.

Avoid freemium and unlimited usage until acquisition economics and delivery costs support them. Define volume in pages, complexity, integrations, turnaround and review scope; document count alone may conceal large cost variation. Do not propose fixed prices as market facts before testing a scoped offer.

## Unit economics worksheet

Populate downside, base and upside cases from observed ranges. No revenue or margin forecast is currently defensible.

| Variable | Include |
| --- | --- |
| Recurring revenue | Actual contracted charge and billable volume |
| Setup revenue | Report separately; do not hide recurring losses with setup fees |
| Variable technical costs | Model inference, retrieval, APIs, compute, storage and retries |
| Delivery labor | Review, rework, exceptions, support and ongoing onboarding burden |
| Learning costs | Candidate generation, annotation, evaluations and failed experiments |
| Other variable costs | Payment fees, refunds and incident allowance where applicable |
| Fixed operating costs | Base infrastructure, software, administration and fixed staffing |
| Acquisition costs | Prospecting/sales labor, tools, channel payments and onboarding acquisition effort |

Recurring contribution per customer = recurring revenue − variable technical costs − delivery labor − allocated learning/other variable costs.

Contribution margin = contribution / recurring revenue. Labor is hours × an explicit replacement-cost rate even when performed by the founder. Report cash spending separately.

Break-even customer count = ceiling(fixed monthly operating cost / positive monthly contribution per customer), subject to delivery capacity. If contribution is zero or negative, scaling does not establish break-even.

CAC payback months = acquisition cost per new paying customer / positive monthly contribution, with setup charges and onboarding treatment disclosed. Do not calculate confident lifetime value before retention evidence exists.

Stress-test longer documents, difficult cases, model price changes, review spikes, low utilization and lost customers. Track customer concentration and founder capacity.

## Proposed pilot decision gates

Set exact buyer-specific thresholds before seeing results. Suggested starting hypotheses:

- Concrete buying evidence: a paid pilot or equivalent purchasing commitment, not enthusiasm alone.
- Material net time reduction including review; a 30% improvement can be a pilot hypothesis, not a universal benchmark.
- Positive contribution profit at a price the buyer will actually accept.
- All critical fields/actions reviewed within the agreed initial scope.
- Zero observed critical errors in the evaluation is necessary for some scopes but is not proof of a zero underlying error rate.
- A willingness to continue or renew after observed delivery.

If demand fails, revise the offer or candidate before adding infrastructure. If A matches B at lower cost, use A. If C fails to improve on B, retain fixed skills. If review remains unaffordable, narrow the workflow or stop.

## Economics status

The offline manifest reports zero external API spend but leaves review time and labor costs null. No human review or normalization effort has been measured. Zero model spend does not mean zero delivery cost. The [review protocol](pilot/review_protocol.md) specifies records needed before contribution profit can be calculated.

---

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
