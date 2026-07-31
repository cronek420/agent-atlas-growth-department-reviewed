# Autonomy Policy

**Owner of this file:** Policy Designer, Phase 03, run `phase-03-2026-07-30-b`.
**Status:** `PROPOSED` policy. The ladder and its transitions are fixed by
`policy/POLICY_CONTRACT.md` §7 and `policy/action_registry.json →
state_machines.autonomy_ladder` and are not this document's to alter; what
this document contributes is the operational **definition** of each stage,
which the source documents name but never define (`D-010` names the six
stages; no governing document says what a capability at any one of them may
actually do).

**Precedence:** as stated in `APPROVAL_POLICY.md` "Precedence" — this
document does not repeat it. Read `APPROVAL_POLICY.md` first; the approval
state machine referenced in §5 below is defined there, not here.

**A note on provenance.** A first Phase 03 attempt (`phase-03-2026-07-30-a`)
drafted a document with this name before the real `CAPABILITY_REGISTRY.md`
existed on this branch and stated, as a load-bearing premise, that promotion
precondition `PP-1` was `BLOCKED` because no registry existed at all. That
premise is now false: `CAPABILITY_REGISTRY.md` exists (141 rows, real
dispositions, `D-037`–`D-039`), and this rewrite states `PP-1`'s actual,
narrower status (§2). See `agent_runs/phase-03/handoffs/HANDOFF_POLICY_DESIGNER.md`
for the full account of why this file was rewritten rather than edited.

---

## 1. The ladder, defined stage by stage

```
DISABLED → SIMULATION → DRAFT_ONLY → APPROVAL_REQUIRED → LIMITED_AUTONOMY → ROUTINE_AUTONOMY
```

Each stage below states what a capability **may** do, what it **may not** do,
and what a promotion out of it would need. These definitions are this Policy
Designer's operational reading of the ladder — `PROPOSED`, built to be
consistent with `D-010`, the fail-closed default (`D-044`), and the nine
gates (`D-011`, `D-020`) — and offered for the Phase Owner to adopt, amend, or
challenge. No governing document defines these stages more precisely than
naming them, so there is no `CONFIRMED` version of this section to defer to.

### `DISABLED`
The capability does not run. No code path for it executes, scheduled or
triggered. It may exist in the repository as code or configuration, but
nothing invokes it against anything — not a test target, not a sandbox, not a
read-only probe of a live external system.
**May:** exist as inert code/config; be discussed, planned, and reviewed.
**May not:** execute, read live external state, or produce any output.
**This is the current stage of every production-facing capability in this
project as of 2026-07-30** (§4).

### `SIMULATION`
The capability runs against synthetic or replayed inputs, with **no network
egress to any real external system** and **no effect that could reach a real
person, account, or public surface**. Think dry-run against fixtures.
**May:** execute its logic end-to-end against test data; log its would-be
actions; be inspected for correctness.
**May not:** make an external network call to a live system (not even
read-only), touch a real account, or produce output a person outside the
project could see.
**Note:** registry row `ACT-P03` (dry-run publish with no network egress) is
`BLOCKED` today because no publishing adapter exists yet (Phase 16) — the
correct first rung exists conceptually, but there is nothing built to occupy
it. `SIMULATION` is defined here so the stage means something the day a
capability is actually built; it is not evidence that any capability can
occupy it today.

### `DRAFT_ONLY`
The capability may act against real external systems **read-only**, or
produce real output artifacts, but nothing it produces reaches an audience,
a recipient, or a live state change without a separate, later step outside
this capability's own autonomy. A `DRAFT_ONLY` content-generation capability
may write a draft post to the repository; it may not post it, schedule it, or
message anyone with it.
**May:** read live external state (subject to `SECURITY_POLICY.md` and the
boundaries in `docs/PROJECT_BOUNDARIES.md`); produce draft artifacts inside
the repository (`ACT-P02` — a draft that reaches no audience is inside the
gates).
**May not:** publish, send, spend, or otherwise cause an external,
observable-by-a-third-party effect. Every one of the nine gated categories
remains fully gated regardless of this stage (`D-020` — the ladder stage
never substitutes for the category gate).

