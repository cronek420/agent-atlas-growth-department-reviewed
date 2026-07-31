# Data Contracts — Shared Conventions

**Owner of this file:** Phase 04 Owner, run `phase-04-2026-07-31-a`.
**Status:** `PROPOSED` — see §8 for honest capability classification. These are schema
*contracts*: structural definitions no runtime code yet enforces (no `src/` exists before
Phase 16; `MASTER_PLAN.md` "First source code (`src/`) appears at Phase 16").
**Precedence:** below `CLAUDE.md`, `DECISIONS.md`, `policy/POLICY_CONTRACT.md`,
`policy/action_registry.json`, and `DATA_RETENTION_POLICY.md`. Where this file and those
disagree, that is a defect to raise, not silently reconcile (`CLAUDE.md` §6). This file never
widens a boundary set elsewhere — in particular it never authorizes collecting or storing
personal data (`DATA_RETENTION_POLICY.md` §2.4 governs `schemas/lead.schema.json` regardless of
anything below).

This is the fixed contract every schema in `schemas/` and the lifecycle model in
`STATE_MACHINE.md` conform to. Written first, before any entity schema, so the four specialists
who draft schemas in parallel produce **structurally consistent, independent outputs** rather
than four incompatible envelopes (`CLAUDE.md` §7, Architecture Rule 5) — the same T0-before-fan-
out pattern Phase 03 used for `policy/POLICY_CONTRACT.md`.

---

## 1. Resolving `Q-016` — where fixtures live

**Decision (recorded as `D-052`):** fixtures live at `schemas/fixtures/<entity>.fixture.json`,
one file per entity schema, colocated with the schema it validates against.

**Why colocated, not a `tests/` directory.** `MASTER_PLAN.md` places the first `tests/`
directory at Phase 13, nine phases away — creating one now would pre-empt a decision that phase
owner hasn't made, and Phase 04 has no test *runner* to put in it, only fixtures a validator
script reads directly. Colocating with the schema keeps one owner (`CLAUDE.md` §7) and needs no
speculative directory structure. When Phase 13 does introduce `tests/`, these fixtures can be
referenced from there without moving — `tools/` scripts should read fixtures by explicit path,
never by convention-guessed location, exactly as `tools/idcheck.py` already resolves paths
explicitly rather than assuming a layout.

**Fixture format:** each `<entity>.fixture.json` is a JSON array of 2–4 objects, each a
structurally valid instance of that entity's schema, covering (at minimum) the initial lifecycle
state and one non-initial state from `STATE_MACHINE.md`. Fixtures are validation inputs, not
production seed data — nothing in `schemas/fixtures/` is ever loaded into a running system.

**Personal-data extension of `DATA_RETENTION_POLICY.md` §7 (data minimisation):** fixtures for
`lead.schema.json` (and any field of any other schema typed as a person's name, email, phone, or
similar) must use structurally-described placeholder values only — e.g.
`"contact_name": "fixture-contact-name"`, never a realistic-looking name or a real-shaped email
address. The same discipline `DATA_RETENTION_POLICY.md` applies to policy-document examples
applies here to schema fixtures, for the identical reason: a realistic-looking placeholder
teaches the wrong habit and could be mistaken for a real record by a later, less careful phase.

---

## 2. Schema conventions

**Decision (recorded as `D-053`):** every file in `schemas/*.schema.json` (excluding
`fixtures/`) is JSON Schema **2020-12** (`"$schema": "https://json-schema.org/draft/2020-12/schema"`),
chosen as the current, actively maintained draft with the broadest current validator support —
a reversible phase-owner tooling choice, not an architectural one.

Every entity schema:

- Sets `"$id"` to `https://rdbc.internal/schemas/<entity>.schema.json` — a stable identifier,
  **not a live URL**; nothing resolves it over the network, and no capability may fetch it
  (`ACT-R09`/borrowed-authority and general external-fetch rules are unaffected — this is a
  literal string, not an invoked network address).
- Sets `"additionalProperties": false` at every object level — the fail-closed default already
  used by `policy/action_registry.json` (`D-044`) and `.gitignore` (`docs/PROJECT_BOUNDARIES.md`
  §7.4), applied here to schema shape: an unknown field is a defect to surface, not silently
  accept.
