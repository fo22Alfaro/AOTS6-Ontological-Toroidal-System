from __future__ import annotations
from dataclasses import dataclass
from hashlib import sha256
from typing import Iterable

@dataclass(frozen=True)
class Dimension:
    id: str
    name: str
    role: str

@dataclass(frozen=True)
class Link:
    source: str
    target: str
    network: str
    mode: str

class ToroidalCore:
    """Explicit finite model of AOTS6's declared dimensional/network layers."""
    DIMENSIONS = (
        Dimension("D1","state","discrete state and symbol layer"),
        Dimension("D2","semantic","semantic/ontological relation layer"),
        Dimension("D3","geometric","toroidal spatial relation layer"),
        Dimension("D4","temporal","event ordering and provenance layer"),
        Dimension("D5","quantum-record","quantum-state record and cryptographic envelope layer"),
        Dimension("D6","integration","cross-layer orchestration and network control layer"),
    )
    NETWORKS = ("ONTOLOGICAL","TOROIDAL","CRYPTO","QUANTUM_RECORD","GLOBAL_NET","DEFENSIVE","AUDIT")

    def __init__(self):
        self.links: list[Link] = []
    def connect(self, source:str, target:str, network:str, mode:str="verified"):
        if source not in {d.id for d in self.DIMENSIONS} or target not in {d.id for d in self.DIMENSIONS}:
            raise ValueError("unknown dimension")
        if network not in self.NETWORKS:
            raise ValueError("unknown network")
        self.links.append(Link(source,target,network,mode))
    def manifest(self)->dict:
        return {
            "schema":"AOTS6-TOROIDAL-CORE-1",
            "dimensions":[d.__dict__ for d in self.DIMENSIONS],
            "networks":list(self.NETWORKS),
            "links":[l.__dict__ for l in self.links],
            "evidence_rule":"verified means repository/software evidence; physical quantum or biological claims require external measurements",
            "audit_gate":"A2-OBOM verification is mandatory before validity is reported"
        }
    def digest(self)->str:
        import json
        raw=json.dumps(self.manifest(),sort_keys=True,separators=(",",":")).encode()
        return sha256(raw).hexdigest()
