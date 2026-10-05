# AOTS6 Hilbert Endpoint

Executable local HTTP endpoint for the six-qubit computational Hilbert space.

The service exposes a normalized complex state vector of dimension sixty-four, applies the declared phase construction and the controlled-X ring, and returns a SHA-256 fingerprint of the resulting state.

Run:

python3 api/aots6_hilbert_endpoint.py --host 127.0.0.1 --port 8766

Health: GET /health

State: GET /state?r=1

POST /state with JSON {"r":1}

The implementation is standard-library Python. It is a computational realization of the abstract Hilbert-space model; it does not claim physical quantum-hardware execution.