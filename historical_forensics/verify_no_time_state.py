#!/usr/bin/env python3
"""AOTS6 verifier for evidence-first no-time state records."""
import argparse,json,hashlib,sys
from pathlib import Path

def hex64(s):
    return isinstance(s,str) and len(s)==64 and all(c in "0123456789abcdefABCDEF" for c in s)

def verify(record, objects=None):
    errors=[]
    for k in ("object_id","state","source","integrity","locator","provenance"):
        if k not in record: errors.append("missing:"+k)
    if errors: return errors
    if not hex64(record["integrity"].get("sha256")): errors.append("invalid:sha256")
    if not record["source"].get("institution") or not record["source"].get("reference"): errors.append("incomplete:source")
    if not record["locator"].get("value"): errors.append("incomplete:locator")
    for i,p in enumerate(record.get("provenance",[])):
        if not p.get("operation") or not p.get("input") or not p.get("output"): errors.append(f"incomplete:provenance:{i}")
    if objects and not errors:
        path=Path(objects)/record["object_id"]
        if not path.exists(): errors.append("object_not_found")
        else:
            digest=hashlib.sha256(path.read_bytes()).hexdigest()
            if digest.lower()!=record["integrity"]["sha256"].lower(): errors.append("hash_mismatch")
    if record.get("state") in {"EXTRACTED","CORROBORATED"} and "literal" not in record: errors.append("literal_required")
    r=record.get("restriction")
    if r and r.get("status")=="VERIFIED" and (not r.get("legal_basis") or not r.get("official_source")):
        errors.append("verified_restriction_without_basis")
    return errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--objects")
    a=ap.parse_args()
    data=json.loads(Path(a.file).read_text(encoding="utf-8"))
    errs=verify(data,a.objects)
    print(json.dumps({"valid":not errs,"object_id":data.get("object_id"),"state":data.get("state"),"errors":errs},ensure_ascii=False,indent=2))
    return 0 if not errs else 1

if __name__=="__main__":
    sys.exit(main())