- Declares every non-optional field in `"required"`.
- Carries a top-level `"description"` stating what the entity is and, if applicable, its current
  operational status (e.g. `lead.schema.json` must state the `Q-009` block inline, not only in
  this file).

### 2.1 Shared envelope

Every entity schema's root object includes these fields, defined once here and referenced by
each schema's own `"description"` rather than copy-pasted with drift risk:

| Field | Type | Rule |
|---|---|---|
| `id` | `string`, `format: uuid` | Server-assigned identity. Never client-supplied, never reused. |
| `schema_version` | `string`, semver pattern `^\d+\.\d+\.\d+$` | The exact schema version this record was written against — see §3. Required on every record so a consumer never has to guess which contract shape applies. |
| `idempotency_key` | `string`, `minLength: 1` | See §4. Required on every record. |
| `status` | `string` | Entity-specific enum, defined per entity in `STATE_MACHINE.md`, never redefined here. |
| `version` | `integer`, `minimum: 1` | Optimistic-concurrency counter. Starts at `1` on creation; deterministic code increments it on every accepted mutation (Rule 3, `D-003`) and rejects a write whose `version` does not match the current stored value. |
| `created_at` | `string`, `format: date-time` | ISO 8601 / RFC 3339. Set once, never mutated. |
| `updated_at` | `string`, `format: date-time` | ISO 8601 / RFC 3339. Set on every accepted mutation; `>= created_at`. |
| `created_by_role` | `string`, one of the `roles[].id` values in `policy/action_registry.json` (`PROJECT_OWNER`, `PHASE_OWNER`, `SPECIALIST`, `INDEPENDENT_REVIEWER`, `GOVERNANCE_AUDITOR`, `RUNTIME_AGENT`) | Which role created the record. Not a person's identity — a role token, already a closed, non-personal vocabulary (`policy/action_registry.json` §`roles`). |

No entity schema may omit or rename any envelope field. An entity-specific field never reuses
one of these seven names for a different meaning.

### 2.2 Fail-closed unknown data

Per `DATA_RETENTION_POLICY.md` §2.10 (fail-closed default) applied to schema validation: a
record that fails validation — including via `additionalProperties: false` rejecting an
unexpected field — must not be silently coerced or partially accepted. This is a structural rule
today (no validator runs in production; `src/` does not exist until Phase 16) and an operating
rule from the moment one does.

---

## 3. Versioning and backward compatibility

