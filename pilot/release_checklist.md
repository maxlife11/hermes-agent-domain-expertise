# Release control

Status: manual gates; no production release exists.

Before a candidate skill/runtime release:
- Identify the exact base and candidate revisions, runtime/model/tool versions and data versions.
- Choose one changed component to preserve attribution.
- Run public regressions and separately run evaluator-controlled private holdout tasks.
- Keep expected holdout answers inaccessible to the agent; separate access controls are required beyond a gitignore.
- Record reviewer decisions, critical failures, costs and sample sizes.
- Check predeclared quality and cost thresholds; document rejection as well as promotion.
- Obtain an authorized promotion decision and limit rollout scope.
- Record the previous approved revision and test rollback in isolation.
- Suspend on critical errors, unauthorized actions, exceeded budgets or unreliable dependencies.

CI enforces documentation consistency and the offline baseline's regression checks. It does not implement private evaluation access control, protected branches, runtime rollback or autonomous deployment. Production permissions and protected-branch settings require a separate configured environment.

## Benchmark alignment — 2026-11-09

Use the [canonical methodology](../INDEX.md), [domain contracts](../benchmarks/DOMAIN_SPECS.md) and [rollout](../benchmarks/ROADMAP.md). Current [v2 evidence](../results/development-baseline-v2/summary.md) is synthetic development only; human acceptance and commercial value remain unknown. Historical entries above are retained, not evidence of current promotion. Private labels must remain outside specialist access; benchmark changes require a version break.
