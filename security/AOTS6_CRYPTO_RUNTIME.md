# AOTS6 Cryptographic Runtime

The runtime centralizes cryptographic provenance around the real-time event hash.

## Families

- **ML-DSA (Dilithium)**: post-quantum signature adapter. The implementation delegates to a provider such as OpenSSL rather than implementing a cryptographic primitive incorrectly in pure Python.
- **Ed25519**: compatibility signature family.
- **SHA3-512 / BLAKE2b / SHA-256**: digest and integrity layers.
- **ML-KEM (Kyber)**: post-quantum key encapsulation integration point.
- **QKD**: physical key-material ingestion. No QKD material is generated or simulated by AOTS6.
- **ZK-SNARK**: proof-envelope integration. A proof is preserved with its proof-system, circuit and public-input metadata; verification belongs to the declared proving system.

Every security envelope contains the AOTS6 event hash, canonical signed-message digest, algorithm identity, raw artifact metadata, the literal fitness trace `54/19/11/0/1`, and an envelope hash.

Historical AOTS6 cryptographic components such as SHA3, BLAKE2b, Ed25519 and the existing ledger/signature artifacts remain representable. Dilithium is named by its current standardized family, **ML-DSA**, while preserving `Dilithium` as the historical lineage name.

No hash is treated as a signature, no simulated QKD key is treated as physical, and no unverified ZK proof is marked verified.
