# Publishing Policy

**Owner of this file:** Marketing Operations Reviewer (specialist), Phase 03, run `phase-03-2026-07-30-b`.
**Status:** Binding on every Phase 03 deliverable and every later phase that touches publishing (10, 11, 13, 15, 16). Prose that describes and justifies rows in `policy/action_registry.json`; where this document and the registry disagree, that is a defect to raise, not silently reconcile (`policy/POLICY_CONTRACT.md` §1).
**Precedence:** `README.md`, `DECISIONS.md`, `docs/PROJECT_BOUNDARIES.md`, `INTAKE_RECORD.md`, `CAPABILITY_REGISTRY.md`, `SKILL_SECURITY_POLICY.md` govern first; then `CLAUDE.md`; then `policy/POLICY_CONTRACT.md`; then `policy/action_registry.json`; then this document.

**Superseded-content notice.** An earlier version of this file, dated to the discarded first Phase 03 attempt (`phase-03-2026-07-30-a`), was found still sitting untracked in this working tree when this run began — `git reset --hard` restores tracked files to a commit but does not delete untracked ones, and the first attempt's draft was never committed. That version was written on the false premise that "Phase 02 was never executed" (`F-03-01`) and cited invented decision IDs (`D-036`–`D-042` in a sense that collided with the real register). This version replaces it in full, against the real, merged Phase 02 state: `CAPABILITY_REGISTRY.md` (141 rows), `SKILL_SECURITY_POLICY.md`, and the real `D-036`–`D-048`. Disclosed in the handoff rather than silently overwritten.

**What this document is for.** Every publishing capability is `DISABLED` today (`D-010`, `CLAUDE.md` §13). No publishing adapter exists (Phase 16), no approval queue exists (Phase 15), and platform selection has not occurred (Phase 10). This is not a policy for a live capability — it is the policy that will bind the capability **when it is eventually built**, written now so the rules exist before there is anything to enforce them on. Everywhere below, read "the answer today is DENY" as the operative fact and the rest as the rule that will apply once a precondition is satisfied.

---

## 1. Definition of "publish"

**The test:** an action is **publishing** if its content becomes reachable by any audience other than the Project Owner — regardless of mechanism, delay before reachability, platform, claimed visibility setting, or whether the actor believes the audience is small, temporary, or non-public.

Drafted deliberately broad because the failure mode this policy exists to prevent — content reaching someone the owner never reviewed it for — does not care how the content got there.

**Edge cases, resolved against the test:**

| Case | Publishing? | Why |
|---|---|---|
| A draft saved as a file in this repository | **No** | Reaches no audience but whoever reads the repo, and the repo's only human audience is the Project Owner (`ACT-P02`, `ALLOW`). Drafting is inside the gates by construction. |
| A post scheduled for future release | **Yes** | Content still reaches a non-owner audience; the delay changes *when*, not *whether* (`ACT-P04`, `DENY`). |
| A "private" or unlisted URL shared with anyone other than the owner | **Yes** | "Unlisted" restricts discovery, not access. Anyone holding the link is a non-owner audience. A platform's own privacy label is not equivalent to non-publication. |
| A preview or staging link sent to a third party (reviewer, a test account not solely controlled by the owner, a link-preview bot) | **Yes** | The audience test is about reachability, not intent. A preview link a non-owner can open has been published to that non-owner. |
| A test post on a real, live account (even one marked "test") | **Yes** | Real content on a real account reachable by the platform's real audience, including anyone who views it, search indexers, and platform-internal systems. No "test post" exemption exists in the registry. |
| A comment or reply on someone else's post | **Yes** | Reaches the post's audience, never solely the owner. Also implicates `MESSAGING_POLICY.md` if directed at a specific person — a public reply is simultaneously a publish and, in substance, a send; both gates apply. |
| A profile bio, display name, or account-metadata update | **Yes** | Visible to anyone who views the account — content reaching a non-owner audience like any other field. |
| A story, ephemeral post, or anything that expires after a fixed window | **Yes** | Expiry limits duration, not reach during the window it is live. This document asserts no specific platform's expiry duration — that is a platform fact to verify at time of use (§6), not to state here. |
| Publishing content to a third-party-hosted artifact/preview page reachable by anyone with the link | **Yes** — see §8 | A distinct case from an ordinary preview link: no credential is used to reach the audience at all. |

