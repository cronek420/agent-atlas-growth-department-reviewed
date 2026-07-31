# MASTER_PLAN.md — Working Plan of Record

Project: Agent Atlas Growth Department (marketing operations for Rough Draft Builders Club)
Owner of this file: phase owner of the current phase — update it at every phase gate.
Created: 2026-07-28 by the Repository Architect, Phase 01, run `phase-01-2026-07-28-a`.

---

## What this file is, and how it relates to `MASTER_LINEAR_BUILD_PLAN.md`

| File | Role |
|---|---|
| `MASTER_LINEAR_BUILD_PLAN.md` | **The original packaged phase list.** Historical source. Defines the 25 phases, the dependency rule, and the release rule. Not edited. |
| `MASTER_PLAN.md` (this file) | **The working plan of record.** Adds gate status, per-phase key deliverables, blocking open questions, milestones, and the question→phase dependency map. Maintained as the project runs. |

Per `D-034`: `MASTER_LINEAR_BUILD_PLAN.md` is retained unmodified as the original
packaged artifact. **Where the two differ in detail, `MASTER_PLAN.md` governs.
Where they conflict on *phase scope*, the conflict is a defect to be raised, not
silently resolved.** Phase numbering, names, and the two rules below are carried
over unchanged, and no such conflict was found while writing this file.

`MASTER_PLAN.md` is named unconditionally in the `READ FIRST` list of every phase
prompt but did not exist through Phase 00 — recorded as `findings.md` `F-00-02`.
This file closes that gap.

---

## The two governing rules

**Dependency rule** (`MASTER_LINEAR_BUILD_PLAN.md`): each phase depends on the
prior phase's gate. A phase may be split internally into parallel specialist
tasks, but the overall path remains linear.

**Release rule** (`MASTER_LINEAR_BUILD_PLAN.md`): **no production launch occurs
before Phase 23 passes and the owner explicitly approves Phase 24.**

Reinforced by Architecture Rule 7 / `D-007`: no phase may auto-start the next.
The owner starts each phase by pasting its prompt. Silence is not approval.

---

## Gate status legend

| Status | Meaning |
|---|---|
| `PASS (owner, date)` | Gate decision recorded by the Project Owner, unconditional |
| `CONDITIONAL PASS (owner, date)` | Gate decision recorded by the Project Owner with one or more **named conditions still open**. The phase counts as passed for the purpose of the next phase's prerequisite, and the conditions remain tracked until closed. *(Added by the Phase 02 Owner 2026-07-29 — the legend had no entry for a status the checklist has always allowed.)* |
| `IN PROGRESS` | Phase started; gate not yet reported |
| `AWAITING GATE DECISION` | Work complete, independent review done, gate report written — the Project Owner has not yet recorded a decision |
| `NOT STARTED` | No work performed |

Gate status is recorded by the **Project Owner** in `CURRENT_PHASE.md`. A phase
gate report recommends; it does not decide.

---

## The 25 phases

Key deliverables are taken from each phase's file in `phase-prompts/` and
summarized tersely. Blocking questions are the open questions from
`OPEN_QUESTIONS.md` whose "Blocks" column names that phase.

