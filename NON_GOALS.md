# Non-Goals

Prepared by: Product Strategist (Phase 00)
Phase: 00 — Decision Lock and Scope Control
Project: Agent Atlas Growth Department (for Rough Draft Builders Club)
Date: 2026-07-28

## Purpose of this document

Defines what is explicitly out of scope for the near-term build (Phases 01–10, see SCOPE.md). A non-goal is not a permanent prohibition unless marked as such — it is a boundary for the current phase of work that a future explicit owner decision can change.

Status labels used below: `CONFIRMED` (owner-stated or fixed in a source document), `INFERRED` (reasonable draft conclusion, needs owner confirmation), `PROPOSED` (specialist recommendation, needs owner decision), `UNRESOLVED` (genuinely unknown), `BLOCKED` (needs an external dependency that doesn't exist yet).

**Important framing note:** During the owner intake that produced this phase's confirmed answers, the owner was offered two specific non-goal options — "no influencer/paid partnerships" and "no testimonials without approval" — as selectable items, and did **not** select either one. Only "solo operator, low time budget" was selected. Non-selection is not rejection — it is simply undecided. These two items must NOT be recorded as confirmed non-goals; see `INTAKE_RECORD.md` Q4 for the verbatim intake record. They appear below only as proposed candidates requiring separate owner confirmation, not as decided.

## Confirmed non-goals

These are locked — owner-stated or already fixed in a source document — and apply across the near-term build (Phases 01–10) and, unless a future explicit decision changes them, beyond.

### NG-001 — No paid advertising or paid spend
**Status:** `CONFIRMED` (the prohibition) / `INFERRED` (its duration)
**Source:** `INTAKE_RECORD.md` Q2; DECISIONS.md D-016 and D-016a; README's "Primary success criteria" (approval required for spending and paid advertising); MASTER_LINEAR_BUILD_PLAN.md Phase 22.

No phase in the near-term build may initiate, plan for execution, or activate any paid advertising campaign, paid boost, paid partnership requiring payment, or any other spend of money on the organization's behalf. This includes platform ad accounts, boosted posts, and paid promotion of any kind. **This much is `CONFIRMED`.**

**On duration — read carefully.** The owner's exact answer was *"organic only **for now**"*, in response to a question framed as *"at least initially."* The owner set no end condition. Treating the prohibition as remaining in force until an explicit future owner decision — rather than lapsing automatically at Phase 22 or any other point — is a fail-closed `INFERRED` default chosen by this project, **not** a quotation of the owner. It is the safe reading, and Phase 22's own wording ("Design—but do not initially activate") supports it, but the owner has not confirmed an indefinite hold. *(Corrected by the Phase 00 Owner per Independent Reviewer Finding 15, which flagged the original wording as strengthening the owner's "for now" into an indefinite prohibition under a `CONFIRMED` label.)*

### NG-002 — No production launch, publishing, sending, or account creation before their designated phase gates
**Status:** `CONFIRMED`
**Source:** Architecture Rule 10 (maturity ladder `DISABLED → SIMULATION → DRAFT_ONLY → APPROVAL_REQUIRED → LIMITED_AUTONOMY → ROUTINE_AUTONOMY`); MASTER_LINEAR_BUILD_PLAN.md release rule ("No production launch occurs before Phase 23 passes and the owner explicitly approves Phase 24"); Phase 00–10 prompts' universal operating rule ("Never publish, send, spend, deploy, or create production resources unless the phase explicitly permits it and approval evidence exists").

Not in scope for Phases 01–10: creating live social media accounts, publishing any content publicly, sending any message to a real customer or lead, or deploying any production service. Phases 01–10 produce plans, policies, schemas, and drafts only.

### NG-003 — No modification of the Rough-Draft-Builders-Club repository
**Status:** `CONFIRMED`
**Source:** `user-guide/USER_INSTRUCTIONS.md`; DECISIONS.md D-013.

This project must not modify `C:\Users\crone\Projects\Rough-Draft-Builders-Club` in any way. Reading is a separate matter and is **not** a non-goal: `user-guide/USER_INSTRUCTIONS.md` permits reading *explicitly approved* source files from that repository. Which specific files are approved has not yet been designated — see OPEN_QUESTIONS.md Q-007. Modification remains unambiguously out of scope regardless of how the read-source question resolves.

### NG-004 — No numeric KPI or growth-target commitments in this phase
**Status:** `CONFIRMED` as absent, not yet decided
**Source:** DECISIONS.md D-021; OPEN_QUESTIONS.md Q-003.

No specific numeric target (follower counts, lead counts, conversion rates, revenue figures, engagement rates, or timelines) is being set as of Phase 00. This is a non-goal for the current phase because no such numbers have been provided by the owner — not because numeric targets are undesirable in principle. See ACCEPTANCE_CRITERIA.md for how this affects measurable pass/fail criteria.

### NG-005 — No skipping ahead to Phases 11–24 work
**Status:** `CONFIRMED`
**Source:** MASTER_LINEAR_BUILD_PLAN.md dependency rule; Architecture Rule 7 ("No phase may auto-start the next phase").

Work belonging to Phases 11–24 (social presence launch, content production, publishing adapters, community/lead routing, analytics, paid growth guardrails, end-to-end testing, controlled launch) is not in scope for the near-term build regardless of how much of Phases 01–10 is completed. Each phase gate must pass independently and in order.

## Candidate non-goals requiring owner confirmation

These were considered but are **not** confirmed. They are the Product Strategist's recommendation only, based on common-sense adjacency to the confirmed non-goals above and general marketing-operations risk patterns — not on anything the owner actually selected. Per the hard rule in this task's briefing, they must not be asserted as decided.

### CNG-001 — Influencer or paid-partnership activity
**Status:** `PROPOSED` (not selected by owner when offered)
**Rationale for proposing:** Influencer/partnership activity typically involves negotiated compensation or reciprocal promotion, which would interact with the paid-spend non-goal (NG-001) and the approval-required list (claims, direct outreach). Flagging it as a candidate boundary worth an explicit owner decision, since the owner was asked and did not confirm it.

**Boundary with NG-001 (per Reviewer Finding 22):** NG-001 already prohibits the *paid* portion — any partnership requiring payment is out of scope as a direct consequence of the organic-only posture. What remains genuinely open here is the *unpaid* portion: unpaid collaborations, reciprocal promotion, product gifting, and affiliate arrangements where no money leaves the business. CNG-001 asks about that remainder only.

**Owner action needed:** Confirm whether *unpaid* influencer/collaboration activity is out of scope for the near-term build, in scope with restrictions, or simply undecided until it becomes relevant (e.g., at Phase 10 or later).

### CNG-002 — Testimonials without approval
**Status:** `PROPOSED` (not selected by owner when offered)
**Rationale for proposing:** README's "Primary success criteria" already lists testimonials among items requiring approval regardless (see D-011, which is `CONFIRMED`) — so *some* control already exists. What remains open is whether testimonial collection/use should be excluded from near-term scope entirely (a stronger non-goal) versus simply gated by the existing approval requirement (the current default). Flagging so the owner can clarify which they intend.
**Owner action needed:** Confirm whether testimonial collection/use is fully out of scope for now, or in scope subject to the existing approval-required gate (D-011).

### CNG-003 — Platforms outside the four named candidates
**Status:** `PROPOSED`
**Rationale for proposing:** The owner named Facebook, Instagram, WhatsApp, and TikTok as candidates of early interest (D-017). No other platform (e.g., LinkedIn, X/Twitter, YouTube, Pinterest, email marketing as a "platform") was named. Proposing that platforms outside this list be treated as out of near-term scope unless the owner adds them, so Phase 08 research and Phase 10 scoring have a bounded candidate set rather than an open-ended one.
**Owner action needed:** Confirm the four named platforms are the complete near-term candidate set, or add/remove candidates before Phase 08–10 research begins.

### CNG-004 — Direct customer outreach and cold contact
**Status:** `PROPOSED`
**Rationale for proposing:** README's approval-required list already includes "direct outreach" (D-011, `CONFIRMED`). Proposing that *unsolicited* cold outreach (as distinct from responding to inbound leads/messages, which Phase 17 covers) be treated as fully out of near-term scope rather than merely approval-gated, given the organic-only, low-time-budget posture. This is a stronger restriction than what D-011 already guarantees, so it needs explicit owner sign-off rather than being assumed.
**Owner action needed:** Confirm whether cold/unsolicited outreach should be a hard non-goal for the near-term build, or remain simply approval-gated like other listed items.

## Summary table

| ID | Non-goal | Status |
|---|---|---|
| NG-001 | No paid advertising or spend | CONFIRMED (prohibition) / INFERRED (indefinite duration) |
| NG-002 | No production launch/publish/send/account creation before designated gates | CONFIRMED |
| NG-003 | No modification of Rough-Draft-Builders-Club repo | CONFIRMED |
| NG-004 | No numeric KPI commitments this phase | CONFIRMED (as currently absent) |
| NG-005 | No skipping ahead to Phases 11-24 | CONFIRMED |
| CNG-001 | Influencer/paid-partnership activity out of scope | PROPOSED — owner did not select when offered |
| CNG-002 | Testimonials without approval out of scope (stronger than existing gate) | PROPOSED — owner did not select when offered |
| CNG-003 | Platforms outside the four named candidates out of scope | PROPOSED |
| CNG-004 | Cold/unsolicited outreach out of scope (stronger than existing gate) | PROPOSED |