**Consequence for this project:** because every audience-reaching case above is publishing, and every publishing capability is `DISABLED`, none may occur today under any framing — "just a test," "nobody will see it," "it expires anyway," and "no account or credential was used" (§8) are none of them exceptions this policy recognizes.

---

## 2. Current state: all publishing is DENY

**Row:** `ACT-P01` — "Publish any content to any public or non-owner audience" — outcome `DENY`, all roles (`PHASE_OWNER`, `SPECIALIST`, `RUNTIME_AGENT`).

**Basis:** `NG-002` (no production launch, publishing, sending, or account creation before designated phase gates), `D-010` (maturity ladder — every production-facing capability is `DISABLED`), `R-08` (unauthorized publishing rated Critical impact if realized). Reinforced by `CLAUDE.md` §6's absolute prohibition on publishing anything publicly without recorded owner authorization.

**Why `DENY` and not `BLOCKED`:** both resolve identically at runtime (`BLOCKED` is "treated as `DENY`" per the outcome enum), but `DENY` is correct here because publishing is *categorically* prohibited by architecture rule and owner-facing non-goal, not merely unevaluable for lack of a prerequisite. `ACT-P03` (dry-run) and its downstream dependents are `BLOCKED` for missing-prerequisite reasons; `ACT-P01` itself is `DENY` on the merits.

**What would have to change for this to become `APPROVAL_REQUIRED`:** every item in the preconditions chain (§3) would need to be satisfied, *and* a Project Owner decision recorded in `DECISIONS.md` would need to explicitly promote the specific capability off `DISABLED` (`ACT-G01`, `OWNER_ONLY`, gated further by promotion preconditions `PP-1`–`PP-5`, see §3). No agent narrows this preconditions list, and no agent may treat their satisfaction as self-evident (`ACT-G04` — a phase owner may assemble evidence, but that assembly "carries no weight on its own," per `findings.md` `F-00-05`).

---

## 3. Preconditions chain

Ordered by real dependency — each item requires the ones above it.

| # | Precondition | Owning phase | Status today |
|---|---|---|---|
| 1 | A `CAPABILITY_REGISTRY.md` entry exists for the specific publishing capability, with use-disposition `PERMITTED` | Phase 02 | **`CAPABILITY_REGISTRY.md` now exists** — 141 rows, delivered by Phase 02 and merged into `main` (`D-037`, `D-039`; `PP-1`, status `PARTIALLY_SATISFIABLE`). An entry existing is necessary but not sufficient: the disposition must be `PERMITTED` for the specific capability, and today the one publishing-adjacent row in the registry, `C-009` (`Artifact`), is dispositioned `PROHIBITED` (§8). No social-platform publishing capability has a registry row at all, because no platform-specific adapter exists yet. Also recall `D-039`: the registry is a **dated snapshot**, not a repository property — it must be re-captured before a later phase relies on it. |
| 2 | The target platform is actually selected (not merely a named candidate) | Phase 10 | **Not selected.** Facebook, Instagram, WhatsApp, and TikTok are `CANDIDATE ONLY` — directional interest the owner named in free text at intake (`INTAKE_RECORD.md` Q3), explicitly not a rollout order, launch commitment, or complete set (`D-017`, `D-018`, `OPEN_QUESTIONS.md` Q-002). Nothing before Phase 10 may treat them as selected. |
| 3 | A production account exists on the selected platform | Owner action (`ACT-C10`) | **No account exists.** Account creation is `OWNER_ONLY` — an agent may prepare launch materials (Phase 11) but may never submit the creation itself, complete identity/phone verification, or accept platform terms (`ACT-C09`, `ACT-C10`, `ACT-C11`, all `OWNER_ONLY`). |
| 4 | A publishing adapter exists for the platform | Phase 16 | **Does not exist.** No adapter has been built for any platform. |
| 5 | An approval queue exists, capable of binding an approval to one artifact digest | Phase 15 | **Does not exist.** Without it there is no mechanism to hold a `PENDING_APPROVAL → APPROVED` transition (`policy/POLICY_CONTRACT.md` §6) for a piece of content. |
| 6 | The capability's autonomy stage has been promoted at least to `APPROVAL_REQUIRED` by the Project Owner, one stage at a time, with no stage skipped | `D-010`, `ACT-G01` | **`DISABLED`** — the stage of every production-facing capability as of 2026-07-30. Promotion additionally requires `PP-2`–`PP-4` (satisfied in principle, not yet exercised for any real capability) and `PP-5` — minimum dwell time and numeric incident thresholds, which are `UNRESOLVED` (`D-047`; no numeric value may be invented, `D-021`, `NG-004`, `OPEN_QUESTIONS.md` Q-003). |

