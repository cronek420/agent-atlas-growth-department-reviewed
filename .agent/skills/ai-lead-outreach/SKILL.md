---
name: ai-lead-outreach
description: Company-first lead discovery, decision-maker verification, professional email verification, personalization, suppression, and controlled outreach for Agent Atlas Growth Department.
version: 2.0
---

# AI Lead Outreach

## Purpose
Turn an approved target-market brief into verified, deduplicated, source-backed B2B leads and personalized outreach while enforcing Agent Atlas governance and earned-autonomy rules.

## Use this skill when
- Atlas must discover companies from fit criteria instead of relying on an existing lead list.
- Atlas must identify and verify the most appropriate business decision-maker.
- Atlas must find and separately verify a professional email.
- Atlas must prepare or execute outreach inside an approved campaign class.

## Do not use this skill when
- The target market, offer, sender identity, or jurisdictions are undefined.
- The work would require prohibited data acquisition, deception, evasion, or sensitive personal data.
- A suppression/do-not-contact check cannot be completed.
- The required capability is BLOCKED by repository policy.

## Required inputs
- Approved campaign/offer brief.
- Target-company fit criteria and exclusions.
- Allowed jurisdictions and sources.
- Sender identity and monitored reply route.
- System of record and suppression source.
- Approved autonomy level and daily volume ceiling.

## Company-first workflow
1. **Discover companies.** Search only approved sources for companies matching the campaign fit criteria.
2. **Score company fit before enrichment.** Reject weak fits before spending contact-enrichment resources.
3. **Choose the decision-maker by use case and company size.** Do not default mechanically to CEO/CFO. Select the role that owns the problem or purchasing decision.
4. **Verify identity and current role.** Require multiple credible sources when practical. If identity/role remains uncertain, skip or mark `NEEDS_HUMAN` rather than guessing.
5. **Find professional email.** Use approved business-contact sources only.
6. **Verify email separately.** Identity verification and email verification are separate checks. Never infer that a plausible email is verified.
7. **Deduplicate and suppress.** Check prior contacts, active campaigns, bounces, opt-outs, complaints, invalid addresses, and global do-not-contact records before drafting or sending.
8. **Personalize from evidence.** Use current, source-backed observations. Do not manufacture pain points, familiarity, results, urgency, relationships, or compliments.
9. **Validate.** Run deterministic lead-record validation and campaign policy checks.
10. **Route by autonomy.** Simulation/draft states prepare output only. Limited-autonomy sending is permitted only for a previously approved campaign class and only inside deterministic audience/template/volume/jurisdiction/suppression boundaries.
11. **Stop and surface meaningful replies.** Stop automated sequences on genuine replies, opt-outs, complaints, or hard bounces. Suppress delivery failures from owner attention unless they indicate a systemic issue. Surface genuine human replies and material exceptions.

## Evidence standard
Every material lead fact must include a source URL/reference and retrieval date. Keep `FACT`, `INFERENCE`, and `UNKNOWN` distinct internally. Unknowns are not facts.

## Minimum lead record
```yaml
lead_id: ""
company:
  name: ""
  website: ""
  fit_score: 0
  fit_reason: ""
  source_url: ""
  source_retrieved_at: ""
decision_maker:
  name: ""
  role: ""
  role_verified: false
  identity_confidence: "low"
  verification_sources: []
contact:
  professional_email: ""
  email_verification_status: "unknown"
  email_verified_at: ""
safety:
  suppression_check: "unknown"
  compliance_status: "review"
  duplicate_check: "unknown"
outreach:
  personalization_evidence: []
  draft_status: "new"
  autonomy_level: "SIMULATION"
  send_allowed: false
```

## Readiness states
- `READY` — record/campaign passes all deterministic checks for its current autonomy level.
- `NEEDS_HUMAN` — safe to continue preparation, but an owner decision/configuration is required before consequential execution.
- `BLOCKED` — a required fact, policy, verification, suppression, or safety check failed. Do not bypass.

## Earned autonomy
Default new campaign classes to `SIMULATION`. Promotion to limited sending autonomy requires successful tests, negative controls, approved boundaries, working suppression/stop logic, and policy authorization. New audience, country, sender/domain, offer, materially changed template/claim, or material volume increase returns the campaign to human approval.

## Hard stops
Never send when email verification is invalid/unknown under a verified-only campaign, suppression is not PASS, identity/role is uncertain beyond the campaign threshold, compliance is FAIL/BLOCKED, the campaign exceeds its approved volume, or the current policy engine denies the action.

## Outputs
- Verified lead records with source/confidence fields.
- Rejected/skipped records with reason codes.
- Personalized drafts or approved sends according to autonomy state.
- Batch summary containing counts, failures, suppressed records, genuine replies, and meaningful exceptions.

## Validation
Before a record is eligible for outreach, run:

```powershell
python tools/lead_pipeline_check.py path\to\lead.json
```

A deliberate bad fixture must fail before the validator is trusted for production changes.

## Failure handling
Fail closed. Retry transient source/provider errors only within configured limits. Never switch domains, addresses, identities, data sources, or campaign classes merely to bypass a failure.

## Governing rule
Do the routine legwork automatically. Escalate consequential boundary changes. Earn autonomy through evidence.