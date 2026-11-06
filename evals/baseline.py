"""Check a deliberately small, normalized API/documentation representation.

Not an OpenAPI parser. Never executes examples, fetches URLs or edits sources.
"""

def analyze(case):
    required = {"id", "source", "before", "after", "docs"}
    if not required <= case.keys():
        raise ValueError("case missing required fields")
    if not isinstance(case["id"], str) or not case["id"]:
        raise ValueError("id must be a nonempty string")
    if not isinstance(case["source"], str) or not case["source"]:
        raise ValueError("source provenance required")
    for version in ("before", "after"):
        if not isinstance(case[version], dict):
            raise ValueError("spec must be an object")
        for operation, spec in case[version].items():
            if not isinstance(operation, str) or not isinstance(spec, dict):
                raise ValueError("invalid operation")
            if set(spec) != {"required"} or not isinstance(spec["required"], list):
                raise ValueError("only required parameter lists are supported")
            if any(not isinstance(p, str) or not p for p in spec["required"]):
                raise ValueError("invalid required parameter")
            if len(set(spec["required"])) != len(spec["required"]):
                raise ValueError("duplicate required parameter")
    if not isinstance(case["docs"], list):
        raise ValueError("docs must be a list")
    findings, escalations, seen = [], [], set()
    for doc in case["docs"]:
        if not isinstance(doc, dict) or set(doc) != {"ref", "operation", "params"}:
            raise ValueError("invalid documentation example")
        if not isinstance(doc["ref"], str) or not doc["ref"] or doc["ref"] in seen:
            raise ValueError("unique nonempty doc references required")
        seen.add(doc["ref"])
        op = doc["operation"]
        if not isinstance(op, str) or not isinstance(doc["params"], list):
            raise ValueError("invalid example fields")
        if any(not isinstance(p, str) for p in doc["params"]):
            raise ValueError("parameter names must be strings")
        base = {"doc_ref": doc["ref"], "operation": op}
        if op not in case["before"]:
            escalations.append({**base, "reason": "operation_not_in_baseline"})
            continue
        if op not in case["after"]:
            findings.append({**base, "kind": "removed_operation", "parameter": None,
                             "evidence": {"before": case["before"][op], "after": None},
                             "proposal": "Review or retire this example; replacement is unknown."})
            continue
        new = set(case["after"][op]["required"]) - set(case["before"][op]["required"])
        for param in sorted(new - set(doc["params"])):
            findings.append({**base, "kind": "missing_new_required_parameter", "parameter": param,
                             "evidence": {"before": case["before"][op], "after": case["after"][op]},
                             "proposal": f"Document required parameter {param}; obtain a valid value from the maintainer."})
    return {"id": case["id"], "source": case["source"], "findings": findings,
            "escalations": escalations, "status": "review_required" if findings or escalations else "no_supported_drift"}
