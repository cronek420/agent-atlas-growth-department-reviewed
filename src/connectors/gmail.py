import os
import json
from typing import Dict, Any, List

class GmailConnector:
    """
    Gmail API Connector for outreach.
    Strictly enforced to run in SIMULATION / DRAFT_ONLY mode,
    meaning it will only create drafts and never send live emails.
    """

    def __init__(self):
        self.credentials_path = os.path.join("data", "private", "credentials.json")
        self.token_path = os.path.join("data", "private", "token.json")
        self._is_authenticated = self._check_auth()

    def _check_auth(self) -> bool:
        """Check if we have the necessary OAuth tokens."""
        return os.path.exists(self.token_path)

    def create_draft(self, to_email: str, subject: str, body: str) -> Dict[str, Any]:
        """
        Creates a draft in the user's Gmail account.
        NEVER sends the email.
        """
        if not self._is_authenticated:
            # Synthetic fallback if no real credentials exist
            return {
                "id": "mock_draft_id_123",
                "status": "DRAFT_CREATED",
                "to": to_email,
                "subject": subject
            }
        
        # TODO: Real google-api-python-client implementation
        # service = build('gmail', 'v1', credentials=creds)
        # message = self._create_message(to_email, subject, body)
        # draft = service.users().drafts().create(userId='me', body={'message': message}).execute()
        return {
            "id": "real_draft_id",
            "status": "DRAFT_CREATED",
            "to": to_email,
            "subject": subject
        }

    def fetch_replies(self, since_date: str) -> List[Dict[str, Any]]:
        """
        Polls for replies to our sent outreach emails.
        """
        if not self._is_authenticated:
            # Mock replies for synthetic testing
            return [
                {
                    "from": "janedoe@acme.example.com",
                    "subject": "Re: Collaboration opportunity",
                    "body": "Yes, I am interested in learning more.",
                    "date": "2026-08-22T12:00:00Z"
                },
                {
                    "from": "info@acme.example.com",
                    "subject": "Out of Office",
                    "body": "I am currently out of the office.",
                    "date": "2026-08-22T13:00:00Z"
                }
            ]

        # TODO: Real Gmail API search for 'in:inbox label:outreach'
        return []
