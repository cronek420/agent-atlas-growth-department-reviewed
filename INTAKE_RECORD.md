# Owner Intake Record — Phase 00

**Date of intake:** 2026-07-28
**Captured by:** Atlas Orchestrator (Phase 00 Owner)
**Owner confirmation:** ✅ **CONFIRMED ACCURATE by the Project Owner on 2026-07-28**, after this record was written and presented for review. The owner was specifically asked to verify that "organic only for now" is correctly treated as holding indefinitely absent a further decision, and that the four named platforms are correctly treated as directional rather than selected. This record is therefore owner-verified, not a phase-owner reconstruction.
**Purpose:** Durable, auditable record of exactly what the Project Owner was asked and exactly what they answered. Created in response to Independent Reviewer Finding 4, which correctly identified that every owner-derived decision cited a "task briefing" that existed nowhere in the repository — violating Architecture Rule 1 (Markdown in the repo is the authoritative source of truth).

This file is the sole authoritative source for owner-confirmed inputs in Phase 00. All `APPROVED`/`CONFIRMED` decisions derived from the owner must cite this file.

## How this intake was conducted

The owner was presented with four multiple-choice questions in the Claude Code session on 2026-07-28, before any Phase 00 deliverable was drafted. The owner selected from presented options. Questions 3 and 4 permitted multiple selections.

## Question 1 — Primary objective

**Exact question asked:** "What's the primary 90-day objective for this growth department to lock into scope?"

**Options presented:**
1. Leads/sales conversion — "Drive qualified leads or direct purchases for Rough Draft Builders Club — content and channels optimized toward conversion."
2. Audience/brand building — "Grow organic reach, followers, and brand recognition first; monetization is a later phase."
3. Community engagement — "Build an active community (members, forum, group) as the core metric, with sales as a downstream effect."
4. Mixed — no single priority yet — "Multiple goals in play; leave the relative priority UNRESOLVED for now and let the Phase 00 team draft options for you to pick from."

**Owner selected:** *"Mixed — no single priority yet"*

**What this does and does not establish:** It establishes that no single objective is prioritized and that the priority is deliberately UNRESOLVED. It does **not** establish any ranking, weighting, or sequencing among the three candidates.

## Question 2 — Paid-spend posture

**Exact question asked:** "What's the paid-spend posture for this build, at least initially?"

**Options presented:**
1. Organic only for now (marked Recommended) — "No paid advertising or spend authorized until a later phase (matches Phase 22's design of building but not activating budget guardrails)."
2. Small test budget planned — "You have a rough dollar figure in mind for early paid tests."
3. Leave UNRESOLVED — "Don't decide this now; mark it as an open question for a future phase/decision."

**Owner selected:** *"Organic only for now"*

**What this does and does not establish:** It establishes that no paid advertising or spend is authorized "for now." The owner's phrasing is time-qualified — *"for now"*, *"at least initially"*. It does **not** establish an indefinite prohibition, nor a specific date or phase at which the posture changes. Treating it as remaining in force until an explicit future owner decision is a fail-closed *inference*, not the owner's words.

## Question 3 — Platform candidates

**Exact question asked:** "Which platforms should be prioritized for initial rollout consideration? (Phase 10 will do formal scoring later — this just sets early scope/non-goals.)"

**Options presented:** Instagram + visual/short-form video (TikTok); YouTube long-form; Email/Newsletter; Undecided — defer to Phase 10.

**Owner answered (free text, not a listed option):** *"facebook, instagram, whatsapp, tiktok"*

**What this does and does not establish:** It establishes four platforms of early owner interest. The question itself framed this as "initial rollout consideration" with formal scoring explicitly deferred to Phase 10. It does **not** establish a rollout order, a launch commitment, a complete candidate set, or that platforms outside these four are excluded. Note the owner typed a free-text answer rather than selecting a presented option, and named WhatsApp and Facebook, which were not among the presented choices.

## Question 4 — Constraints and non-goals

**Exact question asked:** "Any hard constraints or non-goals I should lock in now (industry rules, personal bandwidth, brand sensitivities)?" (multi-select)

**Options presented:**
1. Solo operator — low time budget — "Assume limited hours/week for review and approvals; favor low-maintenance, high-leverage workflows."
2. No influencer/paid partnerships — "Rule out influencer marketing or paid collaborations as out of scope for now."
3. No customer testimonials without explicit approval — "Already covered by default approval policy, but confirms it's a hard non-goal to automate."
4. None of these — keep default policy only.

**Owner selected:** *"Solo operator — low time budget"* — and only that option.

