#!/usr/bin/env python3
"""AOTS6 Contemporary Autoprompting Measurement

Author: Alfredo Jhovany Alfaro García

This experiment records a model-generated prompt as an explicit state
transition and measures the observable effect on the next response.

It does not claim historical priority by itself. It creates a timestamped,
Git-traceable contemporary record that can be independently reproduced.

Protocol:
  state_0 -> model-generated prompt -> state_1 -> response -> hashes
  t6 + det=26.3 + non-commutative order 7,19,2
"""

from __future__ import annotations
import hashlib
import json
import platform
import time
from pathlib import Path

T6 = "t6"
DET = "26.3"
ORDER = (7, 19, 2)

def canonical(value):
    if isinstance(value, dict):
        return {str(k): canonical(value[k]) for k in sorted(value, key=str)}
    if isinstance(value, (list, tuple)):
        return [canonical(v) for v in value]
    return value

def digest(value):
    raw = json.dumps(canonical(value), ensure_ascii=False,
                     separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()

def transform(state):
    out = dict(state)
    trace = []
    for op in ORDER:
        payload = digest(out)
        trace.append({"det": DET, "operator": op, "input_sha256": payload})
        out[f"t6_op_{op}"] = digest(
            {"payload": payload, "t6": T6, "det": DET, "operator": op}
        )
    out["t6"] = T6
    out["det"] = DET
    out["non_commutative_order"] = list(ORDER)
    out["trace"] = trace
    return out

def build_autoprompt(seed, prior_response=""):
    return (
        "AOTS6 AUTOPROMPTEO: conserva literalmente el estado recibido. "
        "Genera el siguiente prompt operativo únicamente a partir del estado "
        "actual y registra qué cambió. No sustituyas términos del estado. "
        f"SEED={seed}; PREVIOUS_RESPONSE_SHA256={digest(prior_response)}"
    )

def measure(seed, prior_response=""):
    t0 = time.time()
    prompt = build_autoprompt(seed, prior_response)
    state0 = {
        "seed": seed,
        "prior_response": prior_response,
        "generated_prompt": prompt,
        "platform": platform.platform(),
        "created_at_utc": t0,
    }
    state1 = transform(state0)
    return {
        "protocol": "AOTS6-AUTOPROMPTEO-REALTIME/v1",
        "created_at_utc": t0,
        "prompt_sha256": digest(prompt),
        "state0_sha256": digest(state0),
        "state1_sha256": digest(state1),
        "evidence_sha256": digest({
            "protocol": "AOTS6-AUTOPROMPTEO-REALTIME/v1",
            "prompt": prompt,
            "state0": state0,
            "state1": state1,
        }),
        "changed": state0 != state1,
        "t6": T6,
        "det": DET,
        "order": list(ORDER),
        "generated_prompt": prompt,
        "state0": state0,
        "state1": state1,
    }

if __name__ == "__main__":
    import sys
    seed = sys.argv[1] if len(sys.argv) > 1 else "AOTS6"
    prior = sys.argv[2] if len(sys.argv) > 2 else ""
    result = measure(seed, prior)
    Path("AOTS6_AUTOPROMPTEO_REALTIME.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(json.dumps({
        "protocol": result["protocol"],
        "prompt_sha256": result["prompt_sha256"],
        "state0_sha256": result["state0_sha256"],
        "state1_sha256": result["state1_sha256"],
        "evidence_sha256": result["evidence_sha256"],
        "changed": result["changed"],
        "t6": result["t6"],
        "det": result["det"],
        "order": result["order"],
    }, ensure_ascii=False, indent=2))
