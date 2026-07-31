# Skill Installation Plan

**Owner of this file:** Phase 02 Owner (Atlas Orchestrator), run `phase-02-2026-07-29-a`.
**Date:** 2026-07-29.
**Companion documents:** `CAPABILITY_REGISTRY.md` (what exists), `CONNECTOR_ACTIVATION_PLAN.md` (what would have to be true before a connector is authorized), `SKILL_SECURITY_POLICY.md` (the rules), `CUSTOM_SKILL_BACKLOG.md` (what would be built), `SKILL_TEST_PLAN.md` (how any of it is verified).

---

## 1. The decision, stated first

**Phase 02 installs nothing, enables nothing, authenticates nothing, and upgrades nothing.**

Recorded as `D-036` (`APPROVED_IMPL`). Reversal cost: zero — this plan changes no machine state, so there is nothing to undo. Reversing the decision means executing one of the specifications in §4 when a phase actually needs it.

The phase objective permits installing: *"Inspect, classify, install, **or specify** the smallest safe skill and connector set required for later phases."* This plan reads that disjunction deliberately rather than treating "install" as an instruction.

**Why specify rather than install — four reasons, in descending order of weight:**

1. **Nothing between Phase 03 and Phase 15 needs a capability that is not already present.** The demand model derived independently from every phase prompt 03–24 (`agent_runs/phase-02/handoffs/HANDOFF_AGENT_ARCHITECTURE_SPECIALIST.md` §3) puts Phase 03's requirement at "local script execution and Markdown authoring" — in use since Phase 01. The first genuinely new requirement arrives at **Phase 04**, and it is small (§4.4).
2. **"No unverified skill enabled" is this phase's first pass condition.** Nothing here has been verified by use, because verifying by use is itself the prohibited act for every capability that touches an external system (`docs/PROJECT_BOUNDARIES.md` §8 step 4). An install performed now would be an unverified capability added to the machine on this phase's authority.
3. **Installing implies decisions the owner has not made.** Installing `gcloud` would imply Google Cloud is the scheduled-automation host — but **no phase owns Google Cloud** (`findings.md` `F-01-02`, reconfirmed independently in this phase), and choosing a host is the owner's call, not an install side effect.
4. **The maturity ladder starts at `DISABLED` and forbids skipping stages** (`D-010`). Adding a capability to the machine ahead of the phase that would take it through `SIMULATION` inverts that order.

**What this decision is not.** It is not a judgement that the current capability set is adequate, safe, or well-chosen. §5 records the opposite. It is a judgement that *adding* to it is not this phase's job.

---

## 2. What "smallest safe set" resolves to today

| Question | Answer |
|---|---|
| Smallest set of capabilities needed to run Phase 03 | The ones already in use since Phase 01: file read/write, search, local shell, `git`. No connector, no credential, no network beyond `git push`/`pull` to the private remote |
| Capabilities to add in Phase 02 | **None** |
| Capabilities to authorize in Phase 02 | **None.** Authorization is a separate act with its own gate — see `CONNECTOR_ACTIVATION_PLAN.md` |
| Capabilities to remove in Phase 02 | **None** — see §5. Removal is an owner action on machine-local state, and this project does not own that state |
| Capabilities recorded as prohibited | 86 of 141 registry rows, each citing the rule that prohibits it |

The smallest safe set is the set already in use. That is a real finding, not an evasion: a documentation-and-policy phase followed by a policy phase does not need new tooling, and the honest answer to "what should we install" is sometimes "nothing yet."

---

## 3. Installation is not the same act as authorization

These are routinely conflated and this project must not conflate them, because they have different gates and different reversal costs.

| Act | What changes | Gate | Reversal |
|---|---|---|---|
| **Install** a tool or plugin | Machine-local state outside this repository | Owner action; nothing in this repo is authoritative over it | Uninstall; usually clean |
| **Authorize** a connector | A live grant to a third-party account, off this machine | Owner personally — an account-level human checkpoint (`user-guide/USER_INSTRUCTIONS.md`) | Revoke at the provider. **Data already sent is not recalled** |
| **Use** an installed, authorized capability | Real-world effect | Every rule in `SKILL_SECURITY_POLICY.md` and the nine gates (`D-011`) | Depends entirely on the effect. Often none |

An installed-but-unauthorized connector is inert. An authorized one is live from that moment, and **nothing in this repository would record that it happened** unless a `DECISIONS.md` row is written first. That ordering requirement lives in `CONNECTOR_ACTIVATION_PLAN.md` and it is the single most important procedural control this phase produces.

---

## 4. Specifications — what would be installed, by whom, when, and how to undo it

Each entry states the triggering phase, the preconditions, the steps, and the rollback. **None of these is authorized now.** Executing any of them is a decision for the phase that needs it, or for the owner.