**What this does and does not establish:** It establishes the solo-operator, low-time-budget constraint. Because option 1's description included the phrase "favor low-maintenance, high-leverage workflows," the owner did see that framing attached to the option they selected — but the selection is properly read as confirming the *constraint*, not as endorsing any particular downstream design posture (e.g., "automation-heavy").

**Critically:** options 2 and 3 were offered and **not** selected. "No influencer/paid partnerships" and "no testimonials without approval" must therefore **not** be recorded as confirmed non-goals. Non-selection is not rejection either — it is simply undecided.

## Second intake round — 2026-07-28, post-review

After the independent review downgraded two decisions that had been wrongly attributed to the owner, the owner was asked to answer them directly. These are owner-stated, not inferred.

### Q-010a — Precedence: approval gates vs. time budget

**Exact question:** "Do approval gates always beat your time budget? (D-020, currently INFERRED)"

**Owner selected:** *"Yes — gates always win."* Full option text: "Automation may reduce your effort on routine, low-risk work, but never removes a required approval step. The nine gated categories (claims, pricing, discounts, testimonials, direct outreach, complaints, controversial topics, spending, paid advertising) stay human-approved regardless of how busy you are."

**Effect:** `D-020` upgraded `INFERRED` → `APPROVED`. The owner declined the two alternatives (narrowing the gate list; allowing some categories to auto-approve). The nine-category gate list stands intact.

### Q-010b — Design posture

**Exact question:** "Is an 'automation-heavy' design posture what you actually want? (D-019a, currently PROPOSED)"

**Owner selected:** *"Yes — automate aggressively."* Full option text: "Favor low-maintenance, high-leverage designs: batched reviews, templated content, deterministic automation, scheduled digests. Minimizes your routine burden within whatever gate rules Q-010a establishes."

**Effect:** `D-019a` upgraded `PROPOSED` → `APPROVED`. Note the two answers compose deliberately: automate aggressively **within** the gates, never through them.

### Q-011 — Rubric defect

**Exact question:** "How should the rubric's unscoreable 'Security' threshold be fixed?"

**Owner selected:** *"Treat Security as covered by Permissions."* Full option text: "Simplest fix. 'Permissions' already covers least-privilege, gates, and access boundaries. No rubric edit needed — phase gates score 12 categories and the threshold reads as Permissions/Testing/Failure-handling ≥ 4."

**Effect:** `D-028` resolved. No edit to `PROMPT_AND_BUILD_QUALITY_RUBRIC.md` is required; the governing document stays as written and the interpretation is recorded here. Applies to all phase gates 00–24.

## Third intake round — 2026-07-29 — Standing Operating Grant

Captured at the moment of receipt, before any deliverable cites it, per `findings.md` `F-00-06`. This is the **first owner-stated authority change since `D-030`**.

**Context.** The owner asked what prompt would make phase execution more efficient, make recurring mistakes stop recurring, make the agent "more powerful without being able to do anything against me," and keep it transparent. A grant was drafted in response and the owner then **pasted it back**, with the instruction that it be pasted after `00_MASTER_START_HERE.md` and before the phase prompt.

**Provenance note, stated plainly because it matters.** The grant text was **drafted by the Phase 02 Owner**, not composed by the owner from scratch. The owner adopted it. That makes its *authority* owner-stated, and its *wording* agent-drafted. Anyone auditing this should read the two facts together: the owner authorized latitude, using language an agent proposed. Recorded so no future phase mistakes agent-authored wording for owner-authored intent.

**What the owner granted — verbatim in substance, by numbered clause:**

| Clause | Grant |
|---|---|
| Preamble | Adds latitude on reversible local work; **removes no prohibition** in `CLAUDE.md` §6, `docs/PROJECT_BOUNDARIES.md`, or the nine gated categories. Where the grant and those files conflict, **those files win and the grant is wrong** |
| 1 | Proceed without asking on: commit and push to the private remote at any point; create/commit/reuse tooling under `tools/`; install **local dev dependencies** into a project-local venv or `node_modules` when a deliverable needs one, recorded as `APPROVED_IMPL` with its uninstall command; make implementation choices in mandate; fix a prior-phase file this phase falsified, as a recorded correction |
| 2 | Hard stops, unchanged and explicitly restated: spending money **or raising any spend or usage limit** or provisioning anything metered; publishing, sending, account creation, deploying, pricing or brand changes; authorizing/authenticating/enabling/invoking any capability not already `PERMITTED` in `CAPABILITY_REGISTRY.md`; ingesting anything from `Rough-Draft-Builders-Club` by any route; widening any boundary; starting the next phase; writing a secret anywhere |
| 3 | **Budget review first.** State and hold back a review reserve before spawning any specialist. Cap specialists at three unless justified in `task_plan.md`. Prefer one agent doing sequential passes over two duplicating context. **If budget runs short, cut a specialist, never the reviewer** |
| 4 | **Preflight** against the named recurring-defect list (`F-00-05`, `F-00-07`, `F-00-09`, `F-01-04`, `F-01-08`, `F-01-09`, `F-02-07`, `F-02-11`), one line each, none skipped |
| 5 | **Turn every lesson into a check.** Each finding becomes an executable check under `tools/` or an explicit statement of why it is not mechanizable. Every check must be shown to **fail on seeded bad input** before any pass counts, with the red demonstration recorded beside the green |
| 6 | **Derive, don't copy.** Any number appearing in more than one file is computed by a committed script at report time, never transcribed |
| 7 | **Transparency ledger** at `agent_runs/phase-XX/ACTION_LEDGER.md`, appended as work proceeds and **never reconstructed at the end**. At the gate, volunteer what the owner might not expect, what could not be verified, and what would be done differently |
| 8 | **No forward writing** of any status, progress, or completion record. Intentions belong in `task_plan.md` only |
| 9 | **Say when the owner is wrong.** If the grant, a phase prompt, or an instruction conflicts with the architecture or would produce bad work, say so and proceed with the safer reading |

