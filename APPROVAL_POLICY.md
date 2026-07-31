# Approval Policy

**Owner of this file:** Policy Designer, Phase 03, run `phase-03-2026-07-30-b`.
**Status:** `PROPOSED` policy — structurally complete, not yet operable in every
respect (see §7, §11). Nothing in this document authorizes any agent to do
anything beyond what `policy/action_registry.json` already grants; this
document explains and justifies those grants.

**Precedence:** `README.md`, `DECISIONS.md`, `docs/PROJECT_BOUNDARIES.md`,
`INTAKE_RECORD.md` govern. `CLAUDE.md` restates them. `policy/POLICY_CONTRACT.md`
fixes the vocabulary this document uses. `policy/action_registry.json` is the
machine-readable source of truth; where this document and the registry
disagree, that is a defect to be raised, not silently reconciled
(`POLICY_CONTRACT.md` §1).

**A note on provenance, because it matters here specifically.** A first Phase
03 attempt (`phase-03-2026-07-30-a`) drafted a document with this same name
against a stale pre-merge `main`, before the real `CAPABILITY_REGISTRY.md` and
the real `D-036`–`D-040` existed on this branch. That attempt was discarded by
explicit Project Owner direction (`findings.md` `F-03-01`) but its uncommitted
files were not removed from disk by the branch reset — `git reset --hard` does
not delete untracked files — and were found sitting in this working tree,
citing decision IDs (`D-038`, `D-040`, `D-042`) that collide with real,
differently-scoped rows. This document is a full rewrite against the real
register (`D-041`, `D-043`–`D-048`; `Q-012`–`Q-017`; `R-20`–`R-24`), not an edit
of that draft. See `agent_runs/phase-03/handoffs/HANDOFF_POLICY_DESIGNER.md`
"Assumptions" for the full account.

This is the keystone policy: `AUTONOMY_POLICY.md` and `BUDGET_POLICY.md` both
reference the approval states defined here.

---

## 1. The nine gated categories

Source: `README.md` "Primary success criteria"; `D-011` (`APPROVED`); registry
IDs `GC-01`…`GC-09`. Every action touching one of these resolves to
`APPROVAL_REQUIRED`, `OWNER_ONLY`, or (today, because the underlying production
capability does not yet exist) `DENY` or `BLOCKED` — never `ALLOW` or
`ALLOW_LOGGED` — under `D-020` (owner-confirmed: "gates always win",
`INTAKE_RECORD.md` Q-010a).

**Read this before the category definitions below.** As implemented in
`policy/action_registry.json` *today*, most concrete actions in these nine
categories resolve to `DENY`, not `APPROVAL_REQUIRED` — see `ACT-P05` (publish
content touching a gated category → `DENY`) and `ACT-S01` (send to a real
person → `DENY`, gated categories `GC-05`/`GC-06`). This is not a weaker gate;
it is a stricter one. `APPROVAL_REQUIRED` means "the agent executes once
approved" — but no publishing, messaging, or spend-executing capability exists
yet (`D-036`, `CLAUDE.md` §13), so approval is not even the missing
ingredient — the capability itself is absent or unauthorized. The distinction
in `D-043` (`APPROVAL_REQUIRED` vs `OWNER_ONLY`, §6 below) presumes a
capability that could execute; today's `DENY` rows are a fail-closed default
one level stricter than either (`D-044`; strictness order in
`policy/POLICY_CONTRACT.md` §4.3: `DENY` > `BLOCKED` > `OWNER_ONLY` >
`APPROVAL_REQUIRED` > `ALLOW_LOGGED` > `ALLOW`). When a later phase builds a
production capability in one of these categories, the registry row for its
specific execution action is expected to become `APPROVAL_REQUIRED` — that
row does not exist yet, and this policy does not invent it.

An operator with no lawyer and a low time budget needs a boundary they can
apply in under a minute. Each category below is defined by what counts and
what does not, with a worked example and counterexample.

