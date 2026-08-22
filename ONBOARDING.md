# Agent Atlas Onboarding

Safe first-run path for a fresh clone.

## Quick start

```powershell
python tools/onboard.py
```

Verification-only:

```powershell
python tools/onboard.py --check
python tools/onboard.py --dry-run
python tools/onboard.py --reset
```

`--check` validates without creating `.env`. `--dry-run` also avoids creating `.env`. `--reset` removes only the generated onboarding status report.

## What onboarding does

- checks Python, Git, required governance files, and deterministic controls
- runs policy regression checks and deliberate negative controls
- validates custom-skill contracts, capability-registry vocabulary, and permission-matrix reproducibility
- creates `.env` from `.env.example` only for normal onboarding when needed
- inventories configuration by variable **name only**; secret values never enter the report
- writes `ONBOARDING_STATUS.md` as `READY`, `NEEDS HUMAN`, or `BLOCKED`

## What onboarding does not do

It does not send messages, publish, deploy production systems, purchase/start subscriptions, create production accounts, change credentials, or promote autonomy. Those remain governed by policy and approval gates.

## Result

- **READY** — deterministic checks passed and no setup warning remains.
- **NEEDS HUMAN** — controls passed, but operator configuration/action remains.
- **BLOCKED** — a required runtime/file/control failed. Diagnose it; do not bypass it.

Read `HUMAN_INSTRUCTIONS.md` before enabling consequential capabilities.