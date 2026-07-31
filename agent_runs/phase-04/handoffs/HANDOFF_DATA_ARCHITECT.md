# Agent Handoff

- Run ID: `phase-04-2026-07-31-a`
- Phase: 04 — Data Contracts and State Model
- Agent: Data Architect (specialist)
- Assignment: Author `schemas/product.schema.json`, `schemas/brand.schema.json`,
  `schemas/content.schema.json`, `schemas/campaign.schema.json`, and this handoff — no other file
  (`task_plan.md` "File ownership").
- Files owned: the four schema files above; this handoff.

## Facts and evidence

- `architecture/DATA_CONTRACTS.md` (Phase 04 Owner, T0) fixes JSON Schema draft 2020-12, the
  seven-field shared envelope (`id`, `schema_version`, `idempotency_key`, `status`, `version`,
  `created_at`, `updated_at`, `created_by_role`), `additionalProperties: false` at every object
  level, semver `schema_version` versioning, the `idempotency_key` dedup rule, the standard error
  shape, and §6's rule that `content`/`campaign` link to an approval record by `approval_id`
  rather than embedding approval states in their own `status` enum. All four schemas below follow
  this exactly — no envelope field renamed, omitted, or redefined.
- `policy/action_registry.json → roles` gives the closed six-value vocabulary used verbatim for
  every `created_by_role` enum: `PROJECT_OWNER`, `PHASE_OWNER`, `SPECIALIST`,
  `INDEPENDENT_REVIEWER`, `GOVERNANCE_AUDITOR`, `RUNTIME_AGENT`.
- `APPROVAL_POLICY.md` §2 defines the 10-state approval machine. Per `DATA_CONTRACTS.md` §6, I did
  **not** copy any of those 10 states into `content.status` or `campaign.status` — each entity's
  `status` enum is its own production/publishing lifecycle, linked to (not merged with) an
  approval record via `approval_id` (nullable `uuid`).
- `CLAUDE.md` §4 / `README.md` "Primary success criteria" / `policy/action_registry.json →
  gated_categories` name the nine approval-gated categories (`GC-01`…`GC-09`). `product.schema.json`
  and `campaign.schema.json` reference this directly in reasoning about `pricing_approval_id` and
  `approval_id` respectively.
- `DECISIONS.md` `D-047`: no numeric threshold may be invented. I added no retry count, TTL,
  staleness window, minimum/maximum duration, or `minItems`/`maxItems` constraint anywhere. The
  only numeric-shaped constraints present (`minLength: 1`, `minimum: 1` on the envelope's `version`
  counter) are structural non-business-rule constants already fixed by `DATA_CONTRACTS.md` §2.1,
  not something I invented.
