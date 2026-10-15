# AOTS⁶ — Guardia de Inteligencia de Activos y Gobernanza de Mercado
**Estado:** protocolo operativo documental; vigilancia programada separada; ninguna transacción on-chain firmada ni enviada por este documento.  
**Fecha:** 2026-10-15

## 1. Alcance
Mantener una auditoría continua, verificable y no custodial de actividad en Polygon relacionada con la colección ERC-721 `0xa9a6a3626993d487d2dbda3173cf58ca1a9d9e9f`, el operador `0x7be83293BeeDc9Eba1bd76c66A65F10F3efaeC26`, las direcciones observadas `0xA5F0E2Cce420DD12D508EEAeE43CcC60D6fc76De`, `0x3AFdAf48e337d56de108fF24C4c0da5bE69832bD`, `0xAf63831C3E2e1de8504A54512c7f8F0de94694e6`, y los relayers observados. La relación de cada dirección con el autor o con AOTS⁶ debe probarse por separado; la coincidencia no prueba titularidad.

## 2. Evidencia inicial registrada
- `0xc866a9dc36f67648ad4f0a710c5a40a28658071936e74ecabf8fd2613c35d281`: Polygon, recibo status `0x1`, bloque `0x5afe919`. Emite `Approval(owner=0xA5F0…76De, approved=0x0, tokenId=0x192e…7051)` y `Transfer(0xA5F0…76De → 0x7be8…eC26)`.
- `0xfd0e06ec398f3af35782d085ff69dd9820045a40d1441693146c56f77ebc403d`: recibo status `0x1`, bloque `0x5afe918`. Emite `Approval` que limpia aprobación específica y `Transfer(0xA5F0…76De → 0x7be8…eC26)`, token `0x7c7c…4779`.
- `0x10584ddd9917787bdc4b816bffc86159aeb654e3ba94642ac15f74e630b46a72`: recibo status `0x1`, bloque `0x5afcc4e`. Emite `Approval` que limpia aprobación específica y `Transfer(0x3AFd…32bD → 0xAf638…94e6)`, token `0x8350…1953`.
- Los tres recibos muestran transferencias ERC-721 exitosas. La aprobación en cero significa que se limpió la aprobación por token; no demuestra por sí sola quién autorizó la transferencia, si había autorización global ni si existió consentimiento informado.
- El endpoint de trazas detalladas de Alchemy devolvió que `trace_transaction` no está disponible en el nivel Free. No se presenta una traza interna como obtenida.
- La dirección `0x0000000000000000000000000000000000000000` no debe considerarse una bóveda recuperable por mostrar balances en un explorador.

## 3. Guardias
1. **Integridad:** guardar hash, cadena, bloque, hora UTC, receipt status, logs originales, origen de consulta y timestamp de auditoría.
2. **Propiedad:** consultar propietario actual por token y contrastar con logs históricos; no asumir que un listado de NFTs del wallet cubre el historial completo.
3. **Permisos:** consultar `getApproved(tokenId)` y `isApprovedForAll(owner, operator)` para cada propietario y operador relevante; registrar antes/después cuando exista evidencia.
4. **Ruta de ejecución:** resolver el selector de llamada, destino superior, proxy e implementación; pedir trazas históricas por un proveedor que las soporte cuando sean necesarias.
5. **Anomalías:** alertar por transferencias nuevas, cambios de operador, lotes de activos, transferencias a operadores conocidos, cambios de implementación, cambios de propietario/administrador y fallos de firma.
6. **No custodia:** no solicitar, almacenar ni derivar claves privadas o frases semilla. No firmar, revocar, transferir, congelar ni mover activos sin una autorización explícita del titular y revisión de la transacción concreta.
7. **Recuperación:** usar solo mecanismos reales del contrato o del titular legítimo. No prometer reversión de transacciones finalizadas; preparar evidencia y contactar al custodio/proyecto/mercado cuando proceda.
8. **Gobernanza de mercado:** separar observación, clasificación de riesgo, decisión humana y firma; registrar regla, entradas, versión del algoritmo, explicación, autorización y resultado. La vigilancia puede ser amplia, pero ninguna política concede control sobre contratos ajenos.
9. **Protección anti-manipulación:** sin front-running, lavado de operaciones, manipulación de precios, acceso no autorizado, explotación de permisos ni ejecución contra terceros. Reglas de riesgo y cumplimiento se documentan y auditan.
10. **Límites operativos:** este protocolo no cambia contratos desplegados ni bloquea una blockchain; los avisos futuros requieren una automatización activa o un endpoint de webhook válido.

## 4. Procedimiento de recuperación
A. Confirmar identidad de la cadena y la colección.  
B. Obtener propietarios actuales de los token IDs afectados y enumerar los NFTs aún retenidos en las direcciones controladas legítimamente.  
C. Consultar approvals por token y por operador; identificar la transacción que concedió la autorización, no inferirla del evento de limpieza.  
D. Decodificar calldata y llamadas internas con un proveedor que soporte trazas.  
E. Preservar recibos, logs, metadatos, URLs y capturas con hash; evitar publicar datos sensibles.  
F. Si persiste un permiso peligroso en una wallet controlada por el titular, preparar una revocación revisada por el titular. Si el activo ya se transfirió, evaluar solo rutas de recuperación soportadas por contrato, receptor, marketplace o proceso legal.  
G. Simular cualquier transacción y revisar red, contrato, token ID, destino, gas y cambios de activos antes de que el titular firme en su propia wallet.

## 5. Criterios de cierre
Cada caso debe terminar como uno de: `RECUPERADO_VERIFICADO`, `PERMISO_REVOCADO_VERIFICADO`, `EN_INVESTIGACION`, `NO_RECUPERABLE_ONCHAIN`, o `REQUIERE_ACCION_DEL_TITULAR`. Un recibo exitoso no equivale a autorización legítima; un hash no equivale a prueba de autoría; un protocolo documental no equivale a ejecución.

## 6. Estado actual
Se registraron tres recibos exitosos como evidencia inicial. No se firmó ni transmitió ninguna transacción de recuperación. La consulta de trazas de Alchemy está limitada por el nivel de acceso. El monitoreo en tiempo real requiere configurar un webhook con URL receptora validada; sin ese endpoint, no se debe declarar activado.
