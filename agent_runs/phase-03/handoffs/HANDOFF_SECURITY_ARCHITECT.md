# Agent Handoff

- Run ID: phase-03-2026-07-30-b
- Phase: 03 — Governance, Security, Approval, and Autonomy Policies
- Agent: Security Architect (specialist)
- Assignment: Author `SECURITY_POLICY.md` per `policy/POLICY_CONTRACT.md` and the Phase 03
  Owner's brief — secrets lifecycle, credential lifecycle, exposure incident response,
  credential-free/borrowed-authority access, access control, repository security,
  untrusted-content boundary extended to preloaded content, tool-grant-list honesty,
  fail-closed statement, coverage gaps, honest capability classification.
- Files owned: `SECURITY_POLICY.md`; this handoff
  (`agent_runs/phase-03/handoffs/HANDOFF_SECURITY_ARCHITECT.md`)

## Facts and evidence

Read, in full or by targeted section, before writing: `CLAUDE.md` (all 13 sections, including
§11's Phase-02 extension); `policy/POLICY_CONTRACT.md` (all 11 sections); the full
`policy/action_registry.json` (schema `2.0.0`, all roles, all 60+ action rows, both state
machines); `docs/PROJECT_BOUNDARIES.md` (all 8 sections, including the §2.1 and §3
Phase-02-added narrowings); `DECISIONS.md` Phase 03 section (`D-041`–`D-048` read directly,
all eight rows) and the real Phase 02 section (`D-036`–`D-040` read directly, all five rows,
plus the `D-027`-partially-discharged note); `CAPABILITY_REGISTRY.md` (the "READ THIS BEFORE
USING THE TABLES" section, the full Vocabularies section, §A rows `C-001`–`C-016`, §C.1–C.7
rows `C-030`–`C-054` including `C-009` and `C-045` in full with their `Notes` columns);
`SKILL_SECURITY_POLICY.md` (all 12 sections, in full — including §0's scope boundary, which
this file is built to respect rather than duplicate); `RISK_REGISTER.md` (R-13, R-14, R-19
through R-24 read in full, plus the Phase 01 amendment note at the top); `findings.md`
(`F-03-01`, `F-02-02` through `F-02-05`, `F-01-06`, `F-01-07`, `F-01-01`, `F-01-02`, `F-00-09`
read in full); `README.md` §"Secrets rules" and §"Verified environment"; `.env.example` in
full; `.gitignore` in full; `user-guide/USER_INSTRUCTIONS.md` in full; `task_plan.md` (this
phase's task graph and file-ownership table); `templates/AGENT_HANDOFF_TEMPLATE.md`.

**Discovered before writing anything, and load-bearing for how I proceeded:** `SECURITY_POLICY.md`
and this handoff already existed on disk, both dated `phase-03-2026-07-30-a` — the discarded
first attempt. `git status --short` confirmed both are **untracked** (`??`), which is why they
survived `git reset --hard origin/main`: that command resets tracked files to match the target
commit but does not touch untracked working-tree files. The old `SECURITY_POLICY.md` cited an
invented `D-036`–`D-042` range that collides with the real `D-036`–`D-040` and lacked a
dedicated treatment of §3 (credential-free/borrowed-authority access) — the section
`task_plan.md` and my brief both flag as the one that matters most. It also cited `F-01-01` for
a force-push precedent I had to re-verify independently rather than trust, since the file's
own premise (built on the false "Phase 02 never happened" branch) was already known-unreliable.
**I overwrote both files in full rather than editing the old ones**, since patching a document
built on a discredited premise risks carrying forward citations that happen to still resolve by
coincidence rather than by having been re-verified against the real state.

**Every identifier in the new `SECURITY_POLICY.md` was mechanically re-derived from this
file, not carried over from the old draft**, using a Python regex extraction of every
`D-0\d{2}[a-z]?`, `Q-0\d{2}`, `R-\d{2}`, `NG-00\d`, `F-\d{2}-\d{2}`, `C-0\d{2}`, `ACT-[A-Z]\d{2}[a-z]?`,
and `ESC-0\d{2}` token, then checked each against its source register:

- `D-` ids (`D-003, D-008, D-009, D-013, D-019a, D-026, D-027, D-030, D-032, D-036, D-040,
  D-041, D-042, D-044, D-045, D-046, D-047, D-048`) — `D-013`, `D-026`, `D-032` confirmed by
  direct grep against `DECISIONS.md` (`^\| D-013 \|`, `^\| D-026 \|`, `^\| D-032 \|`, all
  matched); the Phase 02/03 rows (`D-036`–`D-048`) were read directly in this session, not
  grepped.
- `Q-` ids (`Q-003, Q-004, Q-007, Q-008, Q-009, Q-012, Q-014`) — `Q-003`, `Q-012`, `Q-014`
  confirmed by direct grep against `OPEN_QUESTIONS.md` (`^### Q-003`, `^### Q-012`,
  `^### Q-014`, all matched, all status `UNRESOLVED`); the rest were read directly in
  `CLAUDE.md`/`docs/PROJECT_BOUNDARIES.md`.
- `R-` ids (`R-13, R-14, R-19, R-21, R-22, R-23`) — all read directly in full from
  `RISK_REGISTER.md`.
- `NG-003` — read directly in `NON_GOALS.md`.
- `F-` ids (`F-00-09, F-01-01, F-01-02, F-01-07, F-02-02, F-02-03, F-02-04, F-02-05`) — all
  read directly in full from `findings.md`. `F-01-01` specifically re-verified because the old
  draft cited it for a force-push detail (commit `f282b89`, `--force-with-lease`) — confirmed
  that exact commit hash and mechanism are present verbatim in the real finding text, so the
  old draft's citation, though built on a discredited overall premise, was itself accurate on
  this point. I re-derived it from source rather than trusting the old draft's accuracy by
  assumption.
- `C-` ids (`C-009, C-044, C-045, C-052`) — all read directly, in full, including their
  `Notes` columns, from `CAPABILITY_REGISTRY.md`. (The regex also matched `C-002`, `C-004`,
  `C-011` as substrings of `ESC-002`/`ESC-004`/`ESC-011`/`ACT-C02`/`ACT-C12` tokens — verified
  by follow-up grep to be false positives of the extraction pattern, not real citations in the
  document.)
- `ACT-` ids (`ACT-R01`–`R09` incl. `R04b`/`R07b`, `ACT-W01`–`W14`, `ACT-X01`–`X06`,
  `ACT-C01`–`C12` incl. `C02b`, `ACT-D02`, `ACT-A03`/`A04`, `ACT-E01`, `ACT-M05`) — every one
  read directly, in place, in `policy/action_registry.json`'s `actions` array this session.
- `ESC-` ids (`ESC-002, ESC-004, ESC-011`) — all present in
  `policy/action_registry.json.escalation_codes`, read directly.

No ID above `D-048` was used, per `policy/POLICY_CONTRACT.md` §10's instruction not to cite
`D-049` or higher until this phase's own rows create them.

## Assumptions

Stated plainly rather than hidden behind "none," per `F-00-05`'s standing lesson that a clean
assumptions section is itself a signal to investigate harder, not a success to report.

1. **I assumed `tools/policy_check.py` exists or will exist by gate time**, based on
   `policy/action_registry.json`'s own header text and `D-042`'s description, and I saw it
   listed as untracked (`tools/policy_check.py`) in `git status --short` — but I did not read
   or execute it. §12's `SCAFFOLDED` label for the fail-closed default rests on the registry
   file being machine-readable and the checker being *described* as validating against it, not
   on my having run it against this file. If the checker enforces a citation format I did not
   anticipate, §12's label could be too generous.
2. **I assumed the branch-protection gap named in `R-14` is still open as of this writing.**
   I have no GitHub access and did not attempt to verify live repository settings; I relied on
   the register text, which is itself a known-fallible source in this project (`F-01-09`
   records registers going stale). I named the gap as open rather than assuming it was quietly
   closed.
3. **I did not read the four sibling Phase 03 policy documents** (`APPROVAL_POLICY.md`,
   `AUTONOMY_POLICY.md`, `BUDGET_POLICY.md`, `DATA_RETENTION_POLICY.md`, `PUBLISHING_POLICY.md`,
   `MESSAGING_POLICY.md`), per the explicit instruction not to read or cite sibling
   deliverables in progress and `task_plan.md`'s parallel-execution design (T1 runs four
   specialists concurrently, each against the contract and real repo state only). §11 names
   those files by their `policy/action_registry.json`-assigned `policy` field rather than by
   having read their content. If any of them contradicts a claim in this file, I would not
   know — that is the phase owner's integration pass and the Independent Reviewer's
   `Q-017`/`D-041` prose cross-read to catch, not something I can self-verify.
4. **I assumed my reading of `CAPABILITY_REGISTRY.md` rows `C-044` and `C-052` is current**,
   since `D-039` records the registry as a dated snapshot that nothing in this project detects
   drift against. I read the rows directly this session rather than from memory of an earlier
   pass, which is the best available mitigation short of a fresh capture (which is out of my
   assignment and, per `SKILL_SECURITY_POLICY.md` §7.2 trigger T1, belongs to the phase gate,
   not to a single specialist).
5. **What I did to convince myself I had not silently assumed something:** ran the regex
   extraction described above over the finished document and checked every extracted ID
   against its source file by direct grep or by the read already performed this session —
   not against memory of having read it once. I found no citation in the document that traces
   only to my recollection rather than to a file read or grepped in this session.

## Open questions

- The specific branch-protection ruleset shape (required reviews, status checks, force-push
  restriction) is named in §7 as an owner/implementation decision this policy deliberately
  does not prescribe — raising it here rather than inventing a ruleset.
- Rotation-interval and all other numeric blanks (§4, §5) are `UNRESOLVED` per `D-047` and
  depend on the owner answering `Q-003`. No placeholder number was invented anywhere in the
  document; every spot a number would go is described, not filled.
- I did not verify whether `tools/policy_check.py` actually runs cleanly against citations in
  this specific file (see Assumption 1) — recommend the phase owner's mechanical-verification
  pass (T3 in `task_plan.md`) confirm this before the Independent Governance Auditor or
  Independent Reviewer treats §12's `SCAFFOLDED` label for the fail-closed default as settled.
- I flagged, but did not resolve, that the *old* discarded `SECURITY_POLICY.md`'s citation of
  `F-01-01` happened to be accurate despite the file's overall premise being false. I do not
  know whether that reflects careful work by the discarded attempt's Security Architect or
  coincidence, and did not attempt to find out — it does not change anything in the new file,
  which was re-derived from source regardless.

## Work completed

Overwrote `SECURITY_POLICY.md` (584 lines) in full, replacing the untracked leftover from the
discarded `phase-03-2026-07-30-a` attempt, with all 12 sections required by the brief:

1. Scope, ownership, precedence — including an explicit note that a stale version of this
   file existed on disk from the discarded attempt and is fully superseded, and the
   relationship to `SKILL_SECURITY_POLICY.md` stated as cross-reference, not restatement.
2. Secrets — what counts, the three-tier storage model, the absolute prohibition list, and the
   `ACT-R06` context rule with the structural (not trust-based) reason an LLM agent must never
   receive a secret value into context.
3. **Credential-free/borrowed-authority access** — the five classes named by letter with one
   concrete example each, the governing sentence, `ACT-R09`/`ESC-011` cited directly, `C-009`
   and `C-045` cited as the concrete registry rows this class names, and an explicit statement
   of what actually governs this class (registry disposition, not a credential check;
   detective `git diff` habit per `R-22`; the one preventive control being an operator action
   outside this repository's boundary).
4. Credential lifecycle — request → provision → store → use → rotate → revoke, each stage's
   actor and current state, plus the "what `D-046` does and does not unblock" subsection.
5. Secret exposure incident response — 8-step numbered procedure, `ESC-004`, the
   "deletion doesn't remove it from history" and "once pushed it's already mirrored
   off-machine" points, both required by the brief.
6. Access control — restates `docs/PROJECT_BOUNDARIES.md` without re-deriving it, states the
   RDBC asymmetry **narrowed to content-and-origin, not path** (`F-02-02`, `R-23`, `ACT-R04b`),
   names `C-044`/`C-052` as the concrete capabilities that defeat a path-only rule, and
   restates one-owner-per-file.
7. Repository security — private-repo requirement, branch-protection gap named as open with
   the exact owner action, force-push `OWNER_ONLY` with the `F-01-01` `--force-with-lease`
   precedent pinned to commit `f282b89`.
8. Untrusted content extended to preloaded content — quotes the exact `CLAUDE.md` §11 example
   (the Bright Data plugin description), states the authorship-not-retrieval rule, and the
   required quote/name/escalate/never-obey handling for both fetched and preloaded content.
9. Tool-grant lists are not enforcement — states plainly that no subagent is read-only, `Bash`
   defeats any such grant, and `ACT-X06` makes *treating* a grant list as a boundary itself a
   violation.
10. Fail-closed statement — restates `D-044` (the real fail-closed decision; **not** the old
    draft's incorrect `D-042` citation for this rule) verbatim with its consequences.
11. What is NOT covered — nine named gaps, each pointing at the owning sibling file or open
    question.
12. Capability classification — an honest table grading every element `PROPOSED` /
    `SCAFFOLDED` / `PRODUCTION_BLOCKED`, explicitly stating nothing here is `IMPLEMENTED`.

## Files changed

- `SECURITY_POLICY.md` — overwritten in full (was untracked leftover from the discarded
  `phase-03-2026-07-30-a` attempt; now written fresh against the real merged Phase 02 state
  and the real `policy/POLICY_CONTRACT.md`/`policy/action_registry.json`).
- `agent_runs/phase-03/handoffs/HANDOFF_SECURITY_ARCHITECT.md` — overwritten in full (same
  reason).

No other file was written, edited, or staged. I did not touch `DECISIONS.md`, `findings.md`,
`progress.md`, `RISK_REGISTER.md`, `OPEN_QUESTIONS.md`, `CURRENT_PHASE.md`, `task_plan.md`,
any sibling policy file, `policy/action_registry.json`, `policy/POLICY_CONTRACT.md`, any file
under `tools/`, or any harness config — all outside my two-file assignment.

## Tests run

No automated test exists for a prose policy document, and none was assigned to me. What I
actually ran, as verification rather than testing, with real commands and real output:

- `git status --short` (before writing) — confirmed `SECURITY_POLICY.md` and this handoff were
  present as untracked (`??`) files, explaining why they survived the branch reset and telling
  me I was overwriting a stale leftover, not another live agent's concurrent work.
- A Python (`py -3`) regex extraction over the finished `SECURITY_POLICY.md`, pulling every
  `D-`, `Q-`, `R-`, `NG-`, `F-`, `C-`, `ACT-`, and `ESC-` token, run via the Bash tool. Output
  recorded above under "Facts and evidence."
- Targeted `Grep` calls to confirm existence of `D-013`, `D-026`, `D-032` in `DECISIONS.md`
  (pattern `^\| D-013 \|` etc., all matched) and `Q-003`, `Q-012`, `Q-014` in
  `OPEN_QUESTIONS.md` (pattern `^### Q-003` etc., all matched, all status `UNRESOLVED`).
- `wc -l SECURITY_POLICY.md` after writing — returned 584, confirming the write completed and
  produced a substantive, non-truncated file.
- I did **not** run `tools/policy_check.py` or `tools/render_permission_matrix.py`. Both are
  outside my assignment (owned by the Phase 03 Owner per `task_plan.md`'s file-ownership
  table) and the phase owner's T3 mechanical-verification step should run them against this
  file before the Independent Governance Auditor or Independent Reviewer treats it as verified,
  per `F-00-04`'s "check before review" lesson.

## Failures or risks

- **No mechanical citation-checker was run against my own document.** I self-verified every ID
  by direct grep or read against the source registers, which is a real check, but it is not
  the same as running the actual `tools/policy_check.py` the phase depends on — that tool may
  enforce a citation format or structural rule I am not aware of. Recommend the phase owner
  run it against this file specifically before integration (T3).
- **I could not verify the live state of GitHub branch protection** (Assumption 2) — no GitHub
  access, none authorized for this task. The gap is named from the register text, which could
  in principle be stale, though nothing I found suggests it is.
- **Length.** At 584 lines this is longer than the discarded draft's 388. The added length is
  almost entirely §3 (credential-free/borrowed-authority access), which the brief names as the
  section that matters most and which the old draft treated only glancingly inside its §3
  ("what `D-041` does and does not unblock" subsection, with no five-class enumeration, no
  `ACT-R09`/`ESC-011` citation, and no `C-009`/`C-045` naming). I judged this the correct
  tradeoff given the explicit brief, not scope creep.
- **I did not re-read `SKILL_SECURITY_POLICY.md`'s own §3 table of borrowed-authority classes
  line-by-line against my §3** to confirm zero prose drift beyond what I intended — I read it
  in full once and wrote my own condensed version pointing back to it for the full
  enumeration, per the instruction to cross-reference rather than restate. A future reviewer
  should spot-check that my condensed five-class table does not silently contradict
  `SKILL_SECURITY_POLICY.md` §3.2's fuller version.

## Recommended next action

1. Phase owner runs `tools/policy_check.py` against `SECURITY_POLICY.md` specifically, before
   treating it as reviewed (T3, per `F-00-04`).
2. Independent Reviewer's prose cross-read (`D-041`'s Q-017 resolution) should specifically
   check: (a) no claim here widens a boundary `docs/PROJECT_BOUNDARIES.md`,
   `CAPABILITY_REGISTRY.md`, or `policy/action_registry.json` does not already grant; (b) §12's
   classification table does not overstate any control as more implemented than it is; (c) my
   condensed §3 five-class table does not drift from `SKILL_SECURITY_POLICY.md` §3.2's fuller
   version; (d) §10's `D-044` citation for the fail-closed rule is correct where the discarded
   draft had cited the wrong decision (`D-042`, which in the real register concerns
   `AGENT_PERMISSION_MATRIX.md` generation, not the fail-closed default).
3. Phase owner's integration pass should confirm §11 ("what is NOT covered") correctly names
   the sibling policy files once all four specialists' work lands, since I deliberately did
   not read their content and could be pointing at the wrong file for a given gap.
4. When `Q-003`/`D-047`'s numeric blanks are filled in by the owner, this file's §4 rotation
   row and §11 should be updated to point at the resolved value rather than remain blank — out
   of my scope, flagged so it is not forgotten (`F-01-09` records exactly this kind of
   staleness recurring when nobody owns the update).
5. Before the gate report, re-run the drift check `SKILL_SECURITY_POLICY.md` §7.2 trigger T1
   requires (re-capture the session capability inventory and diff against
   `CAPABILITY_REGISTRY.md`) — this file's §3 depends on `C-009`/`C-045`'s dispositions still
   being current, and nothing in this file itself performs that check.
