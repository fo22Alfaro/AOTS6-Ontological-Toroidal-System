# AOTS⁶ — PROTOCOLO DE RECUPERACIÓN CRIPTOGRÁFICA Y RESTITUCIÓN HISTÓRICA

## Alcance

Define cómo convertir fuentes históricas públicamente accesibles en objetos verificables, reproducibles y trazables dentro de AOTS⁶.

No autoriza acceso no permitido, evasión de controles, extracción de credenciales ni intrusión.

## Flujo

CATÁLOGO → IDENTIFICADOR → OBJETO → CAPTURA → HASH → METADATOS → DERIVADOS → MERKLE → FIRMA → PUBLICACIÓN

## Identificación

Cada objeto recibe source_id y conserva institución, fondo, serie, signatura, título, fecha, URL, fecha de consulta y estado de acceso.

## Hash

Para cada archivo adquirido legítimamente:

SHA256(bytes)

Registrar algoritmo, digest, longitud, MIME y fecha.

## Derivados

OCR, transcripción, traducción, normalización y extracción son objetos derivados. Cada uno conserva parent_hash y su propio SHA-256.

## Merkle

Los hashes se pueden agregar en un árbol Merkle y la raíz se registra en un manifiesto versionado.

## Firma

El manifiesto puede firmarse con una clave controlada por el autor. La firma autentica el manifiesto frente a su clave; no convierte automáticamente los documentos en auténticos ni verdaderos.

## Anclaje externo

Cuando exista un servicio legítimo de preservación, registrar DOI, repositorio institucional, IPFS/CID, Git commit o timestamp.

## Estados

RECUPERADO
HASH_VERIFICADO
PROCEDENCIA_VERIFICADA
CORROBORADO
DERIVADO
NO_DETERMINADO
ACCESO_RESTRINGIDO
NO_DIGITALIZADO
PÉRDIDA_DOCUMENTADA

## Regla de no sobreafirmación

No registrar FRAUDE si sólo existe similitud.
No registrar APROPIACIÓN si sólo existe proximidad temporal.
No registrar CONTINUIDAD si sólo existe continuidad nominal.
No registrar RESTITUIDO si sólo existe una solicitud.

## Integridad

CONCLUSIÓN → EVIDENCIA → DOCUMENTO → HASH → FUENTE

## Autonomía informacional

La finalidad es maximizar la capacidad de una persona o comunidad para localizar, comprender, conservar y utilizar lícitamente información pertinente a sus derechos.

## Prueba mínima

Un registro histórico pasa a DOCUMENTADO sólo con fuente, identificador, fecha, contenido o descripción suficiente, procedencia y estado de acceso.

Una transferencia requiere objeto, transferente, adquirente, fecha, acto y fuente.

Una restitución ejecutada requiere acto competente y evidencia de ejecución.

AOTS6 — Integridad histórica por trazabilidad, no por sustitución narrativa.