| Phase | Name | Gate status | Key deliverables | Blocking open questions |
|---|---|---|---|---|
| 00 | Decision Lock and Scope Control | **PASS (owner, 2026-07-28)** | `DECISIONS.md`, `OPEN_QUESTIONS.md`, `SCOPE.md`, `NON_GOALS.md`, `RISK_REGISTER.md`, `ACCEPTANCE_CRITERIA.md`, `CURRENT_PHASE.md` | — |
| 01 | Workspace, Repository, and Project Memory | **PASS (owner, 2026-07-29)** | `CLAUDE.md`, `README.md`, `MASTER_PLAN.md`, `task_plan.md`, `findings.md`, `progress.md`, `DECISIONS.md`, `.gitignore`, `.env.example`, `docs/PROJECT_BOUNDARIES.md` | — |
| 02 | Capability Registry and Skill Foundation | **CONDITIONAL PASS (owner, 2026-07-29)** — review completed (21 findings, rubric 3.75); **PR #1 merged 2026-07-30**, closing the Critical finding; **four High/Medium findings remain unremediated** (`R-24`, still `OPEN`) | `CAPABILITY_REGISTRY.md`, `SKILL_INSTALLATION_PLAN.md`, `CONNECTOR_ACTIVATION_PLAN.md`, `CUSTOM_SKILL_BACKLOG.md`, `SKILL_SECURITY_POLICY.md`, `SKILL_TEST_PLAN.md` — all six delivered | — (opened `Q-012`–`Q-017`; none blocked this gate) |
| 03 | Governance, Security, Approval, and Autonomy Policies | **IN PROGRESS (2026-07-30)** — run `phase-03-2026-07-30-b`; a first attempt (`-a`) was discarded uncommitted after being built on a pre-merge branch (`F-03-01`) | `SECURITY_POLICY.md`, `APPROVAL_POLICY.md`, `AUTONOMY_POLICY.md`, `BUDGET_POLICY.md`, `PUBLISHING_POLICY.md`, `MESSAGING_POLICY.md`, `DATA_RETENTION_POLICY.md`, `AGENT_PERMISSION_MATRIX.md` | `Q-008`, `Q-017` (resolved by `D-041`) |
| 04 | Data Contracts and State Model | **PASS (owner, 2026-07-31)** — run `phase-04-2026-07-31-a`; all 8 schemas + `architecture/STATE_MACHINE.md` + `architecture/DATA_CONTRACTS.md` written, `tools/schema_validate.py` 8/8 schemas × 20/20 fixtures pass, 5/5 red mutations caught; independent review's 8 findings (2 High, 5 Medium/Low) all fixed before the gate report | `schemas/` — product, brand, content, campaign, approval, experiment, lead, alert; `architecture/STATE_MACHINE.md`, `architecture/DATA_CONTRACTS.md` | `Q-009` (unresolved, does not block; shapes `lead.schema.json` only) |
| 05 | Google Drive Living-Document Control Center | NOT STARTED | `architecture/DRIVE_CONTROL_CENTER.md`, `templates/DRIVE_FOLDER_MAP.md`, `templates/SHEET_SCHEMAS.md`, `templates/DOC_TEMPLATES.md`, `schemas/managed-file.schema.json`, `runbooks/DRIVE_SYNC_RECOVERY.md` | **`Q-004` — `BLOCKED`** |
| 06 | Product and Company Onboarding | NOT STARTED | `product/` — `COMPANY_PROFILE.md`, `PRODUCT_PROFILE.md`, `OFFER_CATALOG.md`, `APPROVED_CLAIMS.md`, `EVIDENCE_REGISTER.md`, `FAQ_AND_OBJECTIONS.md` | `Q-007` |
| 07 | Brand and Creative System | NOT STARTED | `brand/` — `BRAND_BIBLE.md`, `VOICE_AND_TONE.md`, `VISUAL_SYSTEM.md`, `APPROVED_LANGUAGE.md`, `PROHIBITED_LANGUAGE.md`, `ASSET_REGISTER.md` | `Q-006` |
| 08 | Research and Trend Intelligence Engine | NOT STARTED | `architecture/RESEARCH_ENGINE.md`, `research/` — `SOURCE_POLICY.md`, `TREND_SCHEMA.md`, `COMPETITOR_SCHEMA.md`, `CONFIDENCE_RULES.md`; `runbooks/RESEARCH_FAILURES.md` | — |
| 09 | Audience, Offer, and Buyer Psychology Model | NOT STARTED | `strategy/` — `AUDIENCE_PROFILES.md`, `BUYER_JOURNEYS.md`, `OBJECTION_LIBRARY.md`, `OFFER_POSITIONING.md`, `QUICK_BUY_VS_CONSIDERED_BUY.md` | `Q-001` |
| 10 | Platform Strategy and Rollout Selection | NOT STARTED | `strategy/` — `PLATFORM_SCORECARD.md`, `ROLLOUT_WAVES.md`, `CHANNEL_PLAYBOOKS.md`, `PLATFORM_EXIT_RULES.md` | `Q-001`, `Q-002`, `Q-005` |
| 11 | Social Presence Launch Kits | NOT STARTED | `social/ACCOUNT_REGISTER.md`, `social/SETUP_CHECKLISTS/`, `social/PROFILE_COPY/`, `social/CREATIVE_BRIEFS/`, `social/LAUNCH_POSTS/` | `Q-002`, `Q-005` |
| 12 | Content Strategy and Editorial System | NOT STARTED | `content/` — `CONTENT_PILLARS.md`, `EDITORIAL_CALENDAR_SCHEMA.md`, `CAMPAIGN_TAXONOMY.md`, `CONTENT_BRIEF_TEMPLATE.md`, `REPURPOSING_MAP.md` | `Q-001`, `Q-002` |
| 13 | Content Production Agents | NOT STARTED | `directives/content-agents/`, `schemas/content-asset.schema.json`, `templates/content/`, `tests/content/` | `Q-002`, `Q-006` |
| 14 | Copy Testing and Creative Experiment Design | NOT STARTED | `experiments/COPY_TESTING_SOP.md`, `experiments/SCORING_RUBRIC.md`, `experiments/STOPPING_RULES.md`, `schemas/copy-test.schema.json`, `tests/copy-testing/` | — |
| 15 | Approval Queue and Human Review Workflow | NOT STARTED | `architecture/APPROVAL_WORKFLOW.md`, `templates/APPROVAL_QUEUE.md`, `tests/approval/`, `runbooks/APPROVAL_RECOVERY.md` — **`schemas/approval.schema.json` already delivered by Phase 04 (2026-07-31); Phase 15 builds the queue/workflow that operates on it, not a second copy of the schema** | **`Q-004` — `BLOCKED`**, `Q-008` |
| 16 | Publishing and Scheduling Adapters | NOT STARTED | `architecture/PUBLISHING_ADAPTERS.md`, `src/adapters/`, `tests/adapters/`, `runbooks/PUBLISHING_FAILURES.md` — **also owns establishing the Google Cloud scheduled-execution host (`D-051`, resolves `Q-014`)**; spending on it is separately gated | `Q-002`, `Q-005` |
| 17 | Community, Messaging, and Lead Routing | NOT STARTED | `architecture/COMMUNITY_WORKFLOW.md`, `schemas/message.schema.json`, `community/RESPONSE_LIBRARY.md`, `tests/community/` — **`schemas/lead.schema.json` already delivered by Phase 04 (2026-07-31) as a structural contract only; real records remain `DENY` until `Q-009` resolves (`DATA_RETENTION_POLICY.md` §2.4). Phase 17 builds the routing workflow, not a second copy of the schema** | `Q-009` |
| 18 | Analytics, Attribution, and Revenue Data | NOT STARTED | `analytics/METRIC_DICTIONARY.md`, `analytics/ATTRIBUTION_POLICY.md`, `analytics/MANUAL_ENTRY_TEMPLATE.md`, `schemas/metric.schema.json`, `tests/analytics/` | `Q-003`, `Q-009` |
| 19 | Weekly Execution Checklist and Executive Reporting | NOT STARTED | `operations/WEEKLY_RUNBOOK.md`, `operations/WEEKLY_CHECKLIST_TEMPLATE.md`, `operations/EXECUTIVE_SUMMARY_TEMPLATE.md`, `schemas/weekly-run.schema.json`, `tests/weekly-operations/` | `Q-001`, `Q-003`, **`Q-004` — `BLOCKED`** |
| 20 | Organizational Memory and Learning Loop | NOT STARTED | `architecture/MEMORY_SYSTEM.md`, `schemas/memory-entry.schema.json`, `knowledge/WINNING_PATTERNS.md`, `knowledge/FAILED_PATTERNS.md`, `tests/memory/` | — |
| 21 | Alerts, Monitoring, Incident Response, and Recovery | NOT STARTED | `monitoring/ALERT_CATALOG.md`, `monitoring/HEALTH_CHECKS.md`, `runbooks/INCIDENT_RESPONSE.md`, `runbooks/BACKUP_AND_RECOVERY.md`, `schemas/incident.schema.json`, `tests/resilience/` | `Q-008` |
| 22 | Budget Scaling and Paid Growth Guardrails | NOT STARTED | `strategy/BUDGET_SCALING.md`, `strategy/PAID_GROWTH_GATES.md`, `schemas/budget-proposal.schema.json`, `tests/budget-policy/` | — |
| 23 | End-to-End Testing and Production Readiness Audit | NOT STARTED | `tests/e2e/`, `reports/PRODUCTION_READINESS.md`, `reports/SECURITY_REVIEW.md`, `reports/PRIVACY_REVIEW.md`, `reports/MARKETING_QUALITY_REVIEW.md` | — |
| 24 | Controlled Launch, Stabilization, and Handoff | NOT STARTED | `runbooks/CONTROLLED_LAUNCH.md`, `docs/OPERATOR_MANUAL.md`, `docs/DEVELOPER_MANUAL.md`, `docs/TROUBLESHOOTING.md`, `docs/EXTENSION_GUIDE.md`, `reports/LAUNCH_REVIEW.md` | — |

