from __future__ import annotations
import json
from .registry import build_registry,verify_registry
def main()->int:
    registry=build_registry(".")
    ok,errors=verify_registry(registry)
    print(json.dumps({"ok":ok,"errors":errors,"registry":registry},ensure_ascii=False,indent=2,sort_keys=True))
    return 0 if ok else 1
if __name__=="__main__":
    raise SystemExit(main())
