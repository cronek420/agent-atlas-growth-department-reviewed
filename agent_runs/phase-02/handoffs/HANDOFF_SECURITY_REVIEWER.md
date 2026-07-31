# Agent Handoff

- Run ID: `phase-02-2026-07-29-a`
- Phase: 02 — Capability Registry and Skill Foundation
- Agent: Security Reviewer (specialist)
- Assignment: Produce an enforceable, decidable security policy for skills, connectors, MCP servers, subagents, and harness tools; and a conditional activation plan for connectors a later phase might need. Assess the credential-free external-access paths, `ToolSearch` as a control point, subagent read-only claims, the governance-modifying capabilities, and the cross-project read paths.
- Files owned:
  - `SKILL_SECURITY_POLICY.md` (project root) — new
  - `CONNECTOR_ACTIVATION_PLAN.md` (project root) — new
  - `agent_runs/phase-02/handoffs/HANDOFF_SECURITY_REVIEWER.md` — this file

## Facts and evidence

Inputs read in full before writing: `CLAUDE.md`, `docs/PROJECT_BOUNDARIES.md`,
`DECISIONS.md`, `OPEN_QUESTIONS.md`, `RISK_REGISTER.md`, `NON_GOALS.md`,
`findings.md`, `agent_runs/phase-02/evidence/SESSION_CAPABILITY_INVENTORY.md`,
`CAPABILITY_REGISTRY.md`, `agent_runs/phase-02/handoffs/HANDOFF_SKILL_AUDITOR.md`,
`.env.example`, `.gitignore`, `task_plan.md`,
`phase-prompts/PHASE_02_CAPABILITY_REGISTRY_AND_SKILL_FOUNDATION.md`,
`templates/AGENT_HANDOFF_TEMPLATE.md`, and the "Human checkpoints" section of
`user-guide/USER_INSTRUCTIONS.md`.

**1. `docs/PROJECT_BOUNDARIES.md` §3's opening sentence is contradicted by its own
table.** The header reads *"Every external system below is `NOT CONNECTED`."* The
GitHub row in the same table reads **`CONNECTED` (2026-07-29)**, per `D-030`. Both
cannot be current. This is mechanical, not interpretive, and it predates Phase 02 —
Phase 01 updated the row and left the header. Verified by direct read.

**2. Read as a claim about credentials, §3 is otherwise true. Read as a claim about
reachability — which is how §8 step 4 invites a reader to use it — it is false.**
Full verdict and the recommended repair are in `SKILL_SECURITY_POLICY.md` §3.1. The
prohibition in §8 step 4 still binds; what fails is the justification beneath it.

**3. Credential-free external-access paths, enumerated in five classes**
(`SKILL_SECURITY_POLICY.md` §3.2). More than the two named in my assignment:
- **A — the operator's browser session:** `C-045`, 22 tools.
- **B — the operator's Claude platform account:** `Artifact` (`C-009`), the remote
  job runner (`C-043`, `C-044`), session management (`C-052`, `C-053`), the
  scheduling family (`C-011`, `C-017`, `C-025`, `C-048`, `C-090`, `C-101`),
  `PushNotification` (`C-024`), `spawn_task` (`C-014`), the connector registry
  (`C-051`).
- **C — connector grants held in the operator's Claude account rather than in this
  project:** Stripe, Supabase, Gmail, Calendar, Figma (`C-030`–`C-047`).
- **D — harness-mediated network access:** `WebFetch` / `WebSearch` (`C-028`,
  `C-029`) and the preview browser (`C-015`).
- **E — credentials belonging to a plugin rather than to this project:** Bright
  Data (`C-119`, `C-120`), TinyFish (`C-132`).

The unifying statement: **this project's controls govern credentials it holds; its
exposure is governed by authority it borrows.** `.env`, `.env.example`, `.gitignore`,
Google Secret Manager, and `D-027` all operate on credentials. None of these paths
consumes one.

**4. A concrete, checkable consequence in an existing artifact.** `.env.example`
reserves `STRIPE_READ_ONLY_API_KEY` and states read-only "is not a preference, it is
the requirement" — anticipating a project-held restricted key whose scope this
project chooses. But `stripe_api_write` (`C-030`) is present as a **connector** tool.
If that connector is authorized, payments-API write access is reachable with no
variable in `.env`, at a scope chosen by whoever granted the connector. The control
anticipates the wrong delivery mechanism. Same shape for Gmail against
`EMAIL_PROVIDER_API_KEY` and for the CRM placeholder.

