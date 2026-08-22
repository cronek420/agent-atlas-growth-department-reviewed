import json
import os
import uuid
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional

STORAGE_FILE = os.path.join("data", "private", "leads.jsonl")

def init_storage():
    """Ensure the storage directory and file exist."""
    os.makedirs(os.path.dirname(STORAGE_FILE), exist_ok=True)
    if not os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, 'a', encoding='utf-8') as f:
            pass

def generate_id() -> str:
    return str(uuid.uuid4())

def get_current_time() -> str:
    return datetime.now(timezone.utc).isoformat()

def read_all_leads() -> List[Dict[str, Any]]:
    """Read all leads from the JSONL file."""
    if not os.path.exists(STORAGE_FILE):
        return []
    leads = []
    with open(STORAGE_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                leads.append(json.loads(line))
    return leads

def write_lead(lead: Dict[str, Any]):
    """Append a new lead to the JSONL file."""
    init_storage()
    with open(STORAGE_FILE, 'a', encoding='utf-8') as f:
        f.write(json.dumps(lead) + "\n")

def update_lead(lead_id: str, updates: Dict[str, Any]) -> bool:
    """Update an existing lead. Rewrites the file for simplicity."""
    leads = read_all_leads()
    updated = False
    with open(STORAGE_FILE, 'w', encoding='utf-8') as f:
        for lead in leads:
            if lead.get("id") == lead_id:
                lead.update(updates)
                lead["updated_at"] = get_current_time()
                updated = True
            f.write(json.dumps(lead) + "\n")
    return updated

def build_lead_record(
    campaign_id: str,
    company: Dict[str, Any],
    decision_maker: Dict[str, Any],
    contact: Dict[str, Any],
    outreach: Dict[str, Any],
    role: str = "RUNTIME_AGENT"
) -> Dict[str, Any]:
    """
    Build a lead record conforming to schemas/lead.schema.json and the
    extended reporting requirements.
    """
    now = get_current_time()
    return {
        "id": generate_id(),
        "schema_version": "1.0.0",
        "idempotency_key": f"{campaign_id}-{contact.get('professional_email', '')}",
        "status": outreach.get("status", "NEW"),
        "version": 1,
        "created_at": now,
        "updated_at": now,
        "created_by_role": role,
        "contact_name": decision_maker.get("name", ""),
        "email": contact.get("professional_email", ""),
        "phone": contact.get("phone", None),
        "source": company.get("source_url", "manual"),
        "consent_status": "UNKNOWN",
        
        # Extended fields for structured reporting
        "campaign_id": campaign_id,
        "company": company,  # e.g. {"name": "...", "fit_score": 85, "fit_reason": "..."}
        "decision_maker": decision_maker,  # e.g. {"role": "...", "identity_verification_sources": []}
        "contact": contact,  # e.g. {"email_verification_status": "Verified"}
        "outreach": outreach,  # e.g. {"personalization_evidence": [], "reply_classification": None}
    }