### 4.1 `gcloud` — Google Cloud SDK · status `NOT INSTALLED` · **do not install**

- **Verified absent** 2026-07-28 (`README.md` § "Verified environment"; `gcloud --version` → not recognized).
- **Which phase would need it:** Phase 05 (Drive control center) and Phase 19 (scheduled automation).
- **Blocked by, and this is the point:** `Q-004` is the project's only `BLOCKED` item and gates Phase 05. Separately, **no phase in the 25-phase plan owns Google Cloud at all** (`F-01-02`; independently reconfirmed this phase — the string "Google Cloud" appears zero times across all 25 files in `phase-prompts/`). Installing the SDK would quietly answer a question the owner has not been asked.
- **Preconditions before install:** `Q-004` answered; an owner decision recording which phase owns the execution host; `SECURITY_POLICY.md` exists (`D-027`) because any real use needs a credential; and — because any hosted scheduler is metered — a **separate** owner spending approval, since spending is one of the nine gated categories (`D-011`) and no spend is authorized (`D-016`, `NG-001`).
- **Steps:** owner-performed, from Google's official installer for Windows. The exact command is deliberately not written here: this project has not chosen Google Cloud, and writing an install command would imply it had. Confirm the current official procedure at install time (`R-18` — tooling changes between selection and use).
- **Rollback:** uninstall via Windows "Apps & features"; delete the SDK directory and any `.gcloud/` config. `.gitignore` already excludes `.gcloud/` and `gha-creds-*.json`, so no credential could have entered the repository in the interim.

### 4.2 `pwsh` — PowerShell 7 · status `NOT INSTALLED` · **do not install**

- **Verified absent** 2026-07-28. Only Windows PowerShell **5.1.26100.8894** is present.
- **Real consequence:** 5.1 rejects `&&`, `||`, ternaries, and null-coalescing (`findings.md` `F-01-03`). Every script written for this machine must use 5.1-compatible syntax or fail at the prompt.
- **Why not install:** nothing requires it. The constraint is already documented in `README.md` and `CLAUDE.md`, and a documented constraint that is being honoured is not a problem to solve. Installing a second shell adds a way for scripts to work on one operator's machine and fail on another's — the opposite of the portability the rubric asks for.
- **If a later phase installs it anyway:** that phase must re-verify that every existing script still runs under **both** shells, because `pwsh` being present does not make 5.1 disappear.
- **Rollback:** uninstall; no project file references `pwsh`.

### 4.3 `docker` · status `NOT INSTALLED` · **excluded, not deferred**

No phase in the plan depends on containerization. Recorded so a later phase does not treat its absence as an oversight. If a phase ever proposes it, that is a new decision requiring its own rationale.

### 4.4 A JSON Schema validation library — **the first genuine install this project will need**

This is the one entry a future phase owner should actually read.

- **Which phase:** **04** — Data Contracts and State Model.
- **Why it is real:** Phase 04's pass condition *"Schemas validate fixtures"* is, per the demand analysis, **the first pass condition in the entire plan that prose cannot satisfy.** A validator must actually run, against fixtures that must actually exist. Everything before Phase 04 is documentation; `CLAUDE.md` §6 forbids claiming a test ran that did not.
- **What is already present:** Python **3.14.6**, pip **26.1.2**, Node **v24.18.0**, npm **11.16.0** — all verified 2026-07-28. The runtime exists; only a library is missing.
- **What is not decided, and must not be decided here:** which library, which language, and where fixtures live. That last one is a live gap — Phase 04's deliverable list names no home for fixtures, and `MASTER_PLAN.md` places the first `tests/` directory at Phase 13. **The artifact Phase 04 is graded against has nowhere to live.** Recorded as `Q-016`; it is cheap to close before Phase 04 starts and awkward to close during it.
- **Preconditions:** none beyond Phase 03's gate. This install needs **no credential, no network account, no spend approval, and no connector** — it is a local development dependency. It is therefore the lowest-risk install in the plan and should not be confused with the connector activations in §4.1.
- **Rollback:** uninstall the package; delete the virtual environment. `.gitignore` already excludes `.venv/`, `venv/`, `node_modules/`, and `__pycache__/`.

### 4.5 New skills, plugins, or MCP servers — **none, and one standing rule**

No new skill or plugin is proposed. The observed surface already contains roughly 150 skills and 35 MCP servers, of which the registry marks **69 `IRRELEVANT`** to a marketing-operations project. The problem this project has is not too few capabilities.