- `DATA_RETENTION_POLICY.md` §7 (data minimisation): no example, default, or description in any of
  the four schemas contains a real or realistic-looking product name, brand name, price, or
  personal-data value. I used only structural language (e.g. "no example value here resembles a
  real RDBC product name").
- `task_plan.md` "File ownership" confirms my assignment is exactly these four files plus this
  handoff, and confirms I do not write `architecture/STATE_MACHINE.md`,
  `schemas/approval.schema.json`, `schemas/experiment.schema.json`, `schemas/alert.schema.json`,
  `schemas/lead.schema.json`, any fixture, or any register — consistent with the task instructions
  I was given.

## Assumptions

Everything below is an assumption I made because it wasn't dictated by a governing file. Per
`findings.md` `F-00-05`, a "no assumptions" handoff is itself a red flag in this project, so these
are named specifically rather than glossed over:

1. **`product.status` enum = `DRAFT`, `ACTIVE`, `DEPRECATED`, `RETIRED`.** Chosen to distinguish
   "not yet offered" (DRAFT) from "offered" (ACTIVE) from "being phased out but still referenced"
   (DEPRECATED) from "fully retired" (RETIRED). No governing document specifies product lifecycle
   states; this is my own product-management judgment. `DEPRECATED` vs `RETIRED` is the most
   debatable split — I read "deprecated" as "still may be referenced by existing
   commitments/content" and "retired" as "no longer supported in any capacity," but a different
   split (e.g. collapsing them to one state) would also be defensible.
2. **`product.pricing_approval_id` instead of a raw price/amount/currency field.** I deliberately
   did **not** add a numeric price field to `product.schema.json`, even though the prompt invited
   me to "consider fields for pricing/offer details." My reasoning: (a) any price value is GC-02
   gated and I judged that a bare price field with no enforced link to an approval record would
   read as implying a price could be set unilaterally; (b) deciding a currency/amount type
   (integer cents? decimal string? which currency field?) is itself a design decision with no
   governing input, and `D-047` counsels against inventing shape decisions that carry implicit
   business-rule weight. I resolved this by adding only `pricing_approval_id` (nullable `uuid`)
   and leaving the actual price representation to whichever future phase actually implements a
   priced offer against a real approval queue. This is a narrower interpretation of "consider
   pricing fields" than a reviewer might expect — flagged as an open question below.
3. **`brand.status` enum = `DRAFT`, `ACTIVE`, `SUPERSEDED`.** Modeled on a simple versioned-document
   lifecycle: being authored (DRAFT), currently in use (ACTIVE), replaced (SUPERSEDED). I assumed
   at most one brand record is "meant" to be ACTIVE at a time but did **not** encode that as a
   schema constraint (JSON Schema has no native cross-record uniqueness constraint, and enforcing
   it is deterministic-code's job per Architecture Rule 3 once a runtime exists — noted in the
   schema's own `status` description).
4. **`brand.title` / `brand.summary` as the only entity-specific fields.** I kept this schema
   deliberately thin because Phase 07 owns actual brand content and nothing today specifies what a
   brand-identity record's real shape needs (voice attributes? a visual-token list? a version
   label?). I judged two free-text structural fields sufficient for a Phase 04 contract and did not
   invent a richer structure (e.g. nested `voice` / `visual` objects) that Phase 07 would likely
   just replace.
5. **`content.status` enum = `DRAFT`, `READY_FOR_REVIEW`, `SCHEDULED`, `PUBLISHED`, `ARCHIVED`.**
   `READY_FOR_REVIEW` maps to the moment an approval request would be submitted
   (`APPROVAL_POLICY.md` §4); `SCHEDULED` maps to an approved-but-not-yet-published state, included
   for shape completeness even though scheduling is `DENY` today (`ACT-P04`). I explicitly stated
   in the schema's top-level `description` that `PUBLISHED` cannot currently be reached, per the
   task instructions.
6. **`content` does not carry a `campaign_id` back-reference.** The task instructions asked
   `campaign` to reference `content`/`product` by id, not the reverse. I chose not to add a
   symmetric back-reference on `content` to avoid inventing a relationship not requested and to
   keep `campaign` as the single place campaign membership is recorded. A future phase could add
   one as a backward-compatible optional field (`DATA_CONTRACTS.md` §3, MINOR change) if bidirectional
   lookup turns out to matter.
7. **`campaign.status` enum = `DRAFT`, `PLANNED`, `ACTIVE`, `PAUSED`, `COMPLETED`, `ARCHIVED`.** I
   added `PAUSED` (temporarily halted, resumable) as distinct from `ARCHIVED` (terminal retirement)
   and `PLANNED` (scoped and possibly approved, but not yet started) as distinct from `DRAFT` (still
   being assembled). This is the richest enum of the four and the one I am least confident matches
   what `STATE_MACHINE.md` will end up needing — flagged as an open question below.
8. **`campaign.approval_id` exists, separate from each linked content item's own `approval_id`.**
   The task instructions left this as "your call — state your reasoning." I decided campaigns
   warrant their own approval reference because a campaign can constitute a coordinated decision
   (e.g., bundling a discount, or a timed push into a controversial topic) that is not fully
   captured by approving its individual content pieces one at a time. This is a design opinion, not
   a governing-document requirement — `APPROVAL_POLICY.md` does not say campaigns need their own
   approval record distinct from content approval.
9. **`campaign.product_ids` / `campaign.content_ids` have no `minItems`.** I left these arrays
   unconstrained (can be empty) rather than requiring at least one entry, reasoning that a `DRAFT`
   campaign may exist before its scope is decided. I considered `minItems: 1` for non-DRAFT states
   but that would be a cross-field conditional constraint tied to `status`, which JSON Schema can
   express (`if`/`then`) but which I judged out of scope for a Phase 04 structural contract and
   closer to a business rule than this phase's mandate covers.
10. **`campaign.planned_start_at` / `planned_end_at` are independently nullable, with no ordering
    constraint between them.** I did not add a `start <= end` cross-field check. JSON Schema 2020-12
    can express this, but I judged adding it would be validation logic beyond a structural contract
    and risks looking like an invented business rule under `D-047`'s spirit even though it isn't
    numeric. Flagged as an open question below in case the Schema QA Reviewer or Workflow State
    Designer disagrees.

## Open questions

- Should `product.schema.json` eventually carry a real price/amount field once a phase actually
  implements a priced-offer approval flow? I deliberately left this out (Assumption 2) — the Phase
  Owner or a later phase (Phase 06/15 area) should confirm this reading is correct rather than
  something this schema should have attempted.
- Does `campaign.status` need all six values I chose, or would `STATE_MACHINE.md` be simpler with
  fewer (e.g. collapsing `PLANNED` into `DRAFT`, or `PAUSED` into `ARCHIVED`)? I designed this enum
  before seeing how the Workflow State Designer wants to model transitions (`task_plan.md` T2 runs
  after T1, per `F-00-07`) — if the transition table gets awkward with six states, that is better
  evidence than my own reasoning and the enum should be revisited, not silently forced to fit.
- Is a campaign-level `approval_id`, separate from per-content `approval_id`, the right design
  (Assumption 8)? I could not find a governing document that settles this either way. If the Phase
  Owner or a later phase decides campaigns should only ever be approved through their constituent
  content items, `campaign.approval_id` should be removed as a MINOR/backward-incompatible change
  depending on whether it's currently `null` everywhere (it would be, since nothing writes real
  records yet) — likely cheap to reverse.
