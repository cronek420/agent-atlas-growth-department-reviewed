# State Machine — Lifecycles for This Project's Data Entities

**Owner of this file:** Workflow State Designer, Phase 04, run `phase-04-2026-07-31-a`.
**Status:** `PROPOSED` — see § "Capability classification" at the end. Structural documentation only;
no runtime enforces any transition described here (`src/` does not exist before Phase 16,
`MASTER_PLAN.md`).

**What this file is.** This document has two kinds of content, and they are not the same kind of
work:

1. **§1, the approval state machine, is a transcription, not new work.** `APPROVAL_POLICY.md` §2–§3
   already defines a complete 10-state machine — initial state, six terminal states, a 12-row
   transition table, and five numbered invariants, all reproduced in full below — for every one
   of the nine gated categories (`CLAUDE.md` §4). (Corrected 2026-07-31: an earlier draft of this
   sentence confusingly said both "four numbered invariants" and "five invariants in total" in the
   same breath; §1.3 below has always correctly listed all five — only this summary sentence was
   confusing, per independent review Finding L-2.) `policy/action_registry.json →
   state_machines.approval` is the machine-readable source; `APPROVAL_POLICY.md` §2 is its prose
   restatement. §1 below restates both **verbatim in substance**, citing rather than inventing. No
   state, edge, or invariant is added, removed, or reworded here — `APPROVAL_POLICY.md` §2's own
   header says as much ("No state or edge may be added, removed, or renamed by any policy
   document, including this one") and this file is bound by that the same way `schemas/approval.schema.json` is.
2. **§2 (per-entity lifecycles) is this phase's own structural design work**, built on top of the
   seven entity schemas the Data Architect and Analytics Engineer already wrote this run
   (`schemas/product.schema.json`, `schemas/brand.schema.json`, `schemas/content.schema.json`,
   `schemas/campaign.schema.json`, `schemas/experiment.schema.json`, `schemas/alert.schema.json`,
   `schemas/lead.schema.json`). Each entity's `status` enum is quoted directly from its schema file
   — not paraphrased — and the transition table under each is this document's own reasonable
   construction, since no governing document specifies per-entity transitions the way
   `APPROVAL_POLICY.md` §2 does for approvals. Trigger names in §2 (e.g. `submit_for_review`,
   `mark_active`) are this document's own structural labels, invented for legibility, not sourced
   from any governing file — flagged again per-table and in the citing handoff's "Assumptions."
   **No numeric threshold appears anywhere in §2** (`D-047`): where a transition might plausibly
   need one (an experiment's minimum run duration, a campaign's minimum lead time, an alert's
   time-to-resolve), the cell is left blank or described as "owner/operator judgment, no threshold
   defined," never filled with an invented number.

Inputs read in full before writing this file: `APPROVAL_POLICY.md` (all sections, primarily §2–§3),
`architecture/DATA_CONTRACTS.md` (all sections, primarily §2.1 and §6), `policy/action_registry.json`
(`roles`, `state_machines.approval`), `DECISIONS.md` `D-047`, and all seven entity schema files
listed above, read directly from disk rather than trusted from any secondhand summary.

---

## 1. The approval state machine

Reproduced from `APPROVAL_POLICY.md` §2–§3, which is itself "Reproduced exactly from
`policy/action_registry.json → state_machines.approval` and `policy/POLICY_CONTRACT.md` §6." Governs
`schemas/approval.schema.json`'s `status` field. A deterministic checker (`tools/policy_check.py`)
validates the source policy's conformance to the registry; this file adds no independent claim of
conformance beyond citing that chain.

### 1.1 States

`DRAFT` · `PENDING_APPROVAL` · `APPROVED` · `CHANGES_REQUESTED` · `REJECTED` · `EXPIRED` ·
`WITHDRAWN` · `EXECUTED` · `SUPERSEDED` · `VOIDED`

**Initial state:** `DRAFT`.
**Terminal states (six):** `REJECTED`, `EXPIRED`, `WITHDRAWN`, `EXECUTED`, `SUPERSEDED`, `VOIDED`.
**Non-terminal, non-initial states (three):** `PENDING_APPROVAL`, `APPROVED`, `CHANGES_REQUESTED`.

### 1.2 Transition table

Quoted verbatim from `APPROVAL_POLICY.md` §2:

| From | To | Actor | Trigger |
|---|---|---|---|
| `DRAFT` | `PENDING_APPROVAL` | `PHASE_OWNER` | `submit` |
| `DRAFT` | `WITHDRAWN` | `PHASE_OWNER` | `withdraw` |
| `PENDING_APPROVAL` | `APPROVED` | `PROJECT_OWNER` | `owner_approves` |
| `PENDING_APPROVAL` | `REJECTED` | `PROJECT_OWNER` | `owner_rejects` |
| `PENDING_APPROVAL` | `CHANGES_REQUESTED` | `PROJECT_OWNER` | `owner_requests_changes` |
| `PENDING_APPROVAL` | `EXPIRED` | `DETERMINISTIC_CODE` | `staleness_timer` |
| `PENDING_APPROVAL` | `WITHDRAWN` | `PHASE_OWNER` | `withdraw` |
| `CHANGES_REQUESTED` | `DRAFT` | `PHASE_OWNER` | `revise` |
| `APPROVED` | `EXECUTED` | `DETERMINISTIC_CODE` | `execute_once` |
| `APPROVED` | `EXPIRED` | `DETERMINISTIC_CODE` | `validity_window_elapsed` |
| `APPROVED` | `VOIDED` | `DETERMINISTIC_CODE` | `artifact_digest_mismatch` |
| `APPROVED` | `SUPERSEDED` | `PROJECT_OWNER` | `owner_replaces` |

Notes, quoted from `APPROVAL_POLICY.md` §2:

- **The only door into `APPROVED`** is `PENDING_APPROVAL → APPROVED`, and its only key is held by
  `PROJECT_OWNER`. There is no other edge, from any state, to `APPROVED`, anywhere in this machine.
- `CHANGES_REQUESTED` is not a dead end — it loops back to `DRAFT` via `revise`.
- Once `APPROVED`, an artifact moves only by deterministic code (`execute_once`,
  `validity_window_elapsed`, `artifact_digest_mismatch`) or by the owner explicitly superseding it
  — never by an agent's judgment call.
- `DETERMINISTIC_CODE` is not a member of `policy/action_registry.json`'s six-role `roles`
  vocabulary (`PROJECT_OWNER`, `PHASE_OWNER`, `SPECIALIST`, `INDEPENDENT_REVIEWER`,
  `GOVERNANCE_AUDITOR`, `RUNTIME_AGENT`). It names the automated-actor column of this table itself
  — Architecture Rule 3 / `D-003` requires deterministic code, not an LLM agent, to perform these
  four transitions. `schemas/approval.schema.json`'s `decided_by_role` field includes it as a
  distinct literal for exactly this reason, never conflated with any of the six roles.

### 1.3 The five invariants

Reproduced from `APPROVAL_POLICY.md` §3 ("None is negotiable by any Phase 03 document, including
this one" — extended here: none is negotiable by this document either):

1. **The only transition into `APPROVED` is `PENDING_APPROVAL → APPROVED`, and its only permitted
   actor is `PROJECT_OWNER`.** "This is the entire safety model of the project in one rule."
2. **Silence is never consent. No timer, default, or absence of response may produce `APPROVED`. A
   staleness timer may only produce `EXPIRED`.**
3. **An approval binds to one artifact digest. Any change to the artifact voids it.** Encoded as the
   `artifact_digest_mismatch → VOIDED` edge; `schemas/approval.schema.json`'s `artifact_digest`
   field is what this transition compares against a freshly computed digest at execution time.
4. **An approval is single-use. `EXECUTED` is terminal; no second execution may claim the same
   approval.**
5. **No actor may approve what it authored (`D-006`, `ACT-A03`).** "Registry row `ACT-A01` denies
   the `APPROVE` action to every agent role without exception... no agent role holds the `APPROVE`
   transition at all. Only `PROJECT_OWNER` does."

### 1.4 How `schemas/approval.schema.json` encodes this, beyond prose

`schemas/approval.schema.json`'s `decided_by_role` field enum is restricted to `PROJECT_OWNER`,
`PHASE_OWNER`, and `DETERMINISTIC_CODE` — the only three actors that appear anywhere in §1.2's
transition table's "Actor" column for transitions leaving `PENDING_APPROVAL` or `APPROVED`. None of
`SPECIALIST`, `INDEPENDENT_REVIEWER`, `GOVERNANCE_AUDITOR`, or `RUNTIME_AGENT` is a valid value for
this field at all — the schema cannot represent one of those four roles deciding an approval, not
even as a mistake a downstream implementer could accidentally allow. In addition, the schema's
`allOf`/`if`/`then` blocks require `decided_by_role` to equal `PROJECT_OWNER` exactly when `status`
is `APPROVED`, `REJECTED`, `CHANGES_REQUESTED`, or `SUPERSEDED`; `PHASE_OWNER` exactly when `status`
is `WITHDRAWN`; and `DETERMINISTIC_CODE` exactly when `status` is `EXPIRED`, `EXECUTED`, or
`VOIDED`. This is a JSON Schema-level guardrail checkable by any 2020-12 validator today — it is
**not** a substitute for the actual enforcement code Architecture Rule 3 still assigns to a future
phase (no `src/` exists), and it does not by itself stop a future writer from fabricating a false
`decided_by_role` value; it only stops the shape from being internally inconsistent once a value is
asserted.

---

## 2. Per-entity lifecycles

Each subsection below quotes the entity's `status` enum directly from its schema file (verified by
direct read, per this file's intro), states the initial and terminal state(s), and gives a
transition table this document constructs (not sourced from a governing file — see intro §2 and
the citing handoff's "Assumptions" for which parts are invented labels vs. directly citable facts).

### 2.1 `product` (`schemas/product.schema.json`)

Quoted enum: `["DRAFT", "ACTIVE", "DEPRECATED", "RETIRED"]`.
**Initial:** `DRAFT`. **Terminal:** `RETIRED`.

| From | To | Trigger (invented label) | Notes |
|---|---|---|---|
| `DRAFT` | `ACTIVE` | `launch_offering` | Product schema note: pricing is `pricing_approval_id`-gated (GC-02); this transition does not itself require the approval, but any external-facing price statement made about the now-`ACTIVE` product does (`APPROVAL_POLICY.md` §1 GC-02). |
| `DRAFT` | `RETIRED` | `withdraw_before_launch` | A product may be abandoned before ever going active. |
| `ACTIVE` | `DEPRECATED` | `begin_phase_out` | Still referenced by existing commitments/content. |
| `ACTIVE` | `RETIRED` | `retire_directly` | Direct retirement without a deprecation period — no minimum dwell time is defined (`D-047`: no threshold invented). |
| `DEPRECATED` | `RETIRED` | `complete_phase_out` | No minimum or maximum deprecation duration is defined (`D-047`). |
| `DEPRECATED` | `ACTIVE` | `reinstate` | Reversal of a deprecation decision — included for completeness; no governing document confirms or forbids this edge, flagged as an assumption. |

`pricing_approval_id` composition: this field is not a `status` value and is not part of the table
above. It links to an `approval.schema.json` record (or is `null`) independent of where `product`
sits in this lifecycle — a product can be `ACTIVE` with a `null` `pricing_approval_id` if its
current pricing has never been (or no longer needs to be) approved-and-stated externally; the two
are orthogonal per `product.schema.json`'s own description.

### 2.2 `brand` (`schemas/brand.schema.json`)

Quoted enum: `["DRAFT", "ACTIVE", "SUPERSEDED"]`.
**Initial:** `DRAFT`. **Terminal:** `SUPERSEDED`.

| From | To | Trigger (invented label) | Notes |
|---|---|---|---|
| `DRAFT` | `ACTIVE` | `adopt` | Becomes the current, in-use version. `brand.schema.json`'s own description notes at most one record is *expected* to be `ACTIVE` at a time, but the schema does not enforce this — a future phase's deterministic code would (Architecture Rule 3 / `D-003`), not this document. |
| `ACTIVE` | `SUPERSEDED` | `supersede` | Fires the moment a newer version reaches `ACTIVE` — this document does not specify whether `supersede` is a separate action or an automatic side effect of the newer record's `adopt`; that is an implementation choice for whichever future phase builds this, consistent with `D-001`'s general append/supersede rule. |
| `DRAFT` | `SUPERSEDED` | *(no edge)* | Not modeled: a `DRAFT` brand record that never became `ACTIVE` has nothing to supersede. If a `DRAFT` is abandoned, this lifecycle has no terminal state for that case today — flagged as an open question. |

### 2.3 `content` (`schemas/content.schema.json`)

Quoted enum: `["DRAFT", "READY_FOR_REVIEW", "SCHEDULED", "PUBLISHED", "ARCHIVED"]`.
**Initial:** `DRAFT`. **Terminal:** `ARCHIVED`. `PUBLISHED` is structurally defined but, per this
schema's own top-level description, **cannot currently be reached by any lawful path in this
project** — `PUBLISHING_POLICY.md` resolves all publishing to `DENY` today (`ACT-P01`, `ACT-P04`,
`ACT-P05`), and no capability may skip a stage of the `D-010` maturity ladder.

| From | To | Trigger (invented label) | Notes |
|---|---|---|---|
| `DRAFT` | `READY_FOR_REVIEW` | `submit_for_review` | Authoring is complete; content is ready for an approval request to be submitted **against it** (`APPROVAL_POLICY.md` §4) — see § "Relationship to the approval state machine" below for exactly how this composes with §1. |
| `READY_FOR_REVIEW` | `DRAFT` | `return_to_draft` | Author or reviewer sends it back before any approval request is even submitted — distinct from the approval machine's own `CHANGES_REQUESTED → DRAFT` (`revise`) edge, which only applies once an approval record exists. |
| `READY_FOR_REVIEW` | `SCHEDULED` | `schedule_after_approval` | Only sensible once the linked `approval_id` record has reached `APPROVED` (see composition rule below) — this table does not encode that as a JSON-Schema-level constraint (cross-schema conditionals are out of scope for a Phase 04 structural contract), only as a documented expectation. |
| `SCHEDULED` | `PUBLISHED` | `publish` | Structurally defined, currently unreachable in practice (`ACT-P04`/`ACT-P05` `DENY`) — see this subsection's header note. |
| `SCHEDULED` | `DRAFT` | `unschedule` | Pulled back before publishing, e.g. because the linked approval was superseded or voided. |
| `PUBLISHED` | `ARCHIVED` | `archive_published` | Retained for record-keeping. |
| `DRAFT` \| `READY_FOR_REVIEW` \| `SCHEDULED` | `ARCHIVED` | `archive_unpublished` | A content item may be retired without ever publishing. |

### 2.4 `campaign` (`schemas/campaign.schema.json`)

Quoted enum: `["DRAFT", "PLANNED", "ACTIVE", "PAUSED", "COMPLETED", "ARCHIVED"]`.
**Initial:** `DRAFT`. **Terminal:** `ARCHIVED` (also, functionally, `COMPLETED` unless a completed
campaign can still be archived — modeled below as `COMPLETED → ARCHIVED` remaining available, so
`ARCHIVED` is this lifecycle's single true terminal state).

| From | To | Trigger (invented label) | Notes |
|---|---|---|---|
| `DRAFT` | `PLANNED` | `finalize_scope` | Scope (`product_ids`/`content_ids`/timing) is finalized and, where applicable, campaign-level approval has been requested or granted (see composition rule below). |
| `PLANNED` | `ACTIVE` | `start` | No minimum lead time between planning and start is defined (`D-047`; also noted directly in `campaign.schema.json`'s own `planned_start_at` description). |
| `PLANNED` | `DRAFT` | `unplan` | Scope needs rework before starting. |
| `ACTIVE` | `PAUSED` | `pause` | Temporary halt, resumable — distinct from `ARCHIVED`'s terminal retirement, per `campaign.schema.json`'s own `status` description. |
| `PAUSED` | `ACTIVE` | `resume` | |
| `ACTIVE` | `COMPLETED` | `conclude` | Ran its planned course normally. |
| `PAUSED` | `ARCHIVED` | `abandon_paused` | Paused indefinitely rather than resumed. |
| `COMPLETED` | `ARCHIVED` | `archive_completed` | |
| `DRAFT` \| `PLANNED` | `ARCHIVED` | `archive_unstarted` | Retired before ever going active. |

### 2.5 `experiment` (`schemas/experiment.schema.json`)

Quoted enum: `["DRAFT", "RUNNING", "CONCLUDED", "ARCHIVED"]`.
**Initial:** `DRAFT`. **Terminal:** `ARCHIVED`.

Composes with the separate `outcome` enum on the same schema (`["NOT_YET_CONCLUDED",
"WINNER_DECLARED", "INCONCLUSIVE"]`), which is **not** a second `status`-like lifecycle but a
result classification set once, at the same moment `status` reaches `CONCLUDED` — `experiment.schema.json`'s
own description: "`outcome`... record[s] the *result* of an evaluation performed elsewhere; this
schema does not perform or validate that evaluation."

| From | To | Trigger (invented label) | Notes |
|---|---|---|---|
| `DRAFT` | `RUNNING` | `start_experiment` | Sets `started_at`. No minimum variant count or minimum run duration is defined (`D-047`, and stated directly in `experiment.schema.json`'s own `variants`/`concluded_at` descriptions). |
| `DRAFT` | `ARCHIVED` | `abandon_before_start` | |
| `RUNNING` | `CONCLUDED` | `conclude_experiment` | Sets `concluded_at` and `outcome` (to `WINNER_DECLARED` or `INCONCLUSIVE`) together — `outcome` should never be set to anything but `NOT_YET_CONCLUDED` before `status` reaches `CONCLUDED`, though this document does not encode that pairing as a schema-level conditional (out of scope, per §2.3/2.4's identical judgment call on cross-field constraints). |
| `RUNNING` | `ARCHIVED` | `abandon_running` | Abandoned before reaching a conclusion; `outcome` would remain `NOT_YET_CONCLUDED`. |
| `CONCLUDED` | `ARCHIVED` | `archive_concluded` | |

### 2.6 `alert` (`schemas/alert.schema.json`)

Quoted enum: `["NEW", "ACKNOWLEDGED", "INVESTIGATING", "RESOLVED", "CLOSED"]`.
**Initial:** `NEW`. **Terminal:** `CLOSED`.

| From | To | Trigger (invented label) | Notes |
|---|---|---|---|
| `NEW` | `ACKNOWLEDGED` | `acknowledge` | Sets `acknowledged_by_role`/`acknowledged_at`. |
| `NEW` | `CLOSED` | `close_without_triage` | E.g. an immediately obvious duplicate or false positive — `resolution_notes` records which, per the schema's own `status` description. |
| `ACKNOWLEDGED` | `INVESTIGATING` | `begin_investigation` | |
| `ACKNOWLEDGED` | `CLOSED` | `close_after_ack` | Closed without a full investigation (e.g. determined to be a duplicate after acknowledgment). |
| `INVESTIGATING` | `RESOLVED` | `resolve` | Sets `resolved_at`/`resolution_notes`. No maximum time-to-resolve is defined (`D-047`, also stated directly in `alert.schema.json`'s own `resolved_at` description). |
| `INVESTIGATING` | `CLOSED` | `close_after_investigation` | Investigated but closed without resolution (e.g. determined to be a false positive). |
| `RESOLVED` | `CLOSED` | `close_resolved` | |

### 2.7 `lead` (`schemas/lead.schema.json`) — structurally defined, operationally blocked

**This lifecycle is presented in the table below on exactly the same structural footing as the six
above — the same shape of table, the same citation discipline. The caveat that makes it different
belongs in this prose, not in the diagram:** per `lead.schema.json`'s own top-level description and
`DATA_RETENTION_POLICY.md` §2.4, **instantiating a real record against this schema — and therefore
ever executing any transition below against a real person's data — is `DENY`** (`policy/action_registry.json`
`ACT-W10`, every role including `RUNTIME_AGENT`, no exception) **until `Q-009` (data-privacy
handling) is resolved by the Project Owner AND a storage substrate outside this repository's Git
history is decided.** `Q-009` resolving alone does not lift this — the Git-history constraint is
separate and absolute (`DATA_RETENTION_POLICY.md` §2.4, §4). Nothing in this document authorizes
collecting, importing, or storing any actual person's name, email, phone number, or other
identifying detail. The table below defines the shape a real lead's routing *would* follow once
unblocked — defining it now does not authorize using it today, exactly as `lead.schema.json` states
of its own `status` field.

Quoted enum: `["NEW", "CONTACTED", "QUALIFIED", "CONVERTED", "LOST", "ARCHIVED"]`.
**Initial:** `NEW`. **Terminal:** `CONVERTED`, `LOST`, `ARCHIVED` (three terminal states — the
richest terminal set of the seven entities, reflecting that a lead can end in three qualitatively
different outcomes rather than one).

| From | To | Trigger (invented label) | Notes |
|---|---|---|---|
| `NEW` | `CONTACTED` | `first_outreach` | Subject to `MESSAGING_POLICY.md`'s own consent gating (`ACT-S04`, `ACT-S05`), not restated here, per `lead.schema.json`'s own `status` description. Also gated by direct outreach being `GC-05` (`APPROVAL_POLICY.md` §1) — this transition is doubly gated (consent AND approval-category), neither of which this table enforces structurally. |
| `NEW` | `ARCHIVED` | `archive_unqualified` | |
| `CONTACTED` | `QUALIFIED` | `qualify` | |
| `CONTACTED` | `LOST` | `mark_lost_pre_qualification` | |
| `QUALIFIED` | `CONVERTED` | `convert` | |
| `QUALIFIED` | `LOST` | `mark_lost_post_qualification` | |
| `CONVERTED` \| `LOST` | `ARCHIVED` | `archive_outcome` | Included for completeness; whether a `CONVERTED`/`LOST` record is ever archived separately, or whether those are themselves treated as terminal without a further `ARCHIVED` step, is unconfirmed — flagged as an open question. |

`consent_status` (separate enum: `["UNKNOWN", "GRANTED", "DECLINED", "WITHDRAWN"]`) composes with
this table the same way `experiment.outcome` composes with `experiment.status` in §2.5 — a
parallel classification, not a second lifecycle, and one this document does not attempt to
transition-table on its own, per `lead.schema.json`'s own description: "whether consent must be
obtained before outreach, how it is captured, and how an opt-out is honored are owned entirely by
`MESSAGING_POLICY.md`... not restated here."

---

## 3. Relationship to the approval state machine (`content`, `campaign`, `experiment`, `product`)

Per `architecture/DATA_CONTRACTS.md` §6: "Any entity whose lifecycle includes an approval step
(content, campaign) carries its own `status` enum for its own production/publishing lifecycle and
references the approval record by `approval_id`... rather than embedding approval states inside its
own enum. This composition — one entity, one lifecycle, linked to at most one active approval
record..." `experiment.schema.json` and `product.schema.json` extend the same pattern (`approval_id`
and `pricing_approval_id` respectively), per each schema's own description read directly from disk.

**How the two machines actually compose, concretely:**

- **`content`:** `content.approval_id` is `null` until a request exists. The content item's own
  `status` moves `DRAFT → READY_FOR_REVIEW` (§2.3) independent of the approval record's state — an
  item can sit in `READY_FOR_REVIEW` before any approval request is even submitted. Once submitted,
  a new `approval.schema.json` record is created in `DRAFT` and then `PENDING_APPROVAL` (§1), and
  `content.approval_id` is set to point at it. `content.status` should not advance to `SCHEDULED`
  until the linked approval reaches `APPROVED` — a documented expectation, not a schema-level
  cross-reference constraint (JSON Schema cannot check a foreign record's field). If the linked
  approval reaches `REJECTED`, `EXPIRED`, `WITHDRAWN`, or `VOIDED`, `content.status` is expected to
  return to `DRAFT` (or move to `ARCHIVED`) rather than silently staying `READY_FOR_REVIEW` — again
  a documented expectation for a future phase's deterministic code to enforce, not something this
  schema pair enforces today.
- **`campaign`:** identical composition via `campaign.approval_id`, kept **separate from** each
  linked content item's own `approval_id` — a campaign bundling a discount (`GC-03`) or a timed
  push into a controversial topic (`GC-07`) can itself require sign-off distinct from approving its
  constituent content pieces one at a time (`campaign.schema.json`'s own `approval_id` description,
  Data Architect's stated reasoning).
- **`experiment`:** identical composition via `experiment.approval_id`, kept separate from each
  variant's own linked `content.approval_id` — mirrors `campaign`'s reasoning exactly, per
  `experiment.schema.json`'s own description.
- **`product`:** composition via `pricing_approval_id` specifically (not a generic `approval_id`
  field name) — `product.schema.json` deliberately carries no raw price value at all, per that
  schema's own top-level description, precisely so a price cannot be represented without a
  governing approval link.

**What never happens, per `DATA_CONTRACTS.md` §6 and restated here for this file's own scope:** no
entity's own `status` enum contains any of the 10 approval states (`DRAFT`* being the one
name-collision — `content.status`'s `DRAFT` and `approval.status`'s `DRAFT` are different enums on
different schemas that happen to share a token; they are never the same field and never read as
interchangeable). No approval record's `status` field is ever set by reading an entity's own
`status` field, or vice versa — the two machines are linked by id reference only.

---

## Capability classification

Honest classification per `CLAUDE.md` §3 and `architecture/DATA_CONTRACTS.md` §8 — a lifecycle
being documented is not the same as a control being enforced.

| What this file establishes | Classification | Why |
|---|---|---|
| §1, the approval state machine (transcription of `APPROVAL_POLICY.md` §2) | `PROPOSED` | Faithfully restated and cross-checked against `policy/action_registry.json → state_machines.approval` (10 states, 12 transitions — both counts match exactly; corrected 2026-07-31 after independent review found the original "11 states/edges" summary count did not match either figure, `REVIEW_REPORT.md` Finding M-3); no runtime executes any transition (`src/` does not exist before Phase 16; the approval queue itself is Phase 15). |
| §1.4, `schemas/approval.schema.json`'s structural `decided_by_role`/`requested_by_role` guardrails | `SCAFFOLDED` | Real and mechanically checkable **today** by any JSON Schema 2020-12 validator — demonstrated this phase with both `Draft202012Validator.check_schema` and targeted valid/invalid record checks (see `agent_runs/phase-04/handoffs/HANDOFF_WORKFLOW_STATE_DESIGNER.md` "Tests run"). Not itself the deterministic enforcement code Architecture Rule 3 requires — a JSON Schema conditional cannot stop a false value from being asserted in the first place, only catch shape-level inconsistency once one is. |
| §2, the seven per-entity lifecycles and their transition tables | `PROPOSED` | `status` enums are directly quoted, real, and fixed in already-written schema files; the transition tables connecting them are this document's own reasonable construction, not sourced from any governing document, and no code parses or enforces them. |
| §3, approval/entity composition rules (`approval_id` linkage) | `PROPOSED` | States the intended composition, consistent with `DATA_CONTRACTS.md` §6; nothing checks referential integrity or cross-schema state consistency today (`architecture/DATA_CONTRACTS.md` §7 — no runtime enforces any `*_id` reference across schemas). |

Nothing in this document is `IMPLEMENTED`. That is expected and correctly disclosed, not a defect:
Phase 04's objective is the contract and its documented lifecycle, not an enforcement engine.
