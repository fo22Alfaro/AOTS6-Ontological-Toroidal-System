import tempfile,unittest
from pathlib import Path
from centro_madre.registry import build_registry,verify_registry
class CentroMadreTests(unittest.TestCase):
    def test_registry_schema(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)
            for p in ["geometry/AOTS6_Torus.obj","geometry/AOTS6_Geodesics.svg","AOTS6_Paper.md","ARCHITECTURE.md","research/AOTS6_ARTIFACT_ROOT.json","research/AOTS6_PROVENANCE_MANIFEST.json","research/aots6_provenance_detector.py","security/aots6_crypto_runtime.py","security/AOTS6_CRYPTO_RUNTIME.md","research/AOTS6_QUANTUM_STATE_METACOMPUTATION_RECORD.md"]:
                q=r/p; q.parent.mkdir(parents=True,exist_ok=True); q.write_text("x",encoding="utf-8")
            ok,errors=verify_registry(build_registry(d))
            self.assertTrue(ok,errors)
    def test_missing_implemented_artifact_fails(self):
        with tempfile.TemporaryDirectory() as d:
            ok,errors=verify_registry(build_registry(d))
            self.assertFalse(ok)
            self.assertIn("toroidal_geometry:missing",errors)
if __name__=="__main__": unittest.main()
