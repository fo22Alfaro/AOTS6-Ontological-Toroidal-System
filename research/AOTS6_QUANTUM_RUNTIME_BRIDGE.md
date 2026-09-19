# AOTS6 — Real-Time Quantum Metadata Bridge

The runtime provenance event stream can now be enriched with the six-qubit AOTS6
state generated from the canonical alphabet/modulus/prime encoding and six-CX ring.

For every event carrying a `token`, the bridge adds:

- `F_rs`: pairwise state fidelity against requested `reference_tokens`;
- `d_FS`: Fubini–Study distance;
- `S_A`: subsystem entropy for the 012|345 partition;
- `I_A_B`: mutual information, using purity of the global state;
- `QFI`: the six-parameter quantum Fisher information matrix;
- `bipartition_signature_31`: entropy across all 31 unique bipartitions;
- phase coordinates, Hilbert dimension, and six-CX ring metadata.

The bridge is deterministic for a given token and reference set. It uses the
AOTS6 construction:

phi_i = ((r p_i) mod 37)/37

followed by H^6, local RZ phases, and the fixed six-edge CX ring.

## Streaming

python3 research/aots6_realtime_metadata_engine.py <<EOF | python3 research/aots6_quantum_metadata_bridge.py
{"token":"A","reference_tokens":["B","C"]}
EOF

The first process creates the provenance event; the second enriches it with
quantum-state metadata. A production integration can call the bridge directly
from the runtime event writer so the enriched object is persisted as one event.

## Exactness

For the common CX ring, pairwise fidelity is invariant under the ring. The
bridge therefore computes F_rs from the complete post-ring states while retaining
the same physical value as the pre-ring states.

The 31-partition signature is the entropy vector for the 31 unique unordered
bipartitions of six qubits.