**5. `Artifact` and the private-repository control govern the same asset under
different rules.** `D-030` records that private "is not optional." `Artifact`
publishes repository content to a `claude.ai`-hosted page with no owner action.
`Artifact` is additionally an **ingress**: `action: "list"` with `scope: "shared"`
or `"all"` enumerates artifacts other people shared with the operator, and the
tool's own description states those titles are untrusted text written by other
users. The registry captured the egress; the ingress was not connected to the
cross-project finding.

**6. Skill and tool descriptions are untrusted content occupying a stronger position
than anything `BOUNDARIES` §6 enumerates.** Every item in §6 is content an agent
*chose to fetch*. Skill descriptions, tool descriptions, and MCP server instruction
blocks are loaded automatically into every session before any agent decides anything.
`Ev §7` records one instance (`bright-data-mcp`, `C-121`). **Two more are observable
in this Security Reviewer's own session context and had not been recorded:**
- The `claude-in-chrome` MCP server ships an instruction block directing the agent
  to load its browser tools via `ToolSearch` and to batch them into one call —
  server-supplied text prescribing use of the single control point for the whole
  deferred surface, on behalf of the highest-severity capability in the inventory.
- The `claude-api` skill description carries an imperative TRIGGER / SKIP protocol
  specifying when the agent must read a file and which command to run first.

Conclusion: this is the norm on this surface, not a defect in one plugin.

**7. `ToolSearch` is not a single control point, and nothing enforces it.** Three
findings (`SKILL_SECURITY_POLICY.md` §9): it is per-agent-context and the parent
cannot observe a child's loads; it is keyword-driven, so a broad query can surface a
prohibited tool as a side effect; and `D-003` assigns permission enforcement to
deterministic code, of which **none exists**. The rule is decidable but not
enforceable. The only real enforcement is harness-level permission rules, which this
project cannot write (`D-032`, `BOUNDARIES` §1, `F-00-09`) — operator action only.

**8. `Bash` defeats the `Explore` / `Plan` "read-only" grant entirely.** The registry
notes these types can execute shell commands; stated concretely: shell redirection
writes files, `rm` deletes them, `git push` and `curl` reach the network. A subagent
described as read-only can create, overwrite, destroy, and egress. `ToolSearch`
separately defeats every deferred exclusion. **A subagent's tool-grant list is not a
security boundary.**

**9. `Ev §0` Limit 4 is verified, not hypothetical.** The deferred-tool list
disclosed to this Security Reviewer subagent is **not identical** to the primary
session's list in `Ev §2.1` — several orchestration tools the primary session listed
(the cron family, `DesignSync`, `PushNotification`, `RemoteTrigger`, most of the
`Task*` family, the plan-mode pair) are absent here. The difference runs toward
*fewer* tools, which is harmless in itself, but it establishes that **the registry's
row set is context-dependent, not machine-wide.** This is direct evidence from my own
context; nothing was invoked to obtain it. Consequence: a subagent must not infer
permission from the registry's completeness, and `R-0` (unlisted ⇒ DENY) must apply
inside subagents.

**10. Corroboration of the evidence file, obtained without invoking anything.** My
own session context independently discloses: the same 23 auth-required servers as
`Ev §3`; `plugin:firebase:firebase` absent from that list, consistent with
"connecting"; the same 13 subagent types as `Ev §4` with the same six exclusions for
`Explore`; `Artifact`, `mcp__ccd_session__*`, `mcp__Claude_Browser__*`, and
`mcp__visualize__*` loaded as in `Ev §1`; and the `Ev §2.2` server UUIDs unchanged.
`SESSION_CAPABILITY_INVENTORY.md` is accurate for this machine at this moment, on the
points I could check from my own disclosure.

**11. Five governance-modifying capabilities, ranked by severity** with reasons
(`SKILL_SECURITY_POLICY.md` §5). `update-config` (`C-085`) is worst: it writes hooks,
which execute outside any agent's decision loop and outside any phase, persist into
every future session, and — because `.claude/settings.local.json` is git-ignored per
`D-032` — leave **no trace in the repository at all**. `refresh-brand-context`
(`C-116`) is most insidious: a third-party advertising plugin documented as updating
`CLAUDE.md`, the file every agent must read first. That is a supply-chain path into
this project's directive layer.

