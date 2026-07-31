# Phase 04 Independent Review Report

- **Phase:** 04 — Data Contracts and State Model
- **Run under review:** `phase-04-2026-07-31-a`
- **Reviewer:** Independent Reviewer (this run), authored none of the work under review
- **Date:** 2026-07-31

---

## 1. Scope of review

**Read in full:** `CLAUDE.md` (all 13 sections), `task_plan.md` (this phase's full task graph and
validation plan V-1–V-8), `architecture/DATA_CONTRACTS.md`, `architecture/STATE_MACHINE.md`,
`APPROVAL_POLICY.md` §1–§11 (with emphasis on §2–§3), `DATA_RETENTION_POLICY.md` §1–§11 (with
emphasis on §2.4, §4, §7), the `DECISIONS.md` Phase 03/04 sections (`D-047`, `D-050`, `D-052`,
`D-053`), `policy/action_registry.json` (`roles`, `state_machines.approval` in full), all eight
`schemas/*.schema.json` files, all eight `schemas/fixtures/*.fixture.json` files, `tools/schema_validate.py`
in full, all three handoffs in `agent_runs/phase-04/handoffs/`, the Phase 04 sections of `findings.md`
and `progress.md`, `OPEN_QUESTIONS.md` `Q-016` and its summary-table row, and the `MASTER_PLAN.md`
Phase 04 row plus a full pass over the 25-row deliverables table for cross-phase consistency.
`PROMPT_AND_BUILD_QUALITY_RUBRIC.md` in full for scoring.

**Also read, not on the assigned list, because verifying claims required it:** `git status` and
`git diff` for every file this phase modified (`CLAUDE.md`, `CURRENT_PHASE.md`, `DECISIONS.md`,
`MASTER_PLAN.md`, `OPEN_QUESTIONS.md`, `findings.md`, `progress.md`, `task_plan.md`), to confirm what
actually changed rather than trusting the progress log's description of what changed.

**Not reviewed, and why:** `RISK_REGISTER.md`, `NON_GOALS.md`, `SCOPE.md`, `ACCEPTANCE_CRITERIA.md`,
and every Phase 00–03 policy document other than `APPROVAL_POLICY.md`/`DATA_RETENTION_POLICY.md`
(`SECURITY_POLICY.md`, `AUTONOMY_POLICY.md`, `BUDGET_POLICY.md`, `PUBLISHING_POLICY.md`,
`MESSAGING_POLICY.md`) were not read in full — Phase 04's deliverables do not depend on them and the
assignment did not name them. `CAPABILITY_REGISTRY.md` and `SKILL_*` files were not re-read; nothing
in Phase 04 touches the capability surface. The `.agent/skills/` directory (a large untracked tree of
generic skill definitions) was noted in `git status` but not reviewed — it is a harness-local artifact
unrelated to any file this phase's task_plan.md assigns, and no evidence found ties it to this phase's
work.

---

## 2. Verification commands actually run, with real output

### 2.1 `jsonschema` package presence

```
$ python -c "import jsonschema; print(jsonschema.__version__)"
4.26.0
```
Matches the version claimed in `findings.md` F-04-01.

### 2.2 `python tools/schema_validate.py`

```
PASS  product: schema valid, 2 fixture record(s) all validate
PASS  brand: schema valid, 2 fixture record(s) all validate
PASS  content: schema valid, 3 fixture record(s) all validate
PASS  campaign: schema valid, 2 fixture record(s) all validate
PASS  experiment: schema valid, 2 fixture record(s) all validate
PASS  alert: schema valid, 2 fixture record(s) all validate
PASS  lead: schema valid, 2 fixture record(s) all validate
PASS  approval: schema valid, 4 fixture record(s) all validate

8 schemas checked, 19 fixture records checked, 0 failure(s).
```
Reproduces the claimed 8/8 schemas × 19/19 fixture records exactly.

### 2.3 `python tools/schema_validate.py --selftest`

```
CAUGHT  product: required field 'created_by_role' removed
CAUGHT  content: status set to a value outside its enum
CAUGHT  lead: unrecognized additional property injected
CAUGHT  approval: APPROVED record with decided_by_role=PHASE_OWNER (Invariant 5 violation)

4 red mutations attempted, 0 missed.
```
Reproduces the claimed 4/4 red mutations caught exactly.

