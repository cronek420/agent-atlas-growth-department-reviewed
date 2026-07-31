#!/usr/bin/env python3
"""Negative-control self-test for policy_check.py (V-14).

F-01-04: "an unverified checker produces unverified results, and a green check
is not evidence until the checker has been shown to go red." policy_check.py
passing 13/13 against the real deliverables proves nothing on its own. This
script deliberately breaks each property the checker claims to verify and
asserts the checker actually catches the break.

This is the load-bearing evidence for Phase 03's "Testing" and "Failure
handling" rubric scores. If this script reports anything other than
"ALL NEGATIVE CONTROLS CAUGHT", policy_check.py is not trustworthy and must be
fixed before the gate report cites it.

Usage: python tools/policy_check_selftest.py
Exit code 0 iff every fixture was correctly caught (i.e. the checker went red
exactly where it should have).
"""
import copy
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import policy_check as pc  # noqa: E402

ROOT = pc.ROOT


def load_good_registry():
    return pc.load_registry(pc.DEFAULT_REGISTRY)


def expect_fail(name, result, note=""):
    caught = not result.passed
    status = "CAUGHT" if caught else "MISSED (checker did not go red!)"
    print(f"  [{status}] {name}: {result.check_id} -> {result.line().splitlines()[0]}")
    if note:
        print(f"           {note}")
    return caught


results = []

print("=== Negative control 1: fail-closed default broken ===")
reg = load_good_registry()
# Corrupt the default outcome itself.
reg["default_outcome"] = "ALLOW"
r = pc.check_v4_fail_closed(reg)
results.append(expect_fail("default_outcome changed to ALLOW", r))

print("\n=== Negative control 2: contradictory rows introduced ===")
reg = load_good_registry()
victim = copy.deepcopy(reg["actions"][0])
victim["id"] = victim["id"] + "-DUPLICATE"
victim["outcome"] = "ALLOW" if victim["outcome"] != "ALLOW" else "DENY"
reg["actions"].append(victim)
r = pc.check_v5_no_contradictions(reg)
results.append(expect_fail("duplicated action with flipped outcome", r))

print("\n=== Negative control 3: a gated category loses all coverage ===")
reg = load_good_registry()
for a in reg["actions"]:
    if "gated_categories" in a and "GC-05" in a["gated_categories"]:
        a["gated_categories"].remove("GC-05")
r = pc.check_v6_gated_coverage(reg)
results.append(expect_fail("GC-05 (direct outreach) stripped from every action", r))

print("\n=== Negative control 4: invented basis ID ===")
reg = load_good_registry()
reg["actions"][0]["basis"] = list(reg["actions"][0].get("basis", [])) + ["D-999"]
with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
    json.dump(reg, f)
    tmp_registry = Path(f.name)
r = pc.check_v7_basis_ids_resolve(ROOT, tmp_registry)
tmp_registry.unlink()
results.append(expect_fail("nonexistent D-999 cited as a basis", r))

print("\n=== Negative control 5: dangling policy-file reference ===")
reg = load_good_registry()
reg["actions"][0]["policy"] = "NONEXISTENT_POLICY_FILE.md"
r = pc.check_v8_policy_files_exist(reg, ROOT)
results.append(expect_fail("action references a policy file that doesn't exist", r))

print("\n=== Negative control 6: non-owner actor can approve ===")
reg = load_good_registry()
for t in reg["state_machines"]["approval"]["transitions"]:
    if t["to"] == "APPROVED":
        t["actor"] = "PHASE_OWNER"
r = pc.check_v9_approval_machine(reg)
results.append(expect_fail("PHASE_OWNER granted the APPROVED transition instead of PROJECT_OWNER", r))

print("\n=== Negative control 7: terminal state given an outgoing edge ===")
reg = load_good_registry()
reg["state_machines"]["approval"]["transitions"].append(
    {"from": "EXECUTED", "to": "DRAFT", "actor": "PHASE_OWNER", "trigger": "illegal_reopen"}
)
r = pc.check_v9_approval_machine(reg)
results.append(expect_fail("terminal state EXECUTED given an outgoing transition", r))

print("\n=== Negative control 8: autonomy ladder skip edge ===")
reg = load_good_registry()
reg["state_machines"]["autonomy_ladder"]["transitions"].append(
    {"from": "DISABLED", "to": "DRAFT_ONLY", "actor": "PROJECT_OWNER", "trigger": "promote"}
)
r = pc.check_v10_no_skip_edges(reg)
results.append(expect_fail("DISABLED -> DRAFT_ONLY promote edge skips SIMULATION", r))

print("\n=== Negative control 9: emergency-stop edge removed ===")
reg = load_good_registry()
reg["state_machines"]["autonomy_ladder"]["transitions"] = [
    t for t in reg["state_machines"]["autonomy_ladder"]["transitions"]
    if not (t["from"] == "LIMITED_AUTONOMY" and t["to"] == "DISABLED")
]
r = pc.check_v11_estop_reachable(reg)
results.append(expect_fail("LIMITED_AUTONOMY -> DISABLED e-stop edge deleted", r))

print("\n=== Negative control 10: matrix drift ===")
matrix_path = ROOT / "AGENT_PERMISSION_MATRIX.md"
original = matrix_path.read_text(encoding="utf-8")
try:
    matrix_path.write_text(original + "\n<!-- hand-edited drift -->\n", encoding="utf-8")
    r = pc.check_v12_matrix_matches_registry(ROOT)
    results.append(expect_fail("matrix hand-edited after generation", r))
finally:
    matrix_path.write_text(original, encoding="utf-8")

print("\n=== Negative control 11: secret-shaped string injected ===")
with tempfile.TemporaryDirectory() as td:
    fake = Path(td) / "FAKE_POLICY_WITH_SECRET.md"
    fake.write_text(
        "Some policy text.\napi_key: \"AKIAABCDEFGHIJKLMNOP\"\nMore text.\n",
        encoding="utf-8",
    )
    r = pc.check_v13_no_secrets(ROOT, files=[fake])
    results.append(expect_fail("AWS-shaped access key embedded in a fixture file", r))

print("\n=== Negative control 12: malformed JSON ===")
with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
    f.write("{ this is not valid json ]")
    tmp_registry = Path(f.name)
r = pc.check_v2_json_parses(tmp_registry)
tmp_registry.unlink()
results.append(expect_fail("registry file is malformed JSON", r))

print("\n=== Positive control: the real deliverables must still pass cleanly ===")
real_results = pc.run_all()
all_real_pass = all(res.passed for res in real_results)
print(f"  Real registry/deliverables: {sum(1 for r in real_results if r.passed)}/{len(real_results)} passed "
      f"({'OK' if all_real_pass else 'UNEXPECTED FAILURE - investigate before trusting anything above'})")

print()
n_caught = sum(results)
n_total = len(results)
if n_caught == n_total and all_real_pass:
    print(f"ALL {n_total} NEGATIVE CONTROLS CAUGHT. Positive control clean. policy_check.py is trustworthy.")
    sys.exit(0)
else:
    print(f"{n_caught}/{n_total} negative controls caught. "
          f"Positive control {'clean' if all_real_pass else 'FAILED'}.")
    print("policy_check.py has at least one blind spot. Do not cite its PASS results as evidence "
          "until this is fixed.")
    sys.exit(1)
