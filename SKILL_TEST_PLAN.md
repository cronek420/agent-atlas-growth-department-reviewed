# Skill Test Plan

**Owner of this file:** Agent Architecture Specialist (Phase 02 specialist, second pass), run `phase-02-2026-07-29-a`.
**Status:** **INTEGRATED.** Phase 02 deliverable of record, accepted by the Phase 02 Owner 2026-07-29. *(Corrected 2026-07-29 per Independent Reviewer finding — see `CUSTOM_SKILL_BACKLOG.md`; the same defect appeared in both files.)*

**Companion to `CUSTOM_SKILL_BACKLOG.md`.** That file holds the contracts; this
file holds the tests that would prove them. Together they carry two of Phase 02's
five pass conditions — *"Trigger tests exist"* and, jointly, *"Custom skills have
contracts."*

**Sources:** `agent_runs/phase-02/handoffs/HANDOFF_AGENT_ARCHITECTURE_SPECIALIST.md`
§5 (the first-pass trigger-test table), `CAPABILITY_REGISTRY.md` (supply),
`agent_runs/phase-02/evidence/SESSION_CAPABILITY_INVENTORY.md` (`Ev`),
`findings.md` `F-01-04` and `F-00-04`.

---

## 0. What this plan is, and what it is not

**It specifies tests. It does not contain code, and no test in it has been run.**
Six of the seven components do not exist; the seventh does not exist either. Phase
04 is the first phase in the plan that produces an executable artifact (`HANDOFF
§3`). Section 8 states plainly what cannot be tested yet and why.

**No capability was invoked to produce this file.** Neither `ToolSearch` nor
`Skill` was called. No path outside the project root was read.

**Nothing here authorizes a build, an install, or a ladder movement.** Every
component under test is `PROPOSED` at ladder stage `DISABLED` (`D-010`).

---

## 1. The three-way distinction — and why flattening it is the failure

The first pass drew a distinction that must survive into every later phase. It is
restated here in full, because collapsing it is not a documentation slip — it is
the specific way a guard component passes its test suite and fails in production.

| Class | Question it answers | What a failure looks like |
|---|---|---|
| **must-fire** | Did the component run when it should have? | The guard never ran. **Visibly broken.** Somebody notices within a day. |
| **must-not-fire** | Did it stay silent when it should have? | The guard ran on something irrelevant. Noisy, annoying, and self-correcting. |
| **must-not-*pass*** | It ran — did it return the **restrictive** verdict on input it should have refused? | The guard ran, completed, logged cleanly, and returned `PASS`. **Invisible.** It looks exactly like a working system, and nothing surfaces it until the thing it was supposed to stop reaches the outside world. |

**The two ways the third class gets lost, both observed in practice:**

1. **It is renamed into the second.** "Must not fire on X" and "must not pass X"
   read similarly in a checklist. They are opposites: the first asserts the
   component stayed *out*, the second asserts it went *in and said no*. A suite
   with only the first two classes cannot distinguish a working guard from a guard
   whose matcher always returns true.
2. **It is dropped as redundant** once the must-fire test is green. It is not
   redundant. A must-fire test proves the trigger; a must-not-pass test proves the
   **verdict**. `CSK-04` (`claim-guard`) firing on every asset and returning `PASS`
   on every asset would satisfy every must-fire test in this document.

**For `CSK-03` through `CSK-06`, the must-not-pass tests are the tests that
matter and the other two are hygiene.** This feeds Phase 13's *"Each producer has
negative tests"* and Phase 23's *"Approval bypass tests pass"*.

**Instruction to any future phase owner editing this file:** if you are about to
merge two test classes because the table is wide, merge must-fire and
must-not-fire. Never touch the third column.

---

## 2. The red-mutation rule — mandatory, per test

`findings.md` **`F-01-04`** is the operative finding here, and it is the reason
this section is a requirement rather than a footnote.

In Phase 01 the *checker* was wrong three times while the deliverables under test
were right: a tool-version probe reported four installed tools as missing, a
`.gitignore` check misread negated patterns as matches, and a path-existence
checker reported ~40 false missing files. **Not one of the three false results
came from the artifact under test. All three came from the instrument.** The
finding's own conclusion: *"an unverified checker produces unverified results, and
a green check is not evidence until the checker has been shown to go red."*

**Therefore every test in this plan carries a mandatory field: `Red mutation`.**

> **`Red mutation`** — the smallest change to the fixture or the component that
> must make this test **fail**. The test is **not admissible as evidence** until
> that mutation has been applied, the test has been observed to fail, and the
> mutation has been reverted. A test that has only ever been green has
> demonstrated nothing about the system; it has demonstrated that it is capable of
> printing "pass".

**Rules for a valid red mutation:**