### `APPROVAL_REQUIRED` (ladder stage)
**This name collides with the permission outcome of the same name. See §5 —
read it before applying this stage.** At this ladder stage, the capability
may execute an action that has an `APPROVED` approval record bound to its
exact artifact digest (`APPROVAL_POLICY.md` §2, Invariant 3). It may not
execute anything that has not cleared that specific approval, no matter how
routine or how many times a similar action has been approved before.
**May:** execute individual actions, one at a time, each gated by its own
approval record.
**May not:** execute in a loop, in bulk, or on a schedule without each
individual instance being separately approved; treat a prior approval as
covering a new artifact (Invariant 3 forbids this at the approval-record
level; this stage forbids it at the capability-behavior level too).

### `LIMITED_AUTONOMY`
The capability may execute **some class of pre-approved, bounded actions**
without a fresh per-instance approval — but only within limits the owner set
in advance, and never for anything touching one of the nine gated categories
(`GC-01`…`GC-09`), which stay `APPROVAL_REQUIRED`-or-stricter regardless of
ladder stage (`D-020`). "Limited" names the mechanism (bounded, pre-scoped
autonomy) and the scope (excludes every gated category by construction) at
once.
**May:** execute repeatedly within an owner-defined envelope (e.g., a
narrowly scoped, ungated, previously-demonstrated-safe action) without
per-instance sign-off.
**May not:** touch any of `GC-01`–`GC-09`; expand its own envelope; run
without the dwell-time and incident-threshold guardrails in `PP-5` (§2) —
which, as of this policy, are `UNRESOLVED` (`D-047`), so **no capability is
actually eligible to operate at this stage today** even in principle,
independent of the `PP-1` question in §2.

### `ROUTINE_AUTONOMY`
The highest stage: broad, ongoing, scheduled operation within its scope,
still permanently excluding the nine gated categories. The difference from
`LIMITED_AUTONOMY` is **breadth and standing**, not a relaxation of what is
gated:
- `LIMITED_AUTONOMY` — a narrow, explicitly bounded envelope, likely revisited
  by the owner periodically as trust accrues action-by-action.
- `ROUTINE_AUTONOMY` — the capability is trusted to operate as a standing part
  of the system's normal operation within its (still ungated-only) scope,
  without the owner re-examining each expansion.
Neither stage, at any breadth, ever reaches into `GC-01`–`GC-09`. Autonomy
governs *how often and how independently* an ungated action runs; it never
governs *whether* a gated action needs approval. Those are orthogonal axes,
and this ladder only moves on one of them.

---

## 2. Promotion

**One stage at a time. `OWNER_ONLY`. No skipping.** Registry row `ACT-G01`
grants the `PROMOTE` (up) transition to `PROJECT_OWNER` alone; `ACT-G03`
denies stage-skipping to **every** role, including `PROJECT_OWNER` — the only
row in `policy/action_registry.json` that restricts the owner. This is
deliberate: `D-010` is an architecture rule, and changing it would be an
architecture change (`ACT-W13`), which requires its own recorded decision —
not something a promotion, however well-justified, can do as a side effect.

**Promotion preconditions PP-1 through PP-5**, from `policy/action_registry.json
→ state_machines.autonomy_ladder.promotion_preconditions`:

| ID | Requirement | Status |
|---|---|---|
| PP-1 | The capability has an entry in `CAPABILITY_REGISTRY.md` with use-disposition `PERMITTED` | **`PARTIALLY_SATISFIABLE`** |
| PP-2 | The prior stage was actually exercised, with recorded evidence of the exercise | `CONFIRMED` (as a requirement — not evidence that any exercise has occurred) |
| PP-3 | No unresolved incident is open against the capability | `CONFIRMED` (as a requirement) |
| PP-4 | A Project Owner decision authorizing this specific promotion is recorded in `DECISIONS.md` | `CONFIRMED` (as a requirement) |
| PP-5 | Minimum dwell time at the prior stage, and the numeric error/incident thresholds that block promotion | **`UNRESOLVED`** |

**PP-1 is `PARTIALLY_SATISFIABLE`, and this is the load-bearing correction
this rewrite exists to make.** Unlike the first (discarded) Phase 03 attempt,
`CAPABILITY_REGISTRY.md` now really exists — 141 rows, three real axes,
real use-dispositions (`D-037`–`D-039`). A registry entry existing is
**necessary but not sufficient**. Promotion of any specific capability past
`DISABLED` requires **all three** of the following to hold at once, not just
the first:

1. The capability has an entry in `CAPABILITY_REGISTRY.md` (necessary,
   now satisfiable in principle).
2. That entry's use-disposition is specifically `PERMITTED` — not
   `RESTRICTED`, not `PROHIBITED`, not `UNRESOLVED` (`D-037`).
3. A Project Owner decision authorizing *this specific promotion* is recorded
   in `DECISIONS.md` (this is `PP-4`, restated here because it is not a
   separate gate from `PP-1` — it is part of what "satisfiable" means for
   promotion as a whole).

**Do not read `PP-1` as unlocked.** A registry entry existing, by itself,
unlocks nothing. Most of the registry's 141 rows carry `RESTRICTED` or
`PROHIBITED`, not `PERMITTED` — and even a `PERMITTED` row does not promote
itself; `PP-4`'s recorded owner decision is still required, and `PP-2`/`PP-3`
(prior-stage exercise, no open incident) must also hold. **No promotion has
actually occurred for any capability as of this policy** — §4 states the
current state plainly.

**PP-5 is `UNRESOLVED`, separately, and blocks evaluability regardless of
PP-1–PP-4:** dwell times (how long a capability must sit at a stage before
promotion is even considered) and incident thresholds (how many/what
severity of errors block promotion) are numeric values the owner has not
supplied. `D-021`, `NG-004`, `Q-003`, and `D-047` prohibit inventing them.
**This policy does not propose default numbers.** It states only where each
number belongs (a minimum dwell time per stage transition, and an
incident-count/severity ceiling per capability) and leaves both blank pending
owner input via `Q-003`.

**Consequence of PP-1 and PP-5 together:** even for a capability whose
registry entry is `PERMITTED` and whose prior-stage exercise and incident
history clear `PP-2`/`PP-3`, promotion beyond `SIMULATION` remains
unevaluable until the owner supplies `PP-5`'s numbers. A cleared `PP-1` does
not, by itself, unlock the ladder — it only removes one of several gates.

---

## 3. Demotion and emergency stop

**Any distance, any time, no approval, executable by deterministic code.**
This is the asymmetry that makes the ladder a safety mechanism rather than
just a maturity label: going up is slow and gated; coming down is instant and
ungated.

- **Any distance:** demotion may skip any number of stages in one move —
  `ROUTINE_AUTONOMY` can drop straight to `DISABLED` in a single transition.
  There is no "one stage at a time" rule on the way down, unlike promotion.
- **Any time:** no cooldown, no minimum dwell before a demotion is allowed to
  fire.
- **No approval:** registry row `ACT-G02` grants demotion/emergency-stop
  `ALLOW` (not `APPROVAL_REQUIRED`) to `PHASE_OWNER` and `RUNTIME_AGENT` —
  narrowing needs no sign-off, consistent with the general rule that
  narrowing is always permitted (`docs/PROJECT_BOUNDARIES.md` §7.4).
  `disclosure_required: true` still applies — a demotion must be recorded in
  `findings.md` and disclosed in the gate report, but it is never blocked,
  delayed, or rate-limited pending that disclosure.
- **Executable by deterministic code:** the actor triggering `demote` or
  `demote_or_estop` in the state machine is `DETERMINISTIC_CODE`, not an LLM
  agent's judgment call rendered in prose. An agent may recognize that a
  demotion condition has been met and report it, but the transition itself is
  mechanical, matching Architecture Rule 3 (deterministic code enforces state
  changes).

**Every non-`DISABLED` state has a direct edge to `DISABLED`.** From the
registry's transition list: `SIMULATION`, `DRAFT_ONLY`, `APPROVAL_REQUIRED`,
`LIMITED_AUTONOMY`, and `ROUTINE_AUTONOMY` each have their own
`demote_or_estop → DISABLED` edge. **Emergency stop is always reachable in
exactly one transition, from any stage.**