### 2.4 `tools/idcheck.py` — **this is where a real discrepancy was found**

Run against every file this phase actually modified or created (per `git status`), first including
`CLAUDE.md` (which `git status` shows as modified this run):

```
$ python tools/idcheck.py . CLAUDE.md CURRENT_PHASE.md DECISIONS.md MASTER_PLAN.md OPEN_QUESTIONS.md \
    findings.md progress.md task_plan.md architecture/DATA_CONTRACTS.md architecture/STATE_MACHINE.md \
    agent_runs/phase-04/handoffs/HANDOFF_DATA_ARCHITECT.md \
    agent_runs/phase-04/handoffs/HANDOFF_ANALYTICS_ENGINEER.md \
    agent_runs/phase-04/handoffs/HANDOFF_WORKFLOW_STATE_DESIGNER.md

  planned future artefacts allowlisted from MASTER_PLAN.md: 119
  definitions found  D: 55  (from DECISIONS.md)
  definitions found  Q: 17  (from OPEN_QUESTIONS.md)
  definitions found  R: 24  (from RISK_REGISTER.md)
  definitions found  NG: 5  (from NON_GOALS.md)
  definitions found  F: 38  (from findings.md)

MISSING PATHS (13):
  CLAUDE.md: .claude/settings.local.json
  DECISIONS.md: .claude/settings.local.json
  DECISIONS.md: ACTION_LEDGER.md
  DECISIONS.md: agent-atlas-growth-department_build-package_draft.zip
  findings.md: .claude/settings.local.json
  findings.md: .vscode/extensions.json
  findings.md: ACTION_LEDGER.md
  findings.md: agent-atlas-growth-department_build-package_draft.zip
  findings.md: redtest_tmp.md
  progress.md: agent_runs/phase-04/PHASE_GATE_REPORT.md
  progress.md: redtest_tmp.md
  task_plan.md: agent_runs/phase-04/PHASE_GATE_REPORT.md
  task_plan.md: agent_runs/phase-04/REVIEW_REPORT.md
```
Exit code 1 (13 missing paths, 0 unresolved D-/Q-/R-/NG-/F- IDs).

Re-run excluding `CLAUDE.md` in case the phase owner's own run targeted a narrower set:

```
MISSING PATHS (12):  [same list minus the CLAUDE.md line]
```

Both runs report **0 unresolved ID citations** (confirming that half of `progress.md`'s claim is
correct), but **12–13 raw missing-path lines / 7 distinct unique missing paths**
(`.claude/settings.local.json`, `ACTION_LEDGER.md`,
`agent-atlas-growth-department_build-package_draft.zip`, `.vscode/extensions.json`, `redtest_tmp.md`,
`agent_runs/phase-04/PHASE_GATE_REPORT.md`, `agent_runs/phase-04/REVIEW_REPORT.md`) — not the **"5
reported missing paths"** `progress.md`'s Phase 04 section claims, and not fully explained by
`findings.md` F-04-04, which names only two of the seven (`ACTION_LEDGER.md` and the `.zip` file). See
**Finding H-2** below.

---

## 3. Findings

### CRITICAL — none found.

Nothing in this phase publishes, sends, spends, invents a numeric threshold, collects personal data,
or falsifies a gate decision. No finding below rises to that level.

---

### HIGH

**H-1 — `CLAUDE.md` was modified this phase with no file-ownership assignment and no disclosure anywhere in the audit trail.**

- **Where:** `CLAUDE.md`, new §14 "Verification commands (`tools/`)" (lines 375–401, per `git diff
  CLAUDE.md`). `task_plan.md`'s "File ownership" table (the authoritative list for this run) does
  **not** list `CLAUDE.md` anywhere — not for the Phase 04 Owner, not for any specialist.
- **What's wrong:** `git diff CLAUDE.md` shows a new section added this run. No handoff, no
  `findings.md` entry, and no `progress.md` entry for Phase 04 mentions this edit. `CLAUDE.md` itself
  states, in the section that would govern this exact situation: *"One owner per file. Do not write a
  file you do not own — including harness config"* (§7), citing `F-00-09` — the Phase 00 precedent
  where a subagent wrote `.claude/settings.local.json` outside its scope and *"it had to be disclosed
  in the gate report."* This phase repeats the same shape of defect against `CLAUDE.md` itself, the
  file this project's own contract calls *"binding on every agent, every session, every phase"* — and
  discloses it nowhere.