**Reading this table honestly:** item 1 is now partially satisfiable in a way it was not in the discarded first attempt, but no platform-publishing row is `PERMITTED` today; items 2–5 remain unsatisfied; item 6 cannot be evaluated because item 1's specific-capability condition and `PP-5` both remain open. Publishing is not "almost ready" — it is missing every load-bearing piece simultaneously, and the one piece that changed (the registry existing) changed the shape of the gap without closing it. A future phase reading this table should treat a claim that publishing is closer to ready than this as a finding to investigate, not accept.

---

## 4. Dry-run / SIMULATION first

The maturity ladder requires `DISABLED → SIMULATION` as the first promotion (`D-010`; `policy/POLICY_CONTRACT.md` §7), and `SIMULATION` is defined as exercising the capability with no live effect — a dry run.

**Row:** `ACT-P03` — "Dry-run a publish with no network egress" — outcome `BLOCKED`.

**Why it is `BLOCKED` rather than merely unstarted:** a dry run has to run *something* — a publishing adapter, in stub or simulated form, that the dry run exercises. There is no adapter (§3 item 4). The registry existing (§3 item 1) is necessary but does not itself create an adapter to simulate. `SIMULATION` cannot be entered by fiat; it requires an artifact to simulate. Until Phase 16 produces that artifact, "dry-run first" is a correct rule with nothing yet for it to apply to.

This matters for sequencing: a future phase should not treat "we skipped `SIMULATION` because there was nothing to simulate" as an acceptable substitute for actually building and exercising a dry-run path once the adapter exists. `PP-2` ("the prior stage was actually exercised, with recorded evidence of the exercise") is not satisfied by an adapter's mere existence — it requires the dry run to have actually run and its evidence recorded.

---

## 5. Content gates

Of the nine gated categories (`GC-01`…`GC-09`, `policy/POLICY_CONTRACT.md` §8), five bite directly on published content:

- `GC-01` claims
- `GC-02` pricing
- `GC-03` discounts
- `GC-04` testimonials
- `GC-07` controversial topics

**Row:** `ACT-P05` — "Publish content touching any of the nine gated categories" — outcome `DENY` today (because all publishing is `DENY`), citing gated categories `GC-01, GC-02, GC-03, GC-04, GC-07` explicitly. **When publishing is eventually enabled, this row becomes `APPROVAL_REQUIRED` and never weaker** — it cannot resolve to `ALLOW` or `ALLOW_LOGGED` under any future capability build, because `D-011` and the owner-stated `D-020` ("the nine gated categories stay human-approved regardless of owner workload") apply to content regardless of the autonomy stage the *platform connection* has reached. Autonomy-ladder promotion governs how much a capability may act without a human in the loop for *ungated* work; it does not touch the nine categories at all (`policy/POLICY_CONTRACT.md` §8: "automate aggressively within the gates, never through them").

`GC-05` (direct outreach) and `GC-06` (complaints) govern sends to individuals, not publishing to an audience; they are `MESSAGING_POLICY.md`'s to define. `GC-08` (spending) and `GC-09` (paid advertising) govern money moving, not content reaching an audience — a *boosted* or paid-promoted post crosses into `BUDGET_POLICY.md`'s territory (`ACT-M03`) in addition to this policy's, and both gates would need to clear independently.

**How content must be screened before it can even enter an approval queue** (structural requirement — the queue itself is Phase 15's, and does not exist yet, §3 item 5): before any draft is submitted for approval, a deterministic check must classify it against `GC-01`–`GC-04` and `GC-07` and tag which categories it touches, so the approval record itself carries that tag and the Project Owner reviews a labeled artifact rather than independently rediscovering what is being asked of them. This is a requirement on the design of the future approval queue, not a control that exists today — no screening code exists, and this document does not claim otherwise.

---

## 6. Platform-policy compliance

Candidate platforms (Facebook, Instagram, WhatsApp, TikTok) each carry their own policy regimes governing what content may be published, how, and how often. `R-04` records that Facebook, Instagram, and WhatsApp share Meta's business-account infrastructure, so a policy action on one can cascade to the others. `R-05` records — as general platform-policy knowledge, not a specific asserted clause — that WhatsApp Business messaging carries opt-in/consent rules and that TikTok enforces its own content and commerce policies. `R-06` records that platform APIs and terms of service change over time, and that a rollout plan or adapter built against today's understanding may be stale by the time a later phase (13, 16) actually implements it, given the length of this project's build plan.

**The requirement this document states:** any future phase that builds toward publishing must **re-verify the relevant platform's current policy at the time that phase does its work**, not rely on this document's era of understanding or any earlier phase's notes. This project asserts **no specific platform policy clause, rate limit, API capability, or terms-of-service provision** — doing so would violate the invention prohibition (`D-008`, `ACT-N03`: never invent platform permissions). Where a future phase needs to state a platform rule as a fact, it must cite the platform's own current documentation directly, dated, not this policy.

---

## 7. Rollback

**What "unpublish" can achieve:** deleting or retracting a post from the account that published it, where the platform supports deletion, removes it from that account's own feed and (where the platform's deletion is effective) its own future distribution.

