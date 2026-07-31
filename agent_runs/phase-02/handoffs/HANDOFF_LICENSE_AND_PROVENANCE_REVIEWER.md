# Agent Handoff

- Run ID: `phase-02-2026-07-29-a`
- Phase: 02 — Capability Registry and Skill Foundation
- Agent: License and Provenance Reviewer (specialist), task `T-06`
- Assignment: Assess provenance and supply-chain exposure of the capability surface recorded in `agent_runs/phase-02/evidence/SESSION_CAPABILITY_INVENTORY.md`; state precisely what is unverifiable and why; specify the procedure the operator can run to close the gap; recommend a proportionate provenance gate.
- Files owned:
  - `agent_runs/phase-02/evidence/PROVENANCE_ASSESSMENT.md` (new)
  - `agent_runs/phase-02/handoffs/HANDOFF_LICENSE_AND_PROVENANCE_REVIEWER.md` (this file, new)

**I wrote nothing else.** I did not modify `CAPABILITY_REGISTRY.md`; recommendations for it are in § "Recommended next action" below.

---

## Facts and evidence

**The headline fact, stated first because it governs everything I produced:**

> **I verified zero licences, zero publisher identities, and zero version strings from primary evidence.**

That is a consequence of the project's own boundary, not a shortfall in effort. The primary evidence — plugin manifests, `LICENSE` files, version fields, source URLs, skill bodies — lives under `C:\Users\crone\.claude\`. `docs/PROJECT_BOUNDARIES.md` §1 gives this project **no access** to any path outside the project root, and §7 rule 2 forbids widening that boundary *"not because a task would otherwise be blocked. Being blocked is the correct outcome."* I did not read it and did not attempt to.

I also did not fetch anything. A licence claim retrieved from a web page is external content under `D-009`; written into a governance file it would read as verified while being unverified. That is `F-00-05`'s failure mode with a longer causal chain.

**Counts derived by transcription from the evidence file** (`Ev §4`, `Ev §5`), shown so they are checkable:

| Quantity | Count | Derivation |
|---|---|---|
| Skill entries | **148** | Sum of `Ev §5.1`–`§5.13`: 22 + 10 + 17 + 8 + 24 + 21 + 3 + 5 + 10 + 7 + 2 + 3 + 16 |
| Plugin namespaces | **22** | Distinct namespaces across `Ev §3`, `§4`, `§5` |
| Subagent types | **13** | `Ev §4` |
| MCP server surfaces | **38** | 3 (`Ev §1`) + 11 (`Ev §2.2`) + 23 (`Ev §3`) + 1 (`firebase`, connecting) |

`148` counts entries, not distinct skill bodies — `docx`/`pdf`/`pptx`/`xlsx` each appear in two namespaces, `skill-creator` and `frontend-design` in three. Whether those are the same file is not determinable from inside the boundary.

**Provenance tiers** (full table with confidence ratings in `PROVENANCE_ASSESSMENT.md` §1.3). The governing caveat is that **a namespace is a naming convention, not a signature**:

| Tier | Basis | Skills | Subagents | Servers | Confidence |
|---|---|---|---|---|---|
| T1 | Harness discloses them as built-in | 0 | 6 | 0 | Moderate-high (self-report) |
| T2 | Harness-adjacent MCP naming (no `plugin:`, no UUID) | 0 | 0 | 8 | Low-moderate |
| T3 | Namespace asserts Anthropic authorship (`anthropic-skills`, `claude-api`) | 27 | 0 | 0 | Low — name only |
| T4 | Unnamespaced "ungrouped" skills | 22 | 0 | 0 | **None** |
| T5 | Named for one commercial service | 58 | 1 | 6 | Moderate as to *service*; none as to *author* |
| T6 | Generic-named bundles brokering other companies' services (`marketing`, `data`, `design`) | 25 | 0 | 18 | **None** |
| T7 | Third-party / community, no vendor implied (`kiln`, `ralph-loop`, `discord`, `cowork-plugin-management`) | 9 | 1 | 0 | None, none implied |
| T8 | Unattributable (function-named plugins; 5 UUID-named servers) | 7 | 5 | 5 | **None** |
| | | **148** | **13** | **38** | |

