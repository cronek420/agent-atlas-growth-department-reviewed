# Open Questions

Prepared by: Requirements Analyst (Phase 00)
Phase: 00 — Decision Lock and Scope Control
Project: Agent Atlas Growth Department (for Rough Draft Builders Club)
Date: 2026-07-28

Every item below is `UNRESOLVED` or `BLOCKED` per the classification rules in the Phase 00 mandate. None of these are guessed or defaulted — each requires explicit Project Owner input before later phases can rely on it. Each entry lists: the question, why it matters, what a resolution unblocks, and the exact action the owner needs to take.

Q-008 through Q-011 were added by the Phase 00 Owner in response to Independent Reviewer Findings 6, 7, and 3 — material unknowns that had been flagged inside `RISK_REGISTER.md` or surfaced in review but were recorded in no owner-facing question.

---

### Q-001 — Final priority ranking among the three candidate 90-day objectives
**Status:** UNRESOLVED

**Question:** Among the three candidate goal areas the owner named — (a) leads/sales conversion, (b) audience/brand building, (c) community engagement — what is the relative priority for the next 90 days?

**Why it matters:** Content pillars (Phase 12), audience/offer modeling (Phase 09), platform scoring weights (Phase 10), and the weekly executive summary (Phase 19) all need a priority signal to decide what "success" looks like and what gets built first. Without it, later phases would have to guess or build for all three equally, which conflicts with the owner's stated low-time-budget constraint.

**What resolution unblocks:** Phase 09 (audience/offer prioritization), Phase 10 (platform scoring weights), Phase 12 (content pillar allocation), Phase 19 (what the weekly report highlights).

**Owner action required:** Reply with `1`, `2`, `3`, a staged hybrid (e.g. "2 for 60 days, then 1"), or your own phrasing. The options are fully drafted below — nothing further needs to be prepared before you can answer.
1. **Leads/sales-first:** Prioritize converting existing and near-term audience into qualified leads and sales; brand and community work is secondary and mainly in service of conversion.
2. **Brand/audience-first:** Prioritize building visibility, reach, and audience size/quality first, treating leads and community as downstream effects to focus on later once audience exists.
3. **Community-first:** Prioritize deepening engagement and trust with an existing or emerging community (e.g., current customers, local audience) before scaling reach or pushing conversion.
   *(A hybrid/staged answer — e.g., "brand-first for 60 days, then leads-first" — is also acceptable if the owner prefers a sequenced answer rather than a single ranking.)*

---

### Q-002 — Final platform rollout order and selection
**Status:** UNRESOLVED (deferred by design)

**Question:** Which platform(s) — from the candidate list (Facebook, Instagram, WhatsApp, TikTok) or others — will be launched, in what order, and on what timeline?

**Why it matters:** Social presence launch kits (Phase 11), content production (Phase 13), and publishing adapters (Phase 16) all depend on a confirmed platform set and sequence. The owner's four named platforms are directional interest only, not a locked decision.

**What resolution unblocks:** Phase 10 (Platform Strategy and Rollout Selection) itself, and every phase downstream of it (11, 12, 13, 16).

**Owner action required:** No action needed at Phase 00. This is intentionally deferred — Phase 10 will run a formal scoring process (audience fit, reach, intent, effort, risk, measurement) against the four named candidates plus any others the owner wants considered, and will present a recommended sequence for owner approval at that time. Flagging here only so the deferral itself is a recorded, deliberate decision rather than an oversight.

---

### Q-003 — Numeric targets and KPIs
**Status:** UNRESOLVED

**Question:** Are there any specific numeric targets (follower counts, lead counts, conversion rates, revenue figures, engagement rates, timelines) the owner wants the system to track toward?

**Why it matters:** Analytics/attribution (Phase 18) and executive reporting (Phase 19) need to know whether to build against explicit numeric targets or purely against directional/qualitative goals. Without this, the system cannot report "on track" vs. "off track" in any meaningful way.

**What resolution unblocks:** Phase 18 (analytics/attribution data model), Phase 19 (executive summary format and what it reports against).

**Owner action required:** Provide any numeric targets the owner already has in mind (even rough ones, e.g., "20 qualified leads/month" or "no specific number yet, just growth"), or explicitly confirm that no numeric targets exist yet and the system should track raw metrics without target comparisons for now.

---

### Q-004 — Google Drive folder location and access status
**Status:** BLOCKED