**Triggers that force automatic demotion** (this Policy Designer's
`PROPOSED` reading, consistent with the registry but not itself a registry
row — the registry defines that the edges exist and are ungated; it does not
enumerate every trigger condition, which is this document's contribution):

- An unresolved incident opens against the capability (violates `PP-3`, which
  is also a promotion precondition — an open incident should pull a
  capability back down, not merely block it from going further up).
- A boundary violation is detected (`ESC-001`, `ESC-004`, `ESC-007`,
  `ESC-008`, `ESC-011` — any escalation code indicating a boundary was
  crossed).
- The autonomy demotion escalation code fires: `ESC-006` is defined
  specifically for "autonomy demotion triggered" — its existence in the
  registry's escalation table is itself evidence that demotion is expected to
  be an event worth naming and disclosing, not a silent internal state
  change.
- A capability's `CAPABILITY_REGISTRY.md` entry changes disposition away from
  `PERMITTED`, or is found stale relative to a re-capture (`D-039`; `Q-013`)
  — losing `PP-1`'s precondition mid-flight should demote, not merely block
  further promotion.

Because no capability is above `DISABLED` today (§4), none of these triggers
currently has anything to act on. They are recorded so the mechanism exists
correctly the day a capability is actually promoted.

---

## 4. Current state

**Every production-facing capability is at `DISABLED` as of 2026-07-30.**
This is a recorded fact, not an assessment:

- `policy/action_registry.json → state_machines.autonomy_ladder →
  current_stage_all_capabilities`: `"DISABLED"`.
- `CLAUDE.md` §13: "Phases 03–24: not started. Nothing is connected,
  deployed, or published by this project, and nothing has been authorized."
- `CAPABILITY_REGISTRY.md` §H ("Recommended target stages") itself
  recommends **no capability in this inventory moves off `DISABLED` during
  Phase 02** — and Phase 03 has not moved any either. The registry's own
  recommendation is that the first legitimate ladder movement belongs to
  capabilities this project builds (e.g., Phase 16's dry-run-first publishing
  adapters entering `SIMULATION`), not to third-party connectors that would
  arrive already able to act.

Nothing in this document changes that. Nothing in this document could —
promotion is `OWNER_ONLY` and, separately, gated on `PP-1`–`PP-5` together
(§2).

---

## 5. The relationship to approval — a genuine vocabulary collision

**`APPROVAL_REQUIRED` names two different things in this project's source
material, and a reader will trip on it if the collision is not called out
explicitly:**

1. **A ladder stage** (this document, §1) — a capability's position on the
   six-stage maturity ladder, one stage above `DRAFT_ONLY`.
2. **A permission outcome** (`policy/action_registry.json →
   outcome_enum.APPROVAL_REQUIRED`, `POLICY_CONTRACT.md` §4) — one of the six
   tokens (`ALLOW`, `ALLOW_LOGGED`, `APPROVAL_REQUIRED`, `OWNER_ONLY`, `DENY`,
   `BLOCKED`) that every individual action in the registry resolves to.
   `D-043` separately distinguishes this outcome from `OWNER_ONLY`
   (`APPROVAL_POLICY.md` §6) — that is a different axis again from the
   ladder-stage-name collision this section addresses.

**These are orthogonal, and neither implies the other:**

- A capability sitting at ladder stage `DISABLED`, `SIMULATION`, or
  `DRAFT_ONLY` can still have individual actions that resolve to the
  permission outcome `APPROVAL_REQUIRED` — indeed, most of the interesting
  actions in `policy/action_registry.json` do, regardless of what stage any
  capability performing them is at, because the nine gated categories are
  gated by category (`D-020`), not by ladder stage.
- A capability sitting at the ladder stage named `APPROVAL_REQUIRED` (§1)
  does not thereby make all of its actions resolve to the permission outcome
  `APPROVAL_REQUIRED` — some of its actions might resolve to `ALLOW` (fully
  ungated, read-only actions, say) while others resolve to `OWNER_ONLY` or
  `DENY` depending on what they touch.
- Conversely, a capability sitting at `ROUTINE_AUTONOMY` — the *most*
  autonomous ladder stage — still has every one of its gated-category actions
  resolve to the permission outcome `APPROVAL_REQUIRED` or `OWNER_ONLY`. The
  ladder stage never overrides the category gate (`D-020`). `ROUTINE_AUTONOMY`
  describes how independently the *ungated* portion of the capability's work
  runs; it says nothing about the gated portion, which stays gated forever.

**Practical rule for anyone applying this policy:** when you see
"`APPROVAL_REQUIRED`" in a document, check which axis it is on before acting.
If it is describing a capability's maturity, it is the ladder stage in §1. If
it is describing what a specific action needs before an agent may execute it,
it is the permission outcome defined in `APPROVAL_POLICY.md` §2, and it never
means "the ladder happens to be at that stage" — an approval record binds to
an artifact digest (`APPROVAL_POLICY.md` §3, Invariant 3), not to a ladder
position.

---

## 6. Composition with `CAPABILITY_REGISTRY.md`'s three axes (`D-048`)

The ladder in this document and the three axes in `CAPABILITY_REGISTRY.md` §
"Vocabularies" (maturity ladder `D-010` — restated here for operational
meaning; implementation class `CLAUDE.md` §3; use-disposition
`PERMITTED`/`RESTRICTED`/`PROHIBITED`/`UNRESOLVED`, `D-037`) answer **different
questions, and `D-048` requires that they not be merged:**

- **Use-disposition** (registry axis 3) answers: **"may this capability be
  used at all, in principle, today?"** This is a gate on *eligibility*. A
  capability dispositioned `PROHIBITED` (e.g. `stripe_api_write`, `C-030`) is
  not a candidate for anything in this document — it cannot be promoted,
  simulated, or drafted with, because the registry has already ruled it out
  regardless of ladder stage.
- **The autonomy ladder** (this document) answers: **"for a capability that
  has already cleared the use-disposition gate, how much autonomy does it
  have to act on its own, without a fresh approval, each time?"** This is a
  gate on *degree of self-direction*, not on eligibility.

**Both gates must clear, in order, before autonomy increases:**

1. First, the registry's use-disposition must be `PERMITTED` (or, for
   `RESTRICTED`, the named condition in `Notes` must actually hold). If
   `PROHIBITED` or `UNRESOLVED`, the ladder question does not even arise —
   there is nothing to promote.
