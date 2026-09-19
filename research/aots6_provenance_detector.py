#!/usr/bin/env python3
"""AOTS⁶ structural provenance detector.

Compares a candidate artifact against a canonical provenance manifest.
The detector is deliberately evidence-producing: it reports layer matches
and structural divergence instead of asserting legal ownership.
"""

from __future__ import annotations
import hashlib, json, re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

LAYER_WEIGHTS = {
    "origin": 0.10,
    "equations": 0.20,
    "structure": 0.20,
    "parameters": 0.10,
    "relations": 0.15,
    "transformations": 0.10,
    "genealogy": 0.10,
    "artifact": 0.05,
}

EQUATION_PATTERNS = [
    r"U_r\s*=\s*C\s*D_r\s*H",
    r"\phi_i\s*\(",
    r"\bR_Z\b",
    r"\b37\b",
    r"2\^6",
    r"\b31\b",
    r"\bT\^6\b",
    r"\bCP\^?63\b",
]

STRUCTURAL_PATTERNS = [
    r"AOTS",
    r"toroid",
    r"fidel",
    r"entrelaz",
    r"metacomput",
    r"quantum",
]

@dataclass
class LayerEvidence:
    score: float
    matches: list[str]
    mismatches: list[str]

@dataclass
class ProvenanceReport:
    root_id: str
    total_score: float
    classification: str
    layers: dict[str, Any]

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def normalized(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def pattern_score(text: str, patterns: list[str]) -> LayerEvidence:
    hits = [p for p in patterns if re.search(p, text, re.I)]
    misses = [p for p in patterns if p not in hits]
    score = len(hits) / len(patterns) if patterns else 0.0
    return LayerEvidence(score, hits, misses)

def load_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def analyze(manifest: dict, candidate_text: str) -> ProvenanceReport:
    cand = normalized(candidate_text)
    layers: dict[str, Any] = {}

    origin = manifest.get("origin", {})
    origin_tokens = origin.get("tokens", [])
    origin_hits = [x for x in origin_tokens if x.lower() in cand]
    layers["origin"] = asdict(
        LayerEvidence(
            len(origin_hits) / len(origin_tokens) if origin_tokens else 0.0,
            origin_hits,
            [x for x in origin_tokens if x not in origin_hits],
        )
    )

    layers["equations"] = asdict(pattern_score(cand, EQUATION_PATTERNS))
    layers["structure"] = asdict(pattern_score(cand, STRUCTURAL_PATTERNS))

    parameter_tokens = [str(x).lower() for x in manifest.get("parameters", [])]
    parameter_hits = [x for x in parameter_tokens if x in cand]
    layers["parameters"] = asdict(
        LayerEvidence(
            len(parameter_hits) / len(parameter_tokens)
            if parameter_tokens else 0.0,
            parameter_hits,
            [x for x in parameter_tokens if x not in parameter_hits],
        )
    )

    relation_tokens = [str(x).lower() for x in manifest.get("relations", [])]
    relation_hits = [x for x in relation_tokens if x in cand]
    layers["relations"] = asdict(
        LayerEvidence(
            len(relation_hits) / len(relation_tokens)
            if relation_tokens else 0.0,
            relation_hits,
            [x for x in relation_tokens if x not in relation_hits],
        )
    )

    candidate_hash = sha256_text(candidate_text)
    canonical_hash = manifest.get("artifact_sha256")
    artifact_score = 1.0 if canonical_hash and candidate_hash == canonical_hash else 0.0
    layers["artifact"] = {
        "score": artifact_score,
        "matches": ["sha256"] if artifact_score else [],
        "mismatches": [] if artifact_score else ["sha256"],
    }

    # Genealogy and transformation layers require explicit metadata.
    layers["genealogy"] = asdict(
        LayerEvidence(
            1.0 if manifest.get("root_id") else 0.0,
            ["root_id"] if manifest.get("root_id") else [],
            [] if manifest.get("root_id") else ["root_id"],
        )
    )
    layers["transformations"] = asdict(
        LayerEvidence(
            1.0 if manifest.get("transformations") is not None else 0.0,
            ["transformation schema"] if manifest.get("transformations") is not None else [],
            [] if manifest.get("transformations") is not None else ["transformation schema"],
        )
    )

    total = sum(
        LAYER_WEIGHTS[k] * layers[k]["score"]
        for k in LAYER_WEIGHTS
    )

    if total >= 0.75:
        classification = "DERIVACIÓN ESTRUCTURAL FUERTE"
    elif total >= 0.50:
        classification = "COINCIDENCIA ESTRUCTURAL SIGNIFICATIVA"
    elif total >= 0.25:
        classification = "COINCIDENCIA PARCIAL — REQUIERE AUDITORÍA"
    else:
        classification = "EVIDENCIA INSUFICIENTE"

    return ProvenanceReport(
        root_id=manifest.get("root_id", ""),
        total_score=total,
        classification=classification,
        layers=layers,
    )

def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    candidate = args.candidate.read_text(encoding="utf-8")
    report = analyze(manifest, candidate)
    payload = json.dumps(asdict(report), ensure_ascii=False, indent=2)

    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)

if __name__ == "__main__":
    main()
