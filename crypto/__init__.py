"""AOTS6 cryptographic protocol layer.

Classical primitives: SHA-256, HMAC-SHA-256, HKDF-SHA-256, secure tokens,
Ed25519, X25519, AES-256-GCM and ChaCha20-Poly1305.
Post-quantum: ML-DSA-65 and ML-KEM-768 when the installed backend exposes them.
""" 
from .core import *  # noqa: F401,F403
