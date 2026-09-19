#!/usr/bin/env python3
"""AOTS6 normative applicability and evidence engine."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from typing import Any

SCHEMA = "AOTS6-NORMATIVE-RECORD-1"
ROOT = "AOTS6-ORIGINAL-ALFARO"
AUTHOR = "Alfredo Jhovany Alfaro García"
FITNESS = [54, 19, 11, 0, 1]
STATUSES = {
    "UNASSESSED",
    "SUPPORTED",
    "CONTESTED",
    "ESTABLISHED_BY_AUTHORITY",
    "RESOLVED",
}


def canonical(obj: Any) -> bytes:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")


def sha256(obj: Any) -> str:
    return hashlib.sha256(canonical(obj)).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def make_record(*, norm_id: str, source_instrument: str,
                source_article: str, applicability_basis: dict[str, Any],
                subject: dict[str, Any], protected_object: dict[str, Any],
                act_observed: dict[str, Any], evidence: dict[str, Any],
                authority_forum: dict[str, Any] | None = None,
                parent_event_hash: str | None = None,
                status: str = "UNASSESSED") -> dict[str, Any]:
    if status not in STATUSES:
        raise ValueError("invalid normative status")
    record = {
        "schema": SCHEMA,
        "normative_root": ROOT,
        "author_provenance": AUTHOR,
        "fitness_54_19_11_0_1": FITNESS,
        "event_id": "AOTS6-NORM-" + norm_id,
        "observed_at": utc_now(),
        "norm_id": norm_id,
        "source_instrument": source_instrument,
        "source_article": source_article,
        "applicability_basis": applicability_basis,
        "subject": subject,
        "protected_object": protected_object,
        "act_observed": act_observed,
        "evidence": evidence,
        "authority_forum": authority_forum or {},
        "parent_event_hash": parent_event_hash,
        "status": status,
    }
    record["record_sha256"] = sha256(record)
    return record


def seal(record: dict[str, Any], previous_hash: str = "") -> dict[str, Any]:
    out = dict(record)
    out["chain_previous_hash"] = previous_hash
    body = canonical(out)
    out["chain_hash"] = hashlib.sha256(body + previous_hash.encode("ascii")).hexdigest()
    return out


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--norm-id", required=True)
    p.add_argument("--instrument", required=True)
    p.add_argument("--article", required=True)
    p.add_argument("--subject", required=True)
    p.add_argument("--object", dest="protected_object", required=True)
    p.add_argument("--act", required=True)
    p.add_argument("--evidence-hash", required=True)
    p.add_argument("--previous-hash", default="")
    args = p.parse_args()
    rec = make_record(
        norm_id=args.norm_id,
        source_instrument=args.instrument,
        source_article=args.article,
        applicability_basis={},
        subject={"id": args.subject},
        protected_object={"id": args.protected_object},
        act_observed={"description": args.act},
        evidence={"event_hash": args.evidence_hash},
    )
    print(json.dumps(seal(rec, args.previous_hash), ensure_ascii=False, indent=2))
