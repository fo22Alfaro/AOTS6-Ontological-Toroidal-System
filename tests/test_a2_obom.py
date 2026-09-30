from a2_obom import certify_a2_obom, verify_a2_obom, A2OBOMAuditError

def sample():
    return {
        "schema": "AOTS6-A2-OBOM-1",
        "data": {"artifact": "AOTS6"},
        "ontology": {"root": "AOTS6-ORIGINAL-ALFARO"},
        "shacl": {"required": ["data", "ontology", "policy"]},
        "policy": {"sensitive_output": "filtered"},
    }

def test_verify_requires_declared_digest():
    result = verify_a2_obom(sample())
    assert result["verified"] is False
    assert result["integrity"] is False
    assert "digest_missing" in result["errors"]

def test_sensitive_values_are_filtered():
    obj = sample()
    obj["data"]["private_key"] = "DO_NOT_EXPOSE"
    result = verify_a2_obom(obj)
    assert result["artifact"]["data"]["private_key"] == "[FILTERED]"
    assert result["verified"] is False

def test_certification_requires_confirmation():
    try:
        certify_a2_obom(sample(), data={"artifact": "changed"},
                        ontology={"root": "AOTS6-ORIGINAL-ALFARO"},
                        shacl={"required": ["data", "ontology", "policy"]},
                        policy={"sensitive_output": "filtered"})
    except A2OBOMAuditError:
        return
    raise AssertionError("certification must require explicit confirmation")

def test_certification_reverifies_candidate():
    result = certify_a2_obom(
        sample(), data={"artifact": "changed"},
        ontology={"root": "AOTS6-ORIGINAL-ALFARO"},
        shacl={"required": ["data", "ontology", "policy"]},
        policy={"sensitive_output": "filtered"}, user_confirmation=True)
    assert result["certified_candidate"] is True
    assert result["verified"] is True
    assert result["integrity"] is True
    assert result["policy_conformant"] is True
    assert len(result["digest"]) == 64
