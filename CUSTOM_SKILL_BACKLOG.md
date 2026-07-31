# Custom Skill Backlog

**Owner of this file:** Agent Architecture Specialist (Phase 02 specialist, second pass), run `phase-02-2026-07-29-a`.
**Status:** **INTEGRATED.** Phase 02 deliverable of record, accepted by the Phase 02 Owner 2026-07-29. *(Corrected 2026-07-29 per Independent Reviewer finding — this file self-declared as "not yet an integrated deliverable" while being one of the six deliverables the gate report certified.)*

**Two inputs, joined here:**

- **Demand** — `agent_runs/phase-02/handoffs/HANDOFF_AGENT_ARCHITECTURE_SPECIALIST.md` (first pass): 61 capability needs `N-01`…`N-61` derived from the phase prompts alone, deliberately blind to this machine.
- **Supply** — `CAPABILITY_REGISTRY.md` (141 rows, `PERMITTED` 23 / `RESTRICTED` 31 / `PROHIBITED` 86 / `UNRESOLVED` 1), itself sourced from `agent_runs/phase-02/evidence/SESSION_CAPABILITY_INVENTORY.md`.

Cited below as `HANDOFF §n` and by registry row (`C-0nn`) respectively.

---

## What this file is, and what it is not

**It is a specification backlog.** Every entry is `PROPOSED`, at maturity-ladder
stage `DISABLED` (`D-010`, `CLAUDE.md` §3). **Nothing here is authorized to be
built by Phase 02.** Phase 02 specifies; later phases build. Nothing in this file
enables, installs, or permits anything.

**It is not a list of names.** Phase 02's pass condition is *"Custom skills have
contracts"*, and a contract with a missing field is a failed pass condition, not
a partial one. Each entry carries all twelve required fields (§2).

**It is not an inventory of what exists.** Not one of the seven exists. Where an
entry says a component "returns" or "must never", read it as a specification in
the imperative, not a description of behaviour observed. No capability named here
was invoked, loaded, enabled, installed, or tested to produce this file (§10).

---

## 1. Identifiers

`HANDOFF §Assumptions.6` states plainly that `CS-01`…`CS-07` were local to that
document and reserved no namespace. This file registers them.

**Scheme:** `CSK-nn`, zero-padded, allocated sequentially, never reused. A
withdrawn entry keeps its number and gains status `REJECTED`. The register of
record for these IDs is this file; `DECISIONS.md`, `SKILL_TEST_PLAN.md`, and
`MASTER_PLAN.md` cite them, they do not mint them.

| Registered ID | First-pass ID | Name |
|---|---|---|
| `CSK-01` | `CS-01` | `blast-radius-check` |
| `CSK-02` | `CS-02` | `schema-validate` |
| `CSK-03` | `CS-03` | `untrusted-envelope` |
| `CSK-04` | `CS-04` | `claim-guard` |
| `CSK-05` | `CS-05` | `gate-router` |
| `CSK-06` | `CS-06` | `dry-run-publisher` |
| `CSK-07` | `CS-07` | `cycle-runner` |

Rejected candidates are numbered in the same space from `CSK-90` upward (§8), so
that a rejection can be cited and cannot be silently re-proposed under a new
number.

---

## 2. Contract fields — all twelve are mandatory

| Field | What it must state |
|---|---|
| **Name** | The invocation name. Stable; changing it is a decision. |
| **Purpose** | One sentence. What decision or artifact it produces. |
| **Trigger** | The condition under which it fires, and whether firing is optional. |
| **Inputs (typed)** | Named fields with types. |
| **Outputs (typed)** | Named fields with types, including every verdict token. |
| **Preconditions** | What must be true before it runs. |
| **Postconditions** | What is guaranteed true after a successful run. |
| **Failure modes** | Each named failure and the verdict it produces. Every one fails closed. |
| **Negative contract** | "Must never" — the list that makes it a control rather than a helper. |
| **Owning phase / first-needed phase** | Which phase builds it; which phase first cannot proceed without it. |
| **`D-003` classification** | `DET`, `LLM`, or `SPLIT` with the split line stated. |
| **Supply join** | Do-not-build / must-be-custom / blocked-by-disposition. **New in this pass.** |

---

## 3. The join — what knowing the supply side changed

The first pass could not use the word "gap"; it had no supply model. This section
is the reconciliation, and it is the only genuinely new analysis in this file.

### 3.1 The one-line summary per skill

| ID | Do NOT build (adequate supply exists) | Genuinely custom | Blocked by a registry disposition? |
|---|---|---|---|
| `CSK-01` | Change enumeration and diffing (`git` via `C-003`/`C-004`); file reading (`C-001`); output formatting | The fixed register list, the falsification judgement, the fail-closed verdict, the recorded disposition of every candidate | **No** |
| `CSK-02` | The JSON Schema validation engine — use a library | Version resolution, the standard error shape, the no-mutation guarantee | **Partly.** `C-003`'s recorded condition is *"No installs"* — acquiring the library is not permitted under the registry as written. See §3.3 |
| `CSK-03` | HTTP transport (`C-028`/`C-029`) | The envelope shape, the provenance triple, the policy verdict, the no-sanitize rule | **Partly.** Web ingestion only. Every richer ingestion path is `PROHIBITED`; the inbound-message envelope has no permitted channel at all. See §3.4 |
| `CSK-04` | Nothing. No supply row substitutes for any part of it | All of it | **No** |
| `CSK-05` | Escalation channel (`C-008`); operator notification (`C-024`) | The nine categories, the ladder check, the fail-closed default, the approval record | **No** (repo-authoritative store); the Sheet mirror is `Q-004` `BLOCKED` |
| `CSK-06` | Nothing | The four-precondition gate and the dry-run renderer | **Yes, the live branch.** There is no `PERMITTED` outbound write path in 141 rows. See §3.5 |
| `CSK-07` | Report rendering and charting (`C-083`, `C-096`, `C-127`) | The lock, the run record, the resume point, the carry-forward ledger | **Yes, the unattended trigger, and the delivery.** Every scheduler in the inventory is `PROHIBITED`; both of Phase 19's delivery channels are `PROHIBITED`. See §3.6 |

