# Agent Handoff

- Run ID: `phase-02-2026-07-29-a`
- Phase: 02 — Capability Registry and Skill Foundation
- Agent: Agent Architecture Specialist (second pass)
- Assignment: Join the first pass's demand model against the now-existing supply inventory and registry, and express the join as `CUSTOM_SKILL_BACKLOG.md` and `SKILL_TEST_PLAN.md`.
- Files owned: `CUSTOM_SKILL_BACKLOG.md`, `SKILL_TEST_PLAN.md`, `agent_runs/phase-02/handoffs/HANDOFF_ARCHITECTURE_SPECIALIST_PASS2.md`

---

## Facts and evidence

### 0. What changed between the two passes, and why it is the point

The first pass (`agent_runs/phase-02/handoffs/HANDOFF_AGENT_ARCHITECTURE_SPECIALIST.md`)
was **blind to this machine by design** (`F-00-07`). Its own §0 says so: *"nothing
in this document is a gap. Every row is a need."* This pass reads
`CAPABILITY_REGISTRY.md` and `agent_runs/phase-02/evidence/SESSION_CAPABILITY_INVENTORY.md`
and performs the reconciliation. **Everything below that carries weight is a
product of the join, not a restatement of the first pass.**

The most valuable output is §1: what the supply side changed.

### 1. What the join changed — the seven-line answer

**No skill was dropped. None was merged. Four were rescoped, two materially, and
one gained a boundary it structurally cannot cover.**

| ID | Change | Driver |
|---|---|---|
| `CSK-01` `blast-radius-check` | **Unchanged.** All dependencies (`C-001`, `C-003`, `C-004`) are `RESTRICTED` with conditions it satisfies by construction | — |
| `CSK-02` `schema-validate` | **Rescoped — new blocker.** `C-003`'s recorded condition is *"No installs"*. The off-the-shelf library the first pass correctly said to use is **not currently acquirable** under the registry as accepted | `C-003`, `C-004` |
| `CSK-03` `untrusted-envelope` | **Rescoped twice.** (a) Transport narrows to `WebFetch`/`WebSearch` only — every richer ingestion path is `PROHIBITED`; the inbound-message envelope has no permitted channel and is `BLOCKED`. (b) **It cannot cover the whole trust boundary**: pre-loaded third-party skill and MCP tool descriptions never pass through a retrieval, so there is nothing to interpose | `C-028`/`C-029` vs `C-045`, `C-071`, `C-119`–`C-121`, `C-132`, `C-039`, `C-126`; `Ev §7`; registry §I finding 3 |
| `CSK-04` `claim-guard` | **Unchanged, and strengthened.** No supply row substitutes for any part of it. The registry's `RESTRICTED`-to-reference-only marketing skills (`C-110`, `C-111`) make the case for it stronger, not weaker | `C-110`, `C-111` |
| `CSK-05` `gate-router` | **Unchanged; two supply components attached.** `C-008` (`AskUserQuestion`, `PERMITTED`) is the escalation channel; `C-024` (`PushNotification`) carries the registry's own warning that *a notification is not an approval*, which became a negative-contract line and a test (`T-CSK-05-P4`) | `C-008`, `C-024` |
| `CSK-06` `dry-run-publisher` | **Rescoped materially.** The component splits at its own `dry_run` flag: the dry-run branch is fully buildable and testable; **the live branch is `BLOCKED`, not merely unbuilt** | No `PERMITTED` outbound write path exists in 141 rows |
| `CSK-07` `cycle-runner` | **Rescoped materially.** Manual / `SIMULATION` half buildable including the timezone logic; **the unattended trigger and both delivery channels are `BLOCKED`** | Nine `PROHIBITED` schedulers; both Phase 19 delivery channels prohibited or `Q-004`-blocked |

### 2. The four findings the join produced that the first pass could not have