**Question:** Does a Google Drive folder already exist for this project's living documents, and if so, where, and what access (owner, editor, service-account) will the system have? If not, who will create it and grant access?

**Why it matters:** Phase 05 (Google Drive Living-Document Control Center) cannot design folder structure, permissions, or sync contracts without knowing whether it is creating something new or working within an existing structure, and without confirmed access.

**What resolution unblocks:** Phase 05 in its entirety, and any later phase that mirrors data to Docs/Sheets (Phase 15 approval queue, Phase 19 reporting).

**Owner action required:** Confirm (a) whether a Drive folder already exists for this project, (b) its location/link if so, and (c) what Google account or service-account access will be granted, and when. If nothing exists yet, confirm the owner will create the top-level folder and grant access before Phase 05 begins.

---

### Q-005 — Existing social media account status
**Status:** UNRESOLVED

**Question:** Does Rough Draft Builders Club already have accounts on any of the candidate platforms (Facebook, Instagram, WhatsApp, TikTok) or others? If so, who has login access, and what is their current state (active, dormant, claimed, unclaimed)?

**Why it matters:** Phase 11 (Social Presence Launch Kits) needs to know whether it is preparing new-account launch materials or auditing/relaunching existing accounts — these are materially different workflows with different risk profiles.

**What resolution unblocks:** Phase 10 (platform scoring needs to know if switching costs exist for already-claimed handles), Phase 11 (launch kit type), Phase 16 (publishing adapter setup, which needs account credentials/access).

**Owner action required:** Provide an inventory of any existing accounts (platform, handle/URL, who has access, current activity level) or explicitly confirm no accounts currently exist.

---

### Q-006 — Brand asset source location
**Status:** UNRESOLVED

**Question:** Where do existing brand assets live (logo files, brand colors, fonts, product photos, prior marketing materials, style guides), if any exist?

**Why it matters:** Phase 07 (Brand and Creative System) must build an enforceable brand bible from validated, real assets — it is explicitly prohibited from inventing brand identity elements. Without a known source, Phase 07 would be blocked or forced to guess.

**What resolution unblocks:** Phase 07 in its entirety, and downstream content production (Phase 13) which depends on brand rules.