**Scope, by the grant's own words: "applies to this phase only."** It is not a standing change to the operating contract. It must be re-pasted for each phase, or the durable parts must be moved into `CLAUDE.md` by a separate owner decision. Recorded as `D-040`.

**Not granted, and not inferred:** nothing about connectors, credentials, spend, publishing, or `Rough-Draft-Builders-Club`. Clause 2 restates every prohibition and clause 1's install permission is explicitly limited to language packages, explicitly excluding "plugins, skills, connectors, or MCP servers."

---

## Fourth intake round — 2026-07-30, Phase 03

**Exact owner message (verbatim, this session):** *"use logic and you can decide both, Q-008, and Q-014. then pass on current phase."*

**What this establishes:**
1. The owner **explicitly delegated** the substantive resolution of `Q-008` and `Q-014` to the Phase 03 Owner, instructing it to "use logic" — i.e., reason from what is already known rather than invent new facts. This is an owner-stated grant of decision authority, distinct from the Phase 03 Owner deciding unprompted (`APPROVED_IMPL`'s usual "nobody asked the owner" basis does not apply here — the owner was asked, and affirmatively delegated).
2. The owner instructed the Phase 03 Owner to **record a PASS gate decision** for Phase 03, in place of the gate report's own CONDITIONAL PASS recommendation. Precedent: the Phase 01 Owner did exactly this in Phase 01 (accepted an unconditional PASS against a CONDITIONAL PASS recommendation), recorded as the owner's prerogative under `D-007`.

**What this does NOT establish:** it does not supply the specific name of a backup approver, a specific numeric auto-pause threshold, or any other invented fact. "Use logic" is read as authorizing reasoned selection among already-stated options and already-known project structure — not as authorizing invention of facts in the prohibited classes (`CLAUDE.md` §6). The substantive resolutions of `Q-008` and `Q-014`, reasoned from this delegation, are recorded as `D-050` and `D-051`; the delegation itself is recorded as `D-049`. The gate decision is recorded in `CURRENT_PHASE.md`.

---

## What the owner did NOT provide

No numeric targets, KPIs, budgets, dates, or deadlines. No account inventory. No brand asset locations. No Google Drive information. No approved file list from the Rough-Draft-Builders-Club repository. See `OPEN_QUESTIONS.md`.

## Non-owner-derived confirmed facts

These are fixed by existing source documents, not by this intake:

| Fact | Source |
|---|---|
| Project location is `C:\Users\crone\Projects\agent-atlas-growth-department`, standalone from the app repo | `user-guide/USER_INSTRUCTIONS.md`, "Recommended project location" |
| The project may read *explicitly approved* files from `Rough-Draft-Builders-Club`; it must not modify that folder | `user-guide/USER_INSTRUCTIONS.md`, "Recommended project location" |
| The 10 architecture rules | `README.md`, "Architecture rules" |
| Approval-required action list (claims, pricing, discounts, testimonials, direct outreach, complaints, controversial topics, spending, paid advertising) | `README.md`, "Primary success criteria" |
| Human checkpoint list (terms acceptance, captchas, identity verification, OAuth consent, account creation, etc.) | `user-guide/USER_INSTRUCTIONS.md`, "Human checkpoints" |
| Secrets handling: `.env` local, Secret Manager production, `.env.example` placeholders only | `user-guide/USER_INSTRUCTIONS.md`, "Never paste secrets into prompts" |
| Dependency rule and release rule (no launch before Phase 23 passes + explicit Phase 24 approval) | `MASTER_LINEAR_BUILD_PLAN.md` |