**12. The `Rough-Draft-Builders-Club` collision is a vocabulary mismatch.**
`BOUNDARIES` §1 and §2 are written in the vocabulary of **paths**; `C-052` and
`C-044` reach the same content by **provenance** with no path involved, and nothing
in `task_plan.md`'s V-10 attestation would catch it (it is a read, and it has no
path). My response is a narrowing permitted by `BOUNDARIES` §7.4: restate the
prohibition as content-scoped — no content originating from that repository may enter
this project **by any route** — which forbids everything the current rule forbids plus
the additional routes. It widens nothing. Recommended for owner ratification into
`BOUNDARIES` §2 (`SKILL_SECURITY_POLICY.md` §6.3, rule P-4).

**13. All 22 "prohibited today, plausibly relevant later" rows are accounted for** in
`CONNECTOR_ACTIVATION_PLAN.md` §3, grouped G1–G8 by need. `C-045` (G8) is the one
group with **no activation path recommended**, because none of the plan's
preconditions would even engage against a capability that uses no credential.

## Assumptions

`F-00-05` records that a specialist's claim of "no assumptions" carries no
evidentiary weight, so this section is written to be challenged.

1. **`CAPABILITY_REGISTRY.md` was accepted by the Phase 02 Owner**, as my assignment
   states. **No file I can read records that acceptance.** The registry's header still
   reads *"DRAFT for the Phase 02 Owner to integrate. Not yet an integrated
   deliverable,"* and its Axis 3 disposition vocabulary still reads *"`PROPOSED` by
   the Skill Auditor and requires the Phase 02 Owner's acceptance."* I proceeded on the
   vocabulary as assigned. If the acceptance is real, those two passages are stale; if
   it is not, both my deliverables were written against an unaccepted draft — the
   `F-00-07` failure mode. Flagged in `SKILL_SECURITY_POLICY.md` §10 disagreement 8.
2. **`SESSION_CAPABILITY_INVENTORY.md` is an accurate transcription**, and the
   `Ev §2.2` server identifications (Stripe, Supabase, Gmail, Calendar, remote runner)
   are correct. I corroborated what my own context discloses (fact 10) but could not
   re-derive the rest without invoking capabilities. A misidentification would change a
   rule basis; in every case I checked it would not change a disposition, because each
   is denied on more than one ground.
3. **A skill's or tool's disclosed description reflects what it does.** I read no skill
   body — they live outside the project root. This is the weakest evidence I used and
   it most affects §5's severity ranking and rule `R-9`.
4. **"Reaches an external system" includes reaching it through the operator's browser
   or Claude account.** `BOUNDARIES` §3 does not define the term; §8 step 4 uses it as
   a stop condition. My reading is the stricter one, which `BOUNDARIES` §7.5 requires
   when a document and a situation appear to conflict — but it is a reading.
5. **Absence of a permission grant is a prohibition** (`D-008`, `BOUNDARIES` §8),
   applied throughout, including to capabilities that appear in no §3 row at all.
6. **The `/mcp` and `claude mcp` entry points named in §7.2 of the activation plan are
   real** — they were disclosed to this session by the harness itself, not recalled by
   me. I deliberately did **not** state any subcommand or flag, and instructed the
   operator to confirm syntax from the product's own help output. UI labels in §7 may
   drift; the plan names destinations, not exact strings.

## Open questions

1. **Is `CAPABILITY_REGISTRY.md` accepted?** Assumption 1. Needs closing before the
   gate report, either by updating the header and Axis 3 or by correcting my premise.
2. **`docs/PROJECT_BOUNDARIES.md` §3 needs an owner decision, not an edit by me.**
   Three separate items: (a) the header/GitHub-row contradiction; (b) the definition
   of `NOT CONNECTED` (credential-provenance, not reachability); (c) a second status
   axis, `REACHABLE WITHOUT PROJECT CREDENTIAL: YES / NO / UNRESOLVED`. `task_plan.md`
   assigns §3 to the Phase 02 Owner, so I did not touch it. `CLAUDE.md` §6 forbids
   silently changing approved architecture.
3. **Should the provenance restatement (`SKILL_SECURITY_POLICY.md` §6.3 P-2) be
   ratified into `BOUNDARIES` §2?** It binds only within my scope today. It is a
   narrowing, so §7.4 permits it; making it project-wide is §7.1 territory — owner only.
