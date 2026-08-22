# Agent Atlas Growth Department — Human Instructions

This is the plain-English operator guide. It does not replace repository governance. If it conflicts with `APPROVAL_POLICY.md`, `AUTONOMY_POLICY.md`, `BUDGET_POLICY.md`, `SECURITY_POLICY.md`, `PUBLISHING_POLICY.md`, `MESSAGING_POLICY.md`, `DATA_RETENTION_POLICY.md`, `DECISIONS.md`, or deterministic policy controls, the stricter machine-enforced rule wins.

## Operating model

Atlas should perform routine reversible work—research, analysis, drafting, classification, verification, simulations, testing, reporting, and preparation—without requiring constant supervision. Consequential execution is allowed only inside the capability's current approved autonomy boundary.

## Human-gated actions

Unless deterministic policy explicitly grants a narrowly defined earned-autonomy scope, require human approval for spending or paid services, budget changes, external messaging/outreach, public publishing, production deployments, production accounts/credentials/permissions/integrations, destructive or irreversible changes, governance/security/autonomy changes, and autonomy promotion.

Approval applies only to the exact presented scope. Never treat silence or vague permission as approval.

## Simple operator commands

- `APPROVE` — approve exactly the presented action.
- `REJECT` — do not execute it.
- `REVISE: <instruction>` — revise and return the proposal.
- `STOP` — stop the affected autonomous workflow and return it to a safe state.

## Secrets

Secrets belong in local environment configuration or an approved secret manager, never GitHub source, Markdown, logs, screenshots, prompts, or approval comments. If a secret is committed, treat it as exposed and rotate/revoke it.

## Spending

Before approval, show amount, vendor, purpose, one-time versus recurring status, and cancellation implications. Free trials that become paid count as recurring spending. Prefer the lowest-cost reversible experiment that answers the business question.

## Messaging/outreach

Before a newly gated campaign class is approved, show audience, sender identity, approved template/content boundaries, channel, volume, suppression/stop behavior, and applicable compliance constraints. Once a capability earns limited autonomy, it may operate only inside those deterministic boundaries. New audiences, offers, material claims/templates, domains, countries, or material volume increases return to approval.

## Publishing/deployment

Before gated public publishing or production deployment, show the exact change, destination, validation evidence, rollback method, and credential/billing impact. Prefer preview/staging first.

## Emergency stop

If Atlas behaves unexpectedly, exceeds scope, repeatedly fails, or you want it stopped, issue `STOP`. Disable/demote the affected capability before investigation. Never bypass a failed deterministic safety check merely to make a workflow run.

## Earned autonomy

Autonomy increases in stages using repository policy and evidence. Capabilities start disabled/simulation-first, progress only after successful lower-risk operation and required tests, and are demoted/disabled when reliability or safety degrades.

## Regular review

Review pending approvals, failures/retries, costs, external actions, autonomy-state changes, security warnings, recurring manual interventions, and measurable results. Atlas should summarize these rather than requiring the owner to inspect raw logs.

## GitHub/code changes

Use branches and pull requests for meaningful code/governance changes. Automated assurance should be green before merge. Green CI is evidence—not permission to bypass an approval gate.

## Failure recovery

1. Stop/contain potentially consequential actions.
2. Preserve useful evidence without exposing secrets.
3. Classify the failure: code, config, credential, policy, data, vendor/API, or assumption.
4. Fix the smallest root cause rather than weakening a guardrail.
5. Re-run relevant checks and negative controls.
6. Resume only when controls are green and required approval remains valid.

## Definition of finished

A production-capable feature should have a clear purpose/owner, defined inputs/outputs, deterministic boundaries for consequential actions, safe failure behavior, appropriate tests including negative controls, cost visibility, useful logs/reporting, documented human gates, rollback/disable capability, and no committed secrets.

**Governing principle:** automate preparation aggressively; automate consequential execution only after that capability has earned authority. Atlas does the legwork, shows evidence, surfaces decisions, executes only within its authorized boundary, and leaves an auditable record.