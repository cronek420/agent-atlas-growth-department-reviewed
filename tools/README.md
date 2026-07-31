# tools/ — reusable verification scripts

**Created:** Phase 02, 2026-07-29, under Standing Operating Grant clause 1 (`D-040`).
**Why this directory exists:** the Phase 02 Independent Reviewer found that all ten of that phase's mechanical checks were run from a **session scratchpad that no longer exists**, so none of them was reproducible and none of the recorded results could be re-derived. That defect is the main reason Testing scored 3 against a floor of 4.

It was also pure waste. Phase 01 built equivalent checks, threw them away, and Phase 02 rebuilt them from scratch — **and reproduced two of Phase 01's own false positives in the process** (`findings.md` `F-01-04` item 3). Scripts in a scratchpad are a lesson that has to be relearned every phase.

---

## The rule these scripts exist to enforce

> **A checker that reports success proves nothing until it has been shown to fail.**

This is `findings.md` `F-01-04`, and it is not theoretical. Across Phases 01 and 02, checkers produced **seven** false results while the documents under test were correct, and once a check reported a clean pass that was not evidence at all because its own red test silently did not fire.

Every script here therefore ships with a documented red mutation — the smallest change to input that must make it fail. **Run the red case before trusting the green one.** A green result with no accompanying red demonstration is not evidence and must not be recorded as one.

---

## Scripts

### `idcheck.py` — cross-reference and path integrity
```bash
python tools/idcheck.py <repo_root> <file> [<file> ...]
```
Verifies every `D-`/`Q-`/`R-`/`NG-`/`F-` identifier cited in the named files resolves to a real register row, and that every cited relative path exists.