- Should `content.schema.json` carry an explicit `content_type` or `platform` field (post, caption,
  article, email draft; which platform)? I did not add one because no governing document fixes a
  vocabulary for it and `D-018` explicitly defers platform selection to Phase 10. Flagging in case
  the Schema QA Reviewer or a later phase wants it added as a MINOR, backward-compatible optional
  field.
- I did not read `schemas/approval.schema.json`, `schemas/experiment.schema.json`,
  `schemas/alert.schema.json`, or `schemas/lead.schema.json` (out of scope per my assignment), so I
  cannot confirm my `approval_id` fields' shape matches whatever `approval.schema.json`'s own `id`
  field turns out to be — I assumed a plain `format: uuid` string is sufficient, consistent with
  `DATA_CONTRACTS.md` §2.1's own `id` field definition, which should hold since every entity's `id`
  follows the same envelope rule.

## Work completed

- Wrote `schemas/product.schema.json` — envelope + `name`, `description`, `pricing_approval_id`
  (nullable uuid); `status` enum `DRAFT`/`ACTIVE`/`DEPRECATED`/`RETIRED`.
- Wrote `schemas/brand.schema.json` — envelope + `title`, `summary`; `status` enum
  `DRAFT`/`ACTIVE`/`SUPERSEDED`.
- Wrote `schemas/content.schema.json` — envelope + `title`, `body`, `approval_id` (nullable uuid);
  `status` enum `DRAFT`/`READY_FOR_REVIEW`/`SCHEDULED`/`PUBLISHED`/`ARCHIVED`, with an explicit
  top-level `description` note that `PUBLISHED` is structurally defined but not currently reachable
  (`PUBLISHING_POLICY.md`, `D-010`).
- Wrote `schemas/campaign.schema.json` — envelope + `name`, `description`, `approval_id` (nullable
  uuid), `product_ids` (array of uuid, no referential-integrity enforcement), `content_ids` (same),
  `planned_start_at`/`planned_end_at` (nullable date-time); `status` enum
  `DRAFT`/`PLANNED`/`ACTIVE`/`PAUSED`/`COMPLETED`/`ARCHIVED`.
