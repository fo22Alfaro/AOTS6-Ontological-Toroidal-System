from __future__ import annotations
from dataclasses import dataclass,field
from hashlib import sha256
from typing import Iterable

@dataclass(frozen=True)
class Node:
    node_id:str
    region:str
    software_digest:str
    capabilities:tuple[str,...]=()

@dataclass
class Cell:
    node_id:str
    state:int=0
    neighbors:set[str]=field(default_factory=set)
    trust:int=100

class ToroidalAutomata:
    """Deterministic bounded cellular automaton for defensive state propagation."""
    def __init__(self,cells:Iterable[Cell]):
        self.cells={c.node_id:c for c in cells}
    def step(self)->dict[str,int]:
        nxt={}
        for ident,c in self.cells.items():
            votes=sum(self.cells[n].state for n in c.neighbors if n in self.cells)
            degree=len([n for n in c.neighbors if n in self.cells])
            nxt[ident]=1 if degree and votes*2>=degree else 0
        for ident,state in nxt.items(): self.cells[ident].state=state
        return nxt
    def topology_digest(self)->str:
        material="|".join(f"{k}:{self.cells[k].state}:{','.join(sorted(self.cells[k].neighbors))}" for k in sorted(self.cells))
        return sha256(material.encode()).hexdigest()

class NemesisDefense:
    """Bounded defensive response engine; it never issues arbitrary remote commands."""
    ALLOWED={"observe","isolate","quarantine","restore","rotate_credentials"}
    def __init__(self,max_actions_per_cycle:int=3):
        if max_actions_per_cycle<1: raise ValueError("positive action bound required")
        self.max_actions_per_cycle=max_actions_per_cycle
    def plan(self,signals:list[dict])->list[dict]:
        actions=[]
        for s in signals:
            action=s.get("recommended_action")
            if action not in self.ALLOWED: continue
            if s.get("authorization") is not True: continue
            actions.append({"node_id":s.get("node_id"),"action":action,"reason":s.get("reason","")})
            if len(actions)>=self.max_actions_per_cycle: break
        return actions

def attest(node:Node)->dict:
    return {"node_id":node.node_id,"region":node.region,"software_digest":node.software_digest,
            "capabilities":list(node.capabilities),"attestation":"metadata_only"}
