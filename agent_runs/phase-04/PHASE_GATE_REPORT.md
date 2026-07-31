# Phase Gate Report

## Metadata
- Phase: 04 — Data Contracts and State Model
- Run ID: `phase-04-2026-07-31-a`
- Date: 2026-07-31
- Phase owner: Atlas Orchestrator (Phase 04)
- Independent reviewer: Independent Reviewer (fresh; authored none of the work under review) — `agent_runs/phase-04/REVIEW_REPORT.md`
- Git commit/branch: `main`, uncommitted at time of writing (commit pending this report; local repo initialized this session, baseline `3fb83a4`, private remote `cronek420/agent-atlas-growth-department-reviewed`)

## Objective

Define versioned schemas and deterministic lifecycle states before dependent code is built (this phase's own prompt's measurable objective, verbatim).

## Inputs

### Confirmed
Approval state machine (`APPROVAL_POLICY.md` §2: 10 states, six terminal, 12-row transition table, five invariants); six-role vocabulary (`policy/action_registry.json`); fail-closed default (`D-044`); no-invented-numbers rule (`D-047`); Phase 03 gate PASS (prerequisite satisfied).

### Inferred
None — this phase introduced no `INFERRED`-class claim.

### Proposed
Everything in `architecture/DATA_CONTRACTS.md` and `architecture/STATE_MACHINE.md` §2 (per-entity transition tables) is explicitly `PROPOSED` in its own capability-classification section — structural design, not enforced by any runtime.

### Unresolved
`Q-009` (data-privacy handling) — shapes `schemas/lead.schema.json` but does not block this phase; left exactly as open as found, no default proposed.

### Blocked
None for this phase. `Q-004` remains the project's only `BLOCKED` item and does not touch Phase 04.

## Agents and assignments

| Role | Assignment | Ran |
|---|---|---|
| Phase Owner | T0 (contract, `D-052`/`D-053`), T3 (fixtures, validator), T4 (integration), T6 (findings remediation, this report) | Throughout |
| Data Architect | `product`, `brand`, `content`, `campaign` schemas | Parallel wave 1 |
| Analytics Engineer | `experiment`, `alert`, `lead` schemas | Parallel wave 1 (one retry after a transient harness auth error before any work began) |
| Workflow State Designer | `approval.schema.json`, `architecture/STATE_MACHINE.md` | Sequential, after wave 1 (genuine dependency — cites wave 1's actual field choices) |
| Independent Reviewer | `agent_runs/phase-04/REVIEW_REPORT.md` | After all deliverables existed; authored none of them |

Sequencing followed `F-00-07`'s lesson explicitly: the two wave-1 specialists were genuinely independent (neither read the other's assigned schemas); the Workflow State Designer was deliberately serialized after them rather than parallelized, since its work cites their field choices.

## Deliverables

`architecture/DATA_CONTRACTS.md`, `architecture/STATE_MACHINE.md`, `schemas/product.schema.json`, `schemas/brand.schema.json`, `schemas/content.schema.json`, `schemas/campaign.schema.json`, `schemas/experiment.schema.json`, `schemas/alert.schema.json`, `schemas/lead.schema.json`, `schemas/approval.schema.json`, `schemas/fixtures/*.fixture.json` (8 files), `tools/schema_validate.py`, three handoffs, this report, `agent_runs/phase-04/REVIEW_REPORT.md`.

## Files changed

**Created:** all files listed above under Deliverables, plus `DECISIONS.md` (`D-052`, `D-053` rows and Phase 04 section), `OPEN_QUESTIONS.md` (`Q-016` resolved), `findings.md` (`F-04-01`–`F-04-05`), `progress.md` (Phase 04 section), `CURRENT_PHASE.md` (Phase 04 status block), `MASTER_PLAN.md` (Phase 04 row updated; Phase 15/17 rows reconciled; Q-008/Q-014/Q-016/Q-017 rows corrected from stale `UNRESOLVED`), `task_plan.md` (rewritten for this phase).

