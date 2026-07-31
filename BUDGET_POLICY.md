# Budget Policy

**Owner of this file:** Policy Designer, Phase 03, run `phase-03-2026-07-30-b`.
**Status:** `PROPOSED` policy. See `APPROVAL_POLICY.md` "Precedence" — this
document does not repeat it.

**A note on provenance.** A first Phase 03 attempt (`phase-03-2026-07-30-a`)
drafted a document with this name before the real Phase 02 findings
(`F-02-12`, `Q-014`) existed on this branch, and cited a decision ID (`D-042`)
that in the real register names something unrelated (the
`policy/action_registry.json` / `AGENT_PERMISSION_MATRIX.md` generation rule
— the real numeric-invention decision is `D-047`). This is a rewrite against
the real register, not an edit of that draft.

---

## 1. The authorized budget is zero

Not "low." Not "minimal." **Zero.** No amount of spend, of any size, for any
purpose, is authorized today.

**Basis:**
- `D-016` (`APPROVED`, Project Owner): "No paid advertising or paid spend is
  authorized in Phase 00 or the near-term." Owner selected "Organic only for
  now."
- `NG-001`: no paid advertising or spend, `CONFIRMED (prohibition)`.
- No owner decision anywhere in `DECISIONS.md` has changed this. `D-016a`
  (`INFERRED`) extends the hold indefinitely — the owner's phrasing was
  time-qualified ("for now"), and treating that as an open-ended hold rather
  than reading an implicit expiry into it is the fail-closed reading (§3).