Prints the definition counts it parsed, so a run that silently found zero definitions — a broken checker — is visible rather than passing. Allowlists future artefacts **derived from `MASTER_PLAN.md`** rather than hand-maintained, and resolves bare filenames anywhere in the tree (the two fixes for Phase 01's ~92 and ~40 false positives).

- **Red mutation:** add `D-999 Q-888 R-77 NG-999 F-99-99` and `` `docs/NO_SUCH_FILE.md` `` to a scratch copy. All six must be flagged, exit 1.
- **Known accepted exceptions:** documents that *specify or evidence a red test* legitimately cite fake IDs. `SKILL_TEST_PLAN.md` and `agent_runs/phase-02/PHASE_GATE_REPORT.md` do. Do not "fix" these.

### `regcheck.py` — capability-registry vocabulary conformance
```bash
python tools/regcheck.py CAPABILITY_REGISTRY.md
```
Checks every status cell holds exactly one declared bare token across all four axes, and that each row's cell count matches its table header.

Locates columns **by header name, not by index**, because the registry has four different table schemas. An index-based version of this check reported ~80 false non-conformances that were entirely the checker's fault.

- **Red mutation:** change any `Ladder` cell to `PROBABLY_DISABLED`. Must be flagged.
- **Limitation, stated because it caused a real defect:** this script verifies that tokens are *well-formed*, **not that counts stated in prose are correct**. It certified "0 non-conforming" on a registry containing three wrong hand-maintained numbers in §G. **Vocabulary conformance is not arithmetic conformance.** Derive prose counts from this script's output rather than transcribing them (`D-040` clause 6).

### `contractcheck.py` — custom-skill contracts and trigger tests
```bash
python tools/contractcheck.py CUSTOM_SKILL_BACKLOG.md SKILL_TEST_PLAN.md
```
V-8: every `CSK-` entry carries all required contract fields, including the negative contract. V-9: every skill appears in the test plan with must-fire, must-not-fire, and must-not-**pass** cases plus a red mutation.

Section-scoped, not line-scoped. The line-scoped version produced false warnings on a `Red mutation` table column, and its first red test **did not fire** because section boundaries were computed wrongly — meaning it briefly reported a satisfied pass condition on a check that could not fail.

- **Red mutation:** remove `**Negative contract` from one entry (V-8 must flag); strip `must-not-pass` from one test-plan section (V-9 must flag).

---

### `render_permission_matrix.py` — generate `AGENT_PERMISSION_MATRIX.md` from `policy/action_registry.json`
```bash
python tools/render_permission_matrix.py [--check]
```
`AGENT_PERMISSION_MATRIX.md` is never hand-edited (`D-042`). This script is the only writer; `--check` regenerates in memory and diffs against what's on disk without touching it, for use in CI-style verification.

- **Red mutation:** hand-edit a line into `AGENT_PERMISSION_MATRIX.md` after generating it, then run `--check`. Must report drift and exit 1.

### `policy_check.py` — Phase 03 policy registry conformance (V-1..V-13)
```bash
python tools/policy_check.py
```
Fail-closed default, outcome-token validity, contradiction detection, nine-gated-category coverage, basis-ID resolution against the real registers, approval/autonomy state-machine integrity, matrix drift, and a secret-pattern scan across every Phase 03 deliverable.

- **Red mutation:** see `policy_check_selftest.py` below — it *is* the red-mutation suite for this script, one deliberately broken fixture per check (12 in total), run against copies/temp files so nothing on disk is touched.

### `policy_check_selftest.py` — proves `policy_check.py` actually goes red
```bash
python tools/policy_check_selftest.py
```
`F-01-04`: a green check is not evidence until the checker has been shown to fail. Twelve negative controls (broken fail-closed default, contradictory rows, stripped gated-category coverage, invented basis ID, dangling policy reference, non-owner `APPROVED` transition, terminal-state escape, ladder skip edge, deleted e-stop edge, matrix drift, injected secret, malformed JSON), plus a positive control confirming the real deliverables still pass cleanly after the fixtures run.

- **Red mutation:** this script's own failure mode is "a negative control is not caught" — if any of the 12 report `MISSED` instead of `CAUGHT`, it exits 1 and says exactly which check has a blind spot.

### `blast_radius_check.py` — `CSK-01`, `blast-radius-check`
```bash
python tools/blast_radius_check.py --phase-id 03 --baseline-ref <ref> [--changed-files f1 f2 ...] [--clock ISO8601]
```
Full contract: `CUSTOM_SKILL_BACKLOG.md` § "CSK-01". Enumerates candidate claims in the eight fixed governance inputs (`RISK_REGISTER.md`, `OPEN_QUESTIONS.md`, `DECISIONS.md`, `CURRENT_PHASE.md`, `MASTER_PLAN.md`, `README.md`, `CLAUDE.md`, `CAPABILITY_REGISTRY.md`) that this phase's `changed_files` may have made stale — before the gate report is drafted, per `F-01-09`. `D-003` **SPLIT**: deterministic enumeration here; falsification judgement is the phase owner's, done outside this script; the script never sets `verdict` on judgement, only on `(candidate count, unreadable count)`.

If `--changed-files` is omitted, it is derived from `git diff --name-only <baseline-ref>...HEAD` plus `git status --porcelain`, since phases in this project are frequently uncommitted mid-run.

- **Red mutation 1:** an unresolvable `--baseline-ref` must hard-fail with no `verdict` at all, never a silent `CLEAN`. Confirmed: `not-a-real-ref-xyz` → `HARD FAIL`, exit 1.
- **Red mutation 2:** any unreadable fixed input must make `verdict` anything but `CLEAN`, even with zero candidates. Confirmed by direct simulation.
- **Assigned owning phase:** Phase 03 builds it (this attempt). First needed: Phase 03 — the first phase after `F-01-09` was written. Do not confuse with `C-135`/`C-098` (both `PROHIBITED`) — those rewrite governance files; this one only reports on them and modifies nothing.

## For future phase owners

1. **Reuse these. Do not rebuild them in a scratchpad.** That is what this directory is for.
2. **Extend rather than fork.** A new phase's checks belong here, named for what they verify.
3. **Every new script carries a documented red mutation in this README.** No exceptions — a check without one is decoration.
4. **Convert findings into checks** (`D-040` clause 5). A lesson recorded only as prose recurs: `F-01-04` was written down clearly and recurred four times in the very next phase.
5. **These scripts are not a substitute for independent review.** Every serious Phase 00–02 defect that mattered was found by a reviewer or a specialist, never by a script. Mechanical checks catch malformed tokens and broken references. They do not catch a wrong number in prose, a stale status, a claim written before the work, or a boundary rule expressed in the wrong vocabulary — all of which happened and all of which a human-style reader caught.

Windows note: Windows PowerShell 5.1 is the only shell here (`F-01-03`). Python 3.14.6 is installed. No third-party packages are required by any script in this directory — deliberately, so they run with no install step.