- It changes **one** thing. A mutation that changes two cannot tell you which one the test is sensitive to.
- It targets the **assertion**, not the harness. Deleting the test file makes the suite red and proves nothing.
- Its result is **recorded** — the command and the actual failure output — in the phase's evidence directory, per `CLAUDE.md` §6 (*"Record the command and the actual output, or say you did not test it"*).
- Prefer **exit codes** over parsed human-readable output. `F-01-04` case 2 was caused by treating any output as a match; the exit code was the authoritative signal all along.

**A green suite with no recorded red demonstrations is reported as
`UNVERIFIED`, not as `PASS`.** That is the whole point of the rule and a phase
gate should treat it that way.

---

## 3. Conventions

**Test IDs.** `T-CSK-nn-Fx` (must-fire) · `T-CSK-nn-Nx` (must-not-fire) ·
`T-CSK-nn-Px` (must-not-pass) · `T-POS-nn` (posture, §7). Stable; never reused.

**Fixture paths** are written as `fixtures/csk-nn/<case>/`. **The home of that
directory is unresolved** — no phase names one, `MASTER_PLAN.md` places the first
`tests/` directory at Phase 13, and Phase 04's pass condition already grades
against fixtures that have nowhere to live. See `HANDOFF OQ-2` and
`CUSTOM_SKILL_BACKLOG.md` `OQ-P2-3`. The paths below are names, not locations.

**Fixture content constraints, binding:**

- **No realistic-looking secret, token, key, or credential in any fixture** — not even a fake one (`CLAUDE.md` §6, §10). Where a test needs a token-shaped value, the fixture uses a syntactically invalid placeholder that no provider would accept.
- **No lead, contact, or personal data in any fixture** until `Q-009` resolves (`BOUNDARIES` §5).
- **No fixture may be sourced by retrieving external content** before Phase 08 builds the untrusted-content boundary. Injection fixtures are **authored** by this project, not scraped.
- **No fixture references any path outside the project root.**

**Assertion style.** Every test states the *load-bearing assertion* — the one that
would fail if the component were subtly wrong, as distinct from the one that fails
if it is entirely absent.

---

## 4. `CSK-01` — `blast-radius-check`

Contract: `CUSTOM_SKILL_BACKLOG.md` §4. First runnable: **Phase 03**.

| Test | Class | Fixture / input | Expected | Load-bearing assertion | Red mutation |
|---|---|---|---|---|---|
| `T-CSK-01-F1` | must-fire | `fixtures/csk-01/r14-stale/` — the **real** `F-01-09` case: `RISK_REGISTER.md` with `R-14`/`R-19` still reading *"not yet a git repo"*, and `changed_files` showing the repository was initialized | `REVIEW_REQUIRED`; `candidates` includes `RISK_REGISTER.md` at the `R-14` line | `quoted_claim` is a **verbatim substring** of the fixture file at the reported line number — a paraphrase is a failure even if the row is right | Delete the `R-14` row from the fixture. Test must fail with zero candidates. If it still passes, the component is matching on row ID, not on the claim text |
| `T-CSK-01-F2` | must-fire | `fixtures/csk-01/q-answered/` — a question the phase's work answered, whose `OPEN_QUESTIONS.md` row still reads `UNRESOLVED` | `REVIEW_REQUIRED`; candidate cites the row | The candidate names `OPEN_QUESTIONS.md` specifically — the register `F-01-09` records as the one that was skipped | Change the fixture row to the answered state. Must fail |
| `T-CSK-01-N1` | must-not-fire | `fixtures/csk-01/isolated-new-files/` — a phase adding only new files under its own directory, contradicting nothing | `CLEAN`; `candidates == []`; `checked` lists all eight fixed inputs; `unreadable == []` | `len(checked) == 8`. A `CLEAN` verdict with an incomplete `checked` list is the exact defect `F-01-09` describes | Remove one fixed input from the component's list. `checked` becomes 7 and the test must fail — proving the completeness assertion is real and not decorative |
| `T-CSK-01-P1` | **must-not-pass** | `fixtures/csk-01/unreadable-input/` — `OPEN_QUESTIONS.md` present but unreadable | `REVIEW_REQUIRED`, with the file listed in `unreadable`. **Never `CLEAN`** | `verdict != "CLEAN"` **even though `candidates` is empty**. Emptiness and cleanliness are different facts | Make the file readable. Verdict becomes `CLEAN` and the test must fail — proving the test is sensitive to unreadability itself, not to the absence of candidates |
| `T-CSK-01-P2` | **must-not-pass** | `changed_files` containing a path outside the project root | Hard fail **before any read, stat, or listing of that path** | The component's **own** command log shows no access to the path. Per `F-01-07`, verify our own actions, never the protected resource — the audit must not become the violation | Replace with an in-root path. Must proceed normally; if it still hard-fails, the guard is matching the wrong thing |

