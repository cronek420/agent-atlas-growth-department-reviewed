# Task Plan

Working task graph for the current phase. Rewritten at the start of each phase by that phase's
owner; completed phases are summarized at the bottom rather than deleted.

**Run ID:** `phase-04-2026-07-31-a`
**Phase:** 04 — Data Contracts and State Model
**Phase owner:** Atlas Orchestrator (Phase 04)
**Date:** 2026-07-31

## Objective

Define versioned schemas and deterministic lifecycle states before dependent code is built.

## Prerequisite status

| Item | State |
|---|---|
| Phase 03 gate | **PASS**, recorded by the Project Owner 2026-07-30, in `CURRENT_PHASE.md` — an override of the gate report's own CONDITIONAL PASS recommendation, the owner's prerogative under `D-007` |
| Phase 03 deliverables | All 8 policy documents, `policy/POLICY_CONTRACT.md`, `policy/action_registry.json`, `AGENT_PERMISSION_MATRIX.md`, `tools/policy_check.py` (13/13), `tools/policy_check_selftest.py` (12/12) |
| `R-24` — outstanding | Four unremediated High/Medium findings from Phase 02's own independent review, carried forward, **not this phase's to close** (`CURRENT_PHASE.md`) |
| Phase 02 / 01 / 00 gates | PASS / PASS / PASS, no conditions |
| Git | Local repository initialized this session (`git init -b main`), single baseline commit, private remote `cronek420/agent-atlas-growth-department-reviewed` attached and pushed |

## Blocking question resolved before drafting

