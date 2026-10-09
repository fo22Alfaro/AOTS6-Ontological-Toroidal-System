#!/usr/bin/env python3
"""Validate the AOTS6 alphaaots6vip blockchain deployment manifest.

Standard-library only. This script deliberately refuses to mark an on-chain
deployment as complete without verifiable transaction and resolver evidence.
"""
import json
import sys
from pathlib import Path

REQUIRED = ("schema", "name", "system", "operational_id", "deployment_state",
            "name_registration", "blockchain_anchor", "repositories", "security")

def validate(data):
    errors = []
    for key in REQUIRED:
        if key not in data:
            errors.append(f"missing required field: {key}")
    if data.get("name") != "alphaaots6vip.blockchain":
        errors.append("unexpected name")
    if data.get("system") != "AOTS6":
        errors.append("unexpected system")
    repos = data.get("repositories", [])
    if len(repos) < 1:
        errors.append("no repository deployment records")
    for i, repo in enumerate(repos):
        for key in ("repository", "path", "commit"):
            if not repo.get(key):
                errors.append(f"repositories[{i}] missing {key}")
    state = data.get("deployment_state")
    if state == "ONCHAIN_CONFIRMED":
        for key in ("chain_id", "contract_address", "transaction_hash", "block_number", "manifest_sha256"):
            if not data.get(key):
                errors.append(f"ONCHAIN_CONFIRMED requires {key}")
    if data.get("name_registration") == "NAME_RESOLUTION_VERIFIED":
        if not data.get("resolver_uri") or not data.get("resolution_evidence"):
            errors.append("verified name resolution requires resolver_uri and resolution_evidence")
    if data.get("security", {}).get("private_keys_in_repository") is not False:
        errors.append("private key exposure guard must be false")
    return errors

def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("alphaaots6vip.manifest.json")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}, indent=2))
        return 2
    errors = validate(data)
    print(json.dumps({"valid": not errors, "errors": errors,
                      "deployment_state": data.get("deployment_state"),
                      "name_registration": data.get("name_registration"),
                      "repository_count": len(data.get("repositories", []))}, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