2. Only then does the ladder question apply: at what stage does this
   `PERMITTED` capability currently sit, and does it meet `PP-1`–`PP-5` (§2)
   for the next stage up?

**A capability can be use-disposition `PERMITTED` and ladder `DISABLED` at
the same time** — this is in fact the common case today. `PERMITTED` means
"eligible in principle"; it says nothing about whether anyone has actually
promoted it, exercised the prior stage, or obtained a recorded owner decision
to move it up. Being `PERMITTED` in the registry is `PP-1`'s first
sub-condition (§2), not a substitute for the rest of `PP-1` or for `PP-2`
through `PP-5`.

**The `NOT_PRODUCTION_FACING` sentinel (`D-038`) sits outside this
composition entirely.** A capability marked `NOT_PRODUCTION_FACING` in the
registry's `Ladder` column (e.g. `Read`, `Write`, most harness tools) is not
governed by the `D-010` ladder at all — it cannot publish, send, spend,
deploy, or reach an external system, so asking "what stage is it at" is a
category error, not a `DISABLED` answer. This document's promotion,
demotion, and stage definitions do not apply to `NOT_PRODUCTION_FACING` rows.

**Do not conflate the two axes** the way `D-037` and `D-048` both warn
against: a capability's use-disposition is not evidence of its ladder stage,
and its ladder stage is not evidence of its use-disposition. Each is checked
independently, and both must be checked.

---

## Open items this policy could not resolve

- `PP-1` is `PARTIALLY_SATISFIABLE`, not fully satisfiable — a registry entry
  existing is necessary but not sufficient; disposition `PERMITTED` and a
  recorded `PP-4` owner decision are both still required, per capability.
  No capability has actually been promoted as of this policy.
- `Q-003` / `D-047` — `PP-5`'s dwell times and incident thresholds are
  unassigned numbers, not invented ones. Owner input required before
  promotion beyond `SIMULATION` is evaluable even after `PP-1` clears for a
  given capability.
- §3's list of automatic-demotion triggers is this Policy Designer's
  `PROPOSED` synthesis of the registry's escalation codes and `PP-3`, not a
  verbatim registry list. Flagged for Phase Owner review.
- `Q-013` (should the capability surface be under change control) bears
  directly on `PP-1`: if the registry is allowed to drift silently between
  phase gates, a capability's `PERMITTED` disposition could be stale at the
  moment a promotion decision cites it. This policy does not resolve `Q-013`;
  it notes the dependency.