**No skill was dropped and none was merged.** Four were rescoped, two of them
materially. That is the honest result, and §3.3–§3.6 are where the value is.

### 3.2 The finding that reframes all seven: "skill" is a packaging word

`D-003` reserves permissions, state changes, calculations, deduplication,
scheduling, and publishing to **deterministic code**. A Claude Code skill is a
Markdown instruction document that an LLM reads and follows. **For six of the
seven entries, implementing them as skill documents would violate `D-003` on the
day they are built**, because the enforcement would be LLM-mediated: an
instruction document cannot refuse.

The registry supports the distinction rather than contradicting it. `C-097`
(`skill-creator`) is `PERMITTED` / `NEEDED` and is described there as authoring
**project-owned** skills with contracts and evals — the preferred alternative to
installing third-party skills. `C-081` (`find-skills`) is `RESTRICTED` to
discovery, never install. So authoring is blessed; what is authored still has to
satisfy `D-003`.

Each entry below therefore states an **artifact form**:

- **`COMPONENT`** — deterministic code in the repository, invoked by script. The verdict is the code's.
- **`DOCUMENT`** — a skill document; the LLM is the actor. Legitimate only where the output is a proposal with no authority.
- **`COMPONENT + thin DOCUMENT`** — deterministic component, plus a short skill document whose only job is to tell an agent when to invoke it and forbid working around it.

**Where these files live is unresolved.** No phase prompt names a home for
project-owned skill or component source; `MASTER_PLAN.md` places the first
`tests/` directory at Phase 13; `HANDOFF OQ-2` already records that Phase 04's
fixtures have no home either. Placing them under `.claude/skills/` would put
phase deliverables inside harness-configuration territory — the precise collision
`F-00-09` and `D-032` are about. Recorded as **`OQ-P2-3`** in §9; not resolved
here.

### 3.3 `CSK-02` — the library the first pass told us to use may not be installable

`HANDOFF §4` was right that the validation engine is off-the-shelf and that
writing one would be waste. The supply side adds a constraint it could not see:
`C-003` (`Bash`) and `C-004` (`PowerShell`) are `RESTRICTED` with the recorded
condition *"local operations only… **No installs**, no `curl` to third-party
endpoints."*

So the registry, as accepted, permits neither `npm install` nor `pip install`.
Phase 04's first pass condition — *"Schemas validate fixtures"* — depends on a
validator this project is not currently permitted to acquire.

Three defensible resolutions exist and **none of them is mine to pick**:
extend `C-003`'s condition to cover pinned, reviewed, lock-filed dependencies;
route runtime dependencies through `SKILL_INSTALLATION_PLAN.md` (a Phase 02
deliverable I do not own, which today reads as covering skills rather than
libraries); or accept a vendored, licence-reviewed validator committed to the
repository. Recorded as **`OQ-P2-1`**. Until it is answered, `CSK-02` is
`PROPOSED` with an **unresolved dependency-acquisition path** — not "probably
fine because everyone installs libraries."

### 3.4 `CSK-03` — the transport narrows, and the envelope cannot close the whole boundary