**What it cannot achieve, and must not be assumed to achieve:** a public post may already have been viewed, screenshotted, cached by a search engine or web archive, quoted or embedded elsewhere, or syndicated by the platform itself (notifications already sent, algorithmic feeds already populated, third-party aggregators already pulled it). None of these are reversed by deleting the original. **Deletion is not undo.**

**Why this matters for how high the gate has to be:** publishing is functionally closer to irreversible than the mechanics of a "delete" button suggest, so the approval that authorizes it must be taken as seriously as an irreversible action even though the platform technically allows retraction. Consistent with the approval state machine's own design (`policy/POLICY_CONTRACT.md` §6): an approval binds to **one specific artifact digest**, and any change to the artifact voids it (`artifact_digest_mismatch → VOIDED`). There is no "publish now, fix it after" path in this project's model — the artifact that gets published must be the exact artifact that was approved, precisely because what goes out cannot be fully called back.

---

## 8. Borrowed authority: publishing with no credential this project holds (`ACT-P06`)

**This case is new to this attempt, and it is this document's headline finding.** Phase 02's real, merged capability inventory identified `C-009` (`Artifact`) in `CAPABILITY_REGISTRY.md`: a tool that renders repository content to a page hosted on `claude.ai`, reachable by anyone holding the link, one click from shareable, sitting entirely outside this project's Git history. Its disposition is `PROHIBITED` (`CAPABILITY_REGISTRY.md` `C-009`; basis `CLAUDE.md` §6; `docs/PROJECT_BOUNDARIES.md` §4.1, §7.5; `D-001`).

**Why this is publishing under §1's test, and why it is a *distinct* case from an ordinary preview link:** an ordinary shared preview link (§1's table) still generally involves a credential or account this project's controls can see — a platform login, an account this project could in principle track. Artifact publishing does not. **No credential in `.env`, no Secret Manager entry, no platform account, and no `SECURITY_POLICY.md` provision governs it at all**, because none is used. The page is served through the operator's own Claude account (`CAPABILITY_REGISTRY.md` §I; `F-02-03` Class B: "the operator's Claude account"). Content reaches a non-owner audience the moment the link is shared, using an authority this project never held a credential for and therefore could never have withheld a credential to prevent.

**This is the same shape of exposure `SECURITY_POLICY.md` addresses in general (per `F-02-03`: "this project's controls govern the credentials it holds; its exposure is governed by the authority it borrows"), applied here specifically to publishing.** `SECURITY_POLICY.md` — owned by the Security Architect in this same phase — is the file that frames the general borrowed-authority pattern and its five classes (browser session, Claude account, connector grants, harness egress, plugin-held credentials); this document does not restate that framing and cites it by name only. What this document owns is the **publishing-specific consequence**: that a credential-free path to a non-owner audience is still `ACT-P01`'s "publish," and it fails `ACT-P01`'s gate exactly as a credential-bearing publish would, for the same reason and via the same policy — not a weaker rule because no account was involved, and not a stronger one either. The gate does not ask "was a credential used"; it asks "did content reach a non-owner audience."

**Row:** `ACT-P06` — "Publish content to a third-party-hosted artifact/preview page reachable by anyone with the link" — outcome `DENY`, all roles (`PHASE_OWNER`, `SPECIALIST`, `RUNTIME_AGENT`). Basis `NG-002`, `R-21`. Escalation `ESC-001` (boundary conflict) — and, because invoking or nearly invoking this capability is itself the borrowed-authority pattern, a near-invocation additionally escalates under `ESC-011` (`F-02-03`, `R-21`).

