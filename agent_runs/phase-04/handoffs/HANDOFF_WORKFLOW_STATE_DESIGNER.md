# Agent Handoff

- Run ID: `phase-04-2026-07-31-a`
- Phase: 04 — Data Contracts and State Model
- Agent: Workflow State Designer (specialist)
- Assignment: Author `schemas/approval.schema.json`, `architecture/STATE_MACHINE.md`, and this
  handoff — no other file (`task_plan.md` "File ownership": these two files are listed as my sole
  ownership, alongside every specialist's one handoff file).
- Files owned: the two files above; this handoff.

## Facts and evidence

- `APPROVAL_POLICY.md` §2 defines the approval state machine exactly: 10 states (`DRAFT`,
  `PENDING_APPROVAL`, `APPROVED`, `CHANGES_REQUESTED`, `REJECTED`, `EXPIRED`, `WITHDRAWN`,
  `EXECUTED`, `SUPERSEDED`, `VOIDED`), initial state `DRAFT`, six terminal states (`REJECTED`,
  `EXPIRED`, `WITHDRAWN`, `EXECUTED`, `SUPERSEDED`, `VOIDED`), a 12-row transition table, and (per
  §3) five numbered invariants. I cross-checked the state list against
  `policy/action_registry.json → state_machines.approval.states` (line 100) and it matches exactly,
  same order. `schemas/approval.schema.json`'s `status` enum and `architecture/STATE_MACHINE.md` §1
  both transcribe this — neither invents a competing state or edge.
- `architecture/DATA_CONTRACTS.md` §2.1 fixes the seven-field shared envelope (`id`,
  `schema_version`, `idempotency_key`, `status`, `version`, `created_at`, `updated_at`,
  `created_by_role`); §6 states the composition rule between the approval machine and any entity
  carrying `approval_id`. My schema follows the envelope exactly (same seven names, same types,
  `status` overridden per-schema as the convention requires); `STATE_MACHINE.md` §3 restates §6's
  composition rule and extends it to `experiment.approval_id` and `product.pricing_approval_id`,
  both confirmed by direct read of those two schema files (not assumed from `DATA_CONTRACTS.md`
  alone, since §6 only names `content`/`campaign` explicitly).
- I read all seven entity schema files directly from disk (not from the assignment prompt's
  paraphrase, per my instructions) before writing anything: `schemas/product.schema.json`,
  `schemas/brand.schema.json`, `schemas/content.schema.json`, `schemas/campaign.schema.json`,
  `schemas/experiment.schema.json`, `schemas/alert.schema.json`, `schemas/lead.schema.json`. Every
  `status` enum quoted in `STATE_MACHINE.md` §2 is copy-pasted from the actual file, not
  paraphrased. I edited none of the seven.
- `policy/action_registry.json → roles` (lines 27–69) gives the closed six-value vocabulary
  (`PROJECT_OWNER`, `PHASE_OWNER`, `SPECIALIST`, `INDEPENDENT_REVIEWER`, `GOVERNANCE_AUDITOR`,
  `RUNTIME_AGENT`) used verbatim for `created_by_role`. It does **not** include `DETERMINISTIC_CODE`
  — that token only appears in the approval transition table's "Actor" column
  (`policy/action_registry.json → state_machines.approval`, and `APPROVAL_POLICY.md` §2's table). I
  treated this as a real, load-bearing distinction (see Assumptions, item 2) rather than folding
  `DETERMINISTIC_CODE` into the six-role enum or dropping it.
- `DECISIONS.md` `D-047` (full row read directly, lines 167): "Every numeric threshold Phase 03
  would otherwise need... is recorded as `UNRESOLVED` rather than assigned a default value." I
  added no numeric threshold anywhere in either file — every place a threshold might plausibly be
  expected (staleness windows, minimum campaign lead time, minimum experiment duration, alert
  time-to-resolve) is either left undescribed or explicitly noted as "no threshold defined."
- `templates/AGENT_HANDOFF_TEMPLATE.md` fixes this file's section structure; followed exactly, same
  section headers, same order.

## Assumptions

Per `findings.md` `F-00-05` ("a specialist's claim of 'no assumptions' carries no evidentiary
weight"), every assumption is named specifically below rather than glossed over.

1. **All per-entity transition tables in `STATE_MACHINE.md` §2 are my own construction.** No
   governing document specifies transitions for `product`, `brand`, `content`, `campaign`,
   `experiment`, `alert`, or `lead` beyond the `status` enum values and prose descriptions already
   present in each schema file. Every trigger name (`launch_offering`, `submit_for_review`,
   `pause`, `qualify`, etc.) is a structural label I invented for legibility — explicitly flagged as
   such in the document's own intro, not presented as sourced.
2. **`schemas/approval.schema.json`'s `decided_by_role` enum is `["PROJECT_OWNER", "PHASE_OWNER",
   "DETERMINISTIC_CODE", null]`, not the full six-role vocabulary.** This is a deliberate design
   choice, not dictated verbatim by any file: I derived it by reading every "Actor" cell in
   `APPROVAL_POLICY.md` §2's transition table for edges leaving `PENDING_APPROVAL`/`APPROVED` and
   found only those three values ever appear. I judged that letting the field's enum include
   `SPECIALIST`/`INDEPENDENT_REVIEWER`/`GOVERNANCE_AUDITOR`/`RUNTIME_AGENT` — even though the
   generic envelope's `created_by_role` allows all six — would be misleading, since no edge in the
   governing table ever assigns one of those four as an actor. This is the schema-shape response
   the assignment specifically asked for ("your field naming and description should not mislead a
   future implementer"). Similarly, `requested_by_role`'s enum is `["PHASE_OWNER", null]` only,
   since `submit` is the table's only edge into `PENDING_APPROVAL` and its only actor is
   `PHASE_OWNER`.
3. **I added seven `allOf`/`if`/`then` conditionals binding `status` to `decided_by_role` (and one
   binding non-`DRAFT`/non-`WITHDRAWN` statuses to `requested_by_role`).** This goes beyond what the
   assignment literally required (a non-misleading field description) into an actual structural
   guardrail checkable by a JSON Schema validator. I judged this defensible because every state in
   the transition table (except `PENDING_APPROVAL` and `DRAFT`, both reachable by only one path with
   one consistent actor once you exclude the ambiguous case below) has exactly one consistent actor
   across every edge that reaches it — I verified this by re-reading the full 12-row table
   state-by-state before writing the conditionals, not by assumption. **I found and fixed one real
   bug this way**: my first draft required `requested_by_role = PHASE_OWNER` for every non-`DRAFT`
   status, but `WITHDRAWN` is reachable directly from `DRAFT` (via `withdraw`) without a prior
   `submit`, so that blanket rule wrongly rejected a valid direct-withdrawal record. I caught this
   by testing a `WITHDRAWN`-from-`DRAFT` record against the schema (see Tests run) before writing
   this document, per `findings.md` `F-00-04` ("run mechanical verification before review, not
   after"), and narrowed the conditional to exclude `WITHDRAWN` from that requirement.
4. **`entity_type`'s enum includes all seven entity names (`product`, `brand`, `content`,
   `campaign`, `experiment`, `alert`, `lead`) plus `null`, even though only four
   (`content`/`campaign`/`experiment`/`product`) actually carry a live `approval_id`-style
   back-reference today.** I judged including all seven, with a description disclosing which four
   are live, more honest than a closed four-value enum that would need a schema-version bump the
   moment a fifth entity ever needed approval-linking. This is my own judgment call, not derived
   from any governing document — flagged again below as an open question about GC-08/GC-09.
5. **`gated_category`, `summary`, `effect_if_approved`, `reversal_cost`, and `artifact_digest`
   fields go beyond the assignment's literal minimum** (which asked for "a reference to what is
   being approved" and "an `artifact_digest` field or similar"). I added the remaining three because
   `APPROVAL_POLICY.md` §4 explicitly enumerates five elements "an approval request must contain at
   minimum," and I judged a schema that omitted three of the policy's own five named elements would
   under-build the contract relative to what the cited section actually specifies. This is a
   scope-widening judgment call, not a literal instruction — flagged in case the Phase Owner or
   Schema QA Reviewer judges it out of scope for a structural contract.
6. **No cross-schema referential constraint (e.g. `content.approval_id` must point at a real
   `approval.schema.json` record whose `entity_id` matches back) is encoded anywhere.**
   `architecture/DATA_CONTRACTS.md` §7 already states no runtime enforces `*_id` reference
   integrity this phase; I treated that as settling the question rather than attempting a
   `$ref`/cross-file JSON Schema construct, which 2020-12 supports but which none of the other six
   entity schemas attempted for their own `*_id` fields either (kept consistent with sibling
   schemas' own choices, per the Data Architect's and Analytics Engineer's handoffs, which I read
   before writing).
7. **`brand`'s lifecycle (§2.2) has no edge from `DRAFT` directly to a terminal state for an
   abandoned draft that never went `ACTIVE`.** I left this as a documented gap rather than inventing
   a `DRAFT → SUPERSEDED` edge, since "superseded" implies something to supersede. Flagged as an
   open question below.

## Open questions

- **`entity_type`/GC-08/GC-09 gap.** No entity among the seven this phase's schemas cover
  represents a standalone "spend request" or "paid-ad request" record. `gated_category` values
  `GC-08` (spending) and `GC-09` (paid advertising) therefore have no natural `entity_type`/`entity_id`
  target in `schemas/approval.schema.json` today — I left both nullable and documented the gap
  rather than inventing a placeholder entity. If a future phase needs to route a spend or
  paid-advertising approval through this schema, either a new entity schema is needed or
  `entity_type`/`entity_id` should be treated as legitimately null for those two categories
  permanently. Not resolved by this phase; flagged for the Phase Owner.
- **`brand.schema.json`'s `status` enum has no state for an abandoned `DRAFT` that never became
  `ACTIVE`.** Every other entity has an explicit path to a terminal/retired state from its initial
  state (`product.DRAFT → RETIRED`, `content` and `campaign`'s various `archive_*` edges from
  `DRAFT`, `experiment.DRAFT → ARCHIVED`). `brand` cannot reach `SUPERSEDED` except via `ACTIVE`,
  and has no `ARCHIVED`-equivalent state at all. This is not a defect I introduced — it is the Data
  Architect's own three-value enum, read directly from `brand.schema.json` — but it produced the
  one genuinely awkward transition table in §2 of `STATE_MACHINE.md`, and I flagged it there too. A
  fourth state (e.g. `ABANDONED`, or widening `SUPERSEDED`'s meaning) would be a MINOR,
  backward-compatible schema change per `architecture/DATA_CONTRACTS.md` §3 if the Phase Owner or a
  future reviewer agrees this is worth fixing.
- **`lead.status`'s `ARCHIVED` state may be redundant with `CONVERTED`/`LOST` already being
  terminal-shaped outcomes.** I modeled `CONVERTED`/`LOST` → `ARCHIVED` as an available edge for
  completeness (§2.7), but nothing confirms whether a converted or lost lead is ever actually
  archived as a distinct further step, versus `CONVERTED`/`LOST` themselves being treated as the
  real terminal states in practice with `ARCHIVED` reserved only for `NEW` leads that go stale. This
  is exactly the kind of enum-vs-transition-table friction `HANDOFF_DATA_ARCHITECT.md`'s own open
  questions predicted might surface once transitions were modeled (their note: "if the transition
  modeling surfaces a need to revise any of my enums... that should come back... not a silent edit")
  — I did not silently edit `lead.schema.json`; I'm flagging it here per that same discipline.
- **Should `schemas/approval.schema.json` carry a `batch_id` or similar grouping field**, given
  `APPROVAL_POLICY.md` §5's extensive batching rules ("Batching may... Group multiple similar
  requests into one review session")? I deliberately did not add one — batching is explicitly
  described as "a review-time convenience, not a new state-machine object" (§5), and no field on
  the individual approval record seemed necessary to represent a review-session grouping that could
  equally live in a future queue implementation (Phase 15) rather than this record's own shape. Flag
  for the Phase Owner in case the Schema QA Reviewer disagrees.

## Work completed

- Wrote `schemas/approval.schema.json`: seven-field envelope (unchanged names/types) +
  `gated_category` (enum `GC-01`..`GC-09`), `entity_type` (nullable enum of the seven entity names),
  `entity_id` (nullable uuid), `summary`, `effect_if_approved`, `reversal_cost`, `artifact_digest`
  (`APPROVAL_POLICY.md` §4's five packet elements), `requested_by_role`/`requested_at` (nullable,
  restricted to `PHASE_OWNER`/null), `decided_by_role`/`decided_at` (nullable, restricted to
  `PROJECT_OWNER`/`PHASE_OWNER`/`DETERMINISTIC_CODE`/null). `status` enum is exactly the 10
  `APPROVAL_POLICY.md` §2 states, same order. `additionalProperties: false` at the root (no nested
  objects exist in this schema). Seven `allOf`/`if`/`then` conditionals bind `status` to
  `decided_by_role`/`requested_by_role` per the transition table's actor column, structurally
  preventing any agent role from being a valid `decided_by_role` value when `status` is `APPROVED`
  (Invariant 1/5).
- Wrote `architecture/STATE_MACHINE.md`: intro distinguishing transcription (§1) from original
  structural work (§2); §1 the full approval state machine (states, transition table, five
  invariants, all quoted/cross-cited from `APPROVAL_POLICY.md` §2–§3) plus a subsection (§1.4)
  explaining how the schema's conditionals encode Invariant 1/5 structurally; §2 seven per-entity
  lifecycle subsections, each with the entity's `status` enum quoted verbatim, initial/terminal
  states, and an invented (labeled as such) transition table, with `lead` (§2.7) carrying an
  explicit `Q-009`/Git-history-substrate caveat in its prose per the assignment's specific
  instruction; §3 the approval/entity composition rules for `content`/`campaign`/`experiment`/`product`;
  a capability-classification table at the end, styled like `DATA_CONTRACTS.md` §8.
- Did not edit any of the seven entity schema files, any fixture, `DATA_CONTRACTS.md`,
  `APPROVAL_POLICY.md`, or any register (`DECISIONS.md`, `OPEN_QUESTIONS.md`, `findings.md`,
  `progress.md`, `CURRENT_PHASE.md`) — confirmed against `task_plan.md` "File ownership" and this
  assignment's explicit file list before and after writing.

## Files changed

- `schemas/approval.schema.json` (new)
- `architecture/STATE_MACHINE.md` (new)
- `agent_runs/phase-04/handoffs/HANDOFF_WORKFLOW_STATE_DESIGNER.md` (new, this file)

## Tests run

All commands run from the project root.

1. **JSON validity** (the check explicitly requested for this handoff):
   ```
   $ python -c "import json; json.load(open('schemas/approval.schema.json'))" && echo "approval OK"
   approval OK
   ```

2. **Beyond the requested minimum — JSON Schema 2020-12 structural validity**, using the
   `jsonschema` package already installed this run (`task_plan.md` "What this phase inherits" item
   6):
   ```
   $ python -c "
   import json, jsonschema
   schema = json.load(open('schemas/approval.schema.json'))
   jsonschema.Draft202012Validator.check_schema(schema)
   print('schema shape OK (Draft202012Validator.check_schema passed)')
   "
   schema shape OK (Draft202012Validator.check_schema passed)
   ```

3. **Beyond the requested minimum — targeted valid/invalid record checks**, written to verify my
   `allOf`/`if`/`then` conditionals actually enforce what I claim in the schema's own descriptions,
   rather than trusting my own reasoning (`findings.md` `F-00-04`). Full script and output:
   ```
   $ python -c "
   import json, jsonschema, uuid
   schema = json.load(open('schemas/approval.schema.json'))
   validator = jsonschema.Draft202012Validator(schema)
   # ... (base valid APPROVED record, then 10 targeted mutations)
   "
   check_schema OK
   APPROVED/PROJECT_OWNER (valid): PASS (errors=0, want_valid=True)
   APPROVED/RUNTIME_AGENT (invalid): PASS (errors=2, want_valid=False)
   APPROVED/PHASE_OWNER (invalid): PASS (errors=1, want_valid=False)
   DRAFT, all nulls (valid): PASS (errors=0, want_valid=True)
   WITHDRAWN direct-from-DRAFT (valid): PASS (errors=0, want_valid=True)
   WITHDRAWN after submit (valid): PASS (errors=0, want_valid=True)
   PENDING_APPROVAL, requested set (valid): PASS (errors=0, want_valid=True)
   PENDING_APPROVAL, requested null (invalid): PASS (errors=1, want_valid=False)
   EXPIRED/DETERMINISTIC_CODE (valid): PASS (errors=0, want_valid=True)
   VOIDED/PROJECT_OWNER (invalid): PASS (errors=1, want_valid=False)
   extra field (invalid, additionalProperties): PASS (errors=1, want_valid=False)
   ```
   All 11 assertions passed on the second run. The first run of this exact script (before I added
   the `WITHDRAWN`-exclusion fix described in Assumptions item 3) surfaced a real failure — a
   `WITHDRAWN`-direct-from-`DRAFT` record I expected to be valid came back with 1 error — which I
   traced to an over-broad conditional and fixed before treating either file as complete. I am not
   claiming this test suite is exhaustive (it does not, for example, test every one of the seven
   conditionals' `then` branches independently, only a representative sample covering `APPROVED`,
   `WITHDRAWN`, `PENDING_APPROVAL`, `EXPIRED`, and `VOIDED`), and I did not test `REJECTED`,
   `CHANGES_REQUESTED`, `SUPERSEDED`, or `EXECUTED` individually — those three conditionals are
   structurally identical in form to the ones I did test (same `const`/`enum` pattern), but I did
   not independently exercise each one.
   I did **not** write or run any fixture file (`schemas/fixtures/approval.fixture.json`) — that
   file is explicitly the Schema QA Reviewer's task (`task_plan.md` T3), not mine, and I was told
   not to write it.

## Failures or risks

- No unresolved test failures — the one failure I found (Assumption 3 / Tests run item 3) was
  caught and fixed before this handoff was written, and the fix was re-verified.
- **Risk:** my `allOf` conditionals are a genuine addition to what the Data Architect/Analytics
  Engineer's four sibling schemas do (none of them use `if`/`then`). If the Schema QA Reviewer's
  fixture-writing (T3) needs an `approval` fixture record in a state my conditionals don't expect
  (e.g. a state I reasoned has one consistent actor but actually doesn't), fixture validation would
  correctly fail and should be treated as evidence to revisit the conditional, not a fixture bug to
  work around.
- **Risk:** the per-entity transition tables in `STATE_MACHINE.md` §2 are entirely my own
  construction (Assumption 1). If a later phase (e.g. Phase 13 Content Production, Phase 14
  Experimentation) finds these transitions don't match how it actually needs to operate, they should
  be revised openly as a documented change, not silently diverged from in code that never updates
  this file.
- **Risk (disclosed, not a defect):** three open questions above (GC-08/GC-09 entity gap, `brand`'s
  missing abandoned-draft edge, `lead.ARCHIVED` ambiguity) are real gaps in the seven schemas or in
  my own modeling, not resolved by this handoff. None blocks Phase 04's stated pass conditions
  (`task_plan.md` V-1 through V-8 do not require resolving them), but a future phase reader should
  not assume they were considered and dismissed — they were considered and left open.

## Recommended next action

Schema QA Reviewer (Phase Owner, T3) writes `schemas/fixtures/approval.fixture.json` (2–4 records
per `architecture/DATA_CONTRACTS.md` §1, covering at minimum `DRAFT` and one non-initial state) and
validates it against `schemas/approval.schema.json`, along with the other seven fixtures, per
`task_plan.md`'s validation plan V-1 through V-6. Given this schema's `allOf` conditionals are new
relative to its five siblings, I recommend the Schema QA Reviewer's fixture set for `approval`
specifically include at least one record in `PENDING_APPROVAL`, `APPROVED`, and one terminal state
reached via `DETERMINISTIC_CODE` (e.g. `EXPIRED` or `VOIDED`), to exercise all three branches of the
`decided_by_role` actor split (§1.4 of `STATE_MACHINE.md`) rather than only the two states
(`DRAFT`/one non-initial) the fixture-format minimum technically requires. If V-2 fails against my
schema specifically, the conditionals are the first place to look, not the fixture.