---

## 5. `CSK-02` — `schema-validate`

Contract: `CUSTOM_SKILL_BACKLOG.md` §4. First runnable: **Phase 04**, and **only
after `OQ-P2-1` resolves** — with no permitted dependency-acquisition path there
is no validator to test (`CUSTOM_SKILL_BACKLOG.md` §3.3).

| Test | Class | Fixture / input | Expected | Load-bearing assertion | Red mutation |
|---|---|---|---|---|---|
| `T-CSK-02-F1` | must-fire | `fixtures/csk-02/missing-required/` — instance missing one required field | `valid: false` | `errors[0].pointer` equals the exact JSON pointer to the missing field. "An error occurred" is not a pass | Add the field. Must return `valid: true` and the test must fail |
| `T-CSK-02-N1` | must-not-fire | `fixtures/csk-02/valid-instance/` | `valid: true` | `sha256(returned_instance) == sha256(input_instance)` — the **no-mutation guarantee**. No coercion, no default-filling, no trimming, no key reordering | Enable a coercion or default-fill option in the wrapper. Hashes diverge and the test must fail |
| `T-CSK-02-P1a` | **must-not-pass** | Extra undeclared field, `additionalProperties: false` | `valid: false` | Tested **alone**, not combined with P1b/P1c. A composite instance hides which constraint fired | Remove that one field. Must return `valid: true`; test fails |
| `T-CSK-02-P1b` | **must-not-pass** | Wrong-typed field | `valid: false` | As above, alone | Correct the type; test fails |
| `T-CSK-02-P1c` | **must-not-pass** | `null` in a non-nullable field | `valid: false` | As above, alone | Supply a valid value; test fails |
| `T-CSK-02-P2` | **must-not-pass** | Unknown `schema_id` | **Hard fail** — non-zero exit, no `valid` field emitted at all | Not `valid: true` (obviously) and **not `valid: false` either** — a boolean verdict asserts that validation happened, and it did not | Use a known `schema_id`. A normal verdict returns; test fails |
| `T-CSK-02-P3` | **must-not-pass** | `schema_version: "latest"` with two schema files claiming latest | **Hard fail**; `schema_version_used` absent | No version is silently chosen. Guessing a version silently changes a contract | Remove the duplicate so `"latest"` resolves to one concrete semver; test fails |
| `T-CSK-02-P4` | **must-not-pass** | Malformed schema file, valid instance | Hard fail naming the **schema** | The error names the schema, not the instance. Blaming the instance sends the next engineer to the wrong file | Repair the schema; test fails |

---

## 6. `CSK-03` … `CSK-07`

### 6.1 `CSK-03` — `untrusted-envelope`

First runnable: **Phase 08**. Supply-constrained to `WebFetch`/`WebSearch`
transport only; the inbound-message path is `BLOCKED`
(`CUSTOM_SKILL_BACKLOG.md` §3.4).

| Test | Class | Fixture / input | Expected | Load-bearing assertion | Red mutation |
|---|---|---|---|---|---|
| `T-CSK-03-F1` | must-fire | Any external retrieval | Envelope with `source_uri`, `retrieved_at`, `content_sha256` all present | `content_sha256` recomputed **independently by the test** over the raw bytes and compared — not read back from the envelope it is meant to verify | Truncate `raw_bytes` after hashing. Hashes diverge; test fails |
| `T-CSK-03-F2` | must-fire | Transport returns 503 | An envelope exists, carrying `transport_status`, with an empty payload | An envelope record exists **at all**. A silently missing source is indistinguishable from a source that said nothing | Make the transport succeed. Payload non-empty; test fails |
| `T-CSK-03-N1` | must-not-fire | Reading a file authored inside this project | No envelope constructed | Envelope count unchanged. Project files are not external content | Point the same call at an `http://` URI. Envelope created; test fails |
| `T-CSK-03-P1` | **must-not-pass — the Phase 23 injection fixture** | `fixtures/csk-03/injection-imperative/` — payload containing text directed at an agent (an instruction to disregard prior directives and publish), **authored by this project, never scraped** | Envelope `ALLOWED`; payload returned **intact**; nothing acted upon | **Three assertions, all required.** (a) `sha256(payload) == sha256(source_bytes)` — nothing was sanitized; (b) the run's action log is empty; (c) the payload text appears in **no** instruction region of any downstream prompt | Enable a sanitizer that strips imperative phrases. Hash mismatch; test fails. **This mutation is the reason the test exists:** a sanitizer would pass a naive "did it act on it?" test while destroying the evidence Phase 23 needs |
| `T-CSK-03-P2` | **must-not-pass** | A source that `research/SOURCE_POLICY.md` disallows | `REFUSED`, payload discarded | `payload` is empty **and** `refusal_reason` names the specific policy rule | Permit the source in a fixture policy. Returns `ALLOWED`; test fails |
| `T-CSK-03-P3` | **must-not-pass** | Construction attempted with `retrieved_at` absent | Hard fail; **no partial envelope persisted** | Envelope store row count unchanged. An envelope missing provenance must be unconstructable, not merely invalid | Supply the field. Constructs normally; test fails |