- **Why it matters:** This is not a content defect — the added section (a list of verification
  commands with a pointer to `tools/README.md`) is accurate and arguably useful. The defect is
  procedural and precedent-violating: an undisclosed write to the one file every future session reads
  first, by whichever agent integrated this phase, outside any assigned ownership, is exactly the
  failure mode `CLAUDE.md` §7 and `findings.md` F-00-09 exist to prevent, and this project's own
  history (`findings.md` F-00-09, referenced again in `RISK_REGISTER.md`/gate reports) treats this
  class of defect as something that "had to be disclosed," not something that gets to pass silently.
  §8's canonical-files table further states `CLAUDE.md` is updated "only when architecture,
  boundaries, or vocabularies actually change" — adding a tooling-reference section is a defensible
  candidate for that bar, but that judgment call was never surfaced for review, which is the point.
- **Evidence:** `git diff CLAUDE.md` (reproduced above); absence of any "CLAUDE.md" mention in the
  Phase 04 sections of `findings.md` or `progress.md` (checked via targeted grep across both
  sections); absence of `CLAUDE.md` from `task_plan.md`'s file-ownership table (read in full, §"File
  ownership — one owner per file").

**H-2 — `progress.md`'s claimed `idcheck.py` result ("the 5 reported missing paths") does not match the actual, reproducible output.**

- **Where:** `progress.md`, Phase 04 section: *"tools/idcheck.py run against every changed file: 0
  dangling D-/Q-/R-/NG-/F- citations; the 5 reported missing paths were either pre-existing gaps
  predating this phase (findings.md F-04-04) or expected forward references..."*; `findings.md`
  F-04-04, which names only `.claude/settings.local.json`(not named there at all)... actually names
  only `ACTION_LEDGER.md` and `agent-atlas-growth-department_build-package_draft.zip` as the "two
  pre-existing gaps."
- **What's wrong:** Re-running `tools/idcheck.py` myself (§2.4 above) against the same changed-file set
  produces **12–13 raw missing-path lines, 7 distinct unique paths** — not 5, and not the two `F-04-04`
  names. Three of the seven distinct paths (`.claude/settings.local.json`, `.vscode/extensions.json`,
  `redtest_tmp.md`) appear in the real output and are named nowhere in `findings.md` F-04-04 or
  `progress.md`'s Phase 04 section at all.