**Modified after independent review**, addressing findings (see "Reviewer findings" below): `schemas/approval.schema.json` (two new `allOf` conditionals, M-5), `schemas/fixtures/approval.fixture.json` (added a 5th, `EXPIRED`/`DETERMINISTIC_CODE` record, M-4), `schemas/fixtures/product.fixture.json` (L-1), `architecture/DATA_CONTRACTS.md` §5 and `schemas/alert.schema.json` (M-2, "nine" → "ten"), `architecture/STATE_MACHINE.md` (M-3, L-2), `tools/schema_validate.py` (added a 5th red mutation proving the M-5 fix), `findings.md` (F-04-04 corrected, F-04-05 added), `progress.md` (H-2 correction), `MASTER_PLAN.md` (M-1 reconciliation).

**Not modified:** any Phase 00–03 deliverable, `RISK_REGISTER.md`, `NON_GOALS.md`, `SCOPE.md`, `ACCEPTANCE_CRITERIA.md`, any policy document (`SECURITY_POLICY.md`, `APPROVAL_POLICY.md`, etc. — read only, never written), `.agent/skills/` (untracked, unrelated).

## Tests actually run

| Test | Command | Result | Evidence |
|---|---|---|---|
| Schema + fixture validation (initial) | `python tools/schema_validate.py` | 8/8 schemas valid, 19/19 fixture records validate | This session's terminal output |
| Red-mutation proof (initial) | `python tools/schema_validate.py --selftest` | 4/4 caught, 0 missed | This session's terminal output |
| Schema + fixture validation (post-fix) | `python tools/schema_validate.py` | 8/8 schemas valid, **20/20** fixture records validate | This session's terminal output, re-run after M-4/L-1 fixture edits |
| Red-mutation proof (post-fix) | `python tools/schema_validate.py --selftest` | **5/5** caught, 0 missed (new 5th mutation added to prove the M-5 fix) | This session's terminal output |
| ID/path integrity | `python tools/idcheck.py . <all changed/new files>` | 0 dangling `D-`/`Q-`/`R-`/`NG-`/`F-` citations across two full-scope runs (mine, then the reviewer's broader one) | This session's terminal output; `REVIEW_REPORT.md` §2.4 |
| Staleness scan (`CSK-01`) | `python tools/blast_radius_check.py --phase-id 04 --baseline-ref 3fb83a4` | `verdict: REVIEW_REQUIRED`, 16 unique candidates, all 16 individually inspected and dispositioned **not stale** (false-positive keyword matches on `schemas`/`architecture` in unrelated future-phase rows, or already-correctly-preserved historical record) | This session's terminal output; dispositions below |
| Independent review | Agent dispatch, fresh context, authored none of the work | CONDITIONAL PASS, rubric 4.17, Permissions=3/Testing=3 (below `D-028` floor) | `agent_runs/phase-04/REVIEW_REPORT.md` |
| Personal-data placeholder scan | Python script scanning all 8 fixture files for realistic name/email patterns | 0 suspicious values | This session's terminal output |

**`CSK-01` disposition detail** (16 unique candidates, none confirmed stale):
- `DECISIONS.md:60` (`D-026`), `DECISIONS.md:87` (`D-034`) — unrelated to this phase's changes; still accurate.
- `CURRENT_PHASE.md:47`, `CURRENT_PHASE.md:65` — preserved historical record from the Phase 02 owner's own notes, explicitly marked "not rewritten" in this file's own header; already superseded by content above it, not newly stale.
- `MASTER_PLAN.md` rows for Phases 05, 06/07(implicit), 13–22 (lines 70, 73, 78–87) — each still correctly `NOT STARTED`; false-positive keyword matches on `schemas`/`architecture` naming *those phases'* own future deliverables, unaffected by Phase 04's different files. (Note: rows 15 and 17 specifically *were* stale in a way `CSK-01`'s keyword heuristic did not itself catch — found instead by the Independent Reviewer's direct read, Finding M-1, and fixed; see below.)

## Reviewer findings

Full detail: `agent_runs/phase-04/REVIEW_REPORT.md`. Summary and disposition:

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| H-1 | High | `CLAUDE.md` §14 was edited earlier this session (a separate, user-requested `/init` addition predating this phase) with no disclosure against Phase 04's own file-ownership table | **Fixed** — disclosed as `findings.md` F-04-05, with honest timeline (predates this phase's kickoff; the gap was in disclosure, not in an in-phase file-ownership violation) |
| H-2 | High | `progress.md` claimed `tools/idcheck.py` found "5" missing paths; a fuller run finds 18 raw / 6 distinct | **Fixed** — `findings.md` F-04-04 rewritten with the accurate count and per-path explanation; `progress.md` corrected |
| M-1 | Medium | `MASTER_PLAN.md` still listed `schemas/approval.schema.json` (Phase 15) and `schemas/lead.schema.json` (Phase 17) as pending future deliverables after Phase 04 delivered both | **Fixed** — both rows annotated to point at Phase 04's delivery, clarifying Phase 15/17 build workflow atop the schema, not a second copy of it |
| M-2 | Medium | "nine values" miscounted (actual: ten) for the `category`/error-shape vocabulary, propagated across `DATA_CONTRACTS.md` §5 and `alert.schema.json` | **Fixed** in both authoritative files. (Handoffs, which also repeated the miscount, are historical records of what was said at the time and are not rewritten, consistent with this project's append-only practice for authored records.) |
| M-3 | Medium | `STATE_MACHINE.md`'s own classification table claimed "11 states/edges match" against the registry; actual counts are 10 states, 12 transitions | **Fixed** — corrected to the accurate counts, with a note explaining the correction |
| M-4 | Medium | Approval fixture set never exercised the `DETERMINISTIC_CODE` branch of `decided_by_role`, despite the schema's own designer recommending it | **Fixed** — added a 5th fixture record (`EXPIRED`, `decided_by_role: DETERMINISTIC_CODE`); re-validated, 20/20 |
| M-5 | Medium | `approval.schema.json`'s `allOf` conditionals didn't require `decided_at`/`requested_at` non-null when their paired role field was set — reviewer demonstrated a passing record that should have failed | **Fixed** — two new `allOf` conditionals added; a 5th red mutation added to `tools/schema_validate.py --selftest` specifically proving the fix (CAUGHT, confirmed) |
| L-1 | Low | `product.fixture.json`'s second record was `ACTIVE` with `pricing_approval_id` pointing at a still-`DRAFT`, unsubmitted approval | **Fixed** — set to `null`, matching the schema's own documented orthogonality between `status` and `pricing_approval_id` |
| L-2 | Low | `STATE_MACHINE.md`'s intro sentence was internally confusing about the invariant count (said both "four" and "five" in one breath) | **Fixed** — reworded; substance (all five invariants correctly transcribed in §1.3) was never wrong, only this summary sentence |

**All eight findings addressed with recorded evidence, none silently dropped.** No Critical finding was raised. **Not done:** a second, fresh independent-review pass over the fixes themselves — the fixes were verified by re-running the same mechanical tools (`schema_validate.py`, `idcheck.py`) that the reviewer also ran independently, but no fresh human-style adversarial re-read occurred after the fixes. Disclosed here as a real limitation, following this project's precedent (Phase 03's gate report fixed findings mid-run and self-scored the result without a second reviewer pass) rather than silently presented as equivalent to a second review.

