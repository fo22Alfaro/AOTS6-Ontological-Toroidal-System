#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path

STATES={"CATALOG_ONLY","ACQUIRED","HASHED","LOCATED","EXTRACTED","CORROBORATED","CONTESTED","NO_DETERMINADO"}

def digest_bytes(path):
    b=Path(path).read_bytes()
    return hashlib.sha256(b).hexdigest(),len(b)

def instantiate(record, object_path=None):
    errors=[]
    for k in ("record_id","object_id","state","access","provenance","integrity","governance"):
        if k not in record: errors.append("missing:"+k)
    if record.get("state") not in STATES: errors.append("invalid:state")
    if record.get("state") in {"HASHED","LOCATED","EXTRACTED","CORROBORATED"}:
        sha=record.get("integrity",{}).get("sha256","")
        if len(sha)!=64: errors.append("hashed_state_requires_sha256")
    if object_path:
        sha,n=digest_bytes(object_path)
        expected=record.get("integrity",{}).get("sha256","").lower()
        if sha.lower()!=expected: errors.append("hash_mismatch")
        if record.get("integrity",{}).get("byte_length") not in (None,n): errors.append("byte_length_mismatch")
    r=record.get("restriction")
    if r and r.get("status")=="VERIFIED" and (not r.get("legal_basis") or not r.get("official_source")):
        errors.append("verified_restriction_without_basis")
    return errors

def main():
    p=argparse.ArgumentParser()
    p.add_argument("record")
    p.add_argument("--object")
    a=p.parse_args()
    record=json.loads(Path(a.record).read_text(encoding="utf-8"))
    errors=instantiate(record,a.object)
    print(json.dumps({"valid":not errors,"record_id":record.get("record_id"),"state":record.get("state"),"errors":errors},ensure_ascii=False,indent=2))
    return 0 if errors else 0
if __name__=="__main__": raise SystemExit(main())
