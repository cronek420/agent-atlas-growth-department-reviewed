# Data Retention Policy

**Owner of this file:** Privacy Reviewer (specialist), Phase 03, run `phase-03-2026-07-30-b`.
**Status:** `PROPOSED` policy — see §11 for honest capability classification. Structurally
complete for data that exists in this project today; deliberately incomplete for personal
data pending `Q-009`.
**Precedence:** this file sits below `README.md`, `DECISIONS.md`, `docs/PROJECT_BOUNDARIES.md`,
`INTAKE_RECORD.md`, and `CLAUDE.md`, and below `policy/POLICY_CONTRACT.md` and
`policy/action_registry.json` within Phase 03 (`policy/POLICY_CONTRACT.md` §1). Where this
file and those disagree, that is a defect to be raised, not silently reconciled — this file
never widens a boundary set elsewhere, and may only restate or tighten one.

**Note on this file's history — read this before trusting a citation below.** An earlier
version of this file existed on disk, self-labeled run `phase-03-2026-07-30-a` — the first
Phase 03 attempt, built on a branch that predated the real merged Phase 02 and discarded by
explicit Project Owner choice (`findings.md` F-03-01; `policy/POLICY_CONTRACT.md` header;
`task_plan.md` § "Why `-b`"). That draft was never committed, but the working-tree file was
not actually cleared when the branch was reset, so it was still present to read. It cited
`D-042` for "no numeric threshold may be invented" — in the real, merged decision register
`D-042` is a *different* decision (`policy/action_registry.json` is the machine-readable
permission source of truth; `AGENT_PERMISSION_MATRIX.md` is generated from it, never hand-
edited). The real "no number invented" decision is `D-047`. That draft also asserted "Phase 02
was never executed" — true of the stale branch, false of the real project, which has a real
141-row `CAPABILITY_REGISTRY.md` and a real `RUNTIME_AGENT` role (`policy/POLICY_CONTRACT.md`
§5). This version is written fresh against the real repository state and corrects every such
citation; it also adds a data class (§2.8) that this attempt's real Phase 02 context surfaces
and the first attempt's assignment did not ask for.

---

## 1. Scope, ownership, precedence

This policy governs **what data classes exist or could exist in this project, where each may
be stored, how long each may be retained, and how each is deleted** — for every agent and
every phase.

**Who owns this file.** The Privacy Reviewer wrote it in Phase 03. Ownership of the *file*
does not mean ownership of the *facts* it restates — the prohibition on collecting personal
data belongs to `docs/PROJECT_BOUNDARIES.md` §5 and `policy/action_registry.json` (`ACT-R08`,
`ACT-W10`), secrets handling belongs to `SECURITY_POLICY.md` (this file cross-references it by
name only and does not restate or describe its contents — it is being written concurrently by
another specialist this run), and consent *obtaining and honouring* belongs to
`MESSAGING_POLICY.md` (a Phase 03 sibling this agent did not author and did not read, per its
own assignment — this file states only the boundary in §6). This file only changes:

- via a Project Owner decision recorded in `DECISIONS.md` with a status, owner, rationale, and
  evidence traceable to `INTAKE_RECORD.md` or a governing source document
  (`docs/PROJECT_BOUNDARIES.md` §7), or
- by a phase owner narrowing a control (fail-closed tightening), which is `ALLOW_LOGGED` —
  disclosed in `findings.md` and the gate report (`ACT-W14`).

**This file never widens a boundary set elsewhere.** In particular it never authorizes
collecting, importing, or storing personal data — that remains `DENY` (`ACT-R08`, `ACT-W10`;
`Q-009`, `R-12`, `D-033`) regardless of anything below, and it never authorizes invoking a
borrowed-authority access path — that remains `DENY` (`ACT-R09`; `F-02-03`, `R-21`) regardless
of anything below. Any sentence in this document that reads as granting either is an error in
the document, not a new grant — raise it, do not act on it.

**Six-token permission vocabulary.** Every permission claim in this document resolves to
exactly one of `ALLOW` · `ALLOW_LOGGED` · `APPROVAL_REQUIRED` · `OWNER_ONLY` · `DENY` ·
`BLOCKED`, as defined in `policy/POLICY_CONTRACT.md` §4. Where a specific action registry row
governs, its ID (`ACT-xxx`) is cited directly.