## Security, privacy, permission, and policy checks

- **Fail-closed:** `additionalProperties: false` at every object level in all 8 schemas, verified by direct read and by the red-mutation test (an injected unrecognized field on `lead.schema.json` is correctly rejected).
- **Least privilege / role vocabulary:** every `created_by_role`-shaped field restricted to `policy/action_registry.json`'s six roles; `approval.schema.json`'s `decided_by_role`/`requested_by_role` further restricted to exactly the actors `APPROVAL_POLICY.md` §2's transition table assigns, with no agent role able to satisfy the `APPROVED` conditional (Invariant 5) — independently confirmed by the reviewer constructing a rejected test record.
- **`D-047` (no invented numbers):** checked across all 8 schemas and `STATE_MACHINE.md`; no numeric threshold (retry count, TTL, confidence level, significance threshold, minimum/maximum duration) is asserted anywhere. Every place one might plausibly appear is explicitly left blank/null/"owner judgment, no threshold defined."
- **`Q-009`/personal data:** `schemas/lead.schema.json` is structural-only; its own description states the `DENY` (`ACT-W10`) explicitly and ties it to both `Q-009` resolution *and* a non-Git storage substrate decision, never overclaiming partial progress. Every fixture file scanned for realistic-looking personal-data placeholders; none found — `lead.fixture.json` uses `fixture-`-prefixed names and `.invalid`-domain emails throughout.
- **Secrets:** no secret-shaped string in any deliverable (visual scan plus the existing project convention of `.invalid`/`fixture-` placeholders).
- **RDBC boundary:** never accessed by any agent this phase.
- **First third-party dependency (`jsonschema`):** disclosed (`findings.md` F-04-01), local/free/no-account, necessary to satisfy this phase's own pass condition with real evidence rather than a hand-rolled, unverifiable validator.

