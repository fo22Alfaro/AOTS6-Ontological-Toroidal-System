import unittest
from aots6_interai_integrity import detect_prompt_manipulation, anchor_payload

class TestAOTS6InterAIIntegrity(unittest.TestCase):
    def test_detects_changed_prompt(self):
        a={"prompt":"preserve state","source":"A"}
        b={"prompt":"replace state","source":"A"}
        r=detect_prompt_manipulation(a,b)
        self.assertTrue(r.manipulation_detected)
        self.assertIn("prompt",r.changed_fields)
        self.assertEqual(r.order,(7,19,2))
        self.assertEqual(len(r.evidence_sha256),64)

    def test_identical_state(self):
        a={"prompt":"same","source":"A"}
        r=detect_prompt_manipulation(a,a)
        self.assertFalse(r.manipulation_detected)

    def test_anchor_payload(self):
        a={"prompt":"same"}
        r=detect_prompt_manipulation(a,a)
        p=anchor_payload(r)
        self.assertEqual(p["order"],"7,19,2")
        self.assertEqual(len(p["sha256"]),64)

if __name__ == "__main__":
    unittest.main()
