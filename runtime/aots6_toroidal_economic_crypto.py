#!/usr/bin/env python3
"""AOTS⁶ local economic/provenance ledger; Python standard library only.

This is a tamper-evident local audit log, not a blockchain, wallet, payment rail,
or proof that an economic claim is true. Never put secrets in the ledger.
"""
from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import sys
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

GENESIS = "0" * 64
HMAC_ENV = "AOTS6_LEDGER_HMAC_KEY"
REQUIRED = {
    "sequence", "timestamp_utc", "actor", "event_type", "asset_id",
    "amount", "unit", "source_ref", "evidence_ref", "previous_hash",
    "event_hash",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def canonical(value: dict[str, Any]) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def digest_event(event: dict[str, Any]) -> str:
    body = {k: v for k, v in event.items() if k not in {"event_hash", "hmac_sha256"}}
    return hashlib.sha256(canonical(body)).hexdigest()


def hmac_for(event_hash: str) -> str | None:
    key = os.environ.get(HMAC_ENV)
    if not key:
        return None
    return hmac.new(key.encode("utf-8"), event_hash.encode("ascii"), hashlib.sha256).hexdigest()


def read_rows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"JSON inválido en línea {number}: {exc}") from exc
        if not isinstance(item, dict):
            raise ValueError(f"La línea {number} no contiene un objeto JSON")
        rows.append(item)
    return rows


def verify_rows(rows: list[dict[str, Any]]) -> tuple[bool, str]:
    previous = GENESIS
    hmac_key_present = bool(os.environ.get(HMAC_ENV))
    for expected_seq, event in enumerate(rows, 1):
        missing = REQUIRED - set(event)
        if missing:
            return False, f"Evento {expected_seq}: faltan campos {sorted(missing)}"
        if event["sequence"] != expected_seq:
            return False, f"Secuencia inválida en evento {expected_seq}"
        if event["previous_hash"] != previous:
            return False, f"previous_hash no coincide en evento {expected_seq}"
        actual = digest_event(event)
        if not hmac.compare_digest(str(event["event_hash"]), actual):
            return False, f"event_hash no coincide en evento {expected_seq}"
        stored_mac = event.get("hmac_sha256")
        if stored_mac is not None:
            expected_mac = hmac_for(actual)
            if expected_mac is None:
                return False, f"Evento {expected_seq} requiere AOTS6_LEDGER_HMAC_KEY"
            if not hmac.compare_digest(str(stored_mac), expected_mac):
                return False, f"HMAC inválido en evento {expected_seq}"
        elif hmac_key_present:
            return False, f"Evento {expected_seq} no tiene HMAC; verifique configuración de clave"
        previous = actual
    return True, f"OK: {len(rows)} eventos verificados; último hash={previous}"


def cmd_init(path: Path) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)
    ok, message = verify_rows(read_rows(path))
    print(json.dumps({"status": "INITIALIZED" if ok else "INVALID", "ledger": str(path), "verification": message}, ensure_ascii=False))
    return 0 if ok else 2


def cmd_append(args: argparse.Namespace) -> int:
    path: Path = args.ledger
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = read_rows(path)
    ok, message = verify_rows(rows)
    if not ok:
        print(f"ERROR: el registro existente no pasa verificación: {message}", file=sys.stderr)
        return 2
    try:
        amount = str(Decimal(args.amount))
    except InvalidOperation:
        print("ERROR: --amount debe ser un número decimal válido", file=sys.stderr)
        return 2
    if not all([args.actor.strip(), args.type.strip(), args.asset_id.strip(), args.unit.strip(), args.source_ref.strip(), args.evidence_ref.strip()]):
        print("ERROR: los campos de texto no pueden estar vacíos", file=sys.stderr)
        return 2
    event: dict[str, Any] = {
        "sequence": len(rows) + 1,
        "timestamp_utc": utc_now(),
        "actor": args.actor,
        "event_type": args.type,
        "asset_id": args.asset_id,
        "amount": amount,
        "unit": args.unit,
        "source_ref": args.source_ref,
        "evidence_ref": args.evidence_ref,
        "previous_hash": rows[-1]["event_hash"] if rows else GENESIS,
    }
    event["event_hash"] = digest_event(event)
    mac = hmac_for(event["event_hash"])
    if mac:
        event["hmac_sha256"] = mac
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "APPENDED", "sequence": event["sequence"], "event_hash": event["event_hash"], "hmac_enabled": mac is not None}, ensure_ascii=False))
    return 0


def cmd_verify(path: Path) -> int:
    try:
        ok, message = verify_rows(read_rows(path))
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "INVALID", "error": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps({"status": "VERIFIED" if ok else "INVALID", "ledger": str(path), "verification": message}, ensure_ascii=False))
    return 0 if ok else 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    init_p = sub.add_parser("init", help="crear el registro si no existe y verificarlo")
    init_p.add_argument("--ledger", type=Path, required=True)
    append_p = sub.add_parser("append", help="agregar un evento económico/procedencia")
    append_p.add_argument("--ledger", type=Path, required=True)
    append_p.add_argument("--actor", required=True)
    append_p.add_argument("--type", required=True)
    append_p.add_argument("--asset-id", required=True)
    append_p.add_argument("--amount", required=True)
    append_p.add_argument("--unit", required=True)
    append_p.add_argument("--source-ref", required=True)
    append_p.add_argument("--evidence-ref", required=True)
    verify_p = sub.add_parser("verify", help="verificar secuencia y hashes")
    verify_p.add_argument("--ledger", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "init":
        return cmd_init(args.ledger)
    if args.command == "append":
        return cmd_append(args)
    return cmd_verify(args.ledger)


if __name__ == "__main__":
    raise SystemExit(main())
