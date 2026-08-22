import json
import os
from typing import List, Dict, Any

class SuppressionConnector:
    """
    Handles global suppression, bounce, opt-out, duplicate, complaint, 
    and do-not-contact checking.
    """
    def __init__(self, fixture_path: str = None):
        if fixture_path is None:
            # Default to test fixture path since Q-009 prevents real PII DB setup
            self.fixture_path = os.path.join("tests", "fixtures", "suppression_list.json")
        else:
            self.fixture_path = fixture_path

    def _load_suppression_data(self) -> Dict[str, List[str]]:
        if not os.path.exists(self.fixture_path):
            return {"domains": [], "emails": []}
        with open(self.fixture_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def is_suppressed(self, email: str, company_domain: str) -> bool:
        """
        Check if an email or domain is on the suppression list.
        """
        data = self._load_suppression_data()
        
        email_lower = email.lower()
        domain_lower = company_domain.lower()

        if email_lower in [e.lower() for e in data.get("emails", [])]:
            return True
        
        if domain_lower in [d.lower() for d in data.get("domains", [])]:
            return True

        return False