**Narrowing.** The first pass specified transport generically. Supply says the
only ingestion capability this project may condition its way into is
`C-028`/`C-029` (`WebFetch`, `WebSearch`) — `RESTRICTED`, ladder `DISABLED`, four
conditions, the fourth of which is *"no research corpus is assembled before Phase
08 builds the untrusted-content boundary."* Everything richer is `PROHIBITED`:
`C-119` (Bright Data acting skills — also a metered, billed service, so use is
spending under `D-011`), `C-120` (proxy), `C-071`/`C-132` (tinyfish, which *acts
on* sites), `C-045` (the operator's real Chrome, no carve-out even for reads).
Inbound message channels are `PROHIBITED` too: `C-039` (Gmail read),
`C-126` (`resend:agent-email-inbox`).

**Consequence:** design `CSK-03` against `WebFetch`/`WebSearch` and nothing else.
An envelope designed around a scraping provider's response shape would be built
against a capability this project may not use, and would have to be rebuilt.
The inbound-message envelope (`N-38`, Phase 17) has **no permitted channel today**
and is specified but `BLOCKED`.

**The part the envelope cannot cover — and this is the more important half.**
`CSK-03` wraps content that passes through a *retrieval*. `SESSION_CAPABILITY_INVENTORY.md`
§7 and `CAPABILITY_REGISTRY.md` §I finding 3 document a class of external text
that never passes through one: **third-party skill and MCP tool descriptions,
loaded into every session's context unchanged and unreviewed at session start.**
`C-121` (`bright-data-mcp`) is quoted asserting *"No exceptions"* and *"MUST
replace WebFetch and WebSearch"* — third-party text directing agent tool
selection. `C-116`, `C-135`, `C-085`, `C-087`, and `C-054` are documented as
modifying this project's own contract, configuration, permissions, or filesystem
grants.

`D-009` covers these — they are data, not instruction — but **`CSK-03` cannot
enforce it**, because there is no boundary to interpose: the text is already in
context before any agent acts. The control is a policy and a review step, not a
component. That belongs to `SKILL_SECURITY_POLICY.md`, a Phase 02 deliverable I
do not own. **Routed there explicitly in §9 (`OQ-P2-2`) so it is not lost in the
gap between two documents.**

### 3.5 `CSK-06` — the live branch is `BLOCKED`, not merely unbuilt

Every outbound write path in the inventory is `PROHIBITED`: `C-030`
(`stripe_api_write`), `C-038` (Gmail drafts), `C-041` (Calendar writes/invites),
`C-045` (browser-driven action), `C-057`/`C-125` (Resend), `C-059` (Klaviyo),
`C-060` (Intercom), `C-061` (Slack), `C-112` (`marketing:email-sequence`),
`C-115` (the entire ads namespace). **There is no `PERMITTED` outbound write path
in 141 rows.**

Compounding it: authentication state is `UNRESOLVED` for every connected server
(`Ev §0` Limit 3, registry §C header), and `SECURITY_POLICY.md` does not exist
(`D-027`), so no credential may enter this project at all (`CLAUDE.md` §10).

**Rescope, and it is a clean one:** `CSK-06` splits at its own `dry_run` flag.

- **The dry-run branch is fully buildable and fully testable today.** It renders the exact request, opens no socket, and the "no socket opened" assertion is the strongest thing in this backlog that can actually be asserted before Phase 16.
- **The live branch is `BLOCKED`.** It is specified — the four preconditions, the idempotency-before-request ordering, the do-not-retry-blind-on-timeout rule — and it may not be built against any adapter target, because every target is prohibited and none is authenticated.

This is better news than it sounds. It means Phase 16 can build and prove the
*gate* without ever holding a credential, and the ladder's `SIMULATION` stage
(`D-010`) is exactly the stage that describes it.

### 3.6 `CSK-07` — the scheduler gap is not an absence, it is nine prohibitions

`HANDOFF §6` framed the Google Cloud gap as *nothing owns the execution host*.
Supply sharpens it into something more useful and more uncomfortable:

**Nine scheduling capabilities are present on this machine right now, and this
project's own rules prohibit every one of them.** `C-011` (`ScheduleWakeup`),
`C-017` (`CronCreate`/`CronDelete`), `C-025` (`RemoteTrigger`), `C-043`
(`create_job`), `C-048`/`C-049` (`scheduled-tasks` write/delete), `C-090`
(`loop`, `schedule`), `C-101` (`anthropic-skills:schedule`), `C-141`
(`ralph-loop`). The basis is consistent across all of them: `D-003` assigns
scheduling to deterministic code, `D-007` forbids a phase resuming itself, and
`D-027` means no `AUTONOMY_POLICY.md` exists to govern unattended execution.
Meanwhile `C-064` records Google Cloud as `PROHIBITED` and `BOUNDARIES` §3 records
it as `NOT CONNECTED` with **no phase owning it**, and `F-01-02` records that
`gcloud` is not installed.

**The operational instruction that follows is sharper than "open OQ-1":**
`OQ-1` must not be resolved by reaching for one of the nine. They are present,
they are one `ToolSearch` call away (`C-007`), and each would deliver unattended
execution while bypassing the ladder entirely. **The gap is a governance gap, and
a prohibited capability sitting within reach is the shape a governance gap takes.**

Two `RESTRICTED` read-only rows are useful and should be used: `C-018` (`CronList`)
and `C-050` (`list_scheduled_tasks`), each carrying the registry's note that the
one legitimate use is *confirming that no scheduled task targets this project*.
That is a test, and it is specified as `T-POS-07` in `SKILL_TEST_PLAN.md`.

**Delivery is blocked on both channels too.** Phase 19's pass condition names
*"Email and Drive delivery independently retryable."* Email: `C-057`/`C-125`
(Resend) and `C-038` (Gmail) are all `PROHIBITED`, and `HANDOFF §7` / `OQ-3`
records that the send prohibition has no owner carve-out. Drive: `Q-004` is the
project's only `BLOCKED` item. So Phase 19 currently has **zero permitted
delivery channels**, where the first pass identified only the email half.
`C-008` (`AskUserQuestion`, `PERMITTED`) and `C-024` (`PushNotification`,
`RESTRICTED`, operator device only) are the two channels that reach the owner
without a prohibition — and `C-024` carries the registry's own warning that
**a notification is not an approval**.

**Rescope:** `CSK-07`'s manual and `SIMULATION` half is buildable, including the
full timezone logic with an injected clock. The unattended trigger and both
delivery channels are `BLOCKED`.

---

## 4. The seven entries

Ordered by first-needed phase, which is also the recommended build order (§6).

---

### `CSK-01` — `blast-radius-check`

**Status:** `PROPOSED` · **Ladder:** `DISABLED` · **Artifact form:** `COMPONENT + thin DOCUMENT`

**Purpose.** Enumerate files from *prior* phases whose factual claims the current
phase's work has made untrue, before the gate report is written.

**Trigger.** Once per phase, after the last deliverable is written and **before**
`PHASE_GATE_REPORT.md` is drafted. Also on demand. Non-optional: a gate report
written without it is missing a required input.

**Inputs.**
`{ phase_id: string, changed_files: string[], baseline_ref: git-ref, clock: ISO-8601 }`
Fixed inputs, not caller-supplied: `RISK_REGISTER.md`, `OPEN_QUESTIONS.md`,
`DECISIONS.md`, `CURRENT_PHASE.md`, `MASTER_PLAN.md`, `README.md`, `CLAUDE.md` §13,
`CAPABILITY_REGISTRY.md`.

**Outputs.**
`{ candidates: [{ file: string, line: int, quoted_claim: string, why_possibly_false: string, confidence: "HIGH"|"MEDIUM"|"LOW" }], checked: string[], unreadable: string[], verdict: "CLEAN"|"REVIEW_REQUIRED" }`
A report only.

**Preconditions.** A clean working tree relative to `baseline_ref`; every fixed
input exists and is readable; every path resolved lies inside the project root.

**Postconditions.** No file is modified. Every fixed input appears in `checked` or
in `unreadable`, never in neither. `verdict == "CLEAN"` implies `unreadable` is
empty.

**Failure modes.** Missing or unreadable input → `REVIEW_REQUIRED` naming the
file, never `CLEAN`. Unresolvable git ref → hard fail with the exact error, no
verdict. Zero candidates → `CLEAN`, with `checked` still complete. Path resolving
outside the project root → hard fail before reading.

**Negative contract — must never.** Edit any file it inspects. Return `CLEAN`
when any input was unreadable. Substitute for the phase owner's judgement — its
output is a proposal, and **the phase owner records the disposition of every
candidate including the rejections**. Read, stat, list, or check timestamps on
`C:\Users\crone\Projects\Rough-Draft-Builders-Club` — `F-01-07` is the case where
a check written to prove a boundary was respected became the breach of it. Be
confused with `C-135` (`claude-md-improver`) or `C-098` (`consolidate-memory`),
both `PROHIBITED`: those rewrite governance files, this one only reports on them.

**Owning phase / first needed.** Phase 03 builds it. First needed: **Phase 03** —
the first phase after `F-01-09` was written.

**`D-003`.** `SPLIT`. Deterministic enumeration of candidate claims; LLM judgement
of falsification; **the phase owner decides.** The LLM never sets `verdict`.

**Supply join.** *Do not build:* change enumeration and diffing — `git` through
`C-003`/`C-004`; file reading — `C-001`; any output formatter beyond Markdown.
*Custom:* the fixed register list, the falsification rubric, the fail-closed
verdict, the disposition record. *Blocked:* no. Both dependencies are `RESTRICTED`
with conditions this component satisfies by construction (project root only, local
only, no network).

---

### `CSK-02` — `schema-validate`

**Status:** `PROPOSED` · **Ladder:** `DISABLED` · **Artifact form:** `COMPONENT`

**Purpose.** Validate a data instance against a versioned project schema and
return the project's standard error shape.

**Trigger.** Every read or write of any entity typed by a `schemas/*.schema.json`.
Non-optional at every producer boundary from Phase 13 onward, **including in
dry-run**.

**Inputs.** `{ instance: object, schema_id: string, schema_version: semver | "latest" }`

**Outputs.**
`{ valid: boolean, errors: [{ pointer: json-pointer, keyword: string, message: string, code: string }], schema_version_used: semver }`

**Preconditions.** The named schema exists at the named version and parses.

**Postconditions.** `valid: true` implies the instance satisfies every constraint.
The instance is returned byte-identical — no coercion, no default-filling, no
trimming, no key reordering. `schema_version_used` is always a concrete semver,
never `"latest"`.

**Failure modes.** Unknown `schema_id` or version → hard fail, never "valid by
default". Malformed schema → hard fail naming the **schema**, not the instance.
`"latest"` resolving ambiguously (two candidates, or none) → hard fail; silently
guessing a version changes a contract. Absent or empty instance → `valid: false`.

**Negative contract — must never.** Repair an instance to make it valid.
Downgrade an error to a warning. Emit `valid: true` for an absent instance. Be
bypassed by any producer, including in dry-run. Accept a verdict from an LLM —
`C-127` (`data:validate-data`, `RESTRICTED`) may inform schema *authoring* and may
never issue `valid: true` (`D-003`).

**Owning phase / first needed.** Phase 04 builds it. First needed: **Phase 04** —
*"Schemas validate fixtures"*, `HANDOFF §3`'s first pass condition in the whole
plan that cannot be satisfied by prose.

**`D-003`.** `DET`, fully.

**Supply join.** *Do not build:* the JSON Schema validation engine. *Custom:*
version resolution, the standard error shape (`D-004`'s *"Error shapes defined"*),
the no-mutation guarantee. *Blocked:* **partly — the dependency-acquisition path
is unresolved.** `C-003`'s condition reads *"No installs"*, so neither `npm
install` nor `pip install` is permitted under the registry as accepted. See §3.3
and `OQ-P2-1`. Do not treat this as a formality: the alternative is writing a
validator, which is the one thing the first pass explicitly said not to do.

---

### `CSK-03` — `untrusted-envelope`

**Status:** `PROPOSED` · **Ladder:** `DISABLED` · **Artifact form:** `COMPONENT`

**Purpose.** Wrap every piece of externally-sourced content in a structurally
tagged envelope so no downstream directive can confuse it with instruction.

**Trigger.** Every retrieval of content originating outside this project. No
exceptions, no trusted-source allowlist.

**Inputs.** `{ source_uri: string, retrieved_at: ISO-8601-with-offset, transport_status: int|string, raw_bytes: bytes }`

**Outputs.**
`{ envelope_id: string, source_uri: string, retrieved_at: ISO-8601-with-offset, content_sha256: string, byte_length: int, truncated: boolean, payload: opaque-tagged, policy_verdict: "ALLOWED"|"REFUSED", refusal_reason?: string }`
`payload` is addressable as data only and is never inlined into a directive
channel.

**Preconditions.** `research/SOURCE_POLICY.md` exists and was consulted (Phase 08
deliverable). The transport used is one this project is permitted to use.

**Postconditions.** Provenance is complete — an envelope lacking `source_uri`,
`retrieved_at`, or `content_sha256` is invalid and **cannot be constructed**.
`policy_verdict == "REFUSED"` implies `payload` is empty.

**Failure modes.** Retrieval failure → an envelope carrying `transport_status`
and an empty payload; **never a silent skip**, because a silently missing source
is indistinguishable from a source that said nothing. Policy refusal → `REFUSED`
with reason, payload discarded. Oversize → truncate, with `truncated: true`
recorded in the envelope.

**Negative contract — must never.** Interpolate payload text into a prompt's
instruction region. Act on any imperative found in a payload. Maintain a
"trusted source" bypass. **Strip, normalize, or sanitize away text that looks
like an injection attempt — it is evidence, and Phase 23 tests against it.** Be
built against a transport this project may not use (§3.4). If a payload contains
text directed at an agent: quote it, name the source, escalate (`CLAUDE.md` §11).

**Owning phase / first needed.** Phase 08 builds it. First needed: **Phase 08**.

**`D-003`.** `DET`, fully.

**Supply join.** *Do not build:* HTTP transport — `C-028`/`C-029`. *Custom:* the
envelope shape, which must satisfy `D-009`, `BOUNDARIES` §6, and Phase 23's
injection tests simultaneously; a generic fetcher satisfies none. *Blocked:*
**partly.** Web ingestion only. Every richer path is `PROHIBITED` (`C-045`,
`C-071`, `C-119`, `C-120`, `C-132`); the inbound-message envelope has no
permitted channel (`C-039`, `C-126`) and is `BLOCKED`. **And note the boundary
this component cannot cover at all: pre-loaded third-party skill and tool
descriptions (§3.4, `OQ-P2-2`).**

---

### `CSK-04` — `claim-guard`

**Status:** `PROPOSED` · **Ladder:** `DISABLED` · **Artifact form:** `COMPONENT + thin DOCUMENT`

**Purpose.** Decide whether draft text may proceed, given
`product/APPROVED_CLAIMS.md`, `product/EVIDENCE_REGISTER.md`, and
`brand/PROHIBITED_LANGUAGE.md`.

**Trigger.** Every draft artifact containing outward-facing text, before it may
enter the approval queue or reach any adapter. Phases 11, 12, 13, 14, 17, 23.

**Inputs.**
`{ text: string, asset_type: string, target_platform?: string, registers: { approved_claims_ref, evidence_register_ref, prohibited_language_ref } }`

**Outputs.**
`{ verdict: "PASS"|"BLOCK"|"REQUIRES_APPROVAL", findings: [{ span: [int,int], extracted_assertion: string, category: string, matched_claim_id: string|null, reason: string }] }`

**Preconditions.** All three registers exist and are non-empty. **If
`APPROVED_CLAIMS.md` is empty or absent, every verdict is `BLOCK`** — an empty
register means nothing is approved, not that everything is. *(As of 2026-07-29
none of the three exists; Phase 06 creates them. Today `CSK-04` would `BLOCK`
every input, and that is the correct behaviour, not a defect.)*

**Postconditions.** `PASS` implies every extracted assertion matched an approved
claim ID or was classified non-assertive. Every finding cites a span and a
register ID.

**Failure modes.** Extractor returns nothing on non-trivial text →
`REQUIRES_APPROVAL`, not `PASS`; a silent extractor is a broken extractor.
Register unparseable → `BLOCK`. Ambiguous match → `REQUIRES_APPROVAL`.

**Negative contract — must never.** Issue `PASS` from the LLM layer — **only the
deterministic matcher may return `PASS`**. Infer that an unmatched claim is
probably fine. Rewrite the text to make it pass — that is the author's job, and a
silent rewrite destroys the audit trail. Treat pricing, discounts, or testimonials
as anything other than gated regardless of register state (`D-011`); on any of
those it hands off to `CSK-05` and returns at most `REQUIRES_APPROVAL`, never
`PASS`.

**Owning phase / first needed.** Phase 13 builds it; Phase 06 fixes the register
format it consumes. First needed: **Phase 11** (*"Links and claims validated"*).

**`D-003`.** `SPLIT`. LLM extracts candidate assertions; the deterministic matcher
decides. **The LLM half has no authority to produce any verdict.**

**Supply join.** *Do not build:* nothing — no supply row substitutes for any part
of it. *Custom:* all of it; it is a lookup against registers that exist only in
this repository. *Blocked:* no. **The join strengthens the case for this one
rather than trimming it:** `C-110`/`C-111` (`marketing:draft-content`,
`content-creation`, `brand-review`, `campaign-plan`) are `RESTRICTED` to
*reference method only*, precisely because they presuppose a brand voice and offer
catalogue that do not exist. `CSK-04` is the control that would make output from
any producer — third-party or project-authored — safe to route onward. It is the
direct mitigation for `R-07`.

---

### `CSK-05` — `gate-router`

**Status:** `PROPOSED` · **Ladder:** `DISABLED` · **Artifact form:** `COMPONENT + thin DOCUMENT`

**Purpose.** Classify a proposed action against the nine approval-gated categories
and route it — creating an approval record when gated, and never resolving one.

**Trigger.** Before any action with an outward effect: publishing, sending,
spending, changing pricing, using a testimonial, responding to a complaint,
engaging a controversial topic, initiating outreach, or anything touching paid
advertising.

**Inputs.**
`{ action_type: string, payload_ref: string, content_sha256: string, actor: string, requested_capability: string, ladder_stage: enum(D-010) }`

**Outputs.**
`{ decision: "CLEAR"|"REQUIRES_APPROVAL"|"PROHIBITED", categories: string[], approval_record_id?: string, rationale: string }`

**Preconditions.** `APPROVAL_POLICY.md` and `AGENT_PERMISSION_MATRIX.md` exist
(Phase 03); the approval store is writable.

**Postconditions.** `REQUIRES_APPROVAL` implies an approval record now exists in a
state only a **human** transition can leave. `CLEAR` implies zero of the nine
categories matched **and** the capability's ladder stage permits the action.

**Failure modes.** Unclassifiable action → `REQUIRES_APPROVAL`. Policy files
unreadable → `PROHIBITED`. Approval store unwritable → `PROHIBITED` (Phase 15:
*"Failure defaults to blocked"*). Ladder stage below the action's requirement →
`PROHIBITED`, with the stage named.

**Negative contract — must never.** Mark anything approved. Treat a timeout, an
absence of response, or a stale record as approval — **silence is never consent**
(`CLAUDE.md` §7). Treat a delivered notification as an approval — `C-024` carries
that warning in the registry itself. Narrow the nine categories under any workload
argument (`D-020`). Allow a caller to declare its own category set. Permit a
ladder-stage skip (`D-010`).

**Owning phase / first needed.** Phase 15 builds it; Phase 03 specifies its rules.
First needed: **Phase 15**.

**`D-003`.** `SPLIT`. LLM proposes candidate categories; deterministic code
decides and fails closed on ambiguity. Ambiguity classifies **into** the gate.

**Supply join.** *Do not build:* the human escalation channel — `C-008`
(`AskUserQuestion`) is `PERMITTED` and the registry names it the correct
escalation channel; operator notification — `C-024` (`RESTRICTED`, operator device
only). *Custom:* the nine categories, the ladder check, the fail-closed default,
the append-only approval record. *Blocked:* no, for a repo-authoritative store.
The Google Sheet **mirror** is `Q-004`-`BLOCKED`, which is the `HANDOFF §8` point:
`D-002` makes Sheets never a source of truth, so Phase 15 builds a repo-side store
and the Sheet renders it. The queue's logic, state machine, and history need no
Drive access at all.

---

### `CSK-06` — `dry-run-publisher`

**Status:** `PROPOSED` · **Ladder:** `DISABLED` · **Artifact form:** `COMPONENT`

**Purpose.** The single chokepoint through which any outbound platform write must
pass, defaulting to rendering rather than sending.

**Trigger.** Every publish, schedule, or platform-write call from any adapter.

**Inputs.**
`{ adapter_id: string, platform: string, payload: object, idempotency_key: string, approval_record_id: string, dry_run: boolean }`

**Outputs.**
Dry-run → `{ would_send: serialized-request, endpoint: string, idempotency_key: string, redactions: string[], socket_opened: false }`
Live → `{ sent: true, provider_response_id: string, idempotency_key: string, attempt_count: int }`

**Preconditions for a live send — all four, checked in order, any failure
aborting:** (1) `dry_run` is explicitly `false`; (2) an approval record exists
whose content hash equals the payload's; (3) the capability's ladder stage is at
least `APPROVAL_REQUIRED`; (4) the idempotency key has no prior successful send.

**Postconditions.** A dry run opened no socket. A live send recorded the
idempotency key **before** issuing the request, so a crash mid-flight cannot
produce a duplicate on retry.

**Failure modes.** Provider error → bounded retry with backoff, same idempotency
key. **Unknown outcome (timeout) → do not retry blind; query by idempotency key
first, and if the platform does not support that query, halt and escalate.** Rate
limit → back off; never parallelize around it. Unsupported API → `BLOCKED`, never
a workaround (Phase 16: *"Unsupported APIs blocked"*).

**Negative contract — must never.** Send without all four preconditions. Log a
credential or token in the rendered request — redact, and record the redaction.
Infer approval from an adjacent approved item. Treat "the previous attempt
probably failed" as grounds to resend. Bypass itself for "just a test." **Be
built against, or routed through, any capability this registry dispositions
`PROHIBITED`** — including `C-045`, which would reach every platform through the
operator's authenticated browser with no credential and no adapter at all.

**Owning phase / first needed.** Phase 16 builds it. First needed: **Phase 16**.

**`D-003`.** `DET`, fully.

**Supply join.** *Do not build:* nothing is reusable. *Custom:* the
four-precondition gate is this project's release rule and maturity ladder
expressed as code; no off-the-shelf publisher enforces it. *Blocked:* **yes, the
live branch.** No `PERMITTED` outbound write path exists in 141 rows; every
candidate is `PROHIBITED`; authentication state is `UNRESOLVED` for all of them;
`SECURITY_POLICY.md` does not exist (`D-027`), so no credential may enter this
project. **Build the dry-run branch and the gate. Specify the live branch and
leave it `BLOCKED`.** See §3.5.

---

### `CSK-07` — `cycle-runner`

**Status:** `PROPOSED` · **Ladder:** `DISABLED` · **Artifact form:** `COMPONENT`

**Purpose.** The deterministic entry point for the recurring operating cycle:
acquire a lock, stamp a run, execute the checklist, record start and end.

**Trigger.** A wall-clock schedule in a configurable named timezone (Phase 19
names `America/New_York`), plus manual invocation.

**Inputs.**
`{ cycle_id: string, period_start: ISO-8601, period_end: ISO-8601, timezone: IANA-tz-name, dry_run: boolean, clock: ISO-8601-with-offset }`
**`clock` is an input, not an ambient read.** See §5.

**Outputs.**
`{ run_id: string, started_at: ISO-8601-with-offset, ended_at: ISO-8601-with-offset, steps: [{ step_id, status: "OK"|"FAILED"|"SKIPPED", detail }], carried_forward: [{ task_id, reason, age_days: int }], deliverables: string[] }`

**Preconditions.** No other run holds the lock for the same `(cycle_id, period)`;
the run store is writable.

**Postconditions.** Exactly one run record exists per `(cycle_id, period)`. A
crashed run is **resumable from its recorded step**, not restarted from the top.

**Failure modes.** Lock held → exit cleanly, no duplicate run, **no alert** (this
is normal operation). Step failure → record it, continue independent steps, mark
the run partial. Delivery failure → retry that channel only; Phase 19 requires the
two delivery channels to be **independently** retryable, so a failed email must
not re-send the document.

**Negative contract — must never.** Perform a gated action itself — it enqueues
through `CSK-05` and stops. Run two concurrent instances for one period. Suppress
a step failure to make a run look clean. Emit an alert per retry (Phase 19: *"No
alert spam"*). **Acquire its trigger from any of the nine prohibited schedulers
(§3.6).** Read the system clock directly (§5).

**Owning phase / first needed.** Phase 19 builds it. First needed: **Phase 19**.

**`D-003`.** `DET`, fully. `D-003` names scheduling explicitly.

**Supply join.** *Do not build:* report rendering, charting, or document
generation — `C-083` (`dataviz`, `PERMITTED`/`NEEDED`, noted in the registry as
having direct value to Phase 19 executive reporting), `C-096`
(`docx`/`pdf`/`pptx`/`xlsx`, `PERMITTED`/`NEEDED`), `C-127` (`data:*`,
`RESTRICTED` to project-root data). *Custom:* the lock, the run record, the resume
point, the carry-forward ledger with reasons and age. *Blocked:* **yes — the
unattended trigger and both delivery channels.** All nine schedulers are
`PROHIBITED`; Google Cloud is `PROHIBITED`, `NOT CONNECTED`, unowned, and its SDK
is not installed (`F-01-02`); email is `PROHIBITED` on every path and `OQ-3` is
unresolved; Drive is `Q-004`-`BLOCKED`. **The manual / `SIMULATION` half is fully
buildable, including the timezone logic.** See §3.6.

---

## 5. The clock seam — decide it now, not at Phase 19

Carried from `HANDOFF §5` because it is cheap now and expensive later.

Phase 19's pass condition *"America/New_York schedule configurable"* cannot be
tested honestly against an ambient system clock: DST transitions, period
boundaries, and "exactly one run per period" are all statements about specific
instants that a test must be able to choose. **`CSK-07` therefore takes `clock` as
a typed input, and reading the system clock directly is in its negative
contract.**

`CSK-01` takes `clock` for the same reason at much lower cost — its reports carry
timestamps that appear in gate evidence.

Retrofitting a clock seam means changing every call site and every stored
timestamp's provenance. The decision costs one field today.

---

## 6. Priority, build order, and the cut

**Build order — by the first phase that cannot proceed without it:**

| Order | ID | First needed | Buildable today? |
|---|---|---|---|
| 1 | `CSK-01` | Phase 03 | Yes, in full |
| 2 | `CSK-02` | Phase 04 | Yes, once `OQ-P2-1` (dependency acquisition) is answered |
| 3 | `CSK-03` | Phase 08 | Web half yes; inbound half `BLOCKED` |
| 4 | `CSK-04` | Phase 11 | Yes, once Phase 06 creates the registers |
| 5 | `CSK-05` | Phase 15 | Yes, once Phase 03 writes the policies |
| 6 | `CSK-06` | Phase 16 | Dry-run half yes; live half `BLOCKED` |
| 7 | `CSK-07` | Phase 19 | Manual/`SIMULATION` half yes; trigger and delivery `BLOCKED` |

**The maintenance warning, stated plainly.** Seven components is a real standing
load for a solo operator with a low review budget (`D-019`). Each one is code that
must be maintained, tested, and re-verified whenever a platform, schema, or
register format changes (`R-18`). And each carries a second cost the registry
makes visible: **a skill document is itself text that instructs an agent** — the
exact class of artifact `CAPABILITY_REGISTRY.md` §I finding 3 identifies as a risk
surface. Project-owned ones are safer only because they are version-controlled,
phase-gated, and reviewable under Rule 1. That safety is a process, and the process
costs time.

**If the owner must cut — the defensible answer, sharpened by the join:**

- **Cut `CSK-01` first, and only `CSK-01`.** It is the one entry that **degrades gracefully**: `F-01-09`'s lesson can be discharged as a mandatory step in the phase protocol — *"before writing the gate report, enumerate the prior-phase files this phase's work falsified"* — executed by the phase owner with `git` and `Read`, at near-zero standing maintenance. `findings.md` F-01-09 itself says the pass "must be a deliberate human-style pass, not a grep." A component makes it a forcing function; a checklist entry makes it a discipline. Discipline is weaker, and it is not nothing.
- **`CSK-06` and `CSK-07` are already half-cut by circumstance**, not by choice. Their blocked halves cannot be built regardless. Do not read that as permission to skip their buildable halves — the dry-run renderer and the `SIMULATION` cycle runner are the cheapest safety wins in the plan, because they prove the gate without ever holding a credential.
- **`CSK-04` is the one I would argue hardest against cutting**, and the join strengthened rather than weakened the argument. It is the direct mitigation for `R-07` (LLM hallucinating product claims), it is the load-bearing control behind the *claims* gate, and — unlike `CSK-01` — **it does not degrade into a checklist.** A human reviewing every claim in every asset is precisely the review budget `D-019` says does not exist, and `D-020` forbids solving that by narrowing the gate. Cutting `CSK-04` means either the owner reads every line of every asset against a register by hand, or claims ship unchecked. There is no third option, and the second is `R-07` realized.

---

## 7. Interfaces between entries

Stated because the join surfaced one seam the first pass left implicit.

| From | To | Contract |
|---|---|---|
| `CSK-04` | `CSK-05` | Any assertion touching pricing, discounts, or testimonials is handed to `CSK-05` for category routing. `CSK-04` returns at most `REQUIRES_APPROVAL` on those, never `PASS`, even on a register match — the categories are independently gated (`D-011`). **This seam is why the two are not merged**, despite both classifying text against the nine categories: `CSK-04` judges assertions against a register; `CSK-05` judges actions against categories and the ladder. |
| `CSK-05` | `CSK-06` | `CSK-06`'s precondition (2) consumes the approval record `CSK-05` created, matched by content hash. |
| `CSK-07` | `CSK-05` | `CSK-07` never performs a gated action; it enqueues through `CSK-05` and stops. |
| `CSK-03` | `CSK-04` | Any external text reaching a producer arrives as an envelope payload, never as raw string. |
| `CSK-02` | all | Every typed entity crossing any of the above boundaries is validated. |

---

## 8. Considered and rejected

A backlog showing only what was included hides the judgement. Four rejections
carried from `HANDOFF §4`, with the supply join's verdict added; two new.

| ID | Candidate | Rejected because | What the supply join added |
|---|---|---|---|
| `CSK-90` | Confidence-decay arithmetic (`N-22`) | Real and recurring, but it is a **function**, not a skill. It has no trigger, no verdict, and no negative contract worth writing | Unchanged. `C-127` (`data:statistical-analysis`) exists but is an LLM method skill; `D-003` keeps the arithmetic deterministic and in-component |
| `CSK-91` | Multi-criteria scoring arithmetic (`N-24`) | Same shape as `CSK-90`. The judgement is the LLM's per criterion; the weighting is three lines of deterministic code | Unchanged |
| `CSK-92` | Accessibility contrast computation (`N-28`) | A well-solved general problem | **Rejection now evidenced rather than asserted.** `C-129` (`design:accessibility-review` and siblings) is `PERMITTED` / `NEEDED`, and the registry records it as *the only capability in the inventory* addressing Phase 07's accessibility deliverable. Use it; do not rebuild it |
| `CSK-93` | Any per-platform publishing adapter | Premature. `D-017`/`D-018` make the four platforms directional candidates only; building one would treat `Q-002` as answered | **Strengthened.** Every platform connector in the inventory is `PROHIBITED` (`C-045`, `C-055`, `C-057`–`C-061`, `C-112`, `C-115`, `C-125`). An adapter built now would be built against a prohibited capability |
| `CSK-94` | `capability-drift-detector` — watch for the registry going stale | **New in this pass, and rejected as a skill.** `SESSION_CAPABILITY_INVENTORY.md` §8 states there is no command that reproduces the session disclosure; re-capture is an **operator action** no agent capability can perform. What remains is a text diff, which `C-003` already does | Resolved instead as tests `T-POS-06` / `T-POS-07` in `SKILL_TEST_PLAN.md`, run at every phase gate. The need is real; a skill is the wrong shape for it |
| `CSK-95` | `register-consistency-checker` — ID resolution, vocabulary conformance, cross-reference integrity, arithmetic (`F-00-04`'s documentation-phase check set) | **New in this pass, and rejected as a *separate* entry.** It is the mechanical layer of `CSK-01`, not a peer of it, and an eighth standing component contradicts §6's maintenance argument. `F-01-04` also warns that the checker is itself unverified code — one such instrument is enough to keep honest | Not a supply-driven rejection. Whether it becomes real at all is Phase 03's `OQ-4` decision. If it does, it attaches to `CSK-01` |

One further rejection, recorded because it is a natural next thought and belongs
somewhere else: a **connector-authorization ledger** — a component asserting that
no MCP server was authorized without a preceding `DECISIONS.md` row. The need is
real (registry §D: *"one interactive authorization by the operator activates a
server, and nothing in this repository would record that it happened"*), but the
control is a policy in `CONNECTOR_ACTIVATION_PLAN.md`, not a component. Routed,
not built.

---

## 9. Open questions this backlog raises

Numbered `OQ-P2-n` to keep them distinct from `HANDOFF OQ-1`…`OQ-7`, which remain
open and unregistered — as of 2026-07-29 `OPEN_QUESTIONS.md` still holds only
`Q-001`…`Q-011`, so **none of `OQ-1`…`OQ-7` has been carried into the owner-facing
register yet.** That is `F-00-08` waiting to happen and it belongs to the Phase 02
Owner.

| ID | Question | Why it matters | Exact action, by whom |
|---|---|---|---|
| `OQ-P2-1` | How does this project acquire a runtime dependency, given `C-003`'s condition *"No installs"*? | `CSK-02` needs a schema-validation library; Phase 04's first pass condition depends on it; the alternative is writing a validator, which is the one thing the first pass said not to do | **Phase 02 Owner** decides whether `SKILL_INSTALLATION_PLAN.md` covers runtime dependencies or whether `C-003`'s condition needs an amendment; if neither, the **Project Owner** rules. §3.3 |
| `OQ-P2-2` | What controls pre-loaded third-party skill and MCP tool descriptions, which `CSK-03` structurally cannot wrap? | They are external text that instructs agent behaviour, arriving in context before any agent acts. `C-121` is quoted asserting a global tool-selection override; `C-116`, `C-135`, `C-085`, `C-087`, `C-054` are documented as modifying this project's own contract, config, permissions, or grants | **Phase 02 Owner**, in `SKILL_SECURITY_POLICY.md` — the deliverable whose scope this is. Routed here so it does not fall between two documents. §3.4 |
| `OQ-P2-3` | Where does project-owned skill and deterministic-component **source** live? | No phase names a home; `MASTER_PLAN.md` puts the first `tests/` at Phase 13; `.claude/skills/` is harness territory (`D-032`, `F-00-09`). Compounds `HANDOFF OQ-2` (fixtures have no home either) | **Phase 02 or 03 Owner** records the intended location before Phase 04 needs it. §3.2 |
| `OQ-P2-4` | Six of seven entries must be deterministic code, not skill documents (`D-003`). Does Phase 02's deliverable name *"custom skill"* mislead later phases into building instruction documents? | An instruction document cannot refuse. A `CSK-06` implemented as a skill would have an LLM deciding whether to send | **Phase 02 Owner** records the packaging distinction in the gate report so Phase 16 does not have to rediscover it. §3.2 |

`HANDOFF OQ-1` (who owns the scheduled-execution host) gains one instruction from
this pass and no resolution: **it may not be answered by reaching for one of the
nine prohibited schedulers already present on this machine** (§3.6).

---

## 10. Provenance and limits

- **Nothing was invoked.** No skill, MCP tool, connector, plugin, or subagent was called, loaded, enabled, installed, or tested to produce this file. Neither `ToolSearch` nor `Skill` was called. Phase 02's pass condition *"No unverified skill enabled"* is not weakened by this document.
- **No path outside the project root was read**, listed, or stat'd. `C:\Users\crone\Projects\Rough-Draft-Builders-Club` was not accessed in any form.
- **Every capability claim here is a citation of `CAPABILITY_REGISTRY.md`**, which is itself a dated snapshot with the four limits recorded in its own header. Authentication state is `UNRESOLVED` for every connected server and is claimed in neither direction. Where a plan depends on such a capability, this file records `BLOCKED`, not "probably fine."
- **Every entry is `PROPOSED` at ladder stage `DISABLED`.** Nothing here authorizes a build, an install, an activation, or a ladder movement.
