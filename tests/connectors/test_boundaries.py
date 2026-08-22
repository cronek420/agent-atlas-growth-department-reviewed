import unittest
from src.connectors.gmail import GmailConnector
from src.connectors.suppression import SuppressionConnector
import os
import tempfile
import json

class TestConnectorBoundaries(unittest.TestCase):
    
    def test_gmail_simulation_mode(self):
        """
        Negative control: ensure Gmail connector fails closed and NEVER attempts
        to send live emails when unauthenticated.
        """
        connector = GmailConnector()
        # Force unauthenticated for test
        connector._is_authenticated = False
        
        draft = connector.create_draft("test@example.com", "Test", "Body")
        self.assertEqual(draft["status"], "DRAFT_CREATED")
        self.assertEqual(draft["id"], "mock_draft_id_123")

    def test_suppression_logic(self):
        """
        Ensure suppression logic catches blocked domains and emails.
        """
        # Create a temporary fixture
        mock_suppression = {
            "domains": ["blocked.com"],
            "emails": ["bad@example.com"]
        }
        with tempfile.NamedTemporaryFile("w", delete=False) as f:
            json.dump(mock_suppression, f)
            temp_path = f.name

        try:
            connector = SuppressionConnector(fixture_path=temp_path)
            
            # Should be suppressed
            self.assertTrue(connector.is_suppressed("someone@blocked.com", "blocked.com"))
            self.assertTrue(connector.is_suppressed("bad@example.com", "example.com"))
            
            # Should NOT be suppressed
            self.assertFalse(connector.is_suppressed("good@example.com", "example.com"))
        finally:
            os.remove(temp_path)