**Decision (recorded as `D-053`, same row as §2's draft-version choice):**

- Schema changes follow semantic versioning against `schema_version` in §2.1: **MAJOR** for any
  change that could invalidate an existing valid record (removing/renaming a required field,
  narrowing a type or enum, adding a new required field with no default); **MINOR** for additive,
  backward-compatible changes (a new optional field, widening an enum); **PATCH** for
  non-semantic fixes (description text, a corrected `pattern` that matches the same valid set).
- **Existing records are never rewritten to match a newer schema version in place** — this
  restates `D-001`'s append/supersede rule (already binding on `DECISIONS.md`) for entity data.
  A record keeps the `schema_version` it was created under; a future migration (not built by this
  phase — no runtime exists yet) reads old-version records and writes new-version ones as new,
  superseding records, never mutating history.
- A schema file itself, once a version is in use by any fixture or (later) any real record, is
  changed only by incrementing `schema_version` and documenting the change — never silently
  edited in place. This phase's own fixtures are the only consumers today, so this rule is
  aspirational until Phase 13+ gives it teeth, and is recorded now so that phase does not have to
  invent it.

---

## 4. Idempotency keys

**Decision (recorded as `D-053`):** every entity carries a required `idempotency_key` (§2.1).
The rule: **creating a record whose `idempotency_key` matches an existing record of the same
entity type returns the existing record rather than creating a duplicate.** This is the
deterministic-deduplication mechanism Architecture Rule 3 / `D-003` requires and explicitly
assigns to code, not to an LLM agent's judgment.

`idempotency_key` is distinct from `id`: `id` is assigned once a record is accepted;
`idempotency_key` is chosen by whatever is proposing the record (a specialist agent, a future
adapter) *before* acceptance, so a retried request after a timeout or crash is recognized as the
same request rather than a new one. No enforcement code exists yet (no `src/` before Phase 16) —
this section defines the contract a future phase's deduplication code must implement, per
§8's honest classification.

---

## 5. Error shape

**Decision (recorded as `D-053`):** every deterministic-code error surfaced by any future
validator, adapter, or state-machine transition uses this shape:

```json
{
  "error_code": "string — machine-stable, e.g. VALIDATION_REQUIRED_FIELD_MISSING",
  "category": "one of: code | configuration | credentials | permissions | data | dependency | rate_limit | provider_outage | policy | unresolved_decision",
  "message": "string — human-readable, safe to log (never includes a secret or personal-data value)",
  "entity_type": "string — which schema, e.g. content",
  "entity_id": "string (uuid) or null — null if the error occurred before an id was assigned",
  "details": "object or null — structured context, e.g. which field failed which constraint"
}
```

`category`'s ten values are taken verbatim from this phase's own prompt's "FAILURE HANDLING"
classification list, so error handling and phase-failure handling share one vocabulary instead
of two. **`message` and `details` must never contain a secret** (`SECURITY_POLICY.md`) **or
personal data** (`DATA_RETENTION_POLICY.md` §2.4) — an error about a rejected lead record
describes the rejection, not the data that was rejected.

---

## 6. Relationship to the approval state machine

`APPROVAL_POLICY.md` §2 already defines a complete state machine — 10 states, `DRAFT` initial,
six terminal states, four numbered invariants — for the nine gated categories. `schemas/approval.schema.json`
**transcribes that machine's `status` enum and transition table**; it does not define a second,
competing one. Any entity whose lifecycle includes an approval step (content, campaign) carries
its own `status` enum for its own production/publishing lifecycle and references the approval
record by `approval_id` (a `uuid`, nullable until a request is submitted) rather than embedding
approval states inside its own enum. This composition — one entity, one lifecycle, linked to at
most one active approval record — is stated here once so `STATE_MACHINE.md` and every schema
citing it stay consistent. See `STATE_MACHINE.md` for the full per-entity lifecycle definitions.

---

## 7. Role-to-write mapping

Writing any file under `schemas/` (including `fixtures/`) or `architecture/` is `ACT-W01`
(`WRITE REPO_SELF`, `ALLOW` for `PHASE_OWNER`/`SPECIALIST` writing a file assigned to them in
`task_plan.md`). **Writing a real entity *record* — as opposed to a schema or a fixture — is a
different action this phase does not take and no role is granted here:** no runtime exists, no
adapter exists, and `lead.schema.json` records specifically remain `ACT-W10`, `DENY`, regardless
of this file (§1's fixture rule and `DATA_RETENTION_POLICY.md` §2.4 both apply; a fixture is not
a real record and must never be mistaken for one — see §1's placeholder-only rule).

---

## 8. Capability classification

Honest classification per `CLAUDE.md` §3 and `policy/POLICY_CONTRACT.md` §10 — a schema
existing is not the same as a control being enforced.

| What this file establishes | Classification | Why |
|---|---|---|
| The shared envelope (§2.1) | `PROPOSED` | Documented and used consistently by every schema this phase produces; nothing yet parses or enforces it — no `src/` exists before Phase 16. |
| Fail-closed unknown-field rejection (§2.2, `additionalProperties: false`) | `SCAFFOLDED` | Real and mechanically checkable **today** by any JSON Schema validator run against a fixture (this phase does exactly that — see `agent_runs/phase-04/`), but nothing runs that validator automatically or in production yet. |
| Versioning / backward-compatibility policy (§3) | `PROPOSED` | States the rule; no migration tooling exists to enforce it, and no schema has yet had a second version to test it against. |
| Idempotency-key rule (§4) | `PROPOSED` | Field exists in every schema; the deduplication behavior it describes has no implementing code (`D-003` assigns that to a future phase's deterministic code, not this one). |
| Error shape (§5) | `PROPOSED` | A shape for future code to emit; no code emits it yet. |
| Fixture location and format (§1) | `SCAFFOLDED` | Real, present, and exercised this phase — fixtures exist at the stated path and are validated against their schemas with recorded command output. |

Nothing in this document is `IMPLEMENTED`. That is expected and correctly disclosed, not a
defect: Phase 04's objective is the contract, not the enforcement engine.