### 6.2 `CSK-04` — `claim-guard`

First runnable: **Phase 11** as a consumer; buildable at Phase 13 once Phase 06
creates the registers. **Today all three registers are absent, so every verdict
would be `BLOCK` — which is correct behaviour, and `T-CSK-04-P2` is the test that
proves it.**

| Test | Class | Fixture / input | Expected | Load-bearing assertion | Red mutation |
|---|---|---|---|---|---|
| `T-CSK-04-F1` | must-fire | Text asserting a capability claim absent from the register | `BLOCK` | The cited `span` selects the **exact** asserted substring. A whole-document span is not a finding | Add the claim to the fixture register. Verdict changes; test fails |
| `T-CSK-04-N1` | must-not-fire | A question and a greeting — no assertions | `PASS`, `findings == []` | `findings` is empty, not merely short | Append one unregistered assertion. `BLOCK`; test fails |
| `T-CSK-04-P1` | **must-not-pass** | A price stated in text, **and present in the register as an approved claim** | `REQUIRES_APPROVAL` — hands off to `CSK-05`. **Never `PASS`** | `verdict != "PASS"` **despite the register match**. Pricing is independently gated (`D-011`); a register hit does not discharge a gate (`D-020`) | Remove the price from the text. `PASS` returns; test fails. Same for a discount and a testimonial |
| `T-CSK-04-P2` | **must-not-pass** | The `T-CSK-04-N1` fixture — unchanged — run against an **empty** `APPROVED_CLAIMS.md` | `BLOCK` | **The same input returns the opposite verdict, driven only by register state.** An empty register means nothing is approved, not that everything is | Populate the register. `N1`'s `PASS` returns; test fails |
| `T-CSK-04-P3` | **must-not-pass** | Non-trivial text, with the LLM extraction layer stubbed to return **zero** assertions | `REQUIRES_APPROVAL` | Not `PASS`. **This is the test that catches the guard silently becoming a no-op** — the most dangerous single failure in this document, because a silent extractor produces a clean-looking `PASS` on everything | Restore the extractor. Registered text returns `PASS`; test fails |
| `T-CSK-04-P4` | **must-not-pass** | Unparseable register file | `BLOCK` | Not `REQUIRES_APPROVAL` and certainly not `PASS`. An unreadable control is a failed control | Repair the register; test fails |

### 6.3 `CSK-05` — `gate-router`

First runnable: **Phase 15**; its rules come from Phase 03.

| Test | Class | Fixture / input | Expected | Load-bearing assertion | Red mutation |
|---|---|---|---|---|---|
| `T-CSK-05-F1` | must-fire | A proposed post containing a testimonial | `REQUIRES_APPROVAL`; `categories` contains `testimonials`; approval record created | The record's state is in the set of states **only a human transition can leave**. "A record exists" is not enough — a record in an auto-advancing state is a bypass | Remove the testimonial. `CLEAR`, no record; test fails |
| `T-CSK-05-N1` | must-not-fire | Writing an internal repository file | `CLEAR`; no record created | Approval-store row count unchanged. Internal writes are not outward actions | Change `action_type` to `publish`. Record created; test fails |
| `T-CSK-05-P1` | **must-not-pass** | An `action_type` matching no category mapping | `REQUIRES_APPROVAL` | Not `CLEAR`. **Ambiguity classifies *into* the gate.** An LLM deciding an action *isn't* gated has auto-satisfied the gate — precisely what `D-020` forbids | Map that `action_type` to a known non-gated category. `CLEAR`; test fails |
| `T-CSK-05-P2a/b/c` | **must-not-pass** | Approval record that is (a) content-hash-mismatched, (b) expired, (c) revoked — **three separate tests** | Never `CLEAR` | Each attribute is tested alone, so a single composite validity flag cannot mask two of three | Per sub-case, correct that one attribute. `CLEAR` returns; that sub-test fails |
| `T-CSK-05-P3` | **must-not-pass** | Capability at ladder stage `DISABLED` | `PROHIBITED`, with the stage named in `rationale` | `rationale` contains the stage token. `D-010` forbids skipping a stage; the refusal must say which stage blocked it | Raise the stage to `APPROVAL_REQUIRED`. No longer `PROHIBITED`; test fails |
| `T-CSK-05-P4` | **must-not-pass** | An approval record with a **delivered notification** recorded and no human transition | Still `REQUIRES_APPROVAL` | The verdict is **unchanged** by notification-delivery state. `CAPABILITY_REGISTRY.md` `C-024` carries this warning in the registry itself: *a notification is not an approval* | Add a human transition. `CLEAR`; test fails |
| `T-CSK-05-P5` | **must-not-pass** | An approval record aged past any configured timeout, no response | Still not `CLEAR` | **Silence is never consent** (`CLAUDE.md` §7). A timeout must not be a decision | Record human approval. `CLEAR`; test fails |
| `T-CSK-05-P6a/b` | **must-not-pass** | (a) policy files unreadable; (b) approval store unwritable | `PROHIBITED` in both | Phase 15: *"Failure defaults to blocked."* Neither degrades to `CLEAR` or to a warning | Restore readability / writability per sub-case; that sub-test fails |

