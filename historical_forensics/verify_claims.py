#!/usr/bin/env python3
"""AOTS6 forensic claim provenance gate.

Verifies that claims do not overstate their evidence:
- REPRODUCIBLE requires an acquired object, real SHA-256, and exact locator.
- PARCIALMENTE_REPRODUCIBLE may reference a catalog/description without a local object.
- DOCUMENTADO/CORROBORADO cannot carry a placeholder hash when marked reproducible.
- hashes are checked against local evidence files when present.

This verifier never treats a hash as proof of historical truth, ownership, authorship,
causality, or legal title. It only verifies provenance/integrity relationships.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

PLACEHOLDERS={"","PENDIENTE_DE_CAPTURA","PENDIENTE","UNKNOWN","N/A","null","None"}

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()

def load_jsonl(path: Path):
    for n,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try: yield n,json.loads(line)
        except json.JSONDecodeError as e: raise ValueError(f"linea {n}: JSON invalido: {e}")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("claims",type=Path)
    ap.add_argument("--objects",type=Path,default=None)
    args=ap.parse_args()
    errors=[]; checked=0
    objects=args.objects.resolve() if args.objects else None
    for n,c in load_jsonl(args.claims):
        checked+=1
        cid=c.get("claim_id",f"line-{n}")
        src=c.get("source",{})
        ev=c.get("evidence",{})
        if not all(src.get(k) for k in ("institution","reference","url","accessed_at")):
            errors.append(f"{cid}: fuente incompleta")
        if not all(ev.get(k) for k in ("object_id","sha256","locator")):
            errors.append(f"{cid}: evidencia incompleta")
            continue
        h=str(ev["sha256"])
        repro=c.get("reproducibility")
        if repro=="REPRODUCIBLE":
            if h.upper() in PLACEHOLDERS or len(h)!=64:
                errors.append(f"{cid}: REPRODUCIBLE exige SHA-256 real")
            if not ev["locator"].strip():
                errors.append(f"{cid}: REPRODUCIBLE exige locator exacto")
            if objects:
                candidate=objects / ev["object_id"]
                if not candidate.is_file():
                    errors.append(f"{cid}: objeto local ausente: {candidate}")
                elif sha256(candidate).lower()!=h.lower():
                    errors.append(f"{cid}: SHA-256 no coincide con objeto")
        if h.upper() in PLACEHOLDERS and repro=="REPRODUCIBLE":
            errors.append(f"{cid}: hash provisional incompatible con REPRODUCIBLE")
        if c.get("epistemic_state")=="CORROBORADO" and not c.get("corroboration"):
            errors.append(f"{cid}: CORROBORADO exige corroboration")
    result={"valid":not errors,"claims_checked":checked,"errors":errors,
            "policy":"provenance/integrity only; no hash is historical truth"}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if not errors else 1

if __name__=="__main__":
    raise SystemExit(main())