## Quality rubric

Self-scored, on the corrected (post-remediation) state, cross-referenced against the Independent Reviewer's own pre-remediation score (4.17 average; Permissions 3, Testing 3 — below the `D-028` floor of 4 for both). Per this project's Phase 03 precedent, fixing findings before finalizing the gate report is the established practice, disclosed rather than silently absorbed.

| Category | Score 0–5 | Evidence |
|---|---:|---|
| Objective clarity | 5 | Single measurable outcome (versioned schemas + deterministic lifecycle states before dependent code), matched by 8 named schema files and a state-machine document |
| Inputs | 4 | Every input traced to a governing document; docked one point for the M-2/M-3 miscounts the reviewer found — a real, if minor, verification gap in the original work, now fixed |
| Outputs | 5 | Named deliverables, real schemas at real paths, an explicit 8-item validation plan (V-1–V-8), all independently reproduced by the reviewer |
| Agent separation | 5 | One phase owner, two genuinely parallel specialists (verified independent), one correctly-sequenced specialist, one independent reviewer who authored nothing under review |
| Tool realism | 5 | Real `jsonschema` 4.26.0 validator, real fixtures, real red-mutation self-test (5/5), all independently reproduced by the reviewer with matching output |
| Permissions | 4 | Schema-level fail-closed/least-privilege design is strong and independently confirmed (reviewer constructed and validated a rejected test record). Reviewer's original score (3) was driven entirely by H-1 (undisclosed `CLAUDE.md` edit); now disclosed (`F-04-05`). Not raised to 5: the edit still occurred outside any formal `task_plan.md` ownership grant, even though it predates this phase and is now disclosed — a residual process imperfection |
| Determinism | 4 | Versioning, idempotency-key rule, and (after the M-5 fix) `approval.schema.json`'s `allOf` conditionals are genuine, independently-confirmed deterministic guardrails; docked one point because the underlying design initially shipped with the M-5 gap, only caught by review |
| Failure handling | 4 | Shared error shape with a closed, `D-047`-compliant vocabulary (now correctly counted, M-2); a specialist caught and fixed a real bug in its own draft before handoff (F-04-02) |
| Testing | 4 | V-1–V-3, V-4–V-6, V-8 all mechanically verified and independently reproduced by the reviewer with exactly matching output; reviewer's original score (3) was driven entirely by H-2 (the idcheck.py under-reporting), now corrected with an accurate count and full explanation. Not raised to 5: no fresh reviewer pass re-verified the post-fix state (disclosed above) |
| Auditability | 4 | Handoffs are unusually thorough and self-critical (assumptions named per specialist, a real caught-and-fixed bug disclosed); both gaps the reviewer found (H-1, H-2) are now closed and the closure itself is recorded in `findings.md`, not silently folded in |
| User usability | 4 | Every schema field explains *why*, not just *what*; `D-047` discipline stated inline on the relevant fields themselves, not only in a separate policy document |
| Portability | 5 | Standard JSON Schema 2020-12 throughout, no vendor lock-in, literal (non-resolving) `$id` values explicitly disclosed as such |

**Average: (5+4+5+5+5+4+4+4+4+4+4+5) / 12 = 53 / 12 ≈ 4.42.** No category below 3. Both previously-sub-floor categories (Permissions, Testing) now meet `D-028`'s elevated floor of 4, with the specific defect that drove each score explicitly named, fixed, and cross-referenced rather than the score being raised without cause.

