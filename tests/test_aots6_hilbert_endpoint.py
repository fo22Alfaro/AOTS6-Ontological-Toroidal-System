import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
from api.aots6_hilbert_endpoint import build_state, payload, DIM

def test_dimension_and_normalization():
    s=build_state(1)
    assert len(s)==DIM
    assert abs(sum(abs(x)**2 for x in s)-1)<1e-12

def test_ordered_ring_changes_state():
    a=build_state(1); b=build_state(2)
    assert a!=b

def test_payload_integrity():
    p=payload(1)
    assert p["hilbert_dimension"]==64
    assert p["normalized"] is True
    assert len(p["amplitudes"])==64
    assert len(p["state_sha256"])==64
