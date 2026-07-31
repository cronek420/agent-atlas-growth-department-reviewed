# Phase 03 Governance Audit Report

- **Run ID:** `phase-03-2026-07-30-b`
- **Date:** 2026-07-30
- **Auditor role:** Independent Governance Auditor. I authored no Phase 03 deliverable, policy
  document, registry row, tool, or handoff under audit here. This audit is independent of, and
  was conducted without coordination with, the parallel Independent Reviewer.
- **Scope:** completeness/coverage audit of Phase 03 against the phase prompt's own stated pass
  conditions (`phase-prompts/PHASE_03_GOVERNANCE_SECURITY_APPROVAL_AND_AUTONOMY_POLICIES.md`),
  not primarily a fabrication hunt (that is the parallel Independent Reviewer's job, per the
  brief).
- **Materials read in full before writing this report:** `CLAUDE.md` (§11's Phase-02 extension,
  §13); the Phase 03 prompt; `PROMPT_AND_BUILD_QUALITY_RUBRIC.md`; `ACCEPTANCE_CRITERIA.md`
  §Phase 03; `policy/POLICY_CONTRACT.md`; `policy/action_registry.json`; all eight deliverables
  (`SECURITY_POLICY.md`, `APPROVAL_POLICY.md`, `AUTONOMY_POLICY.md`, `BUDGET_POLICY.md`,
  `PUBLISHING_POLICY.md`, `MESSAGING_POLICY.md`, `DATA_RETENTION_POLICY.md`,
  `AGENT_PERMISSION_MATRIX.md`); `tools/render_permission_matrix.py`, `tools/policy_check.py`,
  `tools/policy_check_selftest.py`, `tools/blast_radius_check.py` against its `CUSTOM_SKILL_BACKLOG.md`
  §"CSK-01" contract; `task_plan.md`; `DECISIONS.md` §`D-041`–`D-048` and the real `D-036`–`D-040`;
  `findings.md` `F-03-01`/`F-03-02`; all four Phase 03 handoffs; `CAPABILITY_REGISTRY.md`
  §"Vocabularies"; `SKILL_SECURITY_POLICY.md` §0; `RISK_REGISTER.md` (R-13, R-14, R-20–R-24);
  `OPEN_QUESTIONS.md` (Q-008, Q-017); `git status` and `git diff` against the working tree.

---

## 0. A finding that has to come first: this audit's own output file, and its sibling, were
   already occupied by leftovers from the discarded first attempt

Before writing anything, I found that `agent_runs/phase-03/GOVERNANCE_AUDIT_REPORT.md` (the file
I was assigned to write) and `agent_runs/phase-03/REVIEW_REPORT.md` (the Independent Reviewer's
file) **already existed on disk**, both self-labeled `Run ID: phase-03-2026-07-30-a` — the
discarded first attempt. Both are built entirely around that attempt's central, now-false premise
("Phase 02 was never executed," `CAPABILITY_REGISTRY.md` does not exist, `RUNTIME_AGENT` is
wholesale unresolved) and both recommend action on that basis (the old `GOVERNANCE_AUDIT_REPORT.md`
scored the phase and gave a conditional-PASS recommendation against **that** premise; the old
`REVIEW_REPORT.md`'s Finding 1 is literally the discovery of PR #1, i.e. the event that caused the
`-a → -b` restart in the first place).

**This is the same class of contamination `F-03-01` describes for the eight root-level policy
documents** — an uncommitted draft from `phase-03-2026-07-30-a` surviving a `git reset --hard`
because that command does not delete untracked files — **but it was not disclosed anywhere.**
Every one of the eight root-level deliverables carries an explicit "Superseded-content notice"
recording exactly this history (see e.g. `SECURITY_POLICY.md`'s header, `PUBLISHING_POLICY.md`'s
header). `task_plan.md`, `findings.md`, and `DECISIONS.md` all discuss the discarded `policy/`,
`tools/`, and eight `.md` deliverables from attempt `-a` — but none of them mentions
`agent_runs/phase-03/GOVERNANCE_AUDIT_REPORT.md` or `agent_runs/phase-03/REVIEW_REPORT.md` at
all. I confirmed this with `grep` across `task_plan.md`, `findings.md`, `DECISIONS.md`, and all
four handoffs: zero mentions of either filename outside the ownership table and one handoff's
"files I did not touch" disclaimer.