Note on Phase 22: its own prompt scopes it as *design, do not initially activate*,
and its pass conditions require that no agent can authorize spend and that
recommendations remain proposals. The organic-only posture (`D-016`) does not
lapse at this phase — it holds until an explicit owner decision changes it
(`D-016a`, `INFERRED`).

---

## Open question → phase dependency map

Source: `OPEN_QUESTIONS.md` summary table and `CURRENT_PHASE.md`. Nine of eleven
questions remain open; `Q-010` and `Q-011` were resolved by the owner 2026-07-28.

| ID | Question | Status | Blocks phases |
|---|---|---|---|
| `Q-001` | 90-day objective priority ranking | UNRESOLVED | 09, 10, 12, 19 |
| `Q-002` | Final platform rollout order | UNRESOLVED (deferred to Phase 10 by design) | 10, 11, 12, 13, 16 |
| `Q-003` | Numeric KPIs / targets | UNRESOLVED | 18, 19 |
| **`Q-004`** | **Google Drive folder location and access** | **`BLOCKED` — the project's only blocked item** | **05, 15, 19** |
| `Q-005` | Existing social account status | UNRESOLVED | 10, 11, 16 |
| `Q-006` | Brand asset source location | UNRESOLVED | 07, 13 |
| `Q-007` | Which Rough-Draft-Builders-Club files are approved fact sources | UNRESOLVED — **may block Phase 06's start, not just its content** (see note) | 06 |
| `Q-008` | Backup approver / accept single-approver SPOF | ✅ RESOLVED 2026-07-30 (`D-050`) — single-approver structure stands | 03, 15, 21 |
| `Q-009` | Data-privacy handling for lead/contact data | UNRESOLVED — shapes but does not block Phase 04's `lead.schema.json` (structural only) | 04, 17, 18 |
| `Q-012` | Which connected MCP connectors are actually authorized | UNRESOLVED | Accuracy of `docs/PROJECT_BOUNDARIES.md` §3; `R-21` |
| `Q-013` | Change control over the machine-local capability surface | UNRESOLVED | Validity of `CAPABILITY_REGISTRY.md` at every later gate; `R-20` |
| `Q-014` | Which phase owns the scheduled-execution host | ✅ RESOLVED 2026-07-30 (`D-051`) — Phase 16 | 19, plus the scheduled halves of 16, 20, 21, 24 |
| `Q-015` | May the system send notifications to the Project Owner | UNRESOLVED | 19 (delivery), 21 (alerting) |
| `Q-016` | Where Phase 04's fixtures live | ✅ RESOLVED 2026-07-31 (`D-052`) — `schemas/fixtures/` | 04 |
| `Q-017` | What Phase 03's "Policy conflicts tested" requires | ✅ RESOLVED 2026-07-30 (`D-041`) | 03 |

