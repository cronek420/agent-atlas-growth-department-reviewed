# Prompt and Build Quality Rubric

Score every phase prompt and implementation from 0–5 in each category.

| Category | 0 | 3 | 5 |
|---|---|---|---|
| Objective clarity | Missing | Understandable | Single measurable outcome |
| Inputs | Invented/unknown | Partially defined | Explicit, validated, sourced |
| Outputs | Vague | Named deliverables | Schemas, paths, acceptance criteria |
| Agent separation | None | Some roles | One owner, independent specialists, reviewer |
| Tool realism | Hallucinated | Mostly plausible | Confirmed tools, adapters, fallbacks |
| Permissions | Unbounded | General limits | Least privilege and explicit gates |
| Determinism | LLM-only | Mixed | Deterministic state, validation, retries |
| Failure handling | None | Basic | Classified errors, retry, rollback, escalation |
| Testing | Claimed | Partial | Executed tests with evidence |
| Auditability | None | Logs only | Run IDs, handoffs, decisions, evidence |
| User usability | Technical maze | Usable | Beginner steps and exact next action |
| Portability | Locked in | Some adapters | Standard schemas and provider isolation |

## Passing threshold

- No category below 3.
- Average score at least 4.
- Security, permissions, testing, and failure handling must each score 4 or higher.
- A critical unsupported integration automatically fails the phase.
