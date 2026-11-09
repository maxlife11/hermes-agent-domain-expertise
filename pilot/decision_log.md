# Decision and experiment log

| ID | Decision | Basis | Status / reconsideration |
| --- | --- | --- | --- |
| D01 | Use N01 for first offline prototype | Structured changes support deterministic checks without credentials | Technical choice only; buyer access can change commercial priority |
| D02 | Implement condition A before Hermes | Attribution requires a working baseline | Completed for a narrow normalized-input scope |
| D03 | Keep public fixtures separate from labels | Avoid labels in runner inputs | Implemented structural separation; public data is not a protected holdout |
| D04 | Leave review and labor cost unknown | No independent human review performed | Must populate before customer economics claims |
| D05 | Use pre-pilot gates separately from post-pilot scoring | Original revised scoring depended on outcomes not yet observable | Updated Phase 3 |
| D06 | Store candidate skill in the project only | User authorized repository development | Not installed as a personal skill or promoted to a running Hermes instance |
| D07 | Keep release control manual | No candidate Hermes runtime or private evaluations exist | Promotion checklist required; CI alone cannot authorize production |

Evidence: [development run](../results/development-baseline-v1/summary.md).
Date: 2026-11-05, America/New_York.

No buyer has been contacted through this work. No paid pilot, retention, Hermes improvement, or generalization result is established.

## Benchmark alignment — 2026-11-09

Use the [canonical methodology](../INDEX.md), [domain contracts](../benchmarks/DOMAIN_SPECS.md) and [rollout](../benchmarks/ROADMAP.md). Current [v2 evidence](../results/development-baseline-v2/summary.md) is synthetic development only; human acceptance and commercial value remain unknown. Historical entries above are retained, not evidence of current promotion. Private labels must remain outside specialist access; benchmark changes require a version break.
