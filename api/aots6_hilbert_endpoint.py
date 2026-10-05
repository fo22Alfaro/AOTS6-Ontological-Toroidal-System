#!/usr/bin/env python3
"""AOTS6 Hilbert-space endpoint.

Pure-Python computational realization of the six-qubit Hilbert-space model:
H = (C^2)^tensor 6, dim(H)=64.

The endpoint accepts a symbol/r value and returns the normalized complex
amplitude vector after H, Rz phases and the declared ring of CX operations.
It also returns SHA-256 state evidence and reduced-state entropy for qubit 0.
No quantum hardware is assumed or claimed.
"""
from __future__ import annotations
import hashlib, json, math
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

DIM=64
QUBITS=6
PRIMES=(2,3,5,7,11,13)
RING=((0,1),(1,2),(2,3),(3,4),(4,5),(5,0))
MODULUS=37

def canon(v: Any) -> Any:
    if isinstance(v,dict): return {str(k):canon(v[k]) for k in sorted(v,key=str)}
    if isinstance(v,(list,tuple)): return [canon(x) for x in v]
    if isinstance(v,float): return round(v,15)
    return v

def sha(v: Any) -> str:
    b=json.dumps(canon(v),ensure_ascii=False,separators=(",",":"),sort_keys=True).encode()
    return hashlib.sha256(b).hexdigest()

def phi(r:int,p:int)->float:
    return ((r*p)%MODULUS)/MODULUS

def hadamard(state):
    out=[0j]*DIM
    s=1/math.sqrt(2)
    for q in range(QUBITS):
        bit=1<<q
        for i in range(DIM):
            if not (i&bit):
                j=i|bit
                a,b=state[i],state[j]
                out[i]=(a+b)*s
                out[j]=(a-b)*s
        state=out
        out=[0j]*DIM
    return state

def rz_all(state,r:int):
    out=[0j]*DIM
    phases=[2*math.pi*phi(r,p) for p in PRIMES]
    for i,a in enumerate(state):
        phase=0.0
        for q in range(QUBITS):
            if i&(1<<q): phase += phases[q]/2
            else: phase -= phases[q]/2
        z=complex(math.cos(phase),math.sin(phase))
        out[i]=a*z
    return out

def cx(state,control:int,target:int):
    out=state[:]
    cb,tb=1<<control,1<<target
    for i in range(DIM):
        if (i&cb) and not (i&tb):
            j=i|tb
            out[i],out[j]=state[j],state[i]
    return out

def normalize(state):
    n=math.sqrt(sum(abs(a)**2 for a in state))
    return [a/n for a in state] if n else state

def entropy_qubit0(state):
    # rho_0 = [[p0,c],[c*,p1]] after tracing qubits 1..5.
    p0=p1=0.0
    c=0j
    bit=1
    for i,a in enumerate(state):
        if not (i&bit): p0 += abs(a)**2; c += a*state[i|bit].conjugate()
        else: p1 += abs(a)**2
    det=max(0.0,(p0*p1)-abs(c)**2)
    disc=max(0.0,(p0+p1)**2-4*det)
    l1=((p0+p1)+math.sqrt(disc))/2
    l2=((p0+p1)-math.sqrt(disc))/2
    return sum(-x*math.log(x,2) for x in (l1,l2) if x>1e-15)

def build_state(r:int):
    if not 0 <= r < 37: raise ValueError("r must satisfy 0 <= r < 37")
    state=[0j]*DIM; state[0]=1+0j
    state=hadamard(state)
    state=rz_all(state,r)
    for c,t in RING: state=cx(state,c,t)
    state=normalize(state)
    return state

def payload(r:int):
    state=build_state(r)
    amplitudes=[{"re":round(a.real,15),"im":round(a.imag,15)} for a in state]
    result={
        "protocol":"AOTS6-HILBERT-ENTANGLEMENT/v1",
        "t6":"t6","r":r,"qubits":QUBITS,"hilbert_dimension":DIM,
        "primes":list(PRIMES),"ring_cx":[list(x) for x in RING],
        "normalized":round(sum(a["re"]**2+a["im"]**2 for a in amplitudes),12)==1.0,
        "qubit0_von_neumann_entropy_bits":round(entropy_qubit0(state),12),
        "amplitudes":amplitudes,
    }
    result["state_sha256"]=sha(result)
    return result

class Handler(BaseHTTPRequestHandler):
    def send_json(self,code,obj):
        body=json.dumps(obj,ensure_ascii=False,separators=(",",":")).encode()
        self.send_response(code); self.send_header("Content-Type","application/json; charset=utf-8")
        self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
    def do_GET(self):
        if self.path in ("/health","/"):
            self.send_json(200,{"status":"AOTS6_HILBERT_ENDPOINT_ONLINE","protocol":"AOTS6-HILBERT-ENTANGLEMENT/v1"})
            return
        if self.path.startswith("/state"):
            try:
                r=int(self.path.split("r=",1)[1].split("&",1)[0]) if "r=" in self.path else 1
                self.send_json(200,payload(r))
            except Exception as e: self.send_json(400,{"error":str(e)})
            return
        self.send_json(404,{"error":"not_found"})
    def do_POST(self):
        if self.path!="/state": self.send_json(404,{"error":"not_found"}); return
        try:
            n=int(self.headers.get("Content-Length","0"))
            data=json.loads(self.rfile.read(n) or b"{}")
            self.send_json(200,payload(int(data.get("r",1))))
        except Exception as e: self.send_json(400,{"error":str(e)})
    def log_message(self,*args): pass

def main():
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("--host",default="127.0.0.1"); p.add_argument("--port",type=int,default=8766)
    a=p.parse_args()
    server=ThreadingHTTPServer((a.host,a.port),Handler)
    print(f"AOTS6 Hilbert endpoint: http://{a.host}:{a.port}")
    server.serve_forever()

if __name__=="__main__": main()
