from __future__ import annotations
import hashlib, json
from pathlib import Path
SCHEMA="AOTS6-CENTRO-MADRE-1"
ROOT_ID="AOTS6-ORIGINAL-ALFARO"
COMPONENTS={
"toroidal_geometry":{"status":"implemented","evidence":["geometry/AOTS6_Torus.obj","geometry/AOTS6_Geodesics.svg"]},
"ontological_graph":{"status":"implemented","evidence":["AOTS6_Paper.md","ARCHITECTURE.md"]},
"provenance":{"status":"implemented","evidence":["research/AOTS6_ARTIFACT_ROOT.json","research/AOTS6_PROVENANCE_MANIFEST.json","research/aots6_provenance_detector.py"]},
"crypto_runtime":{"status":"implemented","evidence":["security/aots6_crypto_runtime.py","security/AOTS6_CRYPTO_RUNTIME.md"]},
"quantum_state_record":{"status":"implemented_record","evidence":["research/AOTS6_QUANTUM_STATE_METACOMPUTATION_RECORD.md"]},
"qkd":{"status":"internal_interface_deployed","evidence":["qkd/interface.py","qkd/MANIFEST.json","security/aots6_crypto_runtime.py"],"constraint":"AOTS6 QKD is treated as internal development; secret material is never stored or published. Physical-generation claims require independent physical evidence."},
"zk_snark":{"status":"integration_only","evidence":["security/aots6_crypto_runtime.py"],"constraint":"Proof verification belongs to the declared proving system."},
"artifact_root":{"status":"implemented","evidence":["research/AOTS6_ARTIFACT_ROOT.json"]},
"network_auth_signature":{"status":"blocked_pending_keyed_signature","evidence":["AOTS6_NET_AUTH.sig"],"constraint":"A signature file must not be synthesized without the authorized private signing key."},
"external_anchoring":{"status":"evidence_referenced","evidence":["aots6_authorship_cert.json"],"constraint":"External anchors are references until independently revalidated."}
}
def _sha256(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
def build_registry(root=".")->dict:
    base=Path(root); components={}
    for name,spec in COMPONENTS.items():
        present=[]; missing=[]
        for rel in spec["evidence"]:
            p=base/rel
            if p.is_file(): present.append({"path":rel,"sha256":_sha256(p),"bytes":p.stat().st_size})
            else: missing.append(rel)
        components[name]={**spec,"present":present,"missing":missing}
    return {"schema":SCHEMA,"root_id":ROOT_ID,"components":components}
def verify_registry(registry:dict)->tuple[bool,list[str]]:
    errors=[]
    if registry.get("schema")!=SCHEMA: errors.append("schema")
    if registry.get("root_id")!=ROOT_ID: errors.append("root_id")
    for name,item in registry.get("components",{}).items():
        if item.get("status") in {"implemented","internal_interface_deployed"} and item.get("missing"): errors.append(f"{name}:missing")
    return not errors,errors
if __name__=="__main__":
    print(json.dumps(build_registry(),ensure_ascii=False,indent=2,sort_keys=True))