4. **Should the pre-authorization rule become a standing decision row?**
   `CONNECTOR_ACTIVATION_PLAN.md` §6 proposes the text. I did not assign an ID —
   `DECISIONS.md` ends at `D-035` and the Phase 02 Owner assigns numbers.
5. **Has any connector already been authorized, and when?** Unanswerable from inside
   this project without using the connector, which `BOUNDARIES` §8 step 4 forbids.
   `CONNECTOR_ACTIVATION_PLAN.md` §7 is the operator-side procedure. Note the specific
   sub-question in G7: if a Google connector is live, the project could simultaneously
   hold "no confirmed Drive access" (`Q-004`, `BLOCKED`) and a live Google grant. **I
   assert neither state.**
6. **Should the Project Owner set harness-level deny rules** for
   `mcp__claude-in-chrome__*`, `Artifact`, the scheduling family, and the remote job
   runner while working in this project? That is the only enforcement mechanism that
   does not depend on an agent choosing to comply, and only the operator can set it
   (`D-032`, `BOUNDARIES` §1). Recommended, not granted, not performed.
7. **`task_plan.md` forward-references five identifiers that do not exist.** It cites
   `D-036`, `Q-012`, `Q-013`, `Q-014`, and `R-20`. `DECISIONS.md` ends at `D-035`,
   `OPEN_QUESTIONS.md` at `Q-011`, `RISK_REGISTER.md` at `R-19`. This is the same
   defect class the Skill Auditor flagged in `SESSION_CAPABILITY_INVENTORY.md` (its
   open question 6), and nobody has named this instance. `F-01-08` is the governing
   lesson: a file must not describe as existing something that does not. I own none of
   these files and edited none of them.
8. **Nothing enforces any of this.** 83 of 141 registry rows are `PROHIBITED` and
   every rule in my policy is compliance-based except §5 G-4 (the pre-commit `git
   diff` check on governance files, which is genuinely deterministic). `D-003` says
   deterministic code enforces permissions. **No such code exists and Phase 02 builds
   none.** Whether that gap is acceptable through Phase 03 is the owner's call.

## Work completed

- Read all nine required inputs plus `RISK_REGISTER.md`, `NON_GOALS.md`,
  `task_plan.md`, and the "Human checkpoints" list, before writing anything.
- Wrote `SKILL_SECURITY_POLICY.md`: explicit scope and a table of the seven things it
  does **not** decide with their Phase 03 owners; an eleven-test ordered decision
  procedure reaching ALLOW / DENY / ESCALATE with default DENY; deny-by-default and
  the exactly-two things that override it; the credential-free access analysis with a
  justified verdict on `BOUNDARIES` §3 and a recommended repair; the untrusted-content
  rule extended to skill bodies, tool descriptions, and server instruction blocks with
  three evidenced instances; four rules protecting governance files including one
  deterministic detection control; a provenance-scoped narrowing of the
  `Rough-Draft-Builders-Club` prohibition; recording requirements and five review
  triggers; seven subagent rules; four `ToolSearch` rules with an honest statement of
  their limit; eight recorded disagreements with the registry; and its own rollback.
- Wrote `CONNECTOR_ACTIVATION_PLAN.md`: an unmissable non-authorization banner; eight
  universal preconditions with their current status; all 22 relevant-but-prohibited
  rows grouped G1–G8 by need with per-group gates and ceilings; an eleven-step ordered
  activation sequence naming the performer of each step and why; a seven-step
  deactivation sequence stating that only provider-side revocation is real
  deactivation; the pre-authorization record requirement with the required row fields;
  a beginner-oriented "How the owner verifies this themselves" covering three separate
  surfaces; and a "what this plan does not establish" section.
- Recorded the disagreements with `CAPABILITY_REGISTRY.md` rather than silently
  ratifying it (`D-006`).
- Narrowed only. Widened nothing (`BOUNDARIES` §7.2, §7.4).

## Files changed

| File | Change |
|---|---|
| `SKILL_SECURITY_POLICY.md` | Created |
| `CONNECTOR_ACTIVATION_PLAN.md` | Created |
| `agent_runs/phase-02/handoffs/HANDOFF_SECURITY_REVIEWER.md` | Created. This file |