**The organizing split.** `Q-009` (data-privacy handling for lead and contact data) is
`UNRESOLVED`. Consequently no lead, contact, or personal data may be collected, imported, or
stored today (`docs/PROJECT_BOUNDARIES.md` §5; `R-12`). This document is therefore organized
around a hard line:

- Data classes that **actually exist in this repository today** — governance records, decision
  registers, agent-run evidence, handoffs, gate reports, findings, Git history, scratchpad
  working files, logs — are decidable now, and this policy defines real, operable rules for
  them.
- Personal data and its neighbors, including data reachable only through a borrowed-authority
  path, are **structurally defined but blocked**: the classification exists, the table row
  exists, and the value cells are `UNRESOLVED`, each naming the exact owner input that would
  fill it. No number is invented (`D-047`).

---

## 2. Data classification scheme

Every class below is exhaustive by construction: **§2.10 is the fail-closed default**, so
nothing this project could ever hold or reach falls outside the scheme.

### 2.1 Public / governance artifacts
Markdown documents at the project root and in `docs/` that state the project's own rules,
decisions, plans, and status: `README.md`, `CLAUDE.md`, `DECISIONS.md`, `OPEN_QUESTIONS.md`,
`RISK_REGISTER.md`, `NON_GOALS.md`, `SCOPE.md`, `ACCEPTANCE_CRITERIA.md`,
`MASTER_PLAN.md`, `docs/PROJECT_BOUNDARIES.md`, and this file's siblings. Content is about the
project itself, never about an identifiable individual outside the Project Owner's own stated
role.

### 2.2 Internal project records
Working artifacts produced during a phase that are not themselves governance rules:
`task_plan.md`, `progress.md`, `findings.md`, `agent_runs/*/handoffs/*`,
`agent_runs/*/PHASE_GATE_REPORT.md`, review and audit reports. Internal to the build process,
not customer-facing, not personal data.

### 2.3 Operational / telemetry data
Data generated by running the system rather than authored as a deliverable: OS temp /
harness-provided scratchpad working files (`ACT-W04`), local log files (`*.log`, `logs/` —
`.gitignore` §8). Ephemeral by design; not a deliverable; never a place for a secret
(`docs/PROJECT_BOUNDARIES.md` §1) and, per this policy, never a place for personal data either
(§2.10 applies if any turns up).

### 2.4 Personal data
Any information that identifies or could reasonably identify a specific individual: names,
email addresses, phone numbers, physical addresses, IP addresses tied to a person, social
handles, or any lead/contact/customer record. `ACT-R08` (read) and `ACT-W10` (write/collect/
import/store) are `DENY` for this class today, for every role — including `RUNTIME_AGENT`,
which now exists as a real role (`policy/POLICY_CONTRACT.md` §5; `CAPABILITY_REGISTRY.md`,
141 rows) — with no exception (`Q-009`, `R-12`, `D-033`).

### 2.5 Sensitive personal data
A stricter subset of §2.4: data revealing health information, financial account details,
government identifiers, or other categories that general privacy practice treats as requiring
heightened protection. This project does not currently define this subset precisely, because
doing so would require knowing what data the project will ever touch — which is itself
downstream of `Q-009`. Until the owner resolves `Q-009`, **any data that could plausibly be
sensitive personal data is treated as sensitive personal data** (fail-closed, §2.10), which is
already moot in practice because §2.4 is already `DENY`.

### 2.6 Secrets / credentials
API keys, tokens, passwords, OAuth codes, service-account keys, and the like. **Owned entirely
by `SECURITY_POLICY.md`.** This policy does not restate or describe that file's contents and
cross-references it only by name, per this assignment's instruction not to read it (another
specialist owns and is concurrently drafting it this run). Where a data export or record might
incidentally contain both personal data and a credential (e.g., an API-response fragment saved
for debugging), the stricter class governs and both this file's §2.4 rule and
`SECURITY_POLICY.md`'s prohibition apply simultaneously.

