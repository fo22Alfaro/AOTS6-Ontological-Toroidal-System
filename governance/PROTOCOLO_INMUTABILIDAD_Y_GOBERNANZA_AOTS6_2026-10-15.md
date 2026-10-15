# AOTS⁶ — Protocolo de integridad, custodia y gobernanza de registros
**Versión:** 1.0 | **Fecha:** 2026-10-15  
**Responsable declarado del proyecto:** Alfredo Jhovany Alfaro García  
**Estado:** especificación publicada; implantación integral pendiente de verificación.

## 1. Objetivo
Reducir la posibilidad de alteración, borrado, transferencia no autorizada o pérdida de evidencia. Ningún sistema puede garantizar que jamás habrá manipulación en todos los entornos; se requiere protección por capas, alertas y verificación independiente. Un hash o un registro blockchain no prueban por sí solos identidad, autorización legal ni posibilidad de recuperación.

## 2. Reglas no negociables
1. **Append-only:** no sobrescribir evidencia. Toda corrección añade un evento nuevo que referencia al anterior y registra motivo, actor, hora y prueba.
2. **Integridad:** cada evento incluye hash del contenido canónico, hash previo, versión, hora UTC, origen y estado de verificación.
3. **Anclaje independiente:** publicar raíces hash en un sistema externo y conservar recibo. Un hash dentro del mismo repositorio no es anclaje independiente.
4. **Copias separadas:** mantener al menos tres copias, dos tipos de medio y una ubicación/cuenta separada; usar retención WORM/Object Lock donde esté disponible y probar restauraciones.
5. **GitHub:** activar y verificar ramas protegidas, bloqueo de force-push y borrado, revisiones obligatorias, CODEOWNERS y auditoría de acciones. Documentarlo no activa estas funciones.
6. **Claves:** custodiar claves en hardware/gestor seguro; nunca en código, JSON, historial Git ni mensajes. Separar firma, recuperación y auditoría. Rotar cualquier clave expuesta.
7. **Activos:** antes de operar, comprobar red, contrato, titularidad, aprobaciones, destino, simulación y límites. Operaciones de alto impacto requieren autorización explícita del titular y preferentemente multisig independiente.
8. **Separación de funciones:** el observador no firma; el motor de políticas no custodia claves; el firmante no altera registros; el auditor puede verificar sin escribir.
9. **Gobernanza de mercado:** no comprar, vender, transferir ni liquidar automáticamente sin política publicada, límites de exposición y slippage, interruptor de emergencia y autorización explícita. No garantizar rentabilidad.
10. **Incidentes:** preservar hashes, recibos, calldata, logs y capturas; revocar aprobaciones sólo después de confirmar red, contrato y titularidad. Migrar activos sólo con autorización del titular y tras simular.

## 3. Flujo de control
OBSERVAR → NORMALIZAR → HASH → COMPARAR CON ANCLAJE → EVALUAR POLÍTICA → ALERTAR → APROBACIÓN EXPLÍCITA → FIRMAR LOCALMENTE → ENVIAR → VERIFICAR RECIBO → ANCLAR EVIDENCIA.

Si falla integridad, autorización, simulación o verificación: denegar nuevas operaciones automáticas y preservar evidencia. No declarar robo, fraude o titularidad sólo por una etiqueta o inferencia.

## 4. Campos mínimos de cada evento
event_id, timestamp_utc, actor, action, chain_id, contract, asset_id, previous_event_hash, payload_hash, manifest_hash, signature_algorithm, signature_reference (nunca la clave), external_anchor, verification_status, evidence_uris, reason y supersedes_event_id cuando corresponda.

## 5. Caso Polygon — hechos disponibles
La colección 0xa9a6a3626993d487d2dbda3173cf58ca1a9d9e9f emitió eventos ERC-721 que muestran transferencias desde 0xA5F0E2Cce420DD12D508EEAeE43CcC60D6fc76De al contrato 0x7be83293BeeDc9Eba1bd76c66A65F10F3efaeC26. El recibo de 0xc866a9dc36f67648ad4f0a710c5a40a28658071936e74ecabf8fd2613c35d281 indica éxito (status 0x1) y transferencia del token 0x192e7815249c2c052f3bb0ce30c123f808672dc5a8833fe1ac25783ac8687051 al Minting Manager. Una llamada ownerOf posterior devolvió cero para ese token; hace falta contrastar ABI e implementación antes de concluir si es inexistente, quemado o recuperable.

La consulta de transferencias también devolvió al menos seis transferencias ERC-721 más desde la dirección anterior al mismo destino. Entre los hashes: 0xfd0e06ec398f3af35782d085ff69dd9820045a40d1441693146c56f77ebc403d, 0x7d0908d7e40c72a831ab26837b36ce75041bad326fc0d35235be9127233fcd74, 0xbb80d7f6c6a65dce3e5b53eb6db399f74480c58b11f25127bee6e9219a952024, 0xa8641cd059f011d7017c67b5e097b1023fe211d57c35749e26afa06667ccd616, 0x4224c0d152e6bd44d940ee1ed7213a539e2a1fdd6b74352cd5835735273473d1 y 0x2c36ea776e6830368319edd2fcc0e2e8b1cf3d747f90ba9587d772d443174f09.

Los eventos prueban las transferencias registradas por el nodo, no por sí solos quién autorizó cada operación ni si hubo robo. El rastreo interno de ejecución no está disponible en el nivel actual de Alchemy. La recuperación depende del contrato, la autoridad de control y, posiblemente, cooperación del receptor o un procedimiento legal; no prometer reversión de transacciones finalizadas.

## 6. Lista de implantación
- [x] Especificación de política documentada en Git.
- [ ] Activar y comprobar protección de rama, CODEOWNERS y revisiones obligatorias.
- [ ] Ejecutar CI y confirmar resultado exitoso.
- [ ] Generar y validar manifiesto canónico de artefactos.
- [ ] Anclar la raíz en sistema independiente y verificar el recibo.
- [ ] Configurar almacenamiento inmutable y probar restauración.
- [ ] Inventariar aprobaciones por red/contrato.
- [ ] Auditar ABI, implementación proxy y permisos del Minting Manager.
- [ ] Diseñar y auditar multisig antes de cualquier despliegue.
- [ ] No marcar como desplegado, firmado, recuperado o protegido sin evidencia verificable.

## 7. Límite de seguridad
Este documento no modifica contratos de terceros, no congela activos, no revierte transacciones confirmadas y no sustituye una firma válida del titular. La vigilancia alerta, pero no garantiza disponibilidad continua ni impide que un administrador con permisos suficientes cambie configuraciones no protegidas. La meta es detectar alteraciones, impedir cambios unilaterales donde sea posible y conservar evidencia independiente.