**`Q-016`** (where do Phase 04's fixtures live) was left as this phase's own call
(`OPEN_QUESTIONS.md`, `CURRENT_PHASE.md`). Resolved as `D-052`:
`schemas/fixtures/<entity>.fixture.json`, colocated with the schema each validates. Full
reasoning: `architecture/DATA_CONTRACTS.md` §1.

## Blocking question NOT resolved, and why that's correct

**`Q-009`** (data-privacy handling for lead/contact data) is `UNRESOLVED` and shapes this phase
(`MASTER_PLAN.md` row 04) but does not block it — it is not `BLOCKED` like `Q-004`, and
`OPEN_QUESTIONS.md`'s own text offers the phase owner an option to propose a default policy for
the owner's approval. **This phase does not exercise that option.** Proposing a retention period,
jurisdiction, or storage substrate would require inventing a number or a legal fact this project
has no basis for (`D-047`, `D-008`) — exactly the failure mode `DATA_RETENTION_POLICY.md` §8
already refused. Instead, `schemas/lead.schema.json` is built as a **structural data contract
only**: it defines field shapes so Phase 17 has a target, carries an explicit inline notice that
instantiating a real record is `DENY` (`ACT-W10`) until `Q-009` resolves, and its fixture uses
placeholder-only values per `DATA_RETENTION_POLICY.md` §7 (extended to fixtures in
`architecture/DATA_CONTRACTS.md` §1). `Q-009` is exactly as open after this phase as before it.

## What this phase inherits — read before drafting anything

1. **`APPROVAL_POLICY.md` §2 already defines the approval state machine** (10 states, `DRAFT`
   initial, six terminal states, four numbered invariants). `schemas/approval.schema.json` and
   `architecture/STATE_MACHINE.md` transcribe it; neither invents a competing one
   (`architecture/DATA_CONTRACTS.md` §6).
2. **`policy/action_registry.json`'s six roles are the closed vocabulary** for any
   "who created/acted on this record" field (`created_by_role`) — never a person's name or a
   newly invented role.
3. **Fail-closed is the house style** (`D-044` for actions, extended here to schema shape via
   `additionalProperties: false` — `architecture/DATA_CONTRACTS.md` §2.2).
4. **No number is invented** (`D-047`). Any numeric threshold this phase might want (retry
   counts, staleness windows, retention periods) stays absent from the schemas unless it is
   already fixed by a governing document; none of the eight schemas needs one to satisfy its pass
   conditions, so none is added.
5. **`DATA_RETENTION_POLICY.md` §2.4 governs `lead.schema.json` absolutely** — this phase changes
   nothing about that file and does not attempt to.
6. **A checker that reports success proves nothing until shown to fail** (`F-01-04`). Schema
   validation this phase performs uses a real validator (Python `jsonschema`, installed this run
   — no such package existed in the repository before) against real fixture files, with a
   documented red-mutation demonstration, not a hand-inspection claim.

## Input classification

| Input | Class | Note |
|---|---|---|
| Approval state machine (10 states, invariants) | `CONFIRMED` | `APPROVAL_POLICY.md` §2 |
| Six-role vocabulary | `CONFIRMED` | `policy/action_registry.json` §`roles` |
| Fail-closed default | `CONFIRMED` | `D-044` |
| No invented numbers | `CONFIRMED` (prohibition) | `D-047` |
| Personal-data collection is `DENY` today | `CONFIRMED` | `DATA_RETENTION_POLICY.md` §2.4, `ACT-W10` |
| Fixture location | `CONFIRMED` (this phase's own decision) | `D-052` |
| Shared envelope / versioning / idempotency / error shape | `CONFIRMED` (this phase's own decision) | `D-053` |
| Numeric thresholds anywhere in a schema (retry counts, TTLs) | `UNRESOLVED` — none used | `D-047` |
| `Q-009` jurisdiction, retention period, storage substrate | `UNRESOLVED`, not this phase's to resolve | `Q-009` |

**Blocking questions for Phase 04: none.** `Q-009` shapes `lead.schema.json`'s content and
operational status; it does not stop the phase from producing its deliverables.

## Task graph

```
T0  Phase Owner: read governing corpus, resolve Q-016 (D-052),
    author architecture/DATA_CONTRACTS.md (shared envelope, versioning, idempotency,
    error shape — D-053), install jsonschema validator
     │
     ▼
T1  ┌─ Data Architect ......... product, brand, content, campaign schemas
    └─ Analytics Engineer ..... experiment, alert, lead schemas (Q-009-aware)
     │       (2 agents in parallel, each against DATA_CONTRACTS.md only —
     │        genuinely independent: neither reads the other's assigned schemas)
     ▼
T2  Workflow State Designer: schemas/approval.schema.json (transcribes APPROVAL_POLICY.md §2)
    + architecture/STATE_MACHINE.md (per-entity lifecycles for all 8 entities,
    citing T1's actual field names — runs after T1, not parallel with it, F-00-07)
     ▼
T3  Schema QA Reviewer (Phase Owner, this run): schemas/fixtures/*.fixture.json (8 files) +
    tools/schema_validate.py, run against every schema, red-mutation demonstrated
     ▼
T4  Phase Owner: integrate — DECISIONS.md, OPEN_QUESTIONS.md (done at T0/T1 boundary for D-052),
    findings.md, progress.md, CURRENT_PHASE.md, MASTER_PLAN.md row 04
     ▼
T5  Independent Reviewer (fresh; authored nothing under review)
     ▼
T6  Phase Owner: address findings, rubric score, PHASE_GATE_REPORT.md, STOP
```

**Sequencing note (`F-00-07`):** T2 depends on T1's actual field choices (state-bearing field
names in `content`, `campaign`, `experiment`) and is deliberately serialized after it, not run in
parallel. T1's two specialists are genuinely independent of each other — neither is told the
other's specific field names, only the shared contract both must follow.

## File ownership — one owner per file

| File | Owner |
|---|---|
| `architecture/DATA_CONTRACTS.md` | Phase 04 Owner |
| `schemas/product.schema.json`, `schemas/brand.schema.json`, `schemas/content.schema.json`, `schemas/campaign.schema.json` | Data Architect |
| `schemas/experiment.schema.json`, `schemas/alert.schema.json`, `schemas/lead.schema.json` | Analytics Engineer |
| `schemas/approval.schema.json`, `architecture/STATE_MACHINE.md` | Workflow State Designer |
| `schemas/fixtures/*.fixture.json` (8 files), `tools/schema_validate.py` | Phase 04 Owner (Schema QA Reviewer role, same run) |
| `agent_runs/phase-04/handoffs/*` | Each authoring agent, one file each |
| `agent_runs/phase-04/REVIEW_REPORT.md` | Independent Reviewer |
| `DECISIONS.md`, `OPEN_QUESTIONS.md`, `findings.md`, `progress.md`, `CURRENT_PHASE.md`, `MASTER_PLAN.md`, `task_plan.md` | Phase 04 Owner only |
| `agent_runs/phase-04/PHASE_GATE_REPORT.md` | Phase 04 Owner |

No specialist writes a register. Specialists propose in handoffs; the phase owner records.

## Validation plan

- **V-1** — every `schemas/*.schema.json` file is syntactically valid JSON and a syntactically
  valid JSON Schema (loads under `jsonschema.Draft202012Validator.check_schema`).
- **V-2** — every fixture in `schemas/fixtures/*.fixture.json` validates against its
  corresponding schema (`jsonschema.Draft202012Validator(schema).validate(record)` for every
  record in the array) — the "Schemas validate fixtures" pass condition, with real command
  output recorded.
- **V-3** — red mutation: for at least one schema, a deliberately invalid fixture record (missing
  required field / wrong type / unexpected `additionalProperties`) is shown to **fail**
  validation, proving V-2 is not vacuously green (`F-01-04`).
- **V-4** — every schema's `status` enum matches the corresponding entity's states in
  `architecture/STATE_MACHINE.md` exactly (no schema drifting from its own state model).
- **V-5** — `schemas/approval.schema.json`'s `status` enum is exactly the 10 states in
  `APPROVAL_POLICY.md` §2, same order, no addition or omission.
- **V-6** — every schema's envelope fields match `architecture/DATA_CONTRACTS.md` §2.1 exactly
  (same seven names, same types).
- **V-7** — `tools/idcheck.py` against every new/changed Markdown file — no dangling `D-`/`Q-`/
  `R-`/`NG-`/`F-` citation, no dangling relative path.
- **V-8** — secret/personal-data-shaped-placeholder scan across `schemas/fixtures/*.fixture.json`
  — no realistic-looking name, email, or phone value anywhere (`architecture/DATA_CONTRACTS.md`
  §1's extension of `DATA_RETENTION_POLICY.md` §7).

## Out of scope for Phase 04

- Reopening Phase 00–03's gates, decisions, or unremediated findings (`R-24`).
- Building any enforcement code, adapter, or runtime for these schemas — `src/` does not exist
  before Phase 16 (`MASTER_PLAN.md`).
- Resolving `Q-009` itself, or proposing specific retention/jurisdiction values for it.
- Installing anything beyond the one local, dependency-free-of-network-account validator package
  needed to mechanically satisfy this phase's own pass condition.
- Beginning Phase 05 (`D-007`).

## Completed phases

**Phase 00 — Decision Lock and Scope Control.** PASS (owner, 2026-07-28, unconditional). Rubric 4.00.

**Phase 01 — Workspace, Repository, and Project Memory.** PASS (owner, 2026-07-29, unconditional, against a CONDITIONAL PASS recommendation). Rubric 4.17.

**Phase 02 — Capability Registry and Skill Foundation.** CONDITIONAL PASS (owner, 2026-07-29). All six deliverables real; independent review completed with 21 findings (rubric 3.75); PR #1 merged 2026-07-30. `R-24` remains open, not this or any later phase's to close.

**Phase 03 — Governance, Security, Approval, and Autonomy Policies.** PASS (owner, 2026-07-30, an override of the gate report's CONDITIONAL PASS recommendation). All eight policy documents, `policy/POLICY_CONTRACT.md`, `policy/action_registry.json`, generated `AGENT_PERMISSION_MATRIX.md`; `tools/policy_check.py` 13/13, `tools/policy_check_selftest.py` 12/12. `Q-008`/`Q-014` resolved by owner delegation (`D-050`, `D-051`).