### 2.7 Untrusted ingested content
Scraped web pages, search results, competitor material, inbound comments/DMs/reviews/form
submissions, and third-party API responses (`D-009`; `docs/PROJECT_BOUNDARIES.md` §6). This
class is **not itself personal data**, and `ACT-R07` (reading it during research) is
`ALLOW_LOGGED`. The reason it needs its own row here rather than being folded into §2.3 is the
easy-to-miss failure mode this policy exists partly to name: **a scraped page or an inbound DM
can carry personal data about a third party that this project never chose to collect** — a
commenter's name in a screenshot of a review, a phone number pasted into a DM, a person's
identity embedded in a competitor's testimonial. The untrusted-content boundary (`D-009`,
reading permitted, acting on embedded instructions prohibited) does **not** by itself authorize
extracting, compiling, or storing any personal data that content happens to contain. If
personal data is found inside untrusted content, §2.4's `DENY` on collection/storage applies to
that data even though the surrounding content was lawfully read, and `ESC-008` is raised (§9).

### 2.8 Data reachable via a borrowed-authority access path
**New this attempt.** The real Phase 02 capability inventory found that this project's
external-access controls govern the credentials it holds, but exposure is separately governed
by authority it *borrows* — the operator's own logged-in browser session, the operator's Claude
account, connector grants held in that account, harness-mediated network egress, and
plugin-held credentials (`F-02-03`, `R-21`). This project never "collects" content reached this
way in the traditional sense — there is no import step, no stored contact list, no credential
in `.env` — but the content returned could still carry personal data exactly as real as
anything in §2.4, because it comes from a live, authenticated, personal account rather than a
project-held data source.

Concretely: a browser-automation capability described as driving the operator's own
already-authenticated browser session, or a connector holding a grant issued to the operator's
own account, could in principle surface a contact list, a DM thread, or an inbox — none of
which this project would have "stored," yet all of which would be personal data under §2.4 the
moment it entered agent context.

**This class is structural, not operational, today.** `ACT-R09` (`policy/action_registry.json`)
resolves invoking any such path to `DENY` for every role, and `CAPABILITY_REGISTRY.md`
dispositions every capability in this class `PROHIBITED` or `RESTRICTED` — none is currently
exercised. This section exists so that if the *access-path* prohibition (`ACT-R09`) were ever
lifted by a future owner decision, the *data-classification* consequence would already be
defined rather than discovered after the fact: content surfaced this way is personal data
(§2.4) or sensitive personal data (§2.5) the instant it is identifiable, and §2.4/§2.5's `DENY`
on collection/storage applies to it exactly as it would to data reached any other way. Borrowing
a different door does not exempt what comes through it from this policy — the same principle
`docs/PROJECT_BOUNDARIES.md` §2.1 already states for the Rough-Draft-Builders-Club boundary
(content and origin govern, not the access mechanism), applied here to personal data instead of
to that one repository.

If this path is ever invoked or nearly invoked, `ESC-011` applies in addition to `ESC-008` if
personal data actually surfaces (§9).

### 2.9 What this scheme deliberately excludes
Consent records are **not** a separate data class — they are evidence about §2.4 data and are
addressed structurally in §6, because their retention logic is different from (and, per the
structural point in §6, potentially longer than) the personal data they authorize.

### 2.10 Fail-closed default
**Any data class not classified above, or any specific item whose classification is unclear,
is treated as the most sensitive class defined here (§2.5, sensitive personal data) and may
not be collected or stored.** This mirrors the registry's own fail-closed default — "any
proposed action that matches no row in `policy/action_registry.json` resolves to `DENY`"
(`D-044`) — applied to data instead of actions. An agent that is unsure which class a piece of
data belongs in does not guess downward; it treats it as the strictest class and escalates
(`ESC-008`, §9).

---

## 3. Per-class rules