**`Q-004` requires owner action before Phase 05 can execute** against a real
Drive folder; design work for Phase 05 can proceed, folder creation cannot.
**`Q-001` should be answered before Phase 09.**

**Added by Phase 02 (2026-07-29): `Q-014` should be answered soonest of the six new
questions, and sooner than Phase 19.** It is not a scheduling detail. `README.md`
names Google Cloud as the scheduled-automation platform, but **no phase prompt
assigns it any deliverable** — the string appears zero times across all 25 files in
`phase-prompts/`. Left open, the system degrades to owner-triggered manual runs,
which reverses `D-019a` — a decision the owner actually made on 2026-07-28 — without
anyone deciding to reverse it. A second gate compounds it: any hosted scheduler is
metered, and spending is one of the nine approval-gated categories, so resolving
*ownership* does not by itself unblock the capability. See `findings.md` `F-02-08`.

### `Q-007` may be closer to `BLOCKED` than its status suggests

Raised by the Repository Architect (`HANDOFF_REPOSITORY_ARCHITECT.md`, Open Question 3) and carried forward here per Reviewer Finding F-10.

Under the fail-closed reading adopted in `docs/PROJECT_BOUNDARIES.md` §2, the set of approved Rough-Draft-Builders-Club source files is **empty**, so the read pathway grants nothing in practice. Every Phase 06 deliverable — `COMPANY_PROFILE.md`, `PRODUCT_PROFILE.md`, `OFFER_CATALOG.md`, `APPROVED_CLAIMS.md`, `EVIDENCE_REGISTER.md` — is an assertion about RDBC, and **no alternative source is named anywhere in the plan.** Phase 06's own pass conditions forbid inventing product facts.