**Consequence for pass condition 5 specifically (§2.5 below):** the artifact that is supposed to
be the durable evidence of the Independent Reviewer's prose cross-read (`D-041`'s second,
person-performed check) is, as of the moment I audited, a review of a different, discarded set
of documents. It provides no evidence about the real, current eight deliverables at all — its
findings are about defects (the false Phase-02-absence premise) that do not exist in the current
documents, which correctly cite the real `D-036`–`D-040` and the real 141-row
`CAPABILITY_REGISTRY.md` throughout.

**What I did about it, within my own scope:** I am overwriting `GOVERNANCE_AUDIT_REPORT.md` (the
file assigned to me) with the genuine audit below, against the real current repository state. I
did **not** touch `REVIEW_REPORT.md` — that is the Independent Reviewer's file, not mine, and
`ACT-W02` denies me writing outside my own assignment. I flag its staleness here because it bears
directly on whether pass condition 5 can be certified met, and because the phase owner needs to
know before the gate report is written that the currently-recorded "prose cross-read" is not
evidence of anything that happened against the real documents.

**Recommendation:** before the gate report, the phase owner should either (a) confirm a fresh,
real Independent Reviewer pass produced a new `REVIEW_REPORT.md` reflecting the actual eight
current deliverables, or (b) if `agent_runs/phase-03/REVIEW_REPORT.md` still reads as it did when
I read it, record in `findings.md` that it is stale/inapplicable and that the prose half of
`D-041`'s requirement is not yet demonstrated for the real documents.

---

## 1. Mechanical check results (actual output, run by this auditor)

```
$ python tools/policy_check.py
[PASS] V-1 - All 8 deliverables exist and are non-empty
[PASS] V-2 - action_registry.json parses as JSON
[PASS] V-3 - Every action outcome is a valid enum token
[PASS] V-4 - Unmatched action resolves to fail-closed DENY
[PASS] V-5 - No two rows assign different outcomes to the same statement
[PASS] V-6 - All 9 gated categories referenced at APPROVAL_REQUIRED or stricter
[PASS] V-7 - Every cited D-/Q-/R-/NG-/CNG-/F- identifier resolves against the real registers
[PASS] V-8 - Every action's referenced policy file exists
[PASS] V-9 - Approval state machine integrity (reachability, terminal states, owner-only APPROVED)
[PASS] V-10 - Every promotion edge advances exactly one ladder stage
[PASS] V-11 - Every non-DISABLED autonomy stage has a one-hop edge to DISABLED
[PASS] V-12 - AGENT_PERMISSION_MATRIX.md matches action_registry.json (no drift)
[PASS] V-13 - No secret-shaped strings in any Phase 03 deliverable

13/13 checks passed.
```

```
$ python tools/policy_check_selftest.py
=== Negative control 1..12 === all [CAUGHT]
Positive control — real registry/deliverables: 13/13 passed (OK)

ALL 12 NEGATIVE CONTROLS CAUGHT. Positive control clean. policy_check.py is trustworthy.
```

```
$ python tools/render_permission_matrix.py --check
OK: AGENT_PERMISSION_MATRIX.md matches action_registry.json.
```

```
$ python tools/blast_radius_check.py --phase-id 03 --baseline-ref acabca8
{ "verdict": "REVIEW_REQUIRED", "checked": [8 files], "unreadable": [], "candidates": [19 raw
  lines → 8 unique (file, line) pairs, matching findings.md F-03-02's disposition table almost
  exactly (RISK_REGISTER.md:76/77, DECISIONS.md:55/87, CURRENT_PHASE.md:10/28,
  MASTER_PLAN.md:87, CAPABILITY_REGISTRY.md:168) }
```

