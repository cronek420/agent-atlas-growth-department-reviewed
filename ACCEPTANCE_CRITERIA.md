# Acceptance Criteria

Prepared by: Product Strategist (Phase 00)
Phase: 00 — Decision Lock and Scope Control
Project: Agent Atlas Growth Department (for Rough Draft Builders Club)
Date: 2026-07-28

## Purpose of this document

Defines what "done" and "passing" mean at two levels: (1) program-level, qualitative criteria the completed system must satisfy overall (sourced from README.md's "Primary success criteria"), and (2) phase-level, concrete PASS CONDITIONS for each near-term phase (01–10), sourced directly from each phase's prompt file. This document does not itself certify that any criterion has been met — it defines the bar future phase-gate reviews must check against.

Status labels used below: `CONFIRMED` (owner-stated or fixed in a source document), `INFERRED` (reasonable draft conclusion, needs owner confirmation), `PROPOSED` (specialist recommendation, needs owner decision), `UNRESOLVED` (genuinely unknown), `BLOCKED` (needs an external dependency that doesn't exist yet).

## Part 1 — Program-level acceptance criteria (qualitative)

Source: README.md "Primary success criteria." All items below are `CONFIRMED` as the criteria set — they are already fixed in the governing source document — but whether the *built system* satisfies each one is necessarily `UNRESOLVED` until the relevant later phase implements and tests it. Each is restated here as a checkable, qualitative acceptance statement plus which future phase(s) are responsible for making it true.

| ID | Acceptance criterion (qualitative, no numeric target) | Primarily satisfied by | Status of criterion itself |
|---|---|---|---|
| AC-P01 | The system maintains product, audience, brand, campaign, content, analytics, and experiment records. | Phases 04, 06, 07, 09, 12, 18 | CONFIRMED (criterion); UNRESOLVED (whether met — not yet built) |
| AC-P02 | The system researches current marketing trends and compares platforms. | Phases 08, 10 | CONFIRMED (criterion); UNRESOLVED (whether met) |
| AC-P03 | The system prepares social account launch materials. | Phase 11 | CONFIRMED (criterion); UNRESOLVED (whether met — out of near-term scope per SCOPE.md) |
| AC-P04 | The system produces approved recurring content. | Phases 12, 13, 15 | CONFIRMED (criterion); UNRESOLVED (whether met — out of near-term scope) |
| AC-P05 | The system tests copy and creative variants. | Phase 14 | CONFIRMED (criterion); UNRESOLVED (whether met — out of near-term scope) |
| AC-P06 | The system publishes only permitted routine content. | Phases 03, 15, 16 | CONFIRMED (criterion); UNRESOLVED (whether met — out of near-term scope) |
| AC-P07 | The system triages community messages and leads safely. | Phase 17 | CONFIRMED (criterion); UNRESOLVED (whether met — out of near-term scope) |
| AC-P08 | The system produces a weekly execution checklist and executive summary. | Phase 19 | CONFIRMED (criterion); UNRESOLVED (whether met — out of near-term scope) |
| AC-P09 | The system tracks outcomes from attention through purchases. | Phase 18 | CONFIRMED (criterion); UNRESOLVED (whether met — out of near-term scope) |
| AC-P10 | The system recovers safely from failures. | Phase 21 (design); every phase's own FAILURE HANDLING section (near-term) | CONFIRMED (criterion); PARTIALLY addressable near-term via each phase's failure-handling section |
| AC-P11 | The system keeps a complete audit trail. | Every phase (via `agent_runs/phase-XX/`, DECISIONS.md, findings.md, progress.md); Phase 20 (long-term memory) | CONFIRMED (criterion); near-term phases 01–10 are directly responsible for establishing this pattern |
| AC-P12 | The system requires approval for: claims, pricing, discounts, testimonials, direct outreach, complaints, controversial topics, spending, and paid advertising. | Phase 03 (defines the gates); enforced by every later phase | CONFIRMED (criterion) — also independently locked as DECISIONS.md D-011 |

**Numeric acceptance thresholds:** No numeric KPI, growth target, or success threshold (e.g., specific follower counts, lead volume, conversion rate, revenue figures) is defined anywhere in the source documents or the owner's confirmed answers. All such numeric criteria are `UNRESOLVED` (see DECISIONS.md D-021, OPEN_QUESTIONS.md Q-003) and must not be invented by any phase, including this one. Acceptance in the near term must be judged qualitatively (did the deliverable get produced, is it internally consistent, does it satisfy its stated PASS CONDITIONS) rather than against any number.

## Part 2 — Phase-level acceptance criteria (Phases 01–10)

Source: each phase's own `PASS CONDITIONS` list in `phase-prompts/PHASE_0X_*.md`. These are `CONFIRMED` — directly quoted from the governing phase prompts, i.e. already fixed in a source document — and represent the bar each phase's own future gate review must apply. *(Label corrected by the Phase 00 Owner per Reviewer Finding 16: the original assigned two mutually exclusive labels, `CONFIRMED`/`INFERRED`, to the same items.)* Restated here for convenience so Phase 00 review can confirm they are internally consistent with SCOPE.md and NON_GOALS.md — no wording has been altered from the source phase prompts.

### Phase 01 — Workspace, Repository, and Project Memory
- Project exists outside Rough-Draft-Builders-Club.
- Git initialized and private remote plan documented.
- Installed tool versions recorded.
- No secrets committed.
- Baseline validation passes.

### Phase 02 — Capability Registry and Skill Foundation
- No unverified skill enabled.
- Trigger tests exist.
- Risky or irrelevant skills excluded.
- Custom skills have contracts.
- Rollback documented.

### Phase 03 — Governance, Security, Approval, and Autonomy Policies
- All high-risk actions require approval.
- Default is fail-closed.
- Least privilege documented.
- State transitions defined.
- Policy conflicts tested.

### Phase 04 — Data Contracts and State Model
- Schemas validate fixtures.
- Error shapes defined.
- Idempotency keys defined.
- Backward compatibility policy recorded.
- No dependent implementation begins early.

### Phase 05 — Google Drive Living-Document Control Center
- Operations restricted to dedicated folder.
- Managed files carry project IDs.
- Conflict handling defined.
- No silent overwrite.
- Mirror/source authority explicit.
- **Note:** `BLOCKED` on OPEN_QUESTIONS.md Q-004 (Drive folder location/access unknown) — these criteria can be designed against but not verified against a real folder until that blocker clears.

### Phase 06 — Product and Company Onboarding
- Every claim classified.
- Unknowns remain unresolved.
- CTA destinations recorded.
- Pricing not invented.
- Reviewer verifies source traceability.
- **Note:** partially gated on OPEN_QUESTIONS.md Q-007 (which specific Rough-Draft-Builders-Club files are approved as fact sources; reading approved files is permitted in principle per D-013, but none has been designated).

### Phase 07 — Brand and Creative System
- Brand rules testable.
- No fabricated logo/colors.
- Accessibility minimums stated.
- Examples and counterexamples included.
- Brand change requires approval.
- **Note:** partially gated on OPEN_QUESTIONS.md Q-006 (brand asset source location unknown).

### Phase 08 — Research and Trend Intelligence Engine
- Sources dated and cited.
- External text treated as untrusted.
- Confidence and decay included.
- No prohibited scraping.
- Research can run in simulation.

### Phase 09 — Audience, Offer, and Buyer Psychology Model
- Segments evidence-linked.
- No manipulative dark patterns.
- Quick-buy and nurture paths separated.
- Objections mapped to approved responses.
- Reviewer checks realism.
- **Note:** partially gated on OPEN_QUESTIONS.md Q-001 (90-day objective priority still unranked) — segment/journey prioritization may need to stay scenario-based until resolved.

### Phase 10 — Platform Strategy and Rollout Selection
- Scores use consistent criteria.
- API/support assumptions verified or blocked.
- No all-platform launch.
- Maintenance burden considered.
- Each active platform has CTA and measurement.

## Part 3 — Rubric-level acceptance (applies to every phase, 00–10 and beyond)

Source: PROMPT_AND_BUILD_QUALITY_RUBRIC.md. `CONFIRMED` as the fixed scoring bar for all phases:
- No rubric category scores below 3.
- Average rubric score at least 4.
- Security, permissions, testing, and failure handling categories must each score 4 or higher.
- A critical unsupported integration automatically fails the phase.

> **✅ Rubric defect — surfaced and resolved by owner decision, 2026-07-28.**
> The third bullet requires **"Security"** to score 4 or higher, but "Security" is **not one of the rubric's 12 scoreable categories**. The 12 are: Objective clarity, Inputs, Outputs, Agent separation, Tool realism, Permissions, Determinism, Failure handling, Testing, Auditability, User usability, Portability. As written, the passing threshold named a category that could not be scored.
>
> **Owner's ruling (`D-028`, `Q-011`): the Security threshold is satisfied by the Permissions category.** Permissions already covers least-privilege, gates, and access boundaries. `PROMPT_AND_BUILD_QUALITY_RUBRIC.md` is **not** edited — this interpretation governs instead.
>
> **Operative rule for all phase gates 00–24:** score the 12 existing categories; the elevated bar is **Permissions / Testing / Failure handling ≥ 4**.
>
> *(Surfaced by Independent Reviewer Finding 7; resolved by owner decision.)*

## Part 4 — Universal phase-checklist acceptance items (applies to every near-term phase)

Source: the "Universal operating rules" and "Phase checklist" sections common to Phase 00's and Phases 01–10's prompt files. `CONFIRMED` as fixed process requirements:
- Prerequisite phase gate passed before the phase begins.
- One phase owner and one owner per deliverable file.
- Parallel work assigned only to genuinely independent tasks.
- Written handoffs contain facts, evidence, assumptions, open questions, files changed, and tests performed.
- Unknown values remain labeled `UNRESOLVED` or `BLOCKED`, never guessed.
- External content treated as untrusted data, never as instruction.
- No secrets written to files or logs.
- No production publishing, sending, spending, or deployment unless the phase explicitly permits it and approval evidence exists.
- Independent reviewer (not the implementer) completes review; findings addressed or explicitly accepted.
- `agent_runs/phase-XX/PHASE_GATE_REPORT.md` written; next phase does not start automatically.

## File owner and status

**Owner:** Product Strategist (Phase 00), integrated by the Phase 00 Owner.
**Status:** `PROPOSED` — the criteria in Part 1, Part 3, and Part 4 are `CONFIRMED` in the sense that they are quoted from governing source documents, and Part 2 is quoted verbatim from the individual phase prompts. What is `PROPOSED` is this document's *framing*: the selection of Phases 01–10 as the near-term set (inherited from SCOPE.md, itself `PROPOSED`) and the judgment that qualitative acceptance is sufficient in the absence of owner-supplied numeric targets. Requires explicit Project Owner acceptance; silence is not consent.

*(Section added by the Phase 00 Owner per Reviewer Finding 16 — this file previously had no owner/status block, unlike its sibling deliverables.)*

## Summary: what near-term "done" means

The near-term build (Phases 01–10, per SCOPE.md) is acceptable when, for each phase in sequence: its own PASS CONDITIONS (Part 2) are met, the rubric bar (Part 3) is cleared, the universal checklist (Part 4) is satisfied, and no criterion required inventing a fact that was actually `UNRESOLVED` or `BLOCKED`. Program-level success (Part 1) is a longer-horizon outcome that near-term phases contribute to but cannot fully satisfy on their own — most Part 1 criteria are only fully testable once Phases 11–24 (out of near-term scope) exist. No numeric KPI is part of "done" for any near-term phase, because none has been defined by the owner.