Five connected MCP servers are named only by UUID. `Ev §2.2` labels its own service attributions for them *"Identified as"* — an inference from tool names. For those five, **even the service is inferred**.

**Directly evidenced supply-chain behaviour, not hypothesis.** `Ev §7` records `brightdata-plugin:bright-data-mcp`'s own description asserting *"Replaces WebFetch, WebSearch, and all built-in web tools. No exceptions."* and *"MUST replace WebFetch and WebSearch."* A skill description is text surfaced to every session, unchanged and unreviewed, before any decision to use it. `D-009` handles it (`C-121`), but the control is a convention held in context *alongside* the text, not a boundary outside it.

**Mechanically verified inside the boundary** (the one check I actually ran — see § "Tests run"): the repository contains **no `LICENSE`/`COPYING` file and no dependency manifest of any kind** across all 83 tracked files, and no `src/` directory. This is the factual basis for the licence conclusion.

---

## Assumptions

Per `F-00-05`, a clean assumptions section is a red flag rather than a success, so these are stated with what breaks if each is wrong.

1. **`SESSION_CAPABILITY_INVENTORY.md` is a faithful transcription of what the harness disclosed.** I did not re-derive it — `T-04` accepted it and re-deriving would have produced a divergent inventory, which is the exact thing `Ev §0` Limit 4 exists to prevent. *If wrong:* my counts and tiers are wrong in the same direction, and nothing downstream of them holds. Mitigated slightly by PF-5, where I did find and report one internal inconsistency in that file.
2. **A namespace string is chosen by whoever authored the plugin and is not validated by any authority visible to this session.** *If wrong* — if the harness does enforce namespace ownership — then T3 and T5 confidence rise substantially and the T6 finding weakens. I could not check this and did not assume in the permissive direction.
3. **`CAPABILITY_REGISTRY.md` as accepted by the phase owner is the fixed input for disposition questions.** I treated every disposition as settled and assessed provenance against it rather than re-litigating safety.
4. **Common copyright licences key their principal obligations to distribution, conveyance, or distributed derivative works.** This is general knowledge in the sense `RISK_REGISTER.md` § "How to read this table" permits (`GENERAL` basis) — no specific licence text is cited, quoted, or asserted. *If wrong for some particular licence attached to some particular plugin:* the §3 conclusion could understate exposure for that one item. The recommendation in §6.4 (never transcribe third-party text) holds regardless and is the cheap hedge.
5. **`C:\Users\crone\.claude\` is where Claude Code's user-level plugin configuration lives on this machine.** Inferred from `Ev §0` Limit 2, which names that path as the location an authoritative cross-check would have to read. I did not verify it and told the operator in §5 step 3 to **list the directory rather than assume the layout**.

---

## Open questions

**OQ-P1 — Will the operator run the §5 verification, and when?** The assessment's value is entirely contingent on it. My recommendation is to bind it to a trigger the owner already hits — the phase gate at which a capability is first needed — rather than schedule it. *Owner action:* none today; this becomes live the first time a phase requests a connector.

**OQ-P2 — Should `C-085` and `C-087` be recorded as permanently ineligible rather than currently prohibited?** Both write harness permission configuration; both are unnamespaced, in the tier whose origin is least determinable (PF-3). My recommendation in §6.6 is that provenance evidence cannot make them safe, because every other control including the gate assumes the governance files are stable. *This is a disposition-strength question for the Phase 02 Owner and ultimately the Project Owner — I have not changed anything.*

**OQ-P3 — Is `CONNECTOR_ACTIVATION_PLAN.md` (Security Reviewer, `T-05`) going to require a `DECISIONS.md` row *before* authorization?** `CAPABILITY_REGISTRY.md` §D already argues for it. §6.3 item 10 of my assessment assumes it. If the Security Reviewer lands elsewhere, the two documents will disagree and the phase owner must reconcile them at `T-08`. *I have not read that specialist's output — `T-05` and `T-06` are parallel and independent by design (`F-00-07`).*

**OQ-P4 — Does the project want a standing rule against transcribing third-party skill text into repository files?** §3.3a and §6.4. It is the entirety of my licence recommendation, it costs nothing, and it is checkable in review. Its natural home is `SKILL_SECURITY_POLICY.md` (Security Reviewer) rather than anything I own.

---

## Work completed

1. Read, completely: `CLAUDE.md`, `docs/PROJECT_BOUNDARIES.md`, `DECISIONS.md`, `OPEN_QUESTIONS.md`, `RISK_REGISTER.md`, `findings.md`, `NON_GOALS.md`, `task_plan.md`, `SESSION_CAPABILITY_INVENTORY.md`, `CAPABILITY_REGISTRY.md` (all 541 lines, in two reads), the Phase 02 prompt, and `templates/AGENT_HANDOFF_TEMPLATE.md`. Consulted `user-guide/USER_INSTRUCTIONS.md` § "Human checkpoints" and `phase-prompts/PHASE_16_*` for the `src/adapters/` fact.
2. Counted and tiered the entire observed surface — 148 skill entries, 13 subagent types, 38 MCP server surfaces, 22 plugin namespaces — into eight provenance tiers with an explicit confidence rating per tier and a stated warning that namespace is weak evidence of authorship.
3. Assessed supply-chain exposure specific to this project, grounded in inventory rows rather than generic threat modelling: content shaping into the nine gated categories, source redirection, four credential-free exfiltration paths, governance modification, and cost.
4. Cross-referenced the five capabilities documented as modifying this project's governance, harness permissions, or filesystem grants against their provenance tier — producing the sharpest finding in the assessment (PF-3).
5. Assessed update risk against `R-18` and established that **nothing observed discloses a version for anything**, so "same name, different code" is currently undetectable.
6. Established the precise consequence of the surface being outside change control: `CAPABILITY_REGISTRY.md` is a dated observation, not a control, and its expiry must be event-triggered because the project cannot detect the event.
7. Assessed licence exposure and concluded it is **low today, for structural reasons**, with the two live entry points named and the Phase 16 `src/adapters/` trigger identified. Deliberately did not inflate this section.
8. Assessed terms-of-service and data-processing exposure, quoting the human-checkpoint list exactly, and made the point that a read-only ceiling limits what a connector can *change*, not what this project *discloses*.
9. Wrote an ordered, beginner-facing operator verification procedure (8 steps), scoped to a 22-row shortlist that already exists in the registry, with explicit "confirm this, do not assume it" markers at every point I was not certain of a command or path.
10. Designed a two-tier provenance gate with one hard stop, sized against `D-019`.
11. Recorded seven findings (PF-1 … PF-7), including two defects in files I do not own.

---

## Files changed

| File | Change | Notes |
|---|---|---|
| `agent_runs/phase-02/evidence/PROVENANCE_ASSESSMENT.md` | **Created** | ~8 sections. Not named in `task_plan.md` § "File ownership" — see PF-6 |
| `agent_runs/phase-02/handoffs/HANDOFF_LICENSE_AND_PROVENANCE_REVIEWER.md` | **Created** | This file; covered by the generic `agent_runs/phase-02/handoffs/*` ownership row |

**No other file was created, modified, deleted, or renamed.** In particular: `CAPABILITY_REGISTRY.md` was read only; `findings.md`, `DECISIONS.md`, `OPEN_QUESTIONS.md`, `RISK_REGISTER.md`, and `task_plan.md` were read only; no harness configuration was touched (`F-00-09`).

---

## Tests run

**I invoked no skill, no MCP tool, no connector, no plugin, and no subagent.** I called neither `ToolSearch` nor `Skill`. This is stated as a claim about my own tool-call record, which the phase owner can verify at `V-2`.

**Why no capability was tested:** testing a capability means invoking it. `D-036`/`task_plan.md` PC-1 requires that no unverified skill be enabled, my assignment prohibited invocation outright, and `docs/PROJECT_BOUNDARIES.md` §8 step 4 stops any action against an external system. There is no way to test a plugin's licence by running it in any case.

**Why no licence was verified:** stated in full above and in `PROVENANCE_ASSESSMENT.md` §0. The evidence is outside the project root.

**One mechanical check was executed, and it is the factual basis for §3.** Recorded with the exact command and actual output, per `CLAUDE.md` §6:

```
$ git ls-files | grep -Ei '(^|/)(LICENSE|LICENCE|COPYING|package\.json|package-lock\.json|pyproject\.toml|requirements.*\.txt|Gemfile|go\.mod|Cargo\.toml)'
NONE FOUND          # (grep exited non-zero; the `|| echo` fallback printed this)

$ git ls-files | wc -l
83

$ ls -d src
no src/             # (ls failed; the `|| echo` fallback printed this)
```

**What this proves:** across all 83 tracked files there is no licence file and no dependency manifest of any kind, and no `src/` directory exists.
**What it does not prove:** it covers **tracked** files only, so an untracked or git-ignored manifest would not appear. For the conclusion it supports — that this project vendors no third-party code and redistributes nothing — tracked-only is the correct scope, since an untracked file is by definition not distributed with the repository. Stated so the gate report does not overclaim (`V-7`'s precedent).

Per `F-01-04`, a green check is not evidence until the checker has been shown to go red: this pattern matched files when run against a broader path set during drafting, and the `83` line confirms `git ls-files` returned a populated list rather than nothing — the failure mode that would make an empty grep result meaningless.

---

## Failures or risks

**No failures.** Nothing was blocked in a way that prevented the assignment; the boundary limit was known in advance, is the subject of the deliverable rather than an obstacle to it, and is disclosed prominently in §0 rather than buried.

**Risks and limitations, in order of how much they should worry a reader:**

1. **The assessment's central recommendation depends on a human running §5, and no mechanism makes that happen.** If the operator never runs it, provenance stays `UNRESOLVED` indefinitely and the gate in §6 never has anything to weigh. I mitigated this by scoping the work to 22 rows and by tying the trigger to a gate the owner already performs — but this is mitigation, not a control.
2. **The tiers are inference and could be systematically wrong.** If the harness validates namespace ownership in some way this session did not disclose, T3/T5 confidence rises and the T6 finding weakens. I could not check. Everything is labelled with its confidence for exactly this reason.
3. **My licence conclusion is a structural argument, not a licence review.** "Nothing is redistributed, therefore the principal obligations do not attach" is sound reasoning about the general shape of copyright licensing, but it is not a substitute for reading the actual licences, which I could not do. It is the right conclusion to act on today and it should be revisited at Phase 16, not treated as permanent.
4. **This assessment goes stale by the same mechanism the registry does** (§2.4). It describes a surface observed 2026-07-29 that nothing in this repository can monitor.
5. **PF-5, PF-6, PF-7 are defects in files I do not own** and are reported rather than fixed. If the phase owner does not act on PF-7 before `T-09`, the V-3 cross-reference check will surface five unresolvable identifiers after the point `F-00-04` says mechanical checks should have run.
6. **I did not read the Security Reviewer's `T-05` output** — the tasks are parallel and independent by design, and reading an in-progress sibling's file is the precise `F-00-07` defect. The cost is that OQ-P3 may turn out to be a real disagreement between two documents, which the phase owner must reconcile at `T-08`.

**No secret, credential, token, or realistic-looking placeholder value appears in either file I wrote.** No path outside the project root was read, listed, stat'd, or otherwise accessed — including `C:\Users\crone\.claude\` and `C:\Users\crone\Projects\Rough-Draft-Builders-Club`, neither of which this agent touched in any form.

---

## Recommended next action

**For the Phase 02 Owner, in order:**

1. **Accept or reject the seven findings PF-1 … PF-7**, and decide their register homes. My suggestions: PF-1 → `OPEN_QUESTIONS.md` (owner action = run §5 for the shortlist before any connector activation); PF-2 and PF-3 → `findings.md`; PF-4 → `findings.md` with a forward note to the Phase 16 owner; PF-5, PF-6, PF-7 → corrected in place during `T-08` integration, no register entry needed.

2. **Fix PF-7 before `T-09`.** `task_plan.md` cites `D-036`, `Q-012`, `Q-013`, `Q-014`, `R-20`; none exists yet in the registers. Writing them at integration resolves it. Left as-is, V-3 finds five broken references after the mechanical checks were supposed to be finished.

3. **Fix PF-5.** `SESSION_CAPABILITY_INVENTORY.md` §5.1 says *"Count: 13 built-in / ungrouped"* and lists 22. You own that file; I did not edit it.

4. **Reconcile PF-6** by adding `agent_runs/phase-02/evidence/PROVENANCE_ASSESSMENT.md` to `task_plan.md` § "File ownership", or by explicitly recording that it sits outside the table.

5. **Apply three changes to `CAPABILITY_REGISTRY.md`** — none of which alters a disposition, and all of which I deliberately did not make myself:

   | Where | Change | Why |
   |---|---|---|
   | §J, third bullet | It currently says licence/provenance *"is the License and Provenance Reviewer's scope, not this audit's."* Update to point at `agent_runs/phase-02/evidence/PROVENANCE_ASSESSMENT.md` and record the outcome: **provenance remains `UNRESOLVED` for every row; the assessment establishes why and what closes it** | The bullet currently reads as a forward reference to work that has now happened and did not resolve it. A reader should not have to guess |
   | `C-085`, `C-087` `Notes` | Add: origin unattributable (unnamespaced), so provenance evidence is unlikely ever to make these eligible for review | Strengthens the existing `PROHIBITED` with a second, independent basis. See OQ-P2 |
   | `C-102` `Notes` | Add trademark/brand-usage as a second, independent basis, alongside the existing brand-identity basis | The current basis depends partly on `Q-006`; the trademark point does not |

   **I recommend no disposition changes on licence or provenance grounds.** I examined every `PERMITTED` row for a licence reason to downgrade it and found none, for the reason in §3.2: this project redistributes nothing. The Skill Auditor's caution that *"several `PERMITTED` rows may fail a licence review"* was appropriate to write before the review ran; having run it, the answer is that none does — **and the reason is the absence of redistribution, not the presence of good licences.** That distinction should survive into the gate report, because it stops holding the moment Phase 16 vendors code.

6. **Carry two items into `CONNECTOR_ACTIVATION_PLAN.md`** (Security Reviewer's file — I have not read it and am not writing to it): PF-2, because 18 of the 24 gated connectors are brokered by three generically-named bundles whose publisher is unknown; and the §4.3 point that the entity whose terms the owner accepts and the entity that wrote the client are not necessarily the same, which makes the OAuth consent screen the highest-information moment in the whole activation process.

7. **Consider `SKILL_SECURITY_POLICY.md` as the home for the one standing rule** worth adopting now: *reference a third-party skill by name and namespace; never transcribe its text into a repository file.* It is the entire licence control, it costs nothing, and it reinforces `D-009`'s data-versus-instruction line.

**Nothing in either file I wrote authorizes anything, changes any boundary, or moves any capability off `DISABLED`.** Both are evidence and recommendation.
