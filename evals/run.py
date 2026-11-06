"""Run condition A offline. Input must contain tasks only, never expected labels."""
import argparse
import hashlib
import json
import platform
import subprocess
import time
from pathlib import Path
from evals.baseline import analyze

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--cases", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()
    cases = [json.loads(line) for line in Path(args.cases).read_text().splitlines() if line.strip()]
    ids = [c.get("id") for c in cases]
    if not cases or any(not isinstance(i, str) or not i for i in ids) or len(set(ids)) != len(ids):
        raise ValueError("nonempty cases with unique string ids required")
    allowed = {"id", "source", "before", "after", "docs"}
    if any(set(c) != allowed for c in cases):
        raise ValueError("unexpected fields: runner accepts tasks only, not labels")
    # Validate the complete batch before creating any artifacts.
    started = time.perf_counter()
    outputs = [analyze(c) for c in cases]
    elapsed = time.perf_counter() - started
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=False)
    root = Path(__file__).resolve().parents[1]
    git = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True)
    manifest = {"condition": "A", "engine": "normalized-api-drift-v1", "python": platform.python_version(),
                "git_commit": git.stdout.strip() if git.returncode == 0 else None,
                "input_sha256": digest(args.cases), "engine_sha256": digest(root / "evals/baseline.py"),
                "runner_sha256": digest(__file__), "case_count": len(cases), "elapsed_seconds": elapsed,
                "external_api_cost_usd": 0, "labor_cost_usd": None, "review_minutes": None,
                "model": None, "hermes_version": None, "skill_executed": False,
                "scope": "offline normalized inputs; no network or example execution"}
    (out / "outputs.jsonl").write_text("".join(json.dumps(o, sort_keys=True) + "\n" for o in outputs))
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    reviews = [{"id": c["id"], "decision": None, "review_minutes": None,
                "reviewer": None, "critical_error": None, "notes": ""} for c in cases]
    (out / "reviews.jsonl").write_text("".join(json.dumps(r) + "\n" for r in reviews))
    lines = ["# Review packet", "", "Condition A; synthetic development results are not customer validation.", ""]
    for output in outputs:
        lines += [f"## {output['id']}", "", "```json", json.dumps(output, indent=2), "```", ""]
    (out / "review.md").write_text("\n".join(lines))
    print(f"Wrote {len(cases)} cases to {out}")

if __name__ == "__main__":
    main()
