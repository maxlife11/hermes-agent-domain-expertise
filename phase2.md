# Phase 2 — Controlled Learning and Bounded Autonomy

Updated: 2026-11-05. Status: proposed architecture; no runtime or expertise benchmark completed.

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

## Concrete skill candidates

These are specifications to implement and evaluate, not installed skills.

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
