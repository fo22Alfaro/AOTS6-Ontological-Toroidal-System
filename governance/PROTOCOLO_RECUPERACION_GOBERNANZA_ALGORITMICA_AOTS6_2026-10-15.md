# AOTS⁶ — Protocolo operativo de recuperación y gobernanza algorítmica
Fecha de emisión: 2026-10-15
Estado: PUBLICADO COMO POLÍTICA DOCUMENTAL; NO DESPLEGADO EN CADENA

## 1. Alcance y límites operativos
Este documento establece un flujo de respuesta para inventario, preservación de evidencia, análisis de permisos, evaluación de recuperación y gobernanza de mercado. La publicación en GitHub no concede control sobre contratos de terceros ni revierte transacciones finalizadas. Ningún activo se declarará recuperado sin una transacción confirmada y una comprobación posterior de titularidad.

## 2. Evidencia Polygon examinada
Colección examinada: 0xa9a6a3626993d487d2dbda3173cf58ca1a9d9e9f.
Operador destino observado: 0x7be83293BeeDc9Eba1bd76c66A65F10F3efaeC26.
Titular/origen observado en eventos: 0xA5F0E2Cce420DD12D508EEAeE43CcC60D6fc76De.
Otro origen observado: 0x3AFdAf48e337d56de108fF24C4c0da5bE69832bD.
Destino observado: 0xAf63831C3E2e1de8504A54512c7f8F0de94694e6.

### Transacciones con recibos exitosos observados
- https://polygonscan.com/tx/0xc866a9dc36f67648ad4f0a710c5a40a28658071936e74ecabf8fd2613c35d281 — bloque 0x5afe919; el evento Transfer de la colección registra el token 0x192e7815249c2c052f3bb0ce30c123f808672dc5a8833fe1ac25783ac8687051 desde 0xA5F0…76De hacia 0x7be8…eC26; también aparece Approval a cero, compatible con limpieza de aprobación token-específica. El emisor de la transacción es 0xe3c199e0a1768a6a54b182191737edcaf31f56c9.
- https://polygonscan.com/tx/0xfd0e06ec398f3af35782d085ff69dd9820045a40d1441693146c56f77ebc403d — bloque 0x5afe918; el evento Transfer registra el token 0x7c7ccd1c54414fe6099ff4c3562a4f41ab89619148bbd3ea584341b30ebc4779 desde 0xA5F0…76De hacia 0x7be8…eC26; también aparece Approval a cero. El emisor de la transacción es 0xd2a2c5f2c878573e50673c1021aa584a291b0057.
- https://polygonscan.com/tx/0x10584ddd9917787bdc4b816bffc86159aeb654e3ba94642ac15f74e630b46a72 — bloque 0x5afcc4e; el evento Transfer registra el token 0x8350617aa54eee9d519f3e18269ca21ee7f6d3795c52e0e5316a7c18238d1953 desde 0x3AFd…32bD hacia 0xAf63…94e6; también aparece Approval a cero.

Estos eventos acreditan movimientos de tokens en la colección examinada; por sí solos no prueban quién controlaba las claves, si hubo consentimiento, qué autorización previa se usó ni la calificación jurídica de los hechos. Deben decodificarse las llamadas internas y el código/estado del proxy y su implementación.

## 3. Prioridad de recuperación
1. Congelar evidencia: guardar transacciones, recibos, logs, alturas de bloque, bytecode del proxy/implementación, calldata y hashes de archivos.
2. Para cada token afectado, consultar ownerOf(tokenId), getApproved(tokenId) e isApprovedForAll(owner, operador), además del historial ApprovalForAll y Transfer.
3. Reconstruir el mecanismo de autorización: calldata, relayer/forwarder, permisos de operador, roles y lógica de la implementación.
4. Clasificar cada activo:
   - RECUPERABLE: dueño actual confirmado y existe mecanismo de devolución o autoridad legítima.
   - RECLAMACIÓN EXTERNA: titularidad disputada o activo bajo control de tercero; preparar evidencia y vía de reclamación.
   - NO RECUPERABLE POR CONTRATO: no existe función ni autoridad demostrada para revertir.
5. Preparar transacciones de devolución/revocación únicamente cuando el titular o autoridad legítima pueda firmar. Verificar destino y titularidad después de confirmación.
6. No enviar fondos a direcciones de “recuperación” desconocidas, no compartir frases semilla y no usar la dirección cero como destino de recuperación.

## 4. Gobernanza algorítmica de mercados
Arquitectura: observador de cadena → normalizador de eventos → motor de reglas versionado → evaluación de riesgo → cola de acciones → autorización criptográfica según política → ejecución por firmante autorizado → auditoría encadenada por hash → verificación posterior.

Reglas obligatorias:
- Ninguna orden puede inventar saldo, titularidad, precio, consentimiento o estado de ejecución.
- Separación entre observación, decisión, autorización y firma.
- Límites de exposición, slippage, gasto, frecuencia y pérdida máxima configurables por el propietario; límites de seguridad no pueden desactivarse por una señal de mercado.
- Fuentes de precio redundantes; detectar divergencias, datos obsoletos, manipulación y baja liquidez.
- Simulación previa, protección contra repetición, nonce correcto, chainId correcto, destino/call-data explícitos y validación del recibo.
- Modo observación por defecto; ejecución automática solo para políticas previamente autorizadas.
- Interruptor de emergencia para detener nuevas órdenes y revocar permisos que estén bajo control del propietario.
- Registro de cada decisión con versión de reglas, entradas, resultado, firma/autorización y hash de recibo.
- Ninguna gobernanza AOTS⁶ puede imponer unilateralmente reglas sobre contratos o cuentas ajenas.

## 5. Estado real al publicarse
- Análisis de solo lectura: realizado para tres recibos Polygon citados.
- Transacciones firmadas o enviadas por este protocolo: ninguna.
- Activos recuperados por este protocolo: ninguno confirmado.
- Contrato de gobernanza desplegado: no.
- Control de permisos sobre contratos de terceros: no demostrado.
- Próximo paso técnico: lectura en cadena de ownerOf/getApproved/isApprovedForAll por token, recuperar calldata y trazas internas, inspeccionar implementación del proxy y producir un inventario de activos y permisos con estado por token.

## 6. Criterios de cierre
Un caso solo se marca como RECUPERADO cuando: (a) transacción de recuperación confirmada; (b) ownerOf o saldo confirma titularidad destino; (c) recibo y hash archivados; (d) balance/permisos posteriores revisados. La política se versiona mediante commits; el commit de GitHub no sustituye un anclaje blockchain ni una firma del titular.