**No other file was created, edited, or deleted.** In particular I did not write
`CAPABILITY_REGISTRY.md`, `docs/PROJECT_BOUNDARIES.md`, `DECISIONS.md`,
`findings.md`, `OPEN_QUESTIONS.md`, `RISK_REGISTER.md`, `progress.md`,
`CURRENT_PHASE.md`, `task_plan.md`, `.env.example`, `.gitignore`,
`SESSION_CAPABILITY_INVENTORY.md`, `SKILL_INSTALLATION_PLAN.md`, or any harness
configuration. Each has a different owner; `F-00-09` records a Phase 00 subagent
writing outside its scope.

## Tests run

**No capability was invoked, and none could have been without failing the phase.**

- **No skill was invoked.** The `Skill` tool was not called.
- **`ToolSearch` was not called.** No deferred tool's schema was loaded, so no
  deferred tool was ever callable in this context.
- **No MCP tool, connector, or plugin was invoked, loaded, enabled, installed,
  authenticated, or tested.** No `mcp__*` tool was called.
- **No subagent was spawned.** The `Agent` tool was not called.
- **`Artifact` was not called**, in any mode, including `action: "list"`.
- **Nothing was installed and no configuration was written.**
- **No path outside the project root was read** — no `C:\Users\crone\.claude\`, no
  `C:\Users\crone\Projects\Rough-Draft-Builders-Club`. No read, no listing, no stat,
  no timestamp. Per `F-01-07`, I designed no check that would have required one.

**What was executed, in full:** `Read` against 12 project files; one `Grep` against
`user-guide/`; and three `Bash` commands, all read-only and all inside the project
root:

| Command (abbreviated) | Purpose | Actual result |
|---|---|---|
| `grep -rln "D-036\|Q-012\|Q-013\|Q-014\|R-20\|F-02-01" --include="*.md" .` | Locate the forward-referenced IDs | Two files: `task_plan.md` and `HANDOFF_SKILL_AUDITOR.md`. **Confirms open question 7** — none of the five IDs appears in any register |
| `ls -la` + `ls -R agent_runs/phase-02` | Confirm which Phase 02 artifacts existed before I wrote | Root listing; `agent_runs/phase-02/evidence/SESSION_CAPABILITY_INVENTORY.md` and two handoffs. Neither of my deliverables existed |
| `grep -oh` ID extraction + secret-shaped pattern scan over my two deliverables | Mechanical self-check, run **before** handing off, per `F-00-04` | See below |

**Mechanical self-check results, with the `F-01-04` caveat applied.**

- **Cross-reference integrity.** Every ID cited in my two files was extracted and
  checked against its register by hand. `D-` ids used: `D-001`, `D-003`–`D-011`,
  `D-013`, `D-016`, `D-016a`, `D-020`, `D-025`–`D-027`, `D-030`, `D-032`, `D-035` —
  all defined, all ≤ `D-035`. `Q-003`–`Q-009` — all defined. `R-05`, `R-10`, `R-12`,
  `R-14`, `R-18` — all defined. `NG-001` — defined. `F-00-07`, `F-00-09`, `F-01-02`,
  `F-01-06`, `F-01-07` — all defined. 61 distinct `C-` ids, all within `C-001`–`C-141`
  and each resolving to a real registry row. **I deliberately cited no ID above the
  current end of any register.**
- **Secret-shaped content.** A pattern scan over both deliverables for common key
  prefixes, PEM headers, bearer tokens, and `key=`/`secret=` assignments returned **no
  matches**. **This is a detection result, not a guarantee** — finding none means none
  were found. Neither file contains any value, real or example-shaped.
- **`F-01-04` caveat, stated rather than glossed.** My ID-extraction command is
  unverified code. It reports what its regexes match; a citation written in a form my
  pattern does not match would not have been checked. I did not exercise the checker
  against a case it should fail. **Treat this as a partial check that found nothing,
  not as proof of correctness.** The Phase 02 Owner's `T-09` mechanical sweep should
  cover these two files independently.

## Failures or risks

1. **Nothing enforces this policy.** Its only deterministic control is the pre-commit
   `git diff` check on governance files (§5 G-4). Every other rule depends on an agent
   choosing to comply, and `D-003` says deterministic code should be doing this work.
   Phase 02 builds none. This is the largest single limitation of the deliverable and
   it is structural, not a drafting flaw.
2. **The policy is snapshot-dependent.** It names capabilities from a 2026-07-29
   session on one machine. Rule `R-0` (unlisted ⇒ DENY) is written to keep it
   fail-closed against drift, but a rule the operator's plugin manager cannot see is
   not a control on the operator's plugin manager.
3. **`CONNECTOR_ACTIVATION_PLAN.md` §7 depends on product UI and CLI surfaces I
   cannot verify from here.** I named destinations and told the operator to confirm
   labels and command syntax from the product's own help output rather than fabricate a
   flag. If a menu is renamed, §7 degrades to "look for the section that does this,"
   which is the intended failure mode.
4. **If assumption 1 is wrong, both deliverables cite an unaccepted vocabulary.**
   Rework would be real: the disposition tokens appear throughout both files. This is
   the `F-00-07` sequencing risk and it is the phase owner's to close.
5. **My severity ranking of the governance-modifying capabilities rests on
   descriptions I did not verify** (assumption 3). If `update-config`'s hook capability
   is narrower than described, §5's ranking is too harsh; if broader, too lenient. The
   prohibition holds either way, so the risk is to the *reasoning*, not the outcome.
6. **The `BOUNDARIES` §3 finding is stated but not fixed.** I own neither that file
   nor `DECISIONS.md`. A reader who consults §3 tomorrow still meets a header sentence
   its own table contradicts. Escalated in open question 2; unresolved until the phase
   owner acts.
7. **I recommended harness-level deny rules I cannot implement or verify.** If the
   owner adopts them, nothing in this repository confirms they took effect — the file
   is git-ignored. The verification is the operator's, in `CONNECTOR_ACTIVATION_PLAN.md`
   §7.
8. **This work sits in the git worktree**
   `.claude/worktrees/phase-02-capability-registry-c04753`. Both deliverables exist
   there and not on `main` until merged. Phase 01's residual risk applies: the
   off-machine mirror is only as current as the last push.

## Recommended next action

**For the Phase 02 Owner, in this order:**

1. **Close the registry-acceptance ambiguity** (assumption 1 / open question 1) before
   the independent reviewer sees the file set. Either update
   `CAPABILITY_REGISTRY.md`'s header and Axis 3 to reflect acceptance, or tell the
   downstream specialists their premise was wrong.
2. **Fix `docs/PROJECT_BOUNDARIES.md` §3's header sentence**, which its own GitHub row
   contradicts. This is a factual correction to a file the phase owner owns, not a
   boundary change, and it is the cheapest item on this list.
3. **Open a `DECISIONS.md` row for the `NOT CONNECTED` definition** — credential
   provenance, not reachability — plus the recommended second status axis. The
   recommended wording is in `SKILL_SECURITY_POLICY.md` §3.1.
4. **Open a `DECISIONS.md` row for the pre-authorization requirement**
   (`CONNECTOR_ACTIVATION_PLAN.md` §6). Text supplied; ID unassigned.
5. **Carry these into `findings.md` as Phase 02 findings:** the credential-free access
   classes; the `.env.example` / Stripe-connector delivery-mechanism mismatch; the
   `Artifact` conflict with `D-030`; skill and server descriptions as automatically
   loaded untrusted content, with the two newly recorded instances; `Bash` defeating
   the read-only subagent grant; and the verified context-dependence of the capability
   surface (fact 9).
6. **Carry `C-045` into `RISK_REGISTER.md` as a new risk**, and consider whether
   `R-14`'s access-control framing should widen from repository access to capability
   access. `R-18` (connectors change between selection and use) is also directly
   implicated by the staleness problem.
7. **Fix the five forward-referenced IDs in `task_plan.md`** (open question 7) —
   either write the rows or change the citations. Do it before the reviewer finds it.
8. **Run `T-09`'s mechanical sweep over my two files independently.** My self-check
   found nothing but was not exercised against a case it should fail (`F-01-04`).
9. **Do not begin Phase 03** (`D-007`).

**For the Project Owner, three questions worth asking early:**

- **Which connectors are actually authorized on your Claude account?** This project
  cannot find out without using them, which its own rules forbid.
  `CONNECTOR_ACTIVATION_PLAN.md` §7 walks through it in about ten minutes.
- **Should Claude in Chrome and `Artifact` be denied at the harness level while you
  work on this repository?** They are the two paths that reach outside this project
  without any credential it controls, and only you can turn them off.
- **Is a compliance-based control model acceptable through Phase 03?** Today 83 of
  141 registry rows are prohibited and nothing but an agent's cooperation enforces a
  single one.