### 6.4 `CSK-06` — `dry-run-publisher`

First runnable: **Phase 16**, dry-run branch only. **The live branch is `BLOCKED`
— no `PERMITTED` outbound write path exists in 141 registry rows and
authentication state is `UNRESOLVED` for every connected server**
(`CUSTOM_SKILL_BACKLOG.md` §3.5). Every test below is a dry-run or abort test.
None sends anything, and none may be run against a real provider.

| Test | Class | Fixture / input | Expected | Load-bearing assertion | Red mutation |
|---|---|---|---|---|---|
| `T-CSK-06-F1` | must-fire | `dry_run: true`, complete payload | Rendered request returned | **A network-level assertion that no socket was opened** — observed at the transport layer, not the adapter's own self-report that it did not send | Replace the renderer with a real client pointed at a **loopback sink**. A socket is observed; test fails. Never mutate this test toward a real provider |
| `T-CSK-06-N1` | must-not-fire | Payload with no approval record | Aborts **before any transport code path is entered** | The transport module was never entered — asserted by instrumentation, not by the absence of a send. "It did not send" and "it never got there" are different guarantees | Supply a matching approval record. Transport entered; test fails |
| `T-CSK-06-P1a` | **must-not-pass** | `dry_run` not explicitly `false`; other three preconditions satisfied | Abort, naming precondition 1 | **Exactly one precondition removed.** This structure is the only one that proves the four are checked independently rather than behind one composite flag | Restore precondition 1. The call reaches the gate's exit; test fails |
| `T-CSK-06-P1b` | **must-not-pass** | No approval record whose content hash equals the payload's; other three satisfied | Abort, naming precondition 2 | As above | As above, for precondition 2 |
| `T-CSK-06-P1c` | **must-not-pass** | Ladder stage below `APPROVAL_REQUIRED`; other three satisfied | Abort, naming precondition 3 | As above | As above, for precondition 3 |
| `T-CSK-06-P1d` | **must-not-pass** | Idempotency key with a prior successful send; other three satisfied | Abort, naming precondition 4 | As above | As above, for precondition 4 |
| `T-CSK-06-P2` | **must-not-pass** | The same idempotency key called twice | Exactly **one** send | Send count `== 1`, **and** the second call returns the first call's `provider_response_id` rather than a fresh one | Vary the key between calls. Two sends; test fails |
| `T-CSK-06-P3` | **must-not-pass** | Transport returns an **unknown** outcome (timeout) | Query by idempotency key first; if the fixture platform declares no such query, **halt and escalate** | **Zero additional send attempts.** Distinguishing an unknown outcome from a definite failure is the entire point — "it probably failed" is how a duplicate is published | Change the fixture to a definite `500`. Bounded retry occurs; test fails |
| `T-CSK-06-P4` | **must-not-pass** | Payload containing a token-shaped value — a **syntactically invalid placeholder**, never a realistic value (`CLAUDE.md` §6) | `would_send` shows it redacted; `redactions` names the field | The raw value appears **nowhere** in the output, the log, or the error path | Disable redaction. The value appears; test fails |

### 6.5 `CSK-07` — `cycle-runner`

First runnable: **Phase 19**, manual / `SIMULATION` only. **The unattended trigger
and both delivery channels are `BLOCKED`** — all nine schedulers in the inventory
are `PROHIBITED` and both of Phase 19's delivery channels are `PROHIBITED` or
`Q-004`-blocked (`CUSTOM_SKILL_BACKLOG.md` §3.6). Every test below runs under
manual invocation with an injected clock.

