# Connector Activation Plan

**Owner of this file:** Security Reviewer (Phase 02 specialist), run `phase-02-2026-07-29-a`.
**Date written:** 2026-07-29.
**Evidence base:** `agent_runs/phase-02/evidence/SESSION_CAPABILITY_INVENTORY.md`
(`Ev §N`) and `CAPABILITY_REGISTRY.md` (row IDs `C-0nn`).
**Companion:** `SKILL_SECURITY_POLICY.md` — the rules; this file is the conditional
sequence.

---

## NOTHING IN THIS PLAN IS AUTHORIZATION

**No connector named below is authorized. No step below may be performed today. No
sequence below is a schedule.**

This is a specification of **what would have to be true** before a connector could
be activated — the gates, the order, the performer, and the way back out. It creates
no permission, and reading it grants nothing. Every connector here is
`PROHIBITED` in `CAPABILITY_REGISTRY.md` today, and stays `PROHIBITED` until the
Project Owner records a decision that changes it.

If you are looking for the point at which a connector becomes usable, it is §6:
**a `DECISIONS.md` row written before the authorization, not after.** Nothing else in
this file substitutes for it.

**Snapshot dependence.** Every capability named here comes from a session inventory
captured **2026-07-29, on one machine, under one user profile**. It is not a property
of this repository, it is not under version control, and nothing in this project
detects when it changes. Re-capture before acting on any row
(`SKILL_SECURITY_POLICY.md` §7.2, triggers T1–T5).

**Authentication state is `UNRESOLVED` everywhere in this file** and is never
guessed in either direction (`Ev §0` Limit 3; `CLAUDE.md` §6). This session is
non-interactive, so no authorization flow could run here even if one were wanted —
which is a fact about this session, not a control.

---

## 1. What this plan covers

`CAPABILITY_REGISTRY.md` §G identifies **22 rows that are prohibited today and
plausibly relevant to a later phase**. That set — not the 69-row irrelevance
exclusion list — is where activation planning has work:

`C-031` · `C-038` · `C-041` · `C-045` · `C-047` · `C-057` · `C-058` · `C-059` ·
`C-060` · `C-064` · `C-066` · `C-067` · `C-068` · `C-069` · `C-071` · `C-112` ·
`C-113` · `C-114` · `C-119` · `C-125` · `C-126` · `C-132`

They are grouped below by **the need they would serve**, because a phase needs a
capability, not a vendor. All 22 are accounted for; none is dropped.

