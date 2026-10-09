# AOTS⁶ — Red económica y criptográfica interna del Núcleo Toroidal

**Autoría declarada:** Alfredo Jhovany Alfaro García  
**Sistema:** AOTS⁶ — Alfanumerical Ontological Toroidal System  
**Identificador operativo:** AOTS6-AJAG-INT-001  
**Estado de este despliegue:** código y especificación publicados; ejecución local, custodia de activos, pagos y anclaje on-chain requieren configuración y evidencia propia.

## Vinculación unificada

Este componente enlaza el registro económico, la integridad criptográfica, la procedencia de activos, la gobernanza y la capa de anclaje externo dentro de una sola cadena de trazabilidad:

`IDENTIDAD → ACTIVO → EVENTO ECONÓMICO → FUENTE → REGLA → AUTORIZACIÓN → REGISTRO HASH → AUDITORÍA → ANCLAJE EXTERNO → EVIDENCIA DE CUMPLIMIENTO`

Se integra con:
- [Consolidación de bienes criptográficos, procedencia y gobernanza AOTS⁶](./CONSOLIDACION_BIENES_CRIPTOGRAFICOS_AWS_AOTS6.md)
- [Paquete NFT AOTS⁶](../assets/nft/README.md)
- [Contrato ERC-721 preparado](../assets/nft/contracts/AOTS6AssetRegistry.sol)
- [Informe de estado y recuperación pública NFT](../assets/nft/RECUPERACION_PUBLICA_NFT.md)

## Topología funcional del Núcleo Toroidal

1. **Centro de identidad y políticas:** identifica autor, operador, activo, alcance y permisos declarados.
2. **Registro económico:** registra eventos como alta, asignación, valoración declarada, recompensa propuesta, transferencia propuesta o conciliación. Los eventos son registros de auditoría, no órdenes de pago.
3. **Capa criptográfica:** SHA-256 encadena los registros mediante el hash del evento anterior; HMAC-SHA-256 opcional permite verificar integridad con una clave local proporcionada por variable de entorno.
4. **Motor de reglas:** valida campos requeridos, secuencia, hashes y transiciones registradas. No presume que una declaración económica sea verdadera solo por estar firmada o hasheada.
5. **Auditoría y procedencia:** conserva actor declarado, fuente, hora UTC, tipo de evento, unidad y evidencia referenciada.
6. **Adaptadores externos:** conectores futuros para RPC, contratos, IPFS o servicios de custodia deben registrar red, identificador de transacción, bloque/slot y recibo verificable. No se simulan confirmaciones.
7. **Gobernanza de recompensas:** ninguna recompensa se considera aprobada, financiada o pagada sin política autorizada, saldo/fuente de fondos y recibo verificable.

## Modelo de registro

Cada evento contiene `sequence`, `timestamp_utc`, `actor`, `event_type`, `asset_id`, `amount`, `unit`, `source_ref`, `evidence_ref`, `previous_hash` y `event_hash`. El campo `amount` es una cantidad declarada y `unit` su unidad; no equivale por sí mismo a saldo bancario, token emitido ni valor de mercado.

El archivo JSONL es un registro local encadenado. Un hash encadenado ayuda a detectar modificaciones, pero no es consenso distribuido, no impide que un operador reescriba toda la cadena y no sustituye una firma de clave pública, una auditoría independiente ni un anclaje público.

## Ejecución local

Requiere Python 3.10+ y biblioteca estándar; no requiere instalar dependencias.

```bash
python runtime/aots6_toroidal_economic_crypto.py init --ledger data/aots6_economic_ledger.jsonl
python runtime/aots6_toroidal_economic_crypto.py append --ledger data/aots6_economic_ledger.jsonl --actor "AOTS6-AJAG-INT-001" --type ASSET_REGISTERED --asset-id "AOTS6-CORE-001" --amount 1 --unit "record" --source-ref "github:AOTS6" --evidence-ref "deployment:local"
python runtime/aots6_toroidal_economic_crypto.py verify --ledger data/aots6_economic_ledger.jsonl
```

Para HMAC opcional, define `AOTS6_LEDGER_HMAC_KEY` en el entorno local antes de registrar y verificar. No guardes esa clave en GitHub ni la envíes al chat. Si se cambia la configuración de HMAC, los registros previos sin HMAC no se convierten retroactivamente en firmados.

## Estado de despliegue

- **Publicado en GitHub:** fuente y arquitectura documental.
- **Ejecución en dispositivo o servidor:** no ejecutada por esta publicación; el operador debe iniciar el proceso en su entorno.
- **Base económica real / custodia:** no conectada ni afirmada.
- **Contratos o NFT:** fuente preparada; la acuñación requiere despliegue y transacciones firmadas.
- **Anclaje público:** pendiente de una transacción real y recibo comprobable.
- **Recompensas:** no se declaran aprobadas, financiadas ni pagadas.

Este documento es la referencia de vinculación del componente económico-criptográfico interno; las capas locales y externas se mantienen conectadas por la misma cadena de procedencia, sin confundir publicación de código con ejecución o liquidación real.
