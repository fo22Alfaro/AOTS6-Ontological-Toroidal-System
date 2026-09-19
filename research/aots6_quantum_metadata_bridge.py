#!/usr/bin/env python3
"""AOTS6 real-time quantum-state metadata bridge.

Consumes JSONL events containing token/state observations and enriches each event
with the AOTS6 six-qubit state metrics: pairwise fidelity F_rs, Fubini-Study
distance d_FS, subsystem entropy S_A, mutual information I(A:B), QFI, and the
31-bipartition entropy signature.

The quantum state is constructed exactly from the AOTS6 encoding:
alphabet size 36, modulus 37, primes (2,3,5,7,11,13), H^6, local RZ phases,
and the fixed six-CX ring. Numerical state evolution uses dense NumPy arrays.
"""
from __future__ import annotations
import json, math, sys
from pathlib import Path
import numpy as np

ALPHABET="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PRIMES=(2,3,5,7,11,13)
MODULUS=37
N=6
PARTITIONS=[]
for mask in range(1, (1<<N)-1):
    A=tuple(i for i in range(N) if mask>>i&1)
    B=tuple(i for i in range(N) if not(mask>>i&1))
    if len(A)<=len(B):
        PARTITIONS.append((A,B))
PARTITIONS=PARTITIONS[:31]

def ring_perm():
    p=np.arange(64)
    for c,t in ((0,1),(1,2),(2,3),(3,4),(4,5),(5,0)):
        q=np.array(p,copy=True)
        for x in range(64):
            bit=(x>>c)&1
            if bit: q[x]=p[x^(1<<t)]
        p=q
    return p

RING=ring_perm()

def token_index(token):
    if isinstance(token,int): return token
    s=str(token).upper()
    if s not in ALPHABET: raise ValueError("token must be one AOTS6 alphabet symbol")
    return ALPHABET.index(s)

def state(token):
    k=token_index(token); r=k+1
    phi=((r*np.array(PRIMES))%MODULUS)/MODULUS
    a=np.exp(1j*np.pi*phi)/math.sqrt(2)
    b=np.exp(-1j*np.pi*phi)/math.sqrt(2)
    psi=np.array([1.+0j])
    for i in range(N): psi=np.kron(psi, np.array([a[i],b[i]]))
    return psi[RING], phi

def entropy(rho):
    ev=np.linalg.eigvalsh((rho+rho.conj().T)/2)
    ev=ev[ev>1e-14]
    return float(-np.sum(ev*np.log2(ev)))

def reduced(psi,A):
    A=tuple(A); B=tuple(i for i in range(N) if i not in A)
    arr=psi.reshape([2]*N)
    axes=A+B
    arr=np.transpose(arr,axes)
    da=2**len(A); db=2**len(B)
    mat=arr.reshape(da,db)
    return mat@mat.conj().T

def signature(psi):
    return [entropy(reduced(psi,A)) for A,_ in PARTITIONS]

def metrics(token, references=()):
    psi,phi=state(token)
    sig=signature(psi)
    # For a pure global state, I(A:B)=2 S(A).
    S012=entropy(reduced(psi,(0,1,2)))
    MI=2*S012
    # Product-state phase parameters: QFI = 4*pi^2 I_6.
    qfi_diag=[4*math.pi**2]*N
    qfi_off=[[0.0 if i!=j else qfi_diag[i] for j in range(N)] for i in range(N)]
    refs={}
    for ref in references:
        pr,_=state(ref)
        overlap=np.vdot(pr,psi)
        F=float(abs(overlap)**2)
        F=max(0.0,min(1.0,F))
        refs[str(ref)]={"F_rs":F,"d_FS":math.acos(math.sqrt(F))}
    return {
        "token":ALPHABET[token_index(token)],
        "r":token_index(token)+1,
        "phi":phi.tolist(),
        "F_rs":refs,
        "d_FS":{k:v["d_FS"] for k,v in refs.items()},
        "S_A":{"partition_012|345":S012},
        "I_A_B":{"partition_012|345":MI},
        "QFI":{"diagonal":qfi_diag,"off_diagonal":qfi_off},
        "bipartition_signature_31":[
            {"A":list(A),"B":list(B),"S_A_bits":s}
            for (A,B),s in zip(PARTITIONS,sig)
        ]
    }

def enrich_event(event):
    token=event.get("token",event.get("metadata",{}).get("token"))
    if token is None: return event
    refs=event.get("reference_tokens",[])
    event["quantum_state_metadata"]=metrics(token,refs)
    event["quantum_state_metadata"]["partition_count"]=len(PARTITIONS)
    event["quantum_state_metadata"]["hilbert_dimension"]=64
    event["quantum_state_metadata"]["ring_cx_count"]=6
    return event

def main():
    for line in sys.stdin:
        if not line.strip(): continue
        event=json.loads(line)
        print(json.dumps(enrich_event(event),ensure_ascii=False,sort_keys=True))

if __name__=="__main__": main()