Registry row `ACT-M01` ("Spend money in any amount, by any instrument, for
any purpose") resolves to `DENY`, not `OWNER_ONLY` — note this deliberately:
`DENY` outranks `OWNER_ONLY` in the strictness order
(`policy/action_registry.json → strictness_order`;
`policy/POLICY_CONTRACT.md` §4.3) precisely because there is currently no
amount the owner has authorized *anyone*, including themself acting through
the project's tooling, to spend. `OWNER_ONLY` would imply "the owner can do
this personally" — and for entering payment details or authorizing a
specific charge, that is true and is captured separately in `ACT-M04`. But
`ACT-M01` covers spend "in any amount, by any instrument, for any purpose" as
a general capability, and no such general capability is authorized at all.
§4 is the boundary between what an agent may prepare (`ACT-M05`) and what
only the owner may execute (`ACT-M04`).

---

## 2. What counts as spending

This is the section that earns the document. Spending is not only
advertising — that is the mistake this policy is written to prevent, and it
has two real precedents in this project, both worth stating explicitly.

**Precedent one — raising a spend limit is spending, not a workaround.**
Phase 02's own independent review terminated on an account-level monthly
spend limit (`findings.md` `F-02-12`). Every route around it was considered
and rejected, including "raise the limit" — recorded plainly: *"raising the
limit is spending — one of the nine gated categories (D-011), with no spend
authorized at all (D-016, NG-001). An agent raising a spend limit to unblock
its own gate is automating through a gate, the precise thing D-020
forbids."* Registry row `ACT-M02` codifies this as its own clause: "raising
an account spend limit" is listed alongside cloud compute, paid API tiers,
subscriptions, and paid tiers as a spend action, `DENY`, basis `D-016`,
`NG-001`, `F-02-12`. **The correct response to a spend limit blocking a task
is to stop and escalate, not to raise the limit and continue** — exactly
what Phase 02 did, and exactly what this policy requires of every later
phase.

**Precedent two — no phase owns the scheduled-execution host, and that gap
is now urgent.** `README.md` names Google Cloud as the platform for scheduled
automation, but no phase prompt assigns it any deliverable (`findings.md`
`F-01-02`, reproduced independently by Phase 02 as `F-02-08`: "Google Cloud"
appears zero times across all 25 files in `phase-prompts/`). This is tracked
as `Q-014`, and the Phase 02 Owner flagged it as **the single most urgent
open question** left to the Project Owner, because leaving it open silently
reverses `D-019a` (the owner-confirmed "automate aggressively" posture) by
degrading the system to manual, owner-triggered runs without anyone deciding
that. **The reason it belongs in this policy specifically:** resolving *who
owns* the scheduled host does not by itself authorize spending it. Any hosted
scheduler is metered, so deploying one is a spend decision under this policy
regardless of who is assigned to build it. Registry row `ACT-C05` ("Create a
project, enable an API, or deploy a scheduled job on Google Cloud") is
`BLOCKED`, citing `F-01-02` and `Q-014` directly, and remains `BLOCKED` even
after `Q-014` is answered, until a separate spend authorization exists.

**Spending includes, without limitation:**

- **Cloud compute and storage** — a Google Cloud project, a VM, a container
  job, object storage, a database instance.
- **Paid API tiers** — any API plan with a per-call, per-token, or
  per-request charge above a free tier, or any usage that would cross a free
  tier's limit into billing.
- **Subscriptions** — any recurring service fee, monthly or annual, for any
  tool, platform, or service used by this project.
- **Domain and hosting fees** — registering a domain, paying for hosting,
  paying for a CDN or SSL certificate beyond a free offering.
- **Paid tools** — software licenses, paid design/content tools, paid
  research or data tools.
- **Raising an account spend limit** — see precedent one above. This is
  itself a spend action, never a neutral administrative step.
- **Anything that incurs a metered or recurring charge** — the general test:
  if an action would generate a bill, invoice, or recurring charge to any
  payment instrument, it is spending under this policy, regardless of
  whether the word "advertising" or "money" appears anywhere in its
  description.

**A deploy is a spend decision, not merely a technical one** (`ACT-M02`).
This is worth stating as its own rule because "deploy the scheduled job" and
"spend money" read, to an engineer, as different kinds of requests — one
sounds like ops, the other like finance. Under this policy they are the same
gate. An agent proposing "let's deploy X to Cloud Run on a schedule" is
proposing a spend, and must route it exactly as one, even if no dollar figure
was mentioned in the request.

**Registry cross-reference — `ACT-C06`:** storing or retrieving a secret in
Google Secret Manager is `BLOCKED` today, not because of budget alone but
because the Google Cloud project, the `gcloud` SDK, and any credential to
store are all absent (`F-01-02`, `R-13`). `D-046` records that
`SECURITY_POLICY.md` now satisfies the file-existence precondition `D-027`
required before any credential is introduced — but that clears only the
*policy* gate. The *spend* precondition in this document (standing up Secret
Manager is itself a Google Cloud spend decision under this section) and the
*authority* gate (obtaining a credential remains `OWNER_ONLY`) are both
separate, still-unmet gates. Clearing one does not clear the others.

---

## 3. Organic-only posture and its duration nuance

**The prohibition on paid spend is `CONFIRMED`.** **Its indefinite duration
is `INFERRED`**, not `CONFIRMED` — this distinction matters and must not be
collapsed in either direction:

- `D-016`: the owner said "organic only for now." The word "now" is a real
  part of what the owner said and is not this policy's to erase.
- `D-016a`: the fail-closed reading treats the hold as remaining in force
  until an explicit future owner decision changes it — it does not lapse
  automatically at any phase, including Phase 22 (`MASTER_LINEAR_BUILD_PLAN.md`
  Phase 22 scope: "design — but do not initially activate" paid spend
  controls). `D-016a` is `INFERRED`, credited to "Requirements Analyst (Phase
  00), pending Project Owner confirmation" — it has never been upgraded to
  `APPROVED`.

**This policy's obligation is precise: do not harden "for now" into a
false permanence, and do not let it lapse on a guess either.**

- **Do not harden:** never write, in any Phase 03 or later document, that the
  organic-only rule is permanent, indefinite by owner design, or a settled
  brand position. It is a hold, stated with a time qualifier the owner
  actually used.
- **Do not let it lapse:** never write, in any Phase 03 or later document,
  that the hold has an end date, a review date, or that any phase (including
  Phase 22, which explicitly designs-without-activating) automatically lifts
  it. Absent an explicit new owner decision recorded in `DECISIONS.md`, the
  hold continues.

**Phase 22 designs but does not activate.** `R-11` records exactly this
posture: "Phase 22 (Budget Scaling and Paid Growth Guardrails) is explicitly
scoped in the master plan to 'design — but do not initially activate' paid
spend controls. No paid-spend work should occur before Phase 22." Note the
compound condition: even reaching Phase 22 does not itself authorize spend —
Phase 22 builds the guardrails; activating them still requires the explicit
owner decision this section describes. `R-11`'s status is `ACCEPTED` ("no
spend authorized; risk currently dormant") — a risk register status that
itself depends on the organic-only hold continuing to hold, which is exactly
why this section exists.

---

## 4. What agents may do

Agents may prepare; agents may never spend, and agents may never touch the
mechanics of spending.

**Permitted (`ALLOW`):**
- **Prepare costed proposals** showing what a spend would buy, with figures
  that are **sourced and dated**, never invented (`ACT-M05`, basis `D-019a`:
  "automate aggressively" extends to preparing decisions cheaply, not to
  making them). "Sourced and dated" means: state where the number came from
  (a named source, a quote, a published rate card) and when it was checked —
  never a plausible-sounding estimate presented as fact. If no sourced figure
  is available, the proposal says so and leaves the figure blank; it does not
  approximate.
- Model what a hypothetical budget would enable, as a decision aid, clearly
  labeled as hypothetical and non-authorizing.

**Prohibited, absolutely:**
- **Never invent a price.** A costed proposal with a fabricated number is
  worse than one with a blank, because it looks like evidence. This is the
  general invention prohibition (`D-008`, `CLAUDE.md` §6) applied to money
  specifically, and money is exactly the category where a plausible-looking
  wrong number causes the most damage if acted on.
- **Never create an ad account.** Registry `ACT-M03`: creating an ad account,
  boosting a post, or running paid advertising of any kind is `DENY` for
  every agent role, basis `D-016`, `D-016a`, `NG-001`, `R-11`, escalation
  `ESC-007`.
- **Never enter payment details, accept a paid terms-of-service, or authorize
  a charge.** Registry `ACT-M04`: `OWNER_ONLY`, roles `["PROJECT_OWNER"]`
  only, basis `D-011`. This is on the human-checkpoint list in
  `user-guide/USER_INSTRUCTIONS.md` ("Spending") and is never delegated,
  regardless of amount, urgency, or how routine the charge would be.

The line is exact: an agent may tell the owner "this would cost approximately
$X/month, per [source], as of [date]" and stop there. It may not click
"subscribe," may not fill in a card number, and may not accept a paid tier's
terms on the owner's behalf even if the owner has separately said yes in
principle — that "yes" authorizes the owner's own action, not an agent
performing it (`APPROVAL_POLICY.md` §6's `OWNER_ONLY` reasoning applies
directly here).

---

## 5. Structure for when a budget is eventually authorized

This section is deliberately a skeleton. **Every numeric value below is
`UNRESOLVED`, per `D-047`.** `D-047` states plainly why none is filled in: a
plausible-looking default figure would be indistinguishable from an
owner-supplied one a phase later, and inventing one here would repeat
exactly the failure mode `D-021`/`NG-004` exist to prevent. This policy
states **where** each number goes and **what it controls**, and leaves the
value blank until the owner supplies it.

**Spend categories** (structure only — no category is activated by this
policy; activation requires the owner decision in §1/§3):

| Category | What it would cover | Cap | Status |
|---|---|---|---|
| Paid advertising (`GC-09`) | Boosted posts, ad platform spend | `[UNRESOLVED — owner to set]` | Not authorized |
| Cloud infrastructure (incl. scheduled-execution host, `Q-014`) | Compute, storage, scheduled jobs | `[UNRESOLVED — owner to set]` | Not authorized; host ownership itself unresolved |
| Paid API / SaaS tiers | Any usage-based or tiered paid service | `[UNRESOLVED — owner to set]` | Not authorized |
| Domain / hosting | Registration and hosting fees | `[UNRESOLVED — owner to set]` | Not authorized |
| Paid tools / licenses | One-off or recurring tool purchases | `[UNRESOLVED — owner to set]` | Not authorized |

**Approval path for a future authorized spend** (structure only): a spend
proposal is a `WRITE` to `REPO_SELF` under `ACT-M05` (`ALLOW` — preparing the
proposal), which must then pass through the full approval state machine
defined in `APPROVAL_POLICY.md` §2 — `DRAFT → PENDING_APPROVAL → APPROVED` —
before any agent may act on it, and even an `APPROVED` spend proposal cannot
authorize an agent to execute the charge itself (`ACT-M04` remains
`OWNER_ONLY` regardless of approval state; approval and agency are separate
axes, exactly as `APPROVAL_POLICY.md` §6 describes for `OWNER_ONLY` vs
`APPROVAL_REQUIRED` generally). The owner performs the actual transaction
personally once a proposal is `APPROVED`.

**A hard stop:** whatever cap the owner eventually sets per category (table
above), the structural expectation is that the system enforces a **hard**
ceiling — a spend proposal exceeding the category cap does not get evaluated
as "how much over," it is out of bounds entirely, the same fail-closed logic
already governing every other boundary in this project (`D-044`: unmatched
actions resolve to `DENY`). The exact mechanism (a monitored total, a
per-transaction check, an alert threshold below the hard cap) is
implementation the owner and a later phase would specify; this policy states
only that a hard stop is the required shape, not a soft "flag and continue."

---

## 6. Detection and escalation

**`ESC-007`** — "Spend or cost-incurring action attempted" — is the
escalation code for this entire policy (`policy/action_registry.json →
escalation_codes`, `policy/POLICY_CONTRACT.md` §9). Every `DENY`/`BLOCKED` row
in the registry touching money or metered infrastructure (`ACT-M01`,
`ACT-M02`, `ACT-M03`, `ACT-C05`, `ACT-C06`) carries this escalation code or a
prerequisite-missing code (`ESC-003`) that routes to the same handling.

**What to do when any action would incur cost:**

1. **Stop before executing.** Do not proceed on the theory that the cost is
   small, one-time, or easily reversed — `ACT-M01`/`ACT-M02` do not carry a
   size exception. This includes the specific case Phase 02 already lived
   through: a spend limit blocking a task is not a problem to route around
   by raising the limit (`F-02-12`).
2. **Classify it** against §2 — is this advertising (`GC-09`), general
   spending (`GC-08`), or both? Either way it is gated.
3. **Escalate as `ESC-007`** — record in `findings.md` (per the specialist's
   handoff, not written directly by a specialist to the register) and flag
   in the current handoff's "Open questions" / "Failures or risks" section
   what the cost-incurring action was and why it was about to happen.
4. **Prepare, do not perform.** If a costed proposal is useful to the owner's
   eventual decision, prepare one per §4 — sourced, dated, clearly marked as
   a proposal, not an authorization.
5. **Never treat proceeding as the safe default because stopping would block
   a task.** Being blocked is the correct outcome (`docs/PROJECT_BOUNDARIES.md`
   §7.2). A blocked task is reported with the exact owner action required,
   never worked around by spending anyway.

This mirrors the general escalation posture in `APPROVAL_POLICY.md` §9:
escalation itself is never gated, never rate-limited, and never suppressed —
an agent that hits a spend boundary can always report that it did, even
though it can never cross it.

---

## Open items this policy could not resolve

- `D-016a`'s indefinite-duration reading remains `INFERRED`, not `APPROVED`
  — an explicit owner decision would resolve it either way (confirm the
  indefinite hold, or set an actual review point). Not this Policy Designer's
  call to make.
- `D-047` — every numeric cap in §5's table is unassigned. The owner must
  supply per-category figures (or explicitly decline to set any yet) before
  any spend category can move off "not authorized."
- `Q-014` (who owns the scheduled-execution host) is unresolved and, per the
  Phase 02 Owner, the single most urgent open question in the project —
  leaving it open silently reverses `D-019a`. This policy does not resolve
  it; it notes that resolving *ownership* still would not by itself
  authorize the *spend* a hosted scheduler requires (§2).
