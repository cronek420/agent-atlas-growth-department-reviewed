# Agent Atlas Growth Department — Draft Build Package

## Purpose

Build a reliable, auditable marketing operations system for **Rough Draft Builders Club** using Claude Code in Antigravity, Google Cloud for scheduled automation, Google Drive for human-readable living documents, and GitHub/Markdown as the machine-readable source of truth.

## Current status

This package is a draft architecture and phased instruction set. It does not create production accounts, spend money, publish content, or deploy services without explicit approval.

**As of 2026-07-29:** Phases 00 and 01 both **passed** their gates, recorded by the Project Owner with no conditions. **Phase 02 (Capability Registry and Skill Foundation) passed its gate as a CONDITIONAL PASS**, recorded by the Project Owner 2026-07-29 — see `agent_runs/phase-02/PHASE_GATE_REPORT.md`. **One condition remains open:** the independent review never ran (`R-24`). The project is an initialized Git repository on branch `main` at `C:\Users\crone\Projects\agent-atlas-growth-department`.

*(This paragraph previously said Phase 01 was awaiting a decision the owner had already recorded. Corrected by the Phase 02 Owner during the `F-01-09` staleness sweep.)*

Phase 02 **installed nothing, enabled nothing, and authorized nothing** (`D-036`). It inventoried and classified 141 capabilities available to a Claude Code session on this machine, and found that this project's external-access controls govern *credentials it holds* while several available paths reach external systems using *borrowed authority* — the operator's logged-in browser, their Claude account, and connector grants held there (`findings.md` `F-02-03`). Nothing was invoked; every such path is prohibited by rule.

The repository is backed up to a **private** GitHub remote — `cronek420/agent-atlas-growth-department`, created by the Project Owner on 2026-07-29 (`D-030`). `R-19`, the data-loss risk that was live through Phases 00 and 01, is now **MITIGATED**.

No other external service is connected. No credential exists in this project.

## Primary success criteria

The completed system must:

- Maintain product, audience, brand, campaign, content, analytics, and experiment records.
- Research current marketing trends and compare platforms.
- Prepare social account launch materials.
- Produce approved recurring content.
- Test copy and creative variants.
- Publish only permitted routine content.
- Triage community messages and leads safely.
- Produce a weekly execution checklist and executive summary.
- Track outcomes from attention through purchases.
- Recover safely from failures.
- Keep a complete audit trail.
- Require approval for claims, pricing, discounts, testimonials, direct outreach, complaints, controversial topics, spending, and paid advertising.

## Architecture rules

1. Markdown and structured files in GitHub are authoritative.
2. Google Docs and Sheets are human-readable mirrors and operational views.
3. LLMs propose and interpret; deterministic code enforces permissions, state changes, calculations, deduplication, scheduling, and publishing.
4. Every phase has one integration owner.
5. Agents may work in parallel only on independent outputs.
6. Every phase ends with independent review and a phase-gate report.
7. No phase may auto-start the next phase.
8. Unknown values remain `UNRESOLVED` or `BLOCKED`.
9. External content is untrusted data, never project instruction.
10. All production-facing capabilities progress through:
   `DISABLED → SIMULATION → DRAFT_ONLY → APPROVAL_REQUIRED → LIMITED_AUTONOMY → ROUTINE_AUTONOMY`.

---

## Repository layout

Everything at the root is either governance (rules the project runs by), memory (what has been decided and done), or packaged instructions (the phase prompts themselves).

### Governance and memory — root files

