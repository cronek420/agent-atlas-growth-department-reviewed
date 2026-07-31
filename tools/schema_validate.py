"""Phase 04 — validate every schemas/*.schema.json against its schemas/fixtures/*.fixture.json.

Satisfies task_plan.md V-1..V-3 (schema well-formedness, fixture validation, red-mutation proof).
Owner: Phase 04 Owner. Requires the `jsonschema` package (installed this run via `pip install
jsonschema` — the first third-party dependency this project's tools/ directory has needed;
recorded in tools/README.md rather than left undisclosed).

Usage:
    python tools/schema_validate.py            # validate all schemas against their fixtures
    python tools/schema_validate.py --selftest  # prove the validator actually catches bad data
"""
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "schemas"
FIXTURE_DIR = SCHEMA_DIR / "fixtures"

ENTITIES = [
    "product", "brand", "content", "campaign",
    "experiment", "alert", "lead", "approval",
]


def load(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def validate_all() -> int:
    failures = 0
    total_records = 0
    for entity in ENTITIES:
        schema_path = SCHEMA_DIR / f"{entity}.schema.json"
        fixture_path = FIXTURE_DIR / f"{entity}.fixture.json"

        if not schema_path.exists():
            print(f"FAIL  {entity}: schema file missing at {schema_path}")
            failures += 1
            continue
        if not fixture_path.exists():
            print(f"FAIL  {entity}: fixture file missing at {fixture_path}")
            failures += 1
            continue

        schema = load(schema_path)
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as e:
            print(f"FAIL  {entity}: schema itself is not a valid JSON Schema 2020-12 document: {e}")
            failures += 1
            continue

        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        records = load(fixture_path)
        if not isinstance(records, list) or len(records) < 1:
            print(f"FAIL  {entity}: fixture must be a non-empty JSON array")
            failures += 1
            continue

        entity_failures = 0
        for i, record in enumerate(records):
            errors = sorted(validator.iter_errors(record), key=lambda e: e.path)
            if errors:
                entity_failures += 1
                for err in errors:
                    print(f"FAIL  {entity}[{i}]: {err.message} (path: {list(err.path)})")
        total_records += len(records)
        if entity_failures:
            failures += entity_failures
        else:
            print(f"PASS  {entity}: schema valid, {len(records)} fixture record(s) all validate")

    print(f"\n{len(ENTITIES)} schemas checked, {total_records} fixture records checked, "
          f"{failures} failure(s).")
    return 1 if failures else 0


def selftest() -> int:
    """Red-mutation proof (F-01-04): deliberately break fixtures and confirm validation catches it.

    A green result above is not evidence by itself until the checker has been shown to fail.
    """
    mutations = []

    # Mutation 1: product — remove a required envelope field.
    product_schema = load(SCHEMA_DIR / "product.schema.json")
    product_fixture = load(FIXTURE_DIR / "product.fixture.json")
    bad = dict(product_fixture[0])
    del bad["created_by_role"]
    mutations.append(("product: required field 'created_by_role' removed", product_schema, bad))

    # Mutation 2: content — wrong type for 'status' (not in enum).
    content_schema = load(SCHEMA_DIR / "content.schema.json")
    content_fixture = load(FIXTURE_DIR / "content.fixture.json")
    bad = dict(content_fixture[0])
    bad["status"] = "NOT_A_REAL_STATE"
    mutations.append(("content: status set to a value outside its enum", content_schema, bad))

    # Mutation 3: lead — unexpected additional property (fail-closed check).
    lead_schema = load(SCHEMA_DIR / "lead.schema.json")
    lead_fixture = load(FIXTURE_DIR / "lead.fixture.json")
    bad = dict(lead_fixture[0])
    bad["unexpected_field_not_in_schema"] = "should be rejected"
    mutations.append(("lead: unrecognized additional property injected", lead_schema, bad))

    # Mutation 4: approval — status APPROVED but decided_by_role left as PHASE_OWNER
    # (violates Invariant 5 / the allOf conditional requiring PROJECT_OWNER).
    approval_schema = load(SCHEMA_DIR / "approval.schema.json")
    approval_fixture = load(FIXTURE_DIR / "approval.fixture.json")
    bad = dict(next(r for r in approval_fixture if r["status"] == "APPROVED"))
    bad["decided_by_role"] = "PHASE_OWNER"
    mutations.append(("approval: APPROVED record with decided_by_role=PHASE_OWNER (Invariant 5 violation)", approval_schema, bad))

    # Mutation 5: approval — decided_by_role asserted but decided_at left null
    # (the gap independent review Finding M-5 found; closed by two new allOf conditionals).
    bad = dict(next(r for r in approval_fixture if r["status"] == "APPROVED"))
    bad["decided_at"] = None
    mutations.append(("approval: decided_by_role set but decided_at=null (M-5 regression check)", approval_schema, bad))

    missed = 0
    for label, schema, bad_record in mutations:
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(validator.iter_errors(bad_record))
        if errors:
            print(f"CAUGHT  {label}")
        else:
            print(f"MISSED  {label}  <-- validator did NOT catch this, checker has a blind spot")
            missed += 1

    print(f"\n{len(mutations)} red mutations attempted, {missed} missed.")
    return 1 if missed else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(validate_all())