All four commands were executed directly by me from the repo root (Python 3.14.6) and exited 0.
`policy_check_selftest.py` is itself load-bearing: it deliberately breaks each of the 13
properties `policy_check.py` claims to verify and confirms the checker goes red on every one —
this satisfies `findings.md` `F-01-04`'s standard ("an unverified checker produces unverified
results"). The `blast_radius_check.py` run reproduces, independently, essentially the same
candidate set `findings.md` `F-03-02` records as already dispositioned — good corroboration that
`F-03-02`'s account of the tool's first real run is accurate and reproducible, not merely
asserted.

---

## 2. Per-pass-condition findings

### 2.1 All high-risk actions require approval — **MET**

Walked all nine gated categories against `policy/action_registry.json`:

| Category | Referencing action(s) | Outcome today | Assessment |
|---|---|---|---|
| GC-01 claims | `ACT-P05` | `DENY` | Real row, stricter than the floor |
| GC-02 pricing | `ACT-P05` | `DENY` | Real row, stricter than the floor |
| GC-03 discounts | `ACT-P05` | `DENY` | Real row, stricter than the floor |
| GC-04 testimonials | `ACT-P05` | `DENY` | Real row, stricter than the floor |
| GC-05 direct outreach | `ACT-S01` | `DENY` | Real row, stricter than the floor |
| GC-06 complaints | `ACT-S01` | `DENY` | Real row, stricter than the floor |
| GC-07 controversial topics | `ACT-P05` | `DENY` | Real row, stricter than the floor |
| GC-08 spending | `ACT-M01`, `ACT-M02`, `ACT-M04` | `DENY` / `DENY` / `OWNER_ONLY` | Real rows, stricter |
| GC-09 paid advertising | `ACT-M03` | `DENY` | Real row, stricter than the floor |

Every category resolves at or above `APPROVAL_REQUIRED` in the strictness order (`DENY` >
`BLOCKED` > `OWNER_ONLY` > `APPROVAL_REQUIRED` > `ALLOW_LOGGED` > `ALLOW`) — none is a bare label
with no enforced outcome, and `V-6`'s negative control (stripping `GC-05` from every action)
demonstrates the mechanical check actually fires rather than passing vacuously.

**Precision worth stating plainly, because a future reader could otherwise misread "requires
approval" as meaning the literal token `APPROVAL_REQUIRED`:** none of the nine categories sits at
that literal token today. All nine are pinned at `DENY` (eight rows) or `OWNER_ONLY` (the
payment-authorization row) because no publishing, messaging, or spending capability exists at all
(every production-facing capability is `DISABLED`, `D-010`). `PUBLISHING_POLICY.md` §2 and
`MESSAGING_POLICY.md` §2 both state this precisely: denied today because the capability to
execute doesn't exist; becomes `APPROVAL_REQUIRED` and never weaker once it does. `DENY` is
stricter than `APPROVAL_REQUIRED` in the registry's own order, so this is margin above the pass
condition, not a shortfall against it. `APPROVAL_POLICY.md` §6 states the same design intent but
less precisely in one place — see §5 below.

### 2.2 Default is fail-closed — **MET**

- `action_registry.json` sets `"default_outcome": "DENY"` at the top level, basis
  `docs/PROJECT_BOUNDARIES.md §8` and `D-008`.
- `V-4` is a genuine behavioral test, not a field-presence check: it evaluates a nonsense
  role/verb/resource combination against the reference evaluator and asserts the returned outcome
  is `DENY`. The negative control (flipping `default_outcome` to `ALLOW`) confirms `V-4` catches
  it.
