# AOTS⁶ — Protocolo de Integridad, Custodia y Gobernanza de Registros
**Versión:** 1.0  
**Fecha:** 2026-10-15  
**Autoría del sistema:** AOTS⁶  
**Estado:** Especificación operativa publicada; despliegue de contratos y controles externos pendiente de ejecución y verificación.

## 1. Objetivo de seguridad
Reducir al mínimo la capacidad de un actor individual para modificar, ocultar, eliminar o transferir activos/registros sin autorización detectable. No se declara invulnerabilidad absoluta: una garantía fuerte exige implementación, separación de llaves, anclajes independientes y pruebas adversariales.

## 2. Invariantes obligatorios
1. **Append-only:** los eventos originales no se editan ni sobrescriben; una corrección se registra como evento nuevo enlazado al anterior.
2. **Hash chain:** cada evento incluye hash del evento previo, hash del contenido canónico, identificador, hora UTC, fuente, actor, alcance y resultado.
3. **Firmas verificables:** firmar cada lote de eventos con claves de auditoría independientes de las claves de custodia de activos. Guardar clave pública, algoritmo, versión y resultado de verificación; nunca registrar secretos.
4. **Anclaje externo:** publicar periódicamente la raíz de Merkle/hash en al menos dos dominios de confianza independientes (p. ej. cadena pública y repositorio WORM/almacenamiento inmutable). Registrar transacción, bloque, red, hora y comprobación posterior.
5. **Múltiples custodios:** movimientos de activos críticos requieren multisig o política de umbral; ninguna clave individual puede cambiar política, retirar fondos y borrar evidencia a la vez.
6. **Separación de funciones:** observador, motor de política, firmantes y auditor son roles separados; el observador no puede firmar ni transferir.
7. **Control de cambios:** actualizaciones de contrato/configuración requieren propuesta, revisión independiente, pruebas y ventana de demora cuando el diseño lo permita.
8. **Copias independientes:** copias cifradas y versionadas, con retención, prueba periódica de restauración y credenciales separadas.
9. **Alertas:** eventos inesperados, cambio de administrador/implementación, aprobación amplia, transferencia, fallo de anclaje, ruptura de hash o falta de heartbeat generan alertas fuera del sistema auditado.
10. **Reconciliación:** comparar inventario local con estado de cadena y exploradores/RPC independientes; registrar diferencias sin ocultarlas.

## 3. Registro canónico
Campos mínimos por evento:
- event_id, schema_version, event_type, timestamp_utc
- chain_id, block_number, tx_hash, tx_index, log_index (cuando aplique)
- contract_address, token_standard, token_id/asset_id
- from, to, actor, initiator, relayer (si se conoce)
- authorization_policy_id, approval_state_before/after
- source_rpc, source_independent, raw_evidence_digest
- previous_event_hash, canonical_event_hash, signer_key_id, signature, verification_status
- status: OBSERVED / CORROBORATED / DISPUTED / RECOVERY_CANDIDATE / RECOVERED
No confundir el emisor de una transacción con el titular económico ni declarar fraude únicamente por un evento.

## 4. Procedimiento ante posible extracción no autorizada
1. Capturar recibos, logs, calldata, código/implementación proxy, historial de propietarios y aprobaciones; conservar copia original y hash.
2. Leer estado actual mediante funciones de solo lectura: ownerOf, getApproved, isApprovedForAll, roles/admin, implementation slot y pausas disponibles.
3. Corroborar por dos fuentes RPC/exploradores independientes. La traza interna puede requerir un proveedor que habilite trazas.
4. Clasificar cada activo: en custodia propia, transferido a custodio/operador, transferido a tercero, quemado, o estado no resuelto.
5. Revocar solo aprobaciones controladas por una cuenta autorizada y tras verificar consecuencias. Revocar aprobación no revierte transferencias ya confirmadas.
6. Recuperar únicamente por una ruta válida: función de recuperación documentada, control administrativo legítimo, devolución voluntaria o proceso legal. Nunca prometer reversión de una transacción finalizada sin tal mecanismo.
7. Antes de cualquier firma: simular llamada, revisar destino/calldata/gas/red, validar política y exigir umbral de firmantes. No exponer claves privadas, semillas ni firmas reutilizables.
8. Después: verificar recibo confirmado, estado de propiedad y nuevo anclaje del registro.

## 5. Gobernanza algorítmica de mercados
- Modos separados: OBSERVE → CLASSIFY → PROPOSE → SIMULATE → AUTHORIZE → EXECUTE → VERIFY.
- El modo automático por defecto es solo lectura. La ejecución exige reglas versionadas, límites de exposición, controles de slippage, límites de pérdida, prevención de replay, lista de contratos permitidos y aprobación por umbral.
- Ningún modelo de IA tiene autoridad de custodia por sí solo. Las reglas críticas se ejecutan determinísticamente y son auditables; los modelos generan señales explicables, no autoridad irrestricta.
- Prohibidos cambios silenciosos de políticas, borrado de auditoría y firma automática de transferencias a destinos no verificados.
- Registrar decisiones, datos usados, versión de regla/modelo, simulación, aprobaciones, transacción y verificación posterior.

## 6. Estado actual y límites
- Hay un registro económico local con encadenamiento SHA-256 publicado en el repositorio; por sí solo no es consenso distribuido ni almacenamiento inmutable.
- Hay documentación y workflows de auditoría publicados, pero su ejecución CI y sus anclajes deben verificarse por resultados concretos.
- El objeto AOTS6_NET_AUTH.sig fue observado vacío en la auditoría previa; no debe considerarse firma válida.
- Las huellas NFT topológicas declaradas todavía no equivalen a fingerprints calculados ni a anclajes on-chain.
- La traza interna de Polygon no está disponible en el plan RPC actual consultado; las trazas deben obtenerse mediante fuente habilitada o reconstruirse parcialmente con calldata y logs.
- Este documento no despliega contratos, no firma ni envía transacciones, no revierte transferencias ni bloquea terceros. Cada acción de cadena requiere autorización válida y un firmante disponible.

## 7. Criterios de aceptación
- Pruebas de modificación, borrado, reordenamiento, repetición y omisión detectadas.
- Verificación de firmas y hashes reproducible desde una máquina limpia.
- Raíz de auditoría recuperable desde dos custodios independientes.
- Prueba de restauración completada y documentada.
- Simulaciones negativas para transferencias no autorizadas, cambio de administrador y actualización de proxy.
- Alertas de prueba recibidas por canal externo.
- Inventario reconciliado y diferencias explícitamente clasificadas.
