# Agent Handoff

- Run ID: `phase-04-2026-07-31-a`
- Phase: 04 — Data Contracts and State Model
- Agent: Analytics Engineer (Specialist)
- Assignment: Draft `schemas/experiment.schema.json`, `schemas/alert.schema.json`,
  `schemas/lead.schema.json` per `task_plan.md` row 124 ("Analytics Engineer ..... experiment,
  alert, lead schemas (Q-009-aware)").
- Files owned: `schemas/experiment.schema.json`, `schemas/alert.schema.json`,
  `schemas/lead.schema.json`, this handoff.

## Facts and evidence

- `architecture/DATA_CONTRACTS.md` is the binding contract for every schema in `schemas/`: JSON
  Schema 2020-12, the seven-field shared envelope (§2.1: `id`, `schema_version`,
  `idempotency_key`, `status`, `version`, `created_at`, `updated_at`, `created_by_role`),
  `additionalProperties: false` at every object level (§2.2), semver `schema_version` policy
  (§3), the `idempotency_key` dedup rule (§4), the shared error shape and its nine-value
  `category` vocabulary (§5), and the approval-composition rule (§6: an entity with an approval
  step carries its own `status` enum and links to `schemas/approval.schema.json` by
  `approval_id`, never a merged enum).
- `policy/action_registry.json` `roles` array defines exactly six role tokens:
  `PROJECT_OWNER`, `PHASE_OWNER`, `SPECIALIST`, `INDEPENDENT_REVIEWER`, `GOVERNANCE_AUDITOR`,
  `RUNTIME_AGENT`. Used verbatim for `created_by_role` (all three schemas) and
  `acknowledged_by_role` (`alert.schema.json`).
- `DECISIONS.md` `D-047`: no numeric threshold (retry count, TTL, statistical-significance
  figure, confidence level, retention period, budget figure) may be invented. Applied here: no
  `minItems` on `experiment.variants`, no significance/confidence value anywhere in
  `experiment.schema.json`, no time-to-resolve or dwell-time figure in `alert.schema.json`, no
  consent-expiry period in `lead.schema.json`.
- `DATA_RETENTION_POLICY.md` §2.4, §2.10, §4, §6, §7 (read in full, as instructed) establish:
  personal data (names, emails, phones, any lead/contact/customer record) is `DENY` to collect
  or store for every role including `RUNTIME_AGENT`, with no exception, until `Q-009` resolves
  (`policy/action_registry.json` `ACT-W10`); Git has no real deletion, so even after `Q-009`
  resolves, personal data cannot live in this repository's history — a separate storage
  substrate decision is also required (§4); consent-record retention/substrate is a distinct,
  also-`UNRESOLVED` question owned partly by `MESSAGING_POLICY.md` (§6); and fixtures must use
  structurally-described placeholders, never realistic-looking values (§7, extended by
  `architecture/DATA_CONTRACTS.md` §1).
- `architecture/DATA_CONTRACTS.md` §1 / `D-052`: fixtures live at
  `schemas/fixtures/<entity>.fixture.json`, colocated with the schema — not written by this
  agent (a different owner builds fixtures later per `task_plan.md`).
- Read `schemas/content.schema.json` and `schemas/campaign.schema.json` (already drafted
  concurrently by the Data Architect) purely as a style reference, per the assignment's note
  that my work does not depend on their content. Matched their conventions: verbatim envelope
  property blocks, `status` enum reasoning spelled out value-by-value in each `description`, and
  the `approval_id`-links-rather-than-merges pattern for `experiment.schema.json`.

## Assumptions

Stated explicitly, per `findings.md` F-00-05 — a clean "no assumptions" claim is a red flag, not
a success. Every enum value and structural choice below was my own design call, not dictated by
a governing file, unless otherwise noted:

1. **`experiment.status` enum** (`DRAFT`, `RUNNING`, `CONCLUDED`, `ARCHIVED`) — my own choice,
   using the four values suggested in the assignment prompt as-is. Reasoning: mirrors the
   DRAFT→active→terminal shape already used by `content.status` and `campaign.status`, and gives
   `STATE_MACHINE.md` a small, unambiguous transition set to design against.
2. **`experiment.outcome` enum** (`NOT_YET_CONCLUDED`, `WINNER_DECLARED`, `INCONCLUSIVE`) — my
   own choice, using the values suggested in the assignment prompt. This is deliberately a
   second, orthogonal axis from `status` (an experiment can be `CONCLUDED` and `INCONCLUSIVE` at
   the same time) rather than folded into `status`, for the same reason `DATA_CONTRACTS.md` §6
   keeps approval state separate from entity state.
3. **`experiment.variants` shape** — I designed this as an array of `{variant_label, content_id}`
   objects rather than a flat `content_ids` array, so a variant that has been planned but not
   yet authored (`content_id: null`) is still representable, and so `winning_variant_label` has
   something stable to reference. This is not dictated anywhere; a different specialist might
   reasonably have modeled variants differently (e.g. as separate content records with a shared
   `experiment_id` back-reference instead of an embedded array). I did not add `minItems` to this
   array — see item 7 below.
4. **`experiment.approval_id`** — I added an experiment-level approval link, mirroring
   `campaign.schema.json`'s pattern, on the reasoning that an experiment whose variants
   collectively touch a gated category (CLAUDE.md §4) may need sign-off at the experiment level
   distinct from each variant's own content-level approval. `architecture/DATA_CONTRACTS.md` §6
   names `content` and `campaign` as the entities with this pattern, not `experiment` — so this
   field is my extrapolation, not a requirement. **The Phase Owner should confirm this is wanted**;
   if not, it is a one-field removal with no other consequence.
5. **`alert.status` enum** (`NEW`, `ACKNOWLEDGED`, `INVESTIGATING`, `RESOLVED`, `CLOSED`) and
   **`alert.severity` enum** (`LOW`, `MEDIUM`, `HIGH`, `CRITICAL`) — both my own choice, using the
   values suggested in the assignment prompt. Ordinary incident-triage vocabulary, not sourced
   from any governing document.
6. **`alert.category` reuses the nine-value FAILURE HANDLING / error-shape vocabulary verbatim**
   (`code`, `configuration`, `credentials`, `permissions`, `data`, `dependency`, `rate_limit`,
   `provider_outage`, `policy`, `unresolved_decision`) from `architecture/DATA_CONTRACTS.md` §5.
   **Flagging this explicitly as instructed**: this was a deliberate choice to share one
   vocabulary between alerts and the errors that may trigger them, rather than inventing a
   second, alert-specific category list. The Phase Owner / Workflow State Designer should
   confirm this reuse is desired — an alternative design could give alerts their own, coarser
   category set if the two purposes turn out to want different granularity.
7. **No `minItems`/`maxItems`/numeric constraint was added anywhere** (`experiment.variants`
   array size, alert time-to-resolve, consent-expiry window) — treated as within `D-047`'s scope
   even though the prompt names retry counts / TTLs / significance thresholds specifically. I
   read "any numeric threshold this schema might want" broadly to include a minimum variant
   count, since asserting "a valid experiment needs at least 2 variants" is itself an invented
   business rule this project has stated no basis for.
8. **`alert.schema.json` has no open-ended `details` object field**, unlike the error shape's own
   `details` (`architecture/DATA_CONTRACTS.md` §5, "object or null"). I deliberately did not
   carry that field onto this entity schema, because an unconstrained JSON object is structurally
   incompatible with `additionalProperties: false` "at every object level" (§2.2) — an object
   with no declared `properties` and `additionalProperties: false` would reject every real use.
   `resolution_notes` (free string) is offered as the place for free-text context instead. This
   is a real design tension between §2.2 and §5 worth flagging to the Phase Owner; I resolved it
   by narrowing rather than by weakening `additionalProperties: false`, consistent with the
   fail-closed house style, but a different resolution (e.g. an explicitly-typed `details`
   sub-object once real error shapes are known) is possible later.
9. **`lead.status` enum** (`NEW`, `CONTACTED`, `QUALIFIED`, `CONVERTED`, `LOST`, `ARCHIVED`) — my
   own choice, using the values suggested in the assignment prompt. Its top-level and per-value
   description explicitly states these are future-only states that Q-009 must unblock before use.
10. **`lead.consent_status` enum** (`UNKNOWN`, `GRANTED`, `DECLINED`, `WITHDRAWN`) — my own
    addition, not named in the assignment prompt's example field list but requested by name
    ("`consent_status`, etc."). I deliberately left out an `EXPIRED` value, because a consent
    expiry state implies a numeric expiry window this project has no basis to assert (`D-047`,
    and `DATA_RETENTION_POLICY.md` §6 confirms consent-record retention is itself `UNRESOLVED`).
11. **`lead.source` is a free string, not an enum.** No governing document names a closed list of
    intake channels this organic-only, no-connectors-authorized project actually has, so I did
    not invent one. Noted in the field's own description as a narrowing a future phase could do.
12. **`lead.phone` has no `format` keyword.** JSON Schema 2020-12 defines no standard `"phone"`
    format, and no locale-specific pattern is fixed anywhere in this project, so I left it a
    bare, nullable string rather than inventing a regex.
13. **No example, `default`, or `examples` value appears anywhere in any of the three schemas.**
    I used only type/format descriptions (e.g. "Contact email address as provided at intake"),
    never a realistic-looking placeholder, per the assignment's explicit instruction.

## Open questions

- **For the Phase Owner: does `experiment.schema.json` need `approval_id` at all?**
  `architecture/DATA_CONTRACTS.md` §6 names `content` and `campaign` as the entities composing
  with the approval workflow; `experiment` is my own extrapolation (Assumption 4). If the
  Workflow State Designer's `STATE_MACHINE.md` disagrees, this is a one-field removal.
- **For the Phase Owner: is reusing the nine-value error `category` vocabulary for
  `alert.category` the right call**, or should alerts have their own, possibly coarser,
  category set (Assumption 6)? I made the sharing choice deliberately but it is reversible.
- **For the Phase Owner / Independent Reviewer: the `additionalProperties: false`-vs-open-`details`
  tension (Assumption 8)** is not unique to this schema — any future entity wanting a
  free-form structured-context field will hit the same wall under the current house style. Worth
  a general ruling in `architecture/DATA_CONTRACTS.md` rather than each specialist inventing a
  workaround independently.
- **Not this agent's to resolve, restating for visibility: `Q-009` remains exactly as open after
  this handoff as before it.** `lead.schema.json`'s field shapes, enum values, and inline `DENY`
  notice do not answer `Q-009`; they only give Phase 17 a target once it is answered. See
  "Failures or risks" below for the explicit restatement requested by the assignment.

## Work completed

- Read, in full, in the required order: `architecture/DATA_CONTRACTS.md`,
  `policy/action_registry.json` (`roles` array and, for `alert.category`, the error-shape
  vocabulary at §5 of `DATA_CONTRACTS.md`), `DECISIONS.md` `D-047` (and its neighboring rows
  `D-041`–`D-051` for context), `DATA_RETENTION_POLICY.md` §2 (all subsections), §4, §6, §7, and
  `templates/AGENT_HANDOFF_TEMPLATE.md`.
- Read `schemas/content.schema.json` and `schemas/campaign.schema.json` as a style reference
  only (per the assignment's note that my work does not depend on their content).
- Read `task_plan.md` to confirm my exact file assignment (row 124) and run ID.
- Drafted `schemas/experiment.schema.json`: seven-field envelope, `status` enum (`DRAFT`,
  `RUNNING`, `CONCLUDED`, `ARCHIVED`), `name`, `hypothesis`, `variants` (array of
  `{variant_label, content_id}`), `outcome` enum (`NOT_YET_CONCLUDED`, `WINNER_DECLARED`,
  `INCONCLUSIVE`), `evaluation_method` (free-text, nullable, explicitly not a threshold),
  `winning_variant_label` (nullable), `started_at`/`concluded_at` (nullable date-times),
  `approval_id` (nullable uuid). `additionalProperties: false` at both the root object and the
  `variants` item object.
- Drafted `schemas/alert.schema.json`: seven-field envelope, `status` enum (`NEW`,
  `ACKNOWLEDGED`, `INVESTIGATING`, `RESOLVED`, `CLOSED`), `severity` enum (`LOW`, `MEDIUM`,
  `HIGH`, `CRITICAL`), `category` enum (the nine-value error-shape vocabulary, verbatim), `title`,
  `description`, `source`, `entity_type`/`entity_id` (nullable, mirroring the error shape's own
  fields), `acknowledged_by_role` (nullable, six-role enum), `acknowledged_at`/`resolved_at`
  (nullable date-times), `resolution_notes` (nullable). `additionalProperties: false` at the root.
- Drafted `schemas/lead.schema.json`: seven-field envelope, `status` enum (`NEW`, `CONTACTED`,
  `QUALIFIED`, `CONVERTED`, `LOST`, `ARCHIVED`), `contact_name`, `email` (`format: email`),
  `phone` (nullable), `source` (free string), `consent_status` enum (`UNKNOWN`, `GRANTED`,
  `DECLINED`, `WITHDRAWN`). Top-level `description` states the `ACT-W10`/`DENY`/`Q-009`/
  Git-substrate constraint inline, explicitly, as required. Per-field descriptions on
  `contact_name`, `email`, `phone` each restate the personal-data/`Q-009` constraint and the
  fixture-placeholder requirement individually, not only once at the top. No example, `default`,
  or `examples` value of any kind appears in this file. `additionalProperties: false` at the root.
- Did **not** write `architecture/STATE_MACHINE.md`, any other specialist's schema, any fixture
  file, or any register — confirmed against my file list before each write, per `CLAUDE.md` §7
  / `findings.md` F-00-09.

## Files changed

- `schemas/experiment.schema.json` (new)
- `schemas/alert.schema.json` (new)
- `schemas/lead.schema.json` (new)
- `agent_runs/phase-04/handoffs/HANDOFF_ANALYTICS_ENGINEER.md` (new, this file)

## Tests run

Confirmed each of my three files is valid JSON (structural check only — full JSON Schema
2020-12 conformance and fixture validation are later tasks, per the assignment's own scope note):

```
$ python -c "import json; json.load(open('schemas/experiment.schema.json'))" && echo "experiment.schema.json OK"
experiment.schema.json OK

$ python -c "import json; json.load(open('schemas/alert.schema.json'))" && echo "alert.schema.json OK"
alert.schema.json OK

$ python -c "import json; json.load(open('schemas/lead.schema.json'))" && echo "lead.schema.json OK"
lead.schema.json OK
```

I did not run a JSON Schema meta-schema validator (e.g. `jsonschema` against the 2020-12
meta-schema) or build/validate a fixture — neither was in scope for this handoff, per the
assignment's instruction that full schema validation is a later task.

## Failures or risks

- **No failures.** All three files parse as valid JSON; no tool or write was attempted outside
  my assigned file list.
- **Explicit restatement of the `Q-009` constraint on `lead.schema.json`, as requested:**
  `lead.schema.json` defines the *shape* of a future lead record only. Instantiating a real
  record against it — writing an actual person's name, email, or phone number into any instance
  of this schema, anywhere, including in a fixture — remains `DENY` under `ACT-W10` for every
  role, with no exception, until (a) `Q-009` is resolved by the Project Owner **and** (b) a
  storage substrate outside this repository's Git history is decided (`DATA_RETENTION_POLICY.md`
  §4) — resolving `Q-009` alone does not lift the DENY if no non-Git substrate has also been
  named. I stated this constraint inline in the schema's own top-level `description` and again on
  each of `contact_name`, `email`, and `phone`, not only once.
- **Confirmed: I did not create any real or fixture personal-data value anywhere**, in these
  schemas, in this handoff, or in any scratch file. No `"examples"`, `"default"`, or inline
  example value of any kind appears in any of the three schemas — every field description uses
  a structural/type description only (e.g. "Contact email address as provided at intake"). I did
  not write `schemas/fixtures/lead.fixture.json` (not my assignment) and did not need to
  construct even a placeholder value to complete my three files.
- **Risk to flag, not mine to fix:** the `additionalProperties: false`-vs-open-`details`-object
  tension (Assumption 8 / Open questions) could recur for any future schema (e.g. `alert`-adjacent
  work in Phase 21) unless `architecture/DATA_CONTRACTS.md` states a general rule for free-form
  structured-context fields.

## Recommended next action

1. Phase Owner / Workflow State Designer: when building `architecture/STATE_MACHINE.md`, the
   three `status` enums this handoff fixes are: `experiment.status` = `DRAFT | RUNNING |
   CONCLUDED | ARCHIVED`; `alert.status` = `NEW | ACKNOWLEDGED | INVESTIGATING | RESOLVED |
   CLOSED`; `lead.status` = `NEW | CONTACTED | QUALIFIED | CONVERTED | LOST | ARCHIVED`. Treat
   these as fixed inputs unless a defect is found — per `architecture/DATA_CONTRACTS.md`'s own
   convention, `STATE_MACHINE.md` should cite these enums, not redefine them.
2. Resolve the two open design questions above (`experiment.approval_id`'s necessity; whether
   `alert.category` should share the error-shape vocabulary) before or during transition design,
   since a removed/renamed field is cheaper to change now than after fixtures and a state machine
   reference it.
3. Whoever builds `schemas/fixtures/lead.fixture.json` (a different owner, later, per
   `architecture/DATA_CONTRACTS.md` §1): use only structurally-described placeholder values
   (e.g. `"contact_name": "fixture-contact-name"`, `"email": "fixture-email@example.invalid"`),
   never a realistic-looking name, email, or phone number, and note the fixture itself remains
   subject to the same `Q-009`/`ACT-W10` framing this schema states inline.
4. Independent Reviewer: please specifically check my Assumption 8 resolution
   (`additionalProperties: false` vs. no open `details` field on `alert.schema.json`) against
   `architecture/DATA_CONTRACTS.md` §2.2 and §5 — I believe I resolved a real tension correctly
   but did not originate either governing rule, so a second read is warranted.