### GC-01 — Claims
**Counts:** any external-facing statement asserting a fact about the product,
service, business, capability, or outcome a customer should expect — "we
finish projects in 6 weeks," "our materials are locally sourced," "99% of
clients recommend us."
**Does not count:** internal notes, draft language never intended to leave the
repository (`ACT-P02` — a draft that reaches no audience is inside the gates,
not through them), or a question posed to the owner ("should we claim X?").
**Basis:** `D-011`.

### GC-02 — Pricing
**Counts:** any statement of a price, rate, package cost, or fee schedule
intended for an external audience, and any change to an existing published
price.
**Does not count:** a costed internal proposal prepared for the owner's
decision (`ACT-M05` — costing a decision is not making it; see
`BUDGET_POLICY.md` §4).
**Basis:** `D-011`.

### GC-03 — Discounts
**Counts:** any offer of a reduced price, promotional code, bundled deal, or
"limited time" incentive aimed at an external audience.
**Does not count:** an internal proposal modeling what a discount program
might cost or return.
**Basis:** `D-011`.

### GC-04 — Testimonials
**Counts:** any customer quote, review, before/after example, case study, or
third-party endorsement used in external content.
**Does not count:** research notes summarizing publicly available reviews for
internal competitive analysis, provided they are not republished as this
project's own testimonial content.
**Basis:** `D-011`.

### GC-05 — Direct outreach
**Counts:** any business-initiated message to a specific, identifiable real
person outside the project — cold DM, cold email, personalized comment
soliciting a response, connection request.
**Does not count:** publishing routine scheduled content to a general
audience (that is `GC-09`/`ACT-P01` territory, not outreach), or an agent
drafting outreach copy for the owner to send personally (`ACT-S02`).
**Basis:** `D-011`; registry `ACT-S01`.

### GC-06 — Complaints
**Counts:** any response — public or private — to a customer complaint,
negative review, or dispute.
**Does not count:** internally logging that a complaint was received (not a
response to the complainant).
**Basis:** `D-011`.

### GC-07 — Controversial topics
**Counts:** content that takes a position on politics, religion, social or
cultural disputes, or any subject where a reasonable reader would expect the
business to have deliberately weighed reputational risk before speaking —
including content that is not obviously "political" but touches a live public
dispute (e.g., a construction-industry regulatory fight, a local zoning
controversy, a labor dispute in the trades).
**Does not count:** general educational or how-to content about the business's
actual craft (construction methods, project management, home-improvement
tips) that does not stake a position on a live public dispute. The test is
not "could someone somewhere disagree" — almost anything clears that bar —
it is "does this take a side in a dispute the business did not start and does
not need to settle."
**Where the boundary is genuinely unclear:** treat it as `GC-07` and escalate
(`ACT-E01`). Escalation is free and never gated; guessing wrong is not.
**Basis:** `D-011`.

### GC-08 — Spending
**Counts:** any action that would spend money or incur a metered/recurring
cost. Fully defined in `BUDGET_POLICY.md`, which this policy defers to for
the specifics of what counts as spend.
**Basis:** `D-011`; `D-016`; `NG-001`.

### GC-09 — Paid advertising
**Counts:** any paid promotion, boosted post, sponsored placement, or ad
account activity of any kind.
**Does not count:** organic (unpaid) publishing — subject to its own gates
under `PUBLISHING_POLICY.md`, not this category.
**Basis:** `D-011`; `D-016`; `NG-001`.

---

## 2. The approval state machine

Reproduced exactly from `policy/action_registry.json →
state_machines.approval` and `policy/POLICY_CONTRACT.md` §6. A deterministic
checker (`tools/policy_check.py`) validates conformance to this machine. **No
state or edge may be added, removed, or renamed by any policy document,
including this one.**

**States:** `DRAFT` · `PENDING_APPROVAL` · `APPROVED` · `CHANGES_REQUESTED` ·
`REJECTED` · `EXPIRED` · `WITHDRAWN` · `EXECUTED` · `SUPERSEDED` · `VOIDED`