| Class | May be collected/created today? | Stored where | Retained how long | Deleted how | Who may read |
|---|---|---|---|---|---|
| §2.1 Public/governance artifacts | `ALLOW` — created as part of normal phase work (`ACT-W01`) | This repository; mirrored to the private GitHub remote at every phase gate (`ACT-C01`) | Indefinitely — these are the project's authoritative record (`D-001`) and are append-only in intent; existing rows are never rewritten or deleted, only superseded (`ACT-W11`, `DENY` on rewrite/delete) | Not deleted in the ordinary case; see §4 and §5 for what "deletion" can and cannot mean once committed and pushed | `PROJECT_OWNER`, `PHASE_OWNER`, `SPECIALIST`, `INDEPENDENT_REVIEWER`, `GOVERNANCE_AUDITOR` — all `ALLOW` (`ACT-R01`) |
| §2.2 Internal project records | `ALLOW` — written by the assigned owner per `task_plan.md` (`ACT-W01`) | Same as above | Indefinitely, as the audit trail (`.gitignore` §9 names `agent_runs/` as "tracked on purpose") | Same as §4/§5 | Same as above |
| §2.3 Operational/telemetry (scratchpad, local logs) | `ALLOW` for throwaway working files (`ACT-W04`); local logs are incidental to tool use, not authored | OS temp / harness scratchpad directory (never this repository — `docs/PROJECT_BOUNDARIES.md` §1); `.gitignore` §8 excludes `*.log`, `logs/` if any land in-repo by accident | No retention guarantee and none is promised — ephemeral by design, may be cleared at any time, nothing there is a deliverable | Deletion is simply non-persistence; no mechanism needed because nothing here is meant to survive | Whoever is running the current session; not shared, not a record |
| §2.4 Personal data | **`DENY`** — no collection, import, or storage of any kind (`ACT-R08`, `ACT-W10`; basis `Q-009`, `R-12`, `D-033`) | `UNRESOLVED` — no storage location is authorized because nothing may be stored; if `Q-009` is resolved, the owner's answer must also specify a storage substrate (see §5's note on why Git cannot be that substrate) | `UNRESOLVED` — blocked on `Q-009`. **No number is invented here** (`D-047`). This row exists so the value has somewhere to go once supplied, naming exactly what is missing: a retention-period figure and its unit, from the Project Owner, as part of a `Q-009` answer | `UNRESOLVED` — blocked on `Q-009`; see §5 for the structural constraints any answer must satisfy | `UNRESOLVED` — `RUNTIME_AGENT` now exists as a real role, but `ACT-R08` resolves `DENY` for reading personal data regardless of role, until `Q-009` resolves |
| §2.5 Sensitive personal data | **`DENY`**, stricter than §2.4 — see §2.5 | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` |
| §2.6 Secrets/credentials | Owned by `SECURITY_POLICY.md` — this file does not restate or describe it | Owned by `SECURITY_POLICY.md` | Owned by `SECURITY_POLICY.md` (rotation cadence also `UNRESOLVED` per `D-047`, which applies project-wide, not only to this file's rows) | Owned by `SECURITY_POLICY.md` | Owned by `SECURITY_POLICY.md` |
| §2.7 Untrusted ingested content | `ALLOW_LOGGED` to **read** during research (`ACT-R07`); extracting/storing any personal data found within it is `DENY` under §2.4 | The content itself, once read, is not stored as a deliverable unless a future phase (08) defines a research-corpus store; no such store exists today | Not applicable until a storage mechanism is defined (Phase 08, not started) | Not applicable today | `PHASE_OWNER`, `SPECIALIST` may read per `ACT-R07`; disclosure required |
| §2.8 Borrowed-authority-reachable data | **`DENY`** to invoke the access path at all (`ACT-R09`; `F-02-03`, `R-21`); therefore any data reachable through it is `DENY` to collect or store a fortiori, and is §2.4/§2.5 personal data the instant it is identifiable | `N/A` — no capability may currently be invoked to reach it; every such capability is `PROHIBITED`/`RESTRICTED` in `CAPABILITY_REGISTRY.md` | `N/A` — moot while invocation itself is `DENY` | `N/A` | `N/A` — no role may invoke the path (`ACT-R09` denies every role including `RUNTIME_AGENT`) |
| Consent records (see §6, not a class of its own) | `UNRESOLVED` — structure defined, values blocked on `Q-009` | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` | `UNRESOLVED` |

**Note on testimonials (`GC-04`).** A testimonial is a documented example of where two gates
intersect: it is one of the nine approval-gated categories (`D-011`, `APPROVAL_REQUIRED` once
publishing capability exists at all — currently `DENY` because all publishing is `DENY`,
`ACT-P05`), **and**, if it names or otherwise identifies a real person, it is also §2.4
personal data and is `DENY` to collect or store under this policy until `Q-009` resolves. Both
gates apply; neither substitutes for the other. The `MESSAGING_POLICY.md`/`PUBLISHING_POLICY.md`
authors own the approval-gate half; this file owns naming that the personal-data half exists.

