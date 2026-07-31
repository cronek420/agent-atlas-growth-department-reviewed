#!/usr/bin/env python3
"""Generate AGENT_PERMISSION_MATRIX.md deterministically from policy/action_registry.json.

Never hand-edit AGENT_PERMISSION_MATRIX.md. Edit action_registry.json and re-run this
script. D-042 records why: a hand-maintained matrix drifts silently from whatever
actually governs permissions (D-003 requires deterministic code, not prose, to
enforce them).

Usage: python tools/render_permission_matrix.py [--check]
  --check   Do not write the file; exit 1 if the generated content would differ
            from what's on disk (drift detection, used by policy_check.py / V-12).
"""
import json
import sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = ROOT / "policy" / "action_registry.json"
OUTPUT_PATH = ROOT / "AGENT_PERMISSION_MATRIX.md"

OUTCOME_ICON = {
    "ALLOW": "ALLOW",
    "ALLOW_LOGGED": "ALLOW (logged)",
    "APPROVAL_REQUIRED": "APPROVAL REQUIRED",
    "OWNER_ONLY": "OWNER ONLY",
    "DENY": "DENY",
    "BLOCKED": "BLOCKED",
}


def load_registry():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def esc(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def render(reg: dict) -> str:
    roles = reg["roles"]
    actions = reg["actions"]
    outcome_enum = reg["outcome_enum"]
    strictness = reg["strictness_order"]
    gated = reg["gated_categories"]
    esc_codes = reg["escalation_codes"]
    sm = reg["state_machines"]

    lines = []
    lines.append("# Agent Permission Matrix")
    lines.append("")
    lines.append(
        "**GENERATED FILE — DO NOT HAND-EDIT.** Produced by "
        "`tools/render_permission_matrix.py` from `policy/action_registry.json`, "
        "the machine-readable source of truth (`D-042`). To change a permission, "
        "edit the registry and re-run the script. A hand edit here will be "
        "overwritten and will not match what `tools/policy_check.py` validates."
    )
    lines.append("")
    run_id = reg.get("run_id", "unknown")
    lines.append(f"Generated: {date.today().isoformat()} · Run ID: `{run_id}` · "
                  f"Registry schema: `{reg['schema_version']}`")
    lines.append("")
    lines.append("Full prose justification for these grants lives in the policy documents "
                  "named in each row's **Policy** column. This file is the least-privilege "
                  "grant table (`Permissions` rubric category); the prose documents are the "
                  "reasoning.")
    lines.append("")

    # --- Outcome legend ---
    lines.append("## Outcome legend")
    lines.append("")
    lines.append("Strictness order (leftmost wins when multiple rows match a proposed action): "
                 "`" + "` > `".join(strictness) + "`")
    lines.append("")
    lines.append("| Outcome | Meaning | Agent may execute? |")
    lines.append("|---|---|---|")
    exec_set = set(reg["agent_executable_outcomes"])
    for token, meaning in outcome_enum.items():
        may_exec = "Yes" if token in exec_set else "**Never**"
        if token == "APPROVAL_REQUIRED":
            may_exec = "Yes, after approval"
        lines.append(f"| `{token}` | {esc(meaning)} | {may_exec} |")
    lines.append("")
    lines.append(f"**Default outcome for anything matching no row below: `{reg['default_outcome']}`** "
                 f"({esc(reg['default_outcome_basis'])}).")
    lines.append("")

    # --- Roles ---
    lines.append("## Roles")
    lines.append("")
    lines.append("| Role | Kind | Status | Description |")
    lines.append("|---|---|---|---|")
    for r in roles:
        lines.append(f"| `{r['id']}` | {r['kind']} | {r['status']} | {esc(r['description'])} |")
    lines.append("")

    # --- Per-role matrix ---
    lines.append("## Permission grants by role")
    lines.append("")
    lines.append("One table per role. Within a role, actions are grouped by verb. "
                 "A row's outcome is exactly as recorded in `action_registry.json`; "
                 "this script performs no interpretation.")
    lines.append("")

    role_ids = [r["id"] for r in roles]
    for role_id in role_ids:
        role_actions = [a for a in actions if role_id in a["roles"]]
        if not role_actions:
            continue
        lines.append(f"### {role_id}")
        lines.append("")
        lines.append("| ID | Verb | Resource | Description | Outcome | Basis | Policy | Escalation |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for a in sorted(role_actions, key=lambda x: (x["verb"], x["resource"], x["id"])):
            basis = ", ".join(f"`{b}`" for b in a.get("basis", []))
            escalation = a.get("escalation", "—")
            outcome_disp = OUTCOME_ICON.get(a["outcome"], a["outcome"])
            policy = a.get("policy", "—")
            lines.append(
                f"| `{a['id']}` | {a['verb']} | {a['resource']} | {esc(a['description'])} "
                f"| **{outcome_disp}** | {basis} | {policy} | {escalation} |"
            )
        lines.append("")

    # --- Gated categories cross-reference ---
    lines.append("## The nine gated categories — coverage")
    lines.append("")
    lines.append("Every category must be referenced by at least one action row at "
                 "`APPROVAL_REQUIRED` or stricter (`V-6`).")
    lines.append("")
    lines.append("| ID | Category | Referencing actions | Basis |")
    lines.append("|---|---|---|---|")
    for gc in gated:
        refs = [a["id"] for a in actions if gc["id"] in a.get("gated_categories", [])]
        refs_disp = ", ".join(f"`{r}`" for r in refs) if refs else "*(covered by blanket DENY — see APPROVAL_POLICY.md)*"
        basis = ", ".join(f"`{b}`" for b in gc["basis"])
        lines.append(f"| `{gc['id']}` | {esc(gc['name'])} | {refs_disp} | {basis} |")
    lines.append("")

    # --- Escalation codes ---
    lines.append("## Escalation codes")
    lines.append("")
    lines.append("| Code | Meaning |")
    lines.append("|---|---|")
    for code, meaning in esc_codes.items():
        lines.append(f"| `{code}` | {esc(meaning)} |")
    lines.append("")

    # --- State machines summary ---
    lines.append("## State machines")
    lines.append("")
    lines.append("Full transition tables and invariants are defined in "
                 "`policy/action_registry.json → state_machines` and explained in "
                 "`APPROVAL_POLICY.md` and `AUTONOMY_POLICY.md`. Summary:")
    lines.append("")
    appr = sm["approval"]
    lines.append(f"**Approval:** `{appr['initial']}` initial · terminal states: "
                 + ", ".join(f"`{s}`" for s in appr["terminal"]))
    lines.append("")
    for inv in appr["invariants"]:
        lines.append(f"- {esc(inv)}")
    lines.append("")
    ladder = sm["autonomy_ladder"]
    lines.append("**Autonomy ladder:** `" + "` → `".join(ladder["states"]) + "`")
    lines.append("")
    lines.append(f"Current stage of every production-facing capability: "
                 f"**`{ladder['current_stage_all_capabilities']}`**")
    lines.append("")
    lines.append("Promotion preconditions:")
    lines.append("")
    lines.append("| ID | Requirement | Status | Note |")
    lines.append("|---|---|---|---|")
    for pp in ladder["promotion_preconditions"]:
        lines.append(f"| `{pp['id']}` | {esc(pp['requirement'])} | {pp['status']} | {esc(pp.get('note', ''))} |")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("*Regenerate after any change to `policy/action_registry.json`: "
                 "`python tools/render_permission_matrix.py`*")
    lines.append("")

    return "\n".join(lines)


def main():
    check_only = "--check" in sys.argv
    reg = load_registry()
    content = render(reg)

    if check_only:
        if not OUTPUT_PATH.exists():
            print("AGENT_PERMISSION_MATRIX.md does not exist — run without --check first.")
            sys.exit(1)
        existing = OUTPUT_PATH.read_text(encoding="utf-8")
        # Ignore the generated-date line so --check isn't spuriously red across days.
        norm = lambda s: "\n".join(l for l in s.splitlines() if not l.startswith("Generated: "))
        if norm(existing) != norm(content):
            print("DRIFT DETECTED: AGENT_PERMISSION_MATRIX.md does not match action_registry.json.")
            sys.exit(1)
        print("OK: AGENT_PERMISSION_MATRIX.md matches action_registry.json.")
        sys.exit(0)

    OUTPUT_PATH.write_text(content, encoding="utf-8", newline="\n")
    print(f"Wrote {OUTPUT_PATH} ({len(content.splitlines())} lines) from {REGISTRY_PATH}")


if __name__ == "__main__":
    main()
