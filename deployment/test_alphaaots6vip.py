import importlib.util
import json
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("validate_alphaaots6vip.py")
SPEC = importlib.util.spec_from_file_location("validator", SCRIPT)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)

class DeploymentManifestTests(unittest.TestCase):
    def test_current_manifest_is_structurally_valid(self):
        data = json.loads(Path(__file__).with_name("alphaaots6vip.manifest.json").read_text())
        self.assertEqual(validator.validate(data), [])

    def test_onchain_state_requires_receipt_fields(self):
        data = json.loads(Path(__file__).with_name("alphaaots6vip.manifest.json").read_text())
        data["deployment_state"] = "ONCHAIN_CONFIRMED"
        self.assertTrue(any("chain_id" in e for e in validator.validate(data)))

    def test_name_resolution_requires_evidence(self):
        data = json.loads(Path(__file__).with_name("alphaaots6vip.manifest.json").read_text())
        data["name_registration"] = "NAME_RESOLUTION_VERIFIED"
        self.assertTrue(any("resolution" in e for e in validator.validate(data)))

    def test_private_key_exposure_is_rejected(self):
        data = json.loads(Path(__file__).with_name("alphaaots6vip.manifest.json").read_text())
        data["security"]["private_keys_in_repository"] = True
        self.assertTrue(any("private key" in e for e in validator.validate(data)))

if __name__ == "__main__":
    unittest.main()
