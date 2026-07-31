# Agent Handoff

- Run ID: `phase-02-2026-07-29-a`
- Phase: 02 — Capability Registry and Skill Foundation
- Agent: Skill Auditor (specialist)
- Assignment: Classify the entire observed capability surface into a machine-readable registry, against the project's actual governing rules.
- Files owned:
  - `CAPABILITY_REGISTRY.md` (project root) — **draft** for the Phase 02 Owner to integrate
  - `agent_runs/phase-02/handoffs/HANDOFF_SKILL_AUDITOR.md` — this file

## Facts and evidence

**Sole factual input:** `agent_runs/phase-02/evidence/SESSION_CAPABILITY_INVENTORY.md`,
captured by the Phase 02 Owner on 2026-07-29 and treated as fixed. Governing rules
were read from `CLAUDE.md`, `docs/PROJECT_BOUNDARIES.md`, `DECISIONS.md`,
`OPEN_QUESTIONS.md`, `CURRENT_PHASE.md`, `NON_GOALS.md`, `findings.md`,
`task_plan.md`, `MASTER_LINEAR_BUILD_PLAN.md`,
`phase-prompts/PHASE_02_CAPABILITY_REGISTRY_AND_SKILL_FOUNDATION.md`, and
`templates/AGENT_HANDOFF_TEMPLATE.md`.

1. **141 registry rows** cover every entry in the evidence file: `§1` loaded
   harness tools, `§2.1` deferred harness tools, `§2.2` all 11 connected MCP
   servers with high-authority tools broken out, `§3` all 23 auth-required servers
   plus `firebase`, `§4` all 13 subagent types, and `§5` all 13 skill namespaces.
   A row is a grouping; the rows cover several hundred individual tools and skills.
2. **Counts by disposition:** `PERMITTED` 26 · `RESTRICTED` 31 · `PROHIBITED` 83 ·
   `UNRESOLVED` 1. Sums to 141.
3. **Counts by relevance:** `NEEDED` 17 · `POSSIBLE` 55 · `IRRELEVANT` 69. Sums to
   141. The 69 `IRRELEVANT` rows are the exclusion list Phase 02's pass conditions
   require.
4. **Ladder:** every row is `DISABLED` (87) or `NOT_PRODUCTION_FACING` (54). No
   capability sits above `DISABLED`, consistent with `CLAUDE.md` §3.
5. **22 rows are prohibited today and plausibly relevant to a later phase.** That
   set — not the exclusion list — is where `CONNECTOR_ACTIVATION_PLAN.md` has work.
6. **`Ev §2` states that deferred is not disabled** and that no approval step
   stands between a deferred tool and its use. `ToolSearch` (`C-007`) is therefore
   the single control point for the whole deferred surface, and it is a plain
   harness tool with no gate of its own.
7. **No subagent type in `Ev §4` is read-only.** `Explore` and `Plan` are granted
   all tools except six (`Agent`, `Artifact`, `ExitPlanMode`, `Edit`, `Write`,
   `NotebookEdit`). `Bash` and `ToolSearch` remain, so both can load and call any
   prohibited tool. `general-purpose` and `claude` hold `*`.
