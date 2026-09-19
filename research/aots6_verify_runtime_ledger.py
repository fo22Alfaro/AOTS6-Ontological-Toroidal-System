#!/usr/bin/env python3
"""Verify AOTS6 runtime ledger hash-chain and quantum metadata invariants."""
from __future__ import annotations
import hashlib,json,math,sys
from pathlib import Path

def sha256(b:bytes)->str: return hashlib.sha256(b).hexdigest()
def canonical_event_body(e):
    return {k:e[k] for k in e if k!="event_hash"}

def verify(path):
    lines=[x for x in Path(path).read_text(encoding="utf-8").splitlines() if x.strip()]
    previous="0"*64; errors=[]; quantum_events=0
    for i,line in enumerate(lines):
        try: e=json.loads(line)
        except Exception as ex:
            errors.append(f"line {i+1}: invalid JSON: {ex}"); continue
        if e.get("sequence")!=i: errors.append(f"line {i+1}: sequence={e.get('sequence')} expected={i}")
        if e.get("previous_event_hash")!=previous:
            errors.append(f"line {i+1}: previous_event_hash mismatch")
        expected=sha256(json.dumps(canonical_event_body(e),ensure_ascii=False,sort_keys=True,separators=(",",":")).encode())
        if e.get("event_hash")!=expected: errors.append(f"line {i+1}: event_hash mismatch")
        q=e.get("quantum_state_metadata")
        if q:
            quantum_events+=1
            if q.get("partition_count")!=31: errors.append(f"line {i+1}: partition_count != 31")
            if q.get("hilbert_dimension")!=64: errors.append(f"line {i+1}: hilbert_dimension != 64")
            if len(q.get("bipartition_signature_31",[]))!=31: errors.append(f"line {i+1}: signature length != 31")
            if len(q.get("QFI",{}).get("matrix",[]))!=6: errors.append(f"line {i+1}: QFI dimension != 6")
            if abs(q.get("QFI",{}).get("diagonal_value",0)-4*math.pi**2)>1e-12:
                errors.append(f"line {i+1}: QFI diagonal mismatch")
        previous=e.get("event_hash","")
    return {"valid":not errors,"events":len(lines),"quantum_events":quantum_events,"errors":errors}

if __name__=="__main__":
    result=verify(sys.argv[1] if len(sys.argv)>1 else "aots6_runtime_ledger.jsonl")
    print(json.dumps(result,ensure_ascii=False,indent=2))
    raise SystemExit(0 if result["valid"] else 1)