**2.1 — "Skill" is a packaging word, and for six of seven it is the wrong one.**
`D-003` reserves permissions, state changes, calculations, deduplication,
scheduling, and publishing to deterministic code. A Claude Code skill is a
Markdown instruction document that an LLM reads and follows — **an instruction
document cannot refuse.** A `CSK-06` implemented as a skill would have an LLM
deciding whether to send. Each backlog entry therefore records an *artifact form*
(`COMPONENT` / `DOCUMENT` / `COMPONENT + thin DOCUMENT`). The registry supports
the distinction: `C-097` (`skill-creator`, `PERMITTED`/`NEEDED`) blesses authoring
project-owned skills, and `C-081` (`find-skills`) is `RESTRICTED` to discovery
never install — but what is authored still has to satisfy `D-003`.
Recorded as `OQ-P2-4`.

**2.2 — There is no permitted way to acquire a runtime dependency.** `C-003` and
`C-004` are `RESTRICTED` with the condition *"local operations only… No installs,
no `curl` to third-party endpoints."* Phase 04's first pass condition — *"Schemas
validate fixtures"* — depends on a validator this project may not currently
obtain, and the only alternative is writing one, which the first pass explicitly
identified as waste. `SKILL_INSTALLATION_PLAN.md` (not my file) today reads as
covering *skills*, not libraries. Recorded as `OQ-P2-1`.

**2.3 — `CSK-03` cannot close the trust boundary it was designed for.**
`Ev §7` records `C-121` (`bright-data-mcp`) asserting, in its own description,
*"No exceptions"* and *"MUST replace WebFetch and WebSearch"* — third-party text
directing agent tool selection. Registry §I finding 3 records four further
capabilities documented as modifying this project's own contract, configuration,
permission grants, or filesystem grants (`C-116`, `C-135`, `C-085`, `C-087`,
`C-054`). `D-009` covers all of it — external text is data — but **the envelope
cannot enforce it**, because the text is in context before any agent acts. The
control is a policy, and it belongs to `SKILL_SECURITY_POLICY.md`, which I do not
own. Routed explicitly as `OQ-P2-2` so it does not fall between two documents.

**2.4 — The scheduler gap is not an absence; it is nine prohibitions within
reach.** The first pass framed `OQ-1` as *nothing owns the execution host*.
Supply reframes it: **nine scheduling capabilities are present on this machine
right now and this project's own rules prohibit every one** — `C-011`, `C-017`,
`C-025`, `C-043`, `C-048`, `C-049`, `C-090`, `C-101`, `C-141`. Each is one
`ToolSearch` call away (`C-007`, which `Ev §2` states has no approval step in
front of it). The operational instruction that follows is sharper than "open the
question": **`OQ-1` may not be resolved by reaching for one of the nine.** They
would deliver unattended execution while bypassing the ladder entirely.

Two `RESTRICTED` read-only rows are genuinely useful and are now specified as a
test: `C-018` (`CronList`) and `C-050` (`list_scheduled_tasks`), each carrying the
registry's note that the one legitimate use is confirming nothing is scheduled
against this project. That is `T-POS-07` — and it **cannot run in Phase 02**,
because running it means invoking a capability while Phase 02's pass condition is
that nothing was invoked. Stated openly in `SKILL_TEST_PLAN.md` §7.2 rather than
resolved quietly.

### 3. Phase 19 has zero permitted delivery channels, not one

The first pass (§7) found that Phase 19's email delivery collides with the
absolute send prohibition and has no owner carve-out (`OQ-3`). The join adds the
other half: **Drive delivery is `Q-004`-`BLOCKED`, and every email path in the
inventory is `PROHIBITED`** — `C-057`/`C-125` (Resend), `C-038` (Gmail drafts),
`C-059` (Klaviyo), `C-060` (Intercom). Phase 19's pass condition names *"Email and
Drive delivery independently retryable."* Both channels are unavailable today.
`C-008` (`AskUserQuestion`, `PERMITTED`) and `C-024` (`PushNotification`,
`RESTRICTED`) are the only channels that reach the owner without a prohibition,
and `C-024` is explicitly not an approval mechanism.

### 4. Two mechanical checks I ran, and their red demonstrations