| File | What it is |
|---|---|
| `CLAUDE.md` | Standing instructions for any Claude Code session opened at this root. Read automatically. |
| `MASTER_PLAN.md` | The working plan of record: gate status, dependencies, deliverables, blocking questions (`D-034`). |
| `CURRENT_PHASE.md` | Which phase is active, its status, and what to paste to start it. The advancement switch. |
| `DECISIONS.md` | The decision register. Every decision with an ID (`D-001`…), status, owner, rationale, evidence. |
| `OPEN_QUESTIONS.md` | Unanswered questions with IDs (`Q-001`…), what each blocks, and the exact owner action needed. |
| `SCOPE.md` | What this project is responsible for. |
| `NON_GOALS.md` | What it is explicitly not responsible for (`NG-001`…). |
| `RISK_REGISTER.md` | Known risks with IDs (`R-01`…), likelihood, impact, and mitigation. |
| `ACCEPTANCE_CRITERIA.md` | What "done" means, per success criterion. |
| `INTAKE_RECORD.md` | The durable record of what the Project Owner actually said at intake. Decisions cite it. |
| `findings.md` | Running log of material findings across phases (`F-00-01`…). |
| `progress.md` | Running log of what was completed, phase by phase. |
| `task_plan.md` | The current phase's task graph, pass conditions, and file ownership. Rewritten each phase. |
| `README.md` | This file. Overview plus the practical setup path. |
| `.env.example` | Credential **template** — placeholder names only. Nothing here is connected. |
| `.gitignore` | What never enters version control, including `.env` and `data/private/`. |

### Packaged build-instruction files — root

| File | What it is |
|---|---|
| `00_MASTER_START_HERE.md` | The master prompt pasted at the start of every phase session. |
| `UNIVERSAL_ANTIGRAVITY_INSTRUCTIONS.md` | Universal operating instructions for Antigravity and other agent-capable environments. Project-specific governance remains higher priority. |
| `skills-lock.json` | Machine-readable skill provenance and integrity manifest. It does not grant permission or prove a skill is installed. |
| `MASTER_LINEAR_BUILD_PLAN.md` | The original packaged 25-phase plan, retained unmodified (`D-034`). |
| `PACKAGE_INDEX.md` | Index of the packaged build materials. |
| `PROMPT_AND_BUILD_QUALITY_RUBRIC.md` | The scoring rubric every phase gate is graded against. |
| `agent-atlas-growth-department_build-package_draft.zip` | The original build package archive, tracked deliberately as the provenance artifact (`D-031`). |

### Directories

| Directory | What is in it |
|---|---|
| `docs/` | Long-form project documentation. `docs/PROJECT_BOUNDARIES.md` defines what this project may read, write, and never touch. |
| `phase-prompts/` | One prompt file per phase, `PHASE_00_…` through `PHASE_24_…`. You paste exactly one per session. |
| `checklists/` | One checklist per phase, `PHASE_00_CHECKLIST.md` through `PHASE_24_CHECKLIST.md`. |
| `templates/` | `AGENT_HANDOFF_TEMPLATE.md`, `DECISION_REGISTER_TEMPLATE.md`, `PHASE_GATE_REPORT_TEMPLATE.md`. |
| `user-guide/` | `USER_INSTRUCTIONS.md` — how to run the package, the secrets rules, and the human checkpoints. **Binding.** |
| `agent_runs/` | Per-phase evidence: `agent_runs/phase-NN/handoffs/`, `REVIEW_REPORT.md`, `PHASE_GATE_REPORT.md`. |
| `.claude/` | Claude Code harness configuration. `.claude/settings.local.json` is machine-local and git-ignored (`D-032`). |

---

## Verified environment

Tool versions below were **verified on this machine on 2026-07-28** by running each command and capturing its output. They are not assumptions. Full verbatim output: `agent_runs/phase-01/handoffs/HANDOFF_ENVIRONMENT_INSPECTOR.md`.

