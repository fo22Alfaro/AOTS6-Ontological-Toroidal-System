# AOTS6 — Integrated Quantum Runtime Metadata

Schema: `AOTS6-RUNTIME-META-2`  
Root: `AOTS6-ORIGINAL-ALFARO`  
Meta-operador: **Alfredo Jhovany Alfaro García**

## Unified event

The runtime now produces one ledger event containing provenance metadata and,
when a `token` is present, the AOTS6 quantum-state metadata in the same
hash-covered object.

```
X(t)
 -> provenance extraction
 -> AOTS6 quantum state Ψ_r
 -> {F_rs,d_FS,S_A,I(A:B),QFI,E_r^31}
 -> cryptographic event body
 -> hash-chain ledger
```

Each quantum event contains:

- `F_rs`: fidelity row against the supplied `reference_tokens`, or all 36
  canonical symbols when references are omitted.
- `d_FS`: corresponding Fubini–Study distances.
- `S_A`: entropy for 012|345.
- `I(A:B)`: mutual information for 012|345.
- `QFI`: 6×6 matrix for the local phase parameterization.
- `bipartition_signature_31`: entropy signature over all 31 unique unordered
  bipartitions.
- deterministic phase coordinates, state hash, Hilbert dimension and ring size.

## Integrity

The quantum metadata is part of the exact JSON body used to calculate
`event_hash`. Therefore changing quantum metadata changes the event hash and
breaks all subsequent links in the ledger.

`aots6_verify_runtime_ledger.py` recomputes the chain and checks the quantum
invariants.

## Default reference behavior

A token event with no `reference_tokens` receives its full 36-symbol fidelity
row. A supplied reference list restricts the row to those symbols.

## Reproducibility

The state construction is deterministic for the fixed AOTS6 parameters:
36-symbol alphabet, modulus 37, primes (2,3,5,7,11,13), six qubits, local RZ
phase encoding, and six-CX ring. Floating-point state bytes are hashed as
produced by the configured NumPy runtime; the hash is therefore a runtime
fingerprint, not a claim of cross-platform byte identity.

## Example

```json
{"token":"A"}
```

Run:

```bash
printf '%s\n' '{"token":"A"}' | python3 research/aots6_realtime_metadata_engine.py
python3 research/aots6_verify_runtime_ledger.py
```