- I read all eight policy documents specifically looking for a sentence that would contradict
  fail-closed-by-default (e.g., "an unlisted action is permitted unless explicitly denied"). Found
  none. Every document that states the rule (`SECURITY_POLICY.md` §10, `APPROVAL_POLICY.md` §1/§9,
  `AUTONOMY_POLICY.md`, `DATA_RETENTION_POLICY.md` §2.10) restates it in the same direction —
  absence of a grant is a prohibition.
- `D-044` (`APPROVED`, Project Owner authority) separately records this exact rule in the decision
  register.

### 2.3 Least privilege documented — **MET**, `RUNTIME_AGENT` specifically checked

`AGENT_PERMISSION_MATRIX.md` is generated (never hand-edited, `D-042`) directly from the registry
by `tools/render_permission_matrix.py`; `--check` confirms zero drift. I checked every role's
table by hand:

- `PROJECT_OWNER`: 9 rows, every one `OWNER_ONLY` or `DENY` — consistent with sole-approver status
  and the human-checkpoint list in `user-guide/USER_INSTRUCTIONS.md`.
- `PHASE_OWNER` / `SPECIALIST`: `ALLOW` only on low-risk build-time actions (read repo, read-only
  local commands, write assigned files, write scratch, escalate, draft non-publishing/non-sending
  artifacts). `PHASE_OWNER` additionally holds `ACT-C01` (push/pull, `ALLOW_LOGGED`) and
  `ACT-G02`/`ACT-G04` (demote/self-assess, both disclosure-carrying) — narrowing-direction grants,
  not broadening ones.
- `INDEPENDENT_REVIEWER` / `GOVERNANCE_AUDITOR`: the narrowest tables — read-own-scope, escalate,
  and `DENY` on everything else, including approving anything (`ACT-A01`/`ACT-A03`). Correct for
  roles whose function is independence.
- **`RUNTIME_AGENT`, the composition check I was specifically asked to verify.** I enumerated every
  row under `RUNTIME_AGENT` in the matrix (34 rows in the current registry). Every one resolves to
  `DENY` or `BLOCKED` **except two**: `ACT-G02` (demote/emergency-stop — `ALLOW`) and `ACT-E01`
  (escalate — `ALLOW`). Both are structurally safe: demotion is narrowing (any distance, any time,
  no approval) and escalation is designed to never be gated. No `RUNTIME_AGENT` row grants
  `ALLOW`/`ALLOW_LOGGED`/`APPROVAL_REQUIRED` on reading personal data, sending, spending,
  publishing, or executing untrusted content — all `DENY`.
- **Composition of the two axes (`D-048`), verified rather than assumed:** `AUTONOMY_POLICY.md` §6
  states explicitly that a capability's registry use-disposition (`PERMITTED`/`RESTRICTED`/
  `PROHIBITED`/`UNRESOLVED`, axis 3 of `CAPABILITY_REGISTRY.md`) and a role's matrix grant
  (`action_registry.json`) are different questions that must **both** clear, in order — disposition
  first (eligibility), then the matrix (which role, which action). I checked this is not merely
  asserted but actually built that way: `AGENT_PERMISSION_MATRIX.md`'s `RUNTIME_AGENT` grants
  reference registry-level facts (`ACT-C12`'s note ties `BLOCKED` to `Q-012`'s connector-auth
  `UNRESOLVED` state; `ACT-R09`'s note names `CAPABILITY_REGISTRY.md` rows `C-009`/`C-045`
  directly) rather than restating or overriding the registry's own disposition. I found no row
  where a matrix grant is more permissive than the registry disposition it depends on, and no row
  that double-counts (i.e., treats a `PERMITTED` registry disposition as itself sufficient for a
  role to act — every such case still routes through its own `ACT-*` row).

No over-broad grant found anywhere in the matrix.

### 2.4 State transitions defined — **MET**

Both state machines are fully specified in `action_registry.json → state_machines` (`initial`,
`states`, `terminal`, `transitions` each with `from`/`to`/`actor`/`trigger`, and an `invariants`
array). I hand-verified the five approval invariants against the transition table directly,
rather than trusting `V-9`'s summary:

1. *Only `PENDING_APPROVAL → APPROVED`, only `PROJECT_OWNER`.* Scanned all 12 approval
   transitions: exactly one edge targets `APPROVED` (`from: PENDING_APPROVAL`,
   `actor: PROJECT_OWNER`, `trigger: owner_approves`). No other edge, from any state, targets
   `APPROVED`. **Holds.**
2. *Silence never produces `APPROVED`; a staleness timer produces only `EXPIRED`.* The only
   `staleness_timer`-triggered edge is `PENDING_APPROVAL → EXPIRED`. No timer-triggered edge in
   either state machine targets `APPROVED` or a promotion. **Holds.**
3. *Digest binding.* Not a graph-representable property (digests are not nodes) — it is a semantic
   commitment backed by the real `APPROVED → VOIDED` edge on `artifact_digest_mismatch`, which
   exists in the table. This is an honest limit of what a state-machine checker can verify
   mechanically, not a design gap; `APPROVAL_POLICY.md` §3 states the reasoning in prose and no
   document contradicts it.
4. *Single-use; `EXECUTED` terminal.* `EXECUTED` is in the `terminal` list; I confirmed by scanning
   all 12 transitions that none has `from: "EXECUTED"`. **Holds.**
5. *No self-approval.* A role/authorship rule, not a graph property — `ACT-A03` (`DENY` for every
   agent role approving its own artifact) and, more fundamentally, `ACT-A01` (no agent role holds
   the `APPROVE` transition at all — structural, not artifact-specific). **Holds.**

**Reachability, by hand:** from `DRAFT`, every one of the 10 declared states is reachable
(`DRAFT→PENDING_APPROVAL→{APPROVED→{EXECUTED,EXPIRED,VOIDED,SUPERSEDED}, REJECTED,
CHANGES_REQUESTED→DRAFT, EXPIRED, WITHDRAWN}`, plus `DRAFT→WITHDRAWN` directly). Matches `V-9`.

**Autonomy ladder, by hand:** every promote-triggered edge connects adjacent stages only (checked
list-index adjacency directly — no skip). Every non-`DISABLED` stage
(`SIMULATION`/`DRAFT_ONLY`/`APPROVAL_REQUIRED`/`LIMITED_AUTONOMY`/`ROUTINE_AUTONOMY`) has its own
direct `demote_or_estop → DISABLED` edge. `ACT-G03` denies stage-skipping to **every** role
including `PROJECT_OWNER` — correctly reasoned, since changing the ladder's shape is an
architecture change (`ACT-W13`), not a promotion.

