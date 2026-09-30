from verify_no_time_state import verify

def base():
    return {
      "object_id":"x","state":"HASHED",
      "source":{"institution":"Archive","reference":"REF","accessed_at":"2026-09-30T00:00:00Z"},
      "integrity":{"sha256":"0"*64,"byte_length":1,"algorithm":"SHA-256"},
      "locator":{"kind":"page","value":"1"},"provenance":[]
    }

def test_valid(): assert verify(base())==[]

def test_bad_hash():
    x=base(); x["integrity"]["sha256"]="bad"
    assert "invalid:sha256" in verify(x)

def test_extracted_requires_literal():
    x=base(); x["state"]="EXTRACTED"
    assert "literal_required" in verify(x)

def test_verified_restriction_requires_basis():
    x=base(); x["restriction"]={"status":"VERIFIED"}
    assert "verified_restriction_without_basis" in verify(x)
