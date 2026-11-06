#!/usr/bin/env python3
"""Generate the combined report, or check synchronization and local links."""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHASES = [f"phase{i}.md" for i in range(1, 5)]
HEADER = (
    "# Hermes Agent Domain Expertise — Combined Report\n\n"
    "> Generated from phase1.md through phase4.md. Do not edit directly.\n"
    "> Run: python3 scripts/build_report.py\n\n"
    "Status: hypotheses and proposed validation; no validated business winner.\n\n"
    "See [README](README.md), [evidence register](EVIDENCE.md) and "
    "[revision record](CHANGELOG.md).\n\n"
)

def render():
    return HEADER + "\n\n---\n\n".join(
        (ROOT / name).read_text(encoding="utf-8").strip() for name in PHASES
    ) + "\n"

def check_local_links():
    errors = []
    for path in ROOT.rglob("*.md"):
        if any(part.startswith(".") or part == "private-data" or part.startswith("local-") for part in path.relative_to(ROOT).parts):
            continue
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            local = target.split("#", 1)[0]
            if local and not (path.parent / local).exists():
                errors.append(f"{path.name}: missing local link {target}")
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    output = ROOT / "full_report.md"
    expected = render()
    if not args.check:
        output.write_text(expected, encoding="utf-8")
        print("Generated full_report.md")
    errors = check_local_links()
    if not output.exists() or output.read_text(encoding="utf-8") != expected:
        errors.append("full_report.md differs from phase sources; run the generator")
    if errors:
        raise SystemExit("\n".join(errors))
    print("PASS: combined report is synchronized; local Markdown file links resolve.")

if __name__ == "__main__":
    main()