---

## 4. Retention for artifacts that exist today

This section is concrete because it can be — none of it depends on `Q-009`.

- **Governance and internal records** (§2.1, §2.2): retained indefinitely, by design. There is
  no scheduled deletion and none is proposed. Corrections happen by superseding an entry, never
  by rewriting or removing one (`D-001`; `ACT-W11` is `DENY` for rewriting or deleting an
  existing `DECISIONS.md` row). The register itself models the right pattern for every other
  "retained" class in this project: append, supersede, never erase.

- **Git history, and the fact that it is mirrored off-machine, is the hard case.** This
  project's Git history is committed locally and, per standing practice, pushed to the private
  GitHub remote at every phase gate (`ACT-C01`; `D-030`). Once a commit is pushed, **"delete"
  does not mean deleted.** Removing a file from the working tree (`git rm`) or even amending a
  later commit does not remove the earlier blob from history — it remains reachable from prior
  commits, and once pushed, it exists in at least two places (local disk and GitHub's copy).
  This project has already learned this lesson once with an uncommitted-but-present file: the
  discarded first Phase 03 attempt's draft policy documents were never committed, yet the
  working-tree files themselves survived the branch reset and were still readable — a smaller-
  scale version of the same durability problem Git history poses at larger scale. This file
  adopts the identical reasoning for any data that should never have been committed: the only
  way to actually remove a blob from reachable history is a history rewrite, which is `ACT-D02`,
  `OWNER_ONLY`, absolute, and — per the one precedent this project has (`F-01-01`) — must be
  preceded by inspecting what would be lost, obtaining explicit owner approval, and being pinned
  with `--force-with-lease` to a specific inspected commit, never a bare force-push.

  **The implication for retention policy is structural, not incidental:** for any data class
  where genuine time-bound deletion might ever be required — which today means §2.4/§2.5
  personal data if `Q-009` is ever resolved to permit collecting it, and by extension §2.8 if
  its access-path prohibition were ever lifted — **the control has to be exclusion before
  commit, not deletion after.** This is the same ordering `findings.md` `F-01-06` already
  established for secrets ("the exclusions therefore had to precede the first `git add`...
  exclude first, create second") and this policy adopts it as a general rule, not a
  secrets-specific one: **no data class whose retention might need to end on a schedule may
  ever be committed to this repository's Git history.** If `Q-009` is resolved in a way that
  authorizes collecting personal data, the storage substrate for that data cannot be this
  repository — it must be a store outside Git that supports real deletion (a database, a
  Sheet with row-level delete, etc.). This policy does not invent which substrate; it states
  the constraint any substrate decision must satisfy, so a future phase does not propose "store
  leads as Markdown files in this repo" and discover the permanence problem only after the
  first commit.

- **Scratchpad and local logs** (§2.3): no retention promise, ephemeral, cleared at the
  harness's or operator's discretion. Nothing here is expected to survive a session, and
  nothing here should be relied on as a record — `agent_runs/` is the record.

---

## 5. Deletion and erasure

**For governance/internal records (§2.1, §2.2):** deletion is not the intended mechanism.
Corrections are recorded as corrections (superseding rows), consistent with `D-001` and
`ACT-W11`. `ACT-D01` (deleting a tracked file from the project) is `APPROVAL_REQUIRED` for the
`PHASE_OWNER` role — a deliberate, approved action, not a routine one.

**For personal data (§2.4/§2.5), erasure is `UNRESOLVED`, structurally, on `Q-009`.** What can
be stated without inventing a value:

1. Any future erasure mechanism must operate on a storage substrate outside this repository's
   Git history, per §4's constraint — a `git rm` alone would be a false promise of erasure.
2. An honest deletion commitment, once personal data has ever entered a Git commit that was
   pushed to the remote, **can promise to stop using the value and to supersede or rotate it
   going forward, but cannot promise the value no longer exists anywhere** without a history
   rewrite (`ACT-D02`, `OWNER_ONLY`, the three-element protocol from `F-01-01`: inspect first,
   obtain explicit owner approval, `--force-with-lease` pinned to an inspected commit). Git's
   permanence does not distinguish between a credential and a person's contact information once
   either is committed.
3. The exact owner input that resolves this: `Q-009`'s answer must specify not only a retention
   *period* but a retention *substrate* — where personal data will actually live — because
   without a substrate decision, no retention number is meaningful (a "30-day retention" promise
   is not deliverable if the data lives in Git). This is a gap in how `Q-009` is currently
   phrased in `OPEN_QUESTIONS.md`, and this handoff proposes it be sharpened accordingly (see
   the handoff's Open questions section).
4. No SLA (e.g., "erasure requests are honored within N days") is asserted here. `D-047`
   prohibits inventing that number; the field exists in this policy's structure and its value
   is blank pending the owner.
5. §2.8's borrowed-authority class has no erasure question today, because nothing may be
   collected via it in the first place (`ACT-R09`, `DENY`). If that access-path prohibition is
   ever lifted, whatever it surfaces is personal data under §2.4/§2.5 and this section's rules
   apply to it without modification.

---

## 6. Consent records

**Boundary, stated explicitly so it is not overstepped:** this file owns **how long a consent
record must live and how it is stored**. It does **not** own whether consent must be obtained
before a message is sent, how consent is captured operationally, or how an opt-out is honored
— those are `MESSAGING_POLICY.md`'s, a Phase 03 sibling this agent did not author and did not
read. This file asserts nothing about that half. (`ACT-S04` — sending a business-initiated
message to a recipient with no recorded opt-in is `DENY` — and `ACT-S05` — sending to a
recipient who has opted out is `DENY` — are cited here only to show where the boundary sits,
not restated or interpreted.)

**The structural point this file does own:** a consent record must be capable of outliving the
personal data it authorizes, or the project cannot later prove the consent existed. If a lead's
contact record is deleted (per whatever erasure mechanism `Q-009` eventually defines) but the
record of their having consented is deleted at the same time, the project has no way to
demonstrate — to the individual, to a platform, or to itself — that the outreach that occurred
before deletion was authorized. This creates a real tension worth naming rather than glossing
over: **a consent record that outlives its subject's data must, at minimum, retain enough
identifying information to be checked against a future claim** (e.g., "did we have consent to
message this person"), and that minimal identifying information is itself personal data under
§2.4. This policy does not resolve the tension — resolving it requires the owner to decide how
much a consent record needs to retain (a full contact record indefinitely, versus a minimal
hashed or truncated identifier, versus something else) and for how long. Both the retention
period and the storage substrate for consent records are `UNRESOLVED`, blocked on `Q-009`
(`D-047`: no number invented).

---

## 7. Data minimisation

Restated from `docs/PROJECT_BOUNDARIES.md` §5, not weakened: **do not compile personal
information across sources.** Do not place personal data in URLs, query strings, filenames, or
commit messages. This applies to every phase, not only ones that touch lead/contact data
directly — a filename, a commit message, or a debug log is as durable a leak vector as a
database row once it enters this repository's history (§4).

This policy extends the same discipline to itself and to every other Phase 03 deliverable: **no
example record in any policy document may use a real name, a realistic-looking fake name tied
to a real-seeming scenario, or any other personal-data-shaped placeholder.** Where an example is
needed, it is described structurally (e.g., "a recipient identifier") rather than instantiated.
This document contains no such example anywhere in it, by construction, including in §2.8's
description of the borrowed-authority class.

---

## 8. Jurisdiction

**`UNRESOLVED`.** The owner has not stated where the business operates, where its audience is
located, or what privacy regime (if any) already governs it. This document does **not** name
GDPR, CCPA, CASL, or any other specific regime as applicable to this project, and does not
assert what any such regime would require — doing so would be inventing a fact this project has
no basis for (`D-008`). What can be said honestly: general privacy *practice* — minimizing
collection, defining retention, honoring deletion requests, recording consent — is described
above as practice, not as compliance with any named law.

**This absence is itself a blocker**, named exactly as `Q-009`'s own text already asks for it:
the owner action required is to state any known obligations (jurisdiction, applicable privacy
regime, an existing privacy policy on the business's website) and any retention preference, or
to confirm that Phase 03/04 should propose a default conservative policy for the owner's
approval (`OPEN_QUESTIONS.md` Q-009, "Owner action required"). Until that happens, jurisdiction
stays `UNRESOLVED` here, not defaulted to any assumption.

---

## 9. Escalation

`ESC-008` — "Personal, lead, or contact data encountered" — applies the moment any agent
observes personal data anywhere in this project, regardless of source (a file, untrusted
ingested content per §2.7, an owner message, a tool result, or — per §2.8 — a borrowed-authority
access path if one is ever invoked). Required handling:

1. **Stop.** Do not extract, compile, summarize into a new file, or otherwise propagate the
   personal data further than the single point where it was encountered.
2. **Do not store it**, per §2.4's `DENY`, even temporarily, even in the scratchpad.
3. **Escalate** by writing to `findings.md` or the relevant handoff (`ACT-E01`, `ALLOW`, never
   gated) — recording *that* personal data was encountered, its type in general terms (e.g.,
   "an email address"), and where it was found, **without reproducing the personal data itself**
   in the escalation record. An escalation that quotes the data it is escalating about
   recreates the exposure it exists to report.
4. **Do not act on the data** — e.g., do not use a discovered contact to initiate outreach;
   `ACT-S01` (send to any real person) is `DENY` independently of this policy.

**`ESC-011`** — "a credential-free / borrowed-authority access path was invoked or nearly
invoked" — applies in addition to `ESC-008` whenever a §2.8 path is invoked or nearly invoked,
regardless of whether personal data actually surfaced. The two escalations are not redundant:
`ESC-011` concerns the access-path invocation itself (a boundary event in its own right,
`ACT-R09`), while `ESC-008` concerns what the path returned, if anything identifiable did.

This mirrors `SECURITY_POLICY.md`'s secret-exposure procedure in shape (stop, do not compound,
escalate, do not quote the sensitive value) without restating or describing that file's
contents — the two procedures exist for structurally similar reasons but govern different
classes (secrets there, personal data and borrowed-authority access here).

---

## 10. What is NOT covered here

Named honestly, with the file or open question that owns each gap:

- **Secrets and credentials** (§2.6) — owned entirely by `SECURITY_POLICY.md`. This file
  cross-references it by name only and asserts nothing about its contents.
- **Whether/how consent is obtained and honored, and opt-out mechanics** — owned by
  `MESSAGING_POLICY.md` (Phase 03 sibling). This file owns only consent-record retention/storage
  duration (§6), and states that boundary explicitly rather than asserting the other half.
- **Approval-record mechanics and the approval state machine** — owned by `APPROVAL_POLICY.md`
  (Phase 03 sibling).
- **Autonomy-ladder promotion mechanics** — owned by `AUTONOMY_POLICY.md` (Phase 03 sibling).
  Note only: any future capability that would handle personal data is itself a production-facing
  capability subject to `D-010`'s no-skip ladder, currently `DISABLED`, and is additionally
  blocked by this file's `DENY` on personal-data collection until `Q-009` resolves — two
  independent gates, not one. The same is true, doubly, of any §2.8 borrowed-authority path,
  which is additionally blocked by `ACT-R09` regardless of ladder stage.
- **Publishing and spend specifics** — owned by `PUBLISHING_POLICY.md` and `BUDGET_POLICY.md`
  (Phase 03 siblings).
- **Which specific jurisdiction's law applies, and what it would require** — nobody owns this
  yet; it is `UNRESOLVED`, named in §8, and is exactly what `Q-009` asks the owner to supply.
- **Numeric retention periods, deletion SLAs, and consent-record durations** — `UNRESOLVED` by
  design (`D-047`); this policy states *where* each number goes and never invents *what* it is.
- **A storage substrate for personal data** — does not exist and is not proposed here; §5 states
  the constraint any future proposal must satisfy (not Git), without naming one.
- **Whether any §2.8 borrowed-authority path is actually authorized against the owner's own
  accounts** — `Q-012`, `UNRESOLVED`, not this file's to answer. This file states only the
  data-classification consequence *if* such a path were ever exercised (§2.8); it does not
  assess connector authorization state.
- **`CAPABILITY_REGISTRY.md`'s real 141-row disposition set and its `RUNTIME_AGENT` grants** —
  owned by `CAPABILITY_REGISTRY.md` (Phase 02, `D-039`, a dated snapshot) and
  `AGENT_PERMISSION_MATRIX.md` (Phase 03 Owner, generated). This file cites specific rows
  (`C-009`, `C-045`) only where `RISK_REGISTER.md` R-21 already names them; it does not restate
  the registry's own dispositions.

---

## 11. Capability classification

Honest classification per `CLAUDE.md` §3 and `policy/POLICY_CONTRACT.md` §10: a policy document
existing is not the same as a control being enforced.

| What this policy establishes | Classification | Why |
|---|---|---|
| The data classification scheme (§2), including the new §2.8 borrowed-authority class | `PROPOSED` | Written and cross-referenced against the registry, but no deterministic code classifies incoming data against it — classification today is a human/agent judgment call, not an automated check. |
| Fail-closed default for unclassified data (§2.10) | `PROPOSED` | States the rule; nothing scans a new file or data item and auto-applies it. The registry's own fail-closed default (`D-044`) has a partial mechanical backstop (`tools/policy_check.py`); this data-specific analogue does not yet. |
| Personal-data collection prohibition (§2.4, restating `ACT-R08`/`ACT-W10`) | `SCAFFOLDED` | The prohibition is real and has a partial mechanical backstop already operating: `.gitignore` pre-emptively excludes `data/private/`, `data/leads/`, `data/contacts/`, `*.leads.csv`, `*.contacts.csv` (`D-033`), verified present in this repository by direct inspection this run. That backstop catches accidental commits to those specific paths/patterns; it does not catch personal data placed anywhere else (a Markdown file, a differently-named file, a commit message), so it is a real but partial control, not a complete one. |
| Borrowed-authority access-path prohibition (§2.8, restating `ACT-R09`) | `SCAFFOLDED` | The prohibition is real in `policy/action_registry.json` and every named capability class carries a `PROHIBITED`/`RESTRICTED` disposition in `CAPABILITY_REGISTRY.md` (a real, dated snapshot). It is not `IMPLEMENTED`: nothing deterministically prevents a future session from invoking the capability, and the registry snapshot itself can drift (`R-20`, `D-039`) without anything re-checking it. |
| Retention rules for governance/internal records (§3, §4) | `SCAFFOLDED` | The append-only, indefinite-retention pattern is real and already how `DECISIONS.md` and `findings.md` actually operate in this project (observed directly in the files read for this policy) — a genuinely operating practice, though enforced by convention and `ACT-W11`'s stated prohibition, not by a technical write-lock. |
| Git-history permanence analysis and the exclude-before-commit rule (§4, §5) | `PROPOSED` | Correct as a statement of how Git and the private remote actually behave (verified conceptually against `F-01-01`'s real precedent, and against the concrete example of this file's own predecessor draft surviving an uncommitted branch reset), but there is no tooling in this project that prevents a future commit from violating the rule — it depends on agent discipline and phase-owner review. |
| Personal-data retention values, deletion SLA, jurisdiction (§3 personal-data rows, §5, §8) | `PRODUCTION_BLOCKED` | Explicitly and structurally incomplete pending `Q-009` and, per §5, pending a storage-substrate decision this project has not made. Not a policy gap that more drafting would close — it requires owner input that does not exist yet. |
| Consent-record retention structure (§6) | `PROPOSED`, and partially `PRODUCTION_BLOCKED` | The structural tension (a consent record must outlive its subject's data) is named and real; the values that would make it operable are blocked on the same `Q-009` dependency as personal data generally. |
| Escalation procedure for encountered personal data and borrowed-authority invocation (§9) | `PROPOSED` | A defined procedure citing `ESC-008` and `ESC-011` and `ACT-E01`, with no rehearsal and no tooling that detects either condition automatically — detection remains a human/agent judgment call today. |

Nothing in this document is `IMPLEMENTED`. The one genuinely operating, verified control this
policy relies on is the `.gitignore` pre-emptive exclusion (`D-033`), and even that is partial,
not complete. This policy is a decision surface for the owner and a citation surface for future
phases — not a running control, and it does not claim to be one.