**Initial state:** `DRAFT`. **Terminal states:** `REJECTED`, `EXPIRED`,
`WITHDRAWN`, `EXECUTED`, `SUPERSEDED`, `VOIDED`.

| From | To | Actor | Trigger |
|---|---|---|---|
| `DRAFT` | `PENDING_APPROVAL` | `PHASE_OWNER` | `submit` |
| `DRAFT` | `WITHDRAWN` | `PHASE_OWNER` | `withdraw` |
| `PENDING_APPROVAL` | `APPROVED` | `PROJECT_OWNER` | `owner_approves` |
| `PENDING_APPROVAL` | `REJECTED` | `PROJECT_OWNER` | `owner_rejects` |
| `PENDING_APPROVAL` | `CHANGES_REQUESTED` | `PROJECT_OWNER` | `owner_requests_changes` |
| `PENDING_APPROVAL` | `EXPIRED` | `DETERMINISTIC_CODE` | `staleness_timer` |
| `PENDING_APPROVAL` | `WITHDRAWN` | `PHASE_OWNER` | `withdraw` |
| `CHANGES_REQUESTED` | `DRAFT` | `PHASE_OWNER` | `revise` |
| `APPROVED` | `EXECUTED` | `DETERMINISTIC_CODE` | `execute_once` |
| `APPROVED` | `EXPIRED` | `DETERMINISTIC_CODE` | `validity_window_elapsed` |
| `APPROVED` | `VOIDED` | `DETERMINISTIC_CODE` | `artifact_digest_mismatch` |
| `APPROVED` | `SUPERSEDED` | `PROJECT_OWNER` | `owner_replaces` |

Notes an operator will want, read directly off the table above:

- **The only door into `APPROVED`** is `PENDING_APPROVAL → APPROVED`, and its
  only key is held by `PROJECT_OWNER`. There is no other edge, from any state,
  to `APPROVED`, anywhere in this machine.
- `CHANGES_REQUESTED` is not a dead end — it loops back to `DRAFT` via
  `revise`, so an agent may fix and resubmit rather than starting a new
  approval record from nothing.
- Once `APPROVED`, an artifact moves only by deterministic code
  (`execute_once`, `validity_window_elapsed`, `artifact_digest_mismatch`) or by
  the owner explicitly superseding it — never by an agent's judgment call.

---

## 3. The five invariants

Reproduced from `policy/action_registry.json → state_machines.approval →
invariants` and `POLICY_CONTRACT.md` §6. None is negotiable by any Phase 03
document, including this one.

1. **The only transition into `APPROVED` is `PENDING_APPROVAL → APPROVED`, and
   its only permitted actor is `PROJECT_OWNER`.**
   Why: this is the entire safety model of the project in one rule. Every
   other invariant exists to keep this one from being circumvented — through a
   timer, a default, a second approver, or a clever reading of silence.

2. **Silence is never consent. No timer, default, or absence of response may
   produce `APPROVED`. A staleness timer may only produce `EXPIRED`.**
   Why: the owner is a solo operator with a low time budget (`D-019`,
   `R-01`). Without this rule, the exact pressure that makes review slow —
   volume exceeding available time — would create an incentive to let
   unreviewed items auto-approve. This rule removes that incentive
   structurally rather than relying on discipline. See §7 for what happens
   when the owner is actually unavailable.

3. **An approval binds to one artifact digest. Any change to the artifact
   voids it.**
   Why: "approved" must mean "approved as I saw it," not "approved in
   spirit." Without digest binding, an approved draft could be silently
   edited after the fact and executed under an approval the owner never saw.
   The registry encodes this as the `artifact_digest_mismatch → VOIDED` edge
   (`ACT-A02` requires quoting what the owner actually approved).