`PP-1` is honestly reported as `PARTIALLY_SATISFIABLE` (a real registry entry is necessary but not
sufficient — disposition must be `PERMITTED` and `PP-4`'s owner decision recorded), and `PP-5`
(dwell times, incident thresholds) is `UNRESOLVED` with no invented numbers (`D-047`). No
capability has actually left `DISABLED`. Nothing I read overstates this.

### 2.5 Policy conflicts tested — **PARTIALLY MET**

Two distinct checks, per `D-041`'s resolution of `Q-017` — I confirm the design correctly
recognizes both are required (this is a completeness question, squarely mine; I did not perform
the prose half myself, per my brief):

**(a) Structural/registry-internal — genuinely tested, and well.** `V-5` groups every action by
`(role, verb, resource, description)` and fails on a contradictory duplicate; its negative control
(a duplicated row with a flipped outcome) confirms it fires. `V-7`/`V-8` similarly catch an
invented basis ID and a dangling policy-file reference. These are real, negative-control-verified,
not decorative. **This half is MET.**

**(b) Prose-level, cross-document — correctly assigned, but not demonstrated against the real
documents as of this audit.** `D-041`, `APPROVAL_POLICY.md` §8, and `policy/action_registry.json`'s
`escalation_codes.ESC-009` all correctly state that this half is a natural-language judgment
assigned to the Independent Reviewer, recorded in `REVIEW_REPORT.md`, and that the mechanical
checker's cross-reference is a starting point, not a substitute. **The design does not silently
skip this half — it is explicitly named as the Reviewer's job, not mine, and I have not performed
it here beyond incidental observations below.** However: as §0 above documents, the
`REVIEW_REPORT.md` currently on disk is a review of the discarded first attempt's documents, not
the real current eight deliverables — so as of this audit, **no evidence exists that the prose
cross-read has actually been run against the documents that will go into the gate report.** This
is the reason for the "partially met" rating: the mechanical half is real and rigorous; the
person-performed half is correctly designed into the process but not yet demonstrated to have
occurred against the real artifacts.

In the course of my own read (not a substitute for the Reviewer's itemized cross-read, but worth
recording since I noticed it), I found one minor prose imprecision — see §5.

**Verdict:** structural testing MET; prose testing correctly assigned to the Independent Reviewer
but its evidentiary record is currently stale/inapplicable. Overall: **PARTIALLY MET**, closeable
by confirming a fresh `REVIEW_REPORT.md` exists against the real documents before the gate report.

---

## 3. Independent rubric scores

Scored against `PROMPT_AND_BUILD_QUALITY_RUBRIC.md`'s 12 categories, 0–5, applying `D-028`'s
elevated bar (Permissions / Testing / Failure handling ≥ 4; Security satisfied by Permissions).

| Category | Score | Justification |
|---|---|---|
| Objective clarity | 5 | Single measurable outcome, stated in the phase prompt and restated verbatim in `task_plan.md`. |
| Inputs | 5 | Every input classified `CONFIRMED`/`INFERRED`/`UNRESOLVED`/`BLOCKED` with citation in `task_plan.md`'s Input classification table before drafting began. |
| Outputs | 5 | Eight named deliverables, a machine-readable schema (`action_registry.json`), explicit paths, pass conditions mapped to specific mechanical checks in the Validation plan. |
| Agent separation | 5 | One phase owner, four genuinely independent specialists (made independent by fixing shared vocabulary first, the explicit `F-00-07` fix), a Governance Auditor and Independent Reviewer both structurally barred from reviewing their own work. |
| Tool realism | 5 | All four tools (`policy_check.py`, `policy_check_selftest.py`, `render_permission_matrix.py`, `blast_radius_check.py`) are real, executable, confirmed by me actually running them. |
| Permissions (≥4) | 5 | Least-privilege matrix generated deterministically from one source of truth; fail-closed default behaviorally tested; `RUNTIME_AGENT` checked by hand against both axes (§2.3), no over-broad grant found. |
| Determinism | 5 | Architecture Rule 3 honored: registry is single source of truth, matrix is generated not authored, every transition/outcome is JSON. |
| Failure handling (≥4) | 4 | Every policy document has a dedicated failure-handling section (approval expiry, digest mismatch, double-claim, partial publish/send, queue aging) with a consistent halt-and-escalate posture. Not 5: none of this is exercised against a real failure yet, and the documents themselves say so. |
| Testing | 4 | 13/13 mechanical checks + 12/12 negative controls, all independently re-run by me with real output. Not 5: the gap in §2.5(b) — no mechanical or (currently) demonstrated person-run check of prose-vs-registry consistency for the real documents — is a genuine, non-trivial hole in what "tested" currently covers. |
| Auditability | 4 | Run ID on every artifact, four structured handoffs, `DECISIONS.md` rows `D-041`–`D-048` each with rationale and evidence, `findings.md` `F-03-01`/`F-03-02` naming the phase's own history precisely. Not 5: the undisclosed stale-file contamination in `agent_runs/phase-03/` (§0) is itself an auditability defect — a reader trusting the directory's contents without independently checking dates/run-IDs would be misled. |
| User usability | 4 | Documents are long (250–585 lines each) for a solo operator with a low review budget, though each uses worked examples, tables, and plain-language edge-case tests (e.g. `PUBLISHING_POLICY.md` §1). Usable, not maximally economical. |
| Portability | 4 | The registry schema (enums, roles, actions, state machines) is a clean, reusable JSON shape; the ID scheme (`D-`, `Q-`, `GC-`, `ACT-`) is appropriately bespoke to this repository, capping portability at "some adapters" rather than full provider isolation. |

**Average: 54/12 = 4.5.** No category below 3. All three elevated-bar categories (Permissions 5,
Testing 4, Failure handling 4) meet the `D-028` floor of 4. Rubric threshold satisfied.

---

## 4. File-ownership result

Cross-referenced `git status` against `task_plan.md`'s File ownership table.

**Clean:** every untracked new file (`SECURITY_POLICY.md`, `APPROVAL_POLICY.md`,
`AUTONOMY_POLICY.md`, `BUDGET_POLICY.md`, `DATA_RETENTION_POLICY.md`, `PUBLISHING_POLICY.md`,
`MESSAGING_POLICY.md`, `AGENT_PERMISSION_MATRIX.md`, `policy/`, `tools/render_permission_matrix.py`,
`tools/policy_check.py`, `tools/policy_check_selftest.py`, `tools/blast_radius_check.py`,
`agent_runs/phase-03/`) matches its assigned owner in the table exactly. Modified files
(`CURRENT_PHASE.md`, `DECISIONS.md`, `MASTER_PLAN.md`, `RISK_REGISTER.md`, `findings.md`,
`task_plan.md`) are all listed as "Phase 03 Owner only" — consistent.

**One minor gap:** `tools/README.md` was modified this phase (it now documents
`render_permission_matrix.py`, `policy_check.py`, `policy_check_selftest.py`, and
`blast_radius_check.py`) but is not explicitly listed in `task_plan.md`'s ownership table. This is
a defensible extension of the Phase 03 Owner's existing ownership of the sibling scripts in that
directory, and the content itself (read in full) is accurate and appropriately scoped — I do not
treat this as a boundary violation, only as a small disclosure gap parallel in shape (though far
lower severity) to the `agent_runs/phase-03/` gap in §0.

**Separately, `OPEN_QUESTIONS.md` was not modified this phase, despite `Q-017` being recorded as
resolved by `D-041`.** `Q-017`'s own row (§268–277) and the summary table (line 301) both still
read `UNRESOLVED`. `OPEN_QUESTIONS.md` is listed in `task_plan.md`'s ownership table as a
Phase-03-Owner-only file, so this was available to update. This is not a permissions violation —
Q-017 was designed to be closed by a Phase 03 Owner decision "recorded" rather than requiring a
project-owner-facing status flip — but leaving the question's own status field at `UNRESOLVED`
while `DECISIONS.md` and `task_plan.md` both assert it "resolved" is an internal inconsistency a
future reader of `OPEN_QUESTIONS.md` alone would not catch. Worth noting: `tools/blast_radius_check.py`'s
negation-pattern matching (which looks for phrases like "does not exist," "never executed") would
not catch this class of staleness at all, since "UNRESOLVED" is not a negation phrase in its
pattern list — this is a real blind spot in `CSK-01`'s current pattern set, not a defect in how it
was run.

No other file-ownership issue found. No specialist wrote a file outside its assignment; no
specialist wrote to a register.

---

## 5. Prose-level observations (not my primary job, noted because they jumped out)

**`APPROVAL_POLICY.md` §6** states, of claims/testimonials/pricing/discounts/direct-outreach/
complaints/paid-advertising: "...in the registry these resolve to `APPROVAL_REQUIRED`... not
`OWNER_ONLY`." This is imprecise as a description of the registry's **current** state — the actual
governing rows (`ACT-P05`, `ACT-S01`, `ACT-M03`) all resolve to `DENY` today, because no
publishing/messaging/spending capability exists (`D-010`). `PUBLISHING_POLICY.md` §2 and
`MESSAGING_POLICY.md` §2, covering the same categories, are careful to say "DENY today, becomes
`APPROVAL_REQUIRED` once built" — `APPROVAL_POLICY.md` §6 states the same eventual/conceptual shape
without that qualifier. Not safety-relevant (a reader acting on the imprecise reading would still
be stopped by the real `DENY` rows), and the Policy Designer's own handoff flags this exact section
as its one genuine interpretive judgment call. Recorded as a minor, non-blocking finding for the
Independent Reviewer's formal cross-read to confirm or dispose of.

No other prose-vs-registry or prose-vs-sibling-document contradiction jumped out during this read,
but I did not perform the exhaustive itemized cross-read `D-041` assigns to the Independent
Reviewer — see §2.5(b).

---

## 6. Overall conclusion

**Phase 03's actual policy work — the eight deliverables, the registry, and the tooling — is
substantively strong and satisfies four of its five stated pass conditions cleanly, with the fifth
partially met for a specific, nameable reason.**

1. All high-risk actions require approval — **MET.**
2. Default is fail-closed — **MET**, behaviorally tested.
3. Least privilege documented — **MET**, `RUNTIME_AGENT` and the two-axis composition (`D-048`)
   specifically checked and clean.
4. State transitions defined — **MET**, all five approval invariants and both state machines
   hand-verified against the transition table, not just trusted from `V-9`.
5. Policy conflicts tested — **PARTIALLY MET.** The structural half is real, rigorous, and
   negative-control-verified. The prose half is correctly designed into the process (assigned to
   the Independent Reviewer, per `D-041`) but its recorded evidence (`REVIEW_REPORT.md`) is, as of
   this audit, a review of the discarded first attempt's documents — not the real current eight
   deliverables — so this half is not yet demonstrated against what will actually go into the gate
   report.

**What must be fixed or explicitly accepted before the gate report:**

1. **(Blocking to certifying condition 5)** Confirm a fresh Independent Review of the real, current
   eight deliverables exists, or explicitly disclose in `findings.md` that `REVIEW_REPORT.md` is
   stale/inapplicable and that the prose cross-read is outstanding.
2. **(Should-fix, low cost)** Correct `APPROVAL_POLICY.md` §6's present-tense claim (§5 above) to
   match `PUBLISHING_POLICY.md`/`MESSAGING_POLICY.md`'s already-correct "DENY today, becomes
   `APPROVAL_REQUIRED` when built" phrasing.
3. **(Should-fix, low cost)** Update `OPEN_QUESTIONS.md`'s `Q-017` row and summary-table status to
   reflect `D-041`'s resolution, so the question register does not silently disagree with the
   decision register.
4. **(Should-fix, trivial)** `tools/render_permission_matrix.py` hardcodes the header string
   `Run ID: phase-03-2026-07-30-a` (line 61) rather than reading it from `action_registry.json`'s
   own `run_id` field (which correctly says `-b`). `V-12`'s drift check does not catch this because
   it strips the `Generated:` line before comparing. Cosmetic — it does not affect any permission
   outcome — but it is exactly the kind of provenance mislabeling this entire phase exists to guard
   against, and it is a one-line fix.
5. **(Disclosure, not a fix)** Note in `findings.md` that `agent_runs/phase-03/GOVERNANCE_AUDIT_REPORT.md`
   and `agent_runs/phase-03/REVIEW_REPORT.md` were found pre-populated with discarded-attempt
   content, mirroring — but not previously disclosed alongside — the contamination `F-03-01`
   already documents for the root-level policy drafts.

None of these rises to a defect in the underlying permission design itself: the registry, the
policies' substance, the generated matrix, and the mechanical tooling are all genuinely rigorous,
and I found no invented fact, no secret, no over-broad grant, and no RDBC-boundary issue anywhere
in the real Phase 03 output. The gap is specifically in **evidence of the person-performed half of
"policy conflicts tested"** and in **disclosure hygiene around leftover files from the discarded
first attempt** — both closeable before the gate report without touching the substance of any
policy.
