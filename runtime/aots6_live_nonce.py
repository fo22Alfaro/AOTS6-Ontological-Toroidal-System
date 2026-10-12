#!/usr/bin/env python3
"""Generate an AOTS6 live audit nonce and an artifact-bound SHA-256 manifest.

This is a provenance/audit challenge, NOT an Ethereum account nonce or Bitcoin
block-header nonce. It never signs or broadcasts transactions.
"""
import argparse
import hashlib
import json
import secrets
from datetime import datetime, timezone
from pathlib import Path

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--artifact", required=True, type=Path)
    p.add_argument("--asset-id", required=True)
    p.add_argument("--version", required=True)
    p.add_argument("--topological-parameters-json", required=True,
                   help="Explicit JSON object of versioned parameters; do not leave undefined.")
    p.add_argument("--output", required=True, type=Path)
    args = p.parse_args()
    raw = args.artifact.read_bytes()
    try:
        params = json.loads(args.topological_parameters_json)
    except json.JSONDecodeError as exc:
        p.error(f"invalid topological parameters JSON: {exc}")
    if not isinstance(params, dict) or not params:
        p.error("topological parameters must be a non-empty JSON object")
    record = {
        "schema": "AOTS6-LIVE-ARTIFACT-NONCE-1.0",
        "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "asset_id": args.asset_id,
        "artifact_version": args.version,
        "artifact_sha256": hashlib.sha256(raw).hexdigest(),
        "nonce_scope": "AOTS6_AUDIT_CHALLENGE_NOT_CHAIN_TRANSACTION_NONCE",
        "nonce_algorithm": "CSPRNG-256",
        "nonce_hex": secrets.token_hex(32),
        "topological_parameters": params,
        "hilbert_structure": "NESTED_HILBERT_SPACE_LEVEL_2",
        "majorana_state": "DECLARED_MODEL_STATE_NOT_PHYSICAL_EVIDENCE",
        "onchain_anchor": None,
        "transaction_authorization": None,
    }
    record["manifest_sha256"] = hashlib.sha256(canonical(record)).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "GENERATED",
        "asset_id": args.asset_id,
        "artifact_sha256": record["artifact_sha256"],
        "nonce_hex": record["nonce_hex"],
        "manifest_sha256": record["manifest_sha256"],
        "onchain_anchor": None
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