4. **An approval is single-use. `EXECUTED` is terminal; no second execution
   may claim the same approval.**
   Why: one approval, one action. Reusing an approval for a second execution
   — even of what looks like "the same thing" — would let one review stand in
   for work the owner never saw. If the same action needs to happen again, it
   needs its own approval record and its own review.

5. **No actor may approve what it authored (`D-006`, `ACT-A03`).**
   Why: this is the general independent-review rule (`D-006`, Architecture
   Rule 6) applied to approvals specifically. Self-approval collapses the
   review it is supposed to provide. Registry row `ACT-A01` denies the
   `APPROVE` action to every agent role without exception — this is not a
   role-specific restriction that could be lifted for a trusted agent, it is
   structural: **no agent role holds the `APPROVE` transition at all.** Only
   `PROJECT_OWNER` does, and the Project Owner does not author agent work
   product, so the conflict cannot arise on the approver's side either.

---

## 4. What an approval request must contain

`D-019a` ("automate aggressively") does real work here: the owner's low
review budget is a reason to make each review *cheap*, never a reason to make
it *optional* (`D-020`). A request packet an operator can decide on in under
a minute must contain, at minimum:

1. **What is being asked** — one sentence, plain language, no jargon.
2. **Which gated category** (`GC-01`…`GC-09`) it falls under, and why.
3. **What changes if approved** — the concrete, external-facing effect.
4. **Reversal cost** — how hard this is to undo if it turns out to be wrong
   (compare `DECISIONS.md`'s own `APPROVED_IMPL` rows, which state reversal
   cost as a matter of practice — the same discipline applies here).
5. **The exact artifact digest** being approved, so the binding in Invariant 3
   is meaningful and checkable.

A packet missing any of these five is not reviewable and should not be
submitted (`submit` should not fire on an incomplete packet). This is a
structural requirement on the request format; it does not by itself specify a
digest algorithm, a packet file format, or a queue implementation — those are
build decisions for whichever phase implements the approval queue (Phase 15
per `MASTER_PLAN.md`; not a Phase 03 deliverable).

---

## 5. Batching and digests

Batching is **permitted and encouraged** (`D-019a`, `D-020`). Precisely what
it may and may not do:

**Batching may:**
- Group multiple similar requests into one review session.
- Template repeated request shapes so only the variable content needs
  attention.
- Pre-fill request packets with everything in §4 already computed.
- Schedule reviews into a digest (e.g., "this week's requests") rather than
  interrupting the owner per-item.
- Summarize a batch at the top level, provided the summary is a navigation
  aid to the individual items, not a substitute for seeing them.

**Batching may never:**
- Let one approval cover an artifact the owner did not individually see.
  A batch approval must still **bind to each artifact's digest individually**
  (Invariant 3 applies per-item, not per-batch) — approving a batch means
  approving N digests, not approving "the batch" as an opaque unit.
- Convert several `PENDING_APPROVAL` records into one `APPROVED` record. Each
  item transitions on its own; a batch is a review-time convenience, not a
  new state-machine object.
- Reduce what is shown per-item below the five elements in §4 for the sake of
  fitting more into a batch. Cheap review means fast to read, not thin.
- Apply to different gated categories as if they were one decision. A batch
  may contain items from multiple `GC-` categories, but the packet must still
  make each item's category legible — an owner scanning a mixed batch must be
  able to tell claims from pricing from outreach at a glance.

Note who may even reach this stage: `SEND_MESSAGE`/`PUBLISH` execution
capability for the nine categories is `DENY` or `BLOCKED` today (§1) because
no such production capability exists (`D-036`). Batching rules govern the
*eventual* approval queue's design, per `Phase 15`; they do not imply any
approval requests exist to batch yet.

---

## 6. `OWNER_ONLY` vs `APPROVAL_REQUIRED`

Fixed by `D-043` (`APPROVED_IMPL`) and `POLICY_CONTRACT.md` §4.1. This is a
genuine collision in the source vocabulary — `README.md` calls the nine
categories "approval"-gated, and `user-guide/USER_INSTRUCTIONS.md` calls a
different, overlapping list "human checkpoints" — and `D-043` resolves it by
splitting on **who acts**, not on how important the action is:

- **`APPROVAL_REQUIRED`** — the **agent executes**, once an approval record
  reaches `APPROVED` bound to the exact artifact digest. The missing
  ingredient is a decision, and once supplied, an agent may act on it.
- **`OWNER_ONLY`** — the **owner executes**, personally, always. Approval is
  not the missing ingredient here — agency is. An agent may prepare materials
  (a filled-in form, a drafted message, a summarized decision) but may never
  perform the act itself, with or without any approval record.

**The full human-checkpoint list**, quoted from `user-guide/USER_INSTRUCTIONS.md`
"Human checkpoints" and mapped to registry rows:

| Checkpoint | Resolution | Registry row |
|---|---|---|
| Platform terms acceptance | `OWNER_ONLY` | `ACT-C11` |
| Captchas | `OWNER_ONLY` | `ACT-C11` |
| Identity and phone verification | `OWNER_ONLY` | `ACT-C10` |
| Production OAuth consent | `OWNER_ONLY` | `ACT-C09` |
| Account creation submission | `OWNER_ONLY` | `ACT-C10` |
| Product claims | `APPROVAL_REQUIRED` in design; `DENY` today (§1) | `ACT-P05` (publish) is `DENY`; no drafting-only row is gated — drafting is `ALLOW` under `ACT-P02` |
| Testimonials | `APPROVAL_REQUIRED` in design; `DENY` today (§1) | `ACT-P05`, `GC-04` |
| Pricing and discounts | `APPROVAL_REQUIRED` in design; `DENY` today (§1) | `ACT-P05`, `GC-02`/`GC-03` |
| Direct outreach | `APPROVAL_REQUIRED` in design; `DENY` today | `ACT-S01`, `GC-05` |
| Responses to complaints | `APPROVAL_REQUIRED` in design; `DENY` today | `ACT-S01`, `GC-06` |
| Paid advertising | `DENY` — absolutely, not merely pending approval | `ACT-M03`, basis `D-016`/`NG-001` |
| Spending | `OWNER_ONLY` for the transaction itself; `DENY` for any agent-initiated spend | `ACT-M04` (owner enters payment/authorizes charge); `ACT-M01`/`ACT-M02` (agent spend) |
| Major brand changes | No dedicated registry row exists yet. Covered by the absolute-prohibition list (`CLAUDE.md` §6: "change brand identity") and the fail-closed default (`D-044`) — an unmatched action is `DENY`. Reasoned as `OWNER_ONLY`-equivalent by direct analogy to the other irreversible human-only acts on this list, since no capability to change brand identity is built or authorized | none yet — gap noted, not filled |
| Production deployment | Covered by `CLAUDE.md` §6 ("deploy production resources") as an absolute prohibition; no dedicated `ACT-` row exists because no production deployment capability is built. `D-044` fail-closed default applies: `DENY` | none yet — gap noted, not filled |
| Public launch | `DENY` | `ACT-P01` |
| Recording a gate decision (PASS/CONDITIONAL PASS/FAIL) | `OWNER_ONLY` | `ACT-A05` |

**Reading this table correctly:** six of the nine `README.md` gated categories
(claims, testimonials, pricing, discounts, outreach, complaints) are, by
architectural intent, `APPROVAL_REQUIRED` — an agent may eventually execute
them once a specific artifact is `APPROVED` — while the human-checkpoint items
that are genuinely `OWNER_ONLY` (terms, captchas, identity, OAuth, account
creation, the payment/charge act itself, gate decisions) are acts an agent may
never perform regardless of any approval record. **Today, every one of the
six "eventually `APPROVAL_REQUIRED`" categories still resolves to `DENY`** in
`policy/action_registry.json`, because the production capability to execute
them (a publishing adapter, a messaging adapter) does not exist (`D-036`).
This is not a contradiction — `DENY` is the correct fail-closed answer to "may
an agent do this today," and the `APPROVAL_REQUIRED` design intent is what a
future phase's registry row is expected to carry once the capability is built
and the approval queue (Phase 15) exists to enforce Invariant 3 against it.