- **Why it matters:** `CLAUDE.md` §6 states *"Never claim a test ran that did not run. Record the
  command and the actual output, or say you did not test it."* This is not a case of a test not
  running — the test ran — but its **output was under-reported**, and the explanation offered
  (`F-04-04`) accounts for less than a third of what the tool actually flags. This is the exact class
  of defect `findings.md` F-02-14 already named for this project ("a check is only verification if...
  it has been shown to go red, and is scoped honestly to what it actually proves") and F-01-04
  ("a green result is not evidence by itself") — here the result was not fully green, and the
  incompleteness of the report is itself the defect, independent of whether the underlying missing
  paths are all pre-existing and harmless (they appear to be).
- **Evidence:** command and full output in §2.4 above, run twice (with and without `CLAUDE.md` in the
  target list) to rule out a simple explanation; neither run reproduces "5."

---

### MEDIUM

**M-1 — `MASTER_PLAN.md` still lists `schemas/approval.schema.json` and `schemas/lead.schema.json` as Phase 15 and Phase 17 deliverables respectively, after Phase 04 has already delivered both.**

- **Where:** `MASTER_PLAN.md` row 80 (Phase 15: *"`schemas/approval.schema.json`"* among its key
  deliverables) and row 82 (Phase 17: *"`schemas/lead.schema.json`"*), versus row 69 (Phase 04's own
  row), which explicitly lists both `approval` and `lead` among the eight schemas Phase 04 just
  delivered.
- **What's wrong:** The same two files are now named as deliverables of two different phases in the
  same table, with no note reconciling this. `task_plan.md`'s file-ownership table assigns
  `MASTER_PLAN.md` updates to the Phase 04 Owner "at every phase gate," and the Phase 04 Owner did
  update row 69 for this phase — but did not touch rows 15 or 17, which now read as though those
  phases will build these schemas from scratch.
- **Why it matters:** A future Phase 15 or Phase 17 owner reading `MASTER_PLAN.md` alone (rather than
  `DECISIONS.md`/`CLAUDE.md` §8's "Phase 04 deliverables" note) could reasonably conclude they need to
  (re-)author `approval.schema.json` or `lead.schema.json`, duplicating or silently diverging from
  Phase 04's real, already-reviewed contract — precisely the kind of staleness `tools/blast_radius_check.py`
  (`CSK-01`) exists to catch, but `CSK-01`'s fixed scope (per `findings.md` F-03-02) is eight named
  root-level governance files and does not include `MASTER_PLAN.md`'s per-phase deliverable cells, so
  this gap was never mechanically checked.
- **Evidence:** direct read of `MASTER_PLAN.md` rows 69, 80, 82 (quoted above).

**M-2 — `architecture/DATA_CONTRACTS.md` §5 and `schemas/alert.schema.json` both miscount the error/alert `category` vocabulary as "nine values" when it is ten.**

- **Where:** `architecture/DATA_CONTRACTS.md` §5: *"`category`'s nine values are taken verbatim from
  this phase's own prompt's 'FAILURE HANDLING' classification list"* — immediately followed by the
  actual list: `code | configuration | credentials | permissions | data | dependency | rate_limit |
  provider_outage | policy | unresolved_decision`. `schemas/alert.schema.json`'s top-level description
  repeats the same claim ("this phase's own prompt's nine-value FAILURE HANDLING classification
  list"), as does `HANDOFF_ANALYTICS_ENGINEER.md` Assumption 6 ("the nine-value FAILURE HANDLING /
  error-shape vocabulary") and `HANDOFF_WORKFLOW_STATE_DESIGNER.md`'s Facts and evidence bullet
  ("nine-value `category` vocabulary").
- **What's wrong:** Counting the quoted list gives exactly **ten** tokens, not nine. The enum in
  `schemas/alert.schema.json` itself is correct (ten values, matching `DATA_CONTRACTS.md` §5's list
  verbatim) — this is a documentation/prose arithmetic error, not a schema defect, but it is
  propagated identically across four separate documents written by three different specialists plus
  the Phase Owner, none of whom caught it.
- **Why it matters:** This project has twice before named exactly this failure mode as material
  (`findings.md` F-02-11/F-02-14: "wrong hand-maintained counts... vocabulary conformance is not
  arithmetic conformance"). A miscounted vocabulary size that nobody catches is a small instance of the
  same root cause: nobody re-counted a list before asserting its size, four times over.
- **Evidence:** direct count of the quoted enum in `architecture/DATA_CONTRACTS.md` §5 and
  `schemas/alert.schema.json`'s `category` property (both quoted in full in §2 reads above).

**M-3 — `architecture/STATE_MACHINE.md`'s own capability-classification table claims "11 states/edges match" against the registry, but the actual counts are 10 states and 12 transitions — neither is 11.**

- **Where:** `architecture/STATE_MACHINE.md`, final "Capability classification" table, row for §1:
  *"Faithfully restated and cross-checked against `policy/action_registry.json → state_machines.approval`
  (11 states/edges match — see this file's own citations)."*
- **What's wrong:** `policy/action_registry.json`'s `state_machines.approval` object has exactly 10
  entries in `states` and 12 entries in `transitions` (verified directly by loading and counting the
  JSON in §2 reads above, and by direct count of `APPROVAL_POLICY.md` §2's own 12-row transition
  table). "11" matches neither figure.
- **Why it matters:** Same class of defect as M-2 — an asserted count that is simply wrong on
  inspection, in a document whose entire stated purpose (§1's intro) is that it "cross-checked the
  state list against `policy/action_registry.json`... and it matches exactly." The underlying
  transcription is in fact correct (verified independently, §2 above and DECISIONS.md/`policy/action_registry.json`
  cross-read); only the summary count asserting *how* it was verified is wrong.
- **Evidence:** direct count of `policy/action_registry.json`'s `state_machines.approval.states` (10)
  and `.transitions` (12) arrays via the Python read in this review's tool calls.

**M-4 — The approval fixture set never exercises the `DETERMINISTIC_CODE` branch of `decided_by_role`, despite the Workflow State Designer's own handoff explicitly recommending it.**

- **Where:** `schemas/fixtures/approval.fixture.json` contains four records: `DRAFT`,
  `PENDING_APPROVAL`, `APPROVED`, `WITHDRAWN`. `HANDOFF_WORKFLOW_STATE_DESIGNER.md`'s "Recommended
  next action" states: *"I recommend the Schema QA Reviewer's fixture set for `approval` specifically
  include at least one record in `PENDING_APPROVAL`, `APPROVED`, and one terminal state reached via
  `DETERMINISTIC_CODE` (e.g. `EXPIRED` or `VOIDED`), to exercise all three branches of the
  `decided_by_role` actor split... If V-2 fails against my schema specifically, the conditionals are
  the first place to look, not the fixture."*
- **What's wrong:** The Schema QA Reviewer (Phase Owner, same run) built the fixture set without a
  `DETERMINISTIC_CODE`-decided record (no `EXPIRED`, `EXECUTED`, or `VOIDED` fixture instance), directly
  against a specific, reasoned recommendation from the specialist who designed the conditionals being
  tested. `task_plan.md`'s fixture-format minimum (initial state + one non-initial state) is technically
  satisfied, but the specific coverage gap the design author flagged as worth closing was not closed,
  and nothing in `findings.md`/`progress.md` records that this recommendation was seen and declined
  (versus simply missed).
- **Why it matters:** `schemas/approval.schema.json`'s `allOf` conditionals are this phase's most novel
  and highest-stakes structural guardrail (Invariant 1/5 enforcement). I independently confirmed the
  `PROJECT_OWNER`-required branch actually rejects agent roles (§4 below), so the conditional itself is
  sound — but the shipped fixture set, the thing V-2/V-3 are graded against, provides zero regression
  coverage for the `DETERMINISTIC_CODE` branch (`EXPIRED`/`EXECUTED`/`VOIDED`), the exact branch a
  future schema edit is most likely to break silently.
- **Evidence:** direct read of `schemas/fixtures/approval.fixture.json` (4 records, statuses listed
  above) against the handoff's explicit recommendation (quoted above).

**M-5 — `schemas/approval.schema.json`'s `allOf` conditionals constrain `decided_by_role`/`requested_by_role` but not the paired `decided_at`/`requested_at` timestamps, contrary to what the field descriptions imply.**

- **Where:** `schemas/approval.schema.json`, `decided_at` and `requested_at` property descriptions
  ("Null under the same conditions as `decided_by_role`") versus the `allOf` block, which has no
  conditional requiring `decided_at`/`requested_at` to be non-null when `decided_by_role`/`requested_by_role`
  is required to be set.
- **What's wrong:** I constructed and validated a record directly against the shipped schema using the
  `jsonschema` library (independent of `tools/schema_validate.py`): `status: APPROVED`, `decided_by_role:
  PROJECT_OWNER` (satisfying the existing conditional), but `decided_at: null`. **This record validates
  with 0 errors.** The same is true for `requested_at: null` on an otherwise-valid `PENDING_APPROVAL`+
  record. Full test and output:
  ```
  APPROVED decided_by_role=PROJECT_OWNER but decided_at=None (gap test) -> errors: 0
  APPROVED requested_by_role=PHASE_OWNER but requested_at=None (gap test) -> errors: 0
  ```
  (Full script and base record in this review's tool-call history; reproducible against the shipped
  `schemas/approval.schema.json` as-is.)
- **Why it matters:** The schema's own prose states these fields track together, but the structural
  guardrail — the thing this schema is praised in its own description for adding "beyond merely
  asserting it in prose" — does not actually enforce that pairing. A record could assert `APPROVED` by
  `PROJECT_OWNER` with no record of *when*, and pass validation. This does not violate any of the five
  invariants directly (none of them are about timestamps), so it is not a Critical/High finding, but it
  is a real, demonstrated gap between what the schema's comments claim and what the schema actually
  checks — exactly the category of claim this review was asked to test adversarially rather than take
  on faith.
- **Evidence:** `jsonschema.Draft202012Validator` run directly against `schemas/approval.schema.json`
  with the two constructed records above; 0 errors in both cases (reproduced in this review's tool
  calls, independent of `tools/schema_validate.py`).

---

### LOW

**L-1 — `product.fixture.json`'s second record is `ACTIVE` with a `pricing_approval_id` pointing at an approval record still in `DRAFT` (never submitted).**

- **Where:** `schemas/fixtures/product.fixture.json[1]` (`status: ACTIVE`, `pricing_approval_id:
  "9c9e159d-..."`) references `schemas/fixtures/approval.fixture.json[0]`, whose `status` is `DRAFT`,
  `requested_by_role`/`requested_at`/`decided_by_role`/`decided_at` all `null` — i.e., an approval
  request that has not even been submitted yet.
- **Why it matters:** Not a schema violation (`architecture/STATE_MACHINE.md` §2.1 explicitly says
  `pricing_approval_id` being non-null is "orthogonal" to `product.status`, and no cross-schema
  constraint is claimed or enforced anywhere in this phase, per `architecture/DATA_CONTRACTS.md` §7).
  But as a piece of illustrative fixture data it reads as though a product went `ACTIVE` under pricing
  that is still an unsubmitted draft proposal, which is exactly the kind of quiet inconsistency the
  task's cross-reference sanity check asked to be flagged, even though it is not a pass-condition
  failure.
- **Evidence:** direct read of both fixture files (quoted in full in §2 reads above).

**L-2 — `architecture/STATE_MACHINE.md`'s own intro sentence is internally contradictory about the invariant count.**

- **Where:** `architecture/STATE_MACHINE.md`, opening bullet 1: *"...a transition table, and four
  numbered invariants (renumbered from that section; `APPROVAL_POLICY.md` §3 states there are five
  invariants in total, the fifth being the self-approval prohibition folded into Invariant 1's 'no
  other edge to `APPROVED`' framing below and restated in full)..."*
- **What's wrong:** The parenthetical first says "four numbered invariants," then in the same
  breath says "`APPROVAL_POLICY.md` §3 states there are five invariants in total." The document's own
  §1.3 later correctly lists and transcribes all five invariants verbatim (verified against
  `APPROVAL_POLICY.md` §3 and `policy/action_registry.json`'s `invariants` array — both match exactly),
  so this is a confusingly-worded sentence, not a substantive transcription error, but it is the kind
  of sentence a careful re-read should have caught and simplified.
- **Evidence:** direct read of the passage (quoted above) against §1.3 of the same file and
  `APPROVAL_POLICY.md` §3 (both transcribe five invariants correctly).

---

## 4. Validation plan (V-1 – V-8): genuinely satisfied?

| # | Requirement | Verdict | Evidence |
|---|---|---|---|
| V-1 | Every schema is valid JSON and a valid JSON Schema 2020-12 document | **Satisfied** | `tools/schema_validate.py` calls `Draft202012Validator.check_schema` on all 8; my own run (§2.2) confirms 8/8 pass with no `check_schema` failures printed |
| V-2 | Every fixture record validates against its schema | **Satisfied** | My own run (§2.2): 19/19 fixture records validate, 0 failures, reproduced independently of the phase owner's claim |
| V-3 | Red mutation proves V-2 is not vacuously green | **Satisfied** | My own run (§2.3): 4/4 deliberately-broken records correctly rejected, including one targeting `approval.schema.json`'s Invariant 5 conditional specifically |
| V-4 | Every schema's `status` enum matches `STATE_MACHINE.md` exactly | **Satisfied** | Cross-read all seven entity `status` enums plus `approval`'s against `STATE_MACHINE.md` §2/§1; every enum is quoted verbatim, no drift found |
| V-5 | `approval.schema.json`'s `status` enum matches `APPROVAL_POLICY.md` §2 exactly, same order | **Satisfied** | Both lists compared token-by-token in this review: `DRAFT, PENDING_APPROVAL, APPROVED, CHANGES_REQUESTED, REJECTED, EXPIRED, WITHDRAWN, EXECUTED, SUPERSEDED, VOIDED` — identical order in both files |
| V-6 | Every schema's envelope fields match `DATA_CONTRACTS.md` §2.1 exactly (same 7 names, same types) | **Satisfied** | Verified across all 8 schemas by direct read; no envelope field renamed, retyped, or omitted anywhere |
| V-7 | `tools/idcheck.py` — no dangling ID citation, no dangling path | **Partially satisfied, and inaccurately reported.** IDs: 0 dangling, confirmed. Paths: **not** "5 reported... pre-existing or forward references" as `progress.md` claims — actual re-run finds 12–13 raw / 7 unique missing-path lines, only 2 of which are named in `findings.md` F-04-04. All 7 appear to be genuinely pre-existing or genuinely forward-referencing (none is a new, phase-04-introduced dangling reference to something that should exist and doesn't), so **V-7's substance is not violated**, but its **reporting** is inaccurate. See Finding H-2. | §2.4 above |
| V-8 | No realistic-looking personal-data-shaped placeholder in any fixture | **Satisfied** | All personal-data-shaped fields (`lead.fixture.json`'s `contact_name`, `email`, `phone`) use structurally-labeled placeholders (`fixture-contact-name-N`, `fixture-lead-email-N@example.invalid`, `fixture-phone-placeholder-2`); checked every other fixture file for a stray name/email/phone-shaped value and found none |

**Net:** 7 of 8 fully satisfied on both substance and reporting; V-7 is satisfied in substance but its
reporting in `progress.md`/`findings.md` materially understates what the tool actually found (Finding
H-2).

---

## 5. `Q-016` and `Q-009` handling — honest?

**`Q-016` (`D-052`):** checked against its actual scope. The resolution is narrow and accurately
described everywhere it is cited (`task_plan.md`, `DECISIONS.md`, `OPEN_QUESTIONS.md`,
`architecture/DATA_CONTRACTS.md` §1) — fixture location only, no wider claim smuggled in. No
overclaim found.

**`Q-009`:** checked for overclaiming or quiet narrowing. `task_plan.md`, `architecture/DATA_CONTRACTS.md`
§8, `schemas/lead.schema.json`'s own description, `architecture/STATE_MACHINE.md` §2.7, and both
`findings.md`/`progress.md`'s Phase 04 sections all consistently state `Q-009` is left exactly as
`UNRESOLVED` as before, that `lead.schema.json` is structural-only, and that the `DENY` under `ACT-W10`
requires **both** `Q-009` resolution **and** a non-Git storage substrate decision — this two-part
condition is stated correctly and consistently every time it appears, including inside the schema
file itself (not only in a policy document a future reader might not open). `OPEN_QUESTIONS.md`'s
own updated "Which of the remaining need the Project Owner personally" line explicitly says Phase 04
"did not attempt" the delegation option `Q-009`'s own text offers — an honest disclosure of a road not
taken, not a narrowing. **No overclaim or quiet narrowing found on either question.**

---

## 6. Quality rubric (scored independently; phase owner has not yet self-scored as of this review)

| Category | Score | Evidence |
|---|---:|---|
| Objective clarity | 5 | `task_plan.md`'s objective is a single, measurable outcome ("versioned schemas and deterministic lifecycle states... before dependent code is built"), matched by concrete deliverables |
| Inputs | 4 | Every input traced to a governing document and cross-checked (`APPROVAL_POLICY.md`, `policy/action_registry.json`, `DATA_RETENTION_POLICY.md`); docked for the propagated "nine values"/"11 states" miscounts (M-2, M-3) suggesting inputs were transcribed but not always re-verified by counting |
| Outputs | 5 | Named deliverables, real schemas, real paths, an explicit 8-item validation plan — the strongest category |
| Agent separation | 5 | One Phase Owner, two genuinely parallel specialists (verified independent per `F-00-07` discipline in both handoffs), one sequenced specialist, one Independent Reviewer (this report); no specialist wrote outside its assigned schema files |
| Tool realism | 5 | Real `jsonschema` 4.26.0 validator, real fixtures, real red-mutation self-test — all reproduced independently in this review with matching output |
| Permissions | 3 | Schema-level design correctly encodes least-privilege/fail-closed patterns (`additionalProperties: false`, `ACT-W10` DENY notices, role-restricted `decided_by_role` enum) — but this same phase committed a real, undisclosed write to `CLAUDE.md`, a file with no ownership grant in `task_plan.md` (Finding H-1), which is precisely a permissions/scope violation in the phase's own conduct, not merely its deliverable design |
| Determinism | 4 | Versioning (§3), idempotency-key rule (§4), and the approval schema's `allOf` conditionals are genuine deterministic guardrails, independently confirmed to reject invalid agent-role approvals (§2 tool calls); docked one point for the confirmed `decided_at`/`requested_at` nullability gap (M-5) |
| Failure handling | 4 | Shared error shape (§5) with a closed `category` vocabulary, `D-047` discipline followed with no invented thresholds anywhere across 8 schemas; docked for the vocabulary being miscounted in its own defining document (M-2) |
| Testing | 3 | V-1/V-2/V-3 mechanically verified and reproduced exactly as claimed (a genuine strength) — but the `idcheck.py` (V-7) claim in `progress.md` does not match reality (Finding H-2), which is exactly the "green result is not evidence" failure mode this project has flagged twice before (`F-01-04`, `F-02-14`); this project's own `D-028` sets an elevated floor of 4 for this category, which this phase does not meet |
| Auditability | 3 | Handoffs are unusually thorough and self-critical (assumptions named per specialist, per `F-00-05` discipline, with real caught-and-fixed bugs disclosed, e.g. `F-04-02`) — but a real file edit (`CLAUDE.md`, Finding H-1) is completely undisclosed in `findings.md`/`progress.md`, and the `idcheck.py` result is under-reported (Finding H-2); an audit trail this thorough should not have two gaps this concrete |
| User usability | 4 | Every schema's field descriptions are unusually explicit about *why*, not just *what*, aiding a future implementer; per-field constraints (D-047 discipline) are well explained |
| Portability | 5 | Standard JSON Schema 2020-12 throughout, no vendor lock-in, stable literal `$id` values explicitly disclosed as non-resolving |

**Average: (5+4+5+5+5+3+4+4+3+3+4+5) / 12 = 50 / 12 ≈ 4.17**

No category scores below 3, and the average clears 4 — but per `CLAUDE.md` §7 / `D-028`'s elevated
floor ("Permissions / Testing / Failure handling ≥ 4"), **Permissions (3) and Testing (3) both fall
below the required floor.** The rubric's own stated passing threshold ("Security, permissions,
testing, and failure handling must each score 4 or higher") is therefore **not met**, independent of
the average.

---

## 7. Overall recommendation: **CONDITIONAL PASS**

**Reasoning.** The schemas, fixtures, and state-machine documentation are substantively strong: every
mechanical claim I could independently reproduce (V-1 through V-6, V-8, and the `--selftest`
red-mutation proof) reproduced exactly as claimed, the approval schema's Invariant 1/5 guardrail is
real and I confirmed it independently rejects an agent role attempting to satisfy `APPROVED`, and the
handoffs are unusually candid about their own assumptions and a self-caught bug (`F-04-02`). `Q-009`
and `Q-016` are both handled honestly, with no overclaim.

But this phase does not clear its own project's bar for an unconditional PASS: **one undisclosed,
unassigned write to `CLAUDE.md` (H-1)** — the exact class of defect this project's own `findings.md`
(`F-00-09`) says "had to be disclosed" the first time it happened — and **one mechanical-check result
reported inaccurately in `progress.md` (H-2)**, where the actual `idcheck.py` output (12–13 raw / 7
unique missing paths) is materially larger than the "5" claimed and only two of the seven distinct
paths are explained anywhere. Both are real, reproducible, and neither is hidden by this report — but
neither should have reached this review unaddressed, and `D-028`'s elevated floor on Testing and
Permissions is not met as a direct consequence.

**Recommended conditions before an unconditional PASS:**
1. Disclose the `CLAUDE.md` §14 edit explicitly in `findings.md`/`progress.md` (or revert it and add
   the content through an assigned owner in a future phase) — H-1.
2. Correct `progress.md`'s Phase 04 section and `findings.md` F-04-04 to state the actual `idcheck.py`
   output (7 distinct missing paths, not 5) and account for the three currently unnamed ones
   (`.claude/settings.local.json`, `.vscode/extensions.json`, `redtest_tmp.md`) — H-2.
3. Reconcile `MASTER_PLAN.md` rows 15 and 17 so `schemas/approval.schema.json` and
   `schemas/lead.schema.json` are not listed as pending deliverables of phases that would now be
   redoing already-delivered work — M-1.
4. Fix the two miscounted-vocabulary statements ("nine values," "11 states/edges match") — M-2, M-3.

None of these require reopening the schemas' actual design, and none touches `Q-009`. All four are
inexpensive corrections; the Phase Owner should address them and the gate report should record what
changed, per this project's own standing practice for conditional passes (`APPROVAL_POLICY.md` §10's
worked example).