**Owner action required:** Point to where brand assets currently exist (a folder, a website, a prior designer's files, or "we have none yet and need to create them from scratch") so Phase 07 can validate against real material or explicitly scope a from-scratch creation task.

---

### Q-007 — Which specific files in the Rough-Draft-Builders-Club repository are "explicitly approved" as fact sources
**Status:** UNRESOLVED — **escalated by Phase 01: may block Phase 06's *start*, not merely its content**

> **Phase 01 escalation (2026-07-29).** Raised by the Repository Architect and confirmed by the Independent Setup Reviewer (Finding F-10).
>
> `docs/PROJECT_BOUNDARIES.md` §2 adopts the fail-closed reading of the user guide: reading is permitted for *explicitly approved* files, approval is a stated precondition, and **no file has been designated** — so the approved set is empty and the read pathway grants nothing in practice.
>
> Every Phase 06 deliverable (`COMPANY_PROFILE.md`, `PRODUCT_PROFILE.md`, `OFFER_CATALOG.md`, `APPROVED_CLAIMS.md`, `EVIDENCE_REGISTER.md`) is an assertion about Rough Draft Builders Club, **no alternative source is named anywhere in the plan**, and Phase 06's own pass conditions forbid inventing product facts. Phase 06 may therefore have no authorized source set to work from at all.
>
> **Not promoted to `BLOCKED`** — that is the Project Owner's call, Phase 06 is five gates away, and naming a file list resolves it cheaply. Recorded so Phase 06 does not discover it at the start line. Also carried into `MASTER_PLAN.md`.

**Question:** `user-guide/USER_INSTRUCTIONS.md` already permits this project to read *explicitly approved* source files from `C:\Users\crone\Projects\Rough-Draft-Builders-Club` (writes remain prohibited — see D-013). Which specific files or paths does the owner designate as approved sources of validated product/company facts for Phase 06 onboarding (e.g., product descriptions, pricing structure, service area)?

**Why it matters:** Phase 06 (Product and Company Onboarding) must build a validated product knowledge base "without inventing missing facts." The read pathway exists in principle, but no file has actually been designated as approved, so Phase 06 currently has an empty authorized source set and would be forced to gather everything by owner interview.

**What resolution unblocks:** Phase 06 (Product and Company Onboarding) — specifically, whether it can pull facts from the app repo and from which files, versus sourcing everything directly from the owner via interview/questionnaire.

**Owner action required:** Name the specific files or paths within `Rough-Draft-Builders-Club` that may be read as product/company fact sources (e.g., a README, a pricing config, a marketing copy directory), or confirm that none are approved and Phase 06 should gather all product/company facts directly from the owner instead.

---

### Q-008 — Backup approver / acceptance of the single-approver single point of failure
**Status:** ✅ **RESOLVED 2026-07-30 (`D-050`)**

**Resolution:** Option (c) — the single-approver structure is accepted as the standing operating constraint. No backup approver is named; no auto-pause timer is set. All gated work continues to halt on owner unavailability. The Project Owner delegated this choice to the Phase 03 Owner (`D-049`); options (a) and (b) were not chosen because each requires inventing a fact — a person's name, or a numeric threshold — that no source document supplies and `D-047` forbids guessing. **Revisable at any time**: naming a backup approver or a numeric auto-pause threshold supersedes this row.

Original text retained below for the record.

---

**Status when raised:** UNRESOLVED

**Question:** The owner is the only person who can approve any gated action (claims, pricing, discounts, testimonials, direct outreach, complaints, controversial topics, spending, paid advertising). If the owner is unavailable, every gated action halts indefinitely. Should the system have a backup approver, an auto-pause-on-unavailability mechanism, or should the single point of failure be explicitly accepted as a permanent constraint?

**Why it matters:** `RISK_REGISTER.md` R-02 rates this Medium likelihood / High impact, and R-01 rates approval-queue backlog High/High given the confirmed low time budget. The entire safety model of this architecture rests on human approval; if that human is a bottleneck with no fallback, the practical outcome is either stalled operations or pressure to bypass gates.

**What resolution unblocks:** Phase 03 (Governance/Approval/Autonomy Policies) needs to know whether to design an alternate-approver path. Phase 15 (Approval Queue) needs it to size queue-age limits and escalation. Phase 21 (Alerts/Incident Response) needs it to define what happens when approvals go stale.

**Owner action required:** Choose one: (a) name a backup approver and the scope of what they may approve; (b) require the system to auto-pause all gated work after a defined period of owner unavailability (specify the period); or (c) explicitly accept that all gated work halts when you are unavailable, with no fallback.

---

### Q-009 — Data-privacy handling for lead and contact data
**Status:** UNRESOLVED

**Question:** What are the handling, storage, retention, and deletion rules for personal/contact data collected from leads, DMs, comments, or WhatsApp conversations?

**Why it matters:** `RISK_REGISTER.md` R-12 flags this as UNRESOLVED with no data-privacy policy anywhere in the project. Phase 04 (Data Contracts and State Model) must define lead/contact schemas, and it cannot define retention or access rules without a policy. WhatsApp in particular (a confirmed candidate platform) involves direct personal messaging.

**What resolution unblocks:** Phase 04 (data contracts for lead/contact entities), Phase 17 (community/messaging/lead routing), Phase 18 (analytics on lead data).

**Owner action required:** State any known obligations (jurisdiction, applicable privacy regime, existing privacy policy on the business's website) and any retention preference, or confirm that Phase 03/04 should propose a default conservative policy for your approval.

---

### Q-010 — Precedence between the low-time-budget constraint and the approval gates
**Status:** ✅ **RESOLVED 2026-07-28**

**Owner's answer:** Both parts confirmed directly.
- **Q-010a — approval gates:** *"Gates always win."* Automation may reduce effort on routine, low-risk work but never removes a required approval step. All nine gated categories stay human-approved regardless of workload. The owner declined both alternatives (narrowing the gate list; allowing auto-approval for some categories). → `D-020` upgraded `INFERRED` → `APPROVED`.
- **Q-010b — design posture:** *"Automate aggressively."* Favor batched reviews, templated content, deterministic automation, scheduled digests. → `D-019a` upgraded `PROPOSED` → `APPROVED`.

**Governing formulation for all later phases: automate aggressively *within* the gates, never through them.** Phase 03 (governance/autonomy policy), Phase 15 (approval queue), and Phases 13–17 build against this.

Original question retained below for the record.

---

**Status when raised:** UNRESOLVED

**Question:** Two confirmed inputs pull against each other: you are a solo operator with a low review budget (D-019), and the system must require your approval for nine categories of action (D-011). Do you confirm that (a) automation may reduce your effort on routine, low-risk work but never removes a required approval step (D-020, currently INFERRED), and (b) the "automation-heavy" design posture in D-019a is what you actually want?

**Why it matters:** This precedence rule shapes every later phase's design. It was originally recorded as owner-approved, but you never stated it — the Independent Reviewer caught the fabricated attribution and it has been downgraded to INFERRED pending your actual answer. Getting this wrong in either direction is costly: too rigid and the system is unusable at your time budget; too loose and the human-approval safety model erodes.

**What resolution unblocks:** Phase 03 (governance/autonomy policy design), Phase 15 (approval queue design), and the general design posture of Phases 13–17.

**Owner action required:** Confirm or correct D-020 (approval gates always win) and D-019a (automation-heavy posture). If you want a different balance — for example, a narrower approval list in exchange for stricter automation limits — say so now, because later phases will build against whatever this resolves to.

---

### Q-011 — Defect in the quality rubric's passing threshold
**Status:** ✅ **RESOLVED 2026-07-28**

**Owner's answer:** *"Treat Security as covered by Permissions."* The "Permissions" category already covers least-privilege, gates, and access boundaries. `PROMPT_AND_BUILD_QUALITY_RUBRIC.md` is **not** edited; this interpretation governs instead. Phase gates score the 12 existing categories, and the elevated bar reads as **Permissions / Testing / Failure handling ≥ 4**. Applies to all gates 00–24. → `D-028` resolved to `APPROVED`.

Original question retained below for the record.

---

**Status when raised:** UNRESOLVED

**Question:** `PROMPT_AND_BUILD_QUALITY_RUBRIC.md` requires that "Security, permissions, testing, and failure handling must each score 4 or higher," but "Security" is not one of the rubric's 12 scoreable categories. How should this be resolved?

**Why it matters:** As written, the passing threshold is partly unsatisfiable, and it governs every one of the 25 phases including this one. Phase 00's mandate explicitly requires contradictions to be resolved or marked blocking, so leaving it silent would itself be a phase failure.

**What resolution unblocks:** Consistent, defensible scoring for every phase gate from 00 onward.

**Owner action required:** Choose one: (a) treat "Security" as covered by the existing "Permissions" category; (b) add a 13th "Security" category to the rubric with its own 0/3/5 definitions; or (c) remove "Security" from the threshold sentence. Until you decide, phase gates will score "Permissions" as the nearest analogue and report "Security" as unscoreable.

---

---

# Questions opened by Phase 02 — Capability Registry and Skill Foundation (2026-07-29)

Added by the Phase 02 Owner. Questions `Q-001`–`Q-011` above are **unmodified**.

Evidence base for all six: `agent_runs/phase-02/evidence/SESSION_CAPABILITY_INVENTORY.md`, `CAPABILITY_REGISTRY.md`, and the Phase 02 specialist handoffs.

---

### Q-012 — Which of the connected MCP connectors are actually authorized?
**Status:** UNRESOLVED

**Question:** The session's tool surface includes connectors identified as Gmail (read, draft create/update), Google Calendar (create/update/delete events, respond to invites), Stripe (including `stripe_api_write`), Supabase (including `create_project`, `confirm_cost`, `deploy_edge_function`, `execute_sql`), Figma, a remote job runner (`create_job`), and Claude in Chrome — described by the harness as the operator's real browser with existing logged-in sessions. None of these appeared in the harness's list of servers requiring authentication. **Are they authorized against your real accounts?**

**Why it matters:** `docs/PROJECT_BOUNDARIES.md` §3 states that every external system is `NOT CONNECTED` and no credential of any kind exists for this project. If any of these is authorized, that statement is incomplete — not because a credential entered this repository, but because these paths do not use one. Several are write-capable against live accounts, and two (`stripe_api_write`, Supabase `create_project`/`confirm_cost`) are spend-capable while no spend is authorized (`D-016`, `NG-001`).

**Why Phase 02 did not simply check:** determining a connector's authentication state requires invoking it. `docs/PROJECT_BOUNDARIES.md` §8 step 4 forbids acting against an external system, and probing a write-capable connector to learn whether it is live is exactly that act. `CLAUDE.md` §6 separately forbids inventing account status. Recording `UNRESOLVED` is the only honest option available from inside the boundary — and the answer changes no recommendation, because every one of these is dispositioned `PROHIBITED` or `RESTRICTED` regardless.

**What resolution unblocks:** an accurate `docs/PROJECT_BOUNDARIES.md` §3; the risk rating of `R-20`; and the starting position of `CONNECTOR_ACTIVATION_PLAN.md`.

**Owner action required:** open your claude.ai connector settings (or an interactive `claude` session) and report which of the named connectors are connected. Step-by-step instructions are in `CONNECTOR_ACTIVATION_PLAN.md` § "How the owner verifies this themselves". **If any is connected and you do not want this project's sessions reaching it, disconnect it — that is a one-click control and it is stronger than any rule this project can write.**

---

### Q-013 — Should the capability surface be under change control, and if so, how?
**Status:** UNRESOLVED

**Question:** `CAPABILITY_REGISTRY.md` describes a machine-local snapshot taken 2026-07-29. Plugins, skills, and connectors live outside this repository, under the user profile. Installing, removing, or authorizing any of them changes what every future session can do — with **no commit, no review, and no signal to this project**. Should any control exist over that, and what would you actually maintain?

**Why it matters:** Architecture Rule 1 makes files in Git authoritative, but the capability surface — which determines what any agent *can do* — is not in Git and cannot be. Every control this phase wrote rests on a snapshot that nothing keeps current. `R-18` already records that connectors change between selection and use; this is the same risk one level down.

**What resolution unblocks:** whether later phase gates must re-capture the inventory, and whether `CAPABILITY_REGISTRY.md` is a living document or a dated artifact superseded at each gate.

**Owner action required:** choose one — (a) re-capture the inventory at every phase gate and diff it (cheap, and the phase gate already exists as a checkpoint); (b) re-capture only before a phase that depends on a capability; (c) accept the drift explicitly and treat the registry as advisory. Option (c) is defensible for a solo operator (`D-019`) provided it is a decision rather than a default.

---

### Q-014 — Which phase owns the scheduled-execution host?
**Status:** ✅ **RESOLVED 2026-07-30 (`D-051`)**

**Resolution:** Option (b) — Phase 16 ("Publishing and Scheduling Adapters") owns establishing the Google Cloud scheduled-execution host. It is the first phase in the linear plan requiring genuinely scheduled, unattended execution, and its own name already says "Scheduling Adapters." Phases 19, 20, 21, and 24 consume that infrastructure rather than establish it. The Project Owner delegated this choice to the Phase 03 Owner (`D-049`); this resolves *ownership* only — it does not decide *whether* Google Cloud is the right host (already fixed by `README.md`'s stack intent) and it explicitly does **not** authorize any spend: the second gate this question itself names (any hosted scheduler is metered, and spending is gated per `D-011`/`D-016`) remains fully in force and requires its own separate approval when Phase 16 actually runs.

Original text retained below for the record.

---

**Status when raised:** UNRESOLVED

**Question:** `README.md` names Google Cloud as the platform for scheduled automation. **No phase prompt assigns it any deliverable** — the string "Google Cloud" appears zero times across all 25 files in `phase-prompts/`. Which phase owns the host that would actually run scheduled jobs?

**Why it matters — and this is more than a missing feature.** Phase 19's pass condition *"America/New_York schedule configurable"* is not honestly satisfiable with no execution host, and weakening a test to pass is forbidden. More seriously: a system with no scheduler degrades to owner-triggered manual runs, which **silently reverses `D-019a`** — the posture you confirmed on 2026-07-28, "automate aggressively," chosen precisely because you are a solo operator with a low review budget. The gap does not delay a decision; it inverts one without anyone deciding. Phases 16, 20, 21, and 24 depend on scheduled execution too, and Phase 21's "credentials and account restrictions detected" is the mechanism meant to catch an expired credential before it breaks something — itself with no trigger.

**A second gate nobody has recorded:** any hosted scheduler is metered. Spending is one of the nine approval-gated categories (`D-011`) and no spend is authorized (`D-016`, `NG-001`). **Resolving ownership does not by itself unblock the capability** — it needs a separate spending decision.

**What resolution unblocks:** Phase 19 in full; the scheduled halves of 16, 20, 21, 24; and whether `gcloud` is ever installed (`SKILL_INSTALLATION_PLAN.md` §4.1).

**Owner action required:** choose one — (a) add a phase that owns the execution host, most naturally between 18 and 19; (b) extend an existing phase's scope by recorded decision, the candidates being Phase 19 (its first hard consumer) or Phase 16 (titled "Publishing and *Scheduling* Adapters"); (c) rule that no hosted scheduler is in scope and the operating cycle is owner-triggered manually — permissible and fail-closed, but it conflicts with `D-019a` and that conflict should be recorded rather than absorbed; (d) rule that the host need not be Google Cloud. Extends `findings.md` `F-01-02`.

---

### Q-015 — May the system send notifications to you, the Project Owner?
**Status:** UNRESOLVED

**Question:** `CLAUDE.md` §6 and `docs/PROJECT_BOUNDARIES.md` §4.1 prohibit sending "any message to any real person (email, DM, comment, reply, invite)" with no stated exception. You are a real person. Phase 19's pass condition requires *"Email and Drive delivery independently retryable"* for the weekly executive summary. May the system send to you, and through which channels?

**Why it matters:** as the repository currently reads, **Phase 19 may not email its own digest to you.** `docs/PROJECT_BOUNDARIES.md` §7.5 makes the stricter reading govern a conflict until you resolve it. This is almost certainly not anyone's intent — a weekly digest to the owner is the least dangerous message the system could send, and it is the mechanism `D-019a` depends on — but the reading is the reading, and an agent may not widen a boundary on the strength of "surely they meant."

**What resolution unblocks:** Phase 19's delivery path; Phase 21's alerting.

**Owner action required:** state whether owner-directed notification is exempt from the send prohibition, and scope it precisely — email only, or any channel; to your address only, or any address you name later. Keeping it narrow costs nothing now and prevents the exemption being read broadly later.

---

### Q-016 — Where do Phase 04's fixtures live?
**Status:** UNRESOLVED

**Question:** Phase 04's pass condition is *"Schemas validate fixtures."* Its deliverable list names eight schemas and a state machine — **no home for fixtures**. `MASTER_PLAN.md` places the first `tests/` directory at Phase 13, nine phases later. Where do they go?

**Why it matters:** Phase 04 is the **first phase in the entire plan whose pass condition prose cannot satisfy** — a validator must actually run against artifacts that must actually exist. The artifact it is graded against has nowhere to live. Same species as `F-00-02` (files named in prompts that do not exist), and cheap to close before Phase 04 starts, awkward during it.

**What resolution unblocks:** Phase 04's gate.

**Owner action required:** none strictly required from the Project Owner — the **Phase 03 or Phase 04 owner** may record the intended location as an implementation decision. Raised here so Phase 04 does not discover it at the start line, following the `Q-007` precedent.

---

### Q-017 — What does Phase 03's "Policy conflicts tested" actually require?
**Status:** ✅ **RESOLVED 2026-07-30 (`D-041`, Phase 03 Owner)**

**Question:** Phase 03's fifth pass condition is *"Policy conflicts tested."* Does that require `AGENT_PERMISSION_MATRIX.md` to be machine-parseable plus a script that enumerates rule pairs and reports contradictions — or is it satisfied by the documentation-phase resolution in `findings.md` `F-00-04` (cross-reference integrity, ID resolution, vocabulary conformance, arithmetic)?

**Resolution (`D-041`):** Both, not either. "Policy conflicts tested" requires two distinct checks, both exercised: (1) **structural** — no two rows in `policy/action_registry.json` assign different outcomes to the same (role, verb, resource, statement), checked mechanically (`tools/policy_check.py` V-5/V-7/V-8); (2) **prose** — no policy document's prose contradicts the registry or a sibling document, checked by an itemized cross-read performed by the Independent Reviewer and recorded in `REVIEW_REPORT.md`. Neither alone satisfies the condition.

This was explicitly the **Phase 03 owner's own call**, per the note this question was raised with — not an owner decision, hence `D-041` is `APPROVED_IMPL`, not `APPROVED`.

Original text retained below for the record.

---

**Status when raised:** UNRESOLVED

**Question:** Phase 03's fifth pass condition is *"Policy conflicts tested."* Does that require `AGENT_PERMISSION_MATRIX.md` to be machine-parseable plus a script that enumerates rule pairs and reports contradictions — or is it satisfied by the documentation-phase resolution in `findings.md` `F-00-04` (cross-reference integrity, ID resolution, vocabulary conformance, arithmetic)?

**Why it matters:** it determines whether Phase 03 needs a script runtime and a rigidly structured permission matrix, or careful authoring plus the existing mechanical checks. Both readings are defensible. **Choosing silently is not** — and the choice shapes the format of a document five later phases consume.

**What resolution unblocks:** Phase 03's structure and its gate evidence.

**Owner action required:** none from the Project Owner. The **Phase 03 owner** decides consciously and records the decision. Noted here so it is a decision rather than a drift.

---

## Summary table

| ID | Question | Status | Blocks |
|---|---|---|---|
| Q-001 | 90-day objective priority ranking | UNRESOLVED | Phase 09, 10, 12, 19 |
| Q-002 | Final platform rollout order | UNRESOLVED (deferred to Phase 10 by design) | Phase 10, 11, 12, 13, 16 |
| Q-003 | Numeric KPIs/targets | UNRESOLVED | Phase 18, 19 |
| Q-004 | Google Drive folder location/access | BLOCKED | Phase 05, 15, 19 |
| Q-005 | Existing social account status | UNRESOLVED | Phase 10, 11, 16 |
| Q-006 | Brand asset source location | UNRESOLVED | Phase 07, 13 |
| Q-007 | Which specific Rough-Draft-Builders-Club files are approved fact sources | UNRESOLVED — **may block Phase 06's start** (Phase 01 escalation) | Phase 06 |
| Q-008 | Backup approver / accept single-approver SPOF | ✅ RESOLVED 2026-07-30 (`D-050`) | — |
| Q-009 | Data-privacy handling for lead/contact data | UNRESOLVED | Phase 04, 17, 18 |
| Q-010 | Precedence: low-time-budget constraint vs. approval gates | ✅ RESOLVED 2026-07-28 | — |
| Q-011 | Rubric defect — "Security" threshold is unscoreable | ✅ RESOLVED 2026-07-28 | — |
| Q-012 | Which connected MCP connectors are actually authorized | UNRESOLVED | Accuracy of `BOUNDARIES` §3; `R-20`; connector activation |
| Q-013 | Change control over the machine-local capability surface | UNRESOLVED | Whether `CAPABILITY_REGISTRY.md` stays valid at later gates |
| Q-014 | Which phase owns the scheduled-execution host | ✅ RESOLVED 2026-07-30 (`D-051`) — Phase 16 | — |
| Q-015 | May the system send notifications to the Project Owner | UNRESOLVED | Phase 19 delivery; Phase 21 alerting |
| Q-016 | Where Phase 04's fixtures live | UNRESOLVED | Phase 04 gate |
| Q-017 | What Phase 03's "Policy conflicts tested" requires | ✅ RESOLVED 2026-07-30 (`D-041`) | Phase 03 structure and gate evidence |

## Which of these block the Phase 00 gate

**None remain.** Q-010 and Q-011 were the two gate-blocking items and both were resolved by the owner on 2026-07-28. The third gate condition — confirming `INTAKE_RECORD.md` is accurate — was also cleared by the owner the same day.

**Q-004** is the only item with status `BLOCKED` (external dependency: Google Drive access), but it blocks Phase 05, not this gate.

Q-001, Q-002, Q-003, Q-005, Q-006, Q-007, Q-008, and Q-009 all block *later* phases and do not need resolution before Phase 01 begins. Q-001 in particular should be answered before Phase 09.

### Remaining open: 12 of 17

*(Updated by the Phase 03 Owner, 2026-07-30 — `Q-008` resolved via `D-050`, `Q-014` resolved via `D-051`, both owner-delegated. `Q-017` resolved via `D-041`. Was 14 of 17.)*

Q-001, Q-002, Q-003, **Q-004 (BLOCKED)**, Q-005, Q-006, Q-007, Q-009, Q-012, Q-013, Q-015, Q-016.

**Q-004 remains the only `BLOCKED` item.** None of the six new questions blocked the Phase 02 gate — each was recorded rather than guessed, per `D-008`.

**Which of the new six need the Project Owner personally:** `Q-012`, `Q-013`, `Q-014`, `Q-015`. The other two (`Q-016`, `Q-017`) are decisions for the Phase 03/04 owners and are recorded here only so those phases do not meet them at the start line — the `Q-007` precedent.

**Which is most urgent:** `Q-014`. Left open it silently reverses `D-019a`, an owner-confirmed decision, and it should not wait until Phase 19 discovers it. `Q-012` is the cheapest to answer and the one that most directly affects whether `docs/PROJECT_BOUNDARIES.md` §3 is currently accurate.
