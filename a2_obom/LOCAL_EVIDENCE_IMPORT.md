# AOTS6 A2-OBOM — Local Evidence Import

This bridge connects a locally certified A2-OBOM workspace to the GitHub audit surface without copying secrets or private credentials.

## Observed local verification record

The operator-provided execution reported:

- RDF evidence: 9 triples
- certify allow: true
- SHACL conforms: true
- signature verified: true
- OBOM digest: sha256:c9e264d9c52d96a8def7d4b829287486a370d19950ac60b396cc48390a9202d3
- post-certification verify: verified=true
- checksum failures: []
- policy allow: true

These values are recorded as an operator-supplied local execution record. They are not independently verified by GitHub.

## Import rule

The local artifact must be supplied through a controlled import after local verification. Do not commit private keys, signing tokens, credentials, authorization headers, unfiltered secrets, or sensitive local filesystem paths.

The GitHub A2-OBOM verifier remains the repository validity gate.