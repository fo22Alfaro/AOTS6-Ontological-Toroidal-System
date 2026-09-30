# Historical Forensics — AOTS⁶

This package is the executable integrity layer for the historical-forensic corpus.

It performs only local hashing and manifest construction over material already lawfully acquired.

It does not:
- bypass access restrictions;
- obtain credentials;
- decrypt protected material;
- modify archival originals;
- assert historical truth from hashes.

It does:
- recursively inventory files;
- calculate SHA-256;
- preserve byte length;
- generate deterministic Merkle roots;
- emit a machine-readable manifest;
- support later independent verification.

Run:

python historical_forensics/historical_manifest.py <CORPUS> --output historical_forensics/manifest.json