---

## 7. Owner unavailability

**`Q-008` is resolved (`D-050`, 2026-07-30).** Of the three options, the Project
Owner delegated the choice to the Phase 03 Owner ("use logic") rather than
picking one directly. Option **(c)** was selected — the same outcome `D-045`'s
interim rule already enforced:

> **All gated work halts** when the Project Owner is unavailable. No backup
> approver exists. No auto-approval on timeout exists. A staleness timer may
> only move an approval to `EXPIRED` (Invariant 2).

**Why (c) and not (a) or (b).** Option (a) requires naming a real person with
authority to approve claims, pricing, spending, and outreach on the business's
behalf — no such person is named anywhere in this project, and inventing one
would violate the absolute prohibition on inventing approvals (`CLAUDE.md`
§6). Option (b) requires a numeric auto-pause threshold, which `D-047`
forbids inventing. Option (c) requires no invented fact and was already this
project's operating default — resolving `Q-008` formalized it rather than
changed it.

This remains operationally costly — `R-01` and `R-02` stay `MONITORING`, not
`MITIGATED`, for exactly this reason — but the alternative was guessing a name
or a number, which `D-020` and Invariant 2 both forbid regardless of cost.

**This is not permanent.** Naming a specific backup approver or a specific
numeric auto-pause threshold at any future date supersedes `D-050` outright —
nothing about this resolution locks the door, it only declines to guess
what's behind it.

**Escalation:** owner unavailability with gated work outstanding is
`ESC-010` (`policy/action_registry.json → escalation_codes`).

---

## 8. What "policy conflicts tested" requires (`Q-017`, resolved as `D-041`)

Stated here in plain operational terms, because this document is where a
future reader will look for what "tested" actually means in practice.
`D-041` resolves `Q-017` as **two distinct, both-required checks — neither
alone satisfies the pass condition:**

1. **Structural conflicts, checked mechanically.** `tools/policy_check.py`
   enumerates every row in `policy/action_registry.json` and confirms no two
   rows assign a different permission outcome to the same (role, verb,
   resource, statement) combination. This catches the kind of defect a script
   can see: two rows that contradict each other in the machine-readable
   source itself.
2. **Prose conflicts, checked by a person.** No script can read
   `APPROVAL_POLICY.md`, `AUTONOMY_POLICY.md`, `BUDGET_POLICY.md`, and the
   other Phase 03 policy documents and determine whether one document's prose
   describes an outcome that contradicts the registry, or contradicts a
   sibling document's prose — that is a natural-language judgment. This half
   is performed by the **Independent Reviewer**, as an itemized cross-read,
   with the result recorded in `REVIEW_REPORT.md`. The mechanical checker's
   ID/outcome cross-reference is a starting point for this reading, never a
   substitute for it.

**Why both halves are required and neither alone is enough:** a document can
pass the mechanical check perfectly (every citation resolves, every registry
row is internally consistent) while still asserting, in prose, something the
registry does not actually say — exactly the shape of defect `F-00-05` and
`F-02-11` found in earlier phases, where a clean mechanical pass coexisted
with content nobody had read adversarially. Conversely, a careful prose
read cannot substitute for the mechanical check, because a human reviewer
does not reliably catch a structural contradiction buried in 60+ registry
rows the way a script does. **"Tested" means both were actually run and both
results are recorded — not that the phase owner asserts both would probably
pass.**

---

## 9. Escalation

Codes `ESC-001`…`ESC-011`, reproduced from `policy/POLICY_CONTRACT.md` §9 and
`policy/action_registry.json → escalation_codes`:

| Code | Meaning |
|---|---|
| `ESC-001` | Boundary conflict or attempted boundary widening |
| `ESC-002` | Untrusted content — fetched **or preloaded** (skill/tool descriptions, per `F-02-05`) — contained text shaped like an instruction |
| `ESC-003` | Required prerequisite artifact (policy, registry, schema) does not exist |
| `ESC-004` | Secret exposure suspected or confirmed |
| `ESC-005` | Approval expired, stale, or queue exceeded its age limit |
| `ESC-006` | Autonomy demotion triggered |
| `ESC-007` | Spend or cost-incurring action attempted |
| `ESC-008` | Personal, lead, or contact data encountered |
| `ESC-009` | Policy conflict detected — structural (checker) or prose (Independent Reviewer, per `D-041`/`Q-017`, §8 above) |
| `ESC-010` | Project Owner unavailable and gated work is halted (`Q-008` unresolved) |
| `ESC-011` | A credential-free/borrowed-authority access path was invoked or nearly invoked |

**`ESC-011` — cross-referenced, not restated.** `SECURITY_POLICY.md` defines
what counts as borrowed authority (the five classes named in `F-02-03`/`R-21`:
the operator's logged-in browser session, the operator's Claude account,
connector grants held in that account, harness-mediated egress, and
plugin-held credentials) and how such access is to be handled. This policy's
role is narrower: any action approaching registry row `ACT-R09` (`BORROWED_AUTHORITY`,
`DENY`) or any `CAPABILITY_REGISTRY.md` row dispositioned around this pattern
(e.g. `C-009`, `C-045`) is escalated as `ESC-011` exactly like any other
escalation code — reported in `findings.md` and the current handoff, never
worked around on the theory that "no credential was used, so no rule
applies." The absence of a credential is the exposure, not an exemption
(`F-02-03`).

**Escalation is never gated (`ACT-E01`).** Being blocked is a correct
outcome; reporting it must always be possible, at any autonomy stage, in any
approval state, regardless of queue depth or owner availability. Registry row
`ACT-E01` grants every role `ALLOW` on escalating via `OPEN_QUESTIONS.md`, a
handoff, `findings.md`, or the gate report — with no approval precondition
attached, by design.

Note the boundary on this: `ACT-E02` (escalating to the owner by any channel
*outside this repository*) is `BLOCKED` — no messaging capability exists yet,
and separately `Q-015` (may the system notify the owner at all) is
unresolved, so the repository and the phase report are, today, the only
escalation channel that actually exists. This is a capability gap, not a
policy choice; it resolves to `ESC-003` (missing prerequisite), not to
silence.

---

## 10. Gate decisions

Recorded by the **Project Owner**, never an agent (`ACT-A05`, `D-006`,
`D-007`). A phase-gate report **recommends**; it does not decide. This is
structural, not a courtesy: `CLAUDE.md` §7 states gate decisions belong to
the owner, and registry row `ACT-A05` grants the `PASS`/`CONDITIONAL
PASS`/`FAIL` transition to `PROJECT_OWNER` alone, with no agent role listed.

**Silence is never consent** here either — the same Invariant 2 language
applies by direct analogy. A phase does not become passed because nobody
objected to the gate report; it becomes passed when the Project Owner records
that it has.

**Worked example — Phase 02's own gate, recorded exactly this way.** The
Project Owner recorded a **CONDITIONAL PASS** for Phase 02 on 2026-07-29,
with one named condition (independent review completed and its findings
addressed or explicitly accepted). The review later returned 21 findings and
a rubric score below the `D-028` threshold; four High/Medium findings remain
unremediated (`R-24`, tracked and left open — not this phase's to resolve, per
`policy/POLICY_CONTRACT.md` §2.7). The point this example illustrates for
this policy, and the only point it is cited for here: **the gate report
recommended a course of action, and the owner's recorded decision — not the
report's recommendation — is what actually moved the phase forward.** The
report's job was to inform the decision, not make it.

