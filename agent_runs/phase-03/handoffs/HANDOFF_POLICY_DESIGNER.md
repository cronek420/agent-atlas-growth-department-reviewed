# Agent Handoff

- Run ID: `phase-03-2026-07-30-b`
- Phase: 03 — Governance, Security, Approval, and Autonomy Policies
- Agent: Policy Designer
- Assignment: Author `APPROVAL_POLICY.md`, `AUTONOMY_POLICY.md`, `BUDGET_POLICY.md`, in that order, per `task_plan.md` and the Policy Designer brief.
- Files owned: `APPROVAL_POLICY.md`, `AUTONOMY_POLICY.md`, `BUDGET_POLICY.md`, this handoff.

## Facts and evidence

Read, in full, before drafting: `CLAUDE.md`; `policy/POLICY_CONTRACT.md`;
`policy/action_registry.json`; `docs/PROJECT_BOUNDARIES.md` (all sections, §4
closely); `DECISIONS.md` in full, especially the Phase 03 section `D-041`–`D-048`
and the real Phase 02 section `D-036`–`D-040`; `INTAKE_RECORD.md` (second and
third intake rounds); `OPEN_QUESTIONS.md` in full, including the six Phase-02
questions `Q-012`–`Q-017`; `CAPABILITY_REGISTRY.md` §"Vocabularies" and §H
(recommended target stages); `RISK_REGISTER.md` `R-01`, `R-02`, `R-03`, `R-08`,
`R-11`, and the Capability-Surface category `R-20`–`R-24`; `NON_GOALS.md`;
`findings.md` in full (Phase 03's `F-03-01` and Phase 02's `F-02-01`–`F-02-14`,
plus Phase 00/01's `F-00-05`, `F-00-06`, `F-00-07`, `F-00-09`, `F-01-01`,
`F-01-04`, `F-01-08`, `F-01-09`); `user-guide/USER_INSTRUCTIONS.md` "Human
checkpoints"; `task_plan.md`; `CURRENT_PHASE.md`; `templates/AGENT_HANDOFF_TEMPLATE.md`.