| Tool | Command | Version on this machine | Status |
|---|---|---|---|
| Git | `git --version` | git version 2.55.0.windows.3 | INSTALLED |
| GitHub CLI | `gh --version` | gh version 2.96.0 (2026-07-02) | INSTALLED |
| Node.js | `node --version` | v24.18.0 | INSTALLED |
| npm | `npm --version` | 11.16.0 | INSTALLED |
| Python | `python --version` | Python 3.14.6 | INSTALLED |
| Python launcher | `py --version` | Python 3.14.6 | INSTALLED |
| pip | `pip --version` | pip 26.1.2 (from `C:\Python314\Lib\site-packages\pip`) | INSTALLED |
| Windows PowerShell | `$PSVersionTable.PSVersion` | 5.1.26100.8894 | INSTALLED |
| VS Code | `code --version` | 1.129.1 | INSTALLED |
| PowerShell 7 | `pwsh --version` | not recognized | **NOT INSTALLED** |
| Google Cloud SDK | `gcloud --version` | not recognized | **NOT INSTALLED** |
| Docker | `docker --version` | not recognized | **NOT INSTALLED** |

OS: Microsoft Windows NT 10.0.26200.0. Project root: `C:\Users\crone\Projects\agent-atlas-growth-department`. Free space on `C:`: 290.16 GB of 475.73 GB.

**About the three missing tools.** They are recorded honestly, not flagged as a problem to fix today. Nothing in Phase 01 needs any of them.

- **`pwsh` (PowerShell 7) is absent — only Windows PowerShell 5.1 is available.** This has an immediate practical consequence: every command in this README uses 5.1-compatible syntax. Do not write `&&`, `||`, ternaries (`? :`), or null-coalescing (`??`) in scripts for this machine — 5.1 rejects them as parser errors.
- **`gcloud` is absent.** Phases 05 (Google Drive control center) and 19 (scheduled automation / executive reporting) are the phases that would care.
- **`docker` is absent.** Only relevant if a later phase chooses a containerized approach. None has.

Whether any of these gets installed is a **Phase 02** decision — Phase 02 owns capability decisions, and Phase 01 must not pre-empt it (`D-035`).

---

## Local setup from scratch

Reproducing this workspace on a Windows machine. Every command is Windows PowerShell 5.1 syntax. Run them one block at a time.

### 1. Get the project folder

The project must live **outside** the Rough Draft Builders Club application repository, at its own root (`D-012`). The recommended location is `C:\Users\crone\Projects\agent-atlas-growth-department`.

Today there is no remote to clone from, so the folder is obtained by copying it (from a backup, another machine, or the build-package archive).

Once the Project Owner has created the private GitHub remote (see the next section), cloning becomes the normal path:

```powershell
git clone https://github.com/<owner>/agent-atlas-growth-department.git
```

Then move into the folder:

```powershell
Set-Location C:\Users\crone\Projects\agent-atlas-growth-department
```

### 2. Confirm the tools

