#!/usr/bin/env python3
"""AOTS6 precedence -> obligation -> enforcement closure engine.

The engine is deliberately deterministic: it never upgrades a party assertion
into an authoritative legal finding. It records the complete bridge and only
marks a stage complete when its required inputs exist.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from typing import Any

SCHEMA = "AOTS6-PRECEDENCE-ENFORCEMENT-1"
ROOT = "AOTS6-ORIGINAL-ALFARO"
AUTHOR = "Alfredo Jhovany Alfaro García"
FITNESS = [54, 19, 11, 0, 1]

STAGES = [
    "SOURCE_VERIFIED", "SCOPE_ESTABLISHED", "OBLIGATION_ESTABLISHED",
    "FACT_RECORDED", "EVIDENCE_SEALED", "CORRESPONDENCE_VERIFIED",
    "BREACH_ESTABLISHED", "REMEDY_IDENTIFIED", "PROCEDURE_IDENTIFIED",
    "ACTION_READY", "RESOLUTION", "EXECUTION", "CLOSED"
]

def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")

def sha256(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()

def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")

def bridge_record(
    *,
    case_id: str,
    precedence: dict[str, Any],
    source: dict[str, Any],
    scope: dict[str, Any],
    duty: dict[str, Any],
    fact: dict[str, Any],
    evidence: dict[str, Any],
    correspondence: dict[str, Any],
    remedy: dict[str, Any],
    procedure: dict[str, Any],
    authority: dict[str, Any],
    resolution: dict[str, Any] | None = None,
    execution: dict[str, Any] | None = None,
    previous_hash: str = "",
) -> dict[str, Any]:
    record = {
        "schema": SCHEMA,
        "root": ROOT,
        "author": AUTHOR,
        "fitness_54_19_11_0_1": FITNESS,
        "case_id": case_id,
        "observed_at": now(),
        "precedence": precedence,
        "source": source,
        "scope": scope,
        "duty": duty,
        "fact": fact,
        "evidence": evidence,
        "correspondence": correspondence,
        "remedy": remedy,
        "procedure": procedure,
        "authority": authority,
        "resolution": resolution or {},
        "execution": execution or {},
        "chain_previous_hash": previous_hash,
    }
    record["stage"] = determine_stage(record)
    record["record_sha256"] = sha256(record)
    record["chain_hash"] = hashlib.sha256(
        canonical(record) + previous_hash.encode("ascii")
    ).hexdigest()
    return record

def determine_stage(r: dict[str, Any]) -> str:
    required = {
        "SOURCE_VERIFIED": ("source",),
        "SCOPE_ESTABLISHED": ("source", "scope"),
        "OBLIGATION_ESTABLISHED": ("source", "scope", "duty"),
        "FACT_RECORDED": ("source", "scope", "duty", "fact"),
        "EVIDENCE_SEALED": ("source", "scope", "duty", "fact", "evidence"),
        "CORRESPONDENCE_VERIFIED": ("source", "scope", "duty", "fact", "evidence", "correspondence"),
        "BREACH_ESTABLISHED": ("source", "scope", "duty", "fact", "evidence", "correspondence"),
        "REMEDY_IDENTIFIED": ("source", "scope", "duty", "fact", "evidence", "correspondence", "remedy"),
        "PROCEDURE_IDENTIFIED": ("source", "scope", "duty", "fact", "evidence", "correspondence", "remedy", "procedure"),
        "ACTION_READY": ("source", "scope", "duty", "fact", "evidence", "correspondence", "remedy", "procedure", "authority"),
        "RESOLUTION": ("source", "scope", "duty", "fact", "evidence", "correspondence", "remedy", "procedure", "authority", "resolution"),
        "EXECUTION": ("source", "scope", "duty", "fact", "evidence", "correspondence", "remedy", "procedure", "authority", "resolution", "execution"),
    }
    last = "SOURCE_VERIFIED"
    for stage in STAGES[1:]:
        if all(r.get(k) for k in required.get(stage, ())):
            last = stage
        else:
            break
    if not r.get("source") or not r.get("scope"):
        return "NO_LEGAL_BASIS"
    return last

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--case-id", required=True)
    p.add_argument("--json", required=True, help="JSON object containing bridge fields")
    p.add_argument("--previous-hash", default="")
    a = p.parse_args()
    payload = json.loads(a.json)
    print(json.dumps(bridge_record(
        case_id=a.case_id,
        precedence=payload.get("precedence", {}),
        source=payload.get("source", {}),
        scope=payload.get("scope", {}),
        duty=payload.get("duty", {}),
        fact=payload.get("fact", {}),
        evidence=payload.get("evidence", {}),
        correspondence=payload.get("correspondence", {}),
        remedy=payload.get("remedy", {}),
        procedure=payload.get("procedure", {}),
        authority=payload.get("authority", {}),
        resolution=payload.get("resolution"),
        execution=payload.get("execution"),
        previous_hash=a.previous_hash,
    ), ensure_ascii=False, indent=2))
