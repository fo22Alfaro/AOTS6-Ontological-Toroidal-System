import hashlib
import json
from pathlib import Path

from historical_forensics.historical_manifest import merkle_root, sha256_file

def test_sha256_is_stable(tmp_path: Path):
    p = tmp_path / "doc.bin"
    p.write_bytes(b"AOTS6")
    assert sha256_file(p) == hashlib.sha256(b"AOTS6").hexdigest()

def test_merkle_is_deterministic():
    a = hashlib.sha256(b"A").hexdigest()
    b = hashlib.sha256(b"B").hexdigest()
    assert merkle_root([a, b]) == merkle_root([b, a])

def test_empty_merkle():
    assert merkle_root([]) == ""