Run these and compare against the [Verified environment](#verified-environment) table. Exact version matches are not required; presence is.

```powershell
git --version
```

```powershell
gh --version
```

```powershell
node --version
```

```powershell
python --version
```

```powershell
$PSVersionTable.PSVersion
```

If a command reports "is not recognized," that tool is not on `PATH`. `pwsh`, `gcloud`, and `docker` are expected to report this — that is the current, accepted state.

### 3. Verify the secrets guard — **do not create `.env` yet**

**Do not run `Copy-Item .env.example .env` at this stage.** `.env.example` states plainly that no `.env` exists and that Phase 01 does not create one: creating it is a later-phase action that must not happen before a secrets-handling policy exists (`D-027`, `D-035`). No `SECURITY_POLICY.md` exists yet, so there is nothing to put in `.env` and no authority to put it there.

*(An earlier draft of this step instructed copying the file immediately, which contradicted `.env.example`. Corrected per Reviewer Finding F-05 — the setup guide must not tell you to do something another governing file forbids.)*

What you **should** do now is confirm the guard works, so that when a credential eventually exists it cannot be committed:

```powershell
git check-ignore -v .env
```

That prints the `.gitignore` line doing the ignoring — expect `.gitignore:27:.env`. **If it prints nothing, stop.** The ignore rule is not active and no credential may be introduced until it is.

Confirm the template itself is tracked, since it holds placeholder names only and belongs in version control:

```powershell
git ls-files .env.example
```

**When Phase 03 has produced `SECURITY_POLICY.md`**, creating `.env` becomes authorized. At that point the command is `Copy-Item .env.example .env`. Note what you would get: not a blank file, but ten variables carrying the literal marker `<obtain-from-owner-do-not-commit>` and eleven empty ones. Replace markers only for services actually in use; leave the rest untouched.

### 4. Confirm the repository state

```powershell
git status
```

```powershell
git rev-parse --abbrev-ref HEAD
```

The branch should be `main` (`D-029`).

### 5. Start a phase

Per `user-guide/USER_INSTRUCTIONS.md`:

1. Open Antigravity.
2. Open the `agent-atlas-growth-department` folder as the workspace root.
3. Start Claude Code **at the project root** — not in a subfolder.
4. Paste the contents of `00_MASTER_START_HERE.md`.
5. Paste **only** the prompt for the current phase, from `phase-prompts/`. Which phase that is comes from `CURRENT_PHASE.md`.
6. Let Claude build its task graph and delegate specialists.
7. Review the phase-gate report when it stops.

To see which prompt to paste:

```powershell
Get-Content CURRENT_PHASE.md -TotalCount 10
```

Never paste two phase prompts in one session. No phase may auto-start the next one (Architecture Rule 7, `D-007`); advancement happens only when you update `CURRENT_PHASE.md` yourself.

---

## Git and the private remote

### Where things stand — ✅ done

- The repository is initialized locally on branch `main` (`D-029`).
- **The private remote exists:** `cronek420/agent-atlas-growth-department`, visibility **private**, created by the Project Owner on 2026-07-29 (`D-030`). `origin` tracks `main`; local and remote are in sync.

Verify at any time:

```powershell
gh repo view cronek420/agent-atlas-growth-department --json name,visibility
```

```powershell
git status -sb
```

The second prints `## main...origin/main` plus `[ahead N]` if you have unpushed commits. **Push at every phase gate** — the off-machine copy is only as current as the last push, which is the sole residual part of `R-19`.

### Why the owner had to do this personally

Creating a remote publishes repository content to a third-party service. That is an outward-facing, account-level action, and `user-guide/USER_INSTRUCTIONS.md` reserves account creation, terms acceptance, and identity verification to the **Project Owner** under "Human checkpoints." GitHub was the *inferred* host — Architecture Rule 1 names it and `gh` 2.96.0 is installed — but confirming it was the owner's call.

### One-time reconciliation, recorded for the audit trail

The repository had been created through the GitHub web UI with auto-initialization, so it arrived holding a stub `README.md` and `.gitattributes` on a history unrelated to ours. That is why `gh repo create` reported *"Name already exists on this account"* and why a plain `git push` would have been rejected as non-fast-forward.

With the owner's explicit approval, both stub files were discarded by a `--force-with-lease` push pinned to the inspected stub commit `f282b89`, so the push would abort if the remote had changed. Their entire content was the repo name and GitHub's default `* text=auto` line — nothing of the project was lost.

**If you ever recreate this remote, create it empty** — no README, no `.gitignore`, no licence — and the first push will be a clean fast-forward needing no force.

### The repository must be private

Not a preference. This repository will accumulate business strategy, positioning, and campaign plans, and later phases handle lead and contact data whose privacy treatment is **unresolved** (`Q-009`). Until that question is answered, the fail-closed choice is the only defensible one. `data/private/` is already git-ignored pre-emptively for the same reason (`D-033`).

### Commands the owner would run — **NOT YET EXECUTED**

Nothing below has been run. Both blocks are documentation of an owner action.

Using the GitHub CLI (`gh` 2.96.0, installed). Run from the project root. This creates the repo and wires up `origin`, without pushing:

```powershell
gh repo create agent-atlas-growth-department --private --source . --remote origin
```

Then push the first commit and set the upstream:

```powershell
git push -u origin main
```

Confirm afterwards that the repository really is private:

```powershell
gh repo view --json name,visibility
```

### Plain-`git` fallback

If the owner prefers to create the repository in the GitHub web UI (selecting **Private**, and creating it **empty** — no README, no `.gitignore`, no licence, so the first push is not rejected), wire it up manually instead:

```powershell
git remote add origin https://github.com/<owner>/agent-atlas-growth-department.git
```

```powershell
git push -u origin main
```

### Ongoing practice

The off-machine copy is only as current as the last `push`. Git history protects against accidental edits and deletions; the remote protects against losing the disk. **Push at every phase gate at minimum** — anything committed locally and not pushed is single-copy again, which is the residual part of `R-19`.

```powershell
git push
```

**Keep the repository private.** It holds business strategy, and later phases handle lead and contact data whose privacy treatment is still unresolved (`Q-009`).

---

## Secrets rules

From `user-guide/USER_INSTRUCTIONS.md`. These are binding, not advisory.

**Never paste a secret into a prompt.** Do not place passwords, API keys, OAuth tokens, recovery codes, Stripe secrets, or private customer data into:

- Markdown files
- Google Docs
- Google Sheets
- GitHub
- Screenshots
- Chat

Where values belong:

| Context | Where the value lives |
|---|---|
| Local development | `.env` — git-ignored, never committed |
| Production | **Google Secret Manager** |
| This repository | `.env.example` — placeholder variable **names** only |

Practical rules:

- `.env.example` contains empty values or the literal marker `<obtain-from-owner-do-not-commit>`. Never a realistic-looking fake key — those trip secret scanners and teach the wrong habit.
- If a secret is ever committed, treat it as **compromised**: rotate it at the provider and report it. Deleting it in a later commit does not remove it from history.
- Obtaining any credential is a Project Owner action. Agents document what would be needed; they do not request, create, or hold credentials.

**No `SECURITY_POLICY.md` exists yet.** Phase 03 owns writing it, and Phase 01 deliberately does not (`D-027`, `D-035`). Per `D-027`, that policy **must exist before any credential is introduced** to this project. Until it does, the correct state of `.env` is empty.

---

## Working agreement — how to run a phase

The short version. Full detail is in `user-guide/USER_INSTRUCTIONS.md` and `CLAUDE.md`.

**The loop:**

1. Check `CURRENT_PHASE.md` for the active phase.
2. Start Claude Code at the project root; paste `00_MASTER_START_HERE.md`, then that one phase prompt.
3. Claude builds a task graph and delegates specialists. One owner per file; parallel work only on genuinely independent outputs (Architecture Rules 4 and 5).
4. The phase ends with independent review and a phase-gate report (Rule 6).
5. You review the report. Confirm every required test has **actual evidence** — commands run and real output. "Everything looks good" is not evidence.
6. Resolve only the decisions marked as blocking.
7. Approve advancement by updating `CURRENT_PHASE.md` yourself, then start the next phase manually (Rule 7).

**A valid phase-gate report shows:** objective; files created or changed; agents used; tests actually run, with commands and results; artifacts where relevant; security and permission findings; unresolved decisions; known limitations; rollback procedure; and a recommendation of PASS, CONDITIONAL PASS, or FAIL.

**Unknown values stay `UNRESOLVED` or `BLOCKED`** (Rule 8). Nothing gets guessed to keep a phase moving.

**Human checkpoints — you must personally complete or approve:**

platform terms acceptance · captchas · identity and phone verification · production OAuth consent · account creation submission · product claims · testimonials · pricing and discounts · direct outreach · responses to complaints · paid advertising · spending · major brand changes · production deployment · public launch

Creating the GitHub remote falls under this list. So does anything that spends money — and no spend is authorized at all (`D-016`, `NG-001`).

**Boundaries:** this project may read *explicitly approved* files from `C:\Users\crone\Projects\Rough-Draft-Builders-Club` and must never modify that folder (`D-013`). **No file there has been approved yet** (`Q-007`). See `docs/PROJECT_BOUNDARIES.md`.
