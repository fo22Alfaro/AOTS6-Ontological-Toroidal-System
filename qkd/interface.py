from __future__ import annotations
import hashlib
import hmac
import json
from dataclasses import dataclass, asdict
from typing import Any

SCHEMA = "AOTS6-QKD-INTERNAL-INTERFACE-1"
ROOT_ID = "AOTS6-ORIGINAL-ALFARO"
AUTHOR = "Alfredo Jhovany Alfaro García"

class QKDPolicyError(ValueError):
    pass

def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

@dataclass(frozen=True)
class QKDEvidence:
    schema: str
    root_id: str
    author: str
    source_id: str
    key_id: str
    sequence: int
    generation_time: str
    material_sha256: str
    material_bytes: int
    origin: str
    secret_material_excluded: bool
    replay_guard: str
    envelope_sha256: str

class QKDInterface:
    """Secure metadata/provenance boundary for AOTS6 QKD material.

    The interface accepts key material supplied by an authorized AOTS6 QKD
    process, records only a digest and metadata, and never writes the secret
    key into the repository, logs, or returned evidence object.
    """
    def __init__(self, *, author: str = AUTHOR):
        self.author = author
        self._seen: set[tuple[str, str, int]] = set()

    def attest(self, key_material: bytes, *, source_id: str, key_id: str,
               sequence: int, generation_time: str,
               origin: str = "AOTS6-INTERNAL-QKD") -> QKDEvidence:
        if not isinstance(key_material, (bytes, bytearray, memoryview)) or not key_material:
            raise QKDPolicyError("QKD key material must be non-empty bytes")
        if not source_id.startswith("AOTS6-INTERNAL-"):
            raise QKDPolicyError("source_id must identify an AOTS6 internal source")
        if not key_id or sequence < 0 or not generation_time:
            raise QKDPolicyError("key_id, sequence and generation_time are required")
        replay_key = (source_id, key_id, sequence)
        if replay_key in self._seen:
            raise QKDPolicyError("QKD material event already attested")
        material = bytes(key_material)
        material_digest = sha256(material)
        payload = {
            "schema": SCHEMA, "root_id": ROOT_ID, "author": self.author,
            "source_id": source_id, "key_id": key_id, "sequence": sequence,
            "generation_time": generation_time, "material_sha256": material_digest,
            "material_bytes": len(material), "origin": origin,
            "secret_material_excluded": True,
            "replay_guard": sha256(canonical_bytes({"source_id": source_id, "key_id": key_id, "sequence": sequence}))
        }
        envelope_digest = sha256(canonical_bytes(payload))
        self._seen.add(replay_key)
        return QKDEvidence(envelope_sha256=envelope_digest, **payload)

    @staticmethod
    def verify_material(evidence: QKDEvidence, key_material: bytes) -> bool:
        if evidence.secret_material_excluded is not True:
            return False
        return hmac.compare_digest(evidence.material_sha256, sha256(bytes(key_material)))

    @staticmethod
    def public_record(evidence: QKDEvidence) -> dict[str, Any]:
        record = asdict(evidence)
        record["secret_material"] = None
        return record
