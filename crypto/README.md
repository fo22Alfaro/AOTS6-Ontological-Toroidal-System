# AOTS6 — Crypto Protocol Layer

Esta capa despliega en el repositorio principal las capacidades criptográficas que ya tienen evidencia ejecutable en el Núcleo Toroidal y separa explícitamente las capacidades condicionales o de integración.

## Desplegado

- SHA-256
- HMAC-SHA-256
- HKDF-SHA-256
- generación de material aleatorio seguro
- Ed25519
- X25519 + HKDF para derivación de clave compartida
- AES-256-GCM
- ChaCha20-Poly1305

## Poscuántico condicional

- ML-DSA-65
- ML-KEM-768

Se activan sólo si la versión/backend de `cryptography` disponible expone esas APIs. No se generan claves privadas ni material secreto durante el despliegue.

## Integración, no simulación

- QKD: sólo ingestión de material generado por un sistema QKD real.
- ZK-SNARK: sólo envolvente/verificación perteneciente al sistema de pruebas declarado.
- SHA3-512 y BLAKE2b: ya están expuestos por el runtime de seguridad existente.

## Bibliotecas

La dependencia ejecutable de esta implementación es `cryptography>=49,<50`. El sandbox también documenta PyNaCl/libsodium, liboqs y pqcrypto como alternativas; no se etiquetan como instaladas aquí sin evidencia de instalación.

## Regla de procedencia

Los datos recuperados del sandbox se usan como inventario y trazabilidad. Ningún hash, firma, clave, QKD o prueba ZK se fabrica para aparentar que existe.
