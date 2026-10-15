# AOTS⁶ — Política de integridad, custodia y gobernanza criptográfica
**Estado:** especificación operativa propuesta para implementación y auditoría. Este documento no afirma que los controles estén ya desplegados en cadena.

## Objetivo
Reducir al mínimo la capacidad de cualquier tercero o administrador individual para alterar, borrar, falsificar o mover activos/registros sin autorización, y hacer detectable toda discrepancia.

## Invariantes de seguridad
1. **No una sola clave:** ninguna operación crítica se autoriza con una única clave de operador. Usar multisig/M-of-N con firmantes independientes y hardware wallets; separación entre autoría, revisión y ejecución.
2. **Sin claves en repositorios o registros:** nunca guardar seed phrases, claves privadas, API secrets ni tokens de firma en Git, JSONL, CI logs, issues o artefactos. Rotar credenciales que hayan podido exponerse.
3. **Autorización explícita por operación:** cadena/red, contrato, función, destinatario, activo, cantidad, límites de gas, nonce y caducidad quedan ligados al mensaje firmado. Rechazar mensajes incompletos, expirados o con chainId/destino distinto.
4. **Pausa y límites en contratos propios:** donde sea técnicamente apropiado, usar pausa de emergencia, límites por operación/periodo, allowlists y timelock para cambios administrativos. La pausa no debe ser una puerta de control unilateral: el rol de emergencia y la reactivación requieren política M-of-N.
5. **No atribuir control inexistente:** no se puede imponer una pausa ni revertir una transferencia en un contrato ajeno sin una función y autoridad legítimas que lo permitan. No firmar ni enviar recuperaciones sin comprobar titularidad, autoridad y destino.
6. **Registro de solo anexado:** eventos JSONL encadenados con SHA-256, firma de checkpoints, secuencias monotónicas, reloj UTC y hash del artefacto. El hash encadenado por sí solo no impide que un administrador reescriba todo el archivo; por eso los checkpoints deben anclarse fuera del mismo dominio de administración.
7. **Anclaje independiente:** publicar periódicamente raíz/hash firmado en dos o más destinos bajo control separado (por ejemplo, almacenamiento WORM/Object Lock y repositorio/servicio independiente). Conservar recibos, fecha, clave pública verificadora y política de retención. Un commit Git o un hash local no equivale a anclaje inmutable.
8. **Copias y restauración:** copias cifradas, credenciales separadas, retención protegida contra borrado, y prueba periódica de restauración. Ninguna cuenta de producción puede borrar todas las copias.
9. **Monitoreo de cadena:** registrar hash, chainId, bloque, emisor, destino, input, receipt/status, logs, tokenId/activo, propietario previo y posterior, cambios de approvals y trazas disponibles. Diferenciar hechos on-chain, inferencias y atribución.
10. **Alertas:** notificar inmediatamente ante cambios de owner/admin/implementation, grants de roles, approvals, transferencias desde direcciones vigiladas, discrepancias de propietario, fallo de checkpoint o ausencia de heartbeat.
11. **Respuesta a incidentes:** preservar datos originales y recibos; congelar automatizaciones de firma afectadas; revocar sesiones/API keys expuestas; revisar approvals y roles; rotar claves comprometidas desde un entorno seguro; no divulgar secretos en el informe.
12. **Mercados:** gobernanza basada en reglas públicas, límites de exposición, validación de precios y fuentes múltiples, detección de anomalías, circuit breakers y revisión independiente. Nunca permitir que una señal algorítmica aislada ejecute movimientos irreversibles de activos.

## Protocolo de cada transacción
OBSERVAR → SIMULAR → VALIDAR CADENA/CONTRATO/DESTINO → EVALUAR POLÍTICA → APROBACIÓN M-of-N → FIRMAR EN DISPOSITIVO SEGURO → ENVIAR → CONFIRMAR RECEIPT → VERIFICAR ESTADO FINAL → ANCLAR EVIDENCIA → AUDITAR.

Si falla una etapa, la transacción queda **DENEGADA/PENDIENTE**, no se envía.

## Estado real y límites de este artefacto
- Este documento es una política de diseño y auditoría; no cambia contratos desplegados ni permisos on-chain.
- No se afirma que las transferencias de terceros puedan congelarse o revertirse.
- La monitorización periódica depende de que la automatización tenga acceso al proveedor y complete cada ejecución; una programación no equivale a una alerta en tiempo real.
- Antes de afirmar despliegue: publicar implementación, pruebas positivas/negativas, verificación de firmas, revisión de permisos, prueba de restauración y hashes/recibos de anclaje independientes.
