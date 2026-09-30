"""AOTS6 A2-OBOM verification and certification boundary."""
from __future__ import annotations
from copy import deepcopy
import hashlib, json, re
from typing import Any

SCHEMA = "AOTS6-A2-OBOM-1"
SENSITIVE_KEY_RE = re.compile(
    r"(private.?key|secret|token|password|credential|authorization|access.?key)",
    re.IGNORECASE,
)

class A2OBOMAuditError(ValueError):
    pass

def _filter_sensitive(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: "[FILTERED]" if SENSITIVE_KEY_RE.search(str(k)) else _filter_sensitive(v)
                for k, v in value.items()}
    if isinstance(value, list):
        return [_filter_sensitive(v) for v in value]
    return value

def _canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")

def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()

def _policy_check(obom: dict[str, Any]) -> list[str]:
    errors = []
    if obom.get("schema") != SCHEMA:
        errors.append("schema_mismatch")
    for section in ("data", "ontology", "shacl", "policy"):
        if section not in obom:
            errors.append(f"missing_{section}")
    if obom.get("policy", {}).get("sensitive_output") not in {"filtered", "metadata_only"}:
        errors.append("sensitive_output_policy_required")
    return errors

def verify_a2_obom(obom: dict[str, Any]) -> dict[str, Any]:
    """Mandatory validity gate. Never report validity without this call."""
    if not isinstance(obom, dict):
        raise A2OBOMAuditError("A2-OBOM must be a mapping")
    filtered = _filter_sensitive(deepcopy(obom))
    errors = _policy_check(filtered)
    declared_digest = filtered.get("digest")
    payload = dict(filtered)
    payload.pop("digest", None)
    computed_digest = _digest(payload)
    digest_ok = declared_digest in {None, computed_digest}
    if not digest_ok:
        errors.append("digest_mismatch")
    return {
        "schema": SCHEMA,
        "verified": not errors,
        "integrity": digest_ok,
        "policy_conformant": not any(e in errors for e in _policy_check(filtered)),
        "digest": computed_digest,
        "errors": errors,
        "artifact": filtered,
    }

def certify_a2_obom(obom: dict[str, Any], *, data: Any, ontology: Any,
                    shacl: Any, policy: Any, user_confirmation: bool = False) -> dict[str, Any]:
    """Certify only after explicit user confirmation, then re-verify."""
    if not user_confirmation:
        raise A2OBOMAuditError("explicit_user_confirmation_required_before_certification")
    candidate = deepcopy(obom)
    candidate["schema"] = SCHEMA
    candidate["data"] = data
    candidate["ontology"] = ontology
    candidate["shacl"] = shacl
    candidate["policy"] = policy
    candidate.pop("digest", None)
    candidate["digest"] = _digest(candidate)
    result = verify_a2_obom(candidate)
    result["certified_candidate"] = True
    return result
