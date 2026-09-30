import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MOTOR = ROOT / "ejecucion_restitucion.py"
EJEMPLO = ROOT / "EXPEDIENTE-RESTITUCION-EJEMPLO.json"

def run(path):
    return subprocess.run(
        [sys.executable, str(MOTOR), str(path)],
        capture_output=True, text=True
    )

def test_example_is_structurally_valid():
    p = run(EJEMPLO)
    assert p.returncode == 0, p.stdout + p.stderr
    data = json.loads(p.stdout)
    assert data["valid"] is True
    assert data["state"] == "NO-DETERMINADO"
    assert data["valid"] is True

def test_executed_restitution_requires_evidence(tmp_path):
    x = json.loads(EJEMPLO.read_text(encoding="utf-8"))
    x["restitution"]["executed"] = True
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps(x), encoding="utf-8")
    p = run(bad)
    assert p.returncode != 0
    assert "execution_evidence" in p.stdout

def test_exhaustion_requires_decision_hash(tmp_path):
    x = json.loads(EJEMPLO.read_text(encoding="utf-8"))
    x["epistemic_state"] = "AGOTADO-PROCEDIMIENTO"
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps(x), encoding="utf-8")
    p = run(bad)
    assert p.returncode != 0
    assert "decision.document_hash" in p.stdout


def test_pending_act_cannot_be_reported_as_final():
    x = json.loads(EJEMPLO.read_text(encoding="utf-8"))
    x["epistemic_state"] = "RESTITUCIÓN"
    bad = ROOT / "_tmp_pending_invalid.json"
    bad.write_text(json.dumps(x), encoding="utf-8")
    try:
        p = run(bad)
        assert p.returncode != 0
        assert "PENDIENTE_ACREDITAR" in p.stdout
    finally:
        bad.unlink(missing_ok=True)
