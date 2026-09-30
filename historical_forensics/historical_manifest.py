#!/usr/bin/env python3
"""AOTS6 historical corpus integrity manifest generator.

Computes SHA-256 for a local, lawfully acquired corpus and emits a deterministic
manifest. It never bypasses access controls and never changes source files.
"""

from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from typing import Any

EXCLUDED = {".git", "__pycache__"}

def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()

def merkle_root(hashes: list[str]) -> str:
    if not hashes:
        return ""
    level = [bytes.fromhex(x) for x in sorted(hashes)]
    while len(level) > 1:
        if len(level) % 2:
            level.append(level[-1])
        level = [
            hashlib.sha256(level[i] + level[i + 1]).digest()
            for i in range(0, len(level), 2)
        ]
    return level[0].hex()

def collect(root: Path) -> list[dict[str, Any]]:
    rows = []
    for p in sorted(root.rglob("*")):
        if not p.is_file() or any(part in EXCLUDED for part in p.parts):
            continue
        rows.append({
            "relative_path": str(p.relative_to(root)).replace("\\", "/"),
            "size": p.stat().st_size,
            "sha256": sha256_file(p)
        })
    return rows

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    ap.add_argument("-o", "--output", type=Path, required=True)
    args = ap.parse_args()

    root = args.root.resolve()
    files = collect(root)
    manifest = {
        "schema": "AOTS6-HISTORICAL-MANIFEST-1.0",
        "algorithm": "SHA-256",
        "root": str(root),
        "files": files,
        "merkle_root": merkle_root([x["sha256"] for x in files]),
        "verification_policy": "recompute-and-compare",
        "warning": "Hash integrity does not prove historical truth, ownership, authorship or legal title."
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