- Every schema: `"$schema": "https://json-schema.org/draft/2020-12/schema"`, `"$id":
  "https://rdbc.internal/schemas/<entity>.schema.json"` (stable literal identifier, not a live
  URL, per `DATA_CONTRACTS.md` §2), `"additionalProperties": false` at every object level (no
  nested objects exist in any of the four, only nested arrays of primitive `uuid` strings, so there
  was no second object level to close), a top-level `"description"`, and every non-optional field
  listed in `"required"`.
- Did not write `architecture/STATE_MACHINE.md`, `schemas/approval.schema.json`,
  `schemas/experiment.schema.json`, `schemas/alert.schema.json`, `schemas/lead.schema.json`, any
  fixture file, or any register — confirmed against `task_plan.md` "File ownership" before and
  after writing.

## Files changed

- `schemas/product.schema.json` (new)
- `schemas/brand.schema.json` (new)
- `schemas/content.schema.json` (new)
- `schemas/campaign.schema.json` (new)
- `agent_runs/phase-04/handoffs/HANDOFF_DATA_ARCHITECT.md` (new, this file)

## Tests run

I did **not** run schema validation (`jsonschema.Draft202012Validator.check_schema` or fixture
validation) myself — that is the Schema QA Reviewer's task at `task_plan.md` T3, using real
fixture files I was explicitly told not to write. I only confirmed each of my four files is valid
JSON, using the exact commands and output below (run from the project root):

```
$ python -c "import json; json.load(open('schemas/product.schema.json'))" && echo "product OK"
product OK
$ python -c "import json; json.load(open('schemas/brand.schema.json'))" && echo "brand OK"
brand OK
$ python -c "import json; json.load(open('schemas/content.schema.json'))" && echo "content OK"
content OK
$ python -c "import json; json.load(open('schemas/campaign.schema.json'))" && echo "campaign OK"
campaign OK
```

All four commands exited successfully with no exception and printed their respective "OK" line.
This confirms syntactic JSON validity only — it does **not** confirm these are structurally valid
JSON Schema documents (e.g. that `Draft202012Validator.check_schema` would accept them), and it
does **not** confirm any fixture validates against them, since no fixture exists yet. Both of those
checks are explicitly the Schema QA Reviewer's V-1/V-2/V-3 (`task_plan.md` "Validation plan").

## Failures or risks

- No test failures — the JSON-validity check above is the only check I ran, and all four files
  passed it.
- **Risk:** I have not seen `architecture/STATE_MACHINE.md` (it does not exist yet — the Workflow
  State Designer writes it after this handoff, per `task_plan.md` T2, citing my actual field
  names). If the Workflow State Designer needs a `status` value I didn't include, or finds one of
  mine doesn't fit a needed transition, my enums may need a MINOR (additive) revision — see Open
  questions above for the two enums (`product`, `campaign`) I'm least confident about.
  `DATA_CONTRACTS.md` §3 already defines how such a revision should be versioned (widening an enum
  is MINOR, not MAJOR), so this is a low-cost, anticipated risk, not a defect.
- **Risk:** `campaign.approval_id` is a design choice not dictated by any governing document
  (Assumption 8). If the Phase Owner or a later reviewer determines campaigns should not carry
  their own approval record, this field should be removed — cheap today since nothing writes real
  records yet, but worth flagging explicitly rather than silently asserting it's correct.

## Recommended next action

Workflow State Designer (T2) proceeds to author `architecture/STATE_MACHINE.md` and
`schemas/approval.schema.json`, citing the four `status` enums and the `approval_id`/reference
fields defined above by their actual names. If the transition modeling surfaces a need to revise
any of my four enums (especially `campaign.status`, the richest one, or the `pricing_approval_id`
design choice on `product`), that should come back to me or be handled by the Phase Owner as a
documented, versioned (MINOR) revision per `architecture/DATA_CONTRACTS.md` §3 — not a silent edit.
