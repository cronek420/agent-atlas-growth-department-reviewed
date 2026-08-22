import unittest
import os
import tempfile
from src.pipeline.workflow import LeadPipeline
from src.storage import read_all_leads

class TestWorkflow(unittest.TestCase):
    
    def setUp(self):
        # Override storage file for tests
        self.temp_storage = tempfile.NamedTemporaryFile(delete=False).name
        os.environ["STORAGE_FILE"] = self.temp_storage

    def tearDown(self):
        if os.path.exists(self.temp_storage):
            os.remove(self.temp_storage)

    def test_end_to_end_synthetic_pipeline(self):
        """
        Tests the company-first pipeline end to end using synthetic mock data.
        """
        import src.storage
        src.storage.STORAGE_FILE = self.temp_storage

        brief = {
            "audience": {
                "industries": ["Software"],
                "roles": ["CTO"]
            }
        }
        
        pipeline = LeadPipeline(campaign_id="test_camp_1", campaign_brief=brief)
        # Mock suppression to use standard test fixture
        pipeline.suppression.fixture_path = os.path.join("tests", "fixtures", "suppression_list.json")
        
        results = pipeline.run_pipeline()
        
        self.assertEqual(len(results), 1)
        lead = results[0]
        
        # Verify deterministic checks
        self.assertEqual(lead["status"], "PENDING_REVIEW")
        self.assertEqual(lead["campaign_id"], "test_camp_1")
        self.assertEqual(lead["email"], "jane@acme.example.com")
        self.assertEqual(lead["outreach"]["autonomy_level"], "SIMULATION")
        self.assertFalse(lead["outreach"]["send_allowed"])
        self.assertEqual(lead["outreach"]["draft_id"], "mock_draft_id_123")
        
        # Verify it was persisted
        persisted = read_all_leads()
        self.assertEqual(len(persisted), 1)
        self.assertEqual(persisted[0]["id"], lead["id"])
