#!/usr/bin/env python3
"""Motor auditable de ejecución del Modelo de Restitución CPEUM — AOTS⁶.

No decide procedencia jurídica ni sustituye a una autoridad. Verifica que cada
estado del expediente tenga los campos y constancias documentales mínimos
definidos por el modelo.
"""
from __future__ import annotations
import argparse, json, hashlib, sys
from pathlib import Path

STATES = [
    "EXISTENCIA","AFECTACIÓN","LEGALIDAD","DEFENSA",
    "CONTROL_CONSTITUCIONAL","DECISIÓN","IMPUGNACIÓN",
    "CUMPLIMIENTO","RESTITUCIÓN"
]
FINAL_STATES = {"AGOTADO-PROCEDIMIENTO","AGOTADO-RECURSO",
                "NO-PROCEDENTE","NO-AGOTABLE","PENDIENTE","NO-DETERMINADO"}

def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def validate(e: dict) -> list[str]:
    errors=[]
    required=["id","right","act","authority","legality","defense",
              "evidence","decision","appeal","restitution","epistemic_state"]
    for k in required:
        if k not in e: errors.append(f"MISSING:{k}")
    if errors: return errors
    if not e["right"].get("source"): errors.append("RIGHT:source requerido")
    if not e["act"].get("type") or not e["act"].get("date"):
        errors.append("ACT:tipo y fecha requeridos")
    if not e["authority"].get("competence_source"):
        errors.append("AUTHORITY:competence_source requerido")
    if not e["legality"].get("legal_basis"):
        errors.append("LEGALITY:legal_basis requerido")
    if not e["defense"].get("ordinary_route"):
        errors.append("DEFENSE:ordinary_route requerido")
    if e["defense"].get("amparo_route") and not (
        e["defense"].get("amparo_legal_basis") or
        e["defense"].get("amparo_procedural_finding")
    ):
        errors.append("AMPARO:requiere fundamento legal o determinación procesal documentada")
    if not isinstance(e["evidence"], list):
        errors.append("EVIDENCE:debe ser lista")
    if not e["decision"].get("status"):
        errors.append("DECISION:status requerido")
    if e["restitution"].get("executed") and not e["restitution"].get("execution_evidence"):
        errors.append("RESTITUTION:ejecutada=true exige execution_evidence")
    if e["epistemic_state"] not in STATES + list(FINAL_STATES):
        errors.append("STATE:estado no reconocido")
    if e["epistemic_state"] in {"AGOTADO-PROCEDIMIENTO","AGOTADO-RECURSO"}:
        if not e.get("decision",{}).get("document_hash"):
            errors.append("EXHAUSTION:decision.document_hash requerido")
    return errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("expediente", type=Path)
    ap.add_argument("--hash", action="store_true", help="muestra SHA-256 del expediente")
    args=ap.parse_args()
    raw=args.expediente.read_bytes()
    if args.hash:
        print(hashlib.sha256(raw).hexdigest())
    try:
        data=json.loads(raw)
    except Exception as exc:
        print(f"INVALID_JSON:{exc}", file=sys.stderr); return 2
    errors=validate(data)
    result={"valid":not errors,"id":data.get("id"),"errors":errors,
            "state":data.get("epistemic_state")}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if not errors else 1

if __name__=="__main__":
    raise SystemExit(main())
