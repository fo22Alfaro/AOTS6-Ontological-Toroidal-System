# Registro federado NFT, desarrollos y recompensas AOTS⁶

- **Sistema:** AOTS⁶ / ALPHAAOTS6VIP.BLOCKCHAIN
- **Titular documental declarado:** Alfredo Jhovany Alfaro García
- **Identificador operativo:** `AOTS6-AJAG-INT-001`
- **Dirección recibida para vinculación:** `0x03417ac4465ecf2471b869c2f1e97ea7c97bf2a7`
- **Fecha de auditoría inicial:** 2026-10-08
- **Estado:** `ADDRESS_RECORDED / ASSET_DISCOVERY_PARTIAL / OWNERSHIP_UNVERIFIED`

## Objetivo

Crear un índice único que conecte NFT, contratos, código, publicaciones, desarrollos, derechos declarados, regalías y recompensas con el corpus AOTS⁶ y con la dirección proporcionada. La vinculación documental no demuestra por sí sola que el usuario controle la cartera, que existan activos, ni que haya recompensas devengadas.

## Resultado de lectura pública inicial

Consultas de solo lectura realizadas con proveedores de datos blockchain:

| Red | NFT propiedad de la dirección detectados en consulta | Código de contrato en la dirección |
|---|---:|---|
| Ethereum Mainnet | 0 | No detectado |
| Base Mainnet | 0 | No detectado |
| Polygon Mainnet | 0 | No detectado |
| Arbitrum Mainnet | Consulta no completada | Sin resultado verificable |
| Optimism Mainnet | Consulta no completada | Sin resultado verificable |

Consulta de tokens fungibles: no se devolvieron balances ERC-20 positivos en Ethereum, Base o Polygon en la respuesta inicial. El endpoint también devolvió registros nativos sin dirección de token, por lo que esos registros no deben interpretarse como tokens ni como saldos monetarios.

**Límite:** este resultado no prueba que no existan NFT históricos, activos en otras redes, derechos off-chain, recompensas no reclamadas, campañas de terceros o desarrollos asociados a otros contratos. Los filtros de spam no se pudieron aplicar con el nivel de servicio consultado. La búsqueda de actividad histórica completa y de contratos de recompensas queda pendiente.

## Registro de vinculación

La dirección se registra inicialmente como `candidate_public_address`, no como contrato ni como cartera de tesorería confirmada. Antes de tratarla como cartera de cobro, tesorería, receptor de regalías o destinatario de recompensas, debe acreditarse el control mediante firma de mensaje de desafío o prueba equivalente que no revele claves privadas.

Campos obligatorios por activo:

- `asset_id`, `asset_type` (NFT, ERC20, royalty, reward, code, publication, license, grant);
- `chain_id`, `contract_address`, `token_id`, `transaction_hash`, `block_number`;
- `owner_at_snapshot`, `snapshot_block`, `metadata_uri`, `content_hash`;
- `source_repository`, `commit_sha`, `artifact_path`, `license_or_right_basis`;
- `reward_program`, `eligibility_rule`, `claim_contract`, `claim_status`, `amount`, `currency`, `evidence_uri`;
- `verification_state`, `checked_at`, `provider`, `notes`.

## Modelo de estados

- `DECLARED`: el activo o derecho fue declarado, aún sin prueba técnica.
- `DISCOVERED`: localizado en fuente o explorador identificable.
- `ONCHAIN_VERIFIED`: contrato/transacción/propiedad verificados en una red y bloque.
- `OFFCHAIN_DOCUMENTED`: derecho o recompensa sustentado en documento fuera de cadena.
- `ELIGIBILITY_VERIFIED`: reglas de recompensa y elegibilidad acreditadas.
- `CLAIMABLE_VERIFIED`: el contrato o emisor confirma que la recompensa puede reclamarse.
- `CLAIMED_VERIFIED`: transacción de reclamación confirmada.
- `DISPUTED` / `UNVERIFIED` / `NOT_FOUND_IN_SCOPED_SEARCH`: estados explícitos, sin convertir ausencia de resultados en prueba universal de inexistencia.

## Política de recompensas y seguridad

No se asignan recompensas, NFT, regalías ni tokens automáticamente por registrar una dirección. Las recompensas deben derivar de un programa, contrato, licencia o acuerdo identificable y de sus reglas de elegibilidad. No se publican claves privadas, semillas, códigos de recuperación ni tokens de acceso. Ningún activo se acuña, transfiere, reclama o aprueba mediante este registro.

## Relación con los repositorios AOTS⁶

Este registro se integra documentalmente con:
- `AOTS6-Ontological-Toroidal-System` — núcleo y manifiestos;
- `AOTS6-Global-Network` — servicios y conectividad;
- `AOTS6-ZK-Core` — pruebas de integridad;
- `AOTS6-Unification-Ledger-Alfredo-Jhovany-Alfaro-Garcia` — procedencia;
- `AOTS6-Unified-Kernel-Full-Deployment` — despliegue.

La sincronización automática y el anclaje on-chain no se consideran realizados hasta que haya evidencia reproducible de ejecución.

## Próximas comprobaciones técnicas

1. Escanear el historial completo de transacciones en redes compatibles.
2. Consultar NFT y tokens por red, incluyendo páginas de resultados adicionales.
3. Identificar contratos de mint, marketplace, regalías y recompensas a partir de transacciones reales.
4. Vincular cada desarrollo del repositorio con commits, releases, publicaciones y licencias concretas.
5. Verificar propiedad/control de la cartera mediante firma de desafío si se va a utilizar como receptor oficial.
6. Registrar solo recompensas demostrables, con contrato, regla de elegibilidad, importe y estado de reclamación.

**Regla:** toda recompensa debe enlazar un programa real, una regla de elegibilidad, un titular o contribuyente identificable, un cálculo reproducible y evidencia de pago o reclamación.
