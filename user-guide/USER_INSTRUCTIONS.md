# User Instructions — How to Run This Build Package

## Recommended project location

Create the project as a separate root folder:

`C:\Users\crone\Projects\agent-atlas-growth-department`

Do not place it inside the Rough Draft Builders Club application repository.

The marketing project may read explicitly approved source files from:

`C:\Users\crone\Projects\Rough-Draft-Builders-Club`

It must not modify that folder unless a later decision authorizes specific files.

## How to use each phase

1. Open Antigravity.
2. Open the `agent-atlas-growth-department` root folder.
3. Start Claude Code at the project root.
4. Paste `00_MASTER_START_HERE.md`.
5. Paste only the prompt for the current phase.
6. Let Claude create its task graph and delegate specialists.
7. Review the phase-gate report.
8. Confirm that every required test has actual evidence.
9. Resolve only decisions marked as blocking.
10. Approve advancement by updating `CURRENT_PHASE.md`.
11. Start the next phase manually.

## Never paste secrets into prompts

Do not place passwords, API keys, OAuth tokens, recovery codes, Stripe secrets, or private customer data into Markdown, Google Docs, Google Sheets, GitHub, screenshots, or chat.

Use:
- `.env` for local development when appropriate
- Google Secret Manager for production
- `.env.example` with placeholder variable names only

## Human checkpoints

You must personally complete or approve:

- Platform terms acceptance
- Captchas
- Identity and phone verification
- Production OAuth consent
- Account creation submission
- Product claims
- Testimonials
- Pricing and discounts
- Direct outreach
- Responses to complaints
- Paid advertising
- Spending
- Major brand changes
- Production deployment
- Public launch

## What a valid phase-gate report must show

- Objective
- Files created or changed
- Agents used
- Tests actually run
- Test commands
- Test results
- Screenshots or artifacts where relevant
- Security and permission findings
- Unresolved decisions
- Known limitations
- Rollback procedure
- Recommendation: PASS, CONDITIONAL PASS, or FAIL

A report that only says “everything looks good” is not evidence.
