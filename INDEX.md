

# Domain Benchmark Index Specification and Rationale


## Status

Active specification (2026-11-05). Proposed for integration into the evidence-led validation workflow.

## Purpose

This document defines the **primary benchmark index** and **sub-indexes per domain** used by the Hermes AI Agent domain expertise research project. It explains how and why the construct was adopted, linking the measurement requirements from Phase 2, feasibility gates from Phase 3, and implementation plans from Phase 4.

## How We Arrived at This Outcome

### Step 1: Identical Gaps in the Original Draft

The initial Phase 2 (learning loop) treated accumulation of memory/skills as a proxy for expertise. The controlled-improvement loop operated at a level of abstraction where:

- "Did the agent learn?" → answered by memory entries, skill iterations (diagnostic measures, not expertise measures)
- "Is the agent better?" → answered by field-level output correctness on held-out tasks

The gap: there was no defined **what** constitutes expert knowledge in a given domain, nor **how** sub-domains map to sub-knowledge. Expertise was a black box.

### Step 2: Evidence-Based Revision

The revision (e8ee81f) replaced calendar-based expertise timelines and fixed confidence with evidence-based stages (Assisted → Reliable → Bounded autonomous). This required a measurable representation of "expertise progress."

### Step 3: Index as the Missing Construct

The **primary benchmark index** was identified as the missing measurement substrate:

- **Primary index**: the canonical, versioned, source-linked index of domain knowledge for a candidate workflow (N01–N12)
- **Sub-indexes**: granular partitions within the domain (e.g., OpenAPI parsing, example testing, version diff for N01)

### Step 4: Rationale

The index was adopted because:

1. **Measurement validity**: You cannot measure accuracy, staleness, or coverage without an index defining what those terms mean.
2. **Controlled learning**: The improvement loop needs a target. The index provides it.
3. **Evaluation protocol**: Held-out sets must be separated from training; the index defines the separation.
4. **Buyer evidence**: Buyers need transparent indices to evaluate value.

## Index Specification

### Primary Index Fields
- Domain ID (N01–N12)
- Key facts (with sources, effective dates, confidence)
- Covered subtopics (with mapping to gaps)
- Source registry (authorized feeds, endpoints, last-verified dates)
- Refresh schedule (monthly monitoring cadence)
- Version history (revision, changelog, reviewer approval)

### Sub-Index Hierarchy
For each candidate workflow, sub-indexes partition the domain:

| Workflow | Sub-Index Examples |
| --- | --- |
| N01 | OpenAPI parsing, example testing, version diff, changelog, symbol coverage |
| N02 | Ticket-to-article de-id, KB contradiction resolution, editorial approval |
| N03 | Renewal dates, notice methods, amendment precedence, obligation fields |

### Health Metrics
- Coverage % (per sub-index)
- Staleness score (per source)
- Gap report
- Accuracy decay

## Value Summary

The primary benchmark index + sub-indexes per domain derive the following value:

1. **Measurement**: Converts subjective expertise claims to instrumented metrics
2. **Learning**: Directs skill creation to under-covered sub-indexes
3. **Evaluation**: Provides held-out ground truth via index structure
4. **Commercial**: Positions expertise as measurable, sells index access/consulting
5. **Operational**: Enables scoped, reversible, reviewer-prioritized actions

---

This specification is intended to be reviewed by other agents and humans for completeness, accuracy, and alignment with the broader evidence-led strategy. It is not yet a formal release gate but serves as the operational blueprint for the next experimental increment.


