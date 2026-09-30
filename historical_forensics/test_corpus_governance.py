from instantiate_corpus import instantiate

def base():
    return {
      "record_id":"CORPUS:test:1","object_id":"obj1","state":"HASHED","access":"PUBLIC",
      "provenance":{"institution":"Archive","reference":"REF"},
      "integrity":{"sha256":"0"*64,"algorithm":"SHA-256"},
      "governance":{"roles":["verifier"],"history":[]}
    }

def test_base(): assert instantiate(base())==[]

def test_missing_hash():
    x=base(); x["integrity"]["sha256"]="bad"
    assert "hashed_state_requires_sha256" in instantiate(x)

def test_verified_restriction_requires_basis():
    x=base(); x["restriction"]={"status":"VERIFIED"}
    assert "verified_restriction_without_basis" in instantiate(x)

def test_unknown_state():
    x=base(); x["state"]="FACT"
    assert "invalid:state" in instantiate(x)
