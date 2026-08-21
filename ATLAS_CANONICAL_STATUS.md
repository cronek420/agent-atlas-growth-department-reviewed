# Atlas Growth Department — Canonical Status

This repository is the canonical Atlas Growth Department lineage.

## Source-of-truth rule

- New internal Atlas growth/marketing automation work belongs here.
- `cronek420/agent-atlas-growth-department` is legacy/frozen and must not receive new feature work.
- Do not create another `reviewed`, `new`, `copy`, or alternate Growth Department repository.

## Boundary

This repo owns growth operations: market research, lead discovery, fit scoring, campaign planning, compliant outreach preparation/execution, follow-up, measurement, and reporting.

It does not own Surplus Recovery business logic, Treasure Hunter public-opportunity discovery, or Resume Agent profile/campaign logic.

## Runtime target

Production target: GitHub -> Cloud Build -> Artifact Registry -> Cloud Run Job/Service -> Cloud Scheduler -> Secret Manager -> authorized account connectors.

Local/Antigravity execution is development and maintenance, not the production dependency.

## Verification standard

Company first -> score fit -> choose decision-maker -> verify identity/current role -> find professional contact -> separately verify contact -> dedupe/suppress -> personalize -> send only when policy permits.

Guessed or pattern-derived email addresses are candidates only, never send-ready addresses without independent verification.

## Governance

Keep the existing approval, autonomy, budget, skill-provenance, security, privacy, claims, and phase-gate controls in this repository authoritative for Growth work.