| Test | Class | Fixture / input | Expected | Load-bearing assertion | Red mutation |
|---|---|---|---|---|---|
| `T-CSK-07-F1` | must-fire | Injected clock at the scheduled instant, `timezone: "America/New_York"` | Exactly one run starts | Run-record count for `(cycle_id, period)` `== 1` | Inject a clock one second earlier. Zero runs; test fails |
| `T-CSK-07-N1` | must-not-fire | Same instant, lock already held | No second run, **and no alert** | Run count still 1 **and** alert count `== 0`, asserted separately. A held lock is normal operation; alerting on it is alert spam (Phase 19: *"No alert spam"*) | Release the lock. Second run; test fails |
| `T-CSK-07-P1` | **must-not-pass** | DST spring-forward: `America/New_York`, 2027-03-14, where local 02:00 does not exist | Exactly one cycle — neither skipped nor doubled | Run count `== 1` across the transition window, **and** the run's local wall-clock start matches the configured local time | Reimplement the schedule as "every 168 hours from an epoch" instead of wall-clock. The run lands an hour off local time after the transition; test fails |
| `T-CSK-07-P2` | **must-not-pass** | DST fall-back: 2027-11-07, where local 01:00–02:00 occurs twice | Exactly one cycle | Run count `== 1`. The duplicated local hour must not produce two runs | Key the lock on the local wall-clock string instead of the absolute instant. Two runs (or one wrongly suppressed); test fails |
| `T-CSK-07-P3` | **must-not-pass** | A run record with steps 1–3 `OK` and step 4 absent (crash mid-run) | Resume executes step 4 first | Steps 1–3 are **not re-executed** — asserted by side-effect counters, not by reading log text | Clear the recorded steps. Full re-execution from the top; test fails |
| `T-CSK-07-P4` | **must-not-pass** | Document delivery succeeds; email delivery fails. **Both channels stubbed — neither is permitted in supply today** | Only the email channel is retried | Document-delivery attempt count `== 1`. Phase 19 requires the channels to be **independently** retryable, so a failed email must not re-send the document | Make both channels fail. Both retried; test fails — proving the counter distinguishes channels rather than counting deliveries in aggregate |
| `T-CSK-07-P5` | **must-not-pass** | Cycle checklist containing a step that would publish | Enqueued through `CSK-05`; run marked partial; nothing sent | `CSK-06` send count `== 0`. The runner must never perform a gated action itself | Remove the `CSK-05` hand-off. A send is attempted; test fails |

---

## 7. Posture tests — the project's own capability state

**These do not test the seven components.** They test claims this project makes
about itself, three of which are Phase 02 pass conditions. They are the only tests
in this document that are runnable in a documentation phase, and they are how a
future phase re-verifies what Phase 02 asserted.

`F-00-04` applies: these are the mechanically verifiable checks a documentation
phase can honestly run — ID resolution, cross-reference integrity, vocabulary
conformance, arithmetic. `F-01-04` applies just as hard: **every one carries a red
mutation, because these checkers are the exact species of instrument that was
wrong three times in Phase 01.**