**What would have to change:** nothing in this document proposes a different preconditions chain for `ACT-P06` than §3's — the registry entry (§3 item 1) exists and is `PROHIBITED`, which is a stronger bar than `UNRESOLVED`. Reversing that disposition is `CAPABILITY_REGISTRY.md`'s call, not this document's or this phase's (`policy/action_registry.json` `ACT-W15`: changing a registry disposition is `DENY` for `PHASE_OWNER`/`SPECIALIST` — a Phase 02 finding to escalate, never a Phase 03 edit). Even if the disposition changed, `ACT-P06` would still need every other §3 precondition an ordinary publish needs, because the *audience* question (§1) is identical regardless of which door the content went through.

**Nothing was invoked.** This section documents a rule against a capability that exists in the registry and has never been used by this project.

---

## 9. Failure handling

None of the following can occur today, because no adapter, queue, or artifact-publishing authorization exists to fail (§3, §8). This section states the rules that must govern them once they can occur.

- **Partial publish across platforms.** If a single approved artifact is meant to go to more than one platform and succeeds on some and fails on others, the failure is **not** silently retried to completion. A partial publish is treated as an incident: what published, where, and what did not must be recorded, and remaining platforms are not auto-attempted without confirming the artifact and approval are still valid.
- **Duplicate publish (idempotency).** An approval is single-use — `APPROVED → EXECUTED` is a one-time transition and `EXECUTED` is terminal (`policy/POLICY_CONTRACT.md` §6, invariant 4). Any retry logic must be keyed to the approval's identity and the artifact digest so that a retried or re-run publish attempt cannot claim the same approval twice or post the same content twice under transient-failure recovery. A naive "retry until success" loop is unsafe here for the same structural reason it is unsafe for messaging (`MESSAGING_POLICY.md` §11): the real-world side effect (a live post) cannot be un-caused by detecting the duplicate after the fact.
- **Approval expires mid-flight.** If a multi-platform publish is in progress when the bound approval reaches its validity window (`APPROVED → EXPIRED`, `validity_window_elapsed`) or is superseded, no further platform legs may execute under that approval. This is `ESC-005` (approval expired, stale, or queue exceeded its age limit) and must halt and escalate rather than complete "since it was already approved a moment ago."
- **General principle:** every failure mode above resolves toward *halt and escalate*, never toward *proceed on inference*. `ACT-A04` denies treating silence, a timeout, or a non-response as approval; the same posture applies to inferring that a stalled or partially-failed publish should be pushed through to completion.

---

## 10. Capability classification

Honest classification per `CLAUDE.md` §3 and `policy/POLICY_CONTRACT.md` §4 — nothing below is `IMPLEMENTED`, because a document describing a control is not the control:

| Element | Classification | Why |
|---|---|---|
| This policy document and its `action_registry.json` rows (`ACT-P01`–`ACT-P06`) | `SCAFFOLDED` | The rules exist and are machine-checkable in the registry; no runtime code evaluates a real publish attempt against them, because no publish attempt is possible yet. |
| Content-gate screening described in §5 | `PROPOSED` | Described here as a requirement on a future approval queue; no screening code exists. |
| Publishing adapter (any platform) | `PRODUCTION_BLOCKED` | Phase 16's deliverable; does not exist; blocked behind Phase 10 platform selection. |
| Approval queue | `PRODUCTION_BLOCKED` | Phase 15's deliverable; does not exist. |
| Dry-run / `SIMULATION` capability | `PRODUCTION_BLOCKED` | Cannot be built or exercised without the adapter it would simulate (§4). |
| Artifact-publishing borrowed-authority path (`C-009`, `ACT-P06`) | `PRODUCTION_BLOCKED` | Exists as a capability in the observed session surface, but is dispositioned `PROHIBITED` in `CAPABILITY_REGISTRY.md` and `DENY` here — a documented prohibition against a real capability, not a built control. |
| Draft-only writing to this repository (`ACT-P02`) | `IMPLEMENTED` in the only sense that matters here — ordinary file writing, already possible and already governed by `ACT-W01`/`ACT-W02`. Not a "publishing capability"; the absence of one. |

No capability described in this document may be asserted as `IMPLEMENTED` in any future phase's documentation merely because this policy, or `CAPABILITY_REGISTRY.md`, describes it. `CAPABILITY_REGISTRY.md` is a dated snapshot (`D-039`) — re-verify its rows before relying on any of the statuses above at a later phase gate.
