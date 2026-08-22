import os
import json
from typing import Dict, Any, List

class DiscoveryConnector:
    """
    Interface for company research and discovery.
    In a real-world scenario with budget, this would wrap Exa, Tavily, or Clearbit.
    Since we are enforcing organic-only and no-unapproved-spend, this relies on
    an API key in .env or falls back to synthetic mock data for the tests.
    """
    
    def __init__(self):
        self.api_key = os.getenv("DISCOVERY_API_KEY")

    def discover_companies(self, criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Given audience criteria (industries, size, signals), discover matching companies.
        """
        if self.api_key:
            # TODO: Real implementation when API key is provided
            pass
        
        # Fallback to mock data for synthetic testing
        return [
            {
                "name": "Acme Corp",
                "website": "https://acme.example.com",
                "industry": criteria.get("industries", ["Software"])[0],
                "fit_score": 85,
                "fit_reason": "Acme Corp matches the industry criteria and shows recent signals of software scaling.",
                "source_url": "https://directory.example.com/acme",
                "source_retrieved_at": "2026-08-22T10:00:00Z"
            }
        ]

    def score_fit(self, company: Dict[str, Any], campaign_brief: Dict[str, Any]) -> int:
        """
        Score the fit of a discovered company against the campaign brief.
        0-100 scale.
        """
        return company.get("fit_score", 50)