**Standing rule for every later phase:** installing a plugin or skill adds third-party text that is loaded into the agent's own context on every run. `SESSION_CAPABILITY_INVENTORY.md` §7 records a live example of a third-party skill description asserting a global override of the agent's tool selection. Adding a plugin is therefore not a neutral convenience — it is a change to the instruction surface, and it belongs under `SKILL_SECURITY_POLICY.md`, not under an operator's convenience.

### 4.6 Custom skills — specified, not built

Seven are specified with full contracts in `CUSTOM_SKILL_BACKLOG.md`, each owned by a later phase. **Phase 02 builds none of them.** The earliest, `blast-radius-check`, belongs to Phase 03.

---

## 5. What this plan deliberately does not do: remove anything

The registry marks 86 rows `PROHIBITED` and 69 `IRRELEVANT`. A natural next thought is "uninstall the irrelevant ones." This plan does not recommend that, for three reasons — and it is worth being explicit, because the omission would otherwise look like an oversight.

1. **This project does not own that state.** Plugins and connectors are machine-local and user-profile-scoped, outside the project root, which `docs/PROJECT_BOUNDARIES.md` §1 places out of bounds. The operator may use these capabilities for entirely unrelated work.
2. **Prohibition is the control, not absence.** `PROHIBITED` in the registry plus the rules in `SKILL_SECURITY_POLICY.md` is what governs this project's behaviour. Uninstalling would be a stronger control, but it is the operator's call about their own machine.
3. **Removal cannot be verified from inside this boundary.** This project cannot confirm a plugin is gone without reading outside the project root. A control this project asserts but cannot check is worse than one it merely states.

**What the owner may reasonably choose to do**, entirely at their discretion, is remove plugins they do not use for anything — particularly `adspirer-ads-agent` (paid advertising, against a standing organic-only posture) and `apollo` (lead sourcing and outbound sequencing, against an unresolved data-privacy question). That would reduce exposure genuinely rather than only on paper. It is a recommendation, not a requirement, and it is recorded in `CONNECTOR_ACTIVATION_PLAN.md` with the rest of the owner-facing actions.

---

## 6. Rollback for this phase as a whole

**Phase 02 changed no machine state, so the machine needs no rollback.** Nothing was installed, enabled, authorized, configured, upgraded, or removed. No credential exists. No external system was contacted. No file outside the project root was written.

The phase's entire footprint is Markdown inside the repository, which makes rollback a single revert:

```bash
git revert --no-commit 564e5e3 && git commit -m "Revert Phase 02 deliverables"
```

**Revert only `564e5e3`.** Do **not** revert the whole branch range. `0ccddce` records
`D-040`, which the **owner** stated, and `f583bdd` records the **owner's gate decision**.
Those are owner artifacts, not phase work, and a range revert would silently delete both.
*(The command previously read `<phase-02-commit-range>` — an unfilled placeholder that
would not run, over a range that should not be reverted. Corrected 2026-07-29 per
Independent Reviewer finding.)*

To discard the work before it is merged, delete the branch:

```bash
git checkout main && git branch -D claude/phase-02-capability-registry-c04753
```

`git branch -D` fails on the branch you are standing on, so the checkout is required, not
optional. If the branch has been pushed, also `git push origin --delete
claude/phase-02-capability-registry-c04753`. **Note that `main` currently contains none of
Phase 02** — see the merge warning below.

**What a revert would restore, and what it would lose.** It restores a repository with no `CAPABILITY_REGISTRY.md` — the state `D-027` describes. It loses the record that the observed capability surface includes credential-free paths to external systems. That record is the phase's actual product; the file list is incidental. Anyone reverting should re-read `agent_runs/phase-02/PHASE_GATE_REPORT.md` first, since the findings survive the files.

Per-item rollback for anything a *later* phase installs on the strength of §4 is stated in that item's entry, and each is independent of the others.

---

## 7. What would make this plan wrong

Stated so the next phase owner can check it rather than inherit it.

- **If Phase 03 turns out to need a script runtime for "Policy conflicts tested."** The demand model flags this as genuinely undecided (`OQ-4`, carried into `OPEN_QUESTIONS.md`): whether that pass condition requires a parseable permission matrix plus a conflict-detection script, or is satisfied by the documentation-phase resolution in `findings.md` `F-00-04`. If the former, Phase 03 needs §4.4's runtime one phase earlier than stated here. **Python and Node are already installed**, so even then nothing new is required — only a decision.
- **If the owner resolves the Google Cloud ownership question in favour of Google Cloud**, §4.1 moves from "do not install" to a scheduled install owned by whichever phase the owner names.
- **If the capability surface changes.** This plan rests on a snapshot dated 2026-07-29 with no drift detection. A plugin added tomorrow is invisible to this repository. Re-capture `agent_runs/phase-02/evidence/SESSION_CAPABILITY_INVENTORY.md` before relying on any of this at a later gate.
