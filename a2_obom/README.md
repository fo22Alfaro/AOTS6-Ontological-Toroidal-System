# AOTS6 Audit Interface — A2-OBOM

This component concatenates the A2-OBOM audit boundary with the AOTS6 software architecture.

## Mandatory validity gate
An A2-OBOM is never reported as valid unless verify_a2_obom() has been executed.
Its verified=true result means canonical payload integrity and conformance to the declared A2-OBOM policy.
It does not by itself establish scientific validity of physical, quantum, biological, or experimental claims.

## Certification gate
Before certify_a2_obom() is called, the operator must explain changes to data, ontology, SHACL constraints, policy, and expected digest consequences.
Explicit user confirmation is then required. The certifier refuses to operate without it and re-runs verify_a2_obom() on the candidate.

## Secret handling
Audit output recursively filters fields matching private keys, secrets, tokens, passwords, credentials, authorization material, and access keys.
No private-key material or credentials are stored by this component.

## Digest model
The digest is SHA-256 over canonical JSON with the digest field excluded during computation.
Any change to data, ontology, SHACL, or policy changes the canonical payload and therefore the digest.
verify_a2_obom() recomputes it before returning the audit result.