Per `F-00-04` (run mechanical checks before review) and `F-01-04` (a green check
is not evidence until the checker has been shown to go red). These are read-only
`grep`/`awk` over a repository file. They are not capability invocations.

**Check 1 — registry ID count, uniqueness, contiguity.**

```
grep -oE "^\| C-[0-9]{3} " CAPABILITY_REGISTRY.md | tr -d '| ' | sort > ids.txt
count=141   unique=141   first=C-001   last=C-141
diff <(seq -f "C-%03g" 1 141 | sort) ids.txt   →  NO DIFF
```

**Red demonstration** — mutated a scratch copy, renaming `C-077` to `C-177`:

```
77d76
< C-077
141a141
> C-177
exit=1
```

The checker goes red. **Result: the registry's 141 IDs are unique and contiguous
`C-001`–`C-141`.**

**Check 2 — disposition counts vs. the registry's own §G table.** Whole-cell token
match, so a token appearing inside prose in a `Notes` cell cannot be counted:

```
PERMITTED 26   RESTRICTED 31   PROHIBITED 83   UNRESOLVED 1   (total 141)
```

**Red demonstration** — mutated a scratch copy, changing `C-008` from `PERMITTED`
to `RESTRICTED`:

```
PERMITTED 25   RESTRICTED 32   PROHIBITED 83   UNRESOLVED 1
```

The counter goes red. **Result: §G's counts reconcile exactly with the tables.**
Both are specified for re-running as `T-POS-04` and `T-POS-05`.

