import pytest
from qkd.interface import QKDInterface, QKDPolicyError

def test_internal_qkd_attestation_excludes_secret():
    q = QKDInterface()
    material = b"internal-qkd-test-material"
    ev = q.attest(material, source_id="AOTS6-INTERNAL-QKD-001", key_id="K-001", sequence=1, generation_time="2026-09-30T00:00:00Z")
    record = q.public_record(ev)
    assert record["secret_material"] is None
    assert ev.material_bytes == len(material)
    assert q.verify_material(ev, material)

def test_external_source_is_rejected():
    with pytest.raises(QKDPolicyError):
        QKDInterface().attest(b"x", source_id="EXTERNAL-QKD", key_id="K", sequence=0, generation_time="2026-09-30T00:00:00Z")

def test_replay_is_rejected():
    q = QKDInterface()
    kwargs = dict(source_id="AOTS6-INTERNAL-QKD-001", key_id="K-002", sequence=2, generation_time="2026-09-30T00:00:00Z")
    q.attest(b"x", **kwargs)
    with pytest.raises(QKDPolicyError):
        q.attest(b"x", **kwargs)

def test_wrong_material_fails():
    q = QKDInterface()
    ev = q.attest(b"correct", source_id="AOTS6-INTERNAL-QKD-001", key_id="K-003", sequence=3, generation_time="2026-09-30T00:00:00Z")
    assert not q.verify_material(ev, b"wrong")
