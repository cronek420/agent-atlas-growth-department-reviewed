# Task Plan

Working task graph for the current phase. Rewritten at the start of each phase by that phase's owner; completed phases are summarized at the bottom rather than deleted.

**Run ID:** `phase-03-2026-07-30-b`
**Phase:** 03 — Governance, Security, Approval, and Autonomy Policies
**Phase owner:** Atlas Orchestrator (Phase 03)
**Date:** 2026-07-30

## Why `-b`: this phase restarted mid-run

A first attempt (`phase-03-2026-07-30-a`) was built entirely on `main`/this branch at `de2c16c` — **before** discovering that a complete, real Phase 02 sat unmerged on `claude/phase-02-capability-registry-c04753` (PR #1, opened 2026-07-29, never merged). That attempt invented `D-036`–`D-042`, which collided with the **real** `D-036`–`D-040` already recorded on the unmerged branch, and its central finding ("Phase 02 was never executed") was true of the stale branch and false of the project.

Caught by the Independent Reviewer during the first attempt's own review pass, verified independently (`git log --all`, `gh pr view 1`, `git merge-base`), escalated to the Project Owner, who chose: **merge PR #1, then redo Phase 03 from scratch.** PR #1 merged 2026-07-30 (commit `acabca8`); this branch was reset to the merged `main`; the first attempt's uncommitted draft (8 policy documents, `policy/`, `tools/`) was discarded, since it had never been committed. Nothing shared or pushed was lost. Full account: this phase's gate report § "What went wrong before this phase started."

## Objective

Create deterministic rules governing what agents may read, write, publish, send, spend, or escalate.

## Prerequisite status

| Item | State |
|---|---|
| Phase 02 gate | **CONDITIONAL PASS**, recorded by the Project Owner 2026-07-29, in `CURRENT_PHASE.md` |
| Phase 02 deliverables | **All six exist and are real**: `CAPABILITY_REGISTRY.md` (141 capability rows), `SKILL_SECURITY_POLICY.md`, `CONNECTOR_ACTIVATION_PLAN.md`, `SKILL_INSTALLATION_PLAN.md`, `CUSTOM_SKILL_BACKLOG.md`, `SKILL_TEST_PLAN.md` |
| Phase 02 independent review | **Completed** (after a first attempt hit an account spend limit) — 21 findings (1 Critical, 8 High, 8 Medium, 4 Low), rubric 3.75 (below `D-028` threshold) |
| **`R-24` — outstanding** | The Critical finding (merge PR #1) is now resolved by this phase's own reconciliation. **Four High/Medium findings remain unremediated per the owner's CURRENT_PHASE.md record.** This is Phase 02's debt, not Phase 03's to fix — noted, not silently absorbed |
| Phase 01 gate | PASS, owner, 2026-07-29, no conditions |
| Phase 00 gate | PASS, owner, 2026-07-28, no conditions |

## What this phase inherits from the real Phase 02 — read before drafting anything

These are direct, load-bearing instructions left in `CURRENT_PHASE.md` by the Phase 02 Owner for whoever runs Phase 03:

1. **`SECURITY_POLICY.md` must cover credential-free external access, not only secrets** (`F-02-03`, `R-21`). Five borrowed-authority classes exist in the observed capability surface — the operator's logged-in browser session, the operator's Claude account, connector grants held in that account, harness-mediated network egress, and plugin-held credentials. None of them requires a value in `.env` or Secret Manager, so a security policy that only governs credentials this project holds misses the exposure that actually matters. **Governing sentence: this project's controls govern the credentials it holds; its exposure is governed by the authority it borrows.**
2. **Boundaries must be expressed in terms of what may be *known*, not which door content came through** (`F-02-02`, `R-23`). A path-based rule (`docs/PROJECT_BOUNDARIES.md` §1/§2, pre-Phase-02) is satisfied by a capability that returns Rough-Draft-Builders-Club content without taking a path argument — same content, no path, rule defeated by construction. Already partially narrowed in `docs/PROJECT_BOUNDARIES.md` §2/§3 by the Phase 02 Owner (a fail-closed narrowing, per `docs/PROJECT_BOUNDARIES.md` §7.4); Phase 03's policies must not silently re-introduce a path-only formulation.
3. **Tool-grant lists are not enforcement** (`F-02-04`). No subagent type is genuinely read-only; `Bash` defeats any "read-only" grant; `ToolSearch` availability is decidable but not itself enforced, because `D-003`'s deterministic-enforcement requirement has no implementation anywhere in this project yet. `AGENT_PERMISSION_MATRIX.md` must not claim to be an enforced boundary — it is a documented least-privilege *intent*, same honesty standard as every other Phase 03 deliverable (`PROPOSED`/`SCAFFOLDED`, never `IMPLEMENTED`).
4. **Trust boundary is drawn at authorship, not retrieval** (`F-02-05`, `CLAUDE.md` §11). A skill or tool description loaded into context before any task begins is untrusted third-party text, in a *stronger* trust position than fetched content because it arrived unbidden. `SECURITY_POLICY.md`'s untrusted-content section must cover this, not only scraped/fetched content.
5. **`Q-017` — "what does 'policy conflicts tested' require" — is explicitly left as Phase 03's own call**, not blocking. This phase answers it (see § "Resolving Q-017" below) rather than leaving it open again.
6. **`CUSTOM_SKILL_BACKLOG.md` assigns Phase 03 the first custom skill, `CSK-01 blast-radius-check`** — a deterministic tool that enumerates prior-phase files a phase's own changes may have falsified, before the gate report is drafted. Full contract at `CUSTOM_SKILL_BACKLOG.md` §"CSK-01". This phase builds it (see Task graph).
7. **`SKILL_SECURITY_POLICY.md` does not discharge `D-027`** — it governs which *capabilities* may be used; `SECURITY_POLICY.md` governs credentials, incident response, and access control generally. Cross-reference, never restate or duplicate.
8. **`CAPABILITY_REGISTRY.md`'s three axes** (maturity ladder `D-010`; implementation class `CLAUDE.md` §3; use-disposition `PERMITTED`/`RESTRICTED`/`PROHIBITED`/`UNRESOLVED`, `D-037`) are a different question from what `AGENT_PERMISSION_MATRIX.md` answers (which **role** may take which **action**). They compose — a capability being `PERMITTED` in the registry does not by itself grant any role permission to use it for a specific action; `AGENT_PERMISSION_MATRIX.md` still gates that. Do not merge the two axes.
9. **Do not reopen or re-litigate Phase 02's gate, its 21 review findings, or `R-24`.** That is the Project Owner's and (if resumed) the Phase 02 Owner's business. Phase 03 notes the inherited risk and moves on.

## Resolving Q-017 — "what does Phase 03's 'Policy conflicts tested' pass condition require?"

**Decision (this phase, recorded as `D-041`):** "Policy conflicts tested" means two distinct, both-required checks:

1. **Structural conflicts within `policy/action_registry.json`** — two rows granting different outcomes to the same (role, verb, resource, statement) — caught mechanically (`tools/policy_check.py`, inherited design from the first attempt, since this part owed nothing to the false premise).
2. **Cross-document prose conflicts** — a policy document's prose describing an outcome that contradicts the registry, or contradicting a sibling policy document. This is **not** fully mechanically checkable (natural-language semantics), so it is tested by an explicit, itemized cross-read performed by the Independent Reviewer and recorded in `REVIEW_REPORT.md`, with the mechanical checker providing an ID/outcome cross-reference as a starting point, not a substitute.

Both must be exercised and their results recorded before the phase can claim this pass condition met.

## Input classification

| Input | Class | Note |
|---|---|---|
| 10 architecture rules; nine gated categories | `CONFIRMED` | `README.md`, `D-001`–`D-011` |
| Human-checkpoint list | `CONFIRMED` | `user-guide/USER_INSTRUCTIONS.md` |
| Filesystem / external-system / action / data / trust boundaries, **as narrowed by Phase 02** | `CONFIRMED` | `docs/PROJECT_BOUNDARIES.md` |
| Secrets mechanics (`.env`, `.env.example`, Secret Manager) | `CONFIRMED` | Phase 01 |
| Maturity ladder, use-disposition vocabulary, `NOT_PRODUCTION_FACING` sentinel | `CONFIRMED` | `D-010`, `D-037`, `D-038` |
| `CAPABILITY_REGISTRY.md`'s 141-row snapshot | `CONFIRMED` (as a dated snapshot) | `D-039` — re-capture before relying on it later |
| "Automate within the gates, never through them" | `CONFIRMED` | `D-019a` + `D-020`, owner-stated |
| Organic-only, zero authorized spend | `CONFIRMED` (prohibition) / `INFERRED` (duration) | `D-016`, `D-016a`, `NG-001` |
| Credential-free / borrowed-authority exposure exists and is unaddressed by prior controls | `CONFIRMED` | `F-02-03`, `R-21` |
| Build-time agent roles | `CONFIRMED` | `CLAUDE.md` §7 |
| **Backup approver / owner-unavailable behaviour** | `UNRESOLVED` | `Q-008` |
| **Personal-data retention periods and jurisdiction** | `UNRESOLVED` | `Q-009` |
| **All numeric thresholds** | `UNRESOLVED` | `D-021`, `NG-004`, `Q-003` |
| Who owns the scheduled-execution host (Google Cloud) | `UNRESOLVED`, urgent per Phase 02 Owner | `Q-014` |
| Which connected connectors are actually authorized | `UNRESOLVED` | `Q-012` |
| Google Drive access | `BLOCKED` | `Q-004` — the project's only `BLOCKED` item |

**Blocking questions for Phase 03:** none. `Q-008`, `Q-009`, `Q-012`, `Q-014` shape content but do not stop the phase from producing its deliverables.

## Task graph

```
T0  Phase Owner: re-read real governing corpus post-merge, resolve Q-017 (D-041),
    author policy/POLICY_CONTRACT.md + policy/action_registry.json
    incorporating F-02-02/F-02-03/F-02-04/F-02-05 and real D-036–D-040
     │
     ▼
T1  ┌─ Security Architect ............ SECURITY_POLICY.md (must cover F-02-03)
    ├─ Policy Designer ............... APPROVAL_POLICY.md → AUTONOMY_POLICY.md → BUDGET_POLICY.md
    ├─ Privacy Reviewer .............. DATA_RETENTION_POLICY.md
    └─ Marketing Ops Reviewer ........ PUBLISHING_POLICY.md, MESSAGING_POLICY.md
     │       (4 agents in parallel, each against the contract + real repo state only)
     ▼
T2  Phase Owner: tools/render_permission_matrix.py → AGENT_PERMISSION_MATRIX.md
     ▼
T3  Phase Owner: tools/policy_check.py (structural conflicts) + negative-control self-test
     ▼
T4  Phase Owner: tools/blast_radius_check.py — build CSK-01 per its full contract
    in CUSTOM_SKILL_BACKLOG.md, run it against this phase's own changes
     ▼
T5  Independent Governance Auditor (fresh; authored nothing under audit)
     ▼
T6  Independent Reviewer (fresh; authored nothing; prose conflict cross-read per Q-017)
     ▼
T7  Phase Owner: address findings, update registers per CSK-01's own output,
    rubric score, PHASE_GATE_REPORT.md, STOP
```

## File ownership — one owner per file

| File | Owner |
|---|---|
| `policy/POLICY_CONTRACT.md`, `policy/action_registry.json` | Phase 03 Owner |
| `SECURITY_POLICY.md` | Security Architect |
| `APPROVAL_POLICY.md`, `AUTONOMY_POLICY.md`, `BUDGET_POLICY.md` | Policy Designer |
| `DATA_RETENTION_POLICY.md` | Privacy Reviewer |
| `PUBLISHING_POLICY.md`, `MESSAGING_POLICY.md` | Marketing Operations Reviewer |
| `AGENT_PERMISSION_MATRIX.md` (generated, never hand-edited) | Phase 03 Owner |
| `tools/render_permission_matrix.py`, `tools/policy_check.py`, `tools/policy_check_selftest.py`, `tools/blast_radius_check.py` | Phase 03 Owner |
| `agent_runs/phase-03/handoffs/*` | Each authoring agent, one file each |
| `agent_runs/phase-03/GOVERNANCE_AUDIT_REPORT.md` | Independent Governance Auditor |
| `agent_runs/phase-03/REVIEW_REPORT.md` | Independent Reviewer |
| `DECISIONS.md`, `findings.md`, `progress.md`, `CURRENT_PHASE.md`, `MASTER_PLAN.md`, `OPEN_QUESTIONS.md`, `RISK_REGISTER.md`, `task_plan.md`, `docs/PROJECT_BOUNDARIES.md` (if narrowing needed) | Phase 03 Owner only |
| `agent_runs/phase-03/PHASE_GATE_REPORT.md` | Phase 03 Owner |

No specialist writes a register. Specialists propose in handoffs; the phase owner records.

## Validation plan

Same core mechanical checks as designed in the first attempt (V-1..V-13; none of that design was false, only its premise about Phase 02), plus:

- **V-16** — CSK-01 (`tools/blast_radius_check.py`) runs clean against this phase's own `changed_files` before the gate report, with `unreadable` empty and every candidate dispositioned.
- **V-17** — Q-017 resolution itself: confirm both the structural check (V-5) and a documented prose cross-read exist and were exercised, not just one of the two.

## Out of scope for Phase 03

- Reopening Phase 02's gate, its 21 findings, or `R-24`.
- Authoring anything belonging to Phase 04+.
- Installing anything, connecting any external system, creating `.env`, obtaining any credential.
- Beginning Phase 04 (`D-007`).

## Completed phases

**Phase 00 — Decision Lock and Scope Control.** PASS (owner, 2026-07-28, unconditional). Rubric 4.00.

**Phase 01 — Workspace, Repository, and Project Memory.** PASS (owner, 2026-07-29, unconditional, against a CONDITIONAL PASS recommendation). Rubric 4.17.

**Phase 02 — Capability Registry and Skill Foundation.** CONDITIONAL PASS (owner, 2026-07-29). All six deliverables real; independent review completed with 21 findings (rubric 3.75); PR #1 merged 2026-07-30 during Phase 03's reconciliation. `R-24` remains open pending remediation of four High/Medium findings — not this phase's to close.

**Phase 03 attempt `-a` (2026-07-30, superseded, never committed).** Built on a stale branch predating the Phase 02 merge; produced 8 policy documents, `policy/action_registry.json`, and a self-tested checker, all discarded when the false premise was discovered. No loss: nothing was committed or pushed. Full account in this phase's gate report.