**What these two checks do not establish:** nothing about whether a disposition is
*correct*, only that the register is internally consistent and arithmetically
sound. I did not check vocabulary conformance cell-by-cell (`T-POS-03`) or `Basis`
citation resolution (`T-POS-05`'s second half); both are specified and neither
was run.

---

## Assumptions

`F-00-05` records that all three Phase 00 specialists reported no assumptions and
that review found fabricated attributions in their work. A clean assumptions
section is a red flag. These are mine.

1. **I accepted `CAPABILITY_REGISTRY.md`'s dispositions as given, and built the join on top of them.** `INFERRED`. The registry is marked `DRAFT for the Phase 02 Owner to integrate`, its `Disposition` vocabulary is `PROPOSED` and awaits the owner's acceptance (Skill Auditor open questions 2 and 3), and the `NOT_PRODUCTION_FACING` sentinel is a flagged drafting choice (its open question 1). **If the owner rescopes any disposition, every "blocked by" claim in `CUSTOM_SKILL_BACKLOG.md` §3.1 must be re-derived.** This is the load-bearing assumption in this pass.
2. **I treated `C-003`'s "No installs" condition as binding on runtime dependencies, not only on tool installation.** `INFERRED`. The condition's text does not distinguish them. Reading it narrowly would dissolve `OQ-P2-1`. I chose the stricter reading because `BOUNDARIES` §7.5 makes the stricter reading govern until the owner resolves a conflict — but I am not confident this is what the Skill Auditor meant, and it is cheap for the Phase 02 Owner to settle.
3. **I carried the first pass's reading of "tested" — a command ran and its real output was recorded** (`CLAUDE.md` §6). `INFERRED`. Its own Assumption 1. If a phase owner reads "tested" as "documented", the Phase 03 and Phase 04 hard edges soften and `SKILL_TEST_PLAN.md` §10's schedule slips accordingly.
4. **I did not re-derive the demand model.** I took the 61 needs and seven contracts as given and joined them. If `N-01`…`N-61` is incomplete — and the first pass says it is a floor, not a ceiling — the backlog inherits that.
5. **`OQ-P2-1`…`OQ-P2-4` are local to my two files.** They reserve no namespace in `OPEN_QUESTIONS.md`. If the phase owner registers them, the owner assigns the `Q-` IDs.
6. **I assumed `SKILL_INSTALLATION_PLAN.md`, `CONNECTOR_ACTIVATION_PLAN.md`, and `SKILL_SECURITY_POLICY.md` will exist and will carry what I routed to them.** `PROPOSED`. None exists as of this writing. `T-POS-08` and `OQ-P2-2` both depend on documents that are currently absent — the `F-00-08` pattern, and I have flagged it rather than assumed it away.

---

## Open questions

`HANDOFF OQ-1`…`OQ-7` from the first pass remain open and, as of 2026-07-29,
**unregistered** — `OPEN_QUESTIONS.md` still holds only `Q-001`…`Q-011`. Carrying
them across is the Phase 02 Owner's action, and leaving them uncarried is `F-00-08`
repeating. Four new ones from this pass:

| ID | Question | Why it matters | Exact action, by whom |
|---|---|---|---|
| `OQ-P2-1` | How does this project acquire a runtime dependency, given `C-003`'s *"No installs"*? | `CSK-02` needs a schema-validation library; Phase 04's first pass condition depends on it; the alternative is writing a validator, which the first pass said not to do | **Phase 02 Owner** decides whether `SKILL_INSTALLATION_PLAN.md` covers runtime dependencies or `C-003`'s condition needs amending; if neither, **Project Owner** rules |
| `OQ-P2-2` | What controls pre-loaded third-party skill and MCP tool descriptions, which `CSK-03` structurally cannot wrap? | They are external text that instructs agent behaviour, arriving before any agent acts. `Ev §7` and registry §I finding 3 evidence it | **Phase 02 Owner**, in `SKILL_SECURITY_POLICY.md` — the deliverable whose scope this is |
| `OQ-P2-3` | Where does project-owned skill and deterministic-component **source** live? | No phase names a home; first `tests/` is Phase 13; `.claude/skills/` is harness territory (`D-032`, `F-00-09`). Compounds `HANDOFF OQ-2` (fixtures) | **Phase 02 or 03 Owner** records it **before** Phase 04 needs it |
| `OQ-P2-4` | Does the deliverable name *"custom skill"* mislead later phases into building instruction documents where `D-003` requires code? | An instruction document cannot refuse. Six of seven must be components | **Phase 02 Owner** records the packaging distinction in the gate report |

**One instruction attaches to an existing question rather than opening a new one:**
`HANDOFF OQ-1` (who owns the scheduled-execution host) **may not be answered by
reaching for one of the nine prohibited schedulers already present on this
machine.**

---

## Work completed

1. Read completely: `CLAUDE.md`, the first-pass architecture handoff, `CAPABILITY_REGISTRY.md` (all 541 lines), `SESSION_CAPABILITY_INVENTORY.md`, the Phase 02 prompt, `findings.md`, `templates/AGENT_HANDOFF_TEMPLATE.md`, and the Skill Auditor's open questions. Read the relevant sections of `DECISIONS.md`, `OPEN_QUESTIONS.md`, `RISK_REGISTER.md`, and `docs/PROJECT_BOUNDARIES.md`.
2. Registered stable IDs `CSK-01`…`CSK-07` with an explicit mapping from the first pass's local `CS-nn`, and a `CSK-90+` block for rejections so a rejection can be cited and cannot be silently re-proposed.
3. Performed the demand↔supply join per skill: what **not** to build because adequate supply exists, what is genuinely custom, and where a registry disposition **blocks** a dependency. Summarised in one table (`CUSTOM_SKILL_BACKLOG.md` §3.1) and argued in §3.2–§3.6.
4. Carried all seven contracts forward with the full twelve-field contract, adding the *supply join* and *artifact form* fields.
5. Stated build order, the maintenance warning sized to `D-019`, and the cut analysis — including which entry degrades gracefully (`CSK-01`, into a checklist step) and which does not (`CSK-04`, the `R-07` mitigation).
6. Recorded the four candidates the first pass rejected, with the supply join's verdict added to each, plus two newly rejected in this pass and one routed to another document.
7. Specified `SKILL_TEST_PLAN.md`: the three-way distinction with the two ways it gets lost; the mandatory red-mutation rule with four validity criteria; per-skill test tables preserving must-fire / must-not-fire / must-not-*pass*; nine posture tests; the drift test with its three honest limits; the clock seam; what cannot be tested yet; and a phase-by-phase execution schedule.
8. Ran two mechanical checks over `CAPABILITY_REGISTRY.md` and demonstrated each going red before believing its green result.

---

## Files changed

Three files, all of which I own:

- `CUSTOM_SKILL_BACKLOG.md` (created)
- `SKILL_TEST_PLAN.md` (created)
- `agent_runs/phase-02/handoffs/HANDOFF_ARCHITECTURE_SPECIALIST_PASS2.md` (created)

No other file in the repository was created, modified, or deleted.
`CAPABILITY_REGISTRY.md`, `progress.md`, `findings.md`, `DECISIONS.md`,
`OPEN_QUESTIONS.md`, and `task_plan.md` are other agents' files and I did not touch
them (`F-00-09`, `D-004`).

**Disclosure — files written outside the project root.** The two mechanical checks
above wrote five scratch files to the Git Bash `/tmp` directory
(`ids.txt`, `ids2.txt`, `exp.txt`, `scratch_reg.md`, `scratch_reg2.md`). `/tmp` is
neither the project root nor the session scratchpad, and `C-002`'s recorded
condition and `BOUNDARIES` §1 are narrower than that. The files contained only
derived data from `CAPABILITY_REGISTRY.md` — no secret, no personal data — and all
five were deleted; deletion was verified (`ls` returned *No such file or
directory* for both sampled paths). Disclosed rather than rounded down, per the
Phase 00 precedent and `F-01-07`.

---

## Tests run

**No test from `SKILL_TEST_PLAN.md` was executed, and no capability was invoked.**

To the standard `CLAUDE.md` §6 requires:

- I invoked **no** skill, MCP tool, connector, plugin, or subagent. I called neither `ToolSearch` nor `Skill`.
- I installed, enabled, authorized, configured, or upgraded **nothing**.
- I made **no** network request and touched **no** external system.
- I read **no** path outside the project root. `C:\Users\crone\Projects\Rough-Draft-Builders-Club` was not read, listed, stat'd, or timestamp-checked in any form.

**Why:** Phase 02's first pass condition is *"No unverified skill enabled."*
Testing a capability to see whether it satisfies a need would be the exact action
that condition forbids, and would also convert the registry's `UNRESOLVED`
authentication state into a claim `CLAUDE.md` §6 forbids inventing. Six of the
seven components under test do not exist, so there was nothing of mine to run
either.

**What I did run** — read-only shell over repository files, for verification of
the registry's internal consistency. Commands and actual output are transcribed in
*Facts and evidence* §4, including both red demonstrations. These are file reads
and text arithmetic; they verify no claim about any capability's behaviour.

```
grep -oE "^\| C-[0-9]{3} " CAPABILITY_REGISTRY.md | tr -d '| ' | sort
diff <(seq -f "C-%03g" 1 141 | sort) ids.txt
awk -F'|' '/^\| C-[0-9]{3} /{...}' CAPABILITY_REGISTRY.md      # whole-cell token counts
sed 's/^| C-077 |/| C-177 |/' CAPABILITY_REGISTRY.md           # red mutation 1
sed 's/^\(| C-008 .*\)| PERMITTED |/\1| RESTRICTED |/' ...     # red mutation 2
```

Both checkers were shown to go red before their green results were believed
(`F-01-04`). **The tests specified in `SKILL_TEST_PLAN.md` §4–§6 have not been
run, cannot be run today, and are not claimed to have been.**

---

## Failures or risks

1. **The join is only as good as the registry, and the registry is a `DRAFT` whose vocabulary is `PROPOSED`.** Its `Disposition` axis awaits the Phase 02 Owner's acceptance. Every `BLOCKED` finding in my backlog is downstream of a disposition that could change. If the owner rejects or rescopes the vocabulary, §3.1 must be re-derived — it is a table, not a narrative, precisely so that re-derivation is mechanical.
2. **The registry is a dated snapshot with no drift detection**, and it says so itself. `T-POS-06` is the re-verification test and it has three limits: it is operator-assisted (`Ev §8` records that no command reproduces the disclosure), its cadence is the phase gate so it sees nothing in between, and a clean diff proves the *disclosure* is unchanged, not that an account gained authorization. Drift toward more capability is the case that matters, because `C-007` puts a new connector one call from use with no approval step.
3. **`OQ-P2-1` is on Phase 04's critical path and nobody owns it yet.** Phase 04 is two phases out and its first pass condition depends on a validator with no permitted acquisition path. This is cheap to settle now and awkward to settle mid-phase — the same species of problem as `HANDOFF OQ-2` (fixtures with no home), and the two are best settled together.
4. **`OQ-P2-2` routes a real control into a document that does not exist yet.** If `SKILL_SECURITY_POLICY.md` is written without it, the pre-loaded-instruction surface has no owner at all — `CSK-03` cannot cover it and I do not own the file that can. This is the `F-00-08` pattern: a material unknown documented where nobody will consult it.
5. **I did not verify that every registry row I cite says what I claim it says.** I read the registry in full and cited ~60 rows across two documents. Quote fidelity and citation-target correctness are mechanically checkable and I checked neither. Per `F-00-04` this should run **before** independent review, not after; per `F-01-04`, whatever checker runs it must be shown to go red first.
6. **`R-18` still applies, and the join narrowed rather than removed it.** Platform APIs and connectors change. The rescoped `CSK-06` is now the most durable entry — its four-precondition gate survives a provider swap unchanged, because it never names a provider. `CSK-03`'s transport binding to `WebFetch`/`WebSearch` is the least durable and should be re-checked whenever the inventory drifts.
7. **Seven components remain a real standing load for a solo operator** (`D-019`), and the join added a cost the first pass did not price: each project-owned skill document is itself text that instructs an agent — the class of artifact registry §I finding 3 identifies as a risk surface. Project-owned ones are safer only because they are version-controlled, phase-gated, and reviewable. That safety is a process, and the process costs review time the owner does not have much of.

---

## Recommended next action

**For the Phase 02 Owner, in order:**

1. **Settle the registry's `Disposition` vocabulary and the `NOT_PRODUCTION_FACING` sentinel** before `SKILL_INSTALLATION_PLAN.md`, `CONNECTOR_ACTIVATION_PLAN.md`, or `SKILL_SECURITY_POLICY.md` are written. All three depend on it and so do my two files — this is exactly the dependent-output sequencing `F-00-07` warns about, and the Skill Auditor raised it first.
2. **Carry `OQ-P2-2` into `SKILL_SECURITY_POLICY.md` as a scoped requirement**, not a mention. It is the one control this pass identified that no component can enforce.
3. **Answer `OQ-P2-1` and `HANDOFF OQ-2` together** — dependency acquisition and fixture home. Both gate Phase 04 and both are cheap now.
4. **Register `HANDOFF OQ-1`…`OQ-7` and `OQ-P2-1`…`OQ-P2-4` in `OPEN_QUESTIONS.md`** with the exact owner actions stated. Eleven questions currently live only in handoffs. `F-00-08` is what that becomes.
5. **Record in `findings.md`** the two Phase 02 findings this pass produced that extend `F-01-02`: that nine present schedulers are all prohibited (so `OQ-1` must not be resolved by reaching for one), and that Phase 19 has zero permitted delivery channels rather than one blocked channel.
6. **Run `T-POS-01` through `T-POS-05` and `T-POS-09` before the independent review**, with their red mutations recorded (`F-00-04` + `F-01-04`). Two of the five are already done and transcribed above; three are not. **Do not run `T-POS-07` in this phase** — `SKILL_TEST_PLAN.md` §7.2.

**For the Project Owner** — nothing in this pass requires a decision that
`HANDOFF §6`/`§7` did not already surface. `OQ-1` (who owns the scheduled-execution
host) and `OQ-3` (may the system send email to you) remain the two that only the
owner can settle, and this pass sharpened `OQ-1`: nine schedulers are already on
this machine and every one of them is prohibited, so the answer is a governance
decision and not a tooling choice.

**Do not begin Phase 03** (`D-007`).
