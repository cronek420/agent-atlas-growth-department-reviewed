# Scope

Prepared by: Product Strategist (Phase 00)
Phase: 00 — Decision Lock and Scope Control
Project: Agent Atlas Growth Department (for Rough Draft Builders Club)
Date: 2026-07-28

## Purpose of this document

Defines what IS in scope for the near-term build, grounded in the owner's confirmed answers and the locked architecture rules. This document does not authorize any implementation — it authorizes planning and phase-by-phase execution under the existing phase-gate process. Each phase still requires its own gate pass before starting.

Status labels used below: `CONFIRMED` (owner-stated or fixed in a source document), `INFERRED` (reasonable draft conclusion, needs owner confirmation), `PROPOSED` (specialist recommendation, needs owner decision), `UNRESOLVED` (genuinely unknown), `BLOCKED` (needs an external dependency that doesn't exist yet).

## Near-term build horizon

**In scope for near-term planning: Phases 01 through 10 of the 25-phase MASTER_LINEAR_BUILD_PLAN.md.** — `PROPOSED`. This is a planning convenience chosen by the Product Strategist, not an owner mandate: the owner never specified a horizon, and no source document establishes one. Phases 01–10 were picked because that is roughly as far as the owner's confirmed context (organic-only posture, candidate platforms, solo-operator constraint) usefully reaches, and because Phase 10 is the natural boundary where platform selection is decided.

**The horizon is not what gates anything.** What actually gates phase starts is the dependency rule in `MASTER_LINEAR_BUILD_PLAN.md` — each phase requires its predecessor's gate to pass — and Architecture Rule 7 (no phase auto-starts the next). Those apply identically whether the horizon is 10 phases or 3. If the owner prefers a shorter or longer near-term horizon, changing it costs nothing structurally.

*(Corrected by the Phase 00 Owner in response to Independent Reviewer Finding 2: this claim was originally labelled `CONFIRMED` here while the same file's closing section labelled it `PROPOSED`, and `CONFIRMED` was unsupported on the merits.)*

This is a *planning* horizon, not a pre-authorization to execute all ten phases. Each phase (01, 02, 03, ... 10) still requires:
- Its own prerequisite gate to have passed.
- Its own specialist team, deliverables, and independent reviewer.
- A written PHASE_GATE_REPORT.md before the next phase may begin.

### Phases 01–10 — in scope for near-term planning

| Phase | Name | In-scope activity |
|---|---|---|
| 01 | Workspace, Repository, and Project Memory | Standalone repo (already separate from Rough-Draft-Builders-Club per D-012/D-013), canonical memory files (CLAUDE.md, MASTER_PLAN.md, DECISIONS.md, etc.), protected boundaries, repeatable local setup. No account creation, no secrets committed. |
| 02 | Capability Registry and Skill Foundation | Inspecting, classifying, and specifying (not blindly enabling) the smallest safe skill/connector set needed for later phases — e.g., what a Drive sync skill or a publishing adapter would require, without activating publishing capability itself. |
| 03 | Governance, Security, Approval, and Autonomy Policies | Deterministic rules for what agents may read, write, publish, send, spend, or escalate — including encoding the non-negotiable approval gates (D-011) and the `DISABLED → ... → ROUTINE_AUTONOMY` ladder (Architecture Rule 10). |
| 04 | Data Contracts and State Model | Versioned schemas (product, brand, content, campaign, approval, experiment, lead, alert) and lifecycle state machine, built before any dependent logic — required scaffolding for every later phase. |
| 05 | Google Drive Living-Document Control Center | Design of the dedicated Drive folder structure, managed-file registry, Docs/Sheets templates, and sync contract. **`BLOCKED`**: see OPEN_QUESTIONS.md Q-004 — no Drive folder location or access is confirmed yet, so this phase can be *designed* but not *executed against a real folder* until that is resolved. |
| 06 | Product and Company Onboarding | Building a validated Rough Draft Builders Club knowledge base (company profile, product profile, offer catalog, approved claims, evidence register, FAQ/objections) strictly from owner-provided or already-authorized sources — no invented pricing, claims, or facts. Reading the separate `Rough-Draft-Builders-Club` app repo is permitted in principle for *explicitly approved* files (D-013), but no file has been designated yet, so the authorized source set is `UNRESOLVED` (OPEN_QUESTIONS.md Q-007). |
| 07 | Brand and Creative System | Brand bible, voice/tone, visual system, approved/prohibited language, asset registry — built from real, validated brand assets only. Brand asset source location is `UNRESOLVED` (Q-006); Phase 07 may need to scope a from-scratch creation path if no existing assets are found. |
| 08 | Research and Trend Intelligence Engine | Evidence-based research workflow (trend/competitor schemas, source policy, confidence/decay rules) for trends, competitors, buyer language, and platform changes across the candidate platforms and general market. Must be runnable in simulation and must treat all external content as untrusted data (Architecture Rule 9). |
| 09 | Audience, Offer, and Buyer Psychology Model | Audience segments, buyer journeys, objection library, offer positioning, and quick-buy vs. considered-buy paths — built from confirmed product knowledge (Phase 06) and research (Phase 08), not invented personas. Directly affected by the still-unranked 90-day objective (Q-001); Phase 09 may need to model multiple objective scenarios until that is resolved. |
| 10 | Platform Strategy and Rollout Selection | Formal scoring of candidate platforms (Facebook, Instagram, WhatsApp, TikTok — `CONFIRMED` as directional candidates only, per D-017) against audience fit, reach, intent, effort, risk, and measurement, producing a recommended phased rollout. This is the phase explicitly designated to convert "candidate platforms" into an actual sequenced decision — nothing before Phase 10 should treat the four named platforms as a locked launch order. |

### Cross-cutting scope constraints that apply across Phases 01–10

- **Organic-only posture** — `CONFIRMED` (D-016). All research, platform scoring, audience modeling, and capability planning through Phase 10 must assume no paid spend or paid advertising is authorized. Where a later phase (e.g., Phase 22) is designed for paid growth, Phases 01–10 must not pre-build or pre-authorize any paid-spend mechanism.
- **Solo-operator, low time/review budget** — `CONFIRMED` (D-019). The design response is now also `CONFIRMED`: favor low-maintenance, high-leverage, automation-heavy designs — batched reviews, templated content, deterministic automation, scheduled digests (D-019a), and automation never removes a required approval gate (D-020). **Both were owner-confirmed directly on 2026-07-28** via Q-010, after Reviewer Finding 5 established they had originally been asserted without owner input. The governing formulation: **automate aggressively within the gates, never through them.**
- **Candidate platforms as directional input only** — `CONFIRMED` (D-017/D-018). Facebook, Instagram, WhatsApp, and TikTok are in scope as *research and scoring candidates* for Phases 08–10. They are not in scope as a locked rollout order, and no account creation or publishing setup for any of them is in scope until Phase 10 selects them and a later phase (11+) executes.
- **Mixed/unranked 90-day objective** — `CONFIRMED` as unranked (D-014). Leads/sales conversion, audience/brand building, and community engagement are all in scope as candidate priorities for Phases 09–10 to weigh; none may be silently treated as "the" priority in near-term deliverables. See OPEN_QUESTIONS.md Q-001.

## Later phases (11–24) — on the plan, explicitly NOT started

Phases 11 through 24 of MASTER_LINEAR_BUILD_PLAN.md — including social presence launch (11), content production (13), publishing adapters (16), community/lead routing (17), analytics (18), paid growth guardrails (22), end-to-end testing (23), and controlled launch (24) — remain part of the overall approved plan but are explicitly **out of scope for near-term execution** as of this Phase 00 gate. `CONFIRMED` per the dependency rule in MASTER_LINEAR_BUILD_PLAN.md ("Each phase depends on the prior phase gate... the overall path remains linear") and the release rule ("No production launch occurs before Phase 23 passes and the owner explicitly approves Phase 24").

Nothing in this SCOPE.md, or in any Phase 00–10 deliverable, authorizes:
- Skipping ahead to any Phase 11–24 activity before its prerequisite phase gate passes.
- Activating paid spend or paid advertising (reserved for Phase 22, and even then only after explicit future activation, not automatic activation at that phase's gate).
- Any production launch (reserved for Phase 24, requiring Phase 23 pass plus explicit owner approval per the release rule).

## Explicitly out of near-term scope (see NON_GOALS.md for full detail)

- Any paid advertising or paid spend (`CONFIRMED` non-goal, D-016).
- Production account creation, publishing, sending, or deployment (prohibited in Phase 00 and not yet reached in Phases 01–10 per the maturity ladder).
- Numeric KPI target-setting (`UNRESOLVED`, D-021/Q-003) — near-term scope defines *what* is measured, not target thresholds.

## Open items that constrain near-term scope

The following unresolved/blocked items (fully detailed in OPEN_QUESTIONS.md) directly gate specific phases within this near-term scope and should be tracked, not silently resolved:
- Q-001 (objective priority) — affects Phase 09, 10.
- Q-004 (Google Drive access) — `BLOCKED`, affects Phase 05 execution (design work can proceed; folder creation cannot).
- Q-006 (brand asset source) — affects Phase 07.
- Q-007 (which Rough-Draft-Builders-Club files are approved fact sources) — affects Phase 06.

## Owner and status

Status: `PROPOSED` — this scope framing (near-term horizon = Phases 01–10, cross-cutting constraints as listed) is the Product Strategist's recommendation for how to bound near-term work. It requires the Phase 00 Owner's integration and the Project Owner's **explicit** acceptance.

Acceptance is explicit or it has not occurred. Silence is not consent: Architecture Rule 7 and `D-007` require explicit owner approval to advance, and `user-guide/USER_INSTRUCTIONS.md` step 10 requires the owner to actively update `CURRENT_PHASE.md`. *(Corrected by the Phase 00 Owner in response to Independent Reviewer Finding 8, which flagged an implicit "acceptance by not objecting" clause as a governance regression.)*