| Test | Claim under test | Instrument | Load-bearing assertion | Red mutation | Earliest phase |
|---|---|---|---|---|---|
| `T-POS-01` | Pass condition **"No unverified skill enabled"** | The phase's **own** tool-call record and handoffs, plus the harness's disclosed skill list | Three assertions: (a) no `Skill(` invocation appears in the phase record; (b) no project-authored skill file exists anywhere under the project root; (c) the disclosed skill set is a subset of `Ev §5` — any addition is drift, routed to `T-POS-06` | Seed a scratch copy of the record with a synthetic `Skill(find-skills)` line. The check must flag it | 02 |
| `T-POS-02` | The registry's claim that **no capability was invoked** to produce it | Same record | No `ToolSearch` call and no `mcp__*` call appears in the phase record | Seed a synthetic `ToolSearch(select:WebFetch)` line. Must flag | 02 |
| `T-POS-03` | Registry **vocabulary conformance** (`CLAUDE.md` §5, Rule 1) | Column-token check over all 141 rows | Every `Ladder` ∈ the six `D-010` stages plus the `NOT_PRODUCTION_FACING` sentinel; `Class` ∈ four tokens; `Relevance` ∈ three; `Disposition` ∈ four. **Exactly one bare token per cell** — no parentheticals, no qualifiers | Insert `PERMITTED (conditional)` into a scratch copy. Must flag | 02 |
| `T-POS-04` | Registry **arithmetic** — §G counts vs. actual rows | Row count per column value, four ways | All four totals reconcile to 141. The registry's own rule applies: *if a count and a table disagree, the table is authoritative* | Change one §G count by 1 in a scratch copy. Must flag | 02 |
| `T-POS-05` | Registry **ID resolution and citation integrity** | Reference resolver | Every `C-nnn` unique **and** contiguous 001–141 — contiguity and count are two different assertions and a coincidence between them is not a proof. Every `Basis` token resolves to a real `D-`/`Q-`/`R-`/`F-`/`NG-` row, a real `docs/PROJECT_BOUNDARIES.md` section, or a real `CLAUDE.md` section | **Two mutations, both required.** Insert `D-999` — must flag. Insert `BOUNDARIES §99` — must also flag, proving the section resolver works and not only the `D-` resolver | 02 |
| `T-POS-06` | **Registry drift** — see §7.1 | Operator re-capture + diff | Any difference in `Ev §1`–`§5` between captures. Every registry row touching a changed namespace becomes `UNVERIFIED` until re-classified | Diff the Phase 02 capture against a scratch copy with one server removed and one skill added. Must report **exactly those two** differences; reporting none means the diff is reading the wrong sections | Every phase gate |
| `T-POS-07` | Nothing is **scheduled** against this project | `C-018` (`CronList`) and `C-050` (`list_scheduled_tasks`) — both `RESTRICTED` read-only, with the registry naming this exact use as the one legitimate one | No entry references this project root. **Unrelated entries are not transcribed into this repository** (`D-008`, and the registry's own condition) | Seed a scratch fixture list containing an entry that names this project root. Must flag | **03 — not 02.** See §7.2 |
| `T-POS-08` | Pass condition **"Risky or irrelevant skills excluded"** | Set comparison | `SKILL_INSTALLATION_PLAN.md` names no capability drawn from `filter Disposition == PROHIBITED` (86 rows) or `filter Relevance == IRRELEVANT` (69 rows). The two lists overlap heavily and are **not** the same list — the registry names 22 rows that are prohibited today *and* plausibly relevant later | Add one `PROHIBITED` row's name to a scratch copy of the plan. Must flag | 02, once that plan exists |
| `T-POS-09` | **This backlog's own honesty** — no `CSK` entry depends on a `PROHIBITED` capability without recording `BLOCKED` | Cross-check of `CUSTOM_SKILL_BACKLOG.md` §3.1 against registry dispositions | Every "do not build / blocked" claim resolves to a real registry row with the disposition stated | Edit a scratch copy so `CSK-06` claims its live branch is buildable. Must flag | 02 |

### 7.1 The registry is a dated snapshot, and nothing detects when it goes stale

`CAPABILITY_REGISTRY.md`'s own header says it: the registry *"goes stale the
moment the operator installs, removes, authorizes, or de-authorizes a plugin,
connector, or skill — and nothing in this project will detect that."* One
interactive authorization by the operator activates a server and no file in this
repository would record it (registry §D).

**`T-POS-06` is the re-verification test, and it has three honest limits:**

1. **It is operator-assisted, not automated.** `Ev §8` records that the inventory came from session disclosure, not from a command, and that **no command reproduces it**. A future phase owner must re-capture the disclosure into `agent_runs/phase-XX/evidence/SESSION_CAPABILITY_INVENTORY.md` before the diff can run.
2. **Its cadence is the phase gate.** It detects nothing between gates. A connector authorized on Tuesday and used on Wednesday is caught on Friday, if at all.
3. **A clean diff proves the *disclosure* is unchanged, not that the underlying accounts are.** Authentication state was never probed and remains `UNRESOLVED` in both directions (`Ev §0` Limit 3). A server can gain authorization with no change to its disclosed tool list.

**Prescribed handling when drift is detected:** mark the affected rows
`UNVERIFIED`, do not silently re-classify them, and record the drift in
`findings.md`. Drift toward *more* capability is the case that matters — a new
connector arrives already able to act, and `C-007` (`ToolSearch`) puts it one call
from use with no approval step in between.

### 7.2 The test that cannot run in the phase that needs it

`T-POS-07` proves nothing is scheduled against this project. Running it means
invoking `C-018` or `C-050`. **Phase 02's pass condition is that no capability was
invoked.** The test therefore cannot run in Phase 02 without falsifying the
condition it sits beside.

This is stated openly rather than resolved quietly. Earliest run: **Phase 03**,
recorded with the command and its actual output. Until then, the claim "nothing is
scheduled against this project" is `UNRESOLVED`, not verified.

---

## 8. What cannot be tested yet, and why

Stated so that no later phase mistakes an untested area for a clean one, and so no
gate report counts an absent test as a passed one.

| Not testable | Why | When it becomes testable |
|---|---|---|
| Six of the seven components | They do not exist. Phase 02 specifies; later phases build | Per component, at its owning phase (§4–§6 headers) |
| **Anything with a fixture** | No fixture directory has a home. Phase 04's pass condition already grades against fixtures with nowhere to live | When `HANDOFF OQ-2` / `OQ-P2-3` is answered — **before Phase 04, not during it** |
| `CSK-02` **at all** | With `C-003`'s *"No installs"* condition, there is no permitted path to a validation library, so there is no validator to test | When `OQ-P2-1` is answered |
| A **successful live send** (`CSK-06`) | No `PERMITTED` outbound write path exists; authentication state is `UNRESOLVED` for every connected server; `SECURITY_POLICY.md` does not exist (`D-027`) so no credential may enter the project | Not on the current evidence. *"No socket opened"* is testable today; *"the socket opened correctly"* is not |
| **Unattended** scheduling (`CSK-07`) | All nine schedulers in the inventory are `PROHIBITED`; Google Cloud is `NOT CONNECTED`, unowned, and its SDK is not installed (`F-01-02`) | When `HANDOFF OQ-1` is answered — and **not** by reaching for one of the nine |
| **Real** delivery (`CSK-07`) | Email is `PROHIBITED` on every path and `OQ-3` is unresolved; Drive is `Q-004`-`BLOCKED`. Both of Phase 19's channels | When `OQ-3` and `Q-004` are answered. Until then `T-CSK-07-P4` is a stub-only test and must be reported as such |
| **End-to-end** prompt-injection resistance | `T-CSK-03-P1` tests the envelope in isolation. Whether the whole pipeline resists injection is a system property | Phase 23 |
| **Authentication state** of any connector | Determining it requires invoking the connector, which `BOUNDARIES` §3 and §8 prohibit. It must stay `UNRESOLVED` in **both** directions — "not listed as requiring auth" is not "authenticated" | Only by an owner action recorded in `CONNECTOR_ACTIVATION_PLAN.md`. Never by an agent probing |
| Whether any **third-party** capability behaves as its description claims | Nothing was invoked. Registry §J: a skill description is a marketing artifact written outside this project | Not a target of this plan. If a capability is ever activated, its behaviour is tested then, under `SKILL_SECURITY_POLICY.md` |
| Whether the inventory is **complete** | It was not cross-checked against on-disk configuration; that would require reading outside the project root, which `BOUNDARIES` §1 does not grant | Only by an owner-side check, outside this project's boundary |

---

## 9. The clock seam — a testability decision that expires

`CSK-07`'s DST tests (`T-CSK-07-P1`, `P2`) and its exactly-one-run tests
(`F1`, `N1`) are all statements about **specific instants**. A component that
reads the system clock cannot be pointed at 2027-03-14T02:00 America/New_York, so
those tests cannot be written honestly — they can only be written to pass on
whatever instant the suite happens to run at.

**Therefore `clock` is a typed input on `CSK-07` and reading the system clock
directly is in its negative contract** (`CUSTOM_SKILL_BACKLOG.md` §5).
`CSK-01` takes the same input at negligible cost, because its reports carry
timestamps that end up in gate evidence.

**Why this is decided now rather than at Phase 19.** Retrofitting a clock seam
means changing every call site and re-establishing the provenance of every stored
timestamp. Deciding it costs one field today. Phase 19's pass condition
*"America/New_York schedule configurable"* is the one that becomes unverifiable
without it — and an unverifiable pass condition is the shape of a weakened test,
which every phase prompt forbids (*"Do not weaken tests to obtain a pass"*).

---

## 10. Who runs what, and when

| Phase | Tests it must run | Notes |
|---|---|---|
| **02** | `T-POS-01` … `T-POS-05`, `T-POS-09`; `T-POS-08` once `SKILL_INSTALLATION_PLAN.md` exists | The only tests runnable in this phase. `T-POS-07` explicitly excluded — §7.2 |
| **03** | `T-CSK-01-*`; `T-POS-07`; re-run `T-POS-03` … `T-POS-06` | First phase that may invoke a read-only capability with the command and output recorded |
| **04** | `T-CSK-02-*`, gated on `OQ-P2-1`; re-run posture set | First executable artifact in the plan |
| **08** | `T-CSK-03-*` except the inbound path | Inbound envelope `BLOCKED` |
| **11 / 13** | `T-CSK-04-*` | Registers must exist first (Phase 06) |
| **15** | `T-CSK-05-*` | Policies must exist first (Phase 03) |
| **16** | `T-CSK-06-*`, dry-run and abort tests only | Live branch `BLOCKED` |
| **19** | `T-CSK-07-*` under manual invocation with injected clock | Trigger and delivery `BLOCKED` |
| **23** | The full suite as regression, plus end-to-end injection and approval-bypass tests | `T-CSK-03-P1` and `T-CSK-05-P*` are its inputs |
| **Every gate** | `T-POS-06` (drift) | Operator-assisted; §7.1 |

**Standing rule for every row above:** a green result is reported as `UNVERIFIED`
until that test's red mutation has been run and its failure recorded. `F-01-04`.
