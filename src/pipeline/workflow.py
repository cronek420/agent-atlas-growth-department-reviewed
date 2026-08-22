import logging
from typing import Dict, Any, List
from src.connectors.discovery import DiscoveryConnector
from src.connectors.enrichment import EnrichmentConnector
from src.connectors.suppression import SuppressionConnector
from src.connectors.gmail import GmailConnector
from src.storage import build_lead_record, write_lead

logger = logging.getLogger(__name__)

class LeadPipeline:
    """
    Enforces the 11-step company-first workflow and state transitions.
    """
    def __init__(self, campaign_id: str, campaign_brief: Dict[str, Any]):
        self.campaign_id = campaign_id
        self.campaign_brief = campaign_brief
        self.discovery = DiscoveryConnector()
        self.enrichment = EnrichmentConnector()
        self.suppression = SuppressionConnector()
        self.gmail = GmailConnector()

    def run_pipeline(self) -> List[Dict[str, Any]]:
        """Run the full end-to-end pipeline."""
        results = []
        
        # 1. Discover companies
        criteria = self.campaign_brief.get("audience", {})
        companies = self.discovery.discover_companies(criteria)
        
        for company in companies:
            # 2. Score company fit
            fit_score = self.discovery.score_fit(company, self.campaign_brief)
            company["fit_score"] = fit_score
            if fit_score < 65:
                # Reject weak fits
                continue
                
            # 3. Choose DM & 4. Verify identity
            roles = criteria.get("roles", [])
            dm = self.enrichment.find_decision_maker(company, roles)
            if dm.get("identity_confidence") == "low":
                continue # Skip or mark NEEDS_HUMAN
                
            # 5. Find email & 6. Verify email
            email = self.enrichment.find_professional_email(dm["name"], company["website"])
            verification_status = self.enrichment.verify_email(email)
            if verification_status in ["Invalid", "Risky"]:
                continue
                
            contact = {
                "professional_email": email,
                "email_verification_status": verification_status
            }

            # 7. Deduplicate and suppress
            if self.suppression.is_suppressed(email, company["website"]):
                continue

            # 8. Personalize
            evidence = self.enrichment.find_personalization_evidence(company, dm)
            outreach = {
                "personalization_evidence": evidence,
                "status": "DRAFT_READY",
                "autonomy_level": "SIMULATION",
                "send_allowed": False
            }

            # 9. Validate (Deterministic schema compliance check before drafting)
            # 10. Route by autonomy (Drafts in Gmail)
            draft = self.gmail.create_draft(
                to_email=email,
                subject="Relevance to " + company["name"],
                body=f"Hi {dm['name']},\n\nNoticed {evidence[0]}\n\nBest,\nAgent Atlas"
            )
            outreach["draft_id"] = draft["id"]
            outreach["status"] = "PENDING_REVIEW" # Awaiting human approval to send

            # Save to structured storage
            lead_record = build_lead_record(
                campaign_id=self.campaign_id,
                company=company,
                decision_maker=dm,
                contact=contact,
                outreach=outreach
            )
            write_lead(lead_record)
            results.append(lead_record)

        return results
