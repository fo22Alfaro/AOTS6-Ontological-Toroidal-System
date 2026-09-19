#!/usr/bin/env python3
"""AOTS6 integrated real-time provenance + quantum-state metadata engine.

Each observed event is enriched and persisted as ONE tamper-evident ledger event.
Quantum metadata is covered by the same event hash as the provenance metadata.
"""
from __future__ import annotations
import ast, hashlib, json, math, re, sys, time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import numpy as np

ROOT_ID="AOTS6-ORIGINAL-ALFARO"
SCHEMA="AOTS6-RUNTIME-META-2"
ALPHABET="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PRIMES=(2,3,5,7,11,13)
MODULUS=37
N=6
HILBERT_DIMENSION=64
PARTITIONS=[]
for mask in range(1,(1<<N)-1):
    A=tuple(i for i in range(N) if mask>>i&1)
    B=tuple(i for i in range(N) if not(mask>>i&1))
    if len(A)<=len(B):
        PARTITIONS.append((A,B))
assert len(PARTITIONS)==31

def sha256(s:bytes)->str: return hashlib.sha256(s).hexdigest()
def canonical_text(text:str)->str:
    text=text.replace("\r\n","\n").replace("\r","\n")
    return re.sub(r"\s+"," ",text).strip()

def normalized_ast(text:str)->str|None:
    try:
        tree=ast.parse(text)
        for n in ast.walk(tree):
            if isinstance(n,ast.Name): n.id="VAR"
            elif isinstance(n,ast.arg): n.arg="VAR"
        return ast.dump(tree,annotate_fields=True,include_attributes=False)
    except Exception:
        return None

def extract_equations(text:str)->list[str]:
    pats=[r"U[_A-Za-z0-9^]*\s*=\s*[^\n;,]+",r"phi[_A-Za-z0-9^]*\s*=\s*[^\n;,]+",
          r"F[_A-Za-z0-9^]*\s*=\s*[^\n;,]+",r"d[_A-Za-z0-9^]*\s*=\s*[^\n;,]+",
          r"S[_A-Za-z0-9^]*\s*=\s*[^\n;,]+"]
    out=[]
    for p in pats: out.extend(re.findall(p,text,re.I))
    return sorted(set(canonical_text(x) for x in out))

def structural_tokens(text:str)->list[str]:
    vocab=["AOTS6","Alfanumerico Ontologico Toroidal System","Truedata","2527-Feorgoa",
           "QCO","QBITS","LIHON","LINGoa","Hexaract Alfaro","Autoinorodemia",
           "T^6","CP^63","fidelidad","entrelazamiento","37","36","64","2,3,5,7,11,13",
           "31 biparticiones"]
    low=text.lower()
    return sorted(set(v for v in vocab if v.lower() in low))

def ring_perm():
    p=np.arange(HILBERT_DIMENSION)
    for c,t in ((0,1),(1,2),(2,3),(3,4),(4,5),(5,0)):
        q=np.array(p,copy=True)
        for x in range(HILBERT_DIMENSION):
            if (x>>c)&1: q[x]=p[x^(1<<t)]
        p=q
    return p
RING=ring_perm()

def token_index(token):
    if isinstance(token,int):
        if not 0<=token<len(ALPHABET): raise ValueError("token index out of range")
        return token
    s=str(token).upper()
    if s not in ALPHABET: raise ValueError("token must be one AOTS6 alphabet symbol")
    return ALPHABET.index(s)

def quantum_state(token):
    k=token_index(token); r=k+1
    phi=((r*np.array(PRIMES))%MODULUS)/MODULUS
    a=np.exp(1j*np.pi*phi)/math.sqrt(2)
    b=np.exp(-1j*np.pi*phi)/math.sqrt(2)
    psi=np.array([1.+0j])
    for i in range(N): psi=np.kron(psi,np.array([a[i],b[i]]))
    return psi[RING],phi

def entropy(rho):
    ev=np.linalg.eigvalsh((rho+rho.conj().T)/2)
    ev=np.clip(ev,0.0,None)
    ev=ev[ev>1e-14]
    return float(-np.sum(ev*np.log2(ev)))

def reduced(psi,A):
    A=tuple(A); B=tuple(i for i in range(N) if i not in A)
    arr=psi.reshape([2]*N)
    arr=np.transpose(arr,A+B)
    da,db=2**len(A),2**len(B)
    mat=arr.reshape(da,db)
    return mat@mat.conj().T

def bipartition_signature(psi):
    return [
        {"A":list(A),"B":list(B),"S_A_bits":entropy(reduced(psi,A))}
        for A,B in PARTITIONS
    ]