**A discovery that shaped this entire assignment, disclosed up front because
it changes how everything else in this handoff should be read.** Before
drafting anything, an `ls`-equivalent check on my three target files and this
handoff's directory showed all four **already existed on disk, uncommitted**
(`git status --short` confirmed them as untracked, alongside
`SECURITY_POLICY.md`, `DATA_RETENTION_POLICY.md`, `PUBLISHING_POLICY.md`,
`MESSAGING_POLICY.md`, `policy/`, and `tools/`). Reading them showed their
header line: `run_id: phase-03-2026-07-30-a` — **the first, discarded Phase 03
attempt** described in `findings.md` `F-03-01` and `task_plan.md` § "Why `-b`".
`git reset --hard origin/main` (used to reset this branch to the real merged
`main` per the Project Owner's resolution) does not delete untracked files, so
the discarded attempt's uncommitted drafts survived the reset on disk even
though the branch history does not contain them.

I verified this rather than assuming it: the old `APPROVAL_POLICY.md` cited
`D-038` for the `OWNER_ONLY`/`APPROVAL_REQUIRED` split, but the real
`DECISIONS.md` assigns `D-038` to the `NOT_PRODUCTION_FACING` ladder sentinel
— a completely different topic. The real decision for the split is `D-043`.
Similarly, the old `AUTONOMY_POLICY.md` asserted `PP-1` was `BLOCKED` because
"`CAPABILITY_REGISTRY.md` does not exist" — false today; it exists with 141
rows. The old `BUDGET_POLICY.md` cited `D-042` for "every numeric value is
unassigned" — the real `D-042` is about `AGENT_PERMISSION_MATRIX.md`
generation; the real numeric-invention decision is `D-047`. None of the old
three files mentioned `Q-012`–`Q-017`, `D-045`–`D-048`, `R-24`, `ESC-011`, or
the Q-017/`D-041` resolution — because none of that existed when attempt `-a`
was written. **I treated all three existing files, and the existing handoff,
as unreliable and rewrote all four from scratch against the real register**,
rather than editing them, since the errors were load-bearing premises, not
surface typos. This is disclosed here in addition to being disclosed at the
top of each rewritten file, per the general principle that a specialist's own
process defect belongs in the handoff even when the specialist catches and
fixes it before submitting.

Every claim in the three deliverables carries a basis ID or exact document
reference. I ran a mechanical check of my own — extracted every
`D-`/`Q-`/`R-`/`NG-`/`F-` pattern from all three files with a regex and
confirmed each resolves against the real register (see "Tests run"). This
follows `F-00-04` (mechanical verification is cheap and should run before
trusting prose) even though I do not own `tools/policy_check.py` — I
substituted a manual grep pass since the real checker is a Phase Owner
deliverable (T3 in `task_plan.md`), not mine, and I did not want to submit
uninspected citations.

## Assumptions

Per `F-00-05` — a clean "no assumptions" report from a Phase 00 specialist
carried no evidentiary weight and turned out to be false in all three cases —
I am treating this section as adversarial against myself, not a formality.

1. **The `OWNER_ONLY` vs `APPROVAL_REQUIRED` mapping in `APPROVAL_POLICY.md`
   §6.** I mapped "product claims," "testimonials," "pricing and discounts,"
   "direct outreach," and "responses to complaints" — which appear on the
   `user-guide/USER_INSTRUCTIONS.md` human-checkpoint list — onto the
   permission-outcome `APPROVAL_REQUIRED` **by design intent**, while noting
   that every one of them resolves to `DENY` **today** because no production
   capability exists to execute them (`D-036`). This is a genuine synthesis of
   `D-043` and the fail-closed default (`D-044`), not a verbatim registry
   statement or an owner quote. Labeled `PROPOSED` in the document and flagged
   here again. If the Phase Owner disagrees, this is the highest-value place
   to push back before integration.
2. **`AUTONOMY_POLICY.md` §1's per-stage operational definitions.** The brief
   explicitly asked me to define what each ladder stage means because no
   source document does. Built to be internally consistent with `D-010`, the
   fail-closed default, and `D-020` (gates never relax by ladder stage) — new
   prose, not restated fact, labeled `PROPOSED` throughout §1.
3. **`AUTONOMY_POLICY.md` §3's list of automatic-demotion triggers.** The
   registry establishes that demotion edges exist and are ungated; it does
   not enumerate trigger conditions. Built from `PP-3` and the `ESC-` codes
   and labeled `PROPOSED` explicitly rather than presented as registry
   content.
4. **`AUTONOMY_POLICY.md` §2's precise reading of `PP-1` as
   `PARTIALLY_SATISFIABLE`.** The registry's own note says a registry entry
   existing is "necessary but not sufficient" and names disposition
   `PERMITTED` plus an owner promotion decision as the remaining conditions.
   I stated this as three conjunctive sub-conditions and was careful to write
   "no capability has actually been promoted" rather than implying the
   registry's existence unlocks anything — this is the exact "do not claim
   more is unlocked than actually is" instruction in the brief, and I want it
   checked specifically, since it is easy to overstate in either direction
   (either "still blocked" — wrong, it isn't fully blocked anymore — or
   "now unlocked" — also wrong).
5. **I did not invent any numeric value.** Every place a number would
   normally appear (approval staleness windows, autonomy dwell times,
   incident thresholds, spend caps) is either omitted or explicitly marked
   `[UNRESOLVED — owner to set]`. I re-scanned all three files with a regex
   for dollar signs, day/hour counts, and percentages after drafting; the one
   match (`APPROVAL_POLICY.md` §1, GC-01) is an illustrative example of what
   counts as a marketing *claim* ("we finish projects in 6 weeks," "99% of
   clients recommend us"), in quotation marks, presented as a hypothetical
   external-facing statement to classify — not an asserted fact about Rough
   Draft Builders Club or an invented policy threshold. I judged this
   acceptable because the category definition needs a concrete example to be
   usable by an operator in under a minute, and flag it here so the Phase
   Owner can independently judge whether even an illustrative numeric example
   reads as too close to the invention line.
6. **I did not read `SECURITY_POLICY.md`, `DATA_RETENTION_POLICY.md`,
   `PUBLISHING_POLICY.md`, or `MESSAGING_POLICY.md`**, even though all four
   already exist on disk (confirmed via directory listing, all four
   presumably from the same discarded `-a` attempt, though I did not open any
   of them to check their `run_id`). The brief said not to read sibling
   in-progress or finished output beyond the READ FIRST list, and I held to
   that even knowing these particular files might also be stale — my
   cross-references to security/data/publishing/messaging concepts (e.g.,
   "subject to `SECURITY_POLICY.md`" in `AUTONOMY_POLICY.md` §1, and the
   `ESC-011` cross-reference in `APPROVAL_POLICY.md` §9) are forward
   references to what those files are supposed to cover per `task_plan.md`'s
   file-ownership table and the real registry's own notes, not claims about
   their actual current content.
7. **I assumed `Q-010a` is a citable identifier** even though it lives inside
   `INTAKE_RECORD.md` rather than as a row in `DECISIONS.md` or
   `OPEN_QUESTIONS.md`. Precedent: `DECISIONS.md` row `D-020` itself cites
   "`INTAKE_RECORD.md` 'Second intake round' Q-010a" in its Basis column, so
   this is consistent with existing project practice, not a new citation
   style I introduced.
8. **I did not narrate the discarded-attempt incident inside the policy
   documents themselves beyond a short provenance note at the top of each.**
   The brief for `ACT-C02b` specifically said "do not narrate the incident
   itself; that belongs in the gate report" — I read that instruction as
   applying most directly to the PR-merge precedent, but applied the same
   restraint to the stale-file discovery: each policy file's provenance note
   states what was wrong and why the file was rewritten, in two or three
   sentences, and defers the full account to this handoff and `findings.md`
   `F-03-01`, rather than re-telling the whole story in each of three
   documents.

## Open questions

1. **`Q-008` (owner unavailability)** — `APPROVAL_POLICY.md` §7 states the
   interim `D-045` rule and the exact three-option owner action required. No
   new question raised; restated for the Phase Owner's gate-report visibility.
2. **`Q-003` / `D-047`** — every numeric value in all three files is blank.
   The Phase Owner should confirm this reads as "structurally complete, values
   pending" rather than "incomplete," when scoring against the rubric.
3. **My `PROPOSED` reading in `APPROVAL_POLICY.md` §6** (Assumption 1 above)
   is the one place I'd most want independent-reviewer or Governance-Auditor
   scrutiny — it resolves a real ambiguity between two source lists
   (`README.md` vs `user-guide/USER_INSTRUCTIONS.md`) that neither list
   resolves on its own, and I want to be told if I resolved it wrong rather
   than have it pass through unchallenged.
4. **Should `BUDGET_POLICY.md` §5's spend-category table be considered a
   Phase 03 deliverable structure, or does it overreach into Phase 22's
   scope** (which owns budget-scaling design)? I read the brief's item 5
   ("blank-values skeleton for a future authorized budget") as authorizing
   exactly this skeleton, with every value blank, distinct from actually
   designing Phase 22's guardrails — flagging since Phase 22 is the file's
   most obvious future collision point.
5. **Should the stale `-a`-attempt files that are not mine to own
   (`SECURITY_POLICY.md`, `DATA_RETENTION_POLICY.md`, `PUBLISHING_POLICY.md`,
   `MESSAGING_POLICY.md`, `policy/`, `tools/`) be independently checked for
   the same run-ID/stale-citation problem before this phase's gate report is
   drafted?** I did not open them (Assumption 6), so I cannot say whether they
   carry the same defect, only that the same mechanical cause (untracked
   files surviving a `git reset --hard`) could equally affect them. This is
   the single most important thing for the Phase Owner to check before
   trusting any sibling specialist's output at integration time — recommend
   checking each file's own header/run-id line and its citations against the
   real register before assuming any of them is the `-b` version.

## Work completed

- `APPROVAL_POLICY.md`: nine gated categories with concrete definitions,
  examples, and counterexamples (§1), including an explicit statement that
  most of these categories resolve to `DENY` today rather than
  `APPROVAL_REQUIRED`, because the execution capability itself doesn't exist
  yet; the approval state machine reproduced exactly from the contract with a
  transitions table (§2); the five invariants each with a "why" (§3); the
  request-packet requirement (§4); batching rules (§5) stating what batching
  may/may not do, with the per-digest binding requirement stated explicitly;
  the `OWNER_ONLY` vs `APPROVAL_REQUIRED` distinction (`D-043`) with the full
  human-checkpoint mapping table, including rows with no dedicated registry
  entry yet (§6); owner-unavailability section stating `D-045`'s interim rule
  and the owner's three options verbatim from `Q-008` (§7); a new section
  stating in plain terms what "policy conflicts tested" requires under
  `D-041`/`Q-017` — the structural check plus the prose cross-read, both
  required (§8); escalation codes table including the new `ESC-011`,
  cross-referenced to (not restating) `SECURITY_POLICY.md` (§9); gate-decision
  ownership with the real Phase 02 CONDITIONAL PASS cited as a worked example
  of "recommends, does not decide," and the `ACT-C02b` PR-merge precedent
  cited as a "prepare, never execute" example without narrating the incident
  (§10); failure-handling table covering expiry, digest mismatch, double-claim,
  queue aging, rejection, and withdrawal (§11).
- `AUTONOMY_POLICY.md`: operational definitions for all six ladder stages
  (§1) — the main original contribution the brief asked for; promotion
  preconditions `PP-1`–`PP-5` (§2) with `PP-1` corrected to
  `PARTIALLY_SATISFIABLE` (registry now exists; entry + `PERMITTED`
  disposition + recorded owner decision all required, stated as three
  conjunctive conditions) and `PP-5` stated as `UNRESOLVED` (`D-047`);
  demotion/emergency-stop section (§3) stating the any-distance/any-time/
  no-approval/deterministic-code properties and the one-hop-to-`DISABLED`
  guarantee; current-state statement (§4); the `APPROVAL_REQUIRED`-collision
  disambiguation (§5); a new §6 on composition with `CAPABILITY_REGISTRY.md`'s
  three axes (`D-048`) — disposition answers "usable at all," the ladder
  answers "how much autonomy," both must clear, and the `NOT_PRODUCTION_FACING`
  sentinel sits outside the ladder entirely.
- `BUDGET_POLICY.md`: "authorized budget is zero, not low" (§1); an expansive
  "what counts as spending" section (§2) now citing the two real worked
  precedents the brief specifically required — `F-02-12` (Phase 02's review
  hit a spend limit and correctly refused to raise it) and `Q-014`
  (unresolved, urgent per the Phase 02 Owner, who scheduler ownership does not
  by itself authorize spend on); organic-only duration nuance (§3) keeping
  `D-016` `CONFIRMED` and `D-016a`'s indefinite reading `INFERRED` without
  collapsing either direction; what agents may/may not do (§4); the
  blank-values budget skeleton with every cap `[UNRESOLVED — owner to set]`
  per `D-047` (§5); detection/escalation procedure for `ESC-007` (§6).
- Cross-checked every basis identifier across all three files against the
  real registers (see "Tests run").

## Files changed

- `C:\Users\crone\Projects\agent-atlas-growth-department\.claude\worktrees\new-session-da0ad3\APPROVAL_POLICY.md` (rewritten in full — pre-existing content was the discarded `-a` attempt, see "Facts and evidence")
- `C:\Users\crone\Projects\agent-atlas-growth-department\.claude\worktrees\new-session-da0ad3\AUTONOMY_POLICY.md` (rewritten in full, same reason)
- `C:\Users\crone\Projects\agent-atlas-growth-department\.claude\worktrees\new-session-da0ad3\BUDGET_POLICY.md` (rewritten in full, same reason)
- `C:\Users\crone\Projects\agent-atlas-growth-department\.claude\worktrees\new-session-da0ad3\agent_runs\phase-03\handoffs\HANDOFF_POLICY_DESIGNER.md` (rewritten in full, same reason)

No other file was written or edited. I did not touch `DECISIONS.md`,
`findings.md`, `progress.md`, `RISK_REGISTER.md`, `OPEN_QUESTIONS.md`,
`CURRENT_PHASE.md`, `task_plan.md`, `SECURITY_POLICY.md`,
`DATA_RETENTION_POLICY.md`, `PUBLISHING_POLICY.md`, `MESSAGING_POLICY.md`,
`policy/`, `tools/`, or any harness config, per the brief's explicit scope
restriction and `F-00-09`.

## Tests run

1. **Pre-existing-file discovery (`Bash`).** `ls -la` on my four target paths
   before drafting, showing all four already present with timestamps
   predating this session. Followed by `git status --short` and `git log
   --oneline -5`, confirming all four were untracked (`??`) against a clean
   `main` at `acabca8` (the real merged Phase 02). This is what surfaced the
   stale-attempt problem before any content was trusted.
2. **Citation resolution check (manual, mechanical).** Ran, via the Bash
   tool, a regex extraction of every `D-nnn`, `Q-nnn`, `R-nn`, `NG-nnn`, and
   `F-nn-nn`-shaped token across all three rewritten files:
   `grep -oE '\b(D|Q|R|NG|F)-[0-9]+[a-z]?(-[0-9]+)?\b' <file> | sort -u`.
   **Result — every token resolved against a real register entry:**
   `APPROVAL_POLICY.md`: `D-006, D-007, D-011, D-016, D-019, D-019a, D-020,
   D-028, D-036, D-038, D-040, D-041, D-042, D-043, D-044, D-045, D-047,
   D-048, F-00-05, F-02-03, F-02-05, F-02-11, F-03-01, NG-001, Q-003, Q-008,
   Q-010a, Q-012, Q-015, Q-017, R-01, R-02, R-20, R-21, R-24`.
   `AUTONOMY_POLICY.md`: `D-010, D-011, D-020, D-021, D-037, D-038, D-039,
   D-043, D-044, D-047, D-048, NG-004, Q-003, Q-013`.
   `BUDGET_POLICY.md`: `D-008, D-011, D-016, D-016a, D-019a, D-020, D-021,
   D-027, D-042, D-044, D-046, D-047, F-01-02, F-02-08, F-02-12, NG-001,
   NG-004, Q-014, R-11, R-13`.
   I then separately re-grepped every occurrence of `D-038`, `D-040`, and
   `D-042` (the three IDs the discarded attempt had miscited) with
   `-C 1` context to confirm each appears **only** inside a provenance note
   describing the old attempt's error, or — for `D-038` in
   `AUTONOMY_POLICY.md` — as a correct, standalone citation of the real
   `NOT_PRODUCTION_FACING` sentinel decision. No remaining false-basis usage
   found.
3. **No-numeric-invention scan (`Bash` regex).**
   `grep -nE '\$[0-9]|[0-9]+ days?\b|[0-9]+ hours?\b|[0-9]%' *.md` across all
   three files. One match: `APPROVAL_POLICY.md` §1 GC-01's illustrative claim
   examples ("6 weeks," "99%"), addressed in Assumption 5 above. No other
   digit-bearing threshold, cap, or window appears anywhere in the three
   files; every place a number belongs is `[UNRESOLVED — owner to set]` or
   omitted.
4. **What I did not run:** `tools/policy_check.py` and
   `tools/render_permission_matrix.py` — these are Phase Owner deliverables
   (T2/T3 in `task_plan.md`), not assigned to me. A `tools/policy_check.py`
   file exists on disk (from the same stale attempt, unopened by me per
   Assumption 6), but running someone else's not-yet-verified script against
   my own output would not constitute the deterministic verification `D-003`
   calls for until the Phase Owner has confirmed which version of it, if any,
   is the real `-b` one. I am not claiming the deterministic checker has run
   against my output — that is the Phase Owner's step, and my citation check
   above is a manual substitute for my own confidence, not a replacement for
   it.

## Failures or risks

- **The stale-attempt discovery is the most important thing in this handoff.**
  If the same failure mode (untracked files from attempt `-a` surviving the
  `git reset --hard`) affected the other four specialists' files
  (`SECURITY_POLICY.md`, `DATA_RETENTION_POLICY.md`, `PUBLISHING_POLICY.md`,
  `MESSAGING_POLICY.md`) or the Phase Owner's own `policy/` and `tools/`
  deliverables, this phase could integrate stale, miscited content without
  anyone noticing — exactly the shape of defect `F-00-05` and `F-02-11`
  describe, except at the scale of whole files rather than individual claims.
  I flagged this in "Open questions" item 5; I consider it more important
  than any single content decision in my own three files.
- **Interpretive risk in `APPROVAL_POLICY.md` §6** (Assumption 1 / Open
  question 3) — this is the one place I made a judgment call the source
  documents don't fully settle. It is `PROPOSED`, not `CONFIRMED`, and stated
  as such in the document, but it deserves independent-reviewer attention
  before it is treated as settled policy.
- **All three documents are policy, not enforcement.** I did not claim any of
  these three files makes anything actually happen mechanically. They
  describe and justify registry rows; the registry and its checker are what
  would actually enforce anything. I classify all three as `PROPOSED` policy
  in their own headers.
- No boundary was tested, approached, or crossed during this work. I did not
  access `Rough-Draft-Builders-Club`, did not attempt any external
  connection, and did not touch any file outside my assigned four.

## Recommended next action

Phase Owner: **before proceeding to T2 (render permission matrix) or T3
(mechanical verification), check whether the other four Phase 03 specialist
deliverables and the `policy/`/`tools/` directories are also leftovers from
the discarded `-a` attempt** — check each file's stated `run_id` and spot-check
its citations against the real `D-041`–`D-048`/`Q-012`–`Q-017`/`R-20`–`R-24`.
This is cheap to check and expensive to miss. Then read `APPROVAL_POLICY.md`
§6, §8, §10 and `AUTONOMY_POLICY.md` §2, §6 first — those carry either my own
synthesis or the corrections that most needed the real Phase 02 state to get
right. Then route normally through T2 → T3 → Independent Governance Auditor →
Independent Reviewer per `task_plan.md`, with the prose cross-read in
`APPROVAL_POLICY.md` §8 specifically assigned to the Independent Reviewer, as
`D-041` requires.