## Known limitations

- **Documentation/schema contract, not enforcement.** Every guardrail in this phase — including `approval.schema.json`'s `allOf` conditionals — is a JSON Schema-level structural check, not the deterministic enforcement code Architecture Rule 3 (`D-003`) still assigns to a future phase (no `src/` exists before Phase 16).
- **No fresh independent-review pass over the post-fix state.** Disclosed above under "Reviewer findings" — the fixes were mechanically re-verified but not re-read adversarially by a reviewer with no prior context.
- **`Q-009` remains genuinely open**, exactly as this phase found it. `lead.schema.json` cannot be operationally exercised until it resolves and a non-Git storage substrate is decided.
- **`F-04-03`'s gap stands**: no entity schema exists for `GC-08` (spending) or `GC-09` (paid advertising). Flagged for a future phase (candidate: Phase 22), not fixed here — out of this phase's assigned deliverable list.
- **`CSK-01`'s keyword heuristic did not itself catch `MASTER_PLAN.md`'s Phase 15/17 staleness (M-1)** — it flagged those rows as generic candidates (correctly, per its own contract) but the actual disposition (stale vs. not) required the Independent Reviewer's direct read, not the mechanical tool alone. Consistent with `tools/README.md`'s own stated limitation that mechanical checks catch shape, not always meaning.
- **`R-24` (Phase 02's own unremediated review findings) remains open**, inherited and not this phase's to close.

## Rollback

No external system touched, no credential introduced, no capability invoked beyond local file reads/writes and (separately, at the user's explicit direction, before this phase began) one local `git init` and one GitHub private-repo creation/push. To roll back this phase specifically: revert every file listed under "Files changed" above; none of it affects anything outside this working tree. Nothing has been pushed to the remote since this phase began, so a rollback here has no off-machine consequence yet.

## Gate decision

**Recommendation: PASS.**

The Independent Reviewer's original recommendation was CONDITIONAL PASS, with four named conditions (H-1, H-2, M-1, M-2/M-3 treated together) plus three additional findings (M-4, M-5, L-1, L-2) not framed as blocking conditions but as real, worth-fixing gaps. **All eight findings — every one raised, at every severity — have been fixed, with recorded command output proving each fix**, not merely asserted: the M-5 schema gap is closed and mechanically proven via a new red mutation (CAUGHT); the M-4 fixture gap is closed with a new record exercising the previously-untested branch; H-1 and H-2 are disclosed/corrected in the audit trail itself, not just in this report. No Critical finding was ever raised. No fabrication, invented fact, secret, personal-data value, or `Rough-Draft-Builders-Club` boundary violation was found anywhere, by either the reviewer or this integration pass.

This mirrors the project's own Phase 03 precedent exactly: findings found mid-run, fixed before the gate report was finalized, disclosed rather than absorbed, and a PASS recommendation made on that basis rather than waiting for a second review cycle. The one honestly-disclosed gap — no fresh adversarial re-read of the post-fix state — is named above, not hidden, and is the Project Owner's to weigh.

**Gate decisions are recorded by the Project Owner, not by an agent (`CLAUDE.md` §7).** This is a recommendation.

## Exact next owner action

1. Read this report and `agent_runs/phase-04/REVIEW_REPORT.md` in full.
2. Confirm the evidence for each of the 8 findings' fixes (all commands and output are reproducible — re-run `python tools/schema_validate.py`, `python tools/schema_validate.py --selftest`, `python tools/idcheck.py` yourself if you want independent confirmation beyond this report).
3. Record **PASS**, **CONDITIONAL PASS** (e.g. conditioned on a fresh reviewer pass over the fixes), or **FAIL** in `CURRENT_PHASE.md`, with the date. Silence is never consent.
4. Once recorded, commit and push (nothing from this phase is committed yet — the local repo and remote were only just created this session).
5. **Phase 05 may then be started by pasting `phase-prompts/PHASE_05_GOOGLE_DRIVE_LIVING_DOCUMENT_CONTROL_CENTER.md`** — but note `Q-004` (Google Drive folder access) is `BLOCKED`, the project's only such item, and gates real execution of that phase regardless of this gate's outcome.
