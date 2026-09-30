import json
from pathlib import Path
import pytest
from historical_forensics.verify_claims import main

def test_reproducible_rejects_placeholder(tmp_path, monkeypatch):
    claims=tmp_path/"claims.jsonl"
    claims.write_text(json.dumps({
      "claim_id":"X","text":"x","epistemic_state":"DOCUMENTADO",
      "source":{"institution":"I","reference":"R","url":"https://example.org","accessed_at":"2026-09-30"},
      "evidence":{"object_id":"X","sha256":"PENDIENTE_DE_CAPTURA","locator":"folio 1"},
      "reproducibility":"REPRODUCIBLE"
    })+"\n",encoding="utf-8")
    monkeypatch.setattr("sys.argv",["verify_claims.py",str(claims)])
    assert main()==1

def test_partial_allows_catalog_without_object(tmp_path, monkeypatch):
    claims=tmp_path/"claims.jsonl"
    claims.write_text(json.dumps({
      "claim_id":"X","text":"x","epistemic_state":"DOCUMENTADO",
      "source":{"institution":"I","reference":"R","url":"https://example.org","accessed_at":"2026-09-30"},
      "evidence":{"object_id":"X","sha256":"PENDIENTE_DE_CAPTURA","locator":"registro"},
      "reproducibility":"PARCIALMENTE_REPRODUCIBLE"
    })+"\n",encoding="utf-8")
    monkeypatch.setattr("sys.argv",["verify_claims.py",str(claims)])
    assert main()==0
