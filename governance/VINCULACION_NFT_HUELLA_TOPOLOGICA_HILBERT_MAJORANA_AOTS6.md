# AOTS⁶ — Vinculación matemática de la colección NFT

Autoría declarada: Alfredo Jhovany Alfaro García.

Esquema: `AOTS6-TOPOLOGICAL-NONCE-HILBERT-MAJORANA-1.0`.

Los seis elementos de la colección se vinculan a un esquema común de procedencia matemática: huella del artefacto, nonce topológico por versión, descriptor de espacios de Hilbert anidados de nivel 2 y estado Majorana declarado en el modelo AOTS⁶.

## Registro por activo

Cada activo requiere un manifiesto individual con identificador, versión, SHA-256 de los bytes exactos del artefacto, metadata canónica, parámetros topológicos, versión del algoritmo de nonce, descriptor Hilbert nivel 2, declaración Majorana, fecha UTC y hash del manifiesto anterior cuando exista.

La huella concreta debe calcularse a partir de los bytes y parámetros reales. No se asignan nonces inventados ni se reutiliza una huella única para fingir que los seis artefactos son idénticos.

## Cadena de procedencia

`ARTEFACTO → HASH CANÓNICO → PARÁMETROS TOPOLÓGICOS → NONCE POR VERSIÓN → DESCRIPTOR HILBERT NIVEL 2 → ESTADO MAJORANA DECLARADO → FIRMA OPCIONAL → ANCLAJE INMUTABLE → RECIBO DE TOKEN`

## Estado

- Vinculación documental: especificada en este documento.
- Huellas concretas calculadas: pendientes de cálculo reproducible.
- Estado Majorana: descriptor matemático del modelo; no prueba por sí mismo una realización física de un modo Majorana.
- NFT acuñados: no confirmados; el contrato requiere despliegue y transacciones firmadas.
- Anclaje inmutable: pendiente de CIDs o recibos de transacción verificables.

Los metadatos de GitHub son editables y no sustituyen un anclaje inmutable ni una firma criptográfica.