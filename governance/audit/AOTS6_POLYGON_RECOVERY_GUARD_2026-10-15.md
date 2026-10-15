# AOTS⁶ — Informe operativo de seguimiento Polygon
Fecha de auditoría: 2026-10-15
Modo: consulta de solo lectura; sin firma ni envío de transacciones.

## Alcance y límites
Consulta hecha a Polygon PoS mediante Alchemy, aplicación AOTS⁶. Las trazas de ejecución `trace_transaction` no están disponibles en el nivel Free del proveedor. Por ello este informe se basa en recibos, eventos y consultas de estado RPC; no reconstruye todas las llamadas internas ni determina por sí solo quién autorizó una firma.

## Evidencia verificada

### 1. Transferencia del token 0x192e…7051
- Tx: https://polygonscan.com/tx/0xc866a9dc36f67648ad4f0a710c5a40a28658071936e74ecabf8fd2613c35d281
- Estado del recibo: éxito (`status=0x1`); bloque `0x5afe919`.
- Emisor de la transacción: `0xe3c199e0a1768a6a54b182191737edcaf31f56c9`.
- Evento ERC-721 del contrato `0xa9a6a3626993d487d2dbda3173cf58ca1a9d9e9f`: transferencia de `0xA5F0E2Cce420DD12D508EEAeE43CcC60D6fc76De` a `0x7be83293BeeDc9Eba1bd76c66A65F10F3efaeC26`.
- También aparece un evento Approval del token hacia dirección cero, consistente con limpiar la aprobación individual al transferir; no identifica la autorización previa ni demuestra consentimiento del titular.
- Consulta posterior de `ownerOf(tokenId)` devolvió una palabra de 32 bytes con dirección cero. Es una respuesta RPC observada; dado que el contrato/proxy puede tener semántica no estándar, no se clasifica por sí sola como quema ni como recuperación.

### 2. Transferencia del token 0x7c7c…4779
- Tx: https://polygonscan.com/tx/0xfd0e06ec398f3af35782d085ff69dd9820045a40d1441693146c56f77ebc403d
- Estado: éxito (`status=0x1`); bloque `0x5afe918`.
- Emisor de la transacción: `0xd2a2c5f2c878573e50673c1021aa584a291b0057`; destino de la transacción de nivel superior es la misma dirección.
- El recibo registra transferencia del contrato de colección desde `0xA5F0E2Cce420DD12D508EEAeE43CcC60D6fc76De` al Minting Manager `0x7be83293BeeDc9Eba1bd76c66A65F10F3efaeC26`.
- También se registra Approval hacia cero para ese token.
- Consulta posterior de `ownerOf(tokenId)` devolvió dirección cero en el resultado RPC. No basta para concluir que el activo esté quemado o sea recuperable.

### 3. Transferencia del token 0x8350…1953
- Tx: https://polygonscan.com/tx/0x10584ddd9917787bdc4b816bffc86159aeb654e3ba94642ac15f74e630b46a72
- Estado: éxito (`status=0x1`); bloque `0x5afcc4e`.
- Emisor de la transacción: `0x3AFdAf48e337d56de108fF24C4c0da5bE69832bD`.
- El recibo registra transferencia de ese emisor a `0xAf63831C3E2e1de8504A54512c7f8F0de94694e6` y limpieza de la aprobación individual.

### 4. Actividad posterior observada
La consulta de transferencias desde `0xA5F0E2Cce420DD12D508EEAeE43CcC60D6fc76De` encontró, entre otros resultados devueltos:
- `0x2c36ea776e6830368319edd2fcc0e2e8b1cf3d747f90ba9587d772d443174f09`, bloque `0x5b02545`, 2026-10-13 00:10:26 UTC: ERC-721 a `0x7be83293BeeDc9Eba1bd76c66A65F10F3efaeC26`.
- `0x4224c0d152e6bd44d940ee1ed7213a539e2a1fdd6b74352cd5835735273473d1`, bloque `0x5b01d4c`, 2026-10-12 23:19:24 UTC: ERC-721 a la misma dirección.
- `0xa8641cd059f011d7017c67b5e097b1023fe211d57c35749e26afa06667ccd616`, bloque `0x5afede6`, 2026-10-12 18:16:03 UTC: ERC-721 a la misma dirección.
- `0xc866a9dc36f67648ad4f0a710c5a40a28658071936e74ecabf8fd2613c35d281`, bloque `0x5afe919`, 2026-10-12 17:45:20 UTC.
- `0xfd0e06ec398f3af35782d085ff69dd9820045a40d1441693146c56f77ebc403d`, bloque `0x5afe918`, 2026-10-12 17:45:18 UTC.
La lista es una página limitada de resultados, no un inventario exhaustivo.

## Lectura técnica
- Los recibos confirman ejecuciones exitosas y eventos de transferencia; no confirman por sí mismos legitimidad, consentimiento ni fraude.
- Las trazas internas no pudieron consultarse por restricción de nivel del proveedor.
- La dirección de colección `0xa9a6a3626993d487d2dbda3173cf58ca1a9d9e9f` se ha identificado en los resultados del explorador como colección UD/ERC-721; debe verificarse el vínculo contractual exacto con el activo AOTS⁶ antes de tratarla como contrato propio del usuario.
- Ninguna transacción fue firmada, transmitida, revocada ni revertida durante esta auditoría.
- No se identifica aún una ruta de recuperación ejecutable demostrada. Para avanzar, se necesita establecer titularidad y control legítimo de la cuenta origen, decodificar las llamadas del forwarder/manager y revisar las firmas/autorizaciones de las operaciones.

## Siguiente operación de guardia
1. Capturar eventos nuevos `Transfer`, `Approval` y `ApprovalForAll` en la colección y direcciones observadas.
2. Resolver propietario actual por token y seguir todos los movimientos posteriores hasta el bloque más reciente.
3. Verificar operadores ERC-721 y aprobaciones ERC-20 cuando proceda.
4. Marcar recuperable solo un token que siga bajo control de una cuenta autorizada o para el que exista una vía contractual/legal demostrada.
5. Mantener la recopilación en solo lectura; ninguna firma automática ni envío de fondos.