**A second worked example — preparing, never executing, a human checkpoint.**
Registry row `ACT-C02b` (`CONNECT` / `EXT_GITHUB` / "Merge a pull request into
main") resolves to `APPROVAL_REQUIRED`, with a note that this phase itself
obtained explicit Project Owner direction before merging a pull request — a
shared-state, hard-to-reverse action visible to the owner and any
collaborator. The general pattern the row now records: an agent may prepare
a merge, a deploy, or any other consequential shared-state action completely,
right up to the point of executing it, and still must not cross that last
step without the owner's explicit go-ahead recorded somewhere durable. This
is the same shape as `OWNER_ONLY` reasoning (§6) applied to an action that is
technically `APPROVAL_REQUIRED` rather than reserved to the owner's own
hands — the owner directs; the agent, once directed, executes.

---

## 11. Failure handling

| Failure mode | Handling |
|---|---|
| **Approval expires** (`PENDING_APPROVAL → EXPIRED` via `staleness_timer`, or `APPROVED → EXPIRED` via `validity_window_elapsed`) | Terminal. A new request must be submitted from `DRAFT`; the expired record is not reactivated. Escalate as `ESC-005` if the expiry reflects a systemic queue-age problem rather than a one-off. **The staleness window itself is an unassigned number** — `D-047` prohibits inventing it; it is owner input, tracked at `Q-003`. |
| **Artifact changes after approval** (`APPROVED → VOIDED` via `artifact_digest_mismatch`) | Terminal, automatic, and requires no human judgment call — Invariant 3 makes this deterministic: if the digest does not match, the approval does not apply, full stop. A new request must be submitted for the changed artifact. |
| **Approval claimed twice** (an attempt to execute against an already-`EXECUTED` approval) | Structurally prevented by Invariant 4 — `EXECUTED` is terminal, and the state machine has no outbound edge from it. Any code path that attempts a second `execute_once` against a terminal state is a defect in that code, not a valid use of this policy, and should be treated as `ESC-009` (policy conflict detected). |
| **Queue ages out** (many items sit in `PENDING_APPROVAL` past a reasonable window, e.g. because the owner is unavailable) | Do not auto-approve, ever, regardless of volume (Invariant 2). Follow §7 — if the cause is owner unavailability, this is `ESC-010`; if the cause is volume alone, revisit batching per §5 rather than relaxing the gate. The exact "reasonable window" is another `D-047` blank pending owner input. |
| **Owner rejects or requests changes** | `REJECTED` is terminal — a rejected request does not get silently resubmitted; a materially new request starts fresh from `DRAFT`. `CHANGES_REQUESTED` loops back to `DRAFT` via `revise`, permitting exactly the artifact the owner critiqued, with an evident chain of custody. |
| **Withdrawal** | The submitting side (`PHASE_OWNER`) may withdraw from `DRAFT` or `PENDING_APPROVAL` at any time — this is a narrowing action (fewer things pending) and needs no owner approval, consistent with the general rule that narrowing is always permitted. |

---

## Open items this policy could not resolve

- ~~`Q-008` (backup approver / owner-unavailability posture)~~ — **resolved**
  2026-07-30, `D-050`; see §7. Revisable if the owner later names a backup
  approver or a numeric threshold.
- `Q-003` / `D-047` — every numeric value this policy would need (staleness
  windows, queue-age limits) is a blank, not a guess. Named in §11, not
  invented.
- `Q-017`'s resolution (`D-041`, §8) requires the Independent Reviewer to
  actually perform the prose cross-read this phase — this document states
  what is required, not that it has already happened. Confirm before the
  gate report claims this pass condition met.
- §6's mapping of "product claims / testimonials / pricing / outreach /
  complaints" onto design-intent `APPROVAL_REQUIRED` (currently `DENY` in
  practice) is this Policy Designer's reading of how `D-043` composes with
  the fail-closed default (`D-044`). It is `PROPOSED`, not confirmed by the
  owner under that name, and is flagged for the Phase Owner in the handoff.
