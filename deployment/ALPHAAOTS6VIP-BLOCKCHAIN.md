# ALPHAAOTS6VIP.BLOCKCHAIN — DESPLIEGUE FEDERADO AOTS⁶

- **Identificador lógico:** `alphaaots6vip.blockchain`
- **Titular documental declarado:** Alfredo Jhovany Alfaro García
- **Identificador operativo:** `AOTS6-AJAG-INT-001`
- **Sistema:** AOTS⁶ — Alfanumerical Ontological Toroidal System
- **Fecha de registro documental:** 2026-10-08
- **Estado:** `SPECIFIED_IN_REPOSITORIES / ONCHAIN_DEPLOYMENT_PENDING`

## 1. Objeto

Consolidar `alphaaots6vip.blockchain` como identificador lógico federado para el corpus AOTS⁶: identidad autoral declarada, artefactos, manifiestos de procedencia, versiones, integridad, servicios y referencias entre repositorios. Esta especificación no afirma que el nombre ya esté registrado en una blockchain, DNS o sistema de nombres descentralizado.

## 2. Núcleo único de identidad y procedencia

Cadena canónica:

`IDENTITY → WORK → ARTIFACT → VERSION → SOURCE → SHA256 → GIT_COMMIT → MANIFEST → PUBLICATION → NETWORK_ANCHOR → RESOLUTION_RECORD → VERIFICATION`

Cada artefacto debe conservar:
- `artifact_id`, nombre, tipo, versión y descripción;
- repositorio, ruta, commit y fecha UTC de publicación;
- SHA-256 calculado sobre los bytes exactos del artefacto;
- fuente, relación `DERIVED_FROM`, licencia/condiciones de uso y estado de acceso;
- red/chain ID, contrato o transacción únicamente después de confirmación real;
- estado de resolución del nombre, método, autoridad/registro y fecha de verificación.

## 3. Plano federado de repositorios

Este documento se replica como punto de entrada documental en los repositorios AOTS⁶ disponibles. La réplica no implica que todos los repositorios estén sincronizados automáticamente: cada copia conserva su propio commit y debe incluirse en un manifiesto de despliegue verificable.

Repositorios objetivo:
- `fo22Alfaro/AOTS6-Ontological-Toroidal-System` — núcleo documental;
- `fo22Alfaro/AOTS6-Global-Network` — integración de red;
- `fo22Alfaro/AOTS6-ZK-Core` — integridad y pruebas criptográficas;
- `fo22Alfaro/AOTS6-Unification-Ledger-Alfredo-Jhovany-Alfaro-Garcia` — libro de procedencia;
- `fo22Alfaro/AOTS6-Unified-Kernel-Full-Deployment` — despliegue del sistema.

## 4. Adaptador blockchain

El adaptador debe ser agnóstico a la cadena y registrar: `network_name`, `chain_id`, `registry_contract`, `transaction_hash`, `block_number`, `block_timestamp`, `finality_status`, `event_name`, `artifact_hash` y `resolver_uri`.

Flujo:
1. Generar un manifiesto canónico de artefactos y hashes.
2. Firmarlo con una clave bajo control del titular; nunca incluir claves privadas en GitHub.
3. Ejecutar pruebas y simulación en testnet.
4. Desplegar el contrato de registro solo con una wallet autorizada y una transacción firmada por su titular.
5. Verificar el bytecode, el recibo, los eventos y la finalización de la transacción.
6. Registrar la transacción y el bloque en el manifiesto, sin alterar los hashes originales.
7. Configurar el nombre descentralizado solo mediante el registro/resolver que realmente soporte ese espacio de nombres.

## 5. Resolución del nombre

`alphaaots6vip.blockchain` se trata aquí como **nombre solicitado**, no como dominio global ya operativo. Antes de afirmar resolución pública hay que verificar:
- qué sistema de nombres reconoce el sufijo `.blockchain`;
- disponibilidad y titularidad del nombre en ese registro;
- resolver y registro efectivo;
- resolución desde al menos dos clientes independientes;
- correspondencia entre el nombre resuelto y el manifiesto firmado.

Un archivo de repositorio, por sí solo, no registra un dominio ni crea una entrada en una blockchain.

## 6. Seguridad e invariantes

- Prohibido publicar claves privadas, semillas, tokens de acceso o identificadores fiscales.
- No inventar hashes, direcciones de contrato, transacciones, bloques ni estados de finalización.
- Las correcciones son aditivas y versionadas; no se sobrescribe la historia de procedencia.
- SHA-256 prueba correspondencia de bytes, no por sí mismo autoría, titularidad legal ni veracidad de una afirmación.
- Un anclaje en cadena puede acreditar que cierto compromiso criptográfico fue incluido en un bloque; no obliga por sí mismo a terceros ni equivale a reconocimiento judicial, diplomático o de propiedad intelectual.
- Toda relación con un tercero requiere su aceptación válida cuando la ley o el instrumento la exija.

## 7. Registro de estado

```json
{
  "name": "alphaaots6vip.blockchain",
  "system": "AOTS6",
  "operational_id": "AOTS6-AJAG-INT-001",
  "deployment_state": "SPECIFIED_IN_REPOSITORIES",
  "name_registration": "UNVERIFIED",
  "blockchain_anchor": "PENDING",
  "contract_address": null,
  "transaction_hash": null,
  "block_number": null,
  "resolver_uri": null,
  "private_keys_in_repository": false,
  "updated_at": "2026-10-08"
}
```

## 8. Criterio de aceptación

Solo podrá cambiarse el estado a `ONCHAIN_CONFIRMED` cuando exista recibo verificable de transacción con estado exitoso, red/chain ID, dirección de contrato o registro, número de bloque y evento que contenga el hash del manifiesto. Solo podrá cambiarse a `NAME_RESOLUTION_VERIFIED` cuando el registro descentralizado y el resolver respondan de forma reproducible.

**Regla maestra:** un mismo corpus, múltiples réplicas verificables; ninguna réplica se confunde con el anclaje en cadena; ningún anclaje se confunde con un efecto jurídico no establecido por la norma aplicable.