8. **Two capabilities reach external systems with no credential:** `Artifact`
   (`C-009`, publishes to a claude.ai-hosted page) and `mcp__claude-in-chrome__*`
   (`C-045`, acts inside the operator's authenticated browser). Both bypass every
   credential-based control this project has built.
9. **Two capabilities read work from other projects on this machine:**
   `mcp__ccd_session_mgmt__search_session_transcripts` (`C-052`) and
   `mcp__cb9be2f0-…__get_recent_trajectories` (`C-044`).
10. **Five capabilities are documented as modifying this project's governance or
    permissions:** `C-116` and `C-135` (write `CLAUDE.md`), `C-085` (writes
    `settings.json` including auto-executing hooks), `C-087` (adds permission
    allowlists to reduce prompts), `C-054` (`request_directory`).
11. **The genuinely useful, low-risk capability is real and is named:** document
    generation (`C-096`), skill authoring (`C-097`), local data analysis (`C-127`),
    design and accessibility method (`C-129`), visualization (`C-083`, `C-016`),
    and code review (`C-088`). Five of these six are `PERMITTED` outright.

## Assumptions

Stated explicitly. `findings.md` `F-00-05` records that a specialist's claim of
"no assumptions" carries no evidentiary weight, so this section is written to be
challenged rather than accepted.

1. **The evidence file is accurate as a transcription of session disclosure.** I
   did not re-derive it and could not: doing so would mean invoking capabilities.
   If `SESSION_CAPABILITY_INVENTORY.md` misidentifies a server, my disposition for
   that row inherits the error.
2. **Server identifications in `Ev §2.2` are correct.** The opaque UUIDs were
   mapped to Stripe, Supabase, Gmail, Calendar, and a remote job runner by the
   phase owner from tool names. I reasoned from those identifications. A
   misidentification would change a row's rule basis but, in every case I checked,
   not its disposition — each is prohibited on more than one ground.
3. **A skill's disclosed description reflects what the skill does.** I did not read
   any skill body; they live outside the project root. Descriptions are text
   authored outside this project and are the weakest evidence in the registry. This
   most affects `C-104`, `C-110`, `C-111`, and `C-119`, where I judged intent from
   a description alone.
4. **"Production-facing" means: can publish, send, spend, deploy, create or modify
   an external account or resource, or reach an external system.** `D-010` does not
   define the term. Rows failing this test carry the `NOT_PRODUCTION_FACING`
   sentinel rather than a ladder stage. This is my definition, not the project's.
5. **Absence of a permission grant is a prohibition** (`BOUNDARIES` §8, `D-008`).
   Applied to Supabase, Figma, session management, and the remote runner, none of
   which appear in `BOUNDARIES` §3's table at all.

## Open questions

1. **Does the Phase 02 Owner accept the `NOT_PRODUCTION_FACING` sentinel in the
   ladder column?** It is not a `D-010` stage and I have said so in the registry.
   The alternative — splitting the registry into a production-facing table with a
   ladder column and a local-tooling table without one — is equally honest and
   avoids any token outside `D-010`. I chose the sentinel for a single uniform
   schema. **This is a drafting choice, and it is the owner's to overrule.**
2. **Does the Phase 02 Owner accept the disposition vocabulary
   (`PERMITTED` / `RESTRICTED` / `PROHIBITED` / `UNRESOLVED`)?** It is new to this
   project and is marked `PROPOSED` in the registry. `SKILL_INSTALLATION_PLAN.md`,
   `CONNECTOR_ACTIVATION_PLAN.md`, and `SKILL_SECURITY_POLICY.md` will all depend
   on it, so it should be settled before they are written — this is exactly the
   dependent-output sequencing `F-00-07` warns about.
3. **`Relevance` is a fourth column I introduced** so the exclusion list Phase 02
   must produce is mechanically derivable (`filter Relevance == IRRELEVANT`).
   Accept, rename, or drop.
4. **`C-019 DesignSync` is `UNRESOLVED` and needs an owner answer.** Exact
   question: *what does `DesignSync` synchronise, in which direction, and to what
   destination?* The harness disclosed a name and nothing else. Treated fail-closed
   meanwhile.
5. **`docs/PROJECT_BOUNDARIES.md` §3 states every external system is
   `NOT CONNECTED`. `C-009` and `C-045` complicate that.** I did not edit the
   boundary document — `CLAUDE.md` §6 forbids silently changing approved
   architecture, and §7 of the boundaries file reserves changes to an owner
   decision. **Raised, not fixed.** The registry states the project's position:
   §3 is true about *authorized connections* and misleading about *reachability*.
   A decision row is warranted.
6. **`SESSION_CAPABILITY_INVENTORY.md` cites `F-02-01`, `F-02-02`, `F-02-05`,
   `F-02-06`, and `CONNECTOR_ACTIVATION_PLAN.md`. None of these exists yet.**
   `findings.md` has no Phase 02 section, and no Phase 02 deliverable has been
   written. This is forward-referencing of the kind `F-01-08` names as the sharpest
   lesson of Phase 01 — a file asserting a record that does not yet exist. The
   evidence file is the phase owner's, not mine; **I did not edit it**, and the
   references are placeholders rather than false completion claims. Flagged so the
   owner closes them before the gate report, and so the independent reviewer does
   not have to find it.
7. **Should the 23 auth-required servers require a `DECISIONS.md` row before
   authorization, not after?** Today one interactive authorization enables a server
   and nothing in this repository would record it. This is a policy question for
   `CONNECTOR_ACTIVATION_PLAN.md` and arguably for Phase 03.
8. **Licence and provenance are out of my scope and are not established for any
   row.** A `PERMITTED` disposition is a *safety* judgement only. Several
   `PERMITTED` rows may fail the License and Provenance Reviewer's check.

## Work completed

- Read all eight required inputs plus `NON_GOALS.md`, `task_plan.md`, and
  `MASTER_LINEAR_BUILD_PLAN.md` in full before writing.
- Declared three classification axes and one supporting column, with per-token
  definitions, including how the `IMPLEMENTED` caution in `CLAUDE.md` §3 applies to
  skills (a skill is a document; it is never `IMPLEMENTED` on the strength of its
  own description).
- Classified 141 rows covering every section of the evidence file, each citing its
  evidence section and, where a disposition follows from a rule, the rule ID.
- Reasoned explicitly about every capability the assignment named:
  `adspirer-ads-agent:*` (`C-055`, `C-079`, `C-115` – `C-118`), `apollo:*`
  (`C-056`, `C-123`, `C-124`), `resend:*` (`C-057`, `C-125`, `C-126`),
  `stripe-projects` and `stripe_api_write` (`C-095`, `C-030`),
  `mcp__claude-in-chrome__*` (`C-045`), `Artifact` (`C-009`, `C-084`, `C-103`),
  the scheduling family (`C-011`, `C-017`, `C-048` – `C-050`, `C-090`, `C-101`),
  the remote-execution family (`C-025`, `C-043`), and
  `brightdata-plugin:*` / `tinyfish:*` (`C-119` – `C-122`, `C-132`, `C-071`).
- Assessed low-risk useful capability with the same rigour, and named which later
  phases each serves.
- Produced a summary count table, a recommended-target-stage table clearly labelled
  as recommendation, a three-item findings section, and a "what this registry does
  not establish" section.
- Stated the staleness condition prominently at the top of the registry.

## Files changed

| File | Change |
|---|---|
| `CAPABILITY_REGISTRY.md` | Created. Draft, ~141 classified rows |
| `agent_runs/phase-02/handoffs/HANDOFF_SKILL_AUDITOR.md` | Created. This file |

**No other file was created, edited, or deleted.** In particular I did not write
`findings.md`, `DECISIONS.md`, `progress.md`, `RISK_REGISTER.md`,
`docs/PROJECT_BOUNDARIES.md`, `CURRENT_PHASE.md`, `task_plan.md`,
`SESSION_CAPABILITY_INVENTORY.md`, or any harness configuration — each has a
different owner, and `F-00-09` records a Phase 00 subagent writing outside its
scope.

## Tests run

**No capability was executed, and none could have been without failing the phase.**

- **No skill was invoked.** The `Skill` tool was not called.
- **No MCP tool, connector, or plugin was invoked, loaded, enabled, installed,
  authenticated, or tested.** `ToolSearch` was not called, so no deferred tool's
  schema was ever loaded and none was callable.
- **No subagent was spawned.** The `Agent` tool was not called.
- **Nothing was installed.**
- **No path outside the project root was read**, including
  `C:\Users\crone\.claude\` and `C:\Users\crone\Projects\Rough-Draft-Builders-Club`.
  No listing, no stat, no timestamp read. `F-01-07` records that Phase 01's own
  validation plan mandated exactly such an access; I designed no check that would.

**What was executed:** `Read` against 11 project files, and one `Bash` command —
`ls -R agent_runs/phase-02 && ls` at the project root — to confirm which Phase 02
artifacts existed. That is the complete list.

**What this means for the phase's "Applicable tests actually executed" checklist
item:** this deliverable is a classification of written evidence. The mechanically
checkable properties of it are internal — one bare token per status cell, every
row citing an evidence section, arithmetic in the count tables, and every ID cited
resolving to a real definition. **I did not run those checks with a tool.** Per
`F-01-04`, an unverified checker produces unverified results, so I am not going to
claim a verification I did not perform. The count tables were computed by hand and
the registry says in §G that the tables are authoritative if a count disagrees. The
Phase 02 Owner should run the mechanical sweep before review, per `F-00-04`.

## Failures or risks

1. **The registry is stale on arrival if the operator's plugin set changes.**
   Stated at the top of the file, but stated is not mitigated. There is no
   mechanism in this project that would detect the change. Risk to a later phase
   acting on a row that no longer describes reality.
2. **83 of 141 rows are `PROHIBITED`, and nothing enforces a single one of them.**
   This registry is a document. The enforcement point is `ToolSearch` (`C-007`) and
   the spawn prompt of every subagent, both of which depend on an agent choosing to
   comply. `D-003` says deterministic code enforces permissions; no such code
   exists, and Phase 02 does not build any.
3. **My dispositions for skills rest on descriptions I did not verify** (Assumption
   3). Where a description understates what a skill does, my disposition is too
   permissive. The 16 `PERMITTED` rows in §F are where this risk concentrates.
4. **A `PERMITTED` disposition is a safety judgement only** — no licence,
   provenance, publisher, or terms-of-service check was performed by me.
5. **`Ev §2.2` server identifications could be wrong**, which would misattribute a
   rule basis. Impact is limited because each row is prohibited on multiple
   independent grounds.
6. **This work is in a git worktree** (`.claude/worktrees/phase-02-capability-registry-c04753`).
   Both files exist there and not on `main` until merged. Phase 01's residual risk
   applies: the off-machine mirror is only as current as the last push.
7. **I introduced two vocabularies and one sentinel token.** If the Phase 02 Owner
   changes any of them after `SKILL_INSTALLATION_PLAN.md` or
   `CONNECTOR_ACTIVATION_PLAN.md` cite this file, the rework is real. This is a
   sequencing risk of exactly the shape `F-00-07` describes.

## Recommended next action

**For the Phase 02 Owner, in this order:**

1. **Rule on the three vocabulary questions** (open questions 1–3) before any other
   Phase 02 deliverable cites this registry. Every remaining deliverable depends on
   the disposition vocabulary; settling it after they are drafted repeats `F-00-07`.
2. **Close the forward references in `SESSION_CAPABILITY_INVENTORY.md`** (open
   question 6) — write `F-02-01` … `F-02-06` into `findings.md`, or amend the
   evidence file's citations. Do this before the independent reviewer sees it.
3. **Open a decision row for the `BOUNDARIES` §3 tension** (open question 5).
   `Artifact` and `claude-in-chrome` reach external systems without credentials,
   and §3's `NOT CONNECTED` framing does not describe that. I did not edit the
   boundary document; a decision is the correct instrument.
4. **Run the mechanical sweep over `CAPABILITY_REGISTRY.md` before review**, per
   `F-00-04`: one bare token per status cell, every `Ev §N` resolving, every
   `D-`/`Q-`/`NG-`/`F-`/`C-` ID resolving, and the §G arithmetic. Per `F-01-04`,
   exercise the checker against a case it should fail before trusting a green
   result.
5. **Carry the three §I findings into `findings.md`, and `C-045` into
   `RISK_REGISTER.md`.** The browser path is the largest single gap between this
   project's written boundary model and its actual capability surface.
6. **Do not begin Phase 03** (`D-007`).

**For the Project Owner, one question worth asking early:** `C-019 DesignSync` is
the registry's only `UNRESOLVED` row — what does it synchronise, and where to?
