#!/usr/bin/env python3
"""AOTS6 real-time deep-metadata and provenance engine."""
from __future__ import annotations
import ast, hashlib, json, re, sys, time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

ROOT_ID="AOTS6-ORIGINAL-ALFARO"; SCHEMA="AOTS6-RUNTIME-META-1"
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
    except Exception: return None
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
    low=text.lower(); return sorted(set(v for v in vocab if v.lower() in low))
@dataclass
class Event:
    schema:str; sequence:int; timestamp_ns:int; root_id:str
    observation_sha256:str; canonical_sha256:str; ast_sha256:str|None
    equations:list[str]; structural_tokens:list[str]; metadata:dict[str,Any]
    previous_event_hash:str; event_hash:str
class RuntimeEngine:
    def __init__(self,ledger:str="aots6_runtime_ledger.jsonl"):
        self.ledger=Path(ledger); self.sequence=0; self.previous="0"*64
        if self.ledger.exists():
            lines=[x for x in self.ledger.read_text(encoding="utf-8").splitlines() if x.strip()]
            if lines:
                last=json.loads(lines[-1]); self.sequence=int(last["sequence"])+1
                self.previous=last["event_hash"]
    def observe(self,payload:str|dict[str,Any])->Event:
        raw=payload if isinstance(payload,str) else json.dumps(payload,ensure_ascii=False,sort_keys=True)
        canonical=canonical_text(raw); ast_sig=normalized_ast(raw)
        eq=extract_equations(raw); tok=structural_tokens(raw)
        meta={"length":len(raw),"canonical_length":len(canonical),"equation_count":len(eq),
              "structural_token_count":len(tok),"contains_aots6_root_tokens":bool(tok)}
        body={"schema":SCHEMA,"sequence":self.sequence,"timestamp_ns":time.time_ns(),
              "root_id":ROOT_ID,"observation_sha256":sha256(raw.encode()),
              "canonical_sha256":sha256(canonical.encode()),
              "ast_sha256":sha256(ast_sig.encode()) if ast_sig else None,
              "equations":eq,"structural_tokens":tok,"metadata":meta,
              "previous_event_hash":self.previous}
        event_hash=sha256(json.dumps(body,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode())
        ev=Event(**body,event_hash=event_hash)
        with self.ledger.open("a",encoding="utf-8") as f:
            f.write(json.dumps(asdict(ev),ensure_ascii=False,sort_keys=True)+"\n")
        self.previous=event_hash; self.sequence+=1; return ev
def main():
    engine=RuntimeEngine(sys.argv[1] if len(sys.argv)>1 else "aots6_runtime_ledger.jsonl")
    for line in sys.stdin:
        line=line.rstrip("\n")
        if line: print(json.dumps(asdict(engine.observe(line)),ensure_ascii=False,sort_keys=True))
if __name__=="__main__": main()
