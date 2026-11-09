import sys

def add_index_to_file(filename, anchor, index_block):
    with open(filename, "r") as f:
        content = f.read()
    if anchor not in content:
        print(f"WARNING: anchor '{anchor[:40]}' not found in {filename}")
        return False
    content = content.replace(anchor, index_block + "\n\n" + anchor, 1)
    with open(filename, "w") as f:
        f.write(content)
    print(f"Updated {filename}")
    return True

# Phase 1: Domain Knowledge Index requirement before Concrete Skill Examples
p1_block = '''## Domain Knowledge Index Requirement

For each of the 12 workflow hypotheses (N01–N12), the opportunity definition now includes an explicit domain knowledge index requirement: a bounded, source-linked index of domain facts, sources, and gaps must be created before any commercial or autonomy claim can be advanced. The index serves as the knowledge substrate for the agent's learning loop and must be monitored for staleness and coverage.

### Index Requirements per Candidate
1. **Key facts** — extracted propositions, their sources, effective dates, confidence levels
2. **Covered subtopics** — mapping current vs. missing domain aspects
3. **Source registry** — authorized data feeds, document repositories, API endpoints with last-verified dates
4. **Refresh schedule** — monthly monitoring of staleness, gap detection, accuracy decay metrics
5. **Version history** — indexed revisions with changelog and reviewer approval dates

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

Index entries are scoped to the candidate's bounded workflow and do not expand autonomously. Metadata lives in Hermes memory with source provenance tags.'''

add_index_to_file("phase1.md", "## Concrete Skill Examples", p1_block)

# Phase 2: Domain Knowledge Index before Learning Mechanisms
p2_block = '''## Domain Knowledge Index

For each candidate workflow (N01–N12), maintain a domain knowledge index that catalogs:

1. **Key facts** — extracted propositions, sources, effective dates, confidence levels
2. **Covered subtopics** — mapping current vs. missing domain aspects
3. **Source registry** — authorized data feeds, repository docs, API endpoints with last-verified dates
4. **Refresh schedule** — monthly monitoring of staleness, gap detection, accuracy decay
5. **Version history** — indexed revisions with changelog and reviewer approval dates

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

Index entries are scoped to the candidate's bounded workflow and do not expand autonomously. Metadata lives in Hermes memory with source provenance tags.'''

add_index_to_file("phase2.md", "## Learning Mechanisms", p2_block)

# Phase 3: Domain Knowledge Index as feasibility gate before decision table
p3_block = '''## Domain Knowledge Index Feasibility Gate

Prior to scoring any candidate (N01–N12), the following index readiness conditions must be documented:

1. Index exists — a bounded domain knowledge index has been created for the candidate covering key facts, source registry, and initial gaps
2. Index health measured — coverage %, staleness score, and gap report from the Monthly Index Health Check are on file
3. Monitoring scheduled — recurring task is defined with responsible reviewer

The index readiness assessment is a gate *before* post-pilot scoring; it does not replace the feasibility gates (buyer access, data access, evaluability, scope, economics, delivery) but operates in parallel. A candidate with strong market signals but no viable index receives "Unknown" on all scored dimensions until index readiness is established.

Index metadata (creation date, reviewer, version, coverage %, staleness score) must be recorded in the same evidence register as other feasibility gate outcomes.'''

add_index_to_file("phase3.md", "## Current candidate decision table", p3_block)

# Phase 4: Domain Knowledge Index creation/monitoring step before Concrete skill candidates
p4_block = '''## Domain Knowledge Index Creation and Monitoring Step

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
- Escalation: missing/conflicting evidence, critical ambiguity, permission failure, unfamiliar action, exceeded limits
- Completion: return evidence, validation status, unresolved issues, actual usage
- Recovery: stop, preserve permitted audit evidence, restore last approved release when directed

### First three experiments
| Experiment | Procedure | Proposed pass/fail rule |
| --- | --- | --- |
| Demand | Present bounded sample and scoped offer to reachable relevant buyers | Pass with paid pilot or concrete purchasing commitment plus permitted task access; interest alone inconclusive |
| Delivery | Compare A and B on representative held-out tasks with independent review | Pass only if quality fits agreed limits and fully costed delivery supports offered price; target net time saving set in advance |
| Learning | Compare candidate C with frozen B, including annotation/evaluation costs | Promote only for predeclared held-out gains without critical regressions and credible cost recovery over expected reuse |

Experiments may fail. Preserve negative results and change the offer or method accordingly. Do not tune thresholds after seeing results to manufacture a pass.

### Decision dashboard
Track sampled cases and time period; accepted/rejected outputs; critical and noncritical errors; review and rework minutes; escalation precision/recall where labeled; tool failures; cost per accepted unit; contribution per customer; pilot conversion and continuation.

Separate leading indicators from realized revenue and retention. Include a reason for every stage transition. Readiness is a documented evidence decision, not a date.'''

add_index_to_file("phase4.md", "## Concrete skill candidates", p4_block)

print("All phases updated.")