So Phase 06 may have no authorized source set to work from at all. That is a stronger constraint than "unresolved question affecting content."

**This is recorded, not decided.** `Q-007` remains `UNRESOLVED` rather than being promoted to `BLOCKED`, because promoting it is the Project Owner's call and Phase 06 is five gates away. The owner may also resolve it trivially by naming a file list. Flagged here so Phase 06 does not discover it at the start line.

None of the nine block Phase 01. Two shape it defensively: `Q-007` (no approved
RDBC source file, so the read pathway is documented as empty in practice) and
`Q-009` (no data-privacy policy, so `data/private/` is git-ignored pre-emptively).

---

## Milestones — where the project changes character

Derived from the phase prompts' objectives, deliverables, and pass conditions.

| Milestone | Phase | What changes | Guardrail in force |
|---|---|---|---|
| **Decisions locked** | 00 ✅ | Every material choice carries a status and an owner | Unknowns stay `UNRESOLVED`/`BLOCKED` (`D-008`) |
| **Repository and memory exist** | 01 | Version control (`D-029`), boundaries, and the operating contract exist; nothing was recoverable before this (`R-19`) | No secrets committed. The private GitHub remote is planned, **not created** — owner action (`D-030`, `PROPOSED`) |
| **Capabilities named, not enabled** | 02 ✅ | 141 capabilities classified; nothing installed, enabled, or authorized (`D-036`). **The milestone's own framing turned out to be incomplete:** the project's controls govern credentials it holds, while five classes of path reach external systems on borrowed authority (`F-02-03`) | "No unverified skill enabled" — held: zero capabilities invoked. 86 rows `PROHIBITED`, 69 `IRRELEVANT` |
| **Policies become deterministic** | 03 | Approval, autonomy, security, and permission rules stop being prose and become rules | "Default is fail-closed"; all high-risk actions require approval |
| **First machine-readable contracts** | 04 | First non-Markdown artifacts: eight JSON schemas plus the state machine | "No dependent implementation begins early" |
| **First external system** | 05 | Google Drive — the first system outside this repository | **Currently `BLOCKED` on `Q-004`.** Operations restricted to one dedicated folder; no silent overwrite |
| **First validated product facts** | 06 | The project first asserts things about RDBC | "Pricing not invented"; every claim classified; source traceability verified |
| **First content production** | 13 | Agents generate real marketing assets | Outputs validate against schema; claims checked; every producer has negative tests |
| **First human-approval workflow** | 15 | The approval queue exists — the mechanism the nine gates depend on | Immutable approval history; deterministic state transitions |
| **First publishing capability** | 16 | Adapters that *could* publish exist | **Dry-run first.** "No live publishing without approval"; duplicate prevention tested; retries bounded |
| **Production readiness proven** | 23 | End-to-end workflows, approval-bypass tests, prompt-injection tests, recovery tests | Real-format outputs inspected; critical paths pass |
| **Controlled launch** | 24 | The system operates on a narrow approved channel set | Launch scope narrow **and approved**; no paid spend; four cycles reviewed; rollback ready |

First source code (`src/`) appears at Phase 16; the first `tests/` directory at
Phase 13. Everything before Phase 04 is documentation.

---

## No launch before Phase 23

**No production launch occurs before Phase 23 passes and the owner explicitly
approves Phase 24.** This is the release rule from `MASTER_LINEAR_BUILD_PLAN.md`
and it is not waivable by any agent, gate report, or intermediate phase.

Until then, and in every phase: no publishing, no sending, no production account
creation, no spending, no deployment (`NG-002`, `CLAUDE.md` §6). The maturity
ladder (`D-010`) applies to every production-facing capability with no stage
skipped, and the nine approval gates (`D-011`, `D-020`) hold regardless of
automation level — *automate aggressively within the gates, never through them.*