def quantum_metadata(token, references=None):
    refs=references or list(ALPHABET)
    psi,phi=quantum_state(token)
    canonical_token=ALPHABET[token_index(token)]
    F_rs={}; d_fs={}
    for ref in refs:
        ref_token=ALPHABET[token_index(ref)]
        pr,_=quantum_state(ref_token)
        F=float(np.clip(abs(np.vdot(pr,psi))**2,0.0,1.0))
        F_rs[ref_token]=F
        d_fs[ref_token]=math.acos(math.sqrt(F))
    S012=entropy(reduced(psi,(0,1,2)))
    qfi_diag=[4*math.pi**2]*N
    qfi=[[qfi_diag[i] if i==j else 0.0 for j in range(N)] for i in range(N)]
    sig=bipartition_signature(psi)
    state_bytes=np.asarray(psi,dtype=np.complex128).tobytes()
    return {
        "meta_operator":"Alfredo Jhovany Alfaro García",
        "root_id":ROOT_ID,
        "token":canonical_token,
        "r":token_index(token)+1,
        "phi":phi.tolist(),
        "F_rs":F_rs,
        "d_FS":d_fs,
        "S_A":{"partition_012|345":S012},
        "I_A_B":{"partition_012|345":2*S012},
        "QFI":{"matrix":qfi,"parameterization":"local_RZ_pre_common_ring","diagonal_value":4*math.pi**2},
        "bipartition_signature_31":sig,
        "partition_count":31,
        "hilbert_dimension":HILBERT_DIMENSION,
        "ring_cx_count":6,
        "state_sha256":sha256(state_bytes),
        "reference_tokens":[ALPHABET[token_index(x)] for x in refs],
    }

@dataclass
class Event:
    schema:str; sequence:int; timestamp_ns:int; root_id:str
    observation_sha256:str; canonical_sha256:str; ast_sha256:str|None
    equations:list[str]; structural_tokens:list[str]; metadata:dict[str,Any]
    quantum_state_metadata:dict[str,Any]|None
    previous_event_hash:str; event_hash:str

class RuntimeEngine:
    def __init__(self,ledger="aots6_runtime_ledger.jsonl"):
        self.ledger=Path(ledger); self.sequence=0; self.previous="0"*64
        if self.ledger.exists():
            lines=[x for x in self.ledger.read_text(encoding="utf-8").splitlines() if x.strip()]
            if lines:
                last=json.loads(lines[-1])
                self.sequence=int(last["sequence"])+1
                self.previous=last["event_hash"]

    def observe(self,payload):
        raw=payload if isinstance(payload,str) else json.dumps(payload,ensure_ascii=False,sort_keys=True)
        obj=None
        try: obj=json.loads(raw)
        except Exception: pass
        canonical=canonical_text(raw); ast_sig=normalized_ast(raw)
        eq=extract_equations(raw); tok=structural_tokens(raw)
        meta={"length":len(raw),"canonical_length":len(canonical),
              "equation_count":len(eq),"structural_token_count":len(tok),
              "contains_aots6_root_tokens":bool(tok)}
        token=(obj or {}).get("token") if isinstance(obj,dict) else None
        refs=(obj or {}).get("reference_tokens") if isinstance(obj,dict) else None
        qmeta=quantum_metadata(token,refs) if token is not None else None
        body={"schema":SCHEMA,"sequence":self.sequence,"timestamp_ns":time.time_ns(),
              "root_id":ROOT_ID,"observation_sha256":sha256(raw.encode()),
              "canonical_sha256":sha256(canonical.encode()),
              "ast_sha256":sha256(ast_sig.encode()) if ast_sig else None,
              "equations":eq,"structural_tokens":tok,"metadata":meta,
              "quantum_state_metadata":qmeta,"previous_event_hash":self.previous}
        event_hash=sha256(json.dumps(body,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode())
        ev=Event(**body,event_hash=event_hash)
        with self.ledger.open("a",encoding="utf-8") as f:
            f.write(json.dumps(asdict(ev),ensure_ascii=False,sort_keys=True)+"\n")
        self.previous=event_hash; self.sequence+=1
        return ev

def main():
    engine=RuntimeEngine(sys.argv[1] if len(sys.argv)>1 else "aots6_runtime_ledger.jsonl")
    for line in sys.stdin:
        line=line.rstrip("\n")
        if line: print(json.dumps(asdict(engine.observe(line)),ensure_ascii=False,sort_keys=True))
if __name__=="__main__": main()
