"""Score identifiers/fields, not business value or independent expert agreement."""
import argparse
import json
from pathlib import Path

def indexed(path):
    rows = [json.loads(x) for x in Path(path).read_text().splitlines() if x.strip()]
    result = {}
    for row in rows:
        if row["id"] in result:
            raise ValueError("duplicate case id")
        result[row["id"]] = row
    if not result:
        raise ValueError("empty dataset")
    return result

def key(f):
    return (f["doc_ref"], f["operation"], f["kind"], f["parameter"])

def score(outputs, labels):
    if set(outputs) != set(labels):
        raise ValueError("outputs and labels must cover exactly the same case ids")
    tp = fp = fn = exact = escalation_exact = 0
    for cid, output in outputs.items():
        actual = [key(f) for f in output["findings"]]
        if len(set(actual)) != len(actual):
            raise ValueError("duplicate findings")
        actual, expected = set(actual), {key(f) for f in labels[cid]["findings"]}
        tp += len(actual & expected)
        fp += len(actual - expected)
        fn += len(expected - actual)
        a = {(e["doc_ref"], e["operation"], e["reason"]) for e in output["escalations"]}
        b = {(e["doc_ref"], e["operation"], e["reason"]) for e in labels[cid]["escalations"]}
        escalation_exact += a == b
        exact += actual == expected and a == b
    return {"cases": len(labels), "exact_cases": exact, "true_positive": tp,
            "false_positive": fp, "false_negative": fn,
            "precision": tp / (tp + fp) if tp + fp else None,
            "recall": tp / (tp + fn) if tp + fn else None,
            "escalation_exact_cases": escalation_exact,
            "limitations": "Field matching only; evidence correctness, criticality and usefulness require review."}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--outputs", required=True)
    p.add_argument("--labels", required=True)
    p.add_argument("--require-exact", action="store_true")
    args = p.parse_args()
    result = score(indexed(args.outputs), indexed(args.labels))
    print(json.dumps(result, indent=2))
    if args.require_exact and result["exact_cases"] != result["cases"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