**Skills versus connectors.** Some rows in that set are skills already present on
this machine (`C-112`, `C-113`, `C-114`, `C-119`, `C-125`, `C-126`, `C-132`). For
those, "activation" means a **disposition change**, not an install — and under
`SKILL_SECURITY_POLICY.md` rule `R-9` a skill can never be more permissive than the
capability it invokes, so each is bounded by the connector in its own group.
Installing anything new belongs to `SKILL_INSTALLATION_PLAN.md` (phase owner's file).

---

## 2. Universal preconditions

**Every one of these must hold before *any* group's sequence begins.** They are
cumulative, not alternatives.

| # | Precondition | Basis | Status today |
|---|---|---|---|
| **P-1** | `SECURITY_POLICY.md` exists. No credential may be introduced into this project before it does | `D-027` (`UNRESOLVED`), `D-035`, `CLAUDE.md` §10, `BOUNDARIES` §5 | **Not met.** Phase 03 deliverable |
| **P-2** | `APPROVAL_POLICY.md` and `AUTONOMY_POLICY.md` exist, for anything touching the nine gated categories or any ladder move | `D-027`, `D-011`, `D-020` | **Not met.** Phase 03 deliverables |
| **P-3** | The phase that owns the capability has started, and its prerequisite gate passed | `D-007`, `MASTER_LINEAR_BUILD_PLAN.md` dependency rule | Phase 02 is current; every owning phase below is 05 or later |
| **P-4** | A `DECISIONS.md` row exists **before** activation, status `APPROVED`, owner-stated, traceable to `INTAKE_RECORD.md` | `CLAUDE.md` §5, `BOUNDARIES` §7.1; see §6 | **Not met** for any connector |
| **P-5** | Either the service costs nothing, or an explicit owner spend authorization exists. Metered use is spending | `NG-001`, `D-016`, `D-016a`, `D-011`, `CLAUDE.md` §6 | **Not met.** Organic only is in force and does not lapse on its own |
| **P-6** | The session inventory has been re-captured inside the current phase, and the affected registry rows re-derived | `SKILL_SECURITY_POLICY.md` §7.2 T1/T3 | Captured 2026-07-29; re-capture required at the owning phase |
| **P-7** | The ladder move is `DISABLED` → `SIMULATION` only. No stage may be skipped | `D-010`, `CLAUDE.md` §3, `BOUNDARIES` §4.4 | Everything is `DISABLED` today |
| **P-8** | If the capability collects, reads, or stores personal, lead, or contact data: `Q-009` is resolved and a retention policy exists | `BOUNDARIES` §5, `R-12` | **Not met** |

**If any precondition fails, the phase is blocked and must say so.** `CLAUDE.md` §10
is explicit: a phase that needs a credential before Phase 03 has produced the policy
is blocked — say so, do not proceed. Being blocked is the correct outcome
(`BOUNDARIES` §7.2).

---

## 3. The groups

Each group states: the need, the rows, the owning phase, the gates beyond §2, and
anything specific to it. The **ordered steps** and the **rollback** are in §4 and §5
and apply to every group; per-group deltas are noted inline.

### G1 — Email sending

| | |
|---|---|
| **Rows** | `C-057` (`plugin:resend:resend`, auth-required) · `C-125` (`resend`, `resend-cli`, `react-email`, `email-best-practices`) · `C-126` (`agent-email-inbox`) · `C-112` (`marketing:email-sequence`) |
| **Phase that would need it** | 16 (publishing/scheduling adapters) and 17 (community, messaging, lead routing) |
| **Gates beyond §2** | `D-011` — sending is *direct outreach*, always human-approved · `Q-009` — inbound email is personal data · `Q-008` — the only approver is the owner; an outbound queue with no backup approver stalls · `R-10` (consent/opt-out), `R-05` (messaging policy) |
| **Specific** | `C-126` is inbound: email content triggering agent action is exactly the untrusted-content surface `D-009` governs and Phase 23 must test. Its allowlist and sandbox patterns are legitimate **reading** for Phase 17 design; reading a skill's documented pattern is not activating it. `email-best-practices` is likewise reference material |
| **Ceiling** | `DRAFT_ONLY` for a long time. Sending to a real person is prohibited by `CLAUDE.md` §6 and cannot be reached by activating a connector — only by an owner decision plus the Phase 03 approval policy |

### G2 — CRM, contacts, and customer messaging

| | |
|---|---|
| **Rows** | `C-058` (HubSpot) · `C-059` (Klaviyo) · `C-060` (Intercom) |
| **Phase that would need it** | 17 (lead routing), 18 (analytics — read-only) |
| **Gates beyond §2** | `BOUNDARIES` §3 caps CRM at **read-only under Phase 18** and prohibits any write or contact-data import today — read-only "is the ceiling, and it is not authorized yet" · `Q-009` is binding, not advisory · `D-011` — Intercom touches *direct outreach* and *complaints* |
| **Specific** | Klaviyo and Intercom both send **and** store contact records; they fail `P-8` on two independent grounds. Selecting between them is also a data-residency question this project cannot answer while `Q-009` is open |
| **Ceiling** | Read-only, and only after `Q-009` and Phase 03's retention policy. No write, ever, without a separate owner decision |

### G3 — Research and web ingestion

| | |
|---|---|
| **Rows** | `C-119` (Bright Data acting skills, 16 of them) · `C-071` / `C-132` (TinyFish server and skills) · `C-113` (`marketing:competitive-brief`, `marketing:seo-audit`) |
| **Phase that would need it** | 08 (research and trend intelligence); consumed by 10, 12, 17 |
| **Gates beyond §2** | `D-009` / `BOUNDARIES` §6 — Phase 08 must build the untrusted-content boundary **first**; ingestion before the boundary exists is the failure the rule was written to prevent · `P-5` bites hard: Bright Data is metered and its own CLI skill advertises balance and budget checks, so use is spending · terms-of-service and licensing review, which is the License and Provenance Reviewer's scope, not this file's |
| **Specific** | `tinyfish:agent` **acts on** sites rather than only reading them — materially stronger than `WebFetch` and closer in kind to `C-045`. It should be considered separately from `fetch` / `search`, not activated as a bundle |
| **Ceiling** | `SIMULATION` at Phase 08, against a fixed corpus, with injection tests, before any live crawl |

### G4 — Analytics, SEO, and measurement

| | |
|---|---|
| **Rows** | `C-066` (Ahrefs, SimilarWeb, Supermetrics) · `C-067` (Amplitude, Amplitude EU) · `C-064` (BigQuery) · `C-114` (`marketing:performance-report`) |
| **Phase that would need it** | 18 (analytics/attribution), 19 (weekly operating cycle) |
| **Gates beyond §2** | `Q-003` — no KPI or target is defined, so what would be measured is undecided · `Q-005` — no account inventory exists, so whether the owner even holds these subscriptions is unknown · `C-064`: BigQuery bills per byte scanned, and `BOUNDARIES` §3 records Google Cloud as `NOT CONNECTED` with **no phase owning it** (`F-01-02`) — that plan gap must be resolved by the owner before Google Cloud anything · `C-067`: choosing between the EU and non-EU variant is a data-residency decision that cannot be made while `Q-009` is open |
| **Specific** | `C-114` produces a report. With no source connected and no KPI defined, a report generated today could only contain invented analytics values — named explicitly in `CLAUDE.md` §6's never-invent list. It is bounded by the connectors in this group and unlocks nothing on its own |
| **Ceiling** | Read-only. Phase 18 is manual-first by design; a connector is an optimization, not a prerequisite |

### G5 — Revenue data (Stripe, read-only)

| | |
|---|---|
| **Rows** | `C-031` (`stripe_api_read`, `stripe_api_search`, `stripe_api_details`) |
| **Phase that would need it** | 18 — read-only revenue adapters |
| **Gates beyond §2** | `BOUNDARIES` §3: "Read-only is the ceiling, and it is not authorized yet" · `Q-009` — Stripe records are customer personal data · `.env.example` already specifies a **restricted key with read scopes only**, and calls read-only a requirement rather than a preference |
| **Specific — the one that changes the shape of this group** | `.env.example` anticipates access arriving as a **project-held restricted key whose scope this project chooses**. But `stripe_api_write` (`C-030`) is present in this session as a **connector** tool. If that connector is authorized, write access to a payments API is reachable **with no variable in `.env` at all**, and the scope was chosen by whoever granted the connector. **A connector grant and a restricted key are not interchangeable.** If Stripe access is ever wanted, take it as a restricted key under `SECURITY_POLICY.md` — not by authorizing the MCP server, which cannot be scope-limited from inside this project |
| **Ceiling** | Read-only, restricted key, Phase 18, after `Q-009` |

### G6 — Brand and creative

| | |
|---|---|
| **Rows** | `C-068` (Canva) · `C-069` (`plugin:marketing:figma`) · `C-047` (`mcp__Figma__` read tools) |
| **Phase that would need it** | 07 (brand and creative system); consumed by 11, 13 |
| **Gates beyond §2** | `Q-006` / `D-025` — the brand-asset source location is unknown; Phase 07 is forbidden from inventing brand identity · `CLAUDE.md` §6 — changing brand identity is an absolute prohibition without owner authorization · `BOUNDARIES` §4.3 — major brand changes are a human checkpoint |
| **Specific** | `C-047` and `C-069` are **two independent paths to Figma with different authentication states** — one connector-backed, one on the auth-required list. Activating either without retiring the other leaves two doors to one room, only one of which anyone is watching. Pick one path in the decision row and say so |
| **Ceiling** | Read-only asset retrieval at most, and only after the owner answers `Q-006` by naming where brand assets actually live |

### G7 — Operator productivity surfaces (Gmail drafts, Calendar)

| | |
|---|---|
| **Rows** | `C-038` (`create_draft`, `update_draft`) · `C-041` (`create_event`, `update_event`, `delete_event`, `respond_to_event`) |
| **Phase that would need it** | 19 (weekly operating cycle) — plausibly, not necessarily |
| **Gates beyond §2** | `D-011` — a draft in a real mailbox is one human click from a send, and drafting outreach is inside the *direct outreach* gate · calendar invites and responses notify real people, which is sending under `CLAUDE.md` §6 · `Q-009` — both read personal data |
| **Specific — do not read an absence as a control** | `Ev §2.2` records that **no Gmail `send` tool was disclosed**. That is an observation about this session's tool list, not a guarantee about the underlying API, and a different plugin set or a later session may expose one. Never build a control on the absence of a tool |
| **Specific — the Google identity question** | Gmail and Calendar are Google surfaces. `Q-004` (Drive folder location and access) is the project's only `BLOCKED` item. If a Google connector is already authorized under the operator's Claude account, the project may simultaneously hold "no confirmed Drive access" and "a live Google grant." **This is a question for the owner, not a claim** — nothing here asserts either state |
| **Ceiling** | `D-003` assigns scheduling to deterministic code. A calendar connector is not the right instrument for Phase 19 even if it were permitted |

### G8 — Browser-driven action

| | |
|---|---|
| **Rows** | `C-045` — all 22 `mcp__claude-in-chrome__*` tools |
| **Phase that would need it** | None. |
| **Recommendation** | **No activation path. Do not plan one.** |
| **Why** | It reaches every system `BOUNDARIES` §3 lists as `NOT CONNECTED` with no credential, no `.env` entry, and no `SECURITY_POLICY.md` — so **none of §2's preconditions would even engage**, and a plan that lists preconditions which cannot bind is worse than no plan. `BOUNDARIES` §4.3 names captcha solving and terms acceptance as never delegable to an agent; `computer` + `form_input` + `file_upload` is the mechanism by which an agent would perform them. `D-003` requires deterministic code to enforce permissions and perform publishing — driving an authenticated browser is the opposite architecture: unauditable, non-reproducible, and indistinguishable in any log from the operator's own actions |
| **What to do instead** | Reach external systems through auditable, deterministic, scope-limited adapters built by the owning phase (`D-003`, Phase 16). If the owner nonetheless wants browser automation, that is a **boundary change**, and `BOUNDARIES` §7.1 reserves it to a Project Owner decision with rationale and evidence. It is not an activation step |
| **Interim** | Consider harness-level denial while working in this project — operator action, `SKILL_SECURITY_POLICY.md` §9 |

---

## 4. The activation sequence

**Applies to G1–G7. G8 has no sequence.** Steps run in order; a step may not start
until the previous one is complete and recorded.

| # | Step | Who performs it | Why that performer |
|---|---|---|---|
| 1 | Verify all §2 preconditions and write down which one each gate satisfies | Phase owner (agent) | Evidence, not assertion |
| 2 | **Write the `DECISIONS.md` row — before anything else happens** (§6) | Project Owner states it; phase owner records it | `BOUNDARIES` §7.1; only owner-stated decisions carry `APPROVED` |
| 3 | Confirm the account exists and who controls it | **Project Owner personally** | `Q-005` is unresolved; an agent cannot know and must not guess (`CLAUDE.md` §6) |
| 4 | Read and accept the provider's terms of service | **Project Owner personally** | `user-guide/USER_INSTRUCTIONS.md` "Human checkpoints": *Platform terms acceptance*. Never delegated to an agent |
| 5 | Complete identity/phone verification and any captcha, if required | **Project Owner personally** | Same list: *Captchas*, *Identity and phone verification* |
| 6 | Perform the OAuth consent, in an interactive `claude` session or in claude.ai connector settings | **Project Owner personally** | Same list: *Production OAuth consent*. This session is non-interactive and cannot do it regardless |
| 7 | Scope the grant as narrowly as the provider allows — read-only where read-only is the ceiling | **Project Owner personally** | The scope is chosen at grant time and cannot be narrowed afterwards from inside this project (see G5) |
| 8 | Re-capture the session inventory; confirm the server has moved off the auth-required list; re-derive the affected registry rows | Phase owner (agent) | The only way the repository learns that step 6 happened |
| 9 | Exercise the capability in `SIMULATION` per the owning phase's dry-run design. No live action, no real recipient, no spend | Phase owner (agent) | `D-010` — `DISABLED` → `SIMULATION`, no stage skipped |
| 10 | Review the simulation evidence and record the ladder move | **Project Owner** | A gate report recommends; it does not decide (`CLAUDE.md` §7) |
| 11 | Repeat 9–10 for each subsequent stage — `DRAFT_ONLY`, then `APPROVAL_REQUIRED` — one stage at a time | Phase owner, then Project Owner | `D-010` |

**Never compress steps 2 and 6.** Authorizing first and recording afterwards is the
exact failure §6 exists to prevent.

**Never treat step 8 as optional.** Without it, the repository's picture of its own
capability surface silently diverges from reality — which is `R-18` and the staleness
problem the registry warns about in its own header.

---

## 5. Deactivation and rollback

**The most important sentence in this section:** revoking the authorization **at the
provider or in the Claude account** is the only real deactivation. Changing a
disposition in a Markdown file deactivates nothing.

| # | Step | Who |
|---|---|---|
| 1 | Stop using it. Record the stop, with the reason, in `progress.md` | Phase owner |
| 2 | **Revoke the grant at its source** — claude.ai connector settings, or the provider's own account security page | **Project Owner personally** |
| 3 | If a credential was issued to this project, rotate it at the provider. If it ever appeared in a file, log, or commit, treat it as **compromised** and rotate regardless — deleting it in a later commit does not remove it from history (`F-01-06`, `.env.example`) | **Project Owner personally** |
| 4 | Record a **superseding** `DECISIONS.md` row. Do not edit the original — the register is append-only and history is not rewritten (`CLAUDE.md` §8) | Phase owner |
| 5 | Re-capture the session inventory and confirm the server no longer appears as available, or now appears on the auth-required list | Phase owner |
| 6 | Move the affected registry rows back to `PROHIBITED` and the ladder back to `DISABLED` | Phase owner |
| 7 | If any data was retrieved while it was active, apply the Phase 03 retention policy. If none exists yet, that is itself a reason the activation should not have happened | Phase owner + Project Owner |

**Rollback cost by group.** G1–G7 unwind to zero external state *if* step 9 of §4
(`SIMULATION` only) was honoured — nothing was sent, spent, published, or stored.
Once a capability passes `DRAFT_ONLY`, rollback stops being free: drafts exist in a
real mailbox, events exist on a real calendar, records exist in a real CRM. **The
cheap moment to reverse a decision is before stage two of the ladder, and that is
most of the argument for the ladder.**

---

## 6. The pre-authorization record requirement

**A `DECISIONS.md` row must exist *before* a connector is authorized, never after.**

**Why this is not bureaucracy.** One interactive authorization by the operator —
a few clicks in claude.ai connector settings, or one `/mcp` flow — activates a
server permanently, for every future session on this machine. **Nothing in this
repository would record that it happened.** No file changes. No commit is made. The
harness stops listing the server as requiring authentication, and that is the entire
trace. `CAPABILITY_REGISTRY.md` §D says it plainly: the authentication requirement is
a real control, but a thin one.

The asymmetry is total: authorization takes seconds and leaves no repository
evidence; discovering it after the fact requires someone to notice a changed line in
a session disclosure that nobody diffs.

**The required row, before the authorization:**

| Field | Content |
|---|---|
| ID | The next free `D-xxx`. **`DECISIONS.md` currently ends at `D-035`** — the Phase 02 Owner assigns the number; this file does not invent one |
| Date | The date the owner states the decision |
| Decision | Which connector, which account, which scope, which phase needs it, and what it may do |
| Status | `APPROVED` — owner-stated only. `APPROVED_IMPL` is **not** sufficient: a phase owner's reversible technical choice cannot authorize an external connection (`CLAUDE.md` §5) |
| Owner | Project Owner |
| Rationale | Which §2 preconditions are met and how; which phase is blocked without it |
| Evidence | `INTAKE_RECORD.md` reference for the owner statement, plus the re-captured inventory |

**Plus a standing rule the owner should adopt** (recommended here, decided by the
owner, ID assigned by the phase owner):

> Authorizing, installing, removing, or de-authorizing any connector, MCP server,
> plugin, or skill on the machine used for this project requires a `DECISIONS.md`
> row **before** the change, and a re-captured session inventory **after** it.

**If an authorization has already happened without a row** — including before this
plan existed — that is not a violation to conceal. Record it now, dated with what is
actually known, mark anything uncertain `UNRESOLVED`, and re-capture the inventory.
`CLAUDE.md` §6 forbids inventing account status; it does not forbid saying "this was
authorized at an unknown date."

---

## 7. How the owner verifies this themselves

Written for a solo operator who is not a specialist. **Nothing in this section
authorizes anything** — it is all inspection, and every step is safe to stop
partway.

**First, the thing that matters most.** There are **three separate surfaces**, and
checking one tells you nothing about the other two:

1. **Connectors** — services linked to your Claude account (Gmail, Calendar,
   Stripe, Figma, Supabase, and the rest).
2. **The Chrome extension** — Claude in Chrome, which uses the browser sessions you
   are already logged into. Not a connector, and not shown on the connectors page.
3. **Plugins and skills** — installed sets of instructions and tools, which may
   bring their own connectors with them.

**A note before you start.** This Phase 02 session was **non-interactive**, so no
sign-in or authorization flow could run in it, and none did. Everything below you do
yourself, in your own browser or your own terminal.

### 7.1 Check your connectors (claude.ai)

1. Open claude.ai in your browser and sign in.
2. Open **Settings**, then look for the **Connectors** section. (Product menus
   change; if the label differs, look for the section that lists linked apps or
   integrations.)
3. Read the list. For each entry, ask one question: **do I recognise this, and do I
   want an AI session to be able to use it?**
4. Anything you do not recognise, or do not want: **disconnect it.** Disconnecting is
   always safe. If you later need it, you can reconnect — and per §6 you would record
   a decision row first.
5. Write down the list. That list is the answer to "which connectors are actually
   authorized," and it is the one fact this project could not determine for itself,
   because finding out by using them is exactly what the boundary rules forbid.

### 7.2 Check MCP servers from a terminal

The harness itself names two entry points for this, and this session was told them
directly: **`/mcp` inside an interactive `claude` session**, and the **`claude mcp`
command** in a terminal.

1. Open a terminal and start Claude Code interactively (`claude`).
2. Type `/mcp` and press Enter. It lists the MCP servers this machine knows about
   and their connection state.
3. For the command-line version, run `claude mcp` on its own, or with `--help`, to
   see the available subcommands. **Confirm the exact subcommand and flags from that
   output rather than from any document, including this one** — command syntax
   changes between versions, and this plan deliberately does not guess at flags.
4. If you want to see the full list of slash commands available in a session, type
   `/help`.

### 7.3 Check the Chrome extension

There is no connectors page for this one. Check it in Chrome itself: open your
extensions and look for the Claude browser extension. If it is installed and
enabled, an agent session that has the corresponding tools can act inside the sites
you are logged into.

**This project's recommendation is that it should not be usable while working on
this repository** (`CAPABILITY_REGISTRY.md` `C-045`; `CONNECTOR_ACTIVATION_PLAN.md`
§3 G8). Turning it off is your call and is reversible from the same place.

### 7.4 Check plugins and skills

Plugins are the third surface, and the one most likely to have grown without you
noticing — several in the 2026-07-29 inventory relate to advertising, lead
prospecting, email sending, and web scraping, none of which this project is
authorized to do. From an interactive `claude` session, type `/help` and look for the
plugin management command; use that to list what is installed. **Confirm the exact
command name from `/help` rather than from this document.**

### 7.5 What to do with what you find

- **Something you do not recognise:** disconnect or disable it. Safe, reversible,
  and it costs nothing to be wrong in that direction.
- **Something you recognise but do not want an AI session using:** same action.
- **Something you want to keep:** tell your Claude Code session, so it can be
  recorded in `DECISIONS.md` and the capability registry re-derived. An agent cannot
  see your connector settings and will not learn about it any other way.
- **You are unsure:** leave it, and write the name down. Uncertainty stays
  `UNRESOLVED` in this project; it is never resolved by guessing (`D-008`).

### 7.6 How often

At minimum, before every phase gate, and any time you install or authorize
something. The capability list lives on your machine, not in this repository, so
**this repository has no way to notice when it changes** — you are the detection
mechanism (`SKILL_SECURITY_POLICY.md` §7.2).

---

## 8. What this plan does not establish

Stated so no later phase mistakes silence for a clean result.

- **That any connector is or is not authorized.** Never probed, never claimed
  (`Ev §0` Limit 3). `UNRESOLVED` throughout.
- **That the connector list is complete or accurate.** It was not cross-checked
  against on-disk configuration, because that requires a read outside the project
  root that `BOUNDARIES` §1 does not grant.
- **That any provider supports the integration a later phase would want.** No
  provider documentation was fetched and no API surface was verified.
- **Any cost figure.** `P-5` says metered use is spending; it does not say what
  anything costs. No price is asserted anywhere in this file.
- **Licence, provenance, publisher identity, or terms of service** for any plugin or
  connector. That is the License and Provenance Reviewer's scope.
- **That the exact UI labels in §7 are current.** Product interfaces change. §7 names
  destinations and tells the operator to confirm labels and command syntax from the
  product itself, which is why it does not fabricate a single flag.
- **Any permission whatsoever.** See the banner at the top.
